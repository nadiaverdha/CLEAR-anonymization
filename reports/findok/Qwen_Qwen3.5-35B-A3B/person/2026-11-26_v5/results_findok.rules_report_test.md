# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-26T12:37:00.523777

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
| True Positives | 530 |
| False Positives | 169 |
| False Negatives | 1084 |
| Total Gold Entities | 1614 |
| Micro Precision | 75.8% |
| Micro Recall | 32.8% |
| Micro F1 | 45.8% |
| Macro F1 | 45.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `party_person_defendant` | 28.7% | 90.8% | 17.0% | 303 | 275 | 28 |
| `judge_person` | 23.1% | 82.5% | 13.4% | 263 | 217 | 46 |
| `representative_person` | 4.4% | 39.2% | 2.4% | 97 | 38 | 59 |
| `abbreviated_person_herr_frau` | 0.0% | 0.0% | 0.0% | 24 | 0 | 24 |
| `generic_title_initial_person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `case_citation_person` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `narrative_person_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `party_person_defendant` 🏆

**F1:** 0.287 | **Precision:** 0.908 | **Recall:** 0.170  

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
| 0.908 | 0.170 | 0.287 | 303 | 275 | 28 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 275 | 28 | 1339 |

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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Quentin Girharz` | `Quentin Girharz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Kandler` (person)
- `FA Landeck Reutte` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Prof.in Jeanne Sohns` | `Prof.in Jeanne Sohns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich` (address)
- `Gutwirth Consulting Steuerberatungs GmbH,` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


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

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


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

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


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

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


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

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `H. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

**False Positives:**

- `Charlotte Hirschmueller Silberhumerweg` — partial — gold is substring of pred: `Charlotte Hirschmueller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Charlotte Hirschmueller`(person)
- `Silberhumerweg 2, 9163 Bodental, Österreich`(address)
- `HR Danielle Schochert`(person)
- `Haßreidterstraße 75, 8831 Raiming, Österreich`(address)
- `46-246/2967`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz` — partial — pred is substring of gold: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Matthew Mc` — partial — pred is substring of gold: `Matthew McCarthy`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Sascha de Kort`(person)
- `Matthew McCarthy`(person)
- `Stichlberg 18, 4742 Klinget, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


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

- `Dipl. Kfm. Komm` — partial — pred is substring of gold: `Dipl. Kfm. KommR Yussuf Bätzoldt`

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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

**False Positives:**

- `Mag.a Susanne Groesche Unternurpensalm` — partial — gold is substring of pred: `Mag.a Susanne Groesche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Danielle Merte`(person)
- `Mag.a Susanne Groesche`(person)
- `Unternurpensalm 12, 5141 Moosdorf, Österreich`(address)
- `CONSULTATIO Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes  Wien 1/23`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `76-369/9701`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Dr. Techn R Constantin Rethmann, Bitschweg 5, 6644 Klimm, Österreich, vertreten durch LEDERER & WEBER  Steuerberatungs GmbH, Nibelungengasse 8 Tür 5, 1010 Wien, über die Beschwerden vom 26.  Juni 2018 und 27. Juni 2018 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg (nunmehr: Finanzamt Österreich) vom 22. Juni 2018 betreffend  Einkommensteuer 2016 und Einkommensteuer 2017, Steuernummer 52-821/5355, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Techn` — positional overlap with gold: `Techn R Constantin Rethmann`

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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/145929.1`) (sent_id: `deanon_BFG_20260814_TEST/145929.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)


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

