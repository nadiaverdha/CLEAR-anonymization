# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-26T13:23:11.645559

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
| True Positives | 523 |
| False Positives | 130 |
| False Negatives | 1091 |
| Total Gold Entities | 1614 |
| Micro Precision | 80.1% |
| Micro Recall | 32.4% |
| Micro F1 | 46.1% |
| Macro F1 | 46.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `legal_person_judge_title_combined` | 17.7% | 87.4% | 9.9% | 182 | 159 | 23 |
| `legal_person_complainant_context` | 27.2% | 85.3% | 16.2% | 306 | 261 | 45 |
| `legal_person_honorific_context` | 11.6% | 63.2% | 6.4% | 163 | 103 | 60 |
| `legal_person_representative_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `legal_person_preposition_from` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `legal_person_judge_title_combined` 🏆

**F1:** 0.177 | **Precision:** 0.874 | **Recall:** 0.099  

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
| 0.874 | 0.099 | 0.177 | 182 | 159 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 159 | 23 | 1455 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Mag. Josef Nußbaumer` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Lehwaldt` | `Univ.-Prof. Günter Lehwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Hinterlandt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Mehmet Gessl` | `Dr. Mehmet Gessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donau-Elektro` (organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich` (address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Guntram Antepoth` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Waldemar Faltermeir` | `Dr. Waldemar Faltermeir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Kendziorra` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Clemens Mooß` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Burgschweiger` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernarda Egli` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Susette Volmari` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sulamith Hördegen` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrich Petrag` | `Mag. Ulrich Petrag` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Nodurft` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Mag. Marion Riezinger` (person)
- `Finanzamtes  Linz` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Monika Schmalzl` (person)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Volker Nissle` (person)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Basil Eberhards` | `Mag. Basil Eberhards` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Pawel Schuwirth` | `Hon.-Prof. Pawel Schuwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Griselda Hälmle` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Paolo Reppert` | `Dr. Paolo Reppert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendelin Pham` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Blatner` (person)
- `Hetzerstraße 11, 4712 Armau, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt  Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hugo Pietzak` | `Priv.-Doz. Hugo Pietzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Florens Weißer` (person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adam Rueßbült` | `Hon.-Prof. Adam Rueßbült` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timon Reinhertz` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-325/9824` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Richard Schwanken` | `Priv.-Doz. Richard Schwanken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexandra Hettrich` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Eizenhammer` | `Priv.-Doz. Eckard Eizenhammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ashley Tönisen` (person)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-543/4492` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aloisa Antoni` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Untermeier` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Dr. Christoph Ganahl` (person)
- `Finanzamtes` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Mag. Wladimir Beheim` | `Mag. Wladimir Beheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bruno Rüttgers` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Babette Bernett` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Julia Mundle` (person)
- `Leitersdorf 2, 9344 Psein, Österreich` (address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `23-019/8335` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Edwin Teiwes` | `Univ.-Prof. Edwin Teiwes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Francois Distefano` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Carla Winterkorn` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Leander Hättrich` | `Mag. Leander Hättrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edith Grotehenn` (person)
- `Karlhofstraße 20, 4212 Götschka, Österreich` (address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `FA Wien  4/5/10` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  Basil Vanak, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Basil Vanak` (person)
- `Oberhof 221, 8345 Trössing, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `BFG` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Andreas Kuschy  in der Beschwerdesache Angelika Oligschleger,  Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des Finanzamt Innsbruck  vom 29. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 49-970/7545  nach dem Einlangen des Vorlageantrages vom 10.6.2021  beschlossen:   Der Vorlageantrag wird gem. § 264 Abs 4 lit e Bundesabgabenordnung zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Andreas Kuschy` | `Univ.-Prof. Andreas Kuschy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Angelika Oligschleger` (person)
- `Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `49-970/7545` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  StR OSR Roxana Petkov, Bakk. phil., Am Ramberg 28, 3553 Schiltern, Österreich, über die Beschwerde vom 21. April 2016 gegen den Bescheid des  Finanzamtes Feldkirch vom 1. April 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 Steuernummer 48-815/6843  zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR OSR Roxana Petkov, Bakk. phil.` (person)
- `Am Ramberg 28, 3553 Schiltern, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `48-815/6843` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Wieland Starnberg` | `Priv.-Doz. Wieland Starnberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Walter Aiglsdorfer` | `Mag. Walter Aiglsdorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Leander Pfleumer, LLM` (person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `11-306/0925` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Franziskus Grineisen  in der Beschwerdesache MedR KommR Serena Dillschneider,  Rooseveltplatz 7, 4770 Bruck, Österreich, über die Beschwerde vom 28. Dezember 2020 gegen die Bescheide des  Finanzamt Klosterneuburg  vom 25. November 2020 betreffend Einkommensteuer 2017 und Wiederaufnahme  des Verfahrens bezüglich der Einkommensteuer 2017 und den Bescheid vom 02. August 2021  betreffend die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2018,  Steuernummer 95-890/2122, zu Recht erkannt:   I. Die Beschwerde gegen die Wiederaufnahmebescheide wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Franziskus Grineisen` | `Hon.-Prof. Franziskus Grineisen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR KommR Serena Dillschneider` (person)
- `Rooseveltplatz 7, 4770 Bruck, Österreich` (address)
- `Finanzamt Klosterneuburg` (organisation)
- `95-890/2122` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Björn Stover` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `57-952/0912` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. September 2020 des Beschwerdeführers Klarissa Fuhljahn, Adr Bf, Steuernummer  21-178/1143, vertreten durch den mit Zustellvollmacht ausgewiesenen Martin Friedl, 4650  Lambach, Marktplatz 2 gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr (nunmehr  Finanzamt Österreich) vom 17. August 2020 betreffend Haftung für Lohnsteuer 2012 – 2017  sowie Festsetzung von Dienstgeberbeiträgen und Festsetzung von Zuschlägen zu den  Dienstgeberbeiträgen für die Jahre 2011 – 2017:  I)

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klarissa Fuhljahn` (person)
- `21-178/1143` (tax_number)
- `Martin Friedl` (person)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Klaus Krupok` | `Mag. Klaus Krupok` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernst Eschenbrenner` (person)
- `Irenental 58, 4871 Tiefenbach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `80-953/9265` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Susanne Türner, Viehdorfer Straße 25, 9853 Burgwiese, Österreich, gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg  Tulln vom 25. November 2011 betreffend Körperschaftsteuer und Umsatzsteuer 2007,  Steuernummer 16-353/9813  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Susanne Türner` (person)
- `Viehdorfer Straße 25, 9853 Burgwiese, Österreich` (address)
- `Finanzamtes` (organisation)
- `16-353/9813` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Patrick Hübben  in der Beschwerdesache Alice Rüde,  Auhub 26, 9560 Kraß, Österreich, vertreten durch BDO Steiermark GmbH Wtp u Stb, Schubertstraße 62, 8010  Graz, über die Beschwerde vom 18. März 2019 gegen den Bescheid des FA Tirol Ost  vom  26. Februar 2019 betreffend Abweisung eines Zahlungserleichterungsansuchens zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Patrick Hübben` | `Hon.-Prof. Patrick Hübben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alice Rüde` (person)
- `Auhub 26, 9560 Kraß, Österreich` (address)
- `BDO Steiermark GmbH Wtp` (organisation)
- `FA Tirol Ost` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lewis Fröhner` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 7. Mai 2021 der Beschwerdeführerin Liu Maackens, LLM Bakk. techn., Alfons-Petzold-Hof 4, 2042 Grund, Österreich  vertreten durch die mit  Zustellvollmacht ausgewiesene WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG,  Blumauerstraße 35, 4020 Linz, gegen den Bescheid des Finanzamtes Österreich vom 8. April  2021 betreffend Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand gem. §  308 BAO betreffend Erklärung des Widerrufs des Regelbesteuerungsantrages gem. § 6 Abs 3  UStG 1994  zu Recht:    I)  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Liu Maackens, LLM Bakk. techn.` (person)
- `Alfons-Petzold-Hof 4, 2042 Grund, Österreich` (address)
- `WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Adriana Eiffler, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adriana Eiffler` (person)
- `Waldhofweg 36a, 8321 Entschendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-550/2209` (tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Hartmut Schalk, Parhamerplatz 8, 9112 Gletschach, Österreich, betreffend Beschwerde vom 31. Juli 2012 gegen die Bescheide des  FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 29. Juli 2011 betreffend  Einkommensteuer der Jahre 2006 bis 2010, Steuernummer 16-753/5618  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Zwilling` | `Mag. Josef Zwilling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hartmut Schalk` (person)
- `Parhamerplatz 8, 9112 Gletschach, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-753/5618` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Severin Iwanowsky  in der Beschwerdesache Richard Joistgen,  Breitenbachstraße 15, 4794 Glatzing, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 31. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 81-572/7905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Severin Iwanowsky` | `Dr. Severin Iwanowsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard Joistgen` (person)
- `Breitenbachstraße 15, 4794 Glatzing, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `81-572/7905` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/137043.1`) (sent_id: `deanon_BFG_20260814_TEST/137043.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Massimo Lewerenz  in der Angelegenheit der Parteien  - Natalie Veenema, PLZ1 Stadt1 (Beschwerdeführerin), vertreten durch „die Steuerberater GmbH“,  9020 Klagenfurt und  - Finanzamt Österreich als Amtspartei und als Gesamtrechtsnachfolger des Finanzamt Bruck Eisenstadt Oberwart  über die Beschwerde vom 21.3.2018 gegen den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 26.2.2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016

| Predicted | Gold |
|---|---|
| `Dr. Massimo Lewerenz` | `Dr. Massimo Lewerenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Veenema` (person)
- `Finanzamt Österreich` (organisation)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Edwin Lamken` (person)
- `Steindl 32, 4076 Lengau, Österreich` (address)
- `Caroline Toifl Rechtsanwalt GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Gammersbach&Pelstring Telekom GmbH` (organisation)
- `53-479/4428` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Adriaans` (person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich` (address)
- `Mag. Markus Wagner` (person)
- `Finanzamtes Österreich` (organisation)
- `81-584/4494` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Björn Augusto  in der Beschwerdesache Mona Reinhard,  Urschendorf 19, 4261 Kerschbaum, Österreich, vertreten durch IMMUNITAS Wirtschaftsprüfung GmbH, Schlickgasse 3 Tür 7,  1090 Wien, über die Beschwerde der beschwerdeführenden Partei vom 17.05.2022, beim  Bundesfinanzgericht eingelangt am 19.05.2022, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt für Großbetriebe betreffend Einkommen- und  Umsatzsteuer 2020 den Beschluss:   I. Das Säumnisbeschwerdeverfahren wird eingestellt.    II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr. Björn Augusto` | `Dr. Björn Augusto` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mona Reinhard` (person)
- `Urschendorf 19, 4261 Kerschbaum, Österreich` (address)
- `IMMUNITAS Wirtschaftsprüfung GmbH` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/137175.1`) (sent_id: `deanon_BFG_20260814_TEST/137175.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Ashley Wanagat, Dörfles 5, 9182 Greuth, Österreich, vertreten durch LBG Niederösterreich  Steuerberatung GmbH, Schloßparkgasse 6, 3950 Gmünd, betreffend Beschwerde vom  14. Februar 2020 gegen den Bescheid des Finanzamtes Österreich vom 21. Jänner 2020  betreffend Einkommensteuer 2017 Steuernummer 33-883/1280  den Beschluss:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als  zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ashley Wanagat` (person)
- `Dörfles 5, 9182 Greuth, Österreich` (address)
- `LBG Niederösterreich  Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `33-883/1280` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/137504.1`) (sent_id: `deanon_BFG_20260814_TEST/137504.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Klaus Gerwarth  in der Beschwerdesache  ÖkR Reneé Utzmeier, Chimanigasse 6, 8312 Ottendorf an der Rittschein, Österreich, über die Beschwerde vom 28. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 19. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Klaus Gerwarth` | `Priv.-Doz. Klaus Gerwarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Reneé Utzmeier` (person)
- `Chimanigasse 6, 8312 Ottendorf an der Rittschein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva Danell` (person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich` (address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG` (organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg` (organisation)
- `48-595/6877` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dietmar Hülsmeier  in der Beschwerdesache StR Linn Hochleitner,  Am Schlammteich 131, 4741 Perndorf, Österreich, vertreten durch Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH,  Ötztaler Höhe 11, 6430 Ötztal-Bahnhof, über die Beschwerde vom 31. August 2015 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom 11. August  2015 betreffend Festsetzung von Anspruchszinsen (§ 205 BAO) 2012 und Einkommensteuer  2012, Steuernummer 47-841/9334,  1 ) zu Recht erkannt:   a) Der Beschwerde betr.

| Predicted | Gold |
|---|---|
| `Dr. Dietmar Hülsmeier` | `Dr. Dietmar Hülsmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Linn Hochleitner` (person)
- `Am Schlammteich 131, 4741 Perndorf, Österreich` (address)
- `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH` (organisation)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `47-841/9334` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/137635.1`) (sent_id: `deanon_BFG_20260814_TEST/137635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Frühmark  in der Beschwerdesache Hon.-Prof. Sven Corbin,  Stalderhaus 7, 9363 Feistritz, Österreich, über die Beschwerde vom 23. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juli 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Juni 2018 bis Jänner 2019, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Valerius Frühmark` | `Priv.-Doz. Valerius Frühmark` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Corbin` (person)
- `Stalderhaus 7, 9363 Feistritz, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julia Reittinger` (person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich` (address)
- `Annemarie Entschev-Kurzmann` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Muran Unverricht, Bleischweg 3, 9500 Rennstein, Österreich, über die Beschwerden vom 28. Oktober 2018, vom 9. Februar 2019  und vom 7. Februar 2020 gegen die Bescheide des Finanzamtes Österreich vom 26. Juli 2018  betreffend Abweisung eines Antrages auf Aufhebung des Körperschaftsteuerbescheides 2016  sowie vom 31. Jänner 2019 und vom 16. Jänner 2020 betreffend Körperschaftsteuer 2017 und  2018 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Abweisung eines Antrages auf Aufhebung  des Körperschaftsteuerbescheides 2016 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Muran Unverricht` (person)
- `Bleischweg 3, 9500 Rennstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Frank Ruhleder  in der Beschwerdesache Dr. Luigi Mainholz  vertreten durch STB, über die mit Beschwerden angefochtenen Bescheide des FA Wien 1/23,  Steuernummer 61-747/1918, betreffend Einkommensteuer 2005, 2006, 2008, 2009, 2010  und 2011 zu Recht erkannt:    Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Frank Ruhleder` | `Hon.-Prof. Frank Ruhleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Luigi Mainholz` (person)
- `FA Wien 1/23` (organisation)
- `61-747/1918` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Roderich Stenczel, St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich, über die Beschwerde vom 20. August 2013 gegen die Bescheide  des FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Wiederaufnahme gemäß § 303 BAO  der Körperschaftsteuerbescheide 2008 bis 2010, Steuernummer 60-379/9146  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roderich Stenczel` (person)
- `St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `60-379/9146` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/138120.1`) (sent_id: `deanon_BFG_20260814_TEST/138120.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Birgit Altvater, Pizachweg 11, 2020 Oberfellabrunn, Österreich, vertreten durch JM Wirtschaftsprüfungs-GmbH,  Sonnhubergasse 9, 4060 Leonding, und JM Wirtschaftsprüfungs-GmbH, Sonnhubergasse 9,  4060 Leonding, betreffend Beschwerde vom 15. April 2022 gegen die Bescheide des  Finanzamtes Österreich vom  1. 25. Oktober 2021 betreffend Festsetzung einer Zwangsstrafe iHv 1.000 Euro und   2. 12. Jänner 2022 betreffend Festsetzung einer Zwangsstrafe iHv 4.000 Euro,

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Birgit Altvater` (person)
- `Pizachweg 11, 2020 Oberfellabrunn, Österreich` (address)
- `JM Wirtschaftsprüfungs-GmbH` (organisation)
- `JM Wirtschaftsprüfungs-GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/138259.1`) (sent_id: `deanon_BFG_20260814_TEST/138259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Otto Pavlikova  in der Angelegenheit der Parteien  Oskar Wood (Beschwerdeführer) und Finanzamt Österreich als Amtspartei und als  Gesamtrechtsnachfolger des FA Niederösterreich Mitte  über die Beschwerde vom  22.6.2020 gegen den Bescheid des FA Niederösterreich Mitte  vom 22.5.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019         zu Recht erkannt:  Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Otto Pavlikova` | `Univ.-Prof. Otto Pavlikova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oskar Wood` (person)
- `Finanzamt Österreich` (organisation)
- `FA Niederösterreich Mitte` (organisation)
- `FA Niederösterreich Mitte` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Zlatan Wetterling, Am Kochfeld 129, 4770 Oberndorf, Österreich, vom 21. November 2019, gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 8. November 2019 betreffend gemäß § 8a FLAG gekürzte  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Christian Doktor` | `Mag. Christian Doktor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zlatan Wetterling` (person)
- `Am Kochfeld 129, 4770 Oberndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/138674.1`) (sent_id: `deanon_BFG_20260814_TEST/138674.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Kai Steinacker  in der Säumnisbeschwerdesache  Univ.-Prof. Achmed Singendonk, IZ NÖ-Süd Straße 2 a 4, 3214 Buchberg, Österreich, über die Beschwerde vom 12.11.2022, beim Bundesfinanzgericht  am 24.11.2022 eingelangt, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich betreffend    Erlassung einer Beschwerdevorentscheidung hinsichtlich Einkommensteuer 2021 sowie   Bescheidabänderung gemäß § 295a BAO hinsichtlich Einkommensteuer 2020   beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs 7 lit b BAO iVm § 260 Abs 1 lit a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Kai Steinacker` | `Mag. Kai Steinacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Achmed Singendonk` (person)
- `IZ NÖ-Süd Straße 2 a 4, 3214 Buchberg, Österreich` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamtes  Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Wieland Nieß, Primau 14, 2813 Spratzau, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 20. Februar 2020 gegen  den Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln vom 29. Jänner 2020 betreffend  Einkommensteuer 2018, Steuernummer 72-272/3022, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Nieß` (person)
- `Primau 14, 2813 Spratzau, Österreich` (address)
- `Ernst & Young Steuerberatungs- gesellschaft  m.b.H.` (organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `72-272/3022` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  OSR KommR Susette Stenczel, Amtweg 83, 9542 Tobitsch, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glückspiel vom 25. September 2019  betreffend Gebühr Steuernummer 61-194/1325  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR KommR Susette Stenczel` (person)
- `Amtweg 83, 9542 Tobitsch, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `61-194/1325` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yelec Tummascheit  in der Beschwerdesache Gerda Staigl,  Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich, über die Beschwerde vom 11.08.2022 gegen den Bescheid des Finanzamtes  Österreich vom 05.08.2022, Steuernummer 64-583/4801, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Yelec Tummascheit` | `Univ.-Prof. Yelec Tummascheit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerda Staigl` (person)
- `Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `64-583/4801` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jan Jürn  in der Beschwerdesache Armin Klews, Bakk. art.,  Lesach 119, 3071 Untergrafendorf, Österreich, über die Beschwerde vom 28. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 20. April 2022 betreffend Abweisung des Antrages auf Gewährung von  Familienbeihilfe ab Februar 2022 zur Steuernummer 51-609/6898  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Jan Jürn` | `Hon.-Prof. Jan Jürn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Armin Klews, Bakk. art.` (person)
- `Lesach 119, 3071 Untergrafendorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `51-609/6898` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 1. Juli 2013 des Beschwerdeführers HR Carmen Ruepprich, Adr Bf, Steuernummer: 63-173/6802,  gegen die Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom  25. Juni 2013 betreffend Festsetzung der Umsatzsteuer für den Erwerb neuer Fahrzeuge  (Fahrzeugeinzelbesteuerung) für den PKW Ford Mondeo, Festsetzung der  Normverbrauchsabgabe 1/2012 sowie Kraftfahrzeugsteuer 1-12/2012 und 1-3/2013 zu Recht:    I)  Die Beschwerde betreffend Festsetzung der Umsatzsteuer für den Erwerb neuer Fahrzeuge  (Fahrzeugeinzelbesteuerung) für den PKW Ford Mondeo wird gem. § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR Carmen Ruepprich` (person)
- `63-173/6802` (tax_number)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/139407.1`) (sent_id: `deanon_BFG_20260814_TEST/139407.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Silvius Christidou, Landlerweg 2, 7202 Lichtenwörth, Österreich, betreffend   Beschwerde (ursprünglich Berufung) vom 29. Mai 2012 gegen den  Einkommensteuerbescheid 2009 des Finanzamtes Wien 3/11 Schwechat Gerasdorf vom  25. Mai 2012 zu St.Nr. alteStNr,   am 14. November 2012 beim Finanzamt eingelangter Vorlageantrag gegen die Beru- fungsvorentscheidungen des Finanzamtes Wien 3/11 Schwechat Gerasdorf vom  4. Oktober 2012 zu Steuernummer alteStNr hinsichtlich Einkommensteuer 2009, 2010  und 2011,   Vorlage der Beschwerde gegen den Einkommensteuerbescheid 2009 durch das  Finanzamt Österreich an das Bundesfinanzgericht (BFG) am 25. Oktober 2022,   Vorlagebericht des Finanzamtes Österreich vom 25. Oktober 2022 zu nunmehriger  Steuernummer 15-665/6861  hinsichtlich der eingebrachten Beschwerde (damals:  Berufung) vom 29. Mai 2012 gegen den Einkommensteuerbescheid 2009 vom 25. Mai  2012 sowie hinsichtlich nicht eingebrachter Beschwerden vom 29. Mai 2012 gegen die  Einkommensteuerbescheide 2010 und 2011 vom 25. Mai 2012,  beschlossen:  Der am 14. November 2012 beim Finanzamt eingelangte Vorlageantrag gegen die  Beschwerdevorentscheidungen vom 4. Oktober 2012 hinsichtlich Einkommensteuer 2009,  2010 und 2011 wird gemäß § 260 Abs. 1 lit. b in Verbindung mit § 264 Abs. 4 lit. e und § 264  Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvius Christidou` (person)
- `Landlerweg 2, 7202 Lichtenwörth, Österreich` (address)
- `Finanzamtes Wien 3/11 Schwechat Gerasdorf` (organisation)
- `Finanzamt` (organisation)
- `Finanzamtes Wien 3/11 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `Bundesfinanzgericht (BFG)` (organisation)
- `Finanzamtes Österreich` (organisation)
- `15-665/6861` (tax_number)
- `Finanzamt` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Günter Möhlenfeld  in Vertretung des verhinderten  Richters Hon.-Prof. Kaspar Frantzius  in der Verwaltungsstrafsache gegen Elias Schwabeland, Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 22. November  2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  15. November 2021, GZ. MA67/Zahl/2021, nach Durchführung einer mündlichen Verhandlung  am 19. Dezember 2022, in Anwesenheit des Beschuldigten und der Schriftführerin IP, jedoch in  entschuldigter Abwesenheit einer Vertreterin/eines Vertreters der belangten Behörde, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat die beschwerdeführende Partei keinen Beitrag zu den Kosten  des Beschwerdeverfahrens zu entrichten.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Günter Möhlenfeld` | `Hon.-Prof. Günter Möhlenfeld` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Kaspar Frantzius` (person)
- `Elias Schwabeland` (person)
- `Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Brendon Spade` | `Univ.-Prof. Brendon Spade` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Milena Piechulik` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Walther Kendler` (person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/139653.1`) (sent_id: `deanon_BFG_20260814_TEST/139653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Fridolin Zielke  in der Beschwerdesache Monika Tomm,  Mitteredt 3, 4776 Dobl, Österreich, betreffend Beschwerden vom 7. April 2022 gegen die Bescheide des  Finanzamtes Österreich vom 8. Juli 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Einkommensteuer (Arbeitnehmerveranlagung) 2019 und  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 98-832/4427, den  Beschluss:  I. Die Beschwerden werden als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Fridolin Zielke` | `Priv.-Doz. Fridolin Zielke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Monika Tomm` (person)
- `Mitteredt 3, 4776 Dobl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `98-832/4427` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch Henning & Partner Steuerberatung GmbH,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Imre Zeitner` | `Priv.-Doz. Imre Zeitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daisy Schlimme` (person)
- `Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich` (address)
- `Henning & Partner Steuerberatung GmbH` (organisation)
- `Dr. Michael Kotschnigg` (person)
- `Finanzamtes  Graz-Umgebung` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/139879.1`) (sent_id: `deanon_BFG_20260814_TEST/139879.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Giacomello  in der Beschwerdesache Natascha Theys vertreten  durch StB über die Beschwerde vom 3. Oktober 2022 gegen den Bescheid des FA Linz  vom  9. September 2022 über die Festsetzung eines ersten Säumniszuschlages (Steuernummer  86-989/6915 ) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Wilfried Giacomello` | `Univ.-Prof. Wilfried Giacomello` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natascha Theys` (person)
- `FA Linz` (organisation)
- `86-989/6915` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Waldemar Janaschke, Reithbachweg 6, 4892 Walligen, Österreich, über die Beschwerde vom 7. Juni 2021 gegen  den Bescheid des Finanzamtes Österreich vom 17. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 59-080/2897  zu Recht:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Patrick Brandstetter` | `Mag. Patrick Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waldemar Janaschke` (person)
- `Reithbachweg 6, 4892 Walligen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `59-080/2897` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/140311.1`) (sent_id: `deanon_BFG_20260814_TEST/140311.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Reinhard Milschlag  in der Beschwerdesache Melanie Guidi,  Scheatlers Wies 27, 3633 Dorfstadt, Österreich, über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 5. Juni 2019 betreffend die Bewilligung einer Zahlungserleichterung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Reinhard Milschlag` | `Univ.-Prof. Reinhard Milschlag` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melanie Guidi` (person)
- `Scheatlers Wies 27, 3633 Dorfstadt, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/140320.1`) (sent_id: `deanon_BFG_20260814_TEST/140320.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jonathan Eisbrenner  in der Beschwerdesache Marion Voskuil,  Taschlgrabenrotte 9, 4190 Ortschlag, Österreich, betreffend die Beschwerde vom 30. November 2022 gegen den Bescheid des  Finanzamt Innsbruck  vom 20. Oktober 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2021, Steuernummer 86-965/4065, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Jonathan Eisbrenner` | `Hon.-Prof. Jonathan Eisbrenner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marion Voskuil` (person)
- `Taschlgrabenrotte 9, 4190 Ortschlag, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `86-965/4065` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/140588.1`) (sent_id: `deanon_BFG_20260814_TEST/140588.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Lerchenfelderstraße 9, 4230 Burbach, Österreich, über die Beschwerde vom 16. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Anspruchszinsen (§ 205  BAO) 2015, Steuernummer 87-149/1701, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lerchenfelderstraße 9, 4230 Burbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `87-149/1701` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Jeanne Kraenzlin, KSV-Donaufreunde 25, 8323 Petersdorf II, Österreich, vertreten durch Treuhand-Union Innsbruck  Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH, Anton-Melzer-Straße 7, 6020  Innsbruck, über die Beschwerde vom 28.09.2021 gegen die Bescheide des Finanzamtes  Österreich vom 23.07.2021 über die Festsetzung der Kapitalertragsteuer für die Zeiträume  2015, 2016, 2017 und 2018, beschlossen:  I. Die angefochtenen Bescheide vom 23.07.2021 über die Festsetzung der Kapitalertragsteuer  für die Zeiträume 2015, 2016, 2017 und 2018 sowie die Beschwerdevorentscheidung vom  01.09.2022 werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an das  Finanzamt aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeanne Kraenzlin` (person)
- `KSV-Donaufreunde 25, 8323 Petersdorf II, Österreich` (address)
- `Treuhand-Union Innsbruck  Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Günter Narat über die Beschwerden vom  10. Oktober 2013 bzw. 3. Jänner 2018 der Beschwerdeführerin Franziskus Keilhammer, Gaas-Weinberg 78, 4873 Mitterriegl, Österreich  Steuernummer: 27-823/1627, gegen die Bescheide des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf (nunmehr Finanzamt Österreich) vom 4. Dezember 2017 betreffend  Umsatz- und Körperschaftsteuer 2013 nach der am 4. Mai 2023 über Antrag der Partei (§ 274  Abs 1 Z 1 BAO) in Linz abgehaltenen öffentlichen Verhandlung zu Recht erkannt:  I)  Die Beschwerde vom 10. Oktober 2013 betreffend den Umsatzsteuerbescheid 2013 wird  gem. § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Keilhammer` (person)
- `Gaas-Weinberg 78, 4873 Mitterriegl, Österreich` (address)
- `27-823/1627` (tax_number)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Janosch Herr  in der Beschwerdesache des  René Schiekel, MSc, Auf der Kröß 1, 2151 Altmanns, Österreich, vertreten durch Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH, Gartenaugasse 3, 3500 Krems/Donau, über die Beschwerde vom 11. Juni 2019 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Janosch Herr` | `Mag. Janosch Herr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `René Schiekel, MSc` (person)
- `Auf der Kröß 1, 2151 Altmanns, Österreich` (address)
- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache gegen Birgit Aytekin, Grabenmühlweg 44, 4161 Stollnberg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 26. Mai 2023 gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 9. Mai 2023, GZ.  MA67/[...]/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Birgit Aytekin` (person)
- `Grabenmühlweg 44, 4161 Stollnberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/141437.1`) (sent_id: `deanon_BFG_20260814_TEST/141437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Alina Gawlak, Schultheißweg 10, 9241 Kletschach, Österreich, über die Beschwerde (1.) vom 20. April 2022 gegen den Bescheid  des Finanzamtes Österreich vom 6. April 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 und (2.) vom 20. September 2022 gegen den Bescheid des  Finanzamtes Österreich vom 31. August 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019,  Steuernummer 76-847/7456  zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO teilweise im Sinne des  Beschwerdebegehrens abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alina Gawlak` (person)
- `Schultheißweg 10, 9241 Kletschach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `76-847/7456` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/141488.1`) (sent_id: `deanon_BFG_20260814_TEST/141488.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Jeremias Bogdon, Watzing 3, 9062 Untergöriach, Österreich, vertreten durch HGS - Mag. Hans Günther  Schönauer Wirtschaftsprüfung und Steuerberatung GmbH, Oberfeldstraße 54, 4600 Wels, über  die Beschwerde vom 04. Mai 2016 gegen die Bescheide des Finanzamtes Braunau Ried  Schärding (nunmehr Finanzamt Österreich) vom 15. März 2016 über die Wiederaufnahme des  Verfahrens betreffend Einkommensteuer 2012 und 2013 Steuernummer 04-020/2623  zu  Recht:   I. Die Beschwerde gegen den Bescheid vom 15. März 2016 betreffend die Wiederaufnahme des  Verfahrens hinsichtlich der Einkommensteuer für das Jahr 2012 wird als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Patrick Brandstetter` | `Mag. Patrick Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Bogdon` (person)
- `Watzing 3, 9062 Untergöriach, Österreich` (address)
- `HGS - Mag. Hans Günther  Schönauer Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes Braunau Ried` (organisation)
- `Finanzamt Österreich` (organisation)
- `04-020/2623` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Kira Mathies, Gülke 91, 9560 Regin, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. April 2019 betreffend Aufhebung des  Einkommensteuerbescheides 2015 vom 17.1.2019 gemäß § 299 BAO und Einkommensteuer   2015 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Aufhebung des Einkommensteuerbescheides  2015 vom 17.1.2019 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kira Mathies` (person)
- `Gülke 91, 9560 Regin, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Patrick Poppenheger, Steuernummer 23-019/0780,   Str.1, O1, vertreten durch Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft, Ruster Straße 91, 7000 Eisenstadt, vom 15.07.2020 gegen den  Einkommensteuerbescheid für das Jahr 2018 des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr FA Österreich), vom 29.06.2020, zugestellt am 02.07.2020, nach der im Beisein des  Schriftführers Dietmar Gratz am 29.06.2023 durchgeführten mündlichen Verhandlung  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der  angefochtene Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Patrick Poppenheger` (person)
- `23-019/0780` (tax_number)
- `Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `FA Österreich` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad über die Beschwerde  des Wilhelm Möncher, Hernalser Gürtel 1, 3192 Furthof, Österreich, vom 4. Juli 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26. Juni 2023, GZ.  MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und das angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Konrad` | `Mag. Gerhard Konrad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Möncher` (person)
- `Hernalser Gürtel 1, 3192 Furthof, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/141803.1`) (sent_id: `deanon_BFG_20260814_TEST/141803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Dr. Sven Antonowitsch  in der Beschwerdesache Elvira Klockenberg,  Hochwandweg 38, 4741 Rappoltsberg, Österreich, vertreten durch ÖZIV-Burgenland, Verband für Menschen mit Behinderungen,  Marktstraße 3 Tür 0, 7000 Eisenstadt, betreffend Beschwerde vom 23. Jänner 2023 gegen den  Bescheid des Finanzamtes Österreich vom 12. September 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 den Beschluss:   I. Der Vorlageantrag vom 31.03.2023 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Sven Antonowitsch` | `Dr. Sven Antonowitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elvira Klockenberg` (person)
- `Hochwandweg 38, 4741 Rappoltsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/141952.1`) (sent_id: `deanon_BFG_20260814_TEST/141952.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Niklas Dankwarth, Schüttaustraße 10, 9753 Raggnitz, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse  17, 1030 Wien, über die Beschwerde vom 24. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. August 2020 betreffend Einkommensteuer 2018  Steuernummer 01-612/4118  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Niklas Dankwarth` (person)
- `Schüttaustraße 10, 9753 Raggnitz, Österreich` (address)
- `Caroline Toifl Rechtsanwalt GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `01-612/4118` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Flora Tahir, Sommeregg 24, 9634 Oberbuchach, Österreich, vertreten durch Renate Dolezal, Speisinger Str 50-52 Tür 18, 1130  Wien, über die Beschwerde vom 5. Oktober 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016, Steuernummer 20-636/7581, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Konrad` | `Mag. Gerhard Konrad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Tahir` (person)
- `Sommeregg 24, 9634 Oberbuchach, Österreich` (address)
- `Renate Dolezal` (person)
- `Finanzamtes  Österreich` (organisation)
- `20-636/7581` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Rupert Wedell  in der Beschwerdesache OStR OMedR Rebecca Ehrmanntraut,  Museumplatz 27, 8241 Rohrbachschlag, Österreich, über die Beschwerden vom 10. Oktober 2017 gegen die Bescheide des  FA Baden Mödling  vom 27. Juni 2017 bzw. 10. Juli 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 bis 2015, Steuernummer 38-848/8801, zu Recht erkannt:  I. Den Beschwerden gegen die Bescheide betreffend Einkommensteuer für die Jahre 2012 bis  2015 wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Rupert Wedell` | `Hon.-Prof. Rupert Wedell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR OMedR Rebecca Ehrmanntraut` (person)
- `Museumplatz 27, 8241 Rohrbachschlag, Österreich` (address)
- `FA Baden Mödling` (organisation)
- `38-848/8801` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/142826.1`) (sent_id: `deanon_BFG_20260814_TEST/142826.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Bodo Bookhold  in der Beschwerdesache Samuel Haßelbarth,  Zeilberg 4, 3233 Bühren, Österreich, über die Beschwerde vom 02.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 28.05.2021, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Bodo Bookhold` | `Priv.-Doz. Bodo Bookhold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Haßelbarth` (person)
- `Zeilberg 4, 3233 Bühren, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Alan Sontheimer  in der Angelegenheit der Parteien  Paul Sohm (Beschwerdeführer), und Finanzamt Klagenfurt St. Veit Wolfsberg  als Amtspartei über die Säumnisbeschwerde,  datiert vom 16. Feber 2024, eingebracht beim Bundesfinanzgericht am 17. Jänner 2024   betreffend seine Beschwerde vom 14.8.2023 gegen den Bescheid des Finanzamtes vom  13.7.2023 betreffend Festsetzung von Anspruchszinsen 2021 in Höhe von 67,61 €  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Alan Sontheimer` | `Mag. Alan Sontheimer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paul Sohm` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Priv.-Doz. Dr` — partial — pred is substring of gold: `Priv.-Doz. Dr. Kurt Bartold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

**False Positives:**

- `Mag. Pjotr` — partial — pred is substring of gold: `Mag. Pjotr Übereiter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Pjotr Übereiter`(person)
- `Linn Gouthier`(person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof. Univ` — partial — pred is substring of gold: `Univ.-Prof. Univ.-Prof. Kai Menrath`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

**False Positives:**

- `Mag. Mag` — partial — pred is substring of gold: `Mag. Mag. Niels Rustemeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mag. Niels Rustemeier`(person)
- `Nicoletta Walch`(person)
- `Polheimerweg 2, 3464 Schmida, Österreich`(address)
- `65-653/8677`(tax_number)
- `Finanzamt Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Frederik` — partial — pred is substring of gold: `Priv.-Doz. Frederik von Gruber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Mag. Hon` — partial — pred is substring of gold: `Mag. Hon.-Prof. Engelbert Voglsang`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. David Hell` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `DDr. Ali Franzel`(person)
- `Oberwirtsweg 5, 8562 Bubendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-470/7314`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Priv` — partial — pred is substring of gold: `Mag. Priv.-Doz. Andreas Domingo`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Klara Biallowons, Höslrein 65, 3470 Oberstockstall, Österreich, vertreten durch UnionTAX & LAW, Donau-City- Straße 7/DC Tower/30th Floor, 1220 Wien, betreffend Säumnisbeschwerde vom 10.2.2023  wegen Verletzung der Entscheidungspflicht hinsichtlich Arbeitnehmerveranlagung 2018 und  2019 durch das Finanzamt Österreich zur Sozialversicherungsnummer 5116 301100  beschlossen:  I. Die Säumnisbeschwerde gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Klara Biallowons`(person)
- `Höslrein 65, 3470 Oberstockstall, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `5116 301100`(social_security_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Priv` — partial — pred is substring of gold: `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Univ` — partial — pred is substring of gold: `Hon.-Prof. Univ.-Prof. Florian Rouse`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Univ.-Prof. Florian Rouse`(person)
- `Evamaria Watenphul`(person)
- `Allhartsbergerstraße 47, 8142 Kasten, Österreich`(address)
- `Mehmet Köprücü`(person)
- `Puchheimgasse 14, 6234 Brandenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `83-456/1644`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141869.1`) (sent_id: `deanon_BFG_20260814_TEST/141869.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Theobald Rütgens  in der Beschwerdesache Dagmar Weikart,  Stockstraße 28, 9640 Krieghof, Österreich, vertreten durch UnionTax & Law Rechtsanwälte, Obere Zelgstraße 2, 8590  Romanshorn, Schweiz, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt Österreich über den Antrag vom 27.7.2022 auf Durchführung der  Arbeitnehmerveranlagung 2020, Steuernummer 50-301/3055  beschlossen:   Die Beschwerde wird gemäß § 284 Abs. 7 lit. b BAO in Verbindung mit § 260 Abs. 1 lit. a BAO  als nicht zulässig zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Mag` — partial — pred is substring of gold: `Univ.-Prof. Mag. Theobald Rütgens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Mag. Theobald Rütgens`(person)
- `Dagmar Weikart`(person)
- `Stockstraße 28, 9640 Krieghof, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `50-301/3055`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Chen Thiergarten, Recyclingstraße 4z, 9911 Vergein, Österreich, vertreten durch Lang & Partner Steuerberatung  GmbH & Co KG, Kapfenstein 123, 8353 Kapfenstein, über die Beschwerde der  beschwerdeführenden Partei vom 17. Juli 2023 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Bescheidaufhebung gem § 299 BAO vom 30. Dezember 2022 hinsichtlich der Bescheide  Umsatzsteuer 2019 und Feststellung von Einkünften gemäß § 188 BAO 2019, jeweils vom 7.  Jänner 2022, Steuernummer 91-654/5089  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Martin` — partial — pred is substring of gold: `Dr. Martin C. WITTMANN`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Chen Thiergarten`(person)
- `Recyclingstraße 4z, 9911 Vergein, Österreich`(address)
- `Lang & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamt Österreich`(organisation)
- `91-654/5089`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hon` — partial — pred is substring of gold: `Mag. Hon.-Prof. Wilfried Brokof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Wilfried Brokof`(person)
- `Hademar Haßelbach, BSc`(person)
- `Engerbergstraße 2, 8642 Nechelheim, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `59-681/6477`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142978.1`) (sent_id: `deanon_BFG_20260814_TEST/142978.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Dieter Schwitalski, Zayagasse 125, 8162 Amstein, Österreich, über die Beschwerde vom 17. Oktober 2021  gegen die Bescheide des Finanzamtes Österreich jeweils vom 12. Oktober 2021,  Steuernummer 23-275/5780, betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Martin` — partial — pred is substring of gold: `Dr. Martin C. WITTMANN`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Dieter Schwitalski`(person)
- `Zayagasse 125, 8162 Amstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `23-275/5780`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Mag. Hon` — partial — pred is substring of gold: `Mag. Hon.-Prof. Denis Hoffjan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Nicolaus Pomaroli MAS in der  Beschwerdesache Techn R Miroslav Sängewald, Anton-Leb-Gasse 54, 4760 Bründl, Österreich, über die Beschwerde vom 23. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 18. Mai 2022 betreffend Familienbeihilfe 2022  zu Recht:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr. Nicolaus Pomaroli` — partial — pred is substring of gold: `Dr. Nicolaus Pomaroli MAS`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Nicolaus Pomaroli MAS`(person)
- `Techn R Miroslav Sängewald`(person)
- `Anton-Leb-Gasse 54, 4760 Bründl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144847.1`) (sent_id: `deanon_BFG_20260814_TEST/144847.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Mag. James Thomalla  in der Beschwerdesache Jelena Ziegelmeyer,  Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich, über die Beschwerde vom 30.6.2023 gegen den Bescheid des Finanzamtes  Österreich vom 20.6.2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 den  Beschluss:   I. Der Vorlageantrag vom 22.9.2023 wird gemäß § 256 Abs 3 iVm § 264 Abs 4 lit d BAO als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Mag` — partial — pred is substring of gold: `Hon.-Prof. Mag. James Thomalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Mag. James Thomalla`(person)
- `Jelena Ziegelmeyer`(person)
- `Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch den Richter Mag. David Hell LL.B. LL.M. in der Beschwerde- sache Geraldine Loeper, Bakk. techn., Südstraße 6, 6471 Leins, Österreich, zur Beschwerde vom 20. November 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 16-579/1693, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde- vorentscheidung vom 15. Jänner 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2022 kein Vorlageantrag eingebracht.

**False Positives:**

- `Mag. David Hell` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Geraldine Loeper, Bakk. techn.`(person)
- `Südstraße 6, 6471 Leins, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-579/1693`(tax_number)
- `Bundesfinanzgerichts`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Dr. Nicolaus Pomaroli MAS in der  Finanzstrafsache gegen Merlin Gronmeyer, Panhansstraße 50, 9112 Wölfnitz, Österreich  wegen der Finanzvergehen der  Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes - FinStrG, der versuchten  Abgabenhinterziehung nach §§ 13, 33 Abs. 1 des Finanzstrafgesetzes - FinStrG, der  Abgabenhinterziehung nach § 33 Abs. 2 lit. a des Finanzstrafgesetzes - FinStrG sowie der  Finanzordnungswidrigkeit nach § 51 Abs. 1 lit. g des Finanzstrafgesetzes - FinStrG über die  Beschwerde der Beschuldigten vom 25. April 2024 gegen den Bescheid des Amtes für  Betrugsbekämpfung als Finanzstrafbehörde gemäß § 167 des Finanzstrafgesetzes - FinStrG vom  25. März 2024, Geschäftszahl *GZ*, zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr. Nicolaus Pomaroli` — partial — pred is substring of gold: `Dr. Nicolaus Pomaroli MAS`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Nicolaus Pomaroli MAS`(person)
- `Merlin Gronmeyer`(person)
- `Panhansstraße 50, 9112 Wölfnitz, Österreich`(address)
- `Amtes für  Betrugsbekämpfung`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/146743.1`) (sent_id: `deanon_BFG_20260814_TEST/146743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Priv.-Doz. Priv.-Doz. Urs Heinatzky, Feldpichl 19, 8130 Peggau, Österreich, vertreten durch Mag. Beatrix Anna Elfriede  Reiff-Zehetner, Straße der Menschenrechte 11, 2103 Langenzersdorf, über die Beschwerde  vom 30. August 2023 gegen den Bescheid des Finanzamtes Österreich vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zur Steuernummer  51-583/1758  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Priv.-Doz. Priv.-Doz. Urs Heinatzky`(person)
- `Feldpichl 19, 8130 Peggau, Österreich`(address)
- `Mag. Beatrix Anna Elfriede  Reiff-Zehetner`(person)
- `Finanzamtes Österreich`(organisation)
- `51-583/1758`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/149737.1`) (sent_id: `deanon_BFG_20260814_TEST/149737.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mag. Timon Wandschneider  in der Beschwerdesache Linn Seebade,  Volkenstorferweg 19, 9863 Pron, Österreich, über die Beschwerde vom 23. April 2025 gegen den Bescheid des FA Freistadt Rohrbach Urfahr  vom 14. April 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 43-163/0517, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. Timon Wandschneider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Timon Wandschneider`(person)
- `Linn Seebade`(person)
- `Volkenstorferweg 19, 9863 Pron, Österreich`(address)
- `FA Freistadt Rohrbach Urfahr`(organisation)
- `43-163/0517`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Lothar Kriwet, Gaugen 11, 9150 Draurain, Österreich, vertreten durch Spiss Steuerberatung GmbH,  Timmlerweg 16, 6580 St. Anton am Arlberg, über die Beschwerde vom 31. Oktober 2025 gegen  die Bescheide des Finanzamtes Österreich vom 15. Oktober 2025 betreffend   1. Verzinsung gemäß § 16 COFAG-NoAG (Fixkostenzuschuss I),  2.

**False Positives:**

- `Mag. David Hell` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Lothar Kriwet`(person)
- `Gaugen 11, 9150 Draurain, Österreich`(address)
- `Spiss Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `legal_person_complainant_context` 🏆

**F1:** 0.272 | **Precision:** 0.853 | **Recall:** 0.162  

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
| 0.853 | 0.162 | 0.272 | 306 | 261 | 45 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 261 | 45 | 1353 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waltraud Hinterlandt` | `Waltraud Hinterlandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Lehwaldt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeanne Weiermann` | `Jeanne Weiermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Rzehula` | `Lewis Rzehula` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Parys` | `Daniel Parys` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Krafft` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Eligüzel` | `Chantal Eligüzel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Guntram Antepoth` | `Guntram Antepoth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Finn van Aken` | `Finn van Aken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich` (address)
- `Mag. Musa Işlek` (organisation)
- `Finanzamtes Wien  1/23` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Roxana Dellner` | `Roxana Dellner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Dammkoehler` | `Wladimir Dammkoehler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Pesselt` | `Ruprecht Pesselt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Serena Weidlich` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Isidor Czebulla` | `Isidor Czebulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Kendziorra` | `Elias Kendziorra` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Waldemar Faltermeir` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Floriane Rötker` | `Floriane Rötker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Leonhard Bianchini` | `Leonhard Bianchini` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helga Woschank` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Manuel Fortanz` | `Manuel Fortanz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Caroline Reinwaldt` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Eugen Burgschweiger` | `Eugen Burgschweiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernarda Egli` | `Bernarda Egli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hartwig Simonson` | `Hartwig Simonson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Hördegen` | `Sulamith Hördegen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Serena Leutl` | `Serena Leutl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Daisy Große-Bölting` (person)
- `Wanderweg 7, 2763 Thal, Österreich` (address)
- `Bernhart Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-306/6017` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Natalie Nodurft` | `Natalie Nodurft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrich Petrag` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Mag. Marion Riezinger` (person)
- `Finanzamtes  Linz` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Elisabeth Sarigiannis` | `Elisabeth Sarigiannis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klesenza 7, 9587 Erlendorf, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `84-729/8666` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gernot Kirchenmayer` | `Gernot Kirchenmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anneliese Wäsche` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dominik Moebus` | `Dominik Moebus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aichach 11m, 9375 Knappenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Felizitas Johanesson` | `Felizitas Johanesson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Griselda Hälmle` | `Griselda Hälmle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Pawel Schuwirth` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Christina Tiebout` | `Christina Tiebout` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Berkenkämper` | `Ruprecht Berkenkämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Gudrun Terzoglou` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Wendelin Pham` | `Wendelin Pham` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Paolo Reppert` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Juri Marstaller` | `Juri Marstaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Lydia Rehnen` | `Lydia Rehnen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Andrea Helbok` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexandra Hettrich` | `Alexandra Hettrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Richard Schwanken` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Esra Luetje` | `Esra Luetje` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Sven Hoerlin` | `Sven Hoerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Aloisa Antoni` | `Aloisa Antoni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juliana Untermeier` | `Juliana Untermeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Dr. Christoph Ganahl` (person)
- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Florentine Mugge` | `Florentine Mugge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich` (address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-287/7417` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Bruno Rüttgers` | `Bruno Rüttgers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wladimir Beheim` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

| Predicted | Gold |
|---|---|
| `Julian Gruening` | `Julian Gruening` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` (person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Babette Bernett` | `Babette Bernett` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (im Folgenden: BFG) hat durch den RichterRi in der Beschwerdesache  Anita Imkeller, Zum Roten Kreuzl 13, 4741 Penesedt, Österreich, betreffend Beschwerde vom 29. März 2021 gegen den Bescheid  des Finanzamt Niederösterreich Mitte  vom 4. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 50-932/4879  beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Anita Imkeller` | `Anita Imkeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `Zum Roten Kreuzl 13, 4741 Penesedt, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)
- `50-932/4879` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janis Dührkopp` | `Janis Dührkopp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Ingrid Dohrmaier` | `Ingrid Dohrmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Walter Guggenmoos` | `Walter Guggenmoos` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Alice Schöpfel` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `79-464/0427` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Carla Winterkorn` | `Carla Winterkorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Edith Grotehenn` | `Edith Grotehenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Leander Hättrich` (person)
- `Karlhofstraße 20, 4212 Götschka, Österreich` (address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `FA Wien  4/5/10` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Siebgen` | `Juri Siebgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich` (address)
- `MITTEREGGER Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-670/1415` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Andreas Kuschy  in der Beschwerdesache Angelika Oligschleger,  Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des Finanzamt Innsbruck  vom 29. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 49-970/7545  nach dem Einlangen des Vorlageantrages vom 10.6.2021  beschlossen:   Der Vorlageantrag wird gem. § 264 Abs 4 lit e Bundesabgabenordnung zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Angelika Oligschleger` | `Angelika Oligschleger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Andreas Kuschy` (person)
- `Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `49-970/7545` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Jaros` | `Silvius Jaros` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `97-301/3674` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramon Reissdorf` | `Ramon Reissdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag.Dr. Ingrid Fehrer` (person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich` (address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `86-314/1061` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sibylle Roßmayr` | `Sibylle Roßmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Lieselotte Stiglat` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `58-418/2406` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Björn Stover` | `Björn Stover` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `57-952/0912` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elmira Baintner  in der Beschwerdesache Dietmar Grießmeyer,  Stiftgasse 12, 4654 Aigen, Österreich, über die Beschwerde vom 31. Juli 2021 gegen den Bescheid des FA Steiermark Mitte  vom  26. Juli 2021 betreffend Abweisung eines Rückzahlungsantrages, Steuernummer  64-502/6730, zu Recht erkannt:   I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dietmar Grießmeyer` | `Dietmar Grießmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elmira Baintner` (person)
- `Stiftgasse 12, 4654 Aigen, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `64-502/6730` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ernst Eschenbrenner` | `Ernst Eschenbrenner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Klaus Krupok` (person)
- `Irenental 58, 4871 Tiefenbach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `80-953/9265` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Susanne Türner, Viehdorfer Straße 25, 9853 Burgwiese, Österreich, gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg  Tulln vom 25. November 2011 betreffend Körperschaftsteuer und Umsatzsteuer 2007,  Steuernummer 16-353/9813  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susanne Türner` | `Susanne Türner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Viehdorfer Straße 25, 9853 Burgwiese, Österreich` (address)
- `Finanzamtes` (organisation)
- `16-353/9813` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Patrick Hübben  in der Beschwerdesache Alice Rüde,  Auhub 26, 9560 Kraß, Österreich, vertreten durch BDO Steiermark GmbH Wtp u Stb, Schubertstraße 62, 8010  Graz, über die Beschwerde vom 18. März 2019 gegen den Bescheid des FA Tirol Ost  vom  26. Februar 2019 betreffend Abweisung eines Zahlungserleichterungsansuchens zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alice Rüde` | `Alice Rüde` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Patrick Hübben` (person)
- `Auhub 26, 9560 Kraß, Österreich` (address)
- `BDO Steiermark GmbH Wtp` (organisation)
- `FA Tirol Ost` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Nadine Hupmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Fröhner` | `Lewis Fröhner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dimitri Seewaldt` | `Dimitri Seewaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Marion Schlesing` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `Finanzamtes Österreich` (organisation)
- `93-757/0582` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Raul Türkkan` | `Raul Türkkan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dora Grobstich` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `24-623/5745` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Nicoletta Walch` | `Nicoletta Walch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mag. Niels Rustemeier` (person)
- `Polheimerweg 2, 3464 Schmida, Österreich` (address)
- `65-653/8677` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Adriana Eiffler, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Adriana Eiffler` | `Adriana Eiffler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Waldhofweg 36a, 8321 Entschendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-550/2209` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Hartmut Schalk, Parhamerplatz 8, 9112 Gletschach, Österreich, betreffend Beschwerde vom 31. Juli 2012 gegen die Bescheide des  FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 29. Juli 2011 betreffend  Einkommensteuer der Jahre 2006 bis 2010, Steuernummer 16-753/5618  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hartmut Schalk` | `Hartmut Schalk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Parhamerplatz 8, 9112 Gletschach, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-753/5618` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Severin Iwanowsky  in der Beschwerdesache Richard Joistgen,  Breitenbachstraße 15, 4794 Glatzing, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 31. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 81-572/7905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Richard Joistgen` | `Richard Joistgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Severin Iwanowsky` (person)
- `Breitenbachstraße 15, 4794 Glatzing, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `81-572/7905` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Harald Adriaans` | `Harald Adriaans` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich` (address)
- `Mag. Markus Wagner` (person)
- `Finanzamtes Österreich` (organisation)
- `81-584/4494` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Jörg Kuhstoss, Hasenberg 58, 3240 Grub bei Kilb, Österreich, über die Beschwerde vom 3. April 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 70-705/2274  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jörg Kuhstoss` | `Jörg Kuhstoss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hasenberg 58, 3240 Grub bei Kilb, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `70-705/2274` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Laila Klimenkow` | `Laila Klimenkow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Frederik von Gruber` (person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich` (address)
- `Causa Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Björn Augusto  in der Beschwerdesache Mona Reinhard,  Urschendorf 19, 4261 Kerschbaum, Österreich, vertreten durch IMMUNITAS Wirtschaftsprüfung GmbH, Schlickgasse 3 Tür 7,  1090 Wien, über die Beschwerde der beschwerdeführenden Partei vom 17.05.2022, beim  Bundesfinanzgericht eingelangt am 19.05.2022, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt für Großbetriebe betreffend Einkommen- und  Umsatzsteuer 2020 den Beschluss:   I. Das Säumnisbeschwerdeverfahren wird eingestellt.    II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mona Reinhard` | `Mona Reinhard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Björn Augusto` (person)
- `Urschendorf 19, 4261 Kerschbaum, Österreich` (address)
- `IMMUNITAS Wirtschaftsprüfung GmbH` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/137175.1`) (sent_id: `deanon_BFG_20260814_TEST/137175.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Ashley Wanagat, Dörfles 5, 9182 Greuth, Österreich, vertreten durch LBG Niederösterreich  Steuerberatung GmbH, Schloßparkgasse 6, 3950 Gmünd, betreffend Beschwerde vom  14. Februar 2020 gegen den Bescheid des Finanzamtes Österreich vom 21. Jänner 2020  betreffend Einkommensteuer 2017 Steuernummer 33-883/1280  den Beschluss:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als  zurückgenommen.

| Predicted | Gold |
|---|---|
| `Ashley Wanagat` | `Ashley Wanagat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniel Philip Pfau` (person)
- `Dörfles 5, 9182 Greuth, Österreich` (address)
- `LBG Niederösterreich  Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `33-883/1280` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Johanna Housein, Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 85-874/2370, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Johanna Housein` | `Johanna Housein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-874/2370` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Merlin Leuprecht` | `Merlin Leuprecht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Christine Kralova` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Anton Fleischhacker` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bertha Unverich` | `Bertha Unverich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich` (address)
- `Dr. Robert Karl Galler` (person)
- `92-593/4806` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alva Danell` | `Alva Danell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Stefan Pipal` (person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich` (address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG` (organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg` (organisation)
- `48-595/6877` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Gruenleitner Event` — type mismatch — same span as gold: `Gruenleitner Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Damian Wiecher` — partial — pred is substring of gold: `Mag. Damian Wiecher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

**False Positives:**

- `Linn Förstle` — partial — pred is substring of gold: `Hon.-Prof. Linn Förstle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Linn Förstle`(person)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich`(address)
- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Tamara Poertgen` — partial — pred is substring of gold: `Tamara Poertgen, LLB Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Babette Nimzyk`(person)
- `Tamara Poertgen, LLB Bakk. techn.`(person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes`(organisation)
- `08-216/2001`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dominika Oehlerich` — partial — pred is substring of gold: `Dominika Oehlerich, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Dominika Oehlerich, BEd`(person)
- `Zamberg 9, 3843 Hohenau, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Clemens Mooß` — partial — pred is substring of gold: `Hon.-Prof. Clemens Mooß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `Hon.-Prof. Clemens Mooß`(person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich`(address)
- `PROCURA Steuerberatung  GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)
- `62-757/0278`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Simone Zemanek` — partial — pred is substring of gold: `Simone Zemanek, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `Simone Zemanek, MSc`(person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `15-763/9594`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Eleonore Sawadzki` — partial — pred is substring of gold: `Eleonore Sawadzki, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Thassilo Wedekinn` — partial — pred is substring of gold: `Mag. Thassilo Wedekinn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Mag. Thassilo Wedekinn`(person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich`(address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Florens Weißer` — partial — pred is substring of gold: `Dr. Florens Weißer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hugo Pietzak`(person)
- `Dr. Florens Weißer`(person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)
- `09-64-114/4837`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wigand Maczkiewicz` — partial — pred is substring of gold: `Wigand Maczkiewicz, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Sven Weichmann` — partial — pred is substring of gold: `Mag. Sven Weichmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Mag. Sven Weichmann`(person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich`(address)
- `Mag. Kurt Kreith`(person)
- `Finanzamtes Baden  Mödling`(organisation)
- `78-738/0573`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Bettina Domigall` — partial — pred is substring of gold: `Bettina Domigall, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Mag. Susanne Haim`(person)
- `Mag Stefan Raab`(person)
- `Leopold Pichlbauer`(person)
- `Bettina Domigall, Bakk. iur.`(person)
- `Zickhöhe 66, 3361 Biberbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Tanja Grottenthaler`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Ashley Nagelschmidt` — partial — pred is substring of gold: `Dr. Ashley Nagelschmidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dr. Ashley Nagelschmidt`(person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich`(address)
- `APP Steuerberatung GmbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `16-165/9893`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Priv.-Doz. Timothy Oldenbüttel, Kohlreitweg 2, 4092 Winterhof, Österreich, vertreten durch EHC Wirtschaftstreuhand- gesellschaft m.b.H., Schulgasse 10, 2000  Stockerau, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 5. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Timothy Oldenbüttel` — partial — pred is substring of gold: `Priv.-Doz. Timothy Oldenbüttel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Timothy Oldenbüttel`(person)
- `Kohlreitweg 2, 4092 Winterhof, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Waltraud Pantermühl   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Kindsfater Telekom` — type mismatch — same span as gold: `Kindsfater Telekom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Waltraud Pantermühl`(person)
- `Kindsfater Telekom`(organisation)
- `Pirquethof 3, 8662 Lutschaun, Österreich`(address)
- `SIGNUM Treuhand  Steuerberatungs-GmbH`(organisation)
- `Finanzamt Graz-Stadt`(organisation)
- `11-834/0873`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

**False Positives:**

- `Linus Feyerherdt` — partial — pred is substring of gold: `Ing. Linus Feyerherdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Wieland Starnberg`(person)
- `Ing. Linus Feyerherdt`(person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich`(address)
- `Christina Hildegard Stowasser`(person)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `Finanzamtes Österreich`(organisation)
- `98-011/6615`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz` — partial — pred is substring of gold: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dr. Valerius Somuncu, Seelache 250, 2294 Schloßhof, Österreich, vertreten durch Dr-K, Rechtsanwalt in A, über die Beschwerde vom 22. Dezember  2017 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel  (nunmehr: Finanzamt Österreich) vom 23. November 2017 betreffend Grunderwerbsteuer,  Steuernummer 84-691/1997, Erfassungsnummer 10-2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valerius Somuncu` — partial — pred is substring of gold: `Dr. Valerius Somuncu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Valerius Somuncu`(person)
- `Seelache 250, 2294 Schloßhof, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)
- `84-691/1997`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Delila Holsträter, Bakk. iur. BEd, Ziegelsdorf 25, 4723 Unterhörzing, Österreich, vertreten durch Harald Andreas Rumpler, Mattersburgerstraße 70, 7022 Schattendorf,  über die Beschwerde vom 24. September 2018 gegen den Bescheid des Finanzamtes  Österreich vom 22. August 2018 betreffend Einkommensteuer 2016 Steuernummer  76-140/9765  zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Delila Holsträter` — partial — pred is substring of gold: `Delila Holsträter, Bakk. iur. BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Delila Holsträter, Bakk. iur. BEd`(person)
- `Ziegelsdorf 25, 4723 Unterhörzing, Österreich`(address)
- `Harald Andreas Rumpler`(person)
- `Finanzamtes  Österreich`(organisation)
- `76-140/9765`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/137635.1`) (sent_id: `deanon_BFG_20260814_TEST/137635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Frühmark  in der Beschwerdesache Hon.-Prof. Sven Corbin,  Stalderhaus 7, 9363 Feistritz, Österreich, über die Beschwerde vom 23. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juli 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Juni 2018 bis Jänner 2019, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Sven Corbin` — partial — pred is substring of gold: `Hon.-Prof. Sven Corbin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Valerius Frühmark`(person)
- `Hon.-Prof. Sven Corbin`(person)
- `Stalderhaus 7, 9363 Feistritz, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Stella Isakovitch, MA, Schnell Vorsäß 7, 8241 Kroisbach, Österreich, über die Beschwerde vom 1. Oktober 2019 gegen den Bescheid  des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 24. September 2019  betreffend Familienbeihilfe 01.2019, Steuernummer 67-354/6576  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Stella Isakovitch` — partial — pred is substring of gold: `Stella Isakovitch, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Stella Isakovitch, MA`(person)
- `Schnell Vorsäß 7, 8241 Kroisbach, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `67-354/6576`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jan Jürn  in der Beschwerdesache Armin Klews, Bakk. art.,  Lesach 119, 3071 Untergrafendorf, Österreich, über die Beschwerde vom 28. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 20. April 2022 betreffend Abweisung des Antrages auf Gewährung von  Familienbeihilfe ab Februar 2022 zur Steuernummer 51-609/6898  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Armin Klews` — partial — pred is substring of gold: `Armin Klews, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Jan Jürn`(person)
- `Armin Klews, Bakk. art.`(person)
- `Lesach 119, 3071 Untergrafendorf, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `51-609/6898`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Ing. Nicoletta Papastergios,  Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich  über die Beschwerde vom 12. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 31. März 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 94-528/7027  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Nicoletta Papastergios` — partial — pred is substring of gold: `Ing. Nicoletta Papastergios`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Nicoletta Papastergios`(person)
- `Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `94-528/7027`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ronja Oberth` — partial — pred is substring of gold: `Ronja Oberth, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Hon.-Prof. Justin Jacobeit, Gasthaus Kugelwiese 12, 3841 Markl, Österreich, vertreten durch Schmitt & Schmitt  Wirtschaftstreuhand- gesellschaft m.b.H., Strohgasse 25, 1030 Wien, über die Beschwerde vom  11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 28. April 2022,  Steuernummer 67-100/8891, betreffend Einkommensteuer 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Justin Jacobeit` — partial — pred is substring of gold: `Hon.-Prof. Justin Jacobeit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Justin Jacobeit`(person)
- `Gasthaus Kugelwiese 12, 3841 Markl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `67-100/8891`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Janet Köhle  in der Beschwerdesache der  Textil Bermon, Hans-Bachmann-Straße 4, 2872 Langegg, Österreich  vertreten durch RA-Vertreter, über die Beschwerde vom 31. Mai  2017 gegen die zur Steuernummer 91-124/4580  ergangenen Bescheide des FA St. Johann Tamsweg Zell am See (jetzt  Dienststelle des Finanzamtes Österreich) vom 30. März 2017 betreffend  Einkommensteuer 2009 – 2014 nach Durchführung einer mündlichen Verhandlung am  15.März 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Textil Bermon` — type mismatch — same span as gold: `Textil Bermon`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Janet Köhle`(person)
- `Textil Bermon`(organisation)
- `Hans-Bachmann-Straße 4, 2872 Langegg, Österreich`(address)
- `91-124/4580`(tax_number)
- `FA St. Johann Tamsweg Zell am See`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Leroy Stras` — partial — pred is substring of gold: `Dr. Leroy Stras`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140588.1`) (sent_id: `deanon_BFG_20260814_TEST/140588.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Lerchenfelderstraße 9, 4230 Burbach, Österreich, über die Beschwerde vom 16. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Anspruchszinsen (§ 205  BAO) 2015, Steuernummer 87-149/1701, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Lerchenfelderstraße 9, 4230 Burbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `87-149/1701`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Bodo Adamovic, Bakk. phil., Gantschenbergstraße 24, 4204 Affenberg, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Einkommensteuer 2012  Steuernummer 49-425/9978  beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `Bodo Adamovic` — partial — pred is substring of gold: `Bodo Adamovic, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bodo Adamovic, Bakk. phil.`(person)
- `Gantschenbergstraße 24, 4204 Affenberg, Österreich`(address)
- `Finanzamtes`(organisation)
- `49-425/9978`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Leonie Wehrlin, Bakk. iur., Karl-List-Weg 20, 4222 Frankenberg, Österreich, über die Beschwerde vom 30. Dezember 2021 gegen die Bescheide  des Finanzamtes Österreich vom 30. November 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, 2019 und 2020, Steuernummer 01-053/2123  zu Recht  erkannt:   I. Der Beschwerde wird für die Jahre 2018 im Sinne der Beschwerdevorentscheidung vom  18.2.2022 gemäß § 279 BAO teilweise stattgegeben.

**False Positives:**

- `Leonie Wehrlin` — partial — pred is substring of gold: `Leonie Wehrlin, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Leonie Wehrlin, Bakk. iur.`(person)
- `Karl-List-Weg 20, 4222 Frankenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `01-053/2123`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria Grohe in der Beschwerdesache  Nepomuk Juodvirsis, BSc, Am Römerwall 61, 8451 Muggenau, Österreich, vertreten durch NWT Wirtschaftsprüfung & Steuerberatung GmbH,  Döblinger Hauptstraße 37, 1190 Wien, betreffend Beschwerde vom 11. September 2013 gegen  den Bescheid des Finanzamtes Baden Mödling vom 12. August 2013 betreffend  Forschungsprämie gemäß § 108c EStG 1988 für das Jahr 2012 - Steuernummer  08-697/8586  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs. 4 lit. e BAO als nicht    fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Nepomuk Juodvirsis` — partial — pred is substring of gold: `Nepomuk Juodvirsis, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria Grohe`(person)
- `Nepomuk Juodvirsis, BSc`(person)
- `Am Römerwall 61, 8451 Muggenau, Österreich`(address)
- `NWT Wirtschaftsprüfung & Steuerberatung GmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `08-697/8586`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hademar Haßelbach` — partial — pred is substring of gold: `Hademar Haßelbach, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Wilfried Brokof`(person)
- `Hademar Haßelbach, BSc`(person)
- `Engerbergstraße 2, 8642 Nechelheim, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `59-681/6477`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

**False Positives:**

- `Heinrich Rzeppa` — partial — pred is substring of gold: `Heinrich Rzeppa, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Heinrich Rzeppa, LLM`(person)
- `Toulagasse 1, 8111 Straßengel, Österreich`(address)
- `Dr. Martin Weiser`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `52-580/0972`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Volkmar Bauernschmid` — partial — pred is substring of gold: `Volkmar Bauernschmid, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Volkmar Bauernschmid, MBA`(person)
- `Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich`(address)
- `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`(organisation)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `78-200/9325`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/143660.1`) (sent_id: `deanon_BFG_20260814_TEST/143660.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat in der Beschwerdesache  des Beschwerdeführers Bernadette Steinhaeuser, Trujegasse 56, 9853 Landfraß, Österreich, Steuernummer: 24-095/9600,  betreffend die Beschwerde vom 28. Oktober 2022 gegen die Bescheide des Finanzamtes  Österreich vom 26. September 2022 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2015, vom 27. September 2022 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2016 und vom 30. September 2022 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017 und 2018 den  Beschluss:    I)

**False Positives:**

- `Beschwerdeführers Bernadette Steinhaeuser` — partial — gold is substring of pred: `Bernadette Steinhaeuser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Bernadette Steinhaeuser`(person)
- `Trujegasse 56, 9853 Landfraß, Österreich`(address)
- `24-095/9600`(tax_number)
- `Finanzamtes  Österreich`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/144133.1`) (sent_id: `deanon_BFG_20260814_TEST/144133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Farina Solovieva  in der Beschwerdesache der  Folmer Sanitär, Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich, über die Beschwerde vom 27. Oktober 2022 gegen den Bescheid  des FA Bruck Eisenstadt Oberwart  vom 14. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 06-556/2153  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Folmer Sanitär` — type mismatch — same span as gold: `Folmer Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Farina Solovieva`(person)
- `Folmer Sanitär`(organisation)
- `Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich`(address)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `06-556/2153`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/144714.1`) (sent_id: `deanon_BFG_20260814_TEST/144714.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Tamara Sokol  in der Beschwerdesache der  Heinrich Heckt, Manhartsbergstraße 16, 2326 Maria-Lanzendorf, Österreich, über die Beschwerde vom 19. September 2022 gegen den  Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 23. August 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 87-623/8682  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Heinrich Heckt` — type mismatch — same span as gold: `Heinrich Heckt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Tamara Sokol`(person)
- `Heinrich Heckt`(organisation)
- `Manhartsbergstraße 16, 2326 Maria-Lanzendorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `87-623/8682`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145929.1`) (sent_id: `deanon_BFG_20260814_TEST/145929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria Luise Wohlmayr in der  Beschwerdesache Oskar Bökelheide, MBA, Josef Missongasse 4, 5112 Gresenberg, Österreich, über die Beschwerde vom 27. September 2023  gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023 betreffend  Einkommensteuer 2022 Steuernummer 05-857/8790  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Oskar Bökelheide` — partial — pred is substring of gold: `Oskar Bökelheide, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria Luise Wohlmayr`(person)
- `Oskar Bökelheide, MBA`(person)
- `Josef Missongasse 4, 5112 Gresenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `05-857/8790`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Huberta Maginot  in der Beschwerdesache der  Wolensky Logistik, Knödelhütte 10, 9462 St. Peter im Lavanttal, Österreich, über die Beschwerde vom 10.Okt.2022, eingebracht am  12. Oktober 2022, gegen den zur Steuernummer 61-790/6327  ergangenen Bescheid des  Finanzamt Spittal Villach  vom 14. September 2022 betreffend Abweisung eines Antrages auf  Wiederaufnahme (§ 303 BAO) des Einkommensteuerbescheides 2018 vom 29.Jän 2020 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wolensky Logistik` — type mismatch — same span as gold: `Wolensky Logistik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Dr.in Huberta Maginot`(person)
- `Wolensky Logistik`(organisation)
- `Knödelhütte 10, 9462 St. Peter im Lavanttal, Österreich`(address)
- `61-790/6327`(tax_number)
- `Finanzamt Spittal Villach`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Piedro Ringelsbacher, BEd, Hollehnerweg 53, 2565 Schwarzensee, Österreich, über die Beschwerde vom 30. August 2023 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 6, Referat Parkometerabgabe und  Abgabenstrafen, vom 11. August 2023 betreffend Parkometerabgabe zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Piedro Ringelsbacher` — partial — pred is substring of gold: `Piedro Ringelsbacher, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Lisa Fries`(person)
- `Piedro Ringelsbacher, BEd`(person)
- `Hollehnerweg 53, 2565 Schwarzensee, Österreich`(address)
- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Univ.-Prof. Julian Czernitzki, Faßlergasse 78L-80, 9612 Dellach, Österreich, vertreten durch Schneider Wirtschaftsprüfung und  Steuerberatung GmbH, 6845 Hohenems, Nibelungenstraße 19, über die Beschwerde vom  19.04.2019 gegen die Körperschaftsteuerbescheide 2014, 2015, 2016, gegen die  Umsatzsteuerbescheide 2014, 2015, 2016 (alle Bescheide vom 25.03.2019), gegen die  Bescheide über die Festsetzung von Umsatzsteuer für 12/2017 und 12/2018 vom jeweils  25.03.2019 (Umsatzsteuerbescheid 2017 vom 22.05.2020 und Umsatzsteuerbescheid 2018  vom 17.10.2023), sowie gegen die Haftungsbescheide Kapitalertragsteuer 01/2014, 12/2014,  12/2015, 12/2016 und 12/2017 (Bescheide jeweils vom 21.03.2019), zu Recht erkannt:  I. Der Beschwerde gegen die Körperschaftsteuerbescheide 2015 und 2016, die  Umsatzsteuerbescheide 2015, 2016, 2017 und 2018 wird Folge gegeben.

**False Positives:**

- `Julian Czernitzki` — partial — pred is substring of gold: `Univ.-Prof. Julian Czernitzki`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Univ.-Prof. Julian Czernitzki`(person)
- `Faßlergasse 78L-80, 9612 Dellach, Österreich`(address)
- `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_1`)


IM NAMEN DER REPUBLIK   Das BFG hat durch die Richterin *** in der Beschwerdesache der Beschwerdeführerin, mit  Adresse X, vertreten durch Dr. Wolfgang Schimek Rechtsanwalt GMBH, Graben 42, 3300  Amstetten, über die Beschwerde vom 23. Juli 2020 gegen die Bescheide des FA Graz-Stadt  (nunmehr Finanzamt Österreich) betreffend die Festsetzung der   Normverbrauchsabgabe 5/2018 und   Kraftfahrzeugsteuer für die Zeiträume 4-12/2018, 1-12/2019 und 1-3/2020   jeweils vom 25. Juni 2020 nach Durchführung einer mündlichen Verhandlung am 12.2.2025 in  Anwesenheit der Schriftführerin SF zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Dr. Wolfgang Schimek Rechtsanwalt GMBH,`(organisation)
- `FA Graz-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Hotterweg 4, 5142 Hitzging, Österreich, über die Beschwerde vom 27. Oktober 2023 gegen den  Bescheid des Finanzamtes Österreich vom 6. Oktober 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 47-043/9413, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Hotterweg 4, 5142 Hitzging, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `47-043/9413`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_1`)


IM NAMEN DER REPUBLI K  A) Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Olga Kendziora, Bakk. rer. nat. (Beschwerdeführerin, abgekürzt: Bf.), Im Biofeld 5, 6650 Gramais, Österreich  vertreten  durch Stb1, AdrStb1, über die Beschwerde der Bf. vom 16. März 2017 gegen folgende  Bescheide des Finanzamtes Wien99 (ursprünglich belangte Behörde) zu Steuernummer  56-003/0284    Umsatzsteuerbescheid 2014 vom 23. September 2016,   Körperschaftsteuerbescheid 2014 vom 23. September 2016,   Bescheid über die Festsetzung von Anspruchszinsen 2014 vom 23. September 2016,   Haftungsbescheid für den Zeitraum 2014 betreffend Kapitalertragsteuer vom  22. September 2016,   Körperschaftsteuervorauszahlungsbescheid 2016 vom 23. September 2016,  nach Durchführung der beantragten mündlichen Verhandlung am 25. April 2025 in  Anwesenheit des Schriftführers F  a) zu Recht erkannt:  Der Beschwerde wird, soweit sie gegen den Körperschaftsteuerbescheid 2014 vom  23. September 2016 gerichtet ist, Folge gegeben.

**False Positives:**

- `Olga Kendziora` — partial — pred is substring of gold: `Olga Kendziora, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Olga Kendziora, Bakk. rer. nat.`(person)
- `Im Biofeld 5, 6650 Gramais, Österreich`(address)
- `Finanzamtes`(organisation)
- `56-003/0284`(tax_number)

</details>

---

## `legal_person_honorific_context` 🏆

**F1:** 0.116 | **Precision:** 0.632 | **Recall:** 0.064  

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
| 0.632 | 0.064 | 0.116 | 163 | 103 | 60 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 103 | 60 | 1511 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_8`)


Frau Basyurt erzielt selber keinerlei Einkünfte, auch keine (ausländischen) Kapitaleinkünfte.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_12`)


Der Familienwohnsitz ist in A1.  Pkw:Frau Basyurt benützt den Range Rover Sport, s. beiliegenden Zulassungsschein, dieser steht ihr  tagtäglich zur Verfügung.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)


Frau Basyurt wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |
| `Basyurt` | `Basyurt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_132`)


Ich war schon bei Frau Beerenbrock  da wurde mir gesagt, ich  brauche keine Befunde.

| Predicted | Gold |
|---|---|
| `Beerenbrock` | `Beerenbrock` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_36`)


Im Ermittlungsverfahren wurde bekannt gegeben, dass das Fahrzeug Herrn Vera Schliephacke  überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Unverdroß` (person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Mag. Peter  Mayerhofer` (person)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |
| `Stavrakis` | `Stavrakis` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |
| `Ruckelshaußen` | `Ruckelshaußen` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_45`)


Nach Antwort von Herrn Ruckelshaußen vom 04.08.2015 betreffend  „asymmetrische Arrondierung und Immo-Est-Befreiung“ kommt im wörtlichen Sinne die  Befreiungsbestimmung des § 30 Abs 2 Z 4 EStG immer für denjenigen zur Anwendung, bei dem  ein Grundstückstausch einen Flurbereinigungsvorgang darstellt. Wenn für einen Tauschpartner  eine Flurbereinigung gegeben ist (und auch ein Tausch und keine Veräußerung vorliegt - dh  keine Aufzahlungen über 50%), dann greift für diesen die Befreiung, wohingegen der andere  Tauschpartner steuerpflichtig ist.

| Predicted | Gold |
|---|---|
| `Ruckelshaußen` | `Ruckelshaußen` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

| Predicted | Gold |
|---|---|
| `Bernett` | `Bernett` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_8`)


Mit fristgerechter E-Mail vom 13. März 2021 (Anhang: Lenkerauskunft) nannte die  Zulassungsbesitzerin Herrn Bodewein als jene Person, der das genannte Kraftfahrzeug zum  Beanstandungszeitpunkt überlassen war.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_11`)


Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2  Wiener Parkometerabgabeverordung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 wurde  über Herrn Bodewein eine Geldstrafe iHv € 60,00 und für den Uneinbringlichkeitsfall eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_14`)


Mit Schreiben des Magistrates der Stadt Wien, MA 67 vom 21. April 2021  (Verfahrensanordnung – Nachreichung Unterschrift bzw. Vollmachtsvorlage) wurde die Firma  X_KG zur Vorlage einer Vollmacht, aus welcher das Vertetungsverhältnis zu Herrn Bodewein sowie die  Berechtigung zur Einbringung des Rechtsmittels hervorgehe, binnen zwei Wochen nach  Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_16`)


Der Magistrat der Stadt Wien, MA 67, erließ an Herrn X einen mit 10. Mai 2021 datierten  Bescheid, mit welchem der Einspruch vom 21.03.2021 gegen die an Herrn Bodewein gerichtete  Strafverfügung vom 16.03.2021 infolge der Nichtvorlage der Vollmacht gemäß § 13 Abs. 3 AVG  als unzulässig zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)


Herr Bodewein brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `BFG` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_39`)


Erst ein Telefonat zwischen Magistrat der Stadt Wien und Herrn Bodewein hat ergeben, dass es sich  um beim Anbringen vom 15. September 2021 um eine Beschwerde handeln solle.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)


Für Herrn Bodewein geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_26`)


Im Vorlageantrag wird ausgeführt:  „Herr B ist nach Angaben meines Mandanten erst im Sommer 2013 nach Österreich gekommen  und war ausschließlich für Herrn Mathusczyk tätig.

| Predicted | Gold |
|---|---|
| `Mathusczyk` | `Mathusczyk` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_38`)


Mit Aktenvermerk vom 20. April 2023 hielt die Magistratsabteilung 67 zur gegenständlichen  Geschäftszahl fest, ein Telefonat mit PÜG Dienstführung 1,Herr Mayerer (DW TelNr) habe  ergeben, das Überwachungsorgan DNr. ANr habe am Beanstandungstag (10.11.2022) im 22.

| Predicted | Gold |
|---|---|
| `Mayerer` | `Mayerer` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_142`)


Soweit der Bf. darauf verweist, dass Herr Abersfeller aus Gewerbebetrieb  erzielt bzw bei der SVA pflichtversichert sei, mag zwar richtig sein, ist aber bedeutungslos:  Aufgrund des funktionalen Verständnisses des Begriffes der Eingliederung gemäß der zitierten  Judikatur des VwGH ist es ohne Bedeutung, in welcher Weise die aus der Tätigkeit erzielten  Einkünfte zu qualifizieren wären;

| Predicted | Gold |
|---|---|
| `Abersfeller` | `Abersfeller` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

| Predicted | Gold |
|---|---|
| `Theodora Berenwinkel` | `Theodora Berenwinkel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Klam 26, 8673 Steinhöf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)


Sie sehen im Anhang dass Herr Abeles damit bis 27 Dezember  gefahren ist.

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)


Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr Abeles bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)


Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn Schwent gelenkt wurde.

| Predicted | Gold |
|---|---|
| `Schwent` | `Schwent` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_144`)


