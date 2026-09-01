# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-29T10:12:49.121566

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-29_v4/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2494 |
| Validation documents | 624 |
| Test documents | 786 |
| Train sentences | 4394 |
| Validation sentences | 1166 |
| Test sentences | 92563 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
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
| Accuracy (exact match) | 98.8% |
| True Positives | 1002 |
| False Positives | 810 |
| False Negatives | 895 |
| Total Gold Entities | 1897 |
| Micro Precision | 55.3% |
| Micro Recall | 52.8% |
| Micro F1 | 54.0% |
| Macro F1 | 54.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `names_after_ddr` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `names_after_complaint_context` | 33.7% | 90.1% | 20.7% | 436 | 393 | 43 |
| `names_after_herr_frau` | 16.6% | 53.3% | 9.9% | 351 | 187 | 164 |
| `names_with_academic_titles` | 28.7% | 41.5% | 22.0% | 1006 | 417 | 589 |
| `names_after_omedr` | 0.3% | 27.3% | 0.2% | 11 | 3 | 8 |
| `names_after_fa_context` | 0.1% | 14.3% | 0.1% | 7 | 1 | 6 |
| `names_after_sachbearbeiter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `names_after_ddr` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `69ce2189`  
**Description:**
Captures names following 'DDr.' (double doctor), ensuring the full title is captured if needed.

**Content:**
```
DDr\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 394 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/145374.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145374.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen DDr. Irvin Bukovsky, Warth 138, 9342 Pisweg, Österreich, wegen der Verwaltungsübertretung  nach § 2 in Verbindung mit § 4 Abs. 2 Wiener Parkometergesetz 2006, Landesgesetzblatt für  Wien Nr. 9/2006 in der Fassung Landesgesetzblatt für Wien Nr. 71/2018, über die Beschwerde  der Beschuldigten vom 11. Juni 2024 gegen das Straferkenntnis des Magistrates der Stadt Wien  vom 10. Mai 2024, GZ. MA67/GZ/2024, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `DDr. Irvin Bukovsky` | `DDr. Irvin Bukovsky` |

**Missed by this rule (FN):**

- `Warth 138, 9342 Pisweg, Österreich` (address)

</details>

---

## `names_after_complaint_context` 🏆

**F1:** 0.337 | **Precision:** 0.901 | **Recall:** 0.207  

**Format:** `regex`  
**Rule ID:** `6d692b1e`  
**Description:**
Captures names immediately following 'in der Beschwerdesache' or 'in der Revisionssache', including optional academic/professional suffixes like Bakk. art., Bakk. techn., LLM.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Revisionssache|in\s+der\s+Verwaltungsstrafsache|in\s+der\s+Finanzstrafsache|in\s+der\s+Rechtssache)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+\s*(?:LLM|Bakk\.\s+r\.\s+nat|Bakk\.\s+techn|BEd|Mag\.|Dr\.|Hon\.-Prof\.(?:in)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|OMedR|Techn R|Ing\.|Bakk\.\s+art\.|Bakk\.\s+phil\.|Bakk\.\s+iur\.|BSc|MA|MSc|PhD|DDr\.|DDr\.in|ÖkR|KommR|KzlR|RgR|OStR|StR)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.901 | 0.207 | 0.337 | 436 | 393 | 43 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 393 | 43 | 1495 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Zeno Matyssek` | `Zeno Matyssek` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Florenzia Claußing` | `Florenzia Claußing` |

**Missed by this rule (FN):**

- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich` (address)
- `10-95-558/8694` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wendy Scherl` | `Wendy Scherl` |

**Missed by this rule (FN):**

- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `53-864/4798` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Klarissa Kümml` | `Klarissa Kümml` |

**Missed by this rule (FN):**

- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Anita Stindt, Bachreuth 49, 5143 Haselpfaffing, Österreich, über die Beschwerde vom 10. Juni 2016 gegen den Bescheid des FA vom 3. Juni 2016  betreffend Einkommensteuer 2014 Steuernummer 26-508/6641  zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Anita Stindt` | `Anita Stindt` |

**Missed by this rule (FN):**

- `Bachreuth 49, 5143 Haselpfaffing, Österreich` (address)
- `26-508/6641` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128929.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Erich Nolde  in der Beschwerdesache Urs Locke,  Jägersberg 20, 3654 Pölla, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Urs Locke` | `Urs Locke` |

**Missed by this rule (FN):**

- `Dr. Erich Nolde` (person)
- `Jägersberg 20, 3654 Pölla, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Nadja Rossetto` | `Nadja Rossetto` |

**Missed by this rule (FN):**

- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `85-716/2059` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Bartholomäus Beier  in der Beschwerdesache Daisy Strakbein,  Gottestaler Straße 27, 8693 Dürrenthal, Österreich, betreffend Beschwerde vom 20. Februar 2018 gegen die Bescheide  des  Finanzamtes Gmunden Vöcklabruck vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 den Beschluss:  I. Die angefochtenen Bescheide vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 und die Beschwerdevorentscheidungen vom 28. März 2018  werden gemäß § 278 Abs 1 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Daisy Strakbein` | `Daisy Strakbein` |

**Missed by this rule (FN):**

- `Priv.-Doz. Bartholomäus Beier` (person)
- `Gottestaler Straße 27, 8693 Dürrenthal, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Rainer Leutheußer` | `Rainer Leutheußer` |

**Missed by this rule (FN):**

- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Cornelia Pranckaitis, Petersbergweg 142, 4212 Steigersdorf, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

| Predicted | Gold |
|---|---|
| `Cornelia Pranckaitis` | `Cornelia Pranckaitis` |

**Missed by this rule (FN):**

- `Petersbergweg 142, 4212 Steigersdorf, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximilian Joobs` | `Maximilian Joobs` |

**Missed by this rule (FN):**

- `Forsthausweg 11, 3580 Poigen, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Oleg Kreissl` | `Oleg Kreissl` |

**Missed by this rule (FN):**

- `Schoaderstraße 2, 3441 Freundorf, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129205.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Wilhelm Stoecker,  Zellenbach 18, 4061 Pasching, Österreich, über die Beschwerde vom 10. April 2019 gegen den Bescheid über den Antrag  vom 06.03.2019 auf Mehrkindzuschlag für 2019 aufgrund der Verhältnisse des Jahres 2018  des  Finanzamtes vom 1. April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wilhelm Stoecker` | `Wilhelm Stoecker` |

**Missed by this rule (FN):**

- `Zellenbach 18, 4061 Pasching, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Miroslav Treischl` | `Miroslav Treischl` |

**Missed by this rule (FN):**

- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Wolf Sackner, Altweitra 15, 6091 Götzens, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  34-684/1904  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wolf Sackner` | `Wolf Sackner` |

**Missed by this rule (FN):**

- `Altweitra 15, 6091 Götzens, Österreich` (address)
- `34-684/1904` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129533.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Ludwig Thorbeck, Am Kaibrunnen 29, 9620 Guggenberg, Österreich, vertreten durch Stb, über die Beschwerde vom 21.12.2012 gegen den Bescheid des  Finanzamtes A vom 13.11.2012, betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ludwig Thorbeck` | `Ludwig Thorbeck` |

**Missed by this rule (FN):**

- `Am Kaibrunnen 29, 9620 Guggenberg, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vivian Malek` | `Vivian Malek` |

**Missed by this rule (FN):**

- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Kreul` | `Thomas Kreul` |

**Missed by this rule (FN):**

- `Preberstraße 4, 3911 Dietharts, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jennifer Rösl` | `Jennifer Rösl` |

**Missed by this rule (FN):**

- `Priv.-Doz. Eckard Sellnow` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129696.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Detlev Hafranke, Bichlmayrstraße 9 59, 9231 Kerschdorf, Österreich, über die Beschwerde vom 2. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 7. August 2019 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe für das Kind x im Zeitraum vom 01.07.2014 bis zum 30.09.2016 Recht erkannt:   Der Beschwerde wird gemäß § 279 teilweise BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Detlev Hafranke` | `Detlev Hafranke` |

**Missed by this rule (FN):**

- `Bichlmayrstraße 9 59, 9231 Kerschdorf, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Rosalia Armbrost, Toulagasse 20, 8693 Mürzsteg, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 86-795/2631  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Rosalia Armbrost` | `Rosalia Armbrost` |

**Missed by this rule (FN):**

- `Toulagasse 20, 8693 Mürzsteg, Österreich` (address)
- `86-795/2631` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129950.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129950.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dora Hohbohm, Adresse1,  Ungarn, über die Beschwerde vom 26. März 2019 gegen den Bescheid des Finanzamtes A vom  27. Februar 2019, Steuernummer 27-454/3088, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dora Hohbohm` | `Dora Hohbohm` |

**Missed by this rule (FN):**

- `27-454/3088` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Felizitas Philippov` | `Felizitas Philippov` |

**Missed by this rule (FN):**

- `Hauser 155, 9422 Aich, Österreich` (address)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130064.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Johann Fuetterer, Hungerbichlweg 19, 5112 Schmieden, Österreich, vertreten durch Joachim Herbert Aigner, Gewerbepark 1, 4920 Schildorn, über die  Beschwerde vom 23. Februar 2018 gegen den Haftungsbescheid des Finanzamtes Braunau Ried  Schärding vom 24. Jänner 2018, Steuernummer StNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben, der Haftungsbetrag von  4.588,35 € um 2.258,02 € auf den Betrag von 2.330,33 € eingeschränkt und wie folgt  aufgeschlüsselt:   Abgabenart Zeitraum Fälligkeit Betrag in Euro  Umsatzsteuer 03/2016 17.05.2016 16,87  Dienstgeberbeitrag 05/2016 15.06.2016 60,50  Zuschlag zum DB 05/2016 15.06.2016 4,48  Lohnsteuer 05/2016 15.06.2016 25,86  Umsatzsteuer 04/2016 15.06.2016 48,32  Dienstgeberbeitrag 06/2016 15.07.2016 66,69  Zuschlag zum DB 06/2016 15.07.2016 5,34  Lohnsteuer 06/2016 15.07.2016 25,86  Umsatzsteuer 05/2016 15.07.2016 71,65  Säumniszuschlag 1 2016 18.07.2016 24,75  Dienstgeberbeitrag 07/2016 16.08.2016 85,30  Zuschlag zum DB 07/2016 16.08.2016 6,82  1 von 15 Seite 2 von 15

| Predicted | Gold |
|---|---|
| `Johann Fuetterer` | `Johann Fuetterer` |

**Missed by this rule (FN):**

- `Hungerbichlweg 19, 5112 Schmieden, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gerald Hellbing` | `Gerald Hellbing` |

**Missed by this rule (FN):**

- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Maximiliane Aue, Sternenplatz 39, 4082 Aschach an der Donau, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Maximiliane Aue` | `Maximiliane Aue` |

**Missed by this rule (FN):**

- `Sternenplatz 39, 4082 Aschach an der Donau, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130424.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Bernhard Schmittchen, Platz der Versöhnung 2, 5205 Schleedorf, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernhard Schmittchen` | `Bernhard Schmittchen` |

**Missed by this rule (FN):**

- `Platz der Versöhnung 2, 5205 Schleedorf, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Igor Strunz` | `Igor Strunz` |

**Missed by this rule (FN):**

- `Dr. Björn Hüpscher` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130450.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130450.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Cathleen Bürckmayer, Gindsweg 6, 9431 St. Stefan, Österreich,  über die Beschwerde vom 20. April 2018 gegen die Bescheide des Finanzamtes Klagenfurt, zu  Steuernummer 88-868/8570, vom 23. März 2018, mittels welchen der Antrag auf  Aufhebung der Einkommensteuerbescheide für 2015 und 2016 gemäß § 299 BAO abgewiesen  wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cathleen Bürckmayer` | `Cathleen Bürckmayer` |

**Missed by this rule (FN):**

- `Gindsweg 6, 9431 St. Stefan, Österreich` (address)
- `88-868/8570` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Farina Nardello, Raning 1A, 4060 Leonding, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Farina Nardello` | `Farina Nardello` |

**Missed by this rule (FN):**

- `Raning 1A, 4060 Leonding, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterH.P in der Beschwerdesache Emilia Bollfrass, SDL Am Steinsee 6a, 4951 Imolkam, Österreich, über die Beschwerde vom 23. Juni 2014 gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 12. Juni 2014 betreffend Gebühren 2014,  Steuernummer 56-677/1995, Erfassungsnummer numero098, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emilia Bollfrass` | `Emilia Bollfrass` |

**Missed by this rule (FN):**

- `SDL Am Steinsee 6a, 4951 Imolkam, Österreich` (address)
- `56-677/1995` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Vincent Allert, Marktlände 20, 5121 Ostermiething, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vincent Allert` | `Vincent Allert` |

**Missed by this rule (FN):**

- `Marktlände 20, 5121 Ostermiething, Österreich` (address)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130694.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Alan Kockhans  in der Beschwerdesache Geraldine Melwer,  Geißtobel 17, 9585 Fürnitz, Österreich, Ungarn, über die Beschwerde vom 6. Oktober 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 14. September 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Geraldine Melwer` | `Geraldine Melwer` |

**Missed by this rule (FN):**

- `Priv.-Doz. Alan Kockhans` (person)
- `Geißtobel 17, 9585 Fürnitz, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexander Powell` | `Alexander Powell` |

**Missed by this rule (FN):**

- `Priv.-Doz. Lubomir Gruebert` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Klarissa Aßmus` | `Klarissa Aßmus` |

**Missed by this rule (FN):**

- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich` (address)
- `52-573/0809` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ronald Töws` | `Ronald Töws` |

**Missed by this rule (FN):**

- `Schießstatt 9, 5124 Weyer, Österreich` (address)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Sochurek` | `Gudrun Sochurek` |

**Missed by this rule (FN):**

- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130901.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130901.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Maximiliane Weimer, Kreuzergegend-West 16, 4926 Pilgersham, Österreich, über die Beschwerde vom 21. September 2018 gegen den Bescheid des Finanzamtes A  vom 04. September 2018 betreffend den Antrag auf Wiederaufnahme des mit  Einkommensteuerbescheid 2015 vom 02. Dezember 2016 abgeschlossenen Verfahrens,  Steuernummer 47-793/9886, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Weimer` | `Maximiliane Weimer` |

**Missed by this rule (FN):**

- `Kreuzergegend-West 16, 4926 Pilgersham, Österreich` (address)
- `47-793/9886` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130985.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in James Haemel  in der Beschwerdesache Marianne Rohweder,  Schlägl 1, 8092 Mettersdorf am Saßbach, Österreich, über die Beschwerde vom 30. Dezember 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 2. Dezember 2019 betreffend  Gebühren 2019 Steuernummer 81-888/5729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marianne Rohweder` | `Marianne Rohweder` |

**Missed by this rule (FN):**

- `Hon.-Prof.in James Haemel` (person)
- `Schlägl 1, 8092 Mettersdorf am Saßbach, Österreich` (address)
- `81-888/5729` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/131064.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Harald Demers, Empergergasse 96, 4072 Großhart, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 98-121/1048  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Harald Demers` | `Harald Demers` |

**Missed by this rule (FN):**

