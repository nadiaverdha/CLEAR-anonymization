# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-17T03:30:42.665103

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-16_v12/config.yaml 
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
| Accuracy (exact match) | 98.3% |
| True Positives | 842 |
| False Positives | 419 |
| False Negatives | 1009 |
| Total Gold Entities | 1851 |
| Micro Precision | 66.8% |
| Micro Recall | 45.5% |
| Micro F1 | 54.1% |
| Macro F1 | 54.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Legal_Context_Party_Person` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Party_Name_Beschwerdesache_Enhanced` | 19.0% | 95.1% | 10.5% | 205 | 195 | 10 |
| `Title_Priv_DoZ_in_Person_Enhanced` | 1.8% | 94.4% | 0.9% | 18 | 17 | 1 |
| `Honorific_Herr_Frau` | 10.2% | 91.7% | 5.4% | 109 | 100 | 9 |
| `Specific_Name_Dok2_Fixed` | 1.0% | 90.0% | 0.5% | 10 | 9 | 1 |
| `Title_Univ_Prof_Person_Enhanced_Corrected` | 2.6% | 88.9% | 1.3% | 27 | 24 | 3 |
| `Title_Hon_Prof_in_Person` | 1.7% | 84.2% | 0.9% | 19 | 16 | 3 |
| `Compound_Title_Person` | 36.8% | 77.1% | 24.1% | 580 | 447 | 133 |
| `Title_MedR_Person_Enhanced` | 0.4% | 66.7% | 0.2% | 6 | 4 | 2 |
| `Herrn_Name_Context` | 0.3% | 50.0% | 0.2% | 6 | 3 | 3 |
| `Standalone_Name_Professional_Context_Enhanced` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Title_Mag_a_Person_Enhanced` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Single_Letter_Name_Context_Enhanced_7` | 0.3% | 42.9% | 0.2% | 7 | 3 | 4 |
| `Title_OMedR_Person` | 0.2% | 40.0% | 0.1% | 5 | 2 | 3 |
| `Standalone_Name_Role_Context_Enhanced` | 0.4% | 40.0% | 0.2% | 10 | 4 | 6 |
| `Party_Name_NoTitle_Context_Enhanced_2` | 0.2% | 40.0% | 0.1% | 5 | 2 | 3 |
| `Standalone_Name_Verb_Context_Enhanced_2` | 0.5% | 25.0% | 0.3% | 20 | 5 | 15 |
| `VetR_Title_Person` | 0.1% | 16.7% | 0.1% | 6 | 1 | 5 |
| `Standalone_Name_Rs_Context` | 0.1% | 4.2% | 0.1% | 24 | 1 | 23 |
| `Single_Letter_Name_Context_Enhanced_2` | 0.3% | 3.4% | 0.2% | 89 | 3 | 86 |
| `Standalone_Name_Verb_Context_Enhanced` | 0.1% | 1.8% | 0.1% | 55 | 1 | 54 |
| `Academic_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal_Context_Representative_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag_a_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quote_Name_Context` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Party_Name_NoTitle_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Professional_Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Single_Letter_Name_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `StR_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quote_Name_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_KommR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_StR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Following_Role` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Standalone_Name_Verb_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR_Title_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Ebenho_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HR_OStR_Context_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Abbreviation_Person_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_ProfStR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herrn_Name_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Single_Letter_Name_Context_Enhanced_4` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `Role_Indicator_Person_NoTitle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OSR_KommR_Context_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_KommR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_OMedR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Verb_Context_Enhanced_3` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Multi_Initial_Person_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context_Enhanced_5` | 0.0% | 0.0% | 0.0% | 31 | 0 | 31 |
| `Single_Letter_Name_Context_Enhanced_6` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Mag_a_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_MMag_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Hon_Prof_Compound_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Univ_Prof_Person` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Title_PhD_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Name_NoTitle_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Fr_PhD_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_OkR_DiplIng_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal_Context_Representative_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Professional_Context_Enhanced_2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herrn_Name_Context_Enhanced_2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Legal_Context_Party_Person` 

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `5672565d`  
**Description:**
Matches party names in 'in der Beschwerdesache' context, capturing full names (first + last) even without titles, stopping before addresses.

**Content:**
```
(?:in der Beschwerdesache|Beschwerdesachen)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)+)\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 0 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Grothmann` | `Jaden Grothmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Massimo Friedhoff` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Yussuf Klingler  in der Beschwerdesache Volkmar Kircher vertreten  durch StB über die Beschwerde vom 18. Juli 2023 gegen die Bescheide des FA Braunau Ried Schärding  vom  27. Juni 2023 betreffend Feststellungstellungsbescheid Gruppenträger für die Jahre von 2018  bis 2020, Steuernummer 08-081/0335  zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Volkmar Kircher` | `Volkmar Kircher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Yussuf Klingler` (person)
- `FA Braunau Ried Schärding` (organisation)
- `08-081/0335` (tax_number)

</details>

---

## `Party_Name_Beschwerdesache_Enhanced` 🏆

**F1:** 0.190 | **Precision:** 0.951 | **Recall:** 0.105  

**Format:** `regex`  
**Rule ID:** `3d98b8f8`  
**Description:**
Matches party names in 'Beschwerdesache' context, ensuring at least two words are captured to avoid partial matches and stop before addresses.

**Content:**
```
(?:in der Beschwerdesache|Beschwerdesachen)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)\b(?=,|[:;]|$|[0-9])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.951 | 0.105 | 0.190 | 205 | 195 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 195 | 10 | 1656 |

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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

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

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Seipold` | `Marlies Seipold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Rebecca Hüllhorst,  Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich, über die Beschwerde vom 8. Juli 2021 gegen den Abweisungsbescheid des  Finanzamtes Österreich vom 25. Juni 2021 betreffend Familienbeihilfe für das Kind To für den  Zeitraum Februar 2020 bis Februar 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rebecca Hüllhorst` | `Rebecca Hüllhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Bianca Kristeller, Schröckbach 58, 9652 Nostra, Österreich, über die Beschwerde vom 9. Dezember 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2021 betreffend Familienbeihilfe 10.2020-09.2021  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bianca Kristeller` | `Bianca Kristeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schröckbach 58, 9652 Nostra, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/138313.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138313.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Christine Gäbelt  in der Beschwerdesache Verena Piechura,  Nußöd 5, 2014 Breitenwaida, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Juni 2022, Ordnungsbegriff Nr1, betreffend die Rückforderung zu Unrecht  bezogener Beträge   1. an Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum Oktober 2021 bis        Juni 2022 für den Sohn B  2.

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Christine Gäbelt` (person)
- `Nußöd 5, 2014 Breitenwaida, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/138725.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138725.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138952.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rebecca Altemüller  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Theodor Strohmeier` | `Theodor Strohmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Rebecca Altemüller` (person)
- `Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/139554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139554.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Reneé Stienen, Gmundnerberg 16, 4203 Oberwinkl, Österreich, vertreten durch Schmidt & Schmidt KG, Bahnzeile 10, 2130 Mistelbach, über die  Beschwerde vom 5. März 2019 gegen den Bescheid des Finanzamtes Gänserndorf Mistelbach  vom 30. Jänner 2019 betreffend Einkommensteuer 2017, Steuernummer 25-901/2438, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Reneé Stienen` | `Reneé Stienen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gmundnerberg 16, 4203 Oberwinkl, Österreich` (address)
- `Schmidt & Schmidt KG` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `25-901/2438` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Waldemar Kosiol,  Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich, über die Beschwerde vom 10. Juli 2014 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 7. Juli 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012  Steuernummer 47-100/4541, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waldemar Kosiol` | `Waldemar Kosiol` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)
- `47-100/4541` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/140391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140391.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ali Brücklmayer  in der Beschwerdesache Ulrike Kudlacek,  Nörsach 15, 4223 Standorf, Österreich, vertreten durch Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH,  Wagnastraße 1, 8430 Leibnitz, über die Beschwerde vom 31. Oktober 2019 gegen den Bescheid  des Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 2. Oktober 2019 betreffend  Aufhebung § 299 BAO /  ESt 2015 Steuernummer 26-799/5403  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ulrike Kudlacek` | `Ulrike Kudlacek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Ali Brücklmayer` (person)
- `Nörsach 15, 4223 Standorf, Österreich` (address)
- `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `26-799/5403` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/140642.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140642.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Emanuel Gentner  in der Beschwerdesache Alva Selmayr,  Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich, vertreten durch at reutte Steuerberatungs GmbH, Unterdorf 1, 6600  Lechaschau, gegen den von der belangten Behörde Finanzamt Österreich am 30. September  2022 zu Steuernummer 35-106/4702  ausgefertigten Einkommensteuerbescheid 2019 zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Alva Selmayr` | `Alva Selmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Emanuel Gentner` (person)
- `Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich` (address)
- `at reutte Steuerberatungs GmbH` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-106/4702` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


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

</details>

---

## `Title_Priv_DoZ_in_Person_Enhanced` 🏆

**F1:** 0.018 | **Precision:** 0.944 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `27b0cca0`  
**Description:**
Matches persons with 'Priv.-Doz.in' title, capturing FULL text including title.

**Content:**
```
\bPriv\.-Doz\.in(?:\s+Hon\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.944 | 0.009 | 0.018 | 18 | 17 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 17 | 1 | 1834 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137039.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137039.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Susanne Rohrauer  in der Beschwerdesache der  StadtHandel Planung, Sebastianplatz 18, 3441 Dietersdorf, Österreich  vertreten durch StB, über die Beschwerde vom 7. April 2021 gegen  den Bescheid des FA Salzburg-Stadt  vom 25. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Steuernummer 89-257/7642  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Susanne Rohrauer` | `Priv.-Doz.in Susanne Rohrauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StadtHandel Planung` (organisation)
- `Sebastianplatz 18, 3441 Dietersdorf, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `89-257/7642` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138500.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138500.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Gertrude Kreutl  über die Beschwerden der  Caroline Hesselmann, Mondseeberg 30, 8413 Haslach an der Stiefing, Österreich, vertreten durch die Allgemeine Revisions- und Treuhandgesellschaft  m. b. H. Wirtschaftsprüfungs- und Steuerberatungsgesellschaft in Graz, Brückenkopfgasse 1,  8020 Graz, vom 09.04.2019 gegen die Bescheide des Finanzamtes Graz-Stadt vom 07.03.2019  betreffend Feststellung Gruppenträger 2016 sowie gegen die Bescheide des Finanzamtes Graz- Stadt vom 12.03.2019 betreffend Feststellung Gruppenträger 2014 und 2015 zu Recht erkannt:    Die Beschwerde gegen den Bescheid betreffend Feststellung Gruppenträger 2014 wird als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gertrude Kreutl` | `Priv.-Doz.in Gertrude Kreutl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Caroline Hesselmann` (person)
- `Mondseeberg 30, 8413 Haslach an der Stiefing, Österreich` (address)
- `Allgemeine Revisions- und Treuhandgesellschaft  m. b. H. Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Laetitia Weckerlin  in der Beschwerdesache Zdenko Graucop,  Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich, über die Beschwerde vom 25. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 10. Mai 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  Steuernummer 11-005/1241  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Laetitia Weckerlin` | `Priv.-Doz.in Laetitia Weckerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zdenko Graucop` (person)
- `Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `11-005/1241` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Deborah Stöbesand` | `Priv.-Doz.in Deborah Stöbesand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke` (person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich` (address)
- `FA Waldviertel` (organisation)
- `37-369/8758` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Kimberly Willomeit  in der Beschwerdesache des  Christoph Hermsen, Krehmen 64, 4760 Riedlhof, Österreich, über die Beschwerde vom 14. Juli 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 22. Juni 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  zu Steuernummer 53-856/2225  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Kimberly Willomeit` | `Priv.-Doz.in Kimberly Willomeit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christoph Hermsen` (person)
- `Krehmen 64, 4760 Riedlhof, Österreich` (address)
- `FA Gmunden Vöcklabruck` (organisation)
- `53-856/2225` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/142502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Gloria Rejngardt   in der Beschwerdesache des Estelle Klaffer, Moosscheibe 14, 4942 Außerguggenberg, Österreich,   betreffend den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. März 2020   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2019, Steuernummer  88-435/1011,   zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gloria Rejngardt` | `Priv.-Doz.in Gloria Rejngardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Estelle Klaffer` (person)
- `Moosscheibe 14, 4942 Außerguggenberg, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)
- `88-435/1011` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/143077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Hörth  in der Beschwerdesache  Erhard Goebel,  Hauning 24N, 8225 Köppelreith, Österreich  über die Beschwerde vom 6. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 1. März 2023 betreffend Abweisung eines Zahlungserleichterungsansuchens,  Steuernummer 59-827/7719  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Hörth` | `Priv.-Doz.in Alva Hörth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erhard Goebel` (person)
- `Hauning 24N, 8225 Köppelreith, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `59-827/7719` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Aurelia Frässdorf  in der Beschwerdesache Janet Giesendorf,  Am Teich 47z, 7322 Lackenbach, Österreich, über die Beschwerde vom 21. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 26. September 2023, Ordnungsbegriff Nr1, betreffend Abweisung  des Antrages auf den Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum April 2019 –  September 2022   zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Aurelia Frässdorf` | `Priv.-Doz.in Aurelia Frässdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janet Giesendorf` (person)
- `Am Teich 47z, 7322 Lackenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Daphne Cofalla  in der Beschwerdesache Xenia Rieffers, Bakk. techn.,  Almersberg 23, 5440 Voregg, Österreich, betreffend Beschwerde vom 16. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022   Steuernummer  *** beschlossen:     Die Parteien werden gemäß § 281a BAO formlos in Kenntnis gesetzt, dass nach Auffassung des  Bundesfinanzgerichts in Bezug auf die gegenständliche Beschwerde vom 16. Oktober 2023  gegen den Bescheid vom 6. September 2023 ein Vorlageantrag nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Daphne Cofalla` | `Priv.-Doz.in Daphne Cofalla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Xenia Rieffers, Bakk. techn.` (person)
- `Almersberg 23, 5440 Voregg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147165.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Priv.-Doz.in Antonia Ramdani  in der Beschwerdesache Hedwig Schadek,  Adelsdorf 68, 8755 Feistritzgraben, Österreich, vertreten durch RPW Tulln Steuerberatung GmbH, Franz-Schubert-Straße 8,  3430 Tulln/Donau, betreffend Beschwerde vom 3. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2024 betreffend Säumniszuschlag 2024, Steuernummer  95-051/7682, den Beschluss:  I. Der Vorlageantrag wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs. 4 lit. e BAO als  nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Antonia Ramdani` | `Priv.-Doz.in Antonia Ramdani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Schadek` (person)
- `Adelsdorf 68, 8755 Feistritzgraben, Österreich` (address)
- `RPW Tulln Steuerberatung GmbH,` (organisation)
- `Finanzamtes Österreich` (organisation)
- `95-051/7682` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147744.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147744.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Martha Swiatek  in der Beschwerdesache Roland Gelfuß,  Geyreggerweg 19, 9851 Lurnbichl, Österreich, über die Beschwerde vom 18. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2021 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten gemäß § 236 BAO betreffend Steuernummer 06-247/1161  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Martha Swiatek` | `Priv.-Doz.in Martha Swiatek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roland Gelfuß` (person)
- `Geyreggerweg 19, 9851 Lurnbichl, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `06-247/1161` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143138.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Priv.-Doz.in Li van Clev, Rabenfurter Straße 9, 4770 Schärdingerau, Österreich, über die Beschwerde vom 22. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv.-Doz.in Li` — partial — pred is substring of gold: `Priv.-Doz.in Li van Clev`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Priv.-Doz.in Li van Clev`(person)
- `Rabenfurter Straße 9, 4770 Schärdingerau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Honorific_Herr_Frau` 🏆

**F1:** 0.102 | **Precision:** 0.917 | **Recall:** 0.054  

**Format:** `regex`  
**Rule ID:** `295821c6`  
**Description:**
Matches persons preceded by 'Herr' or 'Frau', capturing ONLY the name part, excluding any subsequent titles (Mag, Dr, etc.) to avoid over-matching.

**Content:**
```
(?:Herr|Frau)\s+(?!.*(?:Mag\.|Dr\.|DDr\.|OStR|Priv\.-Doz\.|Univ\.-Prof|RA|Ing\.))([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.917 | 0.054 | 0.102 | 109 | 100 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 100 | 9 | 1751 |

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

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_84`)


Prima Abo 10,00  Gesamt 431,27  Arbeitsmittel:  1. 1. CD Herr Riese und sein Garten 21,00  5 von 26 Seite 6 von 26

| Predicted | Gold |
|---|---|
| `Riese` | `Riese` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)


Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr Russbüldt  geb. Herrgeb, AdrHerr, sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)


Die Auskunft könne Herr Russbüldt als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_36`)


In weiterer Folge wurde Herr Russbüldt von der Behörde angeschrieben und um Bekanntgabe des  Fahrzeuglenkers ersucht.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_40`)


In dem durch Ihren Rechtsvertreter dagegen erhobenen Einspruch wurde im Wesentlichen  eingewendet, dass Herr Russbüldt  geb. Herrgeb, AdrHerr der einzige und alleinige Verantwortliche  4 von 22 Seite 5 von 22

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_53`)


Dagegen erhoben Sie mit E-Mail vom 2) und 6) 31.08.2020, 3) und 4) 07.09.2020, 5) 04.09.2020  Einspruch und wiederholten, dass Herr Russbüldt der verantwortliche Fuhrparkleiter gewesen sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_58`)


Zum Beweis dafür wurde ein  Dokument vom 27.11.2018 vorgelegt, worin die Firmen Firma1 und Firma2 vereinbaren, dass Herr Russbüldt als Fuhrparkleiter für beide angeführten Firmen ab dem 01.12.2018 beauftragt wird.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_71`)


Aufgrund der Aktenlage ist daher davon auszugehen, dass Herr Russbüldt nicht verantwortlicher  Beauftragter gemäß § 9 Abs. 2 VStG ist.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_105`)


Darin hat der Beschwerdeführer dargelegt, dass der  Beschwerdeführer die verlangte Auskunft nicht erteilen kann, sondern Herr Russbüldt  geb. Herrgeb,  AdrHerr, Verantwortlicher gemäß § 9 VStG.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_110`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_169`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)


Herr Sahin konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

| Predicted | Gold |
|---|---|
| `Sahin` | `Sahin` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Roland Rößle` | `Roland Rößle` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_15`)


Im vorliegenden Fall hat jedoch nicht die Adressatin der verfahrensgegenständlichen  Vollstreckungsverfügung, nämlich Frau Waiser  sondern FirmaBfInhaberLautFirmenbuch,  Firmenbuchnummer FN im eigenen Namen Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung – direkt oder indirekt – von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt - von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_37`)


Im  Allgemeinen gibt Frau Reifgerste an, dass sich ihre Tochter überwiegend „falsch“ fühle und in sozialen  Situationen sich sehr verunsichert fühle, da sie nicht wisse wie sie sich verhalten solle.

| Predicted | Gold |
|---|---|
| `Reifgerste` | `Reifgerste` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl  MA67/Zahl/2022, wurde Herr Annette Preußing (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Annette Preußing` | `Annette Preußing` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

| Predicted | Gold |
|---|---|
| `Dagobert Duewel` | `Dagobert Duewel` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_165`)


In der Bestätigung der AG1 (Adr2) wurde durch den Geschäftsführer GF, bestätigt, dass Herr Luethgarth (geb. am Geb.) die Funktion eines Geschäftsführers in diesem Unternehmen innegehabt  habe.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_167`)


In der Bestätigung der AG2 (Adr3 / FN 1234) wurde durch den Geschäftsführer Gf2, bestätigt,  dass Herr Luethgarth (geb. am Geb.) als Geschäftsführer der AG2 tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Olivia Trienes` | `Olivia Trienes` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)


Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr Ballschmieder laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_13`)


Der Bf. brachte in seinem Einspruch vom 19. Juni 2023 (E-Mail) vor, dass er das Fahrzeug vor  dem Geburtshaus geparkt habe, da seine Frau Wehen gehabt habe.

| Predicted | Gold |
|---|---|
| `Wehen` | `Wehen` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_9`)


Am 16. Februar 2023 langte beim Magistrat per E-Mail ein als Einspruch gewertetes Schreiben  mit dem Betreff ‚Lenkererhebungen Kennz1, Leihvertrag Kennz1‘ ein, indem der  Beschwerdeführer sich bei Frau Reepschläger für das nette Telefonat bedankte, neben der  gegenständlichen Geschäftszahl zahlreiche weitere Geschäftszahlen anführte und als Lenker  Lenker1 (mit seinen persönlichen Daten) bekanntgab.

| Predicted | Gold |
|---|---|
| `Reepschläger` | `Reepschläger` |

**Missed by this rule (FN):**

- `Magistrat` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_42`)


Am 16. Februar 2023 langte beim Magistrat per E-Mail ein als Einspruch gegen die  Strafverfügung vom 12. Jänner 2023 gewertetes Schreiben mit dem Betreff ‚Lenkererhebungen  Kennz1, Leihvertrag Kennz1‘ ein, indem der Beschwerdeführer sich bei Frau Reepschläger für das nette  Telefonat bedankte, neben der nicht gegenständlichen Geschäftszahl MA67/Zahl4/2023 (die  vermutlich gemeinte Zahl lautet: MA67/Zahl3/2023) zahlreiche weitere Geschäftszahlen  anführte und als Lenker Lenker1 (mit seinen persönlichen Daten) bekanntgab.

| Predicted | Gold |
|---|---|
| `Reepschläger` | `Reepschläger` |

**Missed by this rule (FN):**

- `Magistrat` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/145368.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145368.1_34`)


Herr Gotthard Dinkelmann  hat in eigener Recherche noch herausgefunden, dass bei unbeschränkter  Schweizer Steuerpflicht nur ein sehr enger Kostenkatalog berücksichtigt werden könnte:  „Schuldzinsen, Beiträge in die Säule 2b und 3a, berufliche Weiterbildungskosten, bezahlte  Alimente, Unterstützungsbeiträge“ und bei beschränkter Steuerpflicht lediglich „Beiträge an  die Säule 2b und 3a sowie Wochenaufenthaltskosten“.

| Predicted | Gold |
|---|---|
| `Gotthard Dinkelmann` | `Gotthard Dinkelmann` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_726`)


In ihrer per Mail überreichten Vorhaltsbeantwortung vom 23. Mai 2024 (OZ. 111) nahm die  Bf. zu beiden Vorhalten (hg. GZ. RV/2100888/2022 vom 30. April 2024) und RV/2100046/2023  v. 23. April 2024) wie folgt Stellung:  „Sehr geehrter Herr Hartmut Berning   im Namen unseres o.a. Klienten und unter Berufung auf die uns erteilte Vollmacht können wir  zu Ihren Vorhalten vom 30.4.2024 (zugestellt am 6.5.2024) im Verfahren RV/2100888/2022  sowie vom 23.4.2024 (zugestellt am 26.4.2024) im Verfahren RV/2100046/2023 gerne wie  folgt Stellung nehmen:   1. Unternehmereigenschaft der Kunden   Wir haben von unserem Klienten keine weiteren Unterlagen betreffend die unternehmerischen  Leistungsempfänger erhalten, sodass wir keine weiterführenden Angaben zu diesen machen  können.

| Predicted | Gold |
|---|---|
| `Hartmut Berning` | `Hartmut Berning` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_13`)