Zur Begründung der fristgerechten Einbringung der Beschwerde wurde im  Vorlageantrag ausgeführt, die Mitarbeiterin,Frau Pöttmann  habe die Beschwerde am 30. April 2018  um ca. 17:30 Uhr persönlich in den Briefkasten des Finanzamtes eingeworfen und diese  Erledigung auch im Postbuch vermerkt.

| Predicted | Gold |
|---|---|
| `Pöttmann` | `Pöttmann` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_3`)


Begründung  Am 22.03.2024 erließ das Finanzamt für Frau Günter Salfetter, Beschwerdeführerin, einen  Einkommensteuerbescheid (Arbeitnehmerveranlagung) für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `Günter Salfetter` | `Günter Salfetter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


Entscheidungsgründe  Nach dem das Finanzamt in der Beschwerdevorentscheidung (BVE) vom 17.11.2023 das  Pendlerpauschale, den Pendlereuro und den Alleinerzieherabsetzbetrag antragsgemäß  steuermindernd berücksichtigt hat, ist nur mehr strittig, ob sogenannte Familienheimfahrten  von Frau Kuehnhanss (in der Folge: Beschwerdeführerin: Bf) vorliegen und als Werbungskosten zu  berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Kuehnhanss` | `Kuehnhanss` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_14`)


