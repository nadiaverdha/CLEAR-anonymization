# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-25T20:28:59.626862

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
| True Positives | 630 |
| False Positives | 422 |
| False Negatives | 984 |
| Total Gold Entities | 1614 |
| Micro Precision | 59.9% |
| Micro Recall | 39.0% |
| Micro F1 | 47.3% |
| Macro F1 | 47.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `names_after_legal_roles_general` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `names_in_complaint_context_general` | 20.5% | 80.5% | 11.8% | 236 | 190 | 46 |
| `legal_titles_with_names` | 35.5% | 72.0% | 23.5% | 528 | 380 | 148 |
| `names_after_herrn_frau` | 6.7% | 37.8% | 3.7% | 156 | 59 | 97 |
| `names_in_address_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_after_legal_roles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_after_bf_or_representative` | 0.0% | 0.0% | 0.0% | 110 | 0 | 110 |
| `standalone_names_in_legal_context` | 0.0% | 0.0% | 0.0% | 21 | 0 | 21 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `names_after_legal_roles_general` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Alexander Schnelldorfer` | `Alexander Schnelldorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

</details>

---

## `names_in_complaint_context_general` 🏆

**F1:** 0.205 | **Precision:** 0.805 | **Recall:** 0.118  

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
| 0.805 | 0.118 | 0.205 | 236 | 190 | 46 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 190 | 46 | 1424 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Eligüzel` | `Chantal Eligüzel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Quentin Girharz` | `Quentin Girharz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Kandler` (person)
- `FA Landeck Reutte` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Jörg Kuhstoss, Hasenberg 58, 3240 Grub bei Kilb, Österreich, über die Beschwerde vom 3. April 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 70-705/2274  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jörg Kuhstoss` | `Jörg Kuhstoss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hasenberg 58, 3240 Grub bei Kilb, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `70-705/2274` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter [Richter] in der Beschwerdesache Shirley Adamczewski,  Stein 26, 9313 Töplach, Österreich, über die Beschwerde vom 13. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 30. Juni 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Februar bis Dezember 2020 zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shirley Adamczewski` | `Shirley Adamczewski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stein 26, 9313 Töplach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Muran Unverricht, Bleischweg 3, 9500 Rennstein, Österreich, über die Beschwerden vom 28. Oktober 2018, vom 9. Februar 2019  und vom 7. Februar 2020 gegen die Bescheide des Finanzamtes Österreich vom 26. Juli 2018  betreffend Abweisung eines Antrages auf Aufhebung des Körperschaftsteuerbescheides 2016  sowie vom 31. Jänner 2019 und vom 16. Jänner 2020 betreffend Körperschaftsteuer 2017 und  2018 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Abweisung eines Antrages auf Aufhebung  des Körperschaftsteuerbescheides 2016 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Muran Unverricht` | `Muran Unverricht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Bleischweg 3, 9500 Rennstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Maurice Speckner,  Hinterweg 94, 2305 Pframa, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 88-902/6713  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Maurice Speckner` | `Maurice Speckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterweg 94, 2305 Pframa, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-902/6713` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Roderich Stenczel, St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich, über die Beschwerde vom 20. August 2013 gegen die Bescheide  des FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Wiederaufnahme gemäß § 303 BAO  der Körperschaftsteuerbescheide 2008 bis 2010, Steuernummer 60-379/9146  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Stenczel` | `Roderich Stenczel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `60-379/9146` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Dorothea Grosseholz  in der Beschwerdesache Miroslav Runau,  Neu Amerika 13, 4623 Fernreith, Österreich, über die Beschwerde vom 19. Juni 2019 gegen den Einkommensteuerbescheid  2018 des FA Steiermark Mitte  vom 18. Juni 2019, Steuernummer 89-067/6879, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Miroslav Runau` | `Miroslav Runau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Dorothea Grosseholz` (person)
- `Neu Amerika 13, 4623 Fernreith, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `89-067/6879` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Nadine Tomczack` | `Nadine Tomczack` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `15-984/4583` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Heike Lohoff, Odescalchigasse 154, 4264 Lichtenau, Österreich, vertreten durch Vertreter, AdrVertreter, über die Beschwerde vom 15. Juli 2015 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr:  Finanzamt Österreich) vom 6. Juli 2015 betreffend Grunderwerbsteuer, Steuernummer  77-421/3532, Erfassungsnummer 10-2012, nach Durchführung von mündlichen  Verhandlungen am 13.10.2021 und 10.08.2022 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heike Lohoff` | `Heike Lohoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Odescalchigasse 154, 4264 Lichtenau, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `77-421/3532` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dirk Ambrose` | `Dirk Ambrose` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elisabeth Hafner` (person)
- `Mag. Dieter Ortner` (person)
- `Mag. Reinhard Krassnig` (person)
- `Komm. Rat Max Stechauner` (person)
- `Herrnberg 22, 5152 Schönberg, Österreich` (address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-063/4049` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Wieland Nieß, Primau 14, 2813 Spratzau, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 20. Februar 2020 gegen  den Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln vom 29. Jänner 2020 betreffend  Einkommensteuer 2018, Steuernummer 72-272/3022, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Nieß` | `Wieland Nieß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Primau 14, 2813 Spratzau, Österreich` (address)
- `Ernst & Young Steuerberatungs- gesellschaft  m.b.H.` (organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `72-272/3022` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yelec Tummascheit  in der Beschwerdesache Gerda Staigl,  Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich, über die Beschwerde vom 11.08.2022 gegen den Bescheid des Finanzamtes  Österreich vom 05.08.2022, Steuernummer 64-583/4801, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gerda Staigl` | `Gerda Staigl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Yelec Tummascheit` (person)
- `Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `64-583/4801` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Hadenfelt` | `Susette Hadenfelt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak` (person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich` (address)
- `Huber & Rosenthal Steuerberatung KG` (organisation)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `34-724/8270` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für Hartmut Groebmair  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Leonhard Osskinat` | `Leonhard Osskinat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schreyvogelgasse 2V, 8262 Leithen, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)
- `Hartmut Groebmair` (person)
- `39-801/9564` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Esmeralda Fietze  in der Beschwerdesache Norbert Hummels,  Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich, über die Beschwerde vom 18. Mai 2022 gegen die Bescheide des Finanzamtes  Österreich vom 25. April 2022 betreffend Gebühren 2021 sowie Gebührenerhöhung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Norbert Hummels` | `Norbert Hummels` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Esmeralda Fietze` (person)
- `Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Stella Isakovitch, MA, Schnell Vorsäß 7, 8241 Kroisbach, Österreich, über die Beschwerde vom 1. Oktober 2019 gegen den Bescheid  des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 24. September 2019  betreffend Familienbeihilfe 01.2019, Steuernummer 67-354/6576  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stella Isakovitch, MA` | `Stella Isakovitch, MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Schnell Vorsäß 7, 8241 Kroisbach, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-354/6576` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dietlind Döbereiner  in der Beschwerdesache Siegbert Ptasnik,  Kleinseeweg 4, 6341 Ebbs, Österreich, über die Beschwerden vom 25. September 2015 gegen die Bescheide des  Finanzamtes Linz vom 20. August 2015 betreffend Einkommensteuer 2009 - 2014 und  Umsatzsteuer 2009 - 2014 sowie Einkommen- und Umsatzsteuerbescheid 2015 jeweils vom  19.07.2017 und Einkommen –und Umsatzsteuerbescheid 2016 vom 20.07.2017 zu Recht  erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2009, 2010, 2011, 2015 sowie  gegen die Umsatzsteuerbescheide 2009-2016 werden gemäß § 279 BAO als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Siegbert Ptasnik` | `Siegbert Ptasnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dietlind Döbereiner` (person)
- `Kleinseeweg 4, 6341 Ebbs, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die beisitzende Richterin Ria  sowie die fachkundigen Laienrichter KR 1 und 2 in der Beschwerdesache Mona Modlmayr, Paul Hörbiger-Straße 16, 4844 Lixlau, Österreich, vertreten durch BONAFIDE Treuhand- und Revisions- gesellschaft m.b.H., Berggasse  10, 1090 Wien, über die Beschwerde vom 16. Juli 2018 gegen den Bescheid des Finanzamtes  Österreich vom 2. Juli 2018 betreffend Einkommensteuer 2017 Steuernummer  34-594/0695  nach Durchführung einer mündlichen Verhandlung am 13. Oktober 2022 in  Anwesenheit der Schriftführerin S zu Recht erkannt:   Der Bescheid betreffend Einkommensteuer 2017 wird zu Ungunsten der Bf. abgeändert.

| Predicted | Gold |
|---|---|
| `Mona Modlmayr` | `Mona Modlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paul Hörbiger-Straße 16, 4844 Lixlau, Österreich` (address)
- `BONAFIDE Treuhand- und Revisions- gesellschaft m.b.H.` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `34-594/0695` (tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Veit Dworatzeck` | `Veit Dworatzeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Olivia Rodenbach` (person)
- `Zehentberg 7, 4060 Rufling, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)
- `82-692/9441` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/139653.1`) (sent_id: `deanon_BFG_20260814_TEST/139653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Fridolin Zielke  in der Beschwerdesache Monika Tomm,  Mitteredt 3, 4776 Dobl, Österreich, betreffend Beschwerden vom 7. April 2022 gegen die Bescheide des  Finanzamtes Österreich vom 8. Juli 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Einkommensteuer (Arbeitnehmerveranlagung) 2019 und  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 98-832/4427, den  Beschluss:  I. Die Beschwerden werden als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Monika Tomm` | `Monika Tomm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Fridolin Zielke` (person)
- `Mitteredt 3, 4776 Dobl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `98-832/4427` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sheila Mathusczyk, Achatzeweg 10, 5272 Mitterdorf, Österreich, über die Beschwerde vom 15. Juni 2015 gegen den Bescheid des Finanzamtes  Salzburg-Land vom 8. Juni 2015 betreffend Haftungsbescheid /  Lohnsteuer 2012 und 2013  Steuernummer 71-776/4123  zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid/Lohnsteuer 2012 wird als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sheila Mathusczyk` | `Sheila Mathusczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Achatzeweg 10, 5272 Mitterdorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `71-776/4123` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alva Volgenandt  in der Beschwerdesache Pawel Smock,  Kongreßbad 9, 6811 Göfis, Österreich, vertreten durch Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Geusaugasse 39 Tür 8, 1030 Wien, 1.) über die Beschwerde vom 28.02.2014 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 27.01.2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2.) über die Beschwerde vom  28.07.2014 gegen den Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom  30.06.2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012, Steuernummer  20-852/2672, nach der am 19.10.2022 durchgeführten mündlichen Verhandlung zu Recht  erkannt:     I. Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Pawel Smock` | `Pawel Smock` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Alva Volgenandt` (person)
- `Kongreßbad 9, 6811 Göfis, Österreich` (address)
- `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-852/2672` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Felix Rohrmayer, Josef-Riedmüller-Straße 202, 3263 Mitterberg, Österreich, über die Beschwerde vom 10. November 2022 gegen die Bescheide des Finanzamtes  Österreich vom 10. Oktober 2022 betreffend Gebühr und Gebührenerhöhung, Steuernummer  95-690/6876, Erfassungsnummer 10-2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Felix Rohrmayer` | `Felix Rohrmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josef-Riedmüller-Straße 202, 3263 Mitterberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `95-690/6876` (tax_number)

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Donau` — partial — pred is substring of gold: `Donau-Elektro`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Cornelia` — partial — pred is substring of gold: `Cornelia Özgür`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Fabienne Kattner`(person)
- `Cornelia Özgür`(person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich`(address)
- `Thomas Krampl`(person)
- `Finanzamtes für Gebühren`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131857.1`) (sent_id: `deanon_BFG_20260814_TEST/131857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache VetR Eduard van den Berge, Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich, über die Beschwerde vom 6. Juni 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 31. Mai 2019 betreffend Rückforderung Familienbeihilfe und  Kinderabsetzbetrag für September 2018 bis Mai 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Eduard van den Berge`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Eduard van den Berge`(person)
- `Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

**False Positives:**

- `Franz` — partial — pred is substring of gold: `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Basil Eberhards`(person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich`(address)
- `PhD Nancy Prätor`(person)
- `FA Linz`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kzl` — partial — pred is substring of gold: `KzlR Kurt Bätzgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Violetta Colberg`(person)
- `KzlR Kurt Bätzgen`(person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache OSR Juliette Franzisi, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Juliette Franzisi`(person)
- `Spitzesed 172, 4673 Baumgarting, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `47-760/2078`(tax_number)

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

- `Mag` — partial — pred is substring of gold: `Mag. Sven Weichmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Mag. Sven Weichmann`(person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich`(address)
- `Mag. Kurt Kreith`(person)
- `Finanzamtes Baden  Mödling`(organisation)
- `78-738/0573`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.in Jeanne Sohns`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  Prof.in Alma Siegers, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.in Alma Siegers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Prof.in Alma Siegers`(person)
- `Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `37-792/2472`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache KzlR Hon.-Prof. Veit Balsottemeyer, Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich, über die Beschwerde vom 8. September 2021 gegen den Bescheid des Finanzamtes  Österreich vom 24. August 2021 betreffend Abweisung des Antrages vom 28. August 2020 auf  Auszahlung der Familienbeihilfe ohne Indexierung ab 1. Jänner 2019, Steuernummer 55-184/3803,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Kzl` — partial — pred is substring of gold: `KzlR Hon.-Prof. Veit Balsottemeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Hon.-Prof. Veit Balsottemeyer`(person)
- `Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `55-184/3803`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  OSR KommR Susette Stenczel, Amtweg 83, 9542 Tobitsch, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glückspiel vom 25. September 2019  betreffend Gebühr Steuernummer 61-194/1325  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `OSR KommR Susette Stenczel`(person)
- `Amtweg 83, 9542 Tobitsch, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `61-194/1325`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

**False Positives:**

- `Denis` — partial — pred is substring of gold: `Denis Öztopal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Olivia Severien`(person)
- `Denis Öztopal`(person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich`(address)
- `Pschera Steuerberatung GmbH`(organisation)
- `Finanzamt Salzburg-Stadt`(organisation)
- `Finanzamtes Österreich`(organisation)

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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Dr. Katrin Allram in der Beschwerdesache  VetR Dipl. Kfm. Gernot Kurtius, Oberassling 20, 3921 Schmerbach, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des  Finanzamtes Gänserndorf Mistelbach vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Dipl. Kfm. Gernot Kurtius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Katrin Allram`(person)
- `VetR Dipl. Kfm. Gernot Kurtius`(person)
- `Oberassling 20, 3921 Schmerbach, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache OMedR Frauke Klutzuweit, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Frauke Klutzuweit`(person)
- `Weberkogelstraße 114, 8632 Weichselboden, Österreich`(address)
- `N & N Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `50-666/0525`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Regina Mockry  in der Beschwerdesache Gablonsky&Rethlefsen Gastronomie AG&  atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafter  1.

**False Positives:**

- `Gablonsky` — partial — pred is substring of gold: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Regina Mockry`(person)
- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `xx GmbH Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Gabriele Bornscheid  in der Beschwerdesache   DDr. Jens Oberquelle, Obermayrfeld 7, 7302 Nikitsch, Österreich,   über die Beschwerden vom 18. Mai 2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom  11. April 2017 betreffend Wiederaufnahme des Verfahrens zur Vorsteuererstattung 2012  sowie Vorsteuererstattung 2012, 2013 und 2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Gabriele Bornscheid`(person)
- `DDr. Jens Oberquelle`(person)
- `Obermayrfeld 7, 7302 Nikitsch, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  OStR Richarda Schönwaldt, Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich, über die Beschwerde vom 21. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2023 betreffend die Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum November 2022 bis Juni 2023 für das Kind  Heidemarie Fitzenreiter, verbunden mit der Rückforderung der aus der Kinderstaffel (§ 8 Abs 3 FLAG  1967) resultierenden anteiligen Familienbeihilfe für die Kinder Florens Meulenkamp  und  Sara Liebreich, zu Recht:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Lisa Pucher`(person)
- `OStR Richarda Schönwaldt`(person)
- `Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Heidemarie Fitzenreiter`(person)
- `Florens Meulenkamp`(person)
- `Sara Liebreich`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/143793.1`) (sent_id: `deanon_BFG_20260814_TEST/143793.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache   DDr. OStR Ernst Brücklmaier, Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich  vertreten durch Beste & Partner Steuerberatung GmbH,  Perlhofgasse 2/2/8, 2372 Gießhübl, betreffend Beschwerde vom 20. September 2021 gegen  die Bescheide des Finanzamtes für Großbetriebe vom 2. September 2021 betreffend  Wiederaufnahme § 303 BAO Körperschaftsteuer der Jahre 2014-2016 sowie Wiederaufnahme  Körperschaftsteuer für das Jahr 2018, Steuernummer 87-802/5730  beschlossen:  Die Beschwerde wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `DDr. OStR Ernst Brücklmaier`(person)
- `Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich`(address)
- `Beste & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `87-802/5730`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Susanne Groesche`

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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.in Esra Konwischer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Annkathrin Czesielski`(person)
- `Prof.in Esra Konwischer`(person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/144714.1`) (sent_id: `deanon_BFG_20260814_TEST/144714.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Annette Wöhrl  in der Beschwerdesache VetR Univ.-Prof. Wigand Gervais,  Lorenzen 10, 6183 Kühtai, Österreich, vertreten durch die Steuerkanzlei Holowinski  Partner KG, Hasenauerstraße  18/1/Top 2, 1190 Wien, über die Beschwerde vom 19. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Mai 2023  betreffend Körperschaftsteuer 2020,  Steuernummer 92-114/1027, zu Recht erkannt:   I. Von der Festsetzung der Körperschaftsteuer 2020 wird gemäß § 206 lit. b BAO Abstand  genommen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Univ.-Prof. Wigand Gervais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Annette Wöhrl`(person)
- `VetR Univ.-Prof. Wigand Gervais`(person)
- `Lorenzen 10, 6183 Kühtai, Österreich`(address)
- `Steuerkanzlei Holowinski  Partner KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `92-114/1027`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Prof` — similar text (different position): `Hon.-Prof.in Evamaria Fränzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Evamaria Fränzl`(person)
- `Prof. Raphael Grieben`(person)
- `Habegg 37, 5120 Pirach, Österreich`(address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Graz-Stadt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/148827.1`) (sent_id: `deanon_BFG_20260814_TEST/148827.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  OSR Konstanze Dockweiler, Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich, betreffend die am 2. August 2024 beim Finanzamt Österreich  eingelangte Beschwerde gegen die als „festgesetzte Säumniszuschläge für 2021“ bezeichneten  Bescheide beschlossen:  I.  Die Beschwerde gilt gem. § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `OSR Konstanze Dockweiler`(person)
- `Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich`(address)
- `Finanzamt Österreich`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/149452.1`) (sent_id: `deanon_BFG_20260814_TEST/149452.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache HR Vera Kubannek, Stutz 5, 5752 Viehhofen, Österreich  vertreten durch X als ehemaligen Komplementär der HR Vera Kubannek, Ard1, über die  Beschwerde vom 17. Dezember 2021 gegen die Bescheide des Finanzamtes Österreich vom  18. November 2021 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gem. § 188 BAO  für die Jahre 2018 und 2019, Steuernummer 95-973/7826  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `HR Vera Kubannek`(person)
- `Stutz 5, 5752 Viehhofen, Österreich`(address)
- `HR Vera Kubannek`(person)
- `Finanzamtes Österreich`(organisation)
- `95-973/7826`(tax_number)

</details>

---

## `legal_titles_with_names` 🏆

**F1:** 0.355 | **Precision:** 0.720 | **Recall:** 0.235  

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
| 0.720 | 0.235 | 0.355 | 528 | 380 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 380 | 148 | 1234 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Heinz Neuner` | `Dr. Heinz Neuner` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `N.N.` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |
| `RgR Amalia Schuetzke` | `RgR Amalia Schuetzke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)


Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach Dr. Gunther Schmidt und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dr. Kurt Bartold` | `Priv.-Doz. Dr. Kurt Bartold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `OSR Corbinian Friemuth` | `OSR Corbinian Friemuth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Alexander Rimser` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_96`)


Beweis: Einvernahme OSR Corbinian Friemuth, beizuschaffende Transaktionsbeleg Nr.  275,888,722‚ zeugenschaftliche Einvernahme des Parkaufsichtsorgans A352.

| Predicted | Gold |
|---|---|
| `OSR Corbinian Friemuth` | `OSR Corbinian Friemuth` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Techn R Lilia Schöpcke` | `Techn R Lilia Schöpcke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)


Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)


Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

| Predicted | Gold |
|---|---|
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_50`)


Dr. Omasits sei in Pension.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_66`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_68`)


Cipralex und Psychotherapie  Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  emotional instabile Persönlichkeitsstörung mit histrionischen Zügen   Gutachten zur Gewährung der Invaliditätspension 12.04.2016,   Dr. Omasits (Psychiatrie): paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP  auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |
| `Dr. Omasits` | `Dr. Omasits` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_149`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_151`)


Cipralex und Psychotherapie   Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  9 von 18 Seite 10 von 18

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_152`)


emotional instabile Persönlichkeitsstörung mit histrionischen Zügen  Gutachten zur Gewährung der Invaliditätspension 12.04.2016, Dr. Omasits (Psychiatrie):  paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)


LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |
| `Techn R Tosca Häfeli` | `Techn R Tosca Häfeli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_11`)