- `Empergergasse 96, 4072 Großhart, Österreich` (address)
- `98-121/1048` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerie Süssmeier` | `Valerie Süssmeier` |

**Missed by this rule (FN):**

- `Ögglweg 86, 8623 Tutschach, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Samantha Waitschull  in der Beschwerdesache Ramona Keklik,  Gafadura 6, 9620 Kraß, Österreich, vertreten durch PKF CENTURION Wirtschaftsprüfungs- gesellschaft mbH,  Hegelgasse 8, 1010 Wien, über die Beschwerden gegen die Bescheide des Zollamtes Eisenstadt  Flughafen Wien   1) vom 7. Februar 2018, Zl: a, betreffend Festsetzung der Mineralölsteuer für Jänner 2010 mit €  195.809,84 und Festsetzung des Säumniszuschlages mit € 3.916,20;

| Predicted | Gold |
|---|---|
| `Ramona Keklik` | `Ramona Keklik` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Samantha Waitschull` (person)
- `Gafadura 6, 9620 Kraß, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ursula Raubart, Tschupbach 5c, 4144 Karlsbach, Österreich, vertreten durch Rachel Woiczyk, Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 86-917/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Raubart` | `Ursula Raubart` |

**Missed by this rule (FN):**

- `Tschupbach 5c, 4144 Karlsbach, Österreich` (address)
- `Rachel Woiczyk` (person)
- `Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich` (address)
- `86-917/1669` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

| Predicted | Gold |
|---|---|
| `Samuel Herpel` | `Samuel Herpel` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Annemarie Wittjen` (person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich` (address)
- `39-702/2118` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tiffany Kleiß` | `Tiffany Kleiß` |

**Missed by this rule (FN):**

- `Endergasse 74, 5411 Vorderwiestal, Österreich` (address)
- `79-412/0834` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kirsten Constantinescu` | `Kirsten Constantinescu` |

**Missed by this rule (FN):**

- `Mag.a Delia Wilmerdinger` (person)
- `Höhenwald 50, 4822 Primesberg, Österreich` (address)
- `41-83-382/2498` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

| Predicted | Gold |
|---|---|
| `Wendy Schärff` | `Wendy Schärff` |

**Missed by this rule (FN):**

- `Krainberg 12, 4633 Weilbach, Österreich` (address)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131451.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Margarete Ullbricht  in der Beschwerdesache Chen Egeli,  Rudolf-Henke-Straße 162, 4152 Leiten, Österreich, vertreten durch die Erwachsenenvertreterin RA, gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 23. Juli 2018, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016 und Anspruchszinsen 2015, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Chen Egeli` | `Chen Egeli` |

**Missed by this rule (FN):**

- `Dr.in Margarete Ullbricht` (person)
- `Rudolf-Henke-Straße 162, 4152 Leiten, Österreich` (address)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Selma Papenmeyer, Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

| Predicted | Gold |
|---|---|
| `Selma Papenmeyer` | `Selma Papenmeyer` |

**Missed by this rule (FN):**

- `Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131522.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Priv.-Doz.in Sara Lahnstein  in der Beschwerdesache  Siegmund Orgel, Weistracher Straße 23, 3661 Artstetten, Österreich, über die Beschwerde vom 25. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 08. Mai 2020 betreffend Einkommensteuer 2019,  Steuernummer 48-626/5826, zu Recht erkannt:  I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Siegmund Orgel` | `Siegmund Orgel` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Sara Lahnstein` (person)
- `Weistracher Straße 23, 3661 Artstetten, Österreich` (address)
- `48-626/5826` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131524.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131524.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterC in der Beschwerdesache Gabriele Tsakiroudis, Aroniaweg 24n, 2185 Rannersdorf an der Zaya, Österreich, über die Beschwerde vom 17. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 19. Dezember 2019 betreffend Rückforderung  Differenzzahlung/Familienbeihilfe und Kindergeld Juli bis Dezember 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gabriele Tsakiroudis` | `Gabriele Tsakiroudis` |

**Missed by this rule (FN):**

- `Aroniaweg 24n, 2185 Rannersdorf an der Zaya, Österreich` (address)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131561.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Heinrich Möbs, Furnierweg 837, 8481 Siebing, Österreich, über die Beschwerden vom 2. November 2015 und vom 10. Februar 2016 gegen die  Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 15. Oktober 2015 und vom  26.1.2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 und 2014,  Steuernummer 53-492/1507, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinrich Möbs` | `Heinrich Möbs` |

**Missed by this rule (FN):**

- `Furnierweg 837, 8481 Siebing, Österreich` (address)
- `53-492/1507` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131573.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131573.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Svenja Daenhardt, Oberer Weglänger 195, 5124 Witzling, Österreich, über die Beschwerde vom 21. April 2016 gegen  den Bescheid des Finanzamtes Österreich vom 21. März 2016 betreffend Rückforderung von  Kinderabsetzbetrag und Ausgleichszahlung gem. VO (EG) 883/2004 (Familienbeihilfe) für  den  Zeitraum Juni 2014 bis August 2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Svenja Daenhardt` | `Svenja Daenhardt` |

**Missed by this rule (FN):**

- `Oberer Weglänger 195, 5124 Witzling, Österreich` (address)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131626.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Theresa Meisters, Kiurinagasse 699, 4710 Aigen, Österreich, über die Beschwerde vom 28. Juli 2014 gegen den Bescheid des Finanzamtes Lilienfeld  St. Pölten vom 1. Juli 2014 betreffend Einkommensteuer 2012, Steuernummer  48-801/2010, zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Theresa Meisters` | `Theresa Meisters` |

**Missed by this rule (FN):**

- `Kiurinagasse 699, 4710 Aigen, Österreich` (address)
- `48-801/2010` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Thobias Dommert, Hainfelder Straße 56, 4846 Gewerbepark West, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 66-847/2354, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Thobias Dommert` | `Thobias Dommert` |

**Missed by this rule (FN):**

- `Hainfelder Straße 56, 4846 Gewerbepark West, Österreich` (address)
- `66-847/2354` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Moses Hallbauer, Glanstraße 125, 8271 Großhart, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 1. Februar 2017 gegen den Bescheid  des Finanzamtes Gänserndorf Mistelbach vom 12. Jänner 2017 betreffend Einkommensteuer  2015, Steuernummer 73-564/0656, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Moses Hallbauer` | `Moses Hallbauer` |

**Missed by this rule (FN):**

- `Glanstraße 125, 8271 Großhart, Österreich` (address)
- `73-564/0656` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131716.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131716.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Kordula Zacke, Bärleiten 15, 7562 Zahling, Österreich, über die Beschwerde vom 30. Juni 2020 gegen die Bescheide des Finanzamtes Bruck  Eisenstadt Oberwart vom 27. Mai 2020 betreffend Abweisung eines Antrages auf  Wideraufnahme des Verfahrens hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung)  2015, 2016 und 2017 Steuernummer 02-996/1524  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kordula Zacke` | `Kordula Zacke` |

**Missed by this rule (FN):**

- `Bärleiten 15, 7562 Zahling, Österreich` (address)
- `02-996/1524` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131742.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131742.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Priv.-Doz.in Ada Langejürgen  in der Beschwerdesache Cathleen Dickhof, Scheibladegg 14, 8113 Sankt Bartholomä, Österreich  vertreten durch Edith Schicketanz, über die Beschwerde vom 4. Juni 2018 gegen den  Bescheid des Finanzamt Grieskirchen Wels  vom 26. März 2018 betreffend Einkommensteuer 2016, Steuernummer  10-269/3655, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cathleen Dickhof` | `Cathleen Dickhof` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Ada Langejürgen` (person)
- `Scheibladegg 14, 8113 Sankt Bartholomä, Österreich` (address)
- `Edith Schicketanz` (person)
- `Finanzamt Grieskirchen Wels` (organisation)
- `10-269/3655` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131760.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131760.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Tosca Nassery  in der Beschwerdesache Elina Mlinarik,  P. Silberbauer-Straße 3, 9572 Brunn, Österreich, über die Beschwerde vom 10. April 2020 gegen den Bescheid des Finanzamtes  Österreich vom 6. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 47-073/4546  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Elina Mlinarik` | `Elina Mlinarik` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Dr.in Tosca Nassery` (person)
- `P. Silberbauer-Straße 3, 9572 Brunn, Österreich` (address)
- `47-073/4546` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ralph Staibler, Pregerstraße 17, 4242 Kirchberg, Österreich, über die Beschwerde vom 15. Juni 2019 gegen den Bescheid des Finanzamtes  Österreich, vormals des Finanzamtes Salzburg-Land vom 16. Mai 2019 betreffend die  Wiederaufnahme des Verfahren gemäß § 303 Abs.1 BAO zur Einkommensteuer 2013 sowie die  Bescheide vom 17. Mai 2019 betreffend die Wiederaufnahme der Verfahren gemäß § 303  Abs.1 BAO zur Einkommensteuer 2014 und 2015 zu Steuernummer 92-314/9447  zu Recht  erkannt:   1.

| Predicted | Gold |
|---|---|
| `Ralph Staibler` | `Ralph Staibler` |

**Missed by this rule (FN):**

- `Pregerstraße 17, 4242 Kirchberg, Österreich` (address)
- `92-314/9447` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131803.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131803.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Janet Bendert  in der Beschwerdesache Jason Reifferscheid,  Hintere Feldgasse 15M, 4642 Rappersdorf, Österreich, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 5. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer *** zu Recht erkannt:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jason Reifferscheid` | `Jason Reifferscheid` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Janet Bendert` (person)
- `Hintere Feldgasse 15M, 4642 Rappersdorf, Österreich` (address)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Adrian Hofschmidt, Dechantsbühel 10, 9911 Bannberg, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Adrian Hofschmidt` | `Adrian Hofschmidt` |

**Missed by this rule (FN):**

- `Dechantsbühel 10, 9911 Bannberg, Österreich` (address)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thomas Drieschner  in der Beschwerdesache Gebhard Determann,  Mooseggweg 49, 9624 Fritzendorf, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Gebhard Determann` | `Gebhard Determann` |

**Missed by this rule (FN):**

- `Univ.-Prof. Thomas Drieschner` (person)
- `Mooseggweg 49, 9624 Fritzendorf, Österreich` (address)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/131877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131877.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Amy Jonusas, Zieritzgasse 3I, 4963 Hart, Österreich, über die Beschwerde vom 21. Februar 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 29. Jänner 2019 betreffend Einkommensteuer 2017  Steuernummer 04-850/4573  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Amy Jonusas` | `Amy Jonusas` |

**Missed by this rule (FN):**

- `Zieritzgasse 3I, 4963 Hart, Österreich` (address)
- `04-850/4573` (tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/131899.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131899.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sabrina Hary  in der Beschwerdesache Vitus Haselbauer,  Karwendelhaus 12, 8054 Graz, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Land vom 30. April 2020,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vitus Haselbauer` | `Vitus Haselbauer` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Sabrina Hary` (person)
- `Karwendelhaus 12, 8054 Graz, Österreich` (address)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132000.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Gerda Schalch  in der Beschwerdesache Iris Greppmeier,  Vorderholz 1, 9345 Reinsberg, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und Jugendhilfe,  Karl-Borromäus-Platz 3, 1030 Wien, über die Beschwerde vom 14. August 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 (nunmehr Finanzamtes Österreich ) vom 30. Juli  2020 betreffend Abweisung des Antrages auf Familienbeihilfe für 01/2016 bis 06/2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Iris Greppmeier` | `Iris Greppmeier` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Mag.a Gerda Schalch` (person)
- `Vorderholz 1, 9345 Reinsberg, Österreich` (address)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132063.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132063.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Mannweiller  in der Beschwerdesache Edgar Schoenmeyer,  Prof. Erni Mangold Weg 3, 4715 Hofmaning, Österreich, über die Säumnisbeschwerden vom 29. Jänner 2021, eingebracht am 8.  Februar 2021, wegen behaupteter Verletzung der Entscheidungspflicht des FA Salzburg-Stadt  betreffend   1. Antrag an das FA Salzburg-Stadt  vom 26.05.2020 auf Wiederaufnahme des mit  Einstellungsbeschluss des BFG vom 16.04.2020 abgeschlossenen Abgabenverfahrens  2. Antrag an das FA Salzburg-Stadt  vom 02.06.2020 auf Aufhebung des Einstellungsbeschlusses  des BFG vom 16.04.2020 nach § 299 BAO   beschlossen:  Die Säumnisbeschwerden werden gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Edgar Schoenmeyer` | `Edgar Schoenmeyer` |

**Missed by this rule (FN):**

- `Dr.in Estelle Mannweiller` (person)
- `Prof. Erni Mangold Weg 3, 4715 Hofmaning, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `FA Salzburg-Stadt` (organisation)
- `FA Salzburg-Stadt` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Natalie Emmerling` | `Natalie Emmerling` |

**Missed by this rule (FN):**

- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich` (address)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132244.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132244.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Floriane Thürwächter, Sägewerksweg 18, 6822 Schnifnerberg, Österreich, über die Beschwerde vom 6. Mai 2015 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 12. Februar 2016 betreffend Umsatzsteuer 2014 Steuernummer zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Floriane Thürwächter` | `Floriane Thürwächter` |

**Missed by this rule (FN):**

- `Sägewerksweg 18, 6822 Schnifnerberg, Österreich` (address)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132303.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132303.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jana Sülzenbrück  in der Beschwerdesache Edmund Isekait,  Reither Gasse 7, 4842 Heinrichsberg, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 07. April 2020,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Edmund Isekait` | `Edmund Isekait` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Jana Sülzenbrück` (person)
- `Reither Gasse 7, 4842 Heinrichsberg, Österreich` (address)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/132328.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132328.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Michael Mühlbeck, Glöckler 35, 5252 Parz, Österreich, betreffend Beschwerde vom 17. Jänner 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 18. Dezember 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 Steuernummer 92-602/5429  beschlossen:   Der Vorlageantrag vom 5.6.2020 wird gemäß § 260 Abs. 1 lit.b BAO in Verbindung mit § 264  Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michael Mühlbeck` | `Michael Mühlbeck` |

**Missed by this rule (FN):**

- `Glöckler 35, 5252 Parz, Österreich` (address)
- `92-602/5429` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/132355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Janis Hundseder, Oskar Kokoschka-Gasse 100, 3263 Hochkoglberg, Österreich, über die Beschwerde vom 13.08.2019 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 07.08.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Steuernummer 29-864/3306  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Hundseder` | `Janis Hundseder` |

**Missed by this rule (FN):**

- `Oskar Kokoschka-Gasse 100, 3263 Hochkoglberg, Österreich` (address)
- `29-864/3306` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/132361.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Veronika Vierengel, Rohrerbergstraße 11, 8580 Gradenberg, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010  Wien, über die Beschwerde vom 13. Juni 2014 gegen den Bescheid des Finanzamtes Wien 1/23  vom 11. August 2010 betreffend Berichtigung gemäß § 293b BAO des Bescheides vom 1. Juni  2007 betreffend Umsatzsteuer 2005 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Veronika Vierengel` | `Veronika Vierengel` |

**Missed by this rule (FN):**

- `Rohrerbergstraße 11, 8580 Gradenberg, Österreich` (address)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Eugenia Vesen` | `Eugenia Vesen` |

**Missed by this rule (FN):**

- `Apollogasse 213, 5522 Lammertal, Österreich` (address)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Erhard Wintjens, Völkerweg 97, 8940 Döllach, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 17-868/7871  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erhard Wintjens` | `Erhard Wintjens` |

**Missed by this rule (FN):**

- `Völkerweg 97, 8940 Döllach, Österreich` (address)
- `17-868/7871` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132406.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Istvan  Bussen, Felix Faux-Straße 37, 5261 Scheiblberg, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Sibylle Wigandt, Daria Wiegend  und Dipl.-Ing. Jessica Janischewski  für den  Zeitraum August 2014 bis April 2016 bezogener Beträge an Familienbeihilfe,  Kinderabsetzbetrag und Ausgleichszahlung gemäß Verordnung (EG) 833/2004 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Istvan  Bussen` | `Istvan  Bussen` |

**Missed by this rule (FN):**

- `Felix Faux-Straße 37, 5261 Scheiblberg, Österreich` (address)
- `Sibylle Wigandt` (person)
- `Daria Wiegend` (person)
- `Dipl.-Ing. Jessica Janischewski` (person)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer in der Beschwerdesache  Silvius Fingermann, Steibstraße 113, 5723 Litzldorf, Österreich, über die Beschwerde vom 3. Mai 2018 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 5. April 2018 betreffend Anspruchszinsen (§ 205 BAO) 2013,  Steuernummer 91-977/4633, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Fingermann` | `Silvius Fingermann` |

**Missed by this rule (FN):**

- `Steibstraße 113, 5723 Litzldorf, Österreich` (address)
- `91-977/4633` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/132477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Chantal Pankauke, Unterrain 50, 4582 Seebach, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 19. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Chantal Pankauke` | `Chantal Pankauke` |

**Missed by this rule (FN):**

- `Unterrain 50, 4582 Seebach, Österreich` (address)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/132478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Irene Vysoudil, Moosheim 81, 9113 Obermitterdorf, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Irene Vysoudil` | `Irene Vysoudil` |

**Missed by this rule (FN):**

- `Moosheim 81, 9113 Obermitterdorf, Österreich` (address)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/132501.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Cäcilia Rossberg, Egarn 41, 4820 Kreutern, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cäcilia Rossberg` | `Cäcilia Rossberg` |

**Missed by this rule (FN):**

- `Egarn 41, 4820 Kreutern, Österreich` (address)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/132578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Regina Floegel, Retzer Weg 12, 5204 Baierham, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 6.3.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Regina Floegel` | `Regina Floegel` |

**Missed by this rule (FN):**

- `Retzer Weg 12, 5204 Baierham, Österreich` (address)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/132601.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Cornelia Jakubeck  in der Beschwerdesache Gabriel Widerschpan,  Beim Lagerhaus 8, 8984 Äußere Kainisch, Österreich, vertreten durch StB, über die Beschwerde vom 23. Juli 2018 gegen den  Bescheid des Finanzamtes vom 25. Juni 2018 betreffend Einkommensteuervorauszahlungen  2018 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gabriel Widerschpan` | `Gabriel Widerschpan` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Cornelia Jakubeck` (person)
- `Beim Lagerhaus 8, 8984 Äußere Kainisch, Österreich` (address)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Bodo Friehmann, Hohenwartweg 2, 4851 Fischham, Österreich, über die Beschwerde vom 30. September 2019 gegen den Einkommensteuerbescheid  2016 und den Einkommensteuerbescheid 2017 des Finanzamtes Wien 1/23 vom 27. August  2019 zu Steuernummer 09 75-279/5529  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bodo Friehmann` | `Bodo Friehmann` |

**Missed by this rule (FN):**

- `Hohenwartweg 2, 4851 Fischham, Österreich` (address)
- `75-279/5529` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/132743.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ingeborg Rainalter, Karl-Reisenbichler-Straße 60, 9560 Dolintschig, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ingeborg Rainalter` | `Ingeborg Rainalter` |

**Missed by this rule (FN):**

- `Karl-Reisenbichler-Straße 60, 9560 Dolintschig, Österreich` (address)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rocco Girstenbrei` | `Rocco Girstenbrei` |

**Missed by this rule (FN):**

- `Waubergweg 6, 9710 Pöllan, Österreich` (address)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Helga Zeißig` | `Helga Zeißig` |

**Missed by this rule (FN):**

- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich` (address)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/132893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132893.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Lilia Venczel, Rinnmühle 25, 4720 Wies, Österreich, vertreten durch KAPAS Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über  die Beschwerde vom 19.12.2019 gegen den Bescheid des Finanzamtes FA vom 13.05.2020  betreffend Feststellung von Einkünften gemäß § 188 BAO 2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lilia Venczel` | `Lilia Venczel` |

**Missed by this rule (FN):**

- `Rinnmühle 25, 4720 Wies, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Muran Waldhans` — partial — pred is substring of gold: `Muran Waldhans, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miroslav Hankel` — partial — pred is substring of gold: `Miroslav Hankel, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Miroslav Hankel, BEd`(person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dominik Kuzu Bf` — partial — gold is substring of pred: `Dominik Kuzu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Niels Aleksejew`(person)
- `Dominik Kuzu`(person)
- `Finanzamt Spittal Villach`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Vanessa Nemetz  in der Beschwerdesache Lydia Medert, BSc,  Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Innsbruck  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 02-329/4844  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

**False Positives:**

- `Lydia Medert` — partial — pred is substring of gold: `Lydia Medert, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof.in Vanessa Nemetz`(person)
- `Lydia Medert, BSc`(person)
- `Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich`(address)
- `FA Innsbruck`(organisation)
- `02-329/4844`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Rut Hus, LLM, Am Hirschfeld 23, 5232 Obermaisling, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 45-564/9779  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Rut Hus` — partial — pred is substring of gold: `Rut Hus, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rut Hus, LLM`(person)
- `Am Hirschfeld 23, 5232 Obermaisling, Österreich`(address)
- `45-564/9779`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130001.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130001.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Ruprecht Blübaum  in der Beschwerdesache Lee Heterich, Bakk. art. Bakk. iur.,  Economogasse 27, 7503 Zuberbach, Österreich, über die Beschwerde vom 13. Dezember 2016 gegen den Bescheid des  FA Kirchdorf Perg Steyr  vom 24. November 2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2015 zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Lee Heterich` — partial — pred is substring of gold: `Lee Heterich, Bakk. art. Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ruprecht Blübaum`(person)
- `Lee Heterich, Bakk. art. Bakk. iur.`(person)
- `Economogasse 27, 7503 Zuberbach, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gotthard Eppers  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 98-639/6692, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gotthard Eppers  ` — partial — gold is substring of pred: `Gotthard Eppers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gotthard Eppers`(person)
- `98-639/6692`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130285.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130285.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Vincent Scharpff  in der Beschwerdesache  Rita Griguhn Bf1-Adr***StB über die Beschwerde vom 18. Februar 2019 gegen den Bescheid  des Finanzamt Kirchdorf Perg Steyr  vom 9. Jänner 2019 betreffend Festsetzung eines ersten Säumniszuschlages zu  Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Rita Griguhn Bf` — partial — gold is substring of pred: `Rita Griguhn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Vincent Scharpff`(person)
- `Rita Griguhn`(person)
- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130442.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Dora Kühnel, MA, Fellentorstraße 9, 2265 Waltersdorf an der March, Österreich, über die Beschwerden vom 27. November 2018 gegen die Bescheide des Finanzamtes  Baden Mödling vom 12. November 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017, Steuernummer , zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dora Kühnel` — partial — pred is substring of gold: `Dora Kühnel, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dora Kühnel, MA`(person)
- `Fellentorstraße 9, 2265 Waltersdorf an der March, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Natalie Gosebrink` — partial — pred is substring of gold: `Natalie Gosebrink, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Alessia Olschofski`(person)
- `Natalie Gosebrink, Bakk. phil.`(person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich`(address)
- `50-818/5472`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132050.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Klaus Viechtel, MA, Brunfeldstraße 27, 5122 Sengstatt, Österreich, über die Beschwerde vom 22. Juni 2020 gegen  den Bescheid des Finanzamtes Wien 1/23 vom 19. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Klaus Viechtel` — partial — pred is substring of gold: `Klaus Viechtel, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klaus Viechtel, MA`(person)
- `Brunfeldstraße 27, 5122 Sengstatt, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Adrian Radakovitsch  ` — partial — gold is substring of pred: `Adrian Radakovitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Merlin Thorschmidt`(person)
- `Adrian Radakovitsch`(person)
- `Schlatterbergweg 97, 9344 Psein, Österreich`(address)
- `Finanzamt Steiermark Mitte`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Jennifer Kuntzemann, MSc Bakk. iur., Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich, über die Beschwerde vom 11. April 2020 gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 11. März 2020 betreffend  Rückzahlung ausbezahlter Zuschüsse zum Kinderbetreuungsgeld für das Jahr 2014,  Steuernummer StrNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Jennifer Kuntzemann` — partial — pred is substring of gold: `Jennifer Kuntzemann, MSc Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jennifer Kuntzemann, MSc Bakk. iur.`(person)
- `Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich`(address)

</details>

---

## `names_after_herr_frau` 🏆

**F1:** 0.166 | **Precision:** 0.533 | **Recall:** 0.099  

**Format:** `regex`  
**Rule ID:** `e748f7fb`  
**Description:**
Captures names following 'Herrn', 'Herr', 'Frau', or 'Fr.' (and optionally 'von'), stopping before professional suffixes. Does not include the title in the match.

**Content:**
```
(?:Herrn?|Frau|Fr\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.533 | 0.099 | 0.166 | 351 | 187 | 164 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 187 | 164 | 1702 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_69`)


Dazu können die Herrn Louisa Dreß und der Steuerberater, die in der Zeit vor Konkurseröffnung mit der Finanz Gespräche zur Verhinderung geführt haben, als Zeugen berichten.

| Predicted | Gold |
|---|---|
| `Louisa Dreß` | `Louisa Dreß` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129533.1_6`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Ludwig Thorbeck – war von seinem deutschen Arbeitgeber, der B  GmbH, vom 01.09.2004 bis zum 30.09.2009 nach Österreich entsandt worden.

| Predicted | Gold |
|---|---|
| `Ludwig Thorbeck` | `Ludwig Thorbeck` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_49`)


Im Firmenbuch ist Herr Jeskin als Geschäftsführer seit x.2009 eingetragen.

| Predicted | Gold |
|---|---|
| `Jeskin` | `Jeskin` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129937.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129937.1_12`)


Der Herr Burckardt schon geholfen mir, aber blöd gemacht, die Parkscheine etwas zaubern, ich hab  keine Ahnung was oder wie gemacht, aber er ziehen mir immer Geld wegen Parkscheine +  helfen, ich hab mit Hrn.

| Predicted | Gold |
|---|---|
| `Burckardt` | `Burckardt` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129950.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129950.1_5`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Dora Hohbohm – machte in der Erklärung zur Arbeitnehmer-

| Predicted | Gold |
|---|---|
| `Dora Hohbohm` | `Dora Hohbohm` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_92`)


Mit dieser E-Mail entgegnete der Bf in Beantwortung des Vorhaltes der belangten Behörde wie  folgt:   "Ich darf auf Ihr Email vom 06.06.2017 in Sachen Beschwerde Bf — StNr. 61 68-535/9689  zurückkommen und nach Besprechung mit Herrn Noeltge folgenden Lösungsvorschlag unterbreiten:  Grundsätzliche Überlegung:  Der VwGH vertritt in seinem Erkenntnis vom 29.03.2017 zur Hauptwohnsitzbefreiung die  Ansicht, dass sich die Befreiungsbestimmung des § 30 Abs. 2 Z 1 EStG lediglich auf den Grund  und Boden eines bebauten Grundstücks erstreckt, der nach der Verkehrsauffassung einem  üblicherweise als Bauplatz erforderlichen Grundstück entspricht.

| Predicted | Gold |
|---|---|
| `Noeltge` | `Noeltge` |

**Missed by this rule (FN):**

- `68-535/9689` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_106`)


Aus ökonomische Überlegungen (Vermeidung von Sachverständigen- und anderen  Rechtskosten bzw. zur Erlangung von Rechtssicherheit) wäre Herr Noeltge mit folgender Lösung, die  zwar sachlich stark vereinfachend ist, aber auch durch die Erlasslage gedeckt scheint  (Grundanteil lt. VO, Schätzung der anteiligen Anschaffungskosten der steuerhängigen Fläche  nach § 184 BAO aufgrund des VPI = nachvollziehbare Schätzmethode, die auch wie unten  dargestellt nach steuerlichen Grundsätzen plausibilisierbar ist) einverstanden:  Wie von Ihnen vorgeschlagen wird der Grundanteil mit 20% (lt. VO) angenommen und  aliquotiert in einen Teil von 1.000 m2 steuerbefreit und 1.144 m2 steuerpflichtig.

| Predicted | Gold |
|---|---|
| `Noeltge` | `Noeltge` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_15`)