Im Rahmen einer zweiten Stellungsuntersuchung vom  05.01.1989 wurde Herr Luna Fruechtenicht  als für den Präsenzdienst „untauglich“ eingestuft und dies  mit den festgestellten Diagnosen: Grand Mal Epilepsie, chronischer Alkoholabusus sowie  Oligrophenie begründet.

| Predicted | Gold |
|---|---|
| `Luna Fruechtenicht` | `Luna Fruechtenicht` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_7`)


In Beantwortung des Ergänzungsersuchens des Finanzamtes (siehe dazu Vorhalt vom  16.02.2024) teilte die Tochter der Bf,Frau Rittcher  dem Finanzamt daraufhin mit, dass sie einerseits  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamt` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_11`)


Dagegen erhob die Bf, vertreten durch Frau Rittcher  fristgerecht Beschwerde mit der Begründung,  dass W.B. die FB erhalten hätte und nicht die Bf (siehe dazu Beschwerdeschriftsatz vom  25.03.2024).

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_62`)


Durch den steuerlichen Vertreter wurde am 14.04.2015 im Rahmen einer Gebührenprüfung der  Beschluss des Stiftungsrates der XX Stiftung vom 10.10.2007 über die Vornahme einer  Ausschüttung in Höhe von € 240.000,- an Frau Klopstech beigebracht.

| Predicted | Gold |
|---|---|
| `Klopstech` | `Klopstech` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_105`)


Punkt 4   Weder Frau Heumann noch Herr Bf2 hätten jemals in diesem Gebäude gewohnt.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_109`)


Frau Heumann und Herr Bf2 würden seit Dezember 2020 (lt. Meldezettel 18.01.2021) in einer ca.  95m²-großen Wohnung in I 1, J wohnen, welche sich im Eigentum von Frau Heumann befinde.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_111`)


3 Parteien davon seien Mieter von Frau Heumann und die 4.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_112`)


Partei sei die mit einem  Wohnrecht ausgestattete Lebensgefährtin des verstorbenen Großvaters von Frau Heumann  welcher  ihr die Liegenschaft übergeben hätte.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_114`)


Davor hätte Frau Heumann und Herr Bf2 in den jeweiligen Elternhäusern gewohnt,Frau Heumann in K 1, L  und Herr Bf2 in Dorf.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_130`)


Frau Heumann und Herr Bf2 haben das Objekt erworben um damit ebenfalls Mieteinnahmen zu  erzielen – das Objekt also zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_155`)


Zahlreiche Anhaltspunkte weisen klar darauf hin, dass Frau Heumann und Herr Bf2 das Objekt  erworben haben, um es auch tatsächlich zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_158`)


Sie  wohnen seit Dezember 2020 in einer ca. 95m² großen Wohnung im Eigentum von Frau Heumann (siehe Übergabsvertrag).

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_4`)


Entscheidungsgründe  Mit Strafverfügung vom 1) 14.04.2025, GZ. MA67/GZ1/2025 und 2) 12.05.2025, GZ.  MA67/GZ2/2025, wurde Frau Langness für schuldig erkannt, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (Land) am

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_84`)


Nachdem im § 37 Abs. 5 Z 3 EStG keine zeitliche Frist normiert ist, stellt  die ungeplante Wideraufnahme der gerichtlichen Sachverständigentätigkeit keine schädliche  Erwerbstätigkeit dar.“   < Schreiben BG A vom 23.7.2019:  „Herr Beschwerdeführer hat die Austragung aus der Liste der Sachverständigen mit 30.6.2016  entsprechend an die Präsidentin des Landesgerichtes W kommuniziert.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Ministerialrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_30`)


Herr Gf ist darüber hinaus  alleiniger Gesellschafter-Geschäftsführer der Carrasco Software GmbH  der 100%-igen Muttergesellschaft der  Bf.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Carrasco Software GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_151`)


Der Steuerberater von Frau NN1 – Herr Kollege Z von der öStb-Kanzlei – ist cc. gesetzt.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_152`)


Herr Kollege Z und ich konnten uns heute abstimmen.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_155`)


Diesem Verzicht stimmt Herr Kollege Z in Vertretung von Frau  NN1 zu.  11 von 34 Seite 12 von 34

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

</details>

---

## `Specific_Name_Dok2_Fixed` 

**F1:** 0.010 | **Precision:** 0.900 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `355954b6`  
**Description:**
Matches 'Dr. [Letter][Digit]' patterns like 'Dr. Dok2' which were missed due to non-standard name format.

**Content:**
```
\bDr\.\s+[A-Z]\d+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.900 | 0.005 | 0.010 | 10 | 9 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 1 | 1842 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_19`)


Am 18.06.2012 habe der Augenarzt Dr.  A1, A-Stadt, (siehe Befund vom 15.03.2011, Untersuchung vom 21.12.2011 und 18.06.2012  (Befunde beiliegend) seiner Patientin Bf. mündlich erklärt, sie möge einen Augenfacharzt für  ihre Operation selbst aussuchen.

| Predicted | Gold |
|---|---|
| `Dr.  A1` | `Dr.  A1` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_20`)


Die Diagnose der Fachordination von Dr. A2 sei die gleiche  wie jene von Dr. A1 gewesen (Beilage).

| Predicted | Gold |
|---|---|
| `Dr. A2` | `Dr. A2` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_22`)


Nach Erlangung der Kenntnis von Laseroperationen in A-Stadt habe die Bf. Dr. A3 konsultiert,  welcher sich zur Durchführung einer Operation nach entsprechender Vorbereitung der  Patientin bereit erklärt habe.

| Predicted | Gold |
|---|---|
| `Dr. A3` | `Dr. A3` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_24`)


Nach der Kontrolluntersuchung durch Dr. A3 und dem Erhalt von Antibiotika sei der Bf. einige  Wochen später eine Gleitsichtbrille verschrieben worden, welche nach angekündigter  Gewöhnungszeit von einigen Wochen noch immer nicht für den Computer verwendbar  gewesen sei.

| Predicted | Gold |
|---|---|
| `Dr. A3` | `Dr. A3` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_25`)


Beim nächsten Kontrollbesuch bei Dr. A3 habe die Bf. erfahren, dass für diesen  Zweck eine Einfachbrille, zugerichtet auf den cm-Abstand vom Bildschirm zweckmäßiger sei.

| Predicted | Gold |
|---|---|
| `Dr. A3` | `Dr. A3` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_29`)


Seit der  Nachlaserung von Dr. A2 stehe die Bf. unter regelmäßiger Kontrolle bei Dr. A2.

| Predicted | Gold |
|---|---|
| `Dr. A2` | `Dr. A2` |
| `Dr. A2` | `Dr. A2` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_34`)


Mit dem Vorlageantrag wurde die Anerkennung von Kosten in Höhe von [Honorarnoten Dr. A3  (Facharzt für Augenheilkunde) + Brille =] 4.610,00 € als außergewöhnliche Belastung OHNE  Selbstbehalt bei der Einkommensteuer 2014 aufgrund einer vorliegenden Behinderung  beantragt.

| Predicted | Gold |
|---|---|
| `Dr. A3` | `Dr. A3` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_37`)


Daneben  stehe die Bf. in ständiger Überwachung der Klinik Dr. A2 in A-Stadt wegen einer erst  vorgenommenen Laseroperation beim zweiten Auge.

| Predicted | Gold |
|---|---|
| `Dr. A2` | `Dr. A2` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_20`)


Die Diagnose der Fachordination von Dr. A2 sei die gleiche  wie jene von Dr. A1 gewesen (Beilage).

**False Positives:**

- `Dr. A1` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. A2`(person)

</details>

---

## `Title_Univ_Prof_Person_Enhanced_Corrected` 🏆

**F1:** 0.026 | **Precision:** 0.889 | **Recall:** 0.013  

**Format:** `regex`  
**Rule ID:** `2fa998a7`  
**Description:**
Matches persons with 'Univ.-Prof.in' or similar titles, capturing FULL text including title and full name.

**Content:**
```
\b(?:Univ\.-Prof(?:\.in)?|Univ\.Prof(?:\.in)?)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.013 | 0.026 | 27 | 24 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 24 | 3 | 1827 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Penelope Splettstösser` | `Univ.-Prof.in Penelope Splettstösser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Schöbel` (person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-896/6207` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138513.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Univ.-Prof.in Verena Sobzig  über die Beschwerde des  Peter Scheidhauer, Klimaweg 103, 8232 Untersafen, Österreich, vom 31.05.2022 gegen den Bescheid des Finanzamtes Österreich vom  26.04.2022 betreffend Abweisung eines Antrages auf Nachsicht zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Verena Sobzig` | `Univ.-Prof.in Verena Sobzig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Peter Scheidhauer` (person)
- `Klimaweg 103, 8232 Untersafen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Christine Gäbelt  in der Beschwerdesache Verena Piechura,  Nußöd 5, 2014 Breitenwaida, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Juni 2022, Ordnungsbegriff Nr1, betreffend die Rückforderung zu Unrecht  bezogener Beträge   1. an Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum Oktober 2021 bis        Juni 2022 für den Sohn B  2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Christine Gäbelt` | `Univ.-Prof.in Christine Gäbelt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Verena Piechura` (person)
- `Nußöd 5, 2014 Breitenwaida, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paula Tschann  in der Beschwerdesache Merlin Dankwort,  Urtelgasse 9y, 8232 Stambach, Österreich  vertreten durch Valerian Stamataki, Schanze 29 12, 3661 Unterthalheim, Österreich, über die Beschwerde vom  6. September 2022 gegen den Bescheid des Finanzamtes Österreich vom 9. August 2022  betreffend Festsetzung eines ersten Säumniszuschlages, Steuernummer 88-049/5894  nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Paula Tschann` | `Univ.-Prof.in Paula Tschann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Dankwort` (person)
- `Urtelgasse 9y, 8232 Stambach, Österreich` (address)
- `Valerian Stamataki` (person)
- `Schanze 29 12, 3661 Unterthalheim, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-049/5894` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Denise Hatwiger  in der Beschwerdesache Svenja Gelonek,  Leutschacher Straße 37, 9344 Wullroß, Österreich, über die Beschwerden gegen die Bescheide des Finanzamt Oststeiermark (jetzt Finanzamt  Österreich) betreffend Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2013 bis  2017 sowie Anspruchszinsen 2014 und 2015, Steuernummer 46-265/1377, zu Recht erkannt:   I. Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Denise Hatwiger` | `Univ.-Prof.in Denise Hatwiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Gelonek` (person)
- `Leutschacher Straße 37, 9344 Wullroß, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt  Österreich` (organisation)
- `46-265/1377` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Gerda Höfelmair  in der Beschwerdesache des  Ingolf Hillbig, über die Beschwerde vom 11. Jänner 2023 gegen den Bescheid des FA Wien 2/20/21/22  vom  15. Dezember 2022 betreffend Einkommensteuer 2021 zu Steuernummer 92-987/6769  nach der  mündlichen Verhandlung am 5. September 2024 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Gerda Höfelmair` | `Univ.-Prof.in Gerda Höfelmair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingolf Hillbig` (person)
- `FA Wien 2/20/21/22` (organisation)
- `92-987/6769` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/145892.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145892.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karin Gebhardi  in der Beschwerdesache Gotthard Sträßner,  Schmidsdorf Straße 31, 3142 Gunnersdorf, Österreich, Ungarn, über die Beschwerde vom 4. Dezember 2017 gegen die Bescheide des  FA Spittal Villach (nunmehr Finanzamt Österreich) vom 10. November 2017, zu Steuernummer  09-485/6394, betreffend die Abweisung des Antrags vom 14. Oktober 2017 auf  Wiederaufnahme der Verfahren hinsichtlich Einkommensteuer 2014 und 2015 zu Recht  erkannt:   I. Die angefochtenen Bescheide vom 10. November 2017, mit denen der in eventu  eingebrachte Antrag auf Wiederaufnahme der Verfahren betreffend  Einkommensteuer 2014 und 2015 abgewiesen wurde, werden wegen  Unzuständigkeit aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Karin Gebhardi` | `Univ.-Prof.in Karin Gebhardi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gotthard Sträßner` (person)
- `Schmidsdorf Straße 31, 3142 Gunnersdorf, Österreich` (address)
- `FA Spittal Villach` (organisation)
- `Finanzamt Österreich` (organisation)
- `09-485/6394` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Maja Lauers` | `Univ.-Prof.in Maja Lauers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Mehmet Klasema` (person)
- `Labon 67, 4861 Looh, Österreich` (address)
- `Jonathan Goessl` (person)
- `Finanzamt Österreich` (organisation)
- `85-153/1153` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/147920.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Irmgard Rockner  in der Beschwerdesache Samuel Klimasz,  Lorbeerweg 6A, 2202 Enzersfeld im Weinviertel, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 24. April 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 Steuernummer 24-613/0227  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Irmgard Rockner` | `Univ.-Prof.in Irmgard Rockner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Klimasz` (person)
- `Lorbeerweg 6A, 2202 Enzersfeld im Weinviertel, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)
- `24-613/0227` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Garnschröder  in der Beschwerdesache  RgR Corbinian Baranowskij, Schwamingstraße 19, 5452 Reitsam, Österreich, über die Beschwerde vom 6. März 2025 gegen den Bescheid des  Finanzamtes Österreich vom 6. Februar 2025 betreffend Zwangsstrafen 2023 Steuernummer  15-984/7137  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die Zwangsstrafen mit  150,00 Euro für die Körperschaftssteuererklärung und mit 150,00 Euro für die  Umsatzsteuererklärung (insgesamt somit mit 300,00 Euro) festgesetzt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Leila Garnschröder` | `Univ.-Prof.in Leila Garnschröder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Corbinian Baranowskij` (person)
- `Schwamingstraße 19, 5452 Reitsam, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `15-984/7137` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch Mag. Benno Elmar Di Gaspero, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Paulina Borisowa` | `Univ.-Prof.in Paulina Borisowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ilhan Feldmeier, Bakk. rer. nat.` (person)
- `Sittenbergstraße 9, 4294 Stampfendorf, Österreich` (address)
- `Mag. Benno Elmar Di Gaspero` (person)
- `Finanzamtes  Österreich` (organisation)
- `14-548/3314` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shakira Unterbusch  in der Beschwerdesache Norbert Seybt,  Harzhausergasse 66, 8362 Ruppersdorf, Österreich, über die Beschwerde vom 12. November 2024 gegen den Bescheid des  Finanzamt Freistadt Rohrbach Urfahr  vom 11. November 2024 betreffend Abweisung des Antrags auf Familienbeihilfe für  den Zeitraum ab 11/2024 vom 30.10.2024, eingebracht am 30.10.2024, sowie gegen den  Bescheid des Finanzamtes Österreich betreffend Abweisung des Antrags auf Erhöhungsbetrag  wegen erheblicher Behinderung für den Zeitraum ab 11/2024 vom 31.10.2024, eingebracht am  31.10.2024, Steuernummer 22-872/9827, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shakira Unterbusch` | `Univ.-Prof.in Shakira Unterbusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Norbert Seybt` (person)
- `Harzhausergasse 66, 8362 Ruppersdorf, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `Finanzamtes Österreich` (organisation)
- `22-872/9827` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Marion Weßalowski` — partial — pred is substring of gold: `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski`(person)
- `OMedR Leonhard Hestermeyer`(person)
- `Sägerweg 5, 5450 Reitsam, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `52-932/8889`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof.in Ariadne Jurkait` — partial — pred is substring of gold: `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`(person)
- `Prof. Ing. Eduard Skroblies`(person)
- `Forchetweg 18, 4692 Albertsham, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Eva Gund` — partial — pred is substring of gold: `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

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

## `Title_Hon_Prof_in_Person` 🏆

**F1:** 0.017 | **Precision:** 0.842 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `359165c7`  
**Description:**
Matches persons with 'Hon.-Prof.in' or 'Hon.-Prof.' title, capturing FULL text including title.

**Content:**
```
\bHon\.-Prof(?:\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:\s*,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.842 | 0.009 | 0.017 | 19 | 16 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 16 | 3 | 1835 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Vanessa Nowikoff` | `Hon.-Prof.in Vanessa Nowikoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `KommR Lee Ponsard` (person)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Juhass` | `Hon.-Prof.in Dominika Juhass` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludmilla Hühnerfuß, Bakk. techn.` (person)
- `Singham 20, 3465 Unterstockstall, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Barbara Schwalb  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Barbara Schwalb` | `Hon.-Prof.in Barbara Schwalb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annalena Mlynarcik` (person)
- `Ledochowskastraße 5, 4040 Kammerschlag, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `09-012/5071` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/139502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ludmilla Achmiller   in der Beschwerdesache des Harald Köbbe, Hammerfeldstraße 64, 4707 Fürth, Österreich,  betreffend die Bescheide des FA Amstetten Melk Scheibbs  vom 24. September 2021  hinsichtlich Abweisung von Anträgen auf Wiederaufnahme § 303 BAO /  ESt 2018 und ESt 2019  Steuernummer, 50-782/0766,   zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ludmilla Achmiller` | `Hon.-Prof.in Ludmilla Achmiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Köbbe` (person)
- `Hammerfeldstraße 64, 4707 Fürth, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `50-782/0766` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rebecca Altemüller  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Rebecca Altemüller` | `Hon.-Prof.in Rebecca Altemüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theodor Strohmeier` (person)
- `Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/139968.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139968.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Marianne Oberscheidt  in der Beschwerdesache Dipl. Kff. Aurelia Riem,  Sappl - Keuschpeter 68, 5233 Irnstötten, Österreich  über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid des  Finanzamtes Bruck Eisenstadt Oberwart vom 29. November 2019 betreffend Abweisung des  Antrags vom 5. März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages  ohne Vornahme einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG  1967), SV-Nr. Nr., zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Marianne Oberscheidt` | `Hon.-Prof.in Marianne Oberscheidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Aurelia Riem` (person)
- `Sappl - Keuschpeter 68, 5233 Irnstötten, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Chiara Wälte  in der Beschwerdesache Dagobert Duewel,  Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich, über die Beschwerde vom 18. Oktober 2022 gegen die Bescheide des  Finanzamtes Österreich vom 12. September 2022, Ordnungsbegriff Nr1, betreffend Abweisung  der Anträge auf Familienbeihilfe und Erhöhungsbetrag für den Zeitraum ab Juni 2022 zu Recht  erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Chiara Wälte` | `Hon.-Prof.in Chiara Wälte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagobert Duewel` (person)
- `Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/141142.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Felizia Marschinke  in der Beschwerdesache Sven Hoepfl,  Kelterweg 7, 8382 Mogersdorf, Österreich, über die Beschwerde vom 25. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 22. Juli 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  Steuernummer 12-858/0237  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Felizia Marschinke` | `Hon.-Prof.in Felizia Marschinke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Hoepfl` (person)
- `Kelterweg 7, 8382 Mogersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `12-858/0237` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Svenja Kieble  in der Beschwerdesache Vera Henssel, Bakk. rer. nat.,  Lärchenhofweg 43, 4073 Dörnbach, Österreich, über die Beschwerde vom 3. März 2022 gegen die Bescheide des Finanzamtes  Österreich vom 7. Februar 2022, Ordnungsbegriff Nr1, betreffend Abweisung der Anträge auf  Familienbeihilfe und Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung für  den Zeitraum ab August 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Svenja Kieble` | `Hon.-Prof.in Svenja Kieble` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Henssel, Bakk. rer. nat.` (person)
- `Lärchenhofweg 43, 4073 Dörnbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Geraldine Matuschefski  in der Beschwerdesache der Demircan Metall AG&  atypisch stille Gesellschaft, vertreten durch xx Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen  1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Geraldine Matuschefski` | `Hon.-Prof.in Geraldine Matuschefski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Demircan Metall AG` (organisation)
- `xx Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Juliette Burgmann  in der Beschwerdesache Ibrahim Hofler,  Sennstraße 7, 4084 Scharzeredt, Österreich, betreffend Beschwerde vom 23. August 2021 gegen den Bescheid des  Finanzamtes Österreich vom 4. August 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 26-497/2277  beschlossen:  Der eingebrachte Vorlageantrag vom 5. Mai 2022 wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Juliette Burgmann` | `Hon.-Prof.in Juliette Burgmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibrahim Hofler` (person)
- `Sennstraße 7, 4084 Scharzeredt, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `26-497/2277` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ruperta Wengrzinek  in der Beschwerdesache Ali Oberste,  Wolfsedt 11, 4211 Lindach, Österreich, Steuernummer 03-949/9780  über die Beschwerde vom 7. August 2019  gegen den Bescheid des Finanzamtes Feldkirch vom 30. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ruperta Wengrzinek` | `Hon.-Prof.in Ruperta Wengrzinek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ali Oberste` (person)
- `Wolfsedt 11, 4211 Lindach, Österreich` (address)
- `03-949/9780` (tax_number)
- `Finanzamtes Feldkirch` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146422.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Elmira Walkenbach  in der Beschwerdesache der  JLFT Robotik, Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich, über die am 8.August 2023 eingebrachte Beschwerde gegen den  zur Steuernummer 38-455/9315  ergangenen Bescheid des FA Innsbruck  vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Elmira Walkenbach` | `Hon.-Prof.in Elmira Walkenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `JLFT Robotik` (organisation)
- `Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich` (address)
- `38-455/9315` (tax_number)
- `FA Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof.in Laurence Vasylenko` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Laurence Vasylenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Laurence Vasylenko`(person)
- `Finanzamtes Graz`(organisation)
- `02-410/2351`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof.in Hilde Hassenzahl` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Hilde Hassenzahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Hilde Hassenzahl`(person)
- `Gwendolin Rittmüller`(person)
- `Matzlröth 29, 3970 Reinprechts, Österreich`(address)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `10-920/5174`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Hon.-Prof.in Alice Siemglüß  in der Beschwerdesache   Wendy Schuch, Sörg 19, 5441 Erlfeld, Österreich,   betreffend Beschwerde vom 29. August 2024 gegen den Bescheid des Finanzamtes Österreich  vom 1. August 2024 betreffend Umsatzsteuer 2023 beschlossen:    I. Dem Gerichtshof der Europäischen Union werden gemäß Artikel 267 AEUV die Fragen  zur Vorabentscheidung vorgelegt, die die Auslegung der Richtlinie 2006/112/EG des  Rates vom 28. November 2006 über das gemeinsame Mehrwertsteuersystem (in der  Folge MwSt-Richtlinie) und der Achten Richtlinie 79/1072/EWG des Rates vom  6. Dezember 1979 betreffen:   1. Ist die Bekanntgabe einer MwSt-Identifikationsnummer eines anderen  Mitgliedstaates als des Mitgliedstaates, in dem die Versendung oder  Beförderung eines Gegenstandes beginnt, gemäß Art 138 Abs. 1 Buchst.

**False Positives:**

- `Hon.-Prof.in Alice Siemglüß` — partial — pred is substring of gold: `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß`(person)
- `Wendy Schuch`(person)
- `Sörg 19, 5441 Erlfeld, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

