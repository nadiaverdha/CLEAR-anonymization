# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-17T03:31:43.936628

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
| Accuracy (exact match) | 98.6% |
| True Positives | 817 |
| False Positives | 297 |
| False Negatives | 797 |
| Total Gold Entities | 1614 |
| Micro Precision | 73.3% |
| Micro Recall | 50.6% |
| Micro F1 | 59.9% |
| Macro F1 | 59.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Standalone_Name_Professional_Context_Enhanced` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Herrn_Name_Context_Enhanced` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `OSR_KommR_Context_Fixed` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Standalone_Name_Role_Context_Enhanced` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Title_Univ_Prof_Person_Enhanced_Corrected` | 2.3% | 95.0% | 1.2% | 20 | 19 | 1 |
| `Party_Name_Beschwerdesache_Enhanced` | 20.1% | 94.8% | 11.2% | 191 | 181 | 10 |
| `Title_Priv_DoZ_in_Person_Enhanced` | 2.8% | 92.0% | 1.4% | 25 | 23 | 2 |
| `Title_Hon_Prof_in_Person` | 2.0% | 84.2% | 1.0% | 19 | 16 | 3 |
| `Compound_Title_Person` | 43.5% | 82.6% | 29.5% | 576 | 476 | 100 |
| `Honorific_Herr_Frau` | 7.6% | 80.0% | 4.0% | 80 | 64 | 16 |
| `Herrn_Name_Context` | 0.5% | 80.0% | 0.2% | 5 | 4 | 1 |
| `Single_Letter_Name_Context_Enhanced_4` | 1.3% | 68.8% | 0.7% | 16 | 11 | 5 |
| `Title_OMedR_Person` | 0.7% | 66.7% | 0.4% | 9 | 6 | 3 |
| `Legal_Context_Party_Person` | 0.2% | 66.7% | 0.1% | 3 | 2 | 1 |
| `Title_MedR_Person_Enhanced` | 0.2% | 40.0% | 0.1% | 5 | 2 | 3 |
| `Standalone_Name_Rs_Context` | 0.1% | 25.0% | 0.1% | 4 | 1 | 3 |
| `Single_Letter_Name_Context_Enhanced_7` | 0.4% | 21.4% | 0.2% | 14 | 3 | 11 |
| `Party_Name_NoTitle_Context_Enhanced_2` | 0.2% | 20.0% | 0.1% | 10 | 2 | 8 |
| `Standalone_Name_Verb_Context_Enhanced_2` | 0.2% | 11.8% | 0.1% | 17 | 2 | 15 |
| `Academic_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal_Context_Representative_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR_Title_Person` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Mag_a_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quote_Name_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Name_NoTitle_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Professional_Context` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `Single_Letter_Name_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `StR_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quote_Name_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_KommR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_StR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context_Enhanced_2` | 0.0% | 0.0% | 0.0% | 56 | 0 | 56 |
| `Standalone_Name_Following_Role` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Verb_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR_Title_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Dok2_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Ebenho_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HR_OStR_Context_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Verb_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 45 | 0 | 45 |
| `Abbreviation_Person_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_ProfStR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Role_Indicator_Person_NoTitle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_KommR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_OMedR_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Verb_Context_Enhanced_3` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Multi_Initial_Person_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context_Enhanced_5` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single_Letter_Name_Context_Enhanced_6` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Mag_a_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_MMag_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Hon_Prof_Compound_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Univ_Prof_Person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Title_PhD_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Name_NoTitle_Context_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Fr_PhD_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_OkR_DiplIng_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Title_Mag_a_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Legal_Context_Representative_Person_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone_Name_Professional_Context_Enhanced_2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herrn_Name_Context_Enhanced_2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Standalone_Name_Professional_Context_Enhanced` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_254`)


Da sich das Sozialministeriumservice sehr wohl aus einer eigenen Sachverständigenliste von zur  Berufsausübung berechtigter Ärzte zwecks Erstattung der Bescheinigungen gem. § 8 Abs. 6  FLAG bedienen kann, die nicht in der Liste der allgemein beeideten und gerichtlich  zertifizierten Sachverständigen eingetragen sind (siehe wiederum BFG 15.12.2017,  RV/7102062/2017), kommt dem diesbezüglichen Beschwerdeeinwand ebenso keine  Berechtigung zu.  Insgesamt besteht daher für das BFG keine Veranlassung, die fachliche Qualifikation der  begutachtenden Ärztin Amanda Zacharek in Zweifel zu ziehen.

| Predicted | Gold |
|---|---|
| `Amanda Zacharek` | `Amanda Zacharek` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

</details>

---

## `Herrn_Name_Context_Enhanced` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

</details>

---

## `OSR_KommR_Context_Fixed` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  OSR KommR Susette Stenczel, Amtweg 83, 9542 Tobitsch, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glückspiel vom 25. September 2019  betreffend Gebühr Steuernummer 61-194/1325  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OSR KommR Susette Stenczel` | `OSR KommR Susette Stenczel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Amtweg 83, 9542 Tobitsch, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `61-194/1325` (tax_number)

</details>

---

## `Standalone_Name_Role_Context_Enhanced` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 1612 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_3`)


Begründung  Bereits mit Haftungsbescheid vom 23. März 2022 hatte das Finanzamt den ehemaligen  Geschäftsführer Evamaria Watenphul  als Haftungspflichtigen für aushaftende Abgabenschuldigkeiten der  Özyilmaz Recycling GmbH  in Anspruch genommen.

| Predicted | Gold |
|---|---|
| `Evamaria Watenphul` | `Evamaria Watenphul` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Özyilmaz Recycling GmbH` (organisation)

</details>

---

## `Title_Univ_Prof_Person_Enhanced_Corrected` 🏆

**F1:** 0.023 | **Precision:** 0.950 | **Recall:** 0.012  

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
| 0.950 | 0.012 | 0.023 | 20 | 19 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 19 | 1 | 1595 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_43`)


Im Februar seien die Schmerzen dann unerträglich geworden, weshalb sie das KUK aufgesucht  hätte und auch bei Univ.-Prof.in Milena Büttinghausen [Anmerkung Richter: Ärztin für Allgemeinmedizin] in Behandlung  gewesen sei.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Milena Büttinghausen` | `Univ.-Prof.in Milena Büttinghausen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Jacqueline Wolenski` | `Univ.-Prof.in Jacqueline Wolenski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Beyazit` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Sebott` | `Univ.-Prof.in Anastasia Sebott` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Bettina Füsslin` (person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Roberta Sellerer  in der   Beschwerdesache Univ.-Prof.in Susette Teebken, Günther Benedikt-Straße 26, 8052 Graz, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 29. Mai 2017 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 3. Mai 2017,   ErfNr, betreffend 1. Aufhebung gemäß § 299 Abs. 1 BAO und 2. Festsetzung der  Grunderwerbsteuer, im fortgesetzten Verfahren zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 3.5.2017 betreffend Aufhebung des      Grunderwerbsteuerbescheides vom 24.2.2017 gemäß § 299 Abs. 1 BAO wird als      unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Susette Teebken` | `Univ.-Prof.in Susette Teebken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Roberta Sellerer` (person)
- `Günther Benedikt-Straße 26, 8052 Graz, Österreich` (address)
- `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für  Gebühren` (organisation)
- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_7`)


Mit Baurechtsvertrag vom 19.10.2016 hat die Marktgemeinde Ort1 als Baurechtsbestellerin  an den ihr gehörigen Gst1 und Gst2 in EZ1, bebautes Grundstück mit einer Gesamtfläche von  1.094 m², an die Univ.-Prof.in Susette Teebken (= Beschwerdeführerin, Bf) ein Baurecht auf die Dauer von 50  Jahren eingeräumt (Punkte III. und IV.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Susette Teebken` | `Univ.-Prof.in Susette Teebken` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Regina Mockry  in der Beschwerdesache Gablonsky&Rethlefsen Gastronomie AG&  atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafter  1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Regina Mockry` | `Univ.-Prof.in Regina Mockry` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gablonsky&Rethlefsen Gastronomie AG` (organisation)
- `xx GmbH Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache RgR Tanja Tihl, BSc,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shirley Vostrovsky` | `Univ.-Prof.in Shirley Vostrovsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Tanja Tihl, BSc` (person)
- `Kleindorf I 13, 4661 Deising, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `58-854/9841` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/144133.1`) (sent_id: `deanon_BFG_20260814_TEST/144133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Farina Solovieva  in der Beschwerdesache der  Folmer Sanitär, Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich, über die Beschwerde vom 27. Oktober 2022 gegen den Bescheid  des FA Bruck Eisenstadt Oberwart  vom 14. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 06-556/2153  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Farina Solovieva` | `Univ.-Prof.in Farina Solovieva` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Folmer Sanitär` (organisation)
- `Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `06-556/2153` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/145808.1`) (sent_id: `deanon_BFG_20260814_TEST/145808.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Silvia Aust   in der Beschwerdesache des Li Süssle, Zierreit 3, 9113 Lippitzbach, Österreich, betreffend den Bescheid des  FA Wien 1/23  vom 21. April 2020   hinsichtlich Einkommensteuervorauszahlungen 2020, Steuernummer 97-936/9955,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Silvia Aust` | `Univ.-Prof.in Silvia Aust` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Li Süssle` (person)
- `Zierreit 3, 9113 Lippitzbach, Österreich` (address)
- `FA Wien 1/23` (organisation)
- `97-936/9955` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/146223.1`) (sent_id: `deanon_BFG_20260814_TEST/146223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Arabella Ungeruh  in der Beschwerdesache des  Melina Kirstaedter, Olbersdorf 35, 6092 Birgitz, Österreich, über die Beschwerde vom 26. April 2024 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 25. April 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  zu Steuernummer 03-867/9768  zu Recht erkannt:   I. Die Beschwerde wird gemäß als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Arabella Ungeruh` | `Univ.-Prof.in Arabella Ungeruh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Kirstaedter` (person)
- `Olbersdorf 35, 6092 Birgitz, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `03-867/9768` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/149389.1`) (sent_id: `deanon_BFG_20260814_TEST/149389.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Felizia Henrichmöller  in der Beschwerdesache Friedrich Günthardt,  Thonebenstraße 8, 4722 Oberngrub, Österreich, über die Beschwerde vom 13. Oktober 2025, beim Bundesfinanzgericht am  20. Oktober 2025 eingelangt, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich betreffend Erlassung einer Beschwerdevorentscheidung hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2024, Steuernummer 87-033/9289,  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Felizia Henrichmöller` | `Univ.-Prof.in Felizia Henrichmöller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedrich Günthardt` (person)
- `Thonebenstraße 8, 4722 Oberngrub, Österreich` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `87-033/9289` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Oktay  in der Beschwerdesache Christina Schwabendissen,  Leckenholz 16, 6622 Berwang, Österreich, über die Beschwerde vom 19. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 17. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 Steuernummer 28-969/9448  beschlossen:   I. Die Beschwerde wird gemäß § 278 Abs. 1 lit b BAO in Verbindung mit § 256 Abs. 3  BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Eva Oktay` | `Univ.-Prof.in Eva Oktay` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christina Schwabendissen` (person)
- `Leckenholz 16, 6622 Berwang, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `28-969/9448` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

**False Positives:**

- `Univ.-Prof.in Elina Hetcamp` — partial — pred is substring of gold: `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp`(person)
- `Florentine Mugge`(person)
- `Rodlhütte 36, 9782 Plone, Österreich`(address)
- `FA Kufstein  Schwaz`(organisation)
- `Finanzamt Österreich`(organisation)
- `59-679/2034`(tax_number)

</details>

---

## `Party_Name_Beschwerdesache_Enhanced` 🏆

**F1:** 0.201 | **Precision:** 0.948 | **Recall:** 0.112  

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
| 0.948 | 0.112 | 0.201 | 191 | 181 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 181 | 10 | 1433 |

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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Jörg Kuhstoss, Hasenberg 58, 3240 Grub bei Kilb, Österreich, über die Beschwerde vom 3. April 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 70-705/2274  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jörg Kuhstoss` | `Jörg Kuhstoss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hasenberg 58, 3240 Grub bei Kilb, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `70-705/2274` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter [Richter] in der Beschwerdesache Shirley Adamczewski,  Stein 26, 9313 Töplach, Österreich, über die Beschwerde vom 13. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 30. Juni 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Februar bis Dezember 2020 zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shirley Adamczewski` | `Shirley Adamczewski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stein 26, 9313 Töplach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Muran Unverricht, Bleischweg 3, 9500 Rennstein, Österreich, über die Beschwerden vom 28. Oktober 2018, vom 9. Februar 2019  und vom 7. Februar 2020 gegen die Bescheide des Finanzamtes Österreich vom 26. Juli 2018  betreffend Abweisung eines Antrages auf Aufhebung des Körperschaftsteuerbescheides 2016  sowie vom 31. Jänner 2019 und vom 16. Jänner 2020 betreffend Körperschaftsteuer 2017 und  2018 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Abweisung eines Antrages auf Aufhebung  des Körperschaftsteuerbescheides 2016 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Muran Unverricht` | `Muran Unverricht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Bleischweg 3, 9500 Rennstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Maurice Speckner,  Hinterweg 94, 2305 Pframa, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 88-902/6713  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Maurice Speckner` | `Maurice Speckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterweg 94, 2305 Pframa, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-902/6713` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_2`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Esmeralda Fietze  in der Beschwerdesache Norbert Hummels,  Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich, über die Beschwerde vom 18. Mai 2022 gegen die Bescheide des Finanzamtes  Österreich vom 25. April 2022 betreffend Gebühren 2021 sowie Gebührenerhöhung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Norbert Hummels` | `Norbert Hummels` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Esmeralda Fietze` (person)
- `Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dietlind Döbereiner  in der Beschwerdesache Siegbert Ptasnik,  Kleinseeweg 4, 6341 Ebbs, Österreich, über die Beschwerden vom 25. September 2015 gegen die Bescheide des  Finanzamtes Linz vom 20. August 2015 betreffend Einkommensteuer 2009 - 2014 und  Umsatzsteuer 2009 - 2014 sowie Einkommen- und Umsatzsteuerbescheid 2015 jeweils vom  19.07.2017 und Einkommen –und Umsatzsteuerbescheid 2016 vom 20.07.2017 zu Recht  erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2009, 2010, 2011, 2015 sowie  gegen die Umsatzsteuerbescheide 2009-2016 werden gemäß § 279 BAO als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Siegbert Ptasnik` | `Siegbert Ptasnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dietlind Döbereiner` (person)
- `Kleinseeweg 4, 6341 Ebbs, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/139653.1`) (sent_id: `deanon_BFG_20260814_TEST/139653.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sheila Mathusczyk, Achatzeweg 10, 5272 Mitterdorf, Österreich, über die Beschwerde vom 15. Juni 2015 gegen den Bescheid des Finanzamtes  Salzburg-Land vom 8. Juni 2015 betreffend Haftungsbescheid /  Lohnsteuer 2012 und 2013  Steuernummer 71-776/4123  zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid/Lohnsteuer 2012 wird als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sheila Mathusczyk` | `Sheila Mathusczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Achatzeweg 10, 5272 Mitterdorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `71-776/4123` (tax_number)

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


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

</details>

---

## `Title_Priv_DoZ_in_Person_Enhanced` 🏆

**F1:** 0.028 | **Precision:** 0.920 | **Recall:** 0.014  

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
| 0.920 | 0.014 | 0.028 | 25 | 23 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 2 | 1591 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dora Grobstich` | `Priv.-Doz.in Dora Grobstich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raul Türkkan` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `24-623/5745` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Christine Kralova` | `Priv.-Doz.in Christine Kralova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Anton Fleischhacker` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Stephanie Dauben  in der Beschwerdesache MedR Erhard Hauprich,  Wohnpark Ager 97, 8264 Obgrün, Österreich, über die Beschwerde vom 22. Juni 2020 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Stephanie Dauben` | `Priv.-Doz.in Stephanie Dauben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Erhard Hauprich` (person)
- `Wohnpark Ager 97, 8264 Obgrün, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Bettina Füsslin` | `Priv.-Doz.in Bettina Füsslin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anastasia Sebott` (person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Olivia Severien` | `Priv.-Doz.in Olivia Severien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Denis Öztopal` (person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich` (address)
- `Pschera Steuerberatung GmbH` (organisation)
- `Finanzamt Salzburg-Stadt` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dietlind Döbereiner  in der Beschwerdesache Siegbert Ptasnik,  Kleinseeweg 4, 6341 Ebbs, Österreich, über die Beschwerden vom 25. September 2015 gegen die Bescheide des  Finanzamtes Linz vom 20. August 2015 betreffend Einkommensteuer 2009 - 2014 und  Umsatzsteuer 2009 - 2014 sowie Einkommen- und Umsatzsteuerbescheid 2015 jeweils vom  19.07.2017 und Einkommen –und Umsatzsteuerbescheid 2016 vom 20.07.2017 zu Recht  erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2009, 2010, 2011, 2015 sowie  gegen die Umsatzsteuerbescheide 2009-2016 werden gemäß § 279 BAO als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dietlind Döbereiner` | `Priv.-Doz.in Dietlind Döbereiner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegbert Ptasnik` (person)
- `Kleinseeweg 4, 6341 Ebbs, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Olivia Rodenbach` | `Priv.-Doz.in Olivia Rodenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Veit Dworatzeck` (person)
- `Zehentberg 7, 4060 Rufling, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)
- `82-692/9441` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139958.1`) (sent_id: `deanon_BFG_20260814_TEST/139958.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Angelika Sczesni  in der Beschwerdesache Desiree Pillsticker,  Georg-Schicht-Platz 191, 4284 Stranzberg, Österreich, über die Beschwerde vom 4. Juni 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Mai 2021 betreffend Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum März 2020 bis März 2021,  Ordnungsbegriff Nr123, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Angelika Sczesni` | `Priv.-Doz.in Angelika Sczesni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Desiree Pillsticker` (person)
- `Georg-Schicht-Platz 191, 4284 Stranzberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Janet Köhle  in der Beschwerdesache der  Textil Bermon, Hans-Bachmann-Straße 4, 2872 Langegg, Österreich  vertreten durch RA-Vertreter, über die Beschwerde vom 31. Mai  2017 gegen die zur Steuernummer 91-124/4580  ergangenen Bescheide des FA St. Johann Tamsweg Zell am See (jetzt  Dienststelle des Finanzamtes Österreich) vom 30. März 2017 betreffend  Einkommensteuer 2009 – 2014 nach Durchführung einer mündlichen Verhandlung am  15.März 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Janet Köhle` | `Priv.-Doz.in Janet Köhle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Textil Bermon` (organisation)
- `Hans-Bachmann-Straße 4, 2872 Langegg, Österreich` (address)
- `91-124/4580` (tax_number)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Diana Pöppel` | `Priv.-Doz.in Diana Pöppel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Judith Leodolter` (person)
- `Mag. Andrea Proidl` (person)
- `Mag. Martin Saringer` (person)
- `Mag.  Harald  Zeller` (person)
- `Spitalbergweg 20, 4775 Wagholming, Österreich` (address)
- `Baldinger & Partner Unternehmens- und Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)
- `56-661/5349` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch Mag. Aleksandar Hofstätter, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rita Wiersbicki` | `Priv.-Doz.in Rita Wiersbicki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corvin Billmaier` (person)
- `Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Mag. Aleksandar Hofstätter` (person)
- `Finanzamtes  Österreich` (organisation)
- `23-971/7442` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Annkathrin Czesielski` | `Priv.-Doz.in Annkathrin Czesielski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Esra Konwischer` (person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jessica Buddeus  in der Beschwerdesache Heidemarie Helwig,  Schmittengasse 288, 3160 Maierhöfen, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des FA Purkersdorf  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 81-530/8966, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jessica Buddeus` | `Priv.-Doz.in Jessica Buddeus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidemarie Helwig` (person)
- `Schmittengasse 288, 3160 Maierhöfen, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH` (organisation)
- `FA Purkersdorf` (organisation)
- `81-530/8966` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Vivian Gastell` | `Priv.-Doz.in Vivian Gastell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Tosca Toussaint` (person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-564/6636` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Gertrude Ortwich  in der Beschwerdesache des  RgR Florens Netzer, Furrach 6, 2184 Prinzendorf an der Zaya, Österreich, betreffend die Beschwerde vom 9. September 2021 gegen den zur  Steuernummer 34-436/7126  ergangenen Bescheid des FA Oststeiermark  vom 10. August 2021  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 beschlossen:  Der angefochtene Bescheid vom 10. August 2021 und die Beschwerdevorentscheidung vom  15. November 2021 werden gemäß § 278 Abs. 1 BAO aufgehoben und die Sache an die  Abgabenbehörde zur Erledigung zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gertrude Ortwich` | `Priv.-Doz.in Gertrude Ortwich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `RgR Florens Netzer` (person)
- `Furrach 6, 2184 Prinzendorf an der Zaya, Österreich` (address)
- `34-436/7126` (tax_number)
- `FA Oststeiermark` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Laura Fromader` | `Priv.-Doz.in Laura Fromader` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Hagen Atar` (person)
- `Oberpetersdorf 6, 4871 Egg, Österreich` (address)
- `FA Wien 2/20/21/22` (organisation)
- `60-848/5470` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/148316.1`) (sent_id: `deanon_BFG_20260814_TEST/148316.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Elfriede Gehbauer  in der Beschwerdesache Ines Linzenich,  Kriechbaumweg 19, 4912 Wiesen, Österreich, vertreten durch Raiffeisenlandesbank Kärnten - Rechenzentrum und  Revisionsverband, reg. Gen.m.b.H., Raiffeisenplatz 1, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 21. Oktober 2024 gegen die Bescheide des Finanzamtes Österreich vom  3. Oktober 2024 über die Festsetzung eines Verspätungszuschlages betreffend Abgabe einer  Zusammenfassenden Meldung für die Zeiträume 09/2022, 10/2022, 02/2023 und 05/2023,  Steuernummer 53-564/3503, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elfriede Gehbauer` | `Priv.-Doz.in Elfriede Gehbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ines Linzenich` (person)
- `Kriechbaumweg 19, 4912 Wiesen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `53-564/3503` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/149310.1`) (sent_id: `deanon_BFG_20260814_TEST/149310.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Beate Gützlaf  in der Beschwerdesache Priv.-Doz.in Alina Vriesman,  Willing 25N, 2561 Pöllau, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Mai 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  Familienbeihilfe für den Zeitraum „April 2023 – September 2023“ zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alina Vriesman` | `Priv.-Doz.in Alina Vriesman` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Beate Gützlaf` (person)
- `Willing 25N, 2561 Pöllau, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)


Die von Herrn Ing. Priv.-Doz.in Linda Schleglmilch zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Priv.-Doz.in Linda Schleglmilch` — partial — pred is substring of gold: `Ing. Priv.-Doz.in Linda Schleglmilch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Priv.-Doz.in Linda Schleglmilch`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/147471.1`) (sent_id: `deanon_BFG_20260814_TEST/147471.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bauerhansl  in der Beschwerdesache des  ÖkR Priv.-Doz.in Sophie Volkenandt, Bahnhofplatz 6, 3372 Ferschnitz, Österreich, über   1) die Beschwerde vom 28. Februar 2019 gegen die Bescheide des Finanzamtes Graz- Umgebung (nunmehr: Finanzamt Österreich) vom 13. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (hinsichtlich Einkommensteuer 2008), Einkommensteuer  und Anspruchszinsen je 2008 sowie   2) die Beschwerde vom 29. Juli 2019 gegen die Bescheide des Finanzamtes Graz-Umgebung  (Finanzamt Österreich) vom 27. Juni 2019 betreffend Einkommensteuer und Anspruchszinsen  je 2009 bis 2013, Steuernummer 35-829/3184,   I. den Beschluss gefasst:  Die Beschwerde gegen den Bescheid vom 13. Dezember 2018 betreffend Wiederaufnahme  hinsichtlich Einkommensteuer 2008 wird zurückgewiesen.