Die Strafverfügung wurde Ihnen zugestellt und Sie erhoben fristgerecht Einspruch und gaben  erneut Herrn Schnak  geboren am geb, wohnhaft in AdrHerr, als Lenker an.

| Predicted | Gold |
|---|---|
| `Schnak` | `Schnak` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130901.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130901.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Maximiliane Weimer – beantragte in der elektronisch eingebrachten  Erklärung zur Arbeitnehmerveranlagung 2015 – seine Ehegattin betreffend – den „pauschalen  Freibetrag für das eigene Kfz wegen Vorliegens eines Ausweises gemäß   § 29b StVO 1960“.

| Predicted | Gold |
|---|---|
| `Maximiliane Weimer` | `Maximiliane Weimer` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_3`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes für Gebühren, Verkehrsteuer und Glücksspiel über die  Festsetzung eines ersten Säumniszuschlages vom 10. November 2014 wurde über Frau Eign (kurz: Bf.) von den Gebühren (Bestandsverträge) Journale 07/2014 von EUR 2.701,00 gemäß  § 217 Abs. 1 und 2 BAO ein Säumniszuschlag mit 2%, das sind EUR 54,02, mit der Begründung  festgesetzt, dass die oben angeführte Abgabenschuldigkeit nicht bis 15. September 2014  entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Eign` | `Eign` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Floriane Herppich  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Maltern  in Ausbildung zur Krankenpflegerin.

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |

**Missed by this rule (FN):**

- `Maltern` (city)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Floriane Herppich  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Floriane Herppich  nicht mehr in Frage kam, sodass sich Frau  Floriane Herppich  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |
| `Floriane Herppich` | `Floriane Herppich` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Floriane Herppich  nicht gemangelt hat, Frau Floriane Herppich  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |
| `Floriane Herppich` | `Floriane Herppich` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Aufgrund einer anonymen Anzeige im April 2013 wurden finanzpolizeiliche Ermittlungen  durchgeführt und erhoben, dass Frau Samuel Herpel (= Beschwerdeführerin, Bf) das Fahrzeug der  Marke X1, FIN Nr1, Erstzulassung (EZ) 1.10.2012, mit dem deutschen Kennzeichen AA1, im  Inland verwendet.

| Predicted | Gold |
|---|---|
| `Samuel Herpel` | `Samuel Herpel` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_92`)


Im Antwortschreiben vom 7.12.2020 wird seitens der Bf ausgeführt:  " … Ad 1)Frau Merbot hat im strittigen Zeitraum ab Oktober 2012 nach ihren Angaben und nach  ihrer Erinnerung mehrmals monatlich die Strecke D/Y (Hauptwohnsitz) nach A/X  (Nebenwohnsitz) zurück gelegt.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_96`)