**F1:** 0.231 | **Precision:** 0.825 | **Recall:** 0.134  

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
| 0.825 | 0.134 | 0.231 | 263 | 217 | 46 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 217 | 46 | 1397 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Mackiewicz` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Caroline Schröer` | `Mag.a Caroline Schröer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Beha` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Monika Schmalzl` (person)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Thassilo Wedekinn` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Natascha Weingarte  in der Beschwerdesache des B,  vertreten durch StB, über die Berufung vom 27. August 2012 gegen die Bescheide des  Finanzamtes X vom 10. August 2012 betreffend Einkommensteuer für die Jahre 2004 bis 2007  zu Steuernummer 46-139/2044  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Natascha Weingarte` | `Dr.in Natascha Weingarte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `46-139/2044` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Rut Schattel` | `Mag.a Rut Schattel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stanley Wachenschwanz, Bakk. rer. nat.` (person)
- `Finanzamtes` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Mag. Niels Rustemeier` | `Mag. Mag. Niels Rustemeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nicoletta Walch` (person)
- `Polheimerweg 2, 3464 Schmida, Österreich` (address)
- `65-653/8677` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  Prof.in Alma Siegers, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Alma Siegers` (person)
- `Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `37-792/2472` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/137043.1`) (sent_id: `deanon_BFG_20260814_TEST/137043.1_2`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/137175.1`) (sent_id: `deanon_BFG_20260814_TEST/137175.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Johanna Housein, Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 85-874/2370, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johanna Housein` (person)
- `Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-874/2370` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bertha Unverich` (person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich` (address)
- `Dr. Robert Karl Galler` (person)
- `92-593/4806` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Muran Unverricht, Bleischweg 3, 9500 Rennstein, Österreich, über die Beschwerden vom 28. Oktober 2018, vom 9. Februar 2019  und vom 7. Februar 2020 gegen die Bescheide des Finanzamtes Österreich vom 26. Juli 2018  betreffend Abweisung eines Antrages auf Aufhebung des Körperschaftsteuerbescheides 2016  sowie vom 31. Jänner 2019 und vom 16. Jänner 2020 betreffend Körperschaftsteuer 2017 und  2018 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Abweisung eines Antrages auf Aufhebung  des Körperschaftsteuerbescheides 2016 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Muran Unverricht` (person)
- `Bleischweg 3, 9500 Rennstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Dorothea Grosseholz  in der Beschwerdesache Miroslav Runau,  Neu Amerika 13, 4623 Fernreith, Österreich, über die Beschwerde vom 19. Juni 2019 gegen den Einkommensteuerbescheid  2018 des FA Steiermark Mitte  vom 18. Juni 2019, Steuernummer 89-067/6879, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Dorothea Grosseholz` | `Mag.a Dorothea Grosseholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miroslav Runau` (person)
- `Neu Amerika 13, 4623 Fernreith, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `89-067/6879` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/138120.1`) (sent_id: `deanon_BFG_20260814_TEST/138120.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nadine Tomczack` (person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `15-984/4583` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hemma Mauermair` | `Mag.a Hemma Mauermair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziska Fitzmann` (person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich` (address)
- `Mag. Markus Franz Ganzer` (person)
- `Finanzamtes Österreich` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Diana Sammer` | `Mag. Diana Sammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. KzlR Otto Thiesgen` (person)
- `Gränzing 2, 4841 Brunau, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Zlatan Wetterling, Am Kochfeld 129, 4770 Oberndorf, Österreich, vom 21. November 2019, gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 8. November 2019 betreffend gemäß § 8a FLAG gekürzte  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Christian Doktor` | `Mag. Christian Doktor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zlatan Wetterling` (person)
- `Am Kochfeld 129, 4770 Oberndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Ortner` (person)
- `Mag. Reinhard Krassnig` (person)
- `Komm. Rat Max Stechauner` (person)
- `Dirk Ambrose` (person)
- `Herrnberg 22, 5152 Schönberg, Österreich` (address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-063/4049` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.a Philippa Beßerdich` | `Mag.a Philippa Beßerdich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Simone Philipzig` (person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich` (address)
- `Hofer Leitinger Steuerberatung GmbH` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)
- `59-060/2086` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/138674.1`) (sent_id: `deanon_BFG_20260814_TEST/138674.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_1`)


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

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)


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

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Esmeralda Fietze  in der Beschwerdesache Norbert Hummels,  Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich, über die Beschwerde vom 18. Mai 2022 gegen die Bescheide des Finanzamtes  Österreich vom 25. April 2022 betreffend Gebühren 2021 sowie Gebührenerhöhung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Esmeralda Fietze` | `Mag.a Esmeralda Fietze` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Norbert Hummels` (person)
- `Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Stella Isakovitch, MA, Schnell Vorsäß 7, 8241 Kroisbach, Österreich, über die Beschwerde vom 1. Oktober 2019 gegen den Bescheid  des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 24. September 2019  betreffend Familienbeihilfe 01.2019, Steuernummer 67-354/6576  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stella Isakovitch, MA` (person)
- `Schnell Vorsäß 7, 8241 Kroisbach, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-354/6576` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Petra Özkanli  in der Beschwerdesache des  Betriebes gewerblicher Art Radweg A-Tal des Tourismusverbandes A B, Dornackerstraße 480, 4352 Innernstein, Österreich  vertreten durch StB, über die Beschwerden vom 16. August 2017 gegen die Bescheide des  Finanzamt Wien 2/20/21/22  vom 2. Juni 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Körperschaftsteuer 2016 und Körperschaftsteuer 2016 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2016 wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Petra` — partial — pred is substring of gold: `Dr.in Petra Özkanli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Petra Özkanli`(person)
- `Dornackerstraße 480, 4352 Innernstein, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Richarda Blatzer, Rolfis 18, 5144 Feichten, Österreich, wegen behaupteter Verletzung der  Entscheidungspflicht des Finanzamtes Österreich betreffend die Erlassung eines  Einkommensteuerbescheides für das Veranlagungsjahr 2021 (Steuernummer 32-825/9727  ) beschlossen:   I. Die Säumnisbeschwerde vom 02.09.2022 wird gemäß § 260 Abs. 1 lit. a iVm § 284  Abs. 7 lit. b BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Richarda Blatzer`(person)
- `Rolfis 18, 5144 Feichten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `32-825/9727`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_2`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142978.1`) (sent_id: `deanon_BFG_20260814_TEST/142978.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag.a Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/143380.1`) (sent_id: `deanon_BFG_20260814_TEST/143380.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/146474.1`) (sent_id: `deanon_BFG_20260814_TEST/146474.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/146743.1`) (sent_id: `deanon_BFG_20260814_TEST/146743.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


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

## `representative_person` 🏆

**F1:** 0.044 | **Precision:** 0.392 | **Recall:** 0.024  

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
| 0.392 | 0.024 | 0.044 | 97 | 38 | 59 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 38 | 59 | 1576 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Nußbaumer` | `Mag. Josef Nußbaumer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Heinz Neuner` | `Dr. Heinz Neuner` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `N.N.` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Michael Nierla` | `Mag. Michael Nierla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `N.N.` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)
- `Verwaltungsgerichtshof` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Babette Nimzyk` (person)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Krampl` | `Thomas Krampl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Fabienne Kattner` (person)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Marion Riezinger` | `Mag. Marion Riezinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrich Petrag` (person)
- `Natalie Nodurft` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Finanzamtes  Linz` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ronald Kulenkampf` (person)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Sonja Wennemann` | `Sonja Wennemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Kurt Kreith` | `Mag. Kurt Kreith` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Mag. Sven Weichmann` (person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Christoph Ganahl` | `Dr. Christoph Ganahl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Juliana Untermeier` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Christina Hildegard Stowasser` | `Christina Hildegard Stowasser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Prof. Leander Pfleumer, LLM` (person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich` (address)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `11-306/0925` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Markus Wagner` | `Mag. Markus Wagner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Harald Adriaans` (person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `81-584/4494` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Delila Holsträter, Bakk. iur. BEd, Ziegelsdorf 25, 4723 Unterhörzing, Österreich, vertreten durch Harald Andreas Rumpler, Mattersburgerstraße 70, 7022 Schattendorf,  über die Beschwerde vom 24. September 2018 gegen den Bescheid des Finanzamtes  Österreich vom 22. August 2018 betreffend Einkommensteuer 2016 Steuernummer  76-140/9765  zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Harald Andreas Rumpler` | `Harald Andreas Rumpler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Delila Holsträter, Bakk. iur. BEd` (person)
- `Ziegelsdorf 25, 4723 Unterhörzing, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `76-140/9765` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Anton Fleischhacker` | `Anton Fleischhacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Christine Kralova` (person)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Robert Karl Galler` | `Dr. Robert Karl Galler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Bertha Unverich` (person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich` (address)
- `92-593/4806` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_58`)


U.a. wurde von Dr. Keppert auch die „sogenannte Lenneis-Formel“ bemängelt. Zusätzlich  verweist Dr. Keppert auf die Nichtbeachtung von zukünftigen Ertragssteigerungen durch die  Finanz (vgl. Gegenäußerung der Bf., vertreten durch Dr. Keppert, zur Gegenschrift des UFS an  den VwGH vom Juni 2014 zur Streitsache UFS vom 19.12.2012, Zl. RV/0966-W/05).

| Predicted | Gold |
|---|---|
| `Dr. Keppert` | `Dr. Keppert` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Markus Franz Ganzer` | `Mag. Markus Franz Ganzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hemma Mauermair` (person)
- `Franziska Fitzmann` (person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

| Predicted | Gold |
|---|---|
| `Mag. Gottfried Tazol` | `Mag. Gottfried Tazol` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Delila Frenski` (person)
- `Bairbach 31, 4892 Saxigen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `19-849/6261` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Walther Kendler` | `Walther Kendler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brendon Spade` (person)
- `OMedR Milena Piechulik` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mehmet Köprücü` | `Mehmet Köprücü` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Univ.-Prof. Florian Rouse` (person)
- `Evamaria Watenphul` (person)
- `Allhartsbergerstraße 47, 8142 Kasten, Österreich` (address)
- `Puchheimgasse 14, 6234 Brandenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-456/1644` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Flora Tahir, Sommeregg 24, 9634 Oberbuchach, Österreich, vertreten durch Renate Dolezal, Speisinger Str 50-52 Tür 18, 1130  Wien, über die Beschwerde vom 5. Oktober 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016, Steuernummer 20-636/7581, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Renate Dolezal` | `Renate Dolezal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Flora Tahir` (person)
- `Sommeregg 24, 9634 Oberbuchach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `20-636/7581` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

| Predicted | Gold |
|---|---|
| `Dr. Martin Weiser` | `Dr. Martin Weiser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karoline Windsteig` (person)
- `Heinrich Rzeppa, LLM` (person)
- `Toulagasse 1, 8111 Straßengel, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `52-580/0972` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/143207.1`) (sent_id: `deanon_BFG_20260814_TEST/143207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Linus Frauenstein, Göllerichstraße 41, 9323 Wildbad Einöd, Österreich, vertreten durch Dr. Philip Gruber, Oberer Markt 22, 3631 Ottenschlag, über die  Beschwerde vom 21. Juli 2023 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli  2023 betreffend Grunderwerbsteuer, Steuernummer 70-621/7927, Erfassungsnummer 10- 2023, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Philip Gruber` | `Dr. Philip Gruber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Linus Frauenstein` (person)
- `Göllerichstraße 41, 9323 Wildbad Einöd, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `70-621/7927` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch Mag. Aleksandar Hofstätter, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Aleksandar Hofstätter` | `Mag. Aleksandar Hofstätter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rita Wiersbicki` (person)
- `Corvin Billmaier` (person)
- `Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `23-971/7442` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Prof. Yorick Frühbis` | `Prof. Yorick Frühbis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Hon.-Prof. Denis Hoffjan` (person)
- `Hon.-Prof.in Ariadne Iwanowsky` (person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch Mag. Hedwig Maria Weber, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Hedwig Maria Weber` | `Mag. Hedwig Maria Weber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Thassilo Osipenko` (person)
- `Agatha Stingele` (person)
- `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `39-913/2428` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch Ing. Mag. Dr. Roland Erwin Hansely, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Mag. Dr. Roland Erwin Hansely` | `Ing. Mag. Dr. Roland Erwin Hansely` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Maria Daniel` (person)
- `Diana Wüste` (person)
- `Schönangerweg 35, 4925 Gumpling, Österreich` (address)
- `Zollamtes Österreich` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Paulus Maria Christoph Papst` | `Mag. Paulus Maria Christoph Papst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Jacqueline Traxl` (person)
- `Gebhard Hannig` (person)
- `Nußdorfer Markt 4, 4776 Antersham, Österreich` (address)
- `97-347/7690` (tax_number)
- `FA Braunau Ried Schärding` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/147296.1`) (sent_id: `deanon_BFG_20260814_TEST/147296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Erwin Nikolasen  in der Beschwerdesache Doris Weierstahl,  Minibandlweg 18, 9473 Wunderstätten, Österreich, vertreten durch Kirstin Ever, Minibandlweg 18, 9473 Wunderstätten, Österreich, über die Beschwerde vom  21. Mai 2019 gegen den Bescheid des Finanzamtes Salzburg-Land (nun Finanzamt Österreich)  vom 9. Mai 2019 betreffend Säumniszuschlag 2018, Steuernummer 57-656/9365, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kirstin Ever` | `Kirstin Ever` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Erwin Nikolasen` (person)
- `Doris Weierstahl` (person)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)
- `57-656/9365` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_51`)


Daraus folgt, dass der Einspruch gegen die Strafverfügung vom 3. September 2024 des M,  vertreten durch Pjotr Niessl, wieder unerledigt ist und die belangte Behörde darüber zu  entscheiden hat.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Lydia Stockman  in der Beschwerdesache Kaspar Sadowski,  Sankt Wendelin 50j, 3623 Elsenreith, Österreich, vertreten durch Dr. Franz Deutsch, Pfeilgasse 16/26, 1080 Wien, über die  Beschwerde vom 29. Dezember 2021 gegen den Bescheid des Finanzamtes Österreich vom  22. November 2021 betreffend Einkommensteuer 2019, Steuernummer 96-455/6800, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Franz Deutsch` | `Dr. Franz Deutsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Lydia Stockman` (person)
- `Kaspar Sadowski` (person)
- `Sankt Wendelin 50j, 3623 Elsenreith, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `96-455/6800` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Janosch Postema  in der Beschwerdesache Juri Gübele,  Gartnerweg 4, 5145 Eisenhub, Österreich, vertreten durch Lydia Alberth, Steuerberaterin, Am Hochsteg 13, 8434  Tillmitsch, betreffend die Beschwerde vom 23.4.2025 gegen den Bescheid des Finanzamtes  Österreich vom 28.1.2025 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm  § 111 BAO in Höhe von 1.000,00 Euro beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lydia Alberth` | `Lydia Alberth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Janosch Postema` (person)
- `Juri Gübele` (person)
- `Gartnerweg 4, 5145 Eisenhub, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/149107.1`) (sent_id: `deanon_BFG_20260814_TEST/149107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Emilia Göpfardt, Hundsgrub 5, 4492 Rappersdorf, Österreich, vertreten durch Mag. Dr. Walter Ganster,  Hauptplatz 22, 9100 Völkermarkt, über die Beschwerde vom 6. Dezember 2023 gegen den  Bescheid des Finanzamtes Österreich vom 23. November 2023 betreffend Anspruchszinsen (§  205 BAO) 2021, Steuernummer 17-936/5215, zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Walter Ganster` | `Mag. Dr. Walter Ganster` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dr. Wiebke Peperkorn` (person)
- `Emilia Göpfardt` (person)
- `Hundsgrub 5, 4492 Rappersdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `17-936/5215` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R 1 in der Beschwerdesache PhD OSR Nigel Westerfeld,  Timls 1191a, 8966 Auberg, Österreich, vertreten durch Dr. Michael Kotschnigg, Steuerberater, Stadlauer Straße  39/1/Top 12, 1220 Wien, über   die Beschwerde vom 3. Dezember 2020 gegen die Bescheide des FA 1 vom 12. Oktober 2020  betreffend Umsatz- und Einkommensteuer 2015 zu Steuernummer 06-918/7336  zu Recht  erkannt:   I. Die Beschwerde gegen den Umsatzsteuerbescheid 2015 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Kotschnigg` | `Dr. Michael Kotschnigg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `PhD OSR Nigel Westerfeld` (person)
- `Timls 1191a, 8966 Auberg, Österreich` (address)
- `06-918/7336` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/149201.1`) (sent_id: `deanon_BFG_20260814_TEST/149201.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Sven Pertsch  in der Beschwerdesache Hugo Ossiander,  Streit 58, 5204 Hochfeld, Österreich, vertreten durch Vlado Jovic, Meilstraße 7 Tür 5, 6170 Zirl, betreffend  Beschwerde vom 19. November 2024 gegen den Bescheid des Finanzamt Linz  vom 26. September  2024 betreffend Feststellung der Einkünfte § 188 BAO 2023, Steuernummer 75-331/1938,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm. § 278 Abs. 1 lit a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vlado Jovic` | `Vlado Jovic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sven Pertsch` (person)
- `Hugo Ossiander` (person)
- `Streit 58, 5204 Hochfeld, Österreich` (address)
- `Finanzamt Linz` (organisation)
- `75-331/1938` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_6`)