Herr Kaspar Sadowski  führt ab 1.1.2018 den Betrieb „Unternehmensberatung" - der zuvor von der **  GMBH geführt wurde - nun mehr als Einzelunternehmung Kaspar Sadowski  weiter.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)


Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn Kaspar Sadowski  wieder als aktiv gemeldet.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_20`)


Da Herr Kaspar Sadowski  immer  Alleingesellschafter der ** GMBH war, ist der Übergang des Verlustvortrages mit 100 %  vorzunehmen.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Frau Christina Schwabendissen, Beschwerdeführerin, reichte ihre Erklärung zur Arbeitnehmerveranlagung  2015 am 7.12.2020 am Finanzamt ein.

| Predicted | Gold |
|---|---|
| `Christina Schwabendissen` | `Christina Schwabendissen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_28`)


Betreffend die Baurechtseinlage EZ 2 KG XY) wurde mit Schreiben vom 5.4.2017 von Notar Herr  Mag. Z die Befreiung gemäß § 3 Abs. 1 Z 2 GrEStG (damals fälschlicherweise die Befreiung  gemäß § 3 Abs. 1 Z 3 GrEStG bezeichnet) beantragt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Z`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Z`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)
- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_17`)


Herr Bf benützt für seine Wochenendfahrten nach A1 einen anderen Pkw.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_18`)


Herr Bf-Gatte ist während der Woche in D-XY whft und in A1 nicht gemeldet;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Basyurt`(person)
- `Basyurt`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_18`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat seinen Familienwohnsitz gemeinsam mit seinen Kindern (im Beschwerdejahr 8 und  12 Jahre alt) in Ungarn, wo weder er noch seine Frau Einkünfte erzielen.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_100`)