Mit Strafverfügung vom 12.3.2019 lastete der Magistrat der Stadt Wien, Magistratsabteilung  67, Techn R Tosca Häfeli, in der Folge kurz mit Bf. bezeichnet, folgende Verwaltungsübertretung an:  "1. Datum/Zeit:  06.06.2018, 09:29 Uhr   Ort:   TATORT   betroffenes Fahrzeug: KENNZ (A)   Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den   Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder   Wochenpauschalkarte) gesorgt zu haben, da der im Fahrzeug angebrachte   Parkausweis für Behinderte gemäß § 29b der StVO kein Original war.

| Predicted | Gold |
|---|---|
| `Techn R Tosca Häfeli` | `Techn R Tosca Häfeli` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung  67` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_85`)


Behandlungen / Medikamente / Hilfsmittel: Efectin 225mg, Inkotan 15mg, Lasix 40mg,  Pantoprazol 20mg, PK-Merz, Pregabalin 75mg 2x1, Sirdalud 4mg 2x1, Zyprexa 2,5mg 1-2-4-0,  Copaxone Inj.lösung, etc.; FÄ-Betreuung bei Dr. Fux alle 6 Wochen.

| Predicted | Gold |
|---|---|
| `Dr. Fux` | `Dr. Fux` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

| Predicted | Gold |
|---|---|
| `Dr.in Renate Reininger` | `Dr.in Renate Reininger` |

**Missed by this rule (FN):**

- `Dr.in Silvia Bauer` (person)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

| Predicted | Gold |
|---|---|
| `Dr. Baischer` | `Dr. Baischer` |

**Missed by this rule (FN):**

- `Prof. Maida` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |
| `KommR Serge Salameh` | `KommR Serge Salameh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `Hon.-Prof. Clemens Mooß` | `Hon.-Prof. Clemens Mooß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `HR Danielle Schochert` | `HR Danielle Schochert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Hirschmueller` (person)
- `Silberhumerweg 2, 9163 Bodental, Österreich` (address)
- `Haßreidterstraße 75, 8831 Raiming, Österreich` (address)
- `46-246/2967` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_2`)


in der Beschwerdesache PhD KommR Louisa Mühle, Waltersdorferstraße 9, 5310 Scharfling, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 6. Dezember 2017 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 6. November 2017 betreffend  1.

| Predicted | Gold |
|---|---|
| `PhD KommR Louisa Mühle` | `PhD KommR Louisa Mühle` |

**Missed by this rule (FN):**

- `Waltersdorferstraße 9, 5310 Scharfling, Österreich` (address)
- `N & N Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |
| `KommR Ing. Ludwig Taspinar, MA` | `KommR Ing. Ludwig Taspinar, MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Thassilo Wedekinn` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |
| `Techn R Volker Nissle` | `Techn R Volker Nissle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` | `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Johanesson` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `PhD Nancy Prätor` | `PhD Nancy Prätor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Basil Eberhards` (person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Christina Tiebout` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Violetta Colberg` | `Hon.-Prof.in Dr.in Violetta Colberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Kurt Bätzgen` (person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich` (address)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hugo Pietzak` | `Priv.-Doz. Hugo Pietzak` |
| `Dr. Florens Weißer` | `Dr. Florens Weißer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dr.in Esra Schlink` | `Dr.in Esra Schlink` |
| `Dipl. Kff. Sibylle Wahlscheid` | `Dipl. Kff. Sibylle Wahlscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Univ.-Prof. Kai Menrath` | `Univ.-Prof. Univ.-Prof. Kai Menrath` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wigand Maczkiewicz, Bakk. art.` (person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich` (address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `49-963/8463` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ing. OSR Julia Strutwolf` | `Ing. OSR Julia Strutwolf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Emmat 72, 9063 Wrießnitz, Österreich` (address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH` (organisation)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_4`)


Die Beschwerdeführerin (Bf.) Dr. Judith Glazer wurde mit Bescheid des Finanzamtes Baden  Mödling vom 20.08.2020 zur Einkommensteuer 2018 veranlagt.

| Predicted | Gold |
|---|---|
| `Dr. Judith Glazer` | `Dr. Judith Glazer` |

**Missed by this rule (FN):**

- `Finanzamtes Baden  Mödling` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Eizenhammer` | `Priv.-Doz. Eckard Eizenhammer` |
| `KommR Ashley Tönisen` | `KommR Ashley Tönisen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-543/4492` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` | `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentine Mugge` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_480`)


Die Schaffung von Kryptowährungen (am Beispiel Bitcoin) – allgemeines (Auszug aus  Domes-Hohl, Die steuerliche Behandlung von virtuellen Währungen am Beispiel von Bitcoins,  Diplomarbeit Institut für Finanzrecht Graz, Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 3-27;  zum technischen Aufbau des Netzwerks siehe Gerion Entrup, Bitcoin – der Stärkere gewinnt,  2013, Bachelorarbeit, Institut für theoretische Informatik, Dr. Arne Meier):   a. Bitcoin ist eine Kryptowährung und existiert nicht in physischer Form.

| Predicted | Gold |
|---|---|
| `Dr. Arne Meier` | `Dr. Arne Meier` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Dr. Ashley Nagelschmidt` | `Dr. Ashley Nagelschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Priv.-Doz. Timothy Oldenbüttel, Kohlreitweg 2, 4092 Winterhof, Österreich, vertreten durch EHC Wirtschaftstreuhand- gesellschaft m.b.H., Schulgasse 10, 2000  Stockerau, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 5. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Timothy Oldenbüttel` | `Priv.-Doz. Timothy Oldenbüttel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kohlreitweg 2, 4092 Winterhof, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingrid Dohrmaier` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Edwin Teiwes` | `Univ.-Prof. Edwin Teiwes` |
| `MedR Francois Distefano` | `MedR Francois Distefano` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Astrid Gänsl` | `Dipl.-Ing. Astrid Gänsl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `74-872/6854` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Astrid Gänsl` | `Dipl.-Ing. Astrid Gänsl` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache (§ 4 Abs. 1  Parkometergesetz 2006) hinsichtlich Hon.-Prof. Reinhard Bodewein, Klein Greinsfurth 49, 9063 Kading, Österreich, über dessen Anbringen vom  15. September 2021 in Zusammenhang mit   Strafverfügung des Magistrates der Stadt Wien, MA 67, vom 16.03.2021,   Vollstreckungsverfügung des Magistrates der Stadt Wien, MA 6 – BA 32, vom  13.09.2021,  jeweils zu GZ. MA67/Zahl1/2020, gemäß § 5 des Gesetzes über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) sowie  § 24 Abs. 1 Satz 2 Bundesfinanzgerichtsgesetz (BFGG) in Verbindung mit (iVm) § 31 Abs. 1  Verwaltungsgerichtsverfahrensgesetz (VwGVG) den Beschluss gefasst:  I.) Beim Anbringen vom 15. September 2021 handelt es sich um keine Beschwerde im Sinne  des Art. 130 Abs. 1 Z 1 Bundes-Verfassungsgesetz (B-VG).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Reinhard Bodewein` | `Hon.-Prof. Reinhard Bodewein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klein Greinsfurth 49, 9063 Kading, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_26`)


Am 12. Oktober 2021 nahm der Magistrat der Stadt Wien folgenden  Aktenvermerk zum Akt: „Laut Telefonat … mit Herrn Hon.-Prof. Reinhard Bodewein  sind seine Schreiben anlässlich  den Erhalt der Vollstreckungsverfügung als Beschwerde zu sehen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Reinhard Bodewein` | `Hon.-Prof. Reinhard Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Wieland Starnberg` | `Priv.-Doz. Wieland Starnberg` |
| `Ing. Linus Feyerherdt` | `Ing. Linus Feyerherdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_43`)


Im Februar seien die Schmerzen dann unerträglich geworden, weshalb sie das KUK aufgesucht  hätte und auch bei Univ.-Prof.in Milena Büttinghausen [Anmerkung Richter: Ärztin für Allgemeinmedizin] in Behandlung  gewesen sei.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Milena Büttinghausen` | `Univ.-Prof.in Milena Büttinghausen` |

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Franziskus Grineisen  in der Beschwerdesache MedR KommR Serena Dillschneider,  Rooseveltplatz 7, 4770 Bruck, Österreich, über die Beschwerde vom 28. Dezember 2020 gegen die Bescheide des  Finanzamt Klosterneuburg  vom 25. November 2020 betreffend Einkommensteuer 2017 und Wiederaufnahme  des Verfahrens bezüglich der Einkommensteuer 2017 und den Bescheid vom 02. August 2021  betreffend die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2018,  Steuernummer 95-890/2122, zu Recht erkannt:   I. Die Beschwerde gegen die Wiederaufnahmebescheide wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Franziskus Grineisen` | `Hon.-Prof. Franziskus Grineisen` |
| `MedR KommR Serena Dillschneider` | `MedR KommR Serena Dillschneider` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rooseveltplatz 7, 4770 Bruck, Österreich` (address)
- `Finanzamt Klosterneuburg` (organisation)
- `95-890/2122` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Priv.-Doz.in Mag` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Livia Korowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Günter Gopfauf`(person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich`(address)
- `Finanzamtes Salzburg – Stadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

**False Positives:**

- `Dr.in Rene` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Daisy Hoopt`(person)
- `Prof.in StR DDr.in Reneé Plein`(person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)


Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, Prof.in StR DDr.in Reneé Plein  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

**False Positives:**

- `Dr.in Rene` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Prof.in StR DDr.in Reneé Plein`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `OMedR Constantin Wiedewilt` — partial — pred is substring of gold: `VetR OMedR Constantin Wiedewilt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `VetR OMedR Constantin Wiedewilt`(person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich`(address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_71`)


Dr. Maida, Neurologie- und Psychiatriefachärztin.

**False Positives:**

- `Dr. Maida` — partial — pred is substring of gold: `Dr. Maida,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Maida,`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_89`)


Lebt  seit 2005 in teilbetreuter intensiver WG/Verein B. Seit ca. 2012 von Dr. Hofer-Zeni  besachwaltet.

**False Positives:**

- `Dr. Hofer` — partial — pred is substring of gold: `Dr. Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hofer-Zeni`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

**False Positives:**

- `Dr.in Silvia Bauer  Gutachten` — partial — gold is substring of pred: `Dr.in Silvia Bauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Silvia Bauer`(person)
- `Dr.in Renate Reininger`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`
- `Dr. Thomas Hofer` — similar text (different position): `Dr. Thomas Hofer-Zeni`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_149`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Der Bf. wohnt seit 18. Dezember 2006 in Im Mühlfeld 20n, 3205 Weinburg, Österreich /52, Verein B. Der Verein betreut  Erwachsene, Unterstützungsform: teilbetreut intensiv.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Hilde Heidorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `StR Mag` — partial — pred is substring of gold: `StR Mag. Dirk Bröders`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_307`)


Nach der Verwaltungspraxis gilt Art. 3  Abs. 8 Satz 2 auch dann, wenn der Erwerber die UID des Ausgangsmitgliedstaates der  Warenbewegung bekannt gibt (UStR Rz 3777).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy Große` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Dr.in Kzl` — partial — pred is substring of gold: `Dr.in KzlR Helge Erwied`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Regina Manegold`(person)
- `Dr.in KzlR Helge Erwied`(person)
- `Unterfeichten 5, 4055 Sipbach, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `PhD Mag` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`
- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)


Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die Firma2 GmbH & CoKG, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

**False Positives:**

- `PhD Mag` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Firma2 GmbH & CoKG`(organisation)
- `Firma3  GmbH & CoKG`(organisation)
- `PhD Mag. Heinrich Hambücher`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)


Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die PhD Mag. Heinrich Hambücher  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

**False Positives:**

- `PhD Mag` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Mag. Heinrich Hambücher`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_75`)


ihr  Geschäftsanteil wurde von der PhD Mag. Heinrich Hambücher (FN xxxxxx) übernommen;

**False Positives:**

- `PhD Mag` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Mag. Heinrich Hambücher`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Petra Özkanli  in der Beschwerdesache des  Betriebes gewerblicher Art Radweg A-Tal des Tourismusverbandes A B, Dornackerstraße 480, 4352 Innernstein, Österreich  vertreten durch StB, über die Beschwerden vom 16. August 2017 gegen die Bescheide des  Finanzamt Wien 2/20/21/22  vom 2. Juni 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Körperschaftsteuer 2016 und Körperschaftsteuer 2016 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2016 wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Petra` — partial — pred is substring of gold: `Dr.in Petra Özkanli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Petra Özkanli`(person)
- `Dornackerstraße 480, 4352 Innernstein, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Dr. Sebastian Pfeiffer` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer, LL.M.`

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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `StR Ing. Alexandra Ebermaier` — partial — pred is substring of gold: `StR Ing. Alexandra Ebermaier, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132622.1`) (sent_id: `deanon_BFG_20260814_TEST/132622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache RgR VetR Cassandra Sczech, Hainbuchen 119, 3423 Wördern, Österreich, betreffend Beschwerde vom 22. September 2020 gegen die Bescheide  2015/2016/2017/2018 des Finanzamtes Gänserndorf Mistelbach beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `RgR Vet` — partial — pred is substring of gold: `RgR VetR Cassandra Sczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR VetR Cassandra Sczech`(person)
- `Hainbuchen 119, 3423 Wördern, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `Dipl. Kff. Ingrid Klockgiesser` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Heidrun Eifeler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_220`)


Auch in  den UStR Rz 759 werde ausschließlich die virtuelle Währung Bitcoin erwähnt.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_648`)


b. Weiters stellt sich die Frage, ob die unterschiedlichen Miningvarianten (Solomining,  Poolmining, Cloudmining) für das umsatzsteuerrechtliche Ergebnis eine Rolle spielen (Klotz  Alexander, Mining von Kryptowährungen aus der Sicht des Steuerrechts, Diplomarbeit, 2020,  Institut für Finanzrecht, Univ-Prof. Dr. Tina Ehrke-Rabel, S. 63-64).

**False Positives:**