**False Positives:**

- `Priv.-Doz.in Sophie Volkenandt` — partial — pred is substring of gold: `ÖkR Priv.-Doz.in Sophie Volkenandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bauerhansl`(person)
- `ÖkR Priv.-Doz.in Sophie Volkenandt`(person)
- `Bahnhofplatz 6, 3372 Ferschnitz, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Graz`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-829/3184`(tax_number)

</details>

---

## `Title_Hon_Prof_in_Person` 🏆

**F1:** 0.020 | **Precision:** 0.842 | **Recall:** 0.010  

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
| 0.842 | 0.010 | 0.020 | 19 | 16 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 16 | 3 | 1598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Nadine Hupmann` | `Hon.-Prof.in Nadine Hupmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Joachim Kotmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Marion Schlesing` | `Hon.-Prof.in Marion Schlesing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Dimitri Seewaldt` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `Finanzamtes Österreich` (organisation)
- `93-757/0582` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alva Volgenandt  in der Beschwerdesache Pawel Smock,  Kongreßbad 9, 6811 Göfis, Österreich, vertreten durch Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Geusaugasse 39 Tür 8, 1030 Wien, 1.) über die Beschwerde vom 28.02.2014 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 27.01.2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2.) über die Beschwerde vom  28.07.2014 gegen den Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom  30.06.2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012, Steuernummer  20-852/2672, nach der am 19.10.2022 durchgeführten mündlichen Verhandlung zu Recht  erkannt:     I. Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Alva Volgenandt` | `Hon.-Prof.in Alva Volgenandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pawel Smock` (person)
- `Kongreßbad 9, 6811 Göfis, Österreich` (address)
- `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-852/2672` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/141438.1`) (sent_id: `deanon_BFG_20260814_TEST/141438.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  Hon.-Prof.in Chantal Antepoth, Gebharts 4, 4101 Pesenbach, Österreich, über die Beschwerden vom 3. November 2019 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 (nun Finanzamt Österreich) vom 17. Oktober 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis 2018, zu Steuernummer  57-731/4309, den Beschluss:  I. Die Beschwerden betreffend Einkommensteuer 2014, 2016, 2017 und 2018 werden gemäß  § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Chantal Antepoth` | `Hon.-Prof.in Chantal Antepoth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Lisa Pucher` (person)
- `Gebharts 4, 4101 Pesenbach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `57-731/4309` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Wilhelmine Strigl  in der Beschwerdesache Dominik Barfusz,  Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich, über die Beschwerde vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 18. März 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  "Zuerkennung der Familienbeihilfe für den Zeitraum ab Februar 2023" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Wilhelmine Strigl` | `Hon.-Prof.in Wilhelmine Strigl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Barfusz` (person)
- `Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ariadne Iwanowsky` | `Hon.-Prof.in Ariadne Iwanowsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Hon.-Prof. Denis Hoffjan` (person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich` (address)
- `Prof. Yorick Frühbis` (person)
- `Finanzamt Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Jacqueline Traxl` | `Hon.-Prof.in Jacqueline Traxl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Gebhard Hannig` (person)
- `Nußdorfer Markt 4, 4776 Antersham, Österreich` (address)
- `Mag. Paulus Maria Christoph Papst` (person)
- `97-347/7690` (tax_number)
- `FA Braunau Ried Schärding` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frauke Orsini  in der Beschwerdesache Herbert Czarnezki,  Roacher Straße 40, 9241 Ragain, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 30. September 2019 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 28. August 2019, Erf. Nr. Nr1,   betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs. 1 Z 1, TP 5 Abs. 1, TP 6 Abs. 1       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Der angefochtene Sammelbescheid wird abgeändert wie folgt:  1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frauke Orsini` | `Hon.-Prof.in Frauke Orsini` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Herbert Czarnezki` (person)
- `Roacher Straße 40, 9241 Ragain, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt  Österreich/FAÖ` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Evamaria Fränzl` | `Hon.-Prof.in Evamaria Fränzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Raphael Grieben` (person)
- `Habegg 37, 5120 Pirach, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Graz-Stadt` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Lukas Mlnarik  in der Beschwerdesache Mathilda Neuteifl,  Adr, vertreten durch Steuerberater, über die Beschwerde vom 9.4.2015 (gem. § 248 BAO)  gegen den Bescheid des Finanzamtes Innsbruck (nunmehr Finanzamt Österreich/FAÖ) vom  12.12.2014 betreffend die Rückforderung von Familienbeihilfe und Kinderabsetzbetrag für den  Zeitraum 01/2009 bis 11/2014, SV-Nr, nach Durchführung einer mündlichen Verhandlung zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Lukas Mlnarik` | `Hon.-Prof.in Lukas Mlnarik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathilda Neuteifl` (person)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich/FAÖ` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/149717.1`) (sent_id: `deanon_BFG_20260814_TEST/149717.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Antonia Thann  in der Beschwerdesache Chen Stöbermann,  Erlaufpromenade 4, 2442 Schranawand, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, betreffend Beschwerde vom 18. Juni 2024 gegen den Bescheid des  Finanzamtes Österreich vom 12. Juni 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 92-334/0161  beschlossen:   Der Vorlageantrag vom 27.01.2025 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Antonia Thann` | `Hon.-Prof.in Antonia Thann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chen Stöbermann` (person)
- `Erlaufpromenade 4, 2442 Schranawand, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `92-334/0161` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Techn` — partial — pred is substring of gold: `Hon.-Prof.in Techn R Huberta Pauwels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)


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

</details>

---

## `Compound_Title_Person` 🏆

**F1:** 0.435 | **Precision:** 0.826 | **Recall:** 0.295  

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
| 0.826 | 0.295 | 0.435 | 576 | 476 | 100 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 476 | 100 | 1138 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Mag. Josef Nußbaumer` | `Mag. Josef Nußbaumer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


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
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
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
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)


Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)


Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

| Predicted | Gold |
|---|---|
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_50`)


Dr. Omasits sei in Pension.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_66`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_68`)


Cipralex und Psychotherapie  Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  emotional instabile Persönlichkeitsstörung mit histrionischen Zügen   Gutachten zur Gewährung der Invaliditätspension 12.04.2016,   Dr. Omasits (Psychiatrie): paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP  auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |
| `Dr. Omasits` | `Dr. Omasits` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_149`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_151`)


Cipralex und Psychotherapie   Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  9 von 18 Seite 10 von 18

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_152`)


emotional instabile Persönlichkeitsstörung mit histrionischen Zügen  Gutachten zur Gewährung der Invaliditätspension 12.04.2016, Dr. Omasits (Psychiatrie):  paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `RA Mag. Robert Bitsche` | `RA Mag. Robert Bitsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Roxana Dellner` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `MMag. Elisabeth Brunner` | `MMag. Elisabeth Brunner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Serge Pechert` (person)
- `Texing 43, 3143 Oberloitzenberg, Österreich` (address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

| Predicted | Gold |
|---|---|
| `Dr. Maria-Luise Wohlmayr` | `Dr. Maria-Luise Wohlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Günter Gopfauf` (person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich` (address)
- `Finanzamtes Salzburg – Stadt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_85`)


Behandlungen / Medikamente / Hilfsmittel: Efectin 225mg, Inkotan 15mg, Lasix 40mg,  Pantoprazol 20mg, PK-Merz, Pregabalin 75mg 2x1, Sirdalud 4mg 2x1, Zyprexa 2,5mg 1-2-4-0,  Copaxone Inj.lösung, etc.; FÄ-Betreuung bei Dr. Fux alle 6 Wochen.

| Predicted | Gold |
|---|---|
| `Dr. Fux` | `Dr. Fux` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_89`)


Lebt  seit 2005 in teilbetreuter intensiver WG/Verein B. Seit ca. 2012 von Dr. Hofer-Zeni  besachwaltet.

| Predicted | Gold |
|---|---|
| `Dr. Hofer-Zeni` | `Dr. Hofer-Zeni` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

| Predicted | Gold |
|---|---|
| `Dr. Baischer` | `Dr. Baischer` |

**Missed by this rule (FN):**

- `Prof. Maida` (person)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `StR Mag. Dirk Bröders` | `StR Mag. Dirk Bröders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `77-629/3506` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KommR Serge Salameh` | `KommR Serge Salameh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anastasia Schraders` (person)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Caroline Schröer` | `Mag.a Caroline Schröer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Beha` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_2`)