Zudem fasst das Bundesfinanzgericht durch den Richter Mag. Michael Gleiss in der  Beschwerdesache Sibylle Thalhofer, Fabriksgelände 6, 4923 Mitterberg, Österreich  vertreten durch Mag. Hans Gerald Rainer- Harbach, Burgplatz 6 Tür 3, 9800 Spittal an der Drau, über die Beschwerde vom 25. Juli 2013  gegen den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 25. Juni 2013 betreffend Einkommensteuer 2006, den   Beschluss:  IV. Die Beschwerde wird gemäß § 261 Abs 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Hans Gerald Rainer- Harbach` | `Mag. Hans Gerald Rainer- Harbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Michael Gleiss` (person)
- `Sibylle Thalhofer` (person)
- `Fabriksgelände 6, 4923 Mitterberg, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `Steuerberatungs Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Gosteco Goworek  Steuerberatungs-` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer-` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Heinz Neuböck Wthrd Gmb` — partial — pred is substring of gold: `Heinz Neuböck Wthrd GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Bernhart Steuerberatungs Gmb` — partial — pred is substring of gold: `Bernhart Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Eckert Fries Carter Rechtsanwälte Gmb` — partial — pred is substring of gold: `Eckert Fries Carter Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Anneliese Wäsche`(person)
- `Gernot Kirchenmayer`(person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich`(address)
- `Eckert Fries Carter Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Rechtsanwalt Mag. Peter  Mayerhofer` — partial — gold is substring of pred: `Mag. Peter  Mayerhofer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nina Rasem`(person)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `Mag. Peter  Mayerhofer`(person)
- `Magistrates  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Deloitte Tax  Wirtschaftsprüfungs Gmb` — partial — pred is substring of gold: `Deloitte Tax  Wirtschaftsprüfungs GmbH`

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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

**False Positives:**

- `Proxauf Meyer Zeilinger Rechtsanwälte Gmb` — partial — pred is substring of gold: `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Andrea Helbok`(person)
- `Lydia Rehnen`(person)
- `Roßbergl 5, 4923 Gunzing, Österreich`(address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`(organisation)
- `Finanzamtes  Innsbruck`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Astoria Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Astoria Wirtschaftstreuhand GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kastler Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lisa Lindnau`(person)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich`(address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `35-287/7417`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

**False Positives:**

- `Burka Vitek Moser  Rechtsanwälte` — type mismatch — same span as gold: `Burka Vitek Moser  Rechtsanwälte`

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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs Gmb` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`(person)
- `Julian Gruening`(person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-` — partial — pred is substring of gold: `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`

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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Gutwirth Consulting Steuerberatungs Gmb` — partial — pred is substring of gold: `Gutwirth Consulting Steuerberatungs GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Caroline Toifl Rechtsanwalt Gmb` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Causa Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Causa Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dietmar Hülsmeier  in der Beschwerdesache StR Linn Hochleitner,  Am Schlammteich 131, 4741 Perndorf, Österreich, vertreten durch Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH,  Ötztaler Höhe 11, 6430 Ötztal-Bahnhof, über die Beschwerde vom 31. August 2015 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom 11. August  2015 betreffend Festsetzung von Anspruchszinsen (§ 205 BAO) 2012 und Einkommensteuer  2012, Steuernummer 47-841/9334,  1 ) zu Recht erkannt:   a) Der Beschwerde betr.

**False Positives:**

- `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung Gmb` — partial — pred is substring of gold: `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH`

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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Annemarie Entschev-` — partial — pred is substring of gold: `Annemarie Entschev-Kurzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Julia Reittinger`(person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich`(address)
- `Annemarie Entschev-Kurzmann`(person)
- `Finanzamtes  Österreich`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Astrid Binder`(person)
- `Nadine Tomczack`(person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Finanzamtes Österreich`(organisation)
- `15-984/4583`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hofer Leitinger Steuerberatung Gmb` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Philippa Beßerdich`(person)
- `Simone Philipzig`(person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich`(address)
- `Hofer Leitinger Steuerberatung GmbH`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)
- `59-060/2086`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

**False Positives:**

- `Pschera Steuerberatung Gmb` — partial — pred is substring of gold: `Pschera Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Olivia Severien`(person)
- `Denis Öztopal`(person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich`(address)
- `Pschera Steuerberatung GmbH`(organisation)
- `Finanzamt Salzburg-Stadt`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Kanzlei Kiffman` — partial — pred is substring of gold: `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Olivia Rodenbach`(person)
- `Veit Dworatzeck`(person)
- `Zehentberg 7, 4060 Rufling, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-692/9441`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hofer Leitinger Steuerberatung  Gmb` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Lee Joser, Schafwiesenstraße 6, 8443 Goldes, Österreich, vertreten durch Mag. Antonius Falkner Rechtsanwalt GmbH, Barwies 329, 6414  Mieming, über die Beschwerde vom 23. Dezember 2019 gegen den Bescheid des Zollamtes  Feldkirch Wolfurt vom 26. November 2019 betreffend Sicherheitsleistung zur Zollabgabe,  Einfuhrumsatzsteuer und Verzugszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Antonius Falkner Rechtsanwalt Gmb` — partial — pred is substring of gold: `Mag. Antonius Falkner Rechtsanwalt GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lee Joser`(person)
- `Schafwiesenstraße 6, 8443 Goldes, Österreich`(address)
- `Mag. Antonius Falkner Rechtsanwalt GmbH,`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Janosch Herr  in der Beschwerdesache des  René Schiekel, MSc, Auf der Kröß 1, 2151 Altmanns, Österreich, vertreten durch Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH, Gartenaugasse 3, 3500 Krems/Donau, über die Beschwerde vom 11. Juni 2019 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  Gmb` — partial — pred is substring of gold: `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Janosch Herr`(person)
- `René Schiekel, MSc`(person)
- `Auf der Kröß 1, 2151 Altmanns, Österreich`(address)
- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Revisionssache  Bertram Tienemann, Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über den Antrag des  Revisionswerbers vom 20. April 2023, der Revision vom 20. April 2023 gegen das Erkenntnis  des Bundesfinanzgerichtes vom 6. Dezember 2022, RV/7103133/2013, betreffend  Einkommensteuer 2007 erhobenen außerordentlichen Revision aufschiebende Wirkung  zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Bertram Tienemann`(person)
- `Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141952.1`) (sent_id: `deanon_BFG_20260814_TEST/141952.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Niklas Dankwarth, Schüttaustraße 10, 9753 Raggnitz, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse  17, 1030 Wien, über die Beschwerde vom 24. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. August 2020 betreffend Einkommensteuer 2018  Steuernummer 01-612/4118  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Caroline Toifl Rechtsanwalt Gmb` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Niklas Dankwarth`(person)
- `Schüttaustraße 10, 9753 Raggnitz, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `01-612/4118`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Danielle Mäwius, Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich  vertreten durch Dr. Manfred Arbacher-Stöger,  Wickenburggasse 3/14-15, 1080 Wien, über die Beschwerde vom 30. Dezember 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 15. November 2016 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und Einkommensteuer 2011 bis  2014, Umsatzsteuer und Einkommensteuer 2011 bis 2014, Festsetzung von Anspruchszinsen  2011 bis 2014, über die Beschwerde vom 27. September 2017 gegen die Bescheide des  Finanzamtes Kirchdorf Perg Steyr vom 6. September 2017 betreffend Umsatzsteuer und  Einkommensteuer 2015, gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom  8. September 2017 betreffend Umsatzsteuer und Einkommensteuer 2016, StNr.  06-463/1632, zu Recht erkannt:  I.  Die Beschwerde gegen die Wiederaufnahmebescheide hinsichtlich Umsatzsteuer 2011 bis 2014  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Manfred Arbacher-` — partial — pred is substring of gold: `Dr. Manfred Arbacher-Stöger`

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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin Dr.in  Ri.N. sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beratungs Gmb` — partial — pred is substring of gold: `Beratungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in  Ri.N.`(person)
- `Lena Pahlmann`(person)
- `Esra Voskuhle`(person)
- `Brandstetterweg 76k, 4682 Buchet, Österreich`(address)
- `Beratungs GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143380.1`) (sent_id: `deanon_BFG_20260814_TEST/143380.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Dimitri Nickolmann, Oberkogl 34, 5166 Reith, Österreich, vertreten durch Mag. Thomas Kollaczia-Putz,  Annagasse 3-3A Tür 35, 1010 Wien, über die Beschwerde vom 25. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 19. April 2022 betreffend Aussetzungszinsen 2022,  Steuernummer 82-510/2469, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Thomas Kollaczia-` — partial — pred is substring of gold: `Mag. Thomas Kollaczia-Putz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Dimitri Nickolmann`(person)
- `Oberkogl 34, 5166 Reith, Österreich`(address)
- `Mag. Thomas Kollaczia-Putz`(person)
- `Finanzamtes Österreich`(organisation)
- `82-510/2469`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/143628.1`) (sent_id: `deanon_BFG_20260814_TEST/143628.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaroslaw Hoecker  in der Beschwerdesache Valerius Sülzbrück,  Mariazellerstraße 82, 4210 Unterweitrag, Österreich  nunmehr vertreten durch Steuerberaterin Danielle Tafelmeir, Andelberggasse 58, 4760 Niederham, Österreich, über die  Beschwerde vom 5. Oktober 2017 (Postaufgabetag) gegen den Bescheid des ehemaligen  Finanzamtes Wien 12/13/14 Purkersdorf vom 19. September 2017 betreffend Abweisung eines  Zahlungserleichterungsansuchens, Steuernummer 26-264/5699, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Danielle Tafelmeir` — partial — gold is substring of pred: `Danielle Tafelmeir`

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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Woditschka Steuerberatung Gmb` — partial — pred is substring of gold: `Woditschka Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Mag. Christian Seywald`(person)
- `Johannes Steiner`(person)
- `Michael Kamper MSc`(person)
- `Ulrike Ackermaier, Bakk. iur.`(person)
- `Knödelhüttenstraße 12, 9184 Mühlbach, Österreich`(address)
- `Woditschka Steuerberatung GmbH`(organisation)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `FA Österreich`(organisation)
- `75-013/8302`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Elena Sladek, Metnitztalweg 11, 9572 Gantschach, Österreich, vertreten durch Steuerberaterin Allegra Paulenz, Dornblüthstraße 2, 01277 Dresden,  über die Beschwerde vom 20. Juli 2020 gegen den Bescheid des Finanzamtes Österreich vom  22. Juni 2020 betreffend Feststellungsbescheid über die Nichtveranlagung zur Umsatzsteuer  2019 Steuernummer 61-618/5776  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Allegra Paulenz` — partial — gold is substring of pred: `Allegra Paulenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elena Sladek`(person)
- `Metnitztalweg 11, 9572 Gantschach, Österreich`(address)
- `Allegra Paulenz`(person)
- `Finanzamtes Österreich`(organisation)
- `61-618/5776`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dagobert Rönnecke  in der Revisionssache PhD ÖkR Peter Stankeit,  Im Alauntal 10, 3243 Eselsteiggraben, Österreich  vertreten durch Aigner Rechtsanwalts-GmbH, Lugeck 1-2/Stiege 2/Top 12, 1010  Wien, über den Antrag des Revisionswerbers vom 2.Februar 2024, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 12.Dezember 2023, RV/5100686/2021, betreffend  Einkommensteuer 2019 und die Aufhebung des Einkommenssteuerbescheides 2019  erhobenen außerordentlichen Revision die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Aigner Rechtsanwalts-` — partial — pred is substring of gold: `Aigner Rechtsanwalts-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Dagobert Rönnecke`(person)
- `PhD ÖkR Peter Stankeit`(person)
- `Im Alauntal 10, 3243 Eselsteiggraben, Österreich`(address)
- `Aigner Rechtsanwalts-GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jessica Buddeus  in der Beschwerdesache Heidemarie Helwig,  Schmittengasse 288, 3160 Maierhöfen, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des FA Purkersdorf  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 81-530/8966, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Jessica Buddeus`(person)
- `Heidemarie Helwig`(person)
- `Schmittengasse 288, 3160 Maierhöfen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`(organisation)
- `FA Purkersdorf`(organisation)
- `81-530/8966`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sabrina Ternes  in der Beschwerdesache Sheila Szikorra,  Brennersee 10, 9555 St. Gandolf, Österreich, vertreten durch Auxiliaris Steuerberatung GmbH, Grazer Straße 12, 8480  Mureck, über die Beschwerde vom 11. Jänner 2019 gegen den Bescheid des Finanzamtes  Klagenfurt vom 17. Dezember 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Steuernummer 67-828/8052  zu Recht erkannt:   I. Gemäß § 279 BAO wird die Beschwerde als unbegründet abgewiesen und wird der  angefochtene Bescheid abgeändert.

**False Positives:**

- `Auxiliaris Steuerberatung Gmb` — partial — pred is substring of gold: `Auxiliaris Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Sabrina Ternes`(person)
- `Sheila Szikorra`(person)
- `Brennersee 10, 9555 St. Gandolf, Österreich`(address)
- `Auxiliaris Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `67-828/8052`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Woditschka  Steuerberatung Gmb` — partial — pred is substring of gold: `Woditschka  Steuerberatung GmbH`

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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/145306.1`) (sent_id: `deanon_BFG_20260814_TEST/145306.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden Richter Ri 1, den beisitzenden Richter Ri 2  und die fachkundigen Laienrichter Laienri 1 und Laienri 2 in der Beschwerdesache Herbert Koppen,  Reingrubstraße 15, 4615 Lehen, Österreich, vertreten durch Dr. Felix Karl Vogl Rechtsanwalt GmbH, Bahnhofstraße 34/12,  6780 Schruns, betreffend Beschwerde vom 31. März 2020 gegen den Bescheide des Zollamtes  Feldkirch Wolfurt vom 2. März 2020 betreffend Einfuhrabgaben (GZ_angef. Bescheid) in der  am 1.7.2024 stattgefundenen Sitzung beschlossen:  Der angefochtene Bescheid wird gemäß § 278 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde hinsichtlich der NO und Y9 aufgehoben.

**False Positives:**

- `Dr. Felix Karl Vogl Rechtsanwalt Gmb` — partial — pred is substring of gold: `Dr. Felix Karl Vogl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Herbert Koppen`(person)
- `Reingrubstraße 15, 4615 Lehen, Österreich`(address)
- `Dr. Felix Karl Vogl Rechtsanwalt GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Thassilo Wetekam, Moosen 81, 4926 Kleinbach, Österreich, vertreten durch Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die  Beschwerde vom 12. Juni 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom  13. Mai 2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum  1. Juli 2023 bis 31. Dezember 2023, Steuernummer 89-352/4267, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Thassilo Wetekam`(person)
- `Moosen 81, 4926 Kleinbach, Österreich`(address)
- `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `89-352/4267`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/146305.1`) (sent_id: `deanon_BFG_20260814_TEST/146305.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Türkyilmaz  über den Antrag der Revisionswerberin  Esmeralda Pfanne, Steinplattenweg 5, 8091 Pöllau, Österreich  vertreten durch Rechtsanwalt Mag. Dr. Helmut Blum und  Rechtsanwältin Mag.a Andrea Blum, Mozartstraße 11/6, 4020 Linz, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 21. März 2024, GZ. RV/7102000/2023, betreffend Abweisung  eines Nachsichtsansuchens erhobenen a.o. Revision vom 16. November 2024 aufschiebende  Wirkung zuzuerkennen, den Beschluss gefasst:  Der Antrag wird gemäß § 30 Abs. 2 Verwaltungsgerichtshofgesetz, VwGG, abgewiesen.

**False Positives:**

- `Rechtsanwalt Mag. Dr. Helmut Blum` — partial — gold is substring of pred: `Mag. Dr. Helmut Blum`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Zlatan Türkyilmaz`(person)
- `Esmeralda Pfanne`(person)
- `Steinplattenweg 5, 8091 Pöllau, Österreich`(address)
- `Mag. Dr. Helmut Blum`(person)
- `Mag.a Andrea Blum`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Univ.-Prof. Julian Czernitzki, Faßlergasse 78L-80, 9612 Dellach, Österreich, vertreten durch Schneider Wirtschaftsprüfung und  Steuerberatung GmbH, 6845 Hohenems, Nibelungenstraße 19, über die Beschwerde vom  19.04.2019 gegen die Körperschaftsteuerbescheide 2014, 2015, 2016, gegen die  Umsatzsteuerbescheide 2014, 2015, 2016 (alle Bescheide vom 25.03.2019), gegen die  Bescheide über die Festsetzung von Umsatzsteuer für 12/2017 und 12/2018 vom jeweils  25.03.2019 (Umsatzsteuerbescheid 2017 vom 22.05.2020 und Umsatzsteuerbescheid 2018  vom 17.10.2023), sowie gegen die Haftungsbescheide Kapitalertragsteuer 01/2014, 12/2014,  12/2015, 12/2016 und 12/2017 (Bescheide jeweils vom 21.03.2019), zu Recht erkannt:  I. Der Beschwerde gegen die Körperschaftsteuerbescheide 2015 und 2016, die  Umsatzsteuerbescheide 2015, 2016, 2017 und 2018 wird Folge gegeben.

**False Positives:**

- `Schneider Wirtschaftsprüfung` — partial — pred is substring of gold: `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Univ.-Prof. Julian Czernitzki`(person)
- `Faßlergasse 78L-80, 9612 Dellach, Österreich`(address)
- `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/146743.1`) (sent_id: `deanon_BFG_20260814_TEST/146743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Priv.-Doz. Priv.-Doz. Urs Heinatzky, Feldpichl 19, 8130 Peggau, Österreich, vertreten durch Mag. Beatrix Anna Elfriede  Reiff-Zehetner, Straße der Menschenrechte 11, 2103 Langenzersdorf, über die Beschwerde  vom 30. August 2023 gegen den Bescheid des Finanzamtes Österreich vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zur Steuernummer  51-583/1758  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Beatrix Anna Elfriede  Reiff-` — partial — pred is substring of gold: `Mag. Beatrix Anna Elfriede  Reiff-Zehetner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Priv.-Doz. Priv.-Doz. Urs Heinatzky`(person)
- `Feldpichl 19, 8130 Peggau, Österreich`(address)
- `Mag. Beatrix Anna Elfriede  Reiff-Zehetner`(person)
- `Finanzamtes Österreich`(organisation)
- `51-583/1758`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_1`)


IM NAMEN DER REPUBLIK   Das BFG hat durch die Richterin *** in der Beschwerdesache der Beschwerdeführerin, mit  Adresse X, vertreten durch Dr. Wolfgang Schimek Rechtsanwalt GMBH, Graben 42, 3300  Amstetten, über die Beschwerde vom 23. Juli 2020 gegen die Bescheide des FA Graz-Stadt  (nunmehr Finanzamt Österreich) betreffend die Festsetzung der   Normverbrauchsabgabe 5/2018 und   Kraftfahrzeugsteuer für die Zeiträume 4-12/2018, 1-12/2019 und 1-3/2020   jeweils vom 25. Juni 2020 nach Durchführung einer mündlichen Verhandlung am 12.2.2025 in  Anwesenheit der Schriftführerin SF zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Wolfgang Schimek Rechtsanwalt` — partial — pred is substring of gold: `Dr. Wolfgang Schimek Rechtsanwalt GMBH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Dr. Wolfgang Schimek Rechtsanwalt GMBH,`(organisation)
- `FA Graz-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/148199.1`) (sent_id: `deanon_BFG_20260814_TEST/148199.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Siegbert Anweiler  in der Beschwerdesache Thomas Harasymir,  Gerlosstraße 32, 4694 Aurachkirchen, Österreich, vertreten durch Südsteirische Steuerberatung GmbH, Hauptplatz 7, 8430  Leibnitz, zur Beschwerde vom 4.11.2024 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 10.9.2024 betreffend Feststellung von Einkünften gemäß § 188 BAO für die  Jahre 2021 und 2022 beschlossen:  I. Die Beschwerde wird an das vorlegende Finanzamt für Großbetriebe weiter- bzw  rückgeleitet.

**False Positives:**

- `Südsteirische Steuerberatung Gmb` — partial — pred is substring of gold: `Südsteirische Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegbert Anweiler`(person)
- `Thomas Harasymir`(person)
- `Gerlosstraße 32, 4694 Aurachkirchen, Österreich`(address)
- `Südsteirische Steuerberatung GmbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `Finanzamt für Großbetriebe`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/148316.1`) (sent_id: `deanon_BFG_20260814_TEST/148316.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Elfriede Gehbauer  in der Beschwerdesache Ines Linzenich,  Kriechbaumweg 19, 4912 Wiesen, Österreich, vertreten durch Raiffeisenlandesbank Kärnten - Rechenzentrum und  Revisionsverband, reg. Gen.m.b.H., Raiffeisenplatz 1, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 21. Oktober 2024 gegen die Bescheide des Finanzamtes Österreich vom  3. Oktober 2024 über die Festsetzung eines Verspätungszuschlages betreffend Abgabe einer  Zusammenfassenden Meldung für die Zeiträume 09/2022, 10/2022, 02/2023 und 05/2023,  Steuernummer 53-564/3503, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Raiffeisenlandesbank Kärnten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Elfriede Gehbauer`(person)
- `Ines Linzenich`(person)
- `Kriechbaumweg 19, 4912 Wiesen, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `53-564/3503`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Reinhold Jonasius, Johann Tagwerker-Straße 17, 5760 Pabing, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, über die Beschwerde vom 28.08.2015 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 22. Juni 2015  betreffend Festsetzung der Kapitalertragsteuer 2011 – 2013, Steuernummer 81-937/8981  nach Durchführung einer mündlichen Verhandlung am 31. Jänner 2025 zu Recht erkannt:   I. Der Beschwerde wird als teilweise Folge gegeben.

**False Positives:**

- `Gosteco Goworek  Steuerberatungs-` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/148995.1`) (sent_id: `deanon_BFG_20260814_TEST/148995.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Nicola Fedrich, Fresachergasse 7, 5142 Unterhaunsberg, Österreich  vertreten durch Name Erwachsenenvertreter,  Adresse, (gerichtlicher Erwachsenenvertreter) betreffend die Beschwerde vom 9. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 16. Dezember 2022 betreffend  Aufforderung zur Einreichung von Abgabenerklärungen für das Jahr 2021 zu Steuernummer  54-293/0065  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Name Erwachsenenvertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Nicola Fedrich`(person)
- `Fresachergasse 7, 5142 Unterhaunsberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `54-293/0065`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Michael Gleiss in der Beschwerdesache  Sibylle Thalhofer, Fabriksgelände 6, 4923 Mitterberg, Österreich, vertreten durch Mag. Hans Gerald Rainer-Harbach, Burgplatz 6 Tür  3, 9800 Spittal an der Drau, über die Beschwerde vom 25. Juli 2013 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 25. Juni 2013 betreffend Wiederaufnahme Umsatzsteuer 2006,  Umsatzsteuer 2006 sowie Wiederaufnahme Einkommensteuer 2006 zu Recht erkannt:   I. Die Beschwerde wird betreffend Wiederaufnahme Umsatzsteuer 2006 und  Umsatzsteuer 2006 gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hans Gerald Rainer-` — partial — pred is substring of gold: `Mag. Hans Gerald Rainer-Harbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Michael Gleiss`(person)
- `Sibylle Thalhofer`(person)
- `Fabriksgelände 6, 4923 Mitterberg, Österreich`(address)
- `Mag. Hans Gerald Rainer-Harbach`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/149717.1`) (sent_id: `deanon_BFG_20260814_TEST/149717.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Antonia Thann  in der Beschwerdesache Chen Stöbermann,  Erlaufpromenade 4, 2442 Schranawand, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, betreffend Beschwerde vom 18. Juni 2024 gegen den Bescheid des  Finanzamtes Österreich vom 12. Juni 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 92-334/0161  beschlossen:   Der Vorlageantrag vom 27.01.2025 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Antonia Thann`(person)
- `Chen Stöbermann`(person)
- `Erlaufpromenade 4, 2442 Schranawand, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Finanzamtes Österreich`(organisation)
- `92-334/0161`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Lothar Kriwet, Gaugen 11, 9150 Draurain, Österreich, vertreten durch Spiss Steuerberatung GmbH,  Timmlerweg 16, 6580 St. Anton am Arlberg, über die Beschwerde vom 31. Oktober 2025 gegen  die Bescheide des Finanzamtes Österreich vom 15. Oktober 2025 betreffend   1. Verzinsung gemäß § 16 COFAG-NoAG (Fixkostenzuschuss I),  2.

**False Positives:**

- `Spiss Steuerberatung Gmb` — partial — pred is substring of gold: `Spiss Steuerberatung GmbH`

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
| 0.000 | 0.000 | 0.000 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 24 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_15`)