- `Dr. Tina Ehrke` — partial — pred is substring of gold: `Univ-Prof. Dr. Tina Ehrke-Rabel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ-Prof. Dr. Tina Ehrke-Rabel`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Janis Dührkopp`(person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs` — partial — pred is substring of gold: `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`

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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  StR OSR Roxana Petkov, Bakk. phil., Am Ramberg 28, 3553 Schiltern, Österreich, über die Beschwerde vom 21. April 2016 gegen den Bescheid des  Finanzamtes Feldkirch vom 1. April 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 Steuernummer 48-815/6843  zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `StR OSR Roxana Petkov, Bakk. phil` — partial — pred is substring of gold: `StR OSR Roxana Petkov, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `StR OSR Roxana Petkov, Bakk. phil.`(person)
- `Am Ramberg 28, 3553 Schiltern, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `48-815/6843`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_61`)


Darüber hinaus spreche  beispielsweise Sektionschef Univ.-Prof. DDr. Gunter Mayr in RdW 6/2016, S. 419 ff, von den im  „Gewinn" veröffentlichten Grundstückswerten als tauglichen Bewertungsmaßstab für Grund  und Boden.

**False Positives:**

- `Dr. Gunter Mayr` — partial — pred is substring of gold: `Univ.-Prof. DDr. Gunter Mayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. DDr. Gunter Mayr`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Ingrid Fehrer` — partial — pred is substring of gold: `MMag.Dr. Ingrid Fehrer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag.Dr. Ingrid Fehrer`(person)
- `Ramon Reissdorf`(person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich`(address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `86-314/1061`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Hon.-Prof. Engelbert Voglsang` — partial — pred is substring of gold: `Mag. Hon.-Prof. Engelbert Voglsang`
- `Dr.in Magdalena Holtzbecher, Bakk. ` — partial — pred is substring of gold: `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache KzlR Hon.-Prof. Veit Balsottemeyer, Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich, über die Beschwerde vom 8. September 2021 gegen den Bescheid des Finanzamtes  Österreich vom 24. August 2021 betreffend Abweisung des Antrages vom 28. August 2020 auf  Auszahlung der Familienbeihilfe ohne Indexierung ab 1. Jänner 2019, Steuernummer 55-184/3803,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon.-Prof. Veit Balsottemeyer` — partial — pred is substring of gold: `KzlR Hon.-Prof. Veit Balsottemeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Hon.-Prof. Veit Balsottemeyer`(person)
- `Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `55-184/3803`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_5`)


Der Antrag  wurde rückwirkend ab März 2020 gestellt.  Dr. Dok1, Facharzt für Psychiatrie, bescheinigte dem Bf. nach der am 21. Oktober 2020 im  Sozialministeriumservice durchgeführten Untersuchung weder einen Grad der Behinderung  noch eine Erwerbsunfähigkeit, dies mit der Begründung, dass keine ausreichenden Patienten-  bzw. aufschlussreichen medizinischen Unterlagen – bis auf einen 4 Jahre alten Diabetespass –  vorgelegt worden seien.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_10`)


Der Bf. wurde am 14. April 2021 ein weiteres Mal untersucht und von Dr. Dok2, Fachärztin für  Allgemeinmedizin, folgendes Gutachten erstellt:  2 von 13 Seite 3 von 13

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_57`)


Insbesondere der mittlerweile 2020 verstorbene  Prof. Dr. Thomas Keppert (u.a. Wirtschaftsprüfer, Steuerberater, Immobilientreuhänder und  Sachverständiger) warf mit heftigen Worten den Finanzämtern und dem UFS vor, dass  Außenprüfer und in Folge auch der UFS zu sehr durch die in mehreren Artikeln publizierten  Ansichten von Hofrat Dr. Christian Lenneis geprägt wurden (1.1.2003 bis 31.12.2013  Landessenatsvorsitzender UFS, Außenstelle Wien, später Vizepräsident bzw. Präsident des  BFG).

**False Positives:**

- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof. Dr. Thomas Keppert`
- `Dr. Christian Lenneis` — partial — pred is substring of gold: `Hofrat Dr. Christian Lenneis`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Thomas Keppert`(person)
- `Hofrat Dr. Christian Lenneis`(person)
- `BFG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_8`)


Die Gesellschaftsanteile werden von Dipl. Ing.Ing. Bertram Hennlein und Dipl. Ing. B gehalten.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)


Als  Geschäftsführer fungierte im Streitzeitraum Dipl. Ing.Ing. Bertram Hennlein  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

**False Positives:**

- `Ing. Bertram Hennlein  Im Zuge` — positional overlap with gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_39`)


Ad Geschäftsführerbezug, Diäten und GSVG-Beiträge  Im Prüfungszeitraum sei Dipl. Ing.Ing. Bertram Hennlein als Geschäftsführer der Beschwerdeführerin und Dipl.  Ing. B als Prokurist tätig gewesen.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_42`)


Dipl. Ing. B sei täglich an den Standorten W sowie Z anwesend gewesen und habe sich operativ  um die Durchführung der Geschäftsführeragenden gekümmert, während Dipl. Ing.Ing. Bertram Hennlein in  diese Tätigkeiten so gut wie gar nicht eingebunden gewesen sei.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_45`)


Dipl. Ing.Ing. Bertram Hennlein sei nur selten an den Bürostandorten körperlich anwesend gewesen und habe  daher organisatorisch gar nicht die Durchführung der originären Tätigkeiten eines  Geschäftsführers übernehmen können.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_46`)


Die Entlohnung des Dipl. Ing.Ing. Bertram Hennlein betreffe daher  ausschließlich seine Tätigkeit für die oben angeführten Projekte, für die Grenzverhandlungen  und als Sachverständiger.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_57`)


Die operativen Tätigkeiten des Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein hätten in der  Abwicklung der Projekte, in Grenzverhandlungen und im Tätigwerden als Sachverständiger  bestanden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_60`)


In den Jahren 2014-2020 seien auch alle Jahresabschlüsse vom alleinigen  Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein unterzeichnet worden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. Ing.Ing. Bertram Hennlein ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing.Ing. Bertram Hennlein`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_91`)


Insgesamt flossen ihm in den  Streitjahren folgende Beträge zu:  2015 2016 2017 2018 2019  26.447,13 € 37.786,37 € 36.058,96 € 52.441,49 € 54.658,22 €  Dipl. Ing.Ing. Bertram Hennlein war für die Beschwerdeführerin einerseits als Sachverständiger tätig und  andererseits mit der Abwicklung des Projektgeschäftes (z.B. Semmering Basistunnel,  Bosrucktunnel, Sensorik-Anwendungen bei der ÖBB und ASFINAG) betraut.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)
- `ÖBB`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_36`)


Nach herrschender Literaturmeinung (zB Kommentar Dr. Karl-Werner Fellner zur  Grunderwerbsteuer) könnte ein gemeiner Wert eines Gebäudes in der Regel von einem  Bausachverständigen im Wege der Schätzung erfolgen.

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `Dr. Karl-Werner Fellner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl-Werner Fellner`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Otto Thiesgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `Dipl.-Ing. KzlR Otto Thiesgen`(person)
- `Gränzing 2, 4841 Brunau, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_14`)


Anmerkung:  Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem "Rechts- gutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben für das  BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar 2017".

**False Positives:**

- `Univ.-Prof. Dr. Wolfgang Mazal Wien` — partial — gold is substring of pred: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_61`)


Anmerkung:  Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem "Rechts- gutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben für das  BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar 2017".

**False Positives:**

- `Univ.-Prof. Dr. Wolfgang Mazal Wien` — partial — gold is substring of pred: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`
- `Priv.-Doz.in Waltraud Süßmayr` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Priv.-Doz.in Dr` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`(person)
- `Susette Hadenfelt`(person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich`(address)
- `Huber & Rosenthal Steuerberatung KG`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)
- `34-724/8270`(tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_10`)


In Beantwortung der Schreiben des Finanzamtes übermittelte die Bf. am 25. Juni 2020 folgende  Unterlagen betreffend ihren Sohn A.:   – Psychologisches Gutachten von Dr. Mag. E.Sch., Klinische und Gesundheitspsychologin,  allgemein beeidete und gerichtlich zertifizierte Sachverständige für Psychologie,  Psychotherapeutin, und Quirin Spillmann, LLB  Klinische und Gesundheitspsychologin, vom 26. Juni 2019   – Hörverarbeitungsscreening durch Hörtrainer N.R. vom 14. November 2019   (Ergebnis auffällig;

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Mag. E.Sch.`(person)
- `Quirin Spillmann, LLB`(person)
- `N.R.`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_11`)


Empfehlung zu weiteren Tests bzw. Beratungsgespräch)   – Schreiben der Dr. Mag. E.Sch., w.o., vom 18. Dezember 2019 (Zusammenfassung der  Ergebnisse der erfolgten Begutachtung bezüglich einer vermuteten Legasthenie)   – Schulnachricht der Klasse 6 (6. Schulstufe) der Rudolf Steiner … Freie Waldorfschule vom  14. Februar 2020 (Deutsch genügend, Mathematik nicht genügend, Englisch nicht genügend)   – Befundbericht von Univ. Prof.Charlotte Koebbe  Facharzt für Hals-, Nasen-, Ohrenheilkunde, Kopf- und  Halschirurgie, allgemein beeideter und gerichtlich zertifizierter Sachverständiger vom 27. Mai  2020 (Diagnose: Verdacht auf auditive Verarbeitungsstörung;

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)
- `Charlotte Koebbe`(person)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_139`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_158`)


Ritalin mit Beginn ab Einschulung ab Herbst 2020   Sozialanamnese:   lebt zuhause bei den Eltern, Bruder 12J ADHS, besucht die NMS mit Regelbeschulung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_232`)


Bei der Begutachtung fand das eingangs im Punkt Verfahrensgang genannte, von der Bf.  beschaffte und im Verfahren vorgelegte psychologische Gutachten der Dr. Mag. E.Sch.,  Klinische und Gesundheitspsychologin, allgemein beeidete und gerichtlich zertifizierte  19 von 24 Seite 20 von 24

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_239`)


In dem Gutachten wurde das Vorliegen eines Dauerzustandes festgestellt.   Das vierte Sachverständigengutachten des Bundessozialamtes wurde auf Grund einer  Untersuchung des Sohnes der Bf. durch einen Facharzt für Kinder- und Jugendheilkunde am  31. August 2020 erstellt. Bei diesem Gutachten wurden folgende (neu dazugekommenen)  relevanten Befunde bzw. Unterlagen (vgl. die im Verfahrensgang angeführten Atteste)  berücksichtigt:   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_240`)


Psychologin, 26.06.2019 (vgl. Vorgutachten): Überdurchschnittlich logisch- abstrakte Denkleistung Basisintelligenzquotient 120, durchschnittliche visuell-akustische  Reaktionsfähigkeit, Konzentration Ausdauer gerade noch durchschnittlich, Legasthenie alle  3 Teilbereiche betreffend, Defizite im Leistungsbereich F81 Schulunlust und Prüfungsangst   2019-12-18: Dr. Mag. Sch. Psychologin: Legasthenie, Teilleistungsstörung   2020-02-14: Waldorfschule - Zeugnis: Deutsch genügend, Mathematik nicht genügend, Englisch  nicht genügend)   2020-05-27:Emma Richardon HNO: Dg: Verdacht auf auditive Verarbeitungsstörung,  Teilleistungsschwächen   2020-06-10:Mathias Barrois Kinderpsychiater: F90.0 ADHS, Therapie: Ritalin 10mg 2-1-0   Der Untersuchungsbefund dieses Gutachtens wurde wiederum als normal beschrieben  (Allgemeinzustand: guter AZ;

**False Positives:**

- `Dr. Mag` — positional overlap with gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)
- `:Emma Richardon`(person)
- `:Mathias Barrois`(person)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Dr. Katrin Allram in der Beschwerdesache  VetR Dipl. Kfm. Gernot Kurtius, Oberassling 20, 3921 Schmerbach, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des  Finanzamtes Gänserndorf Mistelbach vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl. Kfm. Gernot Kurtius` — partial — pred is substring of gold: `VetR Dipl. Kfm. Gernot Kurtius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Katrin Allram`(person)
- `VetR Dipl. Kfm. Gernot Kurtius`(person)
- `Oberassling 20, 3921 Schmerbach, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr. Ali Franzel` — partial — pred is substring of gold: `DDr. Ali Franzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `DDr. Ali Franzel`(person)
- `Oberwirtsweg 5, 8562 Bubendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-470/7314`(tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Andreas Domingo` — partial — pred is substring of gold: `Mag. Priv.-Doz. Andreas Domingo`
- `Univ.-Prof.in Kzl` — partial — pred is substring of gold: `Univ.-Prof.in KzlR Tiffany Nowakowsky`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_6`)


Gemäß § 9 Abs. 7 VStG haftet die Gerdes Druck GmbH für die mit diesem Bescheid über den zur  Vertretung nach außen Berufenen, HR Tiffany Vacha  Kabic verhängte Geldstrafe von 240,00 €, die  Verfahrenskosten der belangten Behörde in Höhe von 40,00 € und für den Beiträgen zu den  Kosten des Beschwerdeverfahrens von 48,00 € sowie für sonstige in Geld bemessene  Unrechtsfolgen, zur ungeteilten Hand.

**False Positives:**

- `HR Tiffany Vacha  Kabic` — partial — gold is substring of pred: `HR Tiffany Vacha`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerdes Druck GmbH`(organisation)
- `HR Tiffany Vacha`(person)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Priv.-Doz. Hon` — partial — pred is substring of gold: `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`
- `Dr. Otto Scheff` — partial — pred is substring of gold: `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Dipl.-Ing. Milena Panagiotoglou`(person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_19`)


Grundsätzlich würden nach dem System der Pauschalierung die laufenden Einnahmen und die  laufenden Ausgaben abgegolten (EStR Rz. 4172).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_32`)


Die Anschaffungskosten für ein  Milchkontingent seien nicht mit den pauschalen Betriebsausgaben für den Verkauf von Milch  abgegolten (EStR Rz. 4180a), daher seien die Anschaffungskosten für das Holz nicht mit dem  Pauschalbetrag für die laufenden Ausgaben abgegolten.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_37`)


Nach  Hofstätter/Reichel, Einkommensteuer (EStG 1988), § 4 Abs. 10 EStR Rz. 5, werde man daher  davon ausgehen müssen, dass - soweit die Gewinnermittlung nach Durchschnittsätzen erfolgt -  die Bestandsveränderungen nicht berücksichtigt sind, also der Einnahmenüberschussrechnung  gleichzuhalten ist und beim Übergang zum Betriebsvermögensvergleich ein Übergangsgewinn  oder -verlust entstehen kann.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_15`)


Grundsätzlich würden nach dem System der Pauschalierung die laufenden Einnahmen und die  laufenden Ausgaben abgegolten (EStR Rz. 4172).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_30`)


Die Anschaffungskosten für ein  Milchkontingent seien nicht mit den pauschalen Betriebsausgaben für den Verkauf von Milch  abgegolten (EStR Rz. 4180a), daher seien die Anschaffungskosten für das Holz nicht mit dem  Pauschalbetrag für die laufenden Ausgaben abgegolten.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_35`)


Nach  Hofstätter/Reichel, Einkommensteuer (EStG 1988), § 4 Abs. 10 EStR Rz. 5, werde man daher  davon ausgehen müssen, dass - soweit die Gewinnermittlung nach Durchschnittsätzen erfolgt -  die Bestandsveränderungen nicht berücksichtigt sind, also der Einnahmenüberschussrechnung  gleichzuhalten ist und beim Übergang zum Betriebsvermögensvergleich ein Übergangsgewinn  oder -verlust entstehen kann.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/141869.1`) (sent_id: `deanon_BFG_20260814_TEST/141869.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_86`)


Die Fahrstrecke zu Frau DDr. Ramon Luckmeier  Psychiaterin, Adr2, O1 O, betrage hin und zurück je 21 km.

**False Positives:**

- `Dr. Ramon Luckmeier  Psychiaterin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_102`)


K1 befinde sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `Dr. Ramon Luckmeier  Fachärztin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_200`)


K1 befindet sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `Dr. Ramon Luckmeier  Fachärztin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache ÖkR OMedR Gregor Lauerhaas, Riegerl 15, 4343 Hofstetten, Österreich, betreffend Beschwerde vom 16. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 14. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021,   Steuernummer 51-218/3095, beschlossen:  Der Vorlageantrag vom 21. September 2023 wird gemäß 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO zurückgewiesen.

**False Positives:**