in der Beschwerdesache PhD KommR Louisa Mühle, Waltersdorferstraße 9, 5310 Scharfling, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 6. Dezember 2017 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 6. November 2017 betreffend  1.

| Predicted | Gold |
|---|---|
| `PhD KommR Louisa Mühle` | `PhD KommR Louisa Mühle` |

**Missed by this rule (FN):**

- `Waltersdorferstraße 9, 5310 Scharfling, Österreich` (address)
- `N & N Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |
| `KommR Ing. Ludwig Taspinar, MA` | `KommR Ing. Ludwig Taspinar, MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrich Petrag` | `Mag. Ulrich Petrag` |
| `Mag. Marion Riezinger` | `Mag. Marion Riezinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Nodurft` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Finanzamtes  Linz` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich` (address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)


Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die Firma2 GmbH & CoKG, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Missed by this rule (FN):**

- `Firma2 GmbH & CoKG` (organisation)
- `Firma3  GmbH & CoKG` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)


Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die PhD Mag. Heinrich Hambücher  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_75`)


ihr  Geschäftsanteil wurde von der PhD Mag. Heinrich Hambücher (FN xxxxxx) übernommen;

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Mag. Peter  Mayerhofer` | `Mag. Peter  Mayerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nina Rasem` (person)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Basil Eberhards` | `Mag. Basil Eberhards` |
| `PhD Nancy Prätor` | `PhD Nancy Prätor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/132622.1`) (sent_id: `deanon_BFG_20260814_TEST/132622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache RgR VetR Cassandra Sczech, Hainbuchen 119, 3423 Wördern, Österreich, betreffend Beschwerde vom 22. September 2020 gegen die Bescheide  2015/2016/2017/2018 des Finanzamtes Gänserndorf Mistelbach beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `RgR VetR Cassandra Sczech` | `RgR VetR Cassandra Sczech` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hainbuchen 119, 3423 Wördern, Österreich` (address)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Mag. Sven Weichmann` | `Mag. Sven Weichmann` |
| `Mag. Kurt Kreith` | `Mag. Kurt Kreith` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Mag. Pichler` — partial — pred is substring of gold: `ECA Mag. Pichler & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Mag.a Livia Korowski` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Livia Korowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

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

- `Dr. Thomas` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Dr. Thomas` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`
- `Dr. Thomas` — similar text (different position): `Dr. Thomas Hofer-Zeni`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_149`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Der Bf. wohnt seit 18. Dezember 2006 in Im Mühlfeld 20n, 3205 Weinburg, Österreich /52, Verein B. Der Verein betreut  Erwachsene, Unterstützungsform: teilbetreut intensiv.

**False Positives:**

- `Dr. Thomas` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Univ.Prof. Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Hilde Heidorn` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Hilde Heidorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131857.1`) (sent_id: `deanon_BFG_20260814_TEST/131857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache VetR Eduard van den Berge, Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich, über die Beschwerde vom 6. Juni 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 31. Mai 2019 betreffend Rückforderung Familienbeihilfe und  Kinderabsetzbetrag für September 2018 bis Mai 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `VetR Eduard` — partial — pred is substring of gold: `VetR Eduard van den Berge`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Eduard van den Berge`(person)
- `Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

**False Positives:**

- `Mag. Andrea` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Shoshana Döllmann`(person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

**False Positives:**

- `Mag. Andrea` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hademar Sachteleben, MSc`(person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

</details>

---

## `Honorific_Herr_Frau` 🏆

**F1:** 0.076 | **Precision:** 0.800 | **Recall:** 0.040  

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
| 0.800 | 0.040 | 0.076 | 80 | 64 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 64 | 16 | 1550 |

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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Unverdroß` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)


Herr Bodewein brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `BFG` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_38`)


Mit Aktenvermerk vom 20. April 2023 hielt die Magistratsabteilung 67 zur gegenständlichen  Geschäftszahl fest, ein Telefonat mit PÜG Dienstführung 1,Herr Mayerer (DW TelNr) habe  ergeben, das Überwachungsorgan DNr. ANr habe am Beanstandungstag (10.11.2022) im 22.

| Predicted | Gold |
|---|---|
| `Mayerer` | `Mayerer` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_142`)


Soweit der Bf. darauf verweist, dass Herr Abersfeller aus Gewerbebetrieb  erzielt bzw bei der SVA pflichtversichert sei, mag zwar richtig sein, ist aber bedeutungslos:  Aufgrund des funktionalen Verständnisses des Begriffes der Eingliederung gemäß der zitierten  Judikatur des VwGH ist es ohne Bedeutung, in welcher Weise die aus der Tätigkeit erzielten  Einkünfte zu qualifizieren wären;

| Predicted | Gold |
|---|---|
| `Abersfeller` | `Abersfeller` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)


Sie sehen im Anhang dass Herr Abeles damit bis 27 Dezember  gefahren ist.

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)


Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr Abeles bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_144`)


Zur Begründung der fristgerechten Einbringung der Beschwerde wurde im  Vorlageantrag ausgeführt, die Mitarbeiterin,Frau Pöttmann  habe die Beschwerde am 30. April 2018  um ca. 17:30 Uhr persönlich in den Briefkasten des Finanzamtes eingeworfen und diese  Erledigung auch im Postbuch vermerkt.

| Predicted | Gold |
|---|---|
| `Pöttmann` | `Pöttmann` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_3`)


Begründung  Am 22.03.2024 erließ das Finanzamt für Frau Günter Salfetter, Beschwerdeführerin, einen  Einkommensteuerbescheid (Arbeitnehmerveranlagung) für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `Günter Salfetter` | `Günter Salfetter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


Entscheidungsgründe  Nach dem das Finanzamt in der Beschwerdevorentscheidung (BVE) vom 17.11.2023 das  Pendlerpauschale, den Pendlereuro und den Alleinerzieherabsetzbetrag antragsgemäß  steuermindernd berücksichtigt hat, ist nur mehr strittig, ob sogenannte Familienheimfahrten  von Frau Kuehnhanss (in der Folge: Beschwerdeführerin: Bf) vorliegen und als Werbungskosten zu  berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Kuehnhanss` | `Kuehnhanss` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_14`)


Herr Kaspar Sadowski  führt ab 1.1.2018 den Betrieb „Unternehmensberatung" - der zuvor von der **  GMBH geführt wurde - nun mehr als Einzelunternehmung Kaspar Sadowski  weiter.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_20`)


Da Herr Kaspar Sadowski  immer  Alleingesellschafter der ** GMBH war, ist der Übergang des Verlustvortrages mit 100 %  vorzunehmen.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_17`)


Herr Bf benützt für seine Wochenendfahrten nach A1 einen anderen Pkw.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_18`)


Herr Bf-Gatte ist während der Woche in D-XY whft und in A1 nicht gemeldet;

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation
- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Basyurt`(person)
- `Basyurt`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_18`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat seinen Familienwohnsitz gemeinsam mit seinen Kindern (im Beschwerdejahr 8 und  12 Jahre alt) in Ungarn, wo weder er noch seine Frau Einkünfte erzielen.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_67`)


Unstrittig war, dass die Gesellschafter-Geschäftsführerin, Frau Ges-Gf, mit 25,25% im Sinne des  § 22 Z 2 zweiter Teilstrich EStG 1988 an der Bf. wesentlich beteiligt war.

**False Positives:**

- `Ges-Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Unverdroß  Behindertenbetreuerin` — partial — gold is substring of pred: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_122`)


Herr Bf ist im Wesentlichen in der Lage, einfache Sachverhalte zu erfassen, zeigt sich bei  komplexeren Anforderungen allerdings überfordert.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)
- `Zollamt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_36`)


Herr Sohn wurde zwischenzeitlich gemäß § 62 AlKStG als Abfindungsberechtigter  registriert.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_40`)


Unter Hinweis auf §§ 2 Abs. 1, 4 Abs. 2 Z 5, 8 Abs. 1 Z 2, § 9 Abs. 1 Ziffer 2, § 62 Abs. 2 Z 3, 64  Abs. 3 AlkStG betonte das Zollamt, dass durch den Übergabevertrag vom eee2011 Herr Sohn  unzweifelhaft Eigentümer an den Früchten (= alkoholbildende Stoffe) wurde; auf mündliche  Absprachen zwischen Vater und Sohn komme es nicht an.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_81`)


Herr Sohn hat seit 03.bbb.2013 seinen aktuellen  ordentlichen Wohnsitz (Hauptwohnsitz) in Adresse_Sohn.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_88`)


Wie das Zollamt auch zu diesem Beschwerdepunkt ausführlichst und zu Recht betont hat,  wurde mit der Übergabe im Jahr 2011 der Übernehmer der Liegenschaft, Herr Sohn, auch  Eigentümer an den darauf befindlichen Obstbäumen und an deren Früchte.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_289`)


Zum Beweisantrag:  Herr Baumeister Y X war von 3. Oktober 2013 bis 7. November 2016 gewerberechtlicher  Geschäftsführer der e GmbH (vgl. BFG-Akt I Bl. 56b).

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

</details>

---

## `Herrn_Name_Context` 

**F1:** 0.005 | **Precision:** 0.800 | **Recall:** 0.002  

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
| 0.800 | 0.002 | 0.005 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 1 | 1610 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single_Letter_Name_Context_Enhanced_4` 🏆

**F1:** 0.013 | **Precision:** 0.688 | **Recall:** 0.007  

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
| 0.688 | 0.007 | 0.013 | 16 | 11 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 5 | 1603 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_144`)


A. B. behauptet weiters, von N.N. für seine Tätigkeit als Bodenleger lediglich einen monatlichen Nettolohn von € 1.300,00 ausbezahlt bekommen zu haben.

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_203`)


Die Zeugenaussage des A. vor der Finanzstrafbehörde vom 4.9.2018 dahingehend, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa. X. d.o.o erbracht worden seien, er zwar das „Auftragsschreiben – Subunternehmer“ unterschrieben, aber nicht ausgefüllt habe und er schwarz als weisungsunterworfener Dienstnehmer des N.N. mit einem Nettogehalt von € 1.300,00 für Herrn N. gearbeitet habe, widerspricht der Aussage des Beschuldigten in diesen wesentlichen Punkten diametral.

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_5`)


Seite 2 von 6 Zur Begründung wird ausgeführt, mit Kaufvertrag vom 07.01.2013 habe der Bf. von A.B. die Liegenschaft EZ ***, KG ***** Ortsname zu einem im Vertrag ausgewiesenen Kaufpreis von € 36.000,00 erworben.

| Predicted | Gold |
|---|---|
| `A.B.` | `A.B.` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_53`)


Der Bf. begründete an der Adresse in Untersameting 4, 4894 Römerhof, Österreich (Haus im Alleineigentum seiner Mutter,  der Zeugin N.N.) am xx.xx.xxxx seinen Hauptwohnsitz, meldete diesen jedoch noch am selben  Tag wieder ab;

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Missed by this rule (FN):**

- `Untersameting 4, 4894 Römerhof, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_109`)


Der  Aufgabe eines inländischen Wohnsitzes steht auch das – von der Zeugin N.N. im Zuge ihrer  gerichtlichen Einvernahme (VH-Protokoll S. 7) geschilderte - Faktum entgegen, wonach die Art  und Weise, wann und wie der Bf. im Haus der Mutter nächtigen durfte, immer dieselbe war  und sich bis heute nicht geändert hat.

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_112`)


Schließlich wurde auch die Post nach wie vor an dieser Adresse  zugestellt – wie die Zeugin N.N. im Rahmen ihrer Einvernahme – darlegte;

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_123`)


Die im Zusammenhang mit der Zurverfügungstellung eines Schlüssels getätigten –  übereinstimmenden - Angaben des Bf. bzw. der Zeugin N.N. im Rahmen der mündlichen  Verhandlung waren schließlich ebensowenig überzeugend: Es widerspricht nämlich vorerst  8 von 12 Seite 9 von 12

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_128`)


Entgegen den Ausführungen der Zeugin N.N. bzw. des Bf. geht das erkennende Gericht im  gegenständlichen Fall auch davon aus, dass dem Bf. ein Zimmer im Wohnhaus der Mutter -  zwar nach Rücksprache, aber dennoch - jederzeit zur Verfügung stand: So führte die Zeugin  N.N. vor dem erkennenden Gericht aus, dass sich im 1.

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |
| `N.N.` | `N.N.` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_133`)


Nach den Ausführungen der steuerlichen Vertretung sei am ersten Lichtbild (20210406- 11342.jpg) das Zimmer des Bf. und am zweiten (20210406_113825.jpg) dass für Gäste der  Familie reservierte Gästezimmer dargestellt. Ganz offensichtlich wurde somit dem Bf. – wie  vom Gericht vermutet – das von der Zeugin N.N. beschriebene „Blumenzimmer“ zur Nutzung  zugewiesen.

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_134`)


Die Feststellungen die Postsendungen betreffend resultieren aus den Aussagen der Zeugin N.N.  bzw. des Bf.  9 von 12 Seite 10 von 12

| Predicted | Gold |
|---|---|
| `N.N.` | `N.N.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_93`)


Übereinstimmend gaben sowohl er als auch die Zeugin M.M. weiters an, sich im Zuge einer  dieser Ausreisen am xx.xx.2015 in Phuket kennengelernt zu haben.

**False Positives:**

- `M.M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_96`)


Dass die Zeugin M.M. den Bf. insgesamt dreimal in Österreich, und er die Zeugin viermal nach  dem Entsendungsende in Thailand besuchte, geht einerseits aus den diversen Einreisestempel  im Reisepass des Bf. bzw. den diesbezüglichen Ausführungen der Zeugin hervor.

**False Positives:**

- `M.M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_118`)


Schlussendlich führte die Zeugin M.M. auf die Frage, was mit dem Zimmer im Haus  der Mutter bei Auslandsaufenthalten des Bf. passiere aus, wie folgt: „Bei Auslandsaufenthalten  meines Mannes bleibt dieses Zimmer in Untersameting 4, 4894 Römerhof, Österreich  unbenützt.“ (ZV M.M., VH-Protokoll S.  3)

**False Positives:**

- `M.M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Untersameting 4, 4894 Römerhof, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_119`)


Dass der Bf.    auch heute noch davon ausgeht, nicht im Haus der Mutter wohnhaft zu sein, für den  Bezug des Arbeitslosengeldes ab 2016 aber deren Adresse unter dem Antragspunkt  „ordentlicher Wohnsitz“ angab,    im Streitjahr in Malaysien als nicht steueransässig behandelt und bis Juli 2015 dort  weder über eine Aufenthalts- noch eine Arbeitsbewilligung verfügte,    die Zeugin M.M. erst im Jahr 2015 kennenlernte und schließlich   lediglich 2 Koffer mit Kleidung nach Malaysien mitgenommen hat,  runden das Bild, wonach die Verantwortung des Bf. im Zusammenhang mit der  Wohnsitzaufgabe im Inland unglaubwürdig ist, ab.

**False Positives:**

- `M.M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_126`)


Diese Verantwortung erweist sich auch deshalb als wenig glaubhaft, als im  Gegensatz dazu die Zeugin M.M. zu diesem Beweisthema genau das Gegenteil ausführte (ZV  M.M., VH-Protokoll S. 3: „Mein Mann bzw. mein Freund hat einen Schlüssel für das Haus, ich  selbst habe keinen Schlüssel, weil ich nie alleine herumfahre.“).

**False Positives:**

- `M.M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Title_OMedR_Person` 

