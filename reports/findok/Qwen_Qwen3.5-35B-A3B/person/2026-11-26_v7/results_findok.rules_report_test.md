# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-26T13:10:14.159310

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-26_v7/config.yaml 
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
| Enable Prune | False |
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
| True Positives | 607 |
| False Positives | 247 |
| False Negatives | 1007 |
| Total Gold Entities | 1614 |
| Micro Precision | 71.1% |
| Micro Recall | 37.6% |
| Micro F1 | 49.2% |
| Macro F1 | 49.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `party_person_defendant` | 29.5% | 91.0% | 17.6% | 312 | 284 | 28 |
| `judge_person` | 31.9% | 78.2% | 20.0% | 413 | 323 | 90 |
| `representative_person` | 0.0% | 0.0% | 0.0% | 124 | 0 | 124 |
| `narrative_person_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `narrative_person_title` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `party_person_defendant` 🏆

**F1:** 0.295 | **Precision:** 0.910 | **Recall:** 0.176  

**Format:** `regex`  
**Rule ID:** `8b5eced7`  
**Description:**
Captures parties identified after 'in der Beschwerdesache' or 'in der Verwaltungsstrafsache', handling hyphenated names, titles like Dr.in, and suffixes like BA, MAS, LLB.

**Content:**
```
(?:in\s+(?:der\s+)?Beschwerdesache(?:\s+des)?|in\s+der\s+Verwaltungsstrafsache)\s+((?:Mag\.|Dr\.|Dr\.in|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|VetR\s+Hon\.-Prof\.?)?\s*[A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)*(?:\s+(?:LL\.M\.|BSc|MSc|MAS|BA|LLB))?(?=,|\.\s|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.910 | 0.176 | 0.295 | 312 | 284 | 28 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 284 | 28 | 1330 |

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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Eligüzel` | `Chantal Eligüzel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Clemens Mooß` | `Hon.-Prof. Clemens Mooß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Florens Weißer` | `Dr. Florens Weißer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hugo Pietzak` (person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dipl. Kff. Sibylle Wahlscheid` | `Dipl. Kff. Sibylle Wahlscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Esra Schlink` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Sven Weichmann` | `Mag. Sven Weichmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Mag. Kurt Kreith` (person)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin Mag. Andrea Ebner sowie die fachkundigen Laienrichter Mag. Johannes  Denk und Friedrich Nagl in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl. Kfm. Rüdiger Schäffler` | `Dipl. Kfm. Rüdiger Schäffler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Aloisia Bergauer` (person)
- `Mag. Andrea Ebner` (person)
- `Mag. Johannes  Denk` (person)
- `Friedrich Nagl` (person)
- `Anton-Dengler-Gasse 16, 8330 Krennach, Österreich` (address)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ashley Nagelschmidt` | `Dr. Ashley Nagelschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Priv.-Doz. Timothy Oldenbüttel, Kohlreitweg 2, 4092 Winterhof, Österreich, vertreten durch EHC Wirtschaftstreuhand- gesellschaft m.b.H., Schulgasse 10, 2000  Stockerau, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 5. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Timothy Oldenbüttel` | `Priv.-Doz. Timothy Oldenbüttel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kohlreitweg 2, 4092 Winterhof, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Prof.in Julia Mundle` | `Prof.in Julia Mundle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniel Philip Pfau` (person)
- `Leitersdorf 2, 9344 Psein, Österreich` (address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `23-019/8335` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Prof.in Jeanne Sohns` | `Prof.in Jeanne Sohns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich` (address)
- `Gutwirth Consulting Steuerberatungs GmbH,` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Ing. Linus Feyerherdt` | `Ing. Linus Feyerherdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dr. Valerius Somuncu, Seelache 250, 2294 Schloßhof, Österreich, vertreten durch Dr-K, Rechtsanwalt in A, über die Beschwerde vom 22. Dezember  2017 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel  (nunmehr: Finanzamt Österreich) vom 23. November 2017 betreffend Grunderwerbsteuer,  Steuernummer 84-691/1997, Erfassungsnummer 10-2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Valerius Somuncu` | `Dr. Valerius Somuncu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Seelache 250, 2294 Schloßhof, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `84-691/1997` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


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

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


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

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


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

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. OSR Julia Strutwolf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Leander Pfleumer` — partial — pred is substring of gold: `Prof. Leander Pfleumer, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Prof. Leander Pfleumer, LLM`(person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich`(address)
- `Alfred Klaus Fenzl`(person)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `11-306/0925`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz` — partial — pred is substring of gold: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Frank Ruhleder  in der Beschwerdesache Dr. Luigi Mainholz  vertreten durch STB, über die mit Beschwerden angefochtenen Bescheide des FA Wien 1/23,  Steuernummer 61-747/1918, betreffend Einkommensteuer 2005, 2006, 2008, 2009, 2010  und 2011 zu Recht erkannt:    Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Luigi Mainholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Frank Ruhleder`(person)
- `Dr. Luigi Mainholz`(person)
- `FA Wien 1/23`(organisation)
- `61-747/1918`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140588.1`) (sent_id: `deanon_BFG_20260814_TEST/140588.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142969.1`) (sent_id: `deanon_BFG_20260814_TEST/142969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Dipl. Kfm. KommR Yussuf Bätzoldt,  Moserrautweg 4, 9872 Millstatt am See, Österreich, Schweiz, über die Beschwerde vom 13. Juli 2023 gegen den  Zurückweisungsbescheid des Finanzamtes Österreich vom 16. Juni 2023 betreffend den Antrag  auf Gewährung der Familienbeihilfe für das Kind Ki ab Jänner 2022 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dipl. Kfm` — partial — pred is substring of gold: `Dipl. Kfm. KommR Yussuf Bätzoldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl. Kfm. KommR Yussuf Bätzoldt`(person)
- `Moserrautweg 4, 9872 Millstatt am See, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/143660.1`) (sent_id: `deanon_BFG_20260814_TEST/143660.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Dr. Techn R Constantin Rethmann, Bitschweg 5, 6644 Klimm, Österreich, vertreten durch LEDERER & WEBER  Steuerberatungs GmbH, Nibelungengasse 8 Tür 5, 1010 Wien, über die Beschwerden vom 26.  Juni 2018 und 27. Juni 2018 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg (nunmehr: Finanzamt Österreich) vom 22. Juni 2018 betreffend  Einkommensteuer 2016 und Einkommensteuer 2017, Steuernummer 52-821/5355, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Julia Carola Cermak-Kapl MA`(person)
- `Techn R Constantin Rethmann`(person)
- `Bitschweg 5, 6644 Klimm, Österreich`(address)
- `LEDERER & WEBER  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `52-821/5355`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/145929.1`) (sent_id: `deanon_BFG_20260814_TEST/145929.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_1`)


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

## `judge_person` 🏆

**F1:** 0.319 | **Precision:** 0.782 | **Recall:** 0.200  

**Format:** `regex`  
**Rule ID:** `3e2a056c`  
**Description:**
Captures judges with complex titles (Dr., Mag., Univ.-Prof.in, etc.) and hyphenated names after 'durch den Richter' or 'durch die Richterin'. Handles suffixes like LL.M., BSc, MSc and German characters.

**Content:**
```
(?:durch\s+(?:den\s+)?Richter|durch\s+(?:die\s+)?Richterin)\s+((?:Mag\.|Dr\.|Dr\.in|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|VetR\s+Hon\.-Prof\.|Ing\.?)?\s*[A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)*(?:\s+(?:LL\.M\.|BSc|MSc|MAS|BA|LLB))?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.782 | 0.200 | 0.319 | 413 | 323 | 90 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 323 | 90 | 1291 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Alexander Schnelldorfer` | `Alexander Schnelldorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Amalia Schuetzke` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Saphira Blazejewicz` | `Priv.-Doz.in Saphira Blazejewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dr. Kurt Bartold` | `Priv.-Doz. Dr. Kurt Bartold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Mackiewicz` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Dr.in Hemma Ramelow` | `Univ.-Prof.in Dr.in Hemma Ramelow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Damian Wiecher` (person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Gabriele Krafft` | `Dr. Gabriele Krafft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daniel Parys` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finn van Aken` (person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich` (address)
- `Mag. Musa Işlek` (organisation)
- `Finanzamtes Wien  1/23` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Mag.a Livia Korowski` | `Priv.-Doz.in Mag.a Livia Korowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Mitterhuber` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Dammkoehler` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Serena Weidlich` | `Hon.-Prof.in Serena Weidlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Pesselt` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Babette Nimzyk` | `Hon.-Prof.in Babette Nimzyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Martin Friedl` (person)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Fabienne Kattner` | `Univ.-Prof.in Fabienne Kattner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Thomas Krampl` (person)
- `Finanzamtes für Gebühren` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Isidor Czebulla` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heinz Herper` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Hilde Heidorn` | `Univ.-Prof.in Mag.a Hilde Heidorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Floriane Rötker` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helga Woschank` | `Dr. Helga Woschank` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leonhard Bianchini` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Heidemarie Lueckemeyer  in der Verwaltungsstrafsache gegen  Amber Demirdöven, Wiedneralm 4, 4906 Feichtet, Österreich, 1.) über die Beschwerde vom 07.09.2020 gegen das Straferkennt- nis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639161/2020, und 2.) über die Beschwerde vom 07.09.2020 gegen das Strafer- kenntnis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639163/2020, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der Stadt  Wien vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, als unbegründet abgewie- sen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Heidemarie Lueckemeyer` | `Univ.-Prof.in Heidemarie Lueckemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amber Demirdöven` (person)
- `Wiedneralm 4, 4906 Feichtet, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt  Wien` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `KommR Serge Salameh` (person)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Simone Zemanek, MSc` (person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `15-763/9594` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Ada Forstner` | `Univ.-Prof.in Ada Forstner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Elias von Wnuk-Lipinski` (person)
- `Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich` (address)
- `Finanzamt` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `26-066/9346` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Caroline Schröer` | `Mag.a Caroline Schröer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Beha` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Caroline Reinwaldt` | `Priv.-Doz.in Caroline Reinwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Manuel Fortanz` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Monika Schmalzl` (person)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Thassilo Wedekinn` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Manegold` | `Dr.in Regina Manegold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in KzlR Helge Erwied` (person)
- `Unterfeichten 5, 4055 Sipbach, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anneliese Wäsche` | `Univ.-Prof.in Anneliese Wäsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gernot Kirchenmayer` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Violetta Colberg` | `Hon.-Prof.in Dr.in Violetta Colberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Kurt Bätzgen` (person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich` (address)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Gudrun Terzoglou` | `Hon.-Prof.in Gudrun Terzoglou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Berkenkämper` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag.a Lukas Dimitrieff` | `Mag.a Lukas Dimitrieff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dr.in Esra Schlink` | `Dr.in Esra Schlink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Sibylle Wahlscheid` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Dr.in Andrea Helbok` | `Dr.in Andrea Helbok` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lydia Rehnen` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Sven Weichmann` (person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Mag. Kurt Kreith` (person)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Heidrun Eifeler` | `Univ.-Prof.in Mag.a Heidrun Eifeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esra Luetje` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Hoerlin` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ashley Nagelschmidt` (person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` | `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julian Gruening` (person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Dührkopp` (person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Dr.in Alice Schöpfel` | `Dr.in Alice Schöpfel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter Guggenmoos` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `79-464/0427` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Waltraud Pantermühl   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Waltraud Pantermühl` | `Mag.a Waltraud Pantermühl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kindsfater Telekom` (organisation)
- `Pirquethof 3, 8662 Lutschaun, Österreich` (address)
- `SIGNUM Treuhand  Steuerberatungs-GmbH` (organisation)
- `Finanzamt Graz-Stadt` (organisation)
- `11-834/0873` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvius Jaros` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `97-301/3674` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Lieselotte Stiglat` | `Priv.-Doz.in Lieselotte Stiglat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sibylle Roßmayr` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `58-418/2406` (tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ilse Rauhofer in der Beschwerdesache  StR Maximiliane Heegemann, Karlstift 18, 4262 Hiltschen, Österreich, über die Beschwerden vom 25. Juni 2020 gegen die Bescheide des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 6. April 2020 betreffend  Wettgebühren und Glücksspielabgabe 01/2012 – 11/2016, Steuernummer 77-208/1736  zu  Recht erkannt:   I.1 Den Beschwerden gegen die Abgabenbescheide betreffend Wettgebühr für 01/2012 –  11/2016 wird teilweise Folge gegeben und werden die angefochtenen Bescheide gemäß § 279  BAO hinsichtlich der Bemessungsgrundlage und der Höhe der festgesetzten Wettgebühr auf  die in den Entscheidungsgründen unter Punkt 4.2.1 angeführten Abgabenbeträge reduziert.

| Predicted | Gold |
|---|---|
| `Mag. Ilse Rauhofer` | `Mag. Ilse Rauhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Maximiliane Heegemann` (person)
- `Karlstift 18, 4262 Hiltschen, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `77-208/1736` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


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

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elmira Baintner  in der Beschwerdesache Dietmar Grießmeyer,  Stiftgasse 12, 4654 Aigen, Österreich, über die Beschwerde vom 31. Juli 2021 gegen den Bescheid des FA Steiermark Mitte  vom  26. Juli 2021 betreffend Abweisung eines Rückzahlungsantrages, Steuernummer  64-502/6730, zu Recht erkannt:   I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr.in Elmira Baintner` | `Dr.in Elmira Baintner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Grießmeyer` (person)
- `Stiftgasse 12, 4654 Aigen, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `64-502/6730` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Natascha Weingarte  in der Beschwerdesache des B,  vertreten durch StB, über die Berufung vom 27. August 2012 gegen die Bescheide des  Finanzamtes X vom 10. August 2012 betreffend Einkommensteuer für die Jahre 2004 bis 2007  zu Steuernummer 46-139/2044  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Natascha Weingarte` | `Dr.in Natascha Weingarte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `46-139/2044` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chen Walcker`(person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `63-698/2600`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

**False Positives:**

- `Dr. Maria-` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Günter Gopfauf`(person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich`(address)
- `Finanzamtes Salzburg – Stadt`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `VetR OMedR Constantin Wiedewilt`(person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich`(address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Melanie Mavromatakis`(person)
- `Urbanusgasse 1, 3491 Obernholz, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy Große-` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elisabeth Sarigiannis`(person)
- `Klesenza 7, 9587 Erlendorf, Österreich`(address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `84-729/8666`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Petra Özkanli  in der Beschwerdesache des  Betriebes gewerblicher Art Radweg A-Tal des Tourismusverbandes A B, Dornackerstraße 480, 4352 Innernstein, Österreich  vertreten durch StB, über die Beschwerden vom 16. August 2017 gegen die Bescheide des  Finanzamt Wien 2/20/21/22  vom 2. Juni 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Körperschaftsteuer 2016 und Körperschaftsteuer 2016 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2016 wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Petra` — partial — pred is substring of gold: `Dr.in Petra Özkanli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Petra Özkanli`(person)
- `Dornackerstraße 480, 4352 Innernstein, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Shoshana Döllmann`(person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Priv.-Doz.in Hon.-` — partial — pred is substring of gold: `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`(person)
- `Felizitas Johanesson`(person)
- `Aspangweg 17, 9781 Gailberg, Österreich`(address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `48-504/5908`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Holger Buchmüller`(person)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hademar Sachteleben, MSc`(person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof. Univ.-` — partial — pred is substring of gold: `Univ.-Prof. Univ.-Prof. Kai Menrath`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

**False Positives:**

- `Univ.-Prof.in Univ.-` — partial — pred is substring of gold: `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp`(person)
- `Florentine Mugge`(person)
- `Rodlhütte 36, 9782 Plone, Österreich`(address)
- `FA Kufstein  Schwaz`(organisation)
- `Finanzamt Österreich`(organisation)
- `59-679/2034`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Michael Klingsohr`(person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Juri Siebgen`(person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich`(address)
- `MITTEREGGER Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-670/1415`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Mag. Hon.-` — partial — pred is substring of gold: `Mag. Hon.-Prof. Engelbert Voglsang`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache KzlR Hon.-Prof. Veit Balsottemeyer, Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich, über die Beschwerde vom 8. September 2021 gegen den Bescheid des Finanzamtes  Österreich vom 24. August 2021 betreffend Abweisung des Antrages vom 28. August 2020 auf  Auszahlung der Familienbeihilfe ohne Indexierung ab 1. Jänner 2019, Steuernummer 55-184/3803,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Hon.-Prof. Veit Balsottemeyer`(person)
- `Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `55-184/3803`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Maurice Speckner,  Hinterweg 94, 2305 Pframa, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 88-902/6713  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Maurice Speckner`(person)
- `Hinterweg 94, 2305 Pframa, Österreich`(address)
- `Finanzamtes`(organisation)
- `88-902/6713`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Gotthard Kirchhoffs, Unterriese 2, 7432 Oberschützen, Österreich, vertreten durch WWV-GROUP  SteuerberatungsGmbH, Bahnhofstraße 4, 3950 Gmünd, über die Beschwerde vom  28. September 2021 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli 2021  betreffend Haftung für Lohnsteuer, Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für die Jahre 2015 bis 2019, Steuernummer 19-927/9012, zu Recht erkannt:   I. Der Beschwerde gegen die Bescheide betreffend Festsetzung des Zuschlags zum  Dienstgeberbeitrag 2015 bis 2019 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Gotthard Kirchhoffs`(person)
- `Unterriese 2, 7432 Oberschützen, Österreich`(address)
- `WWV-GROUP  SteuerberatungsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-927/9012`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Sascha` — partial — pred is substring of gold: `Univ.-Prof.in Sascha de Kort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Sascha de Kort`(person)
- `Matthew McCarthy`(person)
- `Stichlberg 18, 4742 Klinget, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Richarda Blatzer, Rolfis 18, 5144 Feichten, Österreich, wegen behaupteter Verletzung der  Entscheidungspflicht des Finanzamtes Österreich betreffend die Erlassung eines  Einkommensteuerbescheides für das Veranlagungsjahr 2021 (Steuernummer 32-825/9727  ) beschlossen:   I. Die Säumnisbeschwerde vom 02.09.2022 wird gemäß § 260 Abs. 1 lit. a iVm § 284  Abs. 7 lit. b BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Richarda Blatzer`(person)
- `Rolfis 18, 5144 Feichten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `32-825/9727`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  Pjotr Kristall, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Pjotr Kristall`(person)
- `Schöngrabenweg 12I, 4870 Mösendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138846.1`) (sent_id: `deanon_BFG_20260814_TEST/138846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Techn R Simon Leyn,  Obere Mölten 37, 8232 Stambach, Österreich, über die Beschwerden vom 23. September 2021 gegen die Bescheid des  Finanzamtes Österreich vom 13. September 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 und Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 85-971/5131  zu Recht erkannt:   I. Der Beschwerde gegen den Einkommensteuerbescheid 2019 wird im Umfang der  Beschwerdevorentscheidung Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Techn R Simon Leyn`(person)
- `Obere Mölten 37, 8232 Stambach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-971/5131`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Mag.a Priv.-` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/138911.1`) (sent_id: `deanon_BFG_20260814_TEST/138911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde der Mag.a Selina Kreutle, Kaposigasse 101, 4906 Pumberg, Österreich, vom 6. September 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 1. August 2022, GZ. MA67/Zahl/2022, wegen einer der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, zu Recht erkannt:  Die Beschwerde vom 6. September 2022 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als  verspätet zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Selina Kreutle`(person)
- `Kaposigasse 101, 4906 Pumberg, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Priv.-` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`(person)
- `Susette Hadenfelt`(person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich`(address)
- `Huber & Rosenthal Steuerberatung KG`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)
- `34-724/8270`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für Hartmut Groebmair  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Leonhard Osskinat`(person)
- `Schreyvogelgasse 2V, 8262 Leithen, Österreich`(address)
- `Finanzamtes  Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `Hartmut Groebmair`(person)
- `39-801/9564`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sheila Mathusczyk, Achatzeweg 10, 5272 Mitterdorf, Österreich, über die Beschwerde vom 15. Juni 2015 gegen den Bescheid des Finanzamtes  Salzburg-Land vom 8. Juni 2015 betreffend Haftungsbescheid /  Lohnsteuer 2012 und 2013  Steuernummer 71-776/4123  zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid/Lohnsteuer 2012 wird als  unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sheila Mathusczyk`(person)
- `Achatzeweg 10, 5272 Mitterdorf, Österreich`(address)
- `Finanzamtes`(organisation)
- `71-776/4123`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Priv.-` — partial — pred is substring of gold: `Mag. Priv.-Doz. Andreas Domingo`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Helena von Heyl  in der Beschwerdesache des  Charlotte Buckenleib, Badeteich Bisamberg 32, 3500 Imbach, Österreich, vertreten durch StB, über die Beschwerde vom 26. Jänner 2022  gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 7. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 20-748/3811  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Hon.-Prof.in Helena` — partial — pred is substring of gold: `Hon.-Prof.in Helena von Heyl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Helena von Heyl`(person)
- `Charlotte Buckenleib`(person)
- `Badeteich Bisamberg 32, 3500 Imbach, Österreich`(address)
- `Finanzamt Gmunden Vöcklabruck`(organisation)
- `20-748/3811`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/140202.1`) (sent_id: `deanon_BFG_20260814_TEST/140202.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Anneliese Lorrek, Unteres Pieslwang 34, 9423 Hofwiesen, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Anspruchszinsen (§ 205 BAO) 2012  Steuernummer 69-743/7981  beschlossen:  Der Vorlageantrag vom 3. August 2015 wird gemäß § 278 Abs. 1 lit. a BAO iVm den §§ 260 Abs.  1 lit. a, 264 Abs. 4 lit. e und 264 Abs. 5 BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Anneliese Lorrek`(person)
- `Unteres Pieslwang 34, 9423 Hofwiesen, Österreich`(address)
- `Finanzamtes`(organisation)
- `69-743/7981`(tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Hon.-Prof. Justin Jacobeit, Gasthaus Kugelwiese 12, 3841 Markl, Österreich, vertreten durch Schmitt & Schmitt  Wirtschaftstreuhand- gesellschaft m.b.H., Strohgasse 25, 1030 Wien, über die Beschwerde vom  11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 28. April 2022,  Steuernummer 67-100/8891, betreffend Einkommensteuer 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Justin Jacobeit`(person)
- `Gasthaus Kugelwiese 12, 3841 Markl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `67-100/8891`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache OMedR Frauke Klutzuweit, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Frauke Klutzuweit`(person)
- `Weberkogelstraße 114, 8632 Weichselboden, Österreich`(address)
- `N & N Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `50-666/0525`(tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Priv.-` — partial — pred is substring of gold: `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Dipl.-Ing. Milena Panagiotoglou`(person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Bodo Adamovic, Bakk. phil., Gantschenbergstraße 24, 4204 Affenberg, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Einkommensteuer 2012  Steuernummer 49-425/9978  beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bodo Adamovic, Bakk. phil.`(person)
- `Gantschenbergstraße 24, 4204 Affenberg, Österreich`(address)
- `Finanzamtes`(organisation)
- `49-425/9978`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der Ver- waltungsstrafsache gegen StR Frederike Dalek, Margaretengürtel 113, 3110 Pultendorf, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 22. Februar 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 20. Jänner  2023, GZ. MA67/Zahl/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Frederike Dalek`(person)
- `Margaretengürtel 113, 3110 Pultendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Lee Joser, Schafwiesenstraße 6, 8443 Goldes, Österreich, vertreten durch Mag. Antonius Falkner Rechtsanwalt GmbH, Barwies 329, 6414  Mieming, über die Beschwerde vom 23. Dezember 2019 gegen den Bescheid des Zollamtes  Feldkirch Wolfurt vom 26. November 2019 betreffend Sicherheitsleistung zur Zollabgabe,  Einfuhrumsatzsteuer und Verzugszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lee Joser`(person)
- `Schafwiesenstraße 6, 8443 Goldes, Österreich`(address)
- `Mag. Antonius Falkner Rechtsanwalt GmbH,`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Klara Hienz, Oberfrödenegg 16W, 4952 Appersting, Österreich, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit §  4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 24. März  2023 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  24. November 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Klara Hienz`(person)
- `Oberfrödenegg 16W, 4952 Appersting, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cornelia Reifs`(person)
- `Hub an der Mank 8, 9300 Draschelbach, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter X. in der Beschwerdesache Sibylle Bungards, Perratgasse 13, 7210 Mattersburg, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, über die Beschwerde vom  18. Dezember 2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 22. November 2018  betreffend Umsatzsteuer 2015 und Umsatzsteuer 2016 Steuernummer 63-751/1771  zu  Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sibylle Bungards`(person)
- `Perratgasse 13, 7210 Mattersburg, Österreich`(address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `63-751/1771`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Nadja Bloemendaal, Rapsweg 11, 5151 Gastein, Österreich, vertreten durch CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.,  Klagenfurter Straße 32a, 9300 St.Veit/Glan, über die Beschwerde vom 25. März 2019 gegen  den Bescheid des Finanzamtes St. Veit Wolfsberg vom 19. März 2019 betreffend  Einkommensteuer 2017 Steuernummer 91-908/3748  nach der am 5. Juni 2023  durchgeführten mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nadja Bloemendaal`(person)
- `Rapsweg 11, 5151 Gastein, Österreich`(address)
- `CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.`(organisation)
- `Finanzamtes St. Veit Wolfsberg`(organisation)
- `91-908/3748`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Philipp Boniek, Montjolastraße 6l, 9815 Preisdorf, Österreich, vertreten durch CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.,  Klagenfurter Straße 32a, 9300 St.Veit/Glan, über die Beschwerde vom 31. August 2020 gegen  den Bescheid des Finanzamtes Österreich vom 24. August 2020 betreffend Einkommensteuer  2018 Steuernummer 69-366/4106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Philipp Boniek`(person)
- `Montjolastraße 6l, 9815 Preisdorf, Österreich`(address)
- `CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `69-366/4106`(tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Istvan  Melniczenko, Stritzelberggasse 69, 9142 Jaunstein, Österreich, über die Beschwerde des Beschuldigten vom 16. Juni 2022 gegen  den Zurückweisungsbescheid des Magistrates der Stadt Wien vom 2. Juni 2022, Zahl:  MA67/XX/2021, mit dem der Einspruch vom 3. Mai 2022 gegen die Strafverfügung vom 29.  November 2021 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Istvan  Melniczenko`(person)
- `Stritzelberggasse 69, 9142 Jaunstein, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/141392.1`) (sent_id: `deanon_BFG_20260814_TEST/141392.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Michaela Ondracsek, Arnsdorfer Straße 153, 4881 Kronberg, Österreich, über die Beschwerde vom 11. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 30. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-938/6957  zu Recht erkannt:   I.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Michaela Ondracsek`(person)
- `Arnsdorfer Straße 153, 4881 Kronberg, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `92-938/6957`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Univ.-` — partial — pred is substring of gold: `Hon.-Prof. Univ.-Prof. Florian Rouse`

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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Ulrich Büldmöller,  Hochwassersiedlung 7, 4070 Simbach, Österreich, über die Beschwerde vom 18. März 2022 gegen den Bescheid des Finanzamtes  Österreich vom 21. Dezember 2021 betreffend Zwangsstrafen 2021, Steuernummer BF1StNr2  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrich Büldmöller`(person)
- `Hochwassersiedlung 7, 4070 Simbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Chen Thiergarten, Recyclingstraße 4z, 9911 Vergein, Österreich, vertreten durch Lang & Partner Steuerberatung  GmbH & Co KG, Kapfenstein 123, 8353 Kapfenstein, über die Beschwerde der  beschwerdeführenden Partei vom 17. Juli 2023 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Bescheidaufhebung gem § 299 BAO vom 30. Dezember 2022 hinsichtlich der Bescheide  Umsatzsteuer 2019 und Feststellung von Einkünften gemäß § 188 BAO 2019, jeweils vom 7.  Jänner 2022, Steuernummer 91-654/5089  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Martin C.` — partial — pred is substring of gold: `Dr. Martin C. WITTMANN`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Chen Thiergarten`(person)
- `Recyclingstraße 4z, 9911 Vergein, Österreich`(address)
- `Lang & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamt Österreich`(organisation)
- `91-654/5089`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache ÖkR OMedR Gregor Lauerhaas, Riegerl 15, 4343 Hofstetten, Österreich, betreffend Beschwerde vom 16. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 14. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021,   Steuernummer 51-218/3095, beschlossen:  Der Vorlageantrag vom 21. September 2023 wird gemäß 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR OMedR Gregor Lauerhaas`(person)
- `Riegerl 15, 4343 Hofstetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `51-218/3095`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hon.-` — partial — pred is substring of gold: `Mag. Hon.-Prof. Wilfried Brokof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Wilfried Brokof`(person)
- `Hademar Haßelbach, BSc`(person)
- `Engerbergstraße 2, 8642 Nechelheim, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `59-681/6477`(tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Quentin Schwartkopp, Oggau-Grünland 4, 9462 Weitenbach, Österreich, über die Beschwerde vom 11.3.2019 gegen die Bescheide des Zollamtes Innsbruck  vom 20. Februar 2019 betreffend Berichtigung der Abfindungsanmeldungen Nr. xxxx/01 und  gggg/2016, Festsetzung der Alkoholsteuer für 2016 (800000/cccc);

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Quentin Schwartkopp`(person)
- `Oggau-Grünland 4, 9462 Weitenbach, Österreich`(address)
- `Zollamtes Innsbruck`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Arnold Ulmke, Mazellegasse 14, 2870 Stübegg, Österreich, vertreten durch Steuerberatung, Adresse Steuerberatung, über die Beschwerde vom  17. November 2014 gegen die Bescheide des Finanzamtes St. Johann Tamsweg Zell am See  vom 20. Oktober 2014 betreffend Dienstgeberbeitrag 2009 - 2012 und Zuschlag zum  Dienstgeberbeitrag 2009 - 2012, Steuernummer 26-962/7724  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Arnold Ulmke`(person)
- `Mazellegasse 14, 2870 Stübegg, Österreich`(address)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)
- `26-962/7724`(tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Danielle Mäwius, Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich  vertreten durch Dr. Manfred Arbacher-Stöger,  Wickenburggasse 3/14-15, 1080 Wien, über die Beschwerde vom 30. Dezember 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 15. November 2016 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und Einkommensteuer 2011 bis  2014, Umsatzsteuer und Einkommensteuer 2011 bis 2014, Festsetzung von Anspruchszinsen  2011 bis 2014, über die Beschwerde vom 27. September 2017 gegen die Bescheide des  Finanzamtes Kirchdorf Perg Steyr vom 6. September 2017 betreffend Umsatzsteuer und  Einkommensteuer 2015, gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom  8. September 2017 betreffend Umsatzsteuer und Einkommensteuer 2016, StNr.  06-463/1632, zu Recht erkannt:  I.  Die Beschwerde gegen die Wiederaufnahmebescheide hinsichtlich Umsatzsteuer 2011 bis 2014  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Danielle Mäwius`(person)
- `Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich`(address)
- `Dr. Manfred Arbacher-Stöger`(person)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `06-463/1632`(tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ulrike Stechel, Wanriglgasse 13, 4085 Ratzling, Österreich, über die Beschwerde vom   11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 11. April 2022 betreffend  Rückforderung von für den Zeitraum April bis Oktober 2021 bezogenen Beträgen an  Familienbeihilfe und Kinderabsetzbetrag, Steuernummer 59-221/1323 (SVNR  2596 170942),   zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Stechel`(person)
- `Wanriglgasse 13, 4085 Ratzling, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `59-221/1323`(tax_number)
- `2596 170942`(social_security_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/142978.1`) (sent_id: `deanon_BFG_20260814_TEST/142978.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Dieter Schwitalski, Zayagasse 125, 8162 Amstein, Österreich, über die Beschwerde vom 17. Oktober 2021  gegen die Bescheide des Finanzamtes Österreich jeweils vom 12. Oktober 2021,  Steuernummer 23-275/5780, betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Martin C.` — partial — pred is substring of gold: `Dr. Martin C. WITTMANN`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Dieter Schwitalski`(person)
- `Zayagasse 125, 8162 Amstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `23-275/5780`(tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag.a Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/143380.1`) (sent_id: `deanon_BFG_20260814_TEST/143380.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Dimitri Nickolmann, Oberkogl 34, 5166 Reith, Österreich, vertreten durch Mag. Thomas Kollaczia-Putz,  Annagasse 3-3A Tür 35, 1010 Wien, über die Beschwerde vom 25. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 19. April 2022 betreffend Aussetzungszinsen 2022,  Steuernummer 82-510/2469, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Dimitri Nickolmann`(person)
- `Oberkogl 34, 5166 Reith, Österreich`(address)
- `Mag. Thomas Kollaczia-Putz`(person)
- `Finanzamtes Österreich`(organisation)
- `82-510/2469`(tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Elena Sladek, Metnitztalweg 11, 9572 Gantschach, Österreich, vertreten durch Steuerberaterin Allegra Paulenz, Dornblüthstraße 2, 01277 Dresden,  über die Beschwerde vom 20. Juli 2020 gegen den Bescheid des Finanzamtes Österreich vom  22. Juni 2020 betreffend Feststellungsbescheid über die Nichtveranlagung zur Umsatzsteuer  2019 Steuernummer 61-618/5776  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elena Sladek`(person)
- `Metnitztalweg 11, 9572 Gantschach, Österreich`(address)
- `Allegra Paulenz`(person)
- `Finanzamtes Österreich`(organisation)
- `61-618/5776`(tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Mag. Hon.-` — partial — pred is substring of gold: `Mag. Hon.-Prof. Denis Hoffjan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Dr. Techn R Constantin Rethmann, Bitschweg 5, 6644 Klimm, Österreich, vertreten durch LEDERER & WEBER  Steuerberatungs GmbH, Nibelungengasse 8 Tür 5, 1010 Wien, über die Beschwerden vom 26.  Juni 2018 und 27. Juni 2018 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg (nunmehr: Finanzamt Österreich) vom 22. Juni 2018 betreffend  Einkommensteuer 2016 und Einkommensteuer 2017, Steuernummer 52-821/5355, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Julia Carola Cermak-` — partial — pred is substring of gold: `Mag. Julia Carola Cermak-Kapl MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Julia Carola Cermak-Kapl MA`(person)
- `Techn R Constantin Rethmann`(person)
- `Bitschweg 5, 6644 Klimm, Österreich`(address)
- `LEDERER & WEBER  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `52-821/5355`(tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/144140.1`) (sent_id: `deanon_BFG_20260814_TEST/144140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Cedric Keckeis,  Eppenberg 52, 2472 Prellenkirchen, Österreich, über die Beschwerde vom 9. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 11. Mai 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  Steuernummer 17-104/2219, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cedric Keckeis`(person)
- `Eppenberg 52, 2472 Prellenkirchen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `17-104/2219`(tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri. über die zwei (gleichlautenden)  Beschwerden des Edwin Formanski, Menschenrechtsplatz 2, 3441 Gollarn, Österreich, vom 28. Mai 2024, als gemäß § 9 Abs. 1 VStG zur  Vertretung nach außen berufene Person der Firma Firma mit Sitz in AdrFirma, gegen die zwei  Straferkenntnisse des Magistrats der Stadt Wien, Magistratsabteilung 67, als  Abgabenstrafbehörde, vom 24. Mai 2024, GZ. 1) MA67/GZ1/2024 und GZ. 2) MA67/GZ2/2024,  beide wegen einer Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird den zwei Beschwerden  insoweit teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 60,00 Euro auf  jeweils 36,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten  Ersatzfreiheitsstrafen von jeweils 14 auf jeweils 10 Stunden herabgesetzt werden.

**False Positives:**

- `Ri.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Edwin Formanski`(person)
- `Menschenrechtsplatz 2, 3441 Gollarn, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Techn R RgR Jeffrey Geippel, Dirisam 63, 2813 Pregart, Österreich, über die Beschwerde vom 3. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 2. Mai 2022 betreffend Einkommensteuer 2019  Steuernummer 84-874/5640  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Techn R RgR Jeffrey Geippel`(person)
- `Dirisam 63, 2813 Pregart, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `84-874/5640`(tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ernestine Stasiczek, Parasolstraße 27, 5163 Hiltenwiesen, Österreich, über die Beschwerde vom 17. Oktober 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Oktober 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2022, Steuernummer 16-509/3593   (SVNR 6483180845), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ernestine Stasiczek`(person)
- `Parasolstraße 27, 5163 Hiltenwiesen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `16-509/3593`(tax_number)
- `6483180845`(social_security_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/146474.1`) (sent_id: `deanon_BFG_20260814_TEST/146474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Gloria Wirnhier, Winklmannweg 79, 9562 Spitzenbichl, Österreich, über die Beschwerde vom 31. März 2022 gegen  den Bescheid des Finanzamtes Österreich vom 23. März 2022 betreffend Antrag auf  Zuerkennung des Zuzugsfreibetrages gem. § 103 Abs. 1a EStG 1988 vom 26. November 2020,  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Gloria Wirnhier`(person)
- `Winklmannweg 79, 9562 Spitzenbichl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Wendelin Nakken, Am Teichweg 31, 4131 Grub, Österreich, über die Beschwerde vom 30. Juni 2019 gegen den Bescheid des Finanzamtes St. Veit  Wolfsberg vom 27. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017  Steuernummer 59-732/9240  zu Recht erkannt:   I.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Wendelin Nakken`(person)
- `Am Teichweg 31, 4131 Grub, Österreich`(address)
- `Finanzamtes`(organisation)
- `59-732/9240`(tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/146695.1`) (sent_id: `deanon_BFG_20260814_TEST/146695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri. in der Beschwerdesache Zdenko Jannings,  Norbert-Artner-Park 19, 4694 Ehrendorf, Österreich, über die Beschwerde vom gegen den Bescheid des Finanzamtes Österreich  vom 20. April 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021,  Steuernummer xx xxx/xxxx, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Zdenko Jannings`(person)
- `Norbert-Artner-Park 19, 4694 Ehrendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Christina Buchner MBA in der  Beschwerdesache Klara Bergfelder, Ambros-Zündl-Gasse 10F, 8151 Thal, Österreich, vertreten durch CERHA HEMPEL Rechtsanwälte  GmbH, Parkring 2, 1010 Wien, über die Beschwerde vom 2. Dezember 2024 gegen den  Bescheid des Finanzamtes Österreich vom 26. November 2024 betreffend Abweisung eines  Antrages auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom für den Zeitraum 1.  Jänner 2024 bis 30. Juni 2024 zu Steuernummer 18-515/6588  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Christina Buchner` — partial — pred is substring of gold: `Mag. Christina Buchner MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christina Buchner MBA`(person)
- `Klara Bergfelder`(person)
- `Ambros-Zündl-Gasse 10F, 8151 Thal, Österreich`(address)
- `CERHA HEMPEL Rechtsanwälte  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `18-515/6588`(tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/147906.1`) (sent_id: `deanon_BFG_20260814_TEST/147906.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Miriam Wappenhans, K. Müllerweg 13, 4070 Simbach, Österreich, über die Beschwerde vom 10. November 2024 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 17. Oktober 2024, Zahl:  MA67/Zahl1/2024, mit dem der Einspruch vom 11. April 2024 gegen die Strafverfügung  vom 20. März 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miriam Wappenhans`(person)
- `K. Müllerweg 13, 4070 Simbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/147906.1`) (sent_id: `deanon_BFG_20260814_TEST/147906.1_6`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Miriam Wappenhans, K. Müllerweg 13, 4070 Simbach, Österreich  über die Beschwerde vom 10. November 2024 gegen die  Straferkenntnisse des Magistrates der Stadt Wien vom 23. September 2024, Zahlen:  MA67/Zahl2/2024 und MA67/Zahl3/2024, betreffend Verwaltungsübertretungen nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, Landesgesetzblatt für Wien  Nr. 9/2006 in der Fassung LGBl. für Wien Nr. 24/2012, den Beschluss gefasst:    1 von 11 Seite 2 von 11

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miriam Wappenhans`(person)
- `K. Müllerweg 13, 4070 Simbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/147906.1`) (sent_id: `deanon_BFG_20260814_TEST/147906.1_11`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Miriam Wappenhans, K. Müllerweg 13, 4070 Simbach, Österreich  über die Beschwerde vom 29. September 2024 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 22. August 2024, Zahl:  MA67/Zahl4/2024, mit dem der Einspruch vom 24. Juni 2024 gegen die Strafverfügung vom  16. April 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß §§ 28 Abs. 1, 31 und 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in  Verbindung mit § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das  Wiener Abgabenorganisationsrecht (WAOR) wird die Beschwerde als verspätet  zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miriam Wappenhans`(person)
- `K. Müllerweg 13, 4070 Simbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Reinhold Jonasius, Johann Tagwerker-Straße 17, 5760 Pabing, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, über die Beschwerde vom 28.08.2015 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 22. Juni 2015  betreffend Festsetzung der Kapitalertragsteuer 2011 – 2013, Steuernummer 81-937/8981  nach Durchführung einer mündlichen Verhandlung am 31. Jänner 2025 zu Recht erkannt:   I. Der Beschwerde wird als teilweise Folge gegeben.

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Reinhold Jonasius`(person)
- `Johann Tagwerker-Straße 17, 5760 Pabing, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)
- `Finanzamt Österreich`(organisation)
- `81-937/8981`(tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


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

## `representative_person` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bf6998c9`  
**Description:**
Captures legal representatives after 'vertreten durch', requiring a known person title prefix and explicitly excluding corporate entities and job titles.

**Content:**
```
(?:vertreten\s+durch)\s+((?:Mag\.|Dr\.|Dr\.in|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|VetR\s+Hon\.-Prof\.?)?\s*[A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)*(?:\s+(?:LL\.M\.|BSc|MSc|MAS|BA|LLB))?) (?!(?:GmbH|AG|KG|PartG|UG|OHG|SE|Rechtsanwälte|Notar|Steuerberatung))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 124 | 0 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 124 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Josef` — partial — pred is substring of gold: `Mag. Josef Nußbaumer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

**False Positives:**

- `Dr. Heinz` — partial — pred is substring of gold: `Dr. Heinz Neuner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `N.N.`(person)
- `Dr. Heinz Neuner`(person)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Mag. Michael` — partial — pred is substring of gold: `Mag. Michael Nierla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `N.N.`(person)
- `Mag. Michael Nierla`(person)
- `Finanzamt für Gebühren`(organisation)
- `N.N.`(person)
- `Verwaltungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rabel` — partial — pred is substring of gold: `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Ophelia Dutschka`(person)
- `Diepolding 3, 3754 Trabenreith, Österreich`(address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Kulmburg` — partial — pred is substring of gold: `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Hofmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Alexander` — partial — pred is substring of gold: `Mag. Alexander Rimser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

**False Positives:**

- `Mag. Musa` — partial — pred is substring of gold: `Mag. Musa Işlek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Adebiola Bayer`(person)
- `Finn van Aken`(person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich`(address)
- `Mag. Musa Işlek`(organisation)
- `Finanzamtes Wien  1/23`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Gosteco Goworek` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

**False Positives:**

- `Quintax` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Günter Gopfauf`(person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich`(address)
- `Finanzamtes Salzburg – Stadt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Martin` — partial — pred is substring of gold: `Martin Friedl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Babette Nimzyk`(person)
- `Tamara Poertgen, LLB Bakk. techn.`(person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes`(organisation)
- `08-216/2001`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Thomas` — partial — pred is substring of gold: `Thomas Krampl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Fabienne Kattner`(person)
- `Cornelia Özgür`(person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich`(address)
- `Thomas Krampl`(person)
- `Finanzamtes für Gebühren`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Heinz Neuböck` — partial — pred is substring of gold: `Heinz Neuböck Wthrd GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Magistrat` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Sulamith Hördegen`(person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Marion` — partial — pred is substring of gold: `Mag. Marion Riezinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrich Petrag`(person)
- `Natalie Nodurft`(person)
- `Saileräckergasse 112, 4676 Augassen, Österreich`(address)
- `Mag. Marion Riezinger`(person)
- `Finanzamtes  Linz`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Monika` — partial — pred is substring of gold: `Mag. Monika Schmalzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ronald Kulenkampf`(person)
- `Mag. Monika Schmalzl`(person)
- `FA Wien 1/23`(organisation)
- `06-334/4335`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Eckert Fries` — partial — pred is substring of gold: `Eckert Fries Carter Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Anneliese Wäsche`(person)
- `Gernot Kirchenmayer`(person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich`(address)
- `Eckert Fries Carter Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Rechtsanwalt Mag. Peter` — positional overlap with gold: `Mag. Peter  Mayerhofer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nina Rasem`(person)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `Mag. Peter  Mayerhofer`(person)
- `Magistrates  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Magistrat` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dominik Moebus`(person)
- `Aichach 11m, 9375 Knappenberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Holzinger` — partial — pred is substring of gold: `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`(person)
- `Felizitas Johanesson`(person)
- `Aspangweg 17, 9781 Gailberg, Österreich`(address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `48-504/5908`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax  Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Dr. Sebastian Pfeiffer, LL.M.`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dr. Franz Kandlhofer`(person)
- `Christina Tiebout`(person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Sonja` — partial — pred is substring of gold: `Sonja Wennemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Lukas Dimitrieff`(person)
- `Juri Marstaller`(person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich`(address)
- `Sonja Wennemann`(person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg`(organisation)
- `Finanzamt Österreich`(organisation)
- `21-286/5389`(tax_number)
- `Bundesfinanzgerichtes`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_13`)


Der Spruch lautet:  „Es ergeht die Beschwerdevorentscheidung betreffend die Beschwerde vom 27.03.2018 des Bf.,  vertreten durch Steuerberater XY, gegen Körperschaftsteuer 2013, 2014, 2015;

**False Positives:**

- `Steuerberater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

**False Positives:**

- `Pilz` — partial — pred is substring of gold: `Pilz + Rath Steuerberatung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Esra Schlink`(person)
- `Dipl. Kff. Sibylle Wahlscheid`(person)
- `Gretlern 168, 3874 Gopprechts, Österreich`(address)
- `Pilz + Rath Steuerberatung`(organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Braschel` — partial — pred is substring of gold: `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

**False Positives:**

- `Proxauf Meyer` — partial — pred is substring of gold: `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Andrea Helbok`(person)
- `Lydia Rehnen`(person)
- `Roßbergl 5, 4923 Gunzing, Österreich`(address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`(organisation)
- `Finanzamtes  Innsbruck`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Böhm` — partial — pred is substring of gold: `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Mag. Kurt` — partial — pred is substring of gold: `Mag. Kurt Kreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Mag. Sven Weichmann`(person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich`(address)
- `Mag. Kurt Kreith`(person)
- `Finanzamtes Baden  Mödling`(organisation)
- `78-738/0573`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Astoria` — partial — pred is substring of gold: `Astoria Wirtschaftstreuhand GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Christoph` — partial — pred is substring of gold: `Dr. Christoph Ganahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Juliana Untermeier`(person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich`(address)
- `Dr. Christoph Ganahl`(person)
- `Finanzamtes`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kastler` — partial — pred is substring of gold: `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lisa Lindnau`(person)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich`(address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `35-287/7417`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Shamiyeh` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

**False Positives:**

- `Burka Vitek Moser` — partial — pred is substring of gold: `Burka Vitek Moser  Rechtsanwälte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Petra Port`(person)
- `Konventweg 36, 4613 Unterholz, Österreich`(address)
- `Burka Vitek Moser  Rechtsanwälte`(organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Mag. Wolfgang Moser`(person)
- `Petra Port`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

**False Positives:**

- `Mag. Rothwangl` — partial — pred is substring of gold: `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Wladimir Beheim`(person)
- `Bruno Rüttgers`(person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich`(address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG`(organisation)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`(person)
- `Julian Gruening`(person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hopmeier Wagner Kirnbauer  Rechtsanwälte` — partial — pred is substring of gold: `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Prof.in Julia Mundle`(person)
- `Leitersdorf 2, 9344 Psein, Österreich`(address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `23-019/8335`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Korber` — partial — pred is substring of gold: `Korber & Partner WTH-Stb  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Ingrid Dohrmaier`(person)
- `Daläus 14O, 2301 Wittau, Österreich`(address)
- `Korber & Partner WTH-Stb  GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-654/1190`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Huber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Edwin Teiwes`(person)
- `MedR Francois Distefano`(person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `83-092/9347`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Schwab` — partial — pred is substring of gold: `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alice Schöpfel`(person)
- `Walter Guggenmoos`(person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich`(address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`(organisation)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `79-464/0427`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Gutwirth` — partial — pred is substring of gold: `Gutwirth Consulting Steuerberatungs GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Crowe` — partial — pred is substring of gold: `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Leander Hättrich`(person)
- `Edith Grotehenn`(person)
- `Karlhofstraße 20, 4212 Götschka, Österreich`(address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Wien  4/5/10`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

**False Positives:**

- `Christina Hildegard` — partial — pred is substring of gold: `Christina Hildegard Stowasser`

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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Alfred Klaus` — partial — pred is substring of gold: `Alfred Klaus Fenzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Prof. Leander Pfleumer, LLM`(person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich`(address)
- `Alfred Klaus Fenzl`(person)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `11-306/0925`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Caroline Toifl` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Helmut Mittermayr`(person)
- `Techn R Edwin Lamken`(person)
- `Steindl 32, 4076 Lengau, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Gammersbach&Pelstring Telekom GmbH`(organisation)
- `53-479/4428`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Mag. Markus` — partial — pred is substring of gold: `Mag. Markus Wagner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Harald Adriaans`(person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich`(address)
- `Mag. Markus Wagner`(person)
- `Finanzamtes Österreich`(organisation)
- `81-584/4494`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Causa` — partial — pred is substring of gold: `Causa Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Delila Holsträter, Bakk. iur. BEd, Ziegelsdorf 25, 4723 Unterhörzing, Österreich, vertreten durch Harald Andreas Rumpler, Mattersburgerstraße 70, 7022 Schattendorf,  über die Beschwerde vom 24. September 2018 gegen den Bescheid des Finanzamtes  Österreich vom 22. August 2018 betreffend Einkommensteuer 2016 Steuernummer  76-140/9765  zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Harald Andreas` — partial — pred is substring of gold: `Harald Andreas Rumpler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Delila Holsträter, Bakk. iur. BEd`(person)
- `Ziegelsdorf 25, 4723 Unterhörzing, Österreich`(address)
- `Harald Andreas Rumpler`(person)
- `Finanzamtes  Österreich`(organisation)
- `76-140/9765`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Anton` — partial — pred is substring of gold: `Anton Fleischhacker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Christine Kralova`(person)
- `Merlin Leuprecht`(person)
- `Ketten 21, 4061 Aistental, Österreich`(address)
- `Anton Fleischhacker`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Robert Karl` — partial — pred is substring of gold: `Dr. Robert Karl Galler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Bertha Unverich`(person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich`(address)
- `Dr. Robert Karl Galler`(person)
- `92-593/4806`(tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Nikolaus` — partial — pred is substring of gold: `Nikolaus WP GmbH Rnf. ÖBUG KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Stefan Pipal`(person)
- `Alva Danell`(person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich`(address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG`(organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg`(organisation)
- `48-595/6877`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dietmar Hülsmeier  in der Beschwerdesache StR Linn Hochleitner,  Am Schlammteich 131, 4741 Perndorf, Österreich, vertreten durch Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH,  Ötztaler Höhe 11, 6430 Ötztal-Bahnhof, über die Beschwerde vom 31. August 2015 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom 11. August  2015 betreffend Festsetzung von Anspruchszinsen (§ 205 BAO) 2012 und Einkommensteuer  2012, Steuernummer 47-841/9334,  1 ) zu Recht erkannt:   a) Der Beschwerde betr.

**False Positives:**

- `Ewald Kapeller` — partial — pred is substring of gold: `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dietmar Hülsmeier`(person)
- `StR Linn Hochleitner`(person)
- `Am Schlammteich 131, 4741 Perndorf, Österreich`(address)
- `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH`(organisation)
- `Finanzamtes Landeck Reutte`(organisation)
- `Finanzamt Österreich`(organisation)
- `47-841/9334`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Annemarie` — partial — pred is substring of gold: `Annemarie Entschev-Kurzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Julia Reittinger`(person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich`(address)
- `Annemarie Entschev-Kurzmann`(person)
- `Finanzamtes  Österreich`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_58`)


U.a. wurde von Dr. Keppert auch die „sogenannte Lenneis-Formel“ bemängelt. Zusätzlich  verweist Dr. Keppert auf die Nichtbeachtung von zukünftigen Ertragssteigerungen durch die  Finanz (vgl. Gegenäußerung der Bf., vertreten durch Dr. Keppert, zur Gegenschrift des UFS an  den VwGH vom Juni 2014 zur Streitsache UFS vom 19.12.2012, Zl. RV/0966-W/05).

**False Positives:**

- `Dr.` — similar text (different position): `Dr. Keppert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Keppert`(person)
- `Dr. Keppert`(person)
- `Dr. Keppert`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Astrid Binder`(person)
- `Nadine Tomczack`(person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Finanzamtes Österreich`(organisation)
- `15-984/4583`(tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Markus Franz` — partial — pred is substring of gold: `Mag. Markus Franz Ganzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Hemma Mauermair`(person)
- `Franziska Fitzmann`(person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich`(address)
- `Mag. Markus Franz Ganzer`(person)
- `Finanzamtes Österreich`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hofer` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Philippa Beßerdich`(person)
- `Simone Philipzig`(person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich`(address)
- `Hofer Leitinger Steuerberatung GmbH`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)
- `59-060/2086`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

**False Positives:**

- `Mag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Bettina Füsslin`(person)
- `Univ.-Prof.in Anastasia Sebott`(person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich`(address)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Wieland Nieß, Primau 14, 2813 Spratzau, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 20. Februar 2020 gegen  den Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln vom 29. Jänner 2020 betreffend  Einkommensteuer 2018, Steuernummer 72-272/3022, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ernst` — partial — pred is substring of gold: `Ernst & Young Steuerberatungs- gesellschaft  m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Wieland Nieß`(person)
- `Primau 14, 2813 Spratzau, Österreich`(address)
- `Ernst & Young Steuerberatungs- gesellschaft  m.b.H.`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)
- `72-272/3022`(tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Huber` — partial — pred is substring of gold: `Huber & Rosenthal Steuerberatung KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`(person)
- `Susette Hadenfelt`(person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich`(address)
- `Huber & Rosenthal Steuerberatung KG`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)
- `34-724/8270`(tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `Mag. Gottfried` — partial — pred is substring of gold: `Mag. Gottfried Tazol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Walther` — partial — pred is substring of gold: `Walther Kendler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Brendon Spade`(person)
- `OMedR Milena Piechulik`(person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich`(address)
- `Walther Kendler`(person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `16-827/1246`(tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Kanzlei` — partial — pred is substring of gold: `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Olivia Rodenbach`(person)
- `Veit Dworatzeck`(person)
- `Zehentberg 7, 4060 Rufling, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-692/9441`(tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch Henning & Partner Steuerberatung GmbH,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

**False Positives:**

- `Henning` — partial — pred is substring of gold: `Henning & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Imre Zeitner`(person)
- `Daisy Schlimme`(person)
- `Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich`(address)
- `Henning & Partner Steuerberatung GmbH`(organisation)
- `Dr. Michael Kotschnigg`(person)
- `Finanzamtes  Graz-Umgebung`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hofer Leitinger Steuerberatung` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alva Volgenandt  in der Beschwerdesache Pawel Smock,  Kongreßbad 9, 6811 Göfis, Österreich, vertreten durch Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Geusaugasse 39 Tür 8, 1030 Wien, 1.) über die Beschwerde vom 28.02.2014 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 27.01.2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2.) über die Beschwerde vom  28.07.2014 gegen den Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom  30.06.2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012, Steuernummer  20-852/2672, nach der am 19.10.2022 durchgeführten mündlichen Verhandlung zu Recht  erkannt:     I. Die Beschwerden werden als unbegründet abgewiesen.

**False Positives:**

- `Rogy` — partial — pred is substring of gold: `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Alva Volgenandt`(person)
- `Pawel Smock`(person)
- `Kongreßbad 9, 6811 Göfis, Österreich`(address)
- `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `20-852/2672`(tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Hon.-Prof. Justin Jacobeit, Gasthaus Kugelwiese 12, 3841 Markl, Österreich, vertreten durch Schmitt & Schmitt  Wirtschaftstreuhand- gesellschaft m.b.H., Strohgasse 25, 1030 Wien, über die Beschwerde vom  11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 28. April 2022,  Steuernummer 67-100/8891, betreffend Einkommensteuer 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schmitt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Justin Jacobeit`(person)
- `Gasthaus Kugelwiese 12, 3841 Markl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `67-100/8891`(tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schrettl Herbert` — partial — pred is substring of gold: `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

**False Positives:**

- `Dr.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Mag. Josef Ungericht`(person)
- `Mag. Armin Treichl`(person)
- `Mag.a  Patricia Kathan`(person)
- `Mag. Norbert Metzler`(person)
- `Isabella  Alexandra Längle`(person)
- `VetR Vivian Hirtel`(person)
- `Litzlberger Straße 14, 8530 Kresbach, Österreich`(address)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Lee Joser, Schafwiesenstraße 6, 8443 Goldes, Österreich, vertreten durch Mag. Antonius Falkner Rechtsanwalt GmbH, Barwies 329, 6414  Mieming, über die Beschwerde vom 23. Dezember 2019 gegen den Bescheid des Zollamtes  Feldkirch Wolfurt vom 26. November 2019 betreffend Sicherheitsleistung zur Zollabgabe,  Einfuhrumsatzsteuer und Verzugszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Antonius Falkner` — partial — pred is substring of gold: `Mag. Antonius Falkner Rechtsanwalt GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lee Joser`(person)
- `Schafwiesenstraße 6, 8443 Goldes, Österreich`(address)
- `Mag. Antonius Falkner Rechtsanwalt GmbH,`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Janosch Herr  in der Beschwerdesache des  René Schiekel, MSc, Auf der Kröß 1, 2151 Altmanns, Österreich, vertreten durch Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH, Gartenaugasse 3, 3500 Krems/Donau, über die Beschwerde vom 11. Juni 2019 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Sacha Katzensteiner Blauensteiner Rechtsanwälte` — partial — pred is substring of gold: `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Janosch Herr`(person)
- `René Schiekel, MSc`(person)
- `Auf der Kröß 1, 2151 Altmanns, Österreich`(address)
- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Revisionssache  Bertram Tienemann, Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über den Antrag des  Revisionswerbers vom 20. April 2023, der Revision vom 20. April 2023 gegen das Erkenntnis  des Bundesfinanzgerichtes vom 6. Dezember 2022, RV/7103133/2013, betreffend  Einkommensteuer 2007 erhobenen außerordentlichen Revision aufschiebende Wirkung  zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Bertram Tienemann`(person)
- `Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mehmet` — partial — pred is substring of gold: `Mehmet Köprücü`

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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Patrick Poppenheger, Steuernummer 23-019/0780,   Str.1, O1, vertreten durch Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft, Ruster Straße 91, 7000 Eisenstadt, vom 15.07.2020 gegen den  Einkommensteuerbescheid für das Jahr 2018 des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr FA Österreich), vom 29.06.2020, zugestellt am 02.07.2020, nach der im Beisein des  Schriftführers Dietmar Gratz am 29.06.2023 durchgeführten mündlichen Verhandlung  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der  angefochtene Bescheid abgeändert.

**False Positives:**

- `Crowe` — partial — pred is substring of gold: `Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Patrick Poppenheger`(person)
- `23-019/0780`(tax_number)
- `Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `FA Österreich`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Roberta Sellerer  in der   Beschwerdesache Univ.-Prof.in Susette Teebken, Günther Benedikt-Straße 26, 8052 Graz, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 29. Mai 2017 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 3. Mai 2017,   ErfNr, betreffend 1. Aufhebung gemäß § 299 Abs. 1 BAO und 2. Festsetzung der  Grunderwerbsteuer, im fortgesetzten Verfahren zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 3.5.2017 betreffend Aufhebung des      Grunderwerbsteuerbescheides vom 24.2.2017 gemäß § 299 Abs. 1 BAO wird als      unbegründet abgewiesen.

**False Positives:**

- `Marsoner` — partial — pred is substring of gold: `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Roberta Sellerer`(person)
- `Univ.-Prof.in Susette Teebken`(person)
- `Günther Benedikt-Straße 26, 8052 Graz, Österreich`(address)
- `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes für  Gebühren`(organisation)
- `Finanzamt`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1, die weitere Richterin R2 und die  fachkundigen Laienrichterinnen R3 und R4 in der Beschwerdesache des Achmed Nann, Johann Neydhart-Weg 16h, 4151 Dobretshofen, Österreich, vertreten durch Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG, Rennweg 18, 6020 Innsbruck, über die Beschwerde vom 24. Mai 2017 gegen die Bescheide  des FA Klosterneuburg  vom 26. April 2017 betreffend Umsatzsteuer 2011, Einkommensteuer 2011 und  Anspruchszinsen 2011 zu Steuernummer 03-768/0502  in der mündlichen Verhandlung am  1. August 2023 S zu Recht erkannt:   I. Die Beschwerde gegen den Umsatzsteuerbescheid 2011 wird als unbegründet  abgewiesen.

**False Positives:**

- `Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft` — partial — pred is substring of gold: `Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Achmed Nann`(person)
- `Johann Neydhart-Weg 16h, 4151 Dobretshofen, Österreich`(address)
- `Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG`(organisation)
- `FA Klosterneuburg`(organisation)
- `03-768/0502`(tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Li Lübkemann  in der   Beschwerdesache Theobald Tormöllen, Am Hora 38, 9554 Trenk, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 2. September 2016 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 24. August 2016, ErfNr, betreffend Grunderwerbsteuer im  fortgesetzten Verfahren   zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Marsoner` — partial — pred is substring of gold: `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Li Lübkemann`(person)
- `Theobald Tormöllen`(person)
- `Am Hora 38, 9554 Trenk, Österreich`(address)
- `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/141952.1`) (sent_id: `deanon_BFG_20260814_TEST/141952.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Niklas Dankwarth, Schüttaustraße 10, 9753 Raggnitz, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse  17, 1030 Wien, über die Beschwerde vom 24. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. August 2020 betreffend Einkommensteuer 2018  Steuernummer 01-612/4118  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Caroline Toifl` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Niklas Dankwarth`(person)
- `Schüttaustraße 10, 9753 Raggnitz, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `01-612/4118`(tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Chen Thiergarten, Recyclingstraße 4z, 9911 Vergein, Österreich, vertreten durch Lang & Partner Steuerberatung  GmbH & Co KG, Kapfenstein 123, 8353 Kapfenstein, über die Beschwerde der  beschwerdeführenden Partei vom 17. Juli 2023 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Bescheidaufhebung gem § 299 BAO vom 30. Dezember 2022 hinsichtlich der Bescheide  Umsatzsteuer 2019 und Feststellung von Einkünften gemäß § 188 BAO 2019, jeweils vom 7.  Jänner 2022, Steuernummer 91-654/5089  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Lang` — partial — pred is substring of gold: `Lang & Partner Steuerberatung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Chen Thiergarten`(person)
- `Recyclingstraße 4z, 9911 Vergein, Österreich`(address)
- `Lang & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamt Österreich`(organisation)
- `91-654/5089`(tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Flora Tahir, Sommeregg 24, 9634 Oberbuchach, Österreich, vertreten durch Renate Dolezal, Speisinger Str 50-52 Tür 18, 1130  Wien, über die Beschwerde vom 5. Oktober 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016, Steuernummer 20-636/7581, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Renate` — partial — pred is substring of gold: `Renate Dolezal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `Flora Tahir`(person)
- `Sommeregg 24, 9634 Oberbuchach, Österreich`(address)
- `Renate Dolezal`(person)
- `Finanzamtes  Österreich`(organisation)
- `20-636/7581`(tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Baldinger` — partial — pred is substring of gold: `Baldinger & Partner Unternehmens- und Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Mag. Andrea Proidl`(person)
- `Mag. Martin Saringer`(person)
- `Mag.  Harald  Zeller`(person)
- `Priv.-Doz.in Diana Pöppel`(person)
- `Spitalbergweg 20, 4775 Wagholming, Österreich`(address)
- `Baldinger & Partner Unternehmens- und Steuerberatung GmbH`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)
- `56-661/5349`(tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Danielle Mäwius, Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich  vertreten durch Dr. Manfred Arbacher-Stöger,  Wickenburggasse 3/14-15, 1080 Wien, über die Beschwerde vom 30. Dezember 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 15. November 2016 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und Einkommensteuer 2011 bis  2014, Umsatzsteuer und Einkommensteuer 2011 bis 2014, Festsetzung von Anspruchszinsen  2011 bis 2014, über die Beschwerde vom 27. September 2017 gegen die Bescheide des  Finanzamtes Kirchdorf Perg Steyr vom 6. September 2017 betreffend Umsatzsteuer und  Einkommensteuer 2015, gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom  8. September 2017 betreffend Umsatzsteuer und Einkommensteuer 2016, StNr.  06-463/1632, zu Recht erkannt:  I.  Die Beschwerde gegen die Wiederaufnahmebescheide hinsichtlich Umsatzsteuer 2011 bis 2014  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Manfred` — partial — pred is substring of gold: `Dr. Manfred Arbacher-Stöger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Danielle Mäwius`(person)
- `Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich`(address)
- `Dr. Manfred Arbacher-Stöger`(person)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `06-463/1632`(tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

**False Positives:**

- `Dr. Martin` — partial — pred is substring of gold: `Dr. Martin Weiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Heinrich Rzeppa, LLM`(person)
- `Toulagasse 1, 8111 Straßengel, Österreich`(address)
- `Dr. Martin Weiser`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `52-580/0972`(tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Fabian Kohnke, Hammersdorfstraße 78, 4223 Lungitz, Österreich, vertreten durch Intercura  Treuhand- und Revisionsgesellschaft m.b.H., Bösendorferstraße 2, 1010 Wien, über die  Beschwerde vom 14. Dezember 2018 gegen die Bescheide des Finanzamtes Wien 1/23 vom  16. November 2018 betreffend Haftung Lohnsteuer, Festsetzung Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag sowie Säumniszuschläge jeweils 2015 bis 2017  (Steuernummer 14-263/3594 ) nach Durchführung einer mündlichen Verhandlung am  21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Intercura  Treuhand-` — partial — pred is substring of gold: `Intercura  Treuhand- und Revisionsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Mag. Monika Ahorn`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dipl. Ing.  Thomas Hrdinka`(person)
- `Fabian Kohnke`(person)
- `Hammersdorfstraße 78, 4223 Lungitz, Österreich`(address)
- `Intercura  Treuhand- und Revisionsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `14-263/3594`(tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/143207.1`) (sent_id: `deanon_BFG_20260814_TEST/143207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Linus Frauenstein, Göllerichstraße 41, 9323 Wildbad Einöd, Österreich, vertreten durch Dr. Philip Gruber, Oberer Markt 22, 3631 Ottenschlag, über die  Beschwerde vom 21. Juli 2023 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli  2023 betreffend Grunderwerbsteuer, Steuernummer 70-621/7927, Erfassungsnummer 10- 2023, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Philip` — partial — pred is substring of gold: `Dr. Philip Gruber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Linus Frauenstein`(person)
- `Göllerichstraße 41, 9323 Wildbad Einöd, Österreich`(address)
- `Dr. Philip Gruber`(person)
- `Finanzamtes Österreich`(organisation)
- `70-621/7927`(tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Securitas Revisions-` — partial — pred is substring of gold: `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`

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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/143380.1`) (sent_id: `deanon_BFG_20260814_TEST/143380.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Dimitri Nickolmann, Oberkogl 34, 5166 Reith, Österreich, vertreten durch Mag. Thomas Kollaczia-Putz,  Annagasse 3-3A Tür 35, 1010 Wien, über die Beschwerde vom 25. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 19. April 2022 betreffend Aussetzungszinsen 2022,  Steuernummer 82-510/2469, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Thomas` — partial — pred is substring of gold: `Mag. Thomas Kollaczia-Putz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Dimitri Nickolmann`(person)
- `Oberkogl 34, 5166 Reith, Österreich`(address)
- `Mag. Thomas Kollaczia-Putz`(person)
- `Finanzamtes Österreich`(organisation)
- `82-510/2469`(tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/143628.1`) (sent_id: `deanon_BFG_20260814_TEST/143628.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaroslaw Hoecker  in der Beschwerdesache Valerius Sülzbrück,  Mariazellerstraße 82, 4210 Unterweitrag, Österreich  nunmehr vertreten durch Steuerberaterin Danielle Tafelmeir, Andelberggasse 58, 4760 Niederham, Österreich, über die  Beschwerde vom 5. Oktober 2017 (Postaufgabetag) gegen den Bescheid des ehemaligen  Finanzamtes Wien 12/13/14 Purkersdorf vom 19. September 2017 betreffend Abweisung eines  Zahlungserleichterungsansuchens, Steuernummer 26-264/5699, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Danielle` — positional overlap with gold: `Danielle Tafelmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Jaroslaw Hoecker`(person)
- `Valerius Sülzbrück`(person)
- `Mariazellerstraße 82, 4210 Unterweitrag, Österreich`(address)
- `Danielle Tafelmeir`(person)
- `Andelberggasse 58, 4760 Niederham, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `26-264/5699`(tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/143793.1`) (sent_id: `deanon_BFG_20260814_TEST/143793.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache   DDr. OStR Ernst Brücklmaier, Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich  vertreten durch Beste & Partner Steuerberatung GmbH,  Perlhofgasse 2/2/8, 2372 Gießhübl, betreffend Beschwerde vom 20. September 2021 gegen  die Bescheide des Finanzamtes für Großbetriebe vom 2. September 2021 betreffend  Wiederaufnahme § 303 BAO Körperschaftsteuer der Jahre 2014-2016 sowie Wiederaufnahme  Körperschaftsteuer für das Jahr 2018, Steuernummer 87-802/5730  beschlossen:  Die Beschwerde wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Beste` — partial — pred is substring of gold: `Beste & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `DDr. OStR Ernst Brücklmaier`(person)
- `Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich`(address)
- `Beste & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `87-802/5730`(tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Elena Sladek, Metnitztalweg 11, 9572 Gantschach, Österreich, vertreten durch Steuerberaterin Allegra Paulenz, Dornblüthstraße 2, 01277 Dresden,  über die Beschwerde vom 20. Juli 2020 gegen den Bescheid des Finanzamtes Österreich vom  22. Juni 2020 betreffend Feststellungsbescheid über die Nichtveranlagung zur Umsatzsteuer  2019 Steuernummer 61-618/5776  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Allegra` — positional overlap with gold: `Allegra Paulenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elena Sladek`(person)
- `Metnitztalweg 11, 9572 Gantschach, Österreich`(address)
- `Allegra Paulenz`(person)
- `Finanzamtes Österreich`(organisation)
- `61-618/5776`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dagobert Rönnecke  in der Revisionssache PhD ÖkR Peter Stankeit,  Im Alauntal 10, 3243 Eselsteiggraben, Österreich  vertreten durch Aigner Rechtsanwalts-GmbH, Lugeck 1-2/Stiege 2/Top 12, 1010  Wien, über den Antrag des Revisionswerbers vom 2.Februar 2024, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 12.Dezember 2023, RV/5100686/2021, betreffend  Einkommensteuer 2019 und die Aufhebung des Einkommenssteuerbescheides 2019  erhobenen außerordentlichen Revision die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Aigner` — partial — pred is substring of gold: `Aigner Rechtsanwalts-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Dagobert Rönnecke`(person)
- `PhD ÖkR Peter Stankeit`(person)
- `Im Alauntal 10, 3243 Eselsteiggraben, Österreich`(address)
- `Aigner Rechtsanwalts-GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Albert Salzmann, die  Richterin Dr. Susanne Zankl sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache Ewald Lüttfrenk, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Etschbacher` — partial — pred is substring of gold: `Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Dr. Susanne Zankl`(person)
- `Christine Höll`(person)
- `Dr. Rupert  Mayr`(person)
- `Ewald Lüttfrenk`(person)
- `Triftgasse 9, 5145 Königsaich, Österreich`(address)
- `Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `55-257/7759`(tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch Mag. Aleksandar Hofstätter, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

**False Positives:**

- `Mag. Aleksandar` — partial — pred is substring of gold: `Mag. Aleksandar Hofstätter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Rita Wiersbicki`(person)
- `Corvin Billmaier`(person)
- `Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich`(address)
- `Mag. Aleksandar Hofstätter`(person)
- `Finanzamtes  Österreich`(organisation)
- `23-971/7442`(tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Prof. Yorick` — partial — pred is substring of gold: `Prof. Yorick Frühbis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

**False Positives:**

- `Zachmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Annkathrin Czesielski`(person)
- `Prof.in Esra Konwischer`(person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jessica Buddeus  in der Beschwerdesache Heidemarie Helwig,  Schmittengasse 288, 3160 Maierhöfen, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des FA Purkersdorf  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 81-530/8966, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Jessica Buddeus`(person)
- `Heidemarie Helwig`(person)
- `Schmittengasse 288, 3160 Maierhöfen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`(organisation)
- `FA Purkersdorf`(organisation)
- `81-530/8966`(tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch Mag. Hedwig Maria Weber, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

**False Positives:**

- `Mag. Hedwig Maria` — partial — pred is substring of gold: `Mag. Hedwig Maria Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Thassilo Osipenko`(person)
- `Agatha Stingele`(person)
- `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich`(address)
- `Mag. Hedwig Maria Weber`(person)
- `Finanzamtes  Österreich`(organisation)
- `39-913/2428`(tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch Ing. Mag. Dr. Roland Erwin Hansely, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

**False Positives:**

- `Ing. Mag. Dr. Roland Erwin` — partial — pred is substring of gold: `Ing. Mag. Dr. Roland Erwin Hansely`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Maria Daniel`(person)
- `Diana Wüste`(person)
- `Schönangerweg 35, 4925 Gumpling, Österreich`(address)
- `Ing. Mag. Dr. Roland Erwin Hansely`(person)
- `Zollamtes Österreich`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ilse Leners  in der Beschwerdesache Herta Lindgens,  Ruth-Drexel-Weg 7, 4691 Schlatt, Österreich, vertreten durch Markl Rechtsanwälte OG, Schmerlingstraße 2, 6020 Innsbruck,  über die Beschwerde vom 20. Jänner 2022 gegen den Bescheid des Finanzamtes Österreich  vom 5. Jänner 2022, Str. Nr. X1, betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO   zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Markl Rechtsanwälte` — partial — pred is substring of gold: `Markl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ilse Leners`(person)
- `Herta Lindgens`(person)
- `Ruth-Drexel-Weg 7, 4691 Schlatt, Österreich`(address)
- `Markl Rechtsanwälte OG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Woditschka` — partial — pred is substring of gold: `Woditschka  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Mag. Sonja Stradner`(person)
- `Manfred Fiala`(person)
- `Dipl.Ing. Wolfgang  Weichselbraun`(person)
- `Kira Lentze`(person)
- `In der Krems 35, 3500 Gneixendorf, Österreich`(address)
- `Woditschka  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `97-126/0015`(tax_number)

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `narrative_person_title` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cdc1aa86`  
**Description:**
Captures persons with complex titles in narrative contexts (e.g., 'Herr Mag. X', 'Frau Dr. Y') or standalone titles followed by names where no specific role marker exists.

**Content:**
```
(?:Herr|Frau)\s+((?:Mag\.|Dr\.|Dr\.in|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|VetR\s+Hon\.-Prof\.?)? [A-Z][a-zäöüßÄÖÜß\.\-]+(?: [A-Z][a-zäöüßÄÖÜß\.\-]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_28`)


Betreffend die Baurechtseinlage EZ 2 KG XY) wurde mit Schreiben vom 5.4.2017 von Notar Herr  Mag. Z die Befreiung gemäß § 3 Abs. 1 Z 2 GrEStG (damals fälschlicherweise die Befreiung  gemäß § 3 Abs. 1 Z 3 GrEStG bezeichnet) beantragt.

**False Positives:**

- ` Mag.` — positional overlap with gold: `Mag. Z`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Z`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_149`)


Herr  Dr. YYY ist für Ärzte ohne Grenzen tätig.

**False Positives:**

- ` Dr.` — positional overlap with gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

**False Positives:**

- ` Nina Rasem` — partial — gold is substring of pred: `Nina Rasem`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Nina Rasem`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

**False Positives:**

- ` Quentin Schwartkopp` — partial — gold is substring of pred: `Quentin Schwartkopp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zollamtes Innsbruck`(organisation)
- `Quentin Schwartkopp`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

**False Positives:**

- ` Jeanne Pavlovitsch` — partial — gold is substring of pred: `Jeanne Pavlovitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeanne Pavlovitsch`(person)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1007, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)

In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr **Quentin Schwartkopp**  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache **Cornelia Özgür**,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Cornelia Özgür` (person)
- predicted in sentence: `Univ.-Prof.in Fabienne Kattner`, `Thomas`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)

Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach **Dr. Gunther Schmidt** und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

- missed: `Dr. Gunther Schmidt` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Albert Salzmann, die  Richterin **Dr. Susanne Zankl** sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache Ewald Lüttfrenk, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Susanne Zankl` (person)
- predicted in sentence: `Ewald Lüttfrenk`, `Etschbacher`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  **Leopold Pichlbauer** in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

- missed: `Leopold Pichlbauer` (person)
- predicted in sentence: `Bettina Domigall`, `Shamiyeh`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_250`)

Abgesehen davon verfügt **Amanda Zacharek** als Fachärztin für Kinder- und Jugendheilkunde daneben  ohnehin über eine Zusatzqualifikation in dem – von der Bf monierten - Fach "Humangenetik"  und ist als langjährige Ambulanzleiterin, darunter der Ambulanz für Klinische Genetik, ua. auch  mit der Betreuung von Patienten mit einer – wie hier - seltenen Erkrankung befasst.

- missed: `Amanda Zacharek` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_133`)

Nach den Ausführungen der steuerlichen Vertretung sei am ersten Lichtbild (20210406- 11342.jpg) das Zimmer des Bf. und am zweiten (20210406_113825.jpg) dass für Gäste der  Familie reservierte Gästezimmer dargestellt. Ganz offensichtlich wurde somit dem Bf. – wie  vom Gericht vermutet – das von der Zeugin **N.N.** beschriebene „Blumenzimmer“ zur Nutzung  zugewiesen.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)

In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau **Freßdorf**  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

- missed: `Freßdorf` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_11`)

II. der Verband **Engelbert Schefe**  wurde schuldig erkannt, für durch einen Entscheidungsträger im  Sinne des § 2 Abs. 1 Verbandsverantwortlichkeitsgesetz (VbVG) iVm § 28a FinStrG zu Gunsten  des Verbandes und unter Verletzung den Verband treffender Verpflichtungen begangen  Finanzvergehen verantwortlich zu sein (I.).

- missed: `Engelbert Schefe` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_319`)

Dies war für den Magistrat nicht überprüfbar, weil ein **Vera Schliephacke** an der  angegebenen Adresse nicht bekannt war.

- missed: `Vera Schliephacke` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142978.1`) (sent_id: `deanon_BFG_20260814_TEST/142978.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter **Dr. Martin C. WITTMANN** in der  Beschwerdesache Dieter Schwitalski, Zayagasse 125, 8162 Amstein, Österreich, über die Beschwerde vom 17. Oktober 2021  gegen die Bescheide des Finanzamtes Österreich jeweils vom 12. Oktober 2021,  Steuernummer 23-275/5780, betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Martin C. WITTMANN` (person)
- predicted in sentence: `Dr. Martin C.`, `Dieter Schwitalski`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden **Mag. Albert Salzmann**, die  Richterin Dr. Susanne Zankl sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache Ewald Lüttfrenk, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Albert Salzmann` (person)
- predicted in sentence: `Ewald Lüttfrenk`, `Etschbacher`

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  der **Jeffrey Heilmayr**, Johann Holzmann-Straße 222, 4912 Ponneredt, Österreich, vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 15. März 2023, mit dem der Antrag auf Familienbeihilfe und  Erhöhungsbetrag  ab August 2022 abgewiesen wurde, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Jeffrey Heilmayr` (person)
- predicted in sentence: `Mag. Helga Hochrieser`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140554.1`) (sent_id: `deanon_BFG_20260814_TEST/140554.1_3`)

Entscheidungsgründe  I. Verfahrensgang  An die „**Rinaldo Steckenmesser**“ (Bf.) erging seitens der belangten Behörde am 29.08.2018 eine  Aufforderung, die wirtschaftlichen Eigentümer im Sinne des § 5 Wirtschaftliche Eigentümer  Registergesetz (WiEReG) bis spätestens 10.12.2018 zu erstatten.

- missed: `Rinaldo Steckenmesser` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)

Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr **Vera Schliephacke** in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

- missed: `Vera Schliephacke` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_5`)

Auf Seite 1 des betreffenden Schriftsatzes wird darauf  hingewiesen, dass **Evamaria Watenphul** (nachstehend mit Bf bezeichnet) Beschwerdeführer ist und vom  Anwalt vertreten wird (Vollmacht erteilt).

- missed: `Evamaria Watenphul` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138259.1`) (sent_id: `deanon_BFG_20260814_TEST/138259.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Otto Pavlikova  in der Angelegenheit der Parteien  **Oskar Wood** (Beschwerdeführer) und Finanzamt Österreich als Amtspartei und als  Gesamtrechtsnachfolger des FA Niederösterreich Mitte  über die Beschwerde vom  22.6.2020 gegen den Bescheid des FA Niederösterreich Mitte  vom 22.5.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019         zu Recht erkannt:  Der Beschwerde wird Folge gegeben.

- missed: `Oskar Wood` (person)
- predicted in sentence: `Univ.-Prof. Otto Pavlikova`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)

- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau **Basyurt** tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)

Frau **Basyurt** wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_146`)

Von meiner Seite wurde absolut alles unternommen um zu beweisen, dass Hr. **Dr. YYY** das  gegenständliche Fahrzeug gelenkt und abgestellt hat.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_123`)

Die im Zusammenhang mit der Zurverfügungstellung eines Schlüssels getätigten –  übereinstimmenden - Angaben des Bf. bzw. der Zeugin **N.N.** im Rahmen der mündlichen  Verhandlung waren schließlich ebensowenig überzeugend: Es widerspricht nämlich vorerst  8 von 12 Seite 9 von 12

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache **Wigand Maczkiewicz, Bakk. art.**,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

- missed: `Wigand Maczkiewicz, Bakk. art.` (person)
- predicted in sentence: `Univ.-Prof. Univ.-`, `Wigand Maczkiewicz`, `Braschel`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_80`)

Soweit ersichtlich („Erklärung“) war D nur für **Sheila Mathusczyk**  tätig.

- missed: `Sheila Mathusczyk` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Verwaltungsstraf- sache gegen **Olivia Zumbruch**, Hans Haid-Straße 15, 5233 Hart, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde der Beschuldigten vom 22. Mai 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. April 2023, GZ. MA67/Zahl/2023,  zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren nach § 45 Abs. 1 Z 1 VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

- missed: `Olivia Zumbruch` (person)
- predicted in sentence: `Dr. Anna Radschek`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) **Siegfried Basyurt**, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

- missed: `Siegfried Basyurt` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)

Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn **Jeanne Kraenzlin**) getragen wird.

- missed: `Jeanne Kraenzlin` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_69`)

Es handle sich dabei um eine  Drittschuldnererklärung, die an das Bezirksgericht E. und an Rechtsanwalt **Roxana Hiltenbrand, MA** versendet  wurde.

- missed: `Roxana Hiltenbrand, MA` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_81`)

In der Beschwerde brachte die Bf vor, dass ihre Tochter **Heidemarie Fitzenreiter**  während ihres  Schulbesuches in Israel nicht erwerbstätig und ledig gewesen sei, weshalb sie einen  Unterhaltsanspruch gehabt habe.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)

Überdies hätte Herr **Quentin Schwartkopp**  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_25`)

Weiters habe sich die  Tochter **Heidemarie Fitzenreiter**  aber auch im Beschwerdezeitraum in Israel und damit ständig im  Ausland aufgehalten.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Sascha de Kort**  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof.in Sascha de Kort` (person)
- predicted in sentence: `Univ.-Prof.in Sascha`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_128`)

Entgegen den Ausführungen der Zeugin **N.N.** bzw. des Bf. geht das erkennende Gericht im  gegenständlichen Fall auch davon aus, dass dem Bf. ein Zimmer im Wohnhaus der Mutter -  zwar nach Rücksprache, aber dennoch - jederzeit zur Verfügung stand: So führte die Zeugin  N.N. vor dem erkennenden Gericht aus, dass sich im 1.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der **Wieland Nieß**, Primau 14, 2813 Spratzau, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 20. Februar 2020 gegen  den Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln vom 29. Jänner 2020 betreffend  Einkommensteuer 2018, Steuernummer 72-272/3022, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Wieland Nieß` (person)
- predicted in sentence: `Mag. Andreas Stanek`, `Ernst`

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_4`)

Gegen diesen Bescheid hat **Mehmet Köprücü**  mit Schreiben vom 20. April 2022 als Vertreter  des Bf und eines weiteren Haftungspflichtigen, an den ebenfalls ein Haftungsbescheid  ergangen ist, Beschwerde eingebracht.

- missed: `Mehmet Köprücü` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_480`)

Die Schaffung von Kryptowährungen (am Beispiel Bitcoin) – allgemeines (Auszug aus  Domes-Hohl, Die steuerliche Behandlung von virtuellen Währungen am Beispiel von Bitcoins,  Diplomarbeit Institut für Finanzrecht Graz, Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 3-27;  zum technischen Aufbau des Netzwerks siehe Gerion Entrup, Bitcoin – der Stärkere gewinnt,  2013, Bachelorarbeit, Institut für theoretische Informatik, **Dr. Arne Meier**):   a. Bitcoin ist eine Kryptowährung und existiert nicht in physischer Form.

- missed: `Dr. Arne Meier` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_372`)

kein ÖGK-Kostenersatz oder sonstiger Nachweis der medizinischen Notwendigkeit iSd  VwGH-Judikatur;   - 742,- € **M.** M. für Physiotherapie/Heilmassage/osteopath.

- missed: `M.` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)

Demnach hätte Herr **Dipl.-Ing. Heinz Riechels**  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

- missed: `Dipl.-Ing. Heinz Riechels` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_110`)

Zu den Eingangsrechnungen der Fa. X. d.o.o an das Einzelunternehmen **N.N.** in den Jahren 2012 und 2013 und Vorhalt Zeugenaussage B. A. vom 4.9.2018, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa.  X. d.o.o erbracht worden seien, führte der Beschuldigte aus, Herr A. habe eigenständig eine Firma in Slowenien gegründet und sei mit dieser Firma zu ihm gekommen und habe um Aufträge ersucht.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/144232.1`) (sent_id: `deanon_BFG_20260814_TEST/144232.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat in der  Beschwerdesache Fiona Reckerth, Am Tasen 60, 4941 Mehrnbach, Österreich  vertreten durch **RA Michael Lux**, Lange Weg 118,  B-3090 Overjise und DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger Straße 2-4,  1090 Wien, Steuernummer: 03-123/0344, über die Beschwerde vom 15. Dezember 2023  gegen den Bescheid des Finanzamtes Österreich vom 28. November 2023 betreffend  Zurückweisung des Antrages auf Erteilung einer Fiskalvertreter-USt-ID Nummer gemäß § 27  Abs 8 UStG zu Recht:  I)  Der angefochtene Bescheid wird aufgehoben.

- missed: `RA Michael Lux` (person)
- predicted in sentence: `Mag. Günter Narat`, `Fiona Reckerth`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache **Dipl.-Ing. Tosca Toussaint**,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

- missed: `Dipl.-Ing. Tosca Toussaint` (person)
- predicted in sentence: `Priv.-Doz.in Vivian Gastell`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, **Svenja Nowakowsky**,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Svenja Nowakowsky` (person)
- predicted in sentence: `Univ.-Prof.in Anastasia Schraders`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_4`)

Da **Heidemarie Fitzenreiter**  eine Schule in Israel (= Drittstaat) besucht habe,  bestehe im Rückforderungszeitraum kein Anspruch auf Familienbeihilfe.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)

BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. September 2020 des Beschwerdeführers Klarissa Fuhljahn, Adr Bf, Steuernummer  21-178/1143, vertreten durch den mit Zustellvollmacht ausgewiesenen **Martin Friedl**, 4650  Lambach, Marktplatz 2 gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr (nunmehr  Finanzamt Österreich) vom 17. August 2020 betreffend Haftung für Lohnsteuer 2012 – 2017  sowie Festsetzung von Dienstgeberbeiträgen und Festsetzung von Zuschlägen zu den  Dienstgeberbeiträgen für die Jahre 2011 – 2017:  I)

- missed: `Martin Friedl` (person)
- predicted in sentence: `Mag. Günter Narat`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache **StR Mag. Dirk Bröders**, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `StR Mag. Dirk Bröders` (person)
- predicted in sentence: `Mag. Anna Mechtler-`

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_53`)

Der Bf. begründete an der Adresse in Untersameting 4, 4894 Römerhof, Österreich (Haus im Alleineigentum seiner Mutter,  der Zeugin **N.N.**) am xx.xx.xxxx seinen Hauptwohnsitz, meldete diesen jedoch noch am selben  Tag wieder ab;

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_240`)

Bekannt sei, dass **Dipl.Ing. Dr. H** mehrere Gutachten erstellt habe.

- missed: `Dipl.Ing. Dr. H` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch **Mag. Hedwig Maria Weber**, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

- missed: `Mag. Hedwig Maria Weber` (person)
- predicted in sentence: `Univ.-Prof. Thassilo Osipenko`, `Agatha Stingele`, `Mag. Hedwig Maria`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_423`)

Hinsichtlich der Boni bei den Glücksspielabgaben führte die Bf. ergänzend aus, dass Aufgrund  der von **Oswald Rübberdt**  getrennten Führung eines „Echtgeld-" und eines „Bonuskontos" für den  Zeitraum 01/2012 bis 11/2016 eine klare Abgrenzung vorgenommen werden könne, welchen  Beträgen ein Vermögenswert zukommt und welchen nicht.

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)

ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn **Dr. YYY** übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_116`)

Laut vorgelegtem Gutachten von **Nicola Peterhansel**  Fachärztin für Psychiatrie, vom 7. Jänner 2019, leidet  der Bf. an einer Intelligenzminderung mit einer ausgeprägten Lese- und Rechenschwäche und  kann auf Grund des vorliegenden Krankheitsbildes weder Vertragsinhalte richtig erfassen,  11 von 13 Seite 12 von 13

- missed: `Nicola Peterhansel` (person)
- predicted in sentence: —

</details>

---