Herr und Frau Herpel besuchen dort  gemeinsam Restaurants, das FitnessCenter, Ärzte oder absolvieren Theaterbesuche.

| Predicted | Gold |
|---|---|
| `Herpel` | `Herpel` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_97`)


In Land3 besitzt Frau Merbot ein Haus, das sie alle ca. 6 Wochen im Jahr für einige Tage entweder  allein oder mit ihrem Gatten aufsucht.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_102`)


Überdies besitzt es einen großen Obstgarten mit ca. 800 m2 (Kirschen, Äpfel,  Pflaumen, Walnüsse), die jedes Jahr von Frau Merbot selbst geernet werden.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_103`)


Anmerkungen:  Der Vollständigkeit halber möchten wir festhalten, dass Frau Merbot immer ihren Hauptwohnsitz  in Deutschland, D/Z bzw. D/Y, hatte.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_110`)


Frau Merbot ist und war ausschließlich in Deutschland versichert, bezahlt ihre Steuern nur in  Deutschland und war stets in Deutschland beschäftigt (XX) und wohnhaft (Hauptwohnsitz).

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_113`)


Herr C ist 1985  nach Österreich zurückgekehrt,Frau Herpel hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

| Predicted | Gold |
|---|---|
| `Herpel` | `Herpel` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_116`)


Nach ihrer Pensionierung ist Frau Merbot von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_121`)


Frau Merbot hat sich immer wieder in A/X aufgehalten.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_124`)


Frau Merbot hat nie die Aussage getätigt, dass sie sich zu irgend einem Zeitpunkt überwiegend in  Österreich aufhält. Dies wäre schlichtweg falsch.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/131561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131561.1_10`)


In der angeführten Bestätigung des Arbeitgebers des Bf. (X) vom 19.10.2015 wird wie folgt  ausgeführt:  "Wir bestätigen, dass Herr Möbs, wohnhaft in AdrBf  von 11.3.2013 bis 30.9.2015 in unserem Unternehmen im Bereich Energieberatung tätig war.

| Predicted | Gold |
|---|---|
| `Möbs` | `Möbs` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/131561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131561.1_21`)


Das Schreiben des Dienstgebers des Bf. vom 9.2.2016 lautete wie folgt:  „Ergänzend zu unserem Schreiben von 1.12.2015 können wir bestätigen, dass der maßgebliche  Bestandteil der Tätigkeit von Herrn Möbs die Abwicklung von Geschäftsabschlüssen ist.

| Predicted | Gold |
|---|---|
| `Möbs` | `Möbs` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/131561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131561.1_22`)


Herr Möbs unterliegt einer Zielvereinbarung, welche im Wesentlichen auf die Abwicklung von  Geschäftsabschlüssen basiert.“

| Predicted | Gold |
|---|---|
| `Möbs` | `Möbs` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_5`)


Bescheide der Abgabenbehörde  Mit Einkommensteuerbescheid 2013 vom 5.4.2018 wurde für das Jahr 2013 aus der  Arbeitnehmerveranlagung des Herrn Silvius Fingermann (in der Folge kurz: Bf.) eine Abgabengutschrift  in Höhe von € 1.649,00 festgestellt. Aufgrund dieser Gutschrift erfolgte - ebenfalls mit Bescheid  vom 5.4.2018 - die Berechnung der Anspruchszinsen, woraus sich eine Gutschrift für das Jahr  2013 in Höhe von € 93,06 ergab.

| Predicted | Gold |
|---|---|
| `Silvius Fingermann` | `Silvius Fingermann` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132743.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132743.1_72`)


Im Schreiben der Privatklink vom 21. Oktober 2019 wird auszugsweise ausgeführt:  "Herr Ingeborg Rainalter  stellte sich bei uns am 07.11.2017 erstmals vor.

| Predicted | Gold |
|---|---|
| `Ingeborg Rainalter` | `Ingeborg Rainalter` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_36`)


Herr Wolfgang Orosz  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Wolfgang Orosz` | `Wolfgang Orosz` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_72`)


Während die nach der AP an den Masseverwalter der L- GmbH i.L. ergangenen Bescheide  unbekämpft in Rechtskraft erwuchsen, brachte die T-Datenverarbeitungs GmbH gegen die  KeSt-Bescheide 2007-2009 namens des Bf fristgerecht Berufung ein, die in einem  nachgereichten Schriftsatz wir folgt begründet wurde:  „Wir als Vertretung (Vollmacht liegt auf) und im Auftrag und Rücksprache mit Herrn  Patrick Kirschbauer, legen wir folgenden Sachverhalt dar:  Tz. 4 Kapitalertragssteuer verdeckte Gewinnausschüttung  Jahr 2007  1.)

| Predicted | Gold |
|---|---|
| `Patrick Kirschbauer` | `Patrick Kirschbauer` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_99`)


Wegen  detaillierten Leistungsaufzeichnungen müssen wir darauf hinweisen, dass diese nicht vorliegen,  da sämtliche Unterlagen an die neue Geschäftsleitung Herrn Rubarth übergeben wurden.

| Predicted | Gold |
|---|---|
| `Rubarth` | `Rubarth` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_100`)


Zusammenfassend muss schon gesagt werden, dass von der Seite der Buchhaltungsführung  durch die Kanzlei XY zu groben Fehlern gekommen ist die Herrn Oeverhaus nicht  bekannt sein konnten, da er im vollen Vertrauen die Firmenunterlagen zur Bearbeitung  abgegeben hat und diese Arbeiten naturgemäß nicht geprüft hat.

| Predicted | Gold |
|---|---|
| `Oeverhaus` | `Oeverhaus` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_101`)


Das auch wie der Kunde, A.- Fenster sonderliche Buchungen durchgeführt hat, ist auch nicht Herrn Oeverhaus zu  zuschreiben.

| Predicted | Gold |
|---|---|
| `Oeverhaus` | `Oeverhaus` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_102`)


Grundsätzlich sind gewisse Gegebenheiten zu bemängeln, aber es ist Herrn Oeverhaus in keiner Weise eine verdeckte Gewinnausschüttung an zu lasten.

| Predicted | Gold |
|---|---|
| `Oeverhaus` | `Oeverhaus` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_104`)


Herr Patrick Kirschbauer  ersucht daher höflich um Aufhebung der Bescheide über die Festsetzung der  Kapitalertragssteuer für die Jahre 2007 über € 17.853,95, sowie für 2008 über € 20.933,35 und  2009 über € 8.350,00.“

| Predicted | Gold |
|---|---|
| `Patrick Kirschbauer` | `Patrick Kirschbauer` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_5`)


Alleingesellschafterin und Geschäftsführerin ist Frau Wahl   1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (kurz: Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Bf ist eine GmbH deren alleinige Gesellschafterin Frau Wahl ist.

| Predicted | Gold |
|---|---|
| `Wahl` | `Wahl` |
| `Wahl` | `Wahl` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_144`)


2. Die Gesellschafter der Weierstrass Textil  haben bisher mündlich vereinbart und halten  hinsichtlich des Geschäftsführerbezuges von Herrn Siegfried Terentew  folgendes fest: Herr  Siegfried Terentew  erhält einen fixen Geschäftsführerbezug von € 30.000,00 pro Jahr bzw. €  7 von 16 Seite 8 von 16

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |
| `Siegfried Terentew` | `Siegfried Terentew` |

**Missed by this rule (FN):**

- `Weierstrass Textil` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_145`)


2.500, 00 monatlich, des weiteren erhält Herr Siegfried Terentew  einen variablen Bezug von  max.

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin Dr. Michaela Schmutzer und die fachkundigen  Laienrichter L1 und L2 in der Finanzstrafsache gegen Frau Valerian Unterfranz, geb., Schanzplatz 130, 3664 Hundsbach, Österreich,  vertreten durch LBG Niederösterreich GmbH, Raiffeisenpromenade 2/1/6, 3830 Waidhofen an  der Thaya, wegen der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 1 und  Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde der Beschuldigten vom 9.  März 2020 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19  Klosterneuburg als Organ des Finanzamtes Waldviertel als Finanzstrafbehörde vom  21. November 2019, SpS 19, Strafnummer 23-2018, in Anwesenheit der Beschuldigten, ihres  Verteiigers, des Amtsbeauftragten HR AB sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Waldviertel als Finanzstrafbehörde zur Strafnummer 2018 gegen die  Beschuldigte geführte Finanzstrafverfahren wegen des Verdachts der Verkürzung von  Umsatzsteuer 2012 von € 860,00, Umsatzsteuer 2013 von € 860,00, Umsatzsteuer 2014 von €  860,00, Umsatzsteuer 2015 von € 860,00 bzw. Umsatzsteuer 2016 von € 433,33 und  Umsatzsteuervorauszahlungen 01-09/2017 von € 433,33 wird gemäß §§ 136, 157, 82 Abs. 3  lit. c FinStrG eingestellt.  Über Valerian Unterfranz  wird für die verbleibenden Finanzvergehen (bzw. strafbestimmenden  Werteträge) gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 7.944,00 verhängt.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Missed by this rule (FN):**

- `Schanzplatz 130, 3664 Hundsbach, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Waldviertel als Finanzstrafbehörde vom 21. November 2019, SpS 19,  Strafnummer 2018, wurde Frau Valerian Unterfranz, geboren am 13. Juli 1971, wohnhaft in Schanzplatz 130, 3664 Hundsbach, Österreich  schuldig erkannt, sie habe im Bereich des Finanzamtes Waldviertel   A.) durch Abgabe unrichtige Umsatz- und Einkommensteuererklärungen für die Jahre 2010 bis  2016, sohin unter Verletzung einer Wahrheits- und Offenlegungspﬂicht gemäß § 119 BAO  vorsätzlich bewirkt, dass   Umsatzsteuer für 2012 in Höhe von € 2.614,430, für 2013 in Höhe von € 2.981,49, für 2014 in  Höhe von € 3.307,05, für 2015 in Höhe von € 3.395,74, für 2016 in Höhe von € 3.430,78,   Einkommensteuer für 2010 in Höhe von € 1.446,00, für 2011 in Höhe von € 1.712,00, für 2012  in Höhe von € 4.691,00, für 2013 in Höhe von € 5.037,00, für 2014 in Höhe von € 5.599,00, für  2015 in Höhe von € 7.530,00 (€ 41.744,49)  verkürzt worden sei, und   B) vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes entsprechenden Voranmeldungen eine Verkürzung von  Vorauszahlungen an Umsatzsteuer für 01-09/2017 in der Höhe von € 2.605,11 bewirkt und dies  nicht nur für möglich, sondern für gewiss gehalten.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Missed by this rule (FN):**

- `Schanzplatz 130, 3664 Hundsbach, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_32`)


Begründung  Mit Erkenntnis vom 21.11.2019 wurde Frau Valerian Unterfranz  wegen Finanzvergehen gemäß § 33 Abs  1 FinStrG und § 33 Abs 2 lit a FinStrG zu einer Geldstrafe von € 8.800 verurteilt.  Strafbemessungsbasis waren – neben nichterklärten Einkünften aus Vermietung und  Verpachtung – Sicherheitszuschläge, welche die Außenprüfung den Einkünften aus  Gewerbebetrieb bzw. den Umsätzen hinzugerechnet hat.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_35`)


Laut Prüfungsbericht vom 30.11.2017 wurde von der Außenprüfung bei Frau Valerian Unterfranz  hinsichtlich Ihrer Einkünfte / Umsätze aus Gewerbebetrieb aufgrund von  Aufzeichnungsmängeln ein Sicherheitszuschlag gewinn- und umsatzerhöhend hinzugerechnet.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_6`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. Firmenbuch-  und Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung  als erwiesen zu Grunde legt:  Adressat der angefochtenen Erledigung ist Herr Ronald Jundt (nachfolgend Herr M.), der  aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel  Miteigentümer jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde  (Lageadresse: R-Gasse 15, 9999 Wien).

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_17`)


Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R- Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Herrn M.:   „Herrn   Ronald Jundt   B-Straße 4/7  9999 Wien  Betreff:Furtnex-Versand GmbH in Liqu.    Wien, 05.11.2019   9996 S-Straße 3/9   2 von 9 Seite 3 von 9

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_25`)


Die Inanspruchnahme von Herrn Ronald Jundt  als Zahlungsverpflichteter erfolgte, weil die als  Leistungsgerbringerin fungierende Furtnex-Versand GmbH in Liqu. ihrer Zahlungsverpflichtung nicht  nachgekommen ist.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_32`)


Beschwerde gegen den Bescheid - Leistungsgebot  Meine Beschwerde richtet sich gegen den Bescheid-Leistungsgebot an Herrn Ronald Jundt  vom  5.11.2019, zugestellt am 13.11.2019, mit dem Antrag auf Aufhebung dieses Bescheides.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_33`)


Als Begründung ist anzuführen, dass Herr Ronald Jundt  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Furtnex-Versand GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_8`)


Frau Lentzen erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Amber Biegaj, Bakk. techn.  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Missed by this rule (FN):**

- `Amber Biegaj, Bakk. techn.` (person)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_11`)


Frau werde aufgefordert, binnen zwei Wochen nach  Zustellung des Mängelbehebungsauftrages die fehlende Unterschrift des Beschuldigten  beizubringen oder eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Lentzen sowie die Berechtigung dieser Person zur Einbringung des Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_14`)


Die zwei Schreiben wurde an Frau Lentzen durch Hinterlegung am 14.06.2021 zugestellt und von  dieser am 14.06.2021 nachweislich übernommen (Übernahmebestätigung RSb).

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_15`)


Mit fristgerechtem Schreiben vom 20.06.2021 nahm der Bf. Bezug auf die zwei Schreiben der  MA 67 vom 09.06.2021 ("VERFAHRENSANORDNUNG - Nachreichung Unterschrift bzw.  Vollmachtsvorlage"), die an Frau Lentzen gerichtet waren und führte der Bf. darin aus: „… möchte  ich hiermit eigenhändig bestätigen, dass das Fahrzeug mit dem angegebenen Kennzeichen  nicht in meinem Besitz ist und ich auch nicht weiß, wem es gehört“.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Lentzen im eigenen Namen gegen die an Herrn Amber Biegaj, Bakk. techn.  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Missed by this rule (FN):**

- `Amber Biegaj, Bakk. techn.` (person)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_26`)


Deshalb sei Frau Lentzen mit Schreiben der Magistratsabteilung 67 vom 09.06.2021 aufgefordert  worden, binnen zwei Wochen eine für das Verwaltungsstrafverfahren gültige Vollmacht von  Herrn Amber Biegaj, Bakk. techn.  zu übermitteln.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Missed by this rule (FN):**

- `Amber Biegaj, Bakk. techn.` (person)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_27`)


Dieser Aufforderung sei Frau Lentzen jedoch nicht nachgekommen.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_28`)


Am 23.06.2021 sei von Herrn  Amber Biegaj, Bakk. techn.  lediglich ein Schreiben mit folgendem Inhalt übermittelt worden: „Bezugnehmend  auf Ihr Schreiben an Frau Lentzen vom 09.06.2021 möchte ich hiermit eigenhändig bestätigen,  dass das Fahrzeug mit dem angegebenen Kennzeichen nicht in meinem Besitz ist und ich auch  nicht weiß, wem es gehört“.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Missed by this rule (FN):**