**F1:** 0.007 | **Precision:** 0.667 | **Recall:** 0.004  

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
| 0.667 | 0.004 | 0.007 | 9 | 6 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 3 | 1608 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `OMedR Milena Piechulik` | `OMedR Milena Piechulik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brendon Spade` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Walther Kendler` (person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache OMedR Frauke Klutzuweit, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Frauke Klutzuweit` | `OMedR Frauke Klutzuweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Weberkogelstraße 114, 8632 Weichselboden, Österreich` (address)
- `N & N Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `50-666/0525` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/143519.1`) (sent_id: `deanon_BFG_20260814_TEST/143519.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Jeannine Gondrom  betreffend den Antrag des OMedR Simon Pavlicsek, Fulateia 364, 9562 Spitzenbichl, Österreich,   auf Gewährung der Verfahrenshilfe gemäß § 292 BAO im Beschwerdeverfahren zum Bescheid  des Finanzamt Graz-Stadt  vom 06.06.2023 hinsichtlich Rückforderung von Kinderabsetzbetrag und  Familienbeihilfe für vier Kinder für den Zeitraum 09.2020 – 07.2022  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Simon Pavlicsek` | `OMedR Simon Pavlicsek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dr.in Jeannine Gondrom` (person)
- `Fulateia 364, 9562 Spitzenbichl, Österreich` (address)
- `Finanzamt Graz-Stadt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_204`)


0 OMedR Emilia Kusmierz akupunktur 10 Fahrten bodenst FK 151,20  Ansicht FA:  Das Finanzamt beantragte nach Diskussion um die Führung der Fahrstrecke und die Länge der  einfachen Fahrtstrecke die Stattgabe.

| Predicted | Gold |
|---|---|
| `OMedR Emilia Kusmierz` | `OMedR Emilia Kusmierz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_295`)


28.6.24.7 0,00 OMedR Emilia Kusmierz lOx Akupunktur zus.

| Predicted | Gold |
|---|---|
| `OMedR Emilia Kusmierz` | `OMedR Emilia Kusmierz` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_323`)


maps eine Fahrtstrecke  von 65 km in Ansatz gebracht (wie schon die Fahrt zu OMedR Emilia Kusmierz.

| Predicted | Gold |
|---|---|
| `OMedR Emilia Kusmierz` | `OMedR Emilia Kusmierz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Rupert Wedell  in der Beschwerdesache OStR OMedR Rebecca Ehrmanntraut,  Museumplatz 27, 8241 Rohrbachschlag, Österreich, über die Beschwerden vom 10. Oktober 2017 gegen die Bescheide des  FA Baden Mödling  vom 27. Juni 2017 bzw. 10. Juli 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 bis 2015, Steuernummer 38-848/8801, zu Recht erkannt:  I. Den Beschwerden gegen die Bescheide betreffend Einkommensteuer für die Jahre 2012 bis  2015 wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `OMedR Rebecca Ehrmanntraut` — partial — pred is substring of gold: `OStR OMedR Rebecca Ehrmanntraut`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Rupert Wedell`(person)
- `OStR OMedR Rebecca Ehrmanntraut`(person)
- `Museumplatz 27, 8241 Rohrbachschlag, Österreich`(address)
- `FA Baden Mödling`(organisation)
- `38-848/8801`(tax_number)

</details>

---

## `Legal_Context_Party_Person` 

**F1:** 0.002 | **Precision:** 0.667 | **Recall:** 0.001  

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
| 0.667 | 0.001 | 0.002 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 1 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Quentin Girharz` | `Quentin Girharz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Kandler` (person)
- `FA Landeck Reutte` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139879.1`) (sent_id: `deanon_BFG_20260814_TEST/139879.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Giacomello  in der Beschwerdesache Natascha Theys vertreten  durch StB über die Beschwerde vom 3. Oktober 2022 gegen den Bescheid des FA Linz  vom  9. September 2022 über die Festsetzung eines ersten Säumniszuschlages (Steuernummer  86-989/6915 ) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Natascha Theys` | `Natascha Theys` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Wilfried Giacomello` (person)
- `FA Linz` (organisation)
- `86-989/6915` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


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

</details>

---

## `Title_MedR_Person_Enhanced` 

**F1:** 0.002 | **Precision:** 0.400 | **Recall:** 0.001  

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
| 0.400 | 0.001 | 0.002 | 5 | 2 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 3 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Francois Distefano` | `MedR Francois Distefano` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Edwin Teiwes` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Stephanie Dauben  in der Beschwerdesache MedR Erhard Hauprich,  Wohnpark Ager 97, 8264 Obgrün, Österreich, über die Beschwerde vom 22. Juni 2020 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Erhard Hauprich` | `MedR Erhard Hauprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Stephanie Dauben` (person)
- `Wohnpark Ager 97, 8264 Obgrün, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/146580.1`) (sent_id: `deanon_BFG_20260814_TEST/146580.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mikolaj Wegen  in der Beschwerdesache StR MedR Zeno Direk,  Alpenlandhof 5, 3124 Wetzlarn, Österreich, über die Beschwerde vom 28. November 2024 gegen den Bescheid des  Finanzamtes Österreich vom 15. November 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 18-441/3089  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Zeno Direk` — partial — pred is substring of gold: `StR MedR Zeno Direk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mikolaj Wegen`(person)
- `StR MedR Zeno Direk`(person)
- `Alpenlandhof 5, 3124 Wetzlarn, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-441/3089`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Sonja Stradner in der Beschwerdesache  MedR Silke Sommerbauer, MSc, TAL-Schieberstation 2, 2170 Wetzelsdorf, Österreich, vertreten durch GOBBS Steuer- und Unternehmensberatungs- GmbH,  Schubertstraße 3, 2100 Korneuburg, und FAS Network GmbH, Schubertstraße 3, 2100  Korneuburg, über die Beschwerde vom 8. April 2021 gegen den Haftungsbescheid des  Finanzamtes Österreich vom 19. Februar 2021 betreffend Lohnsteuer 2016, Steuernummer  72-745/5137, zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid betreffend Lohnsteuer 2016 wird gemäß  § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Silke Sommerbauer` — partial — pred is substring of gold: `MedR Silke Sommerbauer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Sonja Stradner`(person)
- `MedR Silke Sommerbauer, MSc`(person)
- `TAL-Schieberstation 2, 2170 Wetzelsdorf, Österreich`(address)
- `GOBBS Steuer- und Unternehmensberatungs- GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `72-745/5137`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_9`)


Dagegen brachte die MedR Silke Sommerbauer, MSc.

**False Positives:**

- `MedR Silke Sommerbauer` — partial — pred is substring of gold: `MedR Silke Sommerbauer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MedR Silke Sommerbauer, MSc`(person)

</details>

---

## `Standalone_Name_Rs_Context` 

**F1:** 0.001 | **Precision:** 0.250 | **Recall:** 0.001  

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
| 0.250 | 0.001 | 0.001 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_102`)


GP) der  Anpassung an die unionsrechtlichen Vorgaben dient und auf die EuGH-Urteile in den Rs  Schmelz und Stoppelkamp verweisen (vgl.: Ruppe/Achatz in Ruppe/Achatz (Hrsg),  Umsatzsteuergesetz: Kommentar5 (2017), § 6 UStG, Rz 446), richtet sich die Voraussetzung des  Betreibens eines Unternehmens im Inland nach den unionsrechtlichen Begriffen des Sitzes der  wirtschaftlichen Tätigkeit oder des Ortes einer festen Niederlassung, von dem aus Umsätze  bewirkt werden (vgl.: Luketina, Umsatzsteuerliche Ansässigkeit von Kleinunternehmern bei  Immobilienvermietung, ÖStZ 2019/234, 175).

| Predicted | Gold |
|---|---|
| `Schmelz` | `Schmelz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_713`)


Anlässlich der Entscheidung zur Rechtssache Hedqvist hat der EuGH nachstehende Aussagen  getroffen: Der EuGH ist der Ansicht, dass Bitcoins keine Gegenstände iSd Art 14 der  MwStSystRL sind, da sie die alleinige Funktion haben, als Zahlungsmittel eingesetzt zu werden,  wie gesetzliche Zahlungsmittel (Domes-Hohl Sara Victoria, Die steuerliche Behandlung von  virtuellen Währungen am Beispiel von Bitcoins, 2019, Institut für Finanzrecht Graz, S. 117 Tina  Ehrke-Rabel mit Verweis auf Rs Hedqvist Rz 25).

**False Positives:**

- `Hedqvist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_768`)


Der Umtausch verschiedener Kryptowährungen in andere Kryptowährungen ist analog der  Beurteilung in der Rs Hedqvist als Dienstleistung gegen Entgelt iSd Art 2 Abs 1 MwStSyStRL  anzusehen, die nach § 6 Abs 1 Z 8 lit b UStG 1994 steuerbefreit ist.

**False Positives:**

- `Hedqvist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_164`)


Verhindert die  Nichterfüllung der formalen Anforderungen (namentlich die Nennung des tatsächlichen  Leistungserbringers) die Überprüfung des Vorliegens der materiellen Voraussetzungen für den  Vorsteuerabzug, ist der Vorsteuerabzug nicht zu gewähren (EuGH 11.11.2021, C-281/20, Rs  Ferimet, Rn 27 und 37;

**False Positives:**

- `Ferimet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single_Letter_Name_Context_Enhanced_7` 💣

**F1:** 0.004 | **Precision:** 0.214 | **Recall:** 0.002  

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
| 0.214 | 0.002 | 0.004 | 14 | 3 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 11 | 1611 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_33`)


Vom Finanzamt  Österreich/Dienststelle Fachbereich wurde uns hierzu mitgeteilt, dass die Vergabe einer zweiten  Steuernummer aus verwaltungstechnischen Gründen initiiert ist (Mail Mag. H. 27.07.2022).

| Predicted | Gold |
|---|---|
| `Mag. H.` | `Mag. H.` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_89`)


Die genauen Zahlen seien vom A. (Dr. R.) übermittelt worden.

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_336`)


Diese Berechnung sei der Bf (z.H. Mag. M.) mit Mail vom 29.4.2014 zur Äußerung übermittelt  worden.

| Predicted | Gold |
|---|---|
| `Mag. M.` | `Mag. M.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_166`)


Der Beschwerdeführer brachte in seiner Stellungnahme vom 16.12.2020 dazu vor, dieses  Erkenntnis sei für den Beschwerdeführer nicht einschlägig, dies unter Verweis auf ein  auszugsweise vorgelegtes, undatiertes, „ausschließlich für Zwecke des Rechtsmittelverfahrens  anlässlich der im Mai 2017 abgeschlossenen Außenprüfung des Tourismusverbandes A B“  verfasstes Gutachten des A. Univ.-Prof. Y. Darin zitiert der Verfasser zunächst § 3 des Tiroler  Tourismusgesetzes 2006, LGBl 19/2006, in dessen Abs. 2 die den Tourismusverbänden  obliegenden Aufgaben demonstrativ genannt sind, und verweist auf eine  Anfragebeantwortung des Amtes der B Landesregierung, derzufolge es sich bei diesen  Aufgaben um keinen hoheitlichen handle.

**False Positives:**

- `Univ.-Prof. Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_11`)


Weiters verwies sie darauf, dass der der Behörde vorgelegte klinische psychologische Befund  des Universitätsklinikums vom 21.05.2019 von Mag. W. der Grund für den Bezug der erhöhten  Familienbeihilfe (FB) wäre und die Notwendigkeit der Therapie beinhalte.

**False Positives:**

- `Mag. W.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_87`)


Die von der Bf für das Jahr 2019 geltend gemachten Therapiekosten für die Behebung der bei  ihrer Tochter festgestellten Lernstörung (Legasthenie, Mag. C.) in Höhe von gesamt € 1906,49  werden als ag. B. anerkannt.

**False Positives:**

- `Mag. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_10`)


In Beantwortung der Schreiben des Finanzamtes übermittelte die Bf. am 25. Juni 2020 folgende  Unterlagen betreffend ihren Sohn A.:   – Psychologisches Gutachten von Dr. Mag. E.Sch., Klinische und Gesundheitspsychologin,  allgemein beeidete und gerichtlich zertifizierte Sachverständige für Psychologie,  Psychotherapeutin, und Quirin Spillmann, LLB  Klinische und Gesundheitspsychologin, vom 26. Juni 2019   – Hörverarbeitungsscreening durch Hörtrainer N.R. vom 14. November 2019   (Ergebnis auffällig;

**False Positives:**

- `Mag. E.` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Mag. E.Sch.`(person)
- `Quirin Spillmann, LLB`(person)
- `N.R.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_11`)


Empfehlung zu weiteren Tests bzw. Beratungsgespräch)   – Schreiben der Dr. Mag. E.Sch., w.o., vom 18. Dezember 2019 (Zusammenfassung der  Ergebnisse der erfolgten Begutachtung bezüglich einer vermuteten Legasthenie)   – Schulnachricht der Klasse 6 (6. Schulstufe) der Rudolf Steiner … Freie Waldorfschule vom  14. Februar 2020 (Deutsch genügend, Mathematik nicht genügend, Englisch nicht genügend)   – Befundbericht von Univ. Prof.Charlotte Koebbe  Facharzt für Hals-, Nasen-, Ohrenheilkunde, Kopf- und  Halschirurgie, allgemein beeideter und gerichtlich zertifizierter Sachverständiger vom 27. Mai  2020 (Diagnose: Verdacht auf auditive Verarbeitungsstörung;

**False Positives:**

- `Mag. E.` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)
- `Charlotte Koebbe`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_24`)


Um eine tiefgreifende Entwicklungsstörung zu diagnostizieren, wird  mein Sohn bei Hrn. Mag. L.N. diesbezüglich mehrere Tests durchlaufen müssen.

**False Positives:**

- `Mag. L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_27`)


Die restlichen benötigten Termine bei Hm. Mag. L.N. gebe ich  gerne bekannt, sobald mir diese vorliegen.

**False Positives:**

- `Mag. L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_80`)


Schließlich wurde von der Bf. der klinisch-psychologische Befund (dient zur Vorlage für  diagnostische und therapeutische Maßnahmen) von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 nachgereicht.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_92`)


Empfehlung:   -Psychotherapie für A. mit begleitenden Elterngesprächen   -Förderung der Konzentrationsfähigkeit, -Lese-Rechtschreibförderung   Diagnose nach ICD 10: expressive Sprachschwäche F 80.1, Lese-Rechtschreibschwäche F 81.0,  Störung mit sozialer Ängstlichkeit des Kindesalters F 93.2   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Situation des im Jänner 2007 geborenen Sohn der Bf. stellt sich folgendermaßen dar  (Auszug aus dem zuletzt vorgelegten klinisch-psychologischen Befund von Mag. S.J., Klinische  Psychologin, Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021):   Der Sohn A. besucht die 3. Klasse einer Neuen Mittelschule.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_232`)


Bei der Begutachtung fand das eingangs im Punkt Verfahrensgang genannte, von der Bf.  beschaffte und im Verfahren vorgelegte psychologische Gutachten der Dr. Mag. E.Sch.,  Klinische und Gesundheitspsychologin, allgemein beeidete und gerichtlich zertifizierte  19 von 24 Seite 20 von 24

**False Positives:**

- `Mag. E.` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_273`)


- Schließlich wird im klinisch-psychologischen Befund von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 – Vorstellungsgrund war  wiederum Verdacht auf Autismus – als Anlass für die Untersuchung festgehalten: „… die  Kriterien einer Autismus-Spektrums-Störung wurden nicht zur Gänze erfüllt. Speziell  eingeengten Interessen, stereotypen Verhaltensabläufe und die Über- bzw.  Unterempfindlichkeit gegenüber Reizen fehlen bei A. für eine eindeutige ASS-Diagnose.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Party_Name_NoTitle_Context_Enhanced_2` 