Hinsichtlich des Unternehmens X.d.o.o. sei Herr A. auf einer Baustelle auf den Beschuldigten zugekommen und habe nach Arbeit gefragt und erklärt, dass er für eine slowenische Firma tätig sei.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_40`)


------ Gegen dieses Erkenntnis des Spruchsenates richtet sich die vorliegende frist- und formgerechte Beschwerde des Amtsbeauftragten vom 7.1.2019, in der wie folgt ausgeführt wird: "Herr N.N., geb. am Datum, wohnhaft in Adresse1, hat vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bewirkt, dass festzusetzende Abgaben zu niedrig festgesetzt wurden sowie vorsätzlich Lohnabgaben nicht spätestens am fünften Tag nach Fälligkeit entrichtet (abgeführt).

**False Positives:**

- `N $2.` — positional overlap with gold: `N.N.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_110`)


Zu den Eingangsrechnungen der Fa. X. d.o.o an das Einzelunternehmen N.N. in den Jahren 2012 und 2013 und Vorhalt Zeugenaussage B. A. vom 4.9.2018, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa.  X. d.o.o erbracht worden seien, führte der Beschuldigte aus, Herr A. habe eigenständig eine Firma in Slowenien gegründet und sei mit dieser Firma zu ihm gekommen und habe um Aufträge ersucht.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `N.N.`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_111`)