- `Amber Biegaj, Bakk. techn.` (person)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_29`)


Aus dieser E-Mail gehe nicht hervor, dass Frau Lentzen am 08.05.2021 zur Einbringung des  Rechtsmittels berechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_31`)


Mit Schreiben vom 11.07.2021 (eingelangt bei der Behörde am 14.07.2021) teilte der Bf. der  MA 67 mit „Anbei finden Sie eine Vollmacht, die ich Frau ausgestellt habe und die sie nicht  mitgeschickt hat“ und legte dem Schreiben eine von ihm unterschriebene Vollmacht bei, mit  der er Frau Lentzen zur Vertretung gegenüber allen Behörden (einschließlich Gerichten, Banken,  Versicherungen und sonstigen Dritten gegenüber) bevollmächtigte.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_32`)


Gegen die zwei an Frau Lentzen gerichteten Zurückweisungsbescheide vom 25.06.2021 wurde von  Amber Biegaj, Bakk. techn.  am 03.09.2021 Einspruch (gemeint: Beschwerde) erhoben und vorgebracht, dass er  für die Eugenia Römgens (Anmerkung BFG: nicht Zulassungsbesitzerin von gegenständlichem Kfz)  vom Jänner 2021 bis April 2021 tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Missed by this rule (FN):**

- `Amber Biegaj, Bakk. techn.` (person)
- `Eugenia Römgens` (person)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_39`)


erschienen, dabei habe er mit Herrn Philippowitz gesprochen und ihm den Zahlschein vorgelegt.

| Predicted | Gold |
|---|---|
| `Philippowitz` | `Philippowitz` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_49`)


Da sich die Behörde über die Identität des Einbringers nicht im Klaren war, wurde Frau Lentzen  aufgefordert, eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zum  Einbringer sowie die Berechtigung dieser Person zur Einbringung des Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_50`)


Der Aufforderung wurde von Frau Lentzen nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_54`)


Die MA 67 ging nunmehr davon aus, dass der Einspruch gegen die zwei Strafverfügungen von Frau Lentzen erhoben wurde und wies deren (jeweiligen) Einspruch mit zwei Bescheiden vom  25.06.2021 gemäß § 13 Abs. 3 AVG iVm § 24 Abs. 1 VStG 1991 mit der im Verfahrensgang  angeführten Begründung zurück.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_56`)


Gegen die zwei an Frau Lentzen gerichteten Zurückweisungsbescheide wurde vom Bf. am  03.09.2021 durch den Bf. Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Lentzen` | `Lentzen` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/134779.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134779.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Jonas Faustmann, Aufsatzweg 16, 9344 Zammelsberg, Österreich, vertreten durch Martin Friedl, Wirtschaftsprüfer -  Steuerberater Marktplatz 2, 4650 Lambach, wegen der Beteiligung an Finanzvergehen der  Abgabenhinterziehungen gemäß §§ 11, 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) bzw. der  Abgabenverkürzungen bzw. §§ 11, 34 Abs. 1 FinStrG über die Beschwerde der  Amtsbeauftragten vom 6. November 2020 gegen das Erkenntnis des Spruchsenates beim  damaligen Finanzamt Wien 9/18/19 Klosterneuburg als Organ des damaligen Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 10. September 2020, SpS,  Finanzstrafverfahren, nach Durchführung einer mündlichen Verhandlung am 5. Oktober 2021  in Anwesenheit des Beschuldigten, seines Verteidigers Rechtsanwalt Mag. Lukas Friedl, der  Beschwerdeführerin und Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Jonas Faustmann  ist schuldig, vorsätzlich als damaliger Steuerberater von Oleg PetigkB.

| Predicted | Gold |
|---|---|
| `Jonas Faustmann` | `Jonas Faustmann` |

**Missed by this rule (FN):**

- `Aufsatzweg 16, 9344 Zammelsberg, Österreich` (address)
- `Oleg PetigkB` (person)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/134779.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134779.1_18`)


Auf Frage der Betriebsprüferin, C. D., ob eine  Selbstanzeige erstattet werde, verneinte dies Jonas Faustmann, so dass Frau Soltmann im Prüfungsformular  „keine SA" ankreuzte.

| Predicted | Gold |
|---|---|
| `Soltmann` | `Soltmann` |

**Missed by this rule (FN):**

- `Jonas Faustmann` (person)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/134779.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134779.1_320`)


A: Der Prüfungsauftrag war ja ursprünglich von 2014 - 2016, zu dem Zeitpunkt, als mich die Frau Soltmann kontaktiert hat, ich habe hier eine E-Mail vom 14.06.2018, da hatte ich die Unterlagen  für 2014 und 2015, und für 2016 habe ich sie am 02.07.2018 bekommen   21 von 37 Seite 22 von 37

| Predicted | Gold |
|---|---|
| `Soltmann` | `Soltmann` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/134779.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134779.1_430`)


Diese Gutschriften wurden von Herrn Engelbert Kolodzej in Kenntnis der Unrichtigkeit in keiner  Weise verwendet, weder wurde eine Rückzahlung beauftragt noch wurden laufende  Umsatzsteuervoranmeldungen damit verrechnet, sondern trotz des Guthabens am  Abgabenkonto weiterhin pünktlich entrichtet.

| Predicted | Gold |
|---|---|
| `Engelbert Kolodzej` | `Engelbert Kolodzej` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_154`)


Ich habe dann mit dem Herrn Kollegen FT Kontakt aufgenommen und er hat mir gesagt, er  sucht auch Unterlagen und hat sie mir dann mitgegeben.

**False Positives:**

- `Kollegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_181`)


Der Herr Ing KB und ich sind langjährig befreundet.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129437.1_16`)


Eine weitere Bestätigung der X- Versicherung a.G. vom 2.5.2019 enthält folgenden Passus: „…Da Sie und Ihre Frau Ihren  Wohnsitz ins Ausland verlegt haben, unterliegen Sie nicht der Versicherungspflicht in  Deutschland.

**False Positives:**

- `Ihren  Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_4`)


Laut Firmenbuchauszug ist Herr Jeskin Geschäftsführer seit 23.7.2009.

**False Positives:**

- `Jeskin Geschäftsführer` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_5`)


Entscheidungsgründe  Mit Schreiben vom 28 April 2014 zeigte die Verpächterin, die Fr. GmbH den Pachtvertrag vom  23.04.2014, abgeschlossen zwischen ihr und der S1.2 Gesellschaft m.b.H. & Co KG (im  Folgenden: KG), für das Pachtobjekt (Restaurantbetrieb), mit dem Ersuchen um Vergebührung  an.

**False Positives:**

- `Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Donald Hayder` — partial — pred is substring of gold: `Donald Hayder, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Jeffrey Wengschick`(person)
- `Donald Hayder, MA`(person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131561.1_71`)


Schulung im Bereich „Verkauf"   Um noch erfolgreicher, meine verkäuferischen Ziele zu erreichen, werde ich von meinem  Arbeitgeber der X NÖ dahingehend auch laufend geschult. Als Beispiel ist das bereits zweimal  stattgefundene Verkaufstraining mit Herrn Hubert Mann zu nennen (siehe Beilagen).

**False Positives:**

- `Hubert Mann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131742.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131742.1_9`)


Die beschwerdeführende Partei sei der  Auffassung von Herrn Univ.-Prof. Dr. Reinhold Beiser (SWK 9/2017, 498): „Wenn es zu einer  Betriebsaufgabe kommt, so bleiben die Wertpapiere die vorher für die Ausnutzung eines  Gewinnfreibetrages angeschafft wurden, notwendiges nachträgliches Betriebsvermögen unter  der Voraussetzung, dass sie bis zum Ablauf der Behaltefrist gehalten werden.

**False Positives:**

- `Univ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131954.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131954.1_39`)


Die MA 65 teilte dem BFG mit E-Mail vom 21. Dezember 2020 Folgendes mit:  „Bei der vom Herrn Istvan  Geißler, MA  genannten Vorschreibung handelt es sich um eine freiwillige  Serviceleistung (Information) der Stadt Wien, die BescheidinhaberInnen die Möglichkeit bietet,  vor Ablauf der alten Bewilligung durch Einzahlung des ausgewiesenen Betrages, rechtzeitig eine  neue zu beantragen.

**False Positives:**

- `Istvan  Geißler` — partial — pred is substring of gold: `Istvan  Geißler, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Istvan  Geißler, MA`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131954.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131954.1_43`)


Herr Istvan  Geißler, MA  hätte daher rechtzeitig einen Antrag auf Erteilung der  Ausnahmebewilligung stellen müssen (idealerweise vor dem 30.4.).

**False Positives:**

- `Istvan  Geißler` — partial — pred is substring of gold: `Istvan  Geißler, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Istvan  Geißler, MA`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_23`)


Auf Grund einer Anfrage des Bundesfinanzgerichtes bei der für Meldeangelegenheiten  zuständigen Fachdienststelle in der Stadt Wien, der MA 62, teilte diese mit E-Mail vom  25.2.2021 folgendes mit:  „Zu Ihrer Anfrage teile ich Ihnen seitens der Magistratsabteilung 62 als zuständiger  Fachdienststelle für Meldeangelegenheiten in der Stadt Wien mit, dass Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wie  von ihm angegeben von uns nach Durchführung eines Verfahrens nach § 15 Meldegesetz  amtlich von der Adresse xy abgemeldet wurde.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_26`)


Der Erheber bekam vor Ort am  14. Jänner 2020 von einer Hauspartei, deren Identität wir nicht kennen, die Auskunft, dass Herr  Lieselotte Rübenkönig, Bakk. rer. nat.  unbekannt wohin verzogen sei.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_27`)


Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wurde von uns zweimal im  Verfahren angeschrieben, davon einmal mit RSb-Rückscheinbrief, und hat darauf nicht  reagiert.“

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Univ.-Prof.in StR Caroline Akkoca, MBA (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/132810.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Dr.in KommR Ida Kschischow (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr.in KommR Ida Kschischow`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in KommR Ida Kschischow`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_54`)


Die Beschwerdevorentscheidungen für die Jahre 2013 und 2014 wurden wie folgt begründet:  „Herr Mag R wurde von seinem österreichischen Arbeitgeber,IGS Pflege AG  von 1. August 2010 bis 31.  März 2015 in die USA entsendet.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IGS Pflege AG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_57`)


Anschließend ist Herr  Mag. R ein neues Dienstverhältnis in der Schweiz eingegangen und mit der Familie von den USA  in die Schweiz übersiedelt. Die Verlagerung des Lebensmittelpunktes in den Entsendestaat sei  ergänzend an Hand der (Vermutungs-)Regel gemäß Rz 7596 EStR zu beurteilen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_75`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Wahl   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Wahl   Gegenstand` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_6`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw.  Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung als  erwiesen zu Grunde legt:  Adressatin der angefochtenen Erledigung ist Frau Brucktranor-Sanitär (nachfolgend Frau M.), die  aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel  Miteigentümerin jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde  (Lageadresse: R-Gasse 15, 9999 Wien).

**False Positives:**

- `Brucktranor` — partial — pred is substring of gold: `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brucktranor-Sanitär`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_14`)


Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R- Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Frau M.:  Frau   Brucktranor-Sanitär   B-Straße 4/7  9999 Wien  Betreff:Telekom Heimver GmbH in Liqu.     Wien, 05.11.2019   9996 S-Straße 3/9    St.Nr. 999/999-BV 24   BESCHEID –  Leistungsgebot

**False Positives:**

- `Brucktranor` — partial — pred is substring of gold: `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brucktranor-Sanitär`(organisation)
- `Telekom Heimver GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_22`)


Die Inanspruchnahme von Frau Brucktranor-Sanitär  als Zahlungsverpflichtete erfolgte, weil die als  Leistungsgerbringerin fungierende M- GmbH in Liqu. ihrer Zahlungsverpflichtung nicht  nachgekommen ist.

**False Positives:**

- `Brucktranor` — partial — pred is substring of gold: `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brucktranor-Sanitär`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_28`)


2019 langte beim FA auf dem Postweg der nachfolgende Schriftsatz ein:  „XY Steuerberater Barbara Früauf  Wirtschaftstreuhand-  gesellschaft m.b.H.   Steuerberater   Zertifizierter Mediator       Wien, 2019-12-03  Betreff: Brucktranor-Sanitär, 9999 Wien B-Straße 4/7   Beschwerde gegen den Bescheid - Leistungsgebot  Meine Beschwerde richtet sich gegen den Bescheid-Leistungsgebot an Frau Brucktranor-Sanitär  vom  5.11.2019, zugestellt am 13.11.2019 (siehe Anhang) mit dem Antrag auf Aufhebung dieses  Bescheides.

**False Positives:**

- `Brucktranor` — similar text (different position): `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Barbara Früauf`(person)
- `Brucktranor-Sanitär`(organisation)
- `Brucktranor-Sanitär`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_29`)


Als Begründung ist anzuführen, dass Frau Brucktranor-Sanitär  keine Gesamtschuldnerin aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der M- GmbH nicht um Bauleistungen  handelt. Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern  bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  3 von 8 Seite 4 von 8

**False Positives:**

- `Brucktranor` — partial — pred is substring of gold: `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brucktranor-Sanitär`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/134080.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134080.1_35`)


Die von der Firma M- GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Frau Brucktranor-Sanitär  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da sie nicht Gesamtschuldnerin ist.

**False Positives:**

- `Brucktranor` — partial — pred is substring of gold: `Brucktranor-Sanitär`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brucktranor-Sanitär`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/134151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134151.1_18`)


Seit 2003: hatte Frau Verwandte 1, eine Verwandte des Bf. („Verwandte 1“), die Konzession  zum Betrieb einer Apotheke.

**False Positives:**

- `Verwandte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_4`)


Es handelt sich hierbei um eine Beschwerde vom  22.7.2020 des Herrn Prof. Priv.-Doz. Johann Engelkemeier.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Priv.-Doz. Johann Engelkemeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Priv.-Doz. Johann Engelkemeier`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/134399.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134399.1_28`)


Mit E-Mail vom 26. April 2021 stellte der Beschwerdeführer einen Vorlageantrag und führte  aus, das Lokal in W., S-Straße, sei auch im Jahr 2020 an Herrn Mieter vermietet gewesen.

**False Positives:**

- `Mieter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/134399.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134399.1_35`)


Das sich im Gebäude befindliche Geschäftslokal war im Streitjahr an Herrn Mieter vermietet.

**False Positives:**

- `Mieter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/134610.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134610.1_10`)


Ich bin ausgestiegen und habe auf der anderen Straßenseite, Cothmannstraße 11, wo wir  eine Baustelle mit Halteverbot hatten, unserem Herrn Arbeitsunterlagen übergeben.

**False Positives:**

- `Arbeitsunterlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_8`)


Frau Lentzen erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Amber Biegaj, Bakk. techn.  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

**False Positives:**

- `Amber Biegaj` — partial — pred is substring of gold: `Amber Biegaj, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lentzen`(person)
- `Amber Biegaj, Bakk. techn.`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Lentzen im eigenen Namen gegen die an Herrn Amber Biegaj, Bakk. techn.  2 von 7 Seite 3 von 7

**False Positives:**

- `Amber Biegaj` — partial — pred is substring of gold: `Amber Biegaj, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lentzen`(person)
- `Amber Biegaj, Bakk. techn.`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_26`)