**F1:** 0.002 | **Precision:** 0.200 | **Recall:** 0.001  

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
| 0.200 | 0.001 | 0.002 | 10 | 2 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 8 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Piedro Ringelsbacher, BEd, Hollehnerweg 53, 2565 Schwarzensee, Österreich, über die Beschwerde vom 30. August 2023 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 6, Referat Parkometerabgabe und  Abgabenstrafen, vom 11. August 2023 betreffend Parkometerabgabe zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Piedro Ringelsbacher, BEd` | `Piedro Ringelsbacher, BEd` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Lisa Fries` (person)
- `Hollehnerweg 53, 2565 Schwarzensee, Österreich` (address)
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Lilia Schöpcke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Techn R Lilia Schöpcke`(person)
- `In der Klaus 8, 5651 Winkl, Österreich`(address)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Volker Nissle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Techn R Volker Nissle`(person)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

**False Positives:**

- `Franz-Hinterholzer-Kai` — partial — pred is substring of gold: `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Basil Eberhards`(person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich`(address)
- `PhD Nancy Prätor`(person)
- `FA Linz`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Edwin Lamken`

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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Matthew` — partial — pred is substring of gold: `Matthew McCarthy`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Sascha de Kort`(person)
- `Matthew McCarthy`(person)
- `Stichlberg 18, 4742 Klinget, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138846.1`) (sent_id: `deanon_BFG_20260814_TEST/138846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Techn R Simon Leyn,  Obere Mölten 37, 8232 Stambach, Österreich, über die Beschwerden vom 23. September 2021 gegen die Bescheid des  Finanzamtes Österreich vom 13. September 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 und Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 85-971/5131  zu Recht erkannt:   I. Der Beschwerde gegen den Einkommensteuerbescheid 2019 wird im Umfang der  Beschwerdevorentscheidung Folge gegeben.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Simon Leyn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Techn R Simon Leyn`(person)
- `Obere Mölten 37, 8232 Stambach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-971/5131`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


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

</details>

---

## `Standalone_Name_Verb_Context_Enhanced_2` 💣

**F1:** 0.002 | **Precision:** 0.118 | **Recall:** 0.001  

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
| 0.118 | 0.001 | 0.002 | 17 | 2 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 15 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_76`)


Bei Pool Jackpots ist Oswald Rübberdt  verpflichtet, einen Teil der Einsätze an den Spielehersteller  weiterzuleiten, der in weiterer Folge diese Beiträge und die der anderen Kunden in den Jackpot  einzahlt.  Sowohl bei lokalen als auch bei den Pool Jackpots kommt es bei der Glückspielabgabe zu  groben lokalen Verzerrungen, weil nur ein Teil der Jackpot Kosten der Steuer unterliegt, im Fall  eines österreichischen Gewinnes aber der gesamte Gewinn die Bemessungsgrundlage mindern  würde.

| Predicted | Gold |
|---|---|
| `Oswald Rübberdt` | `Oswald Rübberdt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_4`)


Gegen diesen Bescheid hat Mehmet Köprücü  mit Schreiben vom 20. April 2022 als Vertreter  des Bf und eines weiteren Haftungspflichtigen, an den ebenfalls ein Haftungsbescheid  ergangen ist, Beschwerde eingebracht.

| Predicted | Gold |
|---|---|
| `Mehmet Köprücü` | `Mehmet Köprücü` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_28`)


Daher ist Ihre Beschwerde als unbegründet  abzuweisen.“

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Das Finanzamt erließ folgenden an den Bf. Z.H. MA 11 Kinder-u Jugendhilfe 13,14,15  gerichteten Bescheid:  Abweisungsbescheid  Ihr Antrag vom 3.8.2020 auf Familienbeihilfe wird abgewiesen für:  Name des Kindes (Bf.) Zeitraum von – bis: Mai 2019–Juli 2020  Begründung  Da die Entscheidung des obersten Gerichtshofes vom 20.5.2020 nicht die  Familienbeihilfe für rückwirkenden Zeitraum abspricht, war Ihr Antrag für  oben genannten Zeitraum abzuweisen.

**False Positives:**

- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_48`)


Da keine Übertragung im Bereich der Vermögensverwaltung vorliegt, ist Ihre Beschwerde als  unbegründet abzuweisen.

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

**False Positives:**

- `Frau Franziska Fitzmann` — partial — gold is substring of pred: `Franziska Fitzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franziska Fitzmann`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138846.1`) (sent_id: `deanon_BFG_20260814_TEST/138846.1_31`)


Damit Sie für Ihre  Pension nicht in Deutschland und in Österreich Steuern zahlen müssen, ist Ihre Deutsche  Pension in Österreich von der Steuer befreit.

**False Positives:**

- `Ihre Deutsche  Pension` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_224`)


Warum ist Ihre Homepage noch immer nicht befüllt?

**False Positives:**

- `Ihre Homepage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_122`)


Wirtschaftliche Verfügungsmacht  Die Fälligkeit der ersten vierteljährlichen Beitragszahlung war Ende Feber 2020.

**False Positives:**

- `Ende Feber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

**False Positives:**

- `Herr Quentin Schwartkopp` — partial — gold is substring of pred: `Quentin Schwartkopp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zollamtes Innsbruck`(organisation)
- `Quentin Schwartkopp`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_21`)


Da auch keine andere Möglichkeit einer steuerlichen Begünstigung gefunden werden konnte,  war Ihre Beschwerde abzuweisen.“

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/144232.1`) (sent_id: `deanon_BFG_20260814_TEST/144232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat in der  Beschwerdesache Fiona Reckerth, Am Tasen 60, 4941 Mehrnbach, Österreich  vertreten durch RA Michael Lux, Lange Weg 118,  B-3090 Overjise und DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger Straße 2-4,  1090 Wien, Steuernummer: 03-123/0344, über die Beschwerde vom 15. Dezember 2023  gegen den Bescheid des Finanzamtes Österreich vom 28. November 2023 betreffend  Zurückweisung des Antrages auf Erteilung einer Fiskalvertreter-USt-ID Nummer gemäß § 27  Abs 8 UStG zu Recht:  I)  Der angefochtene Bescheid wird aufgehoben.

**False Positives:**

- `Csoklich Rechtsanwälte` — partial — pred is substring of gold: `DSC Doralt Seist Csoklich Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Fiona Reckerth`(person)
- `Am Tasen 60, 4941 Mehrnbach, Österreich`(address)
- `RA Michael Lux`(person)
- `DSC Doralt Seist Csoklich Rechtsanwälte GmbH`(organisation)
- `03-123/0344`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_17`)


Da  Sie diesem Vorhalt bis zur Beantwortungsfrist (27.12.2023) nicht entsprochen haben (kein  Nachweis, ob eine doppelte Haushaltsführung vorliegt = Voraussetzung für die Gewährung von  Familienheimfahrten), die genaue Beantwortung jedoch für die Klärung des Sachverhaltes von  großer Wichtigkeit gewesen wäre, war Ihre Beschwerde wegen Verletzung der  Mitwirkungspflicht gemäß § 115 Bundesabgabenordnung abzuweisen.

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_50`)


• Nachweis über Ihren eigenen Wohnraum am Familienwohnsitz z.B. durch Mietvertrag,  Kaufvertrag oder einer entsprechenden Haushaltsführung   • Wie viele Kilometer ist Ihr Familienwohnsitz von der Arbeitsstätte entfernt und welche  Fahrtdauer haben Sie zurückzulegen?

**False Positives:**

- `Ihr Familienwohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_63`)


inkl. Angabe der Wohnnutzfläche), sowie Nachweis sämtlicher im Kalenderjahr 2022  geleisteten Zahlungen (Mietkosten, Betriebskosten...)   • Wie viele Kilometer ist Ihr Familienwohnsitz von der Arbeitsstätte entfernt und welche  Fahrtdauer haben Sie zurückzulegen?

**False Positives:**

- `Ihr Familienwohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_77`)


Sollten Sie oben angeführte Unterlagen  nicht oder nur teilweise beibringen, ist Ihre Beschwerde abzuweisen.

**False Positives:**

- `Ihre Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_69`)


Laut Bestätigung ist Ihre Tochter zum Herbsttermin 2022 und zum  Wintertermin 2023 zu diversen Prüfungen für die Matura angetreten, im September 2024  wurde die Vorwissenschaftliche Arbeit abgegeben und im Oktober 2024 positiv abgeschlossen.

**False Positives:**

- `Ihre Tochter` — no gold match — likely missing annotation

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `VetR_Title_Person` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `VetR Dipl` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Dr. Katrin Allram in der Beschwerdesache  VetR Dipl. Kfm. Gernot Kurtius, Oberassling 20, 3921 Schmerbach, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des  Finanzamtes Gänserndorf Mistelbach vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `VetR Dipl` — partial — pred is substring of gold: `VetR Dipl. Kfm. Gernot Kurtius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Katrin Allram`(person)
- `VetR Dipl. Kfm. Gernot Kurtius`(person)
- `Oberassling 20, 3921 Schmerbach, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

**False Positives:**

- `VetR Vivian Hirtel, ` — partial — gold is substring of pred: `VetR Vivian Hirtel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Mag. Josef Ungericht`(person)
- `Mag. Armin Treichl`(person)
- `Mag.a  Patricia Kathan`(person)
- `Mag. Norbert Metzler`(person)
- `Isabella  Alexandra Längle`(person)
- `VetR Vivian Hirtel`(person)
- `Litzlberger Straße 14, 8530 Kresbach, Österreich`(address)

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Quote_Name_Context` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 9 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA für Neurologie und Psychiatrie`(organisation)
- `Bundesamtes für Soziales  und Behindertenwesen`(organisation)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_387`)


Gerade wenn der  Bf. tatsächlich über die afrikanischen Verhältnisse so gut informiert ist, wie er angibt, und eine  Freundschaft besteht, müsste ihm daran gelegen und müsste es ihm auch möglich sein, in  irgendeiner Form mit dem Arzt Kontakt zu halten.

**False Positives:**

- `Kontakt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_5`)


3. Auf Anforderung des Finanzamtes wurde daraufhin in dem vom Sozialministeriumservice  (SMS) "mit Untersuchung" erstellten Sachverständigengutachten vom 13.1./21.1.2021 durch  den Gutachter DrA, FA f. Psychiatrie, ua. Folgendes bescheinigt:  1 von 13 Seite 2 von 13

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_542`)


Tatsächlich machte der Sachverständige Feststellungen in  unterschiedlichen Wohnungen im EG und OG des Hauses, doch betrafen diese nicht  beschädigte Fliesen.

**False Positives:**

- `Feststellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_559`)


angegeben (Quelle: Der  Sachverständige Heft 3/2013).

**False Positives:**

- `Heft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/143631.1`) (sent_id: `deanon_BFG_20260814_TEST/143631.1_153`)


Dass die  Tauschgrundstücke im Zeitpunkt des Vertragsabschlusses und im Zeitraum der Umsetzung des  Teilungsplanes einen geringeren Wert gehabt haben sollen, ist nicht schlüssig, zumal der  Gutachter Verkaufswerte aus 2019 herangezogen hat.

**False Positives:**

- `Verkaufswerte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_54`)


Aus diesem Grund fasste es den Beschluss, das  Finanzamt das Gutachten vom 25. März 2020 von Gutachter Dr. 1 ergänzen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_55`)


Vom Bundessozialamt für Soziales und Behindertenwesen (Sozialministeriumservice) wurde in  der Folge der Gutachter Dr. 2 mit der Erstellung eines neuen Gutachtens beauftragt.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_299`)


FK 27,30   Laut Bf. im Beschwerdeverfahren soll die Ehegattin im Auftrag der Versicherung beim  Gutachter Dr. T gewesen sein.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Single_Letter_Name_Context_Enhanced_2` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 56 | 0 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 56 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_27`)


Die Aussage des A. im Ermittlungsverfahren, wonach er „schwarz“ € 1.300,00 monatlich bekommen habe und keineswegs für eine Firma tätig gewesen sei, habe durch den Beschuldigten glaubhaft in Zweifel gezogen werden können, zumal dieser Lohn - bei einem 20 Arbeitstage enthaltenen Monat - einen Tageslohn von € 65,00 bedeuten würde, was tatsächlich einen nicht glaubhaft geringen Lohn darstelle, wenn sämtliche Versicherungsleistungen für Sozialversicherung, Pensionsversicherung, etc. vom „Schwarzlohnempfänger“ getragen werden müssten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_28`)


Dazu habe der Beschuldigte auch einen Schuldschein des A. vorgelegt und dazu vorgebracht, dass dieser aus Akontiüberzahlungen herrühre, wodurch die Beauftragung des A. im Zuge eines Unternehmens umso glaubhafter werde.

**False Positives:**

- `A.` — no gold match — likely missing annotation
- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_30`)


Scheinrechnungen in sein Rechenwerk aufgenommen habe, wobei - wie oben dargestellt - die Aussage des A. durchaus in ihrer Glaubwürdigkeit erschüttert worden sei.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_88`)


Diese Feststellungen, die auf den Aussagen des A. fußen, sind falsch.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_140`)


Die Fa. X. d.o.o. wurde von A. B., einem serbischen Staatsbürger mit Wohnsitz in Österreich, am 01.03.2012 gegründet.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_141`)


Dieser hat im Zuge der gleichzeitig stattfindenden GPLA-Prüfung niederschriftlich bekanntgegeben, dass die Firmengründung in Slowenien nur deshalb erfolgte, weil N.N. dies so wollte, weil er sich für A., der in Wirklichkeit während des gesamten Prüfungszeitraumes (2012 - 2015) als Dienstnehmer für ihn beschäftigt war, die Lohn- und Sozialabgaben ersparen wollte.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `N.N.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_203`)


Die Zeugenaussage des A. vor der Finanzstrafbehörde vom 4.9.2018 dahingehend, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa. X. d.o.o erbracht worden seien, er zwar das „Auftragsschreiben – Subunternehmer“ unterschrieben, aber nicht ausgefüllt habe und er schwarz als weisungsunterworfener Dienstnehmer des N.N. mit einem Nettogehalt von € 1.300,00 für Herrn N. gearbeitet habe, widerspricht der Aussage des Beschuldigten in diesen wesentlichen Punkten diametral.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `N.N.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_205`)


Der Zeuge A., der nachweislich eine Firma in Slowenien zum Zwecke der Steuervermeidung gegründet hat, Rechnungen über erbrachte Leistungen erstellt und einen Auftrag unterschrieben hat, erschien den erkennenden Senat nicht ausreichend glaubwürdig, dass die für ein Finanzstrafverfahren zu treffende zweifelsfreie Feststellung möglich gewesen wäre, dass er tatsächlich lediglich Dienstnehmer des Beschuldigten gewesen ist.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_15`)


In der Stellungnahme vom 5. August 2011 gab der Steuerberater Folgendes bekannt: "Zu Ihrer Frage der Nutzung der gegenständlichen Immobilie in der Ru.erlauben wir uns wie folgt auszuführen: Die Immobilie wurde seit Jahrzehnten von der Bäckerei H. genützt, welche sich bis 2001 im Besitz von F. (senior) & E. H. (GnbR) befand, welche auch Besitzer der Immobilie waren.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_16`)


Nach dem Tod von F. (sen) H. wurde der Bäckereibetrieb per 31.12.2001 in die NiederTextil GmbH eingebracht (unter Rückbehalt der Immobilie) und die Immobilie wurde Teil des Verlassenschaftsverfahrens.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NiederTextil GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_50`)


Ein auszugsweise vorgelegtes Gutachten des A. Univ.-Prof. Y (zur  Umsatzsteuer des Tourismusverbandes) belege, dass es sich bei den den Tourismusverbänden  gesetzlich übertragenen Aufgaben um keine hoheitlichen Aufgaben handle.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_166`)