</details>

---

## `Compound_Title_Person` 🏆

**F1:** 0.368 | **Precision:** 0.771 | **Recall:** 0.241  

**Format:** `regex`  
**Rule ID:** `09cd9618`  
**Description:**
Matches persons with compound titles like 'Dr. G', 'OMedR Dr.', 'Univ.-Prof. Mag.' capturing the full sequence.

**Content:**
```
\b(?:Dr\.|OMedR\s+Dr\.|Univ\.-Prof\.|Univ\.Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Mag\.|Mag\.a|MMag\.|StR|KommR|OStR|RgR|VetR|Dipl\.-Ing\.|RA|Ing\.|PhD|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.|MA|BEd|LLM|LL\.M\. M\.B\.L\.)+(?:\s+(?:Dr\.|OMedR\s+Dr\.|Univ\.-Prof\.|Univ\.Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Mag\.|Mag\.a|MMag\.|StR|KommR|OStR|RgR|VetR|Dipl\.-Ing\.|RA|Ing\.|PhD|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.|MA|BEd|LLM|LL\.M\. M\.B\.L\.)+)*\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.771 | 0.241 | 0.368 | 580 | 447 | 133 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 447 | 133 | 1404 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Mirha Karahodzic MA` | `Mag. Mirha Karahodzic MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elisabeth Schafstall` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `SeeAutomotive AG` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Mirha Karahodzic MA` | `Mag. Mirha Karahodzic MA` |
| `Hon.-Prof. Thassilo Schoenrock, LLM` | `Hon.-Prof. Thassilo Schoenrock, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `06-88-920/2630` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Mag. Franz Glashüttner` | `Mag. Franz Glashüttner` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |
| `Mag. Bruno  Sundl` | `Mag. Bruno  Sundl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Leroy Kusznierz` (person)
- `Maximilian Jasper` (person)
- `Gustav Nowak` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Tamara Steinmüller` | `Mag.a Tamara Steinmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gueldner Garten` (organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |
| `StR Univ.-Prof. Alvin Paulikat` | `StR Univ.-Prof. Alvin Paulikat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_25`)


Nach dem vorliegenden Beschluss des Bezirksgerichtes Innere Stadt vom 26.11.2010 wurde der  Rechtsanwalt Dr. Burghardt zum Sachwalter gemäß § 268 Abs. 3 Z 2 ABGB bestellt. Der  Sachwalter wurde u.a. für das Aufgabengebiet zur Vertretung vor Ämter und Behörden  bestellt. Die Sachwalterbestellung wirkt insofern konstitutiv, als ab ihrer Wirksamkeit die  Prozess- und Handlungsfähigkeit im dort umschriebenen Ausmaß für den Bf. keinesfalls mehr  gegeben war (VwGH 27.2.2006, 2004/05/0326).

| Predicted | Gold |
|---|---|
| `Dr. Burghardt` | `Dr. Burghardt` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Elvira Thielsen` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |
| `StR Milena Neidig` | `StR Milena Neidig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Maria-Luise Wohlmayr` | `Dr. Maria-Luise Wohlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lieselotte Reinicker` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Kuprian` | `Mag. Martin Kuprian` |
| `Ing. Werner Böltl` | `Ing. Werner Böltl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Mag.Dr. Hedwig` — partial — pred is substring of gold: `Mag.Dr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag. Susanne` — partial — pred is substring of gold: `Mag. Susanne Pöltenstein-Rosenegger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

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

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

**False Positives:**

- `PhD Wilhelm Reschke` — partial — pred is substring of gold: `PhD Wilhelm Reschke, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Wilhelm Reschke, MBA`(person)
- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Mag. Andrea` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`
- `Dr. Adam` — partial — pred is substring of gold: `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

**False Positives:**

- `Mag. Andrea` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Evelyn Antwerber`(person)
- `Hertzstraße 25, 5134 Spieglern, Österreich`(address)
- `Dr. Farid Rifaad`(person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`
- `Ing. Viktoria Weigart` — similar text (different position): `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Ing. Viktoria Weigart  Dieses Unternehmen` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Ing. Viktoria Weigart  Somit` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Ing. Jonas Thumberger` — partial — pred is substring of gold: `Dipl. Kfm. Ing. Ing. Jonas Thumberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger`(person)
- `Paullehnerweg 72, 9584 Höfling, Österreich`(address)
- `UNICONSULT Steuerberatungs GmbH & Co KG`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_146`)


An der EnnsTouristik Consulting GmbH waren im Streitzeitraum beteiligt:  28.000…..HGesellschaft BFK Baugesellschaft mbH & Co KG  (jedenf. 1.1.08-27.9.11)  25.900…..BFK Holding GmbH ab 28.9.2011  3.500……..Dr. Christian W1 (1.1.2008-31.7.2011)  3.500……..Dr. Christian W2 (1.1.2008-31.7.2011)  7.000..……zweiter Stratege ( jedenfalls ab 1.8.2011-27.9.2011)  10 von 38 Seite 11 von 38

**False Positives:**

- `Dr. Christian` — no gold match — likely missing annotation
- `Dr. Christian` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `EnnsTouristik Consulting GmbH`(organisation)
- `BFK Baugesellschaft mbH & Co KG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_161`)


An der Traver-Planung GmbH waren beteiligt:    26.600 €…Holding (jedenf. 1.1.2008-12.4.2010)  25.900 €… Holding (13.4.2010-8.2.2015)  26.600 €….Holding (9.2.2015-10.9.2019)  8.400 €……Ing. Michael FG2 (jedenfalls. 1.1.2008-12.4.2010)  9.100 €……Ing. Michael FG2 (13.4.2010-8.2.2015)  8.400 €……Ing. Michael FG2 9.2.2015  35.000 €….Summe

**False Positives:**

- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Traver-Planung GmbH`(organisation)

</details>

---

## `Title_MedR_Person_Enhanced` 

**F1:** 0.004 | **Precision:** 0.667 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `5998f772`  
**Description:**
Matches 'MedR' followed by full name including suffixes, ensuring full capture.

**Content:**
```
\bMedR(?:in)?(?:\s+Priv\.-Doz\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.002 | 0.004 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 2 | 1847 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache MedR Gertrude Hartges,  Hübing 15, 9535 Farrendorf, Österreich, über die Beschwerde vom 10. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MedR Gertrude Hartges` | `MedR Gertrude Hartges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hübing 15, 9535 Farrendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Linn Wolek` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_3`)


Begründung  1.a. Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 11. März  2021, Zahl: MA67/216700111216/2021, wurde Frau MedR Uwe Vaculik (in weiterer Folge:   Beschwerdeführerin) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung 2006 für schuldig erkannt und über sie nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer   Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/148407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148407.1_1`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


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

</details>

---

## `Herrn_Name_Context` 

**F1:** 0.003 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `68bcac51`  
**Description:**
Matches names preceded by 'Herr' or 'Herrn', capturing the FULL name including suffixes.

**Content:**
```
(?:Herrn\s+|Herr\s+)([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)?\b(?=[,]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.002 | 0.003 | 6 | 3 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 3 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

</details>

---

## `Standalone_Name_Professional_Context_Enhanced` 

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `a5dd1c31`  
**Description:**
Matches standalone names following professional role indicators like 'Psychiater', 'Arzt', etc., ensuring full name capture including suffixes and requiring at least two words.

**Content:**
```
(?:Psychiater(?:in)? |Arzt(?:in)? |Ärztin |Sachverständiger |Sachverständige |Gutachter(?:in)? |Wahlpsychologin |Klinische und Gesundheitspsychologin |Steuerberater )([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)(?:,? \s*(?:MA|BEd|LLM|LL\\.M\\. M\\.B\\.L\\.|Dipl\\.-Ing\\.|Bakk\\. iur\\.|Bakk\\. phil\\.|Bakk\\. art\\.|Bakk\\. rer\\. nat\\.|Bakk\\. rer\\. pol\\.|Bakk\\. oec\\.|Bakk\\. jur\\.)?)?
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_51`)


Anlässlich einer Besprechung mit dem Prüfer am 22.05.2018 wurde von dem zwischenzeitlich  von S. beauftragten Wirtschaftsprüfer und Steuerberater Ida Katenstroth (Kanzlei L. in L.) die Auffassung  vertreten, dass von zwei einzelnen Lieferungen und nicht von einem Reihengeschäft  auszugehen sei.

| Predicted | Gold |
|---|---|
| `Ida Katenstroth` | `Ida Katenstroth` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

**False Positives:**

- `Herr Karina Burfeindt` — partial — gold is substring of pred: `Karina Burfeindt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karina Burfeindt`(person)

</details>

---

## `Title_Mag_a_Person_Enhanced` 

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `3e24544f`  
**Description:**
Matches 'Mag.a' followed by full name including suffixes, ensuring at least two words are captured.

**Content:**
```
\bMag\.a(?:\s+Priv\.-Doz\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)+)(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag.a Univ.-Prof.in Konstanze Lukass` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

</details>

---

## `Single_Letter_Name_Context_Enhanced_7` 

**F1:** 0.003 | **Precision:** 0.429 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `3f633b4c`  
**Description:**
Matches single letter names or initials with periods (e.g., 'Dr. G', 'Dr. F') in legal contexts, ensuring full capture including the title.

**Content:**
```
\b(?:Dr\.|OMedR|Univ.-Prof|Hon.-Prof|Priv.-Doz|Mag|StR|KommR|RgR|VetR)\.?\s+[A-Z]\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.429 | 0.002 | 0.003 | 7 | 3 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 4 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_17`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  2010-12 klinischer psychologischer Kurzbefund , MA 10 Wr. Kindergärten (Mag. A.):  Asperger Syndrom . Er hat enorme Stärken im mathematischen und logisch schlussfolgerndem  Denken.

| Predicted | Gold |
|---|---|
| `Mag. A.` | `Mag. A.` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_19`)


Arztbrief vom 4. Juli 2022 der Gruppenpraxis X.:  T. leidet an Panikstörung, Vd.a. somatoforme Störung und Insomnie (Anamnese: Vorstellung  aufgrund von zunehmenden Panikattacken und Vd.a. somatoforme Störung, Beginn der  Symptome im November 2021)  Arztbrief von Dr. H.:  Beginn der Panikattacken und der krankheitsbedingten Symptome November 2021  Fachärztlicher Befundbericht von Dalibor Thübel vom 21. April 2022:  T. leidet an einer Panikstörung und mittelgradigen depressiven Episoden  Folgende Unterlagen betreffend den Schulbesuch von T. betreffend den Streitzeitraum wurden  vorgelegt:  Im Wintersemester 2020/21 wurden folgende Leistungen erbracht:  2 von 11 Seite 3 von 11

| Predicted | Gold |
|---|---|
| `Dr. H.` | `Dr. H.` |

**Missed by this rule (FN):**

- `Dalibor Thübel` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_32`)


Der Substanzwert ist  der niedrigste für Gesellschaftsanteile an der Dr.in Flora Lallemand  anzusetzende Wert, selbst wenn man  das gesamte Potential an Mehrwertsteuerrückforderungen durch das Finanzamt berücksichtigt  (Gutachten von Mag. H., gerichtlich beeideter Sachverständiger ON 35 u 48).

| Predicted | Gold |
|---|---|
| `Mag. H.` | `Mag. H.` |

**Missed by this rule (FN):**

- `Dr.in Flora Lallemand` (person)
- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_53`)


Am 05.07.2018 hat in der Kanzlei L. eine Besprechung zwischen Ida Katenstroth und Mag. F.  (Fachbereich U.) stattgefunden.

**False Positives:**

- `Mag. F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ida Katenstroth`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)


Dr.in Dok3, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

**False Positives:**

- `Mag. W.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_65`)


Anstatt dessen wurde eine Kopie des Originalparkscheins mit dem Stempel „beglaubigte  Kopie“ vorgelegt, dem ein Schreiben des öffentlichen Notars Mag. P. mit folgendem Text  beigefügt war: „Diese Kopie stimmt mit der Vorderseite des mir vorliegenden Originals  vollkommen überein.

**False Positives:**

- `Mag. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_84`)


Anstatt dessen wurde eine Kopie des Originalparkscheins mit dem  Stempel „beglaubigte Kopie“ vorgelegt, dem ein Schreiben des öffentlichen Notars Mag. P. mit  folgendem Text beigefügt war: „Diese Kopie stimmt mit der Vorderseite des mir vorliegenden  Originals vollkommen überein.

**False Positives:**

- `Mag. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Title_OMedR_Person` 

**F1:** 0.002 | **Precision:** 0.400 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b3502f29`  
**Description:**
Matches persons with OMedR title (Obermedizinalrat).

**Content:**
```
\bOMedR\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.001 | 0.002 | 5 | 2 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 3 | 1849 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Leonhard Hestermeyer` | `OMedR Leonhard Hestermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` (person)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  OMedR Tanja Kubatsch, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `OMedR Tanja Kubatsch` | `OMedR Tanja Kubatsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Diana Sammer` (person)
- `Sand/Bundesstraße 2, 4170 Damreith, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

**False Positives:**

- `OMedR Ottfried Thei` — partial — pred is substring of gold: `OMedR Ottfried Theißl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Ute Gspan`(person)
- `OMedR Ottfried Theißl`(person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich`(address)
- `FA Wien 8/16/17`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_3`)


Begründung  Im Fristsetzungsantrag vom 10. Oktober 2022 wird als Sachverhalt Folgendes vorgebracht:   Mit Antrag vom 14.06.2021 beantragte die Beschwerdeführerin die Auszahlung von  Familienbeihilfe für ihr Kind OMedR Amanda Ratzmer, MSc  VNR 4982 010771  für den Zeitraum  März 2020 - April 2021.

**False Positives:**

- `OMedR Amanda Ratzmer` — partial — pred is substring of gold: `OMedR Amanda Ratzmer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Amanda Ratzmer, MSc`(person)
- `4982 010771`(social_security_number)

</details>

---

## `Standalone_Name_Role_Context_Enhanced` 

**F1:** 0.004 | **Precision:** 0.400 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `79045aeb`  
**Description:**
Matches names after roles like 'Richter', requiring at least two words to avoid partial matches.

**Content:**
```
(?:durch den Richter|durch die Richterin|Richter|Richterin|Geschäftsführer)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.002 | 0.004 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 1847 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_180`)


Die Bf selbst (insbesondere ihr Geschäftsführer Linn Brümmer IE) ist zu diesem Beweisthema  (Nachnutzung der strittigen Häuser nach deren Nutzung als Musterhäuser) durch das FA bisher  jedenfalls nicht nachvollziehbar dokumentiert befragt worden.

| Predicted | Gold |
|---|---|
| `Linn Brümmer` | `Linn Brümmer` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/143846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143846.1_1`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_234`)


Fazit: Die Ansicht (NiS. 2.6.Kämpker&Mooslechner Holz GmbHS. 6 -9), nur beratende Tätigkeiten der Strategen im  Namen der OG beruhten auf dem Managementvertrag , und die lenkenden und  überwachenden , dh geschäftsführenden Tätigkeiten der Strategen seien nicht auf Grund des  Managementvertrages erfolgt und auch nicht auf der Grundlage des Managementvertrages  oder sonstwie abgegolten worden, ist nicht überzeugend, weil   -der StB selbst die Lenkungs- und Überwachungstätigkeiten der Strategen im Zusammenhang  mit den Managementverträgen erwähnt hat (Schreiben des Steuerberaters vom 22.9.2016),  - weil man die Tätigkeiten der Strategen, die dem Konzern, bestehend aus den  Konzerngesellschaften, gedient haben (Lenkungs- Überwachungstätigkeiten, sonstige  unterstützende Tätigkeiten wie z.B. Beratungen lt. Vorlageantrag S. 3-5, lt. Schreiben des   Steuerberaters vom 22.9.2016, lt Unilemder-Versand GmbH2.6.2021, S. 7 und lt. Gesellschafter- Geschäftsführer Steblein Wind GmbH2.6. S. 11 und 12) nicht trennen kann.

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `2.6.Kämpker&Mooslechner Holz GmbHS.`(organisation)
- `Unilemder-Versand GmbH2.6.2021`(organisation)
- `Steblein Wind GmbH2.6.`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_302`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und  12).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_304`)


Die Fremdgeschäftsführer sollten zu Motivationszwecken mittelfristig auch eine  Beteiligung an der jeweiligen Tochtergesellschaft der Holding, für die sie tätig waren, erlangen  können (Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 11;

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_311`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und 12).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_316`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und 12).  ee.)

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_321`)


Bis jetzt hat diese im Jahr 2004 durch die drei Strategen einvernehmlich erdachte Planung  erfolgreich umgesetzt werden können; der Gesamtumsatz des Konzerns, bestehend aus den  oben erwähnten Konzerngesellschaften, hat sich in den letzten 15 Jahren vervielfacht  (Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6., S. 11).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.`(organisation)

</details>

---

## `Party_Name_NoTitle_Context_Enhanced_2` 

**F1:** 0.002 | **Precision:** 0.400 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `90c9b3e7`  
**Description:**
Matches party names in phrases like 'in der Beschwerdesache [Name]' where the name might not have a title immediately preceding it, capturing full name including suffixes and handling single-word names if context is strong.

**Content:**
```
(?:in der Beschwerdesache|Beschwerdesachen)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)?\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.001 | 0.002 | 5 | 2 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 3 | 1849 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


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

</details>

---

## `Standalone_Name_Verb_Context_Enhanced_2` 🏆

**F1:** 0.005 | **Precision:** 0.250 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `fb063a90`  
**Description:**
Matches standalone names following verbs like 'ist', 'hat', 'war', ensuring at least two words and stopping before non-name words.

**Content:**
```
(?:ist|hat|war|verrechnet|verkauft|eingekauft|verwaltet|geleitet|betreiben)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.003 | 0.005 | 20 | 5 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 15 | 1846 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_108`)


Im Weiteren verweist Ida Katenstroth auf die Entscheidung  des EuGH in der Rechtssache Kreuzmayr GmbH, C-628/16, Rn. 34, die diese Ansicht wiederholt  und wie folgt ausführt: „Schließlich sind zur Feststellung, ob eine Lieferung als  „innergemeinschaftliche Lieferung“ eingestuft werden kann, die Absichten zu berücksichtigen,  die der Erwerber zum Zeitpunkt des Erwerbs des fraglichen Gegenstandes hatte, sofern sie  durch objektive Gesichtspunkte gestützt werden“.

| Predicted | Gold |
|---|---|
| `Ida Katenstroth` | `Ida Katenstroth` |

**Missed by this rule (FN):**

- `Kreuzmayr GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_127`)


Mit Mail vom 10.07.2018 hat Ida Katenstroth noch auf das BFG Judikat vom 27.04.2018 Bezug  genommen.

| Predicted | Gold |
|---|---|
| `Ida Katenstroth` | `Ida Katenstroth` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_134`)


Mit Mail vom 03.10.2018 hat Ida Katenstroth zu der am 01.10.2018 vom Prüfer übermittelten  Prüfungsfeststellung wie folgt Stellung genommen:  Pkt .1.2  Seitens der AP wird auf das Urteil des EuGH vom 22.04.2010 hingewiesen.

| Predicted | Gold |
|---|---|
| `Ida Katenstroth` | `Ida Katenstroth` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_25`)


Somit hat Harald Hilderink  aufgrund des festgestellten Sachverhaltes sowohl objektiv als auch  subjektiv die Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG zu verantworten.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_31`)


Zur beschwerdeführenden Partei  Die beschwerdeführende Partei ist Jonas Bruchmüller  im Sinne des § 1 Bankwesengesetz  (Bundesgesetz über das Bankwesen -BWG) und unterliegt dem Stabilitätsabgabegesetz.

| Predicted | Gold |
|---|---|
| `Jonas Bruchmüller` | `Jonas Bruchmüller` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_28`)


Aus den o.a. Gründen war Ihre Beschwerde ab  3/13 ebenfalls abzuweisen.“

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

**False Positives:**

- `Frau Basil` — positional overlap with gold: `Basil Staerk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Basil Staerk`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_112`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste  gegen ihn Anzeige erstattet werden.

**False Positives:**

- `Herr Russbüldt` — partial — gold is substring of pred: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_117`)


Tatsächlich ist Herr Russbüldt mit Bestellungsurkunde vom 27.11.2018 zum Fuhrparkleiter der  Firma1 und der hier nicht in Rede stehenden Firma2 bestellt worden.

**False Positives:**

- `Herr Russbüldt` — partial — gold is substring of pred: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_171`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste gegen ihn Anzeige erstattet werden.

**False Positives:**

- `Herr Russbüldt` — partial — gold is substring of pred: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_34`)


Das Pendlerpauschale wird aber abhängig von der Anzahl der Tage im Kalendermonat, an  denen die Entfernung Wohnung – Arbeitsstätte – Wohnung zurückgelegt wird, aliquotiert:  Bei Fahrten an mindestens 4 Tagen, aber nicht mehr als 7 Tagen … steht ein 1/3 des  Pendlerpauschales zu.  Bei Fahrten an mindestens 8 Tagen, aber nicht mehr als 10 Tagen … stehen 2/3 des  Pendlerpauschales zu.  Bei Fahrten an mindestens 11 Tagen ……………………………steht das volle Pendlerpauschale zu.  Da laut Ihren Aufzeichnungen die Fahrten zwischen Wohnung – Arbeitsstätte – Wohnung  maximal 3mal im Monat unternommen wurden, war Ihre Beschwerde auch in diesem Punkt  abzuweisen.

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

**False Positives:**

- `Herr Inn Trikraftglanz` — partial — gold is substring of pred: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Trikraftglanz`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_298`)


Antwort: Der hat sich auch telefonisch gemeldet, er hat sich als Herr d. vorgestellt.  Frage: Wer war Ihr Ansprechpartner bei der Fa. d.?  Antwort: Herr d. selber.

**False Positives:**

- `Ihr Ansprechpartner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Frau Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_45`)


Da bereits am 24.09.2018 die Festsetzung der Zwangsstrafe angedroht wurde und Ihnen eine  Nachfrist bis 03.01.2018 gewährt wurde, die Festsetzung der Zwangsstrafe dem Grunde und  Höhe nach im Ermessen der Abgabenbehörde innerhalb der Grenzen getroffen wurde, war Ihre  Beschwerde als unbegründet abzuweisen.“

**False Positives:**

- `Ihre  Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

**False Positives:**