- `OMedR Gregor Lauerhaas` — partial — pred is substring of gold: `ÖkR OMedR Gregor Lauerhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR OMedR Gregor Lauerhaas`(person)
- `Riegerl 15, 4343 Hofstetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `51-218/3095`(tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Wilfried Brokof` — partial — pred is substring of gold: `Mag. Hon.-Prof. Wilfried Brokof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Wilfried Brokof`(person)
- `Hademar Haßelbach, BSc`(person)
- `Engerbergstraße 2, 8642 Nechelheim, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `59-681/6477`(tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, den Richter  Mag.Dr. Wolfgang Pagitsch sowie die fachkundigen Laienrichter Manfred Fiala und DI Thomas  Hrdinka in der Beschwerdesache Saskia Spinnehörn, Gänsdorf 4, 4224 Wolfsegg, Österreich, vertreten durch BONAFIDE  Treuhand- und Revisions- gesellschaft m.b.H., Berggasse 10, 1090 Wien, über deren  Beschwerde vom 15. April 2019 gegen den Bescheid des Finanzamtes Österreich (vormals  Finanzamtes Wien 4/5/10 ) vom 5. April 2019 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten, Steuernummer 59-301/9085, nach Durchführung einer  mündlichen Verhandlung am 12. September 2023 in Anwesenheit der Schriftführerin Nadine  Bernold zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Wolfgang Pagitsch` — partial — pred is substring of gold: `Mag.Dr. Wolfgang Pagitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Mag.Dr. Wolfgang Pagitsch`(person)
- `Manfred Fiala`(person)
- `DI Thomas  Hrdinka`(person)
- `Saskia Spinnehörn`(person)
- `Gänsdorf 4, 4224 Wolfsegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)
- `59-301/9085`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Danielle Mäwius, Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich  vertreten durch Dr. Manfred Arbacher-Stöger,  Wickenburggasse 3/14-15, 1080 Wien, über die Beschwerde vom 30. Dezember 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 15. November 2016 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und Einkommensteuer 2011 bis  2014, Umsatzsteuer und Einkommensteuer 2011 bis 2014, Festsetzung von Anspruchszinsen  2011 bis 2014, über die Beschwerde vom 27. September 2017 gegen die Bescheide des  Finanzamtes Kirchdorf Perg Steyr vom 6. September 2017 betreffend Umsatzsteuer und  Einkommensteuer 2015, gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom  8. September 2017 betreffend Umsatzsteuer und Einkommensteuer 2016, StNr.  06-463/1632, zu Recht erkannt:  I.  Die Beschwerde gegen die Wiederaufnahmebescheide hinsichtlich Umsatzsteuer 2011 bis 2014  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`
- `Dr. Ludwig Thomas` — partial — pred is substring of gold: `Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich`
- `Dr. Manfred Arbacher` — partial — pred is substring of gold: `Dr. Manfred Arbacher-Stöger`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin Dr.in  Ri.N. sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr.in  Ri` — partial — pred is substring of gold: `Dr.in  Ri.N.`

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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Fabian Kohnke, Hammersdorfstraße 78, 4223 Lungitz, Österreich, vertreten durch Intercura  Treuhand- und Revisionsgesellschaft m.b.H., Bösendorferstraße 2, 1010 Wien, über die  Beschwerde vom 14. Dezember 2018 gegen die Bescheide des Finanzamtes Wien 1/23 vom  16. November 2018 betreffend Haftung Lohnsteuer, Festsetzung Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag sowie Säumniszuschläge jeweils 2015 bis 2017  (Steuernummer 14-263/3594 ) nach Durchführung einer mündlichen Verhandlung am  21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing.  Thomas Hrdinka` — partial — pred is substring of gold: `Dipl. Ing.  Thomas Hrdinka`

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

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/142978.1`) (sent_id: `deanon_BFG_20260814_TEST/142978.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/142998.1`) (sent_id: `deanon_BFG_20260814_TEST/142998.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Evelyn Schlessing, Koksbatteriestraße 7, 9560 Bichl, Österreich  vertreten durch Univ.Prof.i.R. Dr. Josef Werndl,  über die Beschwerde vom 27. Dezember 2022 gegen den Bescheid des Finanzamtes Österreich  vom 15. Dezember 2022 betreffend Einkommensteuer 2021 zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`
- `Dr. Josef Werndl` — partial — pred is substring of gold: `Univ.Prof.i.R. Dr. Josef Werndl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Evelyn Schlessing`(person)
- `Koksbatteriestraße 7, 9560 Bichl, Österreich`(address)
- `Univ.Prof.i.R. Dr. Josef Werndl`(person)
- `Finanzamtes Österreich`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache RgR Tanja Tihl, BSc,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `RgR Tanja Tihl` — partial — pred is substring of gold: `RgR Tanja Tihl, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Shirley Vostrovsky`(person)
- `RgR Tanja Tihl, BSc`(person)
- `Kleindorf I 13, 4661 Deising, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `58-854/9841`(tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, die DDr. Jens Oberquelle (im Folgenden: Bf) ist ein  Telekommunikationsunternehmen aus dem Drittland.

**False Positives:**

- `Dr. Jens Oberquelle` — partial — pred is substring of gold: `DDr. Jens Oberquelle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Jens Oberquelle`(person)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Denis Hoffjan` — partial — pred is substring of gold: `Mag. Hon.-Prof. Denis Hoffjan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Dr. Techn R Constantin Rethmann, Bitschweg 5, 6644 Klimm, Österreich, vertreten durch LEDERER & WEBER  Steuerberatungs GmbH, Nibelungengasse 8 Tür 5, 1010 Wien, über die Beschwerden vom 26.  Juni 2018 und 27. Juni 2018 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg (nunmehr: Finanzamt Österreich) vom 22. Juni 2018 betreffend  Einkommensteuer 2016 und Einkommensteuer 2017, Steuernummer 52-821/5355, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Techn R Constantin Rethmann` — partial — gold is substring of pred: `Techn R Constantin Rethmann`

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

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_1`)


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

</details>

---

## `names_after_herrn_frau` 🏆

**F1:** 0.067 | **Precision:** 0.378 | **Recall:** 0.037  

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
| 0.378 | 0.037 | 0.067 | 156 | 59 | 97 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 59 | 97 | 1555 |

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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |

**Missed by this rule (FN):**

- `Ruckelshaußen` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

| Predicted | Gold |
|---|---|
| `Bernett` | `Bernett` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_8`)


Mit fristgerechter E-Mail vom 13. März 2021 (Anhang: Lenkerauskunft) nannte die  Zulassungsbesitzerin Herrn Bodewein als jene Person, der das genannte Kraftfahrzeug zum  Beanstandungszeitpunkt überlassen war.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_11`)


Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2  Wiener Parkometerabgabeverordung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 wurde  über Herrn Bodewein eine Geldstrafe iHv € 60,00 und für den Uneinbringlichkeitsfall eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_14`)


Mit Schreiben des Magistrates der Stadt Wien, MA 67 vom 21. April 2021  (Verfahrensanordnung – Nachreichung Unterschrift bzw. Vollmachtsvorlage) wurde die Firma  X_KG zur Vorlage einer Vollmacht, aus welcher das Vertetungsverhältnis zu Herrn Bodewein sowie die  Berechtigung zur Einbringung des Rechtsmittels hervorgehe, binnen zwei Wochen nach  Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_16`)


Der Magistrat der Stadt Wien, MA 67, erließ an Herrn X einen mit 10. Mai 2021 datierten  Bescheid, mit welchem der Einspruch vom 21.03.2021 gegen die an Herrn Bodewein gerichtete  Strafverfügung vom 16.03.2021 infolge der Nichtvorlage der Vollmacht gemäß § 13 Abs. 3 AVG  als unzulässig zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_39`)


Erst ein Telefonat zwischen Magistrat der Stadt Wien und Herrn Bodewein hat ergeben, dass es sich  um beim Anbringen vom 15. September 2021 um eine Beschwerde handeln solle.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)


Für Herrn Bodewein geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_26`)


Im Vorlageantrag wird ausgeführt:  „Herr B ist nach Angaben meines Mandanten erst im Sommer 2013 nach Österreich gekommen  und war ausschließlich für Herrn Mathusczyk tätig.

| Predicted | Gold |
|---|---|
| `Mathusczyk` | `Mathusczyk` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)


Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn Schwent gelenkt wurde.

| Predicted | Gold |
|---|---|
| `Schwent` | `Schwent` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


Entscheidungsgründe  Nach dem das Finanzamt in der Beschwerdevorentscheidung (BVE) vom 17.11.2023 das  Pendlerpauschale, den Pendlereuro und den Alleinerzieherabsetzbetrag antragsgemäß  steuermindernd berücksichtigt hat, ist nur mehr strittig, ob sogenannte Familienheimfahrten  von Frau Kuehnhanss (in der Folge: Beschwerdeführerin: Bf) vorliegen und als Werbungskosten zu  berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Kuehnhanss` | `Kuehnhanss` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)


Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn Kaspar Sadowski  wieder als aktiv gemeldet.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_18`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat seinen Familienwohnsitz gemeinsam mit seinen Kindern (im Beschwerdejahr 8 und  12 Jahre alt) in Ungarn, wo weder er noch seine Frau Einkünfte erzielen.

**False Positives:**

- `Eink` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_100`)


Lebensjahr, dies wurde in dem  Gutachten von Frau Dr. 2 zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem  nicht attestiert.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_131`)


Lebensjahr, dies wurde in dem Gutachten von Frau Dr. 2  zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem nicht attestiert....  Derzeitige Beschwerden:  Die Antragstellerin gibt an: "Ich habe das gleiche seit meiner Jugend, das sind Panikattacken,  Kopfschmerzen und eine Sozialphobie.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_114`)


Dass die Bfin mit Herrn KT einen gemeinsamen Hausstand im Jahr 2018, der den Mittelpunkt  der Lebensinteressen in Polen gebildet hat, gehabt hat ergibt sich aus dem Vorbringen der Bfin  nicht, weil die Bfin im Schreiben vom 9.3.2020 selbst vorgebracht hat, dass die  Lebensgemeinschaft im Jahr 2020 begründet wurde.

**False Positives:**

- `KT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)


ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn Dr. YYY übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_263`)


Nach Belehrung über das Entschlagungsrecht und Wahrheitserinnerung gemäß § 50 AVG  wurde das Organ der Parkraumüberwachung, welches ursprünglich die Beanstandung  durchgeführt hat, Frau NAME-Zeugin, als Zeugin einvernommen.

**False Positives:**

- `NAME` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_316`)


Mit Mail vom 26.8.2020 übermittelte die Richterin dem Bf. per Mail die Beweisfotos, das  Schreiben, welches der Magistrat an Dr. YYY gerichtet hatte, den Rückschein, die Niederschrift  über die mündliche Verhandlung und ein Schreiben, dessen Inhalt in der Folge wiedergegeben  wird:  "Anbei wird die Niederschrift der heutigen mündlichen Verhandlung übermittelt, in welcher die  Zeugin (das Organ der Parkraumüberwachung, welches die Anzeige gelegt hat, Frau ZEUGIN)  einvernommen wurde.

**False Positives:**

- `ZEUGIN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat`(organisation)
- `Dr. YYY`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_67`)


Unstrittig war, dass die Gesellschafter-Geschäftsführerin, Frau Ges-Gf, mit 25,25% im Sinne des  § 22 Z 2 zweiter Teilstrich EStG 1988 an der Bf. wesentlich beteiligt war.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

**False Positives:**

- `Unverdro` — partial — pred is substring of gold: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unverdroß`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`
- `Unverdro` — partial — pred is substring of gold: `Unverdroß`
- `Prim` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

**False Positives:**

- `Unverdro` — partial — pred is substring of gold: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unverdroß`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Freßdorf`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Am 7.7.2008 wurde ein Strafantrag der belangten Behörde gegen die Geschäftsführerin Frau  GF der Beschwerdeführerin Floriane Rötker (in der Folge als Bf bezeichnet) an das Magistratische  Bezirksamt gestellt wegen illegaler Beschäftigung von Ausländern gem. § 3 Abs. 1 AuslBG.

**False Positives:**

- `GF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Floriane Rötker`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_35`)


Mit Schreiben vom 17.5.2019 stellte die steuerliche Vertretung des BF folgenden Antrag  (wörtlich):  "Betrifft:  Eventualantrag nach § 48 BAO    Ergänzung zum Antrag auf Einleitung eine Verständigungsverfahrens    vom 16.08.2018  Mit 16.08.2018 wurde für meinen Klienten, Herrn BF, die Einleitung eines  Verständigungsverfahrens betreffend einer Doppelbesteuerung zwischen Osterreich und Malta  geführt.

**False Positives:**

- `BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_72`)


Am 26.1.2018 (am Tag danach) seien zwei Poststücke per Einschreiben mit den  Aufgabenummern RQ … 747 und 748 versendet worden, die von Herrn Mag. Sch. auf dem  Nachhauseweg beim Postamt W. aufgegeben worden seien.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. G`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

**False Positives:**

- `WM` — no gold match — likely missing annotation
- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

**False Positives:**

- `Ruckelshau` — partial — pred is substring of gold: `Ruckelshaußen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dimitri Witkoski`(person)
- `Ruckelshaußen`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_45`)


Nach Antwort von Herrn Ruckelshaußen vom 04.08.2015 betreffend  „asymmetrische Arrondierung und Immo-Est-Befreiung“ kommt im wörtlichen Sinne die  Befreiungsbestimmung des § 30 Abs 2 Z 4 EStG immer für denjenigen zur Anwendung, bei dem  ein Grundstückstausch einen Flurbereinigungsvorgang darstellt. Wenn für einen Tauschpartner  eine Flurbereinigung gegeben ist (und auch ein Tausch und keine Veräußerung vorliegt - dh  keine Aufzahlungen über 50%), dann greift für diesen die Befreiung, wohingegen der andere  Tauschpartner steuerpflichtig ist.

**False Positives:**

- `Ruckelshau` — partial — pred is substring of gold: `Ruckelshaußen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ruckelshaußen`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lisa Lindnau`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_54`)


Am 06.12.2013 wurde ein Tauschvertrag zwischen dem Beschwerdeführer … und Herrn WM …  abgeschlossen.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_64`)


Im Bescheid wird festgestellt, dass der zwischen Herrn WM und dem Bf abgeschlossene  Flurbereinigungsvertrag vom 06.12.2013 hinsichtlich des neu gebildeten Grundstückes Nr. zz,  EZ2, für die Durchführung der Flurbereinigung im Sinne der §§ 1 und 28 Oö.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_35`)


Zusätzlich  sei der Beschwerdeführerin unbedingt empfohlen worden, die OP von Herrn Dr. B einem  anerkannten Schulterspezialisten ausführen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_58`)


Die streitgegenständliche Operation wurde schließlich in der Klinik Diakonissen Linz von Herrn  Dr. B durchgeführt (stationärer Aufenthalt von 15.5. bis 20.5.2019).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)


Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  MH-Bau GmbH am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_71`)


Beide Gesellschaften wurden vom Alleingesellschafter-Geschäftsführer,  Herrn RB, vertreten (siehe Firmenbuch).

**False Positives:**

- `RB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_20`)


Nach den Angaben von Herrn Dr. F sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_40`)


Bei den vorgelegten Unterlagen handelt es sich einerseits um Mietverträge und andererseits  um Schreiben des Herrn DI J M.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_126`)


Am 27. Juli 2022 teilte die Magistratsabteilung 67 (Frau Frau1) auf Nachfrage des  Bundesfinanzgerichtes mit, dass die Bf. entgegen ihren Beschwerdeausführungen bis dato  keine weitere Einzahlung zu gegenständlicher GZ. leistete.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

**False Positives:**

- `Amtsdirektor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Kohlfürst`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_23`)


In seinem fristgerecht erhobenen Einspruch brachte der Bf vor, dass das Fahrzeug zur Bean- standungszeit von Herrn LE, Gasse, 2700 Wr. Neustadt, gelenkt worden sei.

**False Positives:**

- `LE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_53`)


Im Einspruch gegen die Strafverfügung vom 22. Juli 2022, eingelangt bei der Behörde am 4.  August 2022, brachte der Bf erstmals vor, dass das Fahrzeug zur Beanstandungszeit von Herrn  LE, Gasse, 2700 Wr. Neustadt, gelenkt worden sei.

**False Positives:**

- `LE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_575`)


Mieten (bis auf jene des Bruders) damit erklärte, dass „solche nicht darstellbar waren bzw.  voraussichtlich nicht beweisbar gewesen wäre, dass bzw. in welcher Höhe der Klient weitere  Mieteinnahmen bei ordnungsgemäßer Ausführung des Werkes durch Herrn XY erzielen hätte  können.“

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_37`)


Der BF lebte  im Beschwerdezeitraum an der Adresse Adr Ö BF gemeinsam mit seiner Frau EB in deren  Einfamilienhaus.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_38`)


Das gegenständliche Einfamilienhaus stand bis Ende 2014 im Eigentum von  Frau EB.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_45`)


Auf die Gattin des BF, Frau EB, war von 04.01.2007 bis 04.09.2013 in Österreich ein  Kraftfahrzeug Nissan Navara mit dem Kennzeichen XY angemeldet.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_46`)


Am 13.09.2013 wurde auf  Frau EB ein Kraftfahrzeug VW Golf Plus mit dem gleichen Kennzeichen in Österreich  angemeldet.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_56`)


Dass auf die Gattin des BF, Frau EB, von 04.01.2007 bis 04.09.2013 in Österreich ein  Kraftfahrzeug Nissan Navara bzw. ab 13.09.2013 ein PKW VW Golf Plus mit dem Kennzeichen  XY angemeldet war, wurde anhand der vorgelegten Unterlagen nachgewiesen.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_12`)


2. Allgemeine Feststellungen zur BP   Die Bp bei Fr. DI DM wurde am 04.12.2012 begonnen, nachdem zuvor eine Bp bei [dem Bf.],  dem Vater von Frau DM, durchgeführt worden war.

**False Positives:**

- `DM` — similar text (different position): `DI DM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI DM`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_15`)


Die Unterlagen [des Bf.] befanden sich in St. Marein,  die Unterlagen von Frau DM bei ihrem Steuerberater, Mag. H, in Graz.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_32`)


3. Missbrauch von Formen und Gestaltungsmöglichkeiten  Frau DM wohnte in den geprüften Jahren immer im Ausland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_34`)


Frau DM handelte mit Kosmetikprodukten und Nahrungsergänzungsmitteln, sie lieferte Waren  an ihren Vater, [den Bf.] in Österreich und nach Deutschland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_35`)


[Der Bf.] liefert dieselbe Ware, die von Frau DM von Deutschland nach Österreich geliefert  wurde wieder weiter nach Deutschland und andere Länder.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_87`)


Daher wurden bei Frau DM Abfragen zu den igE und igL  durchgeführt.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_111`)


Zu Punkt 3 der Niederschrift:   Der Abgabepflichtige handelt(e) mit den von Frau DM (seiner Tochter) bezogenen Waren und  belieferte Kunden in Österreich sowie im europäischen Ausland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_112`)


Es waren dies ausschließlich  Kunden des [Bf.], Frau DM unterhielt zum Großteil dieser Kunden keine geschäftlichen  Beziehungen.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_113`)


Der Abgabepflichtige handelte in eigenem Namen und auf eigene Rechnung und  trug das alleinige unternehmerische Risiko für den erfolgreichen Verkauf der von Frau DM  bezogenen Waren.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_162`)


Zu Pkt. 11 der Niederschrift   Es wird von der Behörde nicht schlüssig dargelegt, in welchem Zusammenhang die Unterlagen  von Herrn GM* mit dem Außenprüfungsverfahren stehen.

**False Positives:**

- `GM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_172`)


Lieferungen von Frau DM.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_173`)