Lebensjahr, dies wurde in dem  Gutachten von Frau Dr. 2 zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem  nicht attestiert.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_131`)


Lebensjahr, dies wurde in dem Gutachten von Frau Dr. 2  zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem nicht attestiert....  Derzeitige Beschwerden:  Die Antragstellerin gibt an: "Ich habe das gleiche seit meiner Jugend, das sind Panikattacken,  Kopfschmerzen und eine Sozialphobie.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_68`)


Herr Dr. YYY hat das Fahrzeug am Morgen diesen Tages in der STRASSE-Hauptwohnsitz  übernommen und mitgeteilt, dass er einige Tage nach Ungarn fahren wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)


ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn Dr. YYY übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_149`)


Herr  Dr. YYY ist für Ärzte ohne Grenzen tätig.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_150`)


Herr Dr. YYY hat mich nach einem schweren  Insektenbiss in GEBIET, mit Lebensgefahr für mich, hervorragend behandelt. Darauf gründet  sich die Freundschaft.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_151`)


Herr Dr. YYY arbeitet in Gebieten, wo kein Mobilfunknetz vorhanden ist.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_385`)


Herr Dr. YYY arbeite in Gebieten, wo kein  Mobilfunknetz vorhanden sei.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_67`)


Unstrittig war, dass die Gesellschafter-Geschäftsführerin, Frau Ges-Gf, mit 25,25% im Sinne des  § 22 Z 2 zweiter Teilstrich EStG 1988 an der Bf. wesentlich beteiligt war.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Unverdroß  Behindertenbetreuerin` — partial — gold is substring of pred: `Unverdroß`
- `Prim` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_122`)


Herr Bf ist im Wesentlichen in der Lage, einfache Sachverhalte zu erfassen, zeigt sich bei  komplexeren Anforderungen allerdings überfordert.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_72`)