Er habe mit der Firmengründung in Slowenien nichts zu tun gehabt, auch habe er das Stammkapital iHv € 7.500,00 für die Gründung in Slowenien nicht zur Verfügung gestellt. Herr A. habe auch eigene Beschäftigte auf seinen Baustellen eingesetzt.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_115`)


Seite 11 von 21 Auf die Frage warum der Beschuldigte glaube, dass Herr A. ihn unter der Strafdrohung einer unrichtigen Zeugenaussage belaste, führte der Beschuldigte aus, dass er annehme, dass sich A. wahrscheinlich selbst reinwaschen habe wollen.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_181`)


Es ist aufgrund des vorliegenden Sachverhalts davon auszugehen, dass Herr A. seine Arbeitskraft geschuldet hat und somit ein Dienstverhältnis anzunehmen ist.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_182`)


Dafür sprechen auch folgende Tatsachen: Das zu verarbeitende Material sowie das benötigte Werkzeug wurden von der Fa. N. zur Verfügung gestellt. Herr A. wurde im gesamten Prüfungszeitraum mtl. mit € 1.300,00 entlohnt.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_49`)


Herr F übertrug von Todes wegen unentgeltlich dieses  Sonderbetriebsvermögen (Baurechtseinlage EZ 2 KG XY) der Wohlgemut Getränke GmbH& Co KG bei gleichzeitiger  Zuwendung von 100% der Mitunternehmeranteile der Wohlgemut Getränke GmbH& Co an Frau A. Der Begriff  Sonderbetriebsvermögen  in § 3 Abs. 1 Z 2 lit a zweiter Teilstrich GrEStG ist ertragsteuerlich zu definieren.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)
- `Wohlgemut Getränke GmbH&`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_28`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 10/2012  Frau M.P. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

**False Positives:**

- `M $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_176`)


Frau M. P. ist voraussichtlich nicht dauernd außerstande, sich selbst den Unterhalt zu  verschaffen.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_217`)