Natürlich wurden alle Waren, die von Frau DM an  [den Bf.] geliefert wurden, in beiden Buchhaltungen gleichermaßen erfasst.“  11 von 33 Seite 12 von 33

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_184`)


In dieser wird auf den Schriftsatz der Frau DI DM vom 10.3.2016 – als „integrierenden  Bestandteil“ der Beschwerdeschrift des Bf. – verwiesen.

**False Positives:**

- `DI` — partial — pred is substring of gold: `DI DM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI DM`(person)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_245`)


Im Verlauf der gegenständlichen Außenprüfung sind schließlich neue Tatsachen, wie  insbesondere Betriebsfinanzierung, Zahlungsströme, Warenströme, die enge betriebliche  Verbindung zum Betrieb der Tochter des Abgabepflichtigen, Fr. DI DM, sowie der gemeinsame  Wareneinkauf für beide Betriebe über das Unternehmen von Frau DM und die Warenverkäufe  (Sitz bzw. Wohnsitz der Abnehmer) neu hervorgekommen.

**False Positives:**

- `DM` — similar text (different position): `DI DM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI DM`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_277`)


(„Frau DM wohnte in den geprüften Jahren immer im  Ausland…“) oder S. 8ff.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_73`)


Der frühere Name von  Herrn GK war GS.

**False Positives:**

- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_75`)


Gesellschafter der BF im Jahr 2013 war Herr S.  Die Fa. I wurde von Herrn DO und Herrn KW im Jahr 2001 gegründet.

**False Positives:**

- `DO` — no gold match — likely missing annotation
- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_83`)


Am 05.01.2005 wurde von der BF die Zahlung der zu diesem Zeitpunkt bestehenden Forderung  gegenüber der Fa. I in Höhe von € 367.290,00 per Email an Herrn KW, Geschäftsführer der Fa. I,  eingemahnt.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_94`)


Die im Vertrag vom 24.07.2007 vereinbarte Zahlung von jährlich € 30.000,00 ab dem Jahr 2011  wurde von der Fa. I nicht erfüllt.  Mit Email vom 15.02.2013 bot die BF dem Geschäftsführer der Fa. I, Herrn KW, an, auf 80 %  der zu diesem Zeitpunkt aushaftenden Forderung in Höhe von € 967.333,62, somit auf €  777.866,90, zu verzichten, wenn im Gegenzug von der Fa. I die verbleibende Restschuld von €  193.466,72 bis zum 31.03.2013 beglichen werde.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_113`)


Die Feststellungen, dass der frühere Name von Herrn GK „GS“ war, dass GK der Sohn von S ist  sowie, dass AS der Bruder von GK ist, wurden von Herrn GK in der mündlichen Verhandlung vor  dem Bundesfinanzgericht am 04.05.2023 bestätigt.

**False Positives:**

- `GK` — no gold match — likely missing annotation
- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_115`)


Die letzte dem Bundesfinanzgericht vorgelegte Mahnung gründet sich auf eine  Email der BF an den Geschäftsführer der Fa. I, Herrn KW vom 05.01.2005.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Mehmet` — similar text (different position): `Mehmet Köprücü`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)
- `Quentin Schwartkopp`(person)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_23`)


Der Baumaschinenhandel und -verleih verfügt über eine größere Kundenanzahl und erlaubt  Herrn NR unabhängig von seiner Tätigkeit für die Rechtsvorgängerin_der_Bf. ein  entsprechendes Einkommen zu erzielen.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_42`)


Zu den – durch die Finanzverwaltung – in den Fokus gesetzten administrativen Leistungen des  Herrn NR führt die Bf. aus, dass sich die Tätigkeiten zwingend vermischen würden: „Die dem  GPLA-Prüfer mehrfach erläuterte und durch Unterlagen nachgewiesene Vermischung und  Verschränkung der beiden Tätigkeiten (einerseits Betreuung und Verwaltung der eigenen  Geräte und Maschinen, andererseits kaufmännische Betreuung) oftmals auf derselben  Baustelle verunmöglicht eine genaue Trennung der Tätigkeitsbereiche des Herrn NR.

**False Positives:**

- `NR` — no gold match — likely missing annotation
- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_46`)


Und weiter: „Zwischen der Rechtsvorgängerin_der_Bf. und Herrn NR besteht daher seit 2002  die grundsätzliche Übereinstimmung, dass Herr NR im Rahmen seiner besonderen  Qualifikationen die Lohnverrechnung, die Buchführung, die Abrechnung div.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_47`)


Bauvorhaben und  sonstige administrative Leistungen je nach gesetzlichen Vorgaben für die Baufirma und je nach  Möglichkeiten seiner Kapazitäten des Herrn NR im Rahmen eines Werkvertrages bereitstellt. Es  gilt als vereinbart, dass für die administrativen Leistungen nur angemessene, fremdübliche  Kosten (vergleichbar einem selbständigen, gewerblichen Buchhalter gem. § 3  Bilanzbuchhaltergesetz) in Rechnung gestellt werden.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_65`)


Überdies wäre - mangels Fachkenntnisse - der selbständig  vertretungsbefugte Geschäftsführer als Bautechniker auch gar nicht in der Lage, dem Herrn NR  fachliche Weisungen zu erteilen.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_78`)


Die Tätigkeit des  Herrn NR sei, so die Behörde, eindeutig eine Dienstleistung.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_81`)


Etwaige Kostentragungen  des Herrn NR aus dem Titel Büromiete und Stromkosten können an der organisatorischen  Eingliederung nichts ändern und seien im Übrigen mangels aktenkundiger vertraglicher  Regelungen nicht nachvollziehbar.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_148`)


Es steht sohin fest: Für die Bf. war die Tätigkeit des Herrn NR von zentraler Bedeutung;

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

**False Positives:**

- `Manhardt  Adresse` — partial — gold is substring of pred: `Manhardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manhardt`(person)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_108`)


Im erwähnten Straferkenntnis vom  7.11.2022 hat die belangte Behörde diese Ermittlungsergebnisse auch wiedergegeben und  dazu auszugsweise wie folgt ausgeführt:  „Ermittlungen ergaben, dass für Herrn Rudolf B kein Ausweis gemäß § 29b StVO ausgestellt  wurde.

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_110`)


……  Im Übrigen ist auch der lt. Anzeigeangaben im Fahrzeug nicht gut erkennbar hinter der  Windschutzscheibe eingelegte Parkausweis gemäß § 29b StVO, dessen Ausweisnummer  teilweise durch eine Postkarte verdeckt war, nicht für Herrn Rudolf B ausgestellt.“

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_17`)


Mit Schreiben vom 4. März 2025 teilte die belangte Behörde dem Bf. mit, mit Lenkerauskunft  vom 03.03.2025 zur Zahl MA67/GZ1/2024 habe er Herrn Lenker1, geb. am geb, als Lenker des  Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 am 20.11.2024 um 17:06 Uhr namhaft  gemacht.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_36`)


Auch die  Tatsache, dass der Bf. im Einspruch gegen die an ihn ergangene Strafverfügung (wegen  Erteilung einer unrichtigen Lenkerauskunft) eine dritte Person, nämlich Herrn Lenker5 als  Lenker genannt habe, wohingegen der Bf. in seiner Lenkerauskunft vom 03.03.2025 Herrn  Lenker4 angeführt habe, spreche dafür, dass es sich bei der Angabe des bzw. der vom Bf.  genannten Lenker um eine reine Schutzbehauptung handle.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation
- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_91`)


In der fristgerecht beantworteten Lenkererhebung vom 26. Februar 2025  gab er hingegen Herrn Lenker1 als Lenker an, der zum Zeitpunkt der Auskunft wiederum  keinen Wohnsitz in Österreich hatte.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_277`)


Die Angaben von Herrn Baumeister Y X werden nicht zur Sachverhaltsfeststellung  herangezogen, weil sie nach der hier vertretenen Auffassung nicht relevant sind und jedenfalls  unzuverlässig sind, wie auch im Detail in Abschnitt 14 dargestellt wird.

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_69`)


Der Bf. war Lenker des auf Herrn ZLB zugelassenen tatgegenständlichen Kraftfahrzeuges.

**False Positives:**

- `ZLB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `names_after_bf_or_representative` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 110 | 0 | 110 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 110 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_27`)


Außerdem sei auf die persönlichen Verhältnisse und auf die wirtschaftliche Leistungsfähigkeit des Bf. Bedacht genommen (§ 23 Abs. 3 FinStrG) worden.

**False Positives:**

- `Bedacht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_17`)


Dagegen erhob die Bf. Beschwerde beim VwGH (Ra 2018/15/0121).

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_8`)


Mit Schriftsatz vom 23.4.2018, Postaufgabedatum laut Poststempel 24.4.2018, erhob der Bf.  Beschwerde gegen diesen Feststellungsbescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_9`)


Dagegen erhob die Bf. Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_115`)


Hinsichtlich der Rechnungen Nr. 005/16, Nr. 007/16 und Nr. 017/16, welche für  Generalplanerleistungen im Zusammenhang mit dem Neubau des Wohnheims ausgestellt  wurden, legte die Bf. Unterlagen vor, aus denen sich sowohl ergibt, dass die  Generalplanerleistungen von einem umsatzsteuerpflichtigen Unternehmer erbracht wurden,  als auch, dass die Bf. seit der Fertigstellung des Wohnheims deren einzelnen Einheiten mit  einer Größe von 24,70 m² bis 80,28 m² um EUR 317,96 bis EUR 809,45 netto pro Monat  zuzüglich Betriebskosten vermietet.

**False Positives:**

- `Unterlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_142`)


c) 1 Konvolut an monatlichen Arbeitszeitnachweislisten des Bf bei der Fa.NiederImmobilien Institut GmbH  Zeitraum  Jänner 2014 – Dezember 2015:  Eine nähere Überprüfung durch das BFG hat in Gegenüberstellung des Arbeitszeitnachweises  (siehe untentstehend 2 rechte Spalten) zu den vom Bf vorgelegten Aufzeichnungen seiner  "Heimfahrten" Ö-D-Ö (siehe untenstehend die 2 linken Spalten) folgende Divergenzen  ergeben:    Fahrten Ö-D-Ö lt.  Aufzeichnung Bf    Lt. Zeitnachweisliste  des Arbeitgebers

**False Positives:**

- `Lt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)
- `BFG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_229`)


Nach dem Dafürhalten des BFG bedürfte es zwecks diesbezüglich konkreter Feststellungen  wohl der Bekanntgabe aller erforderlichen Daten durch den Bf. Bislang wurden seinerseits  lediglich die Aufzeichnungen über die "Heimfahrten Ö-D-Ö" zur Vorlage gebracht, woraus ua.  lediglich zu erahnen ist, dass es sich hiebei um Fahrten von A/XX nach D/XX und retour handeln  wird.

**False Positives:**

- `Bislang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_170`)


Damit kam es aber erst im Jahr  2013 zum Zufluss des Veräußerungspreises an den Bf.   Somit können die neu hervorgekommenen Tatsachen, die vom Finanzamt als  Wiederaufnahmsgründe herangezogen wurden, nicht zu einem geänderten  Einkommensteuerbescheid für 2012 führen.

**False Positives:**

- `Somit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_22`)


Gegen die Strafverfügung erhob der Bf. Einspruch und erklärte, das Schreiben vom 12.3.2019  nach Rückkehr von seinem Auslandsaufenthalt vorgefunden zu haben.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_134`)


Mit E-Mail vom 20.11.2019 brachte der Bf. Beschwerde gegen das Straferkenntnis ein,  beantragte die Durchführung einer mündlichen Verhandlung, die Aufhebung des  9 von 28 Seite 10 von 28

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_33`)


Die Revision der Bf. richtete sich gegen die Anwendbarkeit des § 25 Abs. 1 Z 1 lit b EStG 1988  auf die Tätigkeit der vier, nicht als Geschäftsführer tätigen, nicht wesentlich beteiligten,  Gesellschafter der Bf.  Gegen die Einbeziehung der Honorare der Gesellschafter-Geschäftsführerin in die  Bemessungsgrundlagen für den Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag und  Festsetzung der lohnabhängigen Abgaben für die Jahre 2010 – 2013 wurden keine Vorbringen  erstattet.

**False Positives:**

- `Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_22`)


Mit Schreiben vom 14. Februar 2020 und 21. Februar 2020 wurden dem Bf. Ablichtungen  von 3 am Tattag zur Tatzeit vom Meldungsleger aufgenommene Fotos gesandt.

**False Positives:**

- `Ablichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_53`)


Die Bf wurde weiters darauf hingewiesen, dass ex lege nicht der Arbeitnehmer, sondern die Bf  Abgabenschuldner dieser Arbeitnehmerbeiträge ist:    Gem. § 2 Abs 1 lit.b iVm § 4 Abs 1 des Bundesgesetzes über die Einhebung eines  Wohnbauförderungsbeitrages ist der Arbeitgeber Steuerschuldner bzw. Haftender.

**False Positives:**

- `Abgabenschuldner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_86`)


II. Das Bundesfinanzgericht hat erwogen:  Betreffend das Jahr 2016 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):  Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2016 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 0,00 €  Beilage: Ich bitte zukünftig um Beachtung, dass mir keinerlei Wohnungen mit  Umsatzsteuerpflicht unterliegen.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_88`)


1 Fahrt (deutscher Wohnsitz) (Wohnung in Wien) 740 km (und retour 740 km) á Pauschale  0,42 € 621,60 €, Maut / 10 Tages-Vignette 8,80 €  Verpflegungsmehraufwand 48,00 €, Übernachtungspauschale 104,00 € Anreise/Abreise  Portokosten 3,60 €, Telefonkosten 20,00 €  Betreffend das Jahr 2017 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):  Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2017 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 17.280,00 €  Einkünfte aus Vermietung und Verpachtung … -773.72 €.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_89`)


Betreffend das Jahr 2018 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):   Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2018 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 17.400,00 € *  Davon steuerfrei OHNE Vorsteuerabzug gemäß  a) § 6 Abs. 1 Z 9 lit. a (Grundstücksumsätze) -17.400,00 €  * Kaltmiete 1.200,00 € x 12 + Betriebskosten 250,00 € x 12 = 17.400,00 €  Einkünfte aus Vermietung und Verpachtung … 3.190,09 €  Einnahmen/Werbungskosten-Überschussrechnung:  Hausgeld/Garage 4.184,62, Abschreibung 8.936,56 €, BKA 282,73 €,  Werbungskosten 806,00 € *  * ident der Werbungskostenposition dieses Betrages im Jahr 2016  Gemäß § 6 Abs. 1 Z 27 UStG 1994 sind die Umsätze der Kleinunternehmer steuerfrei.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_97`)


Eine vom Meldungsleger erstellte Fotografie zeigt zum Teil den  Schriftzug „Firma“ an der Gebäudefassade und davor das abgestellte, beanstandete Kfz des Bf.  Daraus geht klar hervor, dass das besagte Kfz in jenem Abschnitt abgestellt wurde, der der  Guglgasse ONr. 1 zuzuordnen war.

**False Positives:**

- `Daraus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_116`)


Selbst bei  Unklarheit hätte der Bf. Erkundigungen einholen und bis zur Klärung  für die ordnungsgemäße  Entwertung von Parkscheinen sorgen müssen.

**False Positives:**

- `Erkundigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_61`)


Die Wiederaufnahme der Verfahren wurde damit begründet, dass im Zuge der  abgabenbehördlichen Prüfung bei der Arbeitgeberin des Bf Unterlagen vorgefunden worden  seien, aufgrund derer festgestellt worden sei, dass ein Teil seines Lohnes ohne Entrichtung der  Lohnabgaben ausbezahlt worden sei.

**False Positives:**

- `Unterlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_18`)


Auf Basis der maßgeblichen Verjährungsbestimmungen sei das Recht zur Festsetzung der  ESt 2010 im Fall des Bf Ende 2016 verjährt.

**False Positives:**

- `Ende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_251`)


GF. 27/11: Ein österreichischer Unternehmer erbringt eine sonstige Leistung an einen  Dienstnehmer der Bf.  Rechtliche Beurteilung: Die Bf. ist nicht Leistungsempfänger und daher nicht zum  Vorsteuerabzug berechtigt.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_70`)


Von September  2013 bis Jänner 2016 bezog der Bf Familienbeihilfe für sich selbst.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_62`)


Dagegen erhob die Bf Vorlageantrag am 6.9.2019 und begründete unter Verweis auf ihre  Bescheidbeschwerden primär dahingehend, dass gemäß § 8 Abs. 2 GrEStG die Steuerschuld mit  dem Eintritt der Bedingung entstehe, wenn die Wirksamkeit des Erwerbsvorganges vom  Eintritt einer Bedingung abhängig sei.

**False Positives:**

- `Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_9`)


Gegen diesen Bescheid erhob die Bf Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_27`)


In der Abgabenerklärung für 2019 setzte der Bf. Kosten der doppelten Haushaltsführung iHv.  € 4.575,72 an.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_10`)


Mit Schriftsatz vom 22. März 2020 brachte der Bf. Beschwerde ein.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_4`)


Am 05.02.2019 legte der Bf Beschwerde ein und führte dazu aus, dass er drei Kinder hätte, für  die er Unterhaltszahlungen in Höhe von gesamt € 600,00/Monat zahlen würde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_67`)


Daneben hatte das Finanzamt mit Bescheid v. 9.10.2013 dem Bf Kraftfahrzeugsteuer für die  Monate 4-9/2013 vorgeschrieben.

**False Positives:**

- `Kraftfahrzeugsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_625`)


