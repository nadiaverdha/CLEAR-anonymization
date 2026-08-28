# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-28T12:08:27.564274

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-28_v5/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 200 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 160 |
| Validation documents | 40 |
| Test documents | 792 |
| Train sentences | 2631 |
| Validation sentences | 631 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 150 |
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
| Accuracy (exact match) | 97.7% |
| True Positives | 15544 |
| False Positives | 620 |
| False Negatives | 2453 |
| Total Gold Entities | 17997 |
| Micro Precision | 96.2% |
| Micro Recall | 86.4% |
| Micro F1 | 91.0% |
| Macro F1 | 91.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Finanzpolizei_entities` | 0.4% | 100.0% | 0.2% | 37 | 37 | 0 |
| `KAG_entities` | 0.1% | 100.0% | 0.1% | 13 | 13 | 0 |
| `KPMG_full_name` | 0.0% | 100.0% | 0.0% | 3 | 3 | 0 |
| `Pensionsversicherungsanstalt` | 0.7% | 100.0% | 0.3% | 62 | 62 | 0 |
| `Universität_Wien` | 0.2% | 100.0% | 0.1% | 21 | 21 | 0 |
| `BMI_Abbreviation` | 0.1% | 100.0% | 0.1% | 13 | 13 | 0 |
| `Gerichtshof_Europaeischen_Union` | 0.3% | 100.0% | 0.2% | 27 | 27 | 0 |
| `Verwaltungsgerichtshof_entities` | 32.0% | 100.0% | 19.1% | 3429 | 3429 | 0 |
| `Verfassungsgerichtshof_entities` | 2.4% | 100.0% | 1.2% | 218 | 218 | 0 |
| `Verwaltungsgericht_Wien` | 0.1% | 100.0% | 0.0% | 7 | 7 | 0 |
| `Ernst_Young_GmbH` | 0.0% | 100.0% | 0.0% | 3 | 3 | 0 |
| `COFAG_Organization` | 0.1% | 100.0% | 0.1% | 13 | 13 | 0 |
| `BHAG_Organization` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `technoRent_International_GmbH` | 0.0% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Bundesministeriums_für_Finanzen` | 0.1% | 100.0% | 0.1% | 9 | 9 | 0 |
| `Landespolizeidirektion` | 0.7% | 100.0% | 0.4% | 66 | 66 | 0 |
| `Reinhard_Stulik_GmbH` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Heinz_Neuböck_GmbH` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Amtes_für_Betrugsbekämpfung` | 0.1% | 100.0% | 0.0% | 6 | 6 | 0 |
| `Wiener_Linien` | 0.0% | 100.0% | 0.0% | 4 | 4 | 0 |
| `Wiener_Gemeindebezirk` | 0.3% | 100.0% | 0.1% | 24 | 24 | 0 |
| `Bundesamtes_für_Soziales` | 1.4% | 100.0% | 0.7% | 131 | 131 | 0 |
| `Wirtschaftsuniversität_Wien` | 0.1% | 100.0% | 0.1% | 11 | 11 | 0 |
| `Magistrat_Stadt_Wien` | 6.0% | 98.9% | 3.1% | 565 | 559 | 6 |
| `Bundesfinanzgericht_Full_BFG_Fixed` | 39.1% | 98.3% | 24.4% | 4468 | 4393 | 75 |
| `BFG_Abbreviation` | 20.9% | 96.3% | 11.7% | 2184 | 2104 | 80 |
| `Bundesminister_Arbeit` | 0.3% | 95.8% | 0.1% | 24 | 23 | 1 |
| `AMS_Organization` | 0.6% | 94.6% | 0.3% | 56 | 53 | 3 |
| `BFH_entities` | 1.1% | 93.3% | 0.5% | 104 | 97 | 7 |
| `Finanzamt_Locations_Fixed` | 36.1% | 92.7% | 22.4% | 4360 | 4040 | 320 |
| `Wiener_Gemeinderat` | 0.6% | 89.1% | 0.3% | 64 | 57 | 7 |
| `BM_Finanzen_Full` | 0.7% | 83.5% | 0.4% | 79 | 66 | 13 |
| `OECD_Organization` | 0.2% | 83.3% | 0.1% | 18 | 15 | 3 |
| `Landesgerichts_Genitive` | 0.0% | 50.0% | 0.0% | 6 | 3 | 3 |
| `Landesgericht_entities` | 0.1% | 43.3% | 0.1% | 30 | 13 | 17 |
| `FA_Location_Pattern_Fixed` | 0.2% | 31.8% | 0.1% | 44 | 14 | 30 |
| `Zollamt_Organization` | 0.1% | 29.4% | 0.0% | 17 | 5 | 12 |
| `m_b_H_entities` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Bundesfinanzgericht_BFG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMF_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fa_GmbH_entities` | 0.0% | 0.0% | 0.0% | 29 | 0 | 29 |
| `Derdonal_Garten_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht_Leoben` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Energie_Verdorfwald_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `St_Johann_Steuergesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schlaich_Bau_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt_Für_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nieder_Unisyn_Manufaktur_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unverdroß_Planung_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schniederjahn_Software_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frieb_Causa_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fritzenwallner_Gandler_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA_Wien_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Werkunival_Verlag_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA_Braunau_Ried_Schärding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `CENTURION_GmbH` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Kraftost_Digital_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Novotny_Getränke_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hellfritsch_Immobilien_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Versand_Seewil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bruckdon-Cloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `I_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag_Reumiller` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kantner_Wirtschaftstreuhand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt_Soziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd_Consynkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `xx_GmbH_Steuer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `yy_Wirtschaftstreuhand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GOBBS_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA_Grieskirchen_Wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Post_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SK_Telecom_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO_Assurance_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM_f_Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Telekom_Organisation_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Austria_GmbH_AG_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SNWG_Textil_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bonafide_Treuhand_Revisions_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AG_Organization_Pattern` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `KG_Organization_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Moser_Rechtsanwalts_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt_Osterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Alpen_KI_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `XY_GmbH_Co_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FIDAS_Graz_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA_Steiermark_Mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA_Spittal_Villach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Valdon_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wald_Zorwaldmon_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sudlexwil_Software_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ost_Daten_KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Alwilkraft_KI_AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht_Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Finanzpolizei_entities` 🏆

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `22b5706b`  
**Description:**
Matches Finanzpolizei as a standalone organization.

**Content:**
```
\bFinanzpolizei\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 37 | 37 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 37 | 0 | 17189 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_53`)


Eine Baustellenkontrolle der  Finanzpolizei am 22.5.2012 habe nicht angemeldete Dienstnehmer der Firma C ergeben.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_94`)


Außerdem  liegen Aktenvermerke der Finanzpolizei bezüglich mehrerer Kontrollen im Jahr 2012  (19.10.2012, 20.6.2012, 30.8.2012.) vor, bei welchen nicht angelmeldete Arbeiter auf den  Baustellen der Firma C angetroffen wurden.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_119`)


Die Begrenzung der UID Nummer wurde aufgrund  von bei der Betriebsprüfung festgestellten Unregelmäßigkeiten, sowie aufgrund von durch die  Finanzpolizei anlässlich von Kontrollen festgestellten nicht angemeldeten Arbeitnehmern auf  den Baustellen der Firma C veranlasst.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_15`)


Im Zuge eines Antrages auf Familienbeihilfe eines der ungarischen Mitgesellschafter UG1 (in  der Folge als UG1 bezeichnet) wurde die KIAB (nunmehr Finanzpolizei) von der belangten  Behörde um Überprüfung der Scheinselbständigkeit ersucht.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_320`)


Im Zuge eines Antrages auf Familienbeihilfe eines der ungarischen Mitgesellschafter UG1  bezeichnet wurde die KIAB (nunmehr Finanzpolizei) von der belangten Behörde um  Überprüfung der Scheinselbständigkeit ersucht.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_325`)


Der Verfahrensgang vor der belangten Behörde sowie dem Bundesfinanzgericht ist durch die  für den gegenständlichen Fall relevanten Aussagen im Vernehmungsprotokoll der Finanzpolizei  (damaligen KIAB), die trotz der Sprachbarriere auf Grund des Dolmetschers ein umfangreiches  Bild der Unternehmensabläufe vermitteln sowie die ausführliche Berufung und die nicht  minder ausführliche Stellungnahme der belangten Behörde, die Vorsprache bei der belangten  Behörde und den dementsprechenden Aktenvermerk evident.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_10`)


Bei einer weiteren Kontrolle durch die Finanzpolizei  wurde erhoben, dass das Fahrzeug wiederum an dieser Wohnadresse abgestellt war.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_12`)


welches der Bf lt. Finanzpolizei nicht beantwortet habe.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_15`)


Sachverhaltsdarstellung kein Datum zur Kontrolle durch die  Finanzpolizei genannt wird und der gesamte Akt keinen an den Bf ergangenen Vorhalt enthält.  2. Laut ZEVIS-Abfrage zum Fahrzeug handelt es sich um einen Nissan D40, Fahrzeugklasse "LKW  offener Kasten", FIN xxx, Erstzulassung 1.12.2005, zugelassen am 26.1.2006 mit dem  Kennzeichen X1 auf den Bf an der deutschen Adresse in D/AA, AStr2.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_16`)


3. An weiteren Fahrzeugdaten wurde von der Finanzpolizei teils durch Einsicht in die  EurotaxGlass-Fahrzeugbewertung erhoben, teils mangels Unterlagen im Rahmen der Schätzung  angenommen:   Nissan 2,5 16V Di, Leistung 98 Kw, Diesel, komb.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_67`)


Erstmals am 14.11.2011 sowie bei einer anschließend nochmaligen Kontrolle durch Zollorgane  wurde der Bf am inländischen Wohnsitz in A/XX angetroffen, wo auch das Fahrzeug Nissan  Pickup jeweils abgestellt war (Kontrollmitteilung des Zollamtes v. 28.11.2011 und  Sachverhaltsdarstellung der Finanzpolizei, undatiert).

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_4`)


Am 16.4.2018 hätten Organe der Finanzpolizei gemeinsam mit Organen der Polizei eine  Kontrolle an dieser Adresse wegen des Verdachtes der illegalen Arbeitnehmerbeschäftigung  und der illegalen Gewerbeausübung durchgeführt.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_36`)


In der Beschwerdevorentscheidung führte das Finanzamt dazu aus, dass sowohl bei Kontrollen  durch die Finanzpolizei als auch bei Amtshandlungen der Polizeiinspektion und in diversen  anderen Verfahren aufgrund von Anzeigen festgestellt worden sei, dass der Bf einen  Ersatzteilhandel sowie einen Handel mit Gebrauchtwägen betreibe.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_12`)


3. In der am 10.10.2013 von der Finanzpolizei zur Frage der "Verwendung eines Fahrzeuges mit  ausländischem behördlichen Kennzeichen" mit der Bf aufgenommenen und von ihr, nach  Vorlage zur Durchsicht und in Bestätigung der Richtigkeit der Angaben, unterfertigten  Niederschrift hat diese wie folgt ausgesagt bzw. geantwortet (kursiv):  "… Ich habe 1981 mit der Arbeit für XX in D/Z begonnen und bin im Jahr 2008 in Pension  gegangen.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_146`)


Veranlaßt durch eine anonyme Anzeige wurde im Anschluss durch die Finanzpolizei  wahrgenommen, dass das Fahrzeug im Inland vor dem Wohnhaus des Ehegatten in X-BWeg2,  abgestellt war (siehe betr. Lichtbilder).

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_197`)


Im Hinblick auf den im Streitzeitraum zusammen mit dem Ehegatten bestehenden inländischen  Wohnsitz in A/X, wo sich die Bf offenkundig regelmäßig bzw. nach eigenen Angaben - wie  festgestellt - sogar "überwiegend" aufgehalten hat, sowie der laut durchgeführter Kontrolle  der Finanzpolizei und auch nach eigenen Angaben erwiesenen und somit unstrittigen  Verwendung des Fahrzeuges im Inland wären sohin sämtliche Tatbestandsvoraussetzungen  nach § 82 Abs. 8 KFG (Hauptwohnsitz/Lebensmittelpunkt und Verwendung des Fahrzeuges im  Inland) erfüllt.   Es läge demnach vorderhand eine "widerrechtliche Verwendung" iSd § 1 Z 3 NoVAG und nach  § 1 Abs. 1 Z 3 KfzStG vor.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_54`)


Bei seiner Vernehmung durch Organe der Finanzpolizei am 13.1.2015 gab der Ehegatte der  Beschwerdeführerin noch an, dass die Beschwerdeführerin bei ihm in Österreich wohne.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_20`)


Im Zuge von Erhebungen der Finanzpolizei und Niederschriften mit Hrn. NachnameGeser1  VornameGeser1 vom 28.8.2015 und seiner Lebensgefährtin Fr. NachnameFreundin  VornameFreundin vom 18.8.2015 wurde festgestellt, dass das gegenständliche Fahrzeug  nahezu ausschließlich privat mit Probekennzeichen verwendet wird.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_35`)


Hinsichtlich Umsatzsteuer und Einkünftefeststellung wird in der Beschwerde vorgebracht:  „Die Niederschrift der Finanzpolizei ist missverständlich.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134648.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134648.1_37`)


In  sachverhaltsmäßiger Hinsicht wurde seitens des Finanzamtes im Vorlagebericht ausgeführt,  auf Grund der von der Finanzpolizei durchgeführten Ermittlungen sei festgestellt worden, dass  sich der dauernde Standort des ausländischen Fahrzeuges mit dem amtliche Kennzeichen xxx  in Österreich befinde.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_36`)


Da es auch keine  Aufzeichnungen über die tatsächlichen Auszahlungsbeträge an die jeweiligen Taxifahrer gäbe,  könne auch nicht festgestellt werden, ob die Fahrer am Umsatz beteiligt waren (wie diese im  Zuge mehrerer von der Finanzpolizei durchgeführten Kontrollen angaben) oder nicht, wie der  Bf. niederschriftlich ausführte.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_125`)


Die Fahrer hätten bei Kontrollen der Finanzpolizei Umsatzbeteiligungen von 40-45%  angegeben.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_16`)


Begründend dazu wurde auszugsweise angeführt:  „Der Entscheidung liegt folgender Sachverhalt zugrunde:   Aufgrund einer anonymen Anzeige, dass Priv.-Doz.in Laetitia Pöstges  seit 5-6 Jahren bei ihrem Lebenspartner A.  in Ort1 (Ö) wohne, hat die Finanzpolizei Feldkirch entsprechende Erhebungen bei Nachbarn  sowie mehrfache Bereisungen dieser Adresse durchgeführt.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Laetitia Pöstges` (person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_34`)


Die  Sachverhaltsfeststellungen zeigen jedoch das Vorliegen einer mehrjährigen Beziehung der  Beschwerdeführerin zu A., der die Beschwerdeführerin gegenüber der Abgabenbehörde selbst  als Lebensgefährtin bezeichnet hatte, und im Rahmen welcher die Beschwerdeführerin nach  den Angaben einer Nachbarin auf Befragung durch die Finanzpolizei in Ort1 (Ö) wohne.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_37`)


Bei der Kontrollfahrt am 8.11.2019 hatte die Finanzpolizei um  6:45 Uhr an der Türe geläutet, weil Licht im Inneren zu erkennen war.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_47`)


Der Wohnsitz in Ort1 (Ö)   • wird von der Beschwerdeführerin tatsächlich (unstrittig) regelmäßig bewohnt,   • umfasst als Wohnsitz des Lebensgefährten der Beschwerdeführerin die stärksten  persönlichen Bindungen,   • ist der Wohnsitz, von dem die Beschwerdeführerin regelmäßig morgens mit dem ggst Kfz  beim Aufbruch gesehen wird   • ist folglich der Wohnsitz, an welchen sie im Laufe des Tages wieder zurückkehrt,   • ist jener, an welchem die Finanzpolizei an mehreren Kontrollterminen das ggst Kfz körperlich  morgens bzw abends abgestellt vorgefunden hatte,   und wird daher ungeachtet der tatsächlichen Häufigkeit der Nächtigung in Ort1 (Ö) bzw am  weiteren Schweizer Wohnsitz, sowie ungeachtet weiterer in den Hintergrund tretenden  persönlichen Bindungen in der Schweiz, da die Mutter der Beschwerdeführerin dort wohnhaft  sind und ggf zT von ihr gepflegt werden müssen, als Mittelpunkt ihrer Lebensinteressen  qualifiziert.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_121`)


Der Wohnsitz in Ort1 (Ö) würde  von der Bf. tatsächlich (unstrittig) regelmäßig bewohnt, umfasse als Wohnsitz des  Lebensgefährten der Bf. die stärksten persönlichen Bindungen, sei der Wohnsitz, von dem die  Bf. regelmäßig morgens mit dem streitgegenständlichen Kfz beim Aufbruch gesehen werde  und folglich der Wohnsitz, an welchen sie im Laufe des Tages wieder zurückkehre und jener, an  welchem die Finanzpolizei an mehreren Kontrollterminen das gegenständliche Kfz körperlich  morgens bzw. abends abgestellt vorgefunden habe.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/144724.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144724.1_14`)


Zudem verwehrte  er sich gegen die Heranziehung einer bei der Amtshandlung der Finanzpolizei (FinPol) am  16.Nov.2018 ohne Beiziehung eines Dolmetschers verfassten Niederschrift als Beweismittel im  Abgabenfestsetzungsverfahren.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/144724.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144724.1_21`)


Am 16.Nov.2018 wurde der Bf im Zuge einer - unter Teilnahme von Organen der  Finanzpolizei der Dienststelle des FA durchgeführten - Verkehrskontrolle in Klagenfurt von  Polizeiorganen am Steuer eines auf ihn zugelassenen Pkw der Marke Auto-C Modell  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/144724.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144724.1_27`)


Am Tag der Betretung durch die Finanzpolizei war der Bf lt. Niederschrift auf dem Weg zu einer  Wohnungsbesichtigung für sich und seine ortsansässige, noch bei der Mutter lebende Freundin  gewesen, mit der er angab, seit 5 Monaten liiert zu sein.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Am 15. Jänner 2020 wurde bei einer Kontrolle der Finanzpolizei das gegenständliche  Kraftfahrzeug, ein Audi A6 Quattro 3.0t mit dem rumänischem Kennzeichen ABC, am Wohnsitz  der Beschwerdeführerin (=Bf.) vorgefunden, wo dieses auch bereits am 12. Juni 2019 gesichtet  und fotografiert worden war.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_6`)


Mit Bescheid vom 30.04.2021 setzte das Finanzamt gegenüber der Bf. aufgrund ihres  festgestellten inländischen Hauptwohnsitzes und mangels Erbringens eines Gegenbeweises zur  von der Finanzpolizei angenommenen Standortvermutung des gegenständlichen Fahrzeuges  Kraftfahrzeugsteuer gem. § 5 Abs. 1 Z 2 lit. a Kraftfahrzeugsteuergesetz (KfzStG) 1992 für den  Zeitraum 07-12/2019 iHv EUR 941,29 fest.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_90`)


Am 15. Jänner 2020 wurde bei einer Kontrolle der Finanzpolizei das gegenständliche  Kraftfahrzeug, ein Audi A6 Quattro 3.0t mit rumänischem Kennzeichen ABC, am Wohnsitz der  Bf. vorgefunden, wo dieses auch bereits am 12. Juni 2019 gesichtet und fotografiert worden  war.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/148292.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148292.1_8`)


GSpA-Bescheide vom 21.4.2021  Anhand von Kontrollen durch die Finanzpolizei (2015, 2017 und 2018) und einer  anschließenden Außenprüfung gemäß § 99 FinStrG, Abgabenkontonummer 45-516/7370,  hat das Finanzamt Österreich (FA) festgestellt, dass die LTD in Österreich an den Standorten X,  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `45-516/7370` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/148292.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148292.1_81`)


die Räumlichkeiten, in denen die Glücksspielgeräte betriebsbereit aufgestellt  waren, haben sich im Verfügungsbereich der LTD als Mieterin befunden und hat Letztere auch  das Personal, das die Geräte bedient, zur Verfügung gestellt. Wie dem Prüfbericht zu  entnehmen ist, waren bei den Kontrollen durch die Finanzpolizei vor Ort angetroffene  Bedienstete (Frau Z und Frau R) bei der LTD angestellt. Auch wenn bei den Einvernahmen von  Kunden (MM, IF, AD) teilweise als Chef, Geschäftsführer bzw. Verantwortlicher „W“ genannt  wurde, so war im Außenverhältnis bei einer Gesamtbetrachtung dennoch die LTD  Vertragspartner der Spieler und somit Veranstalter der Ausspielungen.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/149316.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149316.1_6`)


Mit Verständigungen gem. § 82 Abs. 9 KFG 1967 wurde durch die Landespolizeidirketion  Tirol an die Finanzpolizei mitgeteilt, dass im Zuge von Kontrollen festgestellt werden konnte,  dass die Beschwerdeführerin gemeinsam mit ihrem Ehemann und ebenso deren gemeinsame  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/149316.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149316.1_11`)


2. Bei einer Einvernahme durch die Finanzpolizei gab die Beschwerdeführerin an, dass sie seit  dem Jahr 2005 ein Restaurant in Deutschland im Rahmen eines Einzelunternehmens betreibe,  welches täglich an rund 330 Tagen im Jahr geöffnet sei.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

</details>

---

## `KAG_entities` 🏆

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `8471882c`  
**Description:**
Matches the specific abbreviation KAG as an organization.

**Content:**
```
\bKAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 3916 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_8`)


der Patienten der Sonderklasse gebührenden Honorars zuzurechnen ist und sie  dementsprechend im gleichen Ausmaß auch für den in § § 41 Abs. 6 Tir KAG geregelten  "Hausanteil" von mind.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_64`)


§ 4 Abs. 3 dritter Satz ist anzuwenden.“  § 41 Tiroler Krankenanstaltengesetz - Tir KAG lautet:  „(1) Folgende Sondergebühren sind zu entrichten:  a) für die in der Sonderklasse aufgenommenen Patienten eine Anstaltsgebühr für den erhöhten  Sach- und Personalaufwand und eine Hebammengebühr und   5 von 8 Seite 6 von 8

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_90`)


Die Revision hat der Verwaltungsgerichtshof mit Beschluss vom 16. Juni 2023,  Ra 2021/15/0020-5, zurückgewiesen und begründend dazu ausgeführt:  „…  14 Im Zulässigkeitsvorbringen der Revision wird der Standpunkt vertreten, die im Revisionsfall  anzuwendenden Bestimmungen des Tir KAG seien mit den Bestimmungen des Oö KAG nicht  gleichzusetzen, weshalb es hinsichtlich des Tir KAG an Rechtsprechung des  Verwaltungsgerichtshofes fehle.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |
| `KAG` | `KAG` |
| `KAG` | `KAG` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_91`)


In welchen für die Lösung des vorliegenden Revisionsfalls  entscheidenden Teilen sich das Oö KAG von dem im konkreten Fall anzuwendenden Tir KAG  unterscheidet, legt die Revision im Rahmen des Zulässigkeitsvorbringens nicht dar, weshalb sie  sich schon deswegen als unzulässig erweist.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |
| `KAG` | `KAG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_92`)


15 Soweit dazu in den Revisionsgründen ausgeführt wird, nach § 41 Abs. 5 Tir KAG seien nur  die dort angeführten verantwortlichen leitenden Ärzte sowie die Konsiliarfachärzte berechtigt,  von den von ihnen betreuten Patienten in der Sonderklasse ein mit diesen vereinbartes  Honorar zu verlangen, wohingegen diese Berechtigung nach § 54 Oö KAG einem größeren  Personenkreis zukomme, wird damit kein im gegebenen Zusammenhang relevanter Umstand  aufgezeigt.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |
| `KAG` | `KAG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_93`)


Entscheidend ist, dass dem Revisionswerber gemäß § 41 Abs. 7 Tir KAG für die  Mitwirkung an der Untersuchung und Behandlung der Pfleglinge in der Sonderklasse Anteile an  den Honoraren nach § 41 Abs. 5 Tir KAG zustehen, die gemäß § 46 Abs. 6 Tir KAG um den  Hausanteil des Anstaltsträgers von mindestens 20 % zu kürzen sind.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |
| `KAG` | `KAG` |
| `KAG` | `KAG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_96`)


16 Die Revision erweist sich daher als unzulässig, weshalb sie gemäß § 34 Abs. 1 VwGG ohne  weiteres Verfahren zurückzuweisen war.“  5. Auf Grundlage dieser höchstgerichtlichen Rechtsprechung und des festgestellten  Sachverhalts ist nach Ansicht des Bundesfinanzgerichts auch für den hier zu beurteilenden Fall  festzustellen, dass auch im Anwendungsbereich des Tir KAG neben dem „Hausanteil“ nicht  weitere Betriebsausgaben im Wege eines Durchschnittsatzes iSd § 17 EStG 1988 geltend  gemacht werden können.

| Predicted | Gold |
|---|---|
| `KAG` | `KAG` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

</details>

---

## `KPMG_full_name` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a045f86f`  
**Description:**
Matches the full KPMG entity name which was partially matched before.

**Content:**
```
\bKPMG\s+Alpen-Treuhand\s+GmbH\s+Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 13997 |

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

- `Bundesfinanzgericht` (organisation)
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

- `Bundesfinanzgericht` (organisation)
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

- `Bundesfinanzgericht` (organisation)
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

## `Pensionsversicherungsanstalt` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `87469955`  
**Description:**
Matches Pensionsversicherungsanstalt as an organization.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 62 | 62 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 0 | 16814 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf.) ist eine Philologin, die im Streitjahr über ihre Pensionsbezüge bei  der Pensionsversicherungsanstalt hinaus als Kurs-Trainerin noch lohnsteuerpflichtige Einkünfte  bei der A-OG bezogen und Einkünfte aus selbständiger Arbeit erzielt hat.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_11`)


In weiterer Folge wäre seiner Gattin seitens der  Pensionsversicherungsanstalt rückwirkend die Pension für das gesamte Jahr 2011 zuerkannt  und ein diesbezüglicher Lohnzettel seitens der PVA an das Finanzamt übermittelt worden.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_51`)


Mit E-Mails vom 23. und 24. November 2020 übermittelte die Bezirkshauptmannschaft   - Bescheide betreffend die Zuerkennung bedarfsorientierter Mindestsicherung für die  Zeiträume 5-8/2016, 9/2016-2/2017, 3-6/2017, 7-8/2017 und 9-12/2017   - eine monatsweise Aufstellung der Ansprüche und Zahlungen an Bf für laufende Hilfe zum  Lebensunterhalt für die Monate Juli 2016 bis Februar 2018 mit einer Summe von insgesamt  18.262,20 €  - ein Schreiben der Bezirkshauptmannschaft an die Pensionsversicherungsanstalt vom 26.  August 2016,  mit dem für den Fall der Zuerkennung der vom Bf beantragten Invaliditäts- Pension – Rehabilitationsgeld der Ersatzanspruch für die gewährten Geldleistungen im Rahmen  der bedarfsorientierten Mindestsicherung geltend gemacht und um Einbehalt und  Überweisung  auf ein genanntes Konto des Sozialhilfeverbandes ersucht wird  - ein E-Mail der Bezirkshauptmannschaft an die OÖGKK vom 22. Februar 2018, mit dem der  Ersatzanspruch für den Zeitraum 1. Juli 2016 bis 28. Feber 2018 (mit dem Hinweis  der  Auszahlung der bedarfsorientierten Mindestsicherung im Nachhinein) mit 18.262,20 € beziffert  und um Überweisung auf das genannte Konto des Sozialhilfeverbandes ersucht wurde  - ein Beleg über Eingang des Betrages von 18.262,20 € am Konto des Sozialhilfeverbandes am  12. März 2018 auf Grund der Überweisung durch die OÖGKK  Mit Amtshilfeersuchen per Telefax vom 24. November 2020 ersuchte das erkennende Gericht  die Österreichische Gesundheitskasse um Vorlage der Bescheide betreffend Zuerkennung des  Rehabilitationsgeldes ab 8.6.2016-31.12.2018, der Belege betreffend dessen Überweisung für  den Zeitraum 8.6.2016-28.2.2018 an Bf, das Arbeitsmarktservice und den Sozialverband sowie  der Bescheide und zweckdienlichen Unterlagen zur Begründung der teilweisen Überweisung an  Arbeitsmarktservice und Sozialverband auf.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_52`)


Mit Telefax vom 30. November 2020 übermittelte die Österreichische Gesundheitskasse    - ein Schreiben der Pensionsversicherungsanstalt vom 23. Jänner 2018, wonach Bf ab 8. Juni  2016 für die Dauer der vorübergehenden Invalidität Anspruch auf Rehabilitationsgeld hat  - eine Auszahlungsbestätigung der ÖGK vom 27. November 2020, wonach das ganze  Rehabilitationsgeld  für den Zeitraum 8. Juni 2016 bis 31. Dezember 2017 zur Gänze und jenes  für 1. Jänner bis 28. Februar 2018 zum Teil – insgesamt  18.262,20 €  einbehalten worden ist  - ein Schreiben der ÖGK vom 27. November 2020, wonach der Einbehalt der 18.262,20 € des  Rehabilitationsgeldes des Zeitraumes 1.7.2016 bis 28.2.2018  für die bedarfsorientierte  Mindestsicherung gemäß § 324 ASVG erfolgt ist   Am 3. Dezember 2020 übermittelte das erkennende Gericht dem Finanzamt die an die  Bezirkshauptmannschaft und die Österreichische Gesundheitskasse gerichteten  Amtshilfeersuchen samt den dazu eingelangten Unterlagen zur Kenntnis.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)
- `ÖGK` (organisation)
- `Finanzamt` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_66`)


Der gerichtliche Vergleich über die vorübergehende Invalidität und die rückwirkende  Zuerkennung des Rehabilitationsgeldes gehen aus dem Schreiben der  Pensionsversicherungsanstalt vom 23. Jänner 2018 an Bf hervor.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_158`)


BMSG hat die Bezirkshauptmannschaft  schon mit Schreiben vom 26. August 2016 gegenüber der Pensionsversicherungsanstalt unter  Hinweis auf den „Antrag auf Invaliditätspension- Rehabilitationsgeld“ des Bf für den Fall der  Gewährung gestellt bzw. angemeldet.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_97`)


Somit steht  fest, dass dem Bf. für das Streitjahr von der Pensionsversicherungsanstalt kein  Rehabilitationsaufenthalt bewilligt und von dieser auch keine Rückvergütungen geleistet  wurde, die, wie ausgeführt, die Vorlage eines solchen ärztlichen Zeugnisses ersetzen hätte  können.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_13`)


Die Bf. legte ein Schreiben der Pensionsversicherungsanstalt, Landesstelle Wien vom  17.11.2017 bei, in welchem ausgeführt wird, dass bezüglich des Gesundheitszustandes der Bf.  keine kalkülsrelevante Änderung eingetreten sei und daher vorübergehende Invalidität weiter  vorliege und Maßnahmen zur medizinischen Rehabilitation zur Besserung des  Allgemeinzustandes und Wiederherstellung der Arbeitsfähigkeit notwendig seien.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_15`)


Auszahlende Stelle in Österreich ist die  Pensionsversicherungsanstalt und in Deutschland die Deutsche Rentenversicherung Bund.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/134234.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134234.1_8`)


Die bezugsauszahlende Stelle ist die  Pensionsversicherungsanstalt, die folgende Bezüge meldete:  1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_194`)


Die Bf bezog im Kalenderjahr neben der Bestattungsbeihilfe und der  Hinterbliebenenunterstützung im Kalenderjahr 2012 Einkünfte aus nichtselbständiger Arbeit:  Bezugsauszahlende Stelle Bezugszeitraum Steuerpflichtige Bezüge  Pensionsversicherungsanstalt 01.12.2012 bis 31.12.2012 1.338,96  AUVA Ldst C 01.12.2012 bis 31.12.2012 6.796,11  B GmbH 05.05.2012 bis 05.05.2012 86,29  Pauschbetrag WK  -132,00  Einkünfte aus  nichtselbständiger Arbeit   8.089,36  Die Pension der AUVA in Höhe von 6.963,95 Euro wurde erstmals am 01.02.2013 ausbezahlt.  Die Bf bezog in den letzten Jahren vor dem Tod ihres Ehegatten keine Einkünfte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/134512.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134512.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (in der Folge: Bf.) bezog im Jahr 2019 inländische Pensionszahlungen  der Pensionsversicherungsanstalt in Höhe von brutto € 2.666,40 sowie ausländische  Pensionszahlungen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134840.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134840.1_96`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt  Der Beschwerdeführer (infolge Bf) hat seinen Wohnsitz in Österreich an der Wohnsitzadresse  Ehrensdorf 23, 4720 Hading, Österreich (laut ZMR seit 10.3.2011, vorher befand sich der Wohnsitz in L) und bezieht  auch eine Pension von der Pensionsversicherungsanstalt.  Dem zuständigen FA G wurde laut Aktenvermerk vom 28.10.2015 bekannt, dass der Bf.  ausländische (deutsche) Pensionseinkünfte bezieht, die dem Progressionsvorbehalt  unterliegen, daher wurde dem Bf. die Formulare L1i zur ANV für 2010 bis 2014 zur  Beantwortung ausgehändigt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrensdorf 23, 4720 Hading, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_29`)


Von der Pensionsversicherungsanstalt wurde die Waisenpension nach dem verstorbenen Vater  zuerkannt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_40`)


Seitens der  Pensionsversicherungsanstalt sei die Genehmigung dieses "Kuraufenthaltes" nicht erteilt  worden; mit der Begründung, dass ein neuerlicher Antrag frühestens ein Jahr nach Ausstellung  einer Verständigung eingebracht werden könne, es sei denn der Gesundheitszustand habe sich  verschlechtert und sei von einem Arzt medizinisch begründet worden.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_176`)


Angemerkt wird in diesem Zusammenhang nochmals, dass die Pensionsversicherungsanstalt  den Heilverfahrensantrag abgelehnt hat.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_11`)


Am 13.01.2021 erließ das Finanzamt einen Bescheid über die Wiederaufnahme des  Verfahrens gem. § 303 Abs. 1 BAO betreffend Einkommensteuer 2019 infolge der  Übermittlung eines weiteren Lohnzettels der Pensionsversicherungsanstalt hinsichtlich der  Pensionsbezüge des Bf. .  Der anlässlich der Wiederaufnahme zeitgleich erlassene neue Einkommensteuerbescheid für  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_18`)


Mit Beschwerdevorentscheidung vom 26.02.2021 wies das Finanzamt die Beschwerde mit  der Begründung ab, dass  der Lohnzettel der Pensionsversicherungsanstalt erst eingegangen ist, nachdem der  Erstbescheid vom 25.02.2020 bereits erlassen worden war.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_31`)


Pensionsauszahlende Stelle ist die  Pensionsversicherungsanstalt.  Die Nachweise (Lohnzettel) der bezugsauszahlenden Stellen liegen dem BFG vor.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_36`)


Infolge der späteren elektronischen Übermittlung des Lohnzettels seitens der  Pensionsversicherungsanstalt erfolgte eine „automatische“ Wiederaufnahme des  Einkommensteuerverfahrens und erging der streitgegenständliche Einkommensteuerbescheid  vom 13.01.2021, welcher naturgemäß zu einer Nachforderung führte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_49`)


Die Einkommensteuerpflicht erstreckt sich auf die im gesamten Jahr 2019 erzielten Einkünfte,  somit auf die Einkünfte, die sich aus den Lohnzetteln des Magistrates der Stadt Wien, der  Pensionsversicherungsanstalt sowie der Pensionskassen AG, ergaben.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `Pensionskassen AG` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_53`)


In der Tatsache, dass die Lohnzettelübermittlung seitens der Pensionsversicherungsanstalt an  das Finanzamt aus technischen Gründen nach dem hierfür vorgesehenen Zeitpunkt erfolgte,  kann aber kein Hinderungsgrund für das Finanzamt erblickt werden, eine Wiederaufnahme des  Verfahrens vorzunehmen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_54`)


Dem Einwand, es sei in dem Umstand, dass die Wiederaufnahme seitens des zuständigen  Finanzamtes Monate nach der Einspielung des Lohnzettels der Pensionsversicherungsanstalt  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_55`)


erfolgte, ein die Abgabenfestsetzung hinderndes Verschulden des Finanzamtes zu erblicken, ist  zu entgegnen:  Es ist davon auszugehen, dass dem BF. im Zeitpunkt der Einreichung der  Arbeitnehmerveranlagung 2019 am 22.01.2020 bekannt sein musste, dass infolge des Antrittes  des Ruhestandes mit 01.08.2019 einerseits das aktive Dienstverhältnis beendet wurde und  infolge des Bezuges von Pensionseinkünfte nun nicht nur eine Lohnzettelübermittelung seitens  des seinerzeitigen Arbeitgebers sondern auch seitens der Pensionsversicherungsanstalt zu  erfolgen haben werde, sodass demnach von (zumindest) zwei zu übermittelnden Lohnzetteln  auszugehen sein werde.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_57`)


Im streitgegenständlichen Verfahren erhielt das Finanzamt durch Übermittlung des Lohnzettels  der Pensionsversicherungsanstalt Kenntnis von weiteren steuerpflichtigen Einkünften,  welchem Umstand durch die vorgenommene Wiederaufnahme des Verfahrens Rechnung  getragen und die Besteuerung der im Jahr 2019 zugeflossenen Einkünfte vorgenommen wurde.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_58`)


Dass das Finanzamt die Wiederaufnahme Monate nach Überspielung des die Wiederaufnahme  begründenden Lohnzettels der Pensionsversicherungsanstalt vornahm, mag zwar aus der Sicht  des Bf. als unangemessen erscheinen, doch darf dazu nicht unerwähnt bleiben, dass er den  eine unrichtige Gutschrift ausweisenden Erstbescheid durch die Angabe nur eines Lohnzettels  selbst herbeiführte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/139366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139366.1_12`)


Die Beschwerdeführerin erhielt 2019 folgende Bezüge:  Pensionsversicherungsanstalt (Witwenpension) 18.182,48 €  Österreichische Gesundheitskasse (Krankengelder)  1.2.2019 – 22.2.2019  873,65 €  Österreichische Gesundheitskasse (Krankengelder)  23.2.2019 – 28.2.2019  238,27 €  Österreichische Gesundheitskasse (Krankengelder)  1.3.2019 – 31.3.2019  1.231,05 €  Österreichische Gesundheitskasse (Krankengelder)  1.4.2019 – 3.4.2019  119,13 €  Österreichische Gesundheitskasse (Krankengelder)  2.1.2019 – 31.1.2019  1.573,03 €

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_6`)


- das die Grundlage für diesen Bescheid bildende Sachverständigengutachten vom 23. Jänner  2019, mit welchem ein Grad der Behinderung von 50% und die Fähigkeit trotz  der Funktionsbeeinträchtigung auf einem geschützten Arbeitsplatz oder in einem integrativen  Betrieb (allenfalls unter Zuhilfenahme von Unterstützungsstrukturen) einer Erwerbstätigkeit  nachzugehen, attestiert wurde, sowie  - ein Bescheid der Pensionsversicherungsanstalt über den Bezug von Pflegegeld ab November  2018 in der Höhe der Stufe 1.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_66`)


d) Laut Bescheid der Pensionsversicherungsanstalt vom 14. Jänner 2019 bestand ab  November 2018 Anspruch auf Pflegegeld in der Höhe der Stufe 1.  e)

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/139915.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139915.1_24`)


Sie bezog  im verfahrensgegenständlichen Jahr 2020 Zahlungen von der österreichischen  Pensionsversicherungsanstalt in Höhe von 1.249,08 Euro, sowie zwei Betriebsrenten aus  Deutschland in Höhe von 513,18 Euro beziehungsweise 2.036,10 Euro und zwei Renten der  deutschen gesetzlichen Rentenversicherung in Höhe von 12.135,90 Euro beziehungsweise  6.146,70 Euro.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/139915.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139915.1_36`)


Im gegenständlichen Fall bedeutet diese, dass die Bezüge der Beschwerdeführerin von den  deutschen Betriebsrenten sowie jene von der österreichischen Pensionsversicherungsanstalt in  Österreich zu besteuern sind.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/140032.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140032.1_10`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer hat seinen Wohnsitz in Österreich und erhielt 2020 folgende  steuerpflichtigen Bezüge:  Pensionsversicherungsanstalt 1.1.2020 – 31.12.2020 27.609,24 €  Helvetia Vers.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_23`)


Laut Lohnzettel  der Pensionsversicherungsanstalt für den Zeitraum 01.01.2020 bis 31.12.2020 beliefen sich die  einbehaltenen SV-Beiträge für laufende Bezüge auf 1.707,72 € und nicht auf 1.650,84 € und die  einbehaltene Lohnsteuer betrage 6.363,21 € und nicht 6.100,68 €.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_26`)


Der Bf übermittelte diesbezüglich unter anderem eine Verständigung  über die Leistungshöhe zum 01.01.2020 der Pensionsversicherungsanstalt, Landesstelle  Niederösterreich vom Jänner 2020 und eine Auflistung der Einkünfte und der einbehaltenen  Beträge für Sozialversicherung und Lohnsteuer;

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_28`)


Mit (drittem) Vorhalt vom 14.12.2021 wurde dem Bf – die Steuererklärungen 2015-2020  betreffend – mitgeteilt, dass die Sozialversicherungsbeiträge von der österreichischen Pension  von der Pensionsversicherungsanstalt übermittelt worden seien.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_63`)


Mit Schreiben vom 12.07.2022 ersuchte die Abgabenbehörde die Pensionsversicherungsanstalt  das Lohnkonto des Bf vorzulegen, da der Bf behaupte, dass die anrechenbare Lohnsteuer im  Lohnzettel nicht korrekt sei.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_64`)


Mit Schriftsatz vom 21.07.2022 übermittelte der Bf der Abgabenbehörde ein Schreiben mit  dem selben Datum an die Pensionsversicherungsanstalt, in dem er die Pensionsversicherung  ersuchte, aufzuklären, weshalb die einbehaltene Lohnsteuer im Lohnzettel mit 6.100,68 €  ausgewiesen werde, während in der Auflistung der monatlichen Überweisungen der PVA an  den Bf die Summe der einbehaltenen Lohnsteuer mit 6.363,21 € angegeben werde.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_65`)


Mit Schreiben vom 26.07.2022 teilte die Pensionsversicherungsanstalt dem Bf unter anderem  mit, dass er im Oktober 2020 eine Lohnsteuer Nach- und Rückverrechnung erhalten hätte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_68`)


Mit Schreiben vom 29.11.2022 übermittelte die Pensionsversicherungsanstalt ihr Schreiben  vom 26.07.2022 an den Bf an das Bundesministerium für Finanzen sowie eine E-Mail des Bf an  die Pensionsversicherungsanstalt vom 01.08.2022 in der er einräumt, dass die einbehaltene  Lohnsteuer für 2020 mit 6.100,68 € richtig sei und ihm die Rückverrechnung mit Zahlungs- eingang 07.10.2020 entgangen sei, da er nur die Kontoauszüge der am Monatsanfang  eingegangenen Zahlungen aufgehoben hätte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Bundesministerium für Finanzen` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_69`)


Die Pensionsversicherungsanstalt verwies in  ihrem Schreiben darauf, dass laut der erwähnten Mail vom 01.08.2022 die Sache für den Bf  damit erledigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_85`)


Der von der Pensionsversicherungsanstalt für ausländische Leistung einbehaltene  Krankenversicherungsbeitrag in Höhe von 55,92 € ist somit als Werbungskosten von der  ausländischen Pension in Abzug zu bringen:    ausländische Pension 1.115,58 €  – Werbungskosten: Krankenversicherungsbeitrag f. ausl.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_19`)


Dem Vorlageantrag waren ein Schreiben der Pensionsversicherungsanstalt vom 24.3.2021 und  Bestätigungen der ÖGK hinsichtlich der Nachzahlungen des Rehabilitationsgeldes beigelegt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_4`)


Die Beschwerde gegen den Einkommensteuerbescheid 2020  richtet sich gegen die betragsmäßige Höhe der einbehaltenen Lohnsteuer am Lohnzettel der  Pensionsversicherungsanstalt (kurz: PVA).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_10`)


Diese Angabe finden Sie auf Seite 3 des  Einkommensteuerbescheides 2020 bei den Angaben zum Lohnzettel der  Pensionsversicherungsanstalt. Das hat dazu geführt, dass die Pensionsversicherungsanstalt bei  einer Lohnsteuerbemessungsgrundlage von EUR 40.694,78 Lohnsteuer in Höhe von EUR  9.571,43 einbehalten hat.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_11`)


Im Vergleich dazu hat die Pensionsversicherungsanstalt im  Kalenderjahr 2019 bei einer Lohnsteuerbemessungsgrundlage von EUR 40.239,84 Lohnsteuer  in Höhe von EUR 10.521,04 einbehalten, wobei für dieses Kalenderjahr (2019) kein  Freibetragsbescheid ausgestellt worden ist.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_17`)


Die Summe der 12 monatlichen einbehaltenen Lohnsteuerbeträgen entspricht exakt  dem im Jahreslohnzettel der Pensionsversicherungsanstalt angeführten Betrag an  einbehaltener Lohnsteuer.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_18`)


Eine Abänderung des Lohnzettels der Pensionsversicherungsanstalt  erübrigt sich daher.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_47`)


Die Summe der 12 monatlichen einbehaltenen Lohnsteuerbeträge entspricht exakt dem im  Jahreslohnzettel der Pensionsversicherungsanstalt angeführten Betrag an einbehaltener  Lohnsteuer.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_48`)


Eine Abänderung des Lohnzettels der Pensionsversicherungsanstalt erübrigt sich  daher.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/141773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141773.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 18.5.2022 verfügte das Finanzamt die Pfändung einer dem  Beschwerdeführer angeblich gegenüber der Pensionsversicherungsanstalt zustehenden  beschränkt pfändbaren Forderungen aus einem Arbeitsverhältnis oder sonstigen Bezügen  wegen des Gesamtbetrages von EUR 111.366,79 (Abgaben einschließlich Nebengebühren von  EUR 110.258,60 zuzüglich Gebühren und Barauslagen für diese Pfändung von EUR 1.108,19).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/145403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145403.1_15`)


Der BF befindet sich im Ruhestand und bezog im Jahr 2022 Einkünfte von der  Pensionsversicherungsanstalt. Im Jahr 2022 fielen die als außergewöhnliche Belastung geltend  gemachten Kosten für zahnärztliche Leistungen an, die der BF im Dezember 2022 bezahlte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_39`)


[...]  Pensionsversicherungsanstalt vom 21. März 2019  BU ab dem 1.1:2019  Urkunde der Erwachsenenvertretung vom 4.6.2018  Sachwalterbeschluss vom 4. Juni 2018

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_80`)


Auszug aus dem Ärztlichen Gesamtgutachten zum Antrag auf Gewährung einer Invaliditäts- pension der Pensionsversicherungsanstalt, Landesstelle Wien, vom 20. Februar 2019,Serge Mickenhagen  FA f. Neurologie und Psychiatrie  1. Anamnese:  Die Patientin kommt in Begleitung einer Mitarbeiterin des Sachwalters.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Serge Mickenhagen` (person)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_77`)


Die Pension beträgt ab   8.11.2024  1.1.2025   monatlich      198,07 Euro  207,18 Euro   (Pensionsversicherungsanstalt Bescheid vom 13. Februar 2025).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_78`)


Die Nachzahlung der Pensionsversicherungsanstalt für die Zeit vom 8. November 2024 bis  31. Jänner 2025 betrug 557,10 Euro und wurde überwiesen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_79`)


Die monatliche Leistung betrug im  Februar 2025 (Pensionsversicherungsanstalt Information über die Anweisung):         Waisenpension  Pflegegeld   Leistung     207,18 Euro    200,80 Euro   Anweisungsbetrag   207,18 Euro    200,80 Euro   Die Anweisung erfolgt monatlich im Nachhinein.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_80`)


Laut Mitteilung der Pensionsversicherungsanstalt vom 11. März 2025 gehen für die Dauer des  Aufenthaltes der Bf. in der Wohngemeinschaft der Pensionsanspruch (höchstens 80 Prozent)  sowie der Anspruch auf Pflegegeld (höchstens 8 Prozent) zur teilweisen Deckung der  Verpflegungskosten auf den Kostenträger über.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_211`)


Krankenhaus YY, Innere Medizin und Psychosomatik, 22.6.2020 (bei Vorgutachten bereits  vorliegend) …..  Mitgebrachter Befund  Pensionsversicherungsanstalt Ärztliches Gutachten, DrJ, Allgemeinmedizin, 25.5.2021  Hauptdiagnose: Angst und depressive Störung gemischt, emotional instabile  Persönlichkeitsstörung, Zwangshandlungen, Panikstörung, Reizdarmsyndrom, chronische  Pankreasinsuffizienz, Endometriose, Kopfschmerz, Z.n. 2x Suizidversuch 2011 und 2012  Bescheid, 17.4.2024, MA 40: Mindestsicherungszuerkennung  Arztbrief DrK, FA Psychiatrie und psychotherapeutische Medizin, 29.4.2024  28-jährige Patientin bringt zahlreiche Vorbefunde (KJP beginnend mit 15 Jahren mit  Automutilationen, Zwangsgedanken, rezidivierend depressiv, polytope Ängste, Somatisierung)  Anamnese: Vater Alkohol und Depression, 1xiger SMV vor etwa 10 Jahren, Mutter latent  depressiv, Schwester Essstörung, Bruder Narkolepsie, auch in der Generation davor viel Gewalt  und psychiatrische Probleme.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_217`)


Zwangsgedanken, keine wesentlichen Biorhythmusstörungen, Alpträume, wiederkehrende  Zustände von Derealisation und Depersonalisation, Selbstverletzungen haben sistiert unter  Therapie, keine Abundantien bis auf Nikotin, Impulskontrolle aktuell erhalten, kein akuter  Gefährdungsaspekt  F43.1, F41.1, F40.1, F33.1, F45.1, F61 (ängstlich)  Therapie: Lasea 1-0-0 für 3 Monate, Pregabalin Kps. bis zu 4x 25 mg, Atarax bei Bedarf,  gastroenterologische Abklärung, Erhöhung der Familienbeihilfe aufgrund des frühen  Erkrankungsbeginnes, der Dauer und Intensität der Beschwerden und der Komplexität der  Symptome dringlich indiziert, Psychotherapie weiter, Vagus-Stimulation, Kontrolle bei Bedarf  Nachgereichte Befunde:  Arztbrief DrD, FA Neurologie, 3.8.2022 … (Anm.: bereits im Vorgutachten)  Ärztliches Gutachten Pensionsversicherungsanstalt, DrJ, Allgemeinmedizin, 25.5.2021  Diagnose: Angst und depressive Störung gemischt, emotional-instabile Persönlichkeitsstörung,  Zwangshandlungen, Panikstörung  Bestätigung MagAA, Psychotherapeutin 24.5.2021 … (Anm.: bereits im Vorgutachten)  Krankenhaus XY, Neurologie Ambulanz, 23.7.2018 … (Anm.: bereits im Vorgutachten)  Kurzbrief AKH, Psychiatrie, 24.9.2015  mittelgradig depressive Episode, Angststörung F41  Entlassungsbericht Klinik XX, 15.1.2015  Diagnose: generalisierte Angststörung, rezidivierend depressive Störung - gegenwärtig  remittiert, Akzentuierung von selbstunsicheren, depressiven und emotional-instabilen  Persönlichkeitszügen, Spannungskopfschmerzen, V.a, Cluster-Kopfschmerz  KJP AKH, 12.9.2012  Diagnose: mittelgradige depressive Episode, Alkohol - schädlicher Gebrauch, selbstverletzendes  Verhalten, Vd. a. Migräne ohne Aura  Kriseninterventionelle Aufnahme zur Entlastung ... kann sich am folgenden Tag von Suizidideen  distanzieren.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/149825.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `Universität_Wien` 🏆

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `c6e5750e`  
**Description:**
Matches the specific organization 'Universität Wien'.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 15997 |

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

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

## `BMI_Abbreviation` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `84159154`  
**Description:**
Matches the specific abbreviation 'BMI' (Bundesministerium für Inneres) as an organization.

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 17702 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

</details>

---

## `Gerichtshof_Europaeischen_Union` 🏆

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `7da57f87`  
**Description:**
Matches the specific organization 'Gerichtshof der Europäischen Union'.

**Content:**
```
\bGerichtshof\s+der\s+Europ\u00e4ischen\s+Union\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 27 | 27 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 27 | 0 | 12616 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134614.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134614.1_1`)


An den  Gerichtshof der Europäischen Union  Kanzlei des Gerichtshofes  Rue du Fort Niedergrünewald  L-2925 Luxemburg

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/134614.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134614.1_7`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Richter1, den RichterRichter2  sowie die fachkundigen Laienrichter Richter3 und Richter4 in der Beschwerdesache Massimo Heimker,  Klöpplergasse 7, 9781 Unterpirkach, Österreich  Österreich, vertreten durch Steuerberater Vertreter, AdresseVertreter,  Österreich, betreffend die Beschwerde vom 27. Februar 2012 gegen den  Umsatzsteuerbescheid 2010 des Finanzamtes X vom 27. Jänner 2012 beschlossen:  Dem Gerichtshof der Europäischen Union wird gemäß Art. 267 AEUV folgende Frage zur  Vorabentscheidung vorgelegt:  Ist die Richtlinie 2006/112/EG des Rates vom 28. November 2006 über das gemeinsame  Mehrwertsteuersystem in der Fassung der Richtlinie 2008/8/EG des Rates vom 12. Februar  2008 so auszulegen, dass die nationalen Behörden und Gerichte den Ort einer Dienstleistung,  der formal nach dem geschriebenen Recht in dem anderen Mitgliedstaat, in welchem sich der  Sitz des Leistungsempfängers befindet, liegt, als im Inland liegend anzusehen haben, wenn der  leistungserbringende inländische Steuerpflichtige hätte wissen müssen, dass er sich durch die  erbrachte Dienstleistung an einer im Rahmen einer Leistungskette begangenen  Mehrwertsteuerhinterziehung beteiligt?

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Massimo Heimker` (person)
- `Klöpplergasse 7, 9781 Unterpirkach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/137101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137101.1_68`)


Der Gerichtshof der Europäischen Union (EuGH) hat mit Urteil vom 16. Juni 2022 in der  Rechtssache C-328/20 über eine Vertragsverletzungsklage der Europäischen Kommission nach  Art. 258 AEUV gegen die Republik Österreich in Ziffer 2 seines Urteilstenores bezughabend  ausgesprochen: „Die Republik Österreich hat durch die – auf die Änderung von … und von § 33  des Bundesgesetzes über die Besteuerung des Einkommens natürlicher Personen vom 7. Juli  1988 in der durch das Jahressteuergesetz 2018 vom 14. August 2018 und das Bundesgesetz, mit  dem das Familienlastenausgleichsgesetz 1967, das Einkommensteuergesetz 1988 und das  Entwicklungshelfergesetz geändert werden, vom 4. Dezember 2018 geänderten Fassung  zurückgehende – Einführung eines Anpassungsmechanismus in Bezug auf den Familienbonus  Plus, … und den Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in  einem anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der  Verordnung Nr. 492/2011 verstoßen.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/137101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137101.1_74`)


Auch der Verstoß u.a. gegen Verordnungen der EU ist  eine Vertragsverletzung (vgl. aaO, § 258 Rn. 4 f.).   Art. 260 Abs. 1 AEUV bestimmt: „Stellt der Gerichtshof der Europäischen Union fest,  dass ein Mitgliedstaat gegen eine Verpflichtung aus den Verträgen verstoßen hat, so  hat dieser Staat die Maßnahmen zu ergreifen, die sich aus dem Urteil des Gerichtshofs  ergeben.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/137117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137117.1_38`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  –        die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf  die Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in  einem anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der  Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004  zur Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7  Abs. 2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5.  April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  –        die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf  den Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und  den Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/137334.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137334.1_46`)


Der Gerichtshof der Europäischen Union hat am 16. Juni 2022 betreffend Indexierung der  Familienbeihilfe sowie bestimmter familienbezogener Steuerbegünstigungen auf Grund einer  Klage der Europäischen Kommission entschieden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/137334.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137334.1_52`)


Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung ist auch im gegenständlichen Beschwerdeverfahren vor dem Bundesfinanzgericht zu  beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/137334.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137334.1_111`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/137335.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137335.1_10`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  Der Gerichtshof der Europäischen Union (EuGH) hat mit Urteil vom 16. Juni 2022 in der  Rechtssache C-328/20 über eine Vertragsverletzungsklage der Europäischen Kommission nach  Art. 258 AEUV gegen die Republik Österreich in Ziffer 2 seines Urteilstenores bezughabend  ausgesprochen: „Die Republik Österreich hat durch die … Einführung eines  Anpassungsmechanismus in Bezug auf den Familienbonus Plus, … und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/137335.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137335.1_16`)


Auch der Verstoß u.a. gegen Verordnungen der EU ist  eine Vertragsverletzung (vgl. aaO, § 258 Rn. 4 f.).   Art. 260 Abs. 1 AEUV bestimmt: „Stellt der Gerichtshof der Europäischen Union fest,  dass ein Mitgliedstaat gegen eine Verpflichtung aus den Verträgen verstoßen hat, so  hat dieser Staat die Maßnahmen zu ergreifen, die sich aus dem Urteil des Gerichtshofs  ergeben.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/137683.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137683.1_41`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf den Alleinverdienerabsetzbetrag für Erwerbstätige, deren Kinder  ständig in einem anderen Mitgliedstaat wohnen, mit dem Unionsrecht vereinbar ist, eindeutig  beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/137736.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137736.1_59`)


Der Gerichtshof der Europäischen Union (EuGH) hat mit Urteil vom 16. Juni 2022 in der  Rechtssache C-328/20 über eine Vertragsverletzungsklage der Europäischen Kommission nach  Art. 258 AEUV gegen die Republik Österreich in Ziffer 2 seines Urteilstenores bezughabend  ausgesprochen:   "Die Republik Österreich hat durch die - auf die Änderung … von § 33 des Bundesgesetzes über  die Besteuerung des Einkommens natürlicher Personen vom 7. Juli 1988 in der durch das  Jahressteuergesetz 2018 vom 14. August 2018 und das Bundesgesetz, mit dem das  Familienlastenausgleichsgesetz 1967, das Einkommensteuergesetz 1988 und das  Entwicklungshelfergesetz geändert werden, vom 4. Dezember 2018 geänderten Fassung  zurückgehende - Einführung eines Anpassungsmechanismus in Bezug auf den Familienbonus  Plus, … und den Alleinverdienerabsetzbetrag, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung  Nr. 492/2011 verstoßen."

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/137736.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137736.1_67`)


Art. 260 Abs. 1 AEUV bestimmt:   "Stellt der Gerichtshof der Europäischen Union fest, dass ein Mitgliedstaat gegen eine  Verpflichtung aus den Verträgen verstoßen hat, so hat dieser Staat die Maßnahmen zu  ergreifen, die sich aus dem Urteil des Gerichtshofs ergeben."

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/137736.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137736.1_78`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/137847.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137847.1_14`)


Die Europäische Kommission leitete zu dieser  Frage gegen Österreich ein Vertragsverletzungsverfahren nach Art 258 AEUV ein, in dem der  Gerichtshof der Europäischen Union mit Urteil vom 16.06.2022, C-328/20, entschieden hat,  dass Österreich mit der Bindung der Familienleistungen an die Kaufkraftverhältnisse im  Wohnmitgliedstaat gegen Unionsrecht verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/138054.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138054.1_68`)


...  Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte festzustellen, dass  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der Verordnung  (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004 zur  Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7 Abs.  2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5. April  2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  7 von 11 Seite 8 von 11

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/138165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138165.1_28`)


Demnach stünde dem Bf ein indexierter Alleinverdienerabsetzbetrag für zwei Kinder von  jährlich 414,12 € und ein indexierter Unterhaltsabsetzbetrag für ein Kind von monatlich 18,07  €, das sind für 12 Monate 216,84 €, zu.  Der Gerichtshof der Europäischen Union hat mit Urteil vom EuGH 16.06.2022, C-328/20,  Kommission gegen Österreich, betreffend Indexierung der Familienbeihilfe sowie bestimmter  familienbezogener Steuerbegünstigungen auf Grund einer Klage der Europäischen Kommission  entschieden, dass der Anpassungsmechanismus, nach dem das für die Höhe der  Familienleistungen sowie der sozialen und steuerlichen Vergünstigungen maßgebliche  Kriterium der Auslandswohnsitz der Kinder ist, Wanderarbeitnehmer stärker als  österreichische Staatsbürger betrifft.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/138352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138352.1_23`)


Mit Beschluss vom 16. April 2020 zu RE/7100001/2020 hat das Bundesfinanzgericht den  Gerichtshof der Europäischen Union das Ersuchen um Vorabentscheidung gestellt  (protokolliert zu C-163/20), ob die Indexierung von Familienleistungen durch den  österreichischen Gesetzgeber unionsrechtskonform ist.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/138352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138352.1_24`)


Mit Urteil vom 16. Juni 2022, C-328/20 hat der Gerichtshof der Europäischen Union zu Recht  erkannt und wie folgt entschieden:  "1.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_11`)


Nach Stellung des diesbezüglichen Vorabentscheidungsersuchens eines Richters des  Bundesfinanzgerichts reichte die Europäische Kommission mit Beschluss vom 14.05.2020 im  Verfahren INFR (2018) 2372 am 22.07.2020 Klage gegen die Republik Österreich beim  Gerichtshof der Europäischen Union ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_14`)


Der Gerichtshof der Europäischen Union entschied mit Urteil EuGH 16 06.2022, C-328/20,  ECLI:EU:C:2022:468, im Vertragsverletzungsverfahren (die Indexierung nach der  unterschiedlichen Kaufkraft in den einzelnen Mitgliedstaaten bzw. Vertragsstaaten wird dort  als Anpassungsmechanismus bezeichnet):  2 von 14 Seite 3 von 14

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_19`)


04. 2020, RE/7100001/2020 an den Gerichtshof der Europäischen Union  gemäß Art. 267 AEUV gestellte Ersuchen um Vorabentscheidung, ob die Indexierung von  Familienleistungen durch den österreichischen Gesetzgeber nach der Kaufkraft in den  einzelnen Mitgliedsstaaten bzw. Vertragsstaaten unionsrechtskonform ist, protokolliert zu C- 163/20, gemäß Artikel 100 Abs. 1 Verfahrensordnung des Gerichtshofs der Europäischen Union  und § 290 Abs 3 BAO zurückgenommen.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_22`)


III. Erwägungen  Der Gerichtshof der Europäischen Union wurde mit der Sache vom Bundesfinanzgericht mittels  des Vorabentscheidungsverfahrens gemäß Beschluss BFG 16.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_124`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/139969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139969.1_34`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der  Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004  zur Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7  Abs. 2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5.  April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_95`)


Der Gerichtshof der Europäischen Union hat in seinem Urteil festgehalten, dass eine solche  Bestimmung nicht gegen die Kapitalverkehrsfreiheit verstößt, wenn der Kapitalanlagefonds in  seinem Sitzstaat nicht besteuert wird und die Einkünfte den Anteilinhabern zugerechnet  werden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_365`)


Der Gerichtshof der Europäischen Union hat in seinem Urteil festgehalten, dass eine solche  Bestimmung nicht gegen die Kapitalverkehrsfreiheit verstößt, wenn der Kapitalanlagefonds in  seinem Sitzstaat nicht besteuert wird und die Einkünfte den Anteilinhabern zugerechnet  werden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

</details>

---

## `Verwaltungsgerichtshof_entities` 🏆

**F1:** 0.320 | **Precision:** 1.000 | **Recall:** 0.191  

**Format:** `regex`  
**Rule ID:** `6d815816`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its grammatical variations (genitive 'Verwaltungsgerichtshofes', dative 'Verwaltungsgerichtshofs') as organizations.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.191 | 0.320 | 3429 | 3429 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3429 | 0 | 14566 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_2`)


II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_76`)


Dies weil es an einer Rechtsprechung des Verwaltungsgerichtshofes zu § 6 Abs 1 lit b FLAG 1967 als auch zur thematisierten Auslegung des § 6 Abs 2 lit d FLAG 1967 fehlt.     Innsbruck, am 24. Juli 2014

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_56`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision) Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_58`)


Die Lösung der Rechtsfrage ergab sich aus der einheitlichen Rechtsprechung des Verwaltungsgerichtshofes (vgl  VwGH 31.5.1995, 94/16/0237;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_181`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_4`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_40`)


Zur Unzulässigkeit einer Revision zu Erkenntnis und Beschluss:  Gegen diese Entscheidungen ist gemäß Art. 133 Abs. 4 B-VG eine ordentliche Revision nicht  zulässig, da das Erkenntnis und der Beschluss nicht von der Lösung einer Rechtsfrage abhängt,  der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis und der Beschluss  nicht von der Rechtsprechung des Verwaltungsgerichtshofes zur Aussetzung der Einhebung  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_36`)


Diese Ansicht bestätigte der Verwaltungsgerichtshof auch im Beschluss VwGH 29.03.2017, Ro  2016/15/0036 sowie VwGH 26.04.2017, Ro 2015/13/0011VwGH.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_53`)


Zulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_37`)


Abschließend erfolgte im Vorlageantrag ein Verweis auf ein unter der GZ.  RR/3100030/2019 beim Verwaltungsgerichtshof anhängiges Verfahren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_40`)


Mit Beschluss  vom 4. Dezember 2019, dem Bundesfinanzgericht zugestellt am 19. Dezember 2019, hatte  der Verwaltungsgerichtshof die außerordentliche Revision des betreffenden  Abgabepflichtigen, wie der Bf vertreten durch RA, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_66`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_70`)


Dass der  Besuch von Seminaren für neurolinguistisches Programmieren (NLP) oder für Schauspiel und  Performance aber auch im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den Bereich  der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht (zB VwGH 29.1.2004, 2000/15/0009;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_77`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_79`)


Zum  § 16 liegt eine einheitliche Rechtsprechung des Verwaltungsgerichtshofes vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach   Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_79`)


6. Aufgrund einer vom Finanzamt dagegen erhobenen Amtsbeschwerde hat der  Verwaltungsgerichtshof mit Erkenntnis vom 19.4.2016, 2013/15/0288, die vorgenannte UFS-

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_118`)


Der Mittelpunkt der Lebensinteressen besteht an dem Ort, zu dem die Person die engeren  persönlichen und wirtschaftlichen Beziehungen unterhält. Auch nach der Rechtsprechung des  Verwaltungsgerichtshofs ist unter diesem Begriff der Ort (in jenem Staat) zu verstehen, zu dem  der Steuerpflichtige die engeren persönlichen und wirtschaftlichen Beziehungen hat (vgl. zB  6 von 15 Seite 7 von 15

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_235`)


Mehrwertsteuer-Richtlinie (RL  77/388/EWG), deren Rechtslage der nunmehr geltenden MwStSystRL (RL 2006/112/EG)  vergleichbar ist, und auf die dazu vertretene Rechtsansicht des Verwaltungsgerichtshofes  hinzuweisen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_247`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_261`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_69`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_70`)


Eine derartige Rechtsfrage liegt im zu beurteilenden Fall nicht vor, da die  Schätzungsberechtigung direkt auf den Grundlagen der Bundesabgabenordnung fußt, bzw. die  Schätzungsmethode in Einklang mit der dezidiert dargestellten Rechtsprechung des  Verwaltungsgerichtshofes steht.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Feichtenschlager` (person)
- `Daisy Wegelein` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `61-004/6209` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_100`)


Der Verwaltungsgerichtshof hat in seinem Erkenntnis vom 15.09.2016, Ro 2015/15/0009,  Folgendes ausgesprochen:   „Begünstigungsfähig als außergewöhnliche Belastung ist grundsätzlich nur der durch die  Behinderung bedingte Mehraufwand, somit jener Aufwand, der über die typischen Kosten der  Lebensführung hinausgeht (vgl. VwGH vom 2. Juni 2004, 2003/13/0074, VwSlg. 7933/F).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_142`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_11`)


III. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_184`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  14 von 15 Seite 15 von 15

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_185`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_5`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_60`)


der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_61`)


Dies trifft nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes nicht zu, wenn die  in Betracht kommenden Normen klar und eindeutig sind (vgl. VwGH 6.4.2016, Ro  2016/16/0006 mit vielen weiteren Nachweisen).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_75`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_4`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_208`)


Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_210`)


Dies trifft nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes nicht zu, wenn die  in Betracht kommenden Normen klar und eindeutig sind (vgl. VwGH 6.4.2016, Ro  2016/16/0006 mit vielen weiteren Nachweisen).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_5`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_21`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es Aufgabe des  Vertreters, im Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran  gehindert haben, die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH  23.03.2010, 2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_23`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliegt Ihnen als Vertreter,  Nachweise dafür, wie viel Zahlungsmittel zur Verfügung gestanden sind und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_62`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es  Aufgabe des Geschäftsführers, darzutun, weshalb er den auferlegten Pflichten nicht  entsprochen habe, insbesondere nicht habe Sorge tragen können, dass die Gesellschaft die  angefallenen Abgaben entrichtet hat, widrigenfalls von der Abgabenbehörde eine schuldhafte  Pflichtverletzung angenommen werden darf (VwGH 22.9.1999, 96/15/0049).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_77`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes lastet auf dem Vertreter auch  die Verpflichtung zur Errechnung einer entsprechenden Quote und des Betrages, der bei  anteilsmäßiger Befriedigung der Forderungen der Abgabenbehörde zu entrichten gewesen  wäre (VwGH 28.2.2014, 2012/16/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_87`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_88`)


Nach der durch das  Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.1.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_96`)


Im Übrigen ist eine  Einbringlichmachung bei der Primärschuldnerin unzweifelhaft nicht gegeben, weshalb nach der  Rechtsprechung des Verwaltungsgerichtshofes die Frage der Einbringlichkeit der  Haftungsschuld beim Haftenden von der Abgabenbehörde bei ihren  Zweckmäßigkeitsüberlegungen vernachlässigt werden kann (VwGH 16.12.1999, 97/16/0006;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_101`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Verwaltungsgerichtes ist gemäß Art. 133 B-VG die Revision (nur)  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_102`)


Da diese Voraussetzungen im Beschwerdefall im Hinblick auf die oben  wiedergegebene Rechtsprechung des Verwaltungsgerichtshofes nicht vorliegen, war  auszusprechen, dass die Revision unzulässig ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_97`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_99`)


Rechtsfragen von grundsätzlicher  Bedeutung lagen nicht vor und ist das Gericht auch nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abgewichen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_32`)


Ob und gegebenenfalls wie der Bezieher die erhaltenen Beträge verwendet hat,  ist unerheblich (vgl. das Erkenntnis des Verwaltungsgerichtshofes vom 28.10.2009,  Geschäftszahl 2008/15/0329).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_51`)


Der Verwaltungsgerichtshof hat in einem Rechtssatz zu seinem Erkenntnis vom 28.11.2007,  Geschäftszahl 2007/15/0058, Folgendes festgehalten:  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_55`)


Der Verwaltungsgerichtshof hat ferner in einem Rechtssatz zu seinem Erkenntnis vom  21.09.2009, Geschäftszahl 2009/16/0081 Folgendes ausgeführt:  "Der Verzicht einer anspruchsberechtigten Person auf Bezug der Familienbeihilfe zugunsten des  anderen Elternteiles setzt nach § 2a FLAG voraus, dass das Kind, für das der  Familienbeihilfenanspruch besteht, zum gemeinsamen Haushalt der Eltern gehört (vgl. auch  das hg.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_64`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_65`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_67`)


Das Erkenntnis  stützte sich vielmehr auf den Gesetzestext und die angeführte Judikatur des  Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_181`)


In  Fällen, in denen beide Kriterien noch keine klare Abgrenzung zwischen einer selbständig und  einer nichtselbständig ausgeübten Tätigkeit ermöglichen, ist nach ständiger Rechtsprechung  des Verwaltungsgerichtshofes auf weitere Abgrenzungskriterien (wie etwa auf das Fehlen eines  Unternehmerrisikos oder die Befugnis, sich vertreten zu lassen) Bedacht zu nehmen (vgl VwGH  10.11.2004, 2003/13/0018 vS, sowie seitdem zB VwGH 22.3.2010, 2009/15/0200;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_201`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_4`)


Z 10/12 139,46  ST 2012 285,07  SZA 2012 1.554,94  SZB 2012 292,84  SZC 2012 168,36  Summe          59.286,56  Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_59`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es  Aufgabe des Geschäftsführers, darzutun, weshalb er den auferlegten Pflichten nicht  entsprochen habe, insbesondere nicht habe Sorge tragen können, dass die Gesellschaft die  angefallenen Abgaben entrichtet hat, widrigenfalls von der Abgabenbehörde eine schuldhafte  Pflichtverletzung angenommen werden darf (VwGH 22.09.1999, 96/15/0049).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_74`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes lastet auf dem Vertreter auch  die Verpflichtung zur Errechnung einer entsprechenden Quote und des Betrages, der bei  anteilsmäßiger Befriedigung der Forderungen der Abgabenbehörde zu entrichten gewesen  wäre (VwGH 28.02.2014, 2012/16/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_80`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_82`)


Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.01.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_117`)


Im Übrigen ist eine  Einbringlichmachung bei der Primärschuldnerin unzweifelhaft nicht gegeben, weshalb nach der  Rechtsprechung des Verwaltungsgerichtshofes die Frage der Einbringlichkeit der  Haftungsschuld beim Haftenden von der Abgabenbehörde bei ihren  Zweckmäßigkeitsüberlegungen vernachlässigt werden kann (VwGH 16.12.1999, 97/16/0006).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_119`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_123`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_124`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_33`)


Dass ein Zustellmangel unterlaufen sei und der Bf. nicht rechtzeitig vom Zustellvorgang  Kenntnis erlangen habe können, sei nicht anzunehmen, habe er doch zum Vorhalt der  Verspätung nicht Stellung genommen, sondern lediglich seinen Einspruch neuerlich  übermittelt.  Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sei die Rechtsmittelfrist eine  zwingende, auch durch die Behörde nicht erstreckbare gesetzliche Frist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_76`)


Die Behörde hat dem Bf. - entsprechend der Judikatur des Verwaltungsgerichtshofes - mit  Verspätungsvorhalt vom 28. Jänner 2020 unter näheren Ausführungen zur Kenntnis gebracht,  dass sein am 11. Jänner 2020 mittels E-Mail eingebrachtes Rechtsmittel nach der Aktenlage  verspätet erscheine, und ihn aufgefordert, für den Fall einer nicht nur vorübergehenden  Abwesenheit von der Abgabestelle zum Zeitpunkt der Zustellung der Strafverfügung  entsprechende Bescheinigungsmittel vorzulegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_92`)


Zulässigkeit der Revision   Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine ordentliche Revision für die  belangte Behörde nicht zulässig, da das Erkenntnis nicht von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis nicht von  der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des VwGH nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_93`)


Die Revision ist im gegenständlichen Fall nicht zulässig, da in freier Beweiswürdigung von einer  ordnungsgemäßen Zustellung auszugehen war und sich die Rechtsfolge der Zurückweisung  wegen erwiesener Verspätung aus dem Gesetz ergibt, weshalb es sich auch um keine  Rechtsfrage von grundsätzlicher Bedeutung handelt.   Eine Revision an den Verwaltungsgerichtshof durch die beschwerdeführende Partei wegen  Verletzung in Rechten nach Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft  Gesetzes nicht zulässig, wenn in einer Verwaltungsstrafsache eine Geldstrafe von bis zu 750  Euro und keine (primäre) Freiheitsstrafe verhängt werden durfte und überdies im Erkenntnis  eine Geldstrafe von nicht mehr als 400 Euro verhängt wurde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_161`)


Gemäß § 33 TP 5 Abs. 1 GebG unterliegen Bestandverträge (§§ 1090 ff. ABGB) und sonstige  Verträge, wodurch jemand den Gebrauch einer unverbrauchbaren Sache auf eine gewisse Zeit  und gegen einen bestimmten Preis erhält, nach dem Wert im allgemeinen 1 v.H.   IV. Erwägungen:   Der Begriff des "Wertes" ist im Gesetz selbst nicht definiert, jedoch hat der  Verwaltungsgerichtshof in ständiger Judikatur die Auffassung vertreten, dass zum „Wert“ alle  jene Leistungen zählen, die der Bestandnehmer erbringen muss, um in den Gebrauch der  Bestandsache zu gelangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_163`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes zählen zum "Wert", von  dem die Gebühr für Bestandverträge zu berechnen ist, alle Leistungen, zu deren Erbringung  sich der Bestandnehmer verpflichtet hat, um in den Genuss des Gebrauchsrechtes an der  Bestandsache zu gelangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_193`)


Der Verwaltungsgerichtshof stellte in seinem Erkenntnis VwGH 07.10.1985, 85/15/0136 fest,  dass in allen Fällen eines echten Franchisevertrages der Franchisenehmer im eigenen Namen  und auf eigene Rechnung handelt. Darüber hinaus führte er aus, dass ein Franchisevertrag  immer nur dann vorliegt, wenn eine im Vertrag enthaltene Pacht einer unverbrauchbaren  14 von 19 Seite 15 von 19

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_237`)


Auf Grund der dargestellten Rechtslage, insbesondere im Hinblick auf das Erkenntnis des  Verwaltungsgerichtshofes vom 07.10.1985, 85/15/0136, worin dieser feststellt, dass ein  Franchisevertrag immer nur dann vorliegt, wenn eine im Vertrag enthaltene Pacht einer  unverbrauchbaren Sache vollkommen unberücksichtigt bleiben kann, bildet auch die  Franchisegebühr einen Bestandteil der Bemessungsgrundlage für die Rechtsgeschäftsgebühr.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_240`)


(siehe auch Vorlageantrag RZ 10)   V. Unzulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_241`)


Die getroffene Entscheidung entspricht der Judikatur des Verwaltungsgerichtshofes  07.10.1985, 85/15/0136 und des BFG 26.07.2016, RV/7100282/2010 sowie weitere, weshalb  eine Revision nicht für zulässig erachtet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_3`)


2.Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_69`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_51`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  4 von 5 Seite 5 von 5

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_52`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_3`)


Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_29`)


Zur Revision (Art. 133 Abs. 4 iVm Abs. 9 B-VG):  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_5`)


2. Eine Revision gegen dieses Erkenntnis an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) ist nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_592`)


Das Ergebnis eines derartigen Beweisverfahrens  ist der Kontrolle durch den Verwaltungsgerichtshof nur insofern zugänglich, als es sich um die  Beurteilung handelt, ob der Sachverhalt genügend erhoben ist und ob die bei der  Beweiswürdigung vorgenommenen Erwägungen schlüssig sind, also nicht den Denkgesetzen  oder dem allgemeinen Erfahrungsgut widersprechen (vgl.  etwa das hg.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_700`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  33 von 34 Seite 34 von 34

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `E.` (person)
- `Bundesfinanzgerichtes` (organisation)

</details>

---

## `Verfassungsgerichtshof_entities` 🏆

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `42bddfd3`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.024 | 218 | 218 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 218 | 0 | 17152 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_22`)


II. Das Bundesfinanzgericht hat erwogen:  Der Verwaltungsgerichtshof hat die Entscheidung des Bundesfinanzgerichtes mit Erkenntnis  vom 20.5.2020, Ra 2017/13/0072, mit folgender Begründung aufgehoben:  „Mit Erkenntnis vom 4. Dezember 2019, G 159/2019-13, G 226/2019-11, G 248/2019-8, sprach  der Verfassungsgerichtshof u.a. aufgrund eines aus Anlass des vorliegenden Falls gestellten  Antrags des Verwaltungsgerichtshofes (protokolliert zu G 226/2019) aus, dass der Satz  „Der Antrag ist vor Ablauf der für Wiederaufnahmsanträge nach § 304 BAO maßgeblichen Frist  zu stellen.“ in § 295 Abs. 4 BAO des Bundesgesetzes über allgemeine Bestimmungen und das  Verfahren für die von den Abgabenbehörden des Bundes, der Länder und Gemeinden  verwalteten Abgaben (Bundesabgabenordnung - BAO), BGBI. Nr. 194/1961 idF BGBI. I  Nr. 76/2011, verfassungswidrig war.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)
- `Bundesfinanzgerichtes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_23`)


Da es sich im vorliegenden Fall um einen Anlassfall iSd Art. 140 Abs. 7 B-VG handelt, ist der  vom Verfassungsgerichtshof für verfassungswidrig erklärte letzte Satz des § 295 Abs. 4 BAO,  wonach ein Antrag nach § 295 Abs. 4 BAO vor Ablauf der für Wiederaufnahmsanträge nach  § 304 BAO maßgeblichen Frist zu stellen ist, im gegenständlichen Fall nicht anzuwenden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_58`)


Die Verfassungswidrigkeit wurzle in den angewendeten gesetzlichen Regelungen selbst, welche  sich nur bei entsprechender Aufhebung durch den Verfassungsgerichtshof beheben lasse.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_17`)


Mit diesem Vorbringen wird aber schon deshalb kein unverhältnismäßiger Nachteil aus dem  Vollzug des angefochtenen Erkenntnisses aufgezeigt, weil die Rw. nicht darstellt, weshalb ihr  bei ihrem Einkommen nicht zumindest eine ratenweise Tilgung der Abgabenschuld möglich  wäre (vgl. § 212a BAO und VwGH 9.7.2008, AW 2008/13/0029, sowie VwGH 27.5.2011,  AW 2011/13/0014, oder den Beschluss des Verfassungsgerichtshofes vom 11. August 1999,  B 1181/99).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_25`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_28`)


Der Verfassungsgerichtshof hat in Bezug auf die zeitliche Anwendbarkeit des § 4 Abs. 2 Z 2  EStG 1988 mit Beschluss vom 8. Juni 2020, E 2108/2019-15, ausgesprochen, dass selbst wenn  der Bestimmung der Vorschrift des § 4 Abs. 2 Z 2 EStG materiell-rechtlicher Charakter  zuzumessen wäre, der Gleichheitssatz deren Anwendung auf die ab Inkrafttreten  durchgeführten Veranlagungen der Zeiträume ab 2003 nicht entgegen stehe, da die Vorschrift  in den Fällen der Bilanzberichtigung doch – je nach Sachlage zugunsten wie auch zulasten des  Steuerpflichtigen – der Erzielung einer richtigen Totalgewinnbesteuerung diene, die jener  entsprechen solle, wenn die Bilanz von vornherein richtig erstellt worden wäre.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_32`)


Da die Streitfrage durch die zitierte Judikatur des Verfassungsgerichtshofes geklärt ist, ist eine  Revision nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_108`)


BFG 17.03.2014, RV/7100539/2014):  Festgehalten wird noch, dass der Verfassungsgerichtshof gegen die Einschränkung der  Beweisführung des Grades der Behinderung oder der voraussichtlichen dauerhaften  Unfähigkeit, sich selbst den Erwerb zu verschaffen, im Erkenntnis vom 10.12.2007, B 700/07,  keine verfassungsrechtlichen Bedenken geäußert (vgl. VwGH 22.12.2011, 2009/16/0307) und  weiters erkannt hat, dass von Gutachten NUR nach "entsprechend qualifizierter  Auseinandersetzung" abgegangen werden kann, wenn diese nicht schlüssig sind (vgl. VwGH  13.12.2012, 2009/16/0325;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_151`)


Der Verwaltungsgerichtshof hat sich in seiner Rechtsprechung (sh. zB VwGH 18.11.2008,  2007/15/0019, und VwGH 18.12.2008, 2007/15/0151) der Rechtsansicht des  Verfassungsgerichtshofes angeschlossen;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_388`)


Der Verfassungsgerichtshof äußerte in seinem Erkenntnis vom 10.12.2007, B 700/07 keine  verfassungsrechtlichen Bedenken gegen die Einschränkung der Beweisführung des Grades der  Behinderung oder der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu  verschaffen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_72`)


In diesem Zusammenhang darf auch darauf hingewiesen werden, dass der  Verfassungsgerichtshof den Ausschluss der Familienbeihilfe bei ständigem Aufenthalt des  Kindes im Ausland (§ 5 Abs 3 FLAG 1967) als verfassungsrechtlich zulässig erachtet hat (vgl die  Erkenntnisse VfGH 15.6.2002, G 112/99, VfSlg 16.542, und VfGH 14.12.2001, B 2366/00, VfSlg  16.380).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_3`)


Begründung  In dem Verfahren, in dem die Beschwerdeführerin [...] (in der Folge als Antragstellerin  bezeichnet) den Antrag auf Verfahrenshilfe gestellt hatte, hatte einen handschriftlichen Antrag  auf Rückzahlung eines Betrages von 360 € vom 20.11.2019 an die belangte Behörde zum Inhalt.  Begründet wurde dieser damit, dass der Betrag zu Unrecht eingefordert wurde, weil eine  Beschwerde beim Verfassungsgerichtshof nicht von einem Rechtsanwalt unterfertigt worden  wäre und daher kein Gebührenanspruch entstanden wäre.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_15`)


In der rechtlichen  Würdigung wurde angemerkt wurde, dass selbst bei fristgerechter Einbringung der  Beschwerde eine Abweisung zu treffen gewesen wäre, da die Verpflichtung zur Zahlung einer  Eingabegebühr gem. § 17a VfGG unabhängig davon besteht, ob diese Einbringung den  formalen Voraussetzungen für Beschwerden an den Verfassungsgerichtshof entspricht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_22`)


Das Bundesfinanzgericht stellte mit Beschluss vom 20. Oktober 2020 an den  Verfassungsgerichtshof einen Normenprüfungsantrag hinsichtlich der Bestimmung des § 19  Abs 1 EStG 1988.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_25`)


Beim Verfassungsgerichtshof ist diesbezüglich unter der Zahl G 223/2020 ein weiterer  Normenprüfungsantrag anhängig, außerdem eine unter der Zahl E 513/2020 erfasste  Beschwerde gemäß Art. 144 Abs 1 B-VG.   B. Rechtslage  Gemäß § 292 Abs. 1 BAO ist auf Antrag einer Partei (§ 78), wenn zu entscheidende  Rechtsfragen besondere Schwierigkeiten rechtlicher Art aufweisen, ihr für das  Beschwerdeverfahren Verfahrenshilfe vom Verwaltungsgericht insoweit zu bewilligen,  1. als die Partei außerstande ist, die Kosten der Führung des Verfahrens ohne Beeinträchtigung  des notwendigen Unterhalts zu bestreiten und  2.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_51`)


Der Verfassungsgerichtshof wird sich in den anhängigen  Normenprüfungs- und Beschwerdeverfahren mit dieser Frage auseinandersetzen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_65`)


Weder offenbar aussichtslos noch mutwillig  Eine Beschwerde gegen den Einkommensteuerbescheid 2018 kann aufgrund der geschilderten  verfassungsrechtlichen Bedenken, über die der Verfassungsgerichtshof abzusprechen hat,  weder als offenbar aussichtslos noch als mutwillig iSd § 292 Abs. 5 BAO bezeichnet werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_59`)


Zur Rechtsnatur der Einkommensteuerrichtlinien ist auf das Erkenntnis des  Verwaltungsgerichtshofes vom 31.01.2018, Ra 2017/15/0038, hinzuweisen:  „Der Verfassungsgerichtshof ist in seinem Erkenntnis vom 28. Juni 2017, V 4/2017, von seiner  bisherigen Rechtsprechung zu Art. 89 B-VG und Art. 139 Abs. 3 bzw. Art. 140 Abs. 3 B-VG,  wonach nicht gehörig kundgemachte Verordnungen von den Gerichten auch ohne Anfechtung  vor dem Verfassungsgerichtshof von vorneherein nicht anzuwenden seien, abgegangen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_60`)


Er  vertritt nunmehr die Auffassung, dass auch Gerichte gesetzwidrig kundgemachte Verordnungen  anzuwenden haben und diese, wenn sie Bedenken gegen ihre rechtmäßige Kundmachung  haben, vor dem Verfassungsgerichtshof anzufechten haben;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_61`)


bis zur Aufhebung durch den  Verfassungsgerichtshof sind sie für jedermann verbindlich (vgl. Punkt 2.9 des genannten  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_90`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_69`)


Nach dem Erkenntnis des Verfassungsgerichtshofes VfGH 10. 12. 2007, B 700/07, kann von  solchen Gutachten nach "entsprechend qualifizierter Auseinandersetzung" auch abgegangen  werden (vgl. BFG 27.09.2017, RV/7102586/2017).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_180`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_18`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_142`)


In den zuletzt angeführten Erkenntnissen hat das Bundesfinanzgericht unter Verweis auf das  Erkenntnis BFG 13.7.2015, RV/5100538/2014, darüber hinaus auch festgehalten, dass die  Polizeigrundausbildung die vom Verfassungsgerichtshof herausgearbeiteten Kriterien eines  anerkannten Lehrverhältnisses im Sinne des § 5 Abs. 1 lit. b FLAG 1967 erfüllt und daher als ein  "anerkanntes Lehrverhältnis" anzusehen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_79`)


Eine Verletzung verfassungsrechtlicher Gebote sei vom Verfassungsgerichtshof bislang nicht  festgestellt worden, er habe die Behandlung entsprechender Beschwerden abgelehnt (siehe  diverse Beschlüsse vom 1.12.2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_188`)


Er hat  nach der Rechtsprechung des Verfassungsgerichtshofes auch die Funktion der Abgeltung von  Verzugszinsen und der Abgeltung von erhöhtem, durch die nicht rechtzeitige Einreichung der  Abgabenerklärungen verursachten Verwaltungsaufwand (Ritz, BAO6, § 135 Tz 1).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_108`)


Der Verfassungsgerichtshof hat zu den Zuschüssen zum Kinderbetreuungsgeld in seinem  Erkenntnis vom 26.02.2009, G128/08 ua Folgendes ausgeführt:  12 von 24 Seite 13 von 24

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_135`)


Der Verfassungsgerichtshof vermag diese Bedenken im Ergebnis nicht zu teilen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_151`)


Dass die Ermittlung des maßgeblichen Jahresbetrags auf dieser Basis für die potentiell  anspruchsberechtigten Bezieher von KBG unmöglich oder in verfassungswidriger Weise  erschwert sei, kann der Verfassungsgerichtshof nicht finden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_166`)


Solche Umstände hat der Verfassungsgerichtshof in dem (auch von den antragstellenden  Gerichten zitierten) Erkenntnis VfSlg.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_169`)


Zu  diesem Ergebnis kam der Verfassungsgerichtshof aber vor allem deswegen, weil die damals zu  beurteilende Regelung eine volle, den Betrag der eigenen Einkünfte (unter Umständen weit)  übersteigende Rückzahlungsverpflichtung beinhaltete.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_177`)


In einem anderen vor dem  Verfassungsgerichtshof zu § 18 Abs. 1 Z 1 KBGG geführten  Verfahren hat der Verfassungsgerichtshof in seinem Erkenntnis vom 04.03.2011,  Zl. G184/10 in der Begründung die Stellungnahme der Bundesregierung wie folgt  wiedergegeben:  „3.4. ...

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_181`)


Der Verfassungsgerichtshof hat sich dazu wie folgt geäußert:  „2.3.2. ...

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_183`)


Der Verfassungsgerichtshof schließt sich dieser  Auffassung an.“

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_268`)


Im gegenständlichen Erkenntnis waren keine Rechtsfragen zu lösen, denen grundsätzliche  Bedeutung zukommt, weil der Gesetzgeber eine insoweit eindeutige Regelung getroffen hat  und die Rückforderung des Kinderbetreuungsgeldes und des Zuschusses zum  Kinderbetreuungsgeld durch die Gebietskrankenkasse im Fall eines unrechtmäßigen Bezuges  der angeführten Judikatur des Verfassungsgerichtshofes entspricht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_189`)


Beschwerdeführenden Parteien steht das Recht zu, innerhalb von sechs Wochen ab Zustellung  dieser Entscheidung eine Beschwerde an den Verfassungsgerichtshof, 1010 Wien, Freyung 8,  zu erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_190`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_191`)


Die  Beschwerde an den Verfassungsgerichtshof muss - abgesehen von den gesetzlich bestimmten  Ausnahmen - durch eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten  Rechtsanwalt eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_198`)


Das Antragsformular samt  Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch, postalisch oder  persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_199`)


Das Formular für postalische oder persönliche Einbringung  liegt in der Geschäftsstelle des Verfassungsgerichtshofes auf;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_200`)


es kann auch von der Website  des Verfassungsgerichtshofes (www.vfgh.gv.at; im Bereich Kompetenzen und Verfahren /  Verfahrenshilfe) heruntergeladen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_202`)


Zur Vorgangsweise für die elektronische Einbringung und zu  weiteren Informationen wird auf die Website des Verfassungsgerichtshofes verwiesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_23`)


Im Erkenntnis vom 11. Oktober 2001,  G 12/00, habe der Verfassungsgerichtshof die Verfassungsbestimmung des § 126a Bundesver- gabegesetz 1997 idF BGBl. I Nr. 125/2000 aufgehoben, "weil es dem einfachen Verfassungsge- setzgeber nicht gestattet ist, die Bundesverfassung auch nur für einen Teilbereich der Rechts- ordnung in ihrer Wirkung schlechthin zu suspendieren."

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_26`)


Außerdem sei nach ständiger Rechtsprechung des Verfassungsgerichtshofes (Hinweis auf VfGH  7.12.1988, B 1369/88) "einer Verfassungsbestimmung im Zweifel kein Inhalt beizumessen, der  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_34`)


§ 34 Abs. 7 Z 5 EStG 1988 verstoße somit gegen die verfassungsrechtliche Grundordnung und  sei daher zur Gänze verfassungswidrig, weshalb die Beantragung eines Gesetzesprüfungsver- fahrens beim Verfassungsgerichtshof durch das Bundesfinanzgericht angeregt werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_65`)


Dazu ist anzumerken, dass die Verfassungsnorm des § 34 Abs. 7 Z 5 EStG 1988  nach Auffassung des Verfassungsgerichtshofes nicht gegen Baugesetze der Verfassung verstößt  und dieser die Behandlung einer gegen diese Bestimmungen erhobenen Beschwerde abge- lehnt hat [vgl. VwGH 10.8.2005, 2004/13/0170 (zur gemeinsamen Entscheidung verbunden  mit 2005/13/0002, betreffend Familienbeihilfe), mit Verweis auf den im zugrundeliegenden  Beschwerdefall ergangenen Ablehnungsbeschluss des Verfassungsgerichtshofes vom 4. Okto- ber 2004,  B 634/04).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_66`)


Diese Rechtsansicht wurde auch vom Verwaltungsgerichtshof geteilt  und sah sich dieser daher nicht dazu veranlasst, die Überprüfung der Verfassungsvorschrift  des § 34 Abs. 7 Z 5 EStG 1988 auf ihre Übereinstimmung mit den Baugesetzen der österreichi- schen Bundesverfassung beim Verfassungsgerichtshof zu beantragen (vgl. VwGH 10.8.2005,  2004/13/0170; in diesem Sinne auch VwGH 28.11.2007, 2007/15/0187).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_67`)


Damit vermag aber  auch das Bundesfinanzgericht keine Veranlassung zu erkennen, beim Verfassungsgerichtshof  5 von 7 Seite 6 von 7

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_60`)


Gemäß Art. 135 Abs. 4 B-VG iVm Art. 89 B-VG steht die Prüfung der Gültigkeit gehörig  kundgemachter Gesetze den Verwaltungsgerichten nicht zu. Hat ein solches Gericht gegen die  Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so hat es den  Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_73`)


Der Verfassungsgerichtshof (VfGH) war schon mehrfach mit den verschieden Verlustausgleichs-  und -vortragsbeschränkungen im betrieblichen und außerbetrieblichen Bereich befasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_116`)


Über die  aufgeworfenen verfassungsrechtlichen Rechtsfragen besteht Judikatur des  Verfassungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_498`)


Etwaige unterschiedliche Ergebnisse erkannte der  Verfassungsgerichtshof jedoch nicht als unsachlich (VfGH 8.6.1985, B 488/80).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_44`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit  Erkenntnis vom 2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Mit 20.01.2021 wurde der amtliche Befund über eine Verkürzung von Stempel- oder  Rechtsgebühren vom Verfassungsgerichtshof dem Finanzamt Österreich, Dienststelle für  Sonderzuständigkeiten, zur Anzeige gebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_19`)


Nach der Bestimmung des § 17a VfGG ist für beim Verfassungsgerichtshof eingebrachte  Beschwerden spätestens im Zeitpunkt der Überreichung eine Gebühr in Höhe von € 240.- zu  entrichten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_24`)


Mit dem Einlangen der Beschwerde beim Verfassungsgerichtshof ist der gebührenpflichtige  Tatbestand im Sinne des § 17a VfGG erfüllt (vgl. VwGH 22.10.2015, 2013/16/0101;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_26`)


Wie der Verfassungsgerichtshof letztendlich mit der Beschwerde  verfährt, hat auf das Entstehen der Gebührenschuld keinen Einfluss.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_100`)


Diese Gesetzesfassung beruht auf dem Erkenntnis  des Verfassungsgerichtshofes vom 27.9.1984, G 111/84, worin dieser die Rechtsauffassung  vertreten hat, dass Nachforderungen an Umsatzsteuer auf Grund der Jahresveranlagung  zwangsläufig die Unrichtigkeit der Umsatzsteuervoranmeldung(en) für den  Veranlagungszeitraum implizieren.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/134379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134379.1_107`)


von Rechtsauslegungen des Verfassungsgerichtshofes oder des Verwaltungsgerichtshofes  abweicht, wenn im Vertrauen auf die betreffende Rechtsprechung für die Verwirklichung des  die Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_136`)


Es sah sich daher nicht veranlasst, einen Gesetzesprüfungsantrag an den  Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_141`)


Die vom Bf aufgeworfene Frage der Verfassungskonformität einer gesetzlichen Bestimmung  stellt keine Rechtsfrage im Sinne der Subsumtion unter einen gesetzlichen Tatbestand dar, die  vom Verwaltungsgerichtshofzu überprüfen ist, sondern ist deren Prüfung dem  Verfassungsgerichtshof vorbehalten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_21`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_79`)


X Dauerzustand  2. Beweiswürdigung  Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele (BFG 17.07.2019, RV/7105214/2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_80`)


Der Verwaltungsgerichtshof hat sich in seiner Rechtsprechung (sh. zB VwGH 18.11.2008,  2007/15/0019, und VwGH 18.12.2008, 2007/15/0151) der Rechtsansicht des  Verfassungsgerichtshofes angeschlossen;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/135431.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135431.1_99`)


Diese Gesetzesfassung beruht auf dem Erkenntnis  des Verfassungsgerichtshofes vom 27.9.1984, G 111/84, worin dieser die Rechtsauffassung  vertreten hat, dass Nachforderungen an Umsatzsteuer aufgrund der Jahresveranlagung  zwangsläufig die Unrichtigkeit der Umsatzsteuervoranmeldung(en) für den  Veranlagungszeitraum implizieren.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_38`)


Die Begründung, (nur)  diese beiden Gutachten als Beweismittel heranzuziehen, ist folgende:  Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_44`)


Der Verwaltungsgerichtshof hat sich in seiner Rechtsprechung (sh. zB VwGH 18.11.2008,  2007/15/0019, und VwGH 18.12.2008, 2007/15/0151) der Rechtsansicht des  Verfassungsgerichtshofes angeschlossen;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_137`)


Ad B, Urteile des Verfassungsgerichtshof welche die Anwendung des Nominalwertprinzips in  diesem Fall stützen sollen  Sie bringen die Urteile B 165/75 und B 193/77 des Verfassungsgerichtshofes auf, welche  aussagen sollen, dass das Nominalwertprinzip trotz der damit verbundenen Möglichkeit der  Besteuerung von Scheingewinnen verfassungskonform sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_188`)


Der Verfassungsgerichtshof (VfGH) hat mit Erkenntnissen vom 17. März 1976, B 165/75,  VfSlg 7770, zum EStG 1967, und vom 13.12.1982, B 193/77,G85/77, zum EStG 1972 die  Besteuerung des Einkommens nach dem Nominalwertprinzip trotz der damit verbundenen  Möglichkeit der Scheingewinnbesteuerung als mit der Verfassung im Einklang angesehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_202`)


Der Verfassungsgerichtshof geht vorläufig davon aus, dass es im rechtspolitischen  Gestaltungsspielraum des Gesetzgebers liegt, zu entscheiden, ob und inwieweit er die  Geldentwertung im Rahmen der Einkommensbesteuerung berücksichtigt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_89`)


Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele (BFG 17.07.2019, RV/7105214/2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_90`)


Der Verwaltungsgerichtshof hat sich in seiner Rechtsprechung (sh. zB VwGH 18.11.2008,  2007/15/0019, und VwGH 18.12.2008, 2007/15/0151) der Rechtsansicht des  Verfassungsgerichtshofes angeschlossen;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_59`)


Belehrung und Hinweise  Dem Antragsteller steht das Recht zu, innerhalb von sechs Wochen ab Zustellung dieser  Entscheidung eine Beschwerde an den Verfassungsgerichtshof (Freyung 8, 1010 Wien) zu  erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_60`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_61`)


Die Beschwerde  an den Verfassungsgerichtshof muss - abgesehen von den gesetzlichen Ausnahmen - durch  eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten Rechtsanwalt eingebracht  werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_66`)


Das  Antragsformular samt Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch,  postalisch oder persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_67`)


Das Formular für postalische oder persönliche  Einbringung liegt in der Geschäftsstelle des Verfassungsgerichtshofes auf;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_68`)


es kann auch von der  Website des Verfassungsgerichtshofes (www.vfgh.gv.at; im Bereich Kompetenzen und  Verfahren / Verfahrenshilfe) heruntergeladen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_70`)


Zur Vorgangsweise für die elektronische  Einbringung und zu weiteren Informationen wird auf die Website des Verfassungsgerichtshofes  verwiesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_76`)


Das zuständige Verwaltungsgericht ist gemäß § 5 WAOR das  Bundesfinanzgericht, wie auch der Verfassungsgerichtshof in seinem Erkenntnis vom  27.2.2015, Zahl G 139/2014 bestätigt hat.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_86`)


Den beiden Parteien wird hiermit die Möglichkeit eingeräumt, zu diesem Vorhalt bis 31. Mai  2022 eine Stellungnahme beim Bundesfinanzgericht einzubringen …  Dieser Vorhalt ist ein verfahrensleitender Beschluss, gegen den weder eine abgesonderte  Revision an den Verwaltungsgerichtshof noch eine abgesonderte Beschwerde an den  Verfassungsgerichtshof zulässig ist (§ 25a Abs 3 VwGG, § 88a Abs 3 VfGG).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/138877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138877.1_46`)


Die Behandlung einer gegen dieses  Erkenntnis eingebrachten Verfassungsgerichtshofbeschwerde wurde vom  Verfassungsgerichtshof abgelehnt, eine Revision wurde nicht erhoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_229`)


Gegen die Einschränkung der Beweisführung des Grades der Behinderung oder  der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu verschaffen, hat der  Verfassungsgerichtshof im Erkenntnis vom 10.12.2007, B 700/07, keine verfassungsrechtlichen  Bedenken gesehen (vgl. VwGH 22.12.2011, 2009/16/0307).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_72`)


2. darüber belehrt, dass ein Antrag auf Ausfertigung des Erkenntnisses gemäß § 29 Abs. 4  VwGVG eine Voraussetzung für die Zulässigkeit der Revision beim Verwaltungsgerichtshof und  der Beschwerde beim Verfassungsgerichtshof darstellt.   Eine Ausfertigung der Niederschrift wurde den in der Verhandlung anwesenden Parteien  ausgefolgt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_73`)


Binnen zwei Wochen nach Ausfolgung bzw. Zustellung der Niederschrift über die mündliche  Verhandlung wurde von keiner Partei ein Antrag auf schriftliche Ausfertigung des  Erkenntnisses gemäß § 29 Abs. 4 VwGVG gestellt. Wird auf die Revision beim  Verwaltungsgerichtshof und die Beschwerde beim Verfassungsgerichtshof von den Parteien  verzichtet oder nicht binnen zwei Wochen nach Ausfolgung bzw. Zustellung der Niederschrift  gemäß § 29 Abs. 2a VwGVG eine Ausfertigung des Erkenntnisses gemäß § 29 Abs. 4 VwGVG  von mindestens einem der hiezu Berechtigten beantragt, so kann gemäß § 29 Abs. 5 VwGVG  das Erkenntnis in gekürzter Form ausgefertigt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_115`)


Zur Unzulässigkeit der Revision und Hinweis  Da von den Parteien auf die Revision an den Verwaltungsgerichtshof und die Beschwerde an  den Verfassungsgerichtshof verzichtet wurde bzw. nicht binnen zwei Wochen nach Ausfolgung  bzw. Zustellung der Niederschrift gemäß § 29 Abs. 2a VwGVG eine Ausfertigung des  Erkenntnisses gemäß § 29 Abs. 4 VwGVG beantragt wurde, ist gemäß § 29 Abs. 5 VwGVG die  Erhebung einer Revision beim Verwaltungsgerichtshof oder einer Beschwerde beim  Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/139725.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139725.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/139762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139762.1_74`)


Mit Erkenntnis vom 30. November 2017, G 183/2017, hat der Verfassungsgerichtshof die Wort- folge „oder § 30a Abs. 1“ in § 20 Abs. 2 EStG 1988 idF BGBl. I Nr. 22/2012 als verfassungswidrig  aufgehoben und ausgesprochen, dass die Aufhebung mit Ablauf des 31. Dezember 2018 in  Kraft tritt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/139802.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139802.1_14`)


Diese Vorgehensweise wurde damit begründete, dass der Verfassungsgerichtshof mit  Erkenntnis vom 24. September 2018 (Zl. V 60/2018) die Wortfolge „ausgenommen jene nach §  1 Z 9 (Vertreter)“ in § 4 Abs. 1 der Verordnung über die Aufstellung von Durchschnittssätzen  für Werbungskosten, BGBl. II Nr. 382/2001 idF BGBl. II Nr. 382/2015, als gesetzwidrig  aufgehoben habe.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/140032.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140032.1_29`)


Obige Bestimmung des Progressionsvorbehaltes wurde vom Verfassungsgerichtshof geprüft  und als verfassungskonform beurteilt (vgl. VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/140065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140065.1_2`)


II. Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/140478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140478.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_9`)


Ich rege an, das Bundesfinanzgericht möge gemäß Art. 140 Abs. 1 Z. 1 lit. a B-VG beim  Verfassungsgerichtshof die Aufhebung der gegenständlichen Bestimmung (§ 41 Abs. 3 letzter  Satz EStG) beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_33`)


Ich hoffe,  meine weiteren Ausführungen veranlassen — zusammen mit dem bereits erwähnten Artikel  von Frau Prof. Kanduth-Kristen — das Gericht dazu, meine Zweifel an der  Verfassungsmäßigkeit der gegenständlichen Regelung zu teilen und wie angeregt deren  Aufhebung beim Verfassungsgerichtshof zu beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_59`)


Es besteht daher kein Grund für den Senat gemäß Art. 140 Abs. 1 Z. 1 lit. a B-VG beim  Verfassungsgerichtshof die Aufhebung des § 41 Abs. 3 letzter Satz EStG zu beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_63`)


Belehrung und Hinweise  Dem Antragsteller steht das Recht zu, innerhalb von sechs Wochen ab Zustellung dieser  Entscheidung eine Beschwerde an den Verfassungsgerichtshof (Freyung 8, 1010 Wien) zu  erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_64`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Verwaltungsgericht_Wien` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d66ddd58`  
**Description:**
Matches 'Verwaltungsgericht Wien' as a specific organization.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 10097 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_28`)


Mit Beschluss vom 15. Juni 2020 bewilligte das Verwaltungsgericht Wien die Verfahrenshilfe  für das gesamte Beschwerdeverfahren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_42`)


Der Magistrat der Stadt Wien, MBA 2/20 legte diese Beschwerde an das Verwaltungsgericht  Wien vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht  Wien` | `Verwaltungsgericht  Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_43`)


E) Das Verwaltungsgericht Wien beraumte zunächst eine mündliche Verhandlung über die  Beschwerde für den 17.11.2020 an, welche mit Schreiben des Verwaltungsgerichtes Wien vom  16.11.2020 wieder abberaumt wurde, und zwar mit folgender Begründung: „Der  gegenständliche Akt wird im Hinblick darauf, dass die Beschwerde sich gegen die Verweigerung  der Rückzahlung der pauschalierten Parkometerabgabe gemäß Wr. Parkometergesetz 2006  iVm der VO des Wiener Gemeinderates über die pauschale Entrichtung der Parkometerabgabe  (PauschaIierungsverordnung) richtet, gemäß § 6 AVG an das Bundesfinanzgericht  weitergeleitet und abgetreten.“  F) Die gegenständliche Beschwerde vom 8. Juli 2020 langte beim Bundesfinanzgericht ein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Missed by this rule (FN):**

- `Wiener Gemeinderates` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_10`)


Der Verfassungsgerichtshof bestätigte die Verfassungskonformität dieser  Zuständigkeitsübertragung vom (Landes)Verwaltungsgericht Wien auf das BFG durch  § 5 WAOR mit seinem Erkenntnis vom 27. Februar 2015 unter Zahl G 139/2014-10.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)
- `BFG` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_78`)


Im Vorlagebericht an  das Bundesfinanzgericht führte der Magistrat der Stadt Wien u.a. aus: „Es wird darauf  hingewiesen, dass gleichzeitig eine Beschwerde betreffend eine Übertretung der StVO (GZ:  MA67/andereZahl/2024) dem Verwaltungsgericht Wien vorgelegt wurde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/145527.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145527.1_51`)


Soweit sich die Beschwerde auf den Rückstand aus den  Verkehrsstrafen bezieht (€ 176,00), war die Beschwerde zuständigkeitshalber an das  Verwaltungsgericht Wien weiterzuleiten.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/146673.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146673.1_21`)


Mit E-Mail vom 9. Jänner 2025 hat die belangte Behörde mitgeteilt, dass der  Beschwerdeführer die Beschwerde vor dem Verwaltungsgericht Wien (E-Mail vom 23. Oktober  2024) zurückgezogen hat und dieses die Behörde darüber informiert hat.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

</details>

---

## `Ernst_Young_GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0e89155d`  
**Description:**
Matches 'Ernst & Young Steuerberatungsgesellschaft m.b.H.'

**Content:**
```
\bErnst\s*&\s*Young\s+Steuerberatungsgesellschaft\s+m\.b\.H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 10385 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Simon Zieselsberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Simon Zieselsberger` (person)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/138980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache OMedR DDr.in Griselda Bultink, vertreten durch Ernst & Young Steuerberatungsgesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 12. Juli 2021 gegen die  Bescheide des Finanzamtes Österreich vom 18. Jänner 2021 bzw. 21. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 bzw. 2019 zu Steuernummer  43-697/2735  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft  m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft  m.b.H.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `OMedR DDr.in Griselda Bultink` (person)
- `Finanzamtes Österreich` (organisation)
- `43-697/2735` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/147364.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ramon Launert  in der Beschwerdesache Romana Schnepf,  Hauptgraben 8, 7201 Neudörfl, Österreich, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer  Straße 19, 1220 Wien, über die Beschwerde vom 29. Dezember 2023 gegen die Bescheide des  Finanzamtes für Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr  2013 vom 15. November 2022, für die Jahre 2014 bis 2022 vom 27. September 2023, sowie die  Festsetzung der Sonderzahlung zur Stabilitätsabgabe gemäß § 201 BAO vom 4. Oktober 2023  bzw. über die Beschwerde vom 5. März 2024 gegen den Bescheid des Finanzamtes für  Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr 2023 vom 10.  Jänner 2024, jeweils zur Steuernummer 54-767/5279, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst & Young Steuerberatungsgesellschaft m.b.H.` | `Ernst & Young Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Ramon Launert` (person)
- `Romana Schnepf` (person)
- `Hauptgraben 8, 7201 Neudörfl, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `54-767/5279` (tax_number)

</details>

---

## `COFAG_Organization` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `19172f5a`  
**Description:**
Matches 'COFAG' as an organization, strictly excluding hyphenated suffixes like '-Beihilfen' or '-NoAG' which are not part of the organization name.

**Content:**
```
\bCOFAG\b(?!-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 5785 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/143488.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143488.1_28`)


Die erhebliche Härte sei nicht ganz vom Beschwerdeführer selbst verursacht, die Mitarbeiter  von COFAG und Finanzamt hätten auch eine wichtige Rolle gespielt. Er habe den Fehler  begangen, dass er den Richtlinien der COFAG blind vertraut habe und nicht erwartet habe, dass  die Bearbeitung des Fixkostenzuschussantrages so lange Zeit in Anspruch nehmen würden.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |
| `COFAG` | `COFAG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_42`)


Die Finanzierung der Lebenshaltungskosten sei im Hinblick darauf, dass die Personalkosten  verringert worden seien, und aufgrund der erhaltenen Förderungen aus dem Härtefallfond und  der COFAG - COVID-19 Finanzierungsagentur des Bundes GmbH möglich gewesen.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_55`)


Zu Tz. 1 des Berichtes über die Außenprüfung:  Die Förderung (FKZ 800T) sei als Einnahme 2021 verbucht worden, weil sie in diesem Jahr von  COFAG ausbezahlt wurden sei.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_129`)


Laut Punkt 2.3. des Anhanges zur Verordnung des Bundesministers für Finanzen gemäß § 3b  Abs. 3 des ABBAG-Gesetzes betreffend Richtlinien über die Gewährung von Zuschüssen zur  Deckung von Fixkosten durch die COVID-19 Finanzierungsagentur des Bundes GmbH (COFAG)  wurde Die COFAG vom Bundesminister für Finanzen beauftragt, Zuschüsse zur Deckung von  Fixkosten für Unternehmen zu gewähren, die durch die Ausbreitung von COVID-19 im Zeitraum  16. März 2020 bis 15. September 2020 Umsatzausfälle erleiden („Fixkostenzuschüsse“).

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |
| `COFAG` | `COFAG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_3`)


Entscheidungsgründe  1. Verfahrensgang und Parteienvorbringen  Mit Bescheid vom 14.11.2024 hat die belangte Behörde von der beschwerdeführenden Partei  (bfP) den von der COFAG geleisteten Fixkostenzuschuss I für den Zeitraum 16.3.2020 bis  15.6.2020 in Höhe von 34.685,34 € zurückgefordert.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_50`)


Folglich konnte kein berechtigtes Vertrauen in die Zinslosigkeit allfälliger Rückforderungen  durch die COFAG bestanden haben, in welchem die beschwerdeführende Partei durch die  Erlassung des COFAG-NoAG hätte enttäuscht werden können.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_53`)


Ob die COFAG die ihr zustehenden Zinsen bei ihren  Rückforderungen geltend machte oder nicht, spielt in diesem Zusammenhang keine Rolle.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_31`)


Wurde nach der Zahlung des  ersten Auszahlungsteilbetrages von der COVID-19 Finanzierungsagentur des Bundes  GmbH (COFAG) ein negativer Auszahlungsteilbetrag (§ 2 Abs. 6 COFAG-NoAG) oder ein  Betrag aus einer Rückforderung bzw. eine Saldierung auf null nach Verrechnung (§ 2  Abs. 7 COFAG-NoAG) bekannt gegeben, beginnt die Verzinsung mit dem Zeitpunkt  dieser Bekanntgabe.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_42`)


Der Sachverhalt wurde im Vorlagebericht (eine Ausfertigung davon wurde vom FA der Bf. zu  Handen ihrer steuerlichen Vertretung übermittelt) wie folgt dargestellt:  „Das Unternehmen gehört einem Unternehmensverband an und hat als  Beihilfenempfänger Obergrenzen überschreitende Förderungen der COFAG erhalten.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_47`)


Das Unternehmen ist der Ansicht, dass die Verzinsung laut COFAG NoAG  verfassungsrechtlich bedenklich ist.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_57`)


Erwägungen  Im gegenständlichen Fall wurde in der Beschwerde kein Antrag auf Unterlassung der  Beschwerdevorentscheidung gemäß § 262 Abs. 2 BAO gestellt.  Die belangte Behörde stützt die direkte Vorlage ausdrücklich auf § 262 Abs. 3 BAO und führte  dazu im Vorlagebericht aus, dass die Verzinsung laut COFAG NoAG nach Ansicht der Bf.  verfassungsrechtlich bedenklich sei.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

</details>

---

## `BHAG_Organization` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3120aa9c`  
**Description:**
Matches 'BHAG' (Bundesheer- und Heeresabgaben) as an organization.

**Content:**
```
\bBHAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1703 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_30`)


Im Fall mehrerer Auszahlungsteilbeträge ist gemäß § 16 Abs. 2 COFAG-NoAG jeder  Teilbetrag ab dem Zeitpunkt der jeweiligen Zahlungsanweisung der  Buchhaltungsagentur des Bundes (BHAG) zu verzinsen.

| Predicted | Gold |
|---|---|
| `BHAG` | `BHAG` |

</details>

---

## `technoRent_International_GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9a2f83b5`  
**Description:**
Matches the specific organization 'technoRent International GmbH'.

**Content:**
```
\btechnoRent\s+International\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 6287 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142803.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142803.1_83`)


Der EuGH hätte in seiner Entscheidung in der RS C-844/19 technoRent International GmbH klar  zum Ausdruck gebracht, dass der Grundsatz der steuerlichen Neutralität der Mehrwertsteuer -  auch wenn Art. 183 der Mehrwertsteuerrichtlinie weder eine Pflicht zur Zahlung von Zinsen auf  den zu erstattenden Vorsteuerüberschuss vorsieht noch angibt, ab wann solche Zinsen zu  zahlen wären - , es verlange, dass die finanziellen Verluste, die dadurch entstehen, dass ein  Vorsteuerüberschuss nicht innerhalb einer angemessenen Frist erstattet wird, durch die  Zahlung von Verzugszinsen ausgeglichen werden (Urteile vom 28. Februar 2018, Nidera, C- 387/16, EU:C:2018:121, Rn. 25, und vom 14. Mai 2020, Agrobet CZ, C-446/18, EU:C:2020:369,  Rn. 40).

| Predicted | Gold |
|---|---|
| `technoRent International GmbH` | `technoRent International GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142803.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142803.1_87`)


In technoRent International GmbH bringe der EuGH zudem eindeutig zum Ausdruck, dass nur  Vorsteuerüberschüsse zu verzinsen sind, nicht allerdings isoliert die in einer  Umsatzsteuervoranmeldung geltend gemachten und im Ergebnis mit Umsatzsteuerbeträgen   kompensierten Vorsteuerbeträge (Rz 47).

| Predicted | Gold |
|---|---|
| `technoRent International GmbH` | `technoRent International GmbH` |

</details>

---

## `Bundesministeriums_für_Finanzen` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `5c178ed5`  
**Description:**
Matches the full organization name 'Bundesministeriums für Finanzen' (genitive form).

**Content:**
```
\bBundesministeriums\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 16014 |

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

## `Landespolizeidirektion` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `7c29362c`  
**Description:**
Matches 'Landespolizeidirektion' and 'Landespolizeidirektion [Location]' (e.g., Wien).

**Content:**
```
\bLandespolizeidirektion(?:\s+(?:Nieder\u00f6sterreich|Wien))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 66 | 66 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 0 | 16823 |

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

**Missed by this rule (FN):**

- `BFG` (organisation)

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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_9`)


Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) lastete dem Beschwerdeführer  (Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüber- wachung der Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit  Strafverfügung vom 17. August 2020, Zahl, an, er habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 28. April 2020 in der gebührenpflichtigen Kurzparkzone  in 1030 Wien, Landstraßer Hauptstraße 136, ohne einem für den Beanstandungszeitpunkt  19:40 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig  verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_14`)


Mit Schreiben vom 2. September 2020 („Verständigung vom Ergebnis der Beweisaufnahme“)  wurde der Bf. von der MA 67 in Kenntnis gesetzt, dass sich aus der Organstrafverfügung sowie  zwei Fotos, welche von einem Organ der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung ausgestellt worden sei, ergebe, dass das näher bezeichnete Fahr- zeug am 28. April 2020 um 19:40 Uhr in Wien 3, Landstraßer Hauptstraße 136, in einer ge- bührenpflichtigen Kurzparkzone ohne einem für den Beanstandungszeitpunkt gültigen Park- schein abgestellt gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten eines Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 8. März 2021 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 8. Jänner 2021 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Rustenschacherallee 44-56, ohne einen für  den Beanstandungszeitpunkt 10:18 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_8`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Dem Ansuchen des Sohnes der Bf. um Aufnahme als Vertragsbediensteter bei der  Landespolizeidirektion Wien wurde stattgegeben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_9`)


Ab 1. September 2019 stand er in einem Dienstverhältnis zur polizeilichen Grundausbildung  mit der Landespolizeidirektion Wien und versah gemäß Bestätigung vom 12. September 2019  die polizeiliche Grundausbildung im Bildungszentrum der Sicherheitsakademie Wien, 1030  Wien (vorgelegte Ausbildungsbestätigung vom 12.09.2019).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_10`)


Der Sondervertrag gemäß § 36 VBG 1948 für die exekutivdienstliche Ausbildung vom  01. September 2019 beinhaltet, auszugsweise wiedergegeben, Folgendes:  1. Organisationseinheit, die für den Bund abschließt: Landespolizeidirektion Wien  2. Vor- und Familiennamen: (Sohn der Bf.)  3. Geburtsdatum: (Sohn der Bf.)  4. Beginn des Vertrages: 01. September 2019  5. Befristung: Dieser Dienstvertrag ist auf 24 Monate befristet  7. Beschäftigungsart: VB des Bundes mit Sondervertrag für die exekutivdienstliche Ausbildung  8.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_25`)


Betreffend das Jahr 2019 meldete die Landespolizeidirektion Wien dem Finanzamt gemäß § 84  Abs. 1 EStG 1988 Bezüge für den Zeitraum 01.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_11`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) wurde am 15.  Oktober 2020 um 09:41 Uhr in der gebührenpflichtigen Kurzparkzone in 1040 Wien, Rechte  Wienzeile gegenüber 25-27, von einem Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien zur Anzeige gebracht, da zum Beanstandungszeitpunkt ein  gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach eingeholter Lenkerauskunft mit Strafverfügung vom 19.  März 2021 an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen  Vienna am 17. Dezember 2020 in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Brehmstraße 16, ohne einen für den Beanstandungszeitpunkt 11:23 Uhr gültigen Parkschein  abgestellt, da sich im Fahrzeug der Parkschein Nr. 123 (Fünfzehn-Minuten-Parkschein) mit den  Entwertungen 10:40 Uhr befand und die Parkzeitzeit somit überschritten worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_28`)


Die Organstrafverfügung des  Parkraumüberwachungsorganes der Landespolizeidirektion Wien, welche auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt worden sei, sei als taugliches Beweismittel  anzusehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_13`)


Mag. Dr. Wieland Reinecke (Beschwerdeführer, kurz: Bf.) wurde von Kontrollorganen der  Parkraumüberwachung der Landespolizeidirektion Wien in der gebührenpflichtigen  Kurzparkzone in 1030 Wien, Marokannergasse 18,   1. am 1. Dezember P20 um 15:45 Uhr (Z1 und  2. am 3. Dezember 2020 um 15:11 Uhr (Z2  3. am 7. Dezember 2020 um 12:32 Uhr (Z3),  4. am 9. Dezember 2020 um 20:04 Uhr (Z4)  beanstandet, da es ohne einen für den jeweiligen Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Wieland Reinecke` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_9`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 1. Juli 2021  in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Windmühlgasse 7, beanstandet, da es  ohne einen für den Beanstandungszeitpunkt 20:02 Uhr gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_46`)


Beweiswürdigung:  Aus den eigenen Wahrnehmungen des Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien sowie durch die auf dem Überprüfungsgerät (Personal Digital  Assistant) erfassten Anzeigedaten und den zur Beanstandungszeit angefertigten Fotos sowie  der Überprüfung m-parking ergibt sich, dass zur Beanstandungszeit weder ein gültiger  Papierparkschein im Fahrzeug hinter der Windschutzscheibe hinterlegt noch ein gültiger  elektronischer Parkschein aktiviert war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_70`)


Aktenkundig - und in der vorgenannten Beweiswürdigung der belangten Behörde unbeachtet  gelassen - ist jedoch eine Korrespondenz der belangten Behörde mit der Landespolizeidirektion  Wien vom 7. August 2021, wonach der Bf. gegenständliches Fahrzeug ‚kurz‘ von der  Zulassungsbesitzerin geborgt gehabt habe, da sein eigenes Fahrzeug in der Werkstätte war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_73`)


Da die Korrespondenz mit 7. August 2021 datiert war, kann davon ausgegangen werden, dass  die Wahrnehmung von gegenständlichem Fahrzeug durch die Landespolizeidirektion Wien  allenfalls zwei bis drei Tage vor dem 7. August 2021 eingetreten ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_89`)


Da im vorliegenden Fall die strafbaren Handlungen im Zeitraum vom 16. Februar 2021 bis  21. Juli 2021 begangen wurden und gemäß vorgenannter Korrespondenz der belangten  Behörde mit der Landespolizeidirektion Wien vom 7. August 2021 der Bf. (nach seinen eigenen  Angaben) gegenständliches Fahrzeug vor dem 7. August 2021 nur ‚kurz‘ von der  Zulassungsbesitzerin geborgt gehabt hatte, kann in freier Beweiswürdigung nach § 45 Abs. 2  AVG nicht davon ausgegangen werden, dass die Lenkereigenschaft des Bf. in den  beschwerdegegenständlichen Fällen als erwiesen anzunehmen ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/136598.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136598.1_8`)


Parkraumüberwachung der Landespolizeidirektion Wien am 12. Oktober 2021 um 12:25 Uhr in  der gebührenpflichtigen Kurzparkzone in 1100 Wien, Columbusgasse ggü 101, beanstandet, da  zur Beanstandungszeit kein gültiger Parkschein vorlag.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/136998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136998.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 24. Jänner 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. November 2021  in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Wollzeile 3 ggü, abgestellt, ohne für  seine Kennzeichnung mit einem für den Beanstandungszeitpunkt 19:15 Uhr gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_8`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde vom  Kontrollorgan Zahl2 der Parkraumüberwachung der Landespolizeidirektion Wien am  27. Oktober 2021 um 16:55 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Am  Hauptbahnhof ggü 2, beanstandet, da es sich nach dessen eigenen Wahrnehmungen bei dem  Parkausweis gemäß § 29b StVO 1960 mit der Nr. Zahl3 um eine Farbkopie handelte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_27`)


Begründend stellte die Behörde unter Anführung der erhobenen Beweise (Einsichtnahme in  die Anzeige des Parkraumüberwachungsorgans der Landespolizeidirektion Wien, zur  Beanstandungszeit angefertigte Fotos, eingeholte Lenkerauskunft, Zusatznotiz vom  Meldungsleger) fest, auf Grund der eingeholten Lenkerauskunft sei ihre Tätereigenschaft  festgestellt worden und sei davon auszugehen, dass sie die Verwaltungsübertretung begangen  habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_10`)


Begründend führte die belangte Behörde aus:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien erstattet wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug an der im Spruch bezeichneten  Örtlichkeit zur angeführten Zeit im Bereich einer gebührenpflichtigen Kurzparkzone abgestellt  war, ohne dass die Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/138030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138030.1_12`)


Beweis sei durch Einsichtnahme in die Organstrafverfügung erhoben worden, welche von  einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung gelegt worden sei, sowie in die (von diesem) angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/138705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138705.1_8`)


Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde mit Bericht  vom 26. September 2022 dem Bundesfinanzgericht als zuständiges Verwaltungsgericht  vorgelegten Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Dienstnummer X  stellte am (Montag) 20. Juni 2022 um 12:54 Uhr fest, dass das mehrspurige Kraftfahrzeug mit  dem behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1230  Wien, Haeckelstraße 4, abgestellt war und dass dieses Kraftfahrzeug nicht mit einem für diesen  Beanstandungszeitpunkt gültigen Parkschein gekennzeichnet war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/138859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138859.1_3`)


Begründung  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenkerauskunft mit  Strafverfügung vom 22. November 2021 an, er habe das Fahrzeug am 26. August 1959  in der  gebührenpflichtigen Kurzparkzone in 1160 Wien, Panikengasse 1, ohne einen für den Bean- standungszeitpunkt 10:00 Uhr gültigen Parkschein abgestellt und demnach die Parkometer- abgabe verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `26. August 1959` (date)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/138859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138859.1_7`)


„Aus der Anzeige des Organs der Landespolizeidirektion Wien ergibt sich, dass das gegenständ- liche Kraftfahrzeug am 26. August 1959  um 10:00 Uhr in 1160 Wien, Panikengasse 1 in der  gebührenpflichtigen Kurzparkzone gestanden ist, wobei kein gültiger Parkschein entwertet,  bzw. kein elektronischer gültiger Parkschein aktiviert war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `26. August 1959` (date)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien am 3. Jänner 2022 um 09:32  Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Am Platz, beanstandet, da zur  Beanstandungszeit ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/139274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139274.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 25. Juli 2022 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 15. Juli 2022 in der  gebührenpflichtigen Kurzparkzone in 1220 Wien, Polgarstraße 3 und 5 ggü, ohne einen für die  Beanstandungszeit 16:12 Uhr gültigen Parkschein abgestellt, da der Parkschein Nr. PS1 und PS2  Spuren von entfernten Entwertungen aufgewiesen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/139288.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139288.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin (A. GmbH)  eingeholten Lenkerauskunft mit Strafverfügung vom 15. September 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 1. Juli 2022 in der  gebührenpflichtigen Kurzparkzone in Am Metzgerfeld 43, 3972 Weikertschlag, Österreich, ohne einen für den  Beanstandungszeitpunkt 17:53 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Am Metzgerfeld 43, 3972 Weikertschlag, Österreich` (address)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/139689.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139689.1_9`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 24. August  2022 in der gebührenpflichtigen Kurzparkzone in 1030 Wien, Wassergasse 14, beanstandet, da  zur Beanstandungszeit 15:16 Uhr ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/139974.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139974.1_8`)


der Landespolizeidirektion Wien mit Strafverfügung vom 25. Mai 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 25. März 2022 um  18:05 Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Pacassistraße 1, ohne einen  für den Beanstandungszeitpunkt 18:05 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/140104.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140104.1_4`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna war zur  Beanstandungszeit durch das Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien (22. September 2021, 12:28 Uhr) auf die Fa. XY e.U., Inhaber  ZulBes, zugelassen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_10`)


Entscheidungsgründe  Das bisherige Verfahren stellt sich wie folgt dar:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 1. August 2022  um 18:57 Uhr zur Anzeige gebracht, weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/140597.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140597.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 15. Dezember 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 18. Oktober 2022 in  der gebührenpflichtigen Kurzparkzone in 1020 Wien, Hafenzufahrtsstraße nächst ONr. 60,  ohne einen für den Beanstandungszeitpunkt 12:06 Uhr gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/140707.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140707.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 24. Jänner 2023 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. November 2022  in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Römergasse 79, ohne einen für den  Beanstandungszeitpunkt 20:46 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/140939.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140939.1_8`)


vom Kontrollorgan der Parkraumüberwachung Nr. A1294 der Landespolizeidirektion Wien zur  Anzeige gebracht, da der zum Beanstandungszeitpunkt hinterlegte 60-Minuten- Gebührenparkschein mit der Nummer PSNr unrichtig entwertet war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/141691.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141691.1_6`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 31. August  2022 um 16:15 Uhr in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Neuwaldegger  Straße 57A, zur Anzeige gebracht, da der im Fahrzeug hinter der Windschutzscheibe  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/141996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141996.1_8`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde am 27. April  2023 um 12:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Makartgasse 2,  vom Kontrollorgan der Parkraumüberwachung DNr der Landespolizeidirektion Wien zur  Anzeige gebracht, da zum Beanstandungszeitpunkt ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 19. Mai 2023 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 22. März 2023 in der  gebührenpflichtigen Kurzparkzone in 1010 Wien, Eßlinggasse 5 ggü, ohne einen für den  Beanstandungszeitpunkt 12:29 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_14`)


„Aus der Organstrafverfügung ergibt sich, dass das Fahrzeug mit dem behördlichen  Kennzeichen Vienna am 22.03.2023 um 12:29 Uhr von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien in einer gebührenpflichtigen Kurzparkzone in Wien 1., Eßlinggasse  gegenüber 5 ohne gültigen Parkschein abgestellt wahrgenommen wurde.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/142156.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142156.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 6. Juli 2023 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 9. Mai 2023 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Platz, ohne einen für den  Beanstandungszeitpunkt 19:41 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/143180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143180.1_10`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde am  7. September 2023 um 18:05 Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien,  Ebenfeldgasse, vom Kontrollorgan der Parkraumüberwachung ADNr der  Landespolizeidirektion Wien zur Anzeige gebracht, weil es sich nach dessen eigenen  Wahrnehmungen bei dem im Fahrzeug hinterlegten Parkausweis gemäß § 29b StVO 1960 mit  der Nr. Nr um einen seit tt.mm.2021 abgelaufenen und manipulierten Parknachweis handelte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Ebenfeldgasse` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/143904.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143904.1_8`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 27. Dezember 2023 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 18. Dezember 2023  in der gebührenpflichtigen Kurzparkzone in 1220 Wien, Bernoullistraße nächst ONr. 6, ohne  einen für den Beanstandungszeitpunkt 14:45 Uhr gültigen Parkschein abgestellt, da der  Parkschein Nr. 123 Spuren von entfernten Entwertungen aufgewiesen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/144091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144091.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer beim Zulassungsbesitzer des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenkerauskunft mit  Strafverfügung vom 3. Jänner 2024 an, sie habe das Fahrzeug am 28. September 2023 in der  gebührenpflichtigen Kurzparkzone in 1230 Wien, Perfektastraße 49, ohne einen für den  Beanstandungszeitpunkt 11:22 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_7`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am  1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_19`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung samt Fotos, welche  von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt wurde.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_27`)


Demnach ist es für die Behörde laut vorangegangener Erläuterung nicht relevant, ob das  zuständige Parkraumüberwachungsorgan der Landespolizeidirektion Wien eine handschriftliche  Signatur beifügt, da die automatische Anfügung der Dienstnummer des Organs als ausreichend  zu betrachten ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/145249.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145249.1_12`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung ausgestellt wurde, geht hervor, dass das gegenständliche  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit zur angeführten Zeit im  Bereich einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist, da sich im Fahrzeug lediglich die ungültigen  Parkscheine nach altem Tarif Nr. PS1 und PS2 befanden.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_12`)


Das Straferkenntnis wurde folgendermaßen begründet:  „Aus der dem Verfahren zugrundeliegende Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung erstattet wurde, geht hervor, dass das von Ihnen gelenkte  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit zur angeführten Zeit im  Bereich einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_70`)


Beweiswürdigung:  Die Abstellung des Fahrzeuges in der (jeweils) gebührenpflichtigen Kurzparkzone ohne (jeweils)  gültigen Parkschein lässt sich aus den drei Anzeigen der drei Kontrollorgane der  Parkraumüberwachung der Landespolizeidirektion Wien und den im Akt aufliegenden, zu den  Beanstandungszeitpunkten aufgenommenen Fotos ersehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_8`)


Entscheidungsgründe  Verfahrensgang:    Das Abstellen des auf den Beschwerdeführer zugelassenen mehrspurigen Kraftfahrzeuges mit  dem behördlichen Kennzeichen 123 (A) wurde von einem Kontrollorgan der  Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 01. August 2024 um 20:47  Uhr in 1140 Wien, Rettichgasse 4, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/148818.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/148971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148971.1_12`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, in die von diesem angefertigten Fotos, sowie in die  erteilte Lenker*innenauskunft.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_16`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener dienstlicher  Wahrnehmung gelegt wurde, in die von diesem angefertigten Fotos, sowie in die Bescheide des  Magistratischen Bezirksamtes für den 22.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/149088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149088.1_3`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 21.  August 2024 um 14:26 Uhr in 1010 Wien, Rathausstraße 6 beanstandet, da ein gültiger  Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug, mit dem behördlichen Kennzeichen W-Kennz. (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 04. April  2025 um 09:42 Uhr in der gebührenpflichtigen Kurzparkzone in 1210 Wien, nächst  Zaunscherbgasse ONr. 4 beanstandet, weil es zur Beanstandungszeit ohne gültigen Parkschein  bzw. gültiger Tagespauschalkarte abgestellt war, da die im Fahrzeug hinterlegte  Tagespauschalkarte Nr. TPK-Nr. Spuren von entfernten Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_28`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien aufgrund eigener dienstlicher  Wahrnehmung gelegt wurde, in die von diesem im Rahmen der Amtshandlung angefertigten  Fotos, sowie in die eingeholte Lenkerauskunft.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_53`)


Grundlage für das gegenständliche Verfahren ist die eigene dienstliche Wahrnehmung des  Parkraumüberwachungsorgans der Landespolizeidirektion Wien und die auf der Anzeige  festgehaltenen Angaben (entfernten Entwertungen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/149732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149732.1_7`)


der Landespolizeidirektion Wien mit Strafverfügung vom 31. Juli 2025, GZ. MA67/GZ/2025, an,  sie habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 2. Juni  2025 um 16:49 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Friesenplatz 7,  abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Reinhard_Stulik_GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `85ef252a`  
**Description:**
Matches the specific organization 'Reinhard Stulik Steuerberatungs GmbH & Co OG'.

**Content:**
```
\bReinhard\s+Stulik\s+Steuerberatungs\s+GmbH\s*&\s*Co\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 7440 |

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

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Alois Milter` (person)
- `Obere Marktwiese 11, 6458 Sölden, Österreich` (address)
- `75-325/5614` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Finanzamt Österreich` (organisation)

</details>

---

## `Heinz_Neuböck_GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9ca314b5`  
**Description:**
Matches the specific organization 'Heinz Neuböck Wirtschaftstreuhand Gesellschaft m.b.H.'.

**Content:**
```
\bHeinz\s+Neuböck\s+Wirtschaftstreuhand\s+Gesellschaft\s+m\.b\.H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 9318 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/138926.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138926.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Joachim Hinz, Faning 9, 4725 Edern, Österreich, vertreten durch Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H., Bauernmarkt 24, 1010 Wien, über die Beschwerde vom 22. Juli 2021 gegen den  Bescheid des Finanzamtes Österreich vom 19. Juni 2021 über die Festsetzung einer  Zwangsstrafe, Steuernummer 35-009/5338, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H.` | `Heinz Neuböck Wirtschaftstreuhand Gesellschaft  m.b.H.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Joachim Hinz` (person)
- `Faning 9, 4725 Edern, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `35-009/5338` (tax_number)

</details>

---

## `Amtes_für_Betrugsbekämpfung` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b91ce2e3`  
**Description:**
Matches 'Amtes für Betrugsbekämpfung' in any grammatical case (nominative, genitive, dative) to capture the specific organization.

**Content:**
```
\bAmtes\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 13835 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133409.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133409.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch R in der Finanzstrafsache gegen Priv.-Doz. Hagen Feldtenzer, Bakk. iur., Freidorf 14, 9912 Kobreil, Österreich,  über die Beschwerde des Bestraften vom 12.05.2021 gegen den Bescheid des Amtes für  Betrugsbekämpfung vom 27.04.2021, Strafkontonummer x, über die Abweisung eines  Zahlungserleichterungsansuchens zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Amtes für  Betrugsbekämpfung` | `Amtes für  Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hagen Feldtenzer, Bakk. iur.` (person)
- `Freidorf 14, 9912 Kobreil, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141359.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Torsten Aichler, Unternehmerzentrum 21, 4652 Frohnhofen, Österreich, vertreten durch Rechtsanwälte Estermann und  Partner OG, Stadtplatz 6, 5230 Mattighofen, über die Beschwerde vom 21. April 2022 gegen  den Bescheid des Amtes für Betrugsbekämpfung vom 1. April 2022 betreffend Antrag auf  Akteneinsicht in Sachen Torsten Aichler, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Torsten Aichler` (person)
- `Unternehmerzentrum 21, 4652 Frohnhofen, Österreich` (address)
- `Torsten Aichler` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142178.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142178.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Nancy Traxel, Kupferweg 6, 4263 Riemetschlag, Österreich, vertreten durch Rechtsanwälte Estermann &  Partner OG, Stadtplatz 6, 5230 Mattighofen, über die Beschwerde vom 22. Juni 2022 gegen  den Bescheid des Amtes für Betrugsbekämpfung vom 2. Juni 2022 betreffend Antrag auf  Auskunftserteilung in Sachen Nancy Traxel  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Nancy Traxel` (person)
- `Kupferweg 6, 4263 Riemetschlag, Österreich` (address)
- `Nancy Traxel` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_13`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr Senta Nettekoven  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Springholz, St.Nr. 91-867/0872  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Senta Nettekoven` (person)
- `Finanzamts Österreich` (organisation)
- `Springholz` (organisation)
- `91-867/0872` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/149395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Stockerl  in der Finanzstrafsache des  Univ.-Prof.in Esra Schäler, Starfach-Sandleitenweg 9H, 2552 Enzesfeld-Lindabrunn, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Edwin Stockerl` (person)
- `Univ.-Prof.in Esra Schäler` (person)
- `Starfach-Sandleitenweg 9H, 2552 Enzesfeld-Lindabrunn, Österreich` (address)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/149395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149395.1_6`)


Entscheidungsgründe  Verfahrensgang:  Mit Erkenntnis des Spruchsenates I-1 als Organ des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 2. Mai 2024 wurde der Beschwerdeführer (in der Folge kurz: Bf.) der  Finanzvergehen a) der Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG und b) der  Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG für schuldig erkannt.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

## `Wiener_Linien` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ef7d510e`  
**Description:**
Matches 'Wiener Linien' as a specific organization.

**Content:**
```
\bWiener\s+Linien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 16870 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_31`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. ist eine Philologin, Inhaberin einer Jahreskarte der Wiener Linien, wohnhaft in einer  60m²-Wohnung in Wien, von der die Bf. 14m² dazu bestimmt hat, dort Lernmaterial für den  Unterricht durchschnittlich täglich ca. zwei Stunden lang vorzubereiten;

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_68`)


Der Antrag auf Anerkennung von Fahrtkosten in Höhe von 50% der Kosten für die Jahreskarte  der Wiener Linien als Werbungskosten war abzuweisen, weil die Kosten für den Erwerb einer  7 von 15 Seite 8 von 15

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/144874.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144874.1_42`)


Die Ausführungen zu den Fahrzeiten mit öffentlichen Verkehrsmitteln vom Hauptwohnsitz des  Bf zur Arbeitsstätte ergeben sich aus der Abfrage des Pendlerrechners, Einsicht in Landkarten  und Fahrplanabfragen der Wiener Linien.

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/145249.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145249.1_119`)


Im Übrigen ist darauf zu  verweisen, dass die Parkscheine auch bei anderen Verkaufsstellen (bspw Ticketautomaten der  Wiener Linien, Tankstellen etc) erworben werden können.

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

</details>

---

## `Wiener_Gemeindebezirk` 🏆

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `79abecc9`  
**Description:**
Matches 'Wiener Gemeindebezirk' as a specific organization.

**Content:**
```
\bWiener\s+Gemeindebezirk(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.003 | 24 | 24 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 24 | 0 | 16859 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_52`)


Wiener Gemeindebezirkes.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirkes` | `Wiener Gemeindebezirkes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_49`)


Wiener Gemeindebezirk zur GZ P20 vom 11.12.2020  eindeutig hervorgehe, dass der neue Parkkleber erst ab 11. Dezember 2020 Gültigkeit erlangt  habe.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_99`)


Wiener Gemeindebezirk flächendeckend kundgemachten Kurz- parkzone für das Kraftfahrzeug mit dem Kennzeichen Vienna in der Zeit vom 17.12.2019 bis  30.11.2020.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_101`)


Wiener Gemeindebezirk in der Zeit vom 11.12.2020 bis  30.11.2022 gewährt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/139974.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139974.1_55`)


Über die Beschwerde wurde erwogen:  Feststellungen:  Der Bf. hat das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am  Freitag, den 25. März 2022, in der gebührenpflichtigen Kurzparkzone in 1130 Wien,  Pacassistraße 1, abgestellt.  In der Pacassistraße (13. Wiener Gemeindebezirk) besteht seit 1. März 2022 von Montag bis  Freitag (werktags) von 9 bis 22 Uhr Gebührenpflicht (Parkdauer: 2 Stunden).

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/139974.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139974.1_79`)


Eine Kurzparkzone muss sich nicht nur auf das Gebiet eines Wiener Gemeindebezirkes  beschränken, sondern darf sich auch darüber hinaus erstrecken und mehrere Bezirke umfassen  (vgl zB VwGH 04.08.2005, 2005/17/0056).

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirkes` | `Wiener Gemeindebezirkes` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_35`)


Wiener Gemeindebezirk zur GZ. 1713028-2022 vom 2. August 2022 für das in Rede stehende  Kraftfahrzeug eine Ausnahme von der im 4. und 5.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_36`)


Wiener Gemeindebezirk geltenden Park- zeitbeschränkung (Parkkleber-RFID-Chip) in der Zeit von 2. August 2022 bis 31. Juli 2023 erteilt  und gleichzeitig die Parkometerabgabe pauschal entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_76`)


Wiener Gemeindebezirk  flächendeckend kundgemachten Kurzparkzone für das in Rede stehende Kraftfahrzeug war  bzw. ist in der Zeit vom 1. August 2020 bis 31. Juli 2022 (Bescheid vom 12. Juni 2020) bzw. vom  2. August 2022 bis 31. Juli 2023 (Bescheid vom 2. August 2022) gültig.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_79`)


Wiener Gemeindebezirk flächendeckend kundge- machten Kurzparkzone für das in Rede stehende Fahrzeug in der Zeit vom 2. August 2022 bis  31. Juli 2023 und dem Telefonat mit Herrn X./MBA 4./5.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_98`)


Wiener  Gemeindebezirk flächendeckend kundgemachten Kurzparkzone für das in Rede stehende  Kraftfahrzeug in der Zeit vom 1. August 2020 bis 31. Juli 2022 erteilt.  Im Schreiben des Magistratischen Bezirksamtes für den 4. und 5. Bezirk vom 8. Juni 2022  (Serviceleistung für die Einzahlungsdaten für den Neuantrag des Parkpickerls), welches die Bf.  im Zuge ihres Antrages auf Verlängerung erhalten hat, wurde in grau hervorgehobenen Feldern  darauf hingewiesen, dass die Zahlungsreferenzen unbedingt vollständig angegeben werden  müssen.

| Predicted | Gold |
|---|---|
| `Wiener  Gemeindebezirk` | `Wiener  Gemeindebezirk` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_18`)


Wiener Gemeindebezirk geltenden  Parkzeitbeschänkung in der flächendeckend kundgemachten Kurzparkzone für das  2 von 12 Seite 3 von 12

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_54`)


Wiener Gemeindebezirk geltenden  Parkzeitbeschränkung in der flächendeckend kundgemachten Kurzparkzone für das  Kraftfahrzeug mit dem Kennzeichen 123 (A) unter den genannten Auflagen vom 1.1.2024 bis  31.12.2024 erteilt.  In dem Bescheid vom 2.1.2024 (Ausnahmebewilligung) war in der Rubrik  Zahlungsinformationen (Seite 20/20) in fett hervorgehobenen Buchstaben angeführt:  „Ihre Parkbewilligung wird nach Eingang Ihrer Zahlung freigeschalten (Dauer 2-4 Werktage).“

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_101`)


Wiener  Gemeindebezirk geltenden höchstzulässigen Parkdauer in der flächendeckend kundgemachten  Kurzparkzone von 1.1.2024 bis 31.12.2024 erteilt.   Die Überweisung der im Bescheid vom 2.1.2024 vorgeschriebenen Gebühren erfolgte am  15.1.2024.

| Predicted | Gold |
|---|---|
| `Wiener  Gemeindebezirk` | `Wiener  Gemeindebezirk` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_25`)


Wiener Gemeindebezirk  flächendeckend kundgemachten Kurzparkzone (Parkkleber) ausgestellt worden ist.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_62`)


Wiener Gemeindebezirk befindlichen,  gebührenpflichtigen Kurzparkzone Reisnerstraße gegenüber 61,  Verfahren 2) 08.05.2024 um 14:27 Uhr in der im 3.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_63`)


Wiener Gemeindebezirk befindlichen,  gebührenpflichtigen Kurzparkzone Reisnerstraße gegenüber 61 und   Verfahren 3) 07.05.2024 um 09:16 Uhr in der im 3.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_64`)


Wiener Gemeindebezirk befindlichen,  gebührenpflichtigen Kurzparkzone Reisnerstraße gegenüber 59, ohne Kennzeichnung mit  einem für den (jeweiligen) Beanstandungszeitpunkt gültigen Parkschein beanstandet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_68`)


Wiener Gemeindebezirk für  den Zeitraum 09.05.2023 bis 30.04.2025 ausgestellt worden ist.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_72`)


Wiener Gemeindebezirk in  7 von 12 Seite 8 von 12

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_75`)


Wiener Gemeindebezirk in der  Kurzparkzone geltenden Parkzeitbeschränkung erteilt worden wäre, wurde nicht einmal von  der Bf. behauptet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/147746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147746.1_86`)


Wiener Gemeindebezirk  für das Fahrzeug mit dem Kennzeichen Kennz2(A) erteilt wurde, ist zu entnehmen, dass im Fall  einer kurzfristigen Verhinderung der Benutzung dieses Fahrzeuges ein "Ersatzfahrzeug"  verwendet werden könnte.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_90`)


Wiener Gemeindebezirk umfasste.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_33`)


Wiener Gemeindebezirk in der Kurzparkzone geltenden Parkzeitbeschränkung in der Zeit von  05.03.2025 bis 28.02.2027 erteilt und wurde gleichzeitig die Parkometerabgabe pauschal  entrichtet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeindebezirk` | `Wiener Gemeindebezirk` |

</details>

---

## `Bundesamtes_für_Soziales` 🏆

**F1:** 0.014 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `5d27bb34`  
**Description:**
Matches 'Bundesamtes für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative).

**Content:**
```
\bBundesamt(?:es)?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.014 | 131 | 131 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 131 | 0 | 17859 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_32`)


Mit der Bescheinigung des Bundesamtes für Soziales und Behindertenwesen aus dem Jahr 2004 wurde dem Beihilfenwerber bestätigt, dass er voraussichtlich dauernd außer Stande sei, sich selbst den Unterhalt zu verschaffen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_45`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen (§ 8 Abs 6 FLAG 1967).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_48`)


Die Auszahlung der Familienbeihilfe und des Erhöhungsbetrages hätte somit nicht erfolgen dürfen bzw hätte es einer weiteren Auseinandersetzung mit den Umständen des Einzelfalles und einer allfälligen Ergänzung der Bescheinigung des Bundesamtes für Soziales und Behindertenwesen bedurft, welche nach dem Inhalt des vorgelegten Verwaltungsaktes offensichtlich nicht stattgefunden hat.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_44`)


ii. Schriftsatz 24. Februar 2020  Nach telefonischer Nachfrage durch den Richter ergänzte die Bf. ihre Angaben am 24. Februar  2020 noch einmal und legte den Bescheid des Bundesamtes für Soziales und  Behindertenwesen (Sozialministeriumsservice) vom 22. September 2015 (Behinderungsgrad  50%) mit dem zugehörigen Sachverständigengutachten vom 16. September 2015 vor.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_126`)


Hier ist das das Bundesamt für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_26`)


Der Grad  der Behinderung sei durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens festzustellen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_92`)


Zufolge den Bestimmungen des § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die  voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine  Bescheinigung des Sozialministeriumservice (Bundesamtes für Soziales und  Behindertenwesen) auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen  (vgl. VwGH 20.09.1995, 95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006,  2003/13/0123, VwGH 30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_97`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  8 von 10 Seite 9 von 10

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_9`)


Der Grad der Behinderung oder die voraussichtlich dauernde Erwerbsunfähigkeit ist durch eine  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_11`)


fünf Jahre ab der  Antragstellung möglich bzw. ab dem Monat, ab dem das Bundesamt für Soziales und  Behindertenwesen den Grad der Behinderung festgestellt hat (§ 10  Familienlastenausgleichsgesetz 1967 in der geltenden Fassung).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_23`)


Auf Grund der Untersuchung der Bf. durch einen Facharzt für Neurologie wurde das  Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen vom  3. Dezember 2019 wie folgt erstellt:   Anamnese:   Die AW kommt in Begleitung im Rollstuhl.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_56`)


Der Grad der Behinderung oder die voraussichtlich dauernde Erwerbsunfähigkeit ist nach der  geltenden Rechtslage § 8 Abs. 6 des Familienlastenausgleichsgesetzes 1967 in der Fassung  BGBl Nr. 105/2002 durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_89`)


Nach § 8 Abs. 6 FLAG 1967 ist die dauernde Unfähigkeit sich selbst den Unterhalt zu  verschaffen anhand einer Bescheinigung des Bundesamtes für Soziales und Behindertenwesen  (zwischenzeitig in Sozialministeriumsservice [=SMS] umbenannt) auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_131`)


Der  ärztliche Dienst des zuständigen Bundesamtes für Soziales und Behindertenwesen hat sich  dieser Einschätzung angeschlossen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_138`)


Gemäß § 8 Abs. 6 FLAG ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_137`)


Der Grad der Behinderung oder die voraussichtlich dauernde Erwerbsunfähigkeit ist nach der  geltenden Rechtslage § 8 Abs. 6 des Familienlastenausgleichsgesetzes 1967 in der Fassung  BGBl Nr. 105/2002 durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_170`)


Mit Beschluss vom 24. Februar 2020 erteilte das Bundesfinanzgericht dem Finanzamt einen  Ermittlungsauftrag, sonach ein neuerliches Sachverständigengutachten beim Bundesamt für  Soziales und Behindertenwesen (SMS) einzuholen sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_339`)


• Bescheinigung des Sozialministeriumservice  Zufolge den Bestimmungen des § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die  voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine  Bescheinigung des Sozialministeriumservice (früher des Bundesamtes für Soziales und  Behindertenwesen) auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl.  VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH 30.05.2017, Ro  2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_385`)


• Bindung an die Gutachten des Sozialministeriumservice  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die  Gutachten des Sozialministeriumservice (früher: Bundesamt für Soziales und  Behindertenwesen) gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch Lenneis/Wanke (Hrsg.), FLAG, 2. Aufl.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_26`)


Am 02.11.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor, beantragte die Abweisung und nahm wie folgt Stellung:  „Das Finanzamt ist bei der Beurteilung des Sachverhalts gemäß § 8 Abs. 6 FLAG 1967 an die  vom Bundesamt für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens ausgestellten Bescheinigungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_60`)


§ 8 Abs. 6 FLAG 1967 lautet:  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_61`)


Rechtliche Würdigung  Der Nachweis der voraussichtlich dauernden Erwerbsunfähigkeit ist gemäß § 8 Abs. 6 FLAG  1967 (ausschließlich) durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens zu führen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_62`)


Bei der Antwort auf die Frage, ob das Kind erheblich behindert war bzw. ist oder dauernd  außerstande war bzw. ist, sich selbst den Unterhalt zu verschaffen, ist die Behörde bzw. das  Bundesfinanzgericht an die der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen zugrunde liegenden Gutachten grundsätzlich gebunden und darf diese nur  insoweit prüfen, ob sie schlüssig und vollständig und nicht einander widersprechend sind (vgl.  VwGH 29.09.2011, 2011/16/0063;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_41`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_29`)


Laut Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen (BASB  Landesstelle OÖ) über die Begutachtung am 22.1.2019, in dem ein Gesamtgrad der  Behinderung von 50 % bescheinigt wird, leidet der Beschwerdeführer an    (1) Posttraumatischer Sprunggelenksarthrose rechts bei Z.n. Sprungbeinfraktur,  beginnender Hüft- und Kniegelenksarthrose beidseits (Grad der Behinderung 40 %)   (2) Chronischer Lumbalgie bei degenerativer Wirbelsäulenerkrankung und Z.n.  Bandscheibenoperation L2/L3 (Grad der Behinderung 30 %)   (3) Koronarer Herzkrankheit, Angina pectoris Z.n. erfolgreicher Gefäßaufdehnung und  Stentimplantation (Grad der Behinderung 30 %).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `BASB  Landesstelle OÖ` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_73`)


Laut Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen  (BASB Landesstelle OÖ) ist ein solcher Zusammenhang nicht ersichtlich, sodass bei den geltend  gemachten Behandlungskosten ein Selbstbehalt zu berücksichtigen ist.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `BASB Landesstelle OÖ` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_16`)


Zur Begründung der Abweisung wurde ausgeführt, dass das Finanzamt für die Anerkennung  der beantragten Freibeträge auf die Mitteilungen des Sozialministeriumservice (ehemaliges  Bundesamt für Soziales und Behindertenwesen) angewiesen sei, aktuell für die Bf. jedoch keine  derartigen Mitteilungen vorlägen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_28`)


Die Tatsache der Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit sind durch  eine amtliche Bescheinigung durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_18`)


§ 8 Abs. 6 FLAG 1967 besagt, dass der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_44`)


Im Dezember 2020 und im März 2021 wurden vom Bundesamt für Soziales und  Behindertenwesen Sozialministeriumservice Sachverständigengutachten erstellt.  3 von 11 Seite 4 von 11

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_120`)


Abs. 6:  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/135301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135301.1_115`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_4`)


Mit Bescheid vom 20.03.2020 wies das FA die eingebrachten Familienbeihilfeanträge vom  22.01.2020, gestützt auf das für den Bf erhobene Sachverständigengutachten des  Bundesamtes für Soziales und Behindertenwesen vom 19.03.2020, unter Hinweis auf § 6 Abs. 2  lit. d FLAG 1967 für den Zeitraum ab Jänner 2020 mit folgender Begründung ab:  „Laut Gutachten des Sozialministeriumservice vom 19.3.2020 wurde ein Grad der Behinderung  mit 50% rückwirkend ab 1.6.1987 und 60% rückwirkend ab 1.1.2014 festgestellt. Eine dauernde  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_43`)


Am 15.10.2021 legte das FA das Sachverständigengutachten des Bundesamtes für Soziales und  Behindertenwesen vom 09.09.2021/10.09.2021 dem Bundesfinanzgericht vor.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_62`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist gemäß § 8 Abs 6 FLAG 1967 durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_101`)


Dem Bundesfinanzgericht liegen folgende ärztliche Sachverständigengutachten vor: ein  ärztliches Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen  vom 19.03.2020 erstellt von Frau Dr. Arzt, einer Fachärztin für Neurologie und Psychiatrie,  (hier: Erstgutachten) sowie – infolge der gegenständlichen Bescheidbeschwerde - eine  Gesamtbeurteilung nach der Einschätzverordnung des Bundesamtes für Soziales und  Behindertenwesen vom 28.12.2020 erstellt von Frau Dr. Arzt1, der ein psychiatrisches  Teilgutachten von Frau Dr. Arzt1 - sowie ein psychologisches Teilgutachten von Frau Dr. Arzt2  (beide Teilgutachten erstellt am 22.12.2020) zu Grunde liegt.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_102`)


Das letzte dem  Bundesfinanzgericht zur Verfügung stehende Sachverständigengutachten des Bundesamtes für  Soziales und Behindertenwesen stammt vom 09.09.2021/10.09.2021 und wurde wiederum  von Frau Dr. Arzt erstellt (hier: Letztgutachten).

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_168`)


Bei der Antwort auf die Frage, ob eine körperliche oder geistige Behinderung vor Vollendung  des 21 Lebensjahres eingetreten ist, die zur Unfähigkeit führt, sich selbst den Unterhalt zu  verschaffen, sind die Abgabenbehörden und das Bundesfinanzgericht an die der Bescheinigung  des Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden Gutachten  gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und vollständig sind und im  Falle mehrerer Gutachten nicht einander widersprechen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_16`)


§ 8 Abs 6 FLAG 1967 bestimmt zur Lösung der Frage, ob das Kind behindert oder  voraussichtlich dauernd unfähig ist, sich selbst den Unterhalt zu verschaffen, die  Nachweisführung ausschließlich durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen ( jetzt: Sozialministeriumservicestelle).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_24`)


3.1. Erwägungen  Nach § 8 Abs 6 FLAG ist der Nachweis des Grades der Behinderung durch eine Bescheinigung  des Bundesamtes für Soziales und Behindertenwesen (jetzt: Sozialministeriumservicestelle,  kurz: SMS) aufgrund eines ärztlichen Gutachtens zu erbringen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_38`)


Es besteht nach der Rechtsprechung beider Gerichtshöfe öffentlichen Rechts zu § 8 Abs 6 FLAG  1967 jedoch keine unbedingte Bindung an die Bescheinigungen des Bundesamtes für Soziales  und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales  und Behindertenwesen` | `Bundesamtes für Soziales  und Behindertenwesen` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_6`)


Im über Ersuchen der belangten Behörde und im Auftrag des Bundesamtes für Soziales und  Behindertenwesen (kurz: „Sozialministeriumservice“) erstellten ärztlichen  Sachverständigengutachten vom 06.02.2018 wurde unter Hinweis auf Anamnese, angeführter  vorgelegter Befunde und Untersuchungsbefund eine „Schizophrenie nach der Richtsatzposition  03.07.02 der Einschätzungsverordnung (BGBl. II Nr. 261/2010), GdB 70% seit 04/2015  festgestellt sowie eine dauernde Erwerbsunfähigkeit bescheinigt.“

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_22`)


Über Ersuchen der belangten Behörde und im Auftrag des Bundesamtes für Soziales und  Behindertenwesen wurde neuerlich ein ärztliches Sachverständigengutachten am 23.10.2018  erstellt. Die durchgeführte Begutachtung brachte folgendes Ergebnis:  Grad der Behinderung 70 % ab 04/2015, eine dauernde Erwerbsunfähigkeit liegt vor.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_37`)


2. Beweiswürdigung  Dieser als erwiesen angenommener Sachverhalt beruht auf den beiden im Wege des  Bundesamtes für Soziales und Behindertenwesen erstellten Gutachten.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_67`)


Nach § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_70`)


Wie unter Punkt 2 ausgeführt, besteht eine Bindung der Abgabenbehörden und auch des  Bundesfinanzgerichtes an die im Wege des Bundesamtes für Soziales und Behindertenwesen  nach § 8 Abs. 6 FLAG 1967 erstellten Gutachten, sofern diese schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_78`)


Sowohl VfGH als auch VwGH bejahen  eine Bindung an die im Wege des Bundesamtes für Soziales und Behindertenwesen erstellten  Gutachten.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_30`)


In der Folge erstellte das Bundesamt für Soziales und Behindertenwesen, BASB Landesstelle  NÖ das Sachverständigengutachten auf Grund der Aktenlage vom 4. Mai 2021 nach der  Einschätzungsverordnung (BGBl. II Nr. 261/2010) betreffend Z., den Sohn des Bf.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_61`)


Vom Bundesamt für Soziales und Behindertenwesen wurden im Laufe des  Verwaltungsverfahrens folgende Bescheinigungen erstellt:   BSB-Bescheinigung vom 29. Oktober 2020: Stellungnahme: Keine Unterlagen eingelangt;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_88`)


[Anm.: Geburtsdatum]   4.14 Termin der nächsten Kontrolle  [blank]   Das in der Folge erstellte Gutachten vom 4. Mai 2021 des Bundesamtes für Soziales und  Behindertenwesen, BASB Landesstelle NÖ trifft folgende Aussagen:   Sachverständigengutachten auf Grund der Aktenlage   nach der Einschätzungsverordnung (BGBl. II Nr. 261/2010)   Name: (Sohn des Bf.) … Geburtsdatum: …11.2005, wohnhaft in … Ungarn   Aktengutachten erstellt am: 04.05.2021   Name des Sachverständigen: Dr. G.H.   Fachgebiet: Allgemeinmedizin und Augenheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Formular E407, gezeichnet von Dr.B.E.T. in Papa (Ungarn) am 17.3.2021:   15 Jahre, 4 Monate   85 kg, 187 cm   vollständige Selbständigkeit, keine Hilfestellungen erforderlich   Sehbehinderung ab 11/2005   Behandlung ab 06/2006   keine anderen Behinderungen   TH: Implantat für künstliche Linsen 31.9.2006;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Dr. G.H.` (person)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_105`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_125`)


die voranstehenden Absätze: vollständige  Selbständigkeit des Kindes, keine Hilfestellung erforderlich) durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  10 von 12 Seite 11 von 12

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_4`)


Nach Erstellung eines Sachverständigengutachtens auf Grund der Aktenlage vom 12. April 2021  durch eine Fachärztin für Kinder- und Jugendheilkunde im Auftrag des Bundesamtes für  Soziales und Behindertenwesen, Landesstelle Wien, wies das Finanzamt mit dem  angefochtenen Bescheid vom 19. April 2021 den Antrag der Bf. auf den Erhöhungsbetrag zur  Familienbeihilfe für Ihren Sohn J… für den Zeitraum Februar 2016 bis September 2020 mit  folgender Begründung ab:   Anspruch auf den Erhöhungsbetrag wegen erheblicher Behinderung besteht, wenn:   • Der festgestellte Grad der Behinderung mindestens 50 Prozent beträgt   • Die Behinderung nicht nur vorübergehend ist, sondern mehr als 3 Jahre andauert   1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_23`)


Der Grad der Behinderung oder die voraussichtlich dauernde Erwerbsunfähigkeit ist durch eine  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_25`)


fünf Jahre ab der  Antragstellung möglich bzw. ab dem Monat, ab dem das Bundesamt für Soziales und  Behindertenwesen den Grad der Behinderung festgestellt hat (§ 10  Familienlastenausgleichsgesetz 1967 in der geltenden Fassung).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_57`)


Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Aktengutachten erstellt am 12. April 2021:   Fachgebiet der Sachverständigen: Kinder- und Jugendheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   2021-03-12 Amanda Guichard  Kinder-und Jugendpsychiatrie, Hinterbrühl, Kurzarztbrief nach Aufenthalt  in der kooperativen Tagesklinik vom 20.10.20 bis 29.01.2021, Diagnosen:   einfache Aktivitäts- und Aufmerksamkeitsstörung mit Förderbedürfnissen in der sozialen  Interaktion, Förderbedarf in Bezug auf sensorische Interaktion und die Motorikentwicklung  /fein und grob), logopädisch: phonetische Aussprachestörung in Form eines interdentalen  Sigmatismus sowie ein ad-/bzw. interdentales Schluckmuster, durchschnittliche Intelligenz,  keine chronischen oder akuten körperlichen Erkrankungen bekannt, mäßige soziale  Beeinträchtigung (Aufbau und Erhalt von Freundschaften, wiederholte Konflikte mit  Erwachsenen und Kindern, auch Konflikte mit Erwachsenen außerhalb der Familie, gehemmte  soziale Aktivität, wenig effektive Copingmechanismen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Amanda Guichard` (person)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_60`)


Nachuntersuchung:   NU in 3 Jahren zur Überprüfung der Beeinträchtigung   Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Sachverständigengutachten (mit Untersuchung am 23. August 2021),   vidiert am 27. August 2021:   Fachgebiet des Sachverständigen: Kinder- und Jugendheilkunde   Anamnese:   Die Eltern haben gegen den Bescheid schriftlich Einspruch erhoben, da die rückwirkende  Geltendmachung des GdB mit 10/2020 festgelegt wurde, die Eltern jedoch den Beginn der  Symptomatik dtl.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_82`)


Gemäß § 8 Abs. 6 FLAG 1967 in der Fassung BGBl. I Nr. 105/2002 ist der Grad der Behinderung  oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch  eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/137083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137083.1_33`)


– In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/137277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137277.1_69`)


§ 29b Abs. 1 StVO 1960 normiert:  "Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung ‚Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung‘  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/137507.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137507.1_43`)


vom Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_13`)


3. Auf Anforderung durch das Finanzamt wurde vom Sozialministeriumservice (kurz: SMS;  vormals Bundesamt für Soziales und Behindertenwesen) am 30.8.2018 ein Sachver- ständigengutachten (aufgrund der Aktenlage) von Adam Safak  Facharzt für  Psychiatrie/Allgemeinmediziner, vidiert von Dr. D am 4.9.2018, auszugsweise folgenden  Inhaltes erstellt:  "Zusammenfassung relevanter Befunde …:  14.9.2015: Reha-Befund Ort1: chronischer Kopfschmerz nach komplexer Gesichtsverletzung im  siebten Lebensjahr (vom Ausmaß her wohl auch SHT 1989)  7.3.2018: Entlassungsbericht aus der psychiatrischen Rehabilitation im Klinik1: Diagnose F07.9  organische Persönlichkeits- und Verhaltensstörung nach Schädelhirntrauma, bei Aufnahme  leicht depressiv, bei Entlassung noch Einschränkung der psychosozialen Belastbarkeit  Behandlung/en/Medikamente …:  Lyrica 50 mg … Mirtabene 30 mg … Seroquel 25 mg … bei Bedarf eine ärztliche  Weiterbetreuung bei … sowie eine Einzel-Psychotherapie wurden empfohlen  Ergebnis der durchgeführten Begutachtung:   1 Persönlichkeits- und Verhaltensstörungen … mit maßgeblichen sozialen     Beeinträchtigungen, organische Persönlichkeitsveränderung nach komplexem     Schädel-Hirntrauma vor vielen Jahren;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Adam Safak` (person)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_75`)


3. Der Grad der Behinderung (GdB) oder die voraussichtliche dauernde Unfähigkeit, sich selbst  den Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen (nunmehr Sozialministeriumservice/SMS) aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_208`)


Nach § 8 Abs. 6 FLAG ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (nunmehr Sozialministeriumservice) auf  Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_221`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_227`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der  Beweisführung  Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_5`)


Beigelegt waren dem Antrag  - ein Bescheid des Bundesamtes für Soziales und Behindertenwesen vom 1. Feber 2019, mit  welchem die Zugehörigkeit der Antragstellerin zum Kreis der begünstigten Behinderten ab  6. Dezember 2018 festgestellt wurde,  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_10`)


Das Finanzamt ersuchte das Bundesamt für Soziales und Behindertenwesen die Erstellung  eines ärztlichen Sachverständigengutachtens zu veranlassen und eine darauf basierende  Bescheinigung zu ers tellen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_11`)


Das Bundesamt für Soziales und Behindertenwesen b eauftragte  den gleichen Sachverständig en, der bereits im Jänner 2019 seine Expertise abge geben hat.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_13`)


Aus der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen ergibt sich, dass ein Grad der Behinderung von 50%, rückwirkend ab  Jänner 2019 und keine voraussichtlich dauernde Unfähigkeit, sich selbst der Unterhalt zu  verschaffen, vorliegen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_16`)


Unter Bezugnahme auf die  Bestimmung des § 2 Abs 1 lit c FLAG 1967 (zutreffend wäre § 6 Abs 2 lit d FLAG 1967) und die  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen führte das Finanzamt  begründend aus, die Antragstellerin wäre nicht dauernd erwerbsunfähig, es läge  Selbsterhaltungsfähigkeit vor.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_34`)


Auf Grund der Beschwerdeerhebung wurde vom Finanzamt neuerlich das Bundesamt für  Soziales und Behindertenwesen kontaktiert und diesem die Beschwerde samt Beilagen  übermittelt. Der leitende Arzt des Bundesamtes für Soziales und Behindertenwesen teilte  dem Finanzamt daraufhin mit, dass das im April 2019 erstellte Gutachten schlüssig und  nachvollziehbar sei und keine neuerliche Begutachtung erforderlich wäre.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_45`)


Seitens des Finanzamtes wird auf die Bindungswirkung der Gutachten des Bundesamtes für  Soziales und Behindertenwesen verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_67`)


Mit Bescheid des Bundesamtes für Soziales und Behindertenwesen vom 1. Feber 2019  wurde festgestellt, dass die Beschwerdeführerin ab 6. Dezember 2018 zum Kreis der  begünstigten Behinderten gehört.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_73`)


Hinsichtlich des Grades der Behinderung und der Fähigkeit, sich selbst den Unterhalt zu  verschaffen, liegen dem Bundesfinanzgericht zwei Bescheinigungen des Bundesamtes für  Soziales und Behindertenwesen vor, welche auf ärztlichen Sachverständigengutachten  beruhen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_80`)


Nach der Rechtsprechung (vgl für viele VwGH 29.9.2011, 2011/16/0063, oder VwGH  16.12.2014, Ro 2014/16/0053, mwN) sind die Abgabenbehörden (und in der Folge auch das  Bundesfinanzgericht) an die Bescheinigungen des Bundesamtes für Soziales und  Behindertenwesen gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und  vollständig und im Falle mehrerer Gutachten nicht einander widersprechend sind.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_121`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist nach § 8 Abs 6 FLAG 1967 durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_126`)


Dieser Umstand ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen nachzuweisen, welche auf einem ärztlichen Sachverständigengutachten zu  basieren hat.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_18`)


Im Abweisungsbescheid wird auf die im Zuge dieser Erledigung vom Bundesamt für Soziales  und Behindertenwesen im Auftrag des Finanzamtes erstellte Bescheinigung über das Ausmaß  der Behinderung der Bf. vom 3. Februar 2022 hingewiesen, die durch das Bundesamt für  Soziales und Behindertenwesen zugesendet wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_27`)


In einem Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen  Landesstelle Wien vom 25.06.2021 (siehe Beilage) sowie einer Gesamtbeurteilung vom  09.07.2021 (siehe Beilage) wird ein GdB von 50 v.H. festgestellt und eine Nachuntersuchung  erst für 07/2023 empfohlen, sodass die Begründung für die Nichtgewährung des  Erhöhungsbetrages, dass ein GdB aufgrund fehlender Befunde nicht ermittelt werden konnte,  nicht nachvollziehbar ist und der Bescheid somit mit Rechtswidrigkeit belastet ist.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_158`)


Abs. 6:   Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_165`)


Bei der Beurteilung der Frage, ob die Bf. voraussichtlich dauernd erwerbsunfähig ist (§ 6 Abs. 2  lit. d FLAG 1967), ist die Behörde bzw. das Bundesfinanzgericht an die der Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden Gutachten gebunden  und darf diese nur insoweit prüfen, ob sie schlüssig und vollständig und im Fall mehrerer  Gutachten nicht einander widersprechend sind (vgl. VwGH 9.9.2015, 2013/16/0049;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_218`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  Gutachten gebunden (vgl. VwGH 22.12.2011, 2009/16/0310, VwGH 16.12.2014,  Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und vollständig sind und  - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH 29.09.2011,  2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014,  Ro 2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und  2009/16/0310, VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch die bei Lenneis in  Csaszar/Lenneis/Wanke, FLAG, § 8 Rz 29 zitierte Rechtsprechung).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_224`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt - eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_248`)


Ist eine andere Form der Beweisführung als durch ein Gutachten des Bundesamtes für Soziales  und Behindertenwesen Sozialministeriumservice nicht zugelassen und ist – wie oben  ausgeführt – das letzte Gutachten wie die beiden vorangegangenen Gutachten des Gutachters  des Bundesamtes für Soziales und Behindertenwesen Sozialministeriumservice vollständig,  nachvollziehbar und schlüssig (auf die obigen Ausführungen wird verwiesen), ist das Schicksal  der Beschwerde entschieden.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales  und Behindertenwesen` | `Bundesamtes für Soziales  und Behindertenwesen` |
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_249`)


In der Beschwerde wird unter Verweis auf das oben wiedergegebene  Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen vom  25. Juni 2021 samt Gesamtbeurteilung vom 09. Juli 2021, in welchen „ein GdB von 50 v.H.  festgestellt und eine Nachuntersuchung erst für 07/2023 empfohlen (wird)“, ins Treffen  geführt, „sodass die Begründung für die Nichtgewährung des Erhöhungsbetrages, dass ein GdB  aufgrund fehlender Befunde nicht ermittelt werden konnte, nicht nachvollziehbar ist“.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/142675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142675.1_72`)


Zuständige Stelle ist (…) in allen übrigen Fällen sowie bei Zusammentreffen von  Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_52`)


"Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung "Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung"  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_93`)


Die mit 10.1.2013 festgestellte Behinderung basiert auf dem aktenkundigen Sachverständigen- gutachten vom 10.1.2013, die mit 21.12.2023 festgestellte Behinderung folgt aus der Gesamt- beurteilung des Bundesamtes für Soziales und Behindertenwesen, BASB Landesstelle NÖ vom  21.12.2023.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_117`)


verschiedener Art das Bundesamt für Soziales und Behindertenwesen (nunmehr  Sozialministeriumservice);

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_133`)


Diese Beeinträchtigung ist erst aus der Gesamtbeurteilung des  Bundesamtes für Soziales und Behindertenwesen, BASB Landesstelle NÖ vom 21.12.2023  ersichtlich.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_105`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_124`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_130`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der Beweisführung  Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/146077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146077.1_117`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/146077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146077.1_143`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  als Amtssachverständige bedient, die in die bei dieser Behörde gem. § 90 KOVG 1957 zu  führende Sachverständigenliste, eingetragen sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_14`)


Im Zuge des Verfahrens sei das Bundesamt für  Soziales und Behindertenwesen, Landesstelle Wien, beauftragt worden, ein Sachverständigen- gutachten zu erstellen.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_145`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_147`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_148`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der  anspruchsrelevanten Daten durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes  (BBG), BGBl. Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

</details>

---

## `Wirtschaftsuniversität_Wien` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `33befb3b`  
**Description:**
Matches 'Wirtschaftsuniversität Wien' as an organization.

**Content:**
```
\bWirtschaftsuniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 15987 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_11`)


Sachverhalt:   Tatsächlich befinde ich mich rechtmäßig in Österreich seit Mai 2015 und seit Oktober 2015 bin  ich ordentliche Studentin an der Wirtschaftsuniversität Wien.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_125`)


Seit dem Wintersemester 2015/16, Beginn 25.09.2015, studiert die Bf. als ordentliche  Studierende an der Wirtschaftsuniversität Wien das Bachelorstudium Wirtschafts- und  Sozialwissenschaften.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_5`)


Aus den ebenfalls vorgelegten Studienbestätigungen der Wirtschaftsuniversität Wien vom  03.01.2018 ist ersichtlich, dass die Tochter der Antragstellerin im Wintersemester 2017/18 als  außerordentliche Studierende zum Besuch einzelner Lehrveranstaltungen rückgemeldet  gewesen sei.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_53`)


Laut Betätigung der Wirtschaftsuniversität Wien über die Studienzeit war die Tochter von  19.10.2017 bis 27.02.2018 (Wintersemester 2017) zum außerordentlichen Studium (Besuch  einzelner Lehrveranstaltungen) und vom 27.02 208 bis 01.05.2019 (Sommersemester und  Wintersemester 2018) zum ordentlichen Studium Bachelorstudium Wirtschaftsrecht gemeldet.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_8`)


Der Bf. erhob gegen den Zurückweisungsbescheid fristgerecht Beschwerde (Schreiben vom  15. Dezember 2017) und brachte vor, dass das Finanzamt in der Begründung des Bescheides  von einem Studienwechsel ausgegangen sei, sein Sohn habe aber lediglich zu seinem  bestehenden Studium an der Wirtschaftsuniversität Wien ein fachverwandtes Parallelstudium  an der Fachhochschule begonnen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_8`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_9`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_68`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Camilla Schiedmann) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Camilla Schiedmann` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_83`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_120`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_143`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

## `Magistrat_Stadt_Wien` 

**F1:** 0.060 | **Precision:** 0.989 | **Recall:** 0.031  

**Format:** `regex`  
**Rule ID:** `b56eb701`  
**Description:**
Matches 'Magistrat der Stadt Wien' and its variations including genitive 'Magistrates', strictly excluding department numbers unless part of a specific known full name pattern.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,?\s*Magistratsabteilung\s+\d+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.989 | 0.031 | 0.060 | 565 | 559 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 559 | 6 | 17408 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_15`)


Die Nachforderung an Kommunalsteuer war in der Niederschrift für die Jahre 2007 – 2011 mit  insgesamt Euro 4.274,70 festgehalten und angeführt, dass die Bewertung des Ausmaßes der  Kommunalsteuerpflicht durch den Magistrat der Stadt Wien zu erfolgen hätte.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_51`)


Die Wiener Gebietskrankenkasse habe im Rahmen einer GPLA-Prüfung in ihrer Niederschrift  vom 22.10.2012 die obig beschriebenen Tatbestände festgehalten und abschließend  angemerkt „die Überprüfung des Ausmaßes der Kommunalsteuerpflicht erfolgt durch den  Magistrat der Stadt Wien“.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Wiener Gebietskrankenkasse` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_52`)


Der Prüfer wäre sich offensichtlich über das Ausmaß bzw. die  Aufteilung der Bemessungsgrundlage nicht im Klaren gewesen und habe die Entscheidung dem  Magistrat der Stadt Wien überlassen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_68`)


Der Magistrat der Stadt Wien habe im angefochtenen Bescheid nicht begründet, warum bei  einem gemeinnützigen Verein kein nichtunternehmerischer Bereich vorliegen solle.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_70`)


Mit Beschwerdevorentscheidung (BVE) vom 15.5.2014, zugestellt am 29.8.2014, wies der  Magistrat der Stadt Wien die gegenständliche Beschwerde als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_137`)


Entgegen den, dem angefochtenen Bescheid zugrundeliegenden, zur Kommunalsteuer  getroffenen Feststellungen der GPLA-Prüfung vom 22.10.2012 sowie der darauffolgenden  Prüfung (Revision) durch den Magistrat der Stadt Wien vom 26.9.2013, lag nach Meinung des  Bf. bei seiner Tätigkeit im Sportbereich ein zum Teil nichtunternehmerischer Bereich vor.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Aigner` (person)
- `KzlR Adalbert Bürks` (person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_6`)


Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft (§ 2 Wiener Parkometergesetz 2006) mit Strafverfügung  vom 18. Dezember 2019, MA 67/123/2019, angelastet, er habe das Fahrzeug am 11. Oktober  2019 um 13:54 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Theodor-Sickel- Gasse ggü 14, ohne einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_25`)


Der Magistrat der Stadt Wien wies in der Folge den Einspruch des Bf. vom 11. Jänner 2020  gegen die Strafverfügung vom 18. Dezember 2019 mit Bescheid vom 4. März 2020 gemäß § 49  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_38`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Mai 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_2`)


in der Verwaltungsstrafsache gegen  Desiree Barrabaß, Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 über die  zwei gleichlautenden Beschwerden der Beschuldigten vom 24. März 2020 gegen die zwei  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 25. Februar  2020, Zahl: a) MA67/xxxxx/2019 und b) MA67/yyyyy/2019, zu Recht erkannt:  I) Die zwei Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Desiree Barrabaß` (person)
- `Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_23`)


Der Magistrat der Stadt Wien lastete der Bf. mit zwei Straferkenntnissen, beide vom  25.02.2020, die bereits näher bezeichneten Verwaltungsübertretungen an und verhängte  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung  iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 jeweils eine Geldstrafe von € 60,00 und für den  Fall der Uneinbringlichkeit jeweils eine Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_48`)


Der Magistrat der Stadt Wien legte die Beschwerden samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in den Beschwerdesachen des Janosch Findeise,  Reichenauweg 22, 4724 Oberaubach, Österreich, gegen die zwei Straferkenntnisse des Magistrats der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde (beide) vom 23. Juni 2020, GZen 1)  MA67/Zahl1 und 2) MA67/Zahl2, in beiden Fällen wegen einer Verwaltungsübertretung nach §  2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) werden die Beschwerden als unbegründet abgewiesen  und werden die angefochtenen Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch Findeise` (person)
- `Reichenauweg 22, 4724 Oberaubach, Österreich` (address)
- `Magistrats der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_11`)


Wegen Verletzung des § 2 Wiener Parkometergesetz 2006 verhängte der Magistrat der Stadt  Wien gemäß § 4 Abs. 2 Wiener Parkometergesetz 2006 über den Bf. jeweils eine Geldstrafe in  Höhe von 60,00 Euro (Ersatzfreiheitsstrafe: jeweils 14 Stunden) und schrieb gemäß § 64 VStG  jeweils einen Beitrag zu den Kosten des Strafverfahrens von 10,00 Euro vor, womit sich der zu  zahlende Gesamtbetrag auf jeweils 70,00 Euro belief.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_101`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_5`)


Die Geldstrafe von € 36,00 ist zusammen mit dem Beitrag zu den Kosten des Strafverfahrens  (§ 64 Abs. 1 und 2 VStG) von € 10,00, insgesamt somit € 46,00, binnen zwei Wochen ab  Zustellung des Straferkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete der Beschwerdefüherin (Bf.) unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31.10.2019 an, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 02.09.2019 um 14:43 Uhr in der  gebührenpflichtigen Kurzparkzone in 1140 Wien, Penzinger Straße 157, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt.  Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1  Wiener Parkometergesetz 2006 wurde über die Bf. eine Geldstrafe iHv € 60,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_17`)


Der Magistrat der Stadt Wien erkannte die Bf. mit Straferkenntnis vom 26.11.2019 wegen der  bereits näher bezeichnete Verwaltungsübertretung für schuldig und verhängte wegen  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_39`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 17.12.2019).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_108`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Nicola Folprecht` (person)
- `Florian Abbruzzese, BA` (person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_6`)


Im Straferkenntnis vom 9. März 2020 warf der Magistrat der Stadt Wien dem Beschwerde- führer (Bf.) vor, er habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das  mehrspurige Kraftfahrzeug mit dem im Straferkenntnis näher bezeichneten behördlichen  Kennzeichen am 14. November 2019 um 14:51 Uhr in einer gebührenpflichtigen Kurzparkzone  abgestellt habe, ohne einen gültigen Fahrschein in das Fahrzeug zu legen oder einen elektroni- schen Parkschein zu aktivieren.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_11`)


Der Magistrat der Stadt Wien legte seiner Entscheidung die Anzeige vom 14. November 2019,  die Lenkerauskunft der Zulassungsbesitzerin und den Einspruch des Bf. gegen die an die Zulas- sungsbesitzerin adressierte Anonymverfügung zugrunde, worin der Bf. angegeben habe, dass  er zwischen 14:00 Uhr und 16:00 Uhr zwei Mal kurz und weniger als 10 Minuten in diesem  Areal zwar gehalten aber das Fahrzeug nicht abgestellt habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_13`)


Zu diesem Vorbringen stelle der Magistrat der Stadt Wien fest, dass der Meldungsleger wählen  könne, ob er eine Organstrafverfügung ausstelle oder eine Anzeige erstatte.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_30`)


3.3. Im Einspruch vom 07. Jänner 2020 gegen die als „Verfügung“ bezeichnete Lenkererhe- bung vom 20. Dezember 2019 gab der Bf. an, dass er „dort“ nicht geparkt habe und wies da- rauf hin, dass dem Magistrat der Stadt Wien seine Daten bekannt seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_33`)


3.5. Am 15. Jänner 2020 sandte der Bf. folgende Mail an den Magistrat der Stadt Wien: „Hier- mit beeinspruche ich die Verfügung vom 20.12.2019: Habe ich dort nicht geparkt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_39`)


B. Der Entscheidung wird folgende aus den Verwaltungsakten sich ergebende Sachlage zu- grunde gelegt: Im Straferkenntnis vom 9. März 2020 hat der Magistrat der Stadt Wien dem Bf.  eine Verwaltungsübertretung vorgeworfen, die er ihm auch in der Strafverfügung vom 08.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_2`)


über die Beschwerde des René Werkstetter, Feichtenweg 14, 3922 Thaures, Österreich, vom 6. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 25. August 2020, Zahl MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `René Werkstetter` (person)
- `Feichtenweg 14, 3922 Thaures, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_7`)


Die Geldstrafe von € 48,00 ist gemeinsam mit den Kosten des Verwaltungsstrafverfahrens  (€ 10,00), insgesamt somit € 58,00 binnen zwei Wochen nach Zustellung dieses  Straferkenntnisses an den Magistrat der Stadt Wien zu bezahlen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_8`)


Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_27`)


Mit Straferkenntnis vom 25. August 2020 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung und wegen Verletzung des § 5  Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006  eine Geldstrafe von € 60,00 und für den Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von  14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Franz Trockenbrot,  Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich  vom 15. März 2020, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 10. März 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 9 Abs. 2 Wiener  Kontrolleinrichtungenverordnung iVm § 4 Abs. 3 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 30. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Erkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Trockenbrot` (person)
- `Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich` (address)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_3`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (€ 12,00) ist gemeinsam mit der  Geldstrafe (€ 60,00) und dem Beitrag zu den Kosten der belangten Behörde (€ 10,00) binnen  zwei Wochen ab Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_5`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_23`)


Mit Strafverfügung vom 12. Februar 2020 lastete der Magistrat der Stadt Wien dem Bf. an, er  habe das verfahrensgegenständliche Fahrzeug am 12. Dezember 2019 um 14:52 Uhr in der  gebührenpflichtigen Kurzparkzone in 1110 Wien, Simmeringer Hauptstraße 59 - 61, abgestellt,  wobei elektronische Parkscheine mit einer fünfzehn Minuten nicht übersteigenden Abstellzeit  unmittelbar aufeinander folgend aktiviert worden seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_31`)


Mit Straferkenntnis vom 10. März 2020 wurde dem Bf. vom Magistrat der Stadt Wien die  bereits näher bezeichnete Verwaltungsübertretung angelastet und wegen Verletzung der  Rechtsvorschriften des § 9 Abs. 2 Wiener Kontrolleinrichtungenverordnung iVm § 4 Abs. 3  Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_63`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_242`)


Hier erweist sich die Bestimmung des Magistrat der Stadt Wien als Vollstreckungsbehörde als  zweckmäßig, da dem Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die  Vollstreckung der von den (anderen) Verwaltungsgerichten erlassenen Erkenntnissen und  Beschlüssen obliegt (vgl. für viele ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_6`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) folgende, die Verwaltungsstrafsache  MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich möchte  Ihnen mitteilen, dass am 24.10.2019 das Fahrzeug … folgende Person gelenkt hat: …“  Über eine am 24.10.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 30.12.2019 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  1 von 4 Seite 2 von 4

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_10`)


Mit Vollstreckungsverfügung vom 10.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 30.12.2019 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_13`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) auch folgende, die Verwaltungsstrafsa- che MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich  möchte Ihnen mitteilen, dass ich am 06.10.2020 bereits Einspruch mittels E-Mail auf die Straf- verfügung erhoben habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_14`)


Das Fahrzeug … hat am 21.11.2019 folgende Person gelenkt: …“  Über eine am 21.11.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 20.01.2020 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  21.11.2019 um 17:49 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt habe, ohne für  seine Kennzeichnung mit einem richtig entwerteten Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_18`)


Mit Vollstreckungsverfügung vom 11.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 20.01.2020 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Judith Leodolter` (person)
- `Franziskus Lex` (person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_5`)


III. Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_6`)


Die Geldstrafe von € 48,00 ist gemeinsam mit dem Beitrag zu den Kosten der belangten  Behörde von € 10,00 (§ 64 VStG 1991), insgesamt somit € 58,00, binnen zwei Wochen nach  Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67, erkannte den Beschwerdeführer (Bf.) mit  Straferkenntnis vom 18. Juni 2020, MA67/000/2020, für schuldig, das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 3. Jänner 2020 um 21:37 Uhr in  der gebührenpflichtigen Kurzparkzone in 1010 Wien, Bellariastraße 8, Nebenfahrbahn, ohne  einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_32`)


Da der Bf. die ihm angelastete Verwaltungsübertretung nicht in Abrede stellt, ist der  Schuldspruch des Straferkenntnisses des Magistrates der Stadt Wien vom 18. Juni 2020,  MA67/000/2020, in Rechtskraft erwachsen (vgl. VwGH 27.10.2014, Ra 2014/02/0053) und  oblag dem Bundesfinanzgericht daher nur die Überprüfung der Höhe der verhängten  Geldstrafe (§ 27 VwGVG) bzw. der für den Fall der Uneinbringlichkeit verhängten  Ersatzfreiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_62`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien, Magistratsabteilung 67` | `Magistrates  der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Irene Kohler` (person)
- `Dipl.-Ing. Erwin Göktan` (person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 13. August 2020,  MA67/206700430919/2020, angelastet, sie habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 20. Mai 2020 in der gebührenpflichtigen Kurzparkzone in  1110 Wien, Simmeringer Hauptstraße 152, ohne einem für den Beanstandungszeitpunkt 15:11  Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi über die am 04.11.2020 per Telefax  eingebrachte Beschwerde der Alva van de Velden, Guldenäcker 147, 9020 Klagenfurt, Österreich, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 6, vom 29.10.2020, Zahl:  MA67/Zahl/2020, in Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva van de Velden` (person)
- `Guldenäcker 147, 9020 Klagenfurt, Österreich` (address)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_17`)


Am 29.10.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte  Behörde die beschwerdegegenständliche Vollstreckungsverfügung, GZ. MA67/Zahl/2020, da  die mit obigem Straferkenntnis verhängte rechtskräftige Strafe bislang nicht bezahlt worden  sei, weshalb zur Einbringung des festgesetzten Gesamtbetrages in Höhe von € 75,00 (inkl. €  5,00 Mahngebühren) gemäß den §§ 3 und 10 Verwaltungsvollstreckungsgesetz 1991 (VVG) die  Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Proidl über die Beschwerde der  Istvan  Sicking, Fanny Elßler-Gasse 30, 9375 Zosen, Österreich, vom 09. Oktober 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 28. September 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der Fassung LGBl. für Wien Nr. 24/2012, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als der  Spruch des bekämpften Straferkenntnisses insoweit abgeändert wird, als die Geldstrafe von  Euro 60,00 auf Euro 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden  herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien, Magistratsabteilung 67` | `Magistrates  der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Proidl` (person)
- `Istvan  Sicking` (person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_6`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_75`)


Dazu sei auch angemerkt, dass auf der Rückseite von Organstrafverfügungen des Magistrates  der Stadt Wien wörtlich Folgendes vermerkt ist:  6 von 9 Seite 7 von 9

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien` | `Magistrates  der Stadt Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_83`)


Die Strafe wurde daher nicht ordnungsgemäß bezahlt. In der Folge leitete der Magistrat der  Stadt Wien mit der Strafverfügung vom 19.08.2020 das ordentliche Verwaltungsstrafverfahren  ein, welches letztlich zur verfahrensgegenständlichen Beschwerde gegen das o.a.  Straferkenntnis führte.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_116`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Marion Weißhar, Magnusplatz 23, 9555 Glantscha, Österreich, vom 20. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis mit der Maßgabe bestätigt, dass der Kostenbeitrag für das  behördliche Strafverfahren gemäß § 64 Abs. 2 VStG nicht 10,00 €, sondern 14,00 € beträgt.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien, Magistratsabteilung 67` | `Magistrates  der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Judith Leodolter` (person)
- `Marion Weißhar` (person)
- `Magnusplatz 23, 9555 Glantscha, Österreich` (address)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_4`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_23`)


Mit Straferkenntnis vom 8. Jänner 2021 wurde der Bf. vom Magistrat der Stadt Wien wegen  der bereits näher bezeichnete Verwaltungsübertretung für schuldig befunden und wegen der  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm  § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe iHv € 140,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 1 Tag und 9 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_50`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsstrafakt dem Bundes- finanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Jänner 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_114`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Alice Rainprechter` (person)
- `Ing. Techn R Arthur Kornhass` (person)
- `Gstaudet 21, 9556 Besendorf, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Bundesfinanzgerichtes vom 16.07.2020, Zahl RV/Zahl2/2020 zu Zahl  MA67/Zahl1/2019 wurde gegenüber dem Beschwerdeführer (Bf.) seine Beschwerde vom  18.03.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  vom 14.02.2020, Zahl: MA67/Zahl1/2019, als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Lieselotte Rübenkönig, Bakk. rer. nat., Strohweg 140g, 8593 Salla, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien, Magistratsabteilung 6` | `Magistrates der Stadt  Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Lieselotte Rübenkönig, Bakk. rer. nat.` (person)
- `Strohweg 140g, 8593 Salla, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_5`)


Am 11.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700867324/2019, da die mit GZ.  MA67/196700867324/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_9`)


Am 11.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700891928/2019, da die mit GZ.  MA67/196700891928/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  Verwaltungsvollstreckungsgesetz 1991 (VVG) und § 10 VVG die Zwangsvollstreckung verfügt  wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_12`)


Am 14.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700890302/2019, da die mit GZ.   MA67/196700890302/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  Verwaltungsvollstreckungsgesetz 1991 (VVG) und § 10 VVG die Zwangsvollstreckung verfügt  wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_15`)


Am 25.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700930712/2019, da die mit GZ.  2 von 5 Seite 3 von 5

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Univ.-Prof.in StR Caroline Akkoca, MBA, Hinterbachstraße 8, 4653 Spieldorf, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2021 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Jänner 2021, Zahl: MA67/206700566984/2020, mit  dem der Einspruch vom 10. November 2020 gegen die Strafverfügung vom 8. Oktober 2020 mit  derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Robert Pernegger` (person)
- `Univ.-Prof.in StR Caroline Akkoca, MBA` (person)
- `Hinterbachstraße 8, 4653 Spieldorf, Österreich` (address)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Univ.-Prof.in StR Caroline Akkoca, MBA (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Univ.-Prof.in StR Caroline Akkoca, MBA` (person)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_5`)


Der am 10. November 2020 beim Magistrat der Stadt Wien eingelangte Einspruch gegen diese  Strafverfügung wurde gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_7`)


Der Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8.  Jänner 2021, Zahl:  MA67/20600566984/2020, wurde folgendermaßen begründet:  „Gemäß § 49 Abs. 1 VStG kann der Beschuldigte gegen die Strafverfügung binnen zwei Wochen  nach deren Zustellung Einspruch erheben und dabei die seiner Verteidigung dienlichen  Beweismittel vorbringen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_36`)


Der Einspruch gegen die verfahrensgegenständliche Strafverfügung langte am 10. November  2020 beim Magistrat der Stadt Wien ein und wurde von diesem zu Recht als verspätet  3 von 4 Seite 4 von 4

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_36`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 24. März 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR über die Beschwerde des Siegbert Weicher, Raßnitzer Straße 15, 8292 Unterlimbach, Österreich, vom 6. November 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 7. Oktober 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF ABl. der  Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, nach Durchführung einer mündlichen Verhandlung am  21. April 2021, in Anwesenheit der Schriftführerin Ingrid Pavlik, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegbert Weicher` (person)
- `Raßnitzer Straße 15, 8292 Unterlimbach, Österreich` (address)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_9`)


Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) lastete dem Beschwerdeführer  (Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüber- wachung der Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit  Strafverfügung vom 17. August 2020, Zahl, an, er habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 28. April 2020 in der gebührenpflichtigen Kurzparkzone  in 1030 Wien, Landstraßer Hauptstraße 136, ohne einem für den Beanstandungszeitpunkt  19:40 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig  verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_3`)


über die Beschwerde der Finn Greitmann, MSc,  Fischthallerweg 6, 8200 Wilfersdorf, Österreich, vom 2. Mai 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 6. April 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Finn Greitmann, MSc` (person)
- `Fischthallerweg 6, 8200 Wilfersdorf, Österreich` (address)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten eines Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 8. März 2021 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 8. Jänner 2021 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Rustenschacherallee 44-56, ohne einen für  den Beanstandungszeitpunkt 10:18 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_13`)


Mit Straferkenntnis vom 6. April 2021 wurde die Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_111`)


II.4. Bauvorhaben „2“  Die Bf. beteiligte sich als Mitglied einer Bietergemeinschaft (in der Folge kurz: BIEGE) an der  vom Magistrat der Stadt Wien (Magistratsabteilung 31, Wiener Wasser; in der Folge kurz: MA  31) als Auftraggeberin im offenen Verfahren durchgeführten Ausschreibung von Erd- und  Baumeisterarbeiten das Projekt „Ersatzstollen Neubrucker 2 Umgebung 3270 Scheibbs“  (Projektnummer MA 31-177525/12), durch Legung eines Angebotes am 29.01.2014.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_152`)


Am 09.12.2015 erfolgte an Ort und Stelle die mängelfreie Abnahme der  Innenschalenoberfläche zwischen der (nunmehrigen) ARGE und dem Magistrat der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_155`)


Die gesamten ausschreibungsgegenständlichen Erd- und Baumeisterarbeiten wurden am  31.05.2016 vom Magistrat der Stadt Wien übernommen;

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_3`)


über das von der West Altrader GmbH  Dorf,  eingebrachte Anbringen vom 17. Mai 2021 in Zusammenhang mit dem an Gundula Doerfner, Öttlstraße 14, 3804 Reinsbach, Österreich  ergangenen Straferkenntnis des Magistrates der Stadt Wien vom 7. Mai 2021, GZ.  MA67/Zahl/2021, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, den  Beschluss gefasst:  Das Anbringen vom 17. Mai 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `West Altrader GmbH` (organisation)
- `Gundula Doerfner` (person)
- `Öttlstraße 14, 3804 Reinsbach, Österreich` (address)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_8`)


In der Folge wurde Gundula Doerfner  vom Magistrat der Stadt Wien, MA 67, mit Strafverfügung vom  23. April 2021 angelastet, dass er das in Rede stehende Fahrzeug an der bereits genannten  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Gundula Doerfner` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_15`)


Mit Strafverfügung vom 4. August 2020 wurde Bf1 (Beschwerdeführer, kurz Bf.) vom Magistrat  der Stadt Wien, Magistratsabteilung 67, angelastet, er habe das verfahrensgegenständliche  Fahrzeug am 5. Juni 2020 um 14:14 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Taborstraße 21a ggü, abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat  der Stadt Wien, Magistratsabteilung 67` — partial — gold is substring of pred: `Magistrat  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat  der Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien,  Magistratsabteilung 6` — partial — gold is substring of pred: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

</details>

---

## `Bundesfinanzgericht_Full_BFG_Fixed` 💣

**F1:** 0.391 | **Precision:** 0.983 | **Recall:** 0.244  

**Format:** `regex`  
**Rule ID:** `ddd6863b`  
**Description:**
Matches 'Bundesfinanzgericht' with optional grammatical endings and the '(BFG)' suffix as a single entity. Highest priority to prevent splitting.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?(?:\s*\(BFG\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.983 | 0.244 | 0.391 | 4468 | 4393 | 75 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4393 | 75 | 13604 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr.in Hemma Bährs` (person)
- `Univ.-Prof.in Rachel Darnieder` (person)
- `Finanzamtes Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_15`)


Diese war am 31. Dezember 2013 noch unerledigt anhängig und ist daher nach § 323 Abs 38 BAO vom Bundesfinanzgericht als Beschwerde iSd Art 130 Abs 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_50`)


Vollkommen unverständlich ist es für das Bundesfinanzgericht, dass dem Beihilfenwerber in der Bescheinigung aus dem Jahr 2014 ein voraussichtliches dauernd außer Stande sein, sich den Unterhalt zu verschaffen rückwirkend ab Mai 2010 bescheinigt wurde, obwohl dieser bis Mai 2005 +29 unbestritten Einkünfte aus einem aufrechten Dienstverhältnis erzielte und danach noch Arbeitslosengeld bezogen wurde (gesetzliche Voraussetzung für den Bezug von Arbeitslosengeld sind Arbeitsfähigkeit und Arbeitswilligkeit).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `2005` (date)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_70`)


Hinsichtlich der Verfassungskonformität dieser Regelung bestehen seitens des Bundesfinanzgerichtes keinerlei Bedenken.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `MMag. Gerald Erwin Ehgartner` (person)
- `Zeno Matyssek` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)
- `Finanzamt für Gebühren` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_23`)


II. Das Bundesfinanzgericht hat erwogen Seite 3 von 5 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_50`)


Dem Einwand der Beschwerdeführerin, dass bloß ein nicht der Bestandvertragsgebühr unterliegender Vorvertrag vorliege, kann von Seiten des Bundesfinanzgerichtes nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_56`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision) Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Raphael Williamson, BEd, Züggen 8, 8042 Graz, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Manuela Fischer` (person)
- `Raphael Williamson, BEd` (person)
- `Züggen 8, 8042 Graz, Österreich` (address)
- `Monika Pfundner-Lenz` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_11`)


…  Aus den dem Bundesfinanzgericht, BFG, vorliegenden Unterlagen ging hervor, dass seitens der  Wiener Gebietskrankenkasse im Jahr 2012 eine Sozialversicherungs-, Lohnsteuer- und  Kommunalsteuerprüfung hinsichtlich der Jahre 2007 – 2011 stattgefunden hatte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `Wiener Gebietskrankenkasse` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_99`)


II. Das Bundesfinanzgericht hat erwogen:  Der Bf. ist ein gemeinnütziger Verein, dessen Zweck laut Statuten die Pflege und Förderung des  Körpersports, sowie die geistige und körperliche Ertüchtigung seiner Mitglieder ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_181`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache QZKX Beratung, Lambacher Straße 9, 3123 Mittermerking, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 45-817/1493  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `M.` (person)
- `QZKX Beratung` (organisation)
- `Lambacher Straße 9, 3123 Mittermerking, Österreich` (address)
- `Mag. Dieter Walla & Partner Steuerberater OG` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `45-817/1493` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_8`)


Für den Fall, dass über diese Berufung nicht positiv mittels Berufungsvorentscheidung  entschieden werde, werde die Entscheidung durch den gesamten Berufungssenat der  Abgabenbehörde zweiter Instanz (§ 282 Abs. 1 Z. 1 BAO) sowie Durchführung einer mündlichen  Berufungsverhandlung (§ 284 Abs. 1 Z. 1 BAO) beantragt, was auch als Anträge gilt, sofern über  die Berufung bereits das Bundesfinanzgericht zu entscheiden hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_13`)


Bedauerlicher Weise wurde weder innerhalb des Bundesfinanzgerichtes eine Information über  die bereits erfolgte Entscheidung im zugrundeliegenden Abgabenverfahren noch von der  belangten Behörde eine Information über die Erlassung eines Gutschriftszinsenbescheides für  dieses Beschwerdeverfahren weitergeleitet, sodass es zu dieser weiteren – wenn auch  kurzfristigen – Verzögerung bei der Entscheidung gekommen ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_14`)


Über die Beschwerde wurde erwogen:  Rechtslage:  Gemäß § 323 Abs. 38 BAO sind die am 31. Dezember 2013 bei dem unabhängigen Finanzsenat  anhängigen Berufungen vom Bundesfinanzgericht als Beschwerde im Sinn des Art. 130 Abs. 1  B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_16`)


Mit der Einführung des Bundesfinanzgerichtes haben sich auch diverse Bezeichnungen  geändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Chen Petermüller` (person)
- `Sand 5, 4851 Hehenberg, Österreich` (address)
- `Anka Vrcic` (person)
- `Finanzamtes Salzburg-Land` (organisation)
- `20-238/1198` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_20`)


Mit Eingabe vom 30.09.2019 brachte der Bf einen Vorlageantrag an das Bundesfinanzgericht  ein, den die Abgabenbehörde am 30.04.2020 dem BFG vorlegte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_26`)


II. Das Bundesfinanzgericht hat erwogen:  Sachverhalt:  Der Bf hat nach Rechtskraft der Einkommen- und Umsatsteuerbescheide, in denen die  Festsetzung der Einkommen- und Umsatzsteuer 2016 wegen Nichtabgabe der  Steuererklärungen im Schätzungswege gemäß § 184 BAO erfolgte, einen  Wiederaufnahmeantrag unter Beilegung der ausständigen Steuererklärungen gestellt. Streit  zwischen den beiden Parteien des gegenständlichen verwaltungsgerichtlichen Verfahrens  besteht darüber, ob die Abweisung der Wiederaufnahmeanträge des Bf zu Recht erfolgt ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_53`)


Zulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Florenzia Claußing` (person)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich` (address)
- `Finanzamtes` (organisation)
- `10-95-558/8694` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_23`)


Das Bundesfinanzgericht kam daher zum Schluss, dem Spruch dieser  Beschwerdevorentscheidung fehle der normative, rechtsgestaltende Inhalt, weshalb die  Erledigung nicht als Bescheid angesehen werden könne.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_40`)


Mit Beschluss  vom 4. Dezember 2019, dem Bundesfinanzgericht zugestellt am 19. Dezember 2019, hatte  der Verwaltungsgerichtshof die außerordentliche Revision des betreffenden  Abgabepflichtigen, wie der Bf vertreten durch RA, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_63`)


Bundesfinanzgerichtes zu ähnlich gelagerten Fällen (zB BFG 4.6.2019, RV/3100356/2019;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_66`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Gabriele Grossgut-Palotás` (person)
- `Wendy Scherl` (person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `53-864/4798` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_12`)


Mit Vorlagebericht vom 7.10.2019 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_13`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_64`)


Das Bundesfinanzgericht verkennt nicht, dass die besuchten Seminare auch geeignet waren,  die beruflichen Kenntnisse und Fertigkeiten der Beschwerdeführerin zu verbessern;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_69`)


Seitens des Bundesfinanzgerichtes wird nicht in Abrede gestellt, dass die besuchten Seminare  einen positiven Effekt auf die berufliche Tätigkeit der Beschwerdeführerin hatten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_77`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Viktoria Kreiselmayer` (person)
- `Muran Waldhans, BEd` (person)
- `Am Tegel 5, 9831 Waben, Österreich` (address)
- `Corazza Kocholl Laimer Rechtsanwälte OG` (organisation)
- `Finanzamtes Innsbruck` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_157`)


IV. Rechtslage:  1. Gemäß § 323 Abs. 38 Bundesabgabenordnung (BAO), BGBl 1961/194 idgF., sind die am  31.12.2013 beim Unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen  Berufungen vom Bundesfinanzgericht als Beschwerden iSd Art. 130 Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_158`)


Solche Verfahren betreffende Anbringen wirken mit 1.1.2014 auch gegenüber dem  Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_201`)


Nach der Rechtsprechung des VwGH ist es zulässig, dass das Bundesfinanzgericht den dem  Erstbescheid zugrunde gelegten Sachverhalt rechtlich anders würdigt als das Finanzamt und  den Zeitpunkt der Entstehung der Steuerschuld anders ansetzt (vgl. VwGH vom 11.9.2014,  2013/16/0156, zur Änderung des Zeitraumes bei einer Normverbrauchsabgabe;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_220`)


Der Bf hatte im Streitzeitraum sowohl in Italien als auch in Österreich Wohnsitze, die er  regelmäßig benutzte, seinen Mittelpunkt der Lebensinteressen sieht das Bundesfinanzgericht  als in Österreich gelegen an, wozu auf obigen Punkt Pkt. III.3. verwiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_247`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Klarissa Kümml` (person)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_107`)


Am 24. Februar 2017 wurde die Beschwerde dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_108`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_109`)


Das Bundesfinanzgericht legt seinem Erkenntnis nachstehenden, aus der Aktenlage  hervorgehenden Sachverhalt als feststehend zugrunde:   Der Bf. ist österreichischer Staatsbürger und hatte seinen Wohnsitz seit jeher in Österreich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_141`)


Dem Bundesfinanzgericht ist  jedoch nicht bekannt, ob eine derartige Begründung vom Bf. je verlangt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_145`)


Auch im Hinblick der Ausführungen im Erkenntnis des  Bundesfinanzgerichtes (BFG 30.6.2020, RV 1100515/2013), wonach der Bf. in den Jahren 2011  und 2012 neben seinen Pensionsbezügen in den Sommermonaten beträchtliche Einkünfte aus  „Schwarzlohnzahlungen“ als Aushilfskoch erzielte, erscheint eine Schätzung im Ausmaß einer  Halbtagsanstellung in Höhe von CHF 2.000,00 durchwegs plausibel.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_238`)


Streitjahr 2014  Infolge der Gegenüberstellung der Beziehungen des Bf. gegenüber der Schweiz und Österreich  kommt das Bundesfinanzgericht zum Schluss, dass im Streitjahr 2014 der Mittelpunkt der  Lebensinteressen in die Schweiz verlagert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_241`)


Das Bundesfinanzgericht sieht es als schlüssig an, dass im Jahr 2014 bereits das  Hauptinteresse des Bf. in der Schweiz lag.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_243`)


Die schwierige finanzielle Situation des Bf. und  die nochmalige Bekräftigung des Bf. im Vorlageantrag, dass der Bf. sich in der Schweiz ein  „neues Leben“ aufbauen wollte, sieht das Bundesfinanzgericht durchwegs als glaubhaft an.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_259`)


Das Bundesfinanzgericht hat die Ermittlungsergebnisse im Rahmen der freien  Beweiswürdigung als schlüssig beurteilt.   Insgesamt war wie im Spruch zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_261`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Miroslav Hankel, BEd` (person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_45`)


2013 beim unabhängigen  Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen Berufungen und  Devolutionsanträge vom Bundesfinanzgericht als Beschwerden im Sinne des Art. 130 Abs. 1 B- VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_46`)


Solche Verfahren betreffende Anbringen wirken mit 01.01.2014 auch  gegenüber dem Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_69`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Susanne Feichtenschlager` (person)
- `Daisy Wegelein` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `61-004/6209` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_58`)


Im Antrag auf Entscheidung durch das Bundesfinanzgericht vom 18.01.2019 wurde ausgeführt,  dass ärztliche Bestätigungen mehrfach vorgelegt worden seien.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_74`)


Mit Vorlagebericht vom 21.06.2019 legte das Finanzamt die Beschwerdesache dem  Bundesfinanzgericht vor und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_75`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_142`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz.in DDr.in Rafaela Ringart` (person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich` (address)
- `Silvestri Bau GmbH` (organisation)
- `Mag. WP` (person)
- `38-663/2876` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung:  Der Senat legt der Entscheidung den im Folgenden dargestellten, als erwiesen angenommenen  Sachverhalt zugrunde, der sich aus den Akten des Verwaltungsverfahrens und den  zugrundeliegenden Datenbanken der belangten Behörde sowie dem Vorbringen der BF und  der belangten Behörde im Verfahren bzw. der mündlichen Verhandlung ergibt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_184`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  14 von 15 Seite 15 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers Emma Türker, Frauenhofenstraße 13, 5132 Gasteig, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Emma Türker` (person)
- `Frauenhofenstraße 13, 5132 Gasteig, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_17`)


Am 15.06.2020 wurde die Beschwerde vom Finanzamt dem Bundesfinanzgericht zur  Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_19`)


Sachverhalt  Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:   Dem BF wurde am 22.10.2019 in die Databox von FinanzOnline der Einkommensteuerbescheid  2018 zugestellt. Der Einkommensteuerbescheid 2018 enthält eine Amtssignatur vom  22.10.2019.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_22`)


Beweiswürdigung  Gem. § 167 Abs. 2 BAO haben die Abgabenbehörde und das Bundesfinanzgericht unter  sorgfältiger Berücksichtigung der Ergebnisse des Abgabenverfahrens nach freier Überzeugung  zu beurteilen, ob eine Tatsache als erwiesen anzunehmen ist oder nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Alma Gaedecke, Höbelgasse 24, 9400 St. Thomas, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Alma Gaedecke` (person)
- `Höbelgasse 24, 9400 St. Thomas, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_22`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die am **** geborene Tochter der Bf., T, leidet an einer idiopathischen Skoliose.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_75`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Erich Schwaiger` (person)
- `Matthäus Domrös` (person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Dr. Gerlinde  Rieser` (person)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_36`)


Bei den  angeführten Lebensmitteln treffe dies nicht zu.  c. Verfahren vor dem Bundesfinanzgericht  Die Bf. beantragte daraufhin rechtzeitig die Vorlage an das Bundesfinanzgericht sowie - im  Falle einer weiteren Fragestellung - die Abhaltung eines Erörterungstermins.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_48`)


Über die Beschwerde wurde erwogen:  2. Sachverhalt  Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_93`)


c. Rechtsgrundlagen, rechtliche Würdigung  Beweiswürdigung  Gem. § 167 Abs. 2 BAO haben die Abgabenbehörde und das Bundesfinanzgericht unter  sorgfältiger Berücksichtigung der Ergebnisse des Abgabenverfahrens nach freier Überzeugung  zu beurteilen, ob eine Tatsache als erwiesen anzunehmen ist oder nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_97`)


Das Bundesfinanzgericht hat – wie auch das Finanzamt - die abgabepflichtigen Fälle zu  erforschen und von Amts wegen die tatsächlichen und rechtlichen Verhältnisse zu ermitteln,  die für die Abgabepflicht und die Erhebung der Abgaben wesentlich sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Nadja Rossetto` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Imre & Schaffer Rechtsanwälte OG` (organisation)
- `Finanzamtes` (organisation)
- `85-716/2059` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_47`)


In der weiteren Folge beantragte der Bf. die Beschwerdevorlage an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_51`)


Das Bundesfinanzgericht hat erwogen:  1.1. Zu Spruchpunkt I. (teilweise Stattgabe)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Rainer Leutheußer` (person)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich` (address)
- `Egger & Freidorfer Steuerberatungs-OG` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_44`)


Nach Einbringung eines Vorlageantrages ohne ergänzendem Vorbringen ersuchte das  Bundesfinanzgericht den Bf. den Sachverhalt betreffend die Gerichtsverfahren beim  Handelsgericht Wien und beim Arbeitsgericht darzulegen und mit entsprechenden  Beweismitteln nachzuweisen;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erzielte im streitgegenständlichen Jahr als Vorstand der H. AG Einkünfte aus  nichtselbständiger Tätigkeit;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `H. AG` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_97`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Donald Paulovits` (person)
- `Tröbach 41, 9130 Leibsdorf, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `95-720/4312` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_9`)


Mit Beschluss vom 23.4.2014 hat das  Bundesfinanzgericht die Beschwerde gegen den Feststellungsbescheid als unzulässig  zurückgewiesen, weil die Bescheide nicht ordnungsgemäß adressiert waren.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_16`)


Mit Erkenntnis des Bundesfinanzgerichts vom 6.9.2018,  RV/2100723/2018 wurde die finanzamtliche Entscheidung vollinhaltlich bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_19`)


II. Das Bundesfinanzgericht hat erwogen:  1. Rechtliche Beurteilung  1.1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Monika Kofler` (person)
- `Maximilian Joobs` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Streitpunkte:  Die Bf. lebt auch nach eigenen Angaben seit 3. Juli 2019 nicht mehr mit ihren Kindern in einem  gemeinsamen Haushalt. Ab 4.7.2019 war der Kindesvater an einer gemeinsamen Adresse mit  den Kindern gemeldet und lebte mit diesen unstrittig in einem gemeinsamen Haushalt. Die  Verständigung des Finanzamtes durch die Bf. erfolgte erst am 27.8.2019, als die  Familienbeihilfe bereits überwiesen worden war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_64`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `Oleg Kreissl` (person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_133`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_134`)


Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:  Herr [B] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Aufräumen von Baustellen, bestehend im Zusammentragen und  eigenverantwortlichem Trennen von Bauschutt und -abfällen entsprechend der  Wiederverwertbarkeit‚ einschließlich des Bereitstellens zum Abtransport sowie im  Reinigen von Baumaschinen und Bauwerkzeugen durch Beseitigen von Rückständen  mittels einfacher mechanischer Methoden, wie Abkratzen, Abspachteln und dergleichen  und nachfolgendem Abspritzen mit Wasser, unter Verwendung ausschließlich eigener  Arbeitsgeräte sowie unter Ausschluss der den Denkmal-, Fassaden- und  Gebäudereinigern vorbehaltenen Tätigkeiten einer Grund- oder Bauschlussreinigung“  Herr [A] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Heben, Senken und Befördern von Lasten mittels Einsatzes von mechanischen oder  maschinellen Einrichtungen unter Ausschluss der Beförderung mittels Kraftfahrzeugen“  Herr [B] und Herr [A] führten im Beschwerdezeitraum Baustellenarbeiten entsprechend ihren  Gewerbeberechtigungen für den Beschwerdeführer aus.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_172`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsstellungen  gemäß § 167 Abs 2 BAO als erwiesen annehmen

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_201`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof. Niels Aleksejew` (person)
- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_29`)


Gegen diesen Bescheid erhob die Bf. durch ihren rechtsfreundlichen Vertreter Beschwerde,  warf der belangten Behörde mangelnde Sachverhaltsermittlung, Beweiswürdigung,  Aktenwidrigkeit und Begründung vor und stellte den Antrag, die Beschwerde ohne Erlassung  einer Beschwerdevorentscheidung dem Bundesfinanzgericht vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_49`)


II. Das Bundesfinanzgericht hat erwogen:  Die zur Vertretung juristischer Personen berufenen Personen und die gesetzlichen Vertreter  natürlicher Personen haben alle Pflichten zu erfüllen, die den von ihnen Vertretenen obliegen,  und sind befugt, die diesen zustehenden Rechte wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_78`)


Sie  beschränkt sich lediglich mit dem Hinweis auf ein Erkenntnis des Bundesfinanzgerichts, worin  nicht sie, sondern ihr Ehemann bzw. ihr Sohn wegen des Verdachtes der Hinterziehung von  Umsatzsteuervorauszahlungen und Nichtabfuhr von Lohnabgaben verantwortlich gemacht  wurde bzw. keine finanzstrafrechtliche Bestrafung erfolgte, hinzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_119`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_85`)


7. Zufolge der Aufhebung durch den VwGH hat nunmehr das Bundesfinanzgericht (BFG) im  fortgesetzten Verfahren über die gegen den Festsetzungsbescheid betr.

**False Positives:**

- `Bundesfinanzgericht` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_43`)


Über die Beschwerde wurde erwogen:  1. Zuständigkeit des Bundesfinanzgerichtes (BFG)

**False Positives:**

- `Bundesfinanzgerichtes` — partial — pred is substring of gold: `Bundesfinanzgerichtes (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)

</details>

---

## `BFG_Abbreviation` 💣

**F1:** 0.209 | **Precision:** 0.963 | **Recall:** 0.117  

**Format:** `regex`  
**Rule ID:** `9df4c7c3`  
**Description:**
Matches 'BFG' as an organization, ensuring it is not part of the full name 'Bundesfinanzgericht' (handled by higher priority rule).

**Content:**
```
\bBFG\b(?!\s*\(BFG\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.963 | 0.117 | 0.209 | 2184 | 2104 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2104 | 80 | 15866 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_11`)


…  Aus den dem Bundesfinanzgericht, BFG, vorliegenden Unterlagen ging hervor, dass seitens der  Wiener Gebietskrankenkasse im Jahr 2012 eine Sozialversicherungs-, Lohnsteuer- und  Kommunalsteuerprüfung hinsichtlich der Jahre 2007 – 2011 stattgefunden hatte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wiener Gebietskrankenkasse` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_98`)


Die Beschwerde wurde dem BFG zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_131`)


Zum entscheidungswesentlichen Sachverhalt, der sich für das BFG aus den vorliegenden  Prüfungsakten und Unterlagen ergab, war festzuhalten:  Der Bf. hatte im Prüfungszeitraum ungefähr 190 Mitglieder, welche auf sieben Freiplätzen  sowie vier Hallenplätzen den Tennissport ausüben konnten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_145`)


Dazu wurde durch das BFG festgestellt, dass der Bf. im geprüften Zeitraum seinen Mitgliedern  und auch Nichtmitgliedern unterschiedliche Leistungen, dem „Leistungskatalog“ entsprechend,  zur Nutzung der Tennisanlagen sowie Konditionstraining und die Nutzung einer Sauna anbot.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_165`)


Das BFG kam daher zum Schluss, dass, iSd § 3 Abs. 1 KommStG 1993, das Unternehmen des Bf.  seine gesamte Tätigkeit umfasste;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_11`)


Zwischenzeitig haben beim BFG zu den zugrundeliegenden Abgabenbescheiden  Senatsverhandlungen stattgefunden und wurden neue Abgabenbescheide erlassen, die – wie  im Vorhalt vom 28. März 2014 angekündigt – zu Gutschriftszinsenbescheiden geführt haben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_19`)


Die Abgabenbehörde folge der  Rechtsprechung des BFG, nach der ein Antrag auf Wiederaufnahme gemäß § 303 BAO unter  gleichzeitiger Einreichung der fehlenden Abgabenerklärungen nicht zum Erfolg führe, wenn  Abgaben mangels rechtzeitiger Einreichung von Abgabenerklärungen gemäß § 184 BAO  geschätzt worden seien.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_20`)


Mit Eingabe vom 30.09.2019 brachte der Bf einen Vorlageantrag an das Bundesfinanzgericht  ein, den die Abgabenbehörde am 30.04.2020 dem BFG vorlegte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_39`)


Das sind insbesondere die jeweiligen  Zahlungseingänge und Zahlungsausgänge bzw. das diesen zugrunde liegende Belegmaterial (s.  zB BFG vom 12.01.2015, RV/7101489/2011;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_40`)


BFG 06.12.2017, RV/7101214/2011;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_41`)


BFG  27.3.2019, RV/7100558/2019; jeweils mwN).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_45`)


(BFG 27.3.2019,  RV/7100558/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_49`)


Umstände, die einer Partei im Zeitpunkt der Entscheidung zwar bekannt sind, jedoch etwa auf  Grund einer Verletzung der Offenlegungs- und Wahrheitspflicht bei der Bescheiderlassung  nicht berücksichtigt werden konnten, bilden keinen tauglichen Wiederaufnahmegrund für eine  Wiederaufnahme auf Antrag der Partei (vgl. Fischerlehner, Abgabenverfahren², § 303 BAO,  Anm. 6; sowie nochmals zB BFG 27.3.2019, RV/7100558/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_50`)


Das Wiederaufnahmeverfahren hat nicht den Zweck die Versäumnisse des Bf. im  Abgabenverfahren zu sanieren (siehe nochmals die bereits oben zitierte Literatur bzw. BFG- Rechtsprechung).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_63`)


Bundesfinanzgerichtes zu ähnlich gelagerten Fällen (zB BFG 4.6.2019, RV/3100356/2019;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_107`)


Diese Aussage erscheint dem BFG insofern wenig glaubwürdig, weil seine Familie  mitgefahren sein soll und die Tochter des Bf (E, geb. August 1998) genau zu der Zeit, also Ende  September/Anfang Oktober 2005, in Adr1 wohl die Schule hat besuchen müssen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_139`)


Auch wenn der Bf seinen regulären Wohnsitz in Italien hatte und diesen – wie behauptet -  aufgrund seines Berufes dort haben musste, so ist nach Ansicht des BFG jedenfalls von einer  engeren Beziehung zu Österreich auszugehen, da seine eigene Familie mit Frau und Kindern  hier wohnte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_151`)


Es  kann somit nach dem Dafürhalten des BFG davon ausgegangen werden, dass die  Nutzungsabsicht des Fahrzeuges zum Zeitpunkt der Anschaffung primär in der Strecke Adr1 –  Adr2 und zurück gelegen war.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_240`)


Aber selbst wenn (faktisch) in einem Mitgliedstaat  keine Rückerstattung der Mehrwertsteuer erfolgt, ist die Besteuerung des  innergemeinschaftlichen Erwerbs nicht unbillig (vgl. BFG vom 3.12.2015, RV/3100124/2015).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_145`)


Auch im Hinblick der Ausführungen im Erkenntnis des  Bundesfinanzgerichtes (BFG 30.6.2020, RV 1100515/2013), wonach der Bf. in den Jahren 2011  und 2012 neben seinen Pensionsbezügen in den Sommermonaten beträchtliche Einkünfte aus  „Schwarzlohnzahlungen“ als Aushilfskoch erzielte, erscheint eine Schätzung im Ausmaß einer  Halbtagsanstellung in Höhe von CHF 2.000,00 durchwegs plausibel.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_47`)


2. Festgestellter Sachverhalt   In der Folge legt das BFG dem Erkenntnis nachstehenden, aus der Aktenlage sowie dem  Parteienvorbringen resultierenden Sachverhalt zu Grunde:  Als Ergebnis einer im Betrieb der im streitgegenständlichen Zeitraum als Prostituierte und  Masseuse tätigen Bf. statt gefundenen Außenprüfung wurden - ob der im  Verwaltungsgeschehen ausführlich dargestellten Aufzeichnungsmängel - die  Abgabenbemessungsgrundlagen betreffend die Umsatz- und Einkommensteuern für die Jahre  2009 und 2010 im Schätzungsweg ermittelt, mit der Folge, dass gegenüber der bis dato den  Status eines Kleinunternehmers innehabenden Bf. erstmals Umsatzsteuer für die Jahre 2009  und 2010 vorgeschrieben, respektive in Abweichung der bisher für das Jahr 2010 erklärten  Einkünfte aus Gewerbebetrieb im wiederaufgenommenen Verfahren neue Sachbescheide zur  Einkommensteuer 2009 und 2010 erlassen wurden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_58`)


Festsetzung auf im Schätzungsweg ermittelten Bemessungsgrundlagen gefußt hat -, die Bf. im  Zuge des Prüfungsverfahrens eingestanden hat, die täglichen Erlösaufzeichnungen, sprich die  Bareinnahmezettel weggeworfen zu haben bzw. auf die der steuerlichen Vertretung für das  Jahr 2010 übermittelten Summenaufstellung verwiesen hat, nach dem Dafürhalten des BFG an  der Schätzungsberechtigung dem Grunde nach keine Zweifel obwalten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_62`)


Obige vom BFG gezogene Schlussfolgerung liegt einleitend darin begründet, dass die belangte  Behörde im Ansatz die Wochenerlöse von 800,00 Euro (8 Kunden x 100,00 Euro) rein den  Angaben der Bf. folgt, bzw. auch die Anzahl von 46 Produktivwochen als in Kongruenz zur  allgemeinen Lebenserfahrung stehend zu erachten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_64`)


In der Zurechnung von durch eine weitere Prostituierte erzielten Umsätzen zu den  Betriebsergebnissen der Bf. vermag das BFG ebenfalls keine Unrichtigkeit zu erkennen, da  mangels Mitwirkung der Bf. an der Sachverhaltsaufklärung deren Geschäftsbeziehung zur Bf.  (Dienstnehmereigenschaft, eigenständige Tätigkeit gegen Bestreitung der Geschäftskosten  etc.) nicht zu ermitteln war und ergo dessen etwaige Schätzungsungenauigkeiten zur Lasten,  der Anlass zu Schätzung gebenden Bf. gehen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_24`)


Darauf beantragte der BF durch seine ausgewiesene Vertreterin fristgerecht die Vorlage der  Beschwerde zur Entscheidung durch das BFG.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_65`)


Mit 12.11.2010 wurde er zum allein vertretungsbefugten Geschäftsführer bestellt. Das BFG  folgt damit den Ausführungen des BF in der Beschwerde nicht, wonach er erst mit 29.11.2010  (der Eintragung der GF Funktion im Firmenbuch) zum alleinvertretungsbefugten  Geschäftsführer bestellt worden sei.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_149`)


Dennoch kann das BFG den Überlegungen des FA zur Haftungsinanspruchnahme für die  Säumniszuschläge 2010 und 2011 nicht folgen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_167`)


Das  BFG hat daher keine Bedenken, dass die geltend gemachten Abgaben an Lohnsteuern,  Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag zurecht in dieser Höhe vorange- meldet worden waren.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_171`)


Entscheidung des BFG bereits 63 Jahre alt, seine Einkunftsituation sei somit auch für einen  längeren Zeitraum nicht als positiv zu bewerten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_173`)


Dazu ist aus Sicht des BFG festzuhalten, dass der BF in seiner Beschwerde dargelegt hat, dass  von den steuerlichen Problemen seiner Vorgänger als Geschäftsführer gewusst habe  diesbezüglich auch nachgefragt habe und von diesen damit abgefertigt worden sei, dass ihn  diese Dinge nichts angingen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_177`)


Das BFG stimmt der  Einschränkung der Haftung auf jene Abgaben, die im Zeitraum seiner Geschäftsführertätigkeit  von November 2010 bis April 2011 angefallen sind, zu, da durchaus nachvollziehbar ist, dass  der BF mit der Übernahme der Geschäftsführertätigkeit „geködert“ worden ist und die  tatsächlichen Machthaber damit das Risiko aus den Malversationen auf ihn abwälzen wollten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_178`)


Dennoch kann das BFG aus Zweckmäßigkeitsgründen nicht von einer Haftungsinanspruch- nahme des BF im oben dargestellten Umfang absehen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_39`)


Der Einstieg in FinanzOnline bzw. das tatsächliche Einsehen der Databox durch den  FinanzOnline-Teilnehmer durch konkretes Öffnen, Lesen oder Ausdrucken des Bescheides ist  dabei irrelevant (UFS 22.07.2013, RV/0002-F/13, BFG 24.11.2017, RV/7104134/2017, BFG  18.09.2018, RV/7103033/2018, vgl. weiters Ritz, BAO6, § 98 Tz 4).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_93`)


Die „Bürokosten“ werden wie folgt ermittelt:  Beantragte „Bürokosten“ lt. Bf. € 7.196,51  Wohnungsmiete € -4.485,00  Strom € -160,07  Gas € -281,48  Druckerpatronen 40 % Privatanteil (nicht strittig) € -311,95  „Bürokosten“ lt. BFG € 1.958,01  Die „Sonstigen Werbungskosten“ betragen sohin: Rechtsanwaltskosten € 30.433,50,  Kilometergeld € 2.948,40 und Bürokosten (lt. BFG) € 1.958,01; insgesamt sohin € 35.339,91.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_94`)


Ermittlung der Werbungskosten für das Jahr 2014:  Sonstige Werbungskosten lt. BFG € 35.339,91  Anerkannte nicht strittige Arbeitsmittel € 834,81  Werbungskosten neu € 36.174,72  8 von 9 Seite 9 von 9

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_195`)


Die angefochtenen Bescheide betreffend Festsetzung von Dienstgeberbeiträgen waren daher  (durch Reduzierung der Bemessungsgrundlagen um die strittigen Hinzurechnungen) gemäß  § 279 BAO wie folgt abzuändern:  2010:  Bemessungsgrundlage lt. angefochtenem Bescheid: 5.607,11 €  Bemessungsgrundlage NEU lt BFG: 2.807,11 €  Festsetzung Dienstgeberbeitrag lt. angefochtenem Bescheid: 252,32 €  Festsetzung Dienstgeberbeitrag NEU lt BFG: 126,32 €

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_196`)


2011:  Bemessungsgrundlage lt. angefochtenem Bescheid: 14.198,66 €  Bemessungsgrundlage NEU lt BFG: 8.087,99 €  Festsetzung Dienstgeberbeitrag lt. angefochtenem Bescheid: 638,94 €  Festsetzung Dienstgeberbeitrag NEU lt BFG: 363,96 €  14 von 15 Seite 15 von 15

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_197`)


2012:  Bemessungsgrundlage lt. angefochtenem Bescheid: 66.764,66 €  Bemessungsgrundlage NEU lt BFG: 35.239,55 €  Festsetzung Dienstgeberbeitrag lt. angefochtenem Bescheid: 3.004,41 €  Festsetzung Dienstgeberbeitrag NEU lt BFG: 1.585,78€

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_87`)


Abgesehen davon wurde im – von der Bf. angeführten - Erkenntnis des BFG RV/2300028/2013  zu den eingewandten psychischen Schwierigkeiten des Bf. angemerkt, dass der Unwert seiner  Unterlassungen zwar objektiv abgemildert sei, er aber in seiner grundsätzlichen  Entscheidungsfähigkeit als Geschäftsführer insoweit nicht wesentlich beeinträchtigt war, weil  er immerhin drei Jahre hindurch als Entscheidungsträger gearbeitet und unternehmerische  Dispositionen getroffen habe.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_225`)


Wie bei dem, dem Erkenntnis des BFG vom 26.07.2016,  RV/7100282/2010 zu Grunde liegenden Sachverhalt ist auch im vorliegenden Fall davon  auszugehen, dass der Verpächter ein großes wirtschaftliches Interesse am Bestehen und an der  Art des Betriebes hat.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_241`)


Die getroffene Entscheidung entspricht der Judikatur des Verwaltungsgerichtshofes  07.10.1985, 85/15/0136 und des BFG 26.07.2016, RV/7100282/2010 sowie weitere, weshalb  eine Revision nicht für zulässig erachtet wird.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_12`)


Darauf beantragte die BF fristgerecht die Vorlage der Beschwerde zur Entscheidung durch das  BFG.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_19`)


Mit Verfügung des GV-Ausschusses vom 15.07.2020 wurde die gegenständliche  Beschwerdesache der damit belasteten Gerichtsabteilung gemäß § 9 Abs. 9 BFGG  abgenommen und am 16.07.2020 der derzeit damit befassten Gerichtsabteilung zugeteilt.    II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Das BFG legt seiner Entscheidung den folgenden, als erwiesen angenommenen Sachverhalt  zugrunde:  Die BF hatte vom 22.10.2008 bis 06.08.2009 einen Nebenwohnsitz in X, [...].

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_32`)


Das BFG folgte hinsichtlich der Frage, ob die BF nach dem 31.08.2015 in Österreich noch eine  Wohnung innehatte die sie (frei) benutzen konnte nicht den Ausführungen der BF im  gegenständlichen Beschwerdeverfahren.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_40`)


Eine durchgängige Überlassung der wesentlichen  Teile der Wohnung – wie von der BF behauptet - kann das BFG nicht erkennen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_52`)


Dieser Ansicht schließt sich das BFG aufgrund des oben dargestellten, als erwiesen  angenommenen Sachverhaltes an.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_53`)


Unabhängig davon, dass die Umstände der Nutzung durch  die BF - wie oben dargestellt - nicht glaubhaft sind und das BFG daher davon ausgeht, dass die  Nutzung der Wohnung - wenn überhaupt - in wesentlich eingeschränkterem Umfang durch die  BF erfolgt ist, sieht das BFG eine mögliche Nutzung durch die BF als Nutzung wie ein Gast, der  die Wohnung eines anderen mitbenutzt als erwiesen an.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_72`)


Auch hinsichtlich der Frage, welcher Prozentsatz der Anschaffungskosten einer  Liegenschaft als Grundanteil auszuscheiden ist, folgte das BFG den einschlägigen gesetzlichen  Bestimmungen und den auf deren Basis erlassenen VO.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_49`)


Da vom Beschwerdeführer kein Antrag iSd § 303 Abs. 2 BAO gestellt worden ist, war der  gegenständliche Bescheid nicht zu erlassen (siehe auch BFG 28.10.2014, RV/2100633/2011).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_690`)


UFS, BFG und die deutschen Finanzgerichte gingen in ihrer bisherigen Rechtsprechung davon  aus, dass bei bestimmten Branchen der Warenhandel sehr häufig im Rahmen von  Karussellkonstruktionen oder durch betrügerische Vorlieferanten abgewickelt wird (UFS  6.5.2013, RV/0739-L/08): Dazu zählen beispielsweise der KFZ-Handel (zB FG Saarland,  Beschluss vom 13.5.2003, 1 V 22/03), der Handel mit Mobiltelefonen (zB BFH 19.4.2007, VR  48/04), der Schrotthandel (zB UFS 17.11.2011, RV/0456-L/07) oder der Handel mit  Computerteilen (zB EuGH C-354/03 vom 12.1.2006, Rs „Optigen/Fulcrum/Bond gegen  Commissioners of customs & Exercise).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `BFH` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_691`)


Aufgrund der besonderen Anfälligkeit dieser  Marktbereiche besteht eine erhöhte Sorgfaltsverpflichtung des ordentlichen Kaufmannes (BFG  5.3.2015, RV/5101050/2013).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_45`)


Das BFG habe in einer aktuellen Entscheidung (BFG 29.3.2017, RV/6100881/2014) die  bisherige Rechtsansicht allerdings dahingehend eingeschränkt, dass sich die Abgabenbehörde  auch aus früheren Veranlagungsjahren bekannte Sachverhalte zurechnen lassen müsse, wenn  es einen eindeutigen Sachzusammenhang mit späteren Jahren gebe.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_105`)


Das gelte auch dann, wenn  das BFG in Einzelfällen eine weniger strenge Sichtweise zulasse.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_106`)


i. Zudem sei der gegenständliche Sachverhalt nicht vergleichbar mit dem Verfahren in der BFG- Entscheidung 29.3.2017, RV/6100881/2014.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_66`)


Wie das Bundesfinanzgericht  (BFG) den Akten entnehmen konnte, verfügte dieses Unternehmen weder über Personal, noch  über das Knowhow um solche Leistungen zu erbringen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_76`)


Aus dem Akteninhalt war für das BFG nicht feststellbar, dass der Rechnungsbetrag an die Bf.  zurückgeflossen war bzw. dass, und in welcher Form, der Betrag den Anteilsinhabern  zugeflossen war.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_82`)


Die Vorteilszuwendung an die Gesellschafter der Bf. oder ihnen nahestehende Personen und  eine dadurch ausgelöste verdeckte Ausschüttung war für das BFG dadurch nicht erwiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_60`)


Mit Beschluss des BFG vom 8.4.2020 wurde die Beschwerdeführerin ersucht, betreffend die  Zeiträume 01.01.2011 bis 31.12.2011 und 01.01.2013 bis 31.08.2013 jeweils für einen  repräsentativen Geschäftsfall einen vollständigen Dokumentensatz bestehend aus  Leasingantrag und Antrag auf Full-Service-Vertrag des Kunden und entsprechender  Annahmebestätigung der Beschwerdeführerin zu übermitteln.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_62`)


Mit Beschluss des BFG vom 6.7.2020 wurden der belangten Behörde zur Wahrung des  Parteiengehörs das Schreiben der Beschwerdeführerin vom 30.6.2020 sowie die diesem  Schreiben beigelegten Unterlagen übermittelt. Daraufhin teilte die belangte Behörde dem BFG  mit, dass auf das bisherige Vorbringen verwiesen und keine weitere Stellungnahme abgegeben  werde.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_233`)


Der Vollständigkeit halber wird darauf hingewisen, dass gegen die von der belangten Behörde  unter dem Titel „sonstige Differenzen“ erfolgte Zurechnung iHv 2%, die im Wesentlichen auf  die seitens der Beschwerdeführerin nicht lückenlos erfolgte Einbeziehung der den  Leasingnehmer treffenden Verpflichtung zum Abschluss und zur Finanzierung einer Kollisions- Kaskoversicherung in die Bemessungsgrundlage der Bestandvertragsgebühr zurückzuführen ist,  seitens der Beschwerdeführerin in der Sache keine Einwendungen erhoben wurden und auch  das BFG im Hinblick auf die diesbezügliche Rsp des VwGH (vgl zB VwGH 17.2.1994,  93/16/0160) insoweit keine Rechtswidrigkeit der gegenständlichen Bescheide zu erkennen  vermag.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_27`)


Infolge der Aufhebung des BFG-Erkenntnisses vom 29.6.2017, RV/7101082/2013, durch den  Verwaltungsgerichtshof ist das Beschwerdeverfahren wieder offen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_14`)


In der Folge hob der VwGH das Erkenntnis des BFG mit Entscheidung vom 27.3.2019 , Ra  2018/13/0024-5, wegen Rechtswidrigkeit des Inhaltes auf und führte in deren Rz 15 bis 19  dazu wörtlich wie folgt aus:  "15 Streitpunkt des Verfahrens ist vielmehr - im Rahmen der näheren Bestimmung der in § 3  Abs. 2 EStG 1988 angeordneten "Rechtsfolge" - die Frage, ob eine Hochrechnung von  Einkünften aus nichtselbständiger Arbeit, soweit sie außerhalb des Zeitraums des gleichzeitigen  steuerfreien Bezuges erzielt wurden, zu unterbleiben hat, wenn während des ganzen Jahres  Einkünfte aus nichtselbständiger Arbeit erzielt wurden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_23`)


Für die Fälle des Weiterbildungs-  oder Bildungsteilzeitgeldes ist das Bundesfinanzgericht in einer Mehrzahl neuerer  Entscheidungen, auf die im vorliegenden Fall nicht eingegangen wurde (vgl. zu einer  diesbezüglichen "Änderung der Rspr-Linie des BFG" Jakom/Laudacher EStG, 2018, § 3 Rz 122),  unter Hinweis u.a. auf das Erkenntnis vom 26. März 2003 zum gleichen Ergebnis gekommen  (vgl. aus der Zeit vor dem hier angefochtenen Erkenntnis etwa BFG 21.5.2014,  RV/5100789/2014;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_29`)


Dabei wurde auch schon hervorgehoben, dass die Berechnung  des fiktiven Jahresbetrages gemäß § 3 Abs. 2 EStG 1988 nicht so erfolgen darf, dass dies zu  einer doppelten Erfassung während des steuerfreien Bezuges weiterlaufender nicht steuerfreier  Bezugsteile führt (vgl. dazu etwa BFG 12.12.2016, RV/3100968/2016;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_35`)


Da sowohl die Höhe der vom Bf. für die Zeiträume vom 1.1.2013 bis zum 21.4.2013 und vom  9.7.2013 bis zum 31.12.2013 bezogenen zum laufenden Tarif zu versteuernden Einkünfte aus  nichtselbständiger Arbeit als auch jene der während des Bezuges des steuerfreien  Weiterbildungsgeldes bezogenen Arbeitseinkünfte weder im Lohnzettel des Bf. für das Jahr  2013 noch in den Akten des Finanzamtes und des BFG aufschien, wurde dem Finanzamt gemäß  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamt` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_36`)


§ 269 Abs. 2 BAO aufgetragen, die diesbezüglichen Beträge zu ermitteln und in der Folge dem  BFG bekannt zu geben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_37`)


In Entsprechung dieses Ermittlungsauftrages übermittelte das Finanzamt dem BFG das den Bf.  betreffende Lohnkonto 2013 sowie den Freibetragsbescheid 2013 vom 19.9.2012.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_40`)


Die auf Basis der im vorstehenden Absatz angeführten Beträge seitens des BFG gem. § 3 Abs 2,  1.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_43`)


Diese Berechnung wurde beiden Parteien mittels Ersuchens um Stellungnahme des BFG vom  13.2.2020 zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_44`)


Mit Schreiben vom 17.2.2020 teilte das Finanzamt dem BFG mit, dass es der Berechnung der  Einkommensteuer laut übermittelter Berechnung zustimme.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_45`)


Mit Schreiben vom 14.5.2020 teilte der Bf. dem BFG mit, dass dieser Berechnung nichts  hinzuzufügen sei und dass er auf die Durchführung einer mündlichen Verhandlung verzichte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_56`)


Diese sind in Ansehung des dem BFG vom Finanzamt  per E-Mail vom 27.1.2020 übermittelten Lohnkontos sowie der von diesem dort erstellten  Ausführungen wie folgt zu berechnen:  Summe 905 Freibetrag EUR 2.093,64 abzügl.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_100`)


Zur Frage, ob und wann bei gegenständlich unstrittigem Sachverhalt die Gebührenschuld  entstanden ist, liegt die obbezeichnete umfangreiche VwGH-Judikatur vor, in deren  Anwendung das BFG seine Entscheidung getroffen hat.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_117`)


b. Bei Vorliegen der Voraussetzungen ist das BFG verpflichtet, einen Antrag auf  Normenkontrolle zu stellen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_163`)


Als Sozialplan im Sinne des § 67  Abs. 8 lit. f EStG 1988 kann daher auch eine Vereinbarung zwischen Arbeitgeber und der  gesamten Belegschaft (allen Arbeitnehmern) verstanden werden, die Maßnahmen zur  Verhinderung, Beseitigung oder Milderung der nachteiligen Folgen von Betriebsänderungen im  Sinne des § 109 Abs. 1 Z 1 bis 6 des Arbeitsverfassungsgesetzes oder vergleichbarer  gesetzlicher Bestimmungen zum Inhalt hat.“  d. Auch die Anregung auf Aufhebung der Wortfolge „und Z 8“ selbst ist nach Ansicht des BFG  nicht zielführend.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_166`)


Einer derartigen Anregung würde der VfGH nach Ansicht des BFG nicht folgen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_88`)


Das BMF hat die Beschwerde mitsamt den bezugshabenden Akten dem BFG als Direktvorlage  gemäß § 262 Abs. 4 i.V.m. § 265 BAO zur Entscheidung vorgelegt und dazu im Vorlagebericht  vom 20.04.2018 Folgendes ausgeführt:    „Der Unterlage „Online Gambling in Greece“ (Anhang zum Bericht FA10 vom 20.4.2017),  erstellt von Gambling Complience (https://gamblingcompliance.com), Stand März 2015,  zufolge, befand sich die Regulierung des Online-Wett- und Glücksspielmarktes in Griechenland  in einer Übergangsphase.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `BMF` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_148`)


Das BFG hat volle Kognitionsbefugnis und daher die beschwerdegegenständliche Sache so zu  entscheiden, als ob diese Sache erstmals nach den für sie geltenden materiell-rechtlichen  Bestimmungen behandelt würde.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_149`)


Dabei ist dem BFG in Ermessensfragen eine  uneingeschränkte eigene Ermessensübung übertragen (Art. 130 Abs. 3 B-VG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_164`)


Auch das BFG beurteilt die handschriftlich, in griechischer Sprache und Schrift ausgefüllten  Formulare als Abgabenerklärungen über die Selbstbemessung der Abgaben für Online- Glückspiele und Wetten nach Art. 50 des Gesetzes 4002/2011.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_24`)


Da ändert es auch nichts, wenn im Betreff des Vorlageantrags der Name des  Bescheidadressaten, so dient dies lediglich zur Bezeichnung des Bescheides, gegen den sie sich  richtet (s. BFG 27.2.2019, RV76101073).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_32`)


Diese Beschwerde vom 20.10.2017 wurde mit Beschluss des BFG vom 6.11.2019,  GZ RV/1200003/2018 als verspätet eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_38`)


UFS 3.3.2010, RV/0071-G/10, BFG 27.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_70`)


Wie den dem BFG vorliegenden Unterlagen zu entnehmen war, wurde die Bf. mit  Erinnerungsschreiben vom 29.8.2018 über das Fehlen der Meldung der wirtschaftlichen  Eigentumer gem. § 5 WiEReG informiert.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_81`)


Aus dem angeführten Sachverhalt, der der Entscheidung des BFG zugrunde gelegt wurde, war  festzustellen, dass die Bf. der gesetzlichen Verpflichtung gem. § 5 WiEReG nicht  nachgekommen war und die Meldung nicht dem § 18 Abs. 1 WiEReG entsprechend bis zum  1.6.2018 erstattet hatte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_33`)


den ärztlichen Entlassungsbericht des  medizinischen Zentrums Bad Vigaun GmbH & Co. KG vom 09.09.2014 nach durchgeführtem  Rehabilitationsaufenthalt sowie das Sachverständigengutachten des Sozialministeriums  Service, Landesstelle Salzburg vom 01.09.2016,  II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Bei seiner Entscheidung legte das BFG folgenden Sachverhalt zugrunde, der sich aus den Akten  des Verwaltungsverfahrens und des Beschwerdeverfahrens vor dem BFG ergibt:  Mit Bescheid vom 17.10.2012 wurde die BF zur Einkommensteuer für 2011 veranlagt, mit  Bescheid vom 10.06.2013 zur Einkommensteuer für 2012, mit Bescheid vom 19.11.2014 zur  Einkommensteuer für 2013 und mit Bescheid vom 20.07.2015 zur Einkommensteuer für 2014.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bad Vigaun GmbH & Co. KG` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_44`)


Das BFG sieht mit Ritz (Ritz, BAO6, § 274, Tz 5) im Anbot von Beweisen in einer mündlichen  Verhandlung in der Beschwerde bzw. im Vorlageantrag einen Antrag auf Durchführung einer  mündlichen Verhandlung vor dem Einzelrichter.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_53`)


Dies hat die BF im gegenständlichen Beschwerdeverfahren im Verfahren vor  dem BFG über nochmaligen Vorhalt durch die Vorlage des von der BF angeführten Gutachtens  des medizinischen Sachverständigen und die verschiedene weitere Unterlagen erfüllt.  Gemäß § 35 Abs. 1 EStG steht der Steuerpflichtigen bei einer außergewöhnlichen Belastung  durch eine eigene körperliche … Behinderung unter bestimmten weiteren Voraussetzungen ein  Freibetrag zu, der sich nach § 35 Abs. 3 EStG am Ausmaß der Behinderung orientiert und der  bei einer festgestellten Behinderung von 25% bis 34% mit € 75,00 p.a. bemisst.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_135`)


Mit Eingabe vom 29. Jänner 2018 stellte die Bf. nach Verlängerung der Vorlagefrist den Antrag,  die Bescheide über die Festsetzung der Forschungsprämie für eigenbetriebliche Forschung und  experimentelle Entwicklung der Jahre 2011 und 2012 dem BFG zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_192`)


Das BFG geht von folgendem Sachverhalt aus:  - Die Bf. hat mit Eingabe vom 20. Mai 2012 eine Forschungsprämie für das Wirtschaftsjahr  2011 i.H.v. € 24.491,36 beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_233`)


- Am 29. Jänner 2018 stellte die Bf. (nach Verlängerung der Rechtsmittelfrist) den Antrag auf  Entscheidung u.a. hinsichtlich des Bescheides betreffend Festsetzung der Forschungsprämie für  eigenbetriebliche Forschung und experimentelle Entwicklung u.a. betreffend das Jahr 2011 an  das BFG.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_246`)


Die Darstellung im Vorlageantrag an das BFG wurde teilweise wiederholt.   Die Bf. erläutert, dass sie als start-up das mit dem Ziel der Entwicklung einer neuartigen  Trocknungsanlage gegründet wurde und gemeinsam mit professionellen Forschungs- und  Anlagefirmen Pilotanlagen und Prototypen entwickelt und Probetrocknungen durchgeführt  hat.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_262`)


so lange einzubinden sein, bis die gutachterliche  Stellungnahme der FFG als ausreichend schlüssig und nachvollziehbar anzusehen ist (vgl. BFG  27. November 2014, RV/3100966/2014).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_288`)


Gleiches gilt auch für Begründungen des BFG.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_313`)


Die gegenteilige Darstellung der Bf. im Vorlageantrag vom 29. Jänner 2018 ist für das BFG nicht  nachvollziehbar.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_360`)


Aus Sicht des BFG wurde in der nunmehr zweiten Stellungnahme des FFG vom 20. April 2018  ausreichend geklärt bzw. begründend dargestellt, aus welchem Grund die Tätigkeiten der Bf.  nicht begünstigungsfähig i.S.d. § 108c Abs. 2 Z 1 EStG 1988 sind.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_367`)


Das BFG schließt sich in freier Beweiswürdigung (§ 167 Abs. 2 BAO) der Beurteilung der FFG  an.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_85`)


7. Zufolge der Aufhebung durch den VwGH hat nunmehr das Bundesfinanzgericht (BFG) im  fortgesetzten Verfahren über die gegen den Festsetzungsbescheid betr.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_43`)


Über die Beschwerde wurde erwogen:  1. Zuständigkeit des Bundesfinanzgerichtes (BFG)

**False Positives:**

- `BFG` — partial — pred is substring of gold: `Bundesfinanzgerichtes (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_34`)


Die Abgabenbehörde legte die Beschwerde mit Vorlagebericht vom 12.11.2019 dem  Bundesfinanzgericht (BFG) zur Entscheidung vor.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

</details>

---

## `Bundesminister_Arbeit` 

**F1:** 0.003 | **Precision:** 0.958 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `07e5a87e`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' (genitive form).

**Content:**
```
\bBundesministers\s+f\u00fcr\s+Arbeit,?\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.958 | 0.001 | 0.003 | 24 | 23 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 1 | 16892 |

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

## `AMS_Organization` 

**F1:** 0.006 | **Precision:** 0.946 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `590b92b3`  
**Description:**
Matches 'AMS' (Arbeitsmarktservice) as an organization.

**Content:**
```
\bAMS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.946 | 0.003 | 0.006 | 56 | 53 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 53 | 3 | 16936 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_141`)


Somit kommt § 16 Abs. 2 EStG  gegenüber § 295a BAO der Vorrang zu.  Das Finanzamt hat im bekämpften Bescheid vom 10. September 2019 zu Recht auch keine  Werbungskosten gemäß § 16 Abs. 2 EStG 1988 für Rückzahlung von  „AMS-Geldern“ im Wege  der Legalzession  berücksichtigt:  Bf bezog  zwar vom 1.1.2016 bis 10.2.2016 für 41 Tage Notstandshilfe vom Arbeitsmarktservice  in Höhe von 1.148,41€.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

- `Finanzamt` (organisation)
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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

## `BFH_entities` 

**F1:** 0.011 | **Precision:** 0.933 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `0e58f673`  
**Description:**
Matches the specific abbreviation BFH (Bundesfinanzhof) as an organization.

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.005 | 0.011 | 104 | 97 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 97 | 7 | 17377 |

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

**Missed by this rule (FN):**

- `BFG` (organisation)

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
- `BFG` (organisation)

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

**Missed by this rule (FN):**

- `BFG` (organisation)

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

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)
- `Verwaltungsgerichtshof` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `BFG` (organisation)

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

## `Finanzamt_Locations_Fixed` 💣

**F1:** 0.361 | **Precision:** 0.927 | **Recall:** 0.224  

**Format:** `regex`  
**Rule ID:** `b800ef63`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by specific valid locations or 'Österreich', preventing matches on random numbers or dates.

**Content:**
```
\bFinanzamt(?:es)?(?:\s+(?:Amstetten(?:\s+Melk(?:\s+Scheibbs)?)?|Kufstein(?:\s+Schwaz)?|St\.?\s*Johann(?:\s+Tamsweg(?:\s+Zell\s+am\s+See)?)?|Braunau(?:\s+Ried(?:\s+Schärding)?)?|Grieskirchen(?:\s+Wels)?|Wien(?:\s+\d+(?:/\d+)*\s*(?:Schwechat\s+Gerasdorf)?)?|Spittal\s+Villach|Steiermark\s+Mitte|Tirol\s+Ost|Gmunden\s+Vöcklabruck|Lilienfeld\s+St\.?\s*Pölten|Baden(?:\s*Mödling)?|Österreich|Salzburg-Stadt|Feldkirch|Hollabrunn\s+Korneuburg\s+Tulln|Gmunden\s+Vöcklabruck|Lilienfeld\s+St\.?\s*Pölten|Baden(?:\s*Mödling)?|f\u00fcr\s+(?:Geb\u00fchren|Verkehrsteuern|Gl\u00fccksspiel|Sonstige\s+Abgaben|Gro\u00dfbetriebe)))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.927 | 0.224 | 0.361 | 4360 | 4040 | 320 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4040 | 320 | 13957 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_5`)


Verfahrensgang: Mit Antrag, datiert mit 27. Feber 2012, beim Finanzamt eingebracht am 1. März 2012, begehrte der besachwaltete Antragsteller durch seine Sachwalterin die Gewährung der "erhöhten Familienbeihilfe" im Eigenbezug.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_7`)


Dieser Antrag wurde vom Finanzamt mit Bescheid vom 9. März 2012 abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_14`)


Das Finanzamt legte die Berufung dem Unabhängigen Finanzsenat im September 2012 ohne Erlassung einer Berufungsvorentscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_37`)


Dennoch hat das Finanzamt sowohl die Familienbeihilfe als auch den Erhöhungsbetrag wegen erheblicher Behinderung gewährt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_51`)


Ein Widerspruch, den aufzuklären Aufgabe des Finanzamtes gewesen wäre und der auch Zweifel an der Qualität der Begutachtungen und Bescheinigungen hervorruft.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Zeno Matyssek` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache QZKX Beratung, Lambacher Straße 9, 3123 Mittermerking, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 45-817/1493  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Lilienfeld St. Pölten` | `Finanzamtes Lilienfeld St. Pölten` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `M.` (person)
- `QZKX Beratung` (organisation)
- `Lambacher Straße 9, 3123 Mittermerking, Österreich` (address)
- `Mag. Dieter Walla & Partner Steuerberater OG` (organisation)
- `45-817/1493` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn QZKX Beratung,  nunmehr QZKX Beratung (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Lilienfeld St. Pölten` | `Finanzamtes Lilienfeld St. Pölten` |

**Missed by this rule (FN):**

- `QZKX Beratung` (organisation)
- `QZKX Beratung` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_9`)


Das Finanzamt hat die Berufung ohne Erlassung einer Berufungsvorentscheidung an den  Unabhängigen Finanzsenat vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_23`)


Beschwerdeerwägungen:  Dem angefochtenen Bescheid über die Festsetzung von Anspruchszinsen 2007 liegt der im  Einkommensteuerbescheid 2007 des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013  ausgewiesene Differenzbetrag von € 254.913,99 zugrunde.

| Predicted | Gold |
|---|---|
| `Finanzamtes Lilienfeld St. Pölten` | `Finanzamtes Lilienfeld St. Pölten` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Eingabe vom 17.01.2019 an das Finanzamt begehrte der Bf die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer und Einkommensteuer 2016.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_15`)


Das Finanzamt wies die Anträge auf Wiederaufnahme der Verfahren betreffend  Einkommensteuer und Umsatzsteuer 2016 mit Bescheiden vom 25.03.2019 ab, mit der  Begründung, dass angeforderte Unterlagen nicht beigebracht worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_18`)


Mit Beschwerdevorentscheidung vom 02.09.2019 - Berichtigung des Spruches mit Bescheid  vom 13.09.2018 - wies das Finanzamt die Beschwerden ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_21`)


Der Bf führte begründend aus, dass er im Jahr 2016 in Kroatien und dann in Deutschland  gewesen sei, sodass er die Steuererklärungen nicht rechtzeitig dem Finanzamt vorlegen  konnte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_5`)


Bei der Veranlagung akzeptierte das Finanzamt lediglich Werbungskosten in Höhe von 215,94 €  (Sonstige Werbungskosten: Internet 50 % PA) (Bescheid vom 14.5.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_6`)


Gegen diesen Bescheid erhob die Beschwerdeführerin mit Schriftsatz vom 23.5.2019  (eingelangt beim Finanzamt am 27.5.2019) Beschwerde, legte eine Befürwortung des  Dienstgebers hinsichtlich der getätigten Fortbildungsmaßnahmen vor und beantragte die  Aufhebung des oben genannten Bescheides und eine entsprechende Neuveranlagung unter  Berücksichtigung der Werbungskosten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_8`)


Mit Beschwerdevorentscheidung vom 21.8.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_12`)


Mit Vorlagebericht vom 7.10.2019 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_9`)


Bei einer Befragung am 8.3.2007 hat der Bf beim Finanzamt Folgendes zu Protokoll gegeben:   "Zum Fahrzeug: Es handelt sich um einen XX mit dem Kennzeichen XY, Baujahr 2005.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_34`)


Im Rahmen der Erhebungen wurden dem Finanzamt mit Schreiben vom 27.3.2007 ua.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_52`)


3. Mit Bescheid vom 22.3.2010, StrNr, hat das Finanzamt – neben der NoVA - die Umsatzsteuer  für den Erwerb eines neuen Fahrzeuges für den Zeitraum August 2005 festgesetzt;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_54`)


Begründend führte das Finanzamt aus, der Bf sei seit 2.8.1991 mit Nebenwohnsitz in Adr1,  gemeldet, wo auch seine Gattin und die Kinder mit Hauptwohnsitz gemeldet seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_65`)


In der dagegen rechtzeitig erhobenen Berufung wird im Wesentlichen eingewendet,  hinsichtlich der nun erstmaligen Festsetzung der Umsatzsteuer für August 2005 sei bereits mit  31. Dezember 2008 Verjährung eingetreten, da die Umsatzsteuer als Verkehrssteuer nach drei  Jahren verjähre und keine entsprechenden Verlängerungshandlungen (erkennbare  Amtshandlungen) seitens des Finanzamtes gesetzt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_71`)


Wenn das Finanzamt in Zusammenhalt mit der Umsatzsteuer einen 20%igen Abschlag von der  Bemessungsgrundlage vornehme, welcher Wert einem Fahrzeug mit über 6.000 km  entspreche, so gehe es offenbar von einem gebrauchten Fahrzeug aus.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_73`)


Feststellungen des Finanzamtes, dass der Bf das Fahrzeug als neues Fahrzeug erworben habe  und wann dieses nach Österreich verbracht worden sei, fehlten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_77`)


RV/0506-I/10, der  Berufung hinsichtlich der Umsatzsteuer Folge gegeben, den Bescheid in diesem Umfang  aufgehoben und begründend ausgeführt, beim berufungsgegenständlichen Fahrzeug habe es  sich insofern um ein Gebrauchtfahrzeug gehandelt, als das Finanzamt selbst im Hinblick auf  den für ein benütztes Fahrzeug vorgenommenen Abschlag von 20 % ausgegangen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_79`)


6. Aufgrund einer vom Finanzamt dagegen erhobenen Amtsbeschwerde hat der  Verwaltungsgerichtshof mit Erkenntnis vom 19.4.2016, 2013/15/0288, die vorgenannte UFS-

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_82`)


auf die in Art. 1 Abs. 9 UStG 1994 genannten  Tatbestandsvoraussetzungen - aus, dass die vom Finanzamt zugrunde gelegte  4 von 15 Seite 5 von 15

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_132`)


Laut Erhebungen des Finanzamtes zu dem an der inländischen Wohnadresse abgestellten  Fahrzeug hatte sich der Bf im Zeitraum vom 1. bis 12. Februar 2007 an 7 Tagen zu  unterschiedlichsten Zeiten am Familienwohnsitz aufgehalten (Mitteilung der Steuerfahndung  vom 27.3.2007).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_148`)


Wie aus den eigenen Angaben des Bf bei seinem Erstkontakt mit dem Finanzamt im Zuge der  Ermittlungen zu allfällig in Österreich bestehenden Abgabepflichten in Zusammenhang mit  seinem Fahrzeug hervorgeht, wurde das Fahrzeug für die Fahrt zur Arbeit und zum Besuch der  Familie in Adr1 verwendet;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_188`)


Gibt der Erwerber  die Steueranmeldung nicht ab oder erweist sich die Selbstberechnung als nicht richtig, so kann  das Finanzamt die Steuer festsetzen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_201`)


Nach der Rechtsprechung des VwGH ist es zulässig, dass das Bundesfinanzgericht den dem  Erstbescheid zugrunde gelegten Sachverhalt rechtlich anders würdigt als das Finanzamt und  den Zeitpunkt der Entstehung der Steuerschuld anders ansetzt (vgl. VwGH vom 11.9.2014,  2013/16/0156, zur Änderung des Zeitraumes bei einer Normverbrauchsabgabe;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_205`)


Das Finanzamt hatte  am 22.3.2010 die Umsatzsteuer für das im Jahr 2005 vom Bf erworbene Fahrzeug festgesetzt,  weshalb die Festsetzung innerhalb der Verjährungsfrist erfolgte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_227`)


Der maßgebliche Sachverhalt, den das Finanzamt im Bescheid über die Festsetzung der  Umsatzsteuer für den Erwerb neuer Fahrzeuge (Fahrzeugeinzelbesteuerung) vom 22.3.2010  einer Fahrzeugeinzelbesteuerung unterworfen hat, ist die nicht erfolgte Erwerbsbesteuerung  des Fahrzeuges XX mit der Fahrgestellnummer 123xx in Österreich durch den  Beschwerdeführer.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_228`)


Das Finanzamt hat die Umsatzsteuer für den Zeitraum August 2005 festgesetzt, zu diesem  Zeitpunkt konnte der Bf jedoch noch nicht wie ein Eigentümer über das Fahrzeug verfügen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klarissa Kümml` (person)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_6`)


Am 11. Jänner 2016 erfolgte beim Finanzamt eine anonyme Anzeige.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_8`)


Dieses  Zusatzeinkommen habe der Bf. beim Finanzamt nicht erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_11`)


Begründend führte das Finanzamt jeweils  aus, Ermittlungen hätten ergeben, dass der Bf. entgegen seiner Abmeldung im Zentralen  Melderegister am 10. Dezember 2013 weiterhin bis zum 1. Dezember 2015 einen Wohnsitz in  Österreich (x2x Ort2, Straße 2) gehabt habe und somit während des streitgegenständlichen  Zeitraums in Österreich gewesen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_68`)


Ihm sei es unverständlich, dass er dem Finanzamt seine  Krankengeschichte übermitteln sollte, was seine persönliche Angelegenheit sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_136`)


Trotz Aufforderung legte der Bf. diesbezüglich dem Finanzamt weder Unterlagen zum  Beschäftigungsausmaß noch zur Höhe der Einkünfte (wie z.B. AHV – Auszug) vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_143`)


Das Finanzamt hat, nachdem der Bf. die  Einkünfte nicht nachwies oder bezifferte, diese griffweise mit monatlich CHF 2.000,00 (jährlich  CHF 24.000,00) geschätzt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_15`)


Diätanforderung nicht notwendig und die damit verbundenen Kosten nicht zu berücksichtigen  seien bzw. ob das Finanzamt auch die Arztbriefe mit dem Behandlungsverlauf erhalte, damit  die Diätverpflegung Relevanz bekomme.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_17`)


Mit Schreiben vom 05.12.2018 legte das Finanzamt die Rechtslage dar und hielt der  Beschwerdeführerin vor, dass sie abweichend von den Pauschalsätzen Kosten für die  Beschaffung von Lebensmitteln geltend mache, welche bestimmte Anforderungen erfüllen  würden (Biolebensmittel, glutenfrei, Gemüse), aus deren Artikelbezeichnung aber keinesfalls  geschlossen werden könne, dass sie ausschließlich wegen der bestehenden Behinderung  konsumiert werden müssten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_24`)


Gleichzeitig werde aber vom  Finanzamt gefordert, gerade diese Mehraufwendungen zu errechnen, weil ein Abzug von  normalen Kosten der Lebensführung nach den Bestimmungen des § 20 EStG nicht möglich ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_28`)


Die Beschwerdeführerin könne natürlich feststellen, dass das Finanzamt keine ärztliche  Expertise erstellen könne, welche Lebensmittel ursächlich mit der Krankheit in Zusammenhang  stünden und welche Kosten tatsächlich durch die Krankheit und nicht durch den normalen  Lebensunterhalt verursacht würden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_31`)


Mit Schreiben vom 18.12.2018 nahm die Beschwerdeführerin zum Ergänzungsersuchen des  Finanzamtes vom 05.12.2018 wie folgt Stellung: Es sei Zeit gewesen, aus 151 Kassazetteln  einzelne Posten herauszulesen und zu hinterfragen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_40`)


Die Beschwerdeführerin werde niemals zu einem Arzt gehen, um ihn befinden zu lassen, ob die  einzelnen Medikamente und Lebensmittel, die seitens des Finanzamtes in Frage gestellt  würden, mit ihrer Behinderung in Zusammenhang stünden oder nicht.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_44`)


Für die Art der Kommunikation, wie die Beschwerdeführerin sie vom Finanzamt erfahre, habe  offensichtlich nur ein Finanzamt Zeit und Geld zur Verfügung.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_46`)


Mit Beschwerdevorentscheidung vom 10.01.2019 wies das Finanzamt die Beschwerde als  unbegründet ab, beließ den Erstbescheid unverändertund führte begründend aus:  „Nach den Bestimmungen des § 35 EStG steht einem Steuerpflichtigen jeweils ein Freibetrag für  außergewöhnliche Belastungen durch eine eigene körperliche oder geistige Behinderung zu.  Diese Pauschalsätze sind im Abs. 3 dieser Bestimmung geregelt und betragen bei einer in Ihrem  Fall festgestellten Behinderung von 30 % € 75,-.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_57`)


Es gab  somit im Ermittlungsverfahren für das Finanzamt keine Möglichkeit, den tatsächlich durch Ihre  Behinderung verursachten Mehraufwand für die Diätverpflegung festzustellen, sodass nur der  bereits im Erstbescheid berücksichtigte Pauschalbetrag für die Diätverpflegung als steuerliche  Abzugspost anerkannt werden konnte.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_66`)


Dem Finanzamt seien sämtliche von Ärzten des  Krankenhauses KH erstellte Diagnosen vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_71`)


Sie könne von  keinem Arzt erwarten, dass er die von ihm verschriebenen Medikamente des Jahre 2017 für  das Finanzamt auflisten und sich und die Beschwerdeführerin damit vor dem Finanzamt  rechtfertigen würde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_74`)


Mit Vorlagebericht vom 21.06.2019 legte das Finanzamt die Beschwerdesache dem  Bundesfinanzgericht vor und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_78`)


Im angefochtenen Einkommensteuerbescheid 2017 berücksichtigte das Finanzamt das  Pauschale für Mehraufwendungen wegen Krankendiätverpflegung von 840,00 € und den  Freibetrag von 75,00 € für eine Behinderung zwischen 25 und 34 %.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_112`)


Darüber wurde die  Beschwerdeführerin vom Finanzamt wiederholt aufgeklärt und zum entsprechenden Nachweis  aufgefordert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_121`)


Der monatliche Pauschbetrag von  70,00 € (840,00 €/Jahr) steht daher unbestritten zu.  Dass die Beschwerdeführerin einen tatsächlichen, außergewöhnlichen  Verpflegungsmehraufwand, der über die ohnehin vom Finanzamt anerkannten Mehrkosten in  Höhe des in der Verordnung genannten Betrages von 840 Euro, hinausgeht, wurde nicht  nachgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_122`)


Vom Finanzamt wurde im Erstbescheid irrtümlich zusätzlich zu diesem  Pauschale ein Betrag von 285,98 € für glutenfreie Lebensmittel berücksichtigt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_123`)


Aus der  Bescheidbegründung ist eindeutig erkennbar, dass auch das Finanzamt die zutreffende  Rechtsmeinung vertritt, wonach über den Pauschalbetrag hinaus mangels entsprechender  Beweise keine Aufwendungen berücksichtigt werden können.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_124`)


In Zusammenhang mit den geltend Kosten in Höhe von 836,94 € für Medikamente,  Rezeptgebühren, Behandlungskosten und Arzthonoraren ist in Ergänzung der Ausführungen  des Finanzamtes Folgendes auszuführen:   Gemäß § 4 der VO für außergewöhnliche Belastungen sind Kosten der Heilbehandlung im  nachgewiesene Ausmaß ohne Selbstbehalt zu berücksichtigen, sofern sie mit der Behinderung  in Zusammenhang stehen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_139`)


Die Beschwerdeführerin wurde vom Finanzamt zu einer entsprechenden Beweisführung  aufgefordert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_47`)


Zum weiteren Vorhalt, dass aus den vorgelegten Einbringungsakten  des FA nicht ersichtlich sei, welcher KöSt Bescheid dem Haftungsbescheid beigelegt wurde, da  überhaupt keine Kopien vorhanden sind, führte der Vertreter des Finanzamtes aus, dass dies  für ihn nicht mehr nachvollziehbar ist.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_8`)


Verfahrensgang  Der Beschwerdeführer (in weiterer Folge kurz BF) reichte am 13.02.2019 elektronisch über  FinanzOnline die Erklärung zur Arbeitnehmerveranlagung für 2018 beim Finanzamt ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_9`)


Mit einem Ersuchen um Ergänzung vom 27.08.2019 wurde der BF vom Finanzamt aufgefordert,  hinsichtlich der beantragten Kosten für Familienheimfahrten verschiedenste Fragen zu  beantworten und entsprechende Nachweise vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_12`)


Am 22.10.2019 erging der Einkommensteuerbescheid 2018, wobei vom Finanzamt die  beantragten Kosten für Familienheimfahrten nicht anerkannt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_14`)


Mit Beschwerdevorentscheidung vom 06.02.2020 wurde die Beschwerde vom Finanzamt als  verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_16`)


In der Begründung wurde ausgeführt, dass  die 4-wöchige Frist dem BF bewusst gewesen sei und er deshalb telefonisch beim Finanzamt  um eine 1-wöchige Verlängerung gebeten und diese auch telefonisch von einem Mitarbeiter  des Finanzamtes bewilligt bekommen habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamtes` | `Finanzamtes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_17`)


Am 15.06.2020 wurde die Beschwerde vom Finanzamt dem Bundesfinanzgericht zur  Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_20`)


Mit Postaufgabedatum 25.11.2019 brachte der BF eine Beschwerde gegen den  Einkommensteuerbescheid 2018 ein, welche mit Beschwerdevorentscheidung des Finanzamtes  vom 06.02.2020 als verspätet zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_24`)


Die obigen Sachverhaltsfeststellungen sind allesamt aktenkundig und ergeben sich aus den  vom BF und vom Finanzamt vorgelegten Unterlagen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_25`)


Ob eine vom BF behauptete telefonische  Verlängerung der Beschwerdefrist durch einen Mitarbeiter des Finanzamtes stattgefunden hat,  ist aus den unter „4. Rechtliche Beurteilung“ angeführten Gründen nicht relevant.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_53`)


Da im gegenständlichen Fall die vom BF behauptete Beschwerdefristverlängerung, so sie denn  stattgefunden hat, nur telefonisch zwischen dem Finanzamt und dem BF "vereinbart" wurde,  lag damit aber kein vor Ablauf der Beschwerdefrist im Sinne des § 245 Abs 3 iVm § 85 BAO  wirksam gestellter Antrag auf Erstreckung der Beschwerdefrist vor und konnte solcherart auch  der Lauf der Beschwerdefrist nach § 245 Abs 3 zweiter Satz BAO nicht gehemmt werden  (VwGH 17.11.2005, 2001/13/0279).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_28`)


Im Einkommensteuerbescheid für das Jahr 2016 anerkannte das Finanzamt die Aufwendungen  unter Anrechnung eines Selbstbehaltes in gleicher Höhe, sodass die geltend gemachten Kosten  2 von 6 Seite 3 von 6

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_72`)


Die im Zusammenhang mit der Behinderung der Tochter T stehenden Aufwendungen wurden  vom Finanzamt zu Recht als außergewöhnliche Belastung mit Selbstbehalt anerkannt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_7`)


1. Verfahrensgang, Sachverhalt  Das Finanzamt (kurz FA) erließ den bekämpften Einkommensteuerbescheid mit 8. Juli 2019  weitestgehend erklärungsgemäß, reduzierte allerdings die von der Beschwerdeführerin (kurz  Bf.) als außergewöhnliche Belastung ohne Abzug eines Selbstbehaltes in Anspruch  genommenen Zahlungen um EUR 1.854,71.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_53`)


Vom Finanzamt (kurz FA) wurden EUR 4.766,81  für Begräbniskosten für den verstorbenen Vater (Nachlassüberschuldung) erklärungsgemäß  anerkannt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_97`)


Das Bundesfinanzgericht hat – wie auch das Finanzamt - die abgabepflichtigen Fälle zu  erforschen und von Amts wegen die tatsächlichen und rechtlichen Verhältnisse zu ermitteln,  die für die Abgabepflicht und die Erhebung der Abgaben wesentlich sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_99`)


Eine in der Begründung einer Beschwerdevorentscheidung getroffene Feststellung des  Finanzamtes wirkt wie ein Vorhalt und es obliegt dem Abgabepflichtigen, die vom Finanzamt in  der Begründung der Beschwerdevorentscheidung getroffene Feststellung zu widerlegen bzw.  zumindest deren Unrichtigkeit zu behaupten (vgl. VwGH 8.10.1985, 83/14/0237 etc.).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Nadja Rossetto` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Imre & Schaffer Rechtsanwälte OG` (organisation)
- `85-716/2059` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 29.5.2018 wandte sich das Finanzamt an den Beschwerdeführer (Bf.) als  verantwortlichen Geschäftsführer der GmbH, weil es die Geltendmachung der  abgabenrechtlichen Haftung nach § 9 iVm.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_14`)


3. Da die unter Punkt 1 angeführten Abgabenbeträge während Ihrer Vertretungsperiode fällig  bzw. nicht entrichtet wurden, muss das Finanzamt bis zum Beweis des Gegenteils davon  ausgehen, dass Sie der Ihnen aufgetragenen Erfüllung der abgabenrechtlichen Pflichten der  Vertretenen nicht vorschriftsgemäß nachgekommen sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_24`)


Im Fall  der Nichterbringung dieser Nachweise muss das Finanzamt davon ausgehen, dass Sie die Ihnen  obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwalteten Mitteln zu  entrichten, schuldhaft verletzt haben, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_26`)


6. Wird der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liegt es im Ermessen des Finanzamtes, die Haftung für die unter Punkt 1 genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_28`)


Pflichtverletzung allfällige Einzelinteressen verdrängt (z.B. VwGH 10.10.2005, 2004/14/0112),  sähe sich das Finanzamt veranlasst, die gesetzliche Vertreterhaftung gegen Sie im  erforderlichen Ausmaß geltend zu machen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_87`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_88`)


Nach der durch das  Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.1.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` | `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rainer Leutheußer` (person)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich` (address)
- `Egger & Freidorfer Steuerberatungs-OG` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_6`)


Im Zuge des Ermittlungsverfahrens durch das Finanzamt legte der Bf. das Anlagenverzeichnis  2014, die Aufgliederung der „Sonstigen Werbungskosten 2014“, die Aufgliederung der  Bürokosten 2014, der Reisekosten 2014 für Anwaltstermine in Graz und der Zahlungen an den  Anwalt in einer Gesamthöhe von € 30.433,50 vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_8`)


In einem weiteren Ergänzungsersuchen teilte das Finanzamt mit, dass Kosten eines  Zivilprozesses nur dann als Werbungskosten abzugsfähig seien, wenn der Prozessgegenstand  objektiv betrachtet mit den Einkünften aus nichtselbständiger Arbeit im Zusammenhang  stünde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_9`)


Für eine diesbezügliche Beurteilung ersuchte das Finanzamt um entsprechende  Unterlagen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Bährs`(person)
- `Univ.-Prof.in Rachel Darnieder`(person)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chen Petermüller`(person)
- `Sand 5, 4851 Hehenberg, Österreich`(address)
- `Anka Vrcic`(person)
- `Finanzamtes Salzburg-Land`(organisation)
- `20-238/1198`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  für Gebühren` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Florenzia Claußing`(person)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich`(address)
- `Finanzamtes`(organisation)
- `10-95-558/8694`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Freistadt Rohrbach Urfahr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Wendy Scherl`(person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `53-864/4798`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)
- `Corazza Kocholl Laimer Rechtsanwälte OG`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien 12/13/14 ` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miroslav Hankel, BEd`(person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Feichtenschlager`(person)
- `Daisy Wegelein`(person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `61-004/6209`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers Emma Türker, Frauenhofenstraße 13, 5132 Gasteig, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Emma Türker`(person)
- `Frauenhofenstraße 13, 5132 Gasteig, Österreich`(address)
- `Finanzamtes Linz`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Alma Gaedecke, Höbelgasse 24, 9400 St. Thomas, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien  1/23 ` — partial — gold is substring of pred: `Finanzamtes Wien  1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alma Gaedecke`(person)
- `Höbelgasse 24, 9400 St. Thomas, Österreich`(address)
- `Finanzamtes Wien  1/23`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Matthäus Domrös`(person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Dr. Gerlinde  Rieser`(person)

</details>

---

## `Wiener_Gemeinderat` 💣

**F1:** 0.006 | **Precision:** 0.891 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `b7bc1d86`  
**Description:**
Matches Wiener Gemeinderat as an organization.

**Content:**
```
\bWiener\s+Gemeinderat(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.891 | 0.003 | 0.006 | 64 | 57 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 57 | 7 | 16476 |

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
- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)

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

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_118`)


Der Wiener Gemeinderat hat mit Verordnung (ABl. 1994/07, 7.2.1994) den  Hebesatz der Grundsteuer mit 500 vH (von Hundert = %) festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderat` | `Wiener Gemeinderat` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/144541.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144541.1_50`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_125`)


Damit hat die Gemeinde Wien durch den Wiener Gemeinderat im Rahmen der Ermächtigung  die Parkometerabgabe grundsätzlich für die gesamte Dauer des Abgestelltseins eines  mehrspurigen Kraftfahrzeuges während der zeitlichen Geltung einer Kurzparkzone  ausgeschrieben, folglich ab der ersten Minute und für jede Minute des Abgestelltseins  während der zeitlichen Geltung der Kurzparkzone (idR werktags von Montag bis Freitag und  von 9 bis 22 Uhr).

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderat` | `Wiener Gemeinderat` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_191`)


Dies alles trifft hier  zu. Das Vorbringen des Beschwerdeführers, dass er sich vorbehalte, auf die materielle  Rechtmäßigkeit der Organstrafverfügungen einzugehen („Dauer, Ausladen von Gegenständen“)  ist kein Anlass, von Amts wegen eine Verhandlung durchzuführen, weil – wie bereits  dargestellt wurde – die Ausschreibung der Parkometerabgabe durch den Wiener Gemeinderat   für die gesamte Abstelldauer innerhalb der zeitlichen Geltung der Kurzparkzone erfolgt  ist, sodass die Dauer des Abgestelltseins des Fahrzeuges nicht relevant ist,   und ohne Ausnahme für die Durchführung einer Ladetätigkeit erfolgt ist, sodass das  Ausladen von Gegenständen nicht relevant ist.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderat` | `Wiener Gemeinderat` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/145249.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145249.1_84`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_76`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/146379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146379.1_80`)


§ 4. Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung):   (1) Wird die Abgabe in pauschaler Form (§ 2 und § 3 Abs. 1) entrichtet, hat dies durch  Einzahlung des Abgabenbetrages in bar oder nach Maßgabe der der Abgabenbehörde zur  Verfügung stehenden technischen Mittel im bargeldlosen Zahlungsverkehr zu erfolgen.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_8`)


Die Vorschreibung erfolgte gemäß § 203 BAO iVm § 1 Abs. 4 und 5 Parkometergesetz 2006 bzw  §§ 2 und 5 Abs. 2 Parkometerabgabeverordnung des Wiener Gemeinderates.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_10`)


Gemäß § 5 Abs.  2 der Parkometerabgabeverordnung des Wiener Gemeinderates, ABI. für Wien Nr. 51/2005, in  der jeweils gültigen Fassung, ist für jedes mehrspurige Kraftfahrzeug, das in einem Gebiet  abgestellt wird, für das eine Abgabepflicht besteht, bei Beginn des Abstellens eine Abgabe zu  entrichten.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_37`)


Gemäß § 5 Abs. 2 der  Parkometerabgabeverordnung des Wiener Gemeinderates entsteht die Abgabepflicht bereits  bei Beginn des Abstellens.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/147279.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147279.1_39`)


Gemäß § 5 Abs. 2 der Parkometerabgabeverordnung des Wiener Gemeinderates, ABl. für Wien  Nr. 51/2005, in der geltenden Fassung, sind zur Entrichtung der Abgabe der Lenker, der Besitzer  und der Zulassungsbesitzer zur ungeteilten Hand verpflichtet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_63`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_90`)


dauernd ausschließlicher Nutzer eines Kraftfahrzeugs ist, der nachweist, dass er ein  Dauerschuldverhältnis (insbesondere Leasingvertrag oder Mietvertrag) über einen Zeitraum  von mindestens 4 Monaten hat oder nachweist, dass ihm ein arbeitgebereigenes oder von  seinem Arbeitgeber geleastes Kraftfahrzeug zur Privatnutzung überlassen wird.“  § 4 Abs 1 und 2 der Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung) normiert [Hervorhebungen durch das  Gericht]:  „(1) Wird die Abgabe in pauschaler Form (§ 2 und § 3 Abs. 1) entrichtet, hat dies durch  Einzahlung des Abgabenbetrages in bar oder nach Maßgabe der der Abgabenbehörde zur  Verfügung stehenden technischen Mittel im bargeldlosen Zahlungsverkehr zu erfolgen.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149088.1_79`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_64`)


Gründe zur Zurückweisung des Antrages, z.B. wegen entschiedener Sache (res iudicata), wegen  Unzulässigkeit des öffentlich-rechtlichen Rechtsweges oder wegen Verspätung, kann ich nicht  erkennen:   Aus folgenden Gründen betrifft der Antrag vom 28.4.2020 eine öffentlich-rechtlich  (hoheitlich) zu vollziehende Angelegenheit, sodass der Antrag richtigerweise an den  Magistrat der Stadt Wien, welcher eine Behörde ist, gerichtet wurde:  Es handelt sich hier um eine Angelegenheit der Parkometerabgabe, welche vom Wiener  Gemeinderat mit der Parkometerabgabeverordnung Abl.

**False Positives:**

- `Wiener  Gemeinderat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/140939.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140939.1_65`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), sind  Parkscheine nach dem Muster der Anlagen oder elektronische Parkscheine zu verwenden (§ 1  Wiener Kontrolleinrichtungenverordnung).

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_236`)


Gemäß § 12 und § 18 GrStG sowie gemäß § 192, § 194 Abs. 3 und § 195 BAO sowie gemäß § 8  des Wiener Grundsteuerbefreiungsgesetzes sowie gemäß der Verordnung des Wiener  Gemeinderates (ABl 1994/07, 7.2.1994), mit der der Hebesatz für die Grundsteuer festgesetzt  wird, ist die Grundsteuer für die gegenständliche Liegenschaft mit einem Jahresbetrag von  82,79 € aufgrund folgender Bemessungsgrundlagen vorzuschreiben:   Grundsteuermessbetrag in Höhe von 165,92 €,   Hebesatz im Ausmaß von 500 vom Hundert (=500%) sowie   die Befreiung von der Grundsteuer im Ausmaß von 90,02%.

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/144644.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144644.1_121`)


Somit ist die Gemeinde Wien ermächtigt, mittels Beschlusses der Gemeindevertretung (Wiener  Gemeinderat) für die gesamte Dauer des Abgestelltseins eines mehrspurigen Kraftfahrzeuges  11 von 18 Seite 12 von 18

**False Positives:**

- `Wiener  Gemeinderat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/149581.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149581.1_139`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird, sind Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung, des Wiener  Gemeinderates über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABI Nr 2013/29).

**False Positives:**

- `Wiener  Gemeinderates` — no gold match — likely missing annotation
- `Wiener  Gemeinderates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `BM_Finanzen_Full` 💣

**F1:** 0.007 | **Precision:** 0.835 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `91cc2fc2`  
**Description:**
Matches the full organization name 'BM für Finanzen' and its abbreviation 'BMF'.

**Content:**
```
\bBM\s+für\s+Finanzen\b|\bBMF\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.835 | 0.004 | 0.007 | 79 | 66 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 13 | 17095 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der BergLuftfahrt, KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `BergLuftfahrt` (organisation)
- `KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich` (address)
- `Westra  GmbH Steuerberatungsgesellschaft` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_19`)


Mit Vorhalt vom 21.06.2016 teilte das BMF der Bf. mit, dass eine Entlastungsmaßnahme  gemäß § 48 BAO nur in Betracht komme, wenn eine echte internationale Doppelbesteuerung  vorliege, worunter die Erhebung gleicher oder gleichartiger Steuern von demselben  Steuerpflichtigen für denselben Steuergegenstand und denselben Zeitraum zu versehen sei.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_88`)


Das BMF hat die Beschwerde mitsamt den bezugshabenden Akten dem BFG als Direktvorlage  gemäß § 262 Abs. 4 i.V.m. § 265 BAO zur Entscheidung vorgelegt und dazu im Vorlagebericht  vom 20.04.2018 Folgendes ausgeführt:    „Der Unterlage „Online Gambling in Greece“ (Anhang zum Bericht FA10 vom 20.4.2017),  erstellt von Gambling Complience (https://gamblingcompliance.com), Stand März 2015,  zufolge, befand sich die Regulierung des Online-Wett- und Glücksspielmarktes in Griechenland  in einer Übergangsphase.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_15`)


Die Tatsache, dass für Zwecke der deutschen Besteuerung ein steuerfreier Betrag  der deutschen Alterspension ermittelt wird, ist für Zwecke des österreichischen  Progressionsvorbehalts unerheblich, da dieser nach österreichischem Recht  ermittelt wird (siehe Info auf BMF-Homepage unter https_//www.bmf.gv.at/steuern  /selbststaendige-unternehmer/einkommensteuer/est-faq-deutsche-pension.html)

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_121`)


ob im Zeitpunkt des abgeschlossenen Verfahrens diese Umstände der Partei bekannt waren  (BMF, AÖF 2006/192, Abschn.2.1.; aM VwGH 28.9.1998, 96/16/0158;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_71`)


Diese Schätzung stützt sich auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142- VI/6/2016, BMF-Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der  Besteuerung von Grundstücken und Kapitalvermögen durch das Steuerreformgesetz  2015/2016, BGBI. I Nr. 118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, wonach der  Grundanteil mit 20% des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  geschätzt werden kann.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_89`)


Unter Bezugnahme auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142-VI/6/2016, BMF- Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der Besteuerung von  Grundstücken und Kapitalvermögen durch das Steuerreformgesetz 2015/2016, BGBI. I Nr.  118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, beabsichtigt das Finanzamt, den  Grundanteil mit 20 % des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  zu schätzen, wobei 1.000 m2 steuerfrei bleiben und 1.144 m2 steuerpflichtig sind.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_38`)


8. Im Vorlageantrag samt nachgereichter gesonderter Begründung wird seitens des Bf,  vertreten durch C, Steuerberater in D/BB, ua. vorgebracht:  Abgesehen von der bestrittenen NoVA-Pflicht in Österreich sei der Pickup des Bf von der NoVA  befreit, da dieser lt. NoVA-Richtlinie bis 31.3.2007 als LKW einzustufen und lt. BMF vom  11.7.2007 weiterhin als solcher zu behandeln sei.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_39`)


In der Liste des BMF zu "Pritschenwagen"  gemäß VO aus 1996 und § 4 VO 2002, die als LKW gelten, seien "Nissan Navara" und "Nissan  Pickup" als Pritschenwagen aufgeführt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_105`)


Das BMF habe  sich bis dato nicht veranlasst gesehen, die Rz 705 der Gebührenrichtlinien 2007 zu ändern.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_75`)


Stellungnahme:   Vorweg ist an dieser Stelle festzuhalten, dass, auch wenn der § 26 (3) StuFöG 1992 mit  01.09.2017 (BGBl. I Nr. 54/2016) geändert worden ist, die bislang geltenden Kriterien für die  Beurteilung der Wegzeiten zur Erreichung des Studienortes weiterhin anzuwenden sind, weil  die VO des BMF zur Berufsausbildung des Kindes außerhalb des Wohnortes (BGBl. Nr.  624/1995 idgF) auf das Studienförderungsgesetz idF BGBl. I Nr. 50/2016 verweist.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_240`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. im Verfahren  betreffend Vorjahre vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_17`)


Für die fremdfinanzierte Rentenversicherung sei das  Anwaltshonorar sehr wohl anzuerkennen, als Beweis diene ein Schreiben der Abteilung IV/7  des BMF vom 12.1.2001, in dem ausgeführt wird, dass Zinsen für Fremdkapital, das für den  Erwerb eines Rentenstammrechtes aufgenommen wurde, gemäß § 16 Abs 1 Z 1 EStG  Werbungskosten darstelle (Verweis auf EStR 2000 Rz 7018) und hinsichtlich des  Verlustausgleiches EStR 2000 Rz 151 ff zu beachten seien.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_64`)


Weshalb dieser Judikatur "als Folge der  Gesetzesänderung "der Boden entzogen sein soll", ist für das Bundesfinanzgericht nicht  ersichtlich, zumal Ritz und das Bundesministerium für Finanzen schon zur § 303 Abs. 1 BAO alte  Fassung nachstehende - von der Judikatur des Verwaltungsgerichtshofs abweichende -  Rechtsansicht vertreten haben (vgl. Ritz, BAO4, § 303 Tz 27 und vgl. Ritz, BAO5,§ 303 Tz 47):   "Für die Frage des Neuhervorkommens ist - ebenso wie für die amtswegige Wiederaufnahme -  der Kenntnisstand der Abgabenbehörde (im jeweiligen Verfahren) maßgebend, nicht jedoch,  ob im Zeitpunkt des abgeschlossenen Verfahrens diese Umstände der Partei bekannt waren  (BMF, AÖF 2006/192, Abschn.2.1.; aM VwGH 28.9.1998, 96/16/0158;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesministerium für Finanzen` (organisation)
- `Verwaltungsgerichtshofs` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_263`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. mit der  Beschwerde vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_24`)


Zur Begründung wurde ausgeführt, die Rechtsprechung (bzw die Einkommensteuerrichtlinien  des BMF) sehe den Übergang des wirtschaftlichen Eigentums als entscheidend für die  Beurteilung einer Anschaffung im Sinne des § 10 EStG 1988 an.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_90`)


Im Rundschreiben 293/2007 der österreichischen Ärztekammer vom 07.12.2007 wird zur Frage  der Besteuerung der Bestattungsbeihilfe und Hinterbliebenenunterstützung (§§ 98 Abs 1 und  104 ÄrzteG) auf eine Mitteilung des BMF vom 04.12.2007, BMF-010222/0174-VI//7/2007,  hingewiesen, mit der eine Anfrage der Österreichischen Ärztekammer vom 30.08.2007  beantwortet wurde und der ua Folgendes zu entnehmen ist:  „Die von der Ärztekammer ausbezahlte Hinterbliebenenunterstützung und Bestattungsbeihilfe  ist unabhängig von der Gestaltung des jeweiligen Sachverhalts immer nach § 22 Z 4 iVm § 32 Z  2 EStG beim Rechtsnachfolger zu versteuern.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_97`)


……“  Die österreichische Ärztekammer hat diese Rechtsmeinung des BMF im Rundschreiben  293/2007 vom 07.12.2007 zustimmend kommuniziert.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_30`)


Da die Daten des GWR von der  Statistik Austria dem BMF zur Verfügung gestellt werden und das BMF eine andere Behörde als  das zuständige Finanzamt ist, würde eine Abfrage dieser Daten das Erfordernis einer nach  außen erkennbaren Amtshandlung erfüllen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_79`)


Die Erkennbarkeit im Bundesministerium für Finanzen (BMF)  reicht aber aus, weil das BMF eine andere Behörde als das Finanzamt für Gebühren,  Verkehrsteuern und Glücksspiel ist, sodass die Amtshandlung nach außen erkennbar war.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesministerium für Finanzen` (organisation)
- `Finanzamt für Gebühren` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_53`)


Die Mindesthöhe des Verspätungszuschlages von 0,1% könne  auch als angemessen erscheinen (vgl. Erlass des BMF, GZ BMF-010103/0030-V1/2006 vom  10.042006).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136045.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136045.1_37`)


Im  Rahmen der Entsendung wurden Taggelder ausbezahlt, welche vom Dienstgeber (der  damaligen Erlassmeinung des BMF folgend) zum Teil steuerfrei und zum Teil steuerpflichtig  behandelt wurden.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_113`)


Die fehlende Angabe der  Wiederaufnahmsgründe in der Begründung des mit Beschwerde angefochtenen Bescheides ist  auch in der Beschwerdevorentscheidung nicht „nachholbar“ (vgl BMF, AÖF 2006/192, Abschn  4;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_153`)


Ein „Kurzgutachten“ (mit unvollständiger Befundaufnahme oder reduzierter  Gutachtensmethodik und -begründung) erfüllt diesen Standard nicht, kann daher auch nicht zur  Beweislastumkehr führen, sondern unterliegt ebenso wie ein Gutachten, das von einer anderen  Person als einem Immobiliensachverständigen erstellt wird, der freien Beweiswürdigung (BMF  vom 13. Mai 2016, 010206/0058-VI/5/2016).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/138980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138980.1_137`)


Aigner et al., DBA-Kommentar2, Seite 1510, führt aus, dass das BMF von einer konstitutiven  Wirkung des Progressionsvorbehaltes in den DBA ausgehe, während der VwGH von einer nur  deklaratorischen Klarstellung des Progressionsvorbehaltes in den DBA ausgehe.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/140219.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140219.1_225`)


In Anwendung der angeführten Judikatur des Höchstgerichtes sowie der Rechtsmeinung des  BMF laut den Einkommensteuerrichtlinien, der sich das Bundesfinanzgericht im konkreten Fall  anschließt, sind die geltend gemachten Anschaffungsnebenkosten laut Punkt 8. bis 12.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_76`)


Nach dem klaren Wortlaut der Gebührenrichtlinien des BMF sowie der Rechtsprechung des  VwGH führe die Vereinbarung aller denkmöglichen Kündigungsgründe des § 30 Abs. 2 MRG zur  gebührenrechtlichen Qualifizierung des Mietvertrages als auf „unbestimmte“ Zeit  abgeschlossen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/141397.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141397.1_223`)


Die Ausführungen des BMF würden die  Weiterentwicklung des Rechts widerspiegeln wie zB Verbleiben eines Existenzminimums als  maximale Zumutbarkeit zur Zuordnung des Steuerpflichtigen und danach die Übernahme der  restlichen Kosten aus sittlichen Gründen durch andere Personen, Wegfall von  Regressansprüchen, insbesondere in der Sozialgesetzgebung und Pflege mit Krankheitskosten  etc.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_41`)


g) Aus einer FA-Anfrage an das BMF v. 13.3.2014 geht hervor, dass Erika Puttfarken  seit Jänner 2012  die FB für vier Kinder bezieht;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Erika Puttfarken` (person)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_247`)


d) Laut Abfrage der aktuellen Grunddaten des BMF zum Bf (Stand 4.7.2023) scheint seit       9.8.2016 als Wohnsitz folgende Adresse auf: D-Ort8;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_281`)


Die FB samt Kinderabsetzbeträgen (KG) für  alle vier Kinder wurde vom Finanzamt ab Dezember 2013 (bis März 2014) vorläufig einbehalten  (siehe lt. FA-Anfrage an das BMF v. 13.3.2014).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_286`)


Meldebehörde vom 24.6.2015) und ab 9.8.2016 in D-Ort8 (siehe aktuell abgefragte  Grunddaten des BMF).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/141878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141878.1_34`)


Die BP habe iS der Ansicht des BMF 50% der Kursverluste (65.767,21 €) dem Gewinn  (33.512,61 €) hinzugerechnet (vgl. 804 EStR).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/142618.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142618.1_6`)


In ihrer Begründung verwies die belangte Behörde  auf § 1 Abs. 1 der Verordnung des BMF, mit der ein eigenes Verfahren für die Erstattung der  abziehbaren Vorsteuern an ausländische Unternehmer geschaffen wird (BGBl 1995/279 idgF)  hin.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/142618.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142618.1_38`)


Die belangte Behörde verwies unter Wiedergabe der Bestimmungen der Verordnung des BMF,  mit der ein eigenes Verfahren für die Erstattung der abziehbaren Vorsteuern an ausländische  Unternehmer geschaffen wird (BGBl 1995/279), dass ihres Erachtens das  Vorsteuererstattungsverfahren zwingend anzuwenden sei und daher keine Jahresveranlagung  vorgenommen werden könnte.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_26`)


Inhaltlich sei davon auszugehen, dass bereits für die Mietzinsbildung bei der Anmietung des  Wohnraumes durch den Dienstgeber der Beschwerdeführerin (in Folge: Bf.), das BMLV, die  Umsetzung der im Einvernehmen mit dem BMF verfolgten strategischen Zielsetzung der  Schaffung leistbaren Wohnraumes an den Dienstorten der Mitarbeiter des BMLV und unter  den gesetzlichen Voraussetzungen die Gestattung der Weiterbenutzung auch für Beamte im  Ruhestand maßgeblich gewesen seien.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_28`)


Der Bund selbst habe im Wege des Bundeskanzleramtes für die Berechnung der Vergütung von  Dienst- und Naturalwohnungen im Einvernehmen mit dem BMF Durchführungsbestimmungen  erlassen, welche die Errechnung der Vergütung abschließend im Wege der Vorgabe von  Richtlinien regeln würden.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_59`)


In diesem Zusammenhang  verweist die Bf. auf den Grundsatz von Treu und Glauben (Erlass des BMF 06.04.2006, BMF- 010103/0023-VI/2006).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_69`)


Es werde somit  angeregt, den Antrag an den Verfassungsgerichtshof zu stellen, die Kundmachung des BMF zur  GZ BMF-010202/0100-VI/3/2004 [gemeint wohl: 2014] wegen Gesetzeswidrigkeit sowie die  Bestimmung des § 38 Abs. 1 BewG wegen Verfassungswidrigkeit zu prüfen und aufzuheben.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/144966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144966.1_26`)


Anzumerken sei außerdem, dass eine Ermittlung gemäß der Grundstückswerteverordnung  (BMF-Infos vom 12.5.2016 und 18.7.2017) unter Beachtung des mehrgeschossigen Baus zu  einem noch niedrigeren Wert als der angesetzten 5% führen würde.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/144966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144966.1_108`)


“  (Herzog, Einkommensteuerliche Änderungen bei den Grundstücken ab 2016, SWK 2016, 1035)  „Die BMF-Info eröffnet aber auch selbst die Möglichkeit, das (konkrete) Verhältnis von Grund- und-Boden-Wert und Gebäudewert nach der zum GrEStG ergangenen  Grundstückswertverordnung glaubhaft zu machen (der im Gesetz geforderte Nachweis wird  hier etwas abgeschwächt).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/144971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144971.1_107`)


die bloße  Möglichkeit reicht nicht (vgl Ritz/Koran, BAO7, § 299 Rz 13 mit Verweis auf BMF, AÖF 2003/65,  Abschn 3; VwGH 20.1.2016, 2012/13/0059).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/145202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145202.1_39`)


Sie werden jeweils vom Landesgericht für Zivilrechtssachen in  Wien bekanntgegeben und jährlich vom BMF unter www.bmf.gv.at veröffentlicht.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Landesgericht für Zivilrechtssachen in  Wien` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/146775.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146775.1_77`)


Zahlungen für Dritte kann der Stpfl grundsätzlich nicht geltend machen (zB keine dauernde  Lasten des Ehegatten, BMF, RdW 1995, 329), ausnahmsweise jedoch dann, wenn es sich um  Versicherungsbeiträge, Ausgaben zur Wohnraumschaffung bzw Wohnraumsanierung oder um  Kirchenbeiträge für den nach § 18 Abs 3 Z 1 begünstigten Personenkreis ([Ehe-]Partner, Kinder)  handelt (siehe dazu Tz 254 ff).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_168`)


Derartige Zuschüsse zur  Anschaffung eines Ersatzwirtschaftsgutes würden außerhalb des  Veranlassungszusammenhanges des Veräußerungserlöses für die Liegenschaft liegen und seien  demnach eine steuerpflichtige Betriebseinnahme (BMF-Erlass vom 30.06.2009, SZK- 010203/0336-Est/2009).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/146973.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146973.1_56`)


werden nicht zur beruflichen Tätigkeit des Berufskraftfahrers gezählt (dt BMF 12.11.2014,  BStBl I 2014, 1467, Rz 278).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_133`)


10. Grundsätzlich kommt aus österreichischer Sicht - unter anderem - die Abänderung eines  Bescheides aufgrund eines rückwirkenden Ereignisses nach § 295a BAO als  verfahrensrechtliches Instrument zur Umsetzung der Verständigungsregelung dann in  Betracht, wenn das anwendbare DBA keine dem Art. 25 Abs. 2 entsprechende Bestimmung  enthält (vgl. den diesbezüglichen Hinweis von Papst/Urtz, in Aigner/Kofler/Tumpel, DBA2 Art.  25 Rz 99 auf Erlässe des BMF und deren Aufgriff in der Literatur).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_192`)


17. Also mag die Rechtsauffassung des VwGH der zwischen Österreich und Deutschland  geschlossenen Verständigungslösung (allgemeines Konsultationsverfahren) vom 13. August  2010, Erlass des BMF vom 21. Dezember 2010, BMF-010221/3371-IV/4/2010, insoweit nicht  widersprechen, als ihr zufolge nicht im ehemaligen Tätigkeitsstaat (hier: Deutschland)  besteuerte Abfindungszahlungen „gemäß Artikel 28 Absatz 1 lit. a“ im Ansässigkeitsstaat dieser  Person besteuert werden können (hier: Österreich).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/148033.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148033.1_18`)


Darunter fallen laut BMF zB wenn ein  2 von 24 Seite 3 von 24

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_19`)


Weiters erging mit  selbem Datum ein Schreiben an die im BMF für die technische Abwicklung im Zusammenhang  mit dem FinanzOnline-System zuständige Abteilung, offene Punkte im Zusammenhang mit der  Übermittlung der strittigen Schriftstücke zu klären.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_49`)


Dass der Komplementär am FinanzOnline-System teilnimmt, geht aus seiner diesbezüglichen  Information der für dieses System zuständigen Abteilung im BMF vom 17.bzw. 22.4.2025  hervor.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_52`)


Nach Auskunft  der WiEReG-Registerbehörde (eingerichtet im BMF, Sektion III, Abteilung III/12) vom 8.5.2025  hat der auch im Beschwerdeverfahren einschreitende steuerliche Vertreter diese Meldung für  die Bf. abgegeben.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_15`)


Die zuständige Abteilung des BMF hat dem BFG gegenüber bestätigt, dass der angefochtene  Bescheid der Bf. (bzw. dessen steuerlicher Vertretung) am 6.2.2025 zugestellt – und zudem von  dieser noch am selben Tag gelesen – wurde (E-Mail vom 6.6.2025).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_18`)


Der Zeitpunkt der elektronischen Zustellung am 6.2.2025 (via Databox) wurde dem BFG von  der zuständigen Abteilung des BMF (Zentrale Services – Verfahrensbetreuung) bestätigt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_21`)


Das allgemein gehaltene Vorbringen im Vorlageantrag, „die Beschwerde [gemeint wohl: der  Bescheid]… wurde unseres Erachtens über USP nicht ordnungsgemäß zugestellt“, ließ sich –  insbesondere nach der vorliegenden Bestätigung der für die Verfahrensbetreuung zuständigen  Stelle im BMF (E-Mail vom 6.6.2025) - nicht verifizieren.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_22`)


Laut Auskunft bzw. Auswertung des  BMF erfolgte die Zustellung – ordnungsgemäß - per FinanzOnline (Databox) am 6.2.2025 (und  wurde überdies auch noch am selben Tag von der Empfängerin gelesen).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/148307.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148307.1_47`)


Vielmehr ergibt sich aus  einer technischen Auswertung/Überprüfung durch die zuständige Abteilung im BMF, dass die  wirksame Zustellung an die Bf. (bzw. deren Vertretung) tatsächlich am 6.2.2025 erfolgte.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/148574.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148574.1_76`)


Dafür ist nach Ansicht des Bundesministeriums für Finanzen (BMF, SWI 1998, 553) bereits der  beim österreichischem Arbeitgeber eintretende Leistungserfolg ausreichend, was, wenn der  Beschwerdeführer für seinen österreichischen Arbeitgeber Transportaufträge im Ausland  ausführt, außer Zweifel steht.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesministeriums für Finanzen` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/148936.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148936.1_30`)


Der Vertreter der  belangten Behörde verwies nochmals darauf, dass das Pensionsschema des britischen  Unternehmens aufgrund der (in der Beschwerdevorentscheidung übernommenen) Auskunft  der ZFS (= zentralen Fachstelle des BMF) nicht als begünstigte Pensionskasse im Sinne das DBA  zu sehen sei, da der Trustee neben der Verwaltung des hier zu behandelnden Pensionsfonds  auch noch andere Tätigkeiten ausübe und die ZFS davon ausgehe, dass bei der Übertragung  von einem britischen Pensionsschema auf das andere Pensionsschema zwischenzeitig eine  Verfügungsmacht des BF bestanden habe.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_37`)


Entsprechend den Erlässen des BMF habe die Antragstellerin stellvertretend für ihre  Anteilsinhaber für die Jahre 2009 und 2010 gemäß den Doppelbesteuerungsabkommen mit  Österreich die Herabsetzung der Kapitalertragsteuer auf 15% und Erstattung des  Differenzbetrages (10% der Bruttodividenden) beantragt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_71`)


Diese Schätzung stützt sich auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142- VI/6/2016, BMF-Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der  Besteuerung von Grundstücken und Kapitalvermögen durch das Steuerreformgesetz  2015/2016, BGBI. I Nr. 118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, wonach der  Grundanteil mit 20% des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  geschätzt werden kann.

**False Positives:**

- `BMF` — similar text (different position): `BMF`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BMF`(organisation)
- `BMF`(organisation)
- `BMF`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_89`)


Unter Bezugnahme auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142-VI/6/2016, BMF- Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der Besteuerung von  Grundstücken und Kapitalvermögen durch das Steuerreformgesetz 2015/2016, BGBI. I Nr.  118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, beabsichtigt das Finanzamt, den  Grundanteil mit 20 % des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  zu schätzen, wobei 1.000 m2 steuerfrei bleiben und 1.144 m2 steuerpflichtig sind.

**False Positives:**

- `BMF` — similar text (different position): `BMF`
- `BMF` — similar text (different position): `BMF`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `BMF`(organisation)
- `BMF`(organisation)
- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_18`)


Mit Beschwerdevorentscheidung vom 30.10.2019 wies das Finanzamt die Beschwerde gegen  den Einkommensteuerbescheid 2018 mit nachstehender Begründung ab:  Laut Information des BMF/bundesweiter Fachbereich vom 20.11.2012, SZK-010203/0539-

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_35`)


dem Hinweis auf GZ. BMF-010222/0174-VI/7/2007).

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_90`)


Im Rundschreiben 293/2007 der österreichischen Ärztekammer vom 07.12.2007 wird zur Frage  der Besteuerung der Bestattungsbeihilfe und Hinterbliebenenunterstützung (§§ 98 Abs 1 und  104 ÄrzteG) auf eine Mitteilung des BMF vom 04.12.2007, BMF-010222/0174-VI//7/2007,  hingewiesen, mit der eine Anfrage der Österreichischen Ärztekammer vom 30.08.2007  beantwortet wurde und der ua Folgendes zu entnehmen ist:  „Die von der Ärztekammer ausbezahlte Hinterbliebenenunterstützung und Bestattungsbeihilfe  ist unabhängig von der Gestaltung des jeweiligen Sachverhalts immer nach § 22 Z 4 iVm § 32 Z  2 EStG beim Rechtsnachfolger zu versteuern.

**False Positives:**

- `BMF` — similar text (different position): `BMF`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BMF`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_53`)


Die Mindesthöhe des Verspätungszuschlages von 0,1% könne  auch als angemessen erscheinen (vgl. Erlass des BMF, GZ BMF-010103/0030-V1/2006 vom  10.042006).

**False Positives:**

- `BMF` — similar text (different position): `BMF`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BMF`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_44`)


h) Stellungnahme der Fachabteilung für Familienbeihilfe/BMF v. 25.3.2014, woraus ua.  hervorgeht:  Die Ehegatten B (verheiratet seit 29.2.2012) sind am 22.12.2011 von Deutschland nach  Österreich übersiedelt und haben seit Jänner 2012 ihren Mittelpunkt der Lebensinteressen in  Österreich.

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_69`)


Es werde somit  angeregt, den Antrag an den Verfassungsgerichtshof zu stellen, die Kundmachung des BMF zur  GZ BMF-010202/0100-VI/3/2004 [gemeint wohl: 2014] wegen Gesetzeswidrigkeit sowie die  Bestimmung des § 38 Abs. 1 BewG wegen Verfassungswidrigkeit zu prüfen und aufzuheben.

**False Positives:**

- `BMF` — similar text (different position): `BMF`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)
- `BMF`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_171`)


Bewertung des forstwirtschaftlichen Vermögens  Auf Grund des § 46 Abs. 2 und 3 iVm § 44 BewG 1955 hat der Bundesminister für Finanzen eine  Verordnung über die Bewertung von forstwirtschaftlichem Vermögen (BMF-010202/0104- VI/3/2014) kundgemacht.

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_175`)


Ebenso ergibt sich bereits aus dem angefochtenen  Bescheid, für welche forstwirtschaftlich genutzten Flächen, in welchem Flächenausmaß,  welcher Hektarsatz gemäß § 14 iVm Anlage 13 der Verordnung des Bundesministers für  Finanzen (BMF-010202/0104-VI/3/2014) zur Anwendung gebracht wurde.

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/144619.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144619.1_179`)


Im Lichte dieser Entscheidung hegt das Bundesfinanzgericht keine Zweifel an der  Verfassungskonformität der im Beschwerdefall anzuwendenden Bestimmungen der  Verordnung des Bundesministers für Finanzen (BMF-010202/0104-VI/3/2014) und sieht sich  somit nicht veranlasst einen diesbezüglichen Normenprüfungsantrag an den  Verfassungsgerichtshof zu stellen.

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verfassungsgerichtshof`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_192`)


17. Also mag die Rechtsauffassung des VwGH der zwischen Österreich und Deutschland  geschlossenen Verständigungslösung (allgemeines Konsultationsverfahren) vom 13. August  2010, Erlass des BMF vom 21. Dezember 2010, BMF-010221/3371-IV/4/2010, insoweit nicht  widersprechen, als ihr zufolge nicht im ehemaligen Tätigkeitsstaat (hier: Deutschland)  besteuerte Abfindungszahlungen „gemäß Artikel 28 Absatz 1 lit. a“ im Ansässigkeitsstaat dieser  Person besteuert werden können (hier: Österreich).

**False Positives:**

- `BMF` — similar text (different position): `BMF`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BMF`(organisation)

</details>

---

## `OECD_Organization` 

**F1:** 0.002 | **Precision:** 0.833 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `5cf11104`  
**Description:**
Matches 'OECD' as an organization.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.001 | 0.002 | 18 | 15 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 15 | 3 | 17001 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_180`)


In Anhang I A ist geregelt, dass das Frascati Manual  (2002) der OECD in der jeweils gültigen Fassung Grundlage der Begriffsbestimmungen und  Abgrenzungen der Verordnung ist und ergänzend zu diesen heranzuziehen ist (vgl. VwGH v.  29.3.2017, Ra2015/15/0060).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_344`)


Darüber hinaus entschied der Verwaltungsgerichtshof (VwGH 22.5.2013, 2009/13/0031), dass  der Begriff "Arbeitgeber" in der 183-Tage-Klausel von Doppelbesteuerungsabkommen bzw. in  Art. 15 Abs. 2 OECD-Musterabkommen im Sinn eines "wirtschaftlichen Arbeitgebers" zu  verstehen ist.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_91`)


Die Zentralstelle kann den Beamten mit seiner Zustimmung  1. zu Ausbildungszwecken oder als Nationalen Experten zu einer Einrichtung, die im Rahmen  der europäischen Integration oder der OECD tätig ist, oder  2.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/144557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144557.1_62`)


Unter Bezugnahme auf das OECD-Musterabkommen werde hingegen der Anwendung des  Artikel 19 DBA-Niederlande der Vorzug gegeben.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/144557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144557.1_149`)


…“  Artikel 19 des Abkommens entspricht im Prinzip Artikel 19 des Musterabkommens der OECD  (im Folgenden: MA).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/144557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144557.1_152`)


Das Kassenstaatsprinzip wird bei Ruhegehältern an Staatsbedienstete jedoch dadurch  eingeschränkt, dass nach dem OECD-Konzept (Art 19 Abs. 2 lit. b MA) das Besteuerungsrecht  nicht dem Kassenstaat, sondern dem Ansässigkeitsstaat zustehen soll, wenn es sich bei den  Pensionsbeziehern um dessen Staatsangehörige handelt (vgl. Loukota/Jirousek, Internationales  Steuerrecht I/1 Öffentlicher Dienst, Stand 1.1.2016, rdb.at, Rz 47ff).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/144911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144911.1_65`)


Solche  gelinderen Mittel seien auch explizit für die Ausübung von Kontrollmaßnahmen betreffend die  Einhaltung der Sorgfalts- und Meldepflichten des GMSG durch die OECD für die teilnehmenden  Staaten definiert worden.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_108`)


Ausnahmen können sich allerdings aus dem Art. 25  Abs. 2 zweiter Satz OECD-Musterabkommen entsprechenden Bestimmungen in  Doppelbesteuerungsabkommen ergeben (Ritz/Koran, BAO7 § 48 Rz 15; vgl. ebd., § 209a Rz 1 m.  w. N.).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_112`)


Diesbezüglich nennen Ritz/Koran Art. 25 Abs. 2 zweiter Satz OECD-Musterabkommen zwar als  Beispiel für eine nach Eintritt der Verjährung noch rechtmäßige Abgabenfestsetzung,  hinterfragen dies zugleich aber kritisch.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_120`)


Nach Ansicht von Loukota/Jirousek/Schmidjell-Dommes/Daurer ergibt sich daraus, dass die  „Verständigungsvereinbarung“ nach den DBA, die bereits dem „OECD-Musterabkommen“ aus  1977 folgen, ungeachtet der Fristen des innerstaatlichen Rechts der Vertragsstaaten  umzusetzen ist, dass diese ungeachtet bereits eingetretener Rechtskraft und Verjährung oder  abgelaufener Antragsfristen auch umgesetzt werden könne (Loukota/Jirousek/Schmidjell- Dommes/Daurer, Internationales Steuerrecht, 25.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_122`)


Damit erkennen die Autoren - wenigstens implicite - einer Verständigungsvereinbarung,  welche Art. 25 Abs. 2 OECD-Musterabkommen entspricht, „über ihren zweiten Satz“ (Außen- )Wirkung zu. Nimmt man diese Wirkung nur gegenüber allfälliger Verjährung an, so äußerte sie  9 von 21 Seite 10 von 21

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_131`)


Jedenfalls weist die  Textierung der relevanten Passage sowohl im OECD-Musterabkommen als auch im DBA- Deutschland eher in die Richtung eines Befolgungsanspruches, wobei aber diese Befolgung,  insbesondere auch, weil dieser Anspruch sich in einer an die nationalen Verwaltungsbehörden  gerichteten Durchführungspflicht ausdrückt, regelgeleitet und gebunden an die nationalen  Verfahrensvorschriften erfolgen muss (arg.: „Die Verständigungsregelung ist ungeachtet der  10 von 21 Seite 11 von 21

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_132`)


Fristen des innerstaatlichen Rechts der Vertragsstaaten durchzuführen.“ jeweils wortident  sowohl im OECD-Musterabkommen als auch im DBA-Deutschland).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_149`)


Es scheint daher angebrachter, mit Macho/Spensberger/Steiner von einer in Art. 25 Abs. 2  letzter Satz OECD-Musterabkommen vorgesehenen Durchbrechungswirkung der  innerstaatlichen Fristenregelungen aufgrund von Bestimmungen über das  Verständigungsverfahren im jeweils anzuwendenden DBA zu sprechen (vgl.  Macho/Spensberger/Steiner, SWK 2014, 939 (940);

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/147403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147403.1_157`)


abkommensrechtliche Verpflichtung der Vertragsstaaten zur Umsetzung der  Verständigungsvereinbarung nicht werden beseitigen können (Papst/Urtz, in  Aigner/Kofler/Tumpel, DBA2 Art. 25 Rz 97), gerade nicht zwingend aufgezeigt, dass eine  „Umsetzung“ (Durchführung) auch unter Abstandnahme vom Gebrauch nationaler  Verfahrenstitel wie des in § 295a BAO vorgesehenen unmittelbar auf Basis einer dem zweiten  Satzes des Artikels 25 Abs. 2 OECD-Musterabkommen entsprechenden Regelung in dessen  Rahmen erfolgen könnte (ein Vorteil dieser Position liegt freilich darin, dass überhaupt erst bei  Fehlen des Satzes 2 eine Anwendung nationaler Verfahrenstitel in Betracht käme, diese dann  aber auch in jedem Fall die Beachtung eingetretener Verjährung verlangte).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/144911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144911.1_119`)


teilnehmende Staaten gemäß § 91 Z 2 sind, welche entweder die in § 7 der  mehrseitigen Vereinbarung vom 29. Oktober 2014, BGBl. III Nr. 182/2017, über den  automatischen Austausch von Informationen über Finanzkonten (OECD-MCAA) geforderten  Voraussetzungen erfüllen oder ein anderes bilaterales Übereinkommen abgeschlossen haben.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/149828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149828.1_105`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

**False Positives:**

- `OECD` — no gold match — likely missing annotation
- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `SUVA`(organisation)

</details>

---

## `Landesgerichts_Genitive` 

**F1:** 0.000 | **Precision:** 0.500 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `552ec6e5`  
**Description:**
Matches the genitive form 'Landesgerichts' which was previously missed.

**Content:**
```
\bLandesgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.000 | 0.000 | 6 | 3 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 3 | 6753 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_68`)


Mit Beschluss des Landesgerichts Salzburg vom 20. August 2014 erfolgte hinsichtlich der Klemeyer + Heisterhagen Pharma GmbH die Eröffnung des Sanierungsverfahrens ohne Eigenverwaltung, welches mit Beschluss  vom 19. Dezember 2014 aufgrund der rechtskräftigen Bestätigung des Sanierungsplans  aufgehoben wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

**Missed by this rule (FN):**

- `Klemeyer + Heisterhagen Pharma GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_38`)


Die Glücksspielabgaben für die  in diesen Glücksspielabgabenbescheiden ausgewiesenen Zeiträume sowie der Selbstberechnung  für 06/2018 sind bei der PS uneinbringlich, da das Konkursverfahren nach Schlussverteilung  aufgehoben wurde (14 S AZ des Landesgerichts XY).

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_27`)


Die Änderungen wurden  am 2.3.2021 im Firmenbuch des Landesgerichts XXX eingetragen.

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_162`)


Am 23.9.2019 ist gegen den Bf. ein Urteil des Landesgerichts für Strafsachen Wien ergangen,  dessen Spruch auszugsweise wie folgt lautet:  „Ing. Bianca Karbow  ist schuldig, hat im Zeitraum 2008 bis 2013 im Bereich des Finanzamts Wien  9/18/19 Klosterneuburg als für die Wahrnehmung der abgabenrechtlichen Obliegenheiten  verantwortlicher Einzelunternehmer vorsätzlich unter Verletzung einer abgabenrechtlichen  Anzeige-, Offenlegungs- und Wahrheitspflicht eine Verkürzung von bescheidmäßig  festzusetzenden Abgaben bewirkt bzw zu bewirken versucht, und zwar,  I./ durch die Abgabe inhaltlich unrichtiger Steuererklärungen betreffend Einkommensteuer und  Umsatzsteuer, wobei er die Taten teils unter Verwendung falscher Beweismittel (§ 39 Abs 1 lit a  FinStrG), nämlich durch die Aufnahme von Schein- und Deckungsrechnungen, die gezielt zum  Zwecke der Abgabenhinterziehung produziert worden waren, in sein buchhalterisches  Rechenwerk aufnahm, derweil die Leistungen tatsächlich nicht bzw nicht im ausgewiesenen  Umfang stattgefunden hatten, beging, nämlich  1./ hinsichtlich Einkommensteuer  am 9.3.2010 für das Jahr 2008 EUR 57.486,09,  am 14.1.2011 für das Jahr 2009 EUR 49.150,22,  am 30.4.2012 für das Jahr 2010 EUR 15.424,-,  am 27.5.2013 für das Jahr 2011 EUR 22.581   am 1.12.2013 für das Jahr 2012 EUR 16.299,-,  am 16.1.2015 für das Jahr 2013 EUR 15.531,-,  SUMME EUR 176.471,31,  11 von 16 Seite 12 von 16

**False Positives:**

- `Landesgerichts` — partial — pred is substring of gold: `Landesgerichts für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen`(organisation)
- `Ing. Bianca Karbow`(person)
- `Finanzamts Wien  9/18/19`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_187`)


Der Bf. hat das Urteil des Landesgerichts für Strafsachen angenommen.

**False Positives:**

- `Landesgerichts` — partial — pred is substring of gold: `Landesgerichts für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_191`)


Bescheid betreffend Festsetzung von Umsatzsteuer für die Monate Jänner 2014 bis August  2014  Die im Zuge der Betriebsprüfung aufgedeckten und auch in den Vorjahren laut Urteil des  Landesgerichts für Strafsachen Wien gesetzten Handlungen (Schein- und Deckungsrechnungen)  wurden auch im Jahr 2014 fortgesetzt.

**False Positives:**

- `Landesgerichts` — partial — pred is substring of gold: `Landesgerichts für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen`(organisation)

</details>

---

## `Landesgericht_entities` 💣

**F1:** 0.001 | **Precision:** 0.433 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `a15b0d99`  
**Description:**
Matches Landesgericht and its variations (genitive) as organizations.

**Content:**
```
\bLandesgericht(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.433 | 0.001 | 0.001 | 30 | 13 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 17 | 17588 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_8`)


Mit Beschluss des Landesgerichtes wurde über das Vermögen der GmbH am 3.6.2013 das  Konkursverfahren eröffnet und ein Masseverwalter bestellt. In der weiteren Folge zeigte dieser  am 22.12.2016 dem Konkursgericht an, die Insolvenzmasse reiche nicht aus, um die  Masseforderungen erfüllen zu können (Masseunzulänglichkeit).

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_69`)


Auch im Rahmen der Berichts- und  Prüfungstagsatzung vor dem zuständigen Landesgericht sei dieses Thema erörtert worden und  von den Gläubigerschutzverbänden zur Kenntnis genommen worden, dass keine Anfechtungen  bestünden.

| Predicted | Gold |
|---|---|
| `Landesgericht` | `Landesgericht` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_29`)


Die mit Gesellschaftsvertrag vom xx.xx.2005 als „AB GmbH“ errichtete und im Firmenbuch des  Landesgerichtes xx unter der FN xxxxxxx eingetragene Bf. erwarb am xx.xx.2006 von der Y xxxx  Stück dieser Vorzugsaktien im Nennbetrag von je Euro xxxx (gesamter Nennbetrag sohin Euro  xxxx) um einen Abtretungspreis von Euro xxxx.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_32`)


Die zuständige Referentin des Finanzamtes sei bei der Hauptverhandlung betreffend den Bf.  am 8.9.2015 vor dem Landesgericht anwesend gewesen und daher in Kenntnis davon, dass der  Bf. bereits vor der Hauptverhandlung vom 8.9.2015 an die Firma GmbH eine Zahlung von €  40.000,- an Schadenswiedergutmachung gezahlt habe, dies sei im Verfahren nicht  berücksichtigt worden.

| Predicted | Gold |
|---|---|
| `Landesgericht` | `Landesgericht` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_10`)


Mit Beschluss des Landesgerichtes für ZRS Graz vom 20.10.2015 war sodann über die damalige  Beschwerdeführerin der Konkurs eröffnet worden.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134379.1_59`)


wurde das Insolvenzverfahren mit Beschluss des zuständigen Landesgerichtes vom 20. Jänner  2017 aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_189`)


Somit ist auch das Bundesfinanzgericht gemäß § 116 Abs. 2 BAO an das Urteil des  Landesgerichtes für Strafsachen Wien gebunden.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/144695.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144695.1_5`)


Entscheidungsgründe  Der Beschwerdeführer (Bf.) erwirtschaftete als Einzelunternehmer durch die Veräußerung von  Scheinrechnungen Umsätze und legte weder die daraus im Zeitraum von 2008 bis 2012  erzielten Umsätze noch die erzielten Einnahmen gegenüber der Abgabenbehörde offen (siehe  Urteil des Landesgerichtes für Strafsachen vom 01.06.2022, 12Hv3456/21, mit dem der Bf.  wegen Abgabenhinterziehung nach § 33 Abs. 1 FinStrG zu einer Geldstrafe in der Höhe von  einer Million Euro bzw. ein Jahr Ersatzfreiheitsstrafe verurteilt wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/144695.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144695.1_6`)


Mit dem Urteil des OGH  vom 28.06.2023, 13 Os 119/22g, wurde die vom Bf. gegen das Urteil des Landesgerichtes  eingebrachte Nichtigkeitsbeschwerde zurückgewiesen).

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Beschluss des Landesgerichtes XY vom tt.10.2018, Az.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_7`)


Mit Beschluss des Landesgerichtes XY vom tt.07.2020 AZ s wurde der Konkurs über die  Primärschuldnerin nach Schlussverteilung aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_87`)


Mit Beschluss des Landesgerichtes XY vom 25.10.2018,  Az.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_89`)


Mit Beschluss des  Landesgerichtes XY vom tt.07.2020 AZ s wurde der Konkurs über die Primärschuldnerin nach  Schlussverteilung einer Quote von 1,9% aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichtes` | `Landesgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_27`)


Dies ergebe sich daraus, dass der über das  Vermögen der Gesellschaft eröffnete Konkurs mit Beschluss des Landesgerichtes Ort vom tt.  Juli 2014 nach der Schlussverteilung gemäß § 139 Insolvenzordnung (IO) aufgehoben worden  sei.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes Ort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes Ort`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_91`)


Mit Beschluss des  Landesgerichtes Ort vom tt. Juni 2013 wurde über das Vermögen der Gesellschaft der Konkurs  eröffnet und am 4. Juli 2013 die Schließung des Unternehmens angeordnet.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes Ort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes Ort`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_112`)


Mit Beschluss des Landesgerichtes Ort vom tt. Juli 2014 wurde der am tt. Juni 2013 über das  Vermögen der Gesellschaft eröffnete Konkurs nach der Schlussverteilung aufgehoben.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes Ort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes Ort`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_100`)


Als  Grundlage für diese Annahme wurden die vorliegenden, von Polizeihubschraubern aus,  aufgenommenen Luftbilder, die am Grundstück aufgenommenen Fotos, das für das  Landesgericht für Strafsachen abgegebene Gutachten der Abteilung für Wasserwirtschaft und  diverse Anzeigen herangezogen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_49`)


Im Urteil des Landesgerichtes LG (yCgyy/yyy vom Datum_2; dieses Urteil wurde vom Obersten  Gerichtshof am Datum_1, xObxxx/xxx bestätigt) werde festgehalten, „... dass die beklagte  Partei für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden ... haftet“.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes LG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes LG`(organisation)
- `Obersten  Gerichtshof`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_62`)


In diesem Verfahren entschied der Oberste Gerichtshof mit Urteil vom Datum_1, xObxxx/xxx,  zugunsten der Bf als Klägerin und bestätigte das Urteil des Landesgerichtes LG vom Datum_2,  yCgyy/yyy.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes LG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Landesgerichtes LG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_64`)


In weiterer Folge schlossen die Bf und der Bund am 15. September 2016 vor dem  Landesgericht LG einen gerichtlichen Vergleich betreffend Verdienstentgang iHv 73.234,55  Euro netto (Gehaltsdifferenzen netto und Prüfungsgebühren netto) sowie Zinsen iHv 5.760  Euro netto für den Zeitraum bis zum 30. September 2016 ab.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht LG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht LG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_68`)


Das vom Obersten Gerichtshof bestätigte Urteil des Landesgerichtes LG diente in der Folge als  Rechtgrundlage für die weiteren Nettozahlungen der B an die Bf im streitgegenständlichen Jahr  2019.

**False Positives:**

- `Landesgerichtes` — partial — pred is substring of gold: `Landesgerichtes LG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshof`(organisation)
- `Landesgerichtes LG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_113`)


Darüber hinaus hat das Landesgericht LG im rechtskräftigen Zwischen- und Teilurteil vom  Datum_2, yCgyy/yyy, festgestellt, dass der Bund als beklagte Partei der Bf als klagender Partei  auch für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden aus den  Mobbinghandlungen haftet.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht LG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht LG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_160`)


Am 10.9.2018 übermittelte das Finanzamt Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde gemäß § 100 Abs. 2 StPO den Zwischen- und Abschussbericht an die  Staatsanwaltschaft Wien beim Landesgericht für Strafsachen und diese legte am 15.7.2019 die  Anklageschrift dem Landesgericht für Strafsachen Wien vor.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen`
- `Landesgericht` — similar text (different position): `Landesgericht für Strafsachen`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Landesgericht für Strafsachen`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_174`)


Sachverhaltsmäßig steht fest, dass das Landesgericht für Strafsachen Wien auch betragsmäßig  die Sachverhaltsfeststellungen der Betriebsprüfung bestätigt hat und es als erwiesen  angenommen hat, dass der Bf. die oben angeführten Taten in objektiver und subjektiver  Hinsicht begangen hat.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_175`)


Unstrittig ist weiters, dass das Landesgericht für Strafsachen Wien bei Ermittlung des  Sachverhaltes von Amts wegen vorzugehen hatte.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_185`)


Das Landesgericht für Strafsachen Wien hat in seinem Urteil vom 23.9.2019 festgestellt, dass  der Bf. die oben angeführten Taten in objektiver und subjektiver Hinsicht begangen hat, und es  dabei billigend in Kauf nahm und sich damit abfand seine abgabenrechtliche Anzeige-,  Offenlegungs- bzw. Wahrheitspflicht zu verletzen und damit die im Spruch des Strafurteils  genannten Abgaben zu verkürzen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_186`)


Das Landesgericht für Strafsachen Wien hat die Abgabenforderungen, welche aufgrund der  Feststellungen der Betriebsprüfung, hinsichtlich Einkommensteuer und Umsatzsteuer,  festgesetzt wurden, bestätigt.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/143785.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143785.1_28`)


Dass der von der Sicherstellung betroffene  Abgabenmehrbetrag nicht korrekt berechnet worden ist, sei mittlerweile vom Landesgericht  für Strafsachen, von einem Gerichtssachverständigen im Strafverfahren und vom Spruchsenat  beim Amt für Betrugsbekämpfung festgestellt worden (Anmerkung: Die Beschwerde gegen den  Sicherstellungsauftrag ist mit Beschwerdevorentscheidung vom 23.07.2020 als unbegründet  abgewiesen worden; der Sicherstellungsauftrag ist rechtskräftig).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht  für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht  für Strafsachen`(organisation)
- `Amt für Betrugsbekämpfung`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/145202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145202.1_39`)


Sie werden jeweils vom Landesgericht für Zivilrechtssachen in  Wien bekanntgegeben und jährlich vom BMF unter www.bmf.gv.at veröffentlicht.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen in  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen in  Wien`(organisation)
- `BMF`(organisation)

</details>

---

## `FA_Location_Pattern_Fixed` 💣

**F1:** 0.002 | **Precision:** 0.318 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `41cddcd1`  
**Description:**
Matches 'FA' followed by complex location chains to prevent fragmentation, ensuring valid locations are matched.

**Content:**
```
\bFA\s+(?:Amstetten(?:\s+Melk(?:\s+Scheibbs)?)?|Kufstein(?:\s+Schwaz)?|St\.?\s*Johann(?:\s+Tamsweg(?:\s+Zell\s+am\s+See)?)?|Braunau(?:\s+Ried(?:\s+Sch\u00e4rding)?)?|Grieskirchen(?:\s+Wels)?|Wien(?:\s+\d+(?:/\d+)*\s*(?:Schwechat\s+Gerasdorf)?)?|Spittal\s+Villach|Steiermark\s+Mitte|Tirol\s+Ost|Gmunden\s+V\u00f6cklabruck|Lilienfeld\s+St\.?\s*P\u00f6lten|Baden(?:\s*M\u00f6dling)?|\u00d6sterreich|\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.318 | 0.001 | 0.002 | 44 | 14 | 30 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 30 | 16136 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hon.-Prof. Dragan Höh` (person)
- `ÖkR Mag.a Catharina Schmalenstrot` (person)
- `8.b Straße 126, 4632 Buchet, Österreich` (address)
- `Floriane Herppich` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_61`)


Die Ermittlungen im Zuge der Außenprüfung durch das FA Baden Mödling haben ergeben, dass  das Kfz seit dem Kauf im Jahre 2011 nachweislich nie zum Verkauf angeboten wurde, es nie  einen Ausstellungsraum bzw. einen Abstellplatz zur Besichtigung des Fahrzeuges gegeben hat.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/134859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134859.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Liu Leitgebel  in der Beschwerdesache Hon.-Prof.in Pascal Fredecke, MA BA,  Larchach 48, 7301 Girm, Österreich, über die Beschwerde vom 30. März 2021 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 15. Jänner 2021 betreffend Umsatzsteuer 2019 Steuernummer 40-437/5867  zu Recht  erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Amstetten Melk Scheibbs` | `FA Amstetten Melk Scheibbs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Liu Leitgebel` (person)
- `Hon.-Prof.in Pascal Fredecke, MA BA` (person)
- `Larchach 48, 7301 Girm, Österreich` (address)
- `40-437/5867` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Leitgebel  in der Beschwerdesache ÖkR Achmed von Lampe,  Kreuzbach 25, 6441 Köfels, Österreich, vertreten durch WIRTSCHAFTSTREUHAND Steuerberatung GmbH,  Ohlsdorferstraße 18, 4810 Gmunden, über die Beschwerde vom 31. Jänner 2020 gegen den  Bescheid des FA Steiermark Mitte  vom 28. Jänner 2020 betreffend Abweisung eines Antrages auf  Aussetzung der Einhebung gemäß § 212a BAO, Steuernummer 05-972/9664, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Leitgebel` (person)
- `ÖkR Achmed von Lampe` (person)
- `Kreuzbach 25, 6441 Köfels, Österreich` (address)
- `WIRTSCHAFTSTREUHAND Steuerberatung GmbH` (organisation)
- `05-972/9664` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Lindermeier  in der Beschwerdesache PhD Jeanne Goethemann, BSc,  Weindlau 45, 4230 Zudersdorf, Österreich, vertreten durch Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH, Stelzhamerstraße 14b, 4400 Steyr, über die Beschwerde vom  14.10.2011 gegen den Bescheid des FA Braunau Ried Schärding  vom 22.9.2011 betreffend Festsetzung von  Verspätungszuschlägen 1/2011 – 7/2011 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Lindermeier` (person)
- `PhD Jeanne Goethemann, BSc` (person)
- `Weindlau 45, 4230 Zudersdorf, Österreich` (address)
- `Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wilfried Herzog  in der Beschwerdesache Sheila Girlich, LLB,  Paukenstraße 516, 8272 Neusiedl, Österreich, über die Beschwerden vom 24. März 2018 gegen den Bescheid des FA Braunau Ried Schärding  datiert vom 7. März 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, vom  10. Juni 2020 gegen den Bescheid des Finanzamt Braunau Ried Schärding  datiert vom 12. Mai 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 und ebenfalls vom 10. Juni 2020 gegen  den Bescheid des Finanzamt Braunau Ried Schärding  datiert vom 13. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 13-479/9453  zu Recht erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2013 und 2014 werden gemäß  § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wilfried Herzog` (person)
- `Sheila Girlich, LLB` (person)
- `Paukenstraße 516, 8272 Neusiedl, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `13-479/9453` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/137686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Lubomir Elsayed  in der Beschwerdesache OMedR OMedR Jana Hammers,  Salvenweg 6, 4720 Oberrühringsdorf, Österreich, Tschechische Republik, über die Beschwerde vom 14. Jänner 2022 gegen den  Bescheid des FA Baden Mödling  vom 10. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 15-221/1221, u Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Lubomir Elsayed` (person)
- `OMedR OMedR Jana Hammers` (person)
- `Salvenweg 6, 4720 Oberrühringsdorf, Österreich` (address)
- `15-221/1221` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/142775.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laurin Niegeloh  in der Beschwerdesache des  Thaddäus Wischeid, Freudstraße 81, 3442 Neusiedl, Österreich, über die Beschwerde vom 10. November 2022 gegen den Bescheid  des FA St. Johann Tamsweg Zell am See  vom 21. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 18-226/2821  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Laurin Niegeloh` (person)
- `Thaddäus Wischeid` (person)
- `Freudstraße 81, 3442 Neusiedl, Österreich` (address)
- `18-226/2821` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/144589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144589.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Gerhard Kanzy  in der Angelegenheit der Parteien  VN1 Bf (Beschwerdeführerin), vertreten durch Herrn Dr. Walter Ganster, StB in 9100  Völkermarkt und FA Baden Mödling  als Amtspartei und als Gesamtrechtsnachfolger des Finanzamtes  FAA über die Beschwerde vom 2.5.2019 gegen den Bescheid des Finanzamtes FAA vom 3.4.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Gerhard Kanzy` (person)
- `Dr. Walter Ganster` (person)
- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/144851.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144851.1_13`)


Dem Fahrzeughalter, der FA Steiermark Mitte, wurde in der Folge ein Auftrag zur Lenkernennung erteilt  und anschließend das Verwaltungsstrafverfahren betreffend Parkometerabgabe gegen den  nunmehrigen Bf geführt.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/147492.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147492.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Wolf Volejnik  in der Beschwerdesache Wendy Hirschbiel,  Oberer Winkel 57, 4693 Kreut, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamt Bruck Eisenstadt Oberwart –  nunmehr FA Tirol Ost  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Wolf Volejnik` (person)
- `Wendy Hirschbiel` (person)
- `Oberer Winkel 57, 4693 Kreut, Österreich` (address)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/147515.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147515.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Jaden Thill  in der Beschwerdesache Elisabeth Grieß,  Obertösens 77, 4614 Au an der Traun, Österreich, über die Beschwerde vom 30. Dezember 2016 gegen die Bescheide des  FA Baden Mödling  vom 6. Dezember 2016 und vom 10. April 2017 betreffend Wiederaufnahme der  Verfahren betreffend Einkommensteuer für die Jahre 2010 bis 2014 sowie betreffend  Einkommensteuer 2010 bis 2014 sowie den Bescheid vom 22. März 2017 betreffend  Einkommensteuer 2015, Steuernummer 29-425/6527, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Jaden Thill` (person)
- `Elisabeth Grieß` (person)
- `Obertösens 77, 4614 Au an der Traun, Österreich` (address)
- `29-425/6527` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/148922.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148922.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Moses Vasylevskyy, Koralmblickweg 21, 3661 Lohsdorf, Österreich, vertreten durch Dr. Hugo Mlejnek  Wirtschaftstreuhand- gesellschaft m.b.H., Herrengasse 6-8/1/1, 1010 Wien, vom 28. April 2023  gegen den Bescheid des FA Steiermark Mitte  vom 11. April 2023 betreffend Säumniszuschlag 2023 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniela Regina Denk` (person)
- `Moses Vasylevskyy` (person)
- `Koralmblickweg 21, 3661 Lohsdorf, Österreich` (address)
- `Dr. Hugo Mlejnek  Wirtschaftstreuhand- gesellschaft m.b.H.` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Verena Khalidi  in der Beschwerdesache MedR Fiona Davydova,  St.-Anna-Park 16i, 5274 Unterhartberg, Österreich, vertreten durch Liepert Greussing Sturm Steuerberatung GmbH & Co KG,  Mühlgasse 21, 6700 Bludenz, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid  des FA Baden Mödling  vom 10. Jänner 2018 betreffend Haftungs- und Abgabenbescheid 2016  Steuernummer 96-418/3627  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Verena Khalidi` (person)
- `MedR Fiona Davydova` (person)
- `St.-Anna-Park 16i, 5274 Unterhartberg, Österreich` (address)
- `Liepert Greussing Sturm Steuerberatung GmbH & Co KG` (organisation)
- `96-418/3627` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_22`)


In der mündlichen Verhandlung vom 15. April 2015 wurde vereinbart, zunächst das  Rechtsmittelverfahren betreffend Rückabwicklung des Überrechnungsantrages beim FA 08  abzuwarten und bis dorthin das gegenständliche Beschwerdeverfahren zu vertagen."

**False Positives:**

- `FA 08` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_24`)


In der Beantwortung vom 18. April 2016 teilte die Bf. mit, dass „das Rechtsmittelverfahren  betreffend Rückabwicklung des Überrechnungsantrages m.W. nach beim FA 08 bis dato nicht  abgeschlossen ist, sodass nach wie vor der beantragte Unterbrechungsgrund vorliegt.“

**False Positives:**

- `FA 08` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_29`)


In den gegenständlichen Beschwerdeverfahren, die vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Salzburg-Land`(organisation)
- `BFG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_35`)


In den gegenständlichen Beschwerdeverfahren, das vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Salzburg-Land`(organisation)
- `BFG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Malik Stellmaszick, Am Weberbach 26, 9640 Gailberg, Österreich, über die Beschwerde vom 19. November 2012 gegen den Bescheid  des FA Wien 1/23 vom 8. November 2012 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2011, Steuernummer 92-110/0462  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 1/23 ` — partial — gold is substring of pred: `FA Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Monika Kofler`(person)
- `Malik Stellmaszick`(person)
- `Am Weberbach 26, 9640 Gailberg, Österreich`(address)
- `FA Wien 1/23`(organisation)
- `92-110/0462`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Delia Kavelmann  in der Beschwerdesache Larissa Rastätter,  Wendelgraben 27, 6563 Galtür, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und PhD Isaak Joern wird  abgewiesen.

**False Positives:**

- `FA Wien 9/18/19 ` — partial — pred is substring of gold: `FA Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Delia Kavelmann`(person)
- `Larissa Rastätter`(person)
- `Wendelgraben 27, 6563 Galtür, Österreich`(address)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)
- `PhD Isaak Joern`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133998.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Imre Wittek  über die Beschwerde des Lara Schwertzel,  Stockinger Straße 23, 4892 Schwandeck, Österreich, vertreten durch Mag. Ingrid Huber, Feldweg 7, 9241 Wernberg, vom  02.01.2017 gegen den Bescheid des Finanzamtes St. Veit Wolfsberg (nunmehr FA Österreich),  dieses vertreten durch Ilse König BA MA, vom 17.03.2016 betreffend Einkommensteuer 2010  (ANV) im fortgesetzten Verfahren den Beschluss gefasst:   Der Vorlageantrag wird gemäß § 264 Abs. 4 lit e BAO iVm § 260 Abs. 1 BAO als verspätet  zurückgewiesen.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Imre Wittek`(person)
- `Lara Schwertzel`(person)
- `Stockinger Straße 23, 4892 Schwandeck, Österreich`(address)
- `Mag. Ingrid Huber`(person)
- `Finanzamtes St. Veit Wolfsberg`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Frederike Bookholdt  in der Beschwerdesache DDr. Dr. Lorenz Wachenhusen,  Am Lurnbichl 4, 4871 Redl, Österreich, vertreten durch Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Eduard-Wallnöfer-Platz 1, 6460 Imst, über die Beschwerde vom  10. Juni 2013 gegen den Bescheid des FA Landeck Reutte (nunmehr FA Österreich) vom 15. Mai  2013, StrNr, betreffend Festsetzung der Normverbrauchsabgabe für den Zeitraum März 2012  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Frederike Bookholdt`(person)
- `DDr. Dr. Lorenz Wachenhusen`(person)
- `Am Lurnbichl 4, 4871 Redl, Österreich`(address)
- `Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_21`)


Die Beschwerde gelte als  fristgerecht eingebracht, wenn diese bis zum 10.09.2018 beim FA Baden-Mödling einlange.

**False Positives:**

- `FA Baden` — partial — pred is substring of gold: `FA Baden-Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Baden-Mödling`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_32`)


Mit Beschwerdevorentscheidung vom 25. Juli 2014 hat das FA Wien 2/20/21/22  die Beschwerde als  unbegründet abgewiesen.

**False Positives:**

- `FA Wien 2/20/21/22  ` — partial — gold is substring of pred: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_45`)


Die Franchiseverträge wurden in den  Streitjahren dem FA Wien 2/20/21/22  nicht vorgelegt.

**False Positives:**

- `FA Wien 2/20/21/22  ` — partial — gold is substring of pred: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_47`)


Diese hat darauf hin die  Franchisegebühren als umsatzsteuerrechtlich unecht befreit behandelt. Aus der Tatsache, dass  ein Franchisevertrag im Jahr 1998 der Großbetriebsprüfung vorgelegt wurde, ist aber für die  Beschwerdeführerin nichts zu gewinnen, da im Zuge der Veranlagung der Jahre 2005 bis 2009  ein Franchisevertrag nicht vorgelegt wurde und das FA Wien 2/20/21/22  daher im Zuge der  Umsatzsteuerveranlagung der Jahre 2005 bis 2009 keine Kenntnis des gesamten Sachverhaltes  hatte.

**False Positives:**

- `FA Wien 2/20/21/22  ` — partial — gold is substring of pred: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 2/20/21/22`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Gunderson  in der Beschwerdesache Florentin Mavrakis,  Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich, vertreten durch Intercura Treuhand - und Revisionsgesellschaft m.b.H.,  Langobardenstraße 51 Tür 6, 1220 Wien, über die Beschwerde vom 23. Dezember 2021 gegen  den Bescheid des FA Wien 2/20/21/22  vom 9. Dezember 2021 betreffend Festsetzung eines ersten  Säumniszuschlages, Steuernummer 95-900/0656, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 2/20/21/22  ` — partial — gold is substring of pred: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Björn Gunderson`(person)
- `Florentin Mavrakis`(person)
- `Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich`(address)
- `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `95-900/0656`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/136338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136338.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laurentia Wischnowski  in der Beschwerdesache Geraldine Tielschner, MSc,  Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Kitzbühel Lienz (nunmehr: FA Österreich) vom 12. Dezember 2019, SV-Nr,  betreffend die Abweisung des Antrages auf Zuerkennung der Familienbeihilfe (für die Tochter  B) für den Zeitraum Oktober 2018 bis September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Laurentia Wischnowski`(person)
- `Geraldine Tielschner, MSc`(person)
- `Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/137040.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137040.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Alois Steinfeldt  in der Beschwerdesache RgR Meinrad Leibküchler,  Hintersteindl 2, 5122 Kreil, Österreich, vertreten durch UnionTAX & LAW, Donau-City-Straße 7/DC Tower/30th Floor,  1220 Wien, betreffend Säumnisbeschwerde vom 8.4.2022 betreffend Einkommensteuer 2020  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Österreich  beschlossen:    Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.   Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Alois Steinfeldt`(person)
- `RgR Meinrad Leibküchler`(person)
- `Hintersteindl 2, 5122 Kreil, Österreich`(address)
- `Verwaltungsgerichtshof`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/138464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138464.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Constantin Mosmüller  in der Angelegenheit der Parteien   Sean Spies (Beschwerdeführer), vertreten durch die Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH, 1010 Wien und    FA Freistadt Rohrbach Urfahr  als Amtspartei und Gesamtrechtsnachfolger des FA Wien 2/20/21/22 betreffend die  Beschwerde vom 25.9.2020               gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 25.8.2020 betreffend  Abweisung eines Antrages auf Aufhebung des Einkommensteuerbescheides 2017 vom  28.6.2019 gem. § 299 BAO   den Beschluss gefasst:  Der Vorlageantrag des Beschwerdeführers vom 23.8.2022 gegen die  Beschwerdevorentscheidung vom 21.7.2022 über die Beschwerde gegen den Bescheid vom  25.8.2020 über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides  2017 vom 28.6.2019 gem. § 299 BAO   wird als unzulässig zurückgewiesen.

**False Positives:**

- `FA Wien 2/20/21/22 ` — partial — gold is substring of pred: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Constantin Mosmüller`(person)
- `Sean Spies`(person)
- `Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Freistadt Rohrbach Urfahr`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_39`)


Zur Klärung dieser Rechtsfrage wurde vom Fachbereich des FA  Wien 9/18/19 Klosterneuburg eine Anfrage (v. 26.11.2015) an den BUNDESWEITEN  FACHBEREICH gestellt. Im Rahmen der Schlussbesprechung wird von Seiten der Betriebsprüfung  von Lösung 2 ausgegangen - der Fremdwährungskursverlust im Jahr 2014 wird zur Gänze nicht  anerkannt.

**False Positives:**

- `FA  Wien 9/18/19 ` — partial — gold is substring of pred: `FA  Wien 9/18/19`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA  Wien 9/18/19`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/140065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140065.1_3`)


Begründung  Mit Erkenntnis des Bundesfinanzgerichtes vom 28.12.2022, RV/6100260/2013 u.a. wurde die  Bescheidbeschwerde der Revisionswerberin vom 14. April 2008 gegen den Bescheid des  Finanzamtes Österreich vom 14. März 2008 betreffend Umsatzsteuer 2006, die Beschwerden  vom 27.03.2013 gegen die Bescheide des FA Salzburg-Stadt (nunmehr FA Österreich) vom  17.12.2012 betreffend die Wiederaufnahme des Verfahrens für Umsatzsteuer für 2005 sowie  die Umsatzsteuer für 2005, 2007, 2008 und 2009 und die Körperschaftsteuer für 2008 und  2009, sowie die Beschwerden vom 31.03.2015 gegen die Bescheide des FA Salzburg-Stadt  (nunmehr FA Österreich) vom 12.03.2015 betreffend Umsatzsteuer 2010, 2011, 2012 und 2013  und die Körperschaftsteuer für 2010, 2011, 2012 und 2013 als unbegründet abgewiesen.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation
- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Finanzamtes Österreich`(organisation)
- `FA Salzburg-Stadt`(organisation)
- `FA Salzburg-Stadt`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/140299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140299.1_21`)


Daher stünde ihr für die Monate Jänner und Feber kein Pendlerpauschale und kein  Pendlereuro zu. Daher beantrage das FA, das Pendlerpauschale und den Pendlereuro nur für  10 Monate des Streitjahres zu gewähren:    1.680 €…….168x10 Pendlerpauschale lt. FA  108,30 €……10,83x10 Pendlereuro lt. FA

**False Positives:**

- `FA  108` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_26`)


Das FA verweist darauf, dass den Bf, mangels eigener Vorsteuerabzugsberechtigung, die Pflicht  zur Abfuhr der mittels korrigierter Rechnungen auf ihn übertragenen USt-Zahllast an das FA  2 von 24 Seite 3 von 24

**False Positives:**

- `FA  2` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/141878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141878.1_207`)


Es ist nicht strittig, dass dieser Frankenkredit eine betriebliche Verbindlichkeit war  (Vorlagebericht des FA 11.9.2019, Beschwerdevorentscheidung vom 11.6.2019), weil mit  diesem Frankenkredit der betriebliche Kontokorrentkredit Nr. KontoNR1Z sowohl im Jahr 1998,  als auch im Jahr 2006 abgedeckt wurde (Mails des Bf vom 26.2.2019 und vom 4.2.2019,  Kassajournal Oktober 2006, Nr. 610, Kto Nr. 2800;

**False Positives:**

- `FA 11` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/143536.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Mittermayer  in der Beschwerdesache Brendon Giese,  Schaumboden 25, 8253 Riegersbach, Österreich, über die Beschwerde vom 23. September 2022 gegen den Bescheid des  FA Wien 1/23  vom 25. August 2022 betreffend Einkommensteuer 2021, Steuernummer  04-144/4077, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `FA Wien 1/23  ` — partial — gold is substring of pred: `FA Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Mittermayer`(person)
- `Brendon Giese`(person)
- `Schaumboden 25, 8253 Riegersbach, Österreich`(address)
- `FA Wien 1/23`(organisation)
- `04-144/4077`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/145179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dario Ribbeck  in der Beschwerdesache Otto Koschinski,  Stockham 43, 3334 Gaflenz, Österreich, vertreten durch Dr. Michael Kotschnigg, Stadlauer Straße 39/I/Top12, 1220  Wien, über die Beschwerde vom 13. Februar 2023 gegen den Bescheid über die Festsetzung  von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens des FA Wien 8/16/17  vom  11. Jänner 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 8/16/17  ` — partial — gold is substring of pred: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dario Ribbeck`(person)
- `Otto Koschinski`(person)
- `Stockham 43, 3334 Gaflenz, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `FA Wien 8/16/17`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/145671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145671.1_254`)


31.12.2018 31.12.2019   € €  Einkünfte aus Gewerbebetrieb lt. FA 96.903,88 110.354,37  Teilwertabschreibung -57.469,28 -57.469,28  Einkünfte aus Gewerbebetrieb lt. BFG 39.434,60 52.885,09

**False Positives:**

- `FA 96` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_107`)


Dieses  Erkenntnis erging an die Bf und das FA Österreich, obwohl das FA für Großbetriebe zuständig  gewesen wäre.

**False Positives:**

- `FA Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_237`)


Bescheid vom 23.1.2014  -121.800 € Abzüglich Erhöhung durch FA  18.818,44 € BMG lt. Selbstberechnung der Bf 2012  36.000 € Erhöhung der BMG lt BFG im Verfahren  RV/4100608/2022  54.818,44 € Bemessungsgrundlage 2012 lt. BFG  2.466,83 € DB 2012 4,5%  16 von 75 Seite 17 von 75

**False Positives:**

- `FA  18` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_930`)


140.618,44 € Bemessungsgrundlage (BMG) lt. Bescheid  vom 23.1.2014 für 2012  -121.800 € Abzüglich Erhöhung lt. FA  18.818,44 € BMG lt. Selbstberechnung der Bf 2012  72.000 € Erhöhung lt. BFG: DB- und DZ-pflichtige  Zahlungen an die OG, den OG- Gesellschaftern (erster und zweiter  Stratege) zuzurechnen, nach Abzug der  bereits festgestellten vGA  90.818,44 € Bemessungsgrundlage 2012 lt. BFG  4.086,83 € DB 2012 4,5% lt.BFG  372,36 € DZ 2012 0,41% lt. BFG

**False Positives:**

- `FA  18` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149834.1_10`)


Die Abtretung des Akts vom FA 03 (nun DSt 03) an das FA 23 (nun DSt 23) vom 09.05.2018 war  Folge der Sitzverlegung der Bf von der Adresse in Wien, nach Bf A-Ort 1 mit 01.04.2016.

**False Positives:**

- `FA 03` — no gold match — likely missing annotation
- `FA 23` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Zollamt_Organization` 💣

**F1:** 0.001 | **Precision:** 0.294 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `518e5587`  
**Description:**
Matches 'Zollamt' and 'Zollamtes' as standalone organizations or followed by locations like 'Österreich'.

**Content:**
```
\bZollamt(?:es)?(?:\s+(?:\u00d6sterreich))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.294 | 0.000 | 0.001 | 17 | 5 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 12 | 17058 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_153`)


Zwar habe die TNT die Anmeldung im Namen der Empfänger beim Zollamt beantragt,  allerdings fehlte ihr die Vertretungsmacht.

| Predicted | Gold |
|---|---|
| `Zollamt` | `Zollamt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_56`)


Das Zollamt Österreich tritt am 1. Jänner 2021 an die  Stelle der am 31. Dezember 2020 zuständig gewesenen Zollämter.

| Predicted | Gold |
|---|---|
| `Zollamt Österreich` | `Zollamt Österreich` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_57`)


(2) Die am 31. Dezember 2020 bei einem Finanzamt oder Zollamt anhängigen Verfahren  werden von der jeweils am 1. Jänner 2021 zuständigen Abgabenbehörde in dem zu diesem  Zeitpunkt befindlichen Verfahrensstand fortgeführt.

| Predicted | Gold |
|---|---|
| `Zollamt` | `Zollamt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_127`)


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

| Predicted | Gold |
|---|---|
| `Zollamt Österreich` | `Zollamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Amt für  Betrugsbekämpfung` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_31`)


Das Bundesfinanzgericht gründet den festgestellten Sachverhalt auf den Inhalt der vom  Zollamt Österreich vorgelegten Verwaltungsakten und auf das Erkenntnis des  Bundesfinanzgerichtes vom 19. September 2025, GZ. RV/7200044/2023.

| Predicted | Gold |
|---|---|
| `Zollamt Österreich` | `Zollamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgerichtes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

**False Positives:**

- `Zollamtes` — partial — pred is substring of gold: `Zollamtes Feldkirch Wolfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Walter Summersberger`(person)
- `Florenzia Rutt`(person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich`(address)
- `Zollamtes Feldkirch Wolfurt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

**False Positives:**

- `Zollamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alfred Klaming`(person)
- `Calvin Gorol`(person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich`(address)
- `Helmut Binder`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_4`)


Entscheidungsgründe  Mit Bescheiden (Beschwerdevorentscheidungen) des Zollamtes Klagenfurt Villach vom 17. Juli  2018, GZlen.

**False Positives:**

- `Zollamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_8`)


Die im Zusammenhang mit den Vorlageanträgen vom 14. August 2018 gestellten Anträge auf  Aussetzung der Einhebung der mit den vorgenannten Beschwerdevorentscheidungen  festgesetzten Altlastenbeiträge und Nebenansprüche hat das Zollamt Klagenfurt Villach mit  den nunmehr bekämpften Bescheiden abgewiesen.

**False Positives:**

- `Zollamt` — partial — pred is substring of gold: `Zollamt Klagenfurt Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zollamt Klagenfurt Villach`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_9`)


Die dagegen erhobenen Beschwerden vom 11. Oktober 2018 wurden mit  Beschwerdevorentscheidungen des Zollamtes Klagenfurt Villach vom 19. Oktober 2018, GZlen.

**False Positives:**

- `Zollamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_12`)


Die Beschwerden vom 8. Mai 2015 gegen die Bescheide des Zollamtes Klagenfurt Villach vom  7. April 2015, GZlen.

**False Positives:**

- `Zollamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_67`)


Erstmals am 14.11.2011 sowie bei einer anschließend nochmaligen Kontrolle durch Zollorgane  wurde der Bf am inländischen Wohnsitz in A/XX angetroffen, wo auch das Fahrzeug Nissan  Pickup jeweils abgestellt war (Kontrollmitteilung des Zollamtes v. 28.11.2011 und  Sachverhaltsdarstellung der Finanzpolizei, undatiert).

**False Positives:**

- `Zollamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzpolizei`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Miroslav Spandl  in der Beschwerdesache Rebecca Wölzlein, LLM,  Lahnsattel 29x, 5203 Köstendorf, Österreich, vertreten durch Niederhuber & Partner Rechtsanwälte GmbH, Metahofgasse  16, 8020 Graz, über die Beschwerde vom 16. Juni 2023 gegen den Bescheid des Zollamtes  Österreich vom 12. Mai 2023, Zl. 230000/204741/03/2023, betreffend die Aussetzung der  Einhebung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zollamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Miroslav Spandl`(person)
- `Rebecca Wölzlein, LLM`(person)
- `Lahnsattel 29x, 5203 Köstendorf, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_4`)


Entscheidungsgründe  1. Sachverhalt   Mit Sammelbescheid des Zollamtes Österreich vom 28. November 2022,  Zl. 230000/211442/03/2022, wurden für die Beschwerdeführerin (Bf) gemäß § 201 Abs.1 und  Abs.2 Z.3 BAO iVm § 2 Abs.4, 3 Abs.1 Z.1, § 6 Abs.1 sowie § 7 Abs.1 des  Altlastensanierungsgesetzes (ALSAG) Altlastenbeiträge für das erste bis vierte Quartal 2018  (Bescheid I) in Höhe von € 481.261,20 sowie gemäß § 217 Abs.1 und 2 BAO ein  Säumniszuschlag in der Höhe von € 9.625,23, für das erste bis vierte Quartal 2019 (Bescheid II)  in Höhe von € 617.448,80 sowie gemäß § 217 Abs.1 und 2 BAO ein Säumniszuschlag in der  Höhe von € 12.348,98, für das erste bis vierte Quartal 2020 (Bescheid III) in Höhe von  € 433.375,20 sowie gemäß § 217 Abs.1 und 2 BAO ein Säumniszuschlag in der Höhe von  € 8.667,51 und für das erste Quartal 2021 (Bescheid IV) in Höhe von € 88.982,40 sowie gemäß  § 217 Abs.1 und 2 BAO ein Säumniszuschlag in der Höhe von € 1.779,65 festgesetzt.

**False Positives:**

- `Zollamtes Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_7`)


Mit Beschwerdevorentscheidung des Zollamtes Österreich vom 27. Februar 2023,  Zl. 230000/211442/07/2022, wurde die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Zollamtes Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_10`)


Mit Bescheid des Zollamtes Österreich vom 12. Mai 2023, Zl. 230000/204741/03/2023, wurde  der Antrag auf Aussetzung der Einhebung gemäß § 212a BAO abgewiesen.

**False Positives:**

- `Zollamtes Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_16`)


Mit Beschwerdevorentscheidung des Zollamtes Österreich vom 29. Juni 2023,  Zl. 230000/204741/04/2023, wurde die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Zollamtes Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `m_b_H_entities` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b28f1448`  
**Description:**
Matches companies ending in m.b.H. with strict boundaries.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\s&\-]+(?:\s+)?m\.b\.H\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1362 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_7`)


Mit Haftungsbescheid vom 22. Mai 2018 wurde der Bf. als ehemaliger Geschäftsführer für die  aushaftende Abgabenschuld der *** Gesellschaft m.b.H.in Höhe von € 43.875,92 in Anspruch  genommen.

**False Positives:**

- `Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bundesfinanzgericht_BFG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `da3d9429`  
**Description:**
Matches the full entity 'Bundesfinanzgericht (BFG)' to prevent splitting into two entities. Added as a high-priority rule to override the separate matching of 'Bundesfinanzgericht' and 'BFG'.

**Content:**
```
\bBundesfinanzgericht\s*\(BFG\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5bc0a015`  
**Description:**
Matches specific known company names ending in GmbH, ensuring 'Firma' is NOT included in the match.

**Content:**
```
\b(?:Fa\.?\s+)?(?:Krawcyk\s+Transport|Lexwildon|W\u00e4lz|Waldgart|WQOY\s+Telekom\s+Solutions|Glatzhofer\s+&\s+Matschek\s+Steuerberatungsgesellschaft|Digital\s+Lexwildon|Hoch-IT|Tax\s+Wood\s+Audit|Marsoner\s+\+\s+Partner|CONZEPT|Buuk\s+Logistik|Dorffenlem\s+Holz|Hoch-IT)\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMF_entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7958b7c2`  
**Description:**
Matches the specific abbreviation BMF as an organization.

**Content:**
```
\bBMF\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fa_GmbH_entities` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b77e978d`  
**Description:**
Matches companies starting with 'Fa.' (Firma) followed by a valid name (min 2 chars) and GmbH, ensuring the prefix is included and handling tight spacing.

**Content:**
```
\bFa\.?\s*([A-Z][A-Za-z0-9\s&\-]{1,}[A-Za-z0-9])\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 29 | 0 | 29 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 29 | 13798 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_25`)


Im Jahre 2010 wurden Arbeiten von Arbeitern der Beschwerdeführer GmbH durchgeführt,  welche jedoch nicht von dieser verrechnet werden konnten, da diese Arbeiten bereits über die  Fa.Nexlex GmbH abgerechnet wurden.

**False Positives:**

- `Fa. Nexlex GmbH` — positional overlap with gold: `Fa.Nexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Nexlex GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_46`)


Im  Jahre 2008 wurden 5 Rechnungen mit einem Gesamtvolumen von € 57.000,- von einer Fa.POU Bau GmbH  9999 Wien, (Z-Bau-Adresse), an die Beschwerdeführer GmbH gelegt.

**False Positives:**

- `Fa. POU Bau GmbH` — positional overlap with gold: `Fa.POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.POU Bau GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_54`)


lm Juni wurde eine Rechnung der Fa. Y-Montage GmbH in Höhe von € 35.000,- gegen diese  PRAP umgebucht.

**False Positives:**

- `Fa. Y-Montage GmbH` — partial — gold is substring of pred: `Y-Montage GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Y-Montage GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_96`)


Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH eingesetzt als Subunternehmer im Jahr 2009 um  Scheinfirmen handelt im vollen Umfang zurück gewiesen.

**False Positives:**

- `Fa. POU Bau GmbH` — positional overlap with gold: `Fa.POU Bau GmbH`
- `Fa. Y-Montage GmbH` — partial — gold is substring of pred: `Y-Montage GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.POU Bau GmbH`(organisation)
- `Y-Montage GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_98`)


Bei der Fa. Z- Bau Bau GmbH, kann dies sicher auch der damalige Auftraggeber der Bauvorhaben I-Straße,  9998 Wien und F-Gasse, 9997 Wien, die Fa. Zimmerei Groschang Holz GmbH  bestätigen.

**False Positives:**

- `Fa. Z- Bau Bau GmbH` — no gold match — likely missing annotation
- `Fa. Zimmerei Groschang Holz GmbH` — partial — gold is substring of pred: `Groschang Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Groschang Holz GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_383`)


Feststellbar ist in den vorliegenden Erlöskonten der Synkel-Versicherung GmbH allerdings, dass die Synkel-Versicherung GmbH von  Febr. – Dez 2008 laufend Bauleistungen für eine Fa ABC erbrachte und vereinzelt auch im  Jahr 2009 für dieses Unternehmen tätig war (lt. Rechtsmittel Fa Zimmerei Groschang Holz GmbH (nachfolgend Groschang Holz GmbH.  1.2.

**False Positives:**

- `Fa. Zimmerei Groschang Holz GmbH` — partial — gold is substring of pred: `Groschang Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Groschang Holz GmbH`(organisation)
- `Groschang Holz GmbH.`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_6`)


Begründung  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa.West Altrader GmbH  Dorf, wurde von einem Kontrollorgan der Parkraumüberwachung der Landes- polizeidirektion am 9. April 2021 um 17:50 Uhr in der gebührenpflichtigen Kurzparkzone in  1160 Wien, Haberlgasse 10, beanstandet, da der zur Beanstandungszeit im Fahrzeug hinter- legte Parkschein Nr. 123 nach den Wahrnehmungen des Kontrollorgans Spuren von entfernten  Entwertungen aufwies.

**False Positives:**

- `Fa. West Altrader GmbH` — positional overlap with gold: `Fa.West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.West Altrader GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_21`)


Mit E-Mail vom 17. Mai 2021 brachte die Fa.West Altrader GmbH bei der MA 67 folgendes Schreiben ein:  „An: MA 67 Lenkererhebung …  Es ist bei uns in der Firma leider ein IRRTUM passiert: Bei der Lenkererhebung – KO 681 EB vom  19.4.21 wurde leider eine falsche Person ausgefüllt. Anbei senden wir Ihnen nun die richtige  Person, welche das KFZ zu diesem Zeitpunkt gelenkt hat.

**False Positives:**

- `Fa. West Altrader GmbH` — positional overlap with gold: `Fa.West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.West Altrader GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_38`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, hat das Schreiben der Fa.West Altrader GmbH vom  17. Mai 2021 als Beschwerde gegen das an Gundula Doerfner  als Beschuldigten ergangene  Straferkenntnis vom 7. Mai 2021 gewertet und dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Fa. West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)
- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_39`)


Entgegen der Ansicht der Magistratsabteilung 67 kann der Schriftsatz der Fa.West Altrader GmbH nicht als  Beschwerde im Verwaltungsstrafverfahren des Gundula Doerfner  gewertet werden.

**False Positives:**

- `Fa. West Altrader GmbH` — positional overlap with gold: `Fa.West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_40`)


Weder tritt die  Fa.West Altrader GmbH in seinem Namen auf, noch beruft sie sich auf eine diesbezügliche Vollmacht.

**False Positives:**

- `Fa. West Altrader GmbH` — positional overlap with gold: `Fa.West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.West Altrader GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_41`)


Angesichts der Vorgeschichte und der eindeutigen Formulierung (vgl. Hengstschläger/Leeb,  AVG I (2. Ausgabe 2014) § 13 Rz 37) handelt es sich um eine Nachreichung im Verfahren der Fa.West Altrader GmbH betreffend Lenkerauskunft, wo eine im Nachhinein erfolgte Richtigstellung der am 23.  April 2021 erteilten Lenkerauskunft vorgenommen wurde.

**False Positives:**

- `Fa. West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Altrader GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_20`)


Begründend wurde ausgeführt, da es sich um den gleichen Sachverhalt wie im Jahr 2011  handle (korrigierter Lohnzettel der Fa.Recycling Traderlog GmbH nach einer Lohnsteuerprüfung) werde die  gesetzliche Rechtsmittelfrist daher als ausreichend erachtet.

**False Positives:**

- `Fa. Recycling Traderlog GmbH` — positional overlap with gold: `Fa.Recycling Traderlog GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Recycling Traderlog GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_25`)


Arbeitgeber  Fa.Recycling Traderlog GmbH  Aufgrund der dort festgestellten Sachverhalte wurde ein berichtiger Lohnzettel erstellt und  übermittelt (s. Einkommensteuerbescheid 2012 vom 19.06.2018)"

**False Positives:**

- `Fa. Recycling Traderlog GmbH` — positional overlap with gold: `Fa.Recycling Traderlog GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Recycling Traderlog GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_37`)


Mit Vorhalt vom 21.06.2021 wurde dem FA neben den Sachverständigengutachten der  Wehruntauglichkeitsbeschluss, die Bestätigung des ehemaligen Arbeitgebers AG1, die  Arbeitsbestätigung der Fa AG2 GmbH, Aktenvermerke vom 17.06.2021 samt Anhang und ein  Sozialversicherungsauszug übermittelt und das FA ersucht die angeführten Unterlagen an das  Sozialministeriumservice zur Erstellung eines Ergänzungsgutachtens weiterzuleiten.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_41`)


Lebensjahres eingegangene Beschäftigungsverhältnis des Bf als  Hilfsarbeiter bei der Tischlerei AG2 GmbH ein geschütztes Arbeitsverhältnis gewesen und habe  die Fa AG2 GmbH für die Beschäftigung des Bf staatliche Lohnkostenzuschüsse erhalten.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_85`)


LJ.   04.06.1996 18.06.1996  Krankengeldbezug    19.06.1996 12.07.2002 6 J u 1 M Tischlereihilfsarbeiter  bei der Fa. AG2  GmbH, Vollzeit  19.06.96-31.12.96  5.599,22 Euro  01.01.97-31.12.97  10.073,76 Euro  01.01.98-31.12.98  10.243,74 Euro  01.01.99-31.12.99  10.449,12 Euro  01.01.00-31.12.00  10.664,59 Euro  01.01.01-31.12.01  10.882,25 Euro  01.01.02-12.07.02  5.941,35 Euro  Mit Schreiben 19.02.2021 bestätigt die Fa.  AG2 GmbH (Tischlerei), dass der Bf im  genannten Zeitraum als Hilfsarbeiter tätig  war und es sich hierbei, aufgrund der  Einstufung des Bf als begünstigt behinderte  Person, um einen geschützten Arbeitsplatz  gehandelt hat   Am 00 vollendet der Bf sein 25.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation
- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_95`)


Dem an den Bf gerichteten Bescheid der Bezirkshauptmannschaft O vom 09.09.1996 ist zu  entnehmen, dass die Fa AG2 GmbH für die Dauer des Dienstverhältnisses einen monatlichen  Kostenzuschuss zu den Lohnkosten erhält, um die Minderung der Arbeitsleistung  auszugleichen.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_96`)


Laut des an die Fa AG2 GmbH adressierten Schriftsatzes der  Bezirkshauptmannschaft O vom 27.08.1997 betreffend den Bf wird ua festgehalten, dass das  Land B sich verpflichtet dem Arbeitgeber zum Ausgleich der verminderten Arbeitsproduktivität  7 von 16 Seite 8 von 16

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_151`)


Im Letztgutachten wurden als relevante Befunde angeführt:  -Versicherungsdatenauszug von 01.01.1991 bis 14.02.2021  - Mailverkehr BFG vom Juni 2021: Verein hat 100% der Lohnkosten erhalten  - AV 1 und 2 vom 17.06.2021: Bescheid der Bezirkshauptmannschaft O vom 09.09.1996  betreffend Kostenzuschuss zugunsten der Fa AG2 GmbH;   - Bestätigung AG1 vom 19.02.2021 gestütztes Dienstverhältnis  - Arbeitsbestätigung Fa AG2 GmbH vom 19.02.2021: geschützter Arbeitsplatz  - Bundesheer Stellungskommission 14.07.1993: untauglich wegen Intellegenzminderung –  Grenzfall, Hypotonie und Polyphagie.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation
- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_152`)


- Schreiben AMS O vom 15.09.1998 an Fa AG2 GmbH: Zuschuss in der Höhe von 30% der  fiktiven Lohnkosten auf der Basis eines Monatsbruttolohnes (ohne Sonderzahlungen) von  14.525,00 S für 40 Stunden pro Woche als Hilfsarbeiter im Tischlereibereich  Zusatzvereinbarung Land NÖ vom 27.08.1997: zu monatlicher Geldbeihilfe.

**False Positives:**

- `Fa. AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/140745.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140745.1_15`)


Lt. Vorhaltsbeantwortung im Zuge der Vor-BP bei der Fa. XY Immo GmbH wird das Facility  Management für die Anlagen und Gebäude der Fa. XY Immo GmbH sowie die  Finanzierungsverhandlungen bei Banken und Investoren durchgeführt.

**False Positives:**

- `Fa. XY Immo GmbH` — no gold match — likely missing annotation
- `Fa. XY Immo GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_49`)


Jene Firma, von der die Fytterer Handel GmbH hauptsächlich beliefert wird, ist die Fa.TraunBeratung GmbH  Der  Gesellschafter und Geschäftsführer der letztgenannten GmbH ist B.B., Ehegemahl der Bf..

**False Positives:**

- `Fa. TraunBeratung GmbH` — positional overlap with gold: `Fa.TraunBeratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fytterer Handel GmbH`(organisation)
- `Fa.TraunBeratung GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_50`)


Die  im Laufe der Betriebsprüfung bei der Fytterer Handel GmbH nachgereichten Eingangsrechnungen der Fa.TraunBeratung GmbH  die in der Belegsammlung der Fytterer Handel GmbH zum Teil nicht enthalten gewesen sind,  haben nur einen Teil der Abweichungen aufklären können.

**False Positives:**

- `Fa. TraunBeratung GmbH  die in der Belegsammlung der Fytterer Handel GmbH` — similar text (different position): `Fytterer Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fytterer Handel GmbH`(organisation)
- `Fa.TraunBeratung GmbH`(organisation)
- `Fytterer Handel GmbH`(organisation)

</details>

---

## `Derdonal_Garten_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fd896848`  
**Description:**
Matches the specific organization 'Derdonal-Garten AG'.

**Content:**
```
\bDerdonal-Garten\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht_Leoben` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f6e69d33`  
**Description:**
Matches the specific full entity 'Landesgericht Leoben' to prevent partial matching.

**Content:**
```
\bLandesgericht\s+Leoben\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Energie_Verdorfwald_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `68360f1e`  
**Description:**
Matches the specific organization 'Energie Verdorfwald GmbH'.

**Content:**
```
\bEnergie\s+Verdorfwald\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `St_Johann_Steuergesellschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f3b05ab4`  
**Description:**
Matches the specific organization 'St. Johann Steuerberatung GmbH'.

**Content:**
```
\bSt\.\s*Johann\s*Steuerberatung\s*GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schlaich_Bau_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `29066466`  
**Description:**
Matches the specific organization 'Schlaich Bau KG'.

**Content:**
```
\bSchlaich\s*Bau\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt_Für_Suffix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `884e4181`  
**Description:**
Matches 'Finanzamt für' followed by specific tax types to capture full organization names like 'Finanzamt für Gebühren'.

**Content:**
```
\bFinanzamt\s+für\s+(?:Gebühren|Gebühren,\s+Verkehrsteuern\s+und\s+Glücksspiel|Verkehrsteuern|Glücksspiel|Sonstige\s+Abgaben)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nieder_Unisyn_Manufaktur_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e2e36c54`  
**Description:**
Matches the specific organization 'Nieder Unisyn Manufaktur GmbH'.

**Content:**
```
\bNieder\s+Unisyn\s+Manufaktur\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unverdroß_Planung_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f2ddae90`  
**Description:**
Matches the specific organization 'Unverdroß Planung GmbH'.

**Content:**
```
\bUnverdroß\s+Planung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schniederjahn_Software_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9a4e6f4d`  
**Description:**
Matches the specific organization 'Schniederjahn Software KG'.

**Content:**
```
\bSchniederjahn\s+Software\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frieb_Causa_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4fb0e985`  
**Description:**
Matches the specific organization 'Frieb - Causa Steuerberatung GmbH'.

**Content:**
```
\bFrieb\s*-\s*Causa\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fritzenwallner_Gandler_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `35950354`  
**Description:**
Matches the specific organization 'Fritzenwallner-Gandler Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH'.

**Content:**
```
\bFritzenwallner-Gandler\s+Wirtschaftstreuhand-\s+und\s+Steuerberatungsgesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA_Wien_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `038e18a2`  
**Description:**
Matches the specific compound entity 'FA Wien' followed by numbers/letters to prevent 'FA' from being matched separately.

**Content:**
```
\bFA\s+Wien\s+[0-9/]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Werkunival_Verlag_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e82c18f`  
**Description:**
Matches the specific organization 'Werkunival-Verlag GmbH'.

**Content:**
```
\bWerkunival\-Verlag\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA_Braunau_Ried_Schärding` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `12f6cf9e`  
**Description:**
Matches the specific compound entity 'FA Braunau Ried Schärding'.

**Content:**
```
\bFA\s+Braunau\s+Ried\s+Sch\u00e4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `CENTURION_GmbH` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1ddaf0b2`  
**Description:**
Matches the specific organization 'CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH'.

**Content:**
```
\bCENTURION\s+Wirtschaftspr\u00fcfungs\-\s+und\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 12211 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135028.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135028.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Siegbert Wrosch  in der Beschwerdesache Laurence Loossmann,  Lichtenwaldstraße 79, 4715 Helmling, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Hegelgasse 8 Tür 14, 1010 Wien, über die Beschwerde vom 23. Juli 2021 gegen den  Bescheid des Finanzamt Innsbruck  vom 13. Juli 2021 betreffend Zahlungserleichterung, Steuernummer  05-940/6024, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `CENTURION Wirtschaftsprüfungs- und Steuerberatungs  GmbH` — partial — pred is substring of gold: `CENTURION Wirtschaftsprüfungs- und Steuerberatungs  GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Siegbert Wrosch`(person)
- `Laurence Loossmann`(person)
- `Lichtenwaldstraße 79, 4715 Helmling, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und Steuerberatungs  GmbH,`(organisation)
- `Finanzamt Innsbruck`(organisation)
- `05-940/6024`(tax_number)

</details>

---

## `Kraftost_Digital_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `831bcf8e`  
**Description:**
Matches the specific organization 'Kraftost-Digital AG'.

**Content:**
```
\bKraftost-Digital\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Novotny_Getränke_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `77eac6ce`  
**Description:**
Matches the specific organization 'Novotny Getränke GmbH'.

**Content:**
```
\bNovotny\s+Getränke\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hellfritsch_Immobilien_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb0966c8`  
**Description:**
Matches the specific organization 'Hellfritsch Immobilien GmbH'.

**Content:**
```
\bHellfritsch\s+Immobilien\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Versand_Seewil` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `78f5878a`  
**Description:**
Matches the specific organization 'Versand Seewil' (often followed by GmbH & Co KG).

**Content:**
```
\bVersand\s+Seewil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bruckdon-Cloud` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `56116193`  
**Description:**
Matches the specific organization 'Bruckdon-Cloud' (often followed by GmbH & Co KG).

**Content:**
```
\bBruckdon-Cloud\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `I_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3f05ca58`  
**Description:**
Matches the specific organization 'I AG'.

**Content:**
```
\bI\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag_Reumiller` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4fcf57c0`  
**Description:**
Matches the specific organization 'Mag. Manfred Reumiller, Wirtschaftsprüfung und Steuerberatung GmbH & Co KG'.

**Content:**
```
\bMag\.\s+Manfred\s+Reumiller,\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kantner_Wirtschaftstreuhand` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `59aed83d`  
**Description:**
Matches the specific organization 'Kantner Wirtschaftstreuhand und Steuerberatungs GmbH & Co OG'.

**Content:**
```
\bKantner\s+Wirtschaftstreuhand\s+und\s+Steuerberatungs\s+GmbH\s*&\s*Co\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesamt_Soziales` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e780755f`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamt\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Süd_Consynkel` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `63aca9a1`  
**Description:**
Matches the specific organization 'Süd Consynkel KG'.

**Content:**
```
\bS\u00fcd\s+Consynkel\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `xx_GmbH_Steuer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `075532e7`  
**Description:**
Matches the specific organization 'xx GmbH Steuerberatung und Wirtschaftsprüfung'.

**Content:**
```
\bxx\s+GmbH\s+Steuerberatung\s+und\s+Wirtschaftspr\u00fcfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `yy_Wirtschaftstreuhand` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `43d32b32`  
**Description:**
Matches the specific organization 'yy Wirtschaftstreuhand Gesellschaft mbH'.

**Content:**
```
\byy\s+Wirtschaftstreuhand\s+Gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GOBBS_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a8c00b92`  
**Description:**
Matches the specific organization 'GOBBS Steuerberatungs GmbH'.

**Content:**
```
\bGOBBS\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA_Grieskirchen_Wels` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `059aa92b`  
**Description:**
Matches the specific organization 'FA Grieskirchen Wels'.

**Content:**
```
\bFA\s+Grieskirchen\s+Wels\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Post_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d53b44ad`  
**Description:**
Matches 'Post AG' as a specific organization.

**Content:**
```
\bPost\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SK_Telecom_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fc6d890b`  
**Description:**
Matches 'SK Telecom' and variations like 'SK Telecom Co. Ltd' found in legal citations.

**Content:**
```
\bSK\s+Telecom(?:\s+Co\.\s+Ltd)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BDO_Assurance_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0131387b`  
**Description:**
Matches the specific organization 'BDO Assurance GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft'.

**Content:**
```
\bBDO\s+Assurance\s+GmbH\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BM_f_Finanzen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `814502a0`  
**Description:**
Matches the abbreviated form 'BM f für Finanzen' which appears in the training data.

**Content:**
```
\bBM\s+f\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Telekom_Organisation_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `54bc1260`  
**Description:**
Matches specific German telecom organizations including 'Deutsche Telekom AG', 'Deutschen Telekom AG', 'T-Mobile Austria GmbH', 'A1 Telekom Austria AG', and 'Hutchinson Drei Austria GmbH'. Handles genitive and nominative forms correctly.

**Content:**
```
\b(?:Deutsche\s+Telekom(?:\s+AG)?|Deutschen\s+Telekom(?:\s+AG)?|T-?Mobile\s+Austria\s+(?:GmbH|AG|Co\.\s+KG)|A1\s+Telekom\s+Austria\s+(?:GmbH|AG|Co\.\s+KG)|Hutchinson\s+Drei\s+Austria\s+(?:GmbH|AG|Co\.\s+KG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Austria_GmbH_AG_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `07b6dc31`  
**Description:**
Matches companies ending in 'Austria GmbH' or 'Austria AG' but requires a specific prefix (T-Mobile, A1, Hutchinson Drei) to avoid partial matches like 'Mobile Austria GmbH'.

**Content:**
```
\b(?:T-?Mobile|A1|Hutchinson\s+Drei)\s+Austria\s+(?:GmbH|AG|Co\.\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SNWG_Textil_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0dc03f90`  
**Description:**
Matches the specific organization 'SNWG Textil GmbH'.

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

## `Bonafide_Treuhand_Revisions_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c8d25f9`  
**Description:**
Matches the specific organization 'Bonafide Treuhand & Revisions GmbH'.

**Content:**
```
\bBonafide\s+Treuhand\s+&\s+Revisions\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AG_Organization_Pattern` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2362f5b8`  
**Description:**
Matches specific German corporate entities ending in 'AG' with strict context to avoid matching generic terms or partial names. Requires a known prefix or specific structure.

**Content:**
```
\b(?:Deutsche\s+Telekom(?:\s+AG)?|Deutschen\s+Telekom(?:\s+AG)?|Valdon\s+AG|A1\s+Telekom\s+Austria\s+AG|Hutchinson\s+Drei\s+Austria\s+AG|Post\s+AG|I\s+AG|Kraftost-Digital\s+AG|Derdonal-Garten\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 15584 |

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

## `KG_Organization_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6bf0c689`  
**Description:**
Matches specific KG entities including 'Wald Zorwaldmon KG' and 'X Wirtschaftstreuhand- und Steuerberatungs GmbH & Co KG'. Excludes generic 'Co KG' matches.

**Content:**
```
\b(?:Wald\s+Zorwaldmon\s+KG|X\s+Wirtschaftstreuhand-\s+und\s+Steuerberatungs\s+GmbH\s+&\s+Co\s+KG|Schniederjahn\s+Software\s+KG|Schlaich\s+Bau\s+KG|Süd\s+Consynkel\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Moser_Rechtsanwalts_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fb2f2efb`  
**Description:**
Matches the specific organization 'Moser Rechtsanwalts-GmbH' including the trailing comma if present.

**Content:**
```
\bMoser\s+Rechtsanwalts-GmbH(?:,)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt_Osterreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d0782371`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Österreich' specifically to ensure it is captured as a single entity.

**Content:**
```
\bFinanzamt(?:es)?\s+\u00d6sterreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Alpen_KI_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f5342b8`  
**Description:**
Matches the specific organization 'Alpen-KI GmbH'.

**Content:**
```
\bAlpen-KI\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `XY_GmbH_Co_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `785c8571`  
**Description:**
Matches 'XY- GmbH & Co KG' which was missing from the KG pattern.

**Content:**
```
\bXY-\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FIDAS_Graz_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `33ae92b9`  
**Description:**
Matches 'FIDAS Graz Steuerberatung GmbH'.

**Content:**
```
\bFIDAS\s+Graz\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA_Steiermark_Mitte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0c571cba`  
**Description:**
Matches 'FA Steiermark Mitte' specifically.

**Content:**
```
\bFA\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA_Spittal_Villach` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b0cf8a23`  
**Description:**
Matches 'FA Spittal Villach' specifically.

**Content:**
```
\bFA\s+Spittal\s+Villach\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Valdon_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `40667a21`  
**Description:**
Matches 'Valdon AG'.

**Content:**
```
\bValdon\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wald_Zorwaldmon_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `40999ba4`  
**Description:**
Matches 'Wald Zorwaldmon KG'.

**Content:**
```
\bWald\s+Zorwaldmon\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sudlexwil_Software_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `28770e3e`  
**Description:**
Matches the specific organization 'Sudlexwil-Software KG'.

**Content:**
```
\bSudlexwil-Software\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ost_Daten_KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `62d5917a`  
**Description:**
Matches the specific entity 'Ost-Daten KG' which was previously missing.

**Content:**
```
\bOst-Daten\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Alwilkraft_KI_AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1362c4f2`  
**Description:**
Matches 'Alwilkraft KI AG' as a specific organization.

**Content:**
```
\bAlwilkraft\s+KI\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht_Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d082a9d`  
**Description:**
Matches 'Bezirksgericht' followed by a location (e.g., Innsbruck) as an organization.

**Content:**
```
\bBezirksgericht\s+(?:Innsbruck|Wien|Salzburg|Linz|Graz|Klagenfurt|Bregenz|Eisenstadt|St.\s*P\u00f6lten|Amstetten|Baden|Braunau|Dornbirn|Feldkirch|Feldkirchen|Gmunden|Graz|Hallein|Horn|Innsbruck|Klagenfurt|Krems|Leoben|Leonding|Linz|Lustenau|Mistelbach|Mödling|Neunkirchen|Perg|Ried|Salzburg|Schwaz|St.\s*P\u00f6lten|Steyr|Telfs|Ternitz|Traun|Vöcklabruck|Waidhofen|Wels|Wien|Wolfsberg|Zwettl)\b
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