Deshalb sei Frau Lentzen mit Schreiben der Magistratsabteilung 67 vom 09.06.2021 aufgefordert  worden, binnen zwei Wochen eine für das Verwaltungsstrafverfahren gültige Vollmacht von  Herrn Amber Biegaj, Bakk. techn.  zu übermitteln.

**False Positives:**

- `Amber Biegaj` — partial — pred is substring of gold: `Amber Biegaj, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lentzen`(person)
- `Amber Biegaj, Bakk. techn.`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_28`)


Am 23.06.2021 sei von Herrn  Amber Biegaj, Bakk. techn.  lediglich ein Schreiben mit folgendem Inhalt übermittelt worden: „Bezugnehmend  auf Ihr Schreiben an Frau Lentzen vom 09.06.2021 möchte ich hiermit eigenhändig bestätigen,  dass das Fahrzeug mit dem angegebenen Kennzeichen nicht in meinem Besitz ist und ich auch  nicht weiß, wem es gehört“.

**False Positives:**

- `Amber Biegaj` — partial — pred is substring of gold: `Amber Biegaj, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amber Biegaj, Bakk. techn.`(person)
- `Lentzen`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134652.1_38`)


Herr Amber Biegaj, Bakk. techn.  sei persönlich bei genannter Firma  3 von 7 Seite 4 von 7

**False Positives:**

- `Amber Biegaj` — partial — pred is substring of gold: `Amber Biegaj, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amber Biegaj, Bakk. techn.`(person)

</details>

---

## `names_with_academic_titles` 🏆

**F1:** 0.287 | **Precision:** 0.415 | **Recall:** 0.220  

**Format:** `regex`  
**Rule ID:** `63288caf`  
**Description:**
Captures names preceded by German academic titles (Dr., Mag., Prof., Univ.-Prof., Hon.-Prof., Priv.-Doz., etc.) including the 'in' suffix for female titles and multi-title combinations.

**Content:**
```
(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Mag\.in|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|OMedR|KommR|KzlR|RgR|OStR|StR|Ing\.|Dipl\.-Ing\.|LLM|BEd|Bakk\.|BSc|MA|MSc|PhD|DDr\.|DDr\.in|\u00d6kR|Techn R|VetR|MedR|Kff\.)\s+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.415 | 0.220 | 0.287 | 1006 | 417 | 589 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 417 | 589 | 1480 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hemma Bährs` | `Dr.in Hemma Bährs` |
| `Univ.-Prof.in Rachel Darnieder` | `Univ.-Prof.in Rachel Darnieder` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Viktoria Kreiselmayer` | `Univ.-Prof.in Viktoria Kreiselmayer` |

**Missed by this rule (FN):**

- `Muran Waldhans, BEd` (person)
- `Am Tegel 5, 9831 Waben, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128788.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128788.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Mag. ÖkR Nigel Wawrek,  Felchenstraße 4, 7461 Allersdorf im Burgenland, Österreich, vertreten durch RA, Adr RA A, über die Beschwerde vom 25. April 2016 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 18. April 2016 betreffend  Familienbeihilfe für die Kinder 1 K, 2 K, 3 K und 4 K für die Monate August 2015 bis April 2016  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `ÖkR Nigel Wawrek` | `ÖkR Nigel Wawrek` |

**Missed by this rule (FN):**

- `Felchenstraße 4, 7461 Allersdorf im Burgenland, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128929.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Erich Nolde  in der Beschwerdesache Urs Locke,  Jägersberg 20, 3654 Pölla, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Erich Nolde` | `Dr. Erich Nolde` |

**Missed by this rule (FN):**

- `Urs Locke` (person)
- `Jägersberg 20, 3654 Pölla, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Bartholomäus Beier  in der Beschwerdesache Daisy Strakbein,  Gottestaler Straße 27, 8693 Dürrenthal, Österreich, betreffend Beschwerde vom 20. Februar 2018 gegen die Bescheide  des  Finanzamtes Gmunden Vöcklabruck vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 den Beschluss:  I. Die angefochtenen Bescheide vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 und die Beschwerdevorentscheidungen vom 28. März 2018  werden gemäß § 278 Abs 1 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Bartholomäus Beier` | `Priv.-Doz. Bartholomäus Beier` |

**Missed by this rule (FN):**

- `Daisy Strakbein` (person)
- `Gottestaler Straße 27, 8693 Dürrenthal, Österreich` (address)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_196`)


b. Schreiben des KommR Stephanie Stickling an das Finanzamt zum Konkurs der Bf. vom 6. Juli 2010:  Ich beziehe mich auf das Telefonat vom 5. Juli 2010 und gestatte festzuhalten, dass das  Konkursverfahren über das Vermögen der WaldVersicherung KG nach der Verteilung aufgehoben worden ist.

| Predicted | Gold |
|---|---|
| `KommR Stephanie Stickling` | `KommR Stephanie Stickling` |

**Missed by this rule (FN):**

- `WaldVersicherung KG` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Niels Aleksejew` | `Univ.-Prof. Niels Aleksejew` |

**Missed by this rule (FN):**

- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `KzlR Adalbert Bürks` | `KzlR Adalbert Bürks` |

**Missed by this rule (FN):**

- `Schörbergerstraße 99, 9560 Maltschach, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

| Predicted | Gold |
|---|---|
| `Dr.in Fabienne Siewek` | `Dr.in Fabienne Siewek` |

**Missed by this rule (FN):**

- `Vincent und Zielinska Solar GmbH` (organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache MedR Irvin Leider, 10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich, über die Beschwerde vom 22. September 2017 gegen den Bescheid des FA vom  21. August 2017 betreffend Einkommensteuer 2016 Steuernummer 30-411/2742  zu Recht  erkannt:   1.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Irvin Leider` | `MedR Irvin Leider` |

**Missed by this rule (FN):**

- `10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich` (address)
- `30-411/2742` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Janis Abelen` | `Univ.-Prof. Janis Abelen` |

**Missed by this rule (FN):**

- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Vanessa Nemetz  in der Beschwerdesache Lydia Medert, BSc,  Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Innsbruck  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 02-329/4844  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Vanessa Nemetz` | `Hon.-Prof.in Vanessa Nemetz` |

**Missed by this rule (FN):**

- `Lydia Medert, BSc` (person)
- `Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich` (address)
- `FA Innsbruck` (organisation)
- `02-329/4844` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Rohlfsen  in der Beschwerdesache des  OStR OMedR Gernot Regensburger, Ort im Innkreis 35, 8462 Steinbach, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamt Niederösterreich Mitte  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Rohlfsen` | `Dr.in Ute Rohlfsen` |

**Missed by this rule (FN):**

- `OStR OMedR Gernot Regensburger` (person)
- `Ort im Innkreis 35, 8462 Steinbach, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Dr.in Klara Willumelies` | `Dr.in Klara Willumelies` |

**Missed by this rule (FN):**

- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Sellnow` | `Priv.-Doz. Eckard Sellnow` |

**Missed by this rule (FN):**

- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129861.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Univ.-Prof.in Lucia Crienitz  in der Beschwerdesache PhD Corbinian Perkins,  Ebersbergerstraße 13j, 4770 Hötzenedt, Österreich  vertreten durch RA MMag. Dr. Alexander Lamplmayr als gerichtlicher  Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der  beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt St. Johann Tamsweg Zell am See  betreffend die Anträge vom 3.5.2018 auf Zustellung  des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte  Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge  wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung,  Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung  bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum  unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung  hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe  von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen:  a)

| Predicted | Gold |
|---|---|
| `PhD Corbinian Perkins` | `PhD Corbinian Perkins` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Univ.-Prof.in Lucia Crienitz` (person)
- `Ebersbergerstraße 13j, 4770 Hötzenedt, Österreich` (address)
- `Finanzamt St. Johann Tamsweg Zell am See` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129861.1_5`)


Begründung  PhD Corbinian Perkins   hat mit Eingabe vom 25.06.2020, eingelangt am 29.06.2020, gemäß § 284 Abs. 1 BAO eine  Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht in der Erledigung seiner  Anträge vom 03.05.2018 (siehe oben im Spruch) erhoben.

| Predicted | Gold |
|---|---|
| `PhD Corbinian Perkins` | `PhD Corbinian Perkins` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130001.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130001.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Ruprecht Blübaum  in der Beschwerdesache Lee Heterich, Bakk. art. Bakk. iur.,  Economogasse 27, 7503 Zuberbach, Österreich, über die Beschwerde vom 13. Dezember 2016 gegen den Bescheid des  FA Kirchdorf Perg Steyr  vom 24. November 2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2015 zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ruprecht Blübaum` | `Dr. Ruprecht Blübaum` |

**Missed by this rule (FN):**

- `Lee Heterich, Bakk. art. Bakk. iur.` (person)
- `Economogasse 27, 7503 Zuberbach, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130057.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130057.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Seidenstecher  in der Beschwerdesache des  HR Edith Tuncel, Bakk. rer. nat., Heide, 18.a Straße 30h, 4674 Untergmain, Österreich, über die Beschwerde vom 6. März 2017 gegen den Bescheid des  Finanzamt Bruck Eisenstadt Oberwart  vom 30. Jänner 2017 betreffend Grunderwerbsteuer 2017 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Leila Seidenstecher` | `Univ.-Prof.in Leila Seidenstecher` |

**Missed by this rule (FN):**

- `HR Edith Tuncel, Bakk. rer. nat.` (person)
- `Heide, 18.a Straße 30h, 4674 Untergmain, Österreich` (address)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_26`)


Sie könne nicht  aufstehen, bewegt aber seitengleich (diesbezüglich liegen keine Befunde vor)   Derzeitige Beschwerden:   diverse Schmerzen, sie könne nicht gehen   Behandlung(en) / Medikamente / Hilfsmittel:   kann keine Angaben machen   Sozialanamnese:   lebt in Caritasheim vollbetreut, I(nvaliditäts)Pension, Pflegestufe 4, Erwachsenenvertretung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   28.4.87 Dipl.-Ing. Kirsten Hüffner: Es handelt sich bei (der Bf.) um eine Oligophrenie.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Kirsten Hüffner` | `Dipl.-Ing. Kirsten Hüffner` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Kirsten Hüffner` | `Dipl.-Ing. Kirsten Hüffner` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130285.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130285.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Vincent Scharpff  in der Beschwerdesache  Rita Griguhn Bf1-Adr***StB über die Beschwerde vom 18. Februar 2019 gegen den Bescheid  des Finanzamt Kirchdorf Perg Steyr  vom 9. Jänner 2019 betreffend Festsetzung eines ersten Säumniszuschlages zu  Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Vincent Scharpff` | `Univ.-Prof. Vincent Scharpff` |

**Missed by this rule (FN):**

- `Rita Griguhn` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130413.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130413.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des KzlR Silvius Schlotter, Rehlingenstraße 125, 5251 Miesenberg, Österreich  vom 10. Jänner 2020, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 12. Dezember 2019,  MA67/000/2019, wegen der Verwaltungsübertretung des § 9 Abs. 2 Wiener  Kontrolleinrichtungenverordnung iVm § 4 Abs. 3 Wiener Parkometergesetz 2006 zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 36,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 8 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `KzlR Silvius Schlotter` | `KzlR Silvius Schlotter` |

**Missed by this rule (FN):**

- `Rehlingenstraße 125, 5251 Miesenberg, Österreich` (address)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Techn R Melinda Kälbli  zu tragen.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Techn R Melinda Kälbli  auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Björn Hüpscher` | `Dr. Björn Hüpscher` |

**Missed by this rule (FN):**

- `Igor Strunz` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frieda Krein` | `Hon.-Prof.in Frieda Krein` |
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Missed by this rule (FN):**

- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich` (address)
- `60-936/8299` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_2`)


Begründung  Der Beschwerdeführer Priv.-Doz.in Elena Kaminskiy  hat mit Eingabe vom 22.10.2020, eingelangt am 27.10.2020,  gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  über die Beschwerde gegen den Einkommensteuerbescheid für 2019 erhoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130694.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Alan Kockhans  in der Beschwerdesache Geraldine Melwer,  Geißtobel 17, 9585 Fürnitz, Österreich, Ungarn, über die Beschwerde vom 6. Oktober 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 14. September 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Alan Kockhans` | `Priv.-Doz. Alan Kockhans` |

**Missed by this rule (FN):**

- `Geraldine Melwer` (person)
- `Geißtobel 17, 9585 Fürnitz, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Gruebert` | `Priv.-Doz. Lubomir Gruebert` |

**Missed by this rule (FN):**

- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jeannine Hüpgen` | `Priv.-Doz.in Jeannine Hüpgen` |

**Missed by this rule (FN):**

- `Alois Jeckl` (person)
- `Amlach 6, 2620 Straßhof, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `66-092/6335` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

| Predicted | Gold |
|---|---|
| `RgR Frederike Wegerth` | `RgR Frederike Wegerth` |

**Missed by this rule (FN):**

- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich` (address)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Erwin Göktan` | `Dipl.-Ing. Erwin Göktan` |

**Missed by this rule (FN):**

- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Univ.-Prof. August Häusele, Schnitzlerweg 23, 3542 Gföhleramt, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. August Häusele` | `Univ.-Prof. August Häusele` |

**Missed by this rule (FN):**

- `Schnitzlerweg 23, 3542 Gföhleramt, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130909.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Kaufvertrag vom 8. Mai 2013 verkauften Ehefrau, Univ.-Prof. August Häusele (Beschwerdeführer, im  Folgenden kurz als Bf. bezeichnet) und Sohn die Grundstücke A und B sowie x-tel  Miteigentumsanteile aus dem Grundstück C, KG G, (Kaufobjekt 1) an Frau H und y-tel  Miteigentumsanteile aus dem Grundstück C, KG G, (Kaufobjekt 2) an Frau K.  Mit Vorhalt des Finanzamtes vom 6. Oktober 2014 wurde der Bf. darauf hingewiesen, dass die  beantragte Wohnsitzbefreiung nur für das Gebäude sowie für Grund und Boden gelte, soweit  als das Grundstück der Nutzung des Eigenheimes oder der Eigentumswohnung als Garten oder  Nebenfläche diene.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. August Häusele` | `Univ.-Prof. August Häusele` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Alessia Olschofski` | `Dr.in Alessia Olschofski` |

**Missed by this rule (FN):**