Am 26.1.2018 (am Tag danach) seien zwei Poststücke per Einschreiben mit den  Aufgabenummern RQ … 747 und 748 versendet worden, die von Herrn Mag. Sch. auf dem  Nachhauseweg beim Postamt W. aufgegeben worden seien.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. G`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `74-872/6854`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_26`)


Am 12. Oktober 2021 nahm der Magistrat der Stadt Wien folgenden  Aktenvermerk zum Akt: „Laut Telefonat … mit Herrn Hon.-Prof. Reinhard Bodewein  sind seine Schreiben anlässlich  den Erhalt der Vollstreckungsverfügung als Beschwerde zu sehen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Reinhard Bodewein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Hon.-Prof. Reinhard Bodewein`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_35`)


Zusätzlich  sei der Beschwerdeführerin unbedingt empfohlen worden, die OP von Herrn Dr. B einem  anerkannten Schulterspezialisten ausführen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_36`)


Herr Dr. B würde nur im KH der  Diakonissen operieren;

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_58`)


Die streitgegenständliche Operation wurde schließlich in der Klinik Diakonissen Linz von Herrn  Dr. B durchgeführt (stationärer Aufenthalt von 15.5. bis 20.5.2019).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)


Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  MH-Bau GmbH am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_19`)


Zum  Masseverwalter wurde Herr Mag. G H bestellt.  Gesellschafter der AB sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer waren  Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)


Die von Herrn Ing. Priv.-Doz.in Linda Schleglmilch zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Priv.-Doz.in Linda Schleglmilch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Priv.-Doz.in Linda Schleglmilch`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_20`)


Nach den Angaben von Herrn Dr. F sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_22`)