Der Beschwerdeführer brachte in seiner Stellungnahme vom 16.12.2020 dazu vor, dieses  Erkenntnis sei für den Beschwerdeführer nicht einschlägig, dies unter Verweis auf ein  auszugsweise vorgelegtes, undatiertes, „ausschließlich für Zwecke des Rechtsmittelverfahrens  anlässlich der im Mai 2017 abgeschlossenen Außenprüfung des Tourismusverbandes A B“  verfasstes Gutachten des A. Univ.-Prof. Y. Darin zitiert der Verfasser zunächst § 3 des Tiroler  Tourismusgesetzes 2006, LGBl 19/2006, in dessen Abs. 2 die den Tourismusverbänden  obliegenden Aufgaben demonstrativ genannt sind, und verweist auf eine  Anfragebeantwortung des Amtes der B Landesregierung, derzufolge es sich bei diesen  Aufgaben um keinen hoheitlichen handle.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_14`)


Die abgabenbehördliche Beihilfen-Datenbank FABIAN weist für Y. letztmalig im Okt.

**False Positives:**

- `Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_121`)


Im Verfahrenszeitraum 2019 bezog die Kindesmutter für Y. in der Schweiz eine „Kinderzulage“  von 2.400,- CHF.

**False Positives:**

- `Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_122`)


Unter Anwendung des gemäß § 20 Abs. 6 UStG 1994 iVm Art 90 VO (EG) 987/2009  maßgeblichen EZB-Referenzkurswertes für 2019 von 1,1124 für 1 CHF (vgl. www.oenb.at bzw.  BMF-Formular L17b-2019) ergibt sich ein Jahresbetrag von 2.669,76 € für die im Jahr 2019 für  Y. bezogenen Schweizer Familienleistungen.

**False Positives:**

- `Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_92`)


Empfehlung:   -Psychotherapie für A. mit begleitenden Elterngesprächen   -Förderung der Konzentrationsfähigkeit, -Lese-Rechtschreibförderung   Diagnose nach ICD 10: expressive Sprachschwäche F 80.1, Lese-Rechtschreibschwäche F 81.0,  Störung mit sozialer Ängstlichkeit des Kindesalters F 93.2   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Situation des im Jänner 2007 geborenen Sohn der Bf. stellt sich folgendermaßen dar  (Auszug aus dem zuletzt vorgelegten klinisch-psychologischen Befund von Mag. S.J., Klinische  Psychologin, Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021):   Der Sohn A. besucht die 3. Klasse einer Neuen Mittelschule.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_102`)


danach wurde  auf Grund des Sachverständigengutachtens des Bundessozialamtes vom 15. Oktober 2019 die  Auszahlung der erhöhten Familienbeihilfe für A. eingestellt. Der Antrag der Bf. vom  3. September 2019 auf Gewährung des Erhöhungsbetrages zur Familienbeihilfe für ihren Sohn  ab Juli 2019 wurde mit dem in Beschwerde gezogenen Bescheid abgewiesen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_83`)


Beweiswürdigung:  Der Sachverhalt ergibt sich aus den vorgelegten Verwaltungsakten, insbesondere aus den von  der Zulassungsbesitzerin erteilten Lenkerauskünften vom 7. Oktober 2022, dem Vorbringen  des Bf. im Einspruch vom 30. November 2022, sowie aus dem Einspruchsvorbringen von O.  vom 20. Oktober 2022 und dessen vorgelegten Sozialversicherungsdatenauszug.

**False Positives:**

- `O.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_74`)


GK ist der Sohn von S. AS ist der Bruder von GK.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_158`)


Ähnlich  wie die belangte Behörde, war die polnische Steuerbehörde der Ansicht, dass die  innergemeinschaftliche Lieferung von BOP an B (A-B) zuzuordnen sei und es habe sich für B. (B)  um einen innergemeinschaftlichen Erwerb von Gegenständen gehandelt. Die zweiten  Lieferungen von Gegenständen durch B. (B) fielen daher nicht unter die Regelung für  innergemeinschaftliche Lieferungen von Gegenständen, so dass diese in den Mitgliedstaaten  der Beendigung der Beförderung der Gegenstände (Staat C) als inländische Lieferungen hätten  besteuert werden müssen (Rz. 12 des Urteils des EuGH v. 7.7.2022, B, C-696/20).

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_162`)


Infolgedessen betrug die effektive  Mehrwertsteuerbelastung von B. 46 % (vgl. Rz. 13 des Urteils des EuGH v. 7.7.2022, B, C- 696/20, hier: 40%).

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_34`)


Der Bf. gab an, zum angegebenen Zeitpunkt mit der Zustellung von Paketen unterwegs  gewesen zu sein und legte zum Nachweis ein Schreiben von X.Langeheinrich Holz GmbH  1100 Wien, Gasse,  vor, in dem von der Firma bestätigt wird, dass der Bf. zur Beanstandungszeit (27. Dezember  2022, 21:21 Uhr) an der Adresse 1230 Wien, [...], mit dem Ausliefern von Paketen im Auftrag  von Amazon beschäftigt gewesen sei.

**False Positives:**

- `X.` — partial — pred is substring of gold: `X.Langeheinrich Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `X.Langeheinrich Holz GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_45`)


Dass die Bf. nicht im Besitz eines Parkausweises gemäß § 29b StVO ist und dass der auf ihre  Tochter N. ausgestellte Parkausweis Nr. 123 bis 1. August 2020 befristet war und für N. ein  4 von 7 Seite 5 von 7

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_79`)


zu 10. im Anhang bei den Rechnungen von H.  zu 11.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_191`)


Dies ergibt sich aus den glaubwürdigen Aussagen des  Zeugen Tranga in seiner Einvernahme am 10. März 2017 sowie aus schriftlichen  Stellungnahmen der Zeugin C. zum Bestand eines Mietverhältnisses.

**False Positives:**

- `C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/143688.1`) (sent_id: `deanon_BFG_20260814_TEST/143688.1_4`)


I.Verfahrensgang und entscheidungsrelevanter Sachverhalt  Mit Bescheid vom 28.05.2021 wurde die Beschwerdeführerin (Bf) aufgefordert, die für P., für  die Zeit von März 2016 bis Oktober 2019 bezogene Familienbeihilfe (FB) bzw.  Kinderabsetzbetrag iHv € 16.559,40 zurückzuzahlen (siehe dazu Rückforderungsbescheid vom  28.05.2021).

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Danielle Merte`(person)
- `Mag.a Susanne Groesche`(person)
- `Unternurpensalm 12, 5141 Moosdorf, Österreich`(address)
- `CONSULTATIO Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes  Wien 1/23`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `76-369/9701`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_2`)


Festsetzung der Energieabgabenvergütung jeweils 2005 - 2008 für  A.,   Bäder,   Büchereien und   Bf. Kindergärten  zu Recht erkannt:   I. Die Beschwerde gegen die Wiederaufnahmebescheide wird abgewiesen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_97`)


Da die Vergütung nur für den Energieaufwand, der  „unmittelbar betrieblichen Zwecken“ diene, zu gewähren sei, habe die Außenprüfung eine  entsprechende Kürzung laut den Unterlagen des A. vorgenommen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_201`)


Bezüglich des A. sei eine Dreiteilung vorstellbar, nämlich in Krankenanstalten, Krankenhaus P.  und Pflegeheime, da der A rechnerisch in drei Teilunternehmungen geteilt werde.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_202`)


Die Außenprüfung gehe von 352 Kindergärten, von 22 Bädern, von 11 Büchereien, von 12  Krankenhäusern, von 14 Pflegeheimen und drei weiteren Betrieben (IT-Abteilung, Wäschereien  und Generaldirektion des A.) aus.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_255`)


Konkrete Bemerkungen zum A.  Bezüglich des A. würden die obigen Ausführung ebenfalls gelten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_260`)


Die Zentrale des A. steuere die 29 Standorte in den Bereichen Budget und Personal zentral.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_264`)


Wegen der Einheitlichkeit des Betriebes gewerblicher Art des A. bzw seiner drei  Teilunternehmungen Krankenanstalten, das Krankenhaus P. und Pflegeheime liege(n) jeweils  nur ein (bzw allenfalls drei) – und nicht 29 - Betrieb(e) gewerblicher Art gemäß § 2 Abs. 1 KStG  vor.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_365`)


Für das AKH habe die Bf die Zuordnung als eigene Teilunternehmung im Rahmen des A. von  sich aus vorgenommen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_384`)


Die  diesbezüglichen Daten würden aus der Generaldirektion des A. stammen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_428`)


Ausschlaggebend sei die  Steuerung des A. durch die Zentrale.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_430`)


Hinsichtlich der drei weitere Bereiche des A., nämlich IT-Bereich, Wäschereien und  Generaldirektion, welche von der Außenprüfung zusätzlich als drei eigene Betriebe  gewerblicher Art angenommen wurden, sei insbesondere nicht nachvollziehbar, dass die  Generaldirektion als eigener Betrieb gewerblicher Art bestehen solle.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_534`)


Strittig ist, ob die 11 Büchereien, 352 Kindergärten, 22 Bäder und 29 Einrichtungen des A. an  den einzelnen Standorten wirtschaftlich selbständig sind und damit jeweils als eigene Betriebe  gewerblicher Art zu qualifizieren sind und in der Folge der allgemeine Selbstbehalt von  400 Euro für jeden dieser über 400 Betriebe gewerblicher Art in Abzug zu bringen ist (Meinung  der Abgabenbehörde) oder ob der allgemeine Selbstbehalt lediglich für vier Betriebe  gewerblicher Art, nämlich Büchereien, Kindergärten, Bäder und  A. zur Anwendung kommt  (Meinung der Bf).

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_566`)


Die Bf vertritt hingegen den Standpunkt, dass aufgrund des einheitlichen Betriebes des A. die  Vorleistungen an das Krankenhaus G. im Jahr 2008 in die Bemessungsgrundlage der  Energieabgabenvergütung einzubeziehen sind.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Beschwerdeführerin, geboren am Geburtsdaten, ist Mutter von zwei Kindern im Alter von  15 Jahren und befand sich in der zweiten Hälfte der 1970er Jahre mehr als drei Monate in der  Kinderstation des A. ö.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_31`)


…  Tz. 4 Entnahmen Verrechnungskonto  Die Entnahmen des P. entbehren jeglicher Rechtsgrundlage, wären einem fremden Dritten  nicht als Darlehen gewährt worden, und werden deshalb als verdeckte Ausschüttung  behandelt.   …  Tz. 5 Vorsteuer 2014  Die Gesellschaft erzielt weit überwiegend gem. § 6 Abs. 1 Z. 8 lit a unecht steuerbefreite  Umsätze.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_54`)


G. würde als  Geschäftsführer der Beschwerdeführerin im Übrigen auch für Entnahmen von P. haften.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_55`)


Somit  ist bei der Bonitätsprüfung die Bonität von G. zu berücksichtigen, welche ausgezeichnet ist.

**False Positives:**

- `G.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_110`)


Werden die Entnahmen der Jahre 2014 (14.256 €) und 2015 (14.018 €) den erklärten  „Einkommen“ der betroffenen Jahre des P. hinzugerechnet, verfügte Letzterer über ein  jeweiliges Einkommen, das G. bereits durch dessen nichtselbständige Tätigkeit erwirtschaftete.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_112`)


über das Verrechnungskonto „P.“ beurteilten Vorgänge/Zustände von P. realisiert worden und  den jeweiligen Gesellschaftern zuzurechnen waren.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_88`)


Am 20. April 2023 langte folgende Beschwerde des Erwachsenenvertreters von S. ein:  „…Der Bescheid wird vom Beschwerdeführer seinem gesamten Inhalt und Umfang nach  angefochten und werden geltend gemacht Verfahrensfehler und unrichtige rechtliche  Beurteilung.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_218`)


Die medizinische Beurteilung in Verbindung mit den von der höchstgerichtlichen Judikatur  aufgestellten und im Beschwerdefall beachteten Erfordernissen, wonach Gutachten eingehend  die Art und das Ausmaß der Leiden und die konkreten Auswirkungen der Behinderung auf die  Erwerbstätigkeit in schlüssiger und nachvollziehbarer Weise zu behandeln haben, lässt die in  den vorliegenden Gutachten nicht feststellbare Selbsterhaltungsunfähigkeit auf Grund der  Behinderung von S. somit mit einer an Sicherheit grenzenden Wahrscheinlichkeit als richtig  erscheinen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_220`)


Es würde - wie schon festgehalten - den Gutachten vielmehr an Schlüssigkeit fehlen, wenn die  untersuchenden Sachverständigen eine Erwerbsunfähigkeit von S. ohne Untermauerung durch  entsprechende Befunde festgestellt hätten.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_25`)


Somit begann für N... einer ihrer größten Herausforderungen, mit der sie am Anfang alleine klar  kommen zu versuchte und stillschweigend psychisch mit sich kämpfte.

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_40`)


Wir haben für N... einen Maturacoach  organisiert, mit dem sie dann etwas gestärkter weiterarbeitete.

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_36`)


Es seien auf ihrem Konto keine Eingänge der  Beihilfe, sondern auf dem Konto von S., der zu diesem Zeitpunkt 2019 bis 2020 in Wien  wohnhaft gewesen sei und dort auch studiert habe, bis zum heutigen Datum.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_37`)


Sie lege die  Haben Umsätze (Kontoauszüge) von S. bei (hier seien die Eingänge ersichtlich).

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_70`)


Es  seien auf ihrem Konto keine Eingänge der Beihilfe, sondern auf dem Konto von S., der zu  diesem Zeitpunkt 2019 bis 2020 in Wien wohnhaft gewesen sei und dort auch studiert habe,  bis zum heutigen Datum.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_71`)


Sie lege die Haben Umsätze (Kontoauszüge) von S. bei (hier seien die  Eingänge ersichtlich).

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Standalone_Name_Following_Role` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Specific_Name_Dok2_Fixed` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Standalone_Name_Verb_Context_Enhanced` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 45 | 0 | 45 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 45 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_78`)


Ich bin - als Serbe, zuletzt aber wohnhaft in Kroatien - aufgrund des Balkankonfliktes im Jahr 1992 nach Deutschland gegangen und von dort im Jahr 2002 nach Österreich.

**False Positives:**

- `Serbe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_52`)


Es ist daher von einer Personenversicherung auszugehen, welche nicht ausschließlich die  Berufsunfähigkeit infolge eines typischen Berufsrisikos abdeckt und dementsprechend nicht als  Werbungskosten, sondern lediglich als Sonderausgaben gemäß § 18 Abs. 1 Z. 2 EStG 1988 im  Rahmen der Höchstbeträge (zu einem Viertel), geltend gemacht werden kann.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_42`)


Gemäß Artikel 10 Abs 1 der Verordnung (EU) 282/2011 des Rates vom 15.3.2011 zur  Festlegung von Durchführungsvorschriften zur Richtlinie 2006/112/EG über das gemeinsame  Mehrwertsteuersystem in der Fassung der Durchführungsverordnung (EU) 1042/2013 vom  7.10.2013 gilt als Ort, an dem der Steuerpflichtige den Sitz seiner wirtschaftlichen Tätigkeit hat,  der Ort, an dem die Handlungen zur zentralen Verwaltung des Unternehmens vorgenommen  werden.

**False Positives:**

- `Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_56`)


Gemäß Artikel 10 Abs 1 der Verordnung (EU) 282/2011 des Rates vom 15.3.2011 zur  Festlegung von Durchführungsvorschriften zur Richtlinie 2006/112/EG über das gemeinsame  Mehrwertsteuersystem in der Fassung der Durchführungsverordnung (EU) 1042/2013 vom  7.10.2013 gilt als Ort, an dem der Steuerpflichtige den Sitz seiner wirtschaftlichen Tätigkeit hat,  der Ort, an dem die Handlungen zur zentralen Verwaltung des Unternehmens vorgenommen  werden.

**False Positives:**

- `Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_151`)


Die Abgabenbehörde beurteilt den Gesellschaftsvertrag, welcher zwischen der Dörfel u. Rudolphson Heizung GmbH & Co KG und dem Bf. abgeschlossen wurde, in wirtschaftlicher Betrachtungsweise als Vertrag, mit  welchem eine Beteiligung nach Art eines stillen Gesellschafters abgeschlossen wurde.

**False Positives:**

- `Vertrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_39`)


Bei Abwägung der Angaben des anzeigelegenden Organs und Ihrer Rechtfertigung als  Beschuldigte, die in der Wahl ihrer Verteidigung völlig frei ist, kann der angezeigte  Sachverhalt als erwiesen angesehen werden.

**False Positives:**

- `Beschuldigte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_88`)


Demnach könne es auch nicht sein, den Steuerpflichtigen hier  schlechter zu stellen als Vertreter, die im Inland tätig seien.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_84`)