Schließlich kann nach Ansicht des Bundesfinanzgerichtes auch durch die Einvernahme der  Tante des Bf. (Frau D.) als Zeugin nichts für die Feststellung gewonnen werden, ob beim Bf. die  Erwerbsunfähigkeit bereits vor dem 21.

**False Positives:**

- `D $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_56`)


Zum Nachweis dessen legte die bf. Vertreterin den Leistungsbericht des betreuenden  Sachbearbeiters der Kanzlei und einer Mitarbeiterin Frau H. bei.

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_60`)


sei der Postausgang im kanzleieigenen EDV-Programm (BMD) von Frau L. erfasst und die  Gebühren dem Kunden verrechnet worden.

**False Positives:**

- `L $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_62`)


Die Beschwerde wurde mit dem Einschreibzettel  (Einschreibvignette) versehen und von Frau L. (Mitarbeiterin der Kanzlei) als pdf- Datei  archiviert worden.

**False Positives:**

- `L $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_38`)


Obmann ist  Herr B.  Der Bf ist Alleineigentümer der unbelasteten Liegenschaft an der Grundstücksadresse in  Grundstücksadresse

**False Positives:**

- `B $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Bernett`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_75`)


Gesellschafter der BF im Jahr 2013 war Herr S.  Die Fa. I wurde von Herrn DO und Herrn KW im Jahr 2001 gegründet.

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_20`)


Das Ermittlungsverfahren habe ergeben, dass ein Ausweis gemäß § 29b mit der Nummer 123  für Frau N., ausgestellt worden sei.

**False Positives:**

- `N $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_21`)


Auf Nachfrage beim Sozialministeriumservice, 1010 Wien,  sei der Behörde mitgeteilt worden, dass der für Frau N. ausgestellte Ausweis zum  Beanstandungszeitpunkt keine Gültigkeit mehr besessen habe, da dieser bis 1. August 2020  befristet gewesen sei.

**False Positives:**

- `N $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_88`)


In der Mail vom 29.05.2018 habe der StV an die Versicherung folgendes Ersuchen gerichtet:  „Da Herr T.. VN Fn gerne eine Einmalzahlung von der GmbH haben möchte, würde ich  den kapitalisierten Betrag aus der zugesagten Pension in Höhe von € 1.452 (lt.  Pensionszusage vom 1.6.2006) benötigen.

**False Positives:**

- `T $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_46`)


Im Zuge eines Telefonats hat sich der Sachverhalt  aufgeklärt und der zuständige Bearbeiter Herr K. (BV-Team 23, Finanzamt1/23) hat den  bekämpften Bescheid noch am selben Tag mit Mail vom 17.03.2022 an uns gesandt.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/147275.1`) (sent_id: `deanon_BFG_20260814_TEST/147275.1_10`)


Erst nach dem Urteil hätte der Beschwerdeführer die Kaufverträge erhalten – von Frau A.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_22`)


Begründung – GdB liegt rückwirkend vor:  kein GdB ab aktuellem Untersuchungsdatum   50%: entsprechend VGA  Herr S. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:   NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Da keine Befunde vorgelegt wurden, kann die Erwerbsfähigkeit nicht beurteilt werden.

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_77`)


Herr S. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Es bestehen weder fachärztlich-psychiatrische Behandlungen noch Psychotherapien, eine  medikamentöse Dauertherapie wird nicht eingenommen, sodass ein Leiden, das nicht  behandlungswürdig erscheint, vorliegt, sodass das vorliegende Leiden keine  Erwerbsunfähigkeit begründet.

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `generic_title_initial_person` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 12 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_44`)


siehe dazu auch EuGH 28.7.2007,  C-73/06, Planzer Luxembourg Sari).

**False Positives:**

- `Planzer Luxembourg Sari` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_59`)