In einer Besprechung vom 16.1.2015 hat Herr Dr. F zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_23`)


Weiter hat Herr Dr. F angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_24`)


Mit Mail vom 9.2.2015 teilt Herr Dr. F dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

**False Positives:**

- `Amtsdirektor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Kohlfürst`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Mehmet Köprücü  Vollmacht` — similar text (different position): `Mehmet Köprücü`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)
- `Zollamt`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)
- `Quentin Schwartkopp`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_36`)


Herr Sohn wurde zwischenzeitlich gemäß § 62 AlKStG als Abfindungsberechtigter  registriert.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_40`)


Unter Hinweis auf §§ 2 Abs. 1, 4 Abs. 2 Z 5, 8 Abs. 1 Z 2, § 9 Abs. 1 Ziffer 2, § 62 Abs. 2 Z 3, 64  Abs. 3 AlkStG betonte das Zollamt, dass durch den Übergabevertrag vom eee2011 Herr Sohn  unzweifelhaft Eigentümer an den Früchten (= alkoholbildende Stoffe) wurde; auf mündliche  Absprachen zwischen Vater und Sohn komme es nicht an.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_81`)


Herr Sohn hat seit 03.bbb.2013 seinen aktuellen  ordentlichen Wohnsitz (Hauptwohnsitz) in Adresse_Sohn.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_88`)


Wie das Zollamt auch zu diesem Beschwerdepunkt ausführlichst und zu Recht betont hat,  wurde mit der Übergabe im Jahr 2011 der Übernehmer der Liegenschaft, Herr Sohn, auch  Eigentümer an den darauf befindlichen Obstbäumen und an deren Früchte.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_64`)