Als Hilfsmittel zur Kontrolle der Abgabenent- richtung gilt der Datenträger nach erfolgter Freischaltung in den Fällen des § 2 Abs. 1 lit. a als  Parkkleber, in den Fällen des § 2 Abs. 1 lit. b, c, d in Verbindung mit einer Tages-pauschalkarte  gemäß Anlage VI oder einer Wochenpauschalkarte gemäß Anlage VIa, lit. e in Verbindung mit  einer Tagespauschalkarte gemäß Anlage VI oder einer Wochenpauschalkarte gemäß Anlage  VIa, lit. f sowie des § 3 Abs. 1 lit. a und b als Einlegetafel.

**False Positives:**

- `Parkkleber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_64`)


Beweiswürdigung  Die obigen Feststellungen bezüglich der Tätigkeit als Krankenpflegerin, die Höhe der  Aufwendungen und zum Inhalt der Ausbildung ergeben sich aus den Angaben der Bf.

**False Positives:**

- `Krankenpflegerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_120`)


Ein Siebentel der Bezüge  gemäß § 69 Abs. 5 und 7 gilt als Bezug, der mit dem festen Steuersatz des § 67 Abs. 1 zu  versteuern ist.

**False Positives:**

- `Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_404`)


§ 57 Abs. 2 GSpG nicht zu berücksichtigen sind, weder als Einsatz, noch als ausbezahlter  Gewinn.

**False Positives:**

- `Einsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_27`)


… Folgende  demonstrativ angeführten Indizien lassen … auf einen Gewerbebetrieb schließen: Ausüben der  Tätigkeit als Hauptberuf, Unterhalten eines Büros oder einer Organisation zur Durchführung  von Geschäften, Ausnutzen eines Marktes unter Einsatz beruflicher Erfahrungen etc…“.

**False Positives:**

- `Hauptberuf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_78`)


Der Hauptvergleichsbetrieb  dient als Bewertungsbasis, die einen idealisierten Betrieb umschreibt.

**False Positives:**

- `Bewertungsbasis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_45`)


Im Beschwerdeschreiben erschöpft sich das diesbezügliche  Vorbringen des Bf. in dem Hinweis, dass die zur Vorschreibung gelangte  Abgabennachforderung nicht dem Bf. als Einzelunternehmer, sondern nach einer Art. III –  Umgründung auf die nunmehr bestehende GmbH umzubuchen sei.

**False Positives:**

- `Einzelunternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/136624.1`) (sent_id: `deanon_BFG_20260814_TEST/136624.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Heiko Cortnumme, Barbarasiedlung D/ 3, 9314 Garzern, Österreich, vertreten durch Vertreter, vom 11. Dezember 2017 gegen die Bescheide des  Finanzamtes Österreich, vormals Finanzamtes Bruck Eisenstadt Oberwart, vom 3. Oktober  2017 betreffend Körperschaftsteuer 2006 und 2007, vom 12. Oktober 2017 betreffend  Körperschaftsteuer 2008 sowie vom 16. November 2017 betreffend Körperschaftsteuer 2018,  Steuernummer 01-857/0717, nach der am 9. März 2022 in Hintere Zollamstsstraße 2b,  1030 Wien, durchgeführten mündlichen Verhandlung im Beisein der Schriftführerin R zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Bruck Eisenstadt Oberwart` — type mismatch — same span as gold: `Finanzamtes Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Heiko Cortnumme`(person)
- `Barbarasiedlung D/ 3, 9314 Garzern, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `01-857/0717`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_26`)


Abs. 3) Einkünfte von höchstens 6.000 Euro jährlich erzielt. Der Alleinverdienerabsetzbetrag  steht nur einem der (Ehe-)Partner zu.   Gemäß § 106 Abs. 1 EStG 1988 gelten Kinder im Sinnes des Bundesgesetzes als Kinder, für die  dem Steuerpflichtigen oder seinem Ehepartner mehr als 6 Monate im Kalenderjahr ein  Kinderabsetzbetrag nach § 33 Abs. 3 zusteht.

**False Positives:**

- `Kinder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_81`)


Ein Siebentel der Bezüge  gemäß § 69 Abs. 5 und 7 gilt als Bezug, der mit dem festen Steuersatz des § 67 Abs. 1 zu  versteuern ist.“  Gemäß § 67 Abs. 8 lit. d EStG 1988 sind Ersatzleistungen (Urlaubsentschädigungen,  Urlaubsabfindungen sowie freiwillige Abfertigungen oder Abfindungen für diese Ansprüche)  für nicht verbrauchten Urlaub, soweit sie laufenden Arbeitslohn betreffen, als laufender  Arbeitslohn, soweit sie sonstige Bezüge betreffen, als sonstiger Bezug im Kalendermonat der  Zahlung zu erfassen.

**False Positives:**

- `Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Vorsitzende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Mag. Dieter Ortner`(person)
- `Mag. Reinhard Krassnig`(person)
- `Komm. Rat Max Stechauner`(person)
- `Dirk Ambrose`(person)
- `Herrnberg 22, 5152 Schönberg, Österreich`(address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `21-063/4049`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_746`)


sowie Ausbau des Galeriegeschoßes … („Spitzboden“) für die Nutzung als Abstellraum,  Lagerraum etc“.

**False Positives:**

- `Abstellraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_12`)


Daher könne die Auszahlung der Abfindung  für die vorzeitige Beendigung dieses Dienstverhältnisses als Bezug, der nach Beendigung im  Rahmen von Sozialplänen anfällt, angesehen werden.

**False Positives:**

- `Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_421`)


Eine Tätigkeit als Lauftechniktrainer, deren Ausbildungskosten er ebenfalls geltend gemacht  hat, wurde von ihm ebenfalls nicht ausgeübt.

**False Positives:**

- `Lauftechniktrainer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139407.1`) (sent_id: `deanon_BFG_20260814_TEST/139407.1_29`)


Unschädlich ist die Bezeichnung als Berufung, wenn es sich  rechtlich um einen Vorlageantrag handeln müsste.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_12`)


Begründet wurde dies damit, dass das Psychologiestudium keine Berufsspezifische Fortbildung  (für einen Bediensteten des Magistrates der F als Sicherheitsfachkraft, Arbeitsplatz  Verwendungsgruppe „B“) darstelle.

**False Positives:**

- `Sicherheitsfachkraft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_86`)


Der absolvierte Kurstyp fand als Tageskurs, sowohl in Form eines Präsenzkurses/Webinar bzw.  Blended Learning (dh Präsenz- u. Live-Online-Kurs), als auch als Online-Kurs (zeit- u.  ortsunabhängiges selbstständiges Erarbeiten von Inhalten), statt.

**False Positives:**

- `Tageskurs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_175`)


Der absolvierte Kurstyp fand als Tageskurs,  sowohl in Form eines Präsenzkurses/Webinar bzw. Blended Learning (dh Präsenz- u. Live- Online-Kurs), als auch als Online-Kurs (zeit- u. ortsunabhängiges selbstständiges Erarbeiten von  Inhalten), statt.

**False Positives:**

- `Tageskurs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_22`)


Es sei Sache  der Bf. als Lieferantin, die Ware zum vereinbarten Übergabeort zu transportieren, sie habe die  Kosten dafür zu tragen und trage auch das Risiko von Beschädigungen, Diebstahl oder  sonstigem Untergang der Ware.

**False Positives:**

- `Lieferantin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_194`)


Auf Grund der Verwendung der österreichischen Umsatzsteuer-Identifikationsnummer und der  bisherigen Beurteilung des Erwerbsvorgangs durch die Bf. als Inlandsumsatz, wird das  Mehrwertsteueraustauschsystem durch Abgabe einer entsprechenden Zusammenfassenden  Meldung durch den Lieferanten (A) nicht ausgelöst, sodass der tatsächliche Erwerbsstaat vom  Erwerb der Bf. im Bestimmungsstaat keine Kenntnis erlangen konnte.

**False Positives:**

- `Inlandsumsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vorsitzende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_59`)


Bf. wörtlich: „Zunächst war ich als Eigentümer Abfindungsbrenner und in weiterer Folge als  Berechtigter, es trat daher keine Änderung der abfindungsberechtigten Person ein, nach außen  hin war und bin ich der Abfindungsbrenner.

**False Positives:**

- `Berechtigter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_230`)


Erhält der Stille  bei Beendigung der Gesellschaft einen Anteil an den stillen Reserven und am Firmenwert, gilt  er als Mitunternehmer, der betriebliche Einkünfte und nicht solche aus Kapitalvermögen im  Sinne des § 27 EStG erzielt. Ob eine atypisch stille Gesellschaft vorliegt, ist im Einzelfall nach  dem Gesamtbild der Verhältnisse, insbesondere nach den vertraglichen Vereinbarungen für  den Fall der Beendigung des Gesellschaftsverhältnisses, zu beurteilen (VwGH 22.10.86,  19 von 28 Seite 20 von 28

**False Positives:**

- `Mitunternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_149`)


Für diese Eingabe ist gemäß §§ 13 Abs. 1 Z 1 und 11 Abs. 1 Z 1 GebG 1957 für die Bf als Person,  in deren Interesse die Eingabe erfolgte, die Gebührenschuld (= Verpflichtung zur Entrichtung  dieser Gebühr) in der Höhe von je € 47,30 (dh. insgesamt in Höhe von € 473) zu dem Zeitpunkt  entstanden, in dem ihr die jeweilige Mitteilung der BH Ort1, dass der Schilehrer iSd § 4a Abs. 3  Tiroler Schischulgesetz fachlich befähigt ist, zugestellt wurde.

**False Positives:**

- `Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_154`)


Gemäß §§ 13 Abs. 1 Z 1 und 11 Abs. 1 Z 1 GebG 1957 ist für die Bf als Person, in deren  11 von 13 Seite 12 von 13

**False Positives:**

- `Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_68`)


Vor dem  Hintergrund des objektiven Nettoprinzips erscheine die Ausgestaltung des EKB-S insbesondere  in folgenden zwei Aspekten verfassungswidrig:  Zunächst verwende der EKB-S, im Gegensatz zum Energiekostenbeitrag für fossile  Energieträger (EKB-f), nicht den Gewinn der vergangenen Jahre als Bemessungsgrundlage,  sondern die realisierten Erträge, die ein Beitragsschuldner für den Verkauf und die Lieferung  von Strom in der Union erhalte.

**False Positives:**

- `Bemessungsgrundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_40`)


vergleichbaren Gesellschaften und den Kapitalgesellschaften vergleichbare Gesellschaften, die  den Ort der Geschäftsleitung und den Sitz in einem Mitgliedstaat des Europäischen  Wirtschaftsraumes haben, wenn sie mit einer Zweigniederlassung im Firmenbuch eingetragen  sind und die Beteiligung an den Gruppenmitgliedern (Abs 2) der Zweigniederlassung  zuzurechnen ist, und näher bezeichnete Beteiligungsgemeinschaften (als Personengesellschaft,  Beteiligungssyndikat oder im Wege gemeinsamer Kontrolle) in Frage kommen.

**False Positives:**

- `Personengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_140`)


Vor dem Hintergrund des objektiven Nettoprinzip erscheine die Ausgestaltung der EKB-S  insbesondere in folgenden zwei Aspekten verfassungswidrig:   Zunächst verwende der EKB-S, im Gegensatz zum Energiekostenbeitrag für fossile  Energieträger (EKB-f), nicht den Gewinn der vergangenen Jahre als Bemessungsgrundlage,  sondern die realisierten Erträge, die ein Beitragsschuldner für den Verkauf und die Lieferung  von Strom in der Union erhalte.

**False Positives:**

- `Bemessungsgrundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_193`)


Zu Spruchpunkt I. (Abweisung/Abänderung/Stattgabe)  a) Forderung der Abgabepflichtigen an den Prokuristen, Einlagen Verrechnungskonto,  Entnahmen Verrechnungskonto (Tz. 2 bis 4 des Prüfungsberichtes)  3. Gemäß § 8 Abs. 1 erster Satz KStG 1988 bleiben bei der Ermittlung des Einkommens Einlagen  und Beiträge jeder Art insoweit außer Ansatz, als sie von Personen in ihrer Eigenschaft als  Gesellschafter, Mitglieder oder in ähnlicher Eigenschaft geleistet werden.

**False Positives:**

- `Gesellschafter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/146819.1`) (sent_id: `deanon_BFG_20260814_TEST/146819.1_66`)


Den mit dem Ehepaar Ehepaar X als Mieter am 23.04.2021 abgeschlossenen Mietvertrag  betreffend der Wohnung Z in der Mietobjekt 2 unterfertigten die Bf. als Vermieterin, das  Ehepaar X als Mieter sowie die Tochter und der Sohn der Bf. als Eigentümer.

**False Positives:**

- `Vermieterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_287`)


Wenn auch in der zu Grunde liegenden Anzeige vom 17.4.2020, dass ein Organ der  Straßenaufsicht das Bezug habende Kraftfahrzeug am 8.2.2020, 28.03.2020, 12.04.2020 sowie  am 17.4.2020 in A**, abgestellt gesehen hatte, war dazu auf Grund des erzielten  Beweisergebnisses festzustellen, dass nach den glaubwürdigen Ausführungen der Bf im  Zusammenhang mit der diesbezüglichen Aussage ihres Vaters als Zeuge, die Bf jedenfalls mit  diesem Kraftfahrzeug zu Weihnachten 2019 bis nach Silvester 2020 und von Ende Februar 2020  bis Ende März 2020 (offenkundig bis vor dem 28.3.2020) bei ihrem Vater in Deutschland war  und für die jeweilige Hin- und Rückreise das Bezug habende Kraftfahrzeug mit dem  Kennzeichen XXXX (D) benutzte.

**False Positives:**

- `Zeuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_55`)


Mit Beschwerdevorentscheidung (BVE) vom 18.5.2022 wurde der Beschwerde - nach  Darstellung der bezughabenden gebührenrechtlichen Bestimmungen – zunächst dahin  teilweise stattgegeben, dass die übermittelten Kopien der Lichtbildausweise nicht als  Zeugnisse, sondern vielmehr als Beilagen gem. § 14 TP 5 Abs. 1 GebG zu qualifizieren seien.

**False Positives:**

- `Zeugnisse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_154`)


Für diese Eingabe ist gemäß §§ 13 Abs. 1 Z 1 und 11 Abs. 1 Z 1 GebG 1957 für die Bf als Person,  in deren Interesse die Eingabe erfolgte, die Gebührenschuld (= Verpflichtung zur Entrichtung  dieser Gebühr) in der Höhe von je € 47,30 zu dem Zeitpunkt entstanden, in dem die schriftlich  abschließende Erledigung der BH Ort1 der Bf zugestellt wurde.

**False Positives:**

- `Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_166`)


Gemäß §§ 13 Abs. 1 Z 1 und 11 Abs. 1 Z 1 GebG 1957 ist für die Bf als Person, in deren  Interesse die Vorlage dieser Beilagen zu o.a. Eingaben erfolgte, die Gebührenschuld in Höhe  von gesamt € 132,60 in dem Zeitpunkt entstanden, zu dem ihr die schriftlich abschließenden  Erledigungen der BH Ort1 (Mitteilungen über die fachliche Befähigung) zugestellt wurden.

**False Positives:**

- `Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/148316.1`) (sent_id: `deanon_BFG_20260814_TEST/148316.1_72`)


Für die Anwendung dieser Vorschrift gelten auch nichtselbständige juristische  Personen im Sinne des § 2 Abs. 2 Z 2 als Unternehmer, sofern sie eine eigene  Umsatzsteueridentifikationsnummer haben.