- `Herr  Harald Hilderink` — partial — gold is substring of pred: `Harald Hilderink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Harald Hilderink`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138313.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138313.1_7`)


Da die Beschwerde nicht innerhalb der Beschwerdefrist eingereicht wurde, war Ihre Beschwerde  als nicht fristgerecht zurückzuweisen“.

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/144646.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144646.1_44`)


Die  diesbezügliche Aufforderung (Bescheid vom 28.10.2021) hat Herr Jakob Dombrink  an das Finanzamt  retourniert und vermerkt, dass er eine Rente aus der Schweiz bekommt und diese zur Gänze in  die landwirtschaftliche Gesellschaft fließt (siehe "Schreiben Jakob Dombrink  v. 15.11.2021").

**False Positives:**

- `Herr Jakob Dombrink` — partial — gold is substring of pred: `Jakob Dombrink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jakob Dombrink`(person)
- `Finanzamt`(organisation)
- `Jakob Dombrink`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/144700.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144700.1_31`)


Da mangels Vorliegen der erheblichen Härte kein Raum mehr für eine Ermessensentscheidung  der Behörde ist, war Ihre Beschwerde abzuweisen.“

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_18`)


Geburtstag eingetreten ist  Die Bescheidbegründung, nämlich, dass die Beeinträchtigung nicht vor dem 21.

**False Positives:**

- `Die Bescheidbegründung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `VetR_Title_Person` 

**F1:** 0.001 | **Precision:** 0.167 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `f2660932`  
**Description:**
Matches persons with VetR title (Veterinär), capturing FULL text including suffixes.

**Content:**
```
\bVetR\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*(?:\s*,\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.001 | 0.001 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 5 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143412.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der  Verwaltungsstrafsache gegen VetR Maria Naundorff, Bakk. rer. nat., Genigasse 90G, 8341 Saaz, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 23. Dezember 2023  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  14. Dezember 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `VetR Maria Naundorff, Bakk. rer. nat.` | `VetR Maria Naundorff, Bakk. rer. nat.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Genigasse 90G, 8341 Saaz, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `VetR Elias Voht, ` — partial — gold is substring of pred: `VetR Elias Voht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Elias Voht`(person)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `VetR Burkhard Krautschenko,  ` — partial — gold is substring of pred: `VetR Burkhard Krautschenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Adolf Brehmer  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `VetR Gotthard Lohscheider,  ` — partial — gold is substring of pred: `VetR Gotthard Lohscheider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Adolf Brehmer`(person)
- `VetR Gotthard Lohscheider`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Meinrad Kisewetter`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache DDr.in VetR Rosemarie Srama,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `VetR Rosemarie Srama,  ` — positional overlap with gold: `DDr.in VetR Rosemarie Srama`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Aron Nierenberger`(person)
- `DDr.in VetR Rosemarie Srama`(person)
- `Hollgasse 53, 3244 Riegers, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/141990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141990.1_2`)


Das Bundesfinanzgericht hat durch die Senatsvorsitzende R1, den RichterR2, sowie die  fachkundigen Laienrichter R3 und R4, in der Beschwerdesache VetR Maja Waatsack, Sarottla 115, 8522 Sulzhof, Österreich,  vertreten durch Mag. Wolfgang Schranz, Mahlerstraße 11 Tür 4, 1010 Wien, über die  Beschwerde vom 28. Oktober 2016 gegen die Bescheide des Finanzamtes Wien 8/16/17 vom  25. Juli 2016 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gemäß § 188 BAO für  2009, sowie vom 24. August 2016 betreffend Umsatzsteuer und Feststellung der Einkünfte  gemäß § 188 BAO für die Jahre 2010 bis 2015, Steuernummer 31-345/4688, in der Sitzung  vom 30. August 2023 nach Durchführung einer mündlichen Verhandlung am 30. August 2023 in  Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `VetR Maja Waatsack, ` — partial — gold is substring of pred: `VetR Maja Waatsack`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Maja Waatsack`(person)
- `Sarottla 115, 8522 Sulzhof, Österreich`(address)
- `Mag. Wolfgang Schranz`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `31-345/4688`(tax_number)

</details>

---

## `Standalone_Name_Rs_Context` 💣

**F1:** 0.001 | **Precision:** 0.042 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `165c75c6`  
**Description:**
Matches case names (Rs) which often refer to the person involved, e.g., 'Rs Schmelz'.

**Content:**
```
(?:Rs\s+|Rs\.\s+)([A-Z][a-z]+(?:-[A-Z][a-z]+)*)\b(?=[^a-zA-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.042 | 0.001 | 0.001 | 24 | 1 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 23 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)


12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr Aldewereld von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

| Predicted | Gold |
|---|---|
| `Aldewereld` | `Aldewereld` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_268`)


Verordnungen sind überdies auch unmittelbar anwendbares Unionsrecht (vgl Leidenmühler,  aaO, 31 unter Hinweis auf EuGH vom 5.2.1963, 26/62, Rs van Gend & Loos, Rn 8, 9; ders, aaO,  34 unter Hinweis auf EuGH vom 9.3.1978, 106/77, Rs Simmenthal II, Rn 17, 18).

**False Positives:**

- `Simmenthal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_270`)


Damit hat das fachlich  zuständige Bundesministerium die Unionsrechtslage verkannt, wie sich aus der  Rechtsprechung des EuGH zu Beschäftigungen, die in einem Drittland ausgeübt werden, ergibt  (von EuGH vom 29. Juni 1994, C-60/93, Rs R.L. Aldewereld bis EuGH vom 31.3.1977, 87/76, Rs  Bozzone).

**False Positives:**

- `Bozzone` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aldewereld`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_279`)


Vielmehr ist in § 13 Abs 1 EHG aF eine alternative  nationale Rechtsgrundlage wie in der Rs Hudzinski und Wawrzyniak zu erblicken.

**False Positives:**

- `Hudzinski` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_293`)


Nach ständiger Rechtsprechung des EuGH ist  dieser Sachverhalt ausreichend, um eine hinreichend enge Anknüpfung an das Gebiet der  Union anzunehmen (EuGH vom 12. Juli 1984, C-237/83, Rs Prodest Rn 6; nochmals EuGH Rs  R.L. Aldewereld Rn 14).

**False Positives:**

- `Prodest` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aldewereld`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_299`)


Dass die Ausübung der persönlichen Freiheit  grundsätzlich nicht zu einem Rechtsverlust führen darf, zeigen ua die Urteile EuGH vom 11. Juli  2002, C-224/98, Rs D'Hoop, und EuGH vom 26. November 2009, C-363/08, Rs Slanina.

**False Positives:**

- `Slanina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_319`)


15 In der Literatur wird § 53 Abs 1 FLAG im Hinblick auf EuGH vom 10.10.1973, 34/73, Rs  Variola, kritisch gesehen (Gebhart in Lenneis/Wanke, aaO, § 53, Rz ).

**False Positives:**

- `Variola` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_327`)


16 Anders als in der Rs Variola verfolgt § 53 Abs 1 FLAG nicht das Ziel, den Zeitpunkt der  Anwendung der Wanderarbeitnehmerverordnung zu verschieben.

**False Positives:**

- `Variola` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_411`)


Da nach Ansicht des anfragenden Gerichts Deutschland nach wie vor Wohnortstaat  ist und die Bf das personale Element erfüllt, ist eine hinreichende Bindung an das Unionsgebiet  gegeben (s obige Ausführungen iVm Rs Alderewerld).

**False Positives:**

- `Alderewerld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_473`)


Demnach könnte Österreich aus Gründen der Loyalität der Mitgliedstaaten untereinander und  zur Union verpflichtet sein, die alte Rechtslage des § 13 Abs 1 EHG durch Erfüllung seiner  Rechtsbereinigungspflicht wiederherzustellen (vgl Leidenmühler, aaO, 35 mit Hinweis auf EuGH  vom 25.10.1979, 159/78, Rs Kommission/Italien, Rn 22) und jene Mitgliedstaaten, die für diese  Berufsgruppe keine Familienleistungen in ihren Rechtsvorschriften vorsehen, verpflichtet sein,  die Gewährung von Familienleistungen an Entwicklungshelfer einzuführen.

**False Positives:**

- `Kommission` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_474`)


Ad Frage 9: individuell-konkreter Anspruchsfortbestand  59 Falls Frage 8 verneint wird, ist nach Ansicht des BFG fraglich, ob die Bf aus den in Rn 36, 37  und 40 dieses Beschlusses genannten Gründen einen individuell-konkreten Anspruch auf  Fortbestand der Familienbeihilfe iSv wohlerworbenen Rechten erlangt hat (vgl EuGH vom  12.6.1980, 733/79, Rs Laterza, und das in Rn 10 dieses Beschlusses erwähnte Urteil in der Rs  Slanina).

**False Positives:**

- `Laterza` — no gold match — likely missing annotation
- `Slanina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_24`)


Dass sich der zeitliche Anwendungsbereich der AGVO 651/2014 rückwirkend auch auf  Einzelbeihilfen erstreckt, die vor deren Geltungsbeginn mit 1.7.2014 liegen, stehe erst nach der  Entscheidung des EuGH in der Rs Dilly’s Wellnesshotel ll fest.

**False Positives:**

- `Dilly` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_141`)


Die im  bisherigen Verfahren von der Bf. vorgelegten Unterlagen lassen dies nicht erkennen, zumal  auch der 34-seitige in englischer Sprache vorgelegte Vertrag über den zweiten Umsatz keine  ausreichenden Informationen enthält. Er enthält lediglich Informationen über das  Beschaffungsgeschäft der Bf. bei der Möbel Zorkelglanz GmbH  Abgesehen davon hat der VwGH die  reklamierten Gefahrtragungsregelungen und von der bisherigen Verwaltungspraxis  maßgebliche Transportverantwortlichkeit einschließlich Handelsklauseln nicht weiter erörtert,  sondern sich lediglich auf die dem Bundesfinanzgericht damals noch nicht bekannten Rz. 70, 74  und 75 der Rs. Arex, EuGH v. 19.12.2018, C-414/17 gestützt.

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_332`)


Abgesehen davon habe der VwGH die reklamierten  Gefahrtragungsregelungen und die von der bisherigen Verwaltungspraxis als maßgeblich  erachteten Transportverantwortlichkeit einschließlich Handelsklauseln nicht weiter erörtert,  sondern sich lediglich auf die Rz. 70, 74 und 75 der Rs. Arex, EuGH v. 19.12.2018, C-414/17  gestützt.

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_349`)


So hat der EuGH in der  Rs. Herst, wie schon in der Rs. AREX mit keinem Wort diesen Aspekt aufgegriffen.

**False Positives:**

- `Herst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_362`)


In Hinblick auf die Übertragung der Verfügungsmacht auf den Zweiterwerber im Rahmen eines  Reihengeschäfts hat der EuGH folglich präzisiert (zuletzt in der Rs. Herst), dass die  Verfügungsmacht bereits dann übertragen wird, wenn die Partei die Möglichkeit hat,  Entscheidungen zu treffen, die sich auf die rechtliche Situation des betreffenden Gegenstands  auswirken, etwa die Entscheidung, den Gegenstand zu verkaufen.

**False Positives:**

- `Herst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_418`)


D.h. selbst  wenn man von einem Reihengeschäft ausgehen würde, ergeben sich auf Basis der  Rechtsprechung des EuGH (vgl. zuletzt Rs. Herst, Rn. 41) dieselben umsatzsteuerlichen  Konsequenzen für die Bf. (dh Bezug einer ruhenden Lieferung von JBL und Bewirken einer  innergemeinschaftlichen Lieferung an die EU-Kunden), weil die EU-Kunden die Waren vor  Transportbeginn ihrerseits weiterverkauft haben oder zur Lohnfertigung unmittelbar an ihre  Auftragnehmer versenden ließen (vgl. Anlage 5).

**False Positives:**

- `Herst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_728`)


Im Unterschied dazu judiziert der EuGH in der  Rs. Toridas, Rn. 44, dass die Information die Ware bereits vor Bewirkung dieses Umsatzes (des  ersten) und die tatsächliche Beförderung vom ersten Lieferer an den Warenempfänger  ausreiche, um die bewegte Lieferung und damit die innergemeinschaftliche Lieferung dem  zweiten Umsatz zuzuordnen.

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_114`)


Maßgeblich für diesen Ort ist vielmehr der Ort, an dem  der Unternehmer die Handlungen zur zentralen Verwaltung des Unternehmens vornimmt  (EuGH Rs. Stoppelkamp, C-421/10), an dem das gesamte Unternehmen betrieben wird (VwGH  7.5.2021, Ra 2020/0115).

**False Positives:**

- `Stoppelkamp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_318`)


Der EuGH führte zur Steuerschuld kraft Rechnungslegung in der Rs Stadeco im Urteil EuGH vom  18.6.2009, C-566/07, aus:  „26 Zum anderen ist darauf hinzuweisen, dass nach Art. 21 Abs. 1 Buchst, c der Sechsten  Richtlinie jede Person, die die Mehrwertsteuer in einer Rechnung oder einem ähnlichen  Dokument ausweist, diese Steuer schuldet.

**False Positives:**

- `Stadeco` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_334`)


Der EuGH führte zum  Vorsteuerabzug iZm missbräuchlicher Rechtsgestaltung in der Rs Halifax im Urteil EuGH vom  21.2.2003, C-255/02, aus:  „84 Wie der Gerichtshof jedoch bereits entschieden hat, bleibt nur dann, wenn kein Fall von  Betrug oder Missbrauch vorliegt, das einmal entstandene Recht auf Vorsteuerabzug  vorbehaltlich etwaiger Berichtigungen gemäß Artikel 20 der Sechsten Richtlinie erhalten (vgl. u.  a. Urteile vom 8. Juni 2000 in den Rechtssachen C-400/98, Breitsohl, Slg.

**False Positives:**

- `Halifax` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_129`)


zu letzterer  EuGH vom 21.7.2011, Rs Scheuten Solar Technology GmbH, Rs C-397/09).“  10 von 26 Seite 11 von 26

**False Positives:**

- `Scheuten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_168`)


Aufgrund dieses weiten  Anwendungsbereiches steht die Regelung im Einklang mit zwischenstaatlichen (Art. 24 der  Doppelbesteuerungsabkommen, dem OECD-MA folgend) und unionsrechtlichen Regelungen  (Unionsfreiheiten, Richtlinie des Rates vom 3. Juni 2003 über eine gemeinsame Steuerregelung  für Zahlungen von Zinsen und Lizenzgebühren zwischen verbundenen Unternehmen  verschiedener Mitgliedstaaten (2003/49/EG); zu letzterer EuGH vom 21.7.2011, Rs Scheuten  Solar Technology GmbH, Rs C-397/09).“

**False Positives:**

- `Scheuten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single_Letter_Name_Context_Enhanced_2` 💣

**F1:** 0.003 | **Precision:** 0.034 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `7886d507`  
**Description:**
Matches single letter names or initials with periods (e.g., 'M.', 'Dr. B.') in legal contexts like 'namens M.' or 'Zeuge M.'.

**Content:**
```
(?:namens|Zeuge|Zeugin|als|für|des|von)\s+([A-Z]\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.034 | 0.002 | 0.003 | 89 | 3 | 86 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 86 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_44`)


bf. habe ihn anfangs für eine Hilfskraft oder den Chauffeur von M. gehalten.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_378`)


Ich habe die Preisverhandlungen mit Herrn M. geführt und ich habe  von M. diesen Preis verlangt, da ich bei der e. immer gleich bezahlen musste mit  Eilüberweisung, bei der Fa.F. hatte ich aber ein Zahlungsziel von 30 Tagen vereinbart.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_294`)


Dieser Befund aus 2019 befasst sich ausschließlich mit dem Zustand von M. zum Zeitpunkt der  Untersuchungen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_62`)


lediglich für 2 Monate zusteht, hatte er keinen Anspruch auf Gewährung des  Kinderfreibetrages für W.  Die dem Bf. für seine Kinder zustehenden Ansprüche ermitteln sich wie folgt:  J:   - Kinderfreibetrag für ein haushaltszugehöriges Kind € 440,-  - Kinderbetreuungskosten (a.g. Belastung) € 1.560,-  W:  - Unterhaltsabsetzbetrag (2 Monate): € 58,40  Die Höhe der Abgabe beträgt:      2018    €  Einkünfte aus nichtselbständiger Arbeit    BUAK 2.213,15   A-Bau GmbH 15.278,78   Kontrollrechnung § 3 Abs. 2 EStG 3.578,58   Pauschbetrag f. Werbungkosten -132,00 20.938,51  Gesamtbetrag der Einkünfte  20.938,51

**False Positives:**

- `W.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_21`)


Zu den Fleischlieferanten der Bf. zählten die Lemost-Handel GmbH unter der Geschäftsführung von E.St.  sowie die Dorfleitner+Ternis Versicherung GmbH unter der Geschäftsführung von K.F.St..  Bericht gemäß § 150 BAO vom 21.10.2009  Unter Tz.1ff.

**False Positives:**

- `E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)
- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_80`)


*) Printartikel: Laut Artikel von R.R. in der Zeitschrift Printartikel, würden laut Angaben des V.  A. ca. 150.000 A. Portionen pro Jahr umgesetzt werden.

**False Positives:**

- `V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_404`)


Über Frage des steuerlichen Vertreters nach der Kennzeichnung der speziell an die Bf.  zugestellten Ware des Geschäftsführers der Lemost-Handel GmbH gab Z3 zu Protokoll, dass es ein eigener  Artikel gewesen sei, der von den Köchen als A.- Produkte bestellt werde.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_537`)


Diese Tätigkeiten seien von Z.3 übergreifend auch  für den Betrieb am W-Platz erledigt worden.

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_220`)


Zwischen der beim Firmenbuchgericht aufliegenden Musterfirmazeichnungserklärung des D. C.  und dem Schriftbild auf den Zahlungsbestätigungen (Kassa-Eingang Belege) ist keine  Übereinstimmung hinsichtlich des Schriftzugs zu erkennen.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_235`)


Die am Handelsgericht aufliegende  Musterunterschrift des V. weicht von dem Schriftbild auf diesen Belegen jedoch eindeutig ab.

**False Positives:**

- `V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_47`)


Dieses Recht wird hiemit von A. W angenommen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_51`)


Siebentens: Allgemeine Bestimmungen  7.1 Die Kosten der Errichtung und Vergebührung dieser Vereinbarung werden zur Gänze von A.  W getragen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_109`)


Die  tatsächliche unternehmerische Initiative von A. W während der Vermietung ist unbestritten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_27`)


Laut amtsärztlichen Sachverständigengutachten des Sozialministeriumservice vom 21.5.2020  wurde der Grad der Behinderung von A. im Ausmaß von 30 v.H. festgestellt.   Sohin wurde am 27.5.2020 der Antrag auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe wegen erheblicher Behinderung vom 28.2.2020 ab dem Monat der  Antragstellung Mai 2018 abgewiesen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_29`)


In Ihrem Beschwerdebegehren stellten Sie den Antrag auf Gewährung des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung für A. ab dem Monat September 2015, mit  der Begründung, dass Ihr Sohn A. unter einer Hornhautverkrümmung leide und deswegen eine  Brille zu tragen hat.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_32`)


Der Zustand von A. hat  sich daher schon verbessert.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_46`)


Der  Bescheid wurde nach Zitierung des § 8 Abs. 5 FLAG 1967 wie folgt begründet:   Laut amtsärztlichen Sachverständigengutachten des Sozialministeriumservice vom 21.9.2020  wurde der Grad der Behinderung von A. im Ausmaß von 30 v.H. festgestellt. Demnach besteht  für die Monate September 2015 bis April 2018 kein Anspruch auf den Erhöhungsbetrag zur  Familienbeihilfe wegen erheblicher Behinderung.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_48`)


Es wird zurzeit ein neues aktuelles Gutachten von der  Kinder- und Jugendpsychiatrie wegen seiner Legasthenie in der Klinik Floridsdorf erstellt. Diese  Behinderung war und noch immer ist auch eine psychische Belastung für A.   Diese Beschwerde wies das Finanzamt mit Beschwerdevorentscheidung vom 27. Jänner 2021  als unbegründet ab und begründete seine Entscheidung wie folgt:   Sachverhalt   Ihr Antrag auf erhöhte Familienbeihilfe für das … 2009 geborene Kind A. wurde mit Bescheid  vom 06.10.2020 für den Zeitraum von September 2015 bis April 2018 abgewiesen, da durch  das fachärztliche Sachverständigengutachten vom 21.09.2020 lediglich ein Grad der  Behinderung von 30% ab Mai 2018 festgestellt wurde.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_13`)


Die Ware gelangt direkt vom Werk von J. in P. (Bundesland  Niederösterreich) an die jeweiligen Endabnehmer.

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_16`)


…  In beiden Fällen (Lieferkondition DDP bzw. FCA in den Rechnungen von S.) legt JBL Rechnungen  mit 10% österreichischer Umsatzsteuer, die von S. als Vorsteuer in Abzug gebracht wird.

**False Positives:**

- `S.` — no gold match — likely missing annotation
- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_41`)


Bei den Lieferungen von S. an die jeweiligen Endkunden im EU-Gebiet handelt es sich um die  ruhenden Lieferungen (§ 3 Abs. 7 UStG).

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_51`)


Anlässlich einer Besprechung mit dem Prüfer am 22.05.2018 wurde von dem zwischenzeitlich  von S. beauftragten Wirtschaftsprüfer und Steuerberater Ida Katenstroth (Kanzlei L. in L.) die Auffassung  vertreten, dass von zwei einzelnen Lieferungen und nicht von einem Reihengeschäft  auszugehen sei.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ida Katenstroth`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_56`)


Strittig blieb  aber, ob der Kunde von S. (Zweiterwerber) bereits im Abgangsstaat Österreich über die Ware  verfügen konnte bevor die Warenbewegung beginnt.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_76`)


Entscheidend sind vielmehr die  Umstände, unter denen die Lieferungen von S. als Zweitlieferant an dessen Kunden als  Zweiterwerber erfolgt sind.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_283`)


Die Ware gelangt direkt vom Werk von J. in P. (Bundesland Niederösterreich)  an die jeweiligen Endabnehmer.

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_533`)


2. Bei Anwendung von Abs. 3a wird die Beförderung oder Versendung abweichend von Z. 1 der  Lieferung durch den Unternehmer gemäß Abs. 3a Z. 1 bzw. 2 zugeordnet.

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `X.` — similar text (different position): `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_12`)


Im Prüfungszeitraum wurden auf Basis von „service agreements" mit der A.Bachvalder GmbH (in der  Folge: kurz als D./Deutschland) vom 01.01.2013 bis 31.10.2013 und ab 01.11.2013 mit der A. C.  B.V. (in der Folge: kurz als D./Holland) von der D. „Werbeleistungen" erbracht und auch  dementsprechend verrechnet.

**False Positives:**

- `D.` — no gold match — likely missing annotation
- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `A.Bachvalder GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_34`)


• Schulung und Information der Trafikanten sowie Kontakt mit D.-Außendienst und Marketing  Mitarbeiter  ® Produktvorstellung: N ,H  ® Genussforum: Vorträge von Experten zu Genussmittei-Themen Tabak, Kaffee,...  Verleihung Award  2014  Netzwerken: Kontaktpflege, Meinungsaustausch Trafikanten untereinander sowie mit D.  Außendienst und Marketing Mitarbeiter   Fand in der alten F statt  ® Genussforum: Vortrag Senior Blender des D.-Werkes in G, sowie Laborleiter der Spitz GmbH  ® Verleihung Award: Verleihung, Moderation  2015  Netzwerken: Kontaktpflege, Meinungsaustausch Trafikanten untereinander sowie mit D.  Außendienst und Marketing Mitarbeiter;

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_155`)