Termin & Dauer   Montag, 04.05.2020 - Mittwoch, 25.05.2022   Laufender Einstieg möglich     Abschlussbericht TeilnehmerInnen:   Kurs: Tourismuscenter-Aufbaumodul 2 von: 17.05.2021 bis 30.07.2021   Name TeilnehmerIn: [Sohn des Bf.]     Arbeitsaufnahme während des Kurses    X Kursabbruch aus anderen Gründen   …   Anmerkungen allgemein:   Herr (Sohn des Bf.) hat aufgrund immer wiederkehrender Krankenstände die erforderlichen  Anwesenheitszeiten nicht erfüllt, daher wurde der Kurs abgebrochen.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_65`)


Es wird dringend  empfohlen, dass Herr (Sohn des Bf.) seine gesundheitlichen Probleme klärt bevor er wieder in  eine Maßnahme gebucht wird und ob aus gesundheitlichen Gründen die Berufswahl die  Richtige ist.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_108`)


Im erwähnten Straferkenntnis vom  7.11.2022 hat die belangte Behörde diese Ermittlungsergebnisse auch wiedergegeben und  dazu auszugsweise wie folgt ausgeführt:  „Ermittlungen ergaben, dass für Herrn Rudolf B kein Ausweis gemäß § 29b StVO ausgestellt  wurde.

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_110`)


……  Im Übrigen ist auch der lt. Anzeigeangaben im Fahrzeug nicht gut erkennbar hinter der  Windschutzscheibe eingelegte Parkausweis gemäß § 29b StVO, dessen Ausweisnummer  teilweise durch eine Postkarte verdeckt war, nicht für Herrn Rudolf B ausgestellt.“

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_280`)


Dieses Produkt hat Herr Dr. B nicht verschrieben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_304`)


Herr Dr. T ist ein Arzt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)


Demnach hätte Herr Dipl.-Ing. Heinz Riechels  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_277`)