siehe dazu auch EuGH 28.7.2007,  C-73/06, Planzer Luxembourg Sari).

**False Positives:**

- `Planzer Luxembourg Sari` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_362`)


Nachteile bei der mittelbaren Besteuerung haben (v.a. mit Verweis auf EuGH 9.3.2006,  C-493/04 Piatkowski und EuGH 14.2.1995, C-279/93, Schuhmacker).

**False Positives:**

- `Schuhmacker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_367`)


Die Anwendung des  Progressionsvorbehaltes auf die deutsche Sozialversicherungsrente verstoße nicht gegen das  Gemeinschaftsrecht (mit Verweis auf VwGH 14.12.2006, 2005/14/0099 sowie  EuGH 12.07.2005, Rs C-403/03, Schempp und EuGH 15.07.2004, C-365/02, Lindfors).

**False Positives:**

- `Lindfors` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_214`)


Dies gilt auch für die Fälle der  Vorsteuererstattung an ausländische Unternehmer (vgl. EuGH 15.3.2007, C-35/05, Rn. 27,  Reemtsma , sowie EuGH 13.12.1989, C-342/87, Genius Holding, Rn. 15).

**False Positives:**

- `Rn` — no gold match — likely missing annotation
- `Genius Holding` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_164`)


Verhindert die  Nichterfüllung der formalen Anforderungen (namentlich die Nennung des tatsächlichen  Leistungserbringers) die Überprüfung des Vorliegens der materiellen Voraussetzungen für den  Vorsteuerabzug, ist der Vorsteuerabzug nicht zu gewähren (EuGH 11.11.2021, C-281/20, Rs  Ferimet, Rn 27 und 37;

**False Positives:**

- `Rs  Ferimet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_154`)


Dies liegt im vorliegenden Fall vor: Zwar ist der Buchnachweis und der Nachweis der  Beförderung bzw Versendung nach der Rechtsprechung des EuGH keine materielle  Voraussetzung für die Steuerfreiheit der innergemeinschaftlichen Lieferung (siehe zB  Ruppe/Achatz, UStG6 [2024] Art 7 BMR Rz 24 mit Hinweis auf EuGH 27.9.2007, C-146/05, Collée  [Buchnachweis] sowie Ruppe/Achatz, UStG6 [2024] Art 7 BMR Rz 26 mit Hinweis auf EuGH  6.9.2012, C-273/11, Mecsek-Gabona);

**False Positives:**

- `Coll` — no gold match — likely missing annotation
- `Mecsek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_156`)


Die Steuerbefreiung steht nämlich vielmehr auch  dann zu, wenn der Nachweis zwar nicht ordnungsgemäß erbracht wird, jedoch feststeht, dass  die Voraussetzungen einer innergemeinschaftlichen Lieferung vorliegen (siehe zB  Ruppe/Achatz, UStG6 [2024] Art 7 BMR Rz 24/1 [Buchnachweis] bzw Ruppe/Achatz, UStG6  [2024] Art 7 BMR Rz 26 mit Hinweis auf EuGH 6.9.2012, C-273/11, Mecsek-Gabona  [Beförderungsnachweis]).

**False Positives:**

- `Mecsek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_188`)


Zwar sind, wie bereits bei Punkt 3.1.2. ausgeführt, Buchnachweis und Nachweis der  Beförderung bzw Versendung nach der Rechtsprechung von EuGH und VwGH keine  materiellen Voraussetzungen für die Steuerfreiheit der innergemeinschaftlichen Lieferung  (siehe zB Ruppe/Achatz, UStG6 [2024] Art 7 BMR Rz 24 mit Hinweis auf EuGH 27.9.2007, C- 146/05, Collée und VwGH 19.12.2018, Ra 2017/15/0064 [Buchnachweis] sowie Ruppe/Achatz,  UStG6 [2024] Art 7 BMR Rz 26 mit Hinweis auf EuGH 6.9.2012, C-273/11, Mecsek-Gabona  [Nachweis der Beförderung bzw Versendung]).

**False Positives:**

- `Mecsek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_208`)


Im Ergebnis kann nach Ansicht des Bundesfinanzgerichts und im Sinne der Rechtsprechung des  EuGH (EuGH 27.9.2007, C-409/04, Teleos u.a., vgl auch VwGH 27.4.2016, 2013/13/0051) somit  nicht behauptet werden, dass die Bf alle ihr „zur Verfügung stehenden zumutbaren  Maßnahmen ergriffen hat“, um sicherzustellen, dass die vorgenommene  innergemeinschaftliche Lieferung nicht zur Beteiligung an einer Steuerhinterziehung führt (für  den verfahrensgegenständlichen Sportwagen, der letztlich im Februar 2007 erstmalig  angemeldet wurde, ist bislang keine Umsatzsteuer entrichtet worden).

**False Positives:**

- `Teleos` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)

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

</details>

---

<details>
<summary>❌ False Negatives (1084, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des **Rocco Choudhury**, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

- missed: `Rocco Choudhury` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)

Befund Psychiater **Dr. Mersch** 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

- missed: `Dr. Mersch` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)

Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr **Katharina Bauckholt** (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

- missed: `Katharina Bauckholt` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für **Hartmut Groebmair**  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hartmut Groebmair` (person)
- predicted in sentence: `Leonhard Osskinat`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Sascha de Kort**  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof.in Sascha de Kort` (person)
- predicted in sentence: `Matthew Mc`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)

Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der **Bodo Saday**, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Bodo Saday` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau **Nina Rasem**, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

- missed: `Nina Rasem` (person)
- predicted in sentence: `Rechtsanwalt Mag. Peter  Mayerhofer`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_117`)

Gegenstand des Unternehmens ist gemäß § 2 des Gesellschaftsvertrages der Erwerb  und der Betrieb des Schiffes "**MT**".

- missed: `MT` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_5`)

Mit Erinnerungsschreiben vom 6.11.2021 forderte das Finanzamt die **Herta Lindgens** (=  Beschwerdeführerin, Bf) dazu auf, die "Erstmeldung oder Meldung nach Fälligkeit der  jährlichen Überprüfung der wirtschaftlichen Eigentümer entsprechend den Bestimmungen des  § 5 Wirtschaftliche Eigentümer Registergesetz (WiEReG)" bis spätestens 28.12.2021  nachzuholen.

- missed: `Herta Lindgens` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)

LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin **Dr. Mairinger** 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

- missed: `Dr. Mairinger` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_133`)

Bei **Dr. 2** war ich auch, die mir die Befunde nicht mehr zurückgeben  wollte.

- missed: `Dr. 2` (person)
- predicted in sentence: —

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache **Eleonore Sawadzki, Bakk. art.**, Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

- missed: `Eleonore Sawadzki, Bakk. art.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`, `Eleonore Sawadzki`

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. **Ing.Ing. Bertram Hennlein** ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_73`)

Die zuständige EU- Sozialkommissarin Marianne **Thyssen** hatte Österreichs Pläne in der Vergangenheit wiederholt  kritisch beurteilt und vor einer Diskriminierung gewarnt.

- missed: `Thyssen` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_163`)

Angewandte Mathematik (schriftlich)   genügend   Wirtschaftsinformatik (mündlich)    befriedigend     Sommertermin Mai 2023:   Diplomarbeit     Herbsttermin Oktober 2024:   Diplomarbeit   „… **Luna Schaffrath** (hat) die Diplomarbeit zur Reife- und Diplomprüfung am 06.09.2024  abgegeben … und am 15.10.2024 positiv abgeschlossen“ (Bestätigung vom 11.04.2025).

- missed: `Luna Schaffrath` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_57`)

Sie ging zu **KzlR Gregor Scholt, BA** einem Chirurg der wollte ihr einen Nadel reinstecken, sie  wurde dort festgehalten.

- missed: `KzlR Gregor Scholt, BA` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dietmar Hülsmeier  in der Beschwerdesache **StR Linn Hochleitner**,  Am Schlammteich 131, 4741 Perndorf, Österreich, vertreten durch Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH,  Ötztaler Höhe 11, 6430 Ötztal-Bahnhof, über die Beschwerde vom 31. August 2015 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom 11. August  2015 betreffend Festsetzung von Anspruchszinsen (§ 205 BAO) 2012 und Einkommensteuer  2012, Steuernummer 47-841/9334,  1 ) zu Recht erkannt:   a) Der Beschwerde betr.

- missed: `StR Linn Hochleitner` (person)
- predicted in sentence: `Dr. Dietmar Hülsmeier`, `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung Gmb`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Techn R RgR Jeffrey Geippel, Dirisam 63, 2813 Pregart, Österreich, über die Beschwerde vom 3. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 2. Mai 2022 betreffend Einkommensteuer 2019  Steuernummer 84-874/5640  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut-`

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_22`)