Dabei hat die Prüferin als Empfänger die Teilnehmer des D.-Awards  bezeichnet.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_296`)


Die Prüferin hat nun auch die restlichen 50 % der Aufwendungen für J-Gutscheine  hinzugerechnet und sie damit wie die D.-Awards behandelt.   Mit E-Mail vom 10. August 2021 wurde nachstehende Information, die die steuerliche  Vertretung von der Geschäftsführung der Bf. erhalten hat, übermittelt:  „Die J Gutscheine wurden bis 2014 von unserem Außendienst zu unterschiedlichen Anlässen  zur Entschädigung von Trafikantenleistungen für D. wie bspw.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_320`)


1.2. J Gutscheine in den Jahren 2013 und 2014 :  Die J-Gutscheine wurden in den Jahren 2013 und 2014 durch die Außendienstmitarbeiter zu  unterschiedlichen Anlässen zur Entschädigung von Trafikantenleistungen für D. wie bspw.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_46`)


Als Beweis lege sie auch das Schreiben  (E-Mail vom 11. April 2019) von Z. bei (Anm.: Der Genannte bestätigte im Schreiben vom 11.  April 2019, dass er mit dem Sohn der Bf. von Dezember 2017 bis Jänner 2018 gemeinsam für  die Matura gelernt habe).

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_82`)


Dem Schreiben beigefügt war die Ambulanzkarte der Klinik Landstraße,  Erstuntersuchungsambulanz des N. S. vom 14.3.2022, Anamnese vom 26.03.2018, 02:38 Uhr  sowie die bereits im Akt aufliegenden Blutlaborbefund, ebenfalls vom 26.03.2018.

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_217`)


Das Vorbringen der Bf., wonach sich ihr Sohn vom Februar 2017 bis zum erneuten Termin im  Herbst 2017 sehr intensiv vorbereitet habe, ist jedenfalls genauso wenig ausreichend, um von  einer ernsthaft und zielstrebig betriebenen Ausbildung auszugehen wie die von ihr vorgelegte  Bestätigung des Z., wonach dieser mit ihrem Sohn von Dezember 2017 bis Jänner 2018  gemeinsam für die Matura gelernt hat.

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_33`)


Dagegen brachte die Bf. einen Vorlageantrag mit folgender Begründung ein:  „Ich erhebe Einspruch auf die Mitteilung zur Rückzahlung der Familienbeihilfe für ein Semester  2017 für S. Meine Tochter hat das Studium sehr ernsthaft betrieben.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_4`)


Dr. Dok1, Fachgebiet Allgemeinmedizin, erstellte nach Untersuchung von S. am 2. März 2021  folgendes Gutachten:  Anamnese:  Schwangerschaft und Geburt unauffällig  TE und Paukenröhrchen;

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_32`)


2013/14 habe ich für S. Hilfe in einer psychotherapeutischen Gruppe bei der Österr.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_36`)


2018 haben wir für S.  einen Psychologen gefunden, den er akzeptiert hatte und ihm auch helfen konnte.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_90`)


Bereits in der Beschwerde vom 25.04.2021 wird auf den aktuellen Zustand von S. X. Bezug  genommen und - erkennbar - auf den Umstand hingewiesen, dass das Ermittlungsverfahren  mangels Einholung eines fachspezifischen Sachverständigengutachtens unvollständig blieb.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_112`)


Im Aktengutachten vom 31. Jänner 2022 wurde das (inzwischen vorgelegte) Privatgutachten  von MMag. W., MSc, vom 5. Oktober 2021 berücksichtigt und von Dr.in Dok3 die Erkrankung  von S. unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit einem Gesamtgrad der  Behinderung von 30 vH rückwirkend ab Oktober 2021 eingereiht.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_180`)


in ihrem Aktengutachten vom 31. Jänner 2022 die Erkrankung von S. unter die  Pos.Nr. 03.04.01 der Einschätzungsverordnung mit einem Gesamtgrad der Behinderung von 30  vH rückwirkend ab Oktober 2021.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_8`)


Der Bf. ist seit 31. Juli 2017 als Trockenbau-Monteur in Österreich beschäftigt (Bestätigung des  Arbeitgebers XY vom 19. Jänner 2021) und bezog auf Grund seiner Beschäftigung in Österreich  für K. laufend Differenzzahlungen zur Familienbeihilfe.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_7`)


Die Familienbeihilfe für S. wurde daraufhin bis Juli 2019 verlängert.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_15`)


Daraufhin wurde die Familienbeihilfe für S. für den Zeitraum Oktober 2020 bis September 2021  rückgefordert mit der Begründung, dass es offenbar zu einem Studienwechsel gekommen war  und dieser im Sinne des Familienlastenausgleichgesetzes schädlich wäre (§ 2 Abs.1 lit b FLAG  iVm § 17 StudFG, siehe dazu Rückforderungsbescheid vom 08.11.2021).

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_16`)


Gegen diesen Rückforderungsbescheid reichte die Bf Beschwerde ein und begründete den  Studienabbruch durch eine schwere psychische Erkrankung der Tochter, die einen  Wiedereinstieg für S. in das alte Studium unmöglich gemacht hätte.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_82`)


Nach Ansicht des BFG vermag damit die ärztliche Bestätigung aus dem Jahr 2021 für S. das  Vorliegen einer krankheitsbedingten durchgehenden Studienbehinderung für das dritte  Semester (bzw. bis Frühjahr 2018) weder nachweisen noch glaubhaft machen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Cornelia Reifgerste`(person)
- `Scherzergütl 18K, 9622 Golz, Österreich`(address)
- `Freimüller Rechtsanwalts GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `M. F.`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_177`)


Mit Beschwerdevorentscheidung vom 06.09.2021 verweise die belangte Behörde auf die  beiden fachärztlichen Gutachten des Bundesamtes für Soziales und Behindertenwesen vom  8. Juli 2020 und vom 6. November 2021, laut derer der Grad der Behinderung für M. F. 30 % ab  dem 01.11.2019 betrage und keine dauernde Erwerbsunfähigkeit vorliege.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `M. F.`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_184`)


Aufgrund jenes Befundes sei festgestellt worden, dass die  sozialen Interaktionen von M. F. stark eingeschränkt und starke soziale Unsicherheiten  verbunden mit sozialem Rückzug erkennbar seien.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_186`)


Um den beiden mangelhaften Vorgutachten zusätzlich inhaltlich entgegenzutreten, habe die  Antragstellerin ein Privatgutachten des allgemein beeideten und gerichtlich zertifizierten  Sachverständigen für Nerven- und Geisteskrankheiten Irene Pfleger …, eingeholt und lägen  demnach sowohl der Grad der Behinderung als auch die Minderung der Erwerbstätigkeit von  M. F. deutlich über 50 %.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Irene Pfleger`(person)
- `M. F.`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_196`)


Zusätzlich bestünden weitere psychische Störungen (Angststörungen,  Zwangsstörungen, depressive Störungen), die über eine Begleitsymptomatik hinausgehen  würden wie auch somatische, also den körperlichen Zustand von M. F. umfassende,  Krankheitsbilder (vgl. 8. Diagnosen;

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_208`)


Hinsichtlich der gesetzlichen Voraussetzungen zur Gewährung erhöhter Familienbeihilfe seien  jene gutachterlichen Erhebungen wie folgt zu bewerten:  Nach Zitierung der §§ § 8 Abs 4 FLAG 1967 und 10 Abs 3 FLAG 1967 führte die Bf weiters aus,  dass die tiefgreifenden neuropsychologischen Entwicklungsstörungen von M. F. als dauerhaft  anzusehen seien und jedenfalls über einen zukünftigen dreijährigen Zeitraum hinausgehen  würden.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_12`)


Am 7. Juni 2022 langte beim Finanzamt die Geburtsurkunde von S. sowie eine Kopie des  Mutter-Kind-Passes ein.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_17`)


Am 3. Oktober 2022 wurde vom (nunmehr) steuerlich vertretenen Bf. ein Vorlageantrag an  das Bundesfinanzgericht (BFG) gestellt und gleichzeitig die Verzichtserklärung der  Kindesmutter, die Reisepasskopie und eine Kopie des Aufenthaltstitels von S. vorgelegt.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_102`)


Korrespondierend hierzu ist davon auszugehen, dass der ständige Aufenthalt von S. in diesem  Zeitraum überwiegend in Serbien gelegen ist.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_103`)


Das BFG geht daher in freier Beweiswürdigung davon aus, dass der Mittelpunkt der  Lebensinteressen der Gattin des Bf. und der ständige Aufenthalt von S. bis Oktober 2021 in  Serbien gelegen ist.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_59`)


Im Übrigen ist andererseits zu bemerken, dass die Bf auch im Jänner 2022 nach dem  vorliegenden Sachverhalt keinen Anspruch auf Familienbeihilfe für K. hatte;

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_19`)


Arztbrief vom 4. Juli 2022 der Gruppenpraxis X.:  T. leidet an Panikstörung, Vd.a. somatoforme Störung und Insomnie (Anamnese: Vorstellung  aufgrund von zunehmenden Panikattacken und Vd.a. somatoforme Störung, Beginn der  Symptome im November 2021)  Arztbrief von Dr. H.:  Beginn der Panikattacken und der krankheitsbedingten Symptome November 2021  Fachärztlicher Befundbericht von Dalibor Thübel vom 21. April 2022:  T. leidet an einer Panikstörung und mittelgradigen depressiven Episoden  Folgende Unterlagen betreffend den Schulbesuch von T. betreffend den Streitzeitraum wurden  vorgelegt:  Im Wintersemester 2020/21 wurden folgende Leistungen erbracht:  2 von 11 Seite 3 von 11

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. H.`(person)
- `Dalibor Thübel`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_21`)


Im Wintersemester 2021/22 wurden folgende Leistungen erbracht:    Im Sommersemester 2022 wurden von T. folgende Leistungen erbracht:    Wintersemester 2022/23  Semesterzeugnis  3 von 11 Seite 4 von 11

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_74`)


Das Finanzamt ging davon aus, dass die Bf. zu Unrecht für ihre Tochter für den Streitzeitraum  Juni 2021 bis August 2022 Familienbeihilfe und Kinderabsetzbeträge bezog, da laut  vorliegender Semesterzeugnisse des BRG für Berufstätige in *** die Leistungen von T. im  Wintersemester 2020/21 in sämtlichen angeführten Gegenständen mit "nicht beurteilt"  beurteilt wurden.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_89`)


Die Schulausbildung hat auch nicht die volle Zeit von T. beansprucht, da sie im Wintersemester  2021/22 sowie Sommersemester 2022 lediglich in Gegenständen im Umfang von sechs bzw.  fünf Wochenstunden beurteilt wurde.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  des Bernhard Voronov, Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich, vom 3. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 22. April 2022, betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe vom 31. Jänner 2022 für S., V.nr. Nr., ab Jänner 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Bernhard Voronov`(person)
- `Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_34`)


Er und seine Ex Frau hätten eine Doppelresidenz für S., was bedeute, dass  dieser von Montag bis Montag durchgehend bei ihm und seiner Ex-Frau sei.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_40`)


Gemäß dem Beschluss des Bezirksgerichts Innere Stadt Wien vom 31. Dezember 2021 sei für  die Betreuung von S. das Modell der Doppelresidenz gewählt worden.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_52`)


Das Bundesfinanzgericht ersuchte den Bf. mit Vorhalt vom 14. September 2023, die  überwiegende Zugehörigkeit von S. zu seinem Haushalt binnen einem Monat ab Zustellung des  Schreibens durch geeignete Beweismittel nachzuweisen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_56`)


Für die Betreuung von S. wurde das Modell der Doppelresidenz gewählt. Der Hauptwohnsitz  von S. wurde bei der Kindesmutter festgelegt.

**False Positives:**

- `S.` — no gold match — likely missing annotation
- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_57`)


Der Hauptaufenthalt von S. wurde laut Beschluss (S. 18) bei der Kindesmutter belassen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_60`)


Beweiswürdigung:  Der Bf. beantragte die Teilung der Familienbeihilfe mit der Begründung, dass er und seine Ex- Gattin sich die Betreuung von S. zu je 50% teilen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_63`)


Die Festlegung des Hauptaufenthaltes von S. bei der Kindesmutter wurde im Beschluss damit  begründet, dass bei gemeinsamer Obsorge und Betreuung des Kindes zu gleichen Teilen die  Festsetzung eines Hauptaufenthalts (lediglich) als nomineller Anknüpfungspunkt für andere  Rechtsfolgen diene, deren Grundlage ein bestimmter Aufenthaltsort sei, wie eben für die  Bestimmung des Hauptwohnsitzes des Kindes im Sinn des Melderechts oder die Geltend- machung von Familien- (vgl § 2 Abs 2 FamLAG) und Wohnbeihilfe.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_66`)


Unter Pkt. 3. wurde festgelegt, dass für S. die hauptsächliche Betreuung pro forma im Haushalt  der Mutter stattfindet, wobei mit dieser Festlegung keine weitergehenden Rechte  einhergehen, insbesondere nicht das Aufenthaltsbestimmungsrecht.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_115`)


Eine derartige einheitliche Wirtschaftsführung im Rahmen einer Wohngemeinschaft bestand  im Beschwerdezeitraum sowohl beim Vater (Bf.) als auch bei der Mutter von S..  Betreuung in mehreren Haushalten

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_146`)


Aufgrund des oben zitierten Gerichtsbeschlusses (Beschluss vom 31.12.2021), wonach S. bei  der Kindesmutter seinen hauptsächlichen Aufenthalt hat sowie der Tatsache, dass der Bf. (trotz  Vorhalts des Bundesfinanzgerichts) keine Beweise für die überwiegende  Haushaltszugehörigkeit von S. (während des strittigen Zeitraums) bei ihm vorgelegt hat,  gelangt das erkennende Gericht in freier Beweiswürdigung gemäß § 167 BAO zu dem Ergebnis,  dass der Abweisungsbescheid vom 22. April 2022 sowie die Beschwerdevorentscheidung des  Finanzamts vom 10. Juni 2022 rechtsrichtig waren.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_147`)


Aus diesem Grunde hat der Bf. im Streitzeitraum für S. keinen Anspruch auf Familienbeihilfe im  Sinne des § 2 Abs. 2 FLAG 1967 oder auf Kinderabsetzbeträge.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_12`)


Bis Juni 2020 wurde die Familienbeihilfe von der leiblichen Mutter bezogen, ab Juli 2021 bezog  der leibliche Vater die Familienbeihilfe für L.  Strittig ist die Höhe des Familienbonus Plus 2020 und 2021 für die Stieftochter L.   2.

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_324`)


a) A.  Folgende Gutschriften wurden gewährt, wobei wir die Darstellung aus dem E-Mail von A. vom  21.2.2023 - welches wir als Anlage 1 übermitteln - der Authentizität halber übernehmen:    Die Gutschriften und USt-Beträge können daher wie folgt zusammengefasst werden:  22 von 65 Seite 23 von 65

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_325`)


Jahressummen (bezogen auf das Gutschriftsdatum):    Dem Grunde nach besteht für die Jahre 2010 bis 2017 daher Übereinstimmung zwischen den  Beträgen laut unserem Klienten und den von A. bestätigten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_406`)


Nach Beschwerde vom 15.11.2022 wurde in der Bescheidbegründung zu den  Beschwerdevorentscheidungen betreffend Umsatzsteuer 2017 und 2018 vom 12.12.2022  Folgendes ausgeführt (Verf67 auszugsweise):  …  Mit Vorhaltsbeantwortung vom 15.3.2023 wurden seitens der Bf. (wh.) die A. Rabatte iHv EUR  3.286.675,77 (2017) und EUR 769.816,61 (2018) anerkannt - weiters jedoch im Anhang der  Vorhaltsbeantwortung vom 15.3.2023 nunmehr eine Aufstellung zusätzlich gewährter  nachträglicher Rabattgutschriften von T. iHv netto EUR 2.614.850,80 (2017) und EUR  1.956.421,48 (2018), welche zu weiteren § 16-Berichtigungen/ 20%

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_420`)


Die hohen Kosten bei Handynutzung im Drittland kann man auch noch anhand der derzeitigen  Preise erkennen, so ist auf der Homepage von A. bzw. M. ersichtlich, dass ein abgehendes  29 von 65 Seite 30 von 65

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_448`)


nach Offenlegung von T.- -Gutschriftsbeträgen im Anhang der  Vorhaltsbeantwortung vom 15.3.2023 (siehe P1.), welche zu weiteren § 16 Berichtigungen iHv  EUR 522.970,16 (2017) und EUR 391.284,30 (2018) führen und in die Blg. “ Korr./bea.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_455`)


Mit Schreiben der Bf. vom 27. Juli 2023 (OZ. 94) wurde der Vorhalt des Bundesfinanzgerichts  vom 27. Juni 2023 (OZ. 87) wie folgt beantwortet:  „1. Keine Bekanntgabe von Rabatten durch T.:  …  2. Zuordnung der Gutschrift von A. für 2012:  …  3.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_496`)


Weiters wird in Hinblick auf die (Un-)Glaubwürdigkeit des bf. Vorbringens auch auf folgenden  Umstand Bedacht zu nehmen sein:  Es wurde erst im Frühjahr 2023 für den TADIG-Code der Bf. im Jahr 2014 eine (weitere)  Umsatzsteuerberichtigung (=Vorsteuerberichtigung wegen nachträglich gewährter Rabatte  gem. § 16 UStG 1994) durch/von A. iHv EUR 429.494,33 ho. bekannt.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_733`)


Die nunmehrige Zuordnung zu einem anderen Jahr wird von T. nicht begründet.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_351`)


Siehe hiezu Pkt. b.3.  Die Verordnung für A.i. Enzyme aus dem Jahr 2014 ist kein tauglicher Nachweis für die  medizinische Notwendigkeit der A.i.-Enzyme Mitte des Jahres 2013.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_361`)


Über die Beschwerde wurde erwogen:  Die Aufwendungen für A.i.-Enzyme samt Fahrtkosten werden nicht als ag Bel (ohne SB) zum  Abzug zugelassen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_374`)


Die Aufwendungen für A.i.-Enzyme werden nicht als ag Bel zum Abzug zugelassen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Standalone_Name_Verb_Context_Enhanced` 💣

**F1:** 0.001 | **Precision:** 0.018 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `2f2c4f03`  
**Description:**
Matches standalone names following verbs like 'beauftragt', 'verurteilt', 'genannt' where the person is the object.

**Content:**
```
(?:beauftragt|verurteilt|genannt|namentlich|als)\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:[ \t]+[A-Z][a-z]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)?\b(?=[,]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.018 | 0.001 | 0.001 | 55 | 1 | 54 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 54 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden R1, die RichterinR2 sowie die  fachkundigen Laienrichter R3 und R4 in der Beschwerdesache C als Gottfried Kamperschroer, Allentsgschwendt 4W, 8741 Allersdorf, Österreich,  vertreten durch Schmidt & Schmidt KG, Bahnzeile 10, 2130 Mistelbach, über die Beschwerde  vom 13. Dezember 2012 gegen die gem. § 200 Abs. 2 BAO endgültigen Bescheide des  Finanzamtes Gänserndorf Mistelbach (nunmehr Finanzamt Österreich) vom 4. Oktober 2012  betreffend Einkommensteuer 2005 bis 2008, Steuernummer 84-352/6923, nach  Durchführung einer mündlichen Verhandlung am 10. Juni 2021 in Anwesenheit der  Schriftführerin S1, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gottfried Kamperschroer` | `Gottfried Kamperschroer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Allentsgschwendt 4W, 8741 Allersdorf, Österreich` (address)
- `Schmidt & Schmidt KG` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamt Österreich` (organisation)
- `84-352/6923` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_47`)


Dem Gesetzgeber steht es dabei auch frei, eine solche  Steuer als Objektsteuer, dh. unabhängig von den persönlichen Verhältnissen des  Grundeigentümers, auszugestalten (vgl. VfGH 06.10.2010, B 298/10).

**False Positives:**

- `Objektsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_423`)


Die Union ist nicht nur  eine Wirtschaftsgemeinschaft, sondern noch vielmehr eine Wertgemeinschaft, in der auch die  Tätigkeit als Entwicklungshelfer, die der Verwaltungsgerichtshof zutreffend als „vornehmlich  idealistisch motiviert“ bezeichnet hat, diese Anerkennung durch die europäische Öffentlichkeit  zu Teil wird.

**False Positives:**

- `Entwicklungshelfer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_58`)


Es ist daher von einer Personenversicherung auszugehen, welche nicht ausschließlich die  Berufsunfähigkeit infolge eines typischen Berufsrisikos abdeckt und dementsprechend nicht als  Werbungskosten, sondern lediglich als Sonderausgaben gemäß § 18 Abs. 1 Z. 2 EStG 1988 im  Rahmen der Höchstbeträge (zu einem Viertel), geltend gemacht werden kann.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_279`)


Gleiches gilt für Anschaffungen, vermutlich als Bastelmaterial, wie Pickerl, Filzkugeln, Leimholz,  Papier, Blätter, Klammern, Umschläge, Zeichenpapier.

**False Positives:**

- `Bastelmaterial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_190`)


Soweit Rechnungen zur N. in Erscheinung treten sind diese als Scheinrechnungen  bzw. Nichtleistungsrechnungen zu werten, d.h. als Rechnungen, welche keinen tatsächlichen  Leistungsaustausch widerspiegeln.

**False Positives:**

- `Rechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_352`)


Allein die Tatsache, dass die Finanzstrafbehörden bei diversen  Scheinfirmen mehrere Hundert „Scheinrechnungen“ gefunden wurden, die – da die  angeblichen Bau-GmbHs keine Unternehmen im Sinne des Umsatzsteuergesetzes darstellen –  nicht als Aufwand anzuerkennen waren, reicht dem Senat als Grundlage, dass es sich  tatsächlich um Scheinfirmen handelt. Es wird zwar nicht bezweifelt, dass tatsächlich Umsätze  ausgeführt wurden, jedoch nicht durch die unter den Namen der Scheinfirmen angegebenen  Unternehmen, da diese nicht existent sind.

**False Positives:**

- `Grundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Masseverwalterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_278`)