Die Abläufe lassen sich wie folgt darstellen (Punkte der allgemeinen Geschäftsbedingungen):   Leistung der Bf Verantwortung der Bf Verantwortung der  Vertragspartner  (Kunden)  (1) Zurverfügungstellung von  Rechnerleistung für bestimmte Zeit  und Einspeisung im Namen und im  Auftrag des Vertragspartners  (Kunden) in  Produktion von  Kryptowährung (Schürfung)  im Namen und auf  Rechnung des  Vertragspartners

**False Positives:**

- `Verantwortung` — no gold match — likely missing annotation
- `Verantwortung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_179`)


Damit liege die Haftung und das wirtschaftliche Risiko bei der Bf.  Weder die vertraglichen Grundlagen bzw. Abrechnungen noch die Aussagen bei den  Einvernahmen sprechen dafür, dass von den AN eigenständige und gewährleistungsfähige  Werke erbracht worden wären.

**False Positives:**

- `Weder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_31`)


Da sich der einzige Wohnsitz des Bf. im Jahr 2014 in Österreich befunden habe, habe  Österreich gem. Art. 4 Abs. 1 des Doppelbesteuerungsabkommens Österreich/Deutschland als  Ansässigkeitsstaat das Besteuerungsrecht auf das gesamte Welteinkommen des Bf.  Deutschland habe als Tätigkeitsstaat gem. Art. 15 Abs. 1 DBA Österreich/Deutschland anhand  der lokalen Auslegung des Arbeitnehmerbegriffes das Besteuerungsrecht auf die Einkünfte,  welche die Arbeitstage in Deutschland beträfen.

**False Positives:**

- `Deutschland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_18`)


Die Erstattungsverordnung komme folglich zur Anwendung, weshalb die Bf. Anspruch auf  Erstattung der an die inländischen Provider bezahlten Vorsteuern in voller Höhe habe.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_15`)


Weiters gab das Gericht der Bf Gelegenheit, sich hiezu zu binnen 2 Wochen ab Zustellung des  Vorhaltes zu äußern, innerhalb derer sie die Möglichkeit hatte, darzulegen und durch  Unterlagen nachzuweisen, warum die Beschwerdefrist entgegen dem dargestellten  Sachverhalt nicht am 4.2.2021 zu laufen begonnen und am 4.3.2021 geendet hat.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_60`)


Dieser Sachverhalt ergibt sich aus dem vorgelegten Verwaltungsakt und dem Vorbringen der  Bf.  Rechtsgrundlagen - Rechtliche Würdigung:  Gemäß § 1 Wiener Parkometerabgabeverordnung ist für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen (§ 25 StVO) eine Abgabe zu entrichten.

**False Positives:**

- `Rechtsgrundlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_474`)


Dass im gegenständlichen Besteuerungszeitraum von der Bf. Sportwetten und Ausspielungen  veranstaltet wurden, an der (auch) Spieler teilnahmen, die sich - körperlich – im Inland  aufhielten, wird auch von der Bf. nicht bestritten.

**False Positives:**

- `Sportwetten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_533`)


Die Bf. hat ihren Sitz in Gibraltar und besteht deshalb eine erhöhte  Mitwirkungspflicht der Bf.  Der Bf. war bekannt, dass das Finanzamt auf Grund des -nach der oa.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_563`)


3. Zu den unionsrechtlichen Einwänden der Bf.   Nach Artikel 267 AEUV entscheidet der EuGH im Wege der Vorabentscheidung über die  Auslegung der Verträge sowie über die Gültigkeit und die Auslegung der Handlungen der  Organe, Einrichtungen oder sonstigen Stellen der Union.

**False Positives:**

- `Nach Artikel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_614`)


Andernfalls ist der um den geltend gemachten Rabatt verminderte Einsatz in  Ansatz zu bringen.“  4.2 Ausgestaltung der BONI der Bf.  Es ist somit für die Frage der Einbeziehung der „Boni“ in die Bemessungsgrundlage die  jeweilige konkrete Ausgestaltung der Boni relevant.

**False Positives:**

- `Es` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_7`)


Mit Schreiben vom 31.7.2021 erhob die Bf Beschwerde gegen diesen Bescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_97`)


1.5. Vorlageantrag des Bf   Mit Schreiben vom 20. Oktober 2017 beantragte der Bf die Vorlage der Beschwerde an das  Bundesfinanzgericht.

**False Positives:**

- `Mit Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_25`)


Beschwerde  Fristgerecht wurde von der Bf Beschwerde erhoben und vorgebracht:  “Die Darstellung des Finanzamtes, dass der Vertragserrichter Dr-F die Baukosten für das später  errichtete Gebäude auf der vertragsgegenständlichen Liegenschaft in die  Bemessungsgrundlage hätte aufnehmen müssen, weil die Käufer an ein bestimmtes durch die  Planung des Verkäufers oder eines mit diesem zusammen arbeitenden Organisator als  vorgegebenes Gebäude gebunden waren, ist falsch.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_22`)


Weder in den Beschwerden noch in den Vorlageanträgen oder infolge des Schreibens des BFG  vom 2.3.2022 brachte der Bf. Argumente vor, dass ihm die Einkommensteuerbescheide 2017  und 2018 nicht rechtzeitig zugegangen seien bzw. er einen Verzicht auf die elektronische Form  der Zustellung nicht abgegeben habe.

**False Positives:**

- `Argumente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_114`)


Zufolge der Bestätigung der Familienkasse Bauern-Süd bezog Betreuerin für den Bf. Kindergeld  in Deutschland und wurde dieses ab dem Monat April 2020 gemäß § 70 Abs. 2 dEStG  aufgehoben.

**False Positives:**

- `Kindergeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_17`)


Da keiner der in § 3 Abs. 1 der VO zu §§ 34 und 35, BGBl. 1996/303 idgF, genannten Nachweise  vorgelegt worden sei, stehe der Freibetrag nicht zu.  Beweiswürdigung:  Der festgestellte und unstrittige Sachverhalt ergibt sich aus den vom Finanzamt vorgelegten  Aktenteilen sowie dem Vorbringen der Bf.  Rechtslage:  Nach § 35 Abs. 1 EStG 1988 steht einem Steuerpflichtigen, der außergewöhnliche Belastungen  durch eine eigene körperliche oder geistige Behinderung hat und der keine pflegebedingte  Geldleistung (Pflegegeld, Pflegezulage, Blindengeld oder Blindenzulage) erhält, ein Freibetrag  (Abs. 3) zu.  Nach § 35 Abs. 2 EStG 1988 bestimmt sich die Höhe des Freibetrages nach dem Ausmaß der  Minderung der Erwerbsfähigkeit (Grad der Behinderung).

**False Positives:**

- `Rechtslage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_57`)


Beschwerde  Innerhalb offener Frist wurde von der Bf Beschwerde erhoben und im Wesentlichen unter  Hinweis auf § 6 GrEStG – vor Inkrafttreten der Novelle 01.06.2014 - vorgebracht, dass mit der  Schätzung des Architekten Dipl. Ing. J M für das Kaufgrundstück ein gemeiner Wert von ca. €  235.000,00 nachgewiesen worden sei.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_101`)


3.9. Vorlageantrag vom 11. Jänner 2021  Dagegen stellte der Bf Vorlageantrag und beantragte die Entscheidung des  Bundesfinanzgerichtes sowie die Abhaltung einer mündlichen Verhandlung unter Ladung aller  Beteiligten.

**False Positives:**

- `Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138259.1`) (sent_id: `deanon_BFG_20260814_TEST/138259.1_17`)


Am 22.6.2020 erhob der Bf Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_8`)


Rahmen eines Antrages nach § 295a BA0 die Kosten nachträglich berücksichtigt werden - siehe  dazu auch LStR 2002 Rz 385" (BFG-Akt AS 34 ff)  Mit Schreiben vom 20. Februar 2020 erhob die Bf. Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_249`)


Nach Einbringung eines Rechtsmittels gegen den Baustopp und Nachholung des Antrages auf  Baubewilligung, erteilte die Baubehörde dem Bf Mitte Juli 2000 eine Bewilligung für einen  „Um- und Zubau“ des Wohnhauses HNr 111.

**False Positives:**

- `Mitte Juli` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_459`)


Erst nach erfolgter Baueinstellung beantragte der Bf Anfang Dez.2007 die Erteilung einer  Baubewilligung für die Errichtung der Zufahrtsstraße auf der Parzelle GStNr 999/2 samt  Zutrittstoranlage (Schranken) im Bereich der Abfahrt von der Landesstraße (Einreichplan der E- GmbH vom 28.Nov.2007).

**False Positives:**

- `Anfang Dez` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_486`)


Erst nach erfolgter Asphaltierung der Zufahrtsstraße brachte der Bf Mitte Juli 2009 einen mit  2.Juni 2009 datierten Antrag auf Erteilung einer Baubewilligung zur Errichtung des Carports  und der Stützmauer samt zugehöriger Geländeveränderungen ein.

**False Positives:**

- `Mitte Juli` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_701`)


Wohnung W 2 durch die Gattin des Bf. Zugleich wurde die Privatnutzung der Wohnung  eingeräumt.

**False Positives:**

- `Zugleich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1188`)


Nachdem die Finanzierungsbank des  Bauvorhabens keine Bereitschaft zur Bereitstellung weiterer Mittel gezeigt hatte, wechselte  der Bf Ende 2004 die Bank.

**False Positives:**

- `Ende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_7`)


3. Mit FinanzOnline-Eingabe vom 14.04.2022 erhob der Bf Beschwerde gegen diesen Bescheid  und führte aus, dass die am 26.01.2022 angeforderten Unterlagen/Fahrtenbuch, Mietvertrag,  E9 seiner Frau am 14.02.2022 per Post geschickt worden seien und er diese nochmals  übermittle.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_55`)


Mit Schreiben vom 21. Dezember 2020 teilte die Bf. Folgendes mit:   … ich kann ihnen nun den Ambulanzbefund des Landesklinikum Baden-Mödling zukommen  lassen.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_7`)


Mit Eingabe vom 5. Juni 2020 erhob der Bf. Beschwerde, in der er im Wesentlichen vorbringt,  die Indexierung der steuerlichen Begünstigungen sei diskriminierend und unionsrechtswidrig.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_23`)


Vienna GmbH sowie zwei von Frau an die Bf. gerichtete Schreiben vom 23.5.2017 und vom  10.8.2017 in denen diese bestätigt, von der Bf. Euro 13.000,00 und Euro 998,00 für die  Zahlungen der Modul University für das „2nd, 3rd und 4th Installment“ sowie für das „4th  Installment“ in bar erhalten zu haben, bei.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_416`)


Darin hat der Bf. Erwiderungen  und ergänzendes Vorbringen zu den Ausführungen in der Niederschrift vom 7.9.2015 getätigt,  26 von 33 Seite 27 von 33

**False Positives:**

- `Erwiderungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_29`)


Wegen  Verletzung der Rechtsvorschriften des § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz wurden  über den Bf. Geldstrafen von je 60,00 € und für den Fall der Uneinbringlichkeit  Ersatzfreiheitsstrafen von je 14 Stunden verhängt.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/140320.1`) (sent_id: `deanon_BFG_20260814_TEST/140320.1_17`)


Beweiswürdigung:  Die getroffenen Feststellungen ergeben sich zweifelsfrei aus dem Steuerakt des Bf.  Die Feststellung, dass der Bf am 21.10.2022 den Einkommensteuerbescheid ausgelesen hat,  war aufgrund einer Mitteilung der Verfahrensbetreuung des Finanzamtes Österreich zu treffen.

**False Positives:**

- `Die Feststellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_92`)


In der auf das Telefonat vom 28.Juli 2014 folgenden Besprechung mit dem FA hatte der Gatte  der Bf Anfang August 2014 darauf verwiesen, dass beide Ehepartner in Österreich leben, er  jedoch in Deutschland in die unbeschränkte Steuerpflicht optiert habe (Option nicht aufgrund  7 von 30 Seite 8 von 30

**False Positives:**

- `Anfang August` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_127`)


Auch mit dem Vorbringen in der Beschwerde vom 28. September 2021, wonach bereits im  Februar 2020 der Prüfungsabteilung mitgeteilt worden sei, der Bf. sei niemals im Service tätig  gewesen, habe über keinen Kellnerschlüssel verfügt, habe sich aufgrund eines Traktorunfalles  im August 2016 bis Mai 2017 im Krankenhaus befunden und sei danach an den Rollstuhl  gefesselt gewesen und habe sich erst später nur mühsam mit Krücken fortbewegen können,  und daher auszuschließen sei, dass dem Bf. Geldmittel zugeflossen seien, hat sich das  Finanzamt in der Beschwerdevorentscheidung vom 01.09.2022 nicht auseinandergesetzt.

**False Positives:**

- `Geldmittel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_129`)


Feststellungen und konkrete Ermittlungen dahingehend, ob bzw. in welcher Höhe dem Bf.  Geldmittel aus den Kalkulationsdifferenzen unter Mitberücksichtigung der seitens der  steuerlichen Vertretung aufgezeigten Einwände, wurden vom Finanzamt nicht getroffen.

**False Positives:**

- `Geldmittel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_157`)


Im Erkenntnis vom 28.05.2018, RV/7101269/2018, erwog das BFG: Im Zeitraum Juni 2011 bis  September 2011 bezog der Sohn der Bf. Arbeitslosengeld.

**False Positives:**

- `Arbeitslosengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_208`)


Selbst wenn man  dem Begehren des Bf. Folge gegeben hätte, wäre nicht ausgeschlossen, dass er im Laufe der  Jahre (bedeutend) mehr als die tatsächlichen ursprünglichen Anschaffungskosten abschreibt.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_205`)


dem Begehren des Bf. Folge gegeben hätte, wäre nicht ausgeschlossen, dass er im Laufe der  Jahre (bedeutend) mehr als die tatsächlichen ursprünglichen Anschaffungskosten abschreibt.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/141437.1`) (sent_id: `deanon_BFG_20260814_TEST/141437.1_24`)


Aus diesem Schreiben lässt sich aber  nicht pauschal auch für all jene Produkte, für die der Bf kein Rezept vorgelegt hat, schließen,  dass diese Produkte ärztlich verordnet worden wären, zumal sich die Bestätigung des Arztes  mit jenen Arzneien deckt, für die der Bf Rezepte vorgelegt hat.

**False Positives:**

- `Rezepte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_46`)


8. Gegen die Beschwerdeentscheidung des BFG vom 16.4.2019, RV/1101048/2015, erhoben  sowohl das Finanzamt als auch der Bf. Revisionen an den Verwaltungsgerichtshof.

**False Positives:**

- `Revisionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamt`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_9`)


Mit Bescheid vom 09.09.2022 forderte das FA von der Bf Familienbeihilfe und  Kinderabsetzbetrag für die Kinder K1, K2, K3 und K4 für die Zeit von April 2022 bis September  1 von 13 Seite 2 von 13

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_91`)


Mit Vorhalt vom 05.06.2023 brachte das BFG das Vorhalteverfahren dem FA zur Wahrung des  Parteiengehörs zur Kenntnis und merkte ua noch Folgendes an:  Dem von Seiten des Caritas Dorf H geführten Kassabuch betreffend K1 sei zu entnehmen, dass  in den Monaten April 2022 bis September 2022 von der Bf insgesamt 300,00 Euro einbezahlt  worden seien, wobei Ende September 2022 ein Minus von 55,61 Euro entstanden sei und die  Bf Anfang Oktober 250,00 Euro eingezahlt habe.

**False Positives:**

- `Anfang Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_185`)


In den Monaten April 2022 bis September 2022 wurden von der Bf  insgesamt 300,00 Euro einbezahlt, wobei Ende September 2022 ein Minus von 55,61 Euro  entstand und die Bf Anfang Oktober 250,00 Euro einzahlte.

**False Positives:**

- `Anfang Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_209`)


Unter Beachtung der Grundsätze der freien Beweiswürdigung ist somit für die Monate April  2022 bis September 2022 davon auszugehen, dass die Bf Unterhaltsleistungen zu den Kosten  ihrer Tochter zumindest in Höhe der erhöhten Familienbeihilfe beitrug.

**False Positives:**

- `Unterhaltsleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_59`)


Nachdem eine für Dienstverhältnisse erforderliche Kontrollunterworfenheit oder  wirtschaftliche Abhängigkeit nicht gegeben und die Weisungsgebundenheit auf Grund des  vereinbarten und gelebten Vertragsverhältnisses nicht gegeben sei, diese sogar explizit  ausgeschlossen ist, könne ein Dienstverhältnis im Sinne des EStG keinesfalls vorliegen, so die  Bf.   Und weiter: „Der GPLA-Prüfer und die Finanzbehörde gehen davon aus, dass während der  oben genannten Zeit, in welcher Herr NR auch als Geschäftsführer im Firmenbuch eingetragen  war, dessen Bezüge zwingend als solche gem. § 22 Z 2 zweiter Teilstrich EStG anzusehen seien.

**False Positives:**

- `Und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/143111.1`) (sent_id: `deanon_BFG_20260814_TEST/143111.1_48`)


In welchen Zeiträumen sei die Bf Teilnehmerin bei FinanzOnline gewesen?

**False Positives:**

- `Teilnehmerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_43`)


Mit weiterem Schriftsatz vom 02.11.2023 erhob die Bf. Einwendungen gemäß § 87 Abs. 6 BAO  gegen das Protokoll über den Erörterungstermin und führte zur darin festgehaltenen  Außerstreitstellung im Zusammenhang mit der Überschreitung der „2%-Marge“ aus, dass sich  diese auf das Verhältnis zwischen den unter ein und derselben Projektnummer verbuchten  3 von 23 Seite 4 von 23

**False Positives:**

- `Einwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_320`)


Wir ergänzen im Folgenden die im Ermittlungsbericht des Finanzamtes auf Seite 4 von 5  enthaltene Aufstellung der steuerlichen Jahresergebnisse der Bf.   Laut Erstbescheid/Erklärung Kumuliertes Ergebnis  2006 -8.523,95   2007 -6.735,21 -15.259,16  2008 +4.247,16 -11.012,00  2009 -12.067,28 -23.079,28  2010 -11.234,95 -34.314,23  2011 -57.740,54 -92.054,77  2012 -102.049,70 -194.104,47  2013 -118.133,09 -312.237,56  2014 2.300,00 -309.937,45  2015 11.652,40 -298.285,05  2016 36.037,67 -262.247,38  2017 34.059,36 -228.188,02  2018 68.763,60 -159.424,42  2019 36.976,29 -122.448,13  2020 72.947,17 -49.500,96  Vorl.

**False Positives:**

- `Laut Erstbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_6`)


Am 21.07.2023 erhob die Bf Beschwerde gegen den Rückforderungsbescheid vom 06.07.2023.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_10`)