In einer Besprechung vom 16.1.2015 hat Herr **Dr. F** zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Hon.-Prof. Hagen Atar**  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Hon.-Prof. Hagen Atar` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_22`)

Festgestellt Sachverhalt   Der Beschwerdeführer ist Vater von OStR Priv.-Doz. Theodor Voelpel  und **Herbert Schaffarik**  und lebte dieser im Jahr  2020 bis zum 08. Jänner mit der Mutter der beiden Söhne, mit der der Beschwerdeführer auch  verheiratet war, sowie den beiden Kindern in einem gemeinsamen Haushalt. Am 08. Jänner zog  die Mutter zusammen mit dem Sohn Herbert Schaffarik  aus dem gemeinsamen Haushalt aus.

- missed: `Herbert Schaffarik` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)

GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen **N.N.**, Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `N.N.` (person)
- predicted in sentence: `Mag. Michael Nierla`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn **Dipl.-Ing. Astrid Gänsl**, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

- missed: `Dipl.-Ing. Astrid Gänsl` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende **Dr. Anna Radschek**, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Anna Radschek` (person)
- predicted in sentence: `Kira Lentze`, `Woditschka  Steuerberatung Gmb`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)

Sollte Herr **Nadine Millradt**  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

- missed: `Nadine Millradt` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter **Dr. Hans Blasina** in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

- missed: `Dr. Hans Blasina` (person)
- predicted in sentence: `Ingrid Dohrmaier`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)

Als  Geschäftsführer fungierte im Streitzeitraum Dipl. **Ing.Ing. Bertram Hennlein**  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142534.1`) (sent_id: `deanon_BFG_20260814_TEST/142534.1_5`)

Entscheidungsgründe  Die ursprüngliche Beschwerdeführerin (kurz: Bf), die **Kurt Nicklaß**, FN-b, wurde – laut  Firmenbuch - mit Umwandlungsvertrag vom 30.06.2021 gemäß § 5 UmwG unter gleichzeitiger  Errichtung der Personengesellschaft H-KG, FN-s, umgewandelt.   Das gegenständliche Erkenntnis ergeht daher an die H-KG als Rechtsnachfolgerin der Bf.  I. Verfahrensgang  Mit Gebührenbescheid vom 11.04.2014 wurde die Bestandvertragsgebühr gemäß § 33 TP 5  GebG für den am 05.09.2013 abgeschlossenen Pachtvertrag zwischen der Bf, als Verpächterin,  1 von 10 Seite 2 von 10

- missed: `Kurt Nicklaß` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_5`)

Das Einkommen des Gruppenmitgliedes **Cathleen Gottschlag**  im Jahr 2016 wird mit -189.109,60 Euro  (Verlust) festgesetzt.

- missed: `Cathleen Gottschlag` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_41`)

des Neve College for Woman nicht in Israel aufgehalten habe) nicht widersprochen, weshalb  die durchgehende Anwesenheit von **Heidemarie Fitzenreiter**  in Israel für Zwecke des College-Besuches  vom Bundesfinanzgericht als erwiesen angenommen wird.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  **Mag. Monika Ahorn** sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Fabian Kohnke, Hammersdorfstraße 78, 4223 Lungitz, Österreich, vertreten durch Intercura  Treuhand- und Revisionsgesellschaft m.b.H., Bösendorferstraße 2, 1010 Wien, über die  Beschwerde vom 14. Dezember 2018 gegen die Bescheide des Finanzamtes Wien 1/23 vom  16. November 2018 betreffend Haftung Lohnsteuer, Festsetzung Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag sowie Säumniszuschläge jeweils 2015 bis 2017  (Steuernummer 14-263/3594 ) nach Durchführung einer mündlichen Verhandlung am  21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Monika Ahorn` (person)
- predicted in sentence: `Fabian Kohnke`, `Intercura  Treuhand-`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)

Und weiter: „[…]  hätte Herr **Quentin Schwartkopp**  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. David Hell LL.B. LL.M.** in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Mag. David Hell LL.B. LL.M.` (person)
- predicted in sentence: `Mag. David Hell`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des **Günter Gopfauf**, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

- missed: `Günter Gopfauf` (person)
- predicted in sentence: `Dr. Maria-`

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147139.1`) (sent_id: `deanon_BFG_20260814_TEST/147139.1_64`)

Darauf hinzuweisen ist, dass die erwähnte Beilage zur  Einkommensteuererklärung von der auf die steuerliche Behandlung von Kryptowährungen  spezialisierten Steuerberatungskanzlei **Techn R Silvana Zeika**  verfasst wurde.

- missed: `Techn R Silvana Zeika` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Univ.-Prof. Univ.-Prof. Kai Menrath**  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof. Univ.-Prof. Kai Menrath` (person)
- predicted in sentence: `Wigand Maczkiewicz`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_36`)

Dass **Heidemarie Fitzenreiter**  vom 05.09.2022 bis 31.05.2023 Studentin des Neve College for Woman  (Jerusalem) gewesen ist, ergibt sich aus der im Akt befindlichen Bestätigung des Neve College  for Woman vom 25.06.2023 (Anmerkung: Ursprünglich war offenbar ein Besuch des Neve  College for Woman bis 14.06.2023 geplant, was sich aus einer ebenfalls aktenkundigen, am  19.09.2022 vom Neve College for Woman ausgestellten Bestätigung ergibt).

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)

Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau **Freßdorf** doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

- missed: `Freßdorf` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache **OMedR Frauke Klutzuweit**, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `OMedR Frauke Klutzuweit` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142826.1`) (sent_id: `deanon_BFG_20260814_TEST/142826.1_2`)

Das Bundesfinanzgericht hat durch den Richter **Priv.-Doz. Bodo Bookhold**  in der Beschwerdesache Samuel Haßelbarth,  Zeilberg 4, 3233 Bühren, Österreich, über die Beschwerde vom 02.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 28.05.2021, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Priv.-Doz. Bodo Bookhold` (person)
- predicted in sentence: `Samuel Haßelbarth`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_231`)

Der Kanzler informierte dabei  gemeinsam mit Gesundheitsminister Rudolf Anschober, dem steirischen Landeshauptmann  Hermann Schützenhöfer, dem Wiener Bürgermeister Michael Ludwig und **Univ.-Prof. Dr.  Oswald Wagner**, Vizerektor der Medizinischen Universität Wien und Leiter des klinischen  Institutes für Labormedizin, über die weitere Vorgehensweise in der Corona-Krise.

- missed: `Univ.-Prof. Dr.  Oswald Wagner` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_92`)

Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  1.12.1980, ärztlicher Befund der Stellungskommission Wien: Nervosität, Asthenie, **M.**  Scheuermann.

- missed: `M.` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_11`)

Mit Strafverfügung vom 12.3.2019 lastete der Magistrat der Stadt Wien, Magistratsabteilung  67, **Techn R Tosca Häfeli**, in der Folge kurz mit Bf. bezeichnet, folgende Verwaltungsübertretung an:  "1. Datum/Zeit:  06.06.2018, 09:29 Uhr   Ort:   TATORT   betroffenes Fahrzeug: KENNZ (A)   Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den   Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder   Wochenpauschalkarte) gesorgt zu haben, da der im Fahrzeug angebrachte   Parkausweis für Behinderte gemäß § 29b der StVO kein Original war.

- missed: `Techn R Tosca Häfeli` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)

Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - **Prof. Dr. Franz Leidenmühler**" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

- missed: `Prof. Dr. Franz Leidenmühler` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Mirha Karahodzic MA** in der  Beschwerdesache Hon.-Prof. Justin Jacobeit, Gasthaus Kugelwiese 12, 3841 Markl, Österreich, vertreten durch Schmitt & Schmitt  Wirtschaftstreuhand- gesellschaft m.b.H., Strohgasse 25, 1030 Wien, über die Beschwerde vom  11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 28. April 2022,  Steuernummer 67-100/8891, betreffend Einkommensteuer 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Mirha Karahodzic MA` (person)
- predicted in sentence: `Mag. Mirha Karahodzic`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)

in der Verwaltungsstrafsache gegen  **Detlev Griessmer**, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

- missed: `Detlev Griessmer` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des **Shoshana Döllmann**, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

- missed: `Shoshana Döllmann` (person)
- predicted in sentence: `Mag. Andrea Müller-`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Lisa Fries in der Beschwerdesache  **Piedro Ringelsbacher, BEd**, Hollehnerweg 53, 2565 Schwarzensee, Österreich, über die Beschwerde vom 30. August 2023 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 6, Referat Parkometerabgabe und  Abgabenstrafen, vom 11. August 2023 betreffend Parkometerabgabe zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Piedro Ringelsbacher, BEd` (person)
- predicted in sentence: `Mag. Lisa Fries`, `Piedro Ringelsbacher`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache **RgR Tanja Tihl, BSc**,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `RgR Tanja Tihl, BSc` (person)
- predicted in sentence: —

</details>

---