a VO  883/2004 in deren Geltungsbereich fällt. Das Kindergeld falle als Leistung, die die Kosten für  den Unterhalt von Kindern verringern soll, unter den Begriff "Familienleistung" i. S. d. VO  883/2004 (vgl. EuGH 15.

**False Positives:**

- `Leistung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_90`)


Gegen den (zweiten) Abweisungsbescheid vom 6.10.2020 betreffend den Zeitraum September  2015 – April 2018 erhob die Bf am 2.11.2020 abermals Beschwerde, die mit  Beschwerdevorentscheidung vom 27.1.2021 abgewiesen wurde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_890`)


Auf Grund der Verwendung der österreichischen  Umsatzsteuer-Identifikationsnummer und der bisherigen Beurteilung des Erwerbsvorgangs der  Bf. als Inlandsumsatz, wird das Mehrwertsteueraustauschsystem durch Abgabe einer  entsprechenden Zusammenfassenden Meldung durch den Lieferanten nicht ausgelöst, sodass  der tatsächliche Erwerbstaat vom Erwerb der Bf. im Bestimmungsstaat keine Kenntnis  erlangen konnte.

**False Positives:**

- `Inlandsumsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_87`)


Im Nachhinein erschien für die Bf. dieser Kauf nicht nur im Hinblick  auf die falsche Staatszugehörigkeit als Fehlinvestition, die Besteuerung eines Kfz sei in  der Schweiz vorteilhafter (Nova, Umsatzsteuer, motorbezogene Kfz-Steuer).

**False Positives:**

- `Fehlinvestition` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Verlassenschaftskuratorin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Silvia Gebhart`(person)
- `Erwin Döpkemeier`(person)
- `Minithal 3, 5360 Markt, Österreich`(address)
- `Mag Kerstin Friedrich`(person)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamt  Österreich`(organisation)
- `02-365/4052`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_36`)


2. MRT des Schädels des Instituts für Digitals Bilddiagnostik, St Pölten vom 10.09.1992,  Ergebnis: „Bei der Asymmetrie hinsichtlich der Seitenventrikel ist in erster Linie an eine  Normvariante zu denken.

**False Positives:**

- `Bilddiagnostik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alois Kleynsteuber`(person)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich`(address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`(organisation)
- `FA Wien 9/18/19  Klosterneuburg`(organisation)
- `79-708/0061`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_71`)


Nach den Vorgaben der (unionsrechtlichen) Mehrwertsteuersystemrichtlinie (in der Folge kurz:  MwStSystRL) hingegen gilt als Steuerpflichtiger, wer eine wirtschaftliche Tätigkeit unabhängig  von ihrem Ort, Zweck und Ergebnis selbstständig ausübt (Art 9 Abs 1 Unterabsatz 1  MwStSystRL).

**False Positives:**

- `Steuerpflichtiger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_74`)


Falls sie solche Tätigkeiten ausüben oder Umsätze bewirken,  gelten sie - nach Unterabsatz 2 - für diese Tätigkeiten oder Umsätze jedoch als Steuerpflichtige,  sofern eine Behandlung als Nichtsteuerpflichtige zu größeren Wettbewerbsverzerrungen  führen würde.

**False Positives:**

- `Steuerpflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Insolvenzverwalter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Mittel-Verlag`(organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich`(address)
- `Dr. Stephan Riel`(person)
- `Finanzamtes Österreich`(organisation)
- `44-993/1626`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_177`)


Der VwGH beurteilt die Vorschreibung von Lohnsteuer im Haftungswege in ständiger  Rechtsprechung als Sammelbescheid, bei dem die einzelnen Abgaben durch die Anführung der  Abgabenschuldner (Arbeitnehmer) und der betroffenen Monate klar individualisiert werden  (VwGH 17.

**False Positives:**

- `Sammelbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_60`)


Beweis: STB1; als Zeugen, STB2, als Zeugen;

**False Positives:**

- `Zeugen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Zeuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_32`)


jedem einzelnen Gewerk die freie Entscheidung hatten,  dieses an die Nieder Uniost GmbH als Generalunternehmen, oder in Eigenregie zu vergeben.

**False Positives:**

- `Generalunternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nieder Uniost GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_52`)


3. die sonstigen Leistungen aus der Tätigkeit als Rechtsanwalt, Patentanwalt, Steuerberater,  Wirtschaftsprüfer, Sachverständiger, Ingenieur, Aufsichtsratsmitglied, Dolmetscher und  Übersetzer sowie ähnliche Leistungen anderer Unternehmer;

**False Positives:**

- `Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_37`)


Bei Abwägung der Angaben des anzeigelegenden Organs und der Rechtfertigung des Bf. als  Beschuldigter, der in der Wahl seiner Verteidigung völlig frei sei, könne der angezeigte Sach- verhalt als erwiesen angesehen werden.

**False Positives:**

- `Beschuldigter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_27`)


Bei Abwägung der schlüssigen und nachvollziehbaren Angaben der Zulassungsbesitzerin und  Ihrer Rechtfertigung als Beschuldigter, der in der Wahl seiner Verteidigung völlig frei ist, kann  der angezeigte Sachverhalt als erwiesen angesehen werden.

**False Positives:**

- `Beschuldigter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_147`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Konsequenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_282`)


Dem mit dem zweiten Gutachten betrauten Sachverständigen, Dr. Dok2, Arzt für Allge- meinmedizin, lagen bei der Erstellung seines Gutachtens vom 6. November 2020 folgende  Befunde bzw. Unterlagen vor:  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Konsequenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_315`)


Das FA hat zu den streitentscheidenden Fragen (Frage der Möglichkeit einer Nachnutzung der  in einem Musterhauspark stehenden Häuser nach dem Ende der Verwendbarkeit als  Musterhaus, Frage der fremdüblichen Mietzinse für 9 in Österreich und Deutschland  stehenden Musterhäuser) nicht einmal im Ansatz nachvollziehbar dokumentierte Ermittlungen  durchgeführt.

**False Positives:**

- `Musterhaus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/141161.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141161.1_16`)


Dass  die vom Ehepartner getrennt lebenden, oder geschiedenen Personen, weder als Arbeitnehmer,  noch als Familienangehörige zu betrachten sind.

**False Positives:**

- `Arbeitnehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141221.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141221.1_98`)


Die belangte Behörde wertete allerdings das erste Mail des Bf. vom 30. Dezember 2022, mit  dem er sich zum ersten Mal gegen die Strafverfügung wendet, nicht als Beschwerde, sondern  erst eines der vielen späteren mails vom 11. Jänner 2023, mit dem der Bf. erneut die  Unrichtigkeit seiner neuerlichen Zahlungsverpflichtung zum Ausdruck bringen will und um  8 von 10 Seite 9 von 10

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_41`)


Daher besteht kein Raum für Annahme, dass eine Zustellbevollmächtigung, auf die sich der  Bevollmächtigte im Wege von FinanzOnline gegenüber der Abgabenbehörde beruft, auch in  einem Verfahren zur Einhebung von Abgaben (mit Ausnahme der Entrichtung im Wege der  Überweisung mittels Electronic-Banking), namentlich im Verfahren über die Inanspruchnahme  als Haftungspflichtiger, gelten sollte.

**False Positives:**

- `Haftungspflichtiger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_8`)


Darin beantragte er die Berücksichtigung von  Pendlerpauschale und Pendlereuro und Sozialversicherungsbeiträgen sowie folgender Kosten  als Werbungskosten für seine beruflichen Tätigkeiten als Schilehrer, Lkw-Lenker und  Hausmeister:  1 von 11 Seite 2 von 11

**False Positives:**

- `Schilehrer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_17`)


Die Kommanditisten erhielten einen Anteil von  185% ihrer Einlage unabhängig vom Beteiligungsverhältnis als Verlustzuweisung, und nach  2 von 35 Seite 3 von 35

**False Positives:**

- `Verlustzuweisung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_134`)


Gesellschafter der Bf sind die *Kpl* GmbH als  Komplementärin und eine Vielzahl von Personen (167) als Kommanditisten, wobei im  Firmenbuch nur die *TH-Kdt* GmbH als Kommanditistin aufscheint  („Treuhandkommanditistin“), die neben ihrem eigenen Kommanditanteil für sämtliche  Kommanditisten („Treugeber“) die Anteile treuhändig verwaltet.

**False Positives:**

- `Kommanditisten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_261`)


In diesem Zusammenhang – wie auch ganz allgemein in Hinblick auf die Doppelstöckigkeit der  Beteiligung – ist auch die Rechtsprechung zur Unterbeteiligung (Jakom/Peyerl, EStG 2022, § 23  Rz 154 f) interessant: Diese führt zu Einkünften als Mitunternehmer, und zwar unabhängig  davon, ob die Unterbeteiligung gegenüber der Gesellschaft offengelegt ist (VwGH 15.1.1991,  87/14/0053).

**False Positives:**

- `Mitunternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_390`)


Diese Sichtweise erscheint richtig, denn § 23 Abs 3 UmgrStG definiert Personengesellschaften  als Gesellschaften, bei denen die Gesellschafter als Unternehmer (Mitunternehmer) anzusehen  sind, womit der Begriff der Personengesellschaft mit dem der Mitunternehmerschaft  gleichgesetzt wird (266 BlgNR XVIII. GP, 32).

**False Positives:**

- `Gesellschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_239`)


Erhält der Stille  bei Beendigung der Gesellschaft einen Anteil an den stillen Reserven und am Firmenwert, gilt  er als Mitunternehmer, der betriebliche Einkünfte und nicht solche aus Kapitalvermögen im  Sinne des § 27 EStG erzielt. Ob eine atypisch stille Gesellschaft vorliegt, ist im Einzelfall nach  dem Gesamtbild der Verhältnisse, insbesondere nach den vertraglichen Vereinbarungen für  den Fall der Beendigung des Gesellschaftsverhältnisses, zu beurteilen (VwGH 22.10.86,  86/13/0092).

**False Positives:**

- `Mitunternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_21`)


Der Auskunftsbescheid vom 04.05.2015, zugestellt am 07.05.2015, beurteilte den dargestellten  Sachverhalt und die Bedingungen gem. Art. 9 DBA Österreich-Liechtenstein nicht als  Bedingungen, welche zwischen unabhängigen Unternehmen vereinbart werden würden.

**False Positives:**

- `Bedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/143615.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143615.1_117`)


Seit Herbst 2017 nutzte der BF die bislang vermietete Wohnung Adr 2 als Büro für die  Einkünfte als Terminplaner, die Einkünfte aus dem N Game sowie die Einkünfte aus der  Spekulation mit Fremd- und Kryptowährungen.

**False Positives:**

- `Terminplaner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/143615.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143615.1_196`)


Die Wohnung Adr 2  wurde anteilig für die Einkünfte als Terminplaner, die Einkünfte aus dem N Game sowie die  Einkünfte aus der Spekulation mit Fremd- und Kryptowährungen genutzt.

**False Positives:**

- `Terminplaner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/143615.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143615.1_307`)


Dass der BF für einen kurzen Zeitraum (ab Herbst 2017 bis ca. Mai 2019) eine bislang  vermietete Wohnung als nach außen nicht erkennbares Büro nicht nur für die neu  aufgenommene Tätigkeit als Terminplaner, sondern auch für die hier strittigen Tätigkeiten (N  Game, Spekulieren mit Fremd- und Kryptowährungen) genutzt hat bzw die Einkünfte aus dem  N Game in den Jahren 2015 und 2016 seine Haupteinnahmequelle waren, treten als für das  Vorliegen von gewerblichen Einkünften sprechende Umstände in den Hintergrund.

**False Positives:**

- `Terminplaner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/143615.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143615.1_316`)


Aufgrund des Umstandes, dass hinsichtlich der konkreten Nutzung der Wohnung Adr 2 Tkeine  Aufzeichnungen bestehen und aufgrund der getroffenen Feststellungen aber klar ist, dass die  Wohnung anteilig für die Einkünfte als Terminplaner, die Einkünfte aus dem N Game sowie die  Einkünfte aus der Spekulation mit Fremd- und Kryptowährungen genutzt wurde, erscheint die  vom BF gewählte Berücksichtigung von Betriebsausgaben entsprechend der erzielten  Einnahmen – ausgehend von der vorhin angeführten – Judikatur durchaus als sachgerecht.

**False Positives:**

- `Terminplaner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_29`)


Im Vorlageantrag brachte der Revisionswerber vor, das Gesetz verlange für die Steuerfreiheit  keinesfalls den Erwerb von Aktien oder sonstigen Wertpapieren als Bedingung, vielmehr  umfasse die Begünstigung Optionen auf den Erwerb jeglicher Art von Beteiligungen.

**False Positives:**

- `Bedingung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_149`)


Somit stellen wir im Auftrag unserer Mandantin die  ANTRÄGE  - auf Unterlassung einer Beschwerdevorentscheidung und unmittelbare Vorlage dieser  Beschwerde an das Bundesfinanzgericht,  - auf Entscheidung über die Beschwerde durch den gesamten Senat,  - auf Durchführung einer mündlichen Verhandlung,  -  auf Aussetzung der Einhebung gemäß § 212a BAO im Betrag von € 525.346,30 bis zur  bescheidmäßigen Erledigung dieser Beschwerde,  - auf Aufhebung bzw. auf Abänderung des Umsatzsteuerbescheides für das Jahr 2015  vom 09.9.2016 und Anpassung der Umsatzsteuer an das tatsächliche Ergebnis unter  Berücksichtigung der entrichteten Einfuhrumsatzsteuer als Vorsteuer,  - auf Aufhebung bzw. auf Abänderung des Bescheides über die Festsetzung von  Umsatzsteuer für 03/2016 vom 09.09.2016 und Anpassung der Umsatzsteuer an das  tatsächliche Ergebnis unter Berücksichtigung der entrichteten Einfuhrumsatzsteuer als  Vorsteuer,  - auf Aufhebung der Bescheide über die Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer für die Jahre 2010-2014 vom 12.9.2016 und betreffend Festsetzung von  Umsatzsteuer für 04/2016 vom 09.09.2016.

**False Positives:**

- `Vorsteuer` — no gold match — likely missing annotation
- `Vorsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_150`)


- Auf Aufhebung bzw. auf Abänderung der Umsatzsteuerbescheide für die Jahre 2010 bis  2014 vom 12.9.2016 und Anpassung der Umsatzsteuer an das tatsächliche Ergebnis  unter Berücksichtigung der entrichteten Einfuhrumsatzsteuer als Vorsteuer,  - auf Aufhebung bzw. auf Abänderung des Bescheides über die Festsetzung von  Umsatzsteuer für 04/2016 vom 09.09.2016 und Anpassung der Umsatzsteuer an das  tatsächliche Ergebnis unter Berücksichtigung der entrichteten Einfuhrumsatzsteuer als  Vorsteuer.

**False Positives:**

- `Vorsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_63`)


Das Finanzamt qualifizierte die Fahrt als Einkaufsfahrt, das Geschäft 1 sei kein  Brillenfachgeschäft.

**False Positives:**

- `Einkaufsfahrt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_426`)


Auch wenn es durchaus glaubwürdig ist,  dass keine exakte Feststellung der Anzahl der unternehmerischen Kunden möglich ist, verfügt  die Beschwerdeführerin über Daten die eine Schätzung erleichtern würden (Gesellschaft oder  natürliche Person als Kunde, Anzahl der Telefonnummer, Häufigkeit der Aufenthalte in  Österreich, etc.).

**False Positives:**

- `Kunde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_702`)


20% der Umsätze entfallen auf unternehmerische Leistungsempfänger als  Kunden, weshalb es bei diesen zum Übergang der Steuerschuld auf den  Leistungsempfänger kommt (KZ021).

**False Positives:**

- `Kunden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_248`)


Der Bf. bezahlte im Streitjahr 2020 betreffend Beiträge (Position f/2):   25,00 € an karitativeOrganisation als Mitgliedsbeitrag, wobei der Bf. im Vorstand des  Vereines war.

**False Positives:**

- `Mitgliedsbeitrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_133`)


Vor dem Hintergrund des objektiven Nettoprinzip erscheine die Ausgestaltung der EKB-S  insbesondere in folgenden zwei Aspekten verfassungswidrig:  Zunächst verwende der EKB-S, im Gegensatz zum Energiekostenbeitrag für fossile  Energieträger (EKB-f), nicht den Gewinn der vergangenen Jahre als Bemessungsgrundlage,  sondern die realisierten Erträge, die ein Beitragsschuldner für den Verkauf und die Lieferung  von Strom in der Union erhalte.

**False Positives:**

- `Bemessungsgrundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146608.1_39`)


A. AMC-Aktien, APE-Aktien, Qualifikation als Sonderdividende

**False Positives:**

- `Sonderdividende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_367`)


2. Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus dem vorgelegten Verwaltungsakt, den angeführten  Bescheiden und Ergänzungsvorhalten, dem Bericht gemäß § 150 BAO vom 1.07.2016, dem  Bauakt, den Mietverträgen betreff Wohnung   +) Top 1 vom 1.11.2012 (unterschrieben mit 1.11.2012) und 1.10.2014 (unterschrieben mit       1.11.2014) jeweils mit Mieter M.M.A.,   +) Top 3 vom 1.11.2012 und 1.10.2014 jeweils mit M.M.B als Mieterin,   +) Top. 4 vom a) 1.08.2012 mit Mieterin M.M.B 2 (unterfertigt mit 7.09.2012),                            b) 19.01.2014 mit Fremdmieter R.A. vom 20.01.2014;

**False Positives:**

- `Mieterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.M.A.`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_22`)


Der EKB-S verwende im  Gegensatz zum Energiekostenbeitrag für fossile Energieträger (EKB-F) nicht den  Gewinn der vergangenen Jahre als Bemessungsgrundlage, sondern die erzielten  Erträge.

**False Positives:**

- `Bemessungsgrundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_69`)


Die Bf. mietete mit Vereinbarung vom 30.3.2017 ein ca. 110 m2 großes Geschäftslokal im  Erdgeschoss der Liegenschaft in Adresse1 als Untermieterin, bestehend aus 2 Büroräumen (ein  großer mit ca. 52 m2 und ein weiterer mit ca. 10 m2 Fläche), einem Besprechungszimmer (ca.  22 m2), einer Küche (ca. 9,5 m2), sowie sanitären Einrichtungen.

**False Positives:**

- `Untermieterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Academic_Title_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `57c8fc3b`  
**Description:**
Matches persons with complex academic titles, ensuring the match stops before non-name words.

**Content:**
```
\b(?:VetR\s+Hon\.-Prof\.|Hon\.-Prof\.|Univ\.-Prof(?:\.in)?|Priv\.-Doz\.|Priv\.-Doz\.in|MedR|Bakk\. iur\.|Bakk\. phil\.|LLM|LL\.M\. M\.B\.L\.|BSc|RA|Ing\.|Mag\.|Mag\.a|Dr\.|Dr\.in|DDr\.|DDr\.in|OStR|RgR|OMedR|Dipl\.-Ing\.|StR|KommR|Techn R|PhD)\s+(?:VetR\s+Hon\.-Prof\.|Hon\.-Prof\.|Univ\.-Prof(?:\.in)?|Priv\.-Doz\.|Priv\.-Doz\.in|MedR|Bakk\. iur\.|Bakk\. phil\.|LLM|LL\.M\. M\.B\.L\.|BSc|RA|Ing\.|Mag\.|Mag\.a|Dr\.|Dr\.in|DDr\.|DDr\.in|OStR|RgR|OMedR|Dipl\.-Ing\.|StR|KommR|Techn R|PhD)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,? \s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)? \b(?=[,;:\s]|$)
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

## `Legal_Context_Representative_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8404815a`  
**Description:**
Matches representatives in phrases like 'vertreten durch [Name]', capturing ONLY the name part.

**Content:**
```
(?:vertreten durch)\s+(?:Mag\.a?|Dr\.in?|DDr\.|DDr\.in|OStR|Univ\.-Prof(?:\.in)?|Priv\.-Doz\.|Priv\.-Doz\.in|MedR|Bakk\. iur\.|Bakk\. phil\.|LLM|LL\.M\. M\.B\.L\.|Hon\.-Prof\.|BSc|RA|Ing\.)?\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:,|$))
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

## `Mag_a_Title_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cbf2e3e9`  
**Description:**
Matches persons with 'Mag.a' title, stopping before non-name words.

**Content:**
```
\bMag\.a(?:\s+Priv\.-Doz\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:\s*,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Single_Letter_Name_Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a7d2070f`  
**Description:**
Matches single letter names or initials with periods (e.g., 'M.', 'H.') in legal contexts like 'für M.' or 'des H.'.

**Content:**
```
(?:für|des|von)\s+([A-Z]\.)\b(?=[,\s]|$)
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

## `Quote_Name_Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d01bc353`  
**Description:**
Matches names appearing inside quotes, often used for addresses or specific references.

**Content:**
```
(?:„|“)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)(?:„|”)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_590`)


In  den „Transferred Account Procedures“ werden alle „Call Detail Records” einer gewissen Periode  inklusive der auf die einzelnen Roamingleistungen entfallenden Kosten zusammengefasst.

**False Positives:**

- `Call Detail Records` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Party_Name_NoTitle_Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ab60d83e`  
**Description:**
Matches party names in phrases like 'in der Beschwerdesache [Name]' where the name might not have a title immediately preceding it, capturing single or multi-word names.

**Content:**
```
(?:in der Beschwerdesache|Beschwerdesachen)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*)\b(?=[,;:\s]|$)
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

## `Standalone_Name_Professional_Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ceb405ad`  
**Description:**
Matches standalone names following professional role indicators like 'Psychiater', 'Arzt', etc.

**Content:**
```
(?:Psychiater|Arzt|Sachverständiger|Sachverständige|Gutachter|Gutachterin)\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_82`)


Unser Mandant wurde vom Gericht gebeten, trotz Austragung  aus der Sachverständigentätigkeit als Sachverständiger Gutachten zu übernehmen, um die  gerichtlichen Verfahren nicht hinauszuzögern.

**False Positives:**

- `Gutachten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_318`)


 keine Versuche des Bf. und seiner Ehegattin zu ersehen waren, anstatt der in (weit  zurückliegenden Verschreibungen) verordneten, laut Angaben des Bf. und seiner  Ehegattin aber unverträglichen Medikamente vom verschreibenden Arzt ein  Alternativprodukt zu bekommen,    für den Beschwerdezeitraum kein Mangelbefund der Vitamine für den Bf. und seine  Ehegattin dokumentiert ist,    für das BFG nicht anzunehmen ist, dass der Arzt Dr. B, der die Thrombopenie erkannt  hat, dem Bf. ein ihn schädigendes Medikament - Cetebe - verschrieben haben wird,    der Bf. und seine Ehegattin in Vorverfahren wohl für das Kind, nicht aber für sich  Vitamine geltend machten (siehe BFG GZ. RV/4100524/2017 (E 2008 bis 2010), und BFG  GZ. RV/4100090/2020, intern gestellt (E 2012)), und   der Bf. und seine Ehegattin aufgrund der Thematisierung in den Vorverfahren über die  entsprechenden Voraussetzungen des Nachweises für Vitamine und  Nahrungsergänzungsmittel bei der Veranlagung 2019 Bescheid wussten.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. B`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Dr. B`(person)
- `BFG`(organisation)
- `BFG`(organisation)

</details>

---

## `Single_Letter_Name_Context_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `144fe43a`  
**Description:**
Matches single letter names or initials with periods (e.g., 'M.', 'Dr. B.') in legal contexts like 'namens M.' or 'Zeuge M.'.