- `Natalie Gosebrink, Bakk. phil.` (person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich` (address)
- `50-818/5472` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130985.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in James Haemel  in der Beschwerdesache Marianne Rohweder,  Schlägl 1, 8092 Mettersdorf am Saßbach, Österreich, über die Beschwerde vom 30. Dezember 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 2. Dezember 2019 betreffend  Gebühren 2019 Steuernummer 81-888/5729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in James Haemel` | `Hon.-Prof.in James Haemel` |

**Missed by this rule (FN):**

- `Marianne Rohweder` (person)
- `Schlägl 1, 8092 Mettersdorf am Saßbach, Österreich` (address)
- `81-888/5729` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jeffrey Wengschick` | `Dr. Jeffrey Wengschick` |

**Missed by this rule (FN):**

- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Samantha Waitschull  in der Beschwerdesache Ramona Keklik,  Gafadura 6, 9620 Kraß, Österreich, vertreten durch PKF CENTURION Wirtschaftsprüfungs- gesellschaft mbH,  Hegelgasse 8, 1010 Wien, über die Beschwerden gegen die Bescheide des Zollamtes Eisenstadt  Flughafen Wien   1) vom 7. Februar 2018, Zl: a, betreffend Festsetzung der Mineralölsteuer für Jänner 2010 mit €  195.809,84 und Festsetzung des Säumniszuschlages mit € 3.916,20;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Samantha Waitschull` | `Univ.-Prof.in Samantha Waitschull` |

**Missed by this rule (FN):**

- `Ramona Keklik` (person)
- `Gafadura 6, 9620 Kraß, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/131148.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131148.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der  Verwaltungsstrafsache gegen Dr. Jasper Leo, Englham 23, 3804 Thaua, Österreich, über die Beschwerde vom 20.  November 2020, gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der  Stadt Wien, Magistratsabteilung 6, vom 09. November 2020, Zahl MA67/Zahl/2019, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 08. Mai 2019, Zahl MA67/Zahl/2019, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jasper Leo` | `Dr. Jasper Leo` |

**Missed by this rule (FN):**

- `Englham 23, 3804 Thaua, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Annemarie Wittjen` | `Hon.-Prof.in Annemarie Wittjen` |

**Missed by this rule (FN):**

- `Samuel Herpel` (person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich` (address)
- `39-702/2118` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Delia Wilmerdinger` | `Mag.a Delia Wilmerdinger` |

**Missed by this rule (FN):**

- `Kirsten Constantinescu` (person)
- `Höhenwald 50, 4822 Primesberg, Österreich` (address)
- `41-83-382/2498` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Priv.-Doz.in Nadine Schoormans,  Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des Finanzamtes XY  vom 10.2.2020 betreffend Festsetzung einer Zwangsstrafe zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Nadine Schoormans` | `Priv.-Doz.in Nadine Schoormans` |

**Missed by this rule (FN):**

- `Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich` (address)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Waldemar Zumloh` | `Dipl.-Ing. Waldemar Zumloh` |

**Missed by this rule (FN):**

- `Oberdorfer Weg 40, 4682 Brunau, Österreich` (address)
- `09-591/1655` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131451.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Margarete Ullbricht  in der Beschwerdesache Chen Egeli,  Rudolf-Henke-Straße 162, 4152 Leiten, Österreich, vertreten durch die Erwachsenenvertreterin RA, gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 23. Juli 2018, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016 und Anspruchszinsen 2015, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Margarete Ullbricht` | `Dr.in Margarete Ullbricht` |

**Missed by this rule (FN):**

- `Chen Egeli` (person)
- `Rudolf-Henke-Straße 162, 4152 Leiten, Österreich` (address)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom  29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer  ***, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Kronimus` | `Hon.-Prof.in Dominika Kronimus` |

**Missed by this rule (FN):**

- `Am Spitzteich 225, 5114 Göming, Österreich` (address)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_4`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, betreffend Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Einkommensteuer 2003 – 2010 und vom 29.4.2013 betreffend Einkommensteuer  2011, Steuernummer **, beschlossen:   Die Beschwerde vom 18. Mai 2013 wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Kronimus` | `Hon.-Prof.in Dominika Kronimus` |

**Missed by this rule (FN):**

- `Am Spitzteich 225, 5114 Göming, Österreich` (address)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_8`)


Im Zuge der Überprüfung eines Bescheides für Hon.-Prof.in Dominika Kronimus (in der Folge: Beschwerdeführerin:  Bf) im Jahr 2013 stellte das Finanzamt fest, dass bei den ESt-Veranlagungen (Einkünfte aus  Vermietung und Verpachtung) der streitanhängigen Jahre Daten von Lohnzetteln, welche von  der Pensionsversicherungsanstalt dem Finanzamt zur Sozialversicherungsnummer der Bf  elektronisch übermittelt worden waren, keine Berücksichtigung fanden.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Kronimus` | `Hon.-Prof.in Dominika Kronimus` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Gerald Erwin Ehgartner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zeno Matyssek`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128709.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache OMedR Hon.-Prof. Eduard Ranftel, Spiegelgrundstraße 100, 4920 Piereth, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

**False Positives:**

- `Dr. Ansgar Unterberger` — no gold match — likely missing annotation
- `Hon.-Prof. Eduard Ranftel` — partial — pred is substring of gold: `OMedR Hon.-Prof. Eduard Ranftel`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Hon.-Prof. Eduard Ranftel`(person)
- `Spiegelgrundstraße 100, 4920 Piereth, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128709.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128709.1_3`)


Begründung  Bisheriges Verfahren  Am 20.5.2015 erging der Einkommensteuerbescheid 2014 unter Anrechnung der Daten aus  dem Lohnzettel und der Pauschbeträge, sodass die Arbeitnehmerveranlagung für OMedR Hon.-Prof. Eduard Ranftel  (in der Folge: Bf) weder eine Abgabengutschrift noch eine Nachforderung ergab.

**False Positives:**

- `Hon.-Prof. Eduard Ranftel` — partial — pred is substring of gold: `OMedR Hon.-Prof. Eduard Ranftel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Hon.-Prof. Eduard Ranftel`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendy Scherl`(person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `53-864/4798`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `DDr.in Rafaela Ringart` — partial — pred is substring of gold: `Priv.-Doz.in DDr.in Rafaela Ringart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in DDr.in Rafaela Ringart`(person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich`(address)
- `Silvestri Bau GmbH`(organisation)
- `38-663/2876`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Mag. Erich Schwaiger` — no gold match — likely missing annotation
- `Dr. Gerlinde  Rieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Matthäus Domrös`(person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Alois Pichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nadja Rossetto`(person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich`(address)
- `85-716/2059`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Cornelia Pranckaitis, Petersbergweg 142, 4212 Steigersdorf, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

**False Positives:**

- `Mag. Marco Laudacher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cornelia Pranckaitis`(person)
- `Petersbergweg 142, 4212 Steigersdorf, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Monika Kofler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximilian Joobs`(person)
- `Forsthausweg 11, 3580 Poigen, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Dr. Peter Unger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oleg Kreissl`(person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Dr. Wolfgang Aigner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KzlR Adalbert Bürks`(person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Mag. Marco Laudacher` — no gold match — likely missing annotation
- `Mag. Susanne Haim` — no gold match — likely missing annotation
- `Dr.  Karl Penninger` — no gold match — likely missing annotation
- `Dipl.-Ing. Brunhild Fleischfresser` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

> overlaps gold: 1  |  likely missing annotation: 3

**Gold Entities:**

- `Ing. Dipl.-Ing. Brunhild Fleischfresser`(person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Mag. Marco Laudacher` — no gold match — likely missing annotation
- `ÖkR Horst Stevens` — partial — pred is substring of gold: `Ing. ÖkR Horst Stevens`
- `Mag. Manfred Frühwirth` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Thomas Leitner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof. Prof. Samir Burken, In Fängen 30, 4623 Wilhaming, Österreich, über die Beschwerde vom 27. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 23. Jänner 2020 betreffend Rückforderung von  Familienbeihilfe und Kinderabsetzbeträgen für das Kind x im Zeitraum vom 01.07.2018 bis zum  30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Samir Burken` — partial — pred is substring of gold: `Prof. Prof. Samir Burken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Prof. Samir Burken`(person)
- `In Fängen 30, 4623 Wilhaming, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Mag. Marco Laudacher` — no gold match — likely missing annotation
- `Dr. Andreas Weißenbäck` — partial — pred is substring of gold: `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129520.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129520.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Verwaltungsstrafsache  gegen Jeremias Kleegraefe, Sonnengasse 3, 3123 Heinigstetten, Österreich, über die Beschwerde des Beschuldigten vom 26. März 2020  gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 10. März 2020, Zahl:  MA67/196700631216/2019, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung bestätigt.

**False Positives:**

- `Dr. Peter Unger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kleegraefe`(person)
- `Sonnengasse 3, 3123 Heinigstetten, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Manuela Fischer` — no gold match — likely missing annotation
- `Mag. Walter Dienstl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Vivian Malek`(person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich`(address)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Ali Stasiak, Wurmbgasse 20, 4724 Königshub, Österreich, über die Beschwerde vom 24. Oktober 2019  gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 10. Oktober 2019  betreffend Abweisung des Antrags auf Familienbeihilfe für den Zeitraum März 2019 bis Mai  2019 sowie ab September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Helga Hochrieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR Ali Stasiak`(person)
- `Wurmbgasse 20, 4724 Königshub, Österreich`(address)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Rosalia Armbrost, Toulagasse 20, 8693 Mürzsteg, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 86-795/2631  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rosalia Armbrost`(person)
- `Toulagasse 20, 8693 Mürzsteg, Österreich`(address)
- `86-795/2631`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Rut Hus, LLM, Am Hirschfeld 23, 5232 Obermaisling, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 45-564/9779  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Dr. Michael Mandlmayr` — no gold match — likely missing annotation
- `Dr. Helmut Herbert Moritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Rut Hus, LLM`(person)
- `Am Hirschfeld 23, 5232 Obermaisling, Österreich`(address)
- `45-564/9779`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129861.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Univ.-Prof.in Lucia Crienitz  in der Beschwerdesache PhD Corbinian Perkins,  Ebersbergerstraße 13j, 4770 Hötzenedt, Österreich  vertreten durch RA MMag. Dr. Alexander Lamplmayr als gerichtlicher  Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der  beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt St. Johann Tamsweg Zell am See  betreffend die Anträge vom 3.5.2018 auf Zustellung  des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte  Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge  wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung,  Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung  bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum  unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung  hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe  von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen:  a)

**False Positives:**

- `Univ.-Prof.in Lucia Crienitz` — partial — pred is substring of gold: `Priv.-Doz.in Univ.-Prof.in Lucia Crienitz`
- `Dr. Alexander Lamplmayr` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Univ.-Prof.in Lucia Crienitz`(person)
- `PhD Corbinian Perkins`(person)
- `Ebersbergerstraße 13j, 4770 Hötzenedt, Österreich`(address)
- `Finanzamt St. Johann Tamsweg Zell am See`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129861.1_18`)


Das Finanzamt hat die säumigen Bescheide am 07.09.2020 (nämlich Abweisung des Antrages  auf Einstellung der Vollstreckung, Abweisung des Antrages auf Rückzahlung, Bescheid über die  Einschränkung der Vollstreckung, Bescheid betreffend Antrag auf Kontenschutz) erlassen und  dem Bundesfinanzgericht eine Abschrift übermittelt.  Darüber hinaus wurde der Bescheid – Verfügungsverbot am 03.08.2020 zu Handen des  nunmehr bestellten gerichtlichen Erwachsenenvertreters RA MMag. Dr. Alexander Lamplmayr  erlassen.

**False Positives:**

- `Dr. Alexander Lamplmayr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129872.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache Kevin Montag, Himmelreichgasse 2, 4694 Edt, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Wolfgang Freilinger` — no gold match — likely missing annotation
- `Mag. Gugenberger Barbara` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Kevin Montag`(person)
- `Himmelreichgasse 2, 4694 Edt, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129937.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129937.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Knut Nuh, Gosau 6, 9100 Oschenitzen, Österreich, vom 25. Juni 2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 28. Mai 2020, Zahl: MA67/Zahl, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Abweisung  I. Der Beschwerde wird teilweise Folge gegeben und die Entscheidung des Magistrats der Stadt  Wien in ihrem Ausspruch über die Strafe dahingehend abgeändert, dass die gemäß § 4 Abs. 1  Parkometergesetz 2006 verhängte Geldstrafe von € 140,00 auf € 90,00 und die gemäß § 16  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) verhängte Ersatzfreiheitsstrafe von 1 Tag 9 Stunden  auf 21 Stunden verringert werden.

**False Positives:**

- `Dr. Siegfried Fenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Knut Nuh`(person)
- `Gosau 6, 9100 Oschenitzen, Österreich`(address)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

**False Positives:**

- `Mag. Helga Hochrieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Felizitas Philippov`(person)
- `Hauser 155, 9422 Aich, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gerald Hellbing`(person)
- `Unterretzbach 125, 5092 Kirchental, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Maximiliane Aue, Sternenplatz 39, 4082 Aschach an der Donau, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Aue`(person)
- `Sternenplatz 39, 4082 Aschach an der Donau, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_349`)


Mit der Vertragserrichtung beauftragt wurde Rechtsanwalt StR Lukas Vielmäder, MBA Dieser gilt als  Parteienvertreter iSd § 30c Abs. 3 EStG 1988, welcher unter den genannten Voraussetzungen  für die richtige Berechnung der strittigen Steuer haftet.

**False Positives:**

- `StR Lukas Vielmäder` — partial — pred is substring of gold: `StR Lukas Vielmäder, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Lukas Vielmäder, MBA`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130450.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130450.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Cathleen Bürckmayer, Gindsweg 6, 9431 St. Stefan, Österreich,  über die Beschwerde vom 20. April 2018 gegen die Bescheide des Finanzamtes Klagenfurt, zu  Steuernummer 88-868/8570, vom 23. März 2018, mittels welchen der Antrag auf  Aufhebung der Einkommensteuerbescheide für 2015 und 2016 gemäß § 299 BAO abgewiesen  wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Helga Woschank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cathleen Bürckmayer`(person)
- `Gindsweg 6, 9431 St. Stefan, Österreich`(address)
- `88-868/8570`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Farina Nardello, Raning 1A, 4060 Leonding, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Andrea Müller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Farina Nardello`(person)
- `Raning 1A, 4060 Leonding, Österreich`(address)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

**False Positives:**