Die Angaben von Herrn Baumeister Y X werden nicht zur Sachverhaltsfeststellung  herangezogen, weil sie nach der hier vertretenen Auffassung nicht relevant sind und jedenfalls  unzuverlässig sind, wie auch im Detail in Abschnitt 14 dargestellt wird.

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_289`)


Zum Beweisantrag:  Herr Baumeister Y X war von 3. Oktober 2013 bis 7. November 2016 gewerberechtlicher  Geschäftsführer der e GmbH (vgl. BFG-Akt I Bl. 56b).

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/141421.1`) (sent_id: `deanon_BFG_20260814_TEST/141421.1_69`)


T widme ihre Zeit auch dem  Lernen, Lesen von Klassenlektüre und Schreiben von Portfolios.

**False Positives:**

- `Portfolios` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1091, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie **Dr. Franz Kandlhofer**  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

- missed: `Dr. Franz Kandlhofer` (person)
- predicted in sentence: `Christina Tiebout`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)

Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater **Dr. Mersch** 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

- missed: `Dr. Mersch` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache **Univ.-Prof.in KzlR Tiffany Nowakowsky**,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Univ.-Prof.in KzlR Tiffany Nowakowsky` (person)
- predicted in sentence: `Mag. Priv`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)

Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache **Hon.-Prof.in Techn R Huberta Pauwels**,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

- missed: `Hon.-Prof.in Techn R Huberta Pauwels` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_23`)

Weiter hat Herr **Dr. F** angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

- missed: `Dr. F` (person)
- predicted in sentence: `Dr`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  **VetR Dipl. Kff. Ingrid Klockgiesser**, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

- missed: `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- predicted in sentence: `Mag. Peter Bilger`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)

Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die **PhD Mag. Heinrich Hambücher**  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

- missed: `PhD Mag. Heinrich Hambücher` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Verwaltungsstrafsache gegen  **Heidrun Engehausen**, Weinzierlstraße 31, 2292 Engelhartstetten, Österreich, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  über die Beschwerde vom 13. Oktober 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67- Parkraumüberwachung, als Abgabenstrafbehörde vom  18. September 2020, Zahl: MA67/Zahl1/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Heidrun Engehausen` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende **Dr. Anna Radschek**, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Anna Radschek` (person)
- predicted in sentence: `Kira Lentze`

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)

LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin **Dr. Mairinger** 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

- missed: `Dr. Mairinger` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_133`)

Bei **Dr. 2** war ich auch, die mir die Befunde nicht mehr zurückgeben  wollte.

- missed: `Dr. 2` (person)
- predicted in sentence: —

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_5`)

Das Einkommen des Gruppenmitgliedes **Cathleen Gottschlag**  im Jahr 2016 wird mit -189.109,60 Euro  (Verlust) festgesetzt.

- missed: `Cathleen Gottschlag` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_42`)

Dipl. Ing. B sei täglich an den Standorten W sowie Z anwesend gewesen und habe sich operativ  um die Durchführung der Geschäftsführeragenden gekümmert, während Dipl. **Ing.Ing. Bertram Hennlein** in  diese Tätigkeiten so gut wie gar nicht eingebunden gewesen sei.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)

Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - **Prof. Dr. Franz Leidenmühler**" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

- missed: `Prof. Dr. Franz Leidenmühler` (person)
- predicted in sentence: `Mag`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_163`)

Angewandte Mathematik (schriftlich)   genügend   Wirtschaftsinformatik (mündlich)    befriedigend     Sommertermin Mai 2023:   Diplomarbeit     Herbsttermin Oktober 2024:   Diplomarbeit   „… **Luna Schaffrath** (hat) die Diplomarbeit zur Reife- und Diplomprüfung am 06.09.2024  abgegeben … und am 15.10.2024 positiv abgeschlossen“ (Bestätigung vom 11.04.2025).

- missed: `Luna Schaffrath` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_50`)

**Dr. Omasits** sei in Pension.

- missed: `Dr. Omasits` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Dr. Susanne Zankl** in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

- missed: `Dr. Susanne Zankl` (person)
- predicted in sentence: `Bertha Unverich`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache **Techn R RgR Jeffrey Geippel**, Dirisam 63, 2813 Pregart, Österreich, über die Beschwerde vom 3. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 2. Mai 2022 betreffend Einkommensteuer 2019  Steuernummer 84-874/5640  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Techn R RgR Jeffrey Geippel` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_60`)

In den Jahren 2014-2020 seien auch alle Jahresabschlüsse vom alleinigen  Gesellschafter-Geschäftsführers Dipl. **Ing.Ing. Bertram Hennlein** unterzeichnet worden.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache **Priv.-Doz.in Laura Fromader**,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Priv.-Doz.in Laura Fromader` (person)
- predicted in sentence: `Hon.-Prof. Hagen Atar`

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_14`)

Das Finanzamt Österreich begründete diese Vorgehensweise dergestalt, dass der  Familienbonus Plus für das Kind OStR Priv.-Doz. Theodor Voelpel  hinsichtlich der Monate September bis  Dezember sowie für das Kind **Herbert Schaffarik**  hinsichtlich der Monate August bis Dezember  zustehe.

- missed: `Herbert Schaffarik` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_176`)

Zudem wurde vom Erstgutachter DI **Bodo Meßmacher** ausgeführt, dass die Kosten für den Umbau- und Sanierungsarbeiten zur Verwertung des Gebäudeteils in der Pf. von ihm mit 75.000 Euro geschätzt werden.

- missed: `Bodo Meßmacher` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  **Basil Vanak**, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

- missed: `Basil Vanak` (person)
- predicted in sentence: `Mag. Dieter Fröhlich`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  **Mag. Sonja Stradner** sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Sonja Stradner` (person)
- predicted in sentence: `Kira Lentze`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache **Hademar Haßelbach, BSc**,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hademar Haßelbach, BSc` (person)
- predicted in sentence: `Mag. Hon`, `Hademar Haßelbach`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag.Dr. Thomas Leitner** in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Mag.Dr. Thomas Leitner` (person)
- predicted in sentence: `Janis Dührkopp`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch **Mag. András Péter Radics**, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. András Péter Radics` (person)
- predicted in sentence: `Nadine Tomczack`

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Dr. Maria Grohe** in der Beschwerdesache  Nepomuk Juodvirsis, BSc, Am Römerwall 61, 8451 Muggenau, Österreich, vertreten durch NWT Wirtschaftsprüfung & Steuerberatung GmbH,  Döblinger Hauptstraße 37, 1190 Wien, betreffend Beschwerde vom 11. September 2013 gegen  den Bescheid des Finanzamtes Baden Mödling vom 12. August 2013 betreffend  Forschungsprämie gemäß § 108c EStG 1988 für das Jahr 2012 - Steuernummer  08-697/8586  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs. 4 lit. e BAO als nicht    fristgerecht eingebracht zurückgewiesen.

- missed: `Dr. Maria Grohe` (person)
- predicted in sentence: `Nepomuk Juodvirsis`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_3`)

Das Einkommen des Gruppenmitgliedes **Cathleen Gottschlag**  im Jahr 2014 wird mit 2.678.126,39 Euro  festgesetzt.

- missed: `Cathleen Gottschlag` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_41`)

des Neve College for Woman nicht in Israel aufgehalten habe) nicht widersprochen, weshalb  die durchgehende Anwesenheit von **Heidemarie Fitzenreiter**  in Israel für Zwecke des College-Besuches  vom Bundesfinanzgericht als erwiesen angenommen wird.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_28`)

Nach VwGH 2.7.2002, 98/14/0223, entfaltet ein an „**Dr. A** und Mitges, zHd des Vertreters iSd  § 81“ zugestellter Bescheid, der keinen Hinweis nach § 101 Abs. 3 BAO enthält, in seinem  Abspruch über die Feststellung (bzw. das Unterbleiben einer Feststellung) von Einkünften nach  § 188 BAO im Hinblick auf das durch die Einheitlichkeit einer solchen Feststellung geprägte  Wesen insgesamt keine Wirkung (vgl.  Ritz, BAO6, § 101 Rz. 9, und die dort zitierte Judikatur).

- missed: `Dr. A` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_2`)

Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Rupert Wedell  in der Beschwerdesache **OStR OMedR Rebecca Ehrmanntraut**,  Museumplatz 27, 8241 Rohrbachschlag, Österreich, über die Beschwerden vom 10. Oktober 2017 gegen die Bescheide des  FA Baden Mödling  vom 27. Juni 2017 bzw. 10. Juli 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 bis 2015, Steuernummer 38-848/8801, zu Recht erkannt:  I. Den Beschwerden gegen die Bescheide betreffend Einkommensteuer für die Jahre 2012 bis  2015 wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `OStR OMedR Rebecca Ehrmanntraut` (person)
- predicted in sentence: `Hon.-Prof. Rupert Wedell`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie **Mag. Martin Saringer** und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Martin Saringer` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Dr. Katrin Allram in der Beschwerdesache  **VetR Dipl. Kfm. Gernot Kurtius**, Oberassling 20, 3921 Schmerbach, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des  Finanzamtes Gänserndorf Mistelbach vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `VetR Dipl. Kfm. Gernot Kurtius` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des **Günter Gopfauf**, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

- missed: `Günter Gopfauf` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147139.1`) (sent_id: `deanon_BFG_20260814_TEST/147139.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **MMag. Gerald Erwin Ehgartner** in der  Beschwerdesache Herta Gulacsi, über die Beschwerde vom 3. Jänner 2024 gegen den Bescheid des  Finanzamtes Österreich vom 6. Dezember 2023 betreffend Einkommensteuer 2021 nach  Durchführung einer mündlichen Verhandlung am 3. Februar 2025 in Anwesenheit des  Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `MMag. Gerald Erwin Ehgartner` (person)
- predicted in sentence: `Herta Gulacsi`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Merlin Morkam**  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `Hon.-Prof.in Merlin Morkam` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_36`)

Dass **Heidemarie Fitzenreiter**  vom 05.09.2022 bis 31.05.2023 Studentin des Neve College for Woman  (Jerusalem) gewesen ist, ergibt sich aus der im Akt befindlichen Bestätigung des Neve College  for Woman vom 25.06.2023 (Anmerkung: Ursprünglich war offenbar ein Besuch des Neve  College for Woman bis 14.06.2023 geplant, was sich aus einer ebenfalls aktenkundigen, am  19.09.2022 vom Neve College for Woman ausgestellten Bestätigung ergibt).

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)

in der Verwaltungsstrafsache gegen  **Detlev Griessmer**, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

- missed: `Detlev Griessmer` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Renate Schohaj** in der Verwaltungsstraf- sache gegen Sandra Massin, Grub-Mallinger-Straße 6, 4782 Bubing, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 27. Februar 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. Jänner 2023, GZ.  MA67/226701097306/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 36,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 8 Stunden herabgesetzt  wird.

- missed: `Mag. Renate Schohaj` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142998.1`) (sent_id: `deanon_BFG_20260814_TEST/142998.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag.Dr. Thomas Leitner** in der  Beschwerdesache Evelyn Schlessing, Koksbatteriestraße 7, 9560 Bichl, Österreich  vertreten durch Univ.Prof.i.R. Dr. Josef Werndl,  über die Beschwerde vom 27. Dezember 2022 gegen den Bescheid des Finanzamtes Österreich  vom 15. Dezember 2022 betreffend Einkommensteuer 2021 zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

- missed: `Mag.Dr. Thomas Leitner` (person)
- predicted in sentence: `Evelyn Schlessing`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  **Prof.in Alma Siegers**, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Prof.in Alma Siegers` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_87`)

Sozialanamnese:  Ausbildung: HAK-Matura, Untauglichkeit bei der Stellung 12/1980 (Nervosität, **M.** Schermann),  BWL-Studium nicht abgeschlossen, bisher keine Erwerbstätigkeit.

- missed: `M.` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Serena Weidlich**  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Hon.-Prof.in Serena Weidlich` (person)
- predicted in sentence: `Ruprecht Pesselt`

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Diana Sammer** über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

- missed: `Mag. Diana Sammer` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Helena von Heyl**  in der Beschwerdesache des  Charlotte Buckenleib, Badeteich Bisamberg 32, 3500 Imbach, Österreich, vertreten durch StB, über die Beschwerde vom 26. Jänner 2022  gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 7. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 20-748/3811  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `Hon.-Prof.in Helena von Heyl` (person)
- predicted in sentence: `Charlotte Buckenleib`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Mag.a Hilde Heidorn**  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Mag.a Hilde Heidorn` (person)
- predicted in sentence: `Floriane Rötker`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Lisa Fries** in der Beschwerdesache  Piedro Ringelsbacher, BEd, Hollehnerweg 53, 2565 Schwarzensee, Österreich, über die Beschwerde vom 30. August 2023 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 6, Referat Parkometerabgabe und  Abgabenstrafen, vom 11. August 2023 betreffend Parkometerabgabe zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Lisa Fries` (person)
- predicted in sentence: `Piedro Ringelsbacher`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Alan Sontheimer  in der Angelegenheit der Parteien  **Paul Sohm** (Beschwerdeführer), und Finanzamt Klagenfurt St. Veit Wolfsberg  als Amtspartei über die Säumnisbeschwerde,  datiert vom 16. Feber 2024, eingebracht beim Bundesfinanzgericht am 17. Jänner 2024   betreffend seine Beschwerde vom 14.8.2023 gegen den Bescheid des Finanzamtes vom  13.7.2023 betreffend Festsetzung von Anspruchszinsen 2021 in Höhe von 67,61 €  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Paul Sohm` (person)
- predicted in sentence: `Mag. Alan Sontheimer`

</details>

---