**Content:**
```
(?:namens|Zeuge|Zeugin|als|f\u00fcr|des|von)\s+([A-Z]\.)\b
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

## `StR_Title_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c70ee9aa`  
**Description:**
Matches persons with StR title which was previously missed.

**Content:**
```
\bStR\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*)
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

## `Quote_Name_Context_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a6c445dc`  
**Description:**
Matches names inside quotes, capturing full name.

**Content:**
```
(?:„|")( [A-Z][a-zäöüßéáüé]+(?: [A-Z][a-zäöüßéáüé]+)+ )(?=„|")
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

## `Title_KommR_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `22b90e67`  
**Description:**
Matches persons with KommR title (Kommerzialrat).

**Content:**
```
\bKommR\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*
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

## `Title_StR_Person_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6f51d63`  
**Description:**
Matches 'StR' preceded by other titles like 'Dipl. Kff.' to capture full compound title.

**Content:**
```
\b(?:Dipl\. Kff\. )?StR(?:in)?(?:\s+Priv\.-Doz\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Standalone_Name_Following_Role` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f9f22c3a`  
**Description:**
Matches standalone names following role indicators (Richter, etc.) where the title might be missing, capturing full name including suffixes.

**Content:**
```
(?:durch den Richter|durch die Richterin|Richter|Richterin|Geschäftsführer)\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+(?:van|de|von)\s+[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)?\b(?=[,]|$)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

**False Positives:**

- `Geschäftsführer Herr Albert Sengeisen` — partial — gold is substring of pred: `Albert Sengeisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albert Sengeisen`(person)
- `Starnberg Beratung GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dieter Brennscheid, Bakk. rer. nat. in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

**False Positives:**

- `durch den Richter Dieter Brennscheid` — positional overlap with gold: `Dieter Brennscheid, Bakk. rer. nat.`

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

## `Standalone_Name_Verb_Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4da58b29`  
**Description:**
Matches standalone names following verbs like 'betreiben', 'eingekauft', 'verkauft' where the person is the subject/object, capturing full name.

**Content:**
```
(?:betreiben|eingekauft|verkauft|verwaltet|geleitet|hat|ist|war)\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)+)\b(?=[,\s]|$)
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

## `VetR_Title_Person_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `77753cbb`  
**Description:**
Matches persons with VetR title, capturing FULL name including suffixes and compound names.

**Content:**
```
\b(?:VetR(?:\s+Hon\.-Prof.)?|Hon\.-Prof. VetR) \s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?: \s+[A-Z][a-zäöüßéáüé]+)*)
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

## `Specific_Name_Ebenho_Fixed` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a70ebc56`  
**Description:**
Matches specific entity 'Priv.-Doz. Ingolf Ebenho' and similar compound titles with space variations.

**Content:**
```
\bPriv\. -Doz\.\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*
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

## `HR_OStR_Context_Fixed` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `96780800`  
**Description:**
Matches 'HR OStR' followed by full name, stopping strictly before non-name words like 'Beschwerde'.

**Content:**
```
\bHR\s+OStR\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)+)(?=[,;:\s]|$)
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

## `Abbreviation_Person_Context_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `75445ecf`  
**Description:**
Matches specific person abbreviations like M.M.A. in context of company names or roles, ensuring full capture.

**Content:**
```
(?:GmbH\s*–|GmbH\s+|Geschäftsführer|führte)\s+([A-Z]\.[A-Z]\.[A-Z])\b
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

## `Title_ProfStR_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `91e9de54`  
**Description:**
Matches persons with 'Prof.StR' title, requiring at least two name words.

**Content:**
```
\bProf\.StR\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:\s*,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Herrn_Name_Context_Enhanced` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `db47eaca`  
**Description:**
Matches names preceded by 'Herrn' or 'Herr', capturing ONLY the name part, excluding the title.

**Content:**
```
(?:Herrn\s+|Herr\s+)(?!(?:Vizeleutnant|Oberleutnant|Leutnant|Hauptmann|Major|Oberst|Generalmajor|General|Feldwebel|Unteroffizier|Offizier|Soldat|Korporal|Gefreiter|Stabsgefreiter|Stabsunteroffizier|Stabsoffizier)\s+[A-Z])\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.|BA|MBA)?)?)?\b(?=[,;:\s]|$)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

</details>

---

## `Single_Letter_Name_Context_Enhanced_4` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0db5f3d9`  
**Description:**
Matches single letter names or initials with periods (e.g., 'N.R.') in legal contexts, ensuring the full initial sequence is captured.

**Content:**
```
(?:von|namens|Zeuge|Zeugin|als|für|des)\s+([A-Z]\.[A-Z]\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 14 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Marion Endrulat`(person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_16`)


Die  restlichen 5%-Anteile sind von V.A.  (=geschäftsführender Gesellschafter der Bf.) von  01.06.1990 bis 06.11.2007 treuhändisch für die Privatstiftung gehalten worden.

**False Positives:**

- `V.A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_21`)


Zu den Fleischlieferanten der Bf. zählten die Lemost-Handel GmbH unter der Geschäftsführung von E.St.  sowie die Dorfleitner+Ternis Versicherung GmbH unter der Geschäftsführung von K.F.St..  Bericht gemäß § 150 BAO vom 21.10.2009  Unter Tz.1ff.

**False Positives:**

- `K.F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)
- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_80`)


*) Printartikel: Laut Artikel von R.R. in der Zeitschrift Printartikel, würden laut Angaben des V.  A. ca. 150.000 A. Portionen pro Jahr umgesetzt werden.

**False Positives:**

- `R.R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_140`)


*) Widerspruch der Aussage von V.A. im Printartikel mit der Kalkulation am W- Platz: Bei der  Zahlennennung in der Öffentlichkeit würden immer nur die Verkaufszahlen sämtlicher drei  Betriebe akkumuliert.

**False Positives:**

- `V.A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_221`)


Ergänzung der Beschwerde vom 15.07.2010  In den in die Punkte "A) Mangelhaftigkeit des Verfahrens" und "B) Rechtswidrigkeit des  Inhalts", untergliederten Schreiben wurde der belangten Behörde unter Pkt. „A.1 Ignorieren  von Beweisanträgen" nach Zitierung des § 183 Abs.3 BAO und diesbezüglichen Zitaten aus dem  VwGH-Erkenntnis 96/17/0459 samt Ritz, BAO³, § 183 Tz.3 vorgehalten, die Anträge   – Einvernahme der Zeugen a) Z1 , Z2, b) Z3, c) (fälschlich als B.S. bezeichnete) Z4 und Z5, d) die  Bestellung eines Sachverständigen;

**False Positives:**

- `B.S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_833`)


Der als B.S. angeführte Zeuge könnte zwar zur Zubereitung und Größe des Fleischabschnitts  Angaben machen, jedoch ändert dies nichts an Eigenschaft des Fleischabschnitts in den  Streitjahren als variabler Kostenfaktor.

**False Positives:**

- `B.S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_57`)


Es stellt sich daher die Frage, ob es        stimmt, dass laut dem zum Zeitpunkt der Einräumung der Optionen noch maßgeblichen        Stock Incentive Plan von S.P. tatsächlich ALLEN Managern / Direktoren von        S.P. ab Grad 91 Stock Options zuerkannt worden sind.“

**False Positives:**

- `S.P.` — no gold match — likely missing annotation
- `S.P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_14`)


Die Bescheide  wurden adressiert an C.N. als Erbin des H.N..   Mit Schreiben vom 4. Mai 2017 und – in Erfüllung eines Mängelbehebungsauftrages mit Frist  bis zum 15. Mai 2017 – vom 11. Mai 2017 beantragte der steuerliche Vertreter der Bf. die  Aufhebung dieser Einkommensteuerbescheide gemäß § 299 BAO und die Erlassung neuer  Einkommensteuerbescheide, mit denen die Verluste aus der Vermietung des Geschäftslokales  anerkannt werden.

**False Positives:**

- `H.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_42`)


Nach Aussagen von S.N. sei das Lokal „total verdreckt, verstunken und verraucht“ gewesen.

**False Positives:**

- `S.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_63`)


Pächter war der Ehemann der Inhaberin  eines benachbart gelegenen italienischen Lokales, welches ebenfalls im Eigentum von H.N.  steht und von diesem vermietet wird.

**False Positives:**

- `H.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_68`)


Einer von der Bf. vorgelegten Aktennotiz des Rechtsanwaltes des H.N. vom 1.2.2013  ist zu entnehmen, dass S.N. bereits einen Immobilienmakler mit dem Verkauf des  Geschäftslokales beauftragt hat.

**False Positives:**

- `H.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_63`)


Betreff das Bauprojekt „Saunahaus“ auf dem Grundstück an der zuvor genannten Adresse     folgte dem an das Bauamt adressierten Baubewilligungsansuchen der Bf. vom 17.06.2014     eine Bauverhandlung in Anwesenheit des X.B. für den Bauführer und Planverfasser     Fa. Z-GmbH am 17.09.2014.

**False Positives:**

- `X.B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Role_Indicator_Person_NoTitle` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0959430a`  
**Description:**
Matches names following role indicators (Richter, Richterin) where the title might be missing, ensuring at least two words are captured.

**Content:**
```
(?:durch den Richter|durch die Richterin|Richter|Richterin|Gesch\u00e4ftsf\u00fchrer)\s+([A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)+)\b(?=[,\s]|$)
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

## `OSR_KommR_Context_Fixed` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4fb7d98d`  
**Description:**
Matches persons with compound titles like 'OSR KommR' followed by full names.

**Content:**
```
\b(?:OSR\s+)?KommR\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*
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

## `Title_KommR_Person_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `19683b86`  
**Description:**
Matches persons with KommR title, capturing FULL name including suffixes.

**Content:**
```
\bKommR\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)\b(?=[,;:\s]|$)
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

## `Title_OMedR_Person_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8ff593d8`  
**Description:**
Matches persons with OMedR title, capturing FULL name including suffixes.

**Content:**
```
\bOMedR\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)\b(?=[,;:\s]|$)
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

## `Standalone_Name_Verb_Context_Enhanced_3` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c5a2a6cf`  
**Description:**
Matches standalone names following verbs like 'hat', 'ist', 'war' where the person is the subject/object, ensuring at least two words are captured.

**Content:**
```
(?:hat|ist|war|verrechnet|verkauft|eingekauft|verwaltet|geleitet|betreiben)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)\b(?=[,;:\s]|$)
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

## `Multi_Initial_Person_Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3e3b42c5`  
**Description:**
Matches multi-initial names like 'M.M.A.' in context of company names or roles.

**Content:**
```
(?:GmbH\s*–|GmbH\s+|Geschäftsführer|führte|auf die)\s+([A-Z]\.[A-Z]\.[A-Z])\b
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

## `Single_Letter_Name_Context_Enhanced_5` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8037743c`  
**Description:**
Matches multi-initial names (e.g., M.M.A.) in legal contexts like 'mit M.M.A.' or 'von M.M.A.', capturing the full sequence.

**Content:**
```
(?:mit|von|bei|für|des|an)\s+([A-Z]\.[A-Z]\.[A-Z](?:\.[A-Z])?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 31 | 0 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 31 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_6`)


Der Geschäftsführende Alleingesellschafter ist der Ehegatte von M.M.B.: M.M.A..  Die Stammeinlage von 35.000 € wurde zur Gänze einbezahlt. Der Bilanzstichtag ist der  28. Februar.

**False Positives:**

- `M.M.B` — partial — pred is substring of gold: `M.M.B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.B.`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_14`)


 Das Gruppenmitglied Unistein-Lebensmittel GmbH ist ein Transportunternehmen unter der Geschäftsführung  von M.M.A..

**False Positives:**

- `M.M.A` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unistein-Lebensmittel GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_78`)


Tz. 3 a PB: Zum Zeitpunkt der Betriebsbesichtigung vom 23.10.2013 sei von den drei geplanten  Wohnungen im „(Haupt-) Gebäude (1) - Keller, Erdschoss, ein Stock“- eine Wohnung an M.M.A  und eine weitere Wohnung an M.M.B. vermietet gewesen.

**False Positives:**

- `M.M.A` — no gold match — likely missing annotation
- `M.M.B` — partial — pred is substring of gold: `M.M.B.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `M.M.B.`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_81`)


Im „Gebäude (2) - überdachte Garagenabstellplätze mit Aufgang zum Dachboden über eine  Eisenleiter sowie anschließend zwei Wohnungen“ - sei eine Wohnung an einen Arbeiter des  Unternehmens bzw. eine Wohnung an die Schwiegermutter des M.M.A. vermietet worden.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_84`)


Tz. 3 b PB: Zum Zeitpunkt der Betriebsbesichtigung vom 18.06.2015 sei beim „Gebäude (1)“ die  fertig eingerichtete Wohnung Top 1 (193,2 m²) an M.M.A. vermietet gewesen.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_85`)


Die vom Sohn  des M.M.A. bewohnte Wohnung Top 2 (110,90 m²) sei noch nicht fertiggestellt gewesen - Bad,  WC und Böden hätten gefehlt - und nicht vermietet worden.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_86`)


(Lt. Auskunft von M.M.A. schlafe  der Sohn wegen eines Streits mit seiner Schwester in dieser Wohnung).

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_87`)


Die an M.M.B. vermietete (und nur notdürftig eingerichtete) Wohnung Top 3 (85,11 m2) werde  laut Auskunft von M.M.A. von den Kindern bewohnt.

**False Positives:**

- `M.M.B` — partial — pred is substring of gold: `M.M.B.`
- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.B.`(person)
- `M.M.A.`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_90`)


Vom „Gebäude (2) = Nebengebäude“ sei die Wohnung Top Nr. 4 (65,50 m2) an zwei Arbeiter  der Unternehmensgruppe bzw. die Wohnung Top 5 (65,50 m2) an M.M.F. vermietet gewesen.

**False Positives:**

- `M.M.F` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_97`)


Lt. Auskunft von M.M.A.  sollten hier zwei weitere - vielleicht durch den Dachgeschoßausbau auch mehr- Wohnungen  entstehen.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_98`)


Nach dem Erhebungsergebnis der Betriebsprüfung bei der Bf. hätte die Familie des M.M.A. alle  Wohnungen im „Gebäude (1) Hauptgebäude“ am 18.06.2015 bewohnt.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_101`)


Betreff das „Gebäude (3) Rohbau“ hätte das im Zuge der Erhebungen im Bauamt festgestellte  Ansuchen der Bf. um Bewilligung zur Errichtung eines "Saunahauses" (Nutzfläche 114,35 m2)  am 17.06.2014 der Aussage des M.M.A. bei der Betriebsbesichtigung hinsichtlich des Neubaus  weiterer Wohnungen widersprochen.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_110`)


Die Finanzierung sei mittels Einlage des M.M.A. [380.386,00 € im Prüfungszeitraum 03/2011  bis Wirtschaftsjahr 02/2015] und der M.M.B. [250.000 € (= Verkaufserlös betreff bisheriges  Wohnhaus im  Dezember 2012] jeweils in die Firma erfolgt.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.B.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_115`)


Hinsichtlich den Wohnungen Top 4 und 5 entspreche der per Mietvertrag zwischen der Bf. als  Vermieterin und der Schwiegermutter des M.M.A. - M.M.B2 - als Mieterin der Top 4 am  1.08.2012 vereinbarte Mietzins - 230,00€- einer Nettomiete von 3,51 €/m² für Top 4.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_204`)


Die Gattin miete die Wohnung Top 3 trotz Miete der Top 1 im Ausmaß von 193,2 m² durch       M.M.A.. Top 3 werde von der Tochter des M.M.A. bewohnt.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_205`)


2) Die noch nicht fertiggestellte Wohnung Top 2 sei von des M.M.A. Sohn benützt worden.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_214`)


Der Mieter der 2. Wohnung       sei die Schwiegermutter des M.M.A. ab August 2012 bis Mitte 2014 gewesen.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_305`)


Am  1.11.2014 sei Top 5 an M.M.F. um 5,97 € fremdvermietet worden.

**False Positives:**

- `M.M.F` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_308`)


Die  unentgeltliche Übernahme sämtlicher Hausmeistertätigkeiten durch die Familie - u.a. die  Instandhaltung der Anlage, die ständige Verfügbarkeit bei allfälligen Problemen als erster  Ansprechpartner der Mieter, die Bedienung der Heizung mittels Fernwartungs-App über das  Mobiltelefon von M.M.A.- sei in der Preisgestaltung nicht berücksichtigt worden.

**False Positives:**

- `M.M.A` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_344`)


Bewohnt wird die Wohneinheit Top 3 von der Tochter des M.M.A..

**False Positives:**

- `M.M.A` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_367`)


2. Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus dem vorgelegten Verwaltungsakt, den angeführten  Bescheiden und Ergänzungsvorhalten, dem Bericht gemäß § 150 BAO vom 1.07.2016, dem  Bauakt, den Mietverträgen betreff Wohnung   +) Top 1 vom 1.11.2012 (unterschrieben mit 1.11.2012) und 1.10.2014 (unterschrieben mit       1.11.2014) jeweils mit Mieter M.M.A.,   +) Top 3 vom 1.11.2012 und 1.10.2014 jeweils mit M.M.B als Mieterin,   +) Top. 4 vom a) 1.08.2012 mit Mieterin M.M.B 2 (unterfertigt mit 7.09.2012),                            b) 19.01.2014 mit Fremdmieter R.A. vom 20.01.2014;

**False Positives:**

- `M.M.B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.M.A.`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_492`)


Ein Vergleich der mit M.M.A., M.M.B und M.M.B.2 jeweils als Mieter abgeschlossenen Verträge  mit den mit Fremdmietern abgeschlossenen Verträgen ergab, dass R.A. vor dem Umzug in die  von M.M.B.2 bewohnte und in weiterer Folge frei gewordene Mietwohnung Top 4 am  1.10.2014 Mieter der Top 5 kraft der zeitlich befristeten Verträge für die Arbeiterwohnung  vom 16.10.2013 und 19.01.2014 gewesen war.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`
- `M.M.B` — similar text (different position): `M.M.B.2`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.B.2`(person)
- `M.M.B.2`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_496`)


Während dem  Mietvertrag zwischen der Vermieterin Bf. und der Fremdmieterin M.M.F. betreff Top 5 vom  1.11.2014 mit Beginn der Miete am 1.11.2014 zufolge dieser Vertrag von den Vertragsparteien  unter Einhaltung einer dreimonatigen Kündigungsfrist zum letzten eines Monats aufgekündigt  werden konnte, sah der mit M.M.C. als Fremdmieter abgeschlossene Bestandvertrag für Top 4  vom 1.10.2014 die Möglichkeit einer Kündigung des Mietvertrags von den Vertragsparteien  unter Einhaltung einer sogar nur einmonatigen Kündigungsfrist zum letzten eines Monats vor.

**False Positives:**

- `M.M.C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_510`)


Das Vorbringen der steuerlich vertretenen Bf. in der Verhandlung, wonach M.M.A. und M.M.B.  keine andere Wohnmöglichkeit als die in dem teilweise fertigen Haus an der Adresse A-Platz,  A-Ort, gehabt hätten, wurde durch die durch das Erhebungsergebnis der Betriebsprüfung bei  der Bf. bestätigte tatsächliche Nutzung des Hauses für Wohnzwecke der Familie des M.M.A.  glaubhaft gemacht.

**False Positives:**

- `M.M.A` — similar text (different position): `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.B.`(person)
- `M.M.A.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_537`)


Hinsichtlich der Überlassung der Wohneinheit Top 1 dem Gesellschafter der Bf. - M.M.A. –  bzw. Top 3 der Ehegattin des M.M.A. - M.M.B. - jeweils gegen Entgelt liegt Missbrauch im  Bereich der Umsatzsteuer nicht schon dann vor, wenn die Nutzung durch den Mieter selbst bei  ihm nicht zu einem Vorsteuerabzug geführt hat (vgl. VwGH 16.03.2022, Ra 2019/13/0090).

**False Positives:**

- `M.M.A` — similar text (different position): `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.A.`(person)
- `M.M.B.`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_539`)


Dem von der Betriebsprüfung bei der Bf. thematisierten Anteil der Schwiegermutter des  M.M.A. am Keller war zu entgegnen, dass die in Quadratmetern auszudrückende Nutzfläche  gemäß § 17 Abs. 2 MRG in der Fassung des BGBl. I Nr. 36/2000 die gesamte Bodenfläche einer  Wohnung oder eines sonstigen Mietgegenstandes abzüglich der Wandstärken und der im  Verlauf der Wände befindlichen Durchbrechungen (Ausnehmungen) ist.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_542`)


Betriebsprüfung thematisierten Kellers des Gebäudes mit der von der Schwiegermutter des  M.M.A. bewohnten Wohneinheit für Wohnzwecke anhand des im Zuge der Betriebsprüfung  bei der Bf. erhobenen Beweismaterials zur Kellerausstattung nicht erbracht wurde, war der im  Mietvertrag der Schwiegermutter des M.M.A. ausgewiesene Kelleranteil bei der Berechnung  der Nutzfläche nicht zu berücksichtigen und stellte somit keinen die Miethöhe bestimmenden  Wertfaktor dar.

**False Positives:**

- `M.M.A` — partial — pred is substring of gold: `M.M.A.`
- `M.M.A` — similar text (different position): `M.M.A.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.A.`(person)

</details>

---

## `Single_Letter_Name_Context_Enhanced_6` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46158aff`  
**Description:**
Matches single or double initials (e.g., Dr. G, M.M.) in legal contexts, ensuring full capture.

**Content:**
```
(?:des|von|für|an|namens|Zeuge|Zeugin|als)\s+([A-Z]\.[A-Z]?\.)\b(?=[,;:\s]|$)
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

## `Title_Mag_a_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `411ddf91`  
**Description:**
Matches 'Mag.' or 'Mag.a' followed by full name, ensuring at least two words are captured to avoid partial matches like 'Mag.a Marilyn'.

**Content:**
```
\b(?:Mag\.|Mag\.a|MMag\.)\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)+)(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Title_MMag_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b5987f60`  
**Description:**
Matches persons with 'MMag.' title, capturing full text including title and full name.

**Content:**
```
\bMMag\.\s+([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)+)(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Title_Hon_Prof_Compound_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3e7340fb`  
**Description:**
Matches persons with compound academic titles like 'Dr. Hon.-Prof.' or 'Hon.-Prof. Univ.-Prof.', capturing FULL text.