**False Positives:**

- `Unternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_28`)


Erst danach merkten wir als Eltern, welche Belastung diese  2 von 12 Seite 3 von 12

**False Positives:**

- `Eltern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_21`)


In seiner Entscheidung 2007/15/0026 vom 16.12.2010 führte der  VwGH aus, dass es sich bei einer Auszahlung als Einmalzahlung, die auf Grund eines Wahlrechts  anstatt einer Rentenzahlung bezogen werden kann, nicht um eine Abfindung des  Pensionsanspruches im Sinne des § 124b Z 53 EStG, sondern um einen davon getrennten,  eigenständigen Anspruch handle und daher die Drittelbegünstigung nicht zur Anwendung  komme.

**False Positives:**

- `Einmalzahlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_76`)


Der Verwaltungsgerichtshof stellte im Erkenntnis vom 19.12.2013, 2012/16/0047, fest, dass die  Bekanntgabe einer Kontonummer und der Bezeichnung, auf wen das Konto lautet, die nicht  notwendigerweise den Namen des Anspruchsberechtigten tragen müsse, allein in Verbindung  mit der späteren Auszahlung auf dieses Konto noch nicht bewirke, dass der als  Anspruchsberechtigter Auftretende, der diese Angaben getätigt habe, die Familienbeihilfe  nicht mehr bezogen hätte, sondern ein anderer über dieses Konto Verfügungsberechtigter.

**False Positives:**

- `Anspruchsberechtigter Auftretende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Single_Letter_Name_Context_Enhanced_5` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Title_Mag_a_Person_Enhanced` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag.a Priv.-Doz.in Waltraud Süßmayr` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (797, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/145954.1`) (sent_id: `deanon_BFG_20260814_TEST/145954.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache **Christoph Stofmeel**, Hasibederstraße 60, 3972 Scheiben, Österreich, über die Beschwerde vom 10. Mai 2023 gegen  den Bescheid des Finanzamtes Österreich vom 26. April 2023 betreffend  Rückforderungsbescheid vom 26. April 2023 betreffend Familienbeihilfe und  Kinderabsetzbetrag für V Y sowie Familienbeihilfe betreffend E X-P  für Oktober 2022 bis März  2023 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Christoph Stofmeel` (person)
- predicted in sentence: `Mag. Helga Hochrieser`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, **Svenja Nowakowsky**,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Svenja Nowakowsky` (person)
- predicted in sentence: `Univ.-Prof.in Anastasia Schraders`, `KommR Serge Salameh`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, **Hermann**-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Hermann` (person)
- predicted in sentence: `Mag. Alexander Rimser`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_18`)

Nach § 10 Umgründungssteuergesetz gehen diese Verlustvorträge auf das Einzelunternehmen  des Rechtsnachfolgers **Kaspar Sadowski**  über und sind zukünftig mit erzielten Gewinnen aus diesem  Einzelunternehmen gegenzuverrechnen.

- missed: `Kaspar Sadowski` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  **Prof.in Alma Siegers**, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Prof.in Alma Siegers` (person)
- predicted in sentence: `Dr. Judith Leodolter`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_73`)

**Oswald Rübberdt**  bietet keine solchen lokalen  Jackpots an.

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_8`)

Mit fristgerechter E-Mail vom 13. März 2021 (Anhang: Lenkerauskunft) nannte die  Zulassungsbesitzerin Herrn **Bodewein** als jene Person, der das genannte Kraftfahrzeug zum  Beanstandungszeitpunkt überlassen war.

- missed: `Bodewein` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  **Techn R Volker Nissle**, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Techn R Volker Nissle` (person)
- predicted in sentence: `Dr. Peter Steurer`, `Techn`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  **Adriana Zwick**, Via Monsano 359J, 3830 Nonndorf, Österreich, vom 24. April 2025 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 16. April 2025, GZ. MA67/GZ/2025, wegen einer  Verwaltungsübertretung nach § 2 in Verbindung mit § 4 Abs. 2 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Adriana Zwick` (person)
- predicted in sentence: `Mag. Andreas Stanek`

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)

Wenn der Sachwalter die Einvernahme von **Prof. Maida** als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

- missed: `Prof. Maida` (person)
- predicted in sentence: `Univ.Prof. Dr. Eva Maria Maida`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_9`)

Dagegen brachte die **MedR Silke Sommerbauer, MSc**.

- missed: `MedR Silke Sommerbauer, MSc` (person)
- predicted in sentence: `MedR Silke Sommerbauer`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)

Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn **Kaspar Sadowski**  wieder als aktiv gemeldet.

- missed: `Kaspar Sadowski` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_34`)

Sodann hat sich  **Heidemarie Fitzenreiter**  während ihres Besuches des Neve College for Woman - vom 05.09.2022 bis  31.05.2023 - durchgehend in Israel aufgehalten.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)

Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau **Unverdroß**  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

- missed: `Unverdroß` (person)
- predicted in sentence: `Freßdorf`, `Unverdroß  Behindertenbetreuerin`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_57`)

8. Mit Eingabe vom 7.8.2017 brachte die Bf wiederum vor, die Gebührenerhebung sei  unionsrechtswidrig, und legte ein "Gutachten zur unionsrechtlichen Zulässigkeit bestimmter  österreichischer Meldemodalitäten für ausländische Skischulbetreiber im Rahmen des  Ausflugsverkehrs" des **Prof. Dr. YY, LL.M.**, vom 24.7.2017 vor, welches dieser im Auftrag des  Deutschen Skilehrerverbandes e.V. erstellt hatte.

- missed: `Prof. Dr. YY, LL.M.` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des **Jeanne Kraenzlin**, KSV-Donaufreunde 25, 8323 Petersdorf II, Österreich, vertreten durch Treuhand-Union Innsbruck  Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH, Anton-Melzer-Straße 7, 6020  Innsbruck, über die Beschwerde vom 28.09.2021 gegen die Bescheide des Finanzamtes  Österreich vom 23.07.2021 über die Festsetzung der Kapitalertragsteuer für die Zeiträume  2015, 2016, 2017 und 2018, beschlossen:  I. Die angefochtenen Bescheide vom 23.07.2021 über die Festsetzung der Kapitalertragsteuer  für die Zeiträume 2015, 2016, 2017 und 2018 sowie die Beschwerdevorentscheidung vom  01.09.2022 werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an das  Finanzamt aufgehoben.

- missed: `Jeanne Kraenzlin` (person)
- predicted in sentence: `Mag. Josef Ungericht`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_131`)

Lebensjahr, dies wurde in dem Gutachten von Frau **Dr. 2**  zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem nicht attestiert....  Derzeitige Beschwerden:  Die Antragstellerin gibt an: "Ich habe das gleiche seit meiner Jugend, das sind Panikattacken,  Kopfschmerzen und eine Sozialphobie.

- missed: `Dr. 2` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_57`)

Sie ging zu **KzlR Gregor Scholt, BA** einem Chirurg der wollte ihr einen Nadel reinstecken, sie  wurde dort festgehalten.

- missed: `KzlR Gregor Scholt, BA` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_95`)

2.3.2009, **Prof. Maida**: Gehen einiger Schritte nur mit Hilfe möglich.

- missed: `Prof. Maida` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr.in Alice Schöpfel**  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

- missed: `Dr.in Alice Schöpfel` (person)
- predicted in sentence: `Walter Guggenmoos`, `Dr. Schwab Wirtschaftstreuhand`

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache **Prof. Leander Pfleumer, LLM**, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Prof. Leander Pfleumer, LLM` (person)
- predicted in sentence: `Mag. Walter Aiglsdorfer`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_92`)

So bezog **Quentin Schwartkopp**  diesbezüglich auch keinerlei  Einkünfte, die den Schluss zuließen, dass er tatsächlich fruchtgenussberechtigt gewesen sein  soll.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)

Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn **Schwent** gelenkt wurde.

- missed: `Schwent` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Verwaltungsstrafsache gegen  **Andrea Thünnissen**, Kellergasse Helfens 32, 8074 Raaba, Österreich, vom 23. Februar 2020, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Februar 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 17. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet  abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Andrea Thünnissen` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Chaudhuri  in der Beschwerdesache des  **Thorsten Rödamer**, St. Marienweg 37, 9081 Reifnitz, Österreich, über die Beschwerde vom 19. Jänner 2022 gegen den Bescheid des  Finanzamtes Österreich vom 21. Dezember 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 65-515/6745, zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Thorsten Rödamer` (person)
- predicted in sentence: `Univ.-Prof. Wilfried Chaudhuri`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter **Mag Stefan Raab** und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

- missed: `Mag Stefan Raab` (person)
- predicted in sentence: `Mag. Marco Laudacher`, `Mag. Susanne Haim`, `Bettina Domigall`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Die **Charles Dormayr** (=Bf.) erwarb mit Kaufvertrag vom 25.01.2019 die Liegenschaften EZ BBB und  CCC je KG XX um einen Barbetrag von pauschal 100.000 Euro von der X GmbH (= X GmbH).

- missed: `Charles Dormayr` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/146474.1`) (sent_id: `deanon_BFG_20260814_TEST/146474.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Judith Daniela Herdin-Winter** in der  Beschwerdesache Gloria Wirnhier, Winklmannweg 79, 9562 Spitzenbichl, Österreich, über die Beschwerde vom 31. März 2022 gegen  den Bescheid des Finanzamtes Österreich vom 23. März 2022 betreffend Antrag auf  Zuerkennung des Zuzugsfreibetrages gem. § 103 Abs. 1a EStG 1988 vom 26. November 2020,  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Judith Daniela Herdin-Winter` (person)
- predicted in sentence: `Mag. Judith Daniela`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_20`)

auszugehen gewesen, dass zum Zeitpunkt der Einbringung keine Vollmacht vorgelegen und der  Einspruch somit **Pjotr Niessl**  zuzurechnen sei.

- missed: `Pjotr Niessl` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)

IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen **VetR Vivian Hirtel**, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

- missed: `VetR Vivian Hirtel` (person)
- predicted in sentence: `Mag. Josef Ungericht`, `Mag. Armin Treichl`, `Mag.a  Patricia`, `Mag. Norbert Metzler`, `VetR Vivian Hirtel, `

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  **Basil Vanak**, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

- missed: `Basil Vanak` (person)
- predicted in sentence: `Mag. Dieter Fröhlich`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  **Leonie Wehrlin, Bakk. iur.**, Karl-List-Weg 20, 4222 Frankenberg, Österreich, über die Beschwerde vom 30. Dezember 2021 gegen die Bescheide  des Finanzamtes Österreich vom 30. November 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, 2019 und 2020, Steuernummer 01-053/2123  zu Recht  erkannt:   I. Der Beschwerde wird für die Jahre 2018 im Sinne der Beschwerdevorentscheidung vom  18.2.2022 gemäß § 279 BAO teilweise stattgegeben.

- missed: `Leonie Wehrlin, Bakk. iur.` (person)
- predicted in sentence: `Mag. Regina Vogt`, `Leonie Wehrlin`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_5`)

X1-10) über die "Verkürzung von Stempel- oder Rechtsgebühren" hinsichtlich der "Meldung  des Ausflugsverkehrs" gemäß Tiroler Schischulgesetz 1995 für zehn namentlich genannte Schi-  und Snowboardlehrer (AA u.a.) durch die **Prof.in Esra Konwischer** (= Beschwerdeführerin, Bf), eine deutsche  Schneesportschule, erstellt und an das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz durch die Bf aus Jänner 2016 samt Beilagen  (Prüfungszertifikat des Dten.

- missed: `Prof.in Esra Konwischer` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache **Harald Adriaans**, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Harald Adriaans` (person)
- predicted in sentence: `Dr. Ansgar Unterberger`, `Mag. Markus Wagner`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_142`)

A. gab weiters an, dass er als einziger Gesellschafter und Geschäftsführer der X. d.o.o. in den Jahren 2012 und 2013 Seite 13 von 21 Rechnungen an **N.N.** ausgestellt hatte.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_13`)

In Anbetracht der Umstände bitte ich aufrichtig um die Erlassung der Beträge in Höhe von €  4.000,- sowie der € 1.000,- für die **Juri Gübele**.

- missed: `Juri Gübele` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  **KzlR Jens Koudela, BSc**, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `KzlR Jens Koudela, BSc` (person)
- predicted in sentence: `Hon.-Prof.in Merlin Morkam`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_13`)

Mit E-Mail vom 5. Februar 2025 brachte **Pjotr Niessl**  Folgendes (wörtlich) vor:  „wie im Telefon besprochen, hier finden Sie das Vollmacht von M zu mir.

- missed: `Pjotr Niessl` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  **Pjotr Kristall**, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

- missed: `Pjotr Kristall` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache **OSR Juliette Franzisi**, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `OSR Juliette Franzisi` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache **Ingrid Dohrmaier**, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

- missed: `Ingrid Dohrmaier` (person)
- predicted in sentence: `Dr. Hans Blasina`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/148995.1`) (sent_id: `deanon_BFG_20260814_TEST/148995.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache **Nicola Fedrich**, Fresachergasse 7, 5142 Unterhaunsberg, Österreich  vertreten durch Name Erwachsenenvertreter,  Adresse, (gerichtlicher Erwachsenenvertreter) betreffend die Beschwerde vom 9. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 16. Dezember 2022 betreffend  Aufforderung zur Einreichung von Abgabenerklärungen für das Jahr 2021 zu Steuernummer  54-293/0065  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Nicola Fedrich` (person)
- predicted in sentence: `Mag. Johann Fischerlehner`

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr.in Elisabeth Hafner** als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Dr.in Elisabeth Hafner` (person)
- predicted in sentence: `Vorsitzende`, `Mag. Dieter Ortner`, `Mag. Reinhard Krassnig`, `Dirk Ambrose`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_92`)

Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  1.12.1980, ärztlicher Befund der Stellungskommission Wien: Nervosität, Asthenie, **M.**  Scheuermann.

- missed: `M.` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache **DDr. Ali Franzel**, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `DDr. Ali Franzel` (person)
- predicted in sentence: `Mag. David Hell`

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)

Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von **Dr. Thomas Hofer-Zeni** vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

- missed: `Dr. Thomas Hofer-Zeni` (person)
- predicted in sentence: `Dr. Thomas`, `Dr. Thomas`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_239`)

In dem Gutachten wurde das Vorliegen eines Dauerzustandes festgestellt.   Das vierte Sachverständigengutachten des Bundessozialamtes wurde auf Grund einer  Untersuchung des Sohnes der Bf. durch einen Facharzt für Kinder- und Jugendheilkunde am  31. August 2020 erstellt. Bei diesem Gutachten wurden folgende (neu dazugekommenen)  relevanten Befunde bzw. Unterlagen (vgl. die im Verfahrensgang angeführten Atteste)  berücksichtigt:   **Dr. Sch.**, klin.

- missed: `Dr. Sch.` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  **Denis Öztopal**, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

- missed: `Denis Öztopal` (person)
- predicted in sentence: `Priv.-Doz.in Olivia Severien`, `Denis`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_3`)

Entscheidungsgründe  I. Verfahrensgang  **Noah Kreuzpointner** (Beschwerdeführer, Bf.) übermittelte am 16.2.2024 eine Erklärung zur  Arbeitnehmerveranlagung 2023 an das Finanzamt Österreich (FA).

- missed: `Noah Kreuzpointner` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_5`)

Die belangte Behörde stellte am 18. März 2016 mit Einheitswertbescheid zum 1.1.2014,  Hauptfeststellung mit Wirksamkeit ab 1.1.2015, den Einheitswert für den Grundbesitz des  Beschwerdeführers **Siegfried Beyazit** (in der Folge als Bf bezeichnet) Adresse fest, der jeweils im  Hälfteeigentum des Bf und seiner Gattin steht.

- missed: `Siegfried Beyazit` (person)
- predicted in sentence: —

</details>

---