- `Dr. Hans Blasina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Annette Reeners`(person)
- `Räuflach 3, 8731 Schattenberg, Österreich`(address)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_1`)


BESCHLUSS   Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über den  Vorlageantrag vom 19. Dezember 2018 des Beschwerdeführers Diethard Uphof, Unterrotte 8, 3061 Unterwolfsbach, Österreich,  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten, 3100 St. Pölten, Daniel Gran-Straße 8,  vom 4. Mai 2018 betreffend Umsatzsteuer 2016:    I)

**False Positives:**

- `Mag. Günter Narat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Diethard Uphof`(person)
- `Unterrotte 8, 3061 Unterwolfsbach, Österreich`(address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig über die Beschwerde  des Melchior Bruckhoff, Kienmoserstraße 22, 3261 Thurhofglasen, Österreich, vom 1. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien vom 1. Juli 2020, GZ. MA67/GZ, betreffend Verwaltungsübertretung nach § 5  Abs. 2 (Wiener) Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien  Nr. 24/2012, den Beschluss gefasst:  Die Beschwerde vom 1. August 2020 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Mag. Karoline Windsteig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Melchior Bruckhoff`(person)
- `Kienmoserstraße 22, 3261 Thurhofglasen, Österreich`(address)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130673.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130673.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Verwaltungsstrafsache  gegen Quirin Suenderhauf, Wolfsegger Straße 8, 4632 Oberthambach, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idgF in Verbindung mit § 4  Abs. 1 Parkometergesetz 2006 gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006  LGBl. für Wien Nr. 9/2006 idgF, über die Beschwerde vom 18. September 2020 gegen das  Erkenntnis des Magistrates der Stadt Wien vom 7. September 2020, Zahl  MA67/206700473993/2020, beschlossen:  1.) Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  das Beschwerdeverfahren eingestellt.  2. Gemäß § 52 Abs. 1 VwGVG hat der Beschwerdeführer keinen Beitrag zu den Kosten des  Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Dr. Siegfried Fenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quirin Suenderhauf`(person)
- `Wolfsegger Straße 8, 4632 Oberthambach, Österreich`(address)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Vincent Allert, Marktlände 20, 5121 Ostermiething, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Wolfgang Aigner` — no gold match — likely missing annotation
- `Dr. Elke Hager` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Vincent Allert`(person)
- `Marktlände 20, 5121 Ostermiething, Österreich`(address)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Michael Mandlmayr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Klarissa Aßmus`(person)
- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich`(address)
- `52-573/0809`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Irene Kohler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Regina Vogt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Töws`(person)
- `Schießstatt 9, 5124 Weyer, Österreich`(address)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  2. [...], Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  3. [...]., Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Mag. Gerhard Groschedl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Rupert Karl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gudrun Sochurek`(person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich`(address)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Univ.-Prof. August Häusele, Schnitzlerweg 23, 3542 Gföhleramt, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Wolfgang Freilinger` — no gold match — likely missing annotation
- `Dr. Ulrich Weichselbaumer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Univ.-Prof. August Häusele`(person)
- `Schnitzlerweg 23, 3542 Gföhleramt, Österreich`(address)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Gerhard Groschedl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Peter Unger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130988.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130988.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Haussteinweg 12, 5272 Himmelschlag, Österreich, über die Beschwerde vom 26.2.2016 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 4. Februar 2016, Steuernummer  14-224/9307, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012 und 2013  und gegen den Bescheid vom 8.2.2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Ansgar Unterberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Haussteinweg 12, 5272 Himmelschlag, Österreich`(address)
- `14-224/9307`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Stefan Pipal` — no gold match — likely missing annotation
- `Kff. Cäcilia Wlcek` — partial — pred is substring of gold: `Dipl. Kff. Cäcilia Wlcek`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl. Kff. Cäcilia Wlcek`(person)
- `Rambergweg 3, 4950 Weidenthal, Österreich`(address)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

**False Positives:**

- `Dr. Karl Renner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131064.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Harald Demers, Empergergasse 96, 4072 Großhart, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 98-121/1048  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Susanne Haim` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Harald Demers`(person)
- `Empergergasse 96, 4072 Großhart, Österreich`(address)
- `98-121/1048`(tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Astrid Binder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Valerie Süssmeier`(person)
- `Ögglweg 86, 8623 Tutschach, Österreich`(address)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131148.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131148.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der  Verwaltungsstrafsache gegen Dr. Jasper Leo, Englham 23, 3804 Thaua, Österreich, über die Beschwerde vom 20.  November 2020, gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der  Stadt Wien, Magistratsabteilung 6, vom 09. November 2020, Zahl MA67/Zahl/2019, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 08. Mai 2019, Zahl MA67/Zahl/2019, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Krafft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Jasper Leo`(person)
- `Englham 23, 3804 Thaua, Österreich`(address)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Dragan Höh` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`
- `Mag.a Catharina Schmalenstrot` — partial — pred is substring of gold: `ÖkR Mag.a Catharina Schmalenstrot`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

**False Positives:**

- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Annemarie Wittjen`(person)
- `Samuel Herpel`(person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich`(address)
- `39-702/2118`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Josef Zwilling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tiffany Kleiß`(person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich`(address)
- `79-412/0834`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131361.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Ewald Eylers, Leydoltgasse 3T, 4671 Schörgendorf, Österreich, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, MA 67, als Abgabenstrafbehörde vom 20. März 2020, MA67/GZ, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

**False Positives:**

- `Mag. Andreas Stanek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ewald Eylers`(person)
- `Leydoltgasse 3T, 4671 Schörgendorf, Österreich`(address)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Dr. Siegfried Fenz` — no gold match — likely missing annotation
- `Dr. Viktor Frankl` — partial — pred is substring of gold: `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `Dr. Norbert Zöls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendy Schärff`(person)
- `Krainberg 12, 4633 Weilbach, Österreich`(address)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Michael Mandlmayr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Waldemar Zumloh`(person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich`(address)
- `09-591/1655`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache Dr.in OMedR Daria Salius, Kremsegger Straße 13, 3664 Oed, Österreich, über die Beschwerden vom 16. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding Finanzamtes Österreich vom 21. August  2015 betreffend Einkommensteuer 2009, 2010, 2011, 2012, 2013 und 2014, Steuernummer  61-570/3252, zu Recht erkannt:   Den Beschwerden gegen die Einkommensteuerbescheide für 2009, 2010, 2011, 2012 und 2013  wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Wolfgang Freilinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in OMedR Daria Salius`(person)
- `Kremsegger Straße 13, 3664 Oed, Österreich`(address)
- `61-570/3252`(tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom  29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer  ***, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Ansgar Unterberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Dominika Kronimus`(person)
- `Am Spitzteich 225, 5114 Göming, Österreich`(address)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_4`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, betreffend Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Einkommensteuer 2003 – 2010 und vom 29.4.2013 betreffend Einkommensteuer  2011, Steuernummer **, beschlossen:   Die Beschwerde vom 18. Mai 2013 wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `Dr. Ansgar Unterberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Dominika Kronimus`(person)
- `Am Spitzteich 225, 5114 Göming, Österreich`(address)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Selma Papenmeyer, Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Mag. Helga Hochrieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Selma Papenmeyer`(person)
- `Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich`(address)

</details>

---

## `names_after_omedr` 💣

**F1:** 0.003 | **Precision:** 0.273 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `6f446f08`  
**Description:**
Captures full title 'OMedR' followed by the full name.

**Content:**
```
OMedR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.273 | 0.002 | 0.003 | 11 | 3 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 8 | 1842 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache OMedR Lewis Scherrieb, Brunnhäuserweg 22R, 6080 Vill, Österreich, über die Beschwerde vom 19. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Familienbeihilfe 06.2015-02.2018, Steuernummer  30-264/4672, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Lewis Scherrieb` | `OMedR Lewis Scherrieb` |

**Missed by this rule (FN):**

- `Brunnhäuserweg 22R, 6080 Vill, Österreich` (address)
- `30-264/4672` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/147237.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147237.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Edith Stefan in der Beschwerdesache  OMedR Vitus Janne, Zwischenbrücken 2, 9361 Leimersberg, Österreich, gegen den Bescheid des Finanzamtes Österreich betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für das Jahr 2020,  Steuernummer 34-245/1093, beschlossen:  I. Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.     Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  II. Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `OMedR Vitus Janne` | `OMedR Vitus Janne` |

**Missed by this rule (FN):**

- `Zwischenbrücken 2, 9361 Leimersberg, Österreich` (address)
- `34-245/1093` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/147237.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147237.1_2`)


Begründung  Verfahrensgang:  Mit Bescheid vom 29. April 2021 wurde die Einkommensteuer für das Jahr 2020 betreffend  Herrn OMedR Vitus Janne (Beschwerdeführer, Bf) unter Ansatz von Pensionseinkünften und Einkünften  aus Kapitalvermögen mit € 2.543,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `OMedR Vitus Janne` | `OMedR Vitus Janne` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Rohlfsen  in der Beschwerdesache des  OStR OMedR Gernot Regensburger, Ort im Innkreis 35, 8462 Steinbach, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamt Niederösterreich Mitte  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `OMedR Gernot Regensburger` — partial — pred is substring of gold: `OStR OMedR Gernot Regensburger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ute Rohlfsen`(person)
- `OStR OMedR Gernot Regensburger`(person)
- `Ort im Innkreis 35, 8462 Steinbach, Österreich`(address)
- `Finanzamt Niederösterreich Mitte`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache Dr.in OMedR Daria Salius, Kremsegger Straße 13, 3664 Oed, Österreich, über die Beschwerden vom 16. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding Finanzamtes Österreich vom 21. August  2015 betreffend Einkommensteuer 2009, 2010, 2011, 2012, 2013 und 2014, Steuernummer  61-570/3252, zu Recht erkannt:   Den Beschwerden gegen die Einkommensteuerbescheide für 2009, 2010, 2011, 2012 und 2013  wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `OMedR Daria Salius` — partial — pred is substring of gold: `Dr.in OMedR Daria Salius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in OMedR Daria Salius`(person)
- `Kremsegger Straße 13, 3664 Oed, Österreich`(address)
- `61-570/3252`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_63`)


Mutter der beiden unterhaltspflichtigen Kinder K1 und K2 : Hiermit erkläre ich, dass mein  Exmann Dr.in OMedR Daria Salius  zu allen o.g.

**False Positives:**

- `OMedR Daria Salius` — partial — pred is substring of gold: `Dr.in OMedR Daria Salius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in OMedR Daria Salius`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RgR OMedR Miklos Pellegrin, Ostendeweg 9, 9981 Glor-Berg, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 73-541/6746, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OMedR Miklos Pellegrin` — partial — pred is substring of gold: `RgR OMedR Miklos Pellegrin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR OMedR Miklos Pellegrin`(person)
- `Ostendeweg 9, 9981 Glor-Berg, Österreich`(address)
- `73-541/6746`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 26.11.2013 wurde RgR OMedR Miklos Pellegrin (in der Folge: Beschwerdeführer: Bf) als  Haftungspflichtiger gemäß §§ 9 und 80 BAO ua für die aushaftende Abgabenschuldigkeit  Umsatzsteuer 2008 (€ 81.267,93) der GmbH (in der Folge: GmbH) zur Haftung herangezogen.

**False Positives:**

- `OMedR Miklos Pellegrin` — partial — pred is substring of gold: `RgR OMedR Miklos Pellegrin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR OMedR Miklos Pellegrin`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/138255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138255.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Edgar Nedler  in der Beschwerdesache RgR OMedR Susanne Rosenkranz,  Schlitpacherstraße 8, 4134 Berg bei Mairing, Österreich, vertreten durch Stögerer Preisinger Rechtsanwälte OG, Mariahilfer Straße  76/2/23, 1070 Wien, über die Beschwerde vom 27. Juli 2020 gegen den Bescheid des Zollamtes  Klagenfurt Villach vom 21. Juli 2020, GZ. 420000/202748/1/2020, betreffend  Beschwerdezinsen zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OMedR Susanne Rosenkranz` — partial — pred is substring of gold: `RgR OMedR Susanne Rosenkranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Edgar Nedler`(person)
- `RgR OMedR Susanne Rosenkranz`(person)
- `Schlitpacherstraße 8, 4134 Berg bei Mairing, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/138489.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138489.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Edith Westerhellweg  in der Beschwerdesache Dorothea Claße,  Pinskerweg 1, 8232 Untersafen, Österreich, vertreten durch KzlR OMedR Jasmin Nöthlich, über die Beschwerde vom 23. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 19. Mai 2022, mit dem der Antrag vom 9. Mai 2022  auf Aufhebung des Bescheides über die Festsetzung eines Säumniszuschlages abgewiesen  wurde, Steuernummer 53-981/6586, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OMedR Jasmin Nöthlich` — partial — pred is substring of gold: `KzlR OMedR Jasmin Nöthlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Edith Westerhellweg`(person)
- `Dorothea Claße`(person)
- `Pinskerweg 1, 8232 Untersafen, Österreich`(address)
- `KzlR OMedR Jasmin Nöthlich`(person)
- `53-981/6586`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/149675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149675.1_46`)


Das Fahrzeug ist von der OMedR Naomi Nix  Die Firma war bis vor 4 Monaten noch an der Anschrift AdrFirma1 gemeldet.

**False Positives:**

- `OMedR Naomi Nix  Die Firma` — partial — gold is substring of pred: `OMedR Naomi Nix`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Naomi Nix`(person)

</details>

---

## `names_after_fa_context` 

**F1:** 0.001 | **Precision:** 0.143 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `38a71026`  
**Description:**
Captures person names appearing after 'Fa.' (Firma) or 'Fa' (Company) abbreviation, which often precedes a person's name in legal texts referring to a sole proprietorship or similar.

**Content:**
```
(?:Fa\.|Fa)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.001 | 0.001 | 7 | 1 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 6 | 1484 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135320.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135320.1_40`)


Der angefochtene „Zurückweisungsbescheid“ vom 07.09.2021 enthält in seinem Spruch als  Bescheidadressaten die „Fa. Dagmar Astel“.

| Predicted | Gold |
|---|---|
| `Dagmar Astel` | `Dagmar Astel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_89`)


Tatsache ist, dass es sich bei den Rechnungen um Leistungen bzw.  Ausgaben der Fa. Beschwerdeführer GmbH. handelt. Es besteht daher wie von der  Finanzbehörde normaler weise bezeichnet ein Mängel, da KEG statt GmbH steht, aber sicher  keine verdeckte Gewinnausschüttung.

**False Positives:**

- `Beschwerdeführer Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_92`)


In der Praxis kommt dies  unentwegt vor und wird üblicher weise wie auch bei der Fa. Beschwerdeführer GmbH  ausgebucht.

**False Positives:**

- `Beschwerdeführer Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_98`)


Bei der Fa. Z- Bau Bau GmbH, kann dies sicher auch der damalige Auftraggeber der Bauvorhaben I-Straße,  9998 Wien und F-Gasse, 9997 Wien, die Fa. Zimmerei Groschang Holz GmbH  bestätigen.

**False Positives:**

- `Zimmerei Groschang Holz Gmb` — positional overlap with gold: `Groschang Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Groschang Holz GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_383`)


Feststellbar ist in den vorliegenden Erlöskonten der Synkel-Versicherung GmbH allerdings, dass die Synkel-Versicherung GmbH von  Febr. – Dez 2008 laufend Bauleistungen für eine Fa ABC erbrachte und vereinzelt auch im  Jahr 2009 für dieses Unternehmen tätig war (lt. Rechtsmittel Fa Zimmerei Groschang Holz GmbH (nachfolgend Groschang Holz GmbH.  1.2.

**False Positives:**

- `Zimmerei Groschang Holz Gmb` — positional overlap with gold: `Groschang Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Groschang Holz GmbH`(organisation)
- `Groschang Holz GmbH.`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_8`)


22.901,00 fest  und begründete, dass das Betriebsausgabenpauschale von 6% gemäß § 17 Abs. 1 EStG 1988 für  die Einkünfte des Bf aus selbstständiger Tätigkeit als Gesellschaftsgeschäftsführer der Fa.  Weierstrass Textil (im Folgenden GmbH-Gesellschaft) abweichend von der  1 von 16 Seite 2 von 16

**False Positives:**

- `Weierstrass Textil` — type mismatch — same span as gold: `Weierstrass Textil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weierstrass Textil`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_137`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf übte im Jahr 2014 eine Geschäftsführertätigkeit gemäß § 22 Z. 2 zweiter Teilstrich EStG  1988 (mit einer Gesellschaftsbeteiligung vom 55%) für die Fa. Weierstrass Textil  aus und erzielte  damit (unstrittig) Einkünfte aus selbstständiger Arbeit iHv. EUR. 60.000,00.

**False Positives:**

- `Weierstrass Textil` — type mismatch — same span as gold: `Weierstrass Textil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weierstrass Textil`(organisation)

</details>

---

## `names_after_sachbearbeiter` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `05826052`  
**Description:**
Captures names following 'Sachbearbeiter' or 'Sachbearbeiterin' which often precede a person's name in administrative contexts.

**Content:**
```
(?:Sachbearbeiter|Sachbearbeiterin)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

</details>

---