**Content:**
```
\b(?:Dr(?:in)?|DDr(?:in)?|Hon(?:-)?Prof(?:in)?)(?:[. ]+(?:Dr(?:in)?|DDr(?:in)?|Hon(?:-)?Prof(?:in)?))*[. ]+(?:Hon(?:-)?Prof(?:in)?)(?:[. ]+Univ(?:-)?Prof(?:in)?)?[^a-zA-Z]*([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)
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

## `Title_Univ_Prof_Person` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `49abef9e`  
**Description:**
Matches persons with 'Univ.-Prof.' or 'Univ.Prof.' title, capturing FULL text including title.

**Content:**
```
\b(?:Univ\.-Prof(?:\.in)?|Univ\.Prof(?:\.in)?)\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Alessia von Bauer  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

**False Positives:**

- `Univ.-Prof.in Alessia` — partial — pred is substring of gold: `Univ.-Prof.in Alessia von Bauer`

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

</details>

---

## `Title_PhD_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `71e085ef`  
**Description:**
Matches persons with 'PhD' title, capturing full name.

**Content:**
```
\bPhD\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:\s*,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Party_Name_NoTitle_Context_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ca1ace57`  
**Description:**
Matches party names in phrases like 'in der Beschwerdesache [Name]' where the name might not have a title immediately preceding it, capturing full name including suffixes.

**Content:**
```
(?:in der Beschwerdesache|Beschwerdesachen) \s+ ([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)+)(?:,? \s*(?:MA|BEd|LLM|LL\\.M\\. M\\.B\\.L\\.|Dipl\\.-Ing\\.|Bakk\\. iur\\.|Bakk\\. phil\\.|Bakk\\. art\\.|Bakk\\. rer\\. nat\\.|Bakk\\. rer\\. pol\\.|Bakk\\. oec\\.|Bakk\\. jur\\.)?)? \b(?=[,;:\s]|$)
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

## `Title_Fr_PhD_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6762eceb`  
**Description:**
Matches 'Fr.PhD' (Frau PhD) followed by name, capturing full title and name.

**Content:**
```
\bFr\.PhD\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Title_OkR_DiplIng_Person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cdd9020`  
**Description:**
Matches compound titles like 'ÖkR Dipl.-Ing.' followed by name.

**Content:**
```
\b(?:ÖkR\s+)?Dipl\.-Ing\.(?:\s+Priv\.-Doz\.in)?(?:\s+Univ\.-Prof(?:\.in)?)?\s+[A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:\s+[A-Z][a-zäöüßéáüé]+)*(?:,?\s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?\b(?=[,;:\s]|$)
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

## `Legal_Context_Representative_Person_Enhanced` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `82f63de5`  
**Description:**
Matches representatives in phrases like 'vertreten durch [Name]', capturing ONLY the name part including suffixes and handling compound titles.

**Content:**
```
(?:vertreten durch)\s+(?:Mag\.a?|Dr\.in?|DDr\.|DDr\.in|OStR|Univ\.-Prof(?:\.in)?|Priv\.-Doz\.|Priv\.-Doz\.in|MedR|Bakk\. iur\.|Bakk\. phil\.|LLM|LL\.M\. M\.B\.L\.|Hon\.-Prof\.|BSc|RA|Ing\.)?([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,? \s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)? \b(?=[,;:\s]|$)
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

## `Standalone_Name_Professional_Context_Enhanced_2` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `47665c64`  
**Description:**
Matches standalone names following professional role indicators like 'Psychiater', 'Arzt', etc., ensuring full name capture including suffixes and handling compound titles.

**Content:**
```
(?:Psychiater(?:in)? |Arzt(?:in)? |Ärztin |Sachverständiger |Sachverständige |Gutachter(?:in)? |Wahlpsychologin |Klinische und Gesundheitspsychologin |Steuerberater )([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,? \s*(?:MA|BEd|LLM|LL\.M\. M\.B\.L\.|Dipl\.-Ing\.|Bakk\. iur\.|Bakk\. phil\.|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. rer\. pol\.|Bakk\. oec\.|Bakk\. jur\.)?)?)? \b(?=[,;:\s]|$)
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

## `Herrn_Name_Context_Enhanced_2` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10c6ceba`  
**Description:**
Matches names preceded by 'Herrn' or 'Herr', capturing ONLY the name part, excluding any subsequent titles (Mag, Dr, etc.) to avoid over-matching, but ensuring full name capture.

**Content:**
```
(?:Herrn |Herr )(?!.*(?:Mag |Dr |DDr |OStR |Priv \.-Doz |Univ \.-Prof |RA |Ing \.) )([A-Z][a-zäöüßéáüé]+(?:-[A-Z][a-zäöüßéáüé]+)*(?:[ \t]+[A-Z][a-zäöüßéáüé]+)*(?:,? \s*(?:MA|BEd|LLM|LL \.M \. M \.B \.L \. |Dipl \.-Ing \. |Bakk \. iur \. |Bakk \. phil \. |Bakk \. art \. |Bakk \. rer \. nat \. |Bakk \. rer \. pol \. |Bakk \. oec \. |Bakk \. jur \. |BA|MBA)?)?)? \b(?=[,;:\s]|$)
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
<summary>❌ False Negatives (1009, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_182`)

„Auf diesen  Umgründungsplan wird sowohl im ergänzten Gesellschaftsvertrag der **Uwe Gudian**  als auch im  atypisch stillen Gesellschaftsvertrag der [Geschäftsherrin] Bezug genommen.“

- missed: `Uwe Gudian` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_298`)

Wobei auch 3 dieses Versäumnis spätere Gestaltungsmöglichkeiten weit offen hält.  Infolge einer amtswegigen Umsatzsteuerfestsetzung für den Zeitraum 01-08/2013 musste die  **M.** zur Beschwerdeführung für diesen Zeitraum eine Buchhaltung anfertigen lassen.

- missed: `M.` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und **Dr  Heinrich Vana,** über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

- missed: `Dr  Heinrich Vana,` (person)
- predicted in sentence: `Silvia Gebhart`

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/145807.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145807.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des **Roxana Massott**, Gottschallalmstraße 37, 4792 Ficht, Österreich, vertreten durch Mag. Fatma Islekoglu, Rechtsanwältin,  Landstraße 13, 6971 Hard, über die Beschwerde vom 22. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 22. Februar 2024 betreffend Festsetzung der  Normverbrauchsabgabe (Berechnungsstichtag 02.06.2022), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Roxana Massott` (person)
- predicted in sentence: `Mag. Josef Ungericht`, `Mag. Fatma Islekoglu`

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_145`)

Ein Gespräch mit Hern **OA Dr.  Bieber** bezüglich des weiteren psychotherapeutischen Procedere wurde vor der Entlassung  durchgeführt.“

- missed: `OA Dr.  Bieber` (person)
- predicted in sentence: `Dr.  Bieber`

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)

Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau **Borisowa**- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

- missed: `Borisowa` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_46`)

Da das Beschwerdeverfahren gegen Frau A B als Geschäftsführerin der Saskia Sinnwell  und somit  als Entscheidungsträgerin iSd § 3 Abs. 2 VbVG kein rechtswidriges oder schuldhaftes Verhalten  ergeben hat, liegen die Voraussetzungen für die Verhängung einer Geldbuße über die  **Saskia Sinnwell**  als belangten Verband nicht vor.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch **Dr Christian Burghardt**, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Dr Christian Burghardt` (person)
- predicted in sentence: `Mag. Heidemarie Winkler`, `StR Univ.-Prof. Alvin Paulikat`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_378`)

Die Voraussetzungen für einen Abzug von der Kosten des Herrn **M.** als außergewöhnliche  Belastung im Jahr 2018 liegen insgesamt nicht vor.

- missed: `M.` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)

IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über **Albert Sengeisen**  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

- missed: `Albert Sengeisen` (person)
- predicted in sentence: `Albert Sengeisen`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dr. Martin Wadepfuhl  in der Beschwerdesache Renate Bürvenig,  Kreuzkapellenweg 7, 5151 Hochberg, Österreich, vertreten durch **Ludmilla Flaumbaum**, Herrengschwendt 3, 8761 Mühltal, Österreich, über die Beschwerde vom  15. Februar 2021 gegen die Bescheide des Finanzamtes Österreich vom 19. Jänner 2021  betreffend die Haftung für Lohnsteuer für 2015, 2016, 2017, 2018 und 2019, sowie den  Dienstgeberbeitrag zum FLAF für 2015, 2016, 2017, 2018 und 2019 und den Zuschlag zum  Dienstgeberbeitrag für 2015, 2016, 2017, 2018 und 2019 zu Steuernummer 74-041/7335  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Ludmilla Flaumbaum` (person)
- predicted in sentence: `Univ.-Prof. Dr. Martin Wadepfuhl`, `Renate Bürvenig`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache **Janis Klinckhammer**, Schattenort 33, 9545 Ebene, Österreich, über die Beschwerde vom 15. April 2019 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 15. März  2019, Steuernummer 81-205/5472, betreffend Grunderwerbsteuer 2019 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Janis Klinckhammer` (person)
- predicted in sentence: `Mag. Daniel Philip Pfau`

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_26`)

Mit Verschmelzungsvertrag vom 14.4.2014 wird die ausl._T1 zur Gänze mit der **Gotthard Angelstein**  verschmolzen.

- missed: `Gotthard Angelstein` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen **Annette Preußing**, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

- missed: `Annette Preußing` (person)
- predicted in sentence: `Dr. Sebastian Pfeiffer`

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_74`)

Die **Leroy Kusznierz**  wurde  schließlich am xx.xx.2020 im Firmenbuch des Gericht gelöscht.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)

Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn **Isenmann**  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

- missed: `Isenmann` (person)
- predicted in sentence: `Ballschmieder`

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_23`)

Mit Bescheid vom 03.12.2020 begründe die zuständige Abgabenbehörde die Abweisung des  Aussetzungsantrages damit, dass durch die Tilgung der Nachforderung durch das **Jaden Knauss**  hinsichtlich der ergangenen Bescheide vom 07.10.2018 für einen solchen Zahlungsaufschub iSd  § 212a BAO keine Voraussetzungen mehr bestünden.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)

Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von **Josefine Frikel** (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der Verwaldgart GmbH bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

- missed: `Josefine Frikel` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  **HR OSR Leonie Ercklentz**, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `HR OSR Leonie Ercklentz` (person)
- predicted in sentence: `Dr. Siegfried Fenz`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_94`)

Eingangs ist - zumal die **Leroy Kusznierz**  per xx.xx.2020 endete - die Frage der Rechtsnachfolge zu  klären: Kraft der ausdrücklichen gesetzlichen Anordnung des § 191 Abs. 2 BAO – als lex  specialis zur im § 19 Abs. 1 BAO normierten Gesamtrechtsnachfolge – haben  Feststellungsbescheide nach Beendigung einer Personenvereinigung (Personengemeinschaft)  an die Personen, denen gemeinschaftliche Einkünfte zugeflossen sind, zu ergehen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_12`)

Diese Rechnung (die USt ausweisend, Beilage 3 zum Protokoll) vom 12.6.2019 wurde ihr vom  Steuerberater am 20.6.2019 wiederum per Email (Beilage 2 zum Protokoll) übermittelt.  Der Kaufvertrag wurde am 17.6.2019 unterfertigt, wobei der Käufer die Vorsteuer auf das  Abgabenkonto der **Saskia Sinnwell**  überrechnen hätte sollen und diese wiederum als USt abgeführt  hätte werden sollen.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_436`)

Der Vorhaltsbeantwortung waren fünf Anlagen angeschlossen:  Anlage 1:  1/1: Letter of confirmation vom 26.8.2020  1/2: Bestätigungsschreiben (beglaubigte Übersetzung aus dem Englischen vom 17.9.2020) vom  26.8.2020  1/3: Letter of confirmation vom 26.8.2020  1/4: CMR 80722597 an ZL vom 13.6.2016  Anlage 2:  2/1: Letter of confirmation vom 26.8.2020  2/2: CMR 80265439 an F.B. vom 17.3.2015  2/3: CMR 80828354 an F.B. vom 27.9.2015  2/4: CMR 80914347 an R.U. vom 5.12.2016  2/5: CMR 80914350 an R.U. vom 2.12.2016  Anlage 3:  3/1: This Document has been issud on the request of vom 27.8.2020  3/2: Dieses Dokument wird ausgestellt auf Ansuchen vom 27.8.2020 (Übersetzung vom  29.9.2020)  3/3: This Document has been issud on the request of vom 27.8.2020  3/4: Invoice der Bf. an N. vom 12.10.15  3/5: Invoice der Bf. an N. vom 26.9.16  3/6: CMR an CL vom 9.10.2015  3/7: Purchase Order vom 1.10.2015 (N. an CL)  3/8: Purchase Order vom 20.9.2016 (N. an CL)  3/9: CMR JBL an CL vom 26.9.2016  3/10: CMR 80409868 an K. (Polska) vom 7.8.2015  3/11: CMR 80423569 an K. (Polska) vom 26.8.2015  3/12: CMR 80236735 an Ko. (N.L.) vom 10.2.2015  3/13: CMR 80392557 an Ko. (Polska) vom 21.7.2015  3/14: CMR 80388656 an **M.** (Polska) vom 24.7.2015  3/15: CMR 80320800 an M. (Polska) vom 8.5.2015  3/16: CMR 80257940 an S. (Polska) vom 6.3.2015  3/17: CMR 80323928 an S. (Polska) vom 18.5.2015  3/18: CMR 80265443 an S. (Polska) vom 18.3.2015  3/19: CMR 80423566 an S. (Polska) vom 24.8.2015  3/20: CMR 80673863 an Ko. (Polska) vom 22.4.2016  29 von 59 Seite 30 von 59

- missed: `M.` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_205`)

19.564,68 €……..Mag. ES IE (2,6919 %)  668.105,92 €……Z1Z2Z3 Privatstiftung (91,9243% )Sonja Schönhut Linn Brümmer und Lynn Freimut sind Geschwister (Daten aus dem zentralen Melderegister  betreffend **Sonja Schönhut**  geb. IE; Firmenbuchdaten FN FN1 t mit den Hinweisen auf die  ehemaligen Gesellschafter Cassandra Ungar  SD IE und die Gesellschafter im Streitzeitraum Mag. AI RR;Linn Brümmer und Lynn Freimut.

- missed: `Sonja Schönhut` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch **Helga Kraus**, Johann Vollnhofer-Straße 1/Stg.

- missed: `Helga Kraus` (person)
- predicted in sentence: `OStR Cassandra Schmedtje`

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_290`)

1994, C-60/93, Rs R.L. **Aldewereld** Rn 10).

- missed: `Aldewereld` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_37`)

Mit dem auf Frau **PW** zugelassenen PKW3 seien im beschwerdegegenständlichen Zeitraum  3 von 15 Seite 4 von 15

- missed: `PW` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)

Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin **Dr.in Ing. Viktoria Weigart** der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

- missed: `Dr.in Ing. Viktoria Weigart` (person)
- predicted in sentence: `Ing. Viktoria Weigart`

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_38`)

3,99 Lesebrille Geschäft 1 („Geschäft 1“)  7,14   0 Dr. W („**Dr. W**“)

- missed: `Dr. W` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde des  **Desiree Hannecken**, Lasseestraße 13, 5144 Handenberg, Österreich, vom 5. Oktober 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 28. September 2023, GZ. MA67/Zahl/2023,  wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung  in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Desiree Hannecken` (person)
- predicted in sentence: `Mag. Irene Kohler`

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_183`)

(Vgl EuGH 22.10.2015, C-378/14, Tomislaw **Trapkowski**, VwGH  24.06.2021, Ro 2018/16/0040, BFG 27.06.2023, RV/7105857/2017)

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_16`)

Um eine Verjährung der Forderungen des **Jaden Knauss**  gegenüber seinen Bediensteten  2 von 7 Seite 3 von 7

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_22`)

In der dagegen fristgerecht am eingebrachten Beschwerde des Amtsbeauftragten vom  3. Dezember 2020 wird wie folgt ausgeführt:  Angefochten werde die Einstellung gem. § 136 FinStrG hinsichtlich der Geschäftsführerin A B,  Adresse1, sowie des belangten Verbandes die Saskia Sinnwell, Franz-Michel-Willam-Weg 31, 3580 Groß Burgstall, Österreich  mit folgendem  Inhalt:  „Die Grundlage des Verfahrens bildet die Betriebsprüfung vom 09.10.2019 bei der **Saskia Sinnwell**,  bei welcher festgestellt wurde, dass ein Liegenschaftsverkauf im Juni 2019 nicht in der UVA  gemeldet wurde.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Beschwerdesache Lee Gerstmayer, Wüsterstraße 92, 4972 Stelzham, Österreich, über die Beschwerde vom 13. Oktober 2014  gegen den Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser  vom 12. September 2014 betreffend Wasser- und Abwassergebühr, MA 31-130652/15, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: `Mag. Anna`

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)

Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn **Isenmann**  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

- missed: `Isenmann` (person)
- predicted in sentence: `Ballschmieder`

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_49`)

 Der Bf. wohnt seit dem Jahr 2010 mit seiner Ehefrau, **Ashley Petzack**, und dem  gemeinsamen Sohn Werner Puskeppeleit  in Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich.

- missed: `Ashley Petzack` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_346`)

Die besonders luxuriöse Ausstattung der Wohneinheit Top 1 erfolgt nach den Wünschen und  Vorstellungen des Gesellschafters und Geschäftsführers Ing. **M.M.A.** (z.B. Kosten für a) Küche  und Esszimmer: 90.664,40 € netto; b) "Specksteinofen": 18.200,00 € netto).

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_559`)

Am Beleg scheint nur beim 23.5. der Zusatz „**Dr. S** 19.6.13“ auf.

- missed: `Dr. S` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_12`)

Mit Bescheid vom 12. Juni 2018 wies das Finanzamt den Antrag vom 21.3.2018 auf  Familienbeihilfe für **Jana Papenkord**  ab Jänner 2011 ab.

- missed: `Jana Papenkord` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_96`)

Dazu wurden ein Curriculum vitae (CV) sowie eine Teilnahmebestätigung an einer  Fortbildungsveranstaltung 2020 vorgelegt, bei welcher ua. das DDX3X-Syndrom seitens **Prof.  XX** (USA) behandelt wurde.

- missed: `Prof.  XX` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_323`)

Hinsichtlich den Mietverträgen ab 11/2014 brachte die steuerlich vertretene Bf. zur Erhöhung  der Miete Top 1 von 3,51 €/m2 auf 5,96 €/m2 nochmals vor, dass **M.M.A.** Arbeiten eines  Gärtners und Hausbesorgers verrichtet hätte, die zu höheren Betriebskosten bei Begründung  eines Angestelltenverhältnisses führen würden.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_13`)

Mit Schreiben vom 30. Dezember 2020 wurde die Fa. E. – **Balthasar Brendtke** (kurz: E.) unter Anführung  der erforderlichen Daten als jene Person, die das ihr von der Zulassungsbesitzerin des näher  bezeichneten Fahrzeuges zur Verfügung gestellte Fahrzeug einem Dritten überlassen habe,  gemäß § 2 Wiener Parkometergesetz 2006 zur Lenkerauskunft binnen zwei Wochen ab  Zustellung des Schreibens aufgefordert.

- missed: `Balthasar Brendtke` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler in der  Verwaltungsstrafsache gegen **Bodo Nöth**, Lipizzaner-Gasse 13, 4113 Oberhart, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 11. Jänner 2024 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  11. Dezember 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Der Beschwerde wird Folge gegeben, das angefochtene Straferkenntnis aufgehoben und das  Strafverfahren gemäß § 45 Abs. 1 Z 1 VStG eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat der Beschwerdeführer keinen Beitrag zu den Kosten des  Beschwerdeverfahrens zu leisten.

- missed: `Bodo Nöth` (person)
- predicted in sentence: `Mag. Irene Kohler`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_85`)

Der im Firmenbuch seit 24. Oktober 2011 eingetragene  handelsrechtliche Geschäftsführer dieser Gesellschaft ist **Harald Hilderink**.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_391`)

10. 2015, C-378/14, Tomisław **Trapkowski**, ECLI:EU:C:2015:720, Rn. 38).

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_4`)

Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde  vom , Strafnummer 2019, SpS 2000, wurde das gegen   1) A B, Russland, derzeit in Karenz, wohnhaft Adresse1, und   2) **Saskia Sinnwell**, Wien;

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Piedro Klingebiel  in der Beschwerdesache 1. der  **Tamara Gottschalch**  und 2. der Heidemarie Egghart, beide in ***Bf1 und Bf2-Adr***, beide steuerlich vertreten  durch Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH, Schloßgraben 10,  6800 Feldkirch, über die Beschwerde vom 22.05.2018 gegen den Bescheid des Finanzamtes  Feldkirch vom 12. März 2018 betreffend Feststellungsbescheid Gruppenmitglied 2015  Tamara Gottschalch 22-144/9009  nach Durchführung einer mündlichen Verhandlung, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: `Univ.-Prof. Piedro Klingebiel`

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Dipl.-Ing. Mag.a Andrea Johanningmeyer, Tenniszeile 8, 5424 Rengerberg, Österreich, vertreten durch **Susanne Neuhäuser**, Hartiggasse  22/23, 2700 Wiener Neustadt, vom 12. Dezember 2019 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom  26. November 2019 betreffend Zwangsstrafen 2019 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Susanne Neuhäuser` (person)
- predicted in sentence: `Mag. Daniela Regina Denk`, `Dipl.-Ing. Mag.a Andrea Johanningmeyer`

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_24`)

Rechtlich ergibt sich:   Einer Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG macht sich schuldig, wer  vorsätzlich Abgaben, die selbst zu berechnen sind, Vorauszahlungen an Umsatzsteuer oder  Vorauszahlungen an Abgabe von alkoholischen Getränken nicht spätestens am fünften Tag  nach Fälligkeit entrichtet oder abführt, es sei denn, dass der zuständigen Abgabenbehörde bis  zu diesem Zeitpunkt die Höhe des geschuldeten Betrages bekannt gegeben wird und ist  zumindest die Schuldform des Eventualvorsatzes erforderlich, der bei **Harald Hilderink**  beim  festgestellten Sachverhalt vorlag.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_79`)

Die weiteren Feststellungen zur Historie der **Leroy Kusznierz**  fußen auf den im Firmenbuch  ersichtlichen Änderungen, respektive den diesen Eintragungen zugrunde liegenden und in der  dortigen Urkundensammlung hinterlegten Anträgen (Antrag auf Eintragung einer  Kommanditgesellschaft vom Datum;

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_13`)

Der mj. **OSR Eugenia Balikci**  befand steh im abweisenden Zeitraum ab  Jänner 2016 in einer sozialpädagogischen Wohngemeinschaft der Sozialwerke Clara Fey.

- missed: `OSR Eugenia Balikci` (person)
- predicted in sentence: —

</details>

---