Gemäß Artikel 18 Abs. 1 des  Doppelbesteuerungsabkommens (DBA) Österreich/BRD komme Österreich als  Ansässigkeitsstaat das Besteuerungsrecht für die Firmenrente der Firma MH* zu.  Dagegen erhob der Bf. Beschwerde „bis die ausländischen Einkünfte geklärt sind.“

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/143631.1`) (sent_id: `deanon_BFG_20260814_TEST/143631.1_37`)


Beschwerde  Innerhalb offener Frist wurde vom Bf Beschwerde erhoben und vorgebracht:  Die Stadtgemeinde A hat im eigenen Namen und als Verwalterin des öffentlichen Gutes mit  zahlreichen Parteien den Baulandumlegungsvertrag abgeschlossen.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_199`)


Der A. (Krankenanstalten,  Krankenhaus P. und Pflegeheime) sei ebenfalls ein einheitlicher Betrieb gewerblicher Art, da  dieser grundsätzlich eine Einheit („Unternehmung“ iSd § 72a Bf. Stadtverfassung) darstelle.

**False Positives:**

- `Stadtverfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_256`)


Es bestehe allerdings die  Besonderheit, dass gemäß § 72a der Bf. Stadtverfassung die Krankenanstalten und  Pflegeheime in einem A. zusammengefasst und quasi als „Unternehmung“ der Bf geführt  werden können.

**False Positives:**

- `Stadtverfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_342`)


Zum A.:  Der A. sei gemäß § 72 der Bf. Stadtverfassung eine „Unternehmung“ der Bf.

**False Positives:**

- `Stadtverfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/144140.1`) (sent_id: `deanon_BFG_20260814_TEST/144140.1_184`)


Es steht somit nur für die 4 Monate, in denen die Gattin des Bf. Anspruch auf die  Familienbeihilfe hatte, der Familienbonus Plus, in Höhe von (54,18*4) € 216,72 zu. Dieser  wurde bereits im angefochtenen Bescheid berücksichtigt.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_8`)


2. Festzuhalten ist, dass die Bezirkshauptmannschaft (BH) zugleich mit der jeweiligen  Erledigung bzw. "Mitteilung der fachlichen Befähigung" je gemeldetem Schilehrer vom  25.2.2016, 7.3. und 24.3.2016 an die Bf Bescheide betr.

**False Positives:**

- `Bescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_108`)


Bereits in den Jahren davor – am 7. April 2021 sowie am  6. Mai 2022 – hatte die Bf. Meldungen gemäß § 5 WiEReG erstattet.

**False Positives:**

- `Meldungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_24`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:   Sachverhalt:   Mit Beschwerde vom 17.10.2023 gegen den Einkommensteuerbescheid für das Jahr 2022 vom  16.10.2023 machte der Bf Aufwendungen für Familienheimfahrten geltend.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_6`)


Dagegen erhob der Bf. Beschwerde mit der Begründung, dass sein Jahreseinkommen für das  Jahr 2022 Euro 34.675,28 betragen würde und er um Neuberechnung ersuche.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_110`)


Die im Verfahren vorgelegte Gleitzeitvereinbarung des Bf mit seinem Dienstgeber vom  August 2017 ließ ausreichend Spielraum für eine flexible Anpassung des Arbeitsbeginns bzw.  Arbeitsendes an die Fahrpläne des Regionalbusses 9999 durch den Bf. Auch an Arbeitstagen  mit Arbeitsbeginnzeiten zwischen 8:30 und 9:30 Uhr, die nach den Arbeitsaufzeichnungen des  Bf weitaus überwogen, standen nach einer regelmäßigen/überwiegenden Arbeitszeit von neun  Stunden zumutbare Busverbindungen zur Verfügung.

**False Positives:**

- `Auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_263`)


Zum Jahr 2019 begehrte der Bf Werbungskosten für 14 vom Dienstgeber bestätigte  Dienstreisen, regelmäßig beginnend am Betriebs-/Arbeitsort, für die der Bf „im Jahr 2019“  keinen Kilometergeldersatz erhalten habe.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_287`)


Für 2019 wurde vom Dienstgeber der Dienstreisecharakter aller Reisebewegungen bestätigt, zu  welchen der Bf Werbungskosten geltend machte.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_373`)


Behandlung (lt. Bf Zahlung  8.Febr.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch Rechnung, Zahlung  oder ÖGK-Kostenersatz.

**False Positives:**

- `Zahlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖGK`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/145929.1`) (sent_id: `deanon_BFG_20260814_TEST/145929.1_12`)


Dagegen erhob der Bf. Beschwerde mit der Begründung, er habe im Oktober 2021 einen  großen Auftrag im Volumen von etwa 70% seines Umsatzes erhalten.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_19`)


In der Einkommensteuererklärung 2017 beantragte der Bf. Sonderausgaben in Höhe von  € 457,87, die erklärungsgemäß berücksichtigt wurden.

**False Positives:**

- `Sonderausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_161`)


Am 24.9.2003 wurde ein erhöhter Homocysteinwert festgestellt. Im Befund ist auch  festgehalten, dass der Bf. Augenblutungen hat.

**False Positives:**

- `Augenblutungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/146695.1`) (sent_id: `deanon_BFG_20260814_TEST/146695.1_56`)


Die  Familienbeihilfenbezieherin ist im vorliegenden Fall die Kindesmutter, die Frau des Bf. Der Bf.  selbst hatte im Jahr 2021 weder Anspruch auf den Unterhaltsabsetzbetrag, noch bezog er  Familienbeihilfe für seine beiden Stiefkinder.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_137`)


Außer Streit gestellt wurde, dass das Fahrzeug in Österreich verwendet wurde, dass die Bf  ihren Hauptwohnsitz und Mittelpunkt der Lebensinteressen ab dem 30.4.2018 (=  Hauptwohnsitzmeldung laut ZMR) in Österreich hatte und dass die Bf Verwenderin des  gegenständlichen Fahrzeuges in Österreich war.

**False Positives:**

- `Verwenderin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_162`)


Von 2.3.2020 bis 22.6.2020 bezog die Bf Wochengeld und befand sich danach wieder in Karenz.

**False Positives:**

- `Wochengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_443`)


Nach den dargestellten Sachverhaltsfeststellungen ist dies  unzweifelhaft die Bf. Wie im Sachverhalt festgestellt und aus der Beweiswürdigung ersichtlich,  übt die Bf im streitgegenständlichen Zeitraum die Verfügungsgewalt aus, zumal sie bestimmt  wann sie nach Deutschland fährt bzw. wann sie mit dem Fahrzeug wohin fährt, wie lange sie an  welchem Ort bleibt und auch ein Teil der Kostentragung für Tankrechnungen und die  Jahresvignette in Österreich von der Bf getragen werden.

**False Positives:**

- `Wie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_453`)


Dies ist im gegenständlichen Fall  die Bf.  Wie in der Beweiswürdigung ausgeführt, konnte im gegenständlichen Fall jedoch bereits keine  Zuordnung zu einem „zweiten“ Standort außerhalb Österreichs erfolgen.

**False Positives:**

- `Wie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/147471.1`) (sent_id: `deanon_BFG_20260814_TEST/147471.1_198`)


Die Versicherung diente daher auf  Grund der dargestellten Vertragsgestaltung neben der behaupteten Darlehenssicherung in  nicht bloß geringfügigem Ausmaß auch wesentlichen anderen Zwecken, nämlich einer – aus  welchen Motiven auch immer intendierten - Absicherung der Darlehensnehmerin für den Fall  des Ablebens des Bf.  Wenn der Bf. im Beschwerdeschriftsatz vom 29.7.2019 vorbringt, dass sich das Original der  Polizze in seinen Händen befunden und A bei seinem Ableben daher kein Geld erhalten hätte,  so ist zu erwidern, dass sich dies aus der vorliegenden Polizze nicht ergibt.

**False Positives:**

- `Wenn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_113`)


Der Sachwalter legte im Zuge des Verfahrens folgende Unterlagen vor:  • Stellungsuntersuchungsergebnis des Militärkommando Wien vom 28. August 2013  Der Bf. wurde auf Grund verschiedener Erkrankungen (Morbus Sauermann  [Wachstumsstörung der jugendlichen Wirbelsäule], Senk-Fuß, Ellbogenfraktur li, Nervosität) als  ungeeignet eingestuft.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_24`)


Laut Aktenvermerk vom 27. Februar 2020 (Akt Seite 41/58) teilte der Bf. dem Ma- gistrat der Stadt Wien mit, dass er sich dazu nicht äußere.

**False Positives:**

- `Akt Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_78`)


2. Bescheid vom 24. November 2020 über die Zurückweisung des Antrages auf Aussetzung  der Einhebung vom 22. März 2020:  Mit Erkenntnis vom 25. Februar 2021, GZ.RV/7104659/2020, hat das Bundesfinanzgericht im  Senat die Beschwerde vom 22. März 2020 gegen den Bescheid des ehemaligen Finanzamtes  Wien 1/23 vom 4. März 2020 betreffend Aussetzung der Einhebung gemäß § 212a BAO  hinsichtlich der Einkommensteuernachforderungen und Anspruchszinsen für die Jahre 2008-

**False Positives:**

- `Mit Erkenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_226`)


VORHALTSBEANTWORTUNG durch das FINANZAMT vom 09. März 2020  Das Finanzamt räumte ein, dass der streitgegenständlichen Abzugsteuervorschreibung (für die  Jahre 2014 bis 2015) Verträge und FINPOL-Feststellungen aus dem Jahr 2016 zu Grunde gelegt  worden seien, da die FINPOL eben in diesem Jahr die Erhebungen gepflogen habe.

**False Positives:**

- `Das Finanzamt` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_248`)


Zudem hat mittlerweile der Verwaltungsgerichtshof (siehe das Erkenntnis vom  22.08.2017, Ra 2017/11/0068, Rz. 29) ausgeführt, dass die Erfüllung der von § 4 des  Arbeitskräfteüberlassungsgesetzes normierten Kriterien aus unionsrechtlicher Sicht   nach aktueller Judikatur des EuGH im Urteil vom 18. Juni 2015 "Martin Meat" (C-  586/13) keine ausreichenden Abgrenzungskriterien darstellen.

**False Positives:**

- `Martin Meat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_346`)


Den vom Finanzamt bzw. der GPLA – Prüfung diesbezüglich ins Treffen geführten  Erwägungen bzw. den angesprochenen Beweismitteln ist nämlich entgegen zu halten:  Zu den Bestimmungen des Arbeitskräfteüberlassungsgesetzes  Wie bereits oben ausgeführt, hat mittlerweile der Verwaltungsgerichtshof (im  Erkenntnis vom 22.08.2017, Ra 2017/11/0068, Rz. 29) ausgesprochen, dass die  Erfüllung der von § 4 des AÜG  normierten Kriterien aus unionsrechtlicher Sicht - nach  aktueller Judikatur des EuGH im Urteil vom 18. Juni 2015 "Martin Meat" (C- 586/13)  keine ausreichenden Abgrenzungskriterien für die Beantwortung der Frage darstellen,  ob Werkvertrag oder Arbeitskräftegestellung vorliegt.

**False Positives:**

- `Martin Meat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Hemma Mauermair`(person)
- `Franziska Fitzmann`(person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich`(address)
- `Mag. Markus Franz Ganzer`(person)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_96`)


Beschwerde vom 27. Oktober 2020  Der Bf erhob Beschwerde gegen den Bescheid und begründete sie damit, dass das Lokal von  ihm selbst nie betrieben, sondern zeitweise vermietet gewesen wäre, wie er bereits mit  seinem mail vom 14. September 2020 mitgeteilt hätte, gleichwohl wie, dass er keinen Zugang  zu den Unterlagen hätte, weil sie von der Staatsanwaltschaft Leoben sichergestellt worden  wären und ihm bis dato der Zugang nicht möglich sei.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_106`)


4.2. Ermittlungen und Beschluss Bundesfinanzgericht inklusive Auftrag der  Zeugenvernehmung durch die belangte Behörde vom 26. April 2022  Im Zuge der Ermittlungen des Bundesfinanzgerichts waren einige Punkte offen und das  Bundesfinanzgericht richtete daher einen Vorhalt zur Ermittlung des Sachverhaltes an den Bf  und die belangte Behörde.

**False Positives:**

- `Im Zuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgerichts`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_134`)


Zweite Beantwortung des Bf vom 24. Mai 2022  Der Bf teilte mit Schreiben vom 24. Mai 2022 mit, dass ihm auf Grund seines Schreibens vom 5.  Mai 2022 an die Staatsanwaltschaft Leoben von dieser Akteneinsicht gewährt worden sei, der  er am 19. Mai nachgekommen sei.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_30`)


Bescheid vom 13. September 2019:  Das Finanzamt setzte mit angefochtenem Bescheid vom 13.09.2019 ausgehend von einer  Bemessungsgrundlage iHv Euro 1,220.376,73 die Gebühr gemäß § 30 TP 20 Abs. 1 lit b. GebG   iHv Euro 24.407, 53 fest.

**False Positives:**

- `Das Finanzamt` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_31`)


Begründend wurde ausgeführt, dass aus der schriftlichen Beantwortung des Vorhalts vom  06.05.2019 sich nachfolgende Werte nach § 16 Bewertungsgesetz (BewG) für die Ermittlung  der Bemessungsgrundlage ergeben haben:  Restkredit:  Euro 593.000,00  Wohnrecht:  Euro 196.055,22  Betriebskosten: Euro 58.816,57  Unterhalt:   Euro 372.504,93    Summe:  Euro 1.220.376,73  Beschwerde vom 29. Juni 2023:  Mit Beschwerde vom 29.06.2019 wird der Bescheid dem Grunde und der Höhe nach zur Gänze  angefochten.

**False Positives:**

- `Mit Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_62`)


Beschwerdevorentscheidung vom 13. September 2019:  Das Finanzamt wies mit Beschwerdevorentscheidung vom 13.09.2019 die Beschwerde als  unbegründet ab.

**False Positives:**

- `Das Finanzamt` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_69`)


Vorlageantrag vom 19. September 2019:  Mit Vorlageantrag beantragt der Bf. die mündliche Verhandlung im Senat.

**False Positives:**

- `Mit Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Wilhelmine Strigl  in der Beschwerdesache Dominik Barfusz,  Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich, über die Beschwerde vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 18. März 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  "Zuerkennung der Familienbeihilfe für den Zeitraum ab Februar 2023" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Wilhelmine Strigl`(person)
- `Dominik Barfusz`(person)
- `Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_5`)


Umsatzsteuer 2006 vom 5. Mai 2008  Umsatzsteuer 2007 vom 15. September 2008  Umsatzsteuer 2008 vom 2. September 2009  Umsatzsteuer 2009 vom 20. Dezember 2010  Die Umsatzsteuer für das Jahr 2010 wird festgesetzt:  Gesamtbetrag der steuerpflichtigen  Lieferungen, sonstigen Leistungen und  Eigenverbrauch (einschließlich  steuerpflichtiger Anzahlungen)  0,00 €  Summe Umsatzsteuer 0,00 €  1 von 51 Seite 2 von 51

**False Positives:**

- `Die Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_11`)


Körperschaftsteuer 2009 vom 20. Dezember 2010  Die Körperschaftsteuer für das Jahr 2010 wird wie folgt berechnet:  Einkünfte aus Gewerbebetrieb -11.234,95 €  Gesamtbetrag der Einkünfte -11.234,95 €  Einkommen 0,00 €  Die Körperschaftsteuer vom Einkommen  beträgt:  Gem. § 22 KStG 1988  25% von 0,00 €  0,00 €  Differenz zur Mindestkörperschaftsteuer 1.750,00 €  Körperschaftsteuer 1.750,00 €  Einbehaltene Steuerbeträge -1,54 €  Rundung gem. § 39 Abs. 3 EStG 1988 -0,46 €  Festgesetzte Körperschaftsteuer 1.748,00 €

**False Positives:**

- `Die Körperschaftsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/146562.1`) (sent_id: `deanon_BFG_20260814_TEST/146562.1_81`)


5. Beschwerdevorentscheidung vom 11. September 2023:  Die Beschwerde gegen den Einkommensteuer-Vorauszahlungsbescheid 2023 wurde mit  Beschwerdevorentscheidung vom 11. September 2023 als unbegründet abgewiesen.

**False Positives:**

- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/146562.1`) (sent_id: `deanon_BFG_20260814_TEST/146562.1_88`)


6. Vorlageantrag vom 18. September 2023:  Mit Vorlageantrag vom 18. September 2023 beantragte der Bf. die Vorlage der Beschwerde zur  Entscheidung durch das Bundesfinanzgericht.

**False Positives:**

- `Mit Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/149310.1`) (sent_id: `deanon_BFG_20260814_TEST/149310.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Beate Gützlaf  in der Beschwerdesache Priv.-Doz.in Alina Vriesman,  Willing 25N, 2561 Pöllau, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Mai 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  Familienbeihilfe für den Zeitraum „April 2023 – September 2023“ zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Beate Gützlaf`(person)
- `Priv.-Doz.in Alina Vriesman`(person)
- `Willing 25N, 2561 Pöllau, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_7`)


