# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-28T17:05:47.845101

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-28_v12/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 100 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 80 |
| Validation documents | 20 |
| Test documents | 792 |
| Train sentences | 523 |
| Validation sentences | 143 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 30 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 97.2% |
| True Positives | 3484 |
| False Positives | 441 |
| False Negatives | 2932 |
| Total Gold Entities | 6416 |
| Micro Precision | 88.8% |
| Micro Recall | 54.3% |
| Micro F1 | 67.4% |
| Macro F1 | 67.4% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Oberster_Gerichtshof_entities` | 0.2% | 100.0% | 0.1% | 6 | 6 | 0 |
| `KPMG_Alpen_Treuhand_entities` | 0.1% | 100.0% | 0.0% | 3 | 3 | 0 |
| `Universität_Wien_entities` | 0.7% | 100.0% | 0.3% | 21 | 21 | 0 |
| `BMI_entities` | 0.4% | 100.0% | 0.2% | 13 | 13 | 0 |
| `GmbH_Co_OG_entities` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Bundesministeriums_fuer_Finanzen_entities` | 0.3% | 100.0% | 0.1% | 9 | 9 | 0 |
| `Bundesamt_fuer_Soziales_entities` | 1.6% | 100.0% | 0.8% | 51 | 51 | 0 |
| `Bundesfinanzgericht_entities` | 27.2% | 99.0% | 15.8% | 1023 | 1013 | 10 |
| `Landespolizeidirektion_entities` | 2.2% | 97.3% | 1.1% | 75 | 73 | 2 |
| `BMF_entities` | 0.9% | 96.6% | 0.4% | 29 | 28 | 1 |
| `Finanzamt_entities` | 21.9% | 96.5% | 12.3% | 821 | 792 | 29 |
| `Bundesministers_fuer_Arbeit_entities` | 0.7% | 95.8% | 0.4% | 24 | 23 | 1 |
| `AMS_entities` | 1.6% | 94.6% | 0.8% | 56 | 53 | 3 |
| `BFH_entities` | 3.0% | 93.3% | 1.5% | 104 | 97 | 7 |
| `Wiener_Gemeinderates_entities` | 1.7% | 91.5% | 0.8% | 59 | 54 | 5 |
| `Finanzamtes_standalone` | 15.8% | 84.8% | 8.7% | 659 | 559 | 100 |
| `Firma_entities` | 0.9% | 83.3% | 0.5% | 36 | 30 | 6 |
| `Magistrat_Stadt_Wien_entities` | 17.3% | 79.5% | 9.7% | 781 | 621 | 160 |
| `Fa_Abbreviation_entities` | 0.3% | 69.2% | 0.1% | 13 | 9 | 4 |
| `m_b_H_entities` | 0.3% | 47.8% | 0.2% | 23 | 11 | 12 |
| `Steuerberatungsgesellschaft_entities` | 0.1% | 42.9% | 0.0% | 7 | 3 | 4 |
| `FA_Location_entities` | 0.3% | 16.9% | 0.2% | 65 | 11 | 54 |
| `Finanzamt_StandAlone` | 0.1% | 8.8% | 0.0% | 34 | 3 | 31 |
| `Specific_Company_AGG_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Company_GmbH_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Snajdr_ECommerce_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fa_Glanzder_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Jackobi_Horbank_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Weinzinger_Partner_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt_Wien_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hoch_IT_GmbH_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Derdonal_Garten_AG_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SK_Telecom_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deutsche_Telekom_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `T-Mobile_Austria_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `A1_Hutchinson_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Post_AG_entities` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `SNWG_Textil_GmbH_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Oberster_Gerichtshof_entities` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b7aa16d8`  
**Description:**
Matches 'Obersten Gerichtshofes' which was previously missed.

**Content:**
```
Obersten\s+Gerichtshofes
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 4803 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_13`)


Die B habe der Bf neben ihrem regulären Pensionsbezug einen Schadenersatz zu  leisten, der sich aus dem Urteil des Obersten Gerichtshofes vom Datum_1, xObxxx/xxx, ergebe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofes` | `Obersten Gerichtshofes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_32`)


Die B habe der  Bf aufgrund des erwähnten Urteils des Obersten Gerichtshofes Schadenersatz zu leisten.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofes` | `Obersten Gerichtshofes` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_35`)


Im konkreten Fall sei aber nicht die Bf  Steuerschuldnerin, sondern die B, die ihrer Verpflichtung aus dem Urteil des Obersten  Gerichtshofes sowie dem später vereinbarten Vergleich über die Zahlung der anteiligen  Lohnsteuer, nicht nachkomme.

| Predicted | Gold |
|---|---|
| `Obersten  Gerichtshofes` | `Obersten  Gerichtshofes` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_11`)


b) Beschluss des Obersten Gerichtshofes v. 27.5.2020, GZ. xx2, womit die je ao Revision beider  Parteien zurückgewiesen und ua. (S. 6 oben) ausgeführt wird:  "Die Einordnung des Rechtsverhältnisses der Streitteile als Dienstvertrag ist danach insgesamt  nicht weiter korrekturbedürftig";

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofes` | `Obersten Gerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_87`)


Dies gelte umso mehr, als eine Erweiterung der Kündigungsmöglichkeiten  nach Ansicht des Obersten Gerichtshofes nur sehr eingeschränkt möglich sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofes` | `Obersten Gerichtshofes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_163`)


Der genannten Entscheidung des Obersten Gerichtshofes ist darüber hinaus noch zu  entnehmen, dass der Betrieb auf eigene Rechnung des Halters erfolgt, wenn er den Nutzen aus  der Verwendung zieht und die Kosten trägt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofes` | `Obersten Gerichtshofes` |

</details>

---

## `KPMG_Alpen_Treuhand_entities` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bfeb20f1`  
**Description:**
Matches the long KPMG entity name.

**Content:**
```
KPMG\s+Alpen\-Treuhand\s+GmbH\s+Wirtschaftspr\u00fcfungs\-\s+und\s+Steuerberatungsgesellschaft
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 5185 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Hermann Bloehdorn, Bierbaum 35, 8983 Bad Mitterndorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerden vom 9. und 13. Jänner 2014 sowie vom 25. September 2015 und vom 20.  Oktober 2017 gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt  Österreich) vom 6. Dezember 2013, sowie vom 26. August 2015 und vom 11. September 2017  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 bis 2014, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` | `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Mag. Judith Daniela Herdin-Winter` (person)
- `Hermann Bloehdorn` (person)
- `Bierbaum 35, 8983 Bad Mitterndorf, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/137197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137197.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Gertrude Hochnadel, Habalm 9, 3073 Dachsbach, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 3. März 2022 gegen den Bescheid des Finanzamtes Österreich  Finanzamtes Österreich vom 11. Februar 2022 betreffend Berichtigung (§ 293 BAO) des  Aufhebungsbescheides (§ 299 BAO) vom 3. Dezember 2021 hinsichtlich Einkommensteuer  2019 Steuernummer 07-052/8427  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` | `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Dr. Gabriele Krafft` (person)
- `Gertrude Hochnadel` (person)
- `Habalm 9, 3073 Dachsbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `07-052/8427` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Dr. Adebiola Bayer in der Beschwerdesache  Jean Stapeler, Strittfeldstraße 9, 6260 Bruck am Ziller, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  betreffend die Beschwerden  vom 19. Dezember 2016 gegen den Körperschaftsteuerbescheid Gruppe 2014 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 1. Dezember 2016 gemäß der  Änderung nach § 295 Abs. 1 BAO vom 30. Jänner 2017,  vom 23. Februar 2018 gegen den Körperschaftsteuerbescheid Gruppe 2015 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 26. Jänner 2018 gemäß der Änderung  nach § 295 Abs. 1 BAO vom 15. Februar 2019,    vom 27. Februar 2019 gegen den Körperschaftsteuerbescheid Gruppe 2016 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 20. Februar 2019,    vom 18. Februar 2020 gegen den Körperschaftsteuerbescheid Gruppe 2017 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 14. Februar 2020 sowie    vom 25. Mai 2020 gegen den Körperschaftsteuerbescheid Gruppe 2018 des Finanzamtes Wien  1/23 (nunmehr Finanzamt für Großbetriebe) vom 15. Mai 2020  den Beschluss:  Die Parteien werden gemäß § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Bundesfinanzgerichts in der gegenständlichen Beschwerdesache in Bezug auf die angeführten  angefochtenen Bescheide noch Beschwerdevorentscheidungen zu erlassen sind.

| Predicted | Gold |
|---|---|
| `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` | `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Dr. Adebiola Bayer` (person)
- `Jean Stapeler` (person)
- `Strittfeldstraße 9, 6260 Bruck am Ziller, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Bundesfinanzgerichts` (organisation)

</details>

---

## `Universität_Wien_entities` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `b4be58e0`  
**Description:**
Matches 'Universität Wien' which was previously missed.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 5772 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_60`)


In der Beschwerde gegen die versagte Anerkennung im Einkommensteuerbescheid 2017 gibt  der Bf. an, dass die Fahrzeit zur rechtswissenschaftlichen Fakultät der Universität Wien laut  Fahrplanauskunft mehr als eine Stunde, mitunter bis zu 1 Stunde 30 Minuten dauert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_77`)


Von Wien Hütteldorf aus erreicht man das Juridikum der Universität Wien mit den  U-Bahnen U4 und U2 und vom Westbahnhof aus erreicht man die Universität entweder mit  der U-Bahn U3 (Herrengasse) oder mit den U-Bahnen U3 und U2.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_87`)


In der Beschwerde gegen die versagte Anerkennung im Einkommensteuerbescheid 2017 gibt  der Bf. an, dass die Fahrzeit zur rechtswissenschaftlichen Fakultät der Universität Wien laut  Fahrplanauskunft mehr als eine Stunde, mitunter bis zu 1 Stunde 30 Minuten dauert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_12`)


Weiters habe die Tochter im Sommersemester 2018 (richtig 2019) an der Universität Wien  immatrikuliert und den Studiengang „Kultur- und Sozialanthropologie" inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_30`)


Die Vorlage der Inskriptionsbestätigung der Universität Wien für das Bachelorstudium Kultur-  und Sozialanthropologie im Sommersemester 2019 sei kein Nachweis über die Teilnahme an  Vorlesungen bzw über die Anmeldung oder Absolvierung von Prüfungen.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_63`)


Im Sommersemester 2019 immatrikulierte T. an der Universität Wien, inskribierte als  ordentliche Studierende das Bachelorstudium „Kultur- und Sozialanthropologie" (UA033 610)  und besuchte die Vorlesungen „Grundlagen sozialwissenschaftlicher Methodologie“ und  „Fachspezifische Einführung“.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_142`)


Inskription an der Universität Wien im Studiengang „Kultur- und Sozialanthropologie“  T. war im Sommersemester 2019 an der Universität Wien im Studiengang „Kultur- und  Sozialanthropologie" (UA033 610) inskribiert und hat nach den Angaben der Bf.  (Vorhaltsbeantwortung vom 25. Februar 2020) die Veranstaltungen „Grundlagen  sozialwissenschaftlicher Methodologie“ und „Fachspezifische Einführung“ besucht.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_147`)


Angesichts des Vorbringens der Bf., ihre Tochter habe sich im Laufe des Semesters für die  Aufnahmeprüfung an der FH Kufstein vorbereitet und keine Prüfungen an der Universität Wien  11 von 13 Seite 12 von 13

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `FH Kufstein` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_156`)


(https://www.fh-kufstein.ac.at/Bewerben/faq/Bewerbung-Aufnahme/Wie-funktionieren-der- Online-Aufnahmetest-und-das-Aufnahmegespraech )  Die Bf. brachte zum zeitlichen Umfang der Vorbereitungszeit ihrer Tochter auf den  Aufnahmetest bei der FH Kufstein lediglich vor, dass T. im Sommersemester 2019 an der  Universität Wien im Studiengang „Kultur- und Sozialanthropologie" (UA033 610) inskribierte  und sich im Lauf des Semesters für die Aufnahmeprüfung an der FH Kufstein (März 2019)  vorbereitet habe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `FH Kufstein` (organisation)
- `FH Kufstein` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/139582.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139582.1_4`)


Lebensjahr vollendete ist seit dem  WS 2020/21 an der Universität Wien bis laufend im Masterstudium des Faches  Betriebswirtschaft inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/139582.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139582.1_105`)


Lebensjahr vollendende Beschwerdeführerin (Bf.) ist an der  Universität Wien seit dem WS 2020/21 bis laufend im Masterstudium Betriebswirtschaft  inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_12`)


Es liege somit ab März  2020 keine Berufsausbildung iSd FLAG vor und bestehe kein Anspruch auf Familienbeihilfe für  T..  Der Bf. brachte in seiner dagegen eingebrachten Beschwerde vom 28. Februar 2022  (eingelangt beim Finanzamt am 01. März 2022) vor, dass seine Tochter im Wintersemester  2015 ihre Sprachstudien an der Universität Wien begonnen und im Oktober 2019 an der  University of Birmingham den Titel Master of Arts (Translation Studies) with Distinction  (Auszeichnung) erworben habe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_14`)


Nach Rückkehr aus Großbritannien habe seine Tochter ihre Studien an der Universität Wien im  Wintersemester 2019/20 fortgesetzt und ihre letzte Prüfung am 11. Februar 2020 abgelegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_38`)


Mindeststudienzeit um 1 Jahr durch Auslandsstudium, Fortsetzung  der Studien an der Universität Wien und Prüfung zuletzt am 11. Februar 2020 erhalten habe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_45`)


T. schloss ihr Sprachstudium an der University of Birmingham im Dezember 2019 mit dem Titel  Master of Arts (Translation Studies) with Distinction (Auszeichnung) ab und begann ab dem  Wintersemester 2019 (Oktober 2019) an der Universität Wien das Masterstudium Translation  Deutsch Englisch (A070 331 342).

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_46`)


Die letzte Prüfung an der Universität Wien wurde am 11.  Februar 2020 abgelegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_125`)


Zusammenfassend wird Folgendes festgestellt:  Die Tochter des Bf. schloss ihr Sprachstudium an der University of Birmingham im Dezember  2019 mit dem Titel Master of Arts (Translation Studies) with Distinction (Auszeichnung) ab und  begann ab dem Wintersemester 2019 (Oktober 2019) an der Universität Wien mit dem  Masterstudium Translation Deutsch Englisch (A070 331 342).

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_126`)


Die letzte Prüfung an der  Universität Wien wurde am 11. Februar 2020 abgelegt (ab dem SS 2020 keine ECTS-Punkte).

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/140029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140029.1_24`)


Lebensjahr vollendet und war laut  Studienbestätigung vom 9.4.2021 im Sommersemester 2021 an der Universität Wien im  Studienstatus „ordentlich“ zum UA 032 375 342 Bachelorstudium „Transkulturelle  Kommunikation Polnisch Englisch“ zur Fortsetzung gemeldet.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/140029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140029.1_25`)


Laut Sammelzeugnis, ausgestellt am 9.4.2021 von der Universität Wien, hat die  Beschwerdeführerin im Wintersemester 2020 Prüfungen mit insgesamt 16 ECTS-Punkten  positiv absolviert (StEOP PM1 Modulprüfung Transkulturelle Kommunikation I, 8 ECTS am  1.2.2021;

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `BMI_entities` 🏆

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `59be53d2`  
**Description:**
Matches the abbreviation BMI (Bundesministerium für Inneres) in legal contexts.

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 6323 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_63`)


Die Gruppe D) bezeichnet die Bf. mit „vom Arzt zum Erreichen und zur Aufrechterhaltung eines  einigermaßen an Normalgewicht heranreichenden Ernährungszustandes verordnet  (Ausgangspunkt 47 kg = BMI 16)“.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_56`)


Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung – Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 11 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_58`)


1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_40`)


Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung - Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 1 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_41`)


Diese Verordnung regelt gemäß § 1 Z 1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_27`)


Unbestritten ist, dass der Sohn der Bf. aufgrund eines Sondervertrages gemäß § 36 VBG seit  1. September 2019 in einem Dienstverhältnis zum Bund steht und seit damals die zwei Jahre  dauernde Grundausbildung für den Exekutivdienst (Polizeigrundausbildung) nach der  Grundausbildungsverordnung - Exekutivdienst BMI absolviert (vgl. Seite 1 des o.a.  Erkenntnisses vom 24.06.2021).

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_29`)


Zu Spruchpunkt I.  Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung – Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 1 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_30`)


Diese Verordnung regelt gemäß § 1 Z. 1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_65`)


Mit Schriftsatz vom 07. Jänner 2022 stellte der Bf. einen Vorlageantrag in welchem er  zusätzlich zu dem Vorbringen in der Beschwerde noch angibt, dass eine weitere Möglichkeit für  die steuerfreie Berücksichtigung der € 2.114,80 ein berichtigter Lohnzettel des BMI wäre.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_73`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Missed by this rule (FN):**

- `Flughafen München` (organisation)
- `Frontex` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_81`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Missed by this rule (FN):**

- `Flughafen München` (organisation)
- `Frontex` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_113`)


Befundbericht Dr. … Pa…, FA Psychiatrie, 11.7.2018:   Seit 4.9.2014 bei mir in Behandlung, leichte Intelligenzminderung (IQ 80, Leseschwäche,  Aufmerksamkeitsdefizit), einer Dysthymie mit einer atypischen Anorexia nervosa (BMI dzt.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/146425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146425.1_47`)


Das Bundesfinanzgericht ist im angefochtenen Erkenntnis mit näherer Begründung zum  Ergebnis gelangt, die Polizeigrundausbildung - die zwar durch generelle Normen, und zwar  durch die Grundausbildungsverordnung - Exekutivdienst BMI, BGBl. II Nr. 153/2017, geregelt  ist - sei, nicht zuletzt im Hinblick auf das Gehalt der Auszubildenden, mit einer Lehre - in einem  Lehrberuf - nicht vergleichbar.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

</details>

---

## `GmbH_Co_OG_entities` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `276f2c64`  
**Description:**
Matches GmbH & Co OG entities with strict word boundaries to prevent capturing preceding context.

**Content:**
```
(?:^|\s|,|\(|\[)([A-Z][a-zA-Z0-9\s\.\-]+(?:\s+Steuerberatungs)?(?:\s+GmbH\s+&\s+Co\s+OG))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 2761 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/141326.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141326.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat in der Revisionssache  Alois Milter, Obere Marktwiese 11, 6458 Sölden, Österreich  Steuernummer: 75-325/5614, vertreten durch die Reinhard  Stulik Steuerberatungs GmbH & Co OG, Färbergasse 3, 3150 Wilhelmsburg, über den Antrag  des Revisionswerbers vom 10. Juli 2023 der gegen das Erkenntnis des Bundesfinanzgerichtes  vom 6. Juni 2023, RV/7103454/2022 (belangte Behörde: Finanzamt Österreich), hinsichtlich  Wiederaufnahme der Verfahren betreffend Einkommensteuer 2011 – 2014 sowie  hinsichtlich Einkommensteuer 2011 – 2015, erhobenen außerordentlichen Revision die  aufschiebende Wirkung zuzuerkennen, den Beschluss:   I)  Gem.

| Predicted | Gold |
|---|---|
| `Reinhard  Stulik Steuerberatungs GmbH & Co OG` | `Reinhard  Stulik Steuerberatungs GmbH & Co OG` |

**Missed by this rule (FN):**

- `Mag. Günter Narat` (person)
- `Alois Milter` (person)
- `Obere Marktwiese 11, 6458 Sölden, Österreich` (address)
- `75-325/5614` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Finanzamt Österreich` (organisation)

</details>

---

## `Bundesministeriums_fuer_Finanzen_entities` 

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b663f252`  
**Description:**
Matches 'Bundesministeriums für Finanzen' and 'Bundesminister für Arbeit, Soziales und Konsumentenschutz'.

**Content:**
```
(?:Bundes(?:ministeriums\s+f\u00fcr\s+Finanzen|minister\s+f\u00fcr\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.003 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 5786 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_24`)


Näher geregelt wird das in einer diesbezüglichen Verordnung des Bundesministeriums für  Finanzen betreffend Berufsausbildung eines Kindes außerhalb des Wohnortes.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für  Finanzen` | `Bundesministeriums für  Finanzen` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_24`)


PS: Im Steuerhandbuch des Bundesministeriums für Finanzen ist folgendes nachzulesen:  Heilbehandlung: Im Falle einer Behinderung können auch die Kosten einer Heilbehandlung im  Zusammenhang mit der Behinderung zusätzlich zum Pauschalbetrag und ohne Kürzung durch  den Selbstbehalt berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_30`)


Ergänzend zu § 35 EStG wurde die Verordnung des Bundesministeriums für Finanzen über  außergewöhnliche Belastungen (BGBL 303/1996) erlassen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/136317.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136317.1_121`)


Die für die Datenstromübermittlung und für die Übermittlung mittels  eines Webservice erforderlichen organisatorischen und technischen Spezifikationen (zB XML- Struktur, WSDL) sind auf der Website des Bundesministeriums für Finanzen abrufbar zu halten.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_33`)


Punkt a):  Hingewiesen wird auf die Erlässe des Bundesministeriums für Finanzen zum Thema  Selbstberechnung, dort heißt es wörtlich:  Die für die Ermittlung der Bemessungsgrundlage außerhalb des elektronischen  Selbstberechnungsverfahrens erstellten Berechnungsblätter und/oder Ausdrucke von  automatischen Berechnungshilfen sind dem Selbstberechnungsakt beizuschließen und  gemeinsam mit der über den Rechtsvorgang ausgefertigten Schrift sieben Jahre  aufzubewahren.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_164`)


In der Währungsumrechnungstabelle für 2014 (L17b-2014) des Bundesministeriums für  Finanzen wird vergleichsweise bei den Referenzkursen der EZB ein Umrechnungskurs 2014 des  Schweizer Franken mit 1,21 Euro angegeben (ohne 1,5 % Abschlag für den Steuerwert,  übernommen von der OeNB, 2.1.2015).

| Predicted | Gold |
|---|---|
| `Bundesministeriums für  Finanzen` | `Bundesministeriums für  Finanzen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/143833.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143833.1_22`)


2. Beweiswürdigung   Dem Sachverhalt liegen die elektronisch vorgelegten Verwaltungsakten (Bescheide, Eingaben  des Bf., und die Übersicht zu den Eingaben und Erledigungen betreffend die  Arbeitnehmerveranlagung 2018 aus dem Abgabeninformationssystem des Bundesministeriums  für Finanzen) zu Grunde.

| Predicted | Gold |
|---|---|
| `Bundesministeriums  für Finanzen` | `Bundesministeriums  für Finanzen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/148574.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148574.1_76`)


Dafür ist nach Ansicht des Bundesministeriums für Finanzen (BMF, SWI 1998, 553) bereits der  beim österreichischem Arbeitgeber eintretende Leistungserfolg ausreichend, was, wenn der  Beschwerdeführer für seinen österreichischen Arbeitgeber Transportaufträge im Ausland  ausführt, außer Zweifel steht.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `BMF` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/148574.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148574.1_88`)


Dies ändert jedoch nichts an der Tatsache, dass der Beschwerdeführer in Österreich, wie oben  gezeigt, beschränkt steuerpflichtig und daher berechtigt ist, eine Antragsveranlagung nach § 41  Abs. 2 Z 1 EStG 1988 durchzuführen (vergleiche die gleichlautende Ansicht des  Bundesministeriums für Finanzen SWI 2008, 149, EAS 2953 vom 26.3.2008).

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

</details>

---

## `Bundesamt_fuer_Soziales_entities` 🏆

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `1ebf2304`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen'.

**Content:**
```
(?:Bundesamt\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.016 | 51 | 51 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 51 | 0 | 6283 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_126`)


Hier ist das das Bundesamt für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_11`)


fünf Jahre ab der  Antragstellung möglich bzw. ab dem Monat, ab dem das Bundesamt für Soziales und  Behindertenwesen den Grad der Behinderung festgestellt hat (§ 10  Familienlastenausgleichsgesetz 1967 in der geltenden Fassung).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_170`)


Mit Beschluss vom 24. Februar 2020 erteilte das Bundesfinanzgericht dem Finanzamt einen  Ermittlungsauftrag, sonach ein neuerliches Sachverständigengutachten beim Bundesamt für  Soziales und Behindertenwesen (SMS) einzuholen sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_385`)


• Bindung an die Gutachten des Sozialministeriumservice  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die  Gutachten des Sozialministeriumservice (früher: Bundesamt für Soziales und  Behindertenwesen) gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch Lenneis/Wanke (Hrsg.), FLAG, 2. Aufl.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_26`)


Am 02.11.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor, beantragte die Abweisung und nahm wie folgt Stellung:  „Das Finanzamt ist bei der Beurteilung des Sachverhalts gemäß § 8 Abs. 6 FLAG 1967 an die  vom Bundesamt für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens ausgestellten Bescheinigungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_41`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_16`)


Zur Begründung der Abweisung wurde ausgeführt, dass das Finanzamt für die Anerkennung  der beantragten Freibeträge auf die Mitteilungen des Sozialministeriumservice (ehemaliges  Bundesamt für Soziales und Behindertenwesen) angewiesen sei, aktuell für die Bf. jedoch keine  derartigen Mitteilungen vorlägen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_28`)


Die Tatsache der Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit sind durch  eine amtliche Bescheinigung durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_44`)


Im Dezember 2020 und im März 2021 wurden vom Bundesamt für Soziales und  Behindertenwesen Sozialministeriumservice Sachverständigengutachten erstellt.  3 von 11 Seite 4 von 11

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/135301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135301.1_115`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_30`)


In der Folge erstellte das Bundesamt für Soziales und Behindertenwesen, BASB Landesstelle  NÖ das Sachverständigengutachten auf Grund der Aktenlage vom 4. Mai 2021 nach der  Einschätzungsverordnung (BGBl. II Nr. 261/2010) betreffend Z., den Sohn des Bf.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_61`)


Vom Bundesamt für Soziales und Behindertenwesen wurden im Laufe des  Verwaltungsverfahrens folgende Bescheinigungen erstellt:   BSB-Bescheinigung vom 29. Oktober 2020: Stellungnahme: Keine Unterlagen eingelangt;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_25`)


fünf Jahre ab der  Antragstellung möglich bzw. ab dem Monat, ab dem das Bundesamt für Soziales und  Behindertenwesen den Grad der Behinderung festgestellt hat (§ 10  Familienlastenausgleichsgesetz 1967 in der geltenden Fassung).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_57`)


Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Aktengutachten erstellt am 12. April 2021:   Fachgebiet der Sachverständigen: Kinder- und Jugendheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   2021-03-12 Amanda Guichard  Kinder-und Jugendpsychiatrie, Hinterbrühl, Kurzarztbrief nach Aufenthalt  in der kooperativen Tagesklinik vom 20.10.20 bis 29.01.2021, Diagnosen:   einfache Aktivitäts- und Aufmerksamkeitsstörung mit Förderbedürfnissen in der sozialen  Interaktion, Förderbedarf in Bezug auf sensorische Interaktion und die Motorikentwicklung  /fein und grob), logopädisch: phonetische Aussprachestörung in Form eines interdentalen  Sigmatismus sowie ein ad-/bzw. interdentales Schluckmuster, durchschnittliche Intelligenz,  keine chronischen oder akuten körperlichen Erkrankungen bekannt, mäßige soziale  Beeinträchtigung (Aufbau und Erhalt von Freundschaften, wiederholte Konflikte mit  Erwachsenen und Kindern, auch Konflikte mit Erwachsenen außerhalb der Familie, gehemmte  soziale Aktivität, wenig effektive Copingmechanismen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Amanda Guichard` (person)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_60`)


Nachuntersuchung:   NU in 3 Jahren zur Überprüfung der Beeinträchtigung   Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Sachverständigengutachten (mit Untersuchung am 23. August 2021),   vidiert am 27. August 2021:   Fachgebiet des Sachverständigen: Kinder- und Jugendheilkunde   Anamnese:   Die Eltern haben gegen den Bescheid schriftlich Einspruch erhoben, da die rückwirkende  Geltendmachung des GdB mit 10/2020 festgelegt wurde, die Eltern jedoch den Beginn der  Symptomatik dtl.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/137083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137083.1_33`)


– In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_69`)


§ 29b Abs. 1 StVO 1960 normiert:  "Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung ‚Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung‘  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/137507.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137507.1_43`)


vom Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_13`)


3. Auf Anforderung durch das Finanzamt wurde vom Sozialministeriumservice (kurz: SMS;  vormals Bundesamt für Soziales und Behindertenwesen) am 30.8.2018 ein Sachver- ständigengutachten (aufgrund der Aktenlage) von Adam Safak  Facharzt für  Psychiatrie/Allgemeinmediziner, vidiert von Dr. D am 4.9.2018, auszugsweise folgenden  Inhaltes erstellt:  "Zusammenfassung relevanter Befunde …:  14.9.2015: Reha-Befund Ort1: chronischer Kopfschmerz nach komplexer Gesichtsverletzung im  siebten Lebensjahr (vom Ausmaß her wohl auch SHT 1989)  7.3.2018: Entlassungsbericht aus der psychiatrischen Rehabilitation im Klinik1: Diagnose F07.9  organische Persönlichkeits- und Verhaltensstörung nach Schädelhirntrauma, bei Aufnahme  leicht depressiv, bei Entlassung noch Einschränkung der psychosozialen Belastbarkeit  Behandlung/en/Medikamente …:  Lyrica 50 mg … Mirtabene 30 mg … Seroquel 25 mg … bei Bedarf eine ärztliche  Weiterbetreuung bei … sowie eine Einzel-Psychotherapie wurden empfohlen  Ergebnis der durchgeführten Begutachtung:   1 Persönlichkeits- und Verhaltensstörungen … mit maßgeblichen sozialen     Beeinträchtigungen, organische Persönlichkeitsveränderung nach komplexem     Schädel-Hirntrauma vor vielen Jahren;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Adam Safak` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_10`)


Das Finanzamt ersuchte das Bundesamt für Soziales und Behindertenwesen die Erstellung  eines ärztlichen Sachverständigengutachtens zu veranlassen und eine darauf basierende  Bescheinigung zu ers tellen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_11`)


Das Bundesamt für Soziales und Behindertenwesen b eauftragte  den gleichen Sachverständig en, der bereits im Jänner 2019 seine Expertise abge geben hat.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_34`)


Auf Grund der Beschwerdeerhebung wurde vom Finanzamt neuerlich das Bundesamt für  Soziales und Behindertenwesen kontaktiert und diesem die Beschwerde samt Beilagen  übermittelt. Der leitende Arzt des Bundesamtes für Soziales und Behindertenwesen teilte  dem Finanzamt daraufhin mit, dass das im April 2019 erstellte Gutachten schlüssig und  nachvollziehbar sei und keine neuerliche Begutachtung erforderlich wäre.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesamtes für Soziales und Behindertenwesen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_18`)


Im Abweisungsbescheid wird auf die im Zuge dieser Erledigung vom Bundesamt für Soziales  und Behindertenwesen im Auftrag des Finanzamtes erstellte Bescheinigung über das Ausmaß  der Behinderung der Bf. vom 3. Februar 2022 hingewiesen, die durch das Bundesamt für  Soziales und Behindertenwesen zugesendet wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_224`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt - eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/142675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142675.1_72`)


Zuständige Stelle ist (…) in allen übrigen Fällen sowie bei Zusammentreffen von  Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_52`)


"Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung "Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung"  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_117`)


verschiedener Art das Bundesamt für Soziales und Behindertenwesen (nunmehr  Sozialministeriumservice);

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_105`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/146077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146077.1_117`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/146077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146077.1_143`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  als Amtssachverständige bedient, die in die bei dieser Behörde gem. § 90 KOVG 1957 zu  führende Sachverständigenliste, eingetragen sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_14`)


Im Zuge des Verfahrens sei das Bundesamt für  Soziales und Behindertenwesen, Landesstelle Wien, beauftragt worden, ein Sachverständigen- gutachten zu erstellen.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_145`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_147`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_148`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der  anspruchsrelevanten Daten durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes  (BBG), BGBl. Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_154`)


Bescheinigung des Sozialministeriumservice:  Nach den Bestimmungen des § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die  voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine  Bescheinigung des Sozialministeriumservice (früher: Bundesamt für Soziales und  Behindertenwesen) auf Grund eines ärztlichen Sachverständigengutachtens) nachzuweisen (vgl  z.B. VfGH 10.12.2007, B 700/07;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_44`)


Gemäß § 8 Abs. 6 FLAG 1967 in der ab 01.03.2023 geltenden Fassung ist der Grad der  Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, vom Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice)  dem Finanzamt Österreich durch eine Bescheinigung auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_46`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_47`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der  anspruchsrelevanten Daten durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes  (BBG), BGBl. Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_180`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt - eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/146363.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146363.1_63`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/146520.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146520.1_24`)


Die belangte Behörde hat mit dem Heranziehen des  Wiederaufnahmetatbestandes gemäß § 303 Abs 1 lit b BAO eine unpassende Norm gewählt,  weil diese gar nicht einschlägig ist, sondern § 303 Abs 1 lit c BAO: Über das Vorliegen einer  Behinderung, die zur Anwendbarkeit des Freibetrages nach § 35 Abs 1 EStG führt, hat gemäß  § 35 Abs 2 TS 3 EStG das Bundesamt für Soziales und Behindertenwesen zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/147633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147633.1_77`)


- In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art  das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/148452.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148452.1_41`)


Gemäß § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_78`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) dem Finanzamt Judenburg Liezen  durch eine Bescheinigung auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Judenburg Liezen` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_80`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das FA Judenburg Liezen  hat nicht  zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `FA Judenburg Liezen` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_81`)


Der Nachweis des Grades der Behinderung in Form der Bescheinigung entfällt,  sofern der Grad der Behinderung durch Übermittlung der anspruchsrelevanten Daten durch  das Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) aufgrund des  Verfahrens nach § 40 des Bundesbehindertengesetzes (BBG), BGBl. Nr. 283/1990, zur  Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_90`)


Vom Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) wurde durch  eine Bescheinigung vom 17.08.2018 auf Grund eines ärztlichen Sachverständigengutachtens  ausdrücklich festgestellt, dass keine dauernde Erwerbsunfähigkeit der Bf. vorliegt.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_294`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/149663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149663.1_55`)


Insoweit konnte eine Minderung  der Erwerbsfähigkeit ab 2013 nicht festgestellt werden, weil diese nicht durch eine amtliche  Bescheinigung einer hierfür zuständigen Stelle (Bundesamt für Soziales und  Behindertenwesen) nachgewiesen wurde (§ 35 Abs. 2 EStG 1988).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/149663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149663.1_79`)


Freibetrag nach § 35 EStG 1988   Nach § 35 Abs. 1 EStG 1988 steht einem Steuerpflichtigen, der außergewöhnliche Belastungen  durch eine eigene körperliche Behinderung hat und keine pflegebedingten Geldleistungen  erhält, ein Freibetrag zu. Die Tatsache der Behinderung sowie das Ausmaß der Minderung der  Erwerbsfähigkeit (Grad der Behinderung) ist durch eine amtliche Bescheinigung der für diese  Feststellung zuständigen Stelle - im vorliegenden Fall das Bundesamt für Soziales und  Behindertenwesen - festzustellen (§ 35 Abs. 2 letzter Satz EStG 1988).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

</details>

---

## `Bundesfinanzgericht_entities` 🏆

**F1:** 0.272 | **Precision:** 0.990 | **Recall:** 0.158  

**Format:** `regex`  
**Rule ID:** `4ed3bf3e`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive) with strict context anchors to prevent missing this frequent entity.

**Content:**
```
(?:des|vom|von|bei|an|f\u00fcr|\s)(Bundesfinanzgerichtes)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.990 | 0.158 | 0.272 | 1023 | 1013 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1013 | 10 | 5398 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_70`)


Hinsichtlich der Verfassungskonformität dieser Regelung bestehen seitens des Bundesfinanzgerichtes keinerlei Bedenken.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_50`)


Dem Einwand der Beschwerdeführerin, dass bloß ein nicht der Bestandvertragsgebühr unterliegender Vorvertrag vorliege, kann von Seiten des Bundesfinanzgerichtes nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_56`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision) Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_181`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_13`)


Bedauerlicher Weise wurde weder innerhalb des Bundesfinanzgerichtes eine Information über  die bereits erfolgte Entscheidung im zugrundeliegenden Abgabenverfahren noch von der  belangten Behörde eine Information über die Erlassung eines Gutschriftszinsenbescheides für  dieses Beschwerdeverfahren weitergeleitet, sodass es zu dieser weiteren – wenn auch  kurzfristigen – Verzögerung bei der Entscheidung gekommen ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_16`)


Mit der Einführung des Bundesfinanzgerichtes haben sich auch diverse Bezeichnungen  geändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_53`)


Zulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_66`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_69`)


Seitens des Bundesfinanzgerichtes wird nicht in Abrede gestellt, dass die besuchten Seminare  einen positiven Effekt auf die berufliche Tätigkeit der Beschwerdeführerin hatten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_77`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_247`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_145`)


Auch im Hinblick der Ausführungen im Erkenntnis des  Bundesfinanzgerichtes (BFG 30.6.2020, RV 1100515/2013), wonach der Bf. in den Jahren 2011  und 2012 neben seinen Pensionsbezügen in den Sommermonaten beträchtliche Einkünfte aus  „Schwarzlohnzahlungen“ als Aushilfskoch erzielte, erscheint eine Schätzung im Ausmaß einer  Halbtagsanstellung in Höhe von CHF 2.000,00 durchwegs plausibel.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_261`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_69`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_142`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_184`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  14 von 15 Seite 15 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_75`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_97`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_64`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_201`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_119`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_123`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_240`)


(siehe auch Vorlageantrag RZ 10)   V. Unzulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_69`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_51`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  4 von 5 Seite 5 von 5

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_29`)


Zur Revision (Art. 133 Abs. 4 iVm Abs. 9 B-VG):  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_700`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  33 von 34 Seite 34 von 34

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `E.` (person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_265`)


Der wesentlichste Zurechnungsposten mit 51.423,00 € konnte dabei nach Ansicht des  Bundesfinanzgerichtes vom Verfasser der Steuererklärung nicht übersehen werden, da eine  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_271`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `E.` (person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_88`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_238`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_22`)


II. Das Bundesfinanzgericht hat erwogen:  Der Verwaltungsgerichtshof hat die Entscheidung des Bundesfinanzgerichtes mit Erkenntnis  vom 20.5.2020, Ra 2017/13/0072, mit folgender Begründung aufgehoben:  „Mit Erkenntnis vom 4. Dezember 2019, G 159/2019-13, G 226/2019-11, G 248/2019-8, sprach  der Verfassungsgerichtshof u.a. aufgrund eines aus Anlass des vorliegenden Falls gestellten  Antrags des Verwaltungsgerichtshofes (protokolliert zu G 226/2019) aus, dass der Satz  „Der Antrag ist vor Ablauf der für Wiederaufnahmsanträge nach § 304 BAO maßgeblichen Frist  zu stellen.“ in § 295 Abs. 4 BAO des Bundesgesetzes über allgemeine Bestimmungen und das  Verfahren für die von den Abgabenbehörden des Bundes, der Länder und Gemeinden  verwalteten Abgaben (Bundesabgabenordnung - BAO), BGBI. Nr. 194/1961 idF BGBI. I  Nr. 76/2011, verfassungswidrig war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_32`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  3 von 4 Seite 4 von 4

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_74`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_236`)


Im Ergänzungsvorhalt des Bundesfinanzgerichtes vom 15.10.2019 wurde der  Beschwerdeführer explizit dazu aufgefordert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_270`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_30`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_71`)


Unzulässigkeit einer ordentlichen Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_99`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_149`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts­hofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_67`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision gemäß Art. 133 Abs. 4 iVm  Abs. 9 B-VG zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche  Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_170`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  11 von 12 Seite 12 von 12

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `E.` (person)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_207`)


4. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_17`)


Vergleiche auch die Ausführungen des Bundesfinanzgerichtes zu einem ähnlich  gelagerten Sachverhalt im Erkenntnis vom 21.10.2015, RV/6100700/2014.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_108`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_42`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_114`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_70`)


2.2. Zu Spruchpunkt III. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_369`)


1.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_377`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision gem. Art 133 Abs 4 B-VG iVm §  25a Abs 1 VwGG zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_49`)


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  3 von 4 Seite 4 von 4

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Valentin Heinicke, Hofstätt 196, 3970 Sulz, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Mag. Renate Schohaj` (person)
- `Valentin Heinicke` (person)
- `Hofstätt 196, 3970 Sulz, Österreich` (address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_3`)


Begründung  Sachverhalt:  Die Revisionswerberin (Rw.) hat gegen das Erkenntnis des Bundesfinanzgerichtes vom  1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer 2014, mit Eingabe vom  24. Juni 2020 eine ordentliche Revision eingebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_8`)


Gegen diesen Bescheid wurde mit Eingabe der steuerlichen Vertretung vom 16. Dezember  2016 Beschwerde erhoben, mit der Begründung, dass nach dem Erkenntnis des  Bundesfinanzgerichtes vom 23. Juni 2015, RV/2100388/2013, die Neuregelung der  Bilanzberichtigung gemäß § 4 Abs. 2 Z 2 EStG 1988 erst mit 1.1.2013 in Kraft gesetzt worden sei  und die Anwendung dieser Regelung für Sachverhalte vor dem Jahr 2013 zu einem  unzulässigen Eingriff in die materielle Einkommensbesteuerung der Vorjahre führen würde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_17`)


Nach dem Erkenntnis des  Bundesfinanzgerichtes vom 23.6.2015, RV/2100388/2013, könne eine Wurzelberichtigung  erstmals ab dem Veranlagungszeitraum 2013 vorgenommen werden, da die diesbezügliche  Rechtsvorschrift erst mit 1.1.2013 in Kraft getreten sei, weshalb die Vornahme einer  2 von 4 Seite 3 von 4

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_31`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_117`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_118`)


Die de facto Bindung des Bundesfinanzgerichtes an ärztliche Sachverständigengutachten des  Sozialministeriumservice ist in § 8 Abs. 6 FLAG ausdrücklich gesetzlich geregelt.      Wien, am 1. Oktober 2020

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_126`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_73`)


Hinsichtlich der rechtlichen Beurteilung wird auf folgende drei übereinstimmende Erkenntnisse  des Bundesfinanzgerichtes verwiesen:   Erkenntnis vom 16.06.2014, RV/3100671/2012:   1.)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_108`)


Nach Ansicht des Bundesfinanzgerichtes lässt sich aus den Gesetzesmaterialien nur ableiten,  dass die bis zum 31.12.2013 bei der Wiederaufnahme auf Antrag und von Amts wegen  bestehenden, gesetzlich normierten, unterschiedlichen Anwendungsvoraussetzungen beseitigt  werden sollten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_129`)


Nach Meinung des  Bundesfinanzgerichtes muss ein derartiger Normzweck aber auch dem § 303 Abs. 1 BAO neue  Fassung zukommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_139`)


Auf Basis der vorliegend zu beurteilenden Vorgänge wird im vorliegenden Fall keine  Veranlassung gesehen, von dieser Judikatur des Bundesfinanzgerichtes abzugehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/129969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129969.1_17`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_35`)


Res judicata (entschiedene Sache) steht einem solchen Antrag  nicht entgegen, da mit dem gegenständlichen Erkenntnis des Bundesfinanzgerichtes keine  inhaltliche Entscheidung hinsichtlich dieser Monate getroffen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_10`)


Der Verwaltungsgerichtshof gab der Bf. im Erkenntnis vom 29.6.2020, Ra 2020/16/0001 recht  und hob das Erkenntnis des Bundesfinanzgerichtes wegen Rechtswidrigkeit des Inhaltes auf.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt  Um Wiedeholungen zu vermeiden wird auf das Erkenntnis des Bundesfinanzgerichtes vom  22.10.2019, RV/7101585/2019 und auf das Erkenntnis des Verwaltungsgserichtshofes vom  29.6.2020, Ra 2020/16/0001 verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_158`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_85`)


Zulässigkeit einer Revision   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_91`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_352`)


Begründung nach § 25a Abs. 1 VwGG   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_320`)


Schließlich kann nach Ansicht des Bundesfinanzgerichtes auch durch die Einvernahme der  Fachärztin Dr.in X, die das letzte Gutachten für das SMS am 9.7.2020 erstellt hat, nichts für die  Feststellung gewonnen werden, ob beim Bf. die Erwerbsunfähigkeit bereits vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_402`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_90`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_101`)


Das Erkenntnis des Bundesfinanzgerichtes vom 23.03.2017, RV/5101633/2016, entschied  hinsichtlich der Rechtsansicht des Finanzamtes, wonach für die Begründung der  Unzumutbarkeit der Verlegung des Familienwohnsitzes von Serbien nach Österreich aus  wirtschaftlichen Gründen wegen des Betreibens einer kleinen, der Eigenversorgung dienenden  Landwirtschaft am Familienwohnsitz zusätzlich auch das Vorhandensein von  unterhaltsberechtigten und betreuungsbedürftigen (= minderjährigen) Kindern am  Familienwohnsitz Voraussetzung sei, wie folgt:  Dem Erkenntnis zugrunde gelegter Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_151`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_17`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_27`)


Im vorliegenden Fall geht es bei der Entscheidung, ob Verfahrenshilfe zu gewähren ist, vor  allem darum, ob im Beschwerdeverfahren der Antragstellerin betreffend Rückzahlung eines  Betrages, den sie als nicht rechtmäßig ansieht, der aber auf Grund des Erkenntnisses des  Bundesfinanzgerichtes vom 5.5.2020 RV/7100080/2020 rechtmäßig festgesetzt wurde – da das  Bundesfinanzgericht sogar ausdrücklich in seinem zurückweisenden Erkenntnis ausgesprochen  hat, dass auch bei Rechtzeitigkeit der Beschwerde diese abzuweisen gewesen wäre – und  mittlerweile auch rechtskräftig ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_30`)


Da kein Guthaben seitens der Antragstellerin bestand und auf Grund der genannten  Entscheidung des Bundesfinanzgerichtes durch eine unrechtmäßig festgesetzte Gebühr der  gegenständliche Betrag auch nicht gutgeschrieben werden kann, ist es de facto unmöglich ein  Guthaben, das nicht vorhanden ist, auszuzahlen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_34`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_67`)


Nach der der Judikatur des Bundesfinanzgerichtes muss es sich um einen konkreten Fall einer  ambulanten Hauskrankenpflege handeln und muss die Person, die das Schild „Mobile  Hauskrankenpflege im Dienst” verwendet, in der Lage sein, der Behörde im Fall des  Nachfragens nachzuweisen, dass die Fahrzeugabstellung auf Grund einer konkreten  ambulanten Hauskrankenpflege erfolgt ist (vgl. BFG 12.12.2014, RV/7501868/2014, BFG  04.02.2019, RV/7500092/2019.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_145`)


Da die Bf somit nach Ansicht des Bundesfinanzgerichtes den Nachweis der  Gläubigergleichbehandlung nicht erbracht hat, hat die belangte Behörde zu Recht den  gesamten aushaftenden Betrag (abzüglich der Konkursquote) in die Haftung einbezogen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_179`)


Unzulässigkeit einer ordentlichen Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_38`)


Nach der Rechtsprechung des Bundesfinanzgerichtes würden elektronische Aktivierungen von  15-Minuten-Parkscheinen mit nachfolgenden 15-Minuten-Parkscheinen oder kostenpflichtigen  Parkscheinen bei wenigen Minuten Zwischenraum als unmittelbar aufeinanderfolgend  betrachtet (Verweis auf BFG vom 24.02.2016, RV/7501346/2014, BFG vom 13.01.2016,  RV/7500002/2015, BFG vom 11.02.2016, RV/7501271/2015).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_73`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_75`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art 133 Abs 4 B-VG).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_15`)


Quartal 2012 sowie das 3. Quartal 2012, wurden am 7.  Oktober 2020 zurückgenommen und in der Folge mit Beschluss des Bundesfinanzgerichtes vom  21. Oktober 2020 als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_18`)


Mit Beschluss des Bundesfinanzgerichtes vom 21. Oktober 2020, GZ. RV/4200046/2018,  wurden die in den Hauptsachen eingebrachten Beschwerden gemäß § 256 Abs. 3 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_20`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_232`)


V. Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision gemäß Art. 133 Abs. 4 iVm  Abs. 9 B-VG zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche  Bedeutung zukommt, insbesondere, weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_22`)


Zur Unzulässigkeit einer Revision   Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_26`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/130768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130768.1_22`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen eine Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_7`)


Das zu dieser Zahl ergangene Erkenntnis des  Bundesfinanzgerichtes vom 28.2.2018 wurde mit Erkenntnis des Verwaltungsgerichtshofes  vom 17.7.2019, Ra 2018/13/0058 vom 17.7.2019 wegen Verletzung von  Verfahrensvorschriften aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_9`)


Der Verfahrensgang und der Sachverhalt, der auch dem am 24.3.2016 ergangenen mit  Beschwerde vom 25.4.2016 angefochtenen Körperschaftsteuerbescheid für das Jahr 2010 zu  Grunde liegt, werden daher in verkürzter Form dargestellt und im Übrigen auf das Erkenntnis  des Bundesfinanzgerichtes vom 28.2.2018, RV/7101323/2013, und das Erkenntnis des  Verwaltungsgerichtshofes vom 17.7.2019, Ra 2018/13/0058, verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_113`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_81`)


4 Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_43`)


Über die Beschwerde wurde erwogen:  1. Zuständigkeit des Bundesfinanzgerichtes (BFG)

**False Positives:**

- `Bundesfinanzgerichtes` — partial — pred is substring of gold: `Bundesfinanzgerichtes (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)

</details>

---

## `Landespolizeidirektion_entities` 🏆

**F1:** 0.022 | **Precision:** 0.973 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `1ed9dbeb`  
**Description:**
Matches Landespolizeidirektion Wien and similar police authority names.

**Content:**
```
Landespolizeidirektion(?:\s+Wien)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.973 | 0.011 | 0.022 | 75 | 73 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 73 | 2 | 5989 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde als Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen W-xyz (A) unter Zugrundelegung der  Anzeigedaten des Kontrollorgans zu oa a) A 1119 und zu oa b) A 232 der  Parkraumüberwachung der Landespolizeidirektion Wien mit Strafverfügungen zu oa a) vom  21.01.2020 und zu oa b) vom 23.01.2020 angelastet, sie habe das Fahrzeug zu oa a) am  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete der Beschwerdefüherin (Bf.) unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31.10.2019 an, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 02.09.2019 um 14:43 Uhr in der  gebührenpflichtigen Kurzparkzone in 1140 Wien, Penzinger Straße 157, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt.  Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1  Wiener Parkometergesetz 2006 wurde über die Bf. eine Geldstrafe iHv € 60,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_13`)


Das Fahrzeug wurde am 5. Juni 2020 um 14:14 Uhr vom Kontrollorgan KO der  Parkraumüberwachung der Landespolizeidirektion Wien beanstandet, da es zur  Beanstandungszeit ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_9`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am  12. Dezember 2019 um 14:52 Uhr in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Simmeringer Hauptstraße 59 - 61, beanstandet, da nach dessen Wahrnehmungen  elektronische Parkscheine mit einer fünfzehn Minuten nicht übersteigenden Abstellzeit  unmittelbar aufeinander folgend ohne Vornahme eines Ortswechsels aktiviert wurden.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_49`)


Bezüglich des Aufnahmezeitpunktes sei darauf hinzuweisen, dass sich die Organe der  Landespolizeidirektion Wien bei ihrer Tätigkeit eines PDA (personal digital assistant) bedienen,  der im Zuge einer Beanstandung die zu dem Zeitpunkt aktuelle Uhrzeit über einen Server  beziehe und vorgebe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_74`)


In der Verhandlung vor dem BFG wurde nach dem überwiegend wiederholenden Vorbringen  des Bf., Herr Z, Kontrollorgan der MA 67 der Landespolizeidirektion Wien, als Zeuge und zwar  zu folgendem Beweisthema vernommen:   Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna am 12.  Dezember 2019 um 14:52 Uhr in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Simmeringer Hauptstraße 59 - 61.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 13. August 2020,  MA67/206700430919/2020, angelastet, sie habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 20. Mai 2020 in der gebührenpflichtigen Kurzparkzone in  1110 Wien, Simmeringer Hauptstraße 152, ohne einem für den Beanstandungszeitpunkt 15:11  Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_18`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung samt Fotos, welche  von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt wurde.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_14`)


Die Mahnung wurde ohne Zustellnachweis zugestellt und der geforderte Betrag wurde nicht  einbezahlt.  Mit Aufforderung zum Antritt der Ersatzfreiheitsstrafe vom 19. Jänner 2021 zu obiger  rechtskräftiger Strafverfügung vom 7. Dezember 2018, MA67/Zahl1/2018, wurde der Bf.  aufgefordert binnen zwei Wochen nach Erhalt dieses Schreibens bei der Landespolizeidirektion  im dortigen Polizeianhaltezentrum anzutreten.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_9`)


Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) lastete dem Beschwerdeführer  (Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüber- wachung der Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit  Strafverfügung vom 17. August 2020, Zahl, an, er habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 28. April 2020 in der gebührenpflichtigen Kurzparkzone  in 1030 Wien, Landstraßer Hauptstraße 136, ohne einem für den Beanstandungszeitpunkt  19:40 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig  verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_14`)


Mit Schreiben vom 2. September 2020 („Verständigung vom Ergebnis der Beweisaufnahme“)  wurde der Bf. von der MA 67 in Kenntnis gesetzt, dass sich aus der Organstrafverfügung sowie  zwei Fotos, welche von einem Organ der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung ausgestellt worden sei, ergebe, dass das näher bezeichnete Fahr- zeug am 28. April 2020 um 19:40 Uhr in Wien 3, Landstraßer Hauptstraße 136, in einer ge- bührenpflichtigen Kurzparkzone ohne einem für den Beanstandungszeitpunkt gültigen Park- schein abgestellt gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_148`)


Die Verordnungen ergingen ua. an die MA 53 (Presse- und Informationsdienst, Stadtservice  Wien, MA 67 – Parkraumüberwachung, Austria Presse Agentur, Rundfunk- und Fernsehan- stalten, Landespolizeidirektion, Verkehrsleitzentrale, ARBÖ, ÖAMTC, VCÖ)(S. 15, 16 Ver- waltungsakt).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_73`)


Der Beschwerdeführer erzielte im Zeitraum 09/2019 bis 12/2019 steuerpflichtige Einkünfte  (von der Landespolizeidirektion Steiermark) in Höhe von 5.075,80 € und im Zeitraum von  01/2020 bis 03/2020 4251,98 € (17.007,92 € : 4).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten eines Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 8. März 2021 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 8. Jänner 2021 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Rustenschacherallee 44-56, ohne einen für  den Beanstandungszeitpunkt 10:18 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_8`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Dem Ansuchen des Sohnes der Bf. um Aufnahme als Vertragsbediensteter bei der  Landespolizeidirektion Wien wurde stattgegeben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_9`)


Ab 1. September 2019 stand er in einem Dienstverhältnis zur polizeilichen Grundausbildung  mit der Landespolizeidirektion Wien und versah gemäß Bestätigung vom 12. September 2019  die polizeiliche Grundausbildung im Bildungszentrum der Sicherheitsakademie Wien, 1030  Wien (vorgelegte Ausbildungsbestätigung vom 12.09.2019).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_10`)


Der Sondervertrag gemäß § 36 VBG 1948 für die exekutivdienstliche Ausbildung vom  01. September 2019 beinhaltet, auszugsweise wiedergegeben, Folgendes:  1. Organisationseinheit, die für den Bund abschließt: Landespolizeidirektion Wien  2. Vor- und Familiennamen: (Sohn der Bf.)  3. Geburtsdatum: (Sohn der Bf.)  4. Beginn des Vertrages: 01. September 2019  5. Befristung: Dieser Dienstvertrag ist auf 24 Monate befristet  7. Beschäftigungsart: VB des Bundes mit Sondervertrag für die exekutivdienstliche Ausbildung  8.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_25`)


Betreffend das Jahr 2019 meldete die Landespolizeidirektion Wien dem Finanzamt gemäß § 84  Abs. 1 EStG 1988 Bezüge für den Zeitraum 01.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_11`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) wurde am 15.  Oktober 2020 um 09:41 Uhr in der gebührenpflichtigen Kurzparkzone in 1040 Wien, Rechte  Wienzeile gegenüber 25-27, von einem Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien zur Anzeige gebracht, da zum Beanstandungszeitpunkt ein  gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach eingeholter Lenkerauskunft mit Strafverfügung vom 19.  März 2021 an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen  Vienna am 17. Dezember 2020 in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Brehmstraße 16, ohne einen für den Beanstandungszeitpunkt 11:23 Uhr gültigen Parkschein  abgestellt, da sich im Fahrzeug der Parkschein Nr. 123 (Fünfzehn-Minuten-Parkschein) mit den  Entwertungen 10:40 Uhr befand und die Parkzeitzeit somit überschritten worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_28`)


Die Organstrafverfügung des  Parkraumüberwachungsorganes der Landespolizeidirektion Wien, welche auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt worden sei, sei als taugliches Beweismittel  anzusehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_13`)


Mag. Dr. Wieland Reinecke (Beschwerdeführer, kurz: Bf.) wurde von Kontrollorganen der  Parkraumüberwachung der Landespolizeidirektion Wien in der gebührenpflichtigen  Kurzparkzone in 1030 Wien, Marokannergasse 18,   1. am 1. Dezember P20 um 15:45 Uhr (Z1 und  2. am 3. Dezember 2020 um 15:11 Uhr (Z2  3. am 7. Dezember 2020 um 12:32 Uhr (Z3),  4. am 9. Dezember 2020 um 20:04 Uhr (Z4)  beanstandet, da es ohne einen für den jeweiligen Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Wieland Reinecke` (person)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_9`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 1. Juli 2021  in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Windmühlgasse 7, beanstandet, da es  ohne einen für den Beanstandungszeitpunkt 20:02 Uhr gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_46`)


Beweiswürdigung:  Aus den eigenen Wahrnehmungen des Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien sowie durch die auf dem Überprüfungsgerät (Personal Digital  Assistant) erfassten Anzeigedaten und den zur Beanstandungszeit angefertigten Fotos sowie  der Überprüfung m-parking ergibt sich, dass zur Beanstandungszeit weder ein gültiger  Papierparkschein im Fahrzeug hinter der Windschutzscheibe hinterlegt noch ein gültiger  elektronischer Parkschein aktiviert war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_70`)


Aktenkundig - und in der vorgenannten Beweiswürdigung der belangten Behörde unbeachtet  gelassen - ist jedoch eine Korrespondenz der belangten Behörde mit der Landespolizeidirektion  Wien vom 7. August 2021, wonach der Bf. gegenständliches Fahrzeug ‚kurz‘ von der  Zulassungsbesitzerin geborgt gehabt habe, da sein eigenes Fahrzeug in der Werkstätte war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_73`)


Da die Korrespondenz mit 7. August 2021 datiert war, kann davon ausgegangen werden, dass  die Wahrnehmung von gegenständlichem Fahrzeug durch die Landespolizeidirektion Wien  allenfalls zwei bis drei Tage vor dem 7. August 2021 eingetreten ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_89`)


Da im vorliegenden Fall die strafbaren Handlungen im Zeitraum vom 16. Februar 2021 bis  21. Juli 2021 begangen wurden und gemäß vorgenannter Korrespondenz der belangten  Behörde mit der Landespolizeidirektion Wien vom 7. August 2021 der Bf. (nach seinen eigenen  Angaben) gegenständliches Fahrzeug vor dem 7. August 2021 nur ‚kurz‘ von der  Zulassungsbesitzerin geborgt gehabt hatte, kann in freier Beweiswürdigung nach § 45 Abs. 2  AVG nicht davon ausgegangen werden, dass die Lenkereigenschaft des Bf. in den  beschwerdegegenständlichen Fällen als erwiesen anzunehmen ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/136598.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136598.1_8`)


Parkraumüberwachung der Landespolizeidirektion Wien am 12. Oktober 2021 um 12:25 Uhr in  der gebührenpflichtigen Kurzparkzone in 1100 Wien, Columbusgasse ggü 101, beanstandet, da  zur Beanstandungszeit kein gültiger Parkschein vorlag.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_38`)


wurde von der Landespolizeidirektion OÖ. berichtigt: Der  Betrag für den FRONTEX - Einsatz (vom 16.7. bis 18.8.2019) in Höhe von 2.114,80 wird unter  "Nicht steuerbare Bezüge (§ 26 Z 4) und steuerfreie Bezüge (§ 3 Abs. 1 Z 16 b)" steuerfrei  belassen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Missed by this rule (FN):**

- `FRONTEX` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/136998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136998.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 24. Jänner 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. November 2021  in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Wollzeile 3 ggü, abgestellt, ohne für  seine Kennzeichnung mit einem für den Beanstandungszeitpunkt 19:15 Uhr gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_8`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde vom  Kontrollorgan Zahl2 der Parkraumüberwachung der Landespolizeidirektion Wien am  27. Oktober 2021 um 16:55 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Am  Hauptbahnhof ggü 2, beanstandet, da es sich nach dessen eigenen Wahrnehmungen bei dem  Parkausweis gemäß § 29b StVO 1960 mit der Nr. Zahl3 um eine Farbkopie handelte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_27`)


Begründend stellte die Behörde unter Anführung der erhobenen Beweise (Einsichtnahme in  die Anzeige des Parkraumüberwachungsorgans der Landespolizeidirektion Wien, zur  Beanstandungszeit angefertigte Fotos, eingeholte Lenkerauskunft, Zusatznotiz vom  Meldungsleger) fest, auf Grund der eingeholten Lenkerauskunft sei ihre Tätereigenschaft  festgestellt worden und sei davon auszugehen, dass sie die Verwaltungsübertretung begangen  habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_10`)


Begründend führte die belangte Behörde aus:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien erstattet wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug an der im Spruch bezeichneten  Örtlichkeit zur angeführten Zeit im Bereich einer gebührenpflichtigen Kurzparkzone abgestellt  war, ohne dass die Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/138030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138030.1_12`)


Beweis sei durch Einsichtnahme in die Organstrafverfügung erhoben worden, welche von  einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung gelegt worden sei, sowie in die (von diesem) angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/138705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138705.1_8`)


Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde mit Bericht  vom 26. September 2022 dem Bundesfinanzgericht als zuständiges Verwaltungsgericht  vorgelegten Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Dienstnummer X  stellte am (Montag) 20. Juni 2022 um 12:54 Uhr fest, dass das mehrspurige Kraftfahrzeug mit  dem behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1230  Wien, Haeckelstraße 4, abgestellt war und dass dieses Kraftfahrzeug nicht mit einem für diesen  Beanstandungszeitpunkt gültigen Parkschein gekennzeichnet war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/138859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138859.1_3`)


Begründung  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenkerauskunft mit  Strafverfügung vom 22. November 2021 an, er habe das Fahrzeug am 26. August 1959  in der  gebührenpflichtigen Kurzparkzone in 1160 Wien, Panikengasse 1, ohne einen für den Bean- standungszeitpunkt 10:00 Uhr gültigen Parkschein abgestellt und demnach die Parkometer- abgabe verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `26. August 1959` (date)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/138859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138859.1_7`)


„Aus der Anzeige des Organs der Landespolizeidirektion Wien ergibt sich, dass das gegenständ- liche Kraftfahrzeug am 26. August 1959  um 10:00 Uhr in 1160 Wien, Panikengasse 1 in der  gebührenpflichtigen Kurzparkzone gestanden ist, wobei kein gültiger Parkschein entwertet,  bzw. kein elektronischer gültiger Parkschein aktiviert war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `26. August 1959` (date)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien am 3. Jänner 2022 um 09:32  Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Am Platz, beanstandet, da zur  Beanstandungszeit ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/139274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139274.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 25. Juli 2022 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 15. Juli 2022 in der  gebührenpflichtigen Kurzparkzone in 1220 Wien, Polgarstraße 3 und 5 ggü, ohne einen für die  Beanstandungszeit 16:12 Uhr gültigen Parkschein abgestellt, da der Parkschein Nr. PS1 und PS2  Spuren von entfernten Entwertungen aufgewiesen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/139288.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139288.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin (A. GmbH)  eingeholten Lenkerauskunft mit Strafverfügung vom 15. September 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 1. Juli 2022 in der  gebührenpflichtigen Kurzparkzone in Am Metzgerfeld 43, 3972 Weikertschlag, Österreich, ohne einen für den  Beanstandungszeitpunkt 17:53 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Am Metzgerfeld 43, 3972 Weikertschlag, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/139689.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139689.1_9`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 24. August  2022 in der gebührenpflichtigen Kurzparkzone in 1030 Wien, Wassergasse 14, beanstandet, da  zur Beanstandungszeit 15:16 Uhr ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/139974.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139974.1_8`)


der Landespolizeidirektion Wien mit Strafverfügung vom 25. Mai 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 25. März 2022 um  18:05 Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Pacassistraße 1, ohne einen  für den Beanstandungszeitpunkt 18:05 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/140104.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140104.1_4`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna war zur  Beanstandungszeit durch das Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien (22. September 2021, 12:28 Uhr) auf die Fa. XY e.U., Inhaber  ZulBes, zugelassen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_10`)


Entscheidungsgründe  Das bisherige Verfahren stellt sich wie folgt dar:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 1. August 2022  um 18:57 Uhr zur Anzeige gebracht, weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/140597.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140597.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 15. Dezember 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 18. Oktober 2022 in  der gebührenpflichtigen Kurzparkzone in 1020 Wien, Hafenzufahrtsstraße nächst ONr. 60,  ohne einen für den Beanstandungszeitpunkt 12:06 Uhr gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/140707.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140707.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 24. Jänner 2023 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. November 2022  in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Römergasse 79, ohne einen für den  Beanstandungszeitpunkt 20:46 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/140707.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140707.1_24`)


Bezüglich der dem Bf. angelasteten Verwaltungsübertretung (Abstellen des näher  bezeichneten Fahrzeuges in einer gebührenpflichtigen Kurzparkzone ohne Parkschein) stellte  die Behörde fest, dass keine Veranlassung bestehe, die schlüssigen und widerspruchsfreien  Angaben des meldungslegenden Organs der Landespolizeidirektion in Zweifel zu ziehen, zumal  einem derartigen Organ die Wahrnehmung und richtige Wiedergabe maßgeblicher  Sachverhalte, insbesondere bezüglich eines im ruhenden Verkehr befindlichen Kraftfahrzeuges,  wohl zugemutet werden könne.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/140939.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140939.1_8`)


vom Kontrollorgan der Parkraumüberwachung Nr. A1294 der Landespolizeidirektion Wien zur  Anzeige gebracht, da der zum Beanstandungszeitpunkt hinterlegte 60-Minuten- Gebührenparkschein mit der Nummer PSNr unrichtig entwertet war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/141691.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141691.1_6`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 31. August  2022 um 16:15 Uhr in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Neuwaldegger  Straße 57A, zur Anzeige gebracht, da der im Fahrzeug hinter der Windschutzscheibe  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/141996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141996.1_8`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde am 27. April  2023 um 12:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Makartgasse 2,  vom Kontrollorgan der Parkraumüberwachung DNr der Landespolizeidirektion Wien zur  Anzeige gebracht, da zum Beanstandungszeitpunkt ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 19. Mai 2023 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 22. März 2023 in der  gebührenpflichtigen Kurzparkzone in 1010 Wien, Eßlinggasse 5 ggü, ohne einen für den  Beanstandungszeitpunkt 12:29 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_14`)


„Aus der Organstrafverfügung ergibt sich, dass das Fahrzeug mit dem behördlichen  Kennzeichen Vienna am 22.03.2023 um 12:29 Uhr von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien in einer gebührenpflichtigen Kurzparkzone in Wien 1., Eßlinggasse  gegenüber 5 ohne gültigen Parkschein abgestellt wahrgenommen wurde.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/142156.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142156.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 6. Juli 2023 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 9. Mai 2023 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Platz, ohne einen für den  Beanstandungszeitpunkt 19:41 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/143180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143180.1_10`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde am  7. September 2023 um 18:05 Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien,  Ebenfeldgasse, vom Kontrollorgan der Parkraumüberwachung ADNr der  Landespolizeidirektion Wien zur Anzeige gebracht, weil es sich nach dessen eigenen  Wahrnehmungen bei dem im Fahrzeug hinterlegten Parkausweis gemäß § 29b StVO 1960 mit  der Nr. Nr um einen seit tt.mm.2021 abgelaufenen und manipulierten Parknachweis handelte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Ebenfeldgasse` (address)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/143904.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143904.1_8`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 27. Dezember 2023 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 18. Dezember 2023  in der gebührenpflichtigen Kurzparkzone in 1220 Wien, Bernoullistraße nächst ONr. 6, ohne  einen für den Beanstandungszeitpunkt 14:45 Uhr gültigen Parkschein abgestellt, da der  Parkschein Nr. 123 Spuren von entfernten Entwertungen aufgewiesen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/144091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144091.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer beim Zulassungsbesitzer des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenkerauskunft mit  Strafverfügung vom 3. Jänner 2024 an, sie habe das Fahrzeug am 28. September 2023 in der  gebührenpflichtigen Kurzparkzone in 1230 Wien, Perfektastraße 49, ohne einen für den  Beanstandungszeitpunkt 11:22 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_7`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/144543.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144543.1_124`)


Bei dem im Fahrzeug hinterlegten Parkausweis gemäß § 29b StVO handelte es sich laut den  Feststellungen der Kontrollorgane der Landespolizeidirektion um eine Farbkopie des Ausweises  (siehe Vermerke der Kontrollorgane in den Anzeigen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_19`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung samt Fotos, welche  von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt wurde.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_27`)


Demnach ist es für die Behörde laut vorangegangener Erläuterung nicht relevant, ob das  zuständige Parkraumüberwachungsorgan der Landespolizeidirektion Wien eine handschriftliche  Signatur beifügt, da die automatische Anfügung der Dienstnummer des Organs als ausreichend  zu betrachten ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/145249.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145249.1_12`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung ausgestellt wurde, geht hervor, dass das gegenständliche  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit zur angeführten Zeit im  Bereich einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist, da sich im Fahrzeug lediglich die ungültigen  Parkscheine nach altem Tarif Nr. PS1 und PS2 befanden.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_12`)


Das Straferkenntnis wurde folgendermaßen begründet:  „Aus der dem Verfahren zugrundeliegende Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung erstattet wurde, geht hervor, dass das von Ihnen gelenkte  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit zur angeführten Zeit im  Bereich einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_70`)


Beweiswürdigung:  Die Abstellung des Fahrzeuges in der (jeweils) gebührenpflichtigen Kurzparkzone ohne (jeweils)  gültigen Parkschein lässt sich aus den drei Anzeigen der drei Kontrollorgane der  Parkraumüberwachung der Landespolizeidirektion Wien und den im Akt aufliegenden, zu den  Beanstandungszeitpunkten aufgenommenen Fotos ersehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_8`)


Entscheidungsgründe  Verfahrensgang:    Das Abstellen des auf den Beschwerdeführer zugelassenen mehrspurigen Kraftfahrzeuges mit  dem behördlichen Kennzeichen 123 (A) wurde von einem Kontrollorgan der  Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 01. August 2024 um 20:47  Uhr in 1140 Wien, Rettichgasse 4, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/148818.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/148971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148971.1_12`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, in die von diesem angefertigten Fotos, sowie in die  erteilte Lenker*innenauskunft.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_16`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener dienstlicher  Wahrnehmung gelegt wurde, in die von diesem angefertigten Fotos, sowie in die Bescheide des  Magistratischen Bezirksamtes für den 22.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/149088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149088.1_3`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 21.  August 2024 um 14:26 Uhr in 1010 Wien, Rathausstraße 6 beanstandet, da ein gültiger  Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/149316.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149316.1_23`)


Betreffend des in der Verständigung der Landespolizeidirektion genannten KFZ der Marke X Y  mit dem Kennzeichen (D) Z, gab die Beschwerdeführerin an, dass dieses KFZ über die Firma  geleast worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion` | `Landespolizeidirektion` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug, mit dem behördlichen Kennzeichen W-Kennz. (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 04. April  2025 um 09:42 Uhr in der gebührenpflichtigen Kurzparkzone in 1210 Wien, nächst  Zaunscherbgasse ONr. 4 beanstandet, weil es zur Beanstandungszeit ohne gültigen Parkschein  bzw. gültiger Tagespauschalkarte abgestellt war, da die im Fahrzeug hinterlegte  Tagespauschalkarte Nr. TPK-Nr. Spuren von entfernten Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_28`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien aufgrund eigener dienstlicher  Wahrnehmung gelegt wurde, in die von diesem im Rahmen der Amtshandlung angefertigten  Fotos, sowie in die eingeholte Lenkerauskunft.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_53`)


Grundlage für das gegenständliche Verfahren ist die eigene dienstliche Wahrnehmung des  Parkraumüberwachungsorgans der Landespolizeidirektion Wien und die auf der Anzeige  festgehaltenen Angaben (entfernten Entwertungen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/149732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149732.1_7`)


der Landespolizeidirektion Wien mit Strafverfügung vom 31. Juli 2025, GZ. MA67/GZ/2025, an,  sie habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 2. Juni  2025 um 16:49 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Friesenplatz 7,  abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Anlässlich der Überprüfung des Anspruches auf Familienbeihilfe betreffend ihre Tochter T gab  die Beschwerdeführerin (kurz: Bf) im Juli 2019 bekannt, dass ihre Tochter Aspirantin bei der  Landespolizeidirektion Salzburg sei und legte ua eine Bestätigung des Bildungszentrums der  Sicherheitsakademie in Linz sowie ein Zeugnis über die Ausbildung zur zahnärztlichen  Assistentin vor.

**False Positives:**

- `Landespolizeidirektion` — partial — pred is substring of gold: `Landespolizeidirektion Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Salzburg`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_54`)


Laut Bestätigung des Bildungszentrums der Sicherheitsakademie in Linz vom 05.06.2019 belegt  die Tochter der Bf seit 01.06.2019 für die Landespolizeidirektion Salzburg den Aspiranten- Polizeigrundausbildungslehrgang im Bildungszentrum der Sicherheitsakademie in Linz.

**False Positives:**

- `Landespolizeidirektion` — partial — pred is substring of gold: `Landespolizeidirektion Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Salzburg`(organisation)

</details>

---

## `BMF_entities` 🏆

**F1:** 0.009 | **Precision:** 0.966 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `9bfc2cfc`  
**Description:**
Matches the abbreviation BMF and BM für Finanzen in legal contexts.

**Content:**
```
(?:des|vom|bei|von)(?:\s+)(BM(?:\s+f\u00fcr\s+Finanzen|F))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.966 | 0.004 | 0.009 | 29 | 28 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 1 | 5805 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_39`)


In der Liste des BMF zu "Pritschenwagen"  gemäß VO aus 1996 und § 4 VO 2002, die als LKW gelten, seien "Nissan Navara" und "Nissan  Pickup" als Pritschenwagen aufgeführt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_75`)


Stellungnahme:   Vorweg ist an dieser Stelle festzuhalten, dass, auch wenn der § 26 (3) StuFöG 1992 mit  01.09.2017 (BGBl. I Nr. 54/2016) geändert worden ist, die bislang geltenden Kriterien für die  Beurteilung der Wegzeiten zur Erreichung des Studienortes weiterhin anzuwenden sind, weil  die VO des BMF zur Berufsausbildung des Kindes außerhalb des Wohnortes (BGBl. Nr.  624/1995 idgF) auf das Studienförderungsgesetz idF BGBl. I Nr. 50/2016 verweist.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_240`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. im Verfahren  betreffend Vorjahre vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_17`)


Für die fremdfinanzierte Rentenversicherung sei das  Anwaltshonorar sehr wohl anzuerkennen, als Beweis diene ein Schreiben der Abteilung IV/7  des BMF vom 12.1.2001, in dem ausgeführt wird, dass Zinsen für Fremdkapital, das für den  Erwerb eines Rentenstammrechtes aufgenommen wurde, gemäß § 16 Abs 1 Z 1 EStG  Werbungskosten darstelle (Verweis auf EStR 2000 Rz 7018) und hinsichtlich des  Verlustausgleiches EStR 2000 Rz 151 ff zu beachten seien.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_263`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. mit der  Beschwerde vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_24`)


Zur Begründung wurde ausgeführt, die Rechtsprechung (bzw die Einkommensteuerrichtlinien  des BMF) sehe den Übergang des wirtschaftlichen Eigentums als entscheidend für die  Beurteilung einer Anschaffung im Sinne des § 10 EStG 1988 an.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_90`)


Im Rundschreiben 293/2007 der österreichischen Ärztekammer vom 07.12.2007 wird zur Frage  der Besteuerung der Bestattungsbeihilfe und Hinterbliebenenunterstützung (§§ 98 Abs 1 und  104 ÄrzteG) auf eine Mitteilung des BMF vom 04.12.2007, BMF-010222/0174-VI//7/2007,  hingewiesen, mit der eine Anfrage der Österreichischen Ärztekammer vom 30.08.2007  beantwortet wurde und der ua Folgendes zu entnehmen ist:  „Die von der Ärztekammer ausbezahlte Hinterbliebenenunterstützung und Bestattungsbeihilfe  ist unabhängig von der Gestaltung des jeweiligen Sachverhalts immer nach § 22 Z 4 iVm § 32 Z  2 EStG beim Rechtsnachfolger zu versteuern.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_97`)


……“  Die österreichische Ärztekammer hat diese Rechtsmeinung des BMF im Rundschreiben  293/2007 vom 07.12.2007 zustimmend kommuniziert.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_53`)


Die Mindesthöhe des Verspätungszuschlages von 0,1% könne  auch als angemessen erscheinen (vgl. Erlass des BMF, GZ BMF-010103/0030-V1/2006 vom  10.042006).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/136045.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136045.1_37`)


Im  Rahmen der Entsendung wurden Taggelder ausbezahlt, welche vom Dienstgeber (der  damaligen Erlassmeinung des BMF folgend) zum Teil steuerfrei und zum Teil steuerpflichtig  behandelt wurden.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/140219.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140219.1_225`)


In Anwendung der angeführten Judikatur des Höchstgerichtes sowie der Rechtsmeinung des  BMF laut den Einkommensteuerrichtlinien, der sich das Bundesfinanzgericht im konkreten Fall  anschließt, sind die geltend gemachten Anschaffungsnebenkosten laut Punkt 8. bis 12.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_76`)


Nach dem klaren Wortlaut der Gebührenrichtlinien des BMF sowie der Rechtsprechung des  VwGH führe die Vereinbarung aller denkmöglichen Kündigungsgründe des § 30 Abs. 2 MRG zur  gebührenrechtlichen Qualifizierung des Mietvertrages als auf „unbestimmte“ Zeit  abgeschlossen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/141397.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141397.1_223`)


Die Ausführungen des BMF würden die  Weiterentwicklung des Rechts widerspiegeln wie zB Verbleiben eines Existenzminimums als  maximale Zumutbarkeit zur Zuordnung des Steuerpflichtigen und danach die Übernahme der  restlichen Kosten aus sittlichen Gründen durch andere Personen, Wegfall von  Regressansprüchen, insbesondere in der Sozialgesetzgebung und Pflege mit Krankheitskosten  etc.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_247`)


d) Laut Abfrage der aktuellen Grunddaten des BMF zum Bf (Stand 4.7.2023) scheint seit       9.8.2016 als Wohnsitz folgende Adresse auf: D-Ort8;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_286`)


Meldebehörde vom 24.6.2015) und ab 9.8.2016 in D-Ort8 (siehe aktuell abgefragte  Grunddaten des BMF).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/141878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141878.1_34`)


Die BP habe iS der Ansicht des BMF 50% der Kursverluste (65.767,21 €) dem Gewinn  (33.512,61 €) hinzugerechnet (vgl. 804 EStR).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/142618.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142618.1_6`)


In ihrer Begründung verwies die belangte Behörde  auf § 1 Abs. 1 der Verordnung des BMF, mit der ein eigenes Verfahren für die Erstattung der  abziehbaren Vorsteuern an ausländische Unternehmer geschaffen wird (BGBl 1995/279 idgF)  hin.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/142618.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142618.1_38`)


Die belangte Behörde verwies unter Wiedergabe der Bestimmungen der Verordnung des BMF,  mit der ein eigenes Verfahren für die Erstattung der abziehbaren Vorsteuern an ausländische  Unternehmer geschaffen wird (BGBl 1995/279), dass ihres Erachtens das  Vorsteuererstattungsverfahren zwingend anzuwenden sei und daher keine Jahresveranlagung  vorgenommen werden könnte.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_59`)


In diesem Zusammenhang  verweist die Bf. auf den Grundsatz von Treu und Glauben (Erlass des BMF 06.04.2006, BMF- 010103/0023-VI/2006).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_69`)


Es werde somit  angeregt, den Antrag an den Verfassungsgerichtshof zu stellen, die Kundmachung des BMF zur  GZ BMF-010202/0100-VI/3/2004 [gemeint wohl: 2014] wegen Gesetzeswidrigkeit sowie die  Bestimmung des § 38 Abs. 1 BewG wegen Verfassungswidrigkeit zu prüfen und aufzuheben.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/145202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145202.1_39`)


Sie werden jeweils vom Landesgericht für Zivilrechtssachen in  Wien bekanntgegeben und jährlich vom BMF unter www.bmf.gv.at veröffentlicht.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Landesgericht für Zivilrechtssachen in  Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_133`)


10. Grundsätzlich kommt aus österreichischer Sicht - unter anderem - die Abänderung eines  Bescheides aufgrund eines rückwirkenden Ereignisses nach § 295a BAO als  verfahrensrechtliches Instrument zur Umsetzung der Verständigungsregelung dann in  Betracht, wenn das anwendbare DBA keine dem Art. 25 Abs. 2 entsprechende Bestimmung  enthält (vgl. den diesbezüglichen Hinweis von Papst/Urtz, in Aigner/Kofler/Tumpel, DBA2 Art.  25 Rz 99 auf Erlässe des BMF und deren Aufgriff in der Literatur).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_192`)


17. Also mag die Rechtsauffassung des VwGH der zwischen Österreich und Deutschland  geschlossenen Verständigungslösung (allgemeines Konsultationsverfahren) vom 13. August  2010, Erlass des BMF vom 21. Dezember 2010, BMF-010221/3371-IV/4/2010, insoweit nicht  widersprechen, als ihr zufolge nicht im ehemaligen Tätigkeitsstaat (hier: Deutschland)  besteuerte Abfindungszahlungen „gemäß Artikel 28 Absatz 1 lit. a“ im Ansässigkeitsstaat dieser  Person besteuert werden können (hier: Österreich).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_15`)


Die zuständige Abteilung des BMF hat dem BFG gegenüber bestätigt, dass der angefochtene  Bescheid der Bf. (bzw. dessen steuerlicher Vertretung) am 6.2.2025 zugestellt – und zudem von  dieser noch am selben Tag gelesen – wurde (E-Mail vom 6.6.2025).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_18`)


Der Zeitpunkt der elektronischen Zustellung am 6.2.2025 (via Databox) wurde dem BFG von  der zuständigen Abteilung des BMF (Zentrale Services – Verfahrensbetreuung) bestätigt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_22`)


Laut Auskunft bzw. Auswertung des  BMF erfolgte die Zustellung – ordnungsgemäß - per FinanzOnline (Databox) am 6.2.2025 (und  wurde überdies auch noch am selben Tag von der Empfängerin gelesen).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/148936.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148936.1_30`)


Der Vertreter der  belangten Behörde verwies nochmals darauf, dass das Pensionsschema des britischen  Unternehmens aufgrund der (in der Beschwerdevorentscheidung übernommenen) Auskunft  der ZFS (= zentralen Fachstelle des BMF) nicht als begünstigte Pensionskasse im Sinne das DBA  zu sehen sei, da der Trustee neben der Verwaltung des hier zu behandelnden Pensionsfonds  auch noch andere Tätigkeiten ausübe und die ZFS davon ausgehe, dass bei der Übertragung  von einem britischen Pensionsschema auf das andere Pensionsschema zwischenzeitig eine  Verfügungsmacht des BF bestanden habe.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_37`)


Entsprechend den Erlässen des BMF habe die Antragstellerin stellvertretend für ihre  Anteilsinhaber für die Jahre 2009 und 2010 gemäß den Doppelbesteuerungsabkommen mit  Österreich die Herabsetzung der Kapitalertragsteuer auf 15% und Erstattung des  Differenzbetrages (10% der Bruttodividenden) beantragt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_18`)


Mit Beschwerdevorentscheidung vom 30.10.2019 wies das Finanzamt die Beschwerde gegen  den Einkommensteuerbescheid 2018 mit nachstehender Begründung ab:  Laut Information des BMF/bundesweiter Fachbereich vom 20.11.2012, SZK-010203/0539-

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt_entities` 🏆

**F1:** 0.219 | **Precision:** 0.965 | **Recall:** 0.123  

**Format:** `regex`  
**Rule ID:** `f17f12e1`  
**Description:**
Matches Finanzamt entities including specific locations and standalone genitive forms, handling spacing variations and missing locations like Graz-Stadt, Steiermark Mitte, Klosterneuburg.

**Content:**
```
(?:des|vom|bei|von|der|an|für|\s)(Finanzamt(?:es)?(?:\s+(?:für\s+Großbetriebe|Innsbruck|Österreich/FAÖ|Baden\s+Mödling|Graz-Umgebung|Wien\s+2/20/21/22|FA|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Österreich|Braunau\s+Ried\s+Schärding|Neunkirchen\s+Wr\.\s+Neustadt|Waldviertel|Bregenz|Salzburg-Land|Salzburg-Stadt|Judenburg\s+Liezen|Kirchdorf\s+Perg\s+Steyr|Bruck\s+Eisenstadt\s+Oberwart|Graz-Stadt|Steiermark\s+Mitte|Klosterneuburg|Eisenstadt|Wien\s+12/13/14\s+Purkersdorf)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.965 | 0.123 | 0.219 | 821 | 792 | 29 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 792 | 29 | 5624 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Innsbruck` | `Finanzamtes Innsbruck` |

**Missed by this rule (FN):**

- `Dr.in Hemma Bährs` (person)
- `Univ.-Prof.in Rachel Darnieder` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Chen Petermüller` (person)
- `Sand 5, 4851 Hehenberg, Österreich` (address)
- `Anka Vrcic` (person)
- `20-238/1198` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Innsbruck` | `Finanzamtes Innsbruck` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Viktoria Kreiselmayer` (person)
- `Muran Waldhans, BEd` (person)
- `Am Tegel 5, 9831 Waben, Österreich` (address)
- `Corazza Kocholl Laimer Rechtsanwälte OG` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Miroslav Hankel, BEd` (person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Finanzamtes Kirchdorf Perg Steyr` | `Finanzamtes Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Mag. Susanne Feichtenschlager` (person)
- `Daisy Wegelein` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `61-004/6209` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Mag. Erich Schwaiger` (person)
- `Matthäus Domrös` (person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich` (address)
- `Dr. Gerlinde  Rieser` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Graz-Stadt` | `Finanzamtes Graz-Stadt` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Donald Paulovits` (person)
- `Tröbach 41, 9130 Leibsdorf, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `95-720/4312` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_6`)


Die Änderung erfolgte aufgrund der  bescheidmäßigen Feststellungen des Finanzamtes Graz-Stadt zu Steuernummer xxx/yyyy vom  11.10.2011.

| Predicted | Gold |
|---|---|
| `Finanzamtes Graz-Stadt` | `Finanzamtes Graz-Stadt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Wolf Sackner, Altweitra 15, 6091 Götzens, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  34-684/1904  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  2/20/21/22` | `Finanzamtes Wien  2/20/21/22` |

**Missed by this rule (FN):**

- `Wolf Sackner` (person)
- `Altweitra 15, 6091 Götzens, Österreich` (address)
- `34-684/1904` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Siegfried Fenz` (person)
- `Huberta Nothofer` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Tanja Wescher, Margaretenplatz 55, 3170 Gerstbach, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 07-638/8400  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Dr. Ralf Schatzl` (person)
- `Tanja Wescher` (person)
- `Margaretenplatz 55, 3170 Gerstbach, Österreich` (address)
- `07-638/8400` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Dr.in Klara Willumelies` (person)
- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Dr. Viktoria Blaser` (person)
- `Stephan Antonewitz` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter OMedR Viktor Butterbrod in der Beschwerdesache Holger Virhus,  Bisamberger Straße 67, 8342 Wörth, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 36-425/3917  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `OMedR Viktor Butterbrod` (person)
- `Holger Virhus` (person)
- `Bisamberger Straße 67, 8342 Wörth, Österreich` (address)
- `36-425/3917` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Sahin, Fischmarkt 627, 4153 Vorderschiffl, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Dimitri Sahin` (person)
- `Fischmarkt 627, 4153 Vorderschiffl, Österreich` (address)
- `LMG  Steuerberatungsgesellschaft m.b.H.` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache HR Juliana Seidl, Am Gelände 10, 3282 Wiesmühl, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `HR Juliana Seidl` (person)
- `Am Gelände 10, 3282 Wiesmühl, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt Oberwart` | `Finanzamtes Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Felizitas Philippov` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Gerald Hellbing` (person)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Manuel Rathlev, Hadersfelder Straße 10, 4171 Kasten, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Edwin Meuser  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Wien 2/20/21/22` | `Finanzamtes  Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Manuel Rathlev` (person)
- `Hadersfelder Straße 10, 4171 Kasten, Österreich` (address)
- `Edwin Meuser` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Wien 2/20/21/22` | `Finanzamtes  Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Stephan Neiser` (person)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Mag. Esra Rohleder` (person)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Hademar Berking` (person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich` (address)
- `Mag. Margot Artner` (person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Siegfried Fenz` (person)
- `Techn R HR Martina Pisterer` (person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich` (address)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Braunau Ried Schärding` | `Finanzamt Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Priv.-Doz. Lubomir Gruebert` (person)
- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Jeannine Hüpgen` (person)
- `Alois Jeckl` (person)
- `Amlach 6, 2620 Straßhof, Österreich` (address)
- `66-092/6335` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über den Antrag  der Antonia Piekorz, LLB Bakk. phil., Aubrunnerweg 10d, 9150 Rinkenberg, Österreich  vom 23. März 2020 auf Gewährung der Verfahrenshilfe für das  Beschwerdeverfahren gegen den Bescheid der belangten Behörde Finanzamt Bruck Eisenstadt  Oberwart vom 28. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 beschlossen:  Der Antragstellerin wird gemäß § 292 BAO Verfahrenshilfe bewilligt.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt  Oberwart` | `Finanzamt Bruck Eisenstadt  Oberwart` |

**Missed by this rule (FN):**

- `Dr. Maria-Luise Wohlmayr` (person)
- `Antonia Piekorz, LLB Bakk. phil.` (person)
- `Aubrunnerweg 10d, 9150 Rinkenberg, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Anatol Hasenbein, Josef-Kaut-Straße 3, 4048 Großamberg, Österreich, über die Beschwerde vom 26. Mai 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 15. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  2/20/21/22` | `Finanzamtes Wien  2/20/21/22` |

**Missed by this rule (FN):**

- `Anatol Hasenbein` (person)
- `Josef-Kaut-Straße 3, 4048 Großamberg, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  2/20/21/22` | `Finanzamtes Wien  2/20/21/22` |

**Missed by this rule (FN):**

- `Mag. Regina Vogt` (person)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Waldviertel` | `Finanzamtes Waldviertel` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `HR Frederik Kleinmichel, MA` (person)
- `Haniflgasse 12, 4725 Stadl, Österreich` (address)
- `Astoria Steuerberatung GmbH & Co KG` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_131`)


Entgegen der Ansicht des  Finanzamt Waldviertel sind die geforderten Voraussetzungen sehr wohl erfüllt und  bedürfen näherer Erläuterung.

| Predicted | Gold |
|---|---|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Mag. Stefan Pipal` (person)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Graz-Stadt` | `Finanzamtes Graz-Stadt` |

**Missed by this rule (FN):**

- `Dr. Jeffrey Wengschick` (person)
- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_6`)


Da die Bf im abgabenbehördlichen Rechtmittelverfahren trotz mehrerer Ergänzungsvorhalte  keine hinreichenden Nachweise für die in den nachgereichten ANV-Erklärungen geltend  gemachten verfahrensgegenständlichen Aufwendungen beibrachte, erließ das Finanzamt Salzburg-Stadt (FA)  in der Folge zudem für alle vier Jahre abweisende Beschwerdevorentscheidungen (BVE).

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ursula Raubart, Tschupbach 5c, 4144 Karlsbach, Österreich, vertreten durch Rachel Woiczyk, Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 86-917/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Ursula Raubart` (person)
- `Tschupbach 5c, 4144 Karlsbach, Österreich` (address)
- `Rachel Woiczyk` (person)
- `Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich` (address)
- `86-917/1669` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_27`)


Rechtliche Beurteilung  2.1. Übergang der Zuständigkeit zum 01.01.2021:  Gemäß § 323b Abs.1 BAO treten das Finanzamt Österreich und das Finanzamt für Großbetriebe  für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die Stelle des jeweils am  31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Mag. Josef Zwilling` (person)
- `Tiffany Kleiß` (person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich` (address)
- `79-412/0834` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_3`)


Begründung  Mit Erkenntnis des Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015 wurde die  Bescheidbeschwerde des Revisionswerbers gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart betreffend Einkommensteuer für das Jahr 2010 abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck  Eisenstadt Oberwart` | `Finanzamtes Bruck  Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Kirchdorf Perg Steyr` | `Finanzamtes Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Dr. Michael Mandlmayr` (person)
- `Dipl.-Ing. Waldemar Zumloh` (person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich` (address)
- `09-591/1655` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Innsbruck` | `Finanzamtes Innsbruck` |

**Missed by this rule (FN):**

- `Priv.-Doz. Fridolin Härlin` (person)
- `Alva Czymzik` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Julian Pierchala,  Pracherweg 6, 8635 Gollrad, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 74-273/9351, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Julian Pierchala` (person)
- `Pracherweg 6, 8635 Gollrad, Österreich` (address)
- `74-273/9351` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ralph Staibler, Pregerstraße 17, 4242 Kirchberg, Österreich, über die Beschwerde vom 15. Juni 2019 gegen den Bescheid des Finanzamtes  Österreich, vormals des Finanzamtes Salzburg-Land vom 16. Mai 2019 betreffend die  Wiederaufnahme des Verfahren gemäß § 303 Abs.1 BAO zur Einkommensteuer 2013 sowie die  Bescheide vom 17. Mai 2019 betreffend die Wiederaufnahme der Verfahren gemäß § 303  Abs.1 BAO zur Einkommensteuer 2014 und 2015 zu Steuernummer 92-314/9447  zu Recht  erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Ralph Staibler` (person)
- `Pregerstraße 17, 4242 Kirchberg, Österreich` (address)
- `92-314/9447` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_32`)


Zur Amtspartei ab 01.01.2021:  Gemäß § 323b Abs.1 BAO treten das Finanzamt Österreich und das Finanzamt für Großbetriebe  für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die Stelle des jeweils am  31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Adrian Hofschmidt, Dechantsbühel 10, 9911 Bannberg, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Adrian Hofschmidt` (person)
- `Dechantsbühel 10, 9911 Bannberg, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Gudrun Breunlein, Am Rintl 6, 5324 Faistenau, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 75-682/2104  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Gudrun Breunlein` (person)
- `Am Rintl 6, 5324 Faistenau, Österreich` (address)
- `75-682/2104` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RgR OMedR Miklos Pellegrin, Ostendeweg 9, 9981 Glor-Berg, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 73-541/6746, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Ansgar Unterberger` (person)
- `RgR OMedR Miklos Pellegrin` (person)
- `Ostendeweg 9, 9981 Glor-Berg, Österreich` (address)
- `73-541/6746` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Missed by this rule (FN):**

- `Natalie Emmerling` (person)
- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich` (address)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_145`)


Das Finanzamt Österreich wurde in einer  Information der Abt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Veit Vissers, Wander Bertoni-Straße 166, 5223 Fludau, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 94-198/2586  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Mag. Susanne Haim` (person)
- `Veit Vissers` (person)
- `Wander Bertoni-Straße 166, 5223 Fludau, Österreich` (address)
- `94-198/2586` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Dr.in Sophie Nauman` (person)
- `Prof. Helmut Fürnkäß` (person)
- `Dr Christian Leskoschek` (person)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/132342.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132342.1_15`)


Das Finanzamt Österreich, welches gemäß § 323b Abs. 1 BAO per 1. Jänner 2021 an die Stelle  des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf getreten ist, legte die beiden  Vorlageanträge am 21.1.2021 dem BFG vor.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Eugenia Vesen` (person)
- `Apollogasse 213, 5522 Lammertal, Österreich` (address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_84`)


IV. Rechtliche Beurteilung  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 tritt das Finanzamt Österreich am 01.01.2021  an die Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_85`)


Partei des  Verfahrens ist nunmehr das Finanzamt Österreich als belangte Behörde, deren Bezeichnung  war somit im Spruch entsprechend richtig zu stellen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Erhard Wintjens, Völkerweg 97, 8940 Döllach, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 17-868/7871  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  2/20/21/22` | `Finanzamtes Wien  2/20/21/22` |

**Missed by this rule (FN):**

- `Erhard Wintjens` (person)
- `Völkerweg 97, 8940 Döllach, Österreich` (address)
- `17-868/7871` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Missed by this rule (FN):**

- `Univ.-Prof. Merlin Thorschmidt` (person)
- `Adrian Radakovitsch` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/132524.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132524.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Royackers  in der Beschwerdesache Lena Grobbing,  Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich, betreffend Beschwerde vom 1. Mai 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 12. April 2019 hinsichtlich Wiederaufnahme § 303 BAO /  ESt 2016,  Steuernummer 94-382/8878  den Beschluss gefasst:  I.  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Wien 2/20/21/22` | `Finanzamtes  Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Corinna Royackers` (person)
- `Lena Grobbing` (person)
- `Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich` (address)
- `94-382/8878` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karen Billhard  in der Beschwerdesache der  KEX Solar Entwicklung, Deniflestraße 24, 3032 Rekawinkel, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Innsbruck` | `Finanzamtes Innsbruck` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Karen Billhard` (person)
- `KEX Solar Entwicklung` (organisation)
- `Deniflestraße 24, 3032 Rekawinkel, Österreich` (address)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Samir Schwahn,  Pichlmoarstraße 73, 3653 Ottenberg, Österreich, über die Beschwerde vom 7. Jänner 2016  gegen den Bescheid des  Finanzamtes Österreich vom 9. Dezember 2015 betreffend Abweisung des Antrags auf  Ausgleichszahlung (Familienbeihilfe 01.2010-12.2015 ) zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 9. Dezember 2015 wird gemäß § 279 Abs. 1 BAO  abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Samir Schwahn` (person)
- `Pichlmoarstraße 73, 3653 Ottenberg, Österreich` (address)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Erika Matuszcyk  in der Beschwerdesache Hon.-Prof. Hugo Beerbaum,  Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Innsbruck` | `Finanzamtes  Innsbruck` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Erika Matuszcyk` (person)
- `Hon.-Prof. Hugo Beerbaum` (person)
- `Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich` (address)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/132646.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Urs Zumbroich  in der Beschwerdesache Techn R Huberta Witte,  Ebenweg 188, 4081 Mußbach, Österreich, über die Beschwerde vom 8. Juni 2016 gegen den Bescheid des Finanzamtes  Lilienfeld St. Pölten (jetzt Finanzamt Österreich) vom 13. Mai 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Priv.-Doz. Urs Zumbroich` (person)
- `Techn R Huberta Witte` (person)
- `Ebenweg 188, 4081 Mußbach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Franka Hilgenstock, Bockackerstraße 19, 4892 Sieberer, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Mag. Albert Salzmann` (person)
- `Franka Hilgenstock` (person)
- `Bockackerstraße 19, 4892 Sieberer, Österreich` (address)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_35`)


EStG“  Mit 1. Jänner 2021 trat gemäß § 323b Abs. 1 BAO das Finanzamt Österreich an die Stelle des  Finanzamtes Wien 1/23.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes Wien 1/23` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_37`)


Das Finanzamt Österreich legte die Beschwerde samt einem Vorlagebericht am 26. Jänner  2021 an das Bundesfinanzgericht vor.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132731.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Leila Höflein, Äussere Vorachstraße 25, 4081 Deinham, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Mag. Günter Narat` (person)
- `Leila Höflein` (person)
- `Äussere Vorachstraße 25, 4081 Deinham, Österreich` (address)
- `Dr. Heinz Häupl Rechtsanwalts GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132731.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132731.1_25`)


3.1. Rechtsgrundlagen, rechtliche Würdigung  Zunächst ist festzuhalten, dass das Finanzamt Österreich gem. § 323b Abs 1 BAO an die Stelle  des den angefochtenen Bescheid erlassenden Finanzamtes Freistadt Rohrbach Urfahr getreten  ist.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Eduard Schulden, Bakk. rer. nat., Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 28-951/9095, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Eduard Schulden, Bakk. rer. nat.` (person)
- `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich` (address)
- `Freund & Partner Steuerberater GmbH` (organisation)
- `28-951/9095` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_31`)


2011  nicht anerkannte Vorsteuer 31.500,00  Erfolgsänderung 157.500,00  Das Finanzamt Baden Mödling folgte den Festellungen des Betriebsprüfers und erließ in  wiederaufgenommenen Verfahren an die Bf.:   Umsatzsteuerbescheid 2011 vom 5. Juli 2016, welcher die Umsatzsteuer für das Jahr  2011 mit -83,25 € festsetzte, wobei Vorsteuern in Höhe von 583,25 € berücksichtigt  wurden;

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_59`)


Hierzu erließ das Finanzamt Baden Mödling abweisende, mit 13. September 2017 datierte  Beschwerdevorentscheidungen betreffend Umsatzsteuer 2011 und Feststellung von  Einkünften gemäß § 188 BAO für 2011, wobei jeweils auf eine gesondert zugehende  Begründung verwiesen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_69`)


Aufgrund dieser Feststellungen ist das Finanzamt Baden Mödling der Ansicht, dass die  behauptete Absicht, den streitggstdlKfz angeschafft zu haben, um ihn alsbald zu verkaufen, im  festgestellten Verhalten des Hrn.

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Oleg Bösehans  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 80-404/4147, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Oleg Bösehans` (person)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)
- `80-404/4147` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Helga Zeißig` (person)
- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/133011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133011.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Helena Przybilowski  in der Beschwerdesache Michaela Lomanns,  Kolmtaler Weg 694, 4294 Wenigfirling, Österreich, vertreten durch Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H,  Wienerstraße 73, 2604 Theresienfeld, betreffend Beschwerde vom 28. Februar 2020 gegen die  Bescheide des Finanzamtes Baden Mödling vom 31. Jänner 2020 betreffend Einkommensteuer  2015, 2016 und 2017, Steuernummer 73-613/0108, beschlossen:  Die Vorlageanträge vom 16. Februar 2021 gegen die Beschwerdevorentscheidungen 2015,  2016 und 2017 vom 15. Jänner 2021 werden gemäß § 260 Abs. 1 lit b BAO in Verbindung mit  § 264 Abs. 4 lit e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Helena Przybilowski` (person)
- `Michaela Lomanns` (person)
- `Kolmtaler Weg 694, 4294 Wenigfirling, Österreich` (address)
- `Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H` (organisation)
- `73-613/0108` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/133027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Helge Angenheyster  in der Beschwerdesache des  [...], [...], Steuernummer 86-194/1844, über die Beschwerde vom 19. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 13. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Helge Angenheyster` (person)
- `86-194/1844` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/133027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133027.1_4`)


Der Bf wurde auf Basis der dem Finanzamt Österreich (FA) vom Arbeitgeber übermittelten  Lohnzetteldaten und der Angaben in der ANV-Erklärung 2020 antragsgemäß (unter  Berücksichtigung eines PP von 1.480,- €, eines Pendlereuro von 80,- € und eines  Familienbonus Plus (FABO+) für 3 Kinder) veranlagt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/133037.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133037.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Marcel Tummernicht, Gesern 3, 9433 Kienberg, Österreich, über die Beschwerde vom 9. November 2017  gegen den Bescheid des Finanzamtes Österreich vom 19. Oktober 2017 betreffend Haftung für  Kapitalertragsteuer für die Jahre 2009 bis 2012, Steuernummer 30-367/8113, zu Recht  erkannt:   Der Beschwerde betreffend Haftung für Kapitalertragsteuer 2009 wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Marcel Tummernicht` (person)
- `Gesern 3, 9433 Kienberg, Österreich` (address)
- `30-367/8113` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/133042.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133042.1_89`)


Die Existenz eines „Finanzamtsbriefkastens“ ist aus der Home-Page des Finanzamtes  Österreich, Dienststelle Deutschlandsberg, nicht ersichtlich.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/133114.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133114.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Heinz Clee, Am Seeweg 250, 4284 Schmierreith, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 8.1.2020  gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich)  betreffend  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2013 vom 12.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2014 vom 13.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2015 vom 13.12.2019  zu Recht erkannt:   I. Soweit sich die Beschwerden vom 8.1.2020 gegen die Bescheide über die  Wiederaufnahme der Verfahren betreffend Einkommensteuer 2013, 2014 und 2015  richten, wird diesen gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Stadt` | `Finanzamtes Salzburg-Stadt` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Mag. Albert Salzmann` (person)
- `Heinz Clee` (person)
- `Am Seeweg 250, 4284 Schmierreith, Österreich` (address)
- `Pallauf Meißnitzer Staindl & Partner` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Ulrich Nieklaus, LLM, Weiberfelderweg 11, 5151 Kleinberg, Österreich, über die Beschwerde vom 3. November 2015 gegen die Bescheide des Finanzamtes  Bruck Eisenstadt Oberwart vom 1. Oktober 2015 betreffend Wiederaufnahme § 303 BAO /  ESt  01.10.2015 betreffend Einkommensteuer für die Jahre 2012 und 2013, Steuernummer  41-460/8999  zu Recht erkannt: .  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Bruck Eisenstadt Oberwart` | `Finanzamtes  Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Ulrich Nieklaus, LLM` (person)
- `Weiberfelderweg 11, 5151 Kleinberg, Österreich` (address)
- `41-460/8999` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/133177.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anabel Sezgin  in der Beschwerdesache der  Leichsner u. Knoerrnschild Getränke, Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich, vertreten durch Heinz Wollkopf,  Gartenauerstraße 8, 4616 Grassing, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Graz-Stadt` | `Finanzamtes Graz-Stadt` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Dr.in Anabel Sezgin` (person)
- `Leichsner u. Knoerrnschild Getränke` (organisation)
- `Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich` (address)
- `Heinz Wollkopf` (person)
- `Gartenauerstraße 8, 4616 Grassing, Österreich` (address)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/133179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133179.1_2`)


Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse 17, 1010 Wien, über die Beschwerde vom 24. Februar 2021 gegen die  Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 17. Juli 2020  betreffend  - Umsatzsteuer für die Jahre 2012 bis 2016 sowie  - Wiederaufnahme betreffend Umsatzsteuer für die Jahre 2012 bis 2016  zu Recht:  I. Der Beschwerde gegen die Wiederaufnahmsbescheide betreffend Umsatzsteuer 2012 bis  2016 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `MMag. Gerald Erwin Ehgartner` (person)
- `Annkathrin Cattus` (person)
- `AUDITREU Steuerberatungsgesellschaft  m.b.H.` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Torsten Schattner, Stögersbach 35, 7031 Krensdorf, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 21. September 2017  betreffend Abweisung eines  Antrages auf Aufhebung des Einkommensteuerbescheides 2016 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Torsten Schattner` (person)
- `Stögersbach 35, 7031 Krensdorf, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_47`)


Die eingegangenen Stellungnahmen (die Eidgenössische Finanzmarktaufsicht, der Schweizeri- sche Versicherungsverband und der Liechtensteinische Versicherungsverband haben sich für  nicht zuständig erklärt) hat das Bundesfinanzgericht den Finanzämtern Bregenz und Feldkirch  mit dem Hinweis, dass daraus nach Ansicht des Bundesfinanzgerichtes eine Möglichkeit zur  Aufrechterhaltung des Anspruches auf eine Altersrente nicht abgeleitet werden könne und,  sofern die Finanzämter weiterhin vom Bestehen eines  begünstigungsschädlichen Wahlrechtes  ausgehen sollten, konkrete Versicherungsgesellschaften namhaft zu machen seien, die tatsäch- lich Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform auf dem  freien Markt angeboten hätten, zur Stellungnahme übermittelt.   Das nunmehrige Finanzamt Österreich, Dienststelle Vorarlberg (FA98), hat daraufhin am  18. Februar 2021 mitgeteilt, dass 33 liechtensteinische und schweizerische Versicherungsun- ternehmen (einschließlich schweizerischer Versicherungsunternehmen, die in Liechtenstein im  grenzüberschreitenden Dienstleistungsverkehr zugelassen sind) um Auskunft ersucht worden  seien, ob Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform ange- boten würden bzw. in der Vergangenheit angeboten worden seien (Frage 1) oder andernfalls  die  Möglichkeit bestehe bzw. bestanden habe, den Vorsorgeschutz in Rentenform durch Ab- schluss einer Freizügigkeitspolice im Wege eines individuellen Einzelvertrages aufrechtzuerhal- ten (Frage 2).

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Cathleen Ganczarczyk  in der Beschwerdesache Hon.-Prof. Gregor Liechtenstein,  Platz der Menschenrechte 39, 4652 Reuharting, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, über die Beschwerde vom 28. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 26. November 2020 betreffend Gebühren 29.04.2014  Steuernummer 82-359/1150  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Cathleen Ganczarczyk` (person)
- `Hon.-Prof. Gregor Liechtenstein` (person)
- `Platz der Menschenrechte 39, 4652 Reuharting, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `82-359/1150` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Dalibor Kochendörfer, Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich, über die Beschwerde vom 16. Oktober 2020 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 16. September 2020  betreffend Wiederaufnahme des Verfahrens hinsichtlich des Antrages auf Familienbeihilfe vom  22. Juli 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Dr. Siegfried Fenz` (person)
- `Dalibor Kochendörfer` (person)
- `Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich` (address)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Hermann Bloehdorn, Bierbaum 35, 8983 Bad Mitterndorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerden vom 9. und 13. Jänner 2014 sowie vom 25. September 2015 und vom 20.  Oktober 2017 gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt  Österreich) vom 6. Dezember 2013, sowie vom 26. August 2015 und vom 11. September 2017  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 bis 2014, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Mag. Judith Daniela Herdin-Winter` (person)
- `Hermann Bloehdorn` (person)
- `Bierbaum 35, 8983 Bad Mitterndorf, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/133297.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133297.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Anton Lauscheck, Kesselstraße 10, 9551 Unterberg, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 10. Februar 2017 betreffend Einkommensteuer 2015 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Anton Lauscheck` (person)
- `Kesselstraße 10, 9551 Unterberg, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/133297.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133297.1_22`)


Die eingegangenen Stellungnahmen (die Eidgenössische Finanzmarktaufsicht, der Schweizeri- sche Versicherungsverband und der Liechtensteinische Versicherungsverband haben sich für  nicht zuständig erklärt) hat das Bundesfinanzgericht den Finanzämtern Bregenz und Feldkirch  mit dem Hinweis, dass daraus nach Ansicht des Bundesfinanzgerichtes eine Möglichkeit zur  Aufrechterhaltung des Anspruches auf eine Altersrente nicht abgeleitet werden könne und,  sofern die Finanzämter weiterhin vom Bestehen eines  begünstigungsschädlichen Wahlrechtes  ausgehen sollten, konkrete Versicherungsgesellschaften namhaft zu machen seien, die tatsäch- lich Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform auf dem  freien Markt angeboten hätten, zur Stellungnahme übermittelt.   Das nunmehrige Finanzamt Österreich, Dienststelle Vorarlberg (FA98), hat daraufhin am  18. Februar 2021 mitgeteilt, dass 33 liechtensteinische und schweizerische Versicherungsun- ternehmen (einschließlich schweizerischer Versicherungsunternehmen die in Liechtenstein  im grenzüberschreitenden Dienstleistungsverkehr zugelassen sind) um Auskunft ersucht wor- den seien, ob Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Christian Jovanovic, BA, Himmelsstiege 8, 4521 Matzelsdorf, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Christian Jovanovic, BA` (person)
- `Himmelsstiege 8, 4521 Matzelsdorf, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_32`)


Die eingegangenen Stellungnahmen (die Eidgenössische Finanzmarktaufsicht, der Schweizeri- sche Versicherungsverband und der Liechtensteinische Versicherungsverband haben sich für  nicht zuständig erklärt) hat das Bundesfinanzgericht den Finanzämtern Bregenz und Feldkirch  mit dem Hinweis, dass daraus nach Ansicht des Bundesfinanzgerichtes eine Möglichkeit zur  Aufrechterhaltung des Anspruches auf eine Altersrente nicht abgeleitet werden könne und,  sofern die Finanzämter weiterhin vom Bestehen eines  begünstigungsschädlichen Wahlrechtes  ausgehen sollten, konkrete Versicherungsgesellschaften namhaft zu machen seien, die tatsäch- lich Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform auf dem  freien Markt angeboten hätten, zur Stellungnahme übermittelt.   Das nunmehrige Finanzamt Österreich, Dienststelle Vorarlberg (FA98), hat daraufhin am  18. Februar 2021 mitgeteilt, dass 33 liechtensteinische und schweizerische Versicherungsun- ternehmen (einschließlich schweizerischer Versicherungsunternehmen, die in Liechtenstein im  grenzüberschreitenden Dienstleistungsverkehr zugelassen sind) um Auskunft ersucht worden  seien, ob Freizügigkeitspolicen mit Anspruch auf eine spätere Auszahlung in Rentenform ange- boten würden bzw. in der Vergangenheit angeboten worden seien (Frage 1) oder andernfalls  die  Möglichkeit bestehe bzw. bestanden habe, den Vorsorgeschutz in Rentenform durch Ab- 3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/133392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133392.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ruperta Ekonomou  in der Beschwerdesache Erhard Sennewaldt,  Taubenwaldweg 24, 3232 Unterschildbach, Österreich, betreffend Beschwerde vom 29. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuervorauszahlungen  2021 Steuernummer 21-935/5536  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 5 BAO iVm § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Dr.in Ruperta Ekonomou` (person)
- `Erhard Sennewaldt` (person)
- `Taubenwaldweg 24, 3232 Unterschildbach, Österreich` (address)
- `21-935/5536` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. Juni 2020 des Beschwerdeführers Edgar Soutschek, Am Klosterbruch 21, 3661 Hart, Österreich  gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 26. Mai 2020  hinsichtlich Einkommensteuer 2019 vom 3. April 2020 zu Recht:    I)  Der Einkommensteuerbescheid 2019 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Mag. Günter Narat` (person)
- `Edgar Soutschek` (person)
- `Am Klosterbruch 21, 3661 Hart, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_20`)


Mit Beschluss des Bundesfinanzgerichtes vom 18.05.2021 wurde diese Vorhaltsbeantwortung  des BF dem Finanzamt Österreich zur Kenntnisnahme übermittelt und Gelegenheit gegeben,  eine entsprechende Stellungnahme zum Vorbringen des BF abzugeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_39`)


Zu Spruchpunkt I.  Zunächst ist festzuhalten, dass das Finanzamt Österreich gem. § 323b Abs 1 BAO an die Stelle  des die angefochtenen Bescheide erlassenden Finanzamtes Freistadt Rohrbach Urfahr getreten  ist.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Wolfgang Orosz, Tenoplatz 5, 8524 Hohenfeld, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 45-492/4197  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Dr. Gabriele Krafft` (person)
- `Wolfgang Orosz` (person)
- `Tenoplatz 5, 8524 Hohenfeld, Österreich` (address)
- `Commendatio Wirtschaftstreuhand GmbH` (organisation)
- `45-492/4197` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/133447.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Philipp Harazin  in der Beschwerdesache Priv.-Doz. Kevin Morzinsky,  Strußnighof 37, 9631 Kleinbergl, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Bruck Eisenstadt Oberwart), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 58-060/5953  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Dr. Philipp Harazin` (person)
- `Priv.-Doz. Kevin Morzinsky` (person)
- `Strußnighof 37, 9631 Kleinbergl, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `58-060/5953` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Eleonore Rudloph` (person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_27`)


Weiters wurde der Bescheid des (ehemaligen) Finanzamtes  Bruck Eisenstadt Oberwart vom 12.11.2014 vorgelegt, mit dem die Befreiung von der  Verpflichtung zum Steuerabzug für den Leistungszeitraum 10-12/2014 die Bf. betreffend  ausgesprochen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Bruck Eisenstadt Oberwart` | `Finanzamtes  Bruck Eisenstadt Oberwart` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_38`)


Mit selben Datum wurde der weiteren  Beschwerde für 2014 – rücksichtlich des vorgelegten Befreiungsbescheides des (vormaligen)  Finanzamtes Bruck Eisenstadt Oberwart - teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt Oberwart` | `Finanzamtes Bruck Eisenstadt Oberwart` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Braunau Ried Schärding` — partial — gold is substring of pred: `Finanzamtes Braunau Ried`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Delia Wilmerdinger`(person)
- `Kirsten Constantinescu`(person)
- `Höhenwald 50, 4822 Primesberg, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `41-83-382/2498`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132430.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132430.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 9. April 2020 des Beschwerdeführers Julian Büsges, Schleifmühle 12, 8530 Freiland bei Deutschlandsberg, Österreich  gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 3. April 2020 betreffend Einkommensteuer 2019 zu  Recht:     I)

**False Positives:**

- `Finanzamtes Braunau Ried Schärding` — partial — gold is substring of pred: `Finanzamtes Braunau Ried`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Günter Narat`(person)
- `Julian Büsges`(person)
- `Schleifmühle 12, 8530 Freiland bei Deutschlandsberg, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Oleg Bösehans  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 80-404/4147, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Salzburg-Land` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oleg Bösehans`(person)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `80-404/4147`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

**False Positives:**

- `Finanzamtes Bregenz` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Peter Steurer`(person)
- `Helga Zeißig`(person)
- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Scarlett Beverungen, Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 71-240/3156  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Finanzamtes Braunau Ried Schärding` — partial — gold is substring of pred: `Finanzamtes Braunau Ried`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Karin Pitzer`(person)
- `Scarlett Beverungen`(person)
- `Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich`(address)
- `Uniconsult Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Braunau Ried`(organisation)
- `71-240/3156`(tax_number)

</details>

---

## `Bundesministers_fuer_Arbeit_entities` 🏆

**F1:** 0.007 | **Precision:** 0.958 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `ecee8a71`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' which was previously missed.

**Content:**
```
\bBundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.958 | 0.004 | 0.007 | 24 | 23 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 1 | 6049 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_95`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und  die Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_344`)


• Einschätzungsverordnung vom 18. August 2010, BGBl II 2010/261 idF BGBl II 2012/151  Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl II 2010/261 idF BGBl II 2012/151, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_118`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_60`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_65`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_101`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  8 von 12 Seite 9 von 12

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_79`)


Für die Einschätzung des Grades der  Behinderung sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_70`)


Die näheren  Bestimmungen über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/137507.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137507.1_44`)


Die näheren  Bestimmungen über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz zu treffen.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_119`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl Nr 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl II Nr 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_156`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_216`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_53`)


Die näheren  Bestimmungen über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_103`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/146077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146077.1_115`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_142`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_158`)


Anwendung der Richtsatzverordnung:  Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des Behindertenein- stellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_128`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_172`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/146363.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146363.1_61`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des Behindertenein- stellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsver- ordnung/EVO) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung,  anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/148452.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148452.1_38`)


Für die Einschätzung des  Grades der Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr.  22/1970, in der jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des  Grades der Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr.  261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_75`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_292`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_27`)


Für die Einschätzung des Grades der Behinderung seien § 14 Absatz 3 des  Behinderteneinstellungsgesetzes und die Verordnung des Bundesministers für Arbeit, Soziales  und Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades  der Behinderung (Einschätzungsverordnung) vom 18. August 2010 anzuwenden.

**False Positives:**

- `Bundesministers für Arbeit, Soziales  und Konsumentenschutz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `AMS_entities` 🏆

**F1:** 0.016 | **Precision:** 0.946 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `9c6245ec`  
**Description:**
Matches the abbreviation AMS in legal contexts.

**Content:**
```
\bAMS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.946 | 0.008 | 0.016 | 56 | 53 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 53 | 3 | 6038 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_55`)


(Bekanntschaft, Annonce,  AMS, usw....)

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_58`)


Darum wäre sie im Gegensatz zu großen  Firmen oder Konzernen gezwungen, Arbeiter zu entlassen oder einen nur kurz oder bei AMS  Kurzarbeit anzumelden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_36`)


Neben dem regulären Besuch  der Berufschule hat P… regelmäßig Bewerbungsgespräche gehabt, bewarb sich aktiv per Mail  für eine neue Lehrstelle und besuchte Kurse, die vom AMS vermittelt wurden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_37`)


Diese wurden  mit Sicherheit vom AMS protokolliert und Sie hätten bei Bedarf Einsicht.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_47`)


Zu dem Vorbringen im Vorlageantrag:   Weder die Suche nach einer neuen Lehrstelle noch der Besuch der vom AMS vermittelten  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_57`)


bewarb sich aktiv per  Mail für eine neue Lehrstelle und besuchte Kurse, die vom AMS vermittelt wurden  (Vorlageantrag).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_74`)


Das Bundesfinanzgericht anerkannte eine Reihe von AMS-geförderten Kurse nicht als  Berufsausbildung iSd § 2 Abs. 1 lit. b FLAG 1967: "Vorbereitungskurs der ÜBA" (=  überbetriebliche Ausbildung), Kurs zur Berufsorientierung, Kurs "Projekt Büro Plus", "European  Business Competence Licence" - EBC*L und "Zertifikat Personalwesen", "Lehrgang für EDV und  Office Basics" (BFG vom 27.04.2020, RV/7101863/2019, BFG vom 02.08.2016,  RV/5100817/2014, BFG vom 23.05.2016, RV/7101739/2014, und BFG vom 25.02.2020,  RV/7105041/2019).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_81`)


- sie haben sich bei ihrem AMS arbeitslos gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_204`)


Übers AMS Berufsfindungskurse   Lebte bei den Eltern;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_85`)


Das Bundesfinanzgericht berücksichtigt die vom Bf. in seiner Beschwerde bekanntgegebene als  unterdurchschnittlich zu bezeichnende wirtschaftliche Situation des Bf. (AMS-Bezug) und setzt  die von der Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden festgesetzte Ersatzfreiheitsstrafe auf 10 Stunden herab.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_128`)


Am 5. September 2018 bestätigte das AMS der Bf., dass sie die Voraussetzungen nach § 32a  Abs. 2 bzw. 3 AuslBG erfüllt und damit im gesamten Bundesgebiet Österreichs eine  unselbständige Erwerbstätigkeit aufnehmen darf (EU-Freizügigkeitsbestätigung vom  05.09.2018.).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_17`)


Hinsichtlich des Jahres 2011 gab es von der PVA  vorerst nur einen Lohnzettel für die Monate Jänner bis März, darüber hinaus hat die Ehegattin  Zahlungen vom AMS bezogen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_18`)


Im Jahr 2012 wurde der Gattin des Beschwerdeführers  rückwirkend eine Pension für das gesamte Jahr 2011 zuerkannt und ein diesbezüglicher  Lohnzettel seitens der PVA an das Finanzamt übermittelt.  Dieser Sachverhalt ergibt sich aufgrund der Aktenlage, der Beschwerdeausführungen, der  Lohnzettel der PVA sowie der Bestätigungen des AMS.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_16`)


Am 8. August 2020 stellte Bf mit FinanzOnline einen Vorlageantrag und führte sinngemäß im  Wesentlichen Folgendes aus:  Nach seiner langjährigen Suchterkrankung habe die PVA nach mehreren abgelehnten Anträgen  und Klagen die gesundheitsbezogene Rehabilitation genehmigt und das Rehabilitationsgeld  zwar rückwirkend bis 2016 aber an die auszahlenden Stellen AMS und Sozialamt  ausbezahlt,  jedoch 2018 verbucht.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_28`)


Der Gesamtbetrag von    € 16.917,91 stimme mit den Bruttobezügen lt. Lohnzettel vom  27.02.2019 überein  Im entsprechenden Zeitraum von 08.06.2016 bis 31.12.2017 seien keine steuerfreien  Leistungen durch das AMS erfolgt (vgl. Ausdrucke der Veranlagungsjahre 2016 und 2017).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_44`)


Im gegenständlichen Fall seien jedoch keine AMS-Gelder als Vorschuss auf ein  Rehabilitationsgeld ausbezahlt worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_134`)


Im Vorlageantrag macht Bf geltend, das Rehabilitationsgeld für die Vorjahre sei 2018 nicht an  ihn, sondern die auszahlenden Stellen Arbeitsmarktservice (AMS) und Sozialamt bezahlt  worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_136`)


Darin kann ein Antrag auf Berücksichtigung einbehaltener „AMS-Gelder“ als Werbungskosten  gemäß § 16 Abs. 2 EStG 1988 gesehen werden, wozu der Verwaltungsgerichtshof im bereits  genannten Erkenntnis VwGH 19.12.2018, Ro 2017/15/0025, Folgendes ausgeführt hat:   Nach § 23 Abs. 8 Arbeitslosenversicherungsgesetz 1977 idF BGBl. I Nr. 68/2014, AlVG 1977, gilt  der Vorschuss für den Fall, dass Rehabilitationsgeld nicht zuerkannt wird, als Arbeitslosengeld  oder Notstandshilfe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_141`)


Somit kommt § 16 Abs. 2 EStG  gegenüber § 295a BAO der Vorrang zu.  Das Finanzamt hat im bekämpften Bescheid vom 10. September 2019 zu Recht auch keine  Werbungskosten gemäß § 16 Abs. 2 EStG 1988 für Rückzahlung von  „AMS-Geldern“ im Wege  der Legalzession  berücksichtigt:  Bf bezog  zwar vom 1.1.2016 bis 10.2.2016 für 41 Tage Notstandshilfe vom Arbeitsmarktservice  in Höhe von 1.148,41€.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_10`)


Außerdem bezog er  während folgender Zeiträume folgende Beträge an Notstandshilfe vom AMS:    Laut Einkommensteuerbescheid vom 12.11.2018 wurde der Besteuerung der Bf. für das Jahr  2014 ein steuerpflichtiges Einkommen in Höhe von 71.622,83 Euro zugrunde gelegt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_147`)


die am 19.06.2014 an den Bauleiter der Bf. übermittelte Zustimmung der  MA 31 wurde an die Freigabe des AMS gebunden, die bis heute nicht eingelangt ist.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_211`)


dass deren Freigabe von  der Zustimmung des AMS, die bis dato nicht vorliegt, abhing, resultiert aus dem Mail der MA  31 vom 19.06.2014 an den Zeugen DI I, sowie dem - insbesondere von der Bf. unwidersprochen  gebliebenen - Mail der Auftraggeberin an das erkennende Gericht vom 18.03.2021.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/133963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133963.1_17`)


Die monatliche Anweisung des Familienzuschlages werde vom AMS vorgenommen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133963.1_30`)


Lt. Jugendamt … steht mir als KM diese zu, da ich die Kinder regelmäßig zu den BK's hole, 2 bis  16 Tage/Monat bei mir habe, den Familienzuschlag vom AMS direkt ans Jugendamt abliefere,  weiteres bezahle ich für diese 3 Kinder 30 € mtl.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_23`)


Bei seinen Erwerbstätigkeiten habe es sich um geförderte Dienstverhältnisse für Personen mit  Beeinträchtigungen gehandelt. Eine langfristige Beschäftigung sei trotz Förderung nicht  möglich gewesen und der Bf verweise hier auf die beigelegten Dienstgeberbestätigungen und  die „Eingliederungsbeihilfe AMS“.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_80`)


13.07.1992 28.02.1994 1 J u 7,5 M Angestellter:  Verein  01.01.94-28.02.94  1.154,92 Euro  Projekt über AMS Landschaftspflege;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_89`)


03.08.2011 27.11.2011 4 M Geringfügig  beschäftigter Arbeiter  bei AG3  928,00 Euro   01.06.2015 28.02.2017 1 J u 9 M Vorläufige  Schwerarbeit    Meldende Stelle:   Sozialversicherungsanstalt der  Selbstständigen Landwirte  10.02.2017 01.07.2017 ca 4,5 M Arbeitslosengeldbezug    02.07.2017 17.07.2017 ca 0,5 M Krankengeldbezug     18.07.2017 23.07.2017  Arbeitslosengeldbezug    24.07.2017 24.07.2017  Krankengeldbezug     25.07.2017 01.10.2017 ca 2 M Arbeitslosengeldbezug    02.10.2017 31.03.2019 1 J u 6 M Angestellter:  Caritas der Diözese A  02.10.17-31.12.17  3.163,99 Euro  01.01.18-31.12.18  12.531,62 Euro  01.19-31.03.19  3.216,60 Euro  Diese Anstellung wird durch das AMS  anhand Eingliederungsbeihilfe gemäß § 34  Arbeitsmarktservicegesetz geförderte

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_152`)


- Schreiben AMS O vom 15.09.1998 an Fa AG2 GmbH: Zuschuss in der Höhe von 30% der  fiktiven Lohnkosten auf der Basis eines Monatsbruttolohnes (ohne Sonderzahlungen) von  14.525,00 S für 40 Stunden pro Woche als Hilfsarbeiter im Tischlereibereich  Zusatzvereinbarung Land NÖ vom 27.08.1997: zu monatlicher Geldbeihilfe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/136011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136011.1_26`)


Es lägen auch keine Meldungen des AMS vor.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/136011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136011.1_29`)


Eine „Nichtmeldung" beim AMS bedeute nicht, dass andere  Einkünfte vorliegen müssten.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_35`)


und anschließend bis 01/2019 Arbeitslosengeld bezogen hat und seither als arbeitssuchend  beim AMS gemeldet war.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_187`)


Anschließend hat der Bf bis November 2018 Krankengeld und dann bis Jänner 2019  Arbeitslosengeld bezogen und war seither beim AMS als arbeitssuchend gemeldet (Abfrage der  Sozialversicherungsdaten).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/139351.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139351.1_13`)


Die AMS-Leistungen seien zur Gänze rückgeführt  worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/139351.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139351.1_87`)


Laut dem vorgelegten  Bescheid des AMS vom 12.1.2010 wurde der Bf. jedoch nur für den Zeitraum von 30.4.2009 bis  5.11.2009 zur Rückzahlung des Arbeitslosengeldes verpflichtet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/139351.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139351.1_90`)


Im  Übrigen wird auf die Lohnzettel und die vom AMS gemeldeten Daten laut Bescheid vom  9.12.2010 verwiesen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_12`)


In weiterer Folge brachte die Bf eine „Beschwerde von der Steuernummer 85-520/0851“  am 6.5.2021 fristgerecht ein und brachte vor, dass sie keine doppelte Auszahlung erhalten  habe, da der Betrag an das AMS erstattet worden sei.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `85-520/0851` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_25`)


Das bis dahin bezogene Arbeitslosengeld sei daher  von der ÖGK direkt an das AMS zurückbezahlt worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf erhielt vom 22.2.2020 – 26.4.2020, 27.04.2020 – 15.10.2020, 17.10.2020 – 23.12.2020  Vorschuss auf Rehabilitationsgeld iHv € 33,19 täglich und vom 6.1.2021 – 31.3.2021 iHv € 34,32  täglich vom Arbeitsmarktservice ausbezahlt (Bezugsbestätigung AMS vom 27.1.2023).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_33`)


Die Leistungen des Arbeitsmarktservice (Vorschuss auf Rehabilitationsgeld), welche die Bf vom  22.2.2020 – 23.12.2020 iHv € 10.122,95 und vom 6.1.2021 – 31.3.2021 iHv € 2.917,20 erhielt  (gesamt € 13.040,15), wurden von der ÖGK direkt mit dem Arbeitsmarktservice im April 2021  gegenverrechnet (Bestätigungen der ÖGK, Bestätigung AMS vom 15.4.2021).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)
- `ÖGK` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_34`)


Folgende Lohnzetteldaten wurden im Jahr 2021 dem Finanzamt übermittelt:  ÖGK § 69 Abs 2 14.222,86  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 14.222,86  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 962,68  AMS § 3 Abs 2 2.917,20  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `ÖGK` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_41`)


Die Höhe der Rückzahlung (Vorschuss auf Rehabilitationsgeld) an das Arbeitsmarktservice  ergibt sich zweifelsfrei aus den Bestätigungen der ÖGK und des AMS.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_61`)


Es sind daher die im Jahr 2021 bezogenen Leistungen des AMS iHv € 2.917,20 als  steuerpflichtig zu behandeln und ein Siebentel davon ist als sonstiger Bezug zu erfassen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/141167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141167.1_28`)


Letztlich ersuchte sie den Beschwerdeführer um Bekanntgabe ob und gegebenenfalls  in welcher Höhe sein Arbeitgeber oder Förderstellen wie das Land oder das AMS die Kosten  2 von 8 Seite 3 von 8

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/145570.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145570.1_48`)


Der Vollständigkeit halber sei hier auch erwähnt, dass eine Kontrollrechnung, bei der auf eine  Hochrechnung der Einkünfte aus Oktober bis Dezember 2021 verzichtet wird, dafür aber die  steuerfreien AMS-Leistungen in die Besteuerung mit eingezogen werden, eine  Einkommensteuernachforderung von EUR 2.502,00 ergibt, was die vom FAÖ festgesetzte  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `FAÖ` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_86`)


Beim AMS gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_195`)


- sie haben sich bei ihrem AMS arbeitslos gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_226`)


Beim AMS gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_116`)


eine Meldung als arbeitssuchend, der Bezug von Arbeitslosengeld, Notstandshilfe und  Krankengeld ebenso wie der Erhalt von Beihilfen zur Deckung des Lebensunterhaltes und  Beihilfen zu Kursnebenkosen durch das AMS nicht die Voraussetzungen einer Erwerbstätigkeit  im Sinne der hier in Rede stehenden Bestimmung des § 3 Abs. 4 FLAG.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_117`)


Der VwGH erläutert  beispielsweise in seinem Beschluss vom 05.09.2019, Ra 2017/16/0160, dass der Erhalt einer  Beihilfe vom AMS zur Deckung des Lebensunterhalts iZm einem Schulbesuch (Lehrgang zur  Nachholung eines Pflichtschulabschlusses) eines subsidiär Schutzberechtigten (Eigenantrag)  keine Erwerbstätigkeit iSd § 3 Abs. 4 darstelle und allein aus diesem Grund ein Anspruch auf  Familienbeihilfe nicht bestehe (vgl. dazu auch VwGH 29.05.2013, 2010/16/0152).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_157`)


Es war auch im bisherigen Verfahren nicht strittig, dass der Beschwerdeführer offenbar keine  Grundversorgung, sondern Mindestsicherungsbeträge und Beihilfen des AMS erhalten hat.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_63`)


Sie sei dann beim AMS gewesen, der Bescheid der PV bezügl-  Arbeitsunfähigkeit sei noch ausständig.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_119`)


Aufgrund ihrer Behinderungen  sei sie laut AMS so nicht vermittelbar.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/149765.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149765.1_11`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erhielt für das Jahr 2019 folgende Zahlungen vom Arbeitsmarktservice (AMS):  Am 18.03.2019 308,35 Euro für den Zeitraum 14.01.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_9`)


Herr M. erzielte nach den Daten seines Abgabenkontos langjährig, neben geringfügigen  Einkünften aus der Untervermietung einer Mietwohnung in der S-Straße 3/ 4, 9998 Wien an  die Immo-GmbH, ausschließlich Einkünfte aus steuerfreien Transferleistungen (AMS/GKK).

**False Positives:**

- `AMS` — partial — pred is substring of gold: `AMS/GKK`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `AMS/GKK`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_46`)


2. Der Bf erzielte nach den Daten seines Abgabenkontos langjährig ausschließlich Einkünfte aus  steuerfreien Transferleistungen (AMS/GKK).

**False Positives:**

- `AMS` — partial — pred is substring of gold: `AMS/GKK`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `AMS/GKK`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/149765.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149765.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer vom AMS Österreich der Abgabenbehörde übermittelten korrigierten  Mitteilung nahm die Behörde das Verfahren betreffend Einkommensteuer 2019 gemäß § 303  Abs. 1 BAO wieder auf und erließ unter Berücksichtigung der nunmehr korrigierten  Arbeitslosengeldzahlung iHv 1.228,50 Euro für das Jahr 2019 einen neuen  Einkommensteuerbescheid 2019.

**False Positives:**

- `AMS` — partial — pred is substring of gold: `AMS Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `AMS Österreich`(organisation)

</details>

---

## `BFH_entities` 🏆

**F1:** 0.030 | **Precision:** 0.933 | **Recall:** 0.015  

**Format:** `regex`  
**Rule ID:** `0e58f673`  
**Description:**
Matches the abbreviation BFH.

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.015 | 0.030 | 104 | 97 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 97 | 7 | 6178 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_629`)


Nach der Rspr des BFH kann ein Wiederverkäufer die  Differenzbesteuerung für die Weiterveräußerung eines Gegenstandes nicht beanspruchen,  wenn er den Gegenstand von einem Unternehmer erworben hat, der für diese Lieferung zu  Unrecht die Differenzbesteuerung angewendet hat (BFH 23.4.2009, V R 52/07).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_634`)


(2) In BFH 23.4.2009, V R 52/07 heißt es dazu: Aus den der Klägerin übergebenen  ausländischen Fahrzeugpapieren ergab sich, dass die Fahrzeuge zuvor auf ausländische  Mietwagenunternehmen zugelassen worden waren.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_690`)


UFS, BFG und die deutschen Finanzgerichte gingen in ihrer bisherigen Rechtsprechung davon  aus, dass bei bestimmten Branchen der Warenhandel sehr häufig im Rahmen von  Karussellkonstruktionen oder durch betrügerische Vorlieferanten abgewickelt wird (UFS  6.5.2013, RV/0739-L/08): Dazu zählen beispielsweise der KFZ-Handel (zB FG Saarland,  Beschluss vom 13.5.2003, 1 V 22/03), der Handel mit Mobiltelefonen (zB BFH 19.4.2007, VR  48/04), der Schrotthandel (zB UFS 17.11.2011, RV/0456-L/07) oder der Handel mit  Computerteilen (zB EuGH C-354/03 vom 12.1.2006, Rs „Optigen/Fulcrum/Bond gegen  Commissioners of customs & Exercise).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_300`)


Eine den Progressionsvorbe- halt einräumende Bestimmung in einem DBA hat lediglich deklaratorische Bedeutung (vgl.  VwGH 29.7.2010, Zl. 2010/15/0021 unter Hinweis auf BFH 19.12.2001, I R 63/00 und BFH  10.12.2008, I B 60/08).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_88`)


Jakom/Baldauf, EStG8, § 34 Rz 90,  Stichwort "Kurreise" bzw Endfellner, Krankheit und Behinderung im Einkommensteuerrecht  [Wien 2012], 128 f ; vgl grundsätzlich gleichlautend auch BFH 14.8.1997, III R 67/96, BStBl II  1997, 732).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_88`)


Der deutsche Bundesfinanzhof (BFH) hat in seinem Urteil vom 12.12.2019, V R 3/19, die Frage  der umsatzsteuerlichen Ansässigkeit bei Vermietung im Inland durch eine im Ausland  wohnhafte Steuerpflichtige bereits behandelt.  Die in Italien lebende Klägerin hatte eine Wohnung in Deutschland, an der sie ein  Fruchtgenussrecht hatte, vermietet.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_90`)


Der BFH stützte seine Entscheidung auf die EuGH-Judikatur in der Rs Schmelz und kam zum  eindeutigen Ergebnis, dass „die Vermietung einer Wohnung jedenfalls für die Anwendung der  Kleinunternehmerregelung weder als ansässigkeits- noch als niederlassungsbegründend  anzusehen“ ist.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Missed by this rule (FN):**

- `Schmelz` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_80`)


BFH 18. 4. 2002, III R 15/00).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_100`)


Der besondere Pflege- oder Betreuungsbedarf eines Behinderten (iSd § 35) ist nach LStR 2002  Rz 887 durch ein ärztliches Gutachten oder durch Bezug von Pflegegeld nachzuweisen, ein  amtsärztliches Gutachten ist nicht erforderlich (vgl BFH 9.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_295`)


Die nach Art. 67 VO 883/2004 i. V. m. Art. 60 Abs. 1 Satz 2 VO 987/2009 vorzunehmende  Fiktion bewirkt, dass die Wohnsituation auf Grundlage der im Streitzeitraum im anderen EU- Mitgliedstaat gegebenen Verhältnisse (fiktiv) ins Inland übertragen wird (Bundesfinanzhof in  der Folge abgekürzt mit BFH vom 10.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_297`)


Diese Fiktion besagt aber nur, dass zu unterstellen ist, dass alle Familienangehörige im  zuständigen Mitgliedstaat wohnen, nicht aber, dass diese – wenn dies nicht im  Wohnmitgliedstaat der Fall ist – im selben Haushalt wohnen (vgl. auch BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_300`)


Wer von den unionsrechtlich grundsätzlich als anspruchsberechtige Personen anzusehenden  Familienangehörigen tatsächlich primär oder sekundär (oder gar keinen) Anspruch auf  österreichische Familienleistungen hat, ist daher nach dem nationalen Recht zu beurteilen (vgl.  auch BFH 4.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_302`)


BFH 10. 3. 2016, III R 62/12 und BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_304`)


Wer von den unionsrechtlich grundsätzlich als anspruchsberechtige Personen anzusehenden  Familienangehörigen tatsächlich primär oder sekundär (oder gar keinen) Anspruch auf  österreichische Familienleistungen hat, ist daher nach dem nationalen Recht zu beurteilen (vgl.  jeweils unter Verneinung eines vorrangigen Anspruchs des in Deutschland arbeitenden Vaters  die Entscheidungen des Bundesfinanzhofs BFH 4.2.2016, III R 17/13 betreffend im Haushalt  der Mutter in Polen lebendes Kind, BFH 10.3.2016, III R 62/12 betreffend im Haushalt der  Großmutter in Griechenland lebendes Enkelkind, BFH 28.4.2016, III R 68/13 betreffend im  Haushalt der Mutter in Spanien lebendes Kind, BFH 15.6.2016, III R 60/12 betreffend im  Haushalt der Schwester und des Schwagers in Polen lebendes Pflegekind, BFH 23.8.2016, V R  19/15 betreffend im Haushalt der Mutter in Litauen lebendes Kind, BFH 4.8.2016, III R 10/13  betreffend im Haushalt der Mutter in Ungarn lebendes Kind sowie die weiteren Entscheidungen  BFH 23.8.2016, V R 26/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_305`)


BFH 23.8.2016, V R 25/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_306`)


BFH 23.8.2016, V R 10/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_307`)


BFH  26.10.2016, III R 27/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_308`)


BFH 13.7.2016, XI R 23/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_309`)


BFH 23.8.2016, V R 40/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_310`)


BFH  23.8.2016, V R 16/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_311`)


BFH 7.7.2016, III R 46/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_312`)


BFH 23.8.2016, V R 31/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_313`)


BFH 23.8.2016,  V R 11/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_314`)


BFH 23.8.2016, V R 49/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_315`)


BFH 23.8.2016, V R 50/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_316`)


BFH 4.8.2016, III R 10/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_317`)


BFH 7.7.2016, III R 11/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_318`)


BFH 23.8.2016, V R 19/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_319`)


BFH 23.8.2016, V R 29/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_320`)


BFH  23.8.2016, V R 2/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_321`)


BFH 13.7.2016, XI R 33/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_322`)


BFH 15.6.2016, III R 67/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_323`)


BFH 13.7.2016,  XI R 28/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_324`)


BFH 13.7.2016, XI R 44/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_325`)


BFH 13.7.2016, XI R 7/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_326`)


BFH 21.7.2016, V R  46/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_327`)


BFH 28.4.2016, III R 45/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_328`)


BFH 28.4.2016, III R 65/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_329`)


BFH 13.4.2016, III R 14/13  sowie die Entscheidungen des Bundesfinanzgerichts BFG 19.8.2016, RV/7101889/2016  21 von 32 Seite 22 von 32

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_364`)


Da die Tochter des Bf. dem Haushalt ihrer Mutter M in Polen angehört, hat gemäß § 2 Abs. 2  Satz 1 FLAG 1967 daher die Mutter den vorrangigen Anspruch auf die österreichischen  Familienleistungen (Familienbeihilfe und Kinderabsetzbetrag) (vgl. auch BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_390`)


Der Familienleistungsanspruch des in Österreich wohnhaften Elternteils (hier: des leiblichen  Vaters) wird nach § 2 Abs. 2 Satz 1 FLAG 1967 i. V. m.  Art. 67 VO 883/2004 und  Art. 60 Abs. 1 Satz 2 VO 987/2009 durch den vorrangigen Familienleistungsanspruch des in  einem anderen Mitgliedstaat der Union (des EWR oder in der Schweiz) mit dem Kind im  gemeinsamen Haushalt lebenden Elternteils (hier: der Mutter) verdrängt  (vgl. BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/135135.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135135.1_39`)


Sie ist dann anzunehmen, wenn objektiv ein Zusammenhang mit dem Beruf  besteht und subjektiv die Aufwendungen zur Förderung des Berufes, nämlich zur Erwerbung,  Sicherung und Erhaltung von Einnahmen im Rahmen der Einkunftsart gemacht werden (vgl.  BFH 28.11.1980, BStBl 1981 II 368).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_164`)


Nach dem Urteil des BFH vom 29.01.2015 V R 5/14 sei Schuldner der Einfuhrumsatzsteuer die  Person, die in eigenem Namen die Zollanmeldung abgibt oder in deren Namen eine  Zollanmeldung abgegeben wird.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_332`)


Die TNT hat jedoch nicht für Rechnung der Empfänger gehandelt, weil die zollrechtliche  Abwicklung unabhängig von der Befreiung von der Einfuhrumsatzsteuer durch die Übernahme  aller etwaig anfallenden Steuern und sonstiger Kosten durch die Beschwerdeführerin unter  keinem denkbaren Gesichtspunkt für die Empfänger wirtschaftliche Auswirkungen haben  konnte (siehe BFH Urteil vom 29.01.2015, V R 5/14 und BFH Urteil vom 16.06.2021, XI R  17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_344`)


Auf Grund der Klausel im Punkt 4.9 der AVB, dass die Beschwerdeführerin sämtliche Abgaben  und Gebühren betreffend die Einfuhr übernehmen werde, ist die Bevollmächtigung der  Beschwerdeführerin zur Einfuhr im Namen der Empfänger unwirksam (siehe BFH Urteil vom  29.01.2015, V R 5/14 und BFH Urteil vom 16.06.2021, XI R 17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_346`)


Der Beschwerdeführerin und folglich der TNT als Subunternehmerin, fehlt es nämlich an dem  für die allein in Betracht kommende direkte Vertretung zollrechtlich erforderlichen Handelns  für Rechnung eines anderen (Art. 5 Abs. 2 Teilstrich 1. ZK), da die Bf. sämtliche Abgaben und  Gebühren zu tragen hat (siehe auch BFH vom 29.01.2015, V R 5/14, vom 16.06.2015, XI R  17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_101`)


Sowohl  der Nachweis von Gelegenheiten zum Abschluss eines Vertrages als auch die Kontaktaufnahme  mit der anderen Partei oder das Verhandeln über die Einzelheiten der gegenseitigen Leistungen  setzen voraus, dass sich die Mittlertätigkeit auf ein einzelnes Geschäft, das vermittelt werden  soll, bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_105`)


Dies gilt jedoch nach der EuGH-Rechtsprechung nur, wenn es sich  bei der einzelnen Leistung um ein im Großen und Ganzen eigenständiges Ganzes handelt, das  die spezifischen und wesentlichen Funktionen der Vermittlung erfüllt. Da somit auch Leistungen  im Rahmen einer arbeitsteiligen Vermittlung als eigenständiges Ganzes die spezifischen und  wesentlichen Funktionen der Vermittlung erfüllen müssen, sind sie nur steuerfrei, wenn der  jeweilige Vermittler eine Mittlertätigkeit ausübt, die sich auf einzelne Wertpapier- oder  Anteilsumsätze bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_91`)


Denn eine Betriebsprüfung bei einem  Abgabepflichtigen wird nicht allein und eigens mit dem Ziel durchgeführt werden können, hier  die Verhältnisse Dritter zu erforschen (Stoll, BAO-Kommentar, § 147, unter Verweis auf die  Judikatur des (dt.) BFH).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_48`)


Auch nach  Doralt/Kirchmayr/Mayr/Zorn, EStG14, § 6, Tz 279, sind Fremdwährungsverbindlichkeiten  grundsätzlich mit dem Rückzahlungsbetrag anzusetzen, der sich aus dem Kurs im Zeitpunkt der  Darlehensaufnahme ergibt (BFH 23.4.2009 - IV R 62/06).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_69`)


Auch nach  Doralt/Kirchmayr/Mayr/Zorn, ESt 14, § 6, Tz 279, sind Fremdwährungsverbindlichkeiten  grundsätzlich mit dem Rückzahlungsbetrag anzusetzen, der sich aus dem Kurs im Zeitpunkt der  Darlehensaufnahme ergibt (BFH 23.4.2009 - IV R 62/06).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/139828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139828.1_22`)


Eine außergewöhnliche Belastung auf Grund  sittlicher Verpflichtung zur Übernahme von Begräbniskosten sei nicht ausgeschlossen (BFH  24.7.87, III R 208/82, BStBl II 87, 715), allerdings auf Fälle nicht bestehender bzw. nicht  durchsetzbarer Erstattungsansprüche beschränkt, zB bei Begräbniskosten für einen  vermögenslosen Lebensgefährten oder für einen vermögenslosen ehemaligen Ehegatten (BFG  15.4.15, RV/5100610/2013);

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_116`)


Medizinisch indiziert sei jedes diagnostische oder therapeutische Verfahren, dessen  Anwendung in einem Erkrankungsfall hinreichend gerechtfertigt sei, es sei denn, es liege ein  für jedermann offensichtliches Missverhältnis zwischen dem erforderlichen und dem  tatsächlichen Aufwand vor (vgl BFH 12.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_129`)


Als konkrete Rechercheergebnisse wurden dem Amtsvertreter mitgeteilt:  Im Doralt-Kommentar (§ 34 Tz 78) werde dazu ausgeführt: „Werden Aufwendungen ihrer  Natur nach nicht ausschließlich von Kranken, sondern mitunter auch von Gesunden getätigt,  um ihre Gesundheit zu erhalten, ihr Wohlbefinden zu steigern oder ihre Freizeit sinnvoll zu  gestalten, ist nach dem zum Besuch eines Fitnessstudios ergangenen Erk VwGH 4.9.2014,  2012/15/0136, ein sog „vorfeldweises“ ärztliches Gutachten erforderlich, um die  Zwangsläufigkeit dieser Kosten zu begründen (Verweis auf BFH 14.8.1997, III R 67/96, BStBl II  1997, 732, zu Aufwendungen für eine „medizinische Trainingstherapie“ in einem ärztlich  betreuten Sportstudio).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_131`)


An einem  „formalisierten Nachweisverlangen“ in Form eines vorfeldweisen Gutachtens hielt der BFH  wegen eines Widerspruchs zum Grundsatz der freien Beweiswürdigung auch nicht mehr fest  (zB BFH 11.11.2010, VI R 17/09, BStBl II 2011, 969; vgl zur Rechtsentwicklung in Deutschland –  auch zu einer nachfolgenden legistischen Einführung formalisierter Nachweiserfordernisse  durch das StVereinfG 2011, BStBl I 2011, 986, in § 64 Abs 1 Nr 1 ESt- Durchführungs¬verordnung – zB Schmidt/Loschelder, EStG, § 33 Rz 33f; zum Abzug von  8 von 30 Seite 9 von 30

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_132`)


Krankheits¬kosten als außergewöhnliche Belastung vgl bspw BFH 25.4.2017, VIII R 52/13, DStR  2017, 1693).“

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_324`)


Im Doralt-Kommentar (§ 34 Tz 78) werde dazu ausgeführt: „Werden Aufwendungen ihrer  Natur nach nicht ausschließlich von Kranken, sondern mitunter auch von Gesunden getätigt,  um ihre Gesundheit zu erhalten, ihr Wohlbefinden zu steigern oder ihre Freizeit sinnvoll zu  gestalten, ist nach dem zum Besuch eines Fitnessstudios ergangenen Erk VwGH 4.9.2014,  2012/15/0136, ein sog „vorfeldweises“ ärztliches Gutachten erforderlich, um die  Zwangsläufigkeit dieser Kosten zu begründen (Verweis auf BFH 14.8.1997, III R 67/96, BStBl II  1997, 732, zu Aufwendungen für eine „medizinische Trainingstherapie“ in einem ärztlich  betreuten Sportstudio).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_326`)


An einem  „formalisierten Nachweisverlangen“ in Form eines vorfeldweisen Gutachtens hielt der BFH  wegen eines Widerspruchs zum Grundsatz der freien Beweiswürdigung auch nicht mehr fest  (zB BFH 11.11.2010, VI R 17/09, BStBl II 2011, 969; vgl zur Rechtsentwicklung in Deutschland –  auch zu einer nachfolgenden legistischen Einführung formalisierter Nachweiserfordernisse  durch das StVereinfG 2011, BStBl I 2011, 986, in § 64 Abs 1 Nr 1 ESt- Durchführungs¬verordnung – zB Schmidt/Loschelder, EStG, § 33 Rz 33f; zum Abzug von  Krankheits¬kosten als außergewöhnliche Belastung vgl bspw BFH 25.4.2017, VIII R 52/13, DStR  2017, 1693).“  VwGH vom 22. Dezember 2004, 2001/15/0116, betraf eine Kur: An den - vom Steuerpflichtigen  zu führenden - Nachweis dieser Voraussetzungen müssen wegen der im allgemeinen  schwierigen Abgrenzung solcher Reisen von den ebenfalls der Gesundheit dienenden  Erholungsreisen strenge Anforderungen gestellt werden (vgl. das hg.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_360`)


Abschließend sei auf einige –wenn auch nicht verbindliche, so doch interessante-  Ausführungen des deutschen BFH in seinem Urteil vom 12.5.2011, VI R 37/10 (bei gleicher  Rechtslage wie in Österreich) hingewiesen:   Für die mitunter schwierige Trennung von echten Krankheitskosten einerseits und lediglich  gesundheitsfördernden Vorbeuge- oder Folgekosten andererseits forderte der BFH bislang  regelmäßig die Vorlage eines zeitlich vor der Leistung von Aufwendungen erstellten amts- oder  vertrauensärztlichen Gutachtens bzw. eines Attestes eines anderen öffentlich-rechtlichen  Trägers, aus dem sich die Krankheit und die medizinische Indikation der den Aufwendungen  zugrundeliegenden Behandlung zweifelsfrei entnehmen lässt.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_361`)


Auch bei Aufwendungen für  Maßnahmen, die ihrer Art nach nicht eindeutig nur der Heilung oder Linderung einer Krankheit  dienen können und deren medizinische Indikation deshalb schwer zu beurteilen ist, verlangte  der BFH diesen formalisierten Nachweis.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_378`)


Zur Höhe des Aufwandes  Wanke in Wiesner u.a EStG Anm 78 zu § 34: Zur Heilbehandlung medizinisch indiziert ist jedes  diagnostische oder therapeutische Verfahren, dessen Anwendung in einem Erkrankungsfall  hinreichend gerechtfertigt ist, es sei denn, es liegt ein für jedermann offensichtliches  Missverhältnis zwischen dem erforderlichen und dem tatsächlichen Aufwand vor (vgl BFH 12.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_380`)


Aufwendungen außerhalb der eigentlichen Heilbehandlung sind  jedoch auf Notwendigkeit und Angemessenheit hin zu untersuchen (vgl BFH 30.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_423`)


Zieht man die Definition des deutschen BFH für das Vorliegen einer medizinischen Indikation  („einer angezeigten Behandlung“) heran, liegt diese bei jedem diagnostischen oder  therapeutischen Verfahren, dessen Anwendung in einem Erkrankungsfall hinreichend  gerechtfertigt (angezeigt) ist, vor.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_130`)


Der Verwaltungsgerichtshof hat im Übrigen in dem von der steuerlichen Vertretung im  Schreiben vom 28.04.2016 angeführten Erkenntnis vom 27.11.2014, 2012/15/0002, in dem der  Verwaltungsgerichtshof einen Anrechnungsvortrag ausländischer Quellensteuern nach der  österreichischen Rechtslage verneint hat, auch auf das Urteil des BFH vom 26. Oktober 1972, I  R 125/70, hingewiesen, wonach Anrechnungsüberhänge auch nicht über Billigkeitsmaßnahmen  berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_131`)


Dieser Rechtsprechung hat der BFH in seinem Urteil 26. Oktober 1972  vorangestellt, dass auch nach Bruttoentgelten (konkret: Bruttofrachteinnahmen) bemessene  ausländische Steuern, bezüglich welcher im Ausland verlustbringende Tätigkeiten vorliegen,  die ausländischen Steuern bei der Einkommensermittlung gemäß § 12 Nr. 2 KStG nicht  abziehbar sind (BFH 26.10.1972, I R 125/70, Rz 15f).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/143327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143327.1_43`)


Die Zurechnung von passiven Einkünften (also insbesondere  auch solchen aus Kapitalvermögen) erfolgt grundsätzlich an denjenigen, der das  (wirtschaftliche) Eigentum an den die Einkünfte generierenden Vermögenswerten hat (vgl. in  diesem Sinne Lechner, Überlegungen zur Einkünftezurechnung an ausländische Stiftungen, in FS  Tanzer, Wien 2014, 156, Hammer, Ausländische Stiftungen und vergleichbare Strukturen im  österreichischen Steuerrecht, Wien 2012, 72, sowie das Urteil des BFH vom 22. Dezember 2010,  I R 84/09, DStR 16/2011,755).“

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/145403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145403.1_10`)


Darauf beantragte der BF durch seinen ausgewiesenen Vertreter fristgerecht die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht und verwies in diesem  Vorlageantrag zur rechtlichen Begründung auf den vom Vertreter des BF in der SWK 18/2017,  Seite 838 (stufenweise Ermittlung des Selbstbehaltes nach § 34 Abs. 4 EStG) verfassten  Fachartikel, in dem er aufgrund einer Entscheidung des BFH zur (stufenweisen) Berechnung  des Selbstbehaltes bei außergewöhnlichen Belastungen nach § 33 Abs. 3 dEStG die Meinung  vertrat, dass die Argumente, des BFH im Urteil vom 19.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/145403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145403.1_32`)


Dazu verweist der Vertreter auf einen von  ihm veröffentlichten Fachartikel, in dem er eine Entscheidung des BFH zu § 33 Abs. 3 dEStG,  der den Wortlaut der Vorschrift für die Anwendung eines bestimmten Prozentsatzes des  Gesamtbetrags der Einkünfte gerade nicht auf den „gesamten Gesamtbetrag der Einkünfte“  abstelle, sondern … sich der gesetzlich festgelegte Prozentsatz nur auf den Gesamtbetrag der  Einkünfte in der Spalte der Tabelle beziehe, in der sich auch die jeweilige Prozentzahl befinde.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/145809.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145809.1_156`)


Diese können, einmal eingetreten, nicht ungeschehen gemacht werden (so schon  BFH 17.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_143`)


Die nach Art. 67 VO  883/2004 i. V. m. Art. 60 Abs. 1 Satz 2 VO 987/2009 vorzunehmende Fiktion bewirkt, dass die  Wohnsituation auf Grundlage der im Streitzeitraum im anderen EU-Mitgliedstaat gegebenen  Verhältnisse (fiktiv) ins Inland übertragen wird (BFH 10.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_145`)


Diese Fiktion führt  dazu, dass der Anspruch auf Familienleistungen des Beschäftigungsstaates nicht dem im für  Familienleistungen zuständigen Mitgliedstaat, sondern dem in einem anderen Staat der EU  (des EWR, der Schweiz) lebenden (Groß-)Elternteil zusteht, wenn dieser das Kind in seinen  Haushalt aufgenommen hat (vgl. BFH 4. 2. 2016, III R 17/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_146`)


BFH 21. 7. 2016, V R 46/11 u.a.).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_153`)


i VO 883/2004) gemäß § 2 Abs. 2 FLAG 1967 i. V. m. § 2 Abs. 3 FLAG  1967 jedenfalls das Kind, die Mutter und die Großeltern (Großvater sowie Großmutter)   anzusehen (vgl. auch BFH 10.3.2016, III R 62/12, oder BFG 15.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/146973.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146973.1_52`)


Welcher Anteil der Tätigkeit in Österreich ausgeübt wird, ergibt sich bei einem im  internationalen Fernverkehr tätigen LKW-Fahrer aus folgenden Überlegungen:  Berufskraftfahrer halten sich während der Arbeitsausübung in oder bei ihrem Fahrzeug auf  (s BFH 31.3.2004, BStBl II S 936).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_53`)


für eine konkret ausgeübte Tätigkeit, sondern für den Verlust des Arbeitsplatzes gezahlt. Ein  solcher bloßer Anlasszusammenhang genüge, wie der BFH zu der insoweit gleich lautenden  Bestimmung im Doppelbesteuerungsabkommen Deutschland-Schweiz judiziert habe, nicht, um  Deutschland als Tätigkeitsstaat das Besteuerungsrecht daran einzuräumen.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/147454.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147454.1_89`)


Die Verpflichtung des Erwerbers ist dann als  Gegenleistung anzusehen, wenn sie zum Übergang des Grundstücks in einer solchen  Wechselbeziehung steht, dass der Veräußerer ohne die Zahlungsverpflichtung des Erwerbers  das Grundstück nicht veräußert hätte und sich der Erwerber nur unter der Voraussetzung des  Kaufabschlusses zur Zahlung verpflichtet hat (BFH 15.6.1960, II 250/58 BStBl 1960/314; vgl.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/149096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149096.1_10`)


In der in der Beschwerdeschrift erwähnten Beilage, einem Fachartikel im SWK-Heft 18 vom  20.6.2017, verweist der Autor des Artikels auf ein Urteil des deutschen Bundesfinanzhofes  (BFH) vom 19.1.2017, VI R 75/14, zur Ermittlung der zumutbaren Belastung gemäß § 33 Abs. 3  deutsches EStG und kommt zum Schluss, dass diese Rechtsprechung auf die österreichische  Selbstbehaltsregelung des § 34 Abs. 4 EStG übertragbar sei.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/149096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149096.1_46`)


Soweit der BF auf eine geänderte Rechtsprechung des deutschen BFH zur deutschen  Rechtslage verweist und eine Übertragbarkeit dieser Rechtsprechung auf § 34 Abs. 4 EStG  sieht, wird ausgeführt: Wie dem BFH-Urteil vom 19.1.2017, VI R 75/14, unter RZ 18 zu  entnehmen ist, stellt die deutsche Rechtslage für die Anwendung eines bestimmten  „Selbstbehaltsprozentsatzes" nicht auf den „gesamten Gesamtbetrag der Einkünfte" ab,  sondern bezieht sich der gesetzlich festgelegte Prozentsatz nur auf den Gesamtbetrag der  Einkünfte in der Spalte der Tabelle des § 33 Abs. 3 Satz 1 des deutschen EStG, in der sich auch  die jeweilige Prozentzahl befindet.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/149254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149254.1_18`)


II. Homöopathie und Nahrungsergänzungsmittel  Kosten für alternative Behandlungstherapien (zB Homöopathie) stellen eine außergewöhnliche  Belastung dar, wenn ihre durch die Krankheit bzw Behinderung bedingte Zwangsläufigkeit und  Notwendigkeit mittels ärztlicher Verordnung eines zur Heilkunde zugelassenen Mediziners  nachgewiesen wird (Fuchs in Doralt/Kirchmayr/Mayr/Zorn, EStG25 § 34 Rz 78  „Alternativmedizinische Behandlung“ [Stand 1.1.2025, rdb.at] mit Verweis auf Rechtsprechung  des BFH;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_98`)


2001, I-10237,  BFH/NV Beilage 2002, 35, UR 2002, 84, und Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617  die Vermittlung darin, das Erforderliche zu tun, damit zwei Parteien einen Vertrag über das  jeweilige Finanzprodukt abschließen.

**False Positives:**

- `BFH` — no gold match — likely missing annotation
- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_101`)


Sowohl  der Nachweis von Gelegenheiten zum Abschluss eines Vertrages als auch die Kontaktaufnahme  mit der anderen Partei oder das Verhandeln über die Einzelheiten der gegenseitigen Leistungen  setzen voraus, dass sich die Mittlertätigkeit auf ein einzelnes Geschäft, das vermittelt werden  soll, bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

**False Positives:**

- `BFH` — similar text (different position): `BFH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_102`)


Auch aus der Freiheit des Organisationsmodells (EuGH-Urteil Ludwig in BFH/NV Beilage 2007,  398, UR 2007, 617 Randnrn.

**False Positives:**

- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_105`)


Dies gilt jedoch nach der EuGH-Rechtsprechung nur, wenn es sich  bei der einzelnen Leistung um ein im Großen und Ganzen eigenständiges Ganzes handelt, das  die spezifischen und wesentlichen Funktionen der Vermittlung erfüllt. Da somit auch Leistungen  im Rahmen einer arbeitsteiligen Vermittlung als eigenständiges Ganzes die spezifischen und  wesentlichen Funktionen der Vermittlung erfüllen müssen, sind sie nur steuerfrei, wenn der  jeweilige Vermittler eine Mittlertätigkeit ausübt, die sich auf einzelne Wertpapier- oder  Anteilsumsätze bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

**False Positives:**

- `BFH` — similar text (different position): `BFH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_106`)


Dementsprechend  bejaht der EuGH im Urteil Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617 die Steuerfreiheit,  wenn ein Untervermittler verbindliche Vertragsangebote einzelner Interessenten einholt und  diese an den Hauptvermittler übermittelt, der sie dann nach eigener Kontrolle an das  Finanzinstitut weiterleitet (EuGH-Urteil Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617  Rdnr. 10).

**False Positives:**

- `BFH` — no gold match — likely missing annotation
- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Wiener_Gemeinderates_entities` 💣

**F1:** 0.017 | **Precision:** 0.915 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `bbf7ace8`  
**Description:**
Matches 'Wiener Gemeinderates' which was previously missed.

**Content:**
```
\bWiener\s+Gemeinderates\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.915 | 0.008 | 0.017 | 59 | 54 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 54 | 5 | 5902 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_18`)


Fassung, hat der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines  mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges  überlässt, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine  Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBI. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBI. l Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_49`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_54`)


Dieses wird durch die  Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird  (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_58`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_14`)


Grundsätzlich darf darauf hingewiesen werden, dass die unmittelbar aufeinander folgende  Aktivierung von elektronischen Parkscheinen mit einer fünfzehn Minuten nicht übersteigenden  Abstellzeit oder die Kombination der Aktivierung eines fünfzehn Minuten nicht übersteigenden  elektronischen Parkscheines mit einem Parkschein gemäß § 2 Abs. 1 und 2 in zeitlich  unmittelbarer Aufeinanderfolge unzulässig ist (§ 9 Abs. 2 der Kontrolleinrichtungenverordnung  des Wiener Gemeinderates vom 14.08.2008, ABl. der Stadt Wien Nr. 33/2008, in der  geltenden  Fassung)…"  2 von 20 Seite 3 von 20

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Missed by this rule (FN):**

- `Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_145`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_148`)


Dieses wird durch die Verordnung des Wiener Gemeinderates, mit der  für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer  Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_62`)


Gemäß § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_58`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_82`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_87`)


Dieses wird durch die  Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahr- zeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird (Parkometer- abgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_113`)


Im Amtsblatt der Stadt Wien vom 18. Juli 2013, Nr. 29, Seite 5f, wurde eine Verordnung des  Wiener Gemeinderates, mit welcher u.a. die Parkometerabgabeverordnung und die Kontroll- einrichtungenverordnung geändert wurden, verlautbart.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Missed by this rule (FN):**

- `Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_47`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_48`)


Zur Begründung wurde nach Wiedergabe des Verwaltungsgeschehens und unter Hinweis auf  den Einspruch des Bf. gegen die verfahrensleitende Strafverfügung vom 19. Februar 2021  Folgendes ausgeführt:  Gemäß § 2 Abs. 1 Parkometergesetz habe der Zulassungsbesitzer und jeder, der einem Dritten  das Lenken eines mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen  Kraftfahrzeuges überlasse, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates  eine Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBl. I Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt habe.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_115`)


§ 2 Wiener Parkometergesetz 2006 normiert:  „(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_46`)


Gemäß § 3 Abs. 1 Verordnung des Wiener Gemeinderates über die Art der zu verwendenden  Kontrolleinrichtungen in Kurzparkzonen (Kontrolleinrichtungenverordnung) haben Abgabe- pflichtige, die ein mehrspuriges Kraftfahrzeug in einer Kurzparkzone abstellen, dafür zu sorgen,  dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und richtig  entwerteten Parkschein gekennzeichnet ist.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_47`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- 4 von 11 Seite 5 von 11

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_83`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_87`)


In § 2 der Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung) sind die für einen bestimmten Zeitraum zu  entrichtenden Beträge festgelegt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/136576.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136576.1_55`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136598.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136598.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- 4 von 8 Seite 5 von 8

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/136998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136998.1_49`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_68`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_43`)


E) Das Verwaltungsgericht Wien beraumte zunächst eine mündliche Verhandlung über die  Beschwerde für den 17.11.2020 an, welche mit Schreiben des Verwaltungsgerichtes Wien vom  16.11.2020 wieder abberaumt wurde, und zwar mit folgender Begründung: „Der  gegenständliche Akt wird im Hinblick darauf, dass die Beschwerde sich gegen die Verweigerung  der Rückzahlung der pauschalierten Parkometerabgabe gemäß Wr. Parkometergesetz 2006  iVm der VO des Wiener Gemeinderates über die pauschale Entrichtung der Parkometerabgabe  (PauschaIierungsverordnung) richtet, gemäß § 6 AVG an das Bundesfinanzgericht  weitergeleitet und abgetreten.“  F) Die gegenständliche Beschwerde vom 8. Juli 2020 langte beim Bundesfinanzgericht ein.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Missed by this rule (FN):**

- `Verwaltungsgericht Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_74`)


Die gegenständliche Angelegenheit basiert nicht auf den Regelungen des § 7 der  Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung) betreffend „Vereinbarungen“.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_98`)


2005/51 idgF,   die Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung), ABl.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_100`)


§ 2 Abs. 1 der Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung): „Die Parkometerabgabe ist bei pauschaler  Entrichtung mit folgenden Beträgen vorzuschreiben:  a) Für Inhaber bzw. Inhaberinnen von Ausnahmebewilligungen gemäß § 45 Abs. 4 StVO 1960 in  dem jeweils gemäß § 43 Abs. 2a Z. 1 StVO 1960 zur Abstellung von Kraftfahrzeugen  verordneten Gebiet für ein Jahr mit 120 Euro, …“  Aus all dem folgt, dass die Parkometerabgabe eine Gemeindeabgabe ist und es sich bei ihr um  eine öffentlich-rechtlich (hoheitlich) zu vollziehende Angelegenheit handelt. Über den  verfahrensgegenständliche Antrag auf Festsetzung und Rückzahlung ist daher mit  verwaltungsbehördlichem Bescheid und allenfalls durch Erkenntnis des zuständigen  Verwaltungsgerichtes zu entscheiden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/138030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138030.1_58`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/138648.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138648.1_67`)


Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß §  25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_34`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/139274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139274.1_49`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/139288.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139288.1_37`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/139689.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139689.1_66`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/139974.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139974.1_67`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_85`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/140597.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140597.1_48`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/140939.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140939.1_66`)


In § 2 Wiener Parkometergesetz 2006 ist angeordnet:  "(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  5 von 11 Seite 6 von 11

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/141691.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141691.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_73`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/143180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143180.1_74`)


Rechtsgrundlage und Würdigung  § 2 Wiener Parkometergesetz 2006 normiert:  "(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/143904.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143904.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/144091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144091.1_59`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_50`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/145249.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145249.1_84`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_76`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_80`)


§ 4. Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung):   (1) Wird die Abgabe in pauschaler Form (§ 2 und § 3 Abs. 1) entrichtet, hat dies durch  Einzahlung des Abgabenbetrages in bar oder nach Maßgabe der der Abgabenbehörde zur  Verfügung stehenden technischen Mittel im bargeldlosen Zahlungsverkehr zu erfolgen.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_8`)


Die Vorschreibung erfolgte gemäß § 203 BAO iVm § 1 Abs. 4 und 5 Parkometergesetz 2006 bzw  §§ 2 und 5 Abs. 2 Parkometerabgabeverordnung des Wiener Gemeinderates.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_10`)


Gemäß § 5 Abs.  2 der Parkometerabgabeverordnung des Wiener Gemeinderates, ABI. für Wien Nr. 51/2005, in  der jeweils gültigen Fassung, ist für jedes mehrspurige Kraftfahrzeug, das in einem Gebiet  abgestellt wird, für das eine Abgabepflicht besteht, bei Beginn des Abstellens eine Abgabe zu  entrichten.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_37`)


Gemäß § 5 Abs. 2 der  Parkometerabgabeverordnung des Wiener Gemeinderates entsteht die Abgabepflicht bereits  bei Beginn des Abstellens.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_39`)


Gemäß § 5 Abs. 2 der Parkometerabgabeverordnung des Wiener Gemeinderates, ABl. für Wien  Nr. 51/2005, in der geltenden Fassung, sind zur Entrichtung der Abgabe der Lenker, der Besitzer  und der Zulassungsbesitzer zur ungeteilten Hand verpflichtet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_63`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_90`)


dauernd ausschließlicher Nutzer eines Kraftfahrzeugs ist, der nachweist, dass er ein  Dauerschuldverhältnis (insbesondere Leasingvertrag oder Mietvertrag) über einen Zeitraum  von mindestens 4 Monaten hat oder nachweist, dass ihm ein arbeitgebereigenes oder von  seinem Arbeitgeber geleastes Kraftfahrzeug zur Privatnutzung überlassen wird.“  § 4 Abs 1 und 2 der Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung) normiert [Hervorhebungen durch das  Gericht]:  „(1) Wird die Abgabe in pauschaler Form (§ 2 und § 3 Abs. 1) entrichtet, hat dies durch  Einzahlung des Abgabenbetrages in bar oder nach Maßgabe der der Abgabenbehörde zur  Verfügung stehenden technischen Mittel im bargeldlosen Zahlungsverkehr zu erfolgen.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/149088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149088.1_79`)


Rechtsgrundlagen und Würdigung:  § 2 Wiener Parkometergesetz 2006 lautet:    "(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_114`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), sind  Parkscheine nach dem Muster der Anlagen oder elektronische Parkscheine zu verwenden (§ 1  Wiener Kontrolleinrichtungenverordnung).

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/140939.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140939.1_65`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), sind  Parkscheine nach dem Muster der Anlagen oder elektronische Parkscheine zu verwenden (§ 1  Wiener Kontrolleinrichtungenverordnung).

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_236`)


Gemäß § 12 und § 18 GrStG sowie gemäß § 192, § 194 Abs. 3 und § 195 BAO sowie gemäß § 8  des Wiener Grundsteuerbefreiungsgesetzes sowie gemäß der Verordnung des Wiener  Gemeinderates (ABl 1994/07, 7.2.1994), mit der der Hebesatz für die Grundsteuer festgesetzt  wird, ist die Grundsteuer für die gegenständliche Liegenschaft mit einem Jahresbetrag von  82,79 € aufgrund folgender Bemessungsgrundlagen vorzuschreiben:   Grundsteuermessbetrag in Höhe von 165,92 €,   Hebesatz im Ausmaß von 500 vom Hundert (=500%) sowie   die Befreiung von der Grundsteuer im Ausmaß von 90,02%.

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_139`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird, sind Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung, des Wiener  Gemeinderates über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABI Nr 2013/29).

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation
- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Finanzamtes_standalone` 💣

**F1:** 0.158 | **Precision:** 0.848 | **Recall:** 0.087  

**Format:** `regex`  
**Rule ID:** `1200be7b`  
**Description:**
Matches standalone 'Finanzamtes' (genitive) only when preceded by a preposition or at sentence start, reducing false positives.

**Content:**
```
(?:des|vom|von|bei|an|f\u00fcr|\s|^)(Finanzamtes)(?!\s+(?:f\u00fcr\s+Gro\u00dfbetriebe|Innsbruck|\u00d6sterreich|Baden|Graz|Wien|Braunau|Neunkirchen|Waldviertel|Bregenz|Salzburg|Judenburg|Kirchdorf|Bruck|Steiermark|Klosterneuburg|Eisenstadt|Grieskirchen))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.848 | 0.087 | 0.158 | 659 | 559 | 100 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 559 | 100 | 5853 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_51`)


Ein Widerspruch, den aufzuklären Aufgabe des Finanzamtes gewesen wäre und der auch Zweifel an der Qualität der Begutachtungen und Bescheinigungen hervorruft.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Florenzia Claußing` (person)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich` (address)
- `10-95-558/8694` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_65`)


In der dagegen rechtzeitig erhobenen Berufung wird im Wesentlichen eingewendet,  hinsichtlich der nun erstmaligen Festsetzung der Umsatzsteuer für August 2005 sei bereits mit  31. Dezember 2008 Verjährung eingetreten, da die Umsatzsteuer als Verkehrssteuer nach drei  Jahren verjähre und keine entsprechenden Verlängerungshandlungen (erkennbare  Amtshandlungen) seitens des Finanzamtes gesetzt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_73`)


Feststellungen des Finanzamtes, dass der Bf das Fahrzeug als neues Fahrzeug erworben habe  und wann dieses nach Österreich verbracht worden sei, fehlten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_132`)


Laut Erhebungen des Finanzamtes zu dem an der inländischen Wohnadresse abgestellten  Fahrzeug hatte sich der Bf im Zeitraum vom 1. bis 12. Februar 2007 an 7 Tagen zu  unterschiedlichsten Zeiten am Familienwohnsitz aufgehalten (Mitteilung der Steuerfahndung  vom 27.3.2007).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Klarissa Kümml` (person)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_31`)


Mit Schreiben vom 18.12.2018 nahm die Beschwerdeführerin zum Ergänzungsersuchen des  Finanzamtes vom 05.12.2018 wie folgt Stellung: Es sei Zeit gewesen, aus 151 Kassazetteln  einzelne Posten herauszulesen und zu hinterfragen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_40`)


Die Beschwerdeführerin werde niemals zu einem Arzt gehen, um ihn befinden zu lassen, ob die  einzelnen Medikamente und Lebensmittel, die seitens des Finanzamtes in Frage gestellt  würden, mit ihrer Behinderung in Zusammenhang stünden oder nicht.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_124`)


In Zusammenhang mit den geltend Kosten in Höhe von 836,94 € für Medikamente,  Rezeptgebühren, Behandlungskosten und Arzthonoraren ist in Ergänzung der Ausführungen  des Finanzamtes Folgendes auszuführen:   Gemäß § 4 der VO für außergewöhnliche Belastungen sind Kosten der Heilbehandlung im  nachgewiesene Ausmaß ohne Selbstbehalt zu berücksichtigen, sofern sie mit der Behinderung  in Zusammenhang stehen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_47`)


Zum weiteren Vorhalt, dass aus den vorgelegten Einbringungsakten  des FA nicht ersichtlich sei, welcher KöSt Bescheid dem Haftungsbescheid beigelegt wurde, da  überhaupt keine Kopien vorhanden sind, führte der Vertreter des Finanzamtes aus, dass dies  für ihn nicht mehr nachvollziehbar ist.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_16`)


In der Begründung wurde ausgeführt, dass  die 4-wöchige Frist dem BF bewusst gewesen sei und er deshalb telefonisch beim Finanzamt  um eine 1-wöchige Verlängerung gebeten und diese auch telefonisch von einem Mitarbeiter  des Finanzamtes bewilligt bekommen habe.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_20`)


Mit Postaufgabedatum 25.11.2019 brachte der BF eine Beschwerde gegen den  Einkommensteuerbescheid 2018 ein, welche mit Beschwerdevorentscheidung des Finanzamtes  vom 06.02.2020 als verspätet zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_25`)


Ob eine vom BF behauptete telefonische  Verlängerung der Beschwerdefrist durch einen Mitarbeiter des Finanzamtes stattgefunden hat,  ist aus den unter „4. Rechtliche Beurteilung“ angeführten Gründen nicht relevant.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_99`)


Eine in der Begründung einer Beschwerdevorentscheidung getroffene Feststellung des  Finanzamtes wirkt wie ein Vorhalt und es obliegt dem Abgabepflichtigen, die vom Finanzamt in  der Begründung der Beschwerdevorentscheidung getroffene Feststellung zu widerlegen bzw.  zumindest deren Unrichtigkeit zu behaupten (vgl. VwGH 8.10.1985, 83/14/0237 etc.).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Nadja Rossetto` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Imre & Schaffer Rechtsanwälte OG` (organisation)
- `85-716/2059` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_26`)


6. Wird der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liegt es im Ermessen des Finanzamtes, die Haftung für die unter Punkt 1 genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_90`)


Betreffend die weiteren Werbungskosten (Rechtsanwaltskosten, Kilometergeld, Arbeitsmittel)  schließt sich das Gericht der Ansicht des Finanzamtes an.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Streitpunkte:  Die Bf. lebt auch nach eigenen Angaben seit 3. Juli 2019 nicht mehr mit ihren Kindern in einem  gemeinsamen Haushalt. Ab 4.7.2019 war der Kindesvater an einer gemeinsamen Adresse mit  den Kindern gemeldet und lebte mit diesen unstrittig in einem gemeinsamen Haushalt. Die  Verständigung des Finanzamtes durch die Bf. erfolgte erst am 27.8.2019, als die  Familienbeihilfe bereits überwiesen worden war.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_69`)


Auf Ersuchen des Finanzamtes vom 28.April 2016 um Übersendung des Franchisevertrages  sowie Bekanntgabe der jährlichen Kosten der Versicherungen lt. Vertrag wurde dieser vom  Franchisegeber übermittelt.  Der Franchisevertrag legt in seinen Bestimmungen im Wesentlichen Folgendes dar:   "...   § 2 Gegenstand des Vertrages   Der Franchise-Geber gewährt dem Franchise-Nehmer das Recht,   a) das Restaurant laut Deckblatt in den vom Franchise-Nehmer mit gesondertem Vertrag  gepachteten Räumlichkeiten nach dem Firmen System zu betreiben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_29`)


Es werde ersucht, die Bescheide des  Finanzamtes zu ändern und im neuen Bescheid die beantragten Kosten zu berücksichtigen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_123`)


Im Unterschied zu einer vom Finanzamt auf der Grundlage der vom Gebührenschuldner  vorgelegten Vertragsmuster bewilligten Selbstberechnung gem § 3 Abs 4 GebG (vgl dazu VwGH  18.6.2002, 99/16/0354), beschränkt sich bei einer gemäß § 33 TP 5 Abs 5 Z 5 GebG erfolgten  Selbstberechnung der Bestandvertragsgebühren das Wissen des Finanzamtes nach der  Maßgabe der gemäß § 33 TP 5 Abs 5 Z 5 GebG iVm § 3 Abs 4a GebG vom Bestandgeber  geführten Aufschreibungen im Allgemeinen auf Angaben zur Art des Rechtsgeschäftes, zu den  Namen der Vertragspartei(en), zum Zeitpunkt des Entstehens der Gebührenschuld, zur Höhe  der Bemessungsgrundlage und zur Höhe der selbst berechneten Gebühr.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_124`)


Die erstmalige  Kenntniserlangung des Finanzamtes von dem der Selbstberechnung der  Bestandvertragsgebühren zugrunde gelegten Urkundeninhalt führt somit aus der Sicht des  Finanzamtes in der Regel zu einem Hervorkommen neuer Tatsachen iSd § 303 Abs 1 lit b BAO.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |
| `Finanzamtes` | `Finanzamtes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_35`)


Da sowohl die Höhe der vom Bf. für die Zeiträume vom 1.1.2013 bis zum 21.4.2013 und vom  9.7.2013 bis zum 31.12.2013 bezogenen zum laufenden Tarif zu versteuernden Einkünfte aus  nichtselbständiger Arbeit als auch jene der während des Bezuges des steuerfreien  Weiterbildungsgeldes bezogenen Arbeitseinkünfte weder im Lohnzettel des Bf. für das Jahr  2013 noch in den Akten des Finanzamtes und des BFG aufschien, wurde dem Finanzamt gemäß  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_69`)


Bereits im Vorjahr  (2008) wäre seitens des Finanzamtes die Anerkennung einer höheren AfA als 1,5% (cirka 67  Jahre RND) verweigert worden, wogegen jedoch kein Rechtsmittel erhoben worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_11`)


Im Zuge von Erhebungen (Auskunftsverlangen gemäß § 143 BAO) stellte ein Prüforgan des  Finanzamtes laut Niederschrift vom 2. Juli 2013 fest, dass die Bf hinsichtlich ihrer  internationalen Schachtelbeteiligung an der C-LIMITED-SIRKETI keine Optionserklärung zur  Steuerwirksamkeit gemäß § 10 Abs. 3 Z 1 KStG 1988 abgegeben hatte.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_47`)


Die unstrittigen Sachverhaltsfeststellungen gründen sich auf den Inhalt des vorgelegten Aktes  des Finanzamtes, die Urkundensammlung des Firmenbuchs sowie den elektronischen  Steuerakt.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_10`)


Auf Ersuchen des Finanzamtes wurde anschließend vom BFA der "Schriftverkehr zu dem Antrag  auf Akteneinsicht" des Bf übermittelt, woraus hervorgeht:  a) Mit e-mail vom 16.10.2018 hat der Bf beim BFA einen "Antrag auf Akteneinsicht" gestellt, da  er fremdenpolizeilich überprüft worden wäre, und führt ua. aus:   " … Bitte geben Sie mir eine vollständige Akteneinsicht zu meiner Person ….

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_20`)


Seitens des Finanzamtes wurde festgestellt, dass laut Dienstgeberabfrage im Jahr 2012 bei der  Firma T insgesamt 5 Dienstnehmer angemeldet waren (davon einige Angestellte und einige  geringfügig beschäftigte Arbeiter für jeweils einige Monate).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_59`)


Die Stellungnahme des Finanzamtes wurde zur Wahrung des Parteiengehörs dem Bf.  übermittelt.  Der Bf. erklärte ergänzend, dass nach seiner Ansicht im vorliegenden Fall Fremdleistungen an  seine Firma durch die Firma T zu beurteilen seinen und die Frage, ob der  Fremdleistungsaufwand der Firma T an deren Subfirmen Firma C und Firma Ch anzuerkennen  sei, im gegenständlichen Verfahren nicht relevant sei.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_65`)


Über die Beschwerde wurde erwogen:  Strittig ist im vorliegenden Fall, ob der Bf. dem Verlangen des Finanzamtes gemäß § 162 BAO  den Empfänger des in seiner Steuererklärung für 2012 im Rahmen der Einkünfte aus  Gewerbebetrieb als Betriebsausgaben für Fremdleistungen betreffend die Firma T abgesetzten  Betrages in Höhe von € 271.314,-  bekannt zu geben, entsprochen hat.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_89`)


Die Dienstgebersuche des Finanzamtes betreffend die Firma T ergab für das Jahr 2012, dass  fünf Dienstnehmer jeweils nur für Teile des Jahres (einige Monate)  beschäftigt waren, davon  ein Angestellter, ein Arbeiter und drei geringfügig Beschäftigte;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_92`)


Aus den vorliegenden Unterlagen des Finanzamtes betreffend Betriebsprüfung bei der Firma C  bzw. von Firmen an welche seitens dieser Firma Rechnungen gelegt wurden, ist ersichtlich,  7 von 12 Seite 8 von 12

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_125`)


Auch wenn im vorliegenden Fall von tatsächlichen Zahlungen an unbekannt gebliebene  Empfänger auszugehen ist, sind die Betriebsausgaben nicht anzuerkennen, weil der Bf. dem  Verlangen des Finanzamtes auf Empfängerbenennung gemäß § 162 BAO nicht entsprochen hat  (VwGH 15.9.99, 83/13/0156;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_147`)


Der Bf. hat den gemäß § 162 BAO erteilten  Auftrag des Finanzamtes den Erbringer der  Leistungen und Empfänger des als Betriebsausgaben beantragten Geldbetrages in Höhe von €  271.314,- zu benennen nicht erfüllt, sodass die Rechtsfolge der Nichtanerkennung der  Betriebsausgaben beim Bf. eintritt.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_18`)


Er sehe in der Vorgangsweise  des Finanzamtes eine Missachtung der nach § 115 Abs. 1 BAO vorgegebenen Pflicht, die  abgabepflichtigen Fälle zu erforschen und von Amts wegen die tatsächlichen und rechtlichen  Verhältnisse vermitteln.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_59`)


Er  bringt lediglich zum Ausdruck, dass das Finanzamt Werbungskosten und Betriebsausgaben in  einem höheren Ausmaß hätte berücksichtigen müssen, als dies in den angefochtenen  Bescheiden geschehen ist, bezweifelt aber nicht die Berechtigung des Finanzamtes, die  Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2011 und 2012 zu verfügen,  geht er doch selbst davon aus, dass er die von ihm geltend gemachten Werbungskosten und  Betriebsausgaben nicht in vollem Umfang belegen könne und diese daher mangels Vorlage von  Belegen zu schätzen seien.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_60`)


Damit ergab sich aber gemäß § 85 Abs. 2 BAO die Verpflichtung des Finanzamtes, den  Beschwerdeführer zur Behebung des seiner Beschwerde anhaftenden Mangels im Hinblick auf  die fehlende Begründung seiner Beschwerde gegen die Wiederaufnahmsbescheide  aufzufordern.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_27`)


Sie war daher bis zur Mitteilung des  Finanzamtes am 12. August 2019 überzeugt, die UVA für 05/2019 korrekt übermittelt zu  haben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_36`)


Im Vorlagebericht wurde seitens des zuständigen Finanzamtes nach Darstellung des  Sachverhalts und unter Verweis auf die gesetzlichen Bestimmungen die zur Festsetzung der  Zwangsstrafe führten u.a. wie folgt Stellung genommen:  „…  Die Bf. bestreitet im Rahmen der Beschwerde nicht, die Meldung gem. § 5 WiEReG nicht  fristgerecht vorgenommen zu haben, sondern beruft sich darauf, dass aufgrund der  (automatischen) Übernahme der Firmenbuchdaten ins WiEReg nur eine formale Meldung hätte  erfolgen können.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_255`)


Der Bescheid des Finanzamtes über die beantragte Forschungsprämie des Jahres 2012 erging  ebenfalls in Anwendung des § 201 BAO auf Grundlage des Bezug habenden (negativen)  Jahresgutachtens der FFG für 2012 sowie ihrer nachfolgenden Stellungnahme zu den  Wirtschaftsjahren 2011 und 2012.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_280`)


Die Bf. hat nach Vorhalten/Ergänzungsersuchen der Behörde vor Erlassung der bekämpften  Bescheide mit Eingaben vom 23. Mai 2014 bzw. 22. Oktober 2014 weitergehende  Ausführungen zu ihren Aktivitäten getätigt, die der FFG von Seiten des Finanzamtes im Zuge  einer ersten ergänzenden Anfrage übermittelt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_293`)


Das FFG erklärte in einer ‚Rückfrage zur Anfrage des Finanzamtes 1/23‘ vom 25. Oktober 2016,  dass die vom Finanzamt nachgeforderten Unterlagen eine nur sehr allgemeine Beschreibung  enthalten würden und ersuchte die Behörde zu den Probetrocknungen mit der Pilotanlage  sowie der großen Anlage konkrete Informationen von der Bf. einzufordern, mit denen auf von  ihr formulierte Fragestellungen u.zw.:   - Welche Probetrocknungen (Versuche) wurden im Detail mit welcher technischer Zielsetzung  jeweils durchgeführt?

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_300`)


Das Gesamtbild der Tätigkeit der ungarischen Gesellschafter der Bf sei daher nach  Ansicht des Finanzamtes ein Dienstverhältnis, das vorliege, wenn der Arbeitnehmer dem  Arbeitgeber seine Arbeitskraft schulde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_310`)


Die Argumente wären in der Folge ausführlich besprochen worden, seitens des Finanzamtes  wäre auf das Gesamtbild der Tätigkeiten der ungarischen Arbeitsgesellschafter hingewiesen  worden – verwiesen wurde dabei auf die Stellungnahme zur Berufung.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_313`)


Seitens des Finanzamtes wäre dieses  Ersuchen in der Berufungsvorlage angeführt worden, es wurde jedoch darauf hingewiesen,  dass dies im Ermessen des UFS läge, diese zu gewähren.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr. Alexander Nahler` (person)
- `Ljiljana Kos` (person)
- `Dr. Schmid` (person)
- `Klinik Favoriten` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_30`)


Da dies im gegenständlichen Fall nicht vorliege, sei nach Ansicht des  Finanzamtes die Beschwerde abzuweisen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_29`)


In dem vom Bf. unterzeichneten Antragsformular „Beih 1“ blieb das vorgesehene Feld, ab  wann die Familienbeihilfe/Differenzzahlung beantragt wird, bis auf das Wort „TajNur“  (bedeutet Versicherungsnummer in ungarischer Sprache) unausgefüllt. Dieses Antragsformular  langte laut Eingangsstempel am 27.4.2017 beim Finanzamtes Oberwart ein.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_12`)


Dagegen erhob die Bf. mit Schriftsatz vom 16.01.2020 Beschwerde und führte begründend aus,  dass die Begründung des Finanzamtes nicht rechtmäßig wäre, da der Bescheid keine genauen  Angaben betreffend entsprechende Gesetzesbestimmungen, die die Anstellung eines  Kommanditisten ausdrücklich verbieten, enthalten würden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_40`)


In der Stellungnahme des Finanzamtes vom 14.04.2020 führte dieses aus: „Es wird behauptet,  dass die Geschäftsführerin, die auch die Gattin des Arbeitnehmers und Kommanditisten ist,  ihren Gatten nicht geringfügig angestellt, sondern 35-40 Stunden die Woche beschäftigt habe.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_55`)


Mit Schreiben vom 19.05.2020 replizierte die Geschäftsführerin zunächst kritisch auf die  Stellungnahme des Finanzamtes vom 14.04.2020.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_69`)


Das Bundesfinanzgericht hat Einsicht genommen in die Datenbanken des Finanzamtes und des  Hauptverbandes der Sozialversicherungen sowie in das Firmenbuch.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_145`)


In der am 08.06.2020 abgeführten Senatsverhandlung führte der Amtsvertreter aus, dass aus  nunmehriger Sicht des Finanzamtes die GrundanteilV 2016 doch nicht per analogiam  anwendbar sei, zumal der Wert von GuB von den tatsächlichen Verhältnissen um zumindest 50  v.H. abweiche.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr. Björn Hüpscher` (person)
- `Igor Strunz` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)
- `Vedat Gökdemir` (person)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_33`)


Hier liege jedenfalls auch ein  gravierendes Versäumnis des Finanzamtes vor.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_44`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Der nachfolgend festgestellte Sachverhalt ergibt sich unstrittig aus dem vorgelegten  Verwaltungsakt, insbesondere aus den eigenen Angaben des Beschwerdeführers bzw den  unwidersprochen gebliebenen Ausführungen des Finanzamtes im bekämpften Bescheid.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_101`)


Das Erkenntnis des Bundesfinanzgerichtes vom 23.03.2017, RV/5101633/2016, entschied  hinsichtlich der Rechtsansicht des Finanzamtes, wonach für die Begründung der  Unzumutbarkeit der Verlegung des Familienwohnsitzes von Serbien nach Österreich aus  wirtschaftlichen Gründen wegen des Betreibens einer kleinen, der Eigenversorgung dienenden  Landwirtschaft am Familienwohnsitz zusätzlich auch das Vorhandensein von  unterhaltsberechtigten und betreuungsbedürftigen (= minderjährigen) Kindern am  Familienwohnsitz Voraussetzung sei, wie folgt:  Dem Erkenntnis zugrunde gelegter Sachverhalt

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_138`)


Im Vorlageantrag vom 9. März 2019 wurde aber auf die Ausführungen des  Finanzamtes insofern nicht reagiert, als keine Gegenargumente oder -behauptungen mit  allfälligen Nachweisen oder zumindest Glaubhaftmachung vorgebracht wurden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_29`)


In einer Stellungnahme zum Vorlagebericht wurde von Seiten des Finanzamtes ausgeführt: Das  beantragte Pendlerpauschale sowie der Pendlereuro seien in den  Beschwerdevorentscheidungen berücksichtigt worden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Gudrun Sochurek` (person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Mag. Rupert Karl` (person)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Heumeyer  in der Beschwerdesache Emanuela Schöchl,  J. Schemmerl-Gasse 7, 4906 Felling, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr.in Valentina Heumeyer` (person)
- `Emanuela Schöchl` (person)
- `J. Schemmerl-Gasse 7, 4906 Felling, Österreich` (address)
- `Anton Hörmann` (person)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_67`)


Die mit der  gegenständlichen Beschwerde vorgelegte Kopie des Schreibens vom 1.12.2012 weist  keinen Eingangsstempel des Finanzamtes als Nachweis der tatsächlichen Einreichung  auf.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_108`)


Nach Ansicht des Finanzamtes kann demnach nicht von einer Haupttätigkeit  gesprochen werden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_201`)


Diese Bezeichnung lässt nach Ansicht des Finanzamtes offen, ob unter der  Bezeichnung ‚Ordnung in der Ordination‘ klassische Reinigungsarbeiten unterzuordnen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_216`)


Das beschwerdegegenständliche Dienstverhältnis des Abgabepflichtigen mit seinem  Sohn erfüllt nach Ansicht des Finanzamtes unverändert nicht die Kriterien für die  Anerkennung von Vereinbarungen zwischen nahen Angehörigen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_14`)


Mit 16.6.2020 erging seitens des Finanzamtes folgendes Ersuchen um Ergänzung:  „Gem. Verordnung des Bundesministers für Finanzen betreffend eine Berufsausbildung eines  Kindes außerhalb des Wohnortes gilt folgendes:   Ausbildungsstätten innerhalb einer Entfernung von 80 km zum Wohnort gelten als innerhalb  des Einzugsbereiches des Wohnortes gelegen, wenn von diesen Gemeinden die täglichen Hin-  und Rückfahrt zum und vom Studienort nach den Verordnungen gem. § 26 Abs 3 des  Studienförderungsgesetzes 1992 BGBl. Nr. 305 zeitlich noch zumutbar sind.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_23`)


Mit 31.8.2020 wurde die Beschwerde vom 28.4.2020 gegen den Bescheid vom 20.4.2020  mittels Beschwerdevorentscheidung gem. § 262 BAO seitens des Finanzamtes als unbegründet  abgewiesen:  „Begründung: Der Freibetrag betreffend Berufsausbildung eines Kindes steht gem. § 34 Abs. 8  EStG 1988 dann zu, wenn im Einzugsbereich des Wohnortes keine entsprechende  Ausbildungsmöglichkeit besteht.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_58`)


Im Zuge des Ermittlungsverfahrens wurde seitens des Finanzamtes festgestellt, dass die  Tochter des Bf. in Wien Rechtswissenschaften studiert.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_70`)


Nach Recherche des Finanzamtes ist für Wien nicht nur  die Ankunftszeit am Hauptbahnhof maßgeblich, sondern auch Wien Westbahnhof.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_85`)


Im Zuge des Ermittlungsverfahrens wurde seitens des Finanzamtes festgestellt, dass die  Tochter des Bf. in Wien Rechtswissenschaften studiert.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr. Astrid Binder` (person)
- `Valerie Süssmeier` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_67`)


In dem Vorlagebericht vom 24. August 2020, dem nach der Rechtsprechung Vorhaltscharakter  zukommt, nahm das Finanzamt nach Wiedergabe des Sachverhaltes zum Vorbringen des Bf, er  hätte noch keine Gelegenheit bekommen sich zu den Feststellungen des Finanzamtes zu  äußern, Stellung wie folgt:  „Entgegen der Behauptung des Beschwerdeführers hatte dieser sowohl im Rahmen der  Betriebsprüfung als auch im Beschwerdeverfahren die Möglichkeit an der Ermittlung der  Besteuerungsgrundlagen mitzuwirken.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_74`)


Trotz mehrmaliger Versuche seitens des Finanzamtes, ist es nicht gelungen den Bf telefonisch  zu erreichen, weswegen eine Vorladung elektronisch abgefertigt wurde (siehe auch Mail an  Prüfer wegen Vorladung;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_86`)


Obwohl der Bf bereits in der mit ihm am 5.9.2019 aufgenommenen Niederschrift versprochen  hat, die Umsätze bekannt zu geben und Unterlagen vorzulegen, wurde letztlich jedoch trotz  mehrmaliger diesbezüglicher Versuche des Finanzamtes jegliche Mitwirkung unterlassen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache QZKX Beratung, Lambacher Straße 9, 3123 Mittermerking, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 45-817/1493  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `QZKX Beratung`(organisation)
- `Lambacher Straße 9, 3123 Mittermerking, Österreich`(address)
- `Mag. Dieter Walla & Partner Steuerberater OG`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `45-817/1493`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn QZKX Beratung,  nunmehr QZKX Beratung (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `QZKX Beratung`(organisation)
- `QZKX Beratung`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_23`)


Beschwerdeerwägungen:  Dem angefochtenen Bescheid über die Festsetzung von Anspruchszinsen 2007 liegt der im  Einkommensteuerbescheid 2007 des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013  ausgewiesene Differenzbetrag von € 254.913,99 zugrunde.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers Emma Türker, Frauenhofenstraße 13, 5132 Gasteig, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Emma Türker`(person)
- `Frauenhofenstraße 13, 5132 Gasteig, Österreich`(address)
- `Finanzamtes Linz`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_2`)


Salzburg Steuerberatung und Wirtschaftsprüfung  GmbH, Mildenburggasse 4A, 5020 Salzburg, über die Beschwerde vom 6. Februar 2020 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 15. Jänner  2020 betreffend Gebühren zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Salzburg Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Janis Abelen`(person)
- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`
- `Finanzamtes` — similar text (different position): `Finanzamtes für Gebühren`
- `Finanzamtes` — similar text (different position): `Finanzamtes für Gebühren`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.Dr. Thomas Leitner`(person)
- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_3`)


Der Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern  und Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5  Absatz 1 Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis  31.12.2011 wird wie folgt abgeändert:    Die Gebühr gemäß § 33 TP 5 Abs 1 Z 1 GebG wird   von der Bemessungsgrundlage.......2.956.905,07 Euro  festgesetzt mit 1%...............................29.569,05 Euro

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_6`)


Der Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern  und Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5  Absatz 1 Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis  31.12.2012 wird wie folgt abgeändert:    Die Gebühr gemäß § 33 TP 5 Abs 1 Z 1 GebG wird   von der Bemessungsgrundlage.......5.818.666,39 Euro  festgesetzt mit 1%................................58.186,66 Euro

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_8`)


Der Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern  und Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5  Absatz 1 Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis  31.08.2013 wird wie folgt abgeändert:    Die Gebühr gemäß § 33 TP 5 Abs 1 Z 1 GebG wird   von der Bemessungsgrundlage........828.262,50 Euro  festgesetzt mit 1%................................8.282,63 Euro

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Alwerkmon-Pharma,  Hinteralm 4, 3243 Lachau, Österreich  vertreten durch Stb., über die Beschwerde vom 17.10.2011 gegen den Bescheid  des Finanzamtes Lilienfeld St. Pölten vom 13.7.2011 betreffend Einkommensteuer 2009 nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alwerkmon-Pharma`(organisation)
- `Hinteralm 4, 3243 Lachau, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Marianne Liuni`(person)
- `Luigi Wedekämper`(person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_32`)


Vom Bundesministerium für Finanzen wurde eine Stellungnahme des Finanzamtes für  Gebühren, Verkehrssteuern und Glückspiel eingeholt. Die Abgabenbehörde teilte nach  Durchsicht der Unterlagen, des Steuerkontos und Durchführung einer umfassenden  Internetrecherche im Schreiben vom April 2017 Folgendes mit:  „Laut den Jahresabschlüssen hat das Unternehmen seit seiner Gründung ein hohes negatives  Eigenkapital und hohe Verluste erwirtschaftet:    Jahr Eigenkapital Verlust   (inkl. Vortrag)  2009 - 44.357 - 61.857  2010 - 179.045 - 196.545  2011 - 505.423 - 705.423  2012 - 908.541 - 1.108.541  2013 - 762.561 - 962.561  2014 - 703.195 - 903.195  In allen Jahresabschlüssen werde erklärt, dass eine Überschuldung nicht vorliege, weil im Falle  einer Insolvenz der ehemalige Gesellschafter-Geschäftsführer (G.) auf seine Forderungen bis zur  Höhe des negativen Eigenkapitals verzichte.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für  Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)
- `Finanzamtes für  Gebühren`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_139`)


Im Zuge einer ‚Rückanfrageantwort des Finanzamtes‘ vom 12. Februar 2018 legte die Behörde  der FFG die ihr von der Bf. übermittelten Unterlagen vom 15. Dezember 2016 sowie vom  31. Jänner 2017 mit dem Ersuchen um neuerliche Begutachtung vor.

**False Positives:**

- `Finanzamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Hollabrunn Korneuburg Tulln`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Regina Vogt`(person)
- `StR Dr.in Lydia Vogtleitner`(person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich`(address)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Spittal Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Claudia Noeltge`(person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)
- `Dr. Amtsvertr`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Christine Schweinfort  über den Antrag der Kira Ballis, BEd,  Josefiwaldweg 48, 3071 Diemannsberg, Österreich, auf Gewährung der Verfahrenshilfe im Beschwerdeverfahren gegen den  Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020  betreffend Abweisung des Rückzahlungsantrages, Steuernummer 24-406/6946  beschlossen:  I. Der Antrag auf Gewährung der Verfahrenshilfe wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Christine Schweinfort`(person)
- `Kira Ballis, BEd`(person)
- `Josefiwaldweg 48, 3071 Diemannsberg, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `24-406/6946`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_1`)


BESCHLUSS   Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über den  Vorlageantrag vom 19. Dezember 2018 des Beschwerdeführers Diethard Uphof, Unterrotte 8, 3061 Unterwolfsbach, Österreich,  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten, 3100 St. Pölten, Daniel Gran-Straße 8,  vom 4. Mai 2018 betreffend Umsatzsteuer 2016:    I)

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Günter Narat`(person)
- `Diethard Uphof`(person)
- `Unterrotte 8, 3061 Unterwolfsbach, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Spittal Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_3`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes für Gebühren, Verkehrsteuer und Glücksspiel über die  Festsetzung eines ersten Säumniszuschlages vom 10. November 2014 wurde über Frau Eign (kurz: Bf.) von den Gebühren (Bestandsverträge) Journale 07/2014 von EUR 2.701,00 gemäß  § 217 Abs. 1 und 2 BAO ein Säumniszuschlag mit 2%, das sind EUR 54,02, mit der Begründung  festgesetzt, dass die oben angeführte Abgabenschuldigkeit nicht bis 15. September 2014  entrichtet worden sei.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)
- `Eign`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_12`)


Mit Beschwerdevorentscheidung des Finanzamtes für Gebühren, Verkehrsteuer und  Glücksspiel vom 5. Dezember 2014 wurde die Beschwerde als unbegründet abgewiesen und als  Begründung Folgendes ausgeführt:  "Die Selbstberechnung der Gebühren für den Zeitraum 07/2014 war am 15.09.2014 fällig.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes für  Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Alessia Olschofski`(person)
- `Natalie Gosebrink, Bakk. phil.`(person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `50-818/5472`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_92`)


Darin sei-im Gegensatz zur Rechtsansicht des BFG und des  Finanzamtes- auf das Bestehen eines auf unbestimmte Dauer abgeschlossenen  Bestandvertrages nicht nur wegen dem, darin eingeräumten, Präsentationsrecht erkannt  worden, sondern es sei darin festgestellt worden, dass mit der Einräumung des  Präsentationsrechtes das Vorliegen eines, aufgrund der Vereinbarung aller Kündigungsgrunde  nach § 30 Abs.2 MRG, auf unbestimmte Dauer abgeschlossenen Bestandvertrages, verstärkt  worden sei.

**False Positives:**

- `Finanzamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Firma_entities` 💣

**F1:** 0.009 | **Precision:** 0.833 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `c1b4361a`  
**Description:**
Matches entities introduced by 'Firma' or 'der Firma', strictly bounded by company suffixes or prepositions to avoid over-matching.

**Content:**
```
(?:der\s+Firma|auf\s+die\s+Firma|bei\s+der\s+Firma|mit\s+der\s+Firma|von\s+der\s+Firma)(?:\s+)([A-Z][a-zA-Z0-9\s&\-]+(?:GmbH|AG|m\.b\.H\.)(?:\s+und\s+[A-Z][a-zA-Z0-9]+(?:\s+KI)?(?:\s+GmbH|AG)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.005 | 0.009 | 36 | 30 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 30 | 6 | 6170 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_51`)


Im Zuge einer Betriebsprüfung in einem  anderen Unternehmen seien die Rechnungen der Firma Spies&Wickert Solar GmbH überprüft und als  Scheinrechnungen beurteilt worden.

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Missed by this rule (FN):**

- `Spies&Wickert Solar GmbH€` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_96`)


Die UID Nummer der Firma Spies&Wickert Solar GmbH war laut Finanzamtsunterlagen mit 15.8.2012 begrenzt.

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_9`)


Im gegenständlichen Fall sei zwar am 15. Juli 2019 bei der Firma Gerstbreu Umwelt GmbH ein  Umbuchungsantrag eingebracht worden.

| Predicted | Gold |
|---|---|
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_74`)


Unter Berücksichtigung der angeführten (höchst-)gerichtlichen Judikatur und in Würdigung der  Gesamtumstände des Einzelfalles ist davon auszugehen, dass die Bf. (ihr steuerlicher Vertreter)  in Kenntnis der Produktionsübermittlung der entsprechenden UVA der Firma Gerstbreu Umwelt GmbH davon  ausgegangen ist, dass zum Fälligkeitszeitpunkt 15. Juli 2019 ein entsprechender  Überrechnungsantrag gestellt wurde, der die Entrichtung der betreffenden Abgaben bewirken  würde.

| Predicted | Gold |
|---|---|
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_105`)


Allein die Beschreibung der Kaufartikel in Form von Abkürzungen war nicht ausreichend, die  Anschaffung von Büromaterial und damit einen Zusammenhang zwischen den Kosten bei der  Firma Saturn Vertriebs GmbH und den Einkünften aus nichtselbständiger Arbeit nachzuweisen.

| Predicted | Gold |
|---|---|
| `Saturn Vertriebs GmbH` | `Saturn Vertriebs GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

| Predicted | Gold |
|---|---|
| `Furtnex-Versand GmbH` | `Furtnex-Versand GmbH` |

**Missed by this rule (FN):**

- `Ronald Jundt` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_16`)


Entscheidungsgründe  I. Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020, wurde Brunhild Stanislav (in weiterer Folge:  Beschuldigter) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im April 2020 vor  der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im  Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum  12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Stanislav` (person)
- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_18`)


2. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Mai 2020 vor  der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im  Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum  12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_20`)


3. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juni 2020 vor  der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im  Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum  12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_22`)


4. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juli 2020 vor  der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im  Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum  12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  3 von 11 Seite 4 von 11

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_25`)


5. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im August 2020  vor der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein  Gerüst im Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er  hiefür bis zum 12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_27`)


6. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Oktober 2020  vor der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² genutzt,  wobei er hiefür bis zum 11.11.2020 weder eine Gebrauchserlaubnis erwirkt noch die  Gebrauchsabgabe entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_29`)


7. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im November  2020 vor der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² genutzt,  wobei er hiefür bis zum 11.11.2020 weder eine Gebrauchserlaubnis erwirkt noch die  Gebrauchsabgabe entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_37`)


II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020, wurde Herr Brunhild Stanislav, (in weiterer Folge: Beschuldigter) als  handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  mit Sitz in Altfinkensteiner Weg 15, 9065 Moosberg, Österreich,  schuldig erkannt,   1. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juni 2020 vor  der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `Brunhild Stanislav` (person)
- `Altfinkensteiner Weg 15, 9065 Moosberg, Österreich` (address)
- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_39`)


2. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juni 2020 vor  der Liegenschaft in Schönbichlstraße 23, 5360 Rußbach, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch einen Container im Ausmaß von 20,90 m² genutzt, wobei er hiefür bis  zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Schönbichlstraße 23, 5360 Rußbach, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_41`)


3. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juli 2020 vor  der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_43`)


4. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juli 2020 vor  der Liegenschaft in Schönbichlstraße 23, 5360 Rußbach, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch einen Container im Ausmaß von 20,90 m² genutzt, wobei er hiefür bis  zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Schönbichlstraße 23, 5360 Rußbach, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_47`)


er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im August 2020  vor der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt,  wobei er hiefür bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die  Gebrauchsabgabe entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_49`)


6. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im August 2020  vor der Liegenschaft in Schönbichlstraße 23, 5360 Rußbach, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch einen Container im Ausmaß von 20,90 m² genutzt, wobei er  hiefür bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `Schönbichlstraße 23, 5360 Rußbach, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_51`)


7. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Oktober 2020  vor der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt,  wobei er hiefür bis zum 12.11.2020 weder eine Gebrauchserlaubnis erwirkt noch die  Gebrauchsabgabe entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_53`)


8. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im November  2020 vor der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem  öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt,  wobei er hiefür bis zum 12.11.2020 weder eine Gebrauchserlaubnis erwirkt noch die  Gebrauchsabgabe entrichtet habe.

| Predicted | Gold |
|---|---|
| `KI Synlogtra GmbH` | `KI Synlogtra GmbH` |

**Missed by this rule (FN):**

- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_39`)


Vom 09.05.2014 - 15.10.2018  waren sie bei der Firma Berg-Transport Werke GmbH beschäftigt.

| Predicted | Gold |
|---|---|
| `Berg-Transport Werke GmbH` | `Berg-Transport Werke GmbH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

| Predicted | Gold |
|---|---|
| `Hemken Automotive GmbH` | `Hemken Automotive GmbH` |

**Missed by this rule (FN):**

- `Wilhelm Fißenewert, LLM` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/143892.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143892.1_31`)


Im Zeitraum 01.01.2019 – 27.04.2019 war die Bf. bei der Firma Dorfverglanz GmbH  im Inland  beschäftigt.

| Predicted | Gold |
|---|---|
| `Dorfverglanz GmbH` | `Dorfverglanz GmbH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_79`)


Es handelt  sich dabei um Abrechnungen von Tankkarten der Firma T S.r.l. bei der Firma X GmbH & Co.KG.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/145806.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145806.1_6`)


Der in OrtÖ1 wohnhafte Beschwerdeführer (in der Folge kurz: Bf.) ist bei der Firma Monmon-Analyse GmbH  in OrtÖ1 als Vertreter beschäftigt und erzielt aus dieser Tätigkeit nichtselbständige Einkünfte.

| Predicted | Gold |
|---|---|
| `Monmon-Analyse GmbH` | `Monmon-Analyse GmbH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_16`)


Anzumerken ist,  dass die Firma A.GmbH hauptsächlich von der Firma TraunBeratung GmbH (Gf: B.B.) beliefert wird.

| Predicted | Gold |
|---|---|
| `TraunBeratung GmbH` | `TraunBeratung GmbH` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_18`)


Teilweise waren die ER der Firma TraunBeratung GmbH nicht in der  Belegsammlung enthalten.

| Predicted | Gold |
|---|---|
| `TraunBeratung GmbH` | `TraunBeratung GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_35`)


In diesem Ausgabenbetrag seien Fremdleistungen von zwei Subunternehmen enthalten:  1.) Rechnungen der Firma C Bau GmbH € 228.630,13  2.)

**False Positives:**

- `C Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_62`)


es sei lediglich der Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma Ch angezweifelt worden.

**False Positives:**

- `T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_107`)


Beim  anderen Produkt handelt es sich um eine Kupplung des Herstellers und Distributors von  Zubehör in den Produktbereichen Foto, Video, Audio, Computer und Telekommunikation,  nämlich der Firma Hama GmbH & Co KG, die zum Anschluss eines analogen Telefons an eine  TST-Anschlussdose geeignet ist.

**False Positives:**

- `Hama GmbH` — partial — pred is substring of gold: `Hama GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hama GmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134157.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134157.1_38`)


Aus dieser Berechnungsgrundlage ergibt sich eindeutig, dass die in der Gewinn-  und Verlustrechnung der Beschwerdeführerin ausgewiesenen Provisionsaufwendungen in Höhe  von 7,5 % berechnet wurden und entspricht dies dem zwischen der Firma Nord Kraftzor AG und Firma Bf am  13.12.2002 abgeschlossenen Vertrag.

**False Positives:**

- `Nord Kraftzor AG und Firma` — partial — gold is substring of pred: `Nord Kraftzor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nord Kraftzor AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/136739.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136739.1_6`)


Bundesabgabenordnung für die aushaftenden  Abgabenschuldigkeiten der Firma Masuhr Medien GmbHi.L., Firmenbuchnummer 100, Schießstättgasse 15, 3744 Klein-Meiseldorf, Österreich  im  Ausmaß von 25.293,79 Euro in Anspruch genommen und aufgefordert, diesen Betrag innerhalb  eines Monats ab Zustellung dieses Bescheides zu entrichten.

**False Positives:**

- `Masuhr Medien GmbH` — partial — pred is substring of gold: `Masuhr Medien GmbHi.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Masuhr Medien GmbHi.L.`(organisation)
- `Schießstättgasse 15, 3744 Klein-Meiseldorf, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_76`)


Er ist vom 02.09.2016 bis 02.04.2019 in einem Lehr- bzw. Ausbildungsverhältnis mit der  Firma S-GmbH gestanden (vgl. Lehrvertrag vom 21.09.2016 und  Sozialversicherungsdatenauszug des Sohnes vom 23.02.2023).

**False Positives:**

- `S-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Magistrat_Stadt_Wien_entities` 💣

**F1:** 0.173 | **Precision:** 0.795 | **Recall:** 0.097  

**Format:** `regex`  
**Rule ID:** `2df4515e`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrats der Stadt Wien' including department numbers.

**Content:**
```
(?:Magistrats?\s+der\s+)?Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+\d+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.795 | 0.097 | 0.173 | 781 | 621 | 160 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 621 | 160 | 5784 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Raphael Williamson, BEd, Züggen 8, 8042 Graz, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Manuela Fischer` (person)
- `Raphael Williamson, BEd` (person)
- `Züggen 8, 8042 Graz, Österreich` (address)
- `Monika Pfundner-Lenz` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_15`)


Die Nachforderung an Kommunalsteuer war in der Niederschrift für die Jahre 2007 – 2011 mit  insgesamt Euro 4.274,70 festgehalten und angeführt, dass die Bewertung des Ausmaßes der  Kommunalsteuerpflicht durch den Magistrat der Stadt Wien zu erfolgen hätte.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_17`)


Mit Prüfungs- und Nachschauauftrag des Magistrats der Stadt Wien vom 13.2.2013 wurde der  steuerlichen Vertretung des Bf. u. a. die Prüfung der Kommunalsteuer für den Zeitraum 1/07 –  12/12 am 26.9.2013 zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_18`)


Mittels Schreiben des Magistrats der Stadt Wien vom 26.9.2013 wurde gegenüber dem Bf.  erklärt, dass infolge der im Dezember 2012 durchgeführten Kommunalsteuerprüfung der  2 von 12 Seite 3 von 12

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_32`)


Mit Bescheid vom 19.3.2014 des Magistrats der Stadt Wien, zugestellt am 27.3.2014, wurde  dem Bf. gemäß § 11 Abs. 3 KommStG 1993 die bereits fällige Kommunalsteuer für die in der  Betriebsstätte, Tennisanlage in Wien, gewährten Arbeitslöhne wie folgt vorgeschrieben:  3 von 12 Seite 4 von 12

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_51`)


Die Wiener Gebietskrankenkasse habe im Rahmen einer GPLA-Prüfung in ihrer Niederschrift  vom 22.10.2012 die obig beschriebenen Tatbestände festgehalten und abschließend  angemerkt „die Überprüfung des Ausmaßes der Kommunalsteuerpflicht erfolgt durch den  Magistrat der Stadt Wien“.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Wiener Gebietskrankenkasse` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_52`)


Der Prüfer wäre sich offensichtlich über das Ausmaß bzw. die  Aufteilung der Bemessungsgrundlage nicht im Klaren gewesen und habe die Entscheidung dem  Magistrat der Stadt Wien überlassen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_68`)


Der Magistrat der Stadt Wien habe im angefochtenen Bescheid nicht begründet, warum bei  einem gemeinnützigen Verein kein nichtunternehmerischer Bereich vorliegen solle.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_70`)


Mit Beschwerdevorentscheidung (BVE) vom 15.5.2014, zugestellt am 29.8.2014, wies der  Magistrat der Stadt Wien die gegenständliche Beschwerde als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_101`)


Strittig war die mit Bescheid des Magistrats der Stadt Wien vom 19.3.2014 erfolgte  Festsetzung der Kommunalsteuer für die Jahre 2007 bis 2012 auf Basis von 100% der im  jeweiligen Jahr ausbezahlten Bruttolöhne der Dienstnehmer des Bf.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_137`)


Entgegen den, dem angefochtenen Bescheid zugrundeliegenden, zur Kommunalsteuer  getroffenen Feststellungen der GPLA-Prüfung vom 22.10.2012 sowie der darauffolgenden  Prüfung (Revision) durch den Magistrat der Stadt Wien vom 26.9.2013, lag nach Meinung des  Bf. bei seiner Tätigkeit im Sportbereich ein zum Teil nichtunternehmerischer Bereich vor.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_174`)


Wie in den angeführten Prüfungsverfahren (GPLA-Prüfung vom Dezember 2012 sowie Revision  des Magistrats der Stadt Wien vom 26.9.2013) festgestellt worden war, hatte sich der  selbstberechnete Abgabenbetrag als nicht richtig erwiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_179`)


Die Festsetzung der Kommunalsteuer für die Zeiträume 2007 – 2012 war daher gemäß § 11  Abs. 3 KommStG mit Bescheid des Magistrats der Stadt Wien zu Recht erfolgt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_140`)


Beweiswürdigung  Der konkrete Inhalt und Umfang der Gewerbeberechtigungen ist den aktenkundigen  Gewerbeanmeldungen des Magistrats der Stadt Wien entnehmbar.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_19`)


Mit dem angefochtenen Bescheid sei lediglich die Höhe der  Abgabe, die für die Entleerung der Müllsammelgefäße zu verrechnen sei, neu vorgeschrieben  worden, weil sie sich durch die Valorisierung im Amtsblatt der Stadt Wien Nr. 48 vom  28.11.2019 gegenüber dem Vorbescheid geändert hätte.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_52`)


Die Stadt Wien als Gemeinde wird ermächtigt, für die Bereitstellung und Benützung  von öffentlichen Einrichtungen zur Sammlung und Behandlung von Abfällen sowie für die  Erfüllung der mit der kommunalen Abfallwirtschaft zusammenhängenden sonstigen Aufgaben  auf Grund eines Gemeinderatsbeschlusses eine Abgabe einzuheben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_71`)


Die Grundgebühr ist nur für Sammelbehälter im Eigentum der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_6`)


Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft (§ 2 Wiener Parkometergesetz 2006) mit Strafverfügung  vom 18. Dezember 2019, MA 67/123/2019, angelastet, er habe das Fahrzeug am 11. Oktober  2019 um 13:54 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Theodor-Sickel- Gasse ggü 14, ohne einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_25`)


Der Magistrat der Stadt Wien wies in der Folge den Einspruch des Bf. vom 11. Jänner 2020  gegen die Strafverfügung vom 18. Dezember 2019 mit Bescheid vom 4. März 2020 gemäß § 49  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_38`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Mai 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_23`)


Der Magistrat der Stadt Wien lastete der Bf. mit zwei Straferkenntnissen, beide vom  25.02.2020, die bereits näher bezeichneten Verwaltungsübertretungen an und verhängte  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung  iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 jeweils eine Geldstrafe von € 60,00 und für den  Fall der Uneinbringlichkeit jeweils eine Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_48`)


Der Magistrat der Stadt Wien legte die Beschwerden samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in den Beschwerdesachen des Janosch Findeise,  Reichenauweg 22, 4724 Oberaubach, Österreich, gegen die zwei Straferkenntnisse des Magistrats der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde (beide) vom 23. Juni 2020, GZen 1)  MA67/Zahl1 und 2) MA67/Zahl2, in beiden Fällen wegen einer Verwaltungsübertretung nach §  2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) werden die Beschwerden als unbegründet abgewiesen  und werden die angefochtenen Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien,  Magistratsabteilung 67` | `Magistrats der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Janosch Findeise` (person)
- `Reichenauweg 22, 4724 Oberaubach, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_11`)


Wegen Verletzung des § 2 Wiener Parkometergesetz 2006 verhängte der Magistrat der Stadt  Wien gemäß § 4 Abs. 2 Wiener Parkometergesetz 2006 über den Bf. jeweils eine Geldstrafe in  Höhe von 60,00 Euro (Ersatzfreiheitsstrafe: jeweils 14 Stunden) und schrieb gemäß § 64 VStG  jeweils einen Beitrag zu den Kosten des Strafverfahrens von 10,00 Euro vor, womit sich der zu  zahlende Gesamtbetrag auf jeweils 70,00 Euro belief.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_62`)


Der Bf. wurde mit den gegenständlichen Auskunftsverlangen - Schreiben des Magistrats der  Stadt Wien, Magistratsabteilung 67, beide vom 04.05.2020, als Zulassungsbesitzer des  mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 aufgefordert, Auskunft  darüber zu erteilen, wem er das genannte mehrspurige Kraftfahrzeug   • zu o.a. 1) am 09.01.2020 um 16:05 Uhr überlassen gehabt habe, sodass es zu diesem  Zeitpunkt in 1070 Wien, Lerchenfelder Gürtel 36 gestanden sei;  • zu o.a. 2) am 14.01.2020 um 10:13 Uhr überlassen gehabt habe, sodass es zu diesem  Zeitpunkt in 1150 Wien, Goldschlagstraße 77 gestanden sei.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien, Magistratsabteilung 67` | `Magistrats der  Stadt Wien, Magistratsabteilung 67` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_101`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_5`)


Die Geldstrafe von € 36,00 ist zusammen mit dem Beitrag zu den Kosten des Strafverfahrens  (§ 64 Abs. 1 und 2 VStG) von € 10,00, insgesamt somit € 46,00, binnen zwei Wochen ab  Zustellung des Straferkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete der Beschwerdefüherin (Bf.) unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31.10.2019 an, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 02.09.2019 um 14:43 Uhr in der  gebührenpflichtigen Kurzparkzone in 1140 Wien, Penzinger Straße 157, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt.  Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1  Wiener Parkometergesetz 2006 wurde über die Bf. eine Geldstrafe iHv € 60,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_17`)


Der Magistrat der Stadt Wien erkannte die Bf. mit Straferkenntnis vom 26.11.2019 wegen der  bereits näher bezeichnete Verwaltungsübertretung für schuldig und verhängte wegen  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_39`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 17.12.2019).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_42`)


Das Fahrzeug war zum Beanstandungszeitpunkt ohne gültigen Parkschein und ohne die  Tafel "Mobile Hauskrankenpflege im Dienst" abgestellt.  Am 21.02.2019 wurde der Bf. von der Magistratsdirektion der Stadt Wien für das  verfahrensgegenständliche Fahrzeug eine Berechtigungstafel gemäß § 24 Abs. 5a StVO 1960  und § 6 Wiener Parkometerabgabeverordnung mit der laufenden Nr. 21 ausgestellt.  Dass die Bf. von 14:00 Uhr bis 18:00 Uhr, und somit auch zur Beanstandungszeit, für MOKI  Wien in 1140 Wien, Penzinger Straße 157-156, tätig war, wurde von ihrem Dienstgeber  bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_108`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_6`)


Im Straferkenntnis vom 9. März 2020 warf der Magistrat der Stadt Wien dem Beschwerde- führer (Bf.) vor, er habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das  mehrspurige Kraftfahrzeug mit dem im Straferkenntnis näher bezeichneten behördlichen  Kennzeichen am 14. November 2019 um 14:51 Uhr in einer gebührenpflichtigen Kurzparkzone  abgestellt habe, ohne einen gültigen Fahrschein in das Fahrzeug zu legen oder einen elektroni- schen Parkschein zu aktivieren.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_11`)


Der Magistrat der Stadt Wien legte seiner Entscheidung die Anzeige vom 14. November 2019,  die Lenkerauskunft der Zulassungsbesitzerin und den Einspruch des Bf. gegen die an die Zulas- sungsbesitzerin adressierte Anonymverfügung zugrunde, worin der Bf. angegeben habe, dass  er zwischen 14:00 Uhr und 16:00 Uhr zwei Mal kurz und weniger als 10 Minuten in diesem  Areal zwar gehalten aber das Fahrzeug nicht abgestellt habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_13`)


Zu diesem Vorbringen stelle der Magistrat der Stadt Wien fest, dass der Meldungsleger wählen  könne, ob er eine Organstrafverfügung ausstelle oder eine Anzeige erstatte.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_30`)


3.3. Im Einspruch vom 07. Jänner 2020 gegen die als „Verfügung“ bezeichnete Lenkererhe- bung vom 20. Dezember 2019 gab der Bf. an, dass er „dort“ nicht geparkt habe und wies da- rauf hin, dass dem Magistrat der Stadt Wien seine Daten bekannt seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_33`)


3.5. Am 15. Jänner 2020 sandte der Bf. folgende Mail an den Magistrat der Stadt Wien: „Hier- mit beeinspruche ich die Verfügung vom 20.12.2019: Habe ich dort nicht geparkt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_39`)


B. Der Entscheidung wird folgende aus den Verwaltungsakten sich ergebende Sachlage zu- grunde gelegt: Im Straferkenntnis vom 9. März 2020 hat der Magistrat der Stadt Wien dem Bf.  eine Verwaltungsübertretung vorgeworfen, die er ihm auch in der Strafverfügung vom 08.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_7`)


Die Geldstrafe von € 48,00 ist gemeinsam mit den Kosten des Verwaltungsstrafverfahrens  (€ 10,00), insgesamt somit € 58,00 binnen zwei Wochen nach Zustellung dieses  Straferkenntnisses an den Magistrat der Stadt Wien zu bezahlen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_8`)


Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_27`)


Mit Straferkenntnis vom 25. August 2020 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung und wegen Verletzung des § 5  Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006  eine Geldstrafe von € 60,00 und für den Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von  14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Franz Trockenbrot,  Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich  vom 15. März 2020, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 10. März 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 9 Abs. 2 Wiener  Kontrolleinrichtungenverordnung iVm § 4 Abs. 3 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 30. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Erkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Franz Trockenbrot` (person)
- `Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich` (address)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_3`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (€ 12,00) ist gemeinsam mit der  Geldstrafe (€ 60,00) und dem Beitrag zu den Kosten der belangten Behörde (€ 10,00) binnen  zwei Wochen ab Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_5`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_14`)


Grundsätzlich darf darauf hingewiesen werden, dass die unmittelbar aufeinander folgende  Aktivierung von elektronischen Parkscheinen mit einer fünfzehn Minuten nicht übersteigenden  Abstellzeit oder die Kombination der Aktivierung eines fünfzehn Minuten nicht übersteigenden  elektronischen Parkscheines mit einem Parkschein gemäß § 2 Abs. 1 und 2 in zeitlich  unmittelbarer Aufeinanderfolge unzulässig ist (§ 9 Abs. 2 der Kontrolleinrichtungenverordnung  des Wiener Gemeinderates vom 14.08.2008, ABl. der Stadt Wien Nr. 33/2008, in der  geltenden  Fassung)…"  2 von 20 Seite 3 von 20

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Wiener Gemeinderates` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_23`)


Mit Strafverfügung vom 12. Februar 2020 lastete der Magistrat der Stadt Wien dem Bf. an, er  habe das verfahrensgegenständliche Fahrzeug am 12. Dezember 2019 um 14:52 Uhr in der  gebührenpflichtigen Kurzparkzone in 1110 Wien, Simmeringer Hauptstraße 59 - 61, abgestellt,  wobei elektronische Parkscheine mit einer fünfzehn Minuten nicht übersteigenden Abstellzeit  unmittelbar aufeinander folgend aktiviert worden seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_31`)


Mit Straferkenntnis vom 10. März 2020 wurde dem Bf. vom Magistrat der Stadt Wien die  bereits näher bezeichnete Verwaltungsübertretung angelastet und wegen Verletzung der  Rechtsvorschriften des § 9 Abs. 2 Wiener Kontrolleinrichtungenverordnung iVm § 4 Abs. 3  Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_63`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_242`)


Hier erweist sich die Bestimmung des Magistrat der Stadt Wien als Vollstreckungsbehörde als  zweckmäßig, da dem Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die  Vollstreckung der von den (anderen) Verwaltungsgerichten erlassenen Erkenntnissen und  Beschlüssen obliegt (vgl. für viele ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Melina Wellenbrock  in der Verwaltungsstrafsache  Gabriele Vogrin, Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Melina Wellenbrock` (person)
- `Gabriele Vogrin` (person)
- `Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich` (address)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_6`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) folgende, die Verwaltungsstrafsache  MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich möchte  Ihnen mitteilen, dass am 24.10.2019 das Fahrzeug … folgende Person gelenkt hat: …“  Über eine am 24.10.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 30.12.2019 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  1 von 4 Seite 2 von 4

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_10`)


Mit Vollstreckungsverfügung vom 10.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 30.12.2019 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_13`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) auch folgende, die Verwaltungsstrafsa- che MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich  möchte Ihnen mitteilen, dass ich am 06.10.2020 bereits Einspruch mittels E-Mail auf die Straf- verfügung erhoben habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_14`)


Das Fahrzeug … hat am 21.11.2019 folgende Person gelenkt: …“  Über eine am 21.11.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 20.01.2020 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  21.11.2019 um 17:49 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt habe, ohne für  seine Kennzeichnung mit einem richtig entwerteten Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_17`)


Laut Aktenvermerk des Magistrats der Stadt Wien wurde am 06.01.2020 kein Einspruch  gegen diese Strafverfügung eingebracht.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_18`)


Mit Vollstreckungsverfügung vom 11.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 20.01.2020 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_5`)


III. Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_6`)


Die Geldstrafe von € 48,00 ist gemeinsam mit dem Beitrag zu den Kosten der belangten  Behörde von € 10,00 (§ 64 VStG 1991), insgesamt somit € 58,00, binnen zwei Wochen nach  Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67, erkannte den Beschwerdeführer (Bf.) mit  Straferkenntnis vom 18. Juni 2020, MA67/000/2020, für schuldig, das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 3. Jänner 2020 um 21:37 Uhr in  der gebührenpflichtigen Kurzparkzone in 1010 Wien, Bellariastraße 8, Nebenfahrbahn, ohne  einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_62`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 13. August 2020,  MA67/206700430919/2020, angelastet, sie habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 20. Mai 2020 in der gebührenpflichtigen Kurzparkzone in  1110 Wien, Simmeringer Hauptstraße 152, ohne einem für den Beanstandungszeitpunkt 15:11  Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_19`)


Unter Hinweis auf die maßgeblichen gesetzlichen Normen (§ 5 Abs. 2 Wiener Parkometer- abgabeverordnung, § 7 Wiener Kontrolleinrichtungenverordnung) wurde weiters ausgeführt,  dass die Zeitangabe auf der Organstrafverfügung deshalb glaubwürdig sei, weil den  Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die Erfüllung der über- tragenen Aufgaben elektronische Überwachungsgeräte (sogen. PDA’s) zur Verfügung stünden,  welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen Server beziehen und  vorgeben würden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_3`)


Entscheidungsgründe  Am 3.April 2015 wurde zwischen der Bf., als Mieterin, und der V, als Vermieterin, ein  Mietvertrag über die Anmietung von Büroflächen, in dem, im Eigentum der Vermieterin  stehenden Büro-und Geschäftsgebäude der Liegenschaft KG bbb, BG Innere Stadt Wien,  (Adresse:  ccc) abgeschlossen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_5`)


Entscheidungsgründe  Der Beschwerdeführerin (Bf.) wurde mit Straferkenntnis des Magistrats der Stadt Wien vom  31.08.2020, GZ. MA67/Zahl/2020, zur Last gelegt, das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 06.03.2020 um 17:14 Uhr in 1170 Wien, Comeniusgasse  2, in einer gebührenpflichtigen Kurzparkzone abgestellt zu haben, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_17`)


Am 29.10.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte  Behörde die beschwerdegegenständliche Vollstreckungsverfügung, GZ. MA67/Zahl/2020, da  die mit obigem Straferkenntnis verhängte rechtskräftige Strafe bislang nicht bezahlt worden  sei, weshalb zur Einbringung des festgesetzten Gesamtbetrages in Höhe von € 75,00 (inkl. €  5,00 Mahngebühren) gemäß den §§ 3 und 10 Verwaltungsvollstreckungsgesetz 1991 (VVG) die  Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Proidl über die Beschwerde der  Istvan  Sicking, Fanny Elßler-Gasse 30, 9375 Zosen, Österreich, vom 09. Oktober 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 28. September 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der Fassung LGBl. für Wien Nr. 24/2012, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als der  Spruch des bekämpften Straferkenntnisses insoweit abgeändert wird, als die Geldstrafe von  Euro 60,00 auf Euro 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden  herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Missed by this rule (FN):**

- `Mag. Andrea Proidl` (person)
- `Istvan  Sicking` (person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_6`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_12`)


Die Bf. habe dadurch folgende Rechtsvorschrift verletzt:  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_67`)


Die Überweisung der mit Organstrafverfügung verhängten Geldstrafe von 36 Euro auf das  Konto des Magistrats der Stadt Wien erfolgte nach Ablauf der Frist von zwei Wochen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_83`)


Die Strafe wurde daher nicht ordnungsgemäß bezahlt. In der Folge leitete der Magistrat der  Stadt Wien mit der Strafverfügung vom 19.08.2020 das ordentliche Verwaltungsstrafverfahren  ein, welches letztlich zur verfahrensgegenständlichen Beschwerde gegen das o.a.  Straferkenntnis führte.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_116`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_5`)


Entscheidungsgründe  Der Beschwerdeführer (Bf.) wurde mit Strafverfügung des Magistrats der Stadt Wien,  Magistratsabteilung 67, GZ. MA67/Zahl/2020 vom 14. August 2020 für schuldig befunden, zu  einem näher bestimmten Zeitpunkt in der gebührenpflichtigen Kurzparkzone in 1030 Wien,  Kleistgasse 23, ein näher bestimmtes mehrspuriges Kraftfahrzeug abgestellt zu haben, ohne für  seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt  zu haben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien,  Magistratsabteilung 67` | `Magistrats der Stadt Wien,  Magistratsabteilung 67` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Marion Weißhar, Magnusplatz 23, 9555 Glantscha, Österreich, vom 20. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis mit der Maßgabe bestätigt, dass der Kostenbeitrag für das  behördliche Strafverfahren gemäß § 64 Abs. 2 VStG nicht 10,00 €, sondern 14,00 € beträgt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Dr. Judith Leodolter` (person)
- `Marion Weißhar` (person)
- `Magnusplatz 23, 9555 Glantscha, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_4`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_19`)


Verwaltungsübertretung(en) nach  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung.“

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_23`)


Mit Straferkenntnis vom 8. Jänner 2021 wurde der Bf. vom Magistrat der Stadt Wien wegen  der bereits näher bezeichnete Verwaltungsübertretung für schuldig befunden und wegen der  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm  § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe iHv € 140,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 1 Tag und 9 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_50`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsstrafakt dem Bundes- finanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Jänner 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_114`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Lieselotte Rübenkönig, Bakk. rer. nat., Strohweg 140g, 8593 Salla, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Regina Vogt` (person)
- `Lieselotte Rübenkönig, Bakk. rer. nat.` (person)
- `Strohweg 140g, 8593 Salla, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 6` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wolfgang Aigner`(person)
- `KzlR Adalbert Bürks`(person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_2`)


in der Verwaltungsstrafsache gegen  Desiree Barrabaß, Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 über die  zwei gleichlautenden Beschwerden der Beschuldigten vom 24. März 2020 gegen die zwei  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 25. Februar  2020, Zahl: a) MA67/xxxxx/2019 und b) MA67/yyyyy/2019, zu Recht erkannt:  I) Die zwei Beschwerden werden als unbegründet abgewiesen.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Desiree Barrabaß`(person)
- `Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in den Beschwerdesachen des Janosch Findeise,  Reichenauweg 22, 4724 Oberaubach, Österreich, gegen die zwei Straferkenntnisse des Magistrats der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde (beide) vom 23. Juni 2020, GZen 1)  MA67/Zahl1 und 2) MA67/Zahl2, in beiden Fällen wegen einer Verwaltungsübertretung nach §  2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) werden die Beschwerden als unbegründet abgewiesen  und werden die angefochtenen Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrats der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Janosch Findeise`(person)
- `Reichenauweg 22, 4724 Oberaubach, Österreich`(address)
- `Magistrats der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Nicola Folprecht`(person)
- `Florian Abbruzzese, BA`(person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_2`)


über die Beschwerde des René Werkstetter, Feichtenweg 14, 3922 Thaures, Österreich, vom 6. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 25. August 2020, Zahl MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

**False Positives:**

- `Stadt Wien,  Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `René Werkstetter`(person)
- `Feichtenweg 14, 3922 Thaures, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_15`)


Mit Strafverfügung vom 4. August 2020 wurde Bf1 (Beschwerdeführer, kurz Bf.) vom Magistrat  der Stadt Wien, Magistratsabteilung 67, angelastet, er habe das verfahrensgegenständliche  Fahrzeug am 5. Juni 2020 um 14:14 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Taborstraße 21a ggü, abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat  der Stadt Wien, Magistratsabteilung 67` — partial — gold is substring of pred: `Magistrat  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat  der Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Judith Leodolter`(person)
- `Franziskus Lex`(person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_32`)


Da der Bf. die ihm angelastete Verwaltungsübertretung nicht in Abrede stellt, ist der  Schuldspruch des Straferkenntnisses des Magistrates der Stadt Wien vom 18. Juni 2020,  MA67/000/2020, in Rechtskraft erwachsen (vgl. VwGH 27.10.2014, Ra 2014/02/0053) und  oblag dem Bundesfinanzgericht daher nur die Überprüfung der Höhe der verhängten  Geldstrafe (§ 27 VwGVG) bzw. der für den Fall der Uneinbringlichkeit verhängten  Ersatzfreiheitsstrafe.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Irene Kohler`(person)
- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi über die am 04.11.2020 per Telefax  eingebrachte Beschwerde der Alva van de Velden, Guldenäcker 147, 9020 Klagenfurt, Österreich, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 6, vom 29.10.2020, Zahl:  MA67/Zahl/2020, in Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 6` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alva van de Velden`(person)
- `Guldenäcker 147, 9020 Klagenfurt, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Proidl über die Beschwerde der  Istvan  Sicking, Fanny Elßler-Gasse 30, 9375 Zosen, Österreich, vom 09. Oktober 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 28. September 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der Fassung LGBl. für Wien Nr. 24/2012, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als der  Spruch des bekämpften Straferkenntnisses insoweit abgeändert wird, als die Geldstrafe von  Euro 60,00 auf Euro 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden  herabgesetzt wird.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Andrea Proidl`(person)
- `Istvan  Sicking`(person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt  Wien`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_10`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung, vom 28. September 2020, Zahl MA67/Zahl/2020, wurde Istvan  Sicking,  Fanny Elßler-Gasse 30, 9375 Zosen, Österreich (in weiterer Folge: Bf.) vorgeworfen, am 22.06.2020 um 19:47 Uhr in einer  gebührenpflichtigen Kurzparkzone in 1020 Wien, Machstraße 8, mit dem mehrspurigen  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) folgende Verwaltungsübertretung  begangen zu haben:  Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrats der Stadt Wien, Magistratsabteilung 67` — partial — gold is substring of pred: `Magistrats der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien`(organisation)
- `Istvan  Sicking`(person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_75`)


Dazu sei auch angemerkt, dass auf der Rückseite von Organstrafverfügungen des Magistrates  der Stadt Wien wörtlich Folgendes vermerkt ist:  6 von 9 Seite 7 von 9

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates  der Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien,  Magistratsabteilung 6` — partial — gold is substring of pred: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Marion Weißhar, Magnusplatz 23, 9555 Glantscha, Österreich, vom 20. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis mit der Maßgabe bestätigt, dass der Kostenbeitrag für das  behördliche Strafverfahren gemäß § 64 Abs. 2 VStG nicht 10,00 €, sondern 14,00 € beträgt.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Judith Leodolter`(person)
- `Marion Weißhar`(person)
- `Magnusplatz 23, 9555 Glantscha, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Bundesfinanzgerichtes vom 16.07.2020, Zahl RV/Zahl2/2020 zu Zahl  MA67/Zahl1/2019 wurde gegenüber dem Beschwerdeführer (Bf.) seine Beschwerde vom  18.03.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  vom 14.02.2020, Zahl: MA67/Zahl1/2019, als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien, Magistratsabteilung 67` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Lieselotte Rübenkönig, Bakk. rer. nat., Strohweg 140g, 8593 Salla, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

**False Positives:**

- `Stadt  Wien, Magistratsabteilung 6` — partial — pred is substring of gold: `Magistrates der Stadt  Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Regina Vogt`(person)
- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)
- `Strohweg 140g, 8593 Salla, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 6`(organisation)
- `Stadt Wien`(organisation)

</details>

---

## `Fa_Abbreviation_entities` 💣

**F1:** 0.003 | **Precision:** 0.692 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `db78d659`  
**Description:**
Matches 'Fa.' followed by a company name, ensuring the abbreviation is part of the match if it precedes the name, stopping at punctuation or conjunctions.

**Content:**
```
Fa\.[A-Z][a-zA-Z0-9\s&\.\-]+(?:GmbH|AG|m\.b\.H\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.692 | 0.001 | 0.003 | 13 | 9 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 4 | 5115 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_25`)


Im Jahre 2010 wurden Arbeiten von Arbeitern der Beschwerdeführer GmbH durchgeführt,  welche jedoch nicht von dieser verrechnet werden konnten, da diese Arbeiten bereits über die  Fa.Nexlex GmbH abgerechnet wurden.

| Predicted | Gold |
|---|---|
| `Fa.Nexlex GmbH` | `Fa.Nexlex GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_46`)


Im  Jahre 2008 wurden 5 Rechnungen mit einem Gesamtvolumen von € 57.000,- von einer Fa.POU Bau GmbH  9999 Wien, (Z-Bau-Adresse), an die Beschwerdeführer GmbH gelegt.

| Predicted | Gold |
|---|---|
| `Fa.POU Bau GmbH` | `Fa.POU Bau GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_6`)


Begründung  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa.West Altrader GmbH  Dorf, wurde von einem Kontrollorgan der Parkraumüberwachung der Landes- polizeidirektion am 9. April 2021 um 17:50 Uhr in der gebührenpflichtigen Kurzparkzone in  1160 Wien, Haberlgasse 10, beanstandet, da der zur Beanstandungszeit im Fahrzeug hinter- legte Parkschein Nr. 123 nach den Wahrnehmungen des Kontrollorgans Spuren von entfernten  Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_21`)


Mit E-Mail vom 17. Mai 2021 brachte die Fa.West Altrader GmbH bei der MA 67 folgendes Schreiben ein:  „An: MA 67 Lenkererhebung …  Es ist bei uns in der Firma leider ein IRRTUM passiert: Bei der Lenkererhebung – KO 681 EB vom  19.4.21 wurde leider eine falsche Person ausgefüllt. Anbei senden wir Ihnen nun die richtige  Person, welche das KFZ zu diesem Zeitpunkt gelenkt hat.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_39`)


Entgegen der Ansicht der Magistratsabteilung 67 kann der Schriftsatz der Fa.West Altrader GmbH nicht als  Beschwerde im Verwaltungsstrafverfahren des Gundula Doerfner  gewertet werden.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Missed by this rule (FN):**

- `Gundula Doerfner` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_40`)


Weder tritt die  Fa.West Altrader GmbH in seinem Namen auf, noch beruft sie sich auf eine diesbezügliche Vollmacht.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_20`)


Begründend wurde ausgeführt, da es sich um den gleichen Sachverhalt wie im Jahr 2011  handle (korrigierter Lohnzettel der Fa.Recycling Traderlog GmbH nach einer Lohnsteuerprüfung) werde die  gesetzliche Rechtsmittelfrist daher als ausreichend erachtet.

| Predicted | Gold |
|---|---|
| `Fa.Recycling Traderlog GmbH` | `Fa.Recycling Traderlog GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_25`)


Arbeitgeber  Fa.Recycling Traderlog GmbH  Aufgrund der dort festgestellten Sachverhalte wurde ein berichtiger Lohnzettel erstellt und  übermittelt (s. Einkommensteuerbescheid 2012 vom 19.06.2018)"

| Predicted | Gold |
|---|---|
| `Fa.Recycling Traderlog GmbH` | `Fa.Recycling Traderlog GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_49`)


Jene Firma, von der die Fytterer Handel GmbH hauptsächlich beliefert wird, ist die Fa.TraunBeratung GmbH  Der  Gesellschafter und Geschäftsführer der letztgenannten GmbH ist B.B., Ehegemahl der Bf..

| Predicted | Gold |
|---|---|
| `Fa.TraunBeratung GmbH` | `Fa.TraunBeratung GmbH` |

**Missed by this rule (FN):**

- `Fytterer Handel GmbH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_96`)


Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH eingesetzt als Subunternehmer im Jahr 2009 um  Scheinfirmen handelt im vollen Umfang zurück gewiesen.

**False Positives:**

- `Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH` — partial — gold is substring of pred: `Fa.POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.POU Bau GmbH`(organisation)
- `Y-Montage GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_38`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, hat das Schreiben der Fa.West Altrader GmbH vom  17. Mai 2021 als Beschwerde gegen das an Gundula Doerfner  als Beschuldigten ergangene  Straferkenntnis vom 7. Mai 2021 gewertet und dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Fa.West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_41`)


Angesichts der Vorgeschichte und der eindeutigen Formulierung (vgl. Hengstschläger/Leeb,  AVG I (2. Ausgabe 2014) § 13 Rz 37) handelt es sich um eine Nachreichung im Verfahren der Fa.West Altrader GmbH betreffend Lenkerauskunft, wo eine im Nachhinein erfolgte Richtigstellung der am 23.  April 2021 erteilten Lenkerauskunft vorgenommen wurde.

**False Positives:**

- `Fa.West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Altrader GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_50`)


Die  im Laufe der Betriebsprüfung bei der Fytterer Handel GmbH nachgereichten Eingangsrechnungen der Fa.TraunBeratung GmbH  die in der Belegsammlung der Fytterer Handel GmbH zum Teil nicht enthalten gewesen sind,  haben nur einen Teil der Abweichungen aufklären können.

**False Positives:**

- `Fa.TraunBeratung GmbH  die in der Belegsammlung der Fytterer Handel GmbH` — similar text (different position): `Fytterer Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fytterer Handel GmbH`(organisation)
- `Fa.TraunBeratung GmbH`(organisation)
- `Fytterer Handel GmbH`(organisation)

</details>

---

## `m_b_H_entities` 💣

**F1:** 0.003 | **Precision:** 0.478 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `7d7c0624`  
**Description:**
Matches companies ending in m.b.H. with stricter boundaries to avoid capturing preceding context.

**Content:**
```
(?:^|\s|,|\(|\[)([A-Z][a-zA-Z0-9\s&\.]+(?:Steuerberatungsgesellschaft)?(?:\s+m\.b\.H\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.478 | 0.002 | 0.003 | 23 | 11 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 12 | 6037 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Sahin, Fischmarkt 627, 4153 Vorderschiffl, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `LMG  Steuerberatungsgesellschaft m.b.H.` | `LMG  Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Dimitri Sahin` (person)
- `Fischmarkt 627, 4153 Vorderschiffl, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thomas Drieschner  in der Beschwerdesache Gebhard Determann,  Mooseggweg 49, 9624 Fritzendorf, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` | `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Univ.-Prof. Thomas Drieschner` (person)
- `Gebhard Determann` (person)
- `Mooseggweg 49, 9624 Fritzendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133179.1_2`)


Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse 17, 1010 Wien, über die Beschwerde vom 24. Februar 2021 gegen die  Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 17. Juli 2020  betreffend  - Umsatzsteuer für die Jahre 2012 bis 2016 sowie  - Wiederaufnahme betreffend Umsatzsteuer für die Jahre 2012 bis 2016  zu Recht:  I. Der Beschwerde gegen die Wiederaufnahmsbescheide betreffend Umsatzsteuer 2012 bis  2016 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `AUDITREU Steuerberatungsgesellschaft  m.b.H.` | `AUDITREU Steuerberatungsgesellschaft  m.b.H.` |

**Missed by this rule (FN):**

- `MMag. Gerald Erwin Ehgartner` (person)
- `Annkathrin Cattus` (person)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135280.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Babette Nenne, Landolfgasse 4, 5204 Pölzleiten, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Tribuswinkel, über die Beschwerde  vom 6. Mai 2020 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr: Finanzamt  Österreich) vom 23. März 2020 betreffend Festsetzung des Dienstgeberbeitrages für die Jahre  2014 bis 2018, Steuernummer 22-611/2720, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `LMG  Steuerberatungsgesellschaft m.b.H.` | `LMG  Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Babette Nenne` (person)
- `Landolfgasse 4, 5204 Pölzleiten, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)
- `22-611/2720` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135322.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135322.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Hon.-Prof.in Renate Wester  über die Beschwerde des  Dietlind Lenartowicz, Dag-Hammarskjöld-Siedlung 11, 3144 Steinbach, Österreich, vertreten durch die N & N Steuerberatungsgesellschaft m.b.H.,  Schubertstraße 68, 8010 Graz, vom 19.10.2021 gegen den Bescheid des Finanzamtes  Österreich vom 29.09.2021 betreffen Haftung gemäß § 9 BAO für Kapitalertragsteuer für  06/2020 zu Recht erkannt:   Der angefochtene Bescheid wird aufgehoben.

| Predicted | Gold |
|---|---|
| `N & N Steuerberatungsgesellschaft m.b.H.` | `N & N Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Renate Wester` (person)
- `Dietlind Lenartowicz` (person)
- `Dag-Hammarskjöld-Siedlung 11, 3144 Steinbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135915.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135915.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ronald Morosow, Schlumbergerstraße 26, 9072 Franzendorf, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die Beschwerde  vom 7. April 2021 gegen die Bescheide des Finanzamtes Österreich vom 24. März 2021,  Steuernummer 41-331/9010, betreffend Abweisung des Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2016, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` | `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `MMag.Dr. Ingrid Fehrer` (person)
- `Ronald Morosow` (person)
- `Schlumbergerstraße 26, 9072 Franzendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `41-331/9010` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136721.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136721.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Einzelrichter über die Beschwerde des Elmar Kaminskij,  Zornberg 50, 2230 Gänserndorf, Österreich, vertreten durch die N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße  68, 8010 Graz, vom 06.04.2022 gegen den Bescheid des Finanzamtes Österreich vom  30.03.2022 betreffend Aussetzung der Einhebung zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `N & N Steuerberatungsgesellschaft m.b.H.` | `N & N Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Elmar Kaminskij` (person)
- `Zornberg 50, 2230 Gänserndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Simon Zieselsberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `MMag. Gerald Erwin Ehgartner` (person)
- `Simon Zieselsberger` (person)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/138980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache OMedR DDr.in Griselda Bultink, vertreten durch Ernst & Young Steuerberatungsgesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 12. Juli 2021 gegen die  Bescheide des Finanzamtes Österreich vom 18. Jänner 2021 bzw. 21. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 bzw. 2019 zu Steuernummer  43-697/2735  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft  m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft  m.b.H.` |

**Missed by this rule (FN):**

- `Mag. Christian Seywald` (person)
- `OMedR DDr.in Griselda Bultink` (person)
- `Finanzamtes Österreich` (organisation)
- `43-697/2735` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/142610.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142610.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Emanuela Ungers  in der Beschwerdesache Christina Dennessen,  Lauzilgasse 37 - 54, 3243 Steghof, Österreich, vertreten durch Treufinanz Wirtschaftstreuhand Gesellschaft m.b.H.,  Sternwartestraße 76, 1180 Wien, über die Beschwerde vom 18. August 2022 gegen die  Bescheide des Finanzamtes Österreich vom 2. Februar 2022 und vom 14. Februar 2022,  Steuernummer 98-034/4594, betreffend Umsatz- und Körperschaftsteuer 2017 bis 2019  beschlossen:   Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Treufinanz Wirtschaftstreuhand Gesellschaft m.b.H.` | `Treufinanz Wirtschaftstreuhand Gesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Dr.in Emanuela Ungers` (person)
- `Christina Dennessen` (person)
- `Lauzilgasse 37 - 54, 3243 Steghof, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `98-034/4594` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/147364.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ramon Launert  in der Beschwerdesache Romana Schnepf,  Hauptgraben 8, 7201 Neudörfl, Österreich, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer  Straße 19, 1220 Wien, über die Beschwerde vom 29. Dezember 2023 gegen die Bescheide des  Finanzamtes für Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr  2013 vom 15. November 2022, für die Jahre 2014 bis 2022 vom 27. September 2023, sowie die  Festsetzung der Sonderzahlung zur Stabilitätsabgabe gemäß § 201 BAO vom 4. Oktober 2023  bzw. über die Beschwerde vom 5. März 2024 gegen den Bescheid des Finanzamtes für  Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr 2023 vom 10.  Jänner 2024, jeweils zur Steuernummer 54-767/5279, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Priv.-Doz. Ramon Launert` (person)
- `Romana Schnepf` (person)
- `Hauptgraben 8, 7201 Neudörfl, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `54-767/5279` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_41`)


Dr. X.Y.“  (BFG-Anm: Fertigung mit unleserlicher Unterschrift und Firmenstampiglie der Kirstin Frischbutter  Wirtschaftstreuhandgesellschaft m.b.H.(nachfolgend Mur-Sanitär GmbH.  In Erledigung dieser Beschwerde erging am 30.Nov.2020 zur Steuernummer (StNr.) der  M.-GmbH eine abweisende Beschwerdevorentscheidung (BVE) an Herrn M. (Direktzustellung  an Herrn M. mit geänderter Bescheidadresse;

**False Positives:**

- `Fertigung mit unleserlicher Unterschrift und Firmenstampiglie der Kirstin Frischbutter  Wirtschaftstreuhandgesellschaft m.b.H.` — partial — gold is substring of pred: `Kirstin Frischbutter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. X.Y.`(person)
- `Kirstin Frischbutter`(person)
- `Mur-Sanitär GmbH`(organisation)
- `M.`(person)
- `M.`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_81`)


Im Jahr 2009 erwarb der Bf von der Firma X M Gesellschaft m.b.H. das Röntgengerät R samt  diversem Zubehör um einen Gesamtkaufpreis von 180.000 Euro.

**False Positives:**

- `Im Jahr 2009 erwarb der Bf von der Firma X M Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Gunderson  in der Beschwerdesache Florentin Mavrakis,  Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich, vertreten durch Intercura Treuhand - und Revisionsgesellschaft m.b.H.,  Langobardenstraße 51 Tür 6, 1220 Wien, über die Beschwerde vom 23. Dezember 2021 gegen  den Bescheid des FA Wien 2/20/21/22  vom 9. Dezember 2021 betreffend Festsetzung eines ersten  Säumniszuschlages, Steuernummer 95-900/0656, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Revisionsgesellschaft m.b.H.` — partial — pred is substring of gold: `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Björn Gunderson`(person)
- `Florentin Mavrakis`(person)
- `Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich`(address)
- `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `95-900/0656`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/137456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Siegfried Herboldt  in der Beschwerdesache der Frau  Erich Vossebrink, Voestalpine-Straße 28, 2813 Pengersdorf, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H.` — partial — pred is substring of gold: `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Siegfried Herboldt`(person)
- `Erich Vossebrink`(person)
- `Voestalpine-Straße 28, 2813 Pengersdorf, Österreich`(address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/138700.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138700.1_4`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) forderte die Zulassungsbe- sitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa. X.  m.b.H., mit Schreiben vom 22. November 2019 gemäß § 2 Wiener Parkometergesetz 2006 auf,  der Behörde binnen zwei Wochen nach Zustellung des Schreibens Auskunft darüber zu  erteilen, wem sie das Fahrzeug am 27. August 2019 um 15:46 Uhr überlassen habe, sodass  dieses in 1150 Wien, Goldschlagstraße 1, stand.

**False Positives:**

- `Fa. X.  m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/138926.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138926.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Joachim Hinz, Faning 9, 4725 Edern, Österreich, vertreten durch Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H., Bauernmarkt 24, 1010 Wien, über die Beschwerde vom 22. Juli 2021 gegen den  Bescheid des Finanzamtes Österreich vom 19. Juni 2021 über die Festsetzung einer  Zwangsstrafe, Steuernummer 35-009/5338, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wirtschaftstreuhand Gesellschaft  m.b.H.` — partial — pred is substring of gold: `Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anna Radschek`(person)
- `Joachim Hinz`(person)
- `Faning 9, 4725 Edern, Österreich`(address)
- `Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `35-009/5338`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/141857.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Helmut Noël, Ziehgrabenweg 48, 3650 Hölltal, Österreich, vertreten durch Steirer, Mika & Comp.  Wirtschaftstreuhandgesellschaft m.b.H., Franz-Josefs-Kai 53/2/10, 1010 Wien, über die  Beschwerden vom 28. September 2022 und 27. Oktober 2022 gegen die Bescheide des  Finanzamtes Österreich vom 28. Juni 2022, 27. September2022, 30. September 2022 und vom  11. Oktober 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 bis 2021,  Steuernummer 82-815/5494, nach Durchführung einer mündlichen Verhandlung am  2. August 2023 in Anwesenheit der Schriftführerin FOIin Andrea Newrkla  I.a. zu Recht erkannt:   a.a.

**False Positives:**

- `Mika & Comp.  Wirtschaftstreuhandgesellschaft m.b.H.` — positional overlap with gold: `Steirer, Mika & Comp.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anna Radschek`(person)
- `Helmut Noël`(person)
- `Ziehgrabenweg 48, 3650 Hölltal, Österreich`(address)
- `Steirer, Mika & Comp.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-815/5494`(tax_number)
- `Andrea Newrkla`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/145671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Hildegard Gromann, Ebersegg 8s, 4223 Rothof, Österreich, vertreten durch pwt pannonische Wirtschaftstreuhand - Gesellschaft m.b.H.,  Hauptstraße 26, 7201 Neudörfl, über die Beschwerde vom 27. August 2021 gegen die  Bescheide des Finanzamtes Österreich vom 29. Juli 2021, betreffend Körperschaftsteuer 2018  und 2019, Steuernummer 80-709/3951  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hildegard Gromann`(person)
- `Ebersegg 8s, 4223 Rothof, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `80-709/3951`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist, ob der Beschwerdeführer (Bf.) infolge der Insolvenz der *** Gesellschaft m.b.H.  (Primärschuldnerin) als ehemaliger Geschäftsführer für die aushaftenden Abgabenschulden zur  Haftung herangezogen werden kann.

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_7`)


Mit Haftungsbescheid vom 22. Mai 2018 wurde der Bf. als ehemaliger Geschäftsführer für die  aushaftende Abgabenschuld der *** Gesellschaft m.b.H.in Höhe von € 43.875,92 in Anspruch  genommen.

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. war ab 14. Jänner 1992 alleiniger Geschäftsführer der *** Gesellschaft m.b.H.  (Primärschuldnerin).

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_114`)


Ergebnis  Auf Grund des Vorliegens der gesetzlichen Voraussetzungen des § 9 Abs. 1 BAO erfolgte somit  die Inanspruchnahme des Bf. als Haftungspflichtiger für die im Spruch genannten  Abgabenschuldigkeiten der *** Gesellschaft m.b.H. im Ausmaß von nunmehr € 6.530,15 zu  Recht.

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Steuerberatungsgesellschaft_entities` 

**F1:** 0.001 | **Precision:** 0.429 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `62478a84`  
**Description:**
Matches long 'Steuerberatungsgesellschaft' entities like 'Tax Wood Audit GmbH Steuerberatungs- und Wirtschaftsprüfungsgesellschaft'.

**Content:**
```
[A-Z][a-zA-Z0-9\s\.\-]+(?:Steuerberatungs-\s+und\s+Wirtschaftspr\u00fcfungsgesellschaft|Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.429 | 0.000 | 0.001 | 7 | 3 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 4 | 6136 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134201.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134201.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterDr. Martin Wittmann in der Beschwerdesache  [...], [...], vertreten durch Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Brockmanngasse 75, 8010 Graz, über die Beschwerde vom  27. Jänner 2017 gegen die Bescheide des Finanzamt Landeck Reutte  jeweils vom 10. Jänner 2017,  Steuernummer 16-981/1693, betreffend Energieabgabenvergütung 2011 -2015 zu Recht  erkannt:   I. Der Bescheid vom 10. Jänner 2017 betreffend Festsetzung des Vergütungsbetrages  nach dem Energieabgabenvergütungsgesetz für das Kalenderjahr 2011 wird  abgeändert.

| Predicted | Gold |
|---|---|
| `Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` | `Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Finanzamt Landeck Reutte` (organisation)
- `16-981/1693` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/140387.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140387.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Daisy Röskens  in der Beschwerdesache KzlR Charlotte Pavelek,  Adr, vertreten durch die XY Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und  Wirtschaftsprüfungsgesellschaft, Adr2, über die Beschwerde vom 14. Juni 2016 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr: Finanzamt Österreich) vom 7. Juni 2016,  StrNr, betreffend   1. die Festsetzung der Normverbrauchsabgabe für den Zeitraum 01/2014 und   2.

| Predicted | Gold |
|---|---|
| `XY Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und  Wirtschaftsprüfungsgesellschaft` | `XY Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und  Wirtschaftsprüfungsgesellschaft` |

**Missed by this rule (FN):**

- `Mag.a Daisy Röskens` (person)
- `KzlR Charlotte Pavelek` (person)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Ingeborg Huellhorst, Untere Tanne 20, 4363 Wetzelsberg, Österreich  USA situiert, Steuernummer  67-628/2057, Tax-Identification-Number: XX1, vertreten durch KPMG Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, vom  9.07.2015 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr  Finanzamt für Großbetriebe) vom 8.05.2015, mit welchen die Anträge auf Rückzahlung von  2009 und 2010 einbehaltener und abgeführter Kapitalertragsteuer gemäß § 21 Abs. 1 Z 1a  KStG 1988, Antragsnummern: A1 und A2, abgewiesen wurden   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KPMG Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` | `KPMG Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Mag. Dieter Fröhlich` (person)
- `Ingeborg Huellhorst` (person)
- `Untere Tanne 20, 4363 Wetzelsberg, Österreich` (address)
- `67-628/2057` (tax_number)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt für Großbetriebe` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache KommR Eckard Gaiss, Bakk. phil., Hietzinger Kai 33, 4132 Lug, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 07-088/5911  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` — partial — pred is substring of gold: `Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Hietzinger Kai 33, 4132 Lug, Österreich`(address)
- `Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `07-088/5911`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

**False Positives:**

- `Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft` — partial — gold is substring of pred: `Erwin Baldauf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof.in Annemarie Wittjen`(person)
- `Samuel Herpel`(person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich`(address)
- `Erwin Baldauf`(person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `Finanzamtes Landeck Reutte`(organisation)
- `39-702/2118`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/134388.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134388.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Ibrahim Carstenn, Reindlsedt 5, 8842 Frojach, Österreich, vertreten durch EURAX Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Nußdorfer Straße 10-12 Tür 4, 1090 Wien, über die Beschwerde vom 27. November 2020  gegen den Bescheid des Finanzamtes Österreich vom 5. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 01-821/9784  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `EURAX Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` — partial — pred is substring of gold: `EURAX Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Carstenn`(person)
- `Reindlsedt 5, 8842 Frojach, Österreich`(address)
- `EURAX Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `01-821/9784`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/144557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  OSR Elfriede Heegmann, Suriaweg 114, 9560 Micheldorf, Österreich, vertreten durch Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerden   vom 9. März 2022 gegen den Bescheid des Finanzamtes Österreich vom  15. November 2021 betreffend Einkommensteuer 2018, und    vom 15. März 2023 gegen den Bescheid des Finanzamtes Österreich vom  17. Februar 2023 betreffend Einkommensteuer 2019,  Steuernummer 62-316/8509, zu Recht erkannt:   I.a.

**False Positives:**

- `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` — partial — pred is substring of gold: `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anna Radschek`(person)
- `OSR Elfriede Heegmann`(person)
- `Suriaweg 114, 9560 Micheldorf, Österreich`(address)
- `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Finanzamtes Österreich`(organisation)
- `62-316/8509`(tax_number)

</details>

---

## `FA_Location_entities` 💣

**F1:** 0.003 | **Precision:** 0.169 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `d5d7525b`  
**Description:**
Matches 'FA' followed by a location (e.g., FA Steiermark Mitte, FA Klosterneuburg) which was previously missed.

**Content:**
```
(?:des|vom|bei|von|der|an|für|\s)(FA\s+(?:Steiermark\s+Mitte|Klosterneuburg|Grieskirchen\s+Wels|Baden|Graz|Wien|Bregenz|Salzburg|Judenburg|Kirchdorf|Bruck|Eisenstadt|Neunkirchen|Waldviertel|Braunau|Innsbruck|Österreich))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.169 | 0.002 | 0.003 | 65 | 11 | 54 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 54 | 5750 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Leitgebel  in der Beschwerdesache ÖkR Achmed von Lampe,  Kreuzbach 25, 6441 Köfels, Österreich, vertreten durch WIRTSCHAFTSTREUHAND Steuerberatung GmbH,  Ohlsdorferstraße 18, 4810 Gmunden, über die Beschwerde vom 31. Jänner 2020 gegen den  Bescheid des FA Steiermark Mitte  vom 28. Jänner 2020 betreffend Abweisung eines Antrages auf  Aussetzung der Einhebung gemäß § 212a BAO, Steuernummer 05-972/9664, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Dr.in Huberta Leitgebel` (person)
- `ÖkR Achmed von Lampe` (person)
- `Kreuzbach 25, 6441 Köfels, Österreich` (address)
- `WIRTSCHAFTSTREUHAND Steuerberatung GmbH` (organisation)
- `05-972/9664` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/135028.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135028.1_8`)


Mit Bescheid vom 13. Juli 2021 wies das FA Innsbruck  dieses COVID-19-Ratenzahlungsansuchen  vom 23. Juni 2021 gemäß § 323e Abs. 2 BAO ab und forderte die Bf. auf, zur Vermeidung von  Einbringungsmaßnahmen die rückständigen Abgabenschuldigkeiten in Höhe von € 118.955,76  bis 20.08.2021 zu entrichten.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/136079.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136079.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Moritz Buerkin, Hofgraben 73, 4633 Straß, Österreich, über die Beschwerde vom 7. November 2012 gegen die Bescheide des FA Waldviertel  vom 5. Oktober 2012 betreffend Einkommensteuer 2006 bis 2009, Steuernummer  57-370/3892, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Missed by this rule (FN):**

- `Moritz Buerkin` (person)
- `Hofgraben 73, 4633 Straß, Österreich` (address)
- `57-370/3892` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/140299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gabriel Riedmiller  in der Angelegenheit der Parteien  Armin Lohwasser, BSc (Bf) und FA Innsbruck  als Amtspartei über die Beschwerde vom 7.2.2022              gegen den Bescheid des Finanzamtes vom 31.1.2022 betreffend Einkommensteuer           2020 (Arbeitnehmerveranlagung)

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Mag. Gabriel Riedmiller` (person)
- `Armin Lohwasser, BSc` (person)
- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_17`)


Verbindungsstelle hat Frau B ab 1.1.2012 bis laufend keine berufliche  Tätigkeit in Deutschland ausgeübt (lt. e-mail des FA Innsbruck v. 20.3.2014).

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/144830.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144830.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Alexander Kazenwadel  in der Beschwerdesache Eckard Langfeld,  Körpersportverein Oase 16, 5211 Friedburg, Österreich, über die Beschwerde vom 24. Dezember 2017 gegen den Bescheid des  FA Innsbruck  vom 15. Dezember 2017 betreffend Zahlungserleichterungen § 212 BAO 15.12.2017  Steuernummer 72-623/4945  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Hon.-Prof. Alexander Kazenwadel` (person)
- `Eckard Langfeld` (person)
- `Körpersportverein Oase 16, 5211 Friedburg, Österreich` (address)
- `72-623/4945` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/144851.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144851.1_13`)


Dem Fahrzeughalter, der FA Steiermark Mitte, wurde in der Folge ein Auftrag zur Lenkernennung erteilt  und anschließend das Verwaltungsstrafverfahren betreffend Parkometerabgabe gegen den  nunmehrigen Bf geführt.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/145271.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145271.1_6`)


Da sich jedoch die Steuerberatungsgesellschaft weder im Einspruch noch davor auf eine  seitens des Bf. für dieses Finanzstrafverfahren erteilte Vollmacht berufen hatte, erließ das  Finanzamt FA Innsbruck  am 10.11.2016 einen Mängelbehebungsauftrag an den Bf., mit welchem  es diesen aufforderte den Mangel des Fehlens der schriftlichen (Original-)Vollmacht zu  beheben.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/145271.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145271.1_11`)


Am 06.04.2017 erließ das Finanzamt FA Innsbruck  als Finanzstrafbehörde einen Bescheid über die  Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens, mit welchem  die im Vollstreckungsverfahren angefallenen Gebühren für die Amtshandlung vom 4. April  2017 und die Auslagenersätze gemäß § 172 Abs. 1 FinStrG, § 185 Abs. 5 FinStrG iVm § 26 der  Abgabenexekutionsordnung (AbgEO) wie folgt festgesetzt wurden:   Pfändungsgebühr Summe 1% von 2.750,00   27,50  Auslagenersätze        1,25  Summe       28,75  Gegen diesen Bescheid erhob der Verteidiger am 04.05.2017 fristgerecht Beschwerde und  führte darin im Wesentlichen Folgendes aus:   Aufgrund mehrerer Beschwerden bzw. mehrerer Aussetzungsanträge gäbe es bis dato keinen  vollstreckbaren Rückstand.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/146442.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146442.1_3`)


Begründung  Mit Erkenntnis des Bundesfinanzgerichts vom 4. Oktober 2024, RV/7102578/2024 wurde die  Bescheidbeschwerde des Revisionswerbers vom 15. September 2023 gegen die Bescheide des  FA Waldviertel  vom 3. Juli 2023 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatz-  und Einkommensteuer 2019, Umsatz- und Einkommensteuer 2019, Aufhebung des  Umsatzsteuerbescheides 2020, Umsatzsteuer 2020, Umsatzsteuer 2021, Aufhebung der  Einkommensteuerbescheide 2020 und 2021, Einkommensteuer 2020 und 2021, sowie vom  23.5.2024 betreffend Umsatzsteuer 2022 abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/148922.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148922.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Moses Vasylevskyy, Koralmblickweg 21, 3661 Lohsdorf, Österreich, vertreten durch Dr. Hugo Mlejnek  Wirtschaftstreuhand- gesellschaft m.b.H., Herrengasse 6-8/1/1, 1010 Wien, vom 28. April 2023  gegen den Bescheid des FA Steiermark Mitte  vom 11. April 2023 betreffend Säumniszuschlag 2023 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Mag. Daniela Regina Denk` (person)
- `Moses Vasylevskyy` (person)
- `Koralmblickweg 21, 3661 Lohsdorf, Österreich` (address)
- `Dr. Hugo Mlejnek  Wirtschaftstreuhand- gesellschaft m.b.H.` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Georgette Dörger  in der Beschwerdesache der  Roland Wüstemeier, Sebastianplatz 167, 3420 Klosterneuburg, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des FA Salzburg-Stadt  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Georgette Dörger`(person)
- `Roland Wüstemeier`(organisation)
- `Sebastianplatz 167, 3420 Klosterneuburg, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Braunau` — partial — pred is substring of gold: `FA Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_29`)


In den gegenständlichen Beschwerdeverfahren, die vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`
- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `FA Salzburg-Land`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_35`)


In den gegenständlichen Beschwerdeverfahren, das vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`
- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `FA Salzburg-Land`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Malik Stellmaszick, Am Weberbach 26, 9640 Gailberg, Österreich, über die Beschwerde vom 19. November 2012 gegen den Bescheid  des FA Wien 1/23 vom 8. November 2012 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2011, Steuernummer 92-110/0462  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Monika Kofler`(person)
- `Malik Stellmaszick`(person)
- `Am Weberbach 26, 9640 Gailberg, Österreich`(address)
- `FA Wien 1/23`(organisation)
- `92-110/0462`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_61`)


Die Ermittlungen im Zuge der Außenprüfung durch das FA Baden Mödling haben ergeben, dass  das Kfz seit dem Kauf im Jahre 2011 nachweislich nie zum Verkauf angeboten wurde, es nie  einen Ausstellungsraum bzw. einen Abstellplatz zur Besichtigung des Fahrzeuges gegeben hat.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Baden Mödling`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133447.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Philipp Harazin  in der Beschwerdesache Priv.-Doz. Kevin Morzinsky,  Strußnighof 37, 9631 Kleinbergl, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Bruck Eisenstadt Oberwart), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 58-060/5953  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Philipp Harazin`(person)
- `Priv.-Doz. Kevin Morzinsky`(person)
- `Strußnighof 37, 9631 Kleinbergl, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `58-060/5953`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_240`)


Dies auch unter  Berücksichtigung des Faktums, dass die Bf. im Jahr 2014 etwa auch für die ST tätig war (vgl.  dazu den von der Bf. vorgelegten Befreiungsbescheid des FA Bruck Eisenstadt Oberwart vom  12.11.2014 für den Zeitraum 10-12/2014 zur Vorlage an diese Gesellschaft).

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Bruck Eisenstadt Oberwart`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_335`)


Nach § 5 Abs. 3 DBA- Entlastungsverordnung kann das Finanzamt Österreich (vorher: FA Bruck Eisenstadt Oberwart)  über Antrag eines abkommensberechtigten Arbeitskräfteüberlassungsunternehmens bei  Vergütungen für die Gestellung von Arbeitskräften zur inländischen Arbeitsausübung zeitlich  befristet durch Bescheid eine Entlastung an der Quelle zulassen, wenn sichergestellt ist, dass  keine Umgehungsgestaltung vorliegt und das ausländische  22 von 25 Seite 23 von 25

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `FA Bruck Eisenstadt Oberwart`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Delia Kavelmann  in der Beschwerdesache Larissa Rastätter,  Wendelgraben 27, 6563 Galtür, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und PhD Isaak Joern wird  abgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Delia Kavelmann`(person)
- `Larissa Rastätter`(person)
- `Wendelgraben 27, 6563 Galtür, Österreich`(address)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)
- `PhD Isaak Joern`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133998.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Imre Wittek  über die Beschwerde des Lara Schwertzel,  Stockinger Straße 23, 4892 Schwandeck, Österreich, vertreten durch Mag. Ingrid Huber, Feldweg 7, 9241 Wernberg, vom  02.01.2017 gegen den Bescheid des Finanzamtes St. Veit Wolfsberg (nunmehr FA Österreich),  dieses vertreten durch Ilse König BA MA, vom 17.03.2016 betreffend Einkommensteuer 2010  (ANV) im fortgesetzten Verfahren den Beschluss gefasst:   Der Vorlageantrag wird gemäß § 264 Abs. 4 lit e BAO iVm § 260 Abs. 1 BAO als verspätet  zurückgewiesen.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Imre Wittek`(person)
- `Lara Schwertzel`(person)
- `Stockinger Straße 23, 4892 Schwandeck, Österreich`(address)
- `Mag. Ingrid Huber`(person)
- `Finanzamtes St. Veit Wolfsberg`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Frederike Bookholdt  in der Beschwerdesache DDr. Dr. Lorenz Wachenhusen,  Am Lurnbichl 4, 4871 Redl, Österreich, vertreten durch Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Eduard-Wallnöfer-Platz 1, 6460 Imst, über die Beschwerde vom  10. Juni 2013 gegen den Bescheid des FA Landeck Reutte (nunmehr FA Österreich) vom 15. Mai  2013, StrNr, betreffend Festsetzung der Normverbrauchsabgabe für den Zeitraum März 2012  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Frederike Bookholdt`(person)
- `DDr. Dr. Lorenz Wachenhusen`(person)
- `Am Lurnbichl 4, 4871 Redl, Österreich`(address)
- `Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_21`)


Die Beschwerde gelte als  fristgerecht eingebracht, wenn diese bis zum 10.09.2018 beim FA Baden-Mödling einlange.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden-Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Baden-Mödling`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Lindermeier  in der Beschwerdesache PhD Jeanne Goethemann, BSc,  Weindlau 45, 4230 Zudersdorf, Österreich, vertreten durch Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH, Stelzhamerstraße 14b, 4400 Steyr, über die Beschwerde vom  14.10.2011 gegen den Bescheid des FA Braunau Ried Schärding  vom 22.9.2011 betreffend Festsetzung von  Verspätungszuschlägen 1/2011 – 7/2011 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `FA Braunau` — partial — pred is substring of gold: `FA Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Walter Lindermeier`(person)
- `PhD Jeanne Goethemann, BSc`(person)
- `Weindlau 45, 4230 Zudersdorf, Österreich`(address)
- `Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Edeltraud Kooper  in der Beschwerdesache des *Bf*,  vertreten durch Rechtsanwälte AB, über die Beschwerde vom 20. November 2017 gegen die  Bescheide des FA Judenburg Liezen  vom 19. Oktober 2015 betreffend Einkommensteuer und  Anspruchszinsen für die Jahre 2005 bis 2008 zu Recht erkannt:  I. Der Beschwerde gegen die Einkommensteuerbescheide für die Jahre 2005 bis 2008  wird teilweise Folge gegeben.

**False Positives:**

- `FA Judenburg` — partial — pred is substring of gold: `FA Judenburg Liezen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof.in Edeltraud Kooper`(person)
- `FA Judenburg Liezen`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wilfried Herzog  in der Beschwerdesache Sheila Girlich, LLB,  Paukenstraße 516, 8272 Neusiedl, Österreich, über die Beschwerden vom 24. März 2018 gegen den Bescheid des FA Braunau Ried Schärding  datiert vom 7. März 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, vom  10. Juni 2020 gegen den Bescheid des Finanzamt Braunau Ried Schärding  datiert vom 12. Mai 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 und ebenfalls vom 10. Juni 2020 gegen  den Bescheid des Finanzamt Braunau Ried Schärding  datiert vom 13. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 13-479/9453  zu Recht erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2013 und 2014 werden gemäß  § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Braunau` — partial — pred is substring of gold: `FA Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Wilfried Herzog`(person)
- `Sheila Girlich, LLB`(person)
- `Paukenstraße 516, 8272 Neusiedl, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `13-479/9453`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_32`)


Mit Beschwerdevorentscheidung vom 25. Juli 2014 hat das FA Wien 2/20/21/22  die Beschwerde als  unbegründet abgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_45`)


Die Franchiseverträge wurden in den  Streitjahren dem FA Wien 2/20/21/22  nicht vorgelegt.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_47`)


Diese hat darauf hin die  Franchisegebühren als umsatzsteuerrechtlich unecht befreit behandelt. Aus der Tatsache, dass  ein Franchisevertrag im Jahr 1998 der Großbetriebsprüfung vorgelegt wurde, ist aber für die  Beschwerdeführerin nichts zu gewinnen, da im Zuge der Veranlagung der Jahre 2005 bis 2009  ein Franchisevertrag nicht vorgelegt wurde und das FA Wien 2/20/21/22  daher im Zuge der  Umsatzsteuerveranlagung der Jahre 2005 bis 2009 keine Kenntnis des gesamten Sachverhaltes  hatte.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Gunderson  in der Beschwerdesache Florentin Mavrakis,  Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich, vertreten durch Intercura Treuhand - und Revisionsgesellschaft m.b.H.,  Langobardenstraße 51 Tür 6, 1220 Wien, über die Beschwerde vom 23. Dezember 2021 gegen  den Bescheid des FA Wien 2/20/21/22  vom 9. Dezember 2021 betreffend Festsetzung eines ersten  Säumniszuschlages, Steuernummer 95-900/0656, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Björn Gunderson`(person)
- `Florentin Mavrakis`(person)
- `Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich`(address)
- `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `95-900/0656`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/136338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136338.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laurentia Wischnowski  in der Beschwerdesache Geraldine Tielschner, MSc,  Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Kitzbühel Lienz (nunmehr: FA Österreich) vom 12. Dezember 2019, SV-Nr,  betreffend die Abweisung des Antrages auf Zuerkennung der Familienbeihilfe (für die Tochter  B) für den Zeitraum Oktober 2018 bis September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Laurentia Wischnowski`(person)
- `Geraldine Tielschner, MSc`(person)
- `Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/137040.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137040.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Alois Steinfeldt  in der Beschwerdesache RgR Meinrad Leibküchler,  Hintersteindl 2, 5122 Kreil, Österreich, vertreten durch UnionTAX & LAW, Donau-City-Straße 7/DC Tower/30th Floor,  1220 Wien, betreffend Säumnisbeschwerde vom 8.4.2022 betreffend Einkommensteuer 2020  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Österreich  beschlossen:    Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.   Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Alois Steinfeldt`(person)
- `RgR Meinrad Leibküchler`(person)
- `Hintersteindl 2, 5122 Kreil, Österreich`(address)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/137686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Lubomir Elsayed  in der Beschwerdesache OMedR OMedR Jana Hammers,  Salvenweg 6, 4720 Oberrühringsdorf, Österreich, Tschechische Republik, über die Beschwerde vom 14. Jänner 2022 gegen den  Bescheid des FA Baden Mödling  vom 10. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 15-221/1221, u Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Lubomir Elsayed`(person)
- `OMedR OMedR Jana Hammers`(person)
- `Salvenweg 6, 4720 Oberrühringsdorf, Österreich`(address)
- `FA Baden Mödling`(organisation)
- `15-221/1221`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/138464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138464.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Constantin Mosmüller  in der Angelegenheit der Parteien   Sean Spies (Beschwerdeführer), vertreten durch die Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH, 1010 Wien und    FA Freistadt Rohrbach Urfahr  als Amtspartei und Gesamtrechtsnachfolger des FA Wien 2/20/21/22 betreffend die  Beschwerde vom 25.9.2020               gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 25.8.2020 betreffend  Abweisung eines Antrages auf Aufhebung des Einkommensteuerbescheides 2017 vom  28.6.2019 gem. § 299 BAO   den Beschluss gefasst:  Der Vorlageantrag des Beschwerdeführers vom 23.8.2022 gegen die  Beschwerdevorentscheidung vom 21.7.2022 über die Beschwerde gegen den Bescheid vom  25.8.2020 über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides  2017 vom 28.6.2019 gem. § 299 BAO   wird als unzulässig zurückgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Constantin Mosmüller`(person)
- `Sean Spies`(person)
- `Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Freistadt Rohrbach Urfahr`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/138666.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138666.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Charlotte Bublies  in der Beschwerdesache des  Mario Bohms, Gruberweg 21, 2372 Gießhübl, Österreich, vertreten durch RA Dr. Rainer Wechselberger, Laubichl 121, 6290  Mayrhofen, über die Beschwerde vom 30. Dezember 2014 gegen die Bescheide des FA Bruck Eisenstadt Oberwart  vom 24. November 2014 betreffend Festsetzung der Normverbrauchsabgabe und Festsetzung  eines Verspätungszuschlages für den Zeitraum 06/2010 sowie Festsetzung der  Kraftfahrzeugsteuer für die Monate 06-12/2010, 01-12/2011, 01-12/2012, 01-12/2013 und 01-

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Charlotte Bublies`(person)
- `Mario Bohms`(person)
- `Gruberweg 21, 2372 Gießhübl, Österreich`(address)
- `RA Dr. Rainer Wechselberger`(person)
- `FA Bruck Eisenstadt Oberwart`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_39`)


Zur Klärung dieser Rechtsfrage wurde vom Fachbereich des FA  Wien 9/18/19 Klosterneuburg eine Anfrage (v. 26.11.2015) an den BUNDESWEITEN  FACHBEREICH gestellt. Im Rahmen der Schlussbesprechung wird von Seiten der Betriebsprüfung  von Lösung 2 ausgegangen - der Fremdwährungskursverlust im Jahr 2014 wird zur Gänze nicht  anerkannt.

**False Positives:**

- `FA  Wien` — partial — pred is substring of gold: `FA  Wien 9/18/19`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA  Wien 9/18/19`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/140065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140065.1_3`)


Begründung  Mit Erkenntnis des Bundesfinanzgerichtes vom 28.12.2022, RV/6100260/2013 u.a. wurde die  Bescheidbeschwerde der Revisionswerberin vom 14. April 2008 gegen den Bescheid des  Finanzamtes Österreich vom 14. März 2008 betreffend Umsatzsteuer 2006, die Beschwerden  vom 27.03.2013 gegen die Bescheide des FA Salzburg-Stadt (nunmehr FA Österreich) vom  17.12.2012 betreffend die Wiederaufnahme des Verfahrens für Umsatzsteuer für 2005 sowie  die Umsatzsteuer für 2005, 2007, 2008 und 2009 und die Körperschaftsteuer für 2008 und  2009, sowie die Beschwerden vom 31.03.2015 gegen die Bescheide des FA Salzburg-Stadt  (nunmehr FA Österreich) vom 12.03.2015 betreffend Umsatzsteuer 2010, 2011, 2012 und 2013  und die Körperschaftsteuer für 2010, 2011, 2012 und 2013 als unbegründet abgewiesen.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Stadt`
- `FA Österreich` — no gold match — likely missing annotation
- `FA Salzburg` — similar text (different position): `FA Salzburg-Stadt`
- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Finanzamtes Österreich`(organisation)
- `FA Salzburg-Stadt`(organisation)
- `FA Salzburg-Stadt`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/140074.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140074.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Miroslav Egermeyer  in der Beschwerdesache Luigi Oberhettinger,  Dittersdorf 233, 9911 St. Justina, Österreich, vertreten durch Adelsberger & Thaler Steuerberatungsgesellschaft OG,  Oberndorferstraße 44, 6322 Kirchbichl über die Beschwerde vom 13. November 2020 gegen  den Bescheid des FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 6. November 2020  betreffend Einkommensteuer 2013 (Berichtigung gem § 293b BAO zu Bescheid vom  19.6.2019), Steuernummer 32-372/7905, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Miroslav Egermeyer`(person)
- `Luigi Oberhettinger`(person)
- `Dittersdorf 233, 9911 St. Justina, Österreich`(address)
- `Adelsberger & Thaler Steuerberatungsgesellschaft OG`(organisation)
- `FA Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `32-372/7905`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Andrea Drom  in der Beschwerdesache Corbinian Neumetzler,  Am Haidbach 19, 9620 Obervellach, Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des FA Graz-Stadt  vom  12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer  85-520/0851, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Univ.-Prof. Andrea Drom`(person)
- `Corbinian Neumetzler`(person)
- `Am Haidbach 19, 9620 Obervellach, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `85-520/0851`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/141760.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141760.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Fabian Krempin  in der Beschwerdesache Viktoria Baumanns,  Augustin-Weigl-Weg 63, 8452 Mantrach, Österreich, über die Beschwerde vom 2. August 2021 gegen den Bescheid des FA Salzburg-Land  vom 27. Juli 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 50-365/5500,   zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Fabian Krempin`(person)
- `Viktoria Baumanns`(person)
- `Augustin-Weigl-Weg 63, 8452 Mantrach, Österreich`(address)
- `FA Salzburg-Land`(organisation)
- `50-365/5500`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/142044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142044.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Nicola Theodoros  in der Beschwerdesache Olaf Gmehlin, Bakk. rer. nat.,  Zimmererweg 2, 3601 Rothenhof, Österreich  betreffend die Beschwerde vom 7. August 2015, eingelangt am 12. August  2015, gegen den Bescheid des FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 8. Juli 2015 zu  Steuernummer 61-001/0419, mit dem der Antrag vom 23. Februar 2015 auf Bewilligung  der Aussetzung der Einhebung gemäß § 212a BAO abgewiesen wurde, beschlossen:  Die Beschwerde wird gemäß § 278 Abs. 1 lit. b BAO in Verbindung mit § 261 Abs. 1 lit. a BAO  als gegenstandslos erklärt.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Nicola Theodoros`(person)
- `Olaf Gmehlin, Bakk. rer. nat.`(person)
- `Zimmererweg 2, 3601 Rothenhof, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `61-001/0419`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/143536.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Mittermayer  in der Beschwerdesache Brendon Giese,  Schaumboden 25, 8253 Riegersbach, Österreich, über die Beschwerde vom 23. September 2022 gegen den Bescheid des  FA Wien 1/23  vom 25. August 2022 betreffend Einkommensteuer 2021, Steuernummer  04-144/4077, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Martin Mittermayer`(person)
- `Brendon Giese`(person)
- `Schaumboden 25, 8253 Riegersbach, Österreich`(address)
- `FA Wien 1/23`(organisation)
- `04-144/4077`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Judith Brocks  in der Beschwerdesache des  VetR Stephanie Kabak, Zennergasse 325, 9360 Engelsdorf, Österreich, über die Beschwerde vom 12. Juli 2023 gegen den Bescheid des  FA Graz-Stadt  vom 21. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  zu Steuernummer 70-314/9067  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Judith Brocks`(person)
- `VetR Stephanie Kabak`(person)
- `Zennergasse 325, 9360 Engelsdorf, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `70-314/9067`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/144589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144589.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Gerhard Kanzy  in der Angelegenheit der Parteien  VN1 Bf (Beschwerdeführerin), vertreten durch Herrn Dr. Walter Ganster, StB in 9100  Völkermarkt und FA Baden Mödling  als Amtspartei und als Gesamtrechtsnachfolger des Finanzamtes  FAA über die Beschwerde vom 2.5.2019 gegen den Bescheid des Finanzamtes FAA vom 3.4.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Gerhard Kanzy`(person)
- `Dr. Walter Ganster`(person)
- `FA Baden Mödling`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/144862.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144862.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jean Kirchhuber  in der Beschwerdesache Jolanda Wuebben,  Paul Hörbiger-Straße 19, 4882 Traschwandt, Österreich, über die Beschwerde vom 26. April 2019 gegen den Bescheid des ehemaligen   FA Graz-Stadt  vom 29. März 2019, nunmehr Finanzamt Österreich DS *** , betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 Steuernummer 55-933/2352  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Jean Kirchhuber`(person)
- `Jolanda Wuebben`(person)
- `Paul Hörbiger-Straße 19, 4882 Traschwandt, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `55-933/2352`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/145179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dario Ribbeck  in der Beschwerdesache Otto Koschinski,  Stockham 43, 3334 Gaflenz, Österreich, vertreten durch Dr. Michael Kotschnigg, Stadlauer Straße 39/I/Top12, 1220  Wien, über die Beschwerde vom 13. Februar 2023 gegen den Bescheid über die Festsetzung  von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens des FA Wien 8/16/17  vom  11. Jänner 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien` — partial — pred is substring of gold: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dario Ribbeck`(person)
- `Otto Koschinski`(person)
- `Stockham 43, 3334 Gaflenz, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `FA Wien 8/16/17`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/146565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Silvester Hobe  in der Beschwerdesache Rainer Vollmari,  Zeltschacher Straße 85, 6410 Mösern, Österreich, über die Beschwerde vom 5. April 2024 gegen den Bescheid des FA Salzburg-Land  vom  11. März 2024 betreffend die Festsetzung eines ersten Säumniszuschlag zur Steuernummer  41-803/5842  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Silvester Hobe`(person)
- `Rainer Vollmari`(person)
- `Zeltschacher Straße 85, 6410 Mösern, Österreich`(address)
- `FA Salzburg-Land`(organisation)
- `41-803/5842`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/146640.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die VorsitzendeRi_1, die beisitzende Richterin Ri_2 und die  fachkundigen Laienrichterinnen Ri_3 und Ri_4 in der Beschwerdesache der Dontalcon-Getränke, Im Urtel 11, 9871 Pirk, Österreich, vertreten durch Hadaier Wirtschaftsprüfungs- und Steuerberatungs-GmbH,  Keplerstraße 1, 4910 Ried im Innkreis, über die Beschwerde vom 13. September 2023 gegen  den Bescheid des FA Salzburg-Land  vom 24. August 2023 über die Abweisung eines Antrages auf  Freigabe einer Fahrzeugidentifikationsnummer in der Genehmigungsdatenbank und über die  Beschwerde vom 12. Oktober 2023 gegen den Bescheid des FA Salzburg-Land  vom 2. Oktober 2023  über die Festsetzung der Normverbrauchsabgabe für den Zeitraum 01/2023 zu Steuernummer  73-990/7390  nach Durchführung einer mündlichen Verhandlung am 19. Dezember 2024 G  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Abweisung eines Antrages auf  Freigabe einer Fahrzeugidentifikationsnummer in der Genehmigungsdatenbank  wird als unbegründet abgewiesen.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`
- `FA Salzburg` — similar text (different position): `FA Salzburg-Land`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dontalcon-Getränke`(organisation)
- `Im Urtel 11, 9871 Pirk, Österreich`(address)
- `Hadaier Wirtschaftsprüfungs- und Steuerberatungs-GmbH`(organisation)
- `FA Salzburg-Land`(organisation)
- `FA Salzburg-Land`(organisation)
- `73-990/7390`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/146640.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146640.1_2`)


II. Die Beschwerde gegen den Bescheid des FA Salzburg-Land  vom 2.10.2023 über die  Festsetzung der Normverbrauchsabgabe für den Zeitraum 01/2023 wird als  unbegründet abgewiesen.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Salzburg-Land`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/146640.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146640.1_155`)


Soweit Organe des Zollamts  Österreich oder des Amts für Betrugsbekämpfung Maßnahmen im Sinne dieses Absatzes setzen,  ist ihr Handeln dem FA Salzburg-Land  zuzurechnen.“

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Salzburg-Land`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/147007.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147007.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Manfred Thumshirn  in der Beschwerdesache OStR Thassilo Schickschneit,  Zwergental 13y, 4625 Vornholz, Österreich, vertreten durch PwC PricewaterhouseCoopers Wirtschaftsprüfung und  Steuerberatung GmbH, Donau-City-Straße 7, 1220 Wien, über die Beschwerde vom 22. Mai  2023 gegen den Bescheid des FA Salzburg-Stadt  vom 20. April 2023 betreffend  Gruppenfeststellungsbescheid 2020 zur Steuernummer 67-195/8882  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `FA Salzburg` — partial — pred is substring of gold: `FA Salzburg-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Manfred Thumshirn`(person)
- `OStR Thassilo Schickschneit`(person)
- `Zwergental 13y, 4625 Vornholz, Österreich`(address)
- `PwC PricewaterhouseCoopers Wirtschaftsprüfung und  Steuerberatung GmbH`(organisation)
- `FA Salzburg-Stadt`(organisation)
- `67-195/8882`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/147515.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147515.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Jaden Thill  in der Beschwerdesache Elisabeth Grieß,  Obertösens 77, 4614 Au an der Traun, Österreich, über die Beschwerde vom 30. Dezember 2016 gegen die Bescheide des  FA Baden Mödling  vom 6. Dezember 2016 und vom 10. April 2017 betreffend Wiederaufnahme der  Verfahren betreffend Einkommensteuer für die Jahre 2010 bis 2014 sowie betreffend  Einkommensteuer 2010 bis 2014 sowie den Bescheid vom 22. März 2017 betreffend  Einkommensteuer 2015, Steuernummer 29-425/6527, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Jaden Thill`(person)
- `Elisabeth Grieß`(person)
- `Obertösens 77, 4614 Au an der Traun, Österreich`(address)
- `FA Baden Mödling`(organisation)
- `29-425/6527`(tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/148272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148272.1_73`)


Die Begründung des FA Graz-Stadt wonach im Jahre 2021 die Steuerberatungskosten verglichen  mit den Vorjahren angewachsen sind ist nicht nachvollziehbar.

**False Positives:**

- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Graz-Stadt`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/148705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148705.1_80`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das FA Judenburg Liezen  hat nicht  zu erfolgen.

**False Positives:**

- `FA Judenburg` — partial — pred is substring of gold: `FA Judenburg Liezen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamt für Soziales und  Behindertenwesen`(organisation)
- `FA Judenburg Liezen`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Verena Khalidi  in der Beschwerdesache MedR Fiona Davydova,  St.-Anna-Park 16i, 5274 Unterhartberg, Österreich, vertreten durch Liepert Greussing Sturm Steuerberatung GmbH & Co KG,  Mühlgasse 21, 6700 Bludenz, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid  des FA Baden Mödling  vom 10. Jänner 2018 betreffend Haftungs- und Abgabenbescheid 2016  Steuernummer 96-418/3627  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung  teilweise Folge gegeben.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Verena Khalidi`(person)
- `MedR Fiona Davydova`(person)
- `St.-Anna-Park 16i, 5274 Unterhartberg, Österreich`(address)
- `Liepert Greussing Sturm Steuerberatung GmbH & Co KG`(organisation)
- `FA Baden Mödling`(organisation)
- `96-418/3627`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_325`)


Beschwerdegegenstand ist die Berufung gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 18.04.2013, mit welchem der Antrag vom 12.02.2013 auf Rückerstattung von KESt, einer  erklärt beschränkt steuerpflichtigen Antragstellerin, die mit einer inländischen Körperschaft  gemäß § 1 Abs. 3 Z. 1 KStG 1988 objektiv vergleichbar sei und die wegen der Steuerbefreiung  im Ansässigkeitsstaat USA die österreichische KESt nicht anrechnen könne (und auf Grund  Kapitalverkehrsfreiheit gem. Art 63 AEUV keine finale KESt-Belastung zulässig sei), gemäß § 21  Abs. 1 Z. 1a KStG 1988 als unbegründet abgewiesen wurde.

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Bruck Eisenstadt Oberwart`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_342`)


Anträge nach § 21 Abs. 1 Z. 1a KStG  1988 fielen im Zeitpunkt der Antragstellung und Entscheidung der Abgabenbehörde im Jahr  2013 nach § 18 Abs. 1 Z. 2 AVOG 2010 in die örtliche Sonderzuständigkeit des FA Bruck  Eisenstadt Oberwart, während für Rückerstattungsanträge gemäß § 41 InvFG diese spezielle  Zuständigkeitsregelung nicht zur Anwendung gekommen ist, sondern sich die Zuständigkeit  nach § 23 AVOG für Angelegenheiten der Abzugssteuern beschränkt Steuerpflichtiger und der  Subsidiärzuständigkeit nach § 25 Z. 3 AVOG richtete (vgl. dazu auch die angeführt EAS 3013).

**False Positives:**

- `FA Bruck` — partial — pred is substring of gold: `FA Bruck  Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Bruck  Eisenstadt Oberwart`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_107`)


Dieses  Erkenntnis erging an die Bf und das FA Österreich, obwohl das FA für Großbetriebe zuständig  gewesen wäre.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt_StandAlone` 💣

**F1:** 0.001 | **Precision:** 0.088 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a0aff64a`  
**Description:**
Matches standalone 'Finanzamt Österreich' or 'Finanzamt' at the start of a sentence or after specific punctuation.

**Content:**
```
(?:^|\.|\(|\[)(Finanzamt(?:\s+Österreich)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.088 | 0.000 | 0.001 | 34 | 3 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 31 | 6272 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_53`)


Finanzamt Österreich  § 323b Abs. 1 bis 3 BAO lautet i. d. F. BGBl. I Nr. 99/2020 (2. FORG)  § 323b.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/147128.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147128.1_32`)


Die belangte Behörde (Finanzamt Österreich) legte die Beschwerde dem Bundesfinanzgericht  am 2. Juli 2024 vor und erstattete einen mit 2. Juli 2024 datierten Vorlagebericht, in welchem  zu einigen Streitpunkten der Bf. gefolgt wird bzw. teilweise gefolgt wird.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_84`)


Dass die Registerbehörde (Bundesminister für Finanzen) nicht mit jener Behörde übereinstimmt,  die für die Festsetzung von Zwangsstrafen zuständig ist (Finanzamt Österreich; vor dem Finanz- Organisationsreformgesetz, BGBl. I Nr. 104/2019: jenes Finanzamt, das zur Erhebung der  Abgaben vom Einkommen des Rechtsträgers örtlich zuständig ist oder gemäß § 1 Abs. 2 Z 3  KStG 1988 zuständig wäre), kann daran nichts ändern, da die vom Finanzamt festzusetzende  Zwangsstrafe eben gerade dazu dienen soll, die Meldung an die Registerbehörde vorzunehmen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_256`)


Finanzamtsvertreter: Keine Ergänzungen.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_280`)


Finanzamtsvertreter: Das Finanzamt hat dazu weitgehend Stellung genommen im  Vorlagebericht.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_465`)


Finanzamtsvertreter: Ich habe da Rechnungen aus 2012.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_543`)


Finanzamtsvertreter: Ich darf hinweisen auf die Niederschrift, auf Seite 7, wo ausgeführt  wurde, was auf den Rechnungen darauf ist und was nicht.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_550`)


Finanzamtsvertreter: Es hat ein Auskunftsersuchen nach Deutschland gegeben und es sind von  dort die Rechnungen übermittelt worden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_148`)


Finanzamtsvertreter: Nein, es ist alles gesagt, was ich sagen wollte.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_165`)


Finanzamtsvertreter: Wissen sie ab wann nichts mehr in Papierform vorgelegt worden ist?

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_168`)


Finanzamtsvertreter: Ich glaube nachher ist nichts mehr gekommen.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_188`)


Finanzamtsvertreter: Das heißt, sie sind erst nach der BP dazu gestoßen?

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_222`)


Finanzamtsvertreter: Noch dazu hatten wir die Verfahren 2011 bis 2015, da war das alles noch  weiter in der Vergangenheit.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_15`)


Im gegenständlichen Fall wurde das Guthaben von EUR  3.114,19 mit 09.01.2014 von StNr. 10-15-453/7249 (Finanzamt für Gebühren,  Verkehrsteuern und Glücksspiel) auf StNr. 08 (Finanzamt Wien 12/13/14 Purkersdorf)  überrechnet, um fällige Abgabenrückstände zu tilgen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt für Gebühren`
- `Finanzamt` — similar text (different position): `Finanzamt für Gebühren`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `10-15-453/7249`(tax_number)
- `Finanzamt für Gebühren`(organisation)
- `Finanzamt Wien 12/13/14 Purkersdorf`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_57`)


Wie schon die belangte Behörde richtig ausgeführt hat wurde im gegenständlichen Fall das  Guthaben von EUR 3.114,19 mit 09.01.2014 von StNr. 10-15-453/7249 (Finanzamt für  Gebühren, Verkehrsteuern und Glücksspiel) auf StNr. 08 (Finanzamt Wien 12/13/14  Purkersdorf) überrechnet, um fällige Abgabenrückstände zu tilgen, sodass zum Fälligkeitstag  der Gebühren 07/2014 kein entsprechendes Guthaben auf dem Abgabenkonto mehr bestand.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt für  Gebühren`
- `Finanzamt` — similar text (different position): `Finanzamt für  Gebühren`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `10-15-453/7249`(tax_number)
- `Finanzamt für  Gebühren`(organisation)
- `Finanzamt Wien 12/13/14  Purkersdorf`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_23`)


Finanzamt eine Auszahlungsbestätigung betreffend Rehabilitationsgeld ab 8. Juni 2016 bis 31.  Dezember 2018.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_38`)


Finanzamt gemäß Art. 18 Abs 1 B-VG  (Legalitätsprinzip) an bestehende und ordnungsgemäß kundgemachte Gesetze gebunden ist.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134840.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134840.1_40`)


Finanzamts liegt über die behauptete Auskunftserteilung kein  Aktenvermerk vor.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134840.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134840.1_65`)


Finanzamtes liegt über die behauptete Auskunftserteilung kein  Aktenvermerk vor.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_40`)


Hinsichtlich ihres Zurückweisungsantrages führte die belangte Behörde aus, indem der an das  „Finanzamt für Gebühren und Verkehrssteuern, Marxergasse 4, 4810 Gmunden“ gerichtete  Vorlageantrag am 28. Dezember 2018 beim Finanzamt Gmunden Vöcklabruck einlangte, dieses  Finanzamt jedoch sachlich und örtlich unzuständig gewesen sei und infolge Weiterleitung an  das zuständige Finanzamt (Finanzamt für Gebühren, Verkehrssteuern und Glücksspiel,  Marxergasse 4,1030 Wien) bei diesem am 18. Jänner 2019 einlangte, die Rechtsmittelfrist beim  Einlangen bereits verstrichen sei und der Vorlage Antrag somit als nicht rechtzeitig eingebracht  anzusehen sei.

**False Positives:**

- `Finanzamt` — similar text (different position): `Finanzamt für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt für Gebühren`(organisation)
- `Finanzamt Gmunden Vöcklabruck`(organisation)
- `Finanzamt für Gebühren`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_108`)


Sofern die belangte Behörde in ihrer Stellungnahme vom 12. Juli 2022 ergänzend ausführt, im  Vorlageantrag vom 28. Dezember 2018 sei durch die Bezeichnung „Finanzamt für Gebühren  und Verkehrsteuern“ ein nicht existentes Finanzamt genannt worden, da die  Behördenbezeichnung „Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel“ laute, ist sie  auf die im Akt befindliche Kopie jenes Kuverts mit dem der Vorlageantrag an die zuständige  Abgabenbehörde (Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel) weitergeleitet zu  verweisen.

**False Positives:**

- `Finanzamt` — similar text (different position): `Finanzamt für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt für Gebühren`(organisation)
- `Finanzamt für Gebühren`(organisation)
- `Finanzamt für Gebühren`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_109`)


Hier wird die Behörde im Adressfeld durch das weiterleitende Amt (Finanzamt  Gmunden Vöcklabruck) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt  Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Gmunden Vöcklabruck`(organisation)
- `Finanzamt für Gebühren`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_7`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Camilla Schiedmann (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Camilla Schiedmann`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/140478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140478.1_26`)


Diesbezüglich wurden drei  Grundbuchsauszüge übermittelt, aus denen die auf den Eigentumsanteilen des  Beschwerdeführers lastenden Pfandrechte zu Gunsten der Republik Österreich (Finanzamt  Salzburg-Stadt) ersichtlich sind.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt  Salzburg-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Salzburg-Stadt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_190`)


Bindung an die Gutachten des Sozialministeriumservice   Die Beihilfenbehörden (Finanzamt), und auch das Gericht, haben bei ihrer Entscheidung von  dieser durch ärztliche Gutachten untermauerten Bescheinigung auszugehen und sind an die  Gutachten des SMS gebunden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_25`)


Finanzamt auf "Auszahlung der gewährten  Familienbeihilfe" für die Kinder: A, geb. 11/2012;

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_103`)


Finanzamt Innsbruck hierauf im Verfahren und bei der Entscheidung Rücksicht zu nehmen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Innsbruck`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_336`)


Finanzamt so vorzugehen, als ob Fr. B die betr.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_119`)


In diesem Anschlag wurde auch bekannt  gegeben, bei welcher Behörde (Finanzamt Waldviertel) bis wann (16. März 2007) ein  Rechtsmittel gegen die festgestellten Ergebnisse der Bodenschätzung von den Eigentümern der  betreffenden Grundstücke erhoben werden kann.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Waldviertel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Waldviertel`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/144862.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144862.1_16`)


Der Mängelbehebungsauftrag des ehem.Finanzamtes v. 10.07.2019 (Team AV 01) hatte  folgenden Wortlaut:  „Ihre Beschwerde vom 26.04.2019 gegen den Einkommensteuerbescheid vom 29.03.2019 weist  hinsichtlich dem Fehlen eines Inhaltserfordernisses die nachfolgenden Mängel auf:   Fehlen eines Inhaltserfordernisses gemäß § 250 Abs. 1 BAO  - Eine Erklärung, in welchen Punkten der Bescheid angefochten wird  - Eine Erklärung, welche Änderungen beantragt werden-

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_156`)


Bindung an die Gutachten des Sozialministeriumservice  Die Beihilfenbehörden (Finanzamt), und auch das Gericht, haben bei ihrer Entscheidung von  dieser durch ärztliche Gutachten untermauerten Bescheinigung auszugehen und sind an die  Gutachten des SMS gebunden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/148033.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148033.1_22`)


Finanzamtes im Kalenderjahr 2007  eine Teilwertabschreibung, welche eine Abschreibung in Höhe von 139.180,25 auf sieben Jahre  vorsieht, zu Unrecht vorgenommen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)

</details>

---

## `Specific_Company_AGG_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7b01cd2c`  
**Description:**
Matches specific known company names ending in AG that were missed or partially matched.

**Content:**
```
(?:Kraftost-Digital AG|Versand Seewil|Bruckdon-Cloud|I AG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Company_GmbH_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e051b45`  
**Description:**
Matches specific known GmbH entities and those with '&' or complex structures.

**Content:**
```
(?:xx GmbH Steuerberatung und Wirtschaftspr\u00fcfung|yy Wirtschaftstreuhand Gesellschaft mbH|Kantner Wirtschaftstreuhand und\s+Steuerberatungs GmbH|Novotny Getr\u00e4nke GmbH|Hellfritsch Immobilien GmbH)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Snajdr_ECommerce_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `141a99ee`  
**Description:**
Matches the specific entity 'Snajdr E-Commerce GmbH' which was frequently missed.

**Content:**
```
Snajdr\s+E[\u2011\-]Commerce\s+GmbH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fa_Glanzder_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f807fb3e`  
**Description:**
Matches 'Fa.Glanzder-Automotive GmbH' and 'Glanzder-Automotive GmbH' without requiring 'Firma' prefix, ensuring 'Fa.' is included if present.

**Content:**
```
(?:Fa\.)?Glanzder\-Automotive\s+GmbH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Jackobi_Horbank_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `171b7529`  
**Description:**
Matches 'Jackobi und Horbank KI GmbH' without requiring 'Firma' prefix.

**Content:**
```
Jackobi\s+und\s+Horbank\s+KI\s+GmbH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Weinzinger_Partner_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2b469ebb`  
**Description:**
Matches 'Weinzinger und Partner Steuerberater GmbH' which was missed.

**Content:**
```
Weinzinger\s+und\s+Partner\s+Steuerberater\s+GmbH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt_Wien_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c700fcb8`  
**Description:**
Matches 'Stadt Wien' and 'Magistrats der Stadt Wien' which were missed.

**Content:**
```
(?:Magistrats\s+der\s+)?Stadt\s+Wien
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hoch_IT_GmbH_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1890fb15`  
**Description:**
Matches 'Hoch-IT GmbH' specifically to prevent truncation to 'IT GmbH'.

**Content:**
```
Hoch-IT\s+GmbH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Derdonal_Garten_AG_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `36f8bf34`  
**Description:**
Matches 'Derdonal-Garten AG' specifically to prevent truncation to 'Garten AG'.

**Content:**
```
Derdonal-Garten\s+AG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SK_Telecom_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f1fc186b`  
**Description:**
Matches SK Telecom variations (Co. Ltd, Co Ltd) which were previously missed.

**Content:**
```
(?:SK\s+Telecom(?:\s+Co\.?\s+Ltd)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deutsche_Telekom_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `20078a94`  
**Description:**
Matches Deutsche Telekom AG and its genitive form 'Deutschen Telekom AG'.

**Content:**
```
(?:Deutsche(?:n)?\s+Telekom\s+AG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `T-Mobile_Austria_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7cf18abc`  
**Description:**
Matches T-Mobile Austria GmbH specifically to avoid truncation to 'Mobile Austria GmbH'.

**Content:**
```
(?:T-Mobile\s+Austria\s+GmbH)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `A1_Hutchinson_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9ae4dc54`  
**Description:**
Matches A1 Telekom Austria AG and Hutchinson Drei Austria GmbH.

**Content:**
```
(?:A1\s+Telekom\s+Austria\s+AG|Hutchinson\s+Drei\s+Austria\s+GmbH)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Post_AG_entities` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ecef28db`  
**Description:**
Matches 'Post AG' specifically to catch the missed entity.

**Content:**
```
\bPost\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 5662 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_25`)


Zusätzlich legte er eine Quittung der Österreichische Post AG vom  11.11.2019 über einen per Einschreiben versendeten Brief bei.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_30`)


In der Beilage befand sich neben der mit 8.11.2019 datierten Beschwerde und der bereits  vorgelegten Quittung vom 11.11.2019 auch ein Schreiben der Österreichische Post AG vom  24.2.2020 betreffend Nachforschung zur Aufgabenummer Nr. mit Aufgabedatum 11.11.2019.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_33`)


Zur Rechtzeitigkeit der Beschwerde führte die Vertreterin des Finanzamtes in der Stellung- nahme aus, dass der Beweis des tatsächlichen Einlangens des Kuverts mit der Aufgabenummer  Nr. mit dem vorgelegten Schreiben der Österreichische Post AG vom 24.2.2020 erbracht  worden sei.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Österreichische Post AG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_49`)


Nach den Ausführungen im Vorlagebericht geht die Abgabenbehörde davon aus, dass dem Bf.  der Beweis des tatsächlichen rechtzeitigen Einlangens des Kuverts (mit der darin enthaltenen  Beschwerde) mit dem vorgelegten Schreiben der Österreichische Post AG vom 24.2.2020  gelungen sei.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_26`)


Die Strafverfügung sei nach  einem erfolglosen Zustellversuch bei der zuständigen Geschäftsstelle des Zustelldienstes  Österreichische Post AG hinterlegt worden.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_185`)


Über dem Adressfeld findet sich der Vermerk: „Österreichische Post AG, Briefsendung Bar  freigemacht“ und zusätzlich keine weiteren Angaben.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_188`)


Dieser Bescheid der Ärztekammer Salzburg enthält über dem Adressfeld zusätzlich zum  Vermerk: „Österreichische Post AG, Briefsendung Bar freigemacht2 den unterstrichenen  Hinweis „Einschreiben“.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_191`)


Dazu muss die Sendungsnummer auf der Website der Österreichischen  Post AG in der Rubrik „Sendungsverfolgung“ eingeben.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen  Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen  Post AG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/144827.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144827.1_135`)


Eigenbetriebene Post-Geschäftsstellen werden von der Österreichische Post AG mit  eigenem Personal betrieben;

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/144827.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144827.1_136`)


fremdbetriebene Post-Geschäftsstellen werden von einem  Dritten aufgrund einer vertraglichen Vereinbarung mit der Österreichische Post AG geführt.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/144827.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144827.1_138`)


Da bei der [Postpartner], [Adresse Postdienstleister], aufgrund einer vertraglichen  Vereinbarung mit der Österreichische Post AG Postsendungen abgebeben und abgeholt  werden können, handelt es sich auch bei dieser um eine Post-Geschäftsstelle im Sinne des § 17  Abs. 1 ZustG.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/146521.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146521.1_60`)


Die Feststellungen zu den Postgebühren gründen sich auf die Angaben der belangten Behörde  zu den von der Österreichischen Post AG verrechneten Postgebühren im Zeitraum April 2024.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen Post AG`(organisation)

</details>

---

## `SNWG_Textil_GmbH_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d4ae88a`  
**Description:**
Matches 'SNWG Textil GmbH' specifically to catch the missed entity.

**Content:**
```
\bSNWG\s+Textil\s+GmbH\b
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