Beschwerde vom 10. Juni 2021  Die Bf. brachte in ihrer Beschwerde vor, dass sie bis dato auf ihr Konto Adelheid Lokaizyk  in Österreich  keine Familienbeihilfe ausbezahlt bekommen habe.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Adelheid Lokaizyk`(person)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (984, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache **RgR Tanja Tihl, BSc**,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `RgR Tanja Tihl, BSc` (person)
- predicted in sentence: `Univ.-Prof.in Shirley Vostrovsky`, `RgR Tanja Tihl`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)

Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  **Dr. Thomas Hofer-Zeni** gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

- missed: `Dr. Thomas Hofer-Zeni` (person)
- predicted in sentence: `Dr. Thomas Hofer`, `Dr. Thomas Hofer`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache **Lewis Rzehula**, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Lewis Rzehula` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)

Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr **Abeles** bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

- missed: `Abeles` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)

Herr **Bodewein** brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

- missed: `Bodewein` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden **Mag. Marco Laudacher**, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

- missed: `Mag. Marco Laudacher` (person)
- predicted in sentence: `Bettina Domigall`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`, `Ing. OSR Julia Strutwolf`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  **Elias von Wnuk-Lipinski**, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Elias von Wnuk-Lipinski` (person)
- predicted in sentence: `Univ.-Prof.in Ada Forstner`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag. Gerhard Konrad** in der  Verwaltungsstrafsache gegen Gudrun Joehnk, Lichtenberger Straße 9, 4751 Obernparz, Österreich, über die Beschwerde der  Beschuldigten vom 15. Mai 2024 gegen den Bescheid des Magistrates der Stadt Wien vom 24.  April 2024, GZ. MA67/GZ/2023, mit dem der Einspruch vom 8. April 2024 gegen die  Strafverfügung vom 8. Februar 2024, mit derselben Geschäftszahl, gemäß § 49 Abs 1 VStG als  verspätet zurückgewiesen wurde, zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen und der angefochtene  Zurückweisungsbescheid bestätigt.

- missed: `Mag. Gerhard Konrad` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_71`)

**Dr. Maida,** Neurologie- und Psychiatriefachärztin.

- missed: `Dr. Maida,` (person)
- predicted in sentence: `Dr. Maida`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_73`)

Sofern dies der Fall war, fiel der in § 5 Abs 3 FLAG 1967 normierte  Ausschlussgrund für eine Beihilfengewährung in diesem Monat weg und ein  Familienbeihilfenanspruch der Bf für ihre Tochter im Juni 2023 wäre etwa dann gegeben, wenn  sich **Heidemarie Fitzenreiter**  in einer Ausbildung befunden hat, die als Berufsausbildung im Sinne des  § 2 Abs 1 lit b FLAG 1967 qualifiziert.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)

Sie sehen im Anhang dass Herr **Abeles** damit bis 27 Dezember  gefahren ist.

- missed: `Abeles` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_15`)

Da der Bescheid im Beschwerdefall nicht an den tatsächlichen Zustellungsbevollmächtigten  „**Dipl.-Ing. KzlR Juri Strube**“, sondern die „Hemma Bödker“ adressiert war, vermag er für die Bf. keine  Rechtswirkung zu entfalten.

- missed: `Dipl.-Ing. KzlR Juri Strube` (person)
- predicted in sentence: `Dipl.-Ing. Kzl`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  **Leonie Wehrlin, Bakk. iur.**, Karl-List-Weg 20, 4222 Frankenberg, Österreich, über die Beschwerde vom 30. Dezember 2021 gegen die Bescheide  des Finanzamtes Österreich vom 30. November 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, 2019 und 2020, Steuernummer 01-053/2123  zu Recht  erkannt:   I. Der Beschwerde wird für die Jahre 2018 im Sinne der Beschwerdevorentscheidung vom  18.2.2022 gemäß § 279 BAO teilweise stattgegeben.

- missed: `Leonie Wehrlin, Bakk. iur.` (person)
- predicted in sentence: `Leonie Wehrlin`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)

Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, **Prof.in StR DDr.in Reneé Plein**  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

- missed: `Prof.in StR DDr.in Reneé Plein` (person)
- predicted in sentence: `Dr.in Rene`

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, den Richter  **Mag.Dr. Wolfgang Pagitsch** sowie die fachkundigen Laienrichter Manfred Fiala und DI Thomas  Hrdinka in der Beschwerdesache Saskia Spinnehörn, Gänsdorf 4, 4224 Wolfsegg, Österreich, vertreten durch BONAFIDE  Treuhand- und Revisions- gesellschaft m.b.H., Berggasse 10, 1090 Wien, über deren  Beschwerde vom 15. April 2019 gegen den Bescheid des Finanzamtes Österreich (vormals  Finanzamtes Wien 4/5/10 ) vom 5. April 2019 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten, Steuernummer 59-301/9085, nach Durchführung einer  mündlichen Verhandlung am 12. September 2023 in Anwesenheit der Schriftführerin Nadine  Bernold zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag.Dr. Wolfgang Pagitsch` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Dr. Wolfgang Pagitsch`, `Saskia Spinnehörn`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)

Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr**  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

- missed: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr` (person)
- predicted in sentence: `Hon.-Prof.in Mag`, `Priv.-Doz.in Waltraud Süßmayr`, `Hon.-Prof.in Techn R Huberta Pauwels`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, **Hermann**-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Hermann` (person)
- predicted in sentence: `OSR Corbinian Friemuth`

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_3`)

Begründung  Aus den dem Gericht vorgelegten Unterlagen und dem elektronischen Akt ist ersichtlich, dass  die belangte Behörde (FA) am 6.3.2018 mittels Bescheid gemäß § 92 Abs. 1 lit. c BAO  feststellte, dass hinsichtlich des **Daniel Parys** (Beschwerdeführer, Bf.) im Zeitraum 2014 bis 2016  keine Unternehmereigenschaft vorlag.

- missed: `Daniel Parys` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache **Isidor Czebulla**, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

- missed: `Isidor Czebulla` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_232`)

Das "Vorliegen  der Störung seit Geburt" laut **Dr. F** aufgrund des Gendefektes ist sohin in obigem Sinne nicht,  wie die Bf vermeint, dem Eintritt bereits einer erheblichen Behinderung gleichzuhalten.

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_9`)

Dem  Bericht über das Ergebnis der Außenprüfung vom 7. Oktober 2011 sind auszugsweise folgende  Feststellungen zu entnehmen:  "Tz. 1: Einkünfte aus Nichtselbstständiger Arbeit   In Anlehnung an die ergangenen Bescheide nach der Entscheidung des unabhängigen  Finanzsenates (GZ.RV/1590-W/06, RV/1879-W/06, RV/1949-W/06) vom 16.4.2007 und des  Erkenntnisses des VwGH (Zl.2007/13/0054-7) vom 29.9.2010 beim Ehegatten (=Arbeitgeber)  **Viola Bahlow**, werden die Zahlungen an die Ehegattin den Einkünften aus nichtselbstständiger  Arbeit zugeordnet.

- missed: `Viola Bahlow` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)

IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter **Mag.a  Patricia Kathan**-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

- missed: `Mag.a  Patricia Kathan` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_11`)

In der Folge führte Sohn aus:  „Ich habe meinen Betrieb im Jahr 2011 von meinem Vater **Quentin Schwartkopp**  übernommen.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_72`)

Dazu wurde in der Berufungsschrift ua. ausgeführt, dass das Fahrzeug der  Berufungswerberin/nunmehr Beschwerdeführerin (Bf) **Siegfried Basyurt**  nur dann gelegentlich im  Inland zur Verwendung zur Verfügung gestanden habe, wenn sich der Ehegatte (als  Leasingnehmer des Pkw) in Österreich aufgehalten habe.

- missed: `Siegfried Basyurt` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Peter Bilger** in der Beschwerdesache  Kira Mathies, Gülke 91, 9560 Regin, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. April 2019 betreffend Aufhebung des  Einkommensteuerbescheides 2015 vom 17.1.2019 gemäß § 299 BAO und Einkommensteuer   2015 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Aufhebung des Einkommensteuerbescheides  2015 vom 17.1.2019 wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Peter Bilger` (person)
- predicted in sentence: `Kira Mathies`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_133`)

Nach den Ausführungen der steuerlichen Vertretung sei am ersten Lichtbild (20210406- 11342.jpg) das Zimmer des Bf. und am zweiten (20210406_113825.jpg) dass für Gäste der  Familie reservierte Gästezimmer dargestellt. Ganz offensichtlich wurde somit dem Bf. – wie  vom Gericht vermutet – das von der Zeugin **N.N.** beschriebene „Blumenzimmer“ zur Nutzung  zugewiesen.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald über die  Beschwerde der **Uwe Rossberg**, Stadels 61, 8990 Reith, Österreich, vom 1. Februar 2024, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, als Abgabenstrafbehörde vom 24. Jänner  2024, GZ. MA67/GZ/2023, betreffend eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt  Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Uwe Rossberg` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, die **DDr. Jens Oberquelle** (im Folgenden: Bf) ist ein  Telekommunikationsunternehmen aus dem Drittland.

- missed: `DDr. Jens Oberquelle` (person)
- predicted in sentence: `Dr. Jens Oberquelle`

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_11`)

II. der Verband **Engelbert Schefe**  wurde schuldig erkannt, für durch einen Entscheidungsträger im  Sinne des § 2 Abs. 1 Verbandsverantwortlichkeitsgesetz (VbVG) iVm § 28a FinStrG zu Gunsten  des Verbandes und unter Verletzung den Verband treffender Verpflichtungen begangen  Finanzvergehen verantwortlich zu sein (I.).

- missed: `Engelbert Schefe` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Armin Treichl** in der Beschwerdesache  OSR KommR Susette Stenczel, Amtweg 83, 9542 Tobitsch, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glückspiel vom 25. September 2019  betreffend Gebühr Steuernummer 61-194/1325  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Armin Treichl` (person)
- predicted in sentence: ``

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_254`)

Da sich das Sozialministeriumservice sehr wohl aus einer eigenen Sachverständigenliste von zur  Berufsausübung berechtigter Ärzte zwecks Erstattung der Bescheinigungen gem. § 8 Abs. 6  FLAG bedienen kann, die nicht in der Liste der allgemein beeideten und gerichtlich  zertifizierten Sachverständigen eingetragen sind (siehe wiederum BFG 15.12.2017,  RV/7102062/2017), kommt dem diesbezüglichen Beschwerdeeinwand ebenso keine  Berechtigung zu.  Insgesamt besteht daher für das BFG keine Veranlassung, die fachliche Qualifikation der  begutachtenden Ärztin **Amanda Zacharek** in Zweifel zu ziehen.

- missed: `Amanda Zacharek` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139407.1`) (sent_id: `deanon_BFG_20260814_TEST/139407.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Christian Seywald** in der  Beschwerdesache Silvius Christidou, Landlerweg 2, 7202 Lichtenwörth, Österreich, betreffend   Beschwerde (ursprünglich Berufung) vom 29. Mai 2012 gegen den  Einkommensteuerbescheid 2009 des Finanzamtes Wien 3/11 Schwechat Gerasdorf vom  25. Mai 2012 zu St.Nr. alteStNr,   am 14. November 2012 beim Finanzamt eingelangter Vorlageantrag gegen die Beru- fungsvorentscheidungen des Finanzamtes Wien 3/11 Schwechat Gerasdorf vom  4. Oktober 2012 zu Steuernummer alteStNr hinsichtlich Einkommensteuer 2009, 2010  und 2011,   Vorlage der Beschwerde gegen den Einkommensteuerbescheid 2009 durch das  Finanzamt Österreich an das Bundesfinanzgericht (BFG) am 25. Oktober 2022,   Vorlagebericht des Finanzamtes Österreich vom 25. Oktober 2022 zu nunmehriger  Steuernummer 15-665/6861  hinsichtlich der eingebrachten Beschwerde (damals:  Berufung) vom 29. Mai 2012 gegen den Einkommensteuerbescheid 2009 vom 25. Mai  2012 sowie hinsichtlich nicht eingebrachter Beschwerden vom 29. Mai 2012 gegen die  Einkommensteuerbescheide 2010 und 2011 vom 25. Mai 2012,  beschlossen:  Der am 14. November 2012 beim Finanzamt eingelangte Vorlageantrag gegen die  Beschwerdevorentscheidungen vom 4. Oktober 2012 hinsichtlich Einkommensteuer 2009,  2010 und 2011 wird gemäß § 260 Abs. 1 lit. b in Verbindung mit § 264 Abs. 4 lit. e und § 264  Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

- missed: `Mag. Christian Seywald` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache **Hademar Haßelbach, BSc**,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hademar Haßelbach, BSc` (person)
- predicted in sentence: `Hon.-Prof. Wilfried Brokof`, `Hademar Haßelbach`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)

Das Anbringen, welches Herr **Bodewein** per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

- missed: `Bodewein` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/146305.1`) (sent_id: `deanon_BFG_20260814_TEST/146305.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Türkyilmaz  über den Antrag der Revisionswerberin  Esmeralda Pfanne, Steinplattenweg 5, 8091 Pöllau, Österreich  vertreten durch Rechtsanwalt Mag. Dr. Helmut Blum und  Rechtsanwältin **Mag.a Andrea Blum**, Mozartstraße 11/6, 4020 Linz, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 21. März 2024, GZ. RV/7102000/2023, betreffend Abweisung  eines Nachsichtsansuchens erhobenen a.o. Revision vom 16. November 2024 aufschiebende  Wirkung zuzuerkennen, den Beschluss gefasst:  Der Antrag wird gemäß § 30 Abs. 2 Verwaltungsgerichtshofgesetz, VwGG, abgewiesen.

- missed: `Mag.a Andrea Blum` (person)
- predicted in sentence: `Dr. Helmut Blum`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_11`)

Da der Einspruch nicht von dem Beschuldigten (M), sondern von Pjotr Niessl  erhoben wurde,  ersuchte die Magistratsabteilung 67 **Pjotr Niessl**  mit Schreiben vom 16. Oktober 2024 (aufgrund  einer unwirksamen Zustellung neuerlich zugestellt am: 29. Jänner 2025) um Vorlage einer  Vertretungsvollmacht binnen zwei Wochen nach Zustellung des Mängelbehebungsauftrages.

- missed: `Pjotr Niessl` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_110`)

Zu den Eingangsrechnungen der Fa. X. d.o.o an das Einzelunternehmen **N.N.** in den Jahren 2012 und 2013 und Vorhalt Zeugenaussage B. A. vom 4.9.2018, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa.  X. d.o.o erbracht worden seien, führte der Beschuldigte aus, Herr A. habe eigenständig eine Firma in Slowenien gegründet und sei mit dieser Firma zu ihm gekommen und habe um Aufträge ersucht.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  **Mag. Sonja Stradner** sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Sonja Stradner` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Ing. Wolfgang  Weichselbraun`, `Kira Lentze`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/146305.1`) (sent_id: `deanon_BFG_20260814_TEST/146305.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter **Mag. Zlatan Türkyilmaz**  über den Antrag der Revisionswerberin  Esmeralda Pfanne, Steinplattenweg 5, 8091 Pöllau, Österreich  vertreten durch Rechtsanwalt Mag. Dr. Helmut Blum und  Rechtsanwältin Mag.a Andrea Blum, Mozartstraße 11/6, 4020 Linz, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 21. März 2024, GZ. RV/7102000/2023, betreffend Abweisung  eines Nachsichtsansuchens erhobenen a.o. Revision vom 16. November 2024 aufschiebende  Wirkung zuzuerkennen, den Beschluss gefasst:  Der Antrag wird gemäß § 30 Abs. 2 Verwaltungsgerichtshofgesetz, VwGG, abgewiesen.

- missed: `Mag. Zlatan Türkyilmaz` (person)
- predicted in sentence: `Dr. Helmut Blum`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `PhD Mag`, `Dr. Thomas Keppert`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)

Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die **Engelbert Schefe**, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

- missed: `Engelbert Schefe` (person)
- predicted in sentence: `Dieter Avemaria`

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache **DDr.in Magdalena Holtzbecher, Bakk. rer. nat.**,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

- missed: `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.` (person)
- predicted in sentence: `Hon.-Prof. Engelbert Voglsang`, `Dr.in Magdalena Holtzbecher, Bakk. `

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Ronald Kulenkampf**  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Ronald Kulenkampf` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_124`)

Die anamnestischen Angaben bestätigen eine nur leicht verzögerte motorische Entwicklung in  den ersten 2 Lebensjahren, **M.** sei früh und schnell gekrabbelt, habe mit 20 Monaten die ersten  freien Schritte gemacht und sei mit 23Mo längere Strecken frei gegangen.

- missed: `M.` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_7`)

Beschwerde vom 10. Juni 2021  Die Bf. brachte in ihrer Beschwerde vor, dass sie bis dato auf ihr Konto **Adelheid Lokaizyk**  in Österreich  keine Familienbeihilfe ausbezahlt bekommen habe.

- missed: `Adelheid Lokaizyk` (person)
- predicted in sentence: `Die Bf`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch **Mag. Paulus Maria Christoph Papst**,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

- missed: `Mag. Paulus Maria Christoph Papst` (person)
- predicted in sentence: `Hon.-Prof.in Jacqueline Traxl`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/137175.1`) (sent_id: `deanon_BFG_20260814_TEST/137175.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache **Ashley Wanagat**, Dörfles 5, 9182 Greuth, Österreich, vertreten durch LBG Niederösterreich  Steuerberatung GmbH, Schloßparkgasse 6, 3950 Gmünd, betreffend Beschwerde vom  14. Februar 2020 gegen den Bescheid des Finanzamtes Österreich vom 21. Jänner 2020  betreffend Einkommensteuer 2017 Steuernummer 33-883/1280  den Beschluss:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als  zurückgenommen.

- missed: `Ashley Wanagat` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Manuela Fischer** in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

- missed: `Mag. Manuela Fischer` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. **Ing.Ing. Bertram Hennlein** ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: `Ing. Bertram Hennlein`

</details>

---

