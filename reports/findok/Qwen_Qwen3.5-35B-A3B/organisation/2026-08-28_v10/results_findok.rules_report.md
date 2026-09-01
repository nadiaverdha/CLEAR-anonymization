# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-28T15:33:22.504138

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-28_v10/config.yaml 
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
| Train sentences | 1351 |
| Validation sentences | 394 |
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
| Accuracy (exact match) | 96.8% |
| True Positives | 14989 |
| False Positives | 1287 |
| False Negatives | 3008 |
| Total Gold Entities | 17997 |
| Micro Precision | 92.1% |
| Micro Recall | 83.3% |
| Micro F1 | 87.5% |
| Macro F1 | 87.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Finanzpolizei` | 0.4% | 100.0% | 0.2% | 37 | 37 | 0 |
| `Oberster Gerichtshof` | 0.1% | 100.0% | 0.0% | 6 | 6 | 0 |
| `Verwaltungsgerichtshof` | 31.6% | 100.0% | 18.7% | 3374 | 3374 | 0 |
| `Pensionsversicherungsanstalt` | 0.7% | 100.0% | 0.3% | 62 | 62 | 0 |
| `Bundesministeriums für Finanzen` | 0.1% | 100.0% | 0.1% | 9 | 9 | 0 |
| `FA Steiermark Mitte` | 0.0% | 100.0% | 0.0% | 3 | 3 | 0 |
| `FA Baden Mödling specific` | 0.1% | 100.0% | 0.0% | 5 | 5 | 0 |
| `Universität Wien` | 0.2% | 100.0% | 0.1% | 21 | 21 | 0 |
| `BMI abbreviation` | 0.1% | 100.0% | 0.0% | 8 | 8 | 0 |
| `Gerichtshof der Europäischen Union` | 0.3% | 100.0% | 0.2% | 27 | 27 | 0 |
| `Bundesamt für Soziales und Behindertenwesen` | 0.6% | 100.0% | 0.3% | 51 | 51 | 0 |
| `FA Braunau Ried Schärding` | 0.0% | 100.0% | 0.0% | 3 | 3 | 0 |
| `Finanzamt für Großbetriebe` | 0.4% | 100.0% | 0.2% | 35 | 35 | 0 |
| `COFAG` | 0.1% | 100.0% | 0.1% | 12 | 12 | 0 |
| `BHAG` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `technoRent International GmbH` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Heinz Neuböck Wirtschaftstreuhand Gesellschaft m.b.H.` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Finanzamt Steiermark Mitte` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Magistrat der Stadt Wien` | 6.0% | 98.9% | 3.1% | 565 | 559 | 6 |
| `Bundesfinanzgericht` | 37.8% | 98.2% | 23.4% | 4281 | 4206 | 75 |
| `ÖGK abbreviation` | 0.4% | 97.5% | 0.2% | 40 | 39 | 1 |
| `Landespolizeidirektion` | 0.8% | 97.3% | 0.4% | 75 | 73 | 2 |
| `BFG abbreviation` | 20.8% | 96.3% | 11.7% | 2180 | 2100 | 80 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.3% | 95.8% | 0.1% | 24 | 23 | 1 |
| `AMS abbreviation` | 0.6% | 94.6% | 0.3% | 56 | 53 | 3 |
| `Finanzamt with location` | 0.3% | 93.5% | 0.2% | 31 | 29 | 2 |
| `Wiener Gemeinderates` | 0.6% | 91.5% | 0.3% | 59 | 54 | 5 |
| `BMF and BFH` | 1.8% | 89.1% | 0.9% | 183 | 163 | 20 |
| `Finanzamt` | 34.1% | 87.3% | 21.2% | 4364 | 3808 | 556 |
| `Fa. GmbH abbreviation` | 0.1% | 76.9% | 0.1% | 13 | 10 | 3 |
| `Landesgericht with city` | 0.1% | 66.7% | 0.0% | 12 | 8 | 4 |
| `Verwaltungsgericht Wien` | 0.1% | 58.3% | 0.0% | 12 | 7 | 5 |
| `Landesgericht standalone` | 0.1% | 50.0% | 0.1% | 18 | 9 | 9 |
| `Landesgerichts standalone` | 0.0% | 40.0% | 0.0% | 5 | 2 | 3 |
| `GmbH after article` | 1.9% | 34.7% | 1.0% | 507 | 176 | 331 |
| `GmbH & Co KG/OG` | 0.1% | 33.3% | 0.1% | 27 | 9 | 18 |
| `GmbH at sentence start or after punctuation` | 0.0% | 2.6% | 0.0% | 154 | 4 | 150 |
| `m.b.H. entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberatungsgesellschaft m.b.H.` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Snajdr E-Commerce GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Wien full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kraftost-Digital AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Novotny Getränke GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hellfritsch Immobilien GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `xx GmbH Steuerberatung und Wirtschaftsprüfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `yy Wirtschaftstreuhand Gesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Grieskirchen Wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH with date prefix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hoch-IT GmbH specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `H SteuerberatungsGmbH specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dorffenlem Holz KG specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberatung Dr. Alfred Sorger GmbH specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Wien double space` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Derdonal-Garten AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Post AG` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `SK Telecom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deutsche Telekom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgerichtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Energie Verdorfwald GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `St. Johann Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schlaich Bau KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt standalone` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nieder Unisyn Manufaktur GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frieb - Causa Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fritzenwallner-Gandler Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dreissigacker Möbel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `I AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `T-Mobile Austria GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schniederjahn Software KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unverdroß Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion Niederösterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `FA Wien 6/7/15` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young Steuerberatungs-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Werkunival-Verlag GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SNWG Textil GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GOBBS Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Assurance GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `A1 Telekom Austria AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Finanzpolizei` 🏆

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `f55e5202`  
**Description:**
Matches the specific entity 'Finanzpolizei'.

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

## `Oberster Gerichtshof` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `13ddee01`  
**Description:**
Matches 'Oberster Gerichtshof' and its genitive form 'Obersten Gerichtshofes'.

**Content:**
```
\b(Obersten\s+Gerichtshofes|Oberster\s+Gerichtshof)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 13295 |

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

## `Verwaltungsgerichtshof` 🏆

**F1:** 0.316 | **Precision:** 1.000 | **Recall:** 0.187  

**Format:** `regex`  
**Rule ID:** `fc569986`  
**Description:**
Matches the specific entity 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofes'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.187 | 0.316 | 3374 | 3374 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3374 | 0 | 14621 |

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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_235`)


Mehrwertsteuer-Richtlinie (RL  77/388/EWG), deren Rechtslage der nunmehr geltenden MwStSystRL (RL 2006/112/EG)  vergleichbar ist, und auf die dazu vertretene Rechtsansicht des Verwaltungsgerichtshofes  hinzuweisen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_247`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_261`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_69`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_70`)


Eine derartige Rechtsfrage liegt im zu beurteilenden Fall nicht vor, da die  Schätzungsberechtigung direkt auf den Grundlagen der Bundesabgabenordnung fußt, bzw. die  Schätzungsmethode in Einklang mit der dezidiert dargestellten Rechtsprechung des  Verwaltungsgerichtshofes steht.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_100`)


Der Verwaltungsgerichtshof hat in seinem Erkenntnis vom 15.09.2016, Ro 2015/15/0009,  Folgendes ausgesprochen:   „Begünstigungsfähig als außergewöhnliche Belastung ist grundsätzlich nur der durch die  Behinderung bedingte Mehraufwand, somit jener Aufwand, der über die typischen Kosten der  Lebensführung hinausgeht (vgl. VwGH vom 2. Juni 2004, 2003/13/0074, VwSlg. 7933/F).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_142`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_11`)


III. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_184`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  14 von 15 Seite 15 von 15

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_185`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_5`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_60`)


der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_61`)


Dies trifft nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes nicht zu, wenn die  in Betracht kommenden Normen klar und eindeutig sind (vgl. VwGH 6.4.2016, Ro  2016/16/0006 mit vielen weiteren Nachweisen).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_75`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_4`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_208`)


Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_210`)


Dies trifft nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes nicht zu, wenn die  in Betracht kommenden Normen klar und eindeutig sind (vgl. VwGH 6.4.2016, Ro  2016/16/0006 mit vielen weiteren Nachweisen).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_5`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_21`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es Aufgabe des  Vertreters, im Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran  gehindert haben, die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH  23.03.2010, 2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_23`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliegt Ihnen als Vertreter,  Nachweise dafür, wie viel Zahlungsmittel zur Verfügung gestanden sind und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_62`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es  Aufgabe des Geschäftsführers, darzutun, weshalb er den auferlegten Pflichten nicht  entsprochen habe, insbesondere nicht habe Sorge tragen können, dass die Gesellschaft die  angefallenen Abgaben entrichtet hat, widrigenfalls von der Abgabenbehörde eine schuldhafte  Pflichtverletzung angenommen werden darf (VwGH 22.9.1999, 96/15/0049).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_77`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes lastet auf dem Vertreter auch  die Verpflichtung zur Errechnung einer entsprechenden Quote und des Betrages, der bei  anteilsmäßiger Befriedigung der Forderungen der Abgabenbehörde zu entrichten gewesen  wäre (VwGH 28.2.2014, 2012/16/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_87`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_88`)


Nach der durch das  Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.1.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_96`)


Im Übrigen ist eine  Einbringlichmachung bei der Primärschuldnerin unzweifelhaft nicht gegeben, weshalb nach der  Rechtsprechung des Verwaltungsgerichtshofes die Frage der Einbringlichkeit der  Haftungsschuld beim Haftenden von der Abgabenbehörde bei ihren  Zweckmäßigkeitsüberlegungen vernachlässigt werden kann (VwGH 16.12.1999, 97/16/0006;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_101`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Verwaltungsgerichtes ist gemäß Art. 133 B-VG die Revision (nur)  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_102`)


Da diese Voraussetzungen im Beschwerdefall im Hinblick auf die oben  wiedergegebene Rechtsprechung des Verwaltungsgerichtshofes nicht vorliegen, war  auszusprechen, dass die Revision unzulässig ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_97`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_99`)


Rechtsfragen von grundsätzlicher  Bedeutung lagen nicht vor und ist das Gericht auch nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abgewichen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_32`)


Ob und gegebenenfalls wie der Bezieher die erhaltenen Beträge verwendet hat,  ist unerheblich (vgl. das Erkenntnis des Verwaltungsgerichtshofes vom 28.10.2009,  Geschäftszahl 2008/15/0329).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_51`)


Der Verwaltungsgerichtshof hat in einem Rechtssatz zu seinem Erkenntnis vom 28.11.2007,  Geschäftszahl 2007/15/0058, Folgendes festgehalten:  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_55`)


Der Verwaltungsgerichtshof hat ferner in einem Rechtssatz zu seinem Erkenntnis vom  21.09.2009, Geschäftszahl 2009/16/0081 Folgendes ausgeführt:  "Der Verzicht einer anspruchsberechtigten Person auf Bezug der Familienbeihilfe zugunsten des  anderen Elternteiles setzt nach § 2a FLAG voraus, dass das Kind, für das der  Familienbeihilfenanspruch besteht, zum gemeinsamen Haushalt der Eltern gehört (vgl. auch  das hg.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_64`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_65`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_67`)


Das Erkenntnis  stützte sich vielmehr auf den Gesetzestext und die angeführte Judikatur des  Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_181`)


In  Fällen, in denen beide Kriterien noch keine klare Abgrenzung zwischen einer selbständig und  einer nichtselbständig ausgeübten Tätigkeit ermöglichen, ist nach ständiger Rechtsprechung  des Verwaltungsgerichtshofes auf weitere Abgrenzungskriterien (wie etwa auf das Fehlen eines  Unternehmerrisikos oder die Befugnis, sich vertreten zu lassen) Bedacht zu nehmen (vgl VwGH  10.11.2004, 2003/13/0018 vS, sowie seitdem zB VwGH 22.3.2010, 2009/15/0200;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_201`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_4`)


Z 10/12 139,46  ST 2012 285,07  SZA 2012 1.554,94  SZB 2012 292,84  SZC 2012 168,36  Summe          59.286,56  Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_59`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes ist es  Aufgabe des Geschäftsführers, darzutun, weshalb er den auferlegten Pflichten nicht  entsprochen habe, insbesondere nicht habe Sorge tragen können, dass die Gesellschaft die  angefallenen Abgaben entrichtet hat, widrigenfalls von der Abgabenbehörde eine schuldhafte  Pflichtverletzung angenommen werden darf (VwGH 22.09.1999, 96/15/0049).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_74`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes lastet auf dem Vertreter auch  die Verpflichtung zur Errechnung einer entsprechenden Quote und des Betrages, der bei  anteilsmäßiger Befriedigung der Forderungen der Abgabenbehörde zu entrichten gewesen  wäre (VwGH 28.02.2014, 2012/16/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_80`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_82`)


Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.01.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_117`)


Im Übrigen ist eine  Einbringlichmachung bei der Primärschuldnerin unzweifelhaft nicht gegeben, weshalb nach der  Rechtsprechung des Verwaltungsgerichtshofes die Frage der Einbringlichkeit der  Haftungsschuld beim Haftenden von der Abgabenbehörde bei ihren  Zweckmäßigkeitsüberlegungen vernachlässigt werden kann (VwGH 16.12.1999, 97/16/0006).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_119`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_123`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_124`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_33`)


Dass ein Zustellmangel unterlaufen sei und der Bf. nicht rechtzeitig vom Zustellvorgang  Kenntnis erlangen habe können, sei nicht anzunehmen, habe er doch zum Vorhalt der  Verspätung nicht Stellung genommen, sondern lediglich seinen Einspruch neuerlich  übermittelt.  Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sei die Rechtsmittelfrist eine  zwingende, auch durch die Behörde nicht erstreckbare gesetzliche Frist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_76`)


Die Behörde hat dem Bf. - entsprechend der Judikatur des Verwaltungsgerichtshofes - mit  Verspätungsvorhalt vom 28. Jänner 2020 unter näheren Ausführungen zur Kenntnis gebracht,  dass sein am 11. Jänner 2020 mittels E-Mail eingebrachtes Rechtsmittel nach der Aktenlage  verspätet erscheine, und ihn aufgefordert, für den Fall einer nicht nur vorübergehenden  Abwesenheit von der Abgabestelle zum Zeitpunkt der Zustellung der Strafverfügung  entsprechende Bescheinigungsmittel vorzulegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_92`)


Zulässigkeit der Revision   Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine ordentliche Revision für die  belangte Behörde nicht zulässig, da das Erkenntnis nicht von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis nicht von  der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des VwGH nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_93`)


Die Revision ist im gegenständlichen Fall nicht zulässig, da in freier Beweiswürdigung von einer  ordnungsgemäßen Zustellung auszugehen war und sich die Rechtsfolge der Zurückweisung  wegen erwiesener Verspätung aus dem Gesetz ergibt, weshalb es sich auch um keine  Rechtsfrage von grundsätzlicher Bedeutung handelt.   Eine Revision an den Verwaltungsgerichtshof durch die beschwerdeführende Partei wegen  Verletzung in Rechten nach Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft  Gesetzes nicht zulässig, wenn in einer Verwaltungsstrafsache eine Geldstrafe von bis zu 750  Euro und keine (primäre) Freiheitsstrafe verhängt werden durfte und überdies im Erkenntnis  eine Geldstrafe von nicht mehr als 400 Euro verhängt wurde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_161`)


Gemäß § 33 TP 5 Abs. 1 GebG unterliegen Bestandverträge (§§ 1090 ff. ABGB) und sonstige  Verträge, wodurch jemand den Gebrauch einer unverbrauchbaren Sache auf eine gewisse Zeit  und gegen einen bestimmten Preis erhält, nach dem Wert im allgemeinen 1 v.H.   IV. Erwägungen:   Der Begriff des "Wertes" ist im Gesetz selbst nicht definiert, jedoch hat der  Verwaltungsgerichtshof in ständiger Judikatur die Auffassung vertreten, dass zum „Wert“ alle  jene Leistungen zählen, die der Bestandnehmer erbringen muss, um in den Gebrauch der  Bestandsache zu gelangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_163`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes zählen zum "Wert", von  dem die Gebühr für Bestandverträge zu berechnen ist, alle Leistungen, zu deren Erbringung  sich der Bestandnehmer verpflichtet hat, um in den Genuss des Gebrauchsrechtes an der  Bestandsache zu gelangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_193`)


Der Verwaltungsgerichtshof stellte in seinem Erkenntnis VwGH 07.10.1985, 85/15/0136 fest,  dass in allen Fällen eines echten Franchisevertrages der Franchisenehmer im eigenen Namen  und auf eigene Rechnung handelt. Darüber hinaus führte er aus, dass ein Franchisevertrag  immer nur dann vorliegt, wenn eine im Vertrag enthaltene Pacht einer unverbrauchbaren  14 von 19 Seite 15 von 19

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_237`)


Auf Grund der dargestellten Rechtslage, insbesondere im Hinblick auf das Erkenntnis des  Verwaltungsgerichtshofes vom 07.10.1985, 85/15/0136, worin dieser feststellt, dass ein  Franchisevertrag immer nur dann vorliegt, wenn eine im Vertrag enthaltene Pacht einer  unverbrauchbaren Sache vollkommen unberücksichtigt bleiben kann, bildet auch die  Franchisegebühr einen Bestandteil der Bemessungsgrundlage für die Rechtsgeschäftsgebühr.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_240`)


(siehe auch Vorlageantrag RZ 10)   V. Unzulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_241`)


Die getroffene Entscheidung entspricht der Judikatur des Verwaltungsgerichtshofes  07.10.1985, 85/15/0136 und des BFG 26.07.2016, RV/7100282/2010 sowie weitere, weshalb  eine Revision nicht für zulässig erachtet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_3`)


2.Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_69`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_51`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  4 von 5 Seite 5 von 5

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_52`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_3`)


Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_29`)


Zur Revision (Art. 133 Abs. 4 iVm Abs. 9 B-VG):  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_5`)


2. Eine Revision gegen dieses Erkenntnis an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) ist nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_592`)


Das Ergebnis eines derartigen Beweisverfahrens  ist der Kontrolle durch den Verwaltungsgerichtshof nur insofern zugänglich, als es sich um die  Beurteilung handelt, ob der Sachverhalt genügend erhoben ist und ob die bei der  Beweiswürdigung vorgenommenen Erwägungen schlüssig sind, also nicht den Denkgesetzen  oder dem allgemeinen Erfahrungsgut widersprechen (vgl.  etwa das hg.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_700`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  33 von 34 Seite 34 von 34

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `E.` (person)
- `Bundesfinanzgerichtes` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_701`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

## `Pensionsversicherungsanstalt` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `b5b984b4`  
**Description:**
Matches the specific entity 'Pensionsversicherungsanstalt'.

**Content:**
```
\b(Pensionsversicherungsanstalt)\b
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

## `Bundesministeriums für Finanzen` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `efdbc42a`  
**Description:**
Matches 'Bundesministeriums für Finanzen' and 'BM für Finanzen' when preceded by 'Verordnung des' or similar context.

**Content:**
```
(?:Verordnung\s+des\s+|des\s+)(Bundesministeriums\s+f\u00fcr\s+Finanzen|BM\s+f\u00fcr\s+Finanzen)
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

## `FA Steiermark Mitte` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `29901ca0`  
**Description:**
Matches 'FA Steiermark Mitte'.

**Content:**
```
\bFA\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 12227 |

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

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Leitgebel` (person)
- `ÖkR Achmed von Lampe` (person)
- `Kreuzbach 25, 6441 Köfels, Österreich` (address)
- `WIRTSCHAFTSTREUHAND Steuerberatung GmbH` (organisation)
- `05-972/9664` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/144851.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144851.1_13`)


Dem Fahrzeughalter, der FA Steiermark Mitte, wurde in der Folge ein Auftrag zur Lenkernennung erteilt  und anschließend das Verwaltungsstrafverfahren betreffend Parkometerabgabe gegen den  nunmehrigen Bf geführt.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/148922.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148922.1_1`)


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

</details>

---

## `FA Baden Mödling specific` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a2d3e40b`  
**Description:**
Matches the specific entity 'FA Baden Mödling' to ensure it is captured correctly.

**Content:**
```
\bFA\s+Baden\s+Mödling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 14528 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_61`)


Die Ermittlungen im Zuge der Außenprüfung durch das FA Baden Mödling haben ergeben, dass  das Kfz seit dem Kauf im Jahre 2011 nachweislich nie zum Verkauf angeboten wurde, es nie  einen Ausstellungsraum bzw. einen Abstellplatz zur Besichtigung des Fahrzeuges gegeben hat.

| Predicted | Gold |
|---|---|
| `FA Baden Mödling` | `FA Baden Mödling` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/137686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137686.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/144589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144589.1_2`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/147515.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147515.1_2`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


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

## `Universität Wien` 🏆

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `1b2f4223`  
**Description:**
Matches the specific entity 'Universität Wien' as an organisation.

**Content:**
```
\bUniversit\u00e4t\s+Wien\b
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

## `BMI abbreviation` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1cba19d0`  
**Description:**
Matches the abbreviation 'BMI' (Bundesministerium für Inneres) as an organisation, ensuring it is not a false positive in non-legal contexts.

**Content:**
```
\bBMI\b(?!\s*(?:Index|Index|\w))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 15192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_56`)


Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung – Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 11 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_58`)


1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_40`)


Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung - Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 1 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_41`)


Diese Verordnung regelt gemäß § 1 Z 1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_29`)


Zu Spruchpunkt I.  Die Polizeigrundausbildung ist in der Verordnung des Bundesministers für Inneres über die  Grundausbildungen für den Exekutivdienst (Grundausbildungsverordnung – Exekutivdienst  BMI), BGBl. II Nr. 153/2017, geregelt. Diese Verordnung wurde aufgrund der Bestimmungen  der §§ 26 und 144 BDG, des § 67 VBG und des §§ 1 Abs. 4 SPG erlassen.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_30`)


Diese Verordnung regelt gemäß § 1 Z. 1 für den Ressortbereich des Bundesministeriums für  Inneres (BMI) die Grundausbildung für den Exekutivdienst - Polizeigrundausbildung.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_73`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Missed by this rule (FN):**

- `Flughafen München` (organisation)
- `Frontex` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/146425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146425.1_47`)


Das Bundesfinanzgericht ist im angefochtenen Erkenntnis mit näherer Begründung zum  Ergebnis gelangt, die Polizeigrundausbildung - die zwar durch generelle Normen, und zwar  durch die Grundausbildungsverordnung - Exekutivdienst BMI, BGBl. II Nr. 153/2017, geregelt  ist - sei, nicht zuletzt im Hinblick auf das Gehalt der Auszubildenden, mit einer Lehre - in einem  Lehrberuf - nicht vergleichbar.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

</details>

---

## `Gerichtshof der Europäischen Union` 🏆

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `3d580358`  
**Description:**
Matches the specific entity 'Gerichtshof der Europäischen Union'.

**Content:**
```
\bGerichtshof\s+der\s+Europäischen\s+Union\b
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

## `Bundesamt für Soziales und Behindertenwesen` 🏆

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `9b8ec037`  
**Description:**
Matches the specific entity 'Bundesamt für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamt\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 51 | 51 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 51 | 0 | 17658 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_385`)


• Bindung an die Gutachten des Sozialministeriumservice  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die  Gutachten des Sozialministeriumservice (früher: Bundesamt für Soziales und  Behindertenwesen) gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch Lenneis/Wanke (Hrsg.), FLAG, 2. Aufl.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_26`)


Am 02.11.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor, beantragte die Abweisung und nahm wie folgt Stellung:  „Das Finanzamt ist bei der Beurteilung des Sachverhalts gemäß § 8 Abs. 6 FLAG 1967 an die  vom Bundesamt für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens ausgestellten Bescheinigungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

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

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

- `Finanzamt` (organisation)
- `Adam Safak` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_10`)


Das Finanzamt ersuchte das Bundesamt für Soziales und Behindertenwesen die Erstellung  eines ärztlichen Sachverständigengutachtens zu veranlassen und eine darauf basierende  Bescheinigung zu ers tellen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

- `Finanzamt` (organisation)
- `Bundesamtes für Soziales und Behindertenwesen` (organisation)
- `Finanzamt` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

## `FA Braunau Ried Schärding` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7bd4ca5b`  
**Description:**
Matches the specific entity 'FA Braunau Ried Schärding'.

**Content:**
```
\bFA\s+Braunau\s+Ried\s+Schärding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 15860 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/135301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135301.1_1`)


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

</details>

---

## `Finanzamt für Großbetriebe` 🏆

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `d865be93`  
**Description:**
Matches the specific entity 'Finanzamt für Großbetriebe' and its genitive form.

**Content:**
```
\bFinanzamt(?:es)?\s+für\s+Großbetriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 35 | 35 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 35 | 0 | 15776 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_27`)


Rechtliche Beurteilung  2.1. Übergang der Zuständigkeit zum 01.01.2021:  Gemäß § 323b Abs.1 BAO treten das Finanzamt Österreich und das Finanzamt für Großbetriebe  für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die Stelle des jeweils am  31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_32`)


Zur Amtspartei ab 01.01.2021:  Gemäß § 323b Abs.1 BAO treten das Finanzamt Österreich und das Finanzamt für Großbetriebe  für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die Stelle des jeweils am  31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Eleonore Rudloph` (person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_252`)


Partei des  Verfahrens ist nunmehr das Finanzamt für Großbetriebe als belangte Behörde, deren  Bezeichnung war somit im Spruch entsprechend richtig zu stellen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_55`)


Das Finanzamt Österreich und das Finanzamt für Großbetriebe treten für ihren  jeweiligen Zuständigkeitsbereich am 1. Jänner 2021 an die Stelle des jeweils am 31. Dezember  2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `Finanzamtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/140121.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140121.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Amy Feyh, Labaunalpe 46, 4870 Kropfling, Österreich, vertreten durch Mag. Christian Eisl, Gewerbestraße 14, 5301  Eugendorf, wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt für  Großbetriebe, betreffend Rückzahlung der österreichischen Abzugsteuer für das Jahr 2019,  beschlossen:  Das Beschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Großbetriebe` | `Finanzamt für  Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Amy Feyh` (person)
- `Labaunalpe 46, 4870 Kropfling, Österreich` (address)
- `Mag. Christian Eisl` (person)
- `Verwaltungsgerichtshof` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/140121.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140121.1_4`)


Auftrag an die belangte Behörde  Mit Beschluss vom 3. November 2022 wurde dem Finanzamt für Großbetriebe gemäß § 284  Abs. 2 BAO aufgetragen, zu entscheiden und eine Abschrift des Bescheides vorzulegen oder  anzugeben, warum eine Verletzung der Entscheidungspflicht nicht oder nicht mehr vorliegt.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/140121.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140121.1_5`)


Mitteilung des Finanzamtes für Großbetriebe  Mit Eingabe vom 23. Februar 2023 teilte das Finanzamt für Großbetriebe mit, dass es den  Bescheid über die Rückzahlung der österreichischen Abzugsteuer für das Jahr 2019 erlassen hat  und legte eine Abschrift des Bescheides vom 22. Februar 2023 vor.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_22`)


Anmerkung zum Sachverhalt: Die aktenführende Dienststelle des  Finanzamt Vorarlberg  hat sich an das für die PVA zuständige Finanzamt für Großbetriebe (kurz: FAG) mit  der Bitte um Prüfung dieses Lohnzettels gewendet.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt Vorarlberg` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/143534.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143534.1_60`)


Die Androhung und Verhängung einer Zwangsstrafe ist an einen, dem Finanzamt Freistadt Rohrbach Urfahr  oder dem  Finanzamt für Großbetriebe in einem Verfahren betreffend Abgaben gemäß § 213 Abs. 1 BAO  bekannt gegebenen Zustellungsbevollmächtigten zuzustellen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/143756.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143756.1_4`)


Mit Erkenntnis des Bundesfinanzgerichtes vom 21.12.2023, RV/3100688/2014, wurde die  Bescheidbeschwerde der Revisionswerberin vom 15.4.2011 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  (jetzt Finanzamt für Großbetriebe) vom 15.3.2011 betreffend Haftungsbescheid 2006,  Haftungsbescheid 2007 und Haftungsbescheid 2008 abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Gerald Sellemerten, Mühlgrabenweg 55, 7151 Wallern im Burgenland, Österreich  vertreten durch Glatzhofer & Matschek GmbH,  Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 31. März 2014  gegen die Bescheide des Finanzamtes für Großbetriebe je vom 23. Jänner 2014 betreffend  Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2009 - 2012 (Steuernummer  14-586/7014) zu Recht erkannt:   I. Die Beschwerde vom 31. März 2014 gegen die Bescheide betreffend Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag 2009 und 2011 wird gemäß § 279 BAO als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Gerald Sellemerten` (person)
- `Mühlgrabenweg 55, 7151 Wallern im Burgenland, Österreich` (address)
- `Glatzhofer & Matschek GmbH` (organisation)
- `14-586/7014` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/144911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Ophelia Kleinhenrich, Jägerheimweg 33, 9560 Unterberg, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau-City-Straße 7, 1220 Wien, über die  Beschwerde vom 28. Februar 2023 gegen den Bescheid des Finanzamtes für Großbetriebe vom  2. Februar 2023 betreffend Zwangsstrafen 2023 Steuernummer 26-626/5290  nach  Durchführung einer mündlichen Verhandlung am 22. April 2024 und 11. Juni 2024 in  Anwesenheit der Schriftführerin Tanja Grottenthaler zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Ophelia Kleinhenrich` (person)
- `Jägerheimweg 33, 9560 Unterberg, Österreich` (address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `26-626/5290` (tax_number)
- `Tanja Grottenthaler` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/144911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144911.1_29`)


Das Bankgeheimnis werde einerseits für die  Datenübermittlung It § 38 Abs 2 Z 10 BWG iVm § 4 Abs 1 GMSG beschränkt, andererseits auch  mit dem spezifischen Beschränkungstatbestand des § 38 Abs 3 BWG (iVm § 111 GMSG), der  festhält, dass sich ein Kreditinstitut auf das Bankgeheimnis insoweit nicht berufen kann, als die  Offenbarung des Geheimnisses zur Feststellung seiner eigenen Abgabepflicht erforderlich ist,  weshalb konsequenterweise das Finanzamt für Großbetriebe bei der steuerlichen Erfassung  des Kreditinstituts nicht gehindert sei, in dessen Geschäftsunterlagen einerseits Einsicht zu  nehmen, andererseits auch entsprechende Auskünfte iSd BAO zu verlangen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/144911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144911.1_101`)


Das zuständige Finanzamt ist das Finanzamt für Großbetriebe.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/145561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145561.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Hon.-Prof. Sebastian Dimitrijevski  in der Beschwerdesache  KommR Dietlind Kratkey, Friedhof der Namenlosen 15, 8952 Winklern, Österreich, über die Beschwerde vom 5. April 2024 gegen den Bescheid des  Finanzamtes für Großbetriebe vom 4. April 2024, mit dem der Antrag vom 12.10.2023 auf  Festsetzung des Energiekrisenbeitrag-Strom iSd Bundesgesetz über den Energiekrisenbeitrag- Strom (EKBSG) BGBl I 220/2022 idgF für den Zeitraum 12/2022 bis 06/2023 gemäß § 201 Abs 3  Z 1 BAO abgewiesen wurde, Steuernummer 17-577/2007, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sebastian Dimitrijevski` (person)
- `KommR Dietlind Kratkey` (person)
- `Friedhof der Namenlosen 15, 8952 Winklern, Österreich` (address)
- `17-577/2007` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/145629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145629.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter[...] in der Beschwerdesache Ulrike Philippzig, Klimaweg 7, 8543 Graschach, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH,  Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 21.6.2024 gegen den Bescheid des  Finanzamtes für Großbetriebe vom 28.5.2024 mit dem der Antrag vom 25.10.2023 auf  bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom iSd Bundesgesetz über den  Energiekrisenbeitrag-Strom (EKBSG) BGBl I 220/2022 idgF für den Zeitraum 12/2022 bis  06/2023 gemäß § 201 Abs 3 Z 1 BAO abgewiesen wurde, Steuernummer [...], zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrike Philippzig` (person)
- `Klimaweg 7, 8543 Graschach, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr.R. in der Beschwerdesache Joshua Kaphan,  Am Reinegg 13, 4772 Blindendorf, Österreich, über die Beschwerde vom 28. September 2015 gegen die Bescheide des  Finanzamtes für Großbetriebe (vormals des  Finanzamtes Baden Mödling ) vom 21. August  2015 betreffend die Kapitalertragsteuer für die Jahre 2011 bis 2013 zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Joshua Kaphan` (person)
- `Am Reinegg 13, 4772 Blindendorf, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_6`)


Das Finanzamt für  Großbetriebe wurde von Mag. Mag. (F.H) Michael Wukowits vom ehemaligen Finanzamt  Baden Mödling vertreten.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Großbetriebe` | `Finanzamt für  Großbetriebe` |

**Missed by this rule (FN):**

- `Mag. Mag. (F.H) Michael Wukowits` (person)
- `Finanzamt  Baden Mödling` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/146675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Dr. Adebiola Bayer in der Beschwerdesache  Jean Stapeler, Strittfeldstraße 9, 6260 Bruck am Ziller, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  betreffend die Beschwerden  vom 19. Dezember 2016 gegen den Körperschaftsteuerbescheid Gruppe 2014 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 1. Dezember 2016 gemäß der  Änderung nach § 295 Abs. 1 BAO vom 30. Jänner 2017,  vom 23. Februar 2018 gegen den Körperschaftsteuerbescheid Gruppe 2015 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 26. Jänner 2018 gemäß der Änderung  nach § 295 Abs. 1 BAO vom 15. Februar 2019,    vom 27. Februar 2019 gegen den Körperschaftsteuerbescheid Gruppe 2016 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 20. Februar 2019,    vom 18. Februar 2020 gegen den Körperschaftsteuerbescheid Gruppe 2017 des Finanzamtes  Wien 1/23 (nunmehr Finanzamt für Großbetriebe) vom 14. Februar 2020 sowie    vom 25. Mai 2020 gegen den Körperschaftsteuerbescheid Gruppe 2018 des Finanzamtes Wien  1/23 (nunmehr Finanzamt für Großbetriebe) vom 15. Mai 2020  den Beschluss:  Die Parteien werden gemäß § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Bundesfinanzgerichts in der gegenständlichen Beschwerdesache in Bezug auf die angeführten  angefochtenen Bescheide noch Beschwerdevorentscheidungen zu erlassen sind.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Jean Stapeler` (person)
- `Strittfeldstraße 9, 6260 Bruck am Ziller, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/146917.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146917.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Annemarie Volmer, Am Wiesenweg 11, 8543 Aigen, Österreich, über die Beschwerde vom 29. Dezember 2023 gegen den Bescheid  des Finanzamtes für Großbetriebe vom 18. September 2023 betreffend Bescheide über die  Festsetzung der Stabilitätsabgabe 2020 bis 2023, Steuernummer 46-357/8622  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Annemarie Volmer` (person)
- `Am Wiesenweg 11, 8543 Aigen, Österreich` (address)
- `46-357/8622` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/147088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147088.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Leopold Hattemer, Seifriedsedt 4, 9150 Penk, Österreich  vertreten durch Ernst & Young Steuerberatungs  GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 5. März 2024 gegen die  Bescheide des Finanzamtes für Großbetriebe vom 13. Dezember 2023 bzw. 17. und 29. Jänner  2024 die Festsetzung der Stabilitätsabgabe die Jahre 2018-2023 betreffend (Steuernummer xx  xxx/xxxx) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Leopold Hattemer` (person)
- `Seifriedsedt 4, 9150 Penk, Österreich` (address)
- `Ernst & Young Steuerberatungs  GmbH` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/147364.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ramon Launert  in der Beschwerdesache Romana Schnepf,  Hauptgraben 8, 7201 Neudörfl, Österreich, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer  Straße 19, 1220 Wien, über die Beschwerde vom 29. Dezember 2023 gegen die Bescheide des  Finanzamtes für Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr  2013 vom 15. November 2022, für die Jahre 2014 bis 2022 vom 27. September 2023, sowie die  Festsetzung der Sonderzahlung zur Stabilitätsabgabe gemäß § 201 BAO vom 4. Oktober 2023  bzw. über die Beschwerde vom 5. März 2024 gegen den Bescheid des Finanzamtes für  Großbetriebe betreffend die Festsetzung der Stabilitätsabgabe für das Jahr 2023 vom 10.  Jänner 2024, jeweils zur Steuernummer 54-767/5279, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Großbetriebe` | `Finanzamtes für Großbetriebe` |
| `Finanzamtes für  Großbetriebe` | `Finanzamtes für  Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Ramon Launert` (person)
- `Romana Schnepf` (person)
- `Hauptgraben 8, 7201 Neudörfl, Österreich` (address)
- `Ernst & Young Steuerberatungsgesellschaft m.b.H.` (organisation)
- `54-767/5279` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/148574.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148574.1_29`)


Die Rückerstattung der in Österreich abgeführten Lohnsteuer habe nach einem  entsprechenden Antrag gemäß § 240 Abs. 3 BAO beim Finanzamt für Großbetriebe zu erfolgen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Ingeborg Huellhorst, Untere Tanne 20, 4363 Wetzelsberg, Österreich  USA situiert, Steuernummer  67-628/2057, Tax-Identification-Number: XX1, vertreten durch KPMG Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, vom  9.07.2015 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr  Finanzamt für Großbetriebe) vom 8.05.2015, mit welchen die Anträge auf Rückzahlung von  2009 und 2010 einbehaltener und abgeführter Kapitalertragsteuer gemäß § 21 Abs. 1 Z 1a  KStG 1988, Antragsnummern: A1 und A2, abgewiesen wurden   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Ingeborg Huellhorst` (person)
- `Untere Tanne 20, 4363 Wetzelsberg, Österreich` (address)
- `67-628/2057` (tax_number)
- `KPMG Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Berufung vom  16.05.2013 der Bf.-, X- Street, O., US-Plz, TIN: 11, vertreten durch Vanas & Partner  Steuerberatungsgesellschaft mbH, Teinfaltstraße 9/7, 1010 Wien, gegen den Bescheid des  Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt für Großbetriebe), vom  18.04.2013, mit dem der Antrag vom 12.02.2013 auf vollständige Rückerstattung der 2011  einbehaltenen Kapitalertragsteuer von inländischen Dividenden, Evidenznummer: X2,  abgewiesen wurde  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Vanas & Partner  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_54`)


Auf Grund von Übergangsrecht ist die Berufung als Bescheidbeschwerde gemäß § 245 BAO von  dem an die Stelle des UFG getretenen Bundesfinanzgericht zu erledigen (§ 323 Abs. 38 BAO)  und ist belangte Behörde nunmehr das Finanzamt für Großbetriebe (§ 61 ‚BAO idF des Finanz- Organisationsreformgesetzes 2020).

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_305`)


Das Finanzamt für Großbetriebe beantragt daher weiterhin die Abweisung der Beschwerde  [Zitat Ende]“.

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Mag. Oskar Raczeck  über die Beschwerde vom 31.3.2014   der Benedikt Rehkopp , vertreten durch DI Mag. Gabriele Wiedergut, Steuerberaterin in 9500 Villach,  gegen die Bescheide des Finanzamt St. Johann Tamsweg Zell am See  vom 23.1.2014 (Gesamtrechtsnachfolger Finanzamt für  Großbetriebe) betreffend Festsetzung Dienstgeberbeitrag und des Zuschlages zum  Dienstgeberbeitrag 2011-2012   nach am 12.5.2021, 2.6.2021, 2.3.2023 und 16.10.2025 durchgeführten mündlichen  Verhandlungen   zu Recht erkannt:    Die bekämpften Bescheide werden abgeändert (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Finanzamt für  Großbetriebe` | `Finanzamt für  Großbetriebe` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Mag. Mag. Oskar Raczeck` (person)
- `Benedikt Rehkopp` (person)
- `DI Mag. Gabriele Wiedergut` (person)
- `Finanzamt St. Johann Tamsweg Zell am See` (organisation)

</details>

---

## `COFAG` 🏆

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `9ffc9ec9`  
**Description:**
Matches the specific Austrian organization 'COFAG' as a standalone word, excluding compound forms like 'COFAG-NoAG' or 'COFAG-Beihilfen'.

**Content:**
```
\bCOFAG\b(?!-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 0 | 5786 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_55`)


Zu Tz. 1 des Berichtes über die Außenprüfung:  Die Förderung (FKZ 800T) sei als Einnahme 2021 verbucht worden, weil sie in diesem Jahr von  COFAG ausbezahlt wurden sei.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_129`)


Laut Punkt 2.3. des Anhanges zur Verordnung des Bundesministers für Finanzen gemäß § 3b  Abs. 3 des ABBAG-Gesetzes betreffend Richtlinien über die Gewährung von Zuschüssen zur  Deckung von Fixkosten durch die COVID-19 Finanzierungsagentur des Bundes GmbH (COFAG)  wurde Die COFAG vom Bundesminister für Finanzen beauftragt, Zuschüsse zur Deckung von  Fixkosten für Unternehmen zu gewähren, die durch die Ausbreitung von COVID-19 im Zeitraum  16. März 2020 bis 15. September 2020 Umsatzausfälle erleiden („Fixkostenzuschüsse“).

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |
| `COFAG` | `COFAG` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_3`)


Entscheidungsgründe  1. Verfahrensgang und Parteienvorbringen  Mit Bescheid vom 14.11.2024 hat die belangte Behörde von der beschwerdeführenden Partei  (bfP) den von der COFAG geleisteten Fixkostenzuschuss I für den Zeitraum 16.3.2020 bis  15.6.2020 in Höhe von 34.685,34 € zurückgefordert.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_50`)


Folglich konnte kein berechtigtes Vertrauen in die Zinslosigkeit allfälliger Rückforderungen  durch die COFAG bestanden haben, in welchem die beschwerdeführende Partei durch die  Erlassung des COFAG-NoAG hätte enttäuscht werden können.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_53`)


Ob die COFAG die ihr zustehenden Zinsen bei ihren  Rückforderungen geltend machte oder nicht, spielt in diesem Zusammenhang keine Rolle.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_31`)


Wurde nach der Zahlung des  ersten Auszahlungsteilbetrages von der COVID-19 Finanzierungsagentur des Bundes  GmbH (COFAG) ein negativer Auszahlungsteilbetrag (§ 2 Abs. 6 COFAG-NoAG) oder ein  Betrag aus einer Rückforderung bzw. eine Saldierung auf null nach Verrechnung (§ 2  Abs. 7 COFAG-NoAG) bekannt gegeben, beginnt die Verzinsung mit dem Zeitpunkt  dieser Bekanntgabe.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_42`)


Der Sachverhalt wurde im Vorlagebericht (eine Ausfertigung davon wurde vom FA der Bf. zu  Handen ihrer steuerlichen Vertretung übermittelt) wie folgt dargestellt:  „Das Unternehmen gehört einem Unternehmensverband an und hat als  Beihilfenempfänger Obergrenzen überschreitende Förderungen der COFAG erhalten.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_47`)


Das Unternehmen ist der Ansicht, dass die Verzinsung laut COFAG NoAG  verfassungsrechtlich bedenklich ist.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/148593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148593.1_57`)


Erwägungen  Im gegenständlichen Fall wurde in der Beschwerde kein Antrag auf Unterlassung der  Beschwerdevorentscheidung gemäß § 262 Abs. 2 BAO gestellt.  Die belangte Behörde stützt die direkte Vorlage ausdrücklich auf § 262 Abs. 3 BAO und führte  dazu im Vorlagebericht aus, dass die Verzinsung laut COFAG NoAG nach Ansicht der Bf.  verfassungsrechtlich bedenklich sei.

| Predicted | Gold |
|---|---|
| `COFAG` | `COFAG` |

</details>

---

## `BHAG` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d26651f`  
**Description:**
Matches the specific entity 'BHAG' (Bundesheer-Haftpflichtversicherungsgesellschaft or similar context).

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

## `technoRent International GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11355548`  
**Description:**
Matches the specific entity 'technoRent International GmbH'.

**Content:**
```
\btechnoRent\s+International\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 6288 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142803.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142803.1_83`)


Der EuGH hätte in seiner Entscheidung in der RS C-844/19 technoRent International GmbH klar  zum Ausdruck gebracht, dass der Grundsatz der steuerlichen Neutralität der Mehrwertsteuer -  auch wenn Art. 183 der Mehrwertsteuerrichtlinie weder eine Pflicht zur Zahlung von Zinsen auf  den zu erstattenden Vorsteuerüberschuss vorsieht noch angibt, ab wann solche Zinsen zu  zahlen wären - , es verlange, dass die finanziellen Verluste, die dadurch entstehen, dass ein  Vorsteuerüberschuss nicht innerhalb einer angemessenen Frist erstattet wird, durch die  Zahlung von Verzugszinsen ausgeglichen werden (Urteile vom 28. Februar 2018, Nidera, C- 387/16, EU:C:2018:121, Rn. 25, und vom 14. Mai 2020, Agrobet CZ, C-446/18, EU:C:2020:369,  Rn. 40).

| Predicted | Gold |
|---|---|
| `technoRent International GmbH` | `technoRent International GmbH` |

</details>

---

## `Heinz Neuböck Wirtschaftstreuhand Gesellschaft m.b.H.` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `983d7a88`  
**Description:**
Matches the specific entity 'Heinz Neuböck Wirtschaftstreuhand Gesellschaft m.b.H.' which was previously missed.

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

## `Finanzamt Steiermark Mitte` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6493730a`  
**Description:**
Matches the specific entity 'Finanzamt Steiermark Mitte' to ensure it is captured correctly.

**Content:**
```
\bFinanzamt\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 15001 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Merlin Thorschmidt` (person)
- `Adrian Radakovitsch` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)

</details>

---

## `Magistrat der Stadt Wien` 🏆

**F1:** 0.060 | **Precision:** 0.989 | **Recall:** 0.031  

**Format:** `regex`  
**Rule ID:** `b1a17d61`  
**Description:**
Matches the Vienna City Administration entity including genitive forms and department details, handling double spaces and irregular spacing.

**Content:**
```
\b(Magistrat(?:es)?\s{1,2}der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?)\b
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

## `Bundesfinanzgericht` 🏆

**F1:** 0.378 | **Precision:** 0.982 | **Recall:** 0.234  

**Format:** `regex`  
**Rule ID:** `bb32e55a`  
**Description:**
Matches the specific German tax court entity 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichtes'.

**Content:**
```
\bBundesfinanzgericht(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.982 | 0.234 | 0.378 | 4281 | 4206 | 75 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4206 | 75 | 13791 |

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

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_93`)


c. Rechtsgrundlagen, rechtliche Würdigung  Beweiswürdigung  Gem. § 167 Abs. 2 BAO haben die Abgabenbehörde und das Bundesfinanzgericht unter  sorgfältiger Berücksichtigung der Ergebnisse des Abgabenverfahrens nach freier Überzeugung  zu beurteilen, ob eine Tatsache als erwiesen anzunehmen ist oder nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_97`)


Das Bundesfinanzgericht hat – wie auch das Finanzamt - die abgabepflichtigen Fälle zu  erforschen und von Amts wegen die tatsächlichen und rechtlichen Verhältnisse zu ermitteln,  die für die Abgabepflicht und die Erhebung der Abgaben wesentlich sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_47`)


In der weiteren Folge beantragte der Bf. die Beschwerdevorlage an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_51`)


Das Bundesfinanzgericht hat erwogen:  1.1. Zu Spruchpunkt I. (teilweise Stattgabe)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Rainer Leutheußer` (person)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich` (address)
- `Egger & Freidorfer Steuerberatungs-OG` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_44`)


Nach Einbringung eines Vorlageantrages ohne ergänzendem Vorbringen ersuchte das  Bundesfinanzgericht den Bf. den Sachverhalt betreffend die Gerichtsverfahren beim  Handelsgericht Wien und beim Arbeitsgericht darzulegen und mit entsprechenden  Beweismitteln nachzuweisen;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erzielte im streitgegenständlichen Jahr als Vorstand der H. AG Einkünfte aus  nichtselbständiger Tätigkeit;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `H. AG` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_97`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_9`)


Mit Beschluss vom 23.4.2014 hat das  Bundesfinanzgericht die Beschwerde gegen den Feststellungsbescheid als unzulässig  zurückgewiesen, weil die Bescheide nicht ordnungsgemäß adressiert waren.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_19`)


II. Das Bundesfinanzgericht hat erwogen:  1. Rechtliche Beurteilung  1.1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_38`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Monika Kofler` (person)
- `Maximilian Joobs` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Streitpunkte:  Die Bf. lebt auch nach eigenen Angaben seit 3. Juli 2019 nicht mehr mit ihren Kindern in einem  gemeinsamen Haushalt. Ab 4.7.2019 war der Kindesvater an einer gemeinsamen Adresse mit  den Kindern gemeldet und lebte mit diesen unstrittig in einem gemeinsamen Haushalt. Die  Verständigung des Finanzamtes durch die Bf. erfolgte erst am 27.8.2019, als die  Familienbeihilfe bereits überwiesen worden war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_64`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_133`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_134`)


Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:  Herr [B] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Aufräumen von Baustellen, bestehend im Zusammentragen und  eigenverantwortlichem Trennen von Bauschutt und -abfällen entsprechend der  Wiederverwertbarkeit‚ einschließlich des Bereitstellens zum Abtransport sowie im  Reinigen von Baumaschinen und Bauwerkzeugen durch Beseitigen von Rückständen  mittels einfacher mechanischer Methoden, wie Abkratzen, Abspachteln und dergleichen  und nachfolgendem Abspritzen mit Wasser, unter Verwendung ausschließlich eigener  Arbeitsgeräte sowie unter Ausschluss der den Denkmal-, Fassaden- und  Gebäudereinigern vorbehaltenen Tätigkeiten einer Grund- oder Bauschlussreinigung“  Herr [A] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Heben, Senken und Befördern von Lasten mittels Einsatzes von mechanischen oder  maschinellen Einrichtungen unter Ausschluss der Beförderung mittels Kraftfahrzeugen“  Herr [B] und Herr [A] führten im Beschwerdezeitraum Baustellenarbeiten entsprechend ihren  Gewerbeberechtigungen für den Beschwerdeführer aus.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_172`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsstellungen  gemäß § 167 Abs 2 BAO als erwiesen annehmen

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_201`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof. Niels Aleksejew` (person)
- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_29`)


Gegen diesen Bescheid erhob die Bf. durch ihren rechtsfreundlichen Vertreter Beschwerde,  warf der belangten Behörde mangelnde Sachverhaltsermittlung, Beweiswürdigung,  Aktenwidrigkeit und Begründung vor und stellte den Antrag, die Beschwerde ohne Erlassung  einer Beschwerdevorentscheidung dem Bundesfinanzgericht vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_49`)


II. Das Bundesfinanzgericht hat erwogen:  Die zur Vertretung juristischer Personen berufenen Personen und die gesetzlichen Vertreter  natürlicher Personen haben alle Pflichten zu erfüllen, die den von ihnen Vertretenen obliegen,  und sind befugt, die diesen zustehenden Rechte wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_119`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Anna Radschek` (person)
- `Rudolf Schlohsmacher` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_23`)


Er stelle daher  den Antrag, die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_25`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

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

## `ÖGK abbreviation` 

**F1:** 0.004 | **Precision:** 0.975 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `72adaf79`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse) as an organisation.

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.975 | 0.002 | 0.004 | 40 | 39 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 39 | 1 | 15587 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_52`)


Mit Telefax vom 30. November 2020 übermittelte die Österreichische Gesundheitskasse    - ein Schreiben der Pensionsversicherungsanstalt vom 23. Jänner 2018, wonach Bf ab 8. Juni  2016 für die Dauer der vorübergehenden Invalidität Anspruch auf Rehabilitationsgeld hat  - eine Auszahlungsbestätigung der ÖGK vom 27. November 2020, wonach das ganze  Rehabilitationsgeld  für den Zeitraum 8. Juni 2016 bis 31. Dezember 2017 zur Gänze und jenes  für 1. Jänner bis 28. Februar 2018 zum Teil – insgesamt  18.262,20 €  einbehalten worden ist  - ein Schreiben der ÖGK vom 27. November 2020, wonach der Einbehalt der 18.262,20 € des  Rehabilitationsgeldes des Zeitraumes 1.7.2016 bis 28.2.2018  für die bedarfsorientierte  Mindestsicherung gemäß § 324 ASVG erfolgt ist   Am 3. Dezember 2020 übermittelte das erkennende Gericht dem Finanzamt die an die  Bezirkshauptmannschaft und die Österreichische Gesundheitskasse gerichteten  Amtshilfeersuchen samt den dazu eingelangten Unterlagen zur Kenntnis.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `Pensionsversicherungsanstalt` (organisation)
- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_10`)


bei den Honorarnoten  wurden zudem die Kostenersätze der ÖGK berücksichtigt (Bescheid vom 22.10.2020).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_26`)


Beweiswürdigung  Die Höhe der beantragten Krankheitskosten ergibt sich aus den vorgelegten Unterlagen  (Aufstellung Krankheitskosten bzw. Fahrtkosten, Honorarnoten, Schreiben der ÖGK bzgl.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_13`)


Aus der Beilage ÖGK gehe  hervor, dass die Heilbehandlungen sowohl ärztlich verschrieben als auch die Kosten teilweise  von der SV erstattet worden seien.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_25`)


Der BF hatte im Jahr 2019 Kosten der Heilbehandlung im Zusammenhang mit der Behinderung  in Höhe von € 1.804,00, die sich folgendermaßen zusammensetzen:  S Heilmassagen (abzüglich € 26,00 Ersatz ÖGK)  €    568,50  Apotheke Rezeptgebühren       €    140,30  Fahrtkosten         € 1.095,20  Die Fahrtkosten in Höhe von € 1.095,20 setzen sich folgendermaßen zusammen:  Dr. B in LG:   40 km x 0,42 = € 16,80  Orthopädie F in ON:   3 x 2 Fahrten a 23,8 km = 142,8 km x 0,42 = € 60,00  Dr. M in R:    27 Hinfahrten a 44,6 km laut Routenplaner = 1.204,20 km x 0,42 = 505,80  27 Rückfahrten a 45,2 km laut Routenplaner = 1.220,40 km x 0,42 = 512,60

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/139366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139366.1_8`)


Die Beschwerdeführerin ersuchte mit Vorlageantrag vom 5.8.2021 um Nichtberücksichtigung  der von der ÖGK überwiesenen Beträge;

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_13`)


Der Beschwerde war eine  Rehabilitationsgeldbestätigung der ÖGK vom 3.5.2022 beigelegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_19`)


Dem Vorlageantrag waren ein Schreiben der Pensionsversicherungsanstalt vom 24.3.2021 und  Bestätigungen der ÖGK hinsichtlich der Nachzahlungen des Rehabilitationsgeldes beigelegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `Pensionsversicherungsanstalt` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_25`)


Das bis dahin bezogene Arbeitslosengeld sei daher  von der ÖGK direkt an das AMS zurückbezahlt worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `AMS` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_26`)


Der Eingabe waren eine Kontoübersicht  der Bf, Bestätigungen der ÖGK, eine Bezugsbestätigung des Arbeitsmarktservices Ramberg  und die Beschwerdevorentscheidung des Finanzamtes Österreich beigelegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `Ramberg` (city)
- `Finanzamtes Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_30`)


Die ÖGK erstellte daraufhin einen Lohnzettel und  übermittelte diesen dem Finanzamt Österreich am 18.3.2022.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_33`)


Die Leistungen des Arbeitsmarktservice (Vorschuss auf Rehabilitationsgeld), welche die Bf vom  22.2.2020 – 23.12.2020 iHv € 10.122,95 und vom 6.1.2021 – 31.3.2021 iHv € 2.917,20 erhielt  (gesamt € 13.040,15), wurden von der ÖGK direkt mit dem Arbeitsmarktservice im April 2021  gegenverrechnet (Bestätigungen der ÖGK, Bestätigung AMS vom 15.4.2021).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `AMS` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_34`)


Folgende Lohnzetteldaten wurden im Jahr 2021 dem Finanzamt übermittelt:  ÖGK § 69 Abs 2 14.222,86  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 14.222,86  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 962,68  ÖGK § 69 Abs 2 931,63  ÖGK § 69 Abs 2 962,68  AMS § 3 Abs 2 2.917,20  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `AMS` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_39`)


Die Feststellung, dass der Bf rückwirkend das Rehabilitationsgeld zugesprochen worden war,  ergibt sich aus den glaubhaften Ausführungen der Bf in Zusammenschau mit den vorgelegten  Urkunden der ÖGK und des Arbeitsmarktservice.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_40`)


Dass das gesamte Rehabilitationsgeld im Jahr 2021 steuerpflichtig behandelt wurde, ergibt sich  aus dem von der ÖGK übermittelten Lohnzettel, weshalb diese Feststellung bedenkenlos  getroffen werden konnte.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_41`)


Die Höhe der Rückzahlung (Vorschuss auf Rehabilitationsgeld) an das Arbeitsmarktservice  ergibt sich zweifelsfrei aus den Bestätigungen der ÖGK und des AMS.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `AMS` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_174`)


Der besseren Verständlichkeit halber werden die Fragen des BFG im Schreiben vom 9.08.2024  samt den fragebezüglichen Antworten der Bf. im Schreiben vom 3.10.2024 zusammengefasst   dargestellt:   BFG 09.08.2024, Punkt 1): „Wurde ein Antrag der Patientin auf Übernahme der Kosten für die  Operation, die für den April 2021 geplant war und vorzeitig im Februar 2021 durchgeführt  wurde, samt stationären Spitalsaufenthalt in der Sonderklasse durch die Österreichische  Gesundheitskasse (ÖGK) gestellt?

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_176`)


Gegebenenfalls wird um Vorlage der in Rede stehenden Anträge samt detaillierten  Ausführungen zum Verwaltungsverfahren beim Wiener Gesundheitsverbund und/oder bei der  LGA Niederösterreich und/oder bei der ÖGK ersucht.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_195`)


Antwortschreiben der Bf. vom 03.10.2024: Die Bf. habe keinen Antrag an die ÖGK gestellt, da  sie Selbstzahler gewesen sei.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_331`)


Die Geltendmachung von Wahlfacharztkosten als außergewöhnliche Belastung gemäß § 34  EStG 1988 in der Gesamthöhe war ungewöhnlich, weil ein Vergleich zwischen Ärzten mit und  ohne Krankenkassavertrag zeigt, dass Versicherte der ÖGK bei einem Wahlarzt oder einer  wahlärztlichen Einrichtung laut https: // www.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_333`)


bei der ÖGK entweder durch den Wahlarzt im Namen des Patienten einreichen oder selbst  einen Antrag auf Kostenerstattung stellen können.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_334`)


Die ÖGK erstattet die Kosten eines  Wahlarztes grundsätzlich in der Höhe von 80% jenes Betrages, den die ÖGK bei  Inanspruchnahme eines entsprechenden Vertragspartners aufwenden hätte müssen, jedoch  nicht mehr als die tatsächlichen Kosten.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_335`)


Die Berechnung der Erstattung von Kosten für  Leistungen der ärztlichen Hilfe, für Leistungen, die der ärztlichen Hilfe gleichgestellt sind, sowie  für medizinische Hauskrankenpflege (§§ 131 Abs. 1 und 2, 151 Abs. 4 ASVG) erfolgt gemäß § 23  der Satzung der ÖGK.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_336`)


Auf die Erstattung dieser Kosten durch die ÖGK nur, wenn die  Voraussetzungen des § 37 der Krankenordnung erfüllt sind, sei verwiesen.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/149749.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149749.1_19`)


Auf telefonische Anfrage habe die Rechtsabteilung der ÖGK mit- geteilt, dass SUVA-Renten nicht unter die Krankenversicherungspflicht fielen und nicht von  der Regelung des § 73a ASVG umfasst seien.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `SUVA` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149825.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_16`)


Die Fragen, ob die Bf. für die von der Bf. beantragten Krankheitskosten Ersätze bzw.  Zuschüsse (z.B. Österreichische Gesundheitskasse (=ÖGK) erhalten hätte und  gegebenenfalls in welcher Höhe die Ersätze gewesen wäre, wurden gestellt.   2 von 25 Seite 3 von 25

**False Positives:**

- `ÖGK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Landespolizeidirektion` 

**F1:** 0.008 | **Precision:** 0.973 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `015c0cb0`  
**Description:**
Matches 'Landespolizeidirektion' optionally followed by 'Wien' ONLY. Excludes other locations like Burgenland which are not part of the entity name.

**Content:**
```
\b(Landespolizeidirektion(?:\s+Wien)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.973 | 0.004 | 0.008 | 75 | 73 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 73 | 2 | 16816 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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
- `Bundesfinanzgericht` (organisation)

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

## `BFG abbreviation` 💣

**F1:** 0.208 | **Precision:** 0.963 | **Recall:** 0.117  

**Format:** `regex`  
**Rule ID:** `faf8fd08`  
**Description:**
Matches the abbreviation 'BFG' (Bundesfinanzgericht) when used as an entity.

**Content:**
```
\bBFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.963 | 0.117 | 0.208 | 2180 | 2100 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2100 | 80 | 15870 |

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

## `Bundesministers für Arbeit, Soziales und Konsumentenschutz` 

**F1:** 0.003 | **Precision:** 0.958 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `44e180ab`  
**Description:**
Matches the specific entity 'Bundesministers für Arbeit, Soziales und Konsumentenschutz'.

**Content:**
```
\bBundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
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

## `AMS abbreviation` 

**F1:** 0.006 | **Precision:** 0.946 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `bac14e19`  
**Description:**
Matches the abbreviation 'AMS' (Arbeitsmarktservice) as an organisation.

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

## `Finanzamt with location` 

**F1:** 0.003 | **Precision:** 0.935 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `b767a97c`  
**Description:**
Matches 'Finanzamt' and its genitive form 'Finanzamtes' followed by specific locations including Feldkirch, Linz, and others not previously covered.

**Content:**
```
\b(Finanzamt(?:es)?(?:\s+(?:Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Österreich|Feldkirch|Linz|Wien\s+12/13/14\s+Purkersdorf)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.935 | 0.002 | 0.003 | 31 | 29 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 29 | 2 | 17789 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miroslav Hankel, BEd` (person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers Emma Türker, Frauenhofenstraße 13, 5132 Gasteig, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emma Türker` (person)
- `Frauenhofenstraße 13, 5132 Gasteig, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Ing. ÖkR Horst Stevens` (person)
- `Glinzen 13, 4661 Kirnbach, Österreich` (address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `HR Hedwig Barkholt` (person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich` (address)
- `ICON Wirtschaftstreuhand GmbH` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_15`)


Im gegenständlichen Fall wurde das Guthaben von EUR  3.114,19 mit 09.01.2014 von StNr. 10-15-453/7249 (Finanzamt für Gebühren,  Verkehrsteuern und Glücksspiel) auf StNr. 08 (Finanzamt Wien 12/13/14 Purkersdorf)  überrechnet, um fällige Abgabenrückstände zu tilgen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 12/13/14 Purkersdorf` | `Finanzamt Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `10-15-453/7249` (tax_number)
- `Finanzamt für Gebühren` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_57`)


Wie schon die belangte Behörde richtig ausgeführt hat wurde im gegenständlichen Fall das  Guthaben von EUR 3.114,19 mit 09.01.2014 von StNr. 10-15-453/7249 (Finanzamt für  Gebühren, Verkehrsteuern und Glücksspiel) auf StNr. 08 (Finanzamt Wien 12/13/14  Purkersdorf) überrechnet, um fällige Abgabenrückstände zu tilgen, sodass zum Fälligkeitstag  der Gebühren 07/2014 kein entsprechendes Guthaben auf dem Abgabenkonto mehr bestand.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 12/13/14  Purkersdorf` | `Finanzamt Wien 12/13/14  Purkersdorf` |

**Missed by this rule (FN):**

- `10-15-453/7249` (tax_number)
- `Finanzamt für  Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Stefan Pipal` (person)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Holger Weiskittel` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |
| `Finanzamtes Linz` | `Finanzamtes Linz` |
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Norbert Zöls` (person)
- `Wendy Schärff` (person)
- `Krainberg 12, 4633 Weilbach, Österreich` (address)
- `LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_2`)


2018 mit dem Anspruchszinsen (§ 205  BAO) für 2015 in Höhe von 2.159,99 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 11.07.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2016 in Höhe von 1.016,05 € festgesetzt wurden   zu Steuernummer 98-870/6822  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `98-870/6822` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Torsten Schattner, Stögersbach 35, 7031 Krensdorf, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 21. September 2017  betreffend Abweisung eines  Antrages auf Aufhebung des Einkommensteuerbescheides 2016 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Torsten Schattner` (person)
- `Stögersbach 35, 7031 Krensdorf, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133297.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133297.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Anton Lauscheck, Kesselstraße 10, 9551 Unterberg, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 10. Februar 2017 betreffend Einkommensteuer 2015 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Anton Lauscheck` (person)
- `Kesselstraße 10, 9551 Unterberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Christian Jovanovic, BA, Himmelsstiege 8, 4521 Matzelsdorf, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Christian Jovanovic, BA` (person)
- `Himmelsstiege 8, 4521 Matzelsdorf, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133447.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Philipp Harazin  in der Beschwerdesache Priv.-Doz. Kevin Morzinsky,  Strußnighof 37, 9631 Kleinbergl, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Bruck Eisenstadt Oberwart), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 58-060/5953  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Philipp Harazin` (person)
- `Priv.-Doz. Kevin Morzinsky` (person)
- `Strußnighof 37, 9631 Kleinbergl, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `58-060/5953` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Priv.-Doz.in Laetitia Pöstges, Krist 12, 3843 Riegers, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Priv.-Doz.in Laetitia Pöstges` (person)
- `Krist 12, 3843 Riegers, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/136011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Nadja Leinhardt, Lagerhauspark 35, 8720 Mitterbach, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 4. Oktober 2019 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer 2015 bis 2017 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Nadja Leinhardt` (person)
- `Lagerhauspark 35, 8720 Mitterbach, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/137203.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137203.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Dominika Mühlpforte, Herminenhof 6, 3812 Fistritz, Österreich, vertreten durch GERSTGRASSER Wirtschaftsprüfung und  Steuerberatung GmbH, Werdenbergerstraße 39a, 6700 Bludenz, über die Beschwerde vom  27.09.2016 gegen den Bescheid des Finanzamtes Feldkirch vom 13. September 2016  betreffend Körperschaftsteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Dominika Mühlpforte` (person)
- `Herminenhof 6, 3812 Fistritz, Österreich` (address)
- `GERSTGRASSER Wirtschaftsprüfung und  Steuerberatung GmbH` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/139725.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139725.1_3`)


Begründung  Das Bundesfinanzgericht hat mit Erkenntnis vom 2.1.2023, GZ. RV/5100155/2020, die  Bescheidbeschwerde des Revisionswerbers vom 8.11.2019 gegen den Haftungsbescheid des  Finanzamtes Linz vom 16.9.2019 abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Karim Ickstadt  in der Beschwerdesache   Axel Jastrzemsky, als Gruppenträgerin, V GmbH, als Gruppenmitglied und der Klemeyer + Heisterhagen Pharma GmbH  als von der  Teilnahme an der Unternehmensgruppe ausgeschlossene Körperschaft, jeweils vertreten durch  Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG, Linzer Bundesstraße 101, 5023  Salzburg-Gnigl, über die Beschwerde der Axel Jastrzemsky, Sandweg 7, 4782 Aigerding, Österreich, vom 28. März 2019 gegen  den Gruppenfeststellungsbescheid 2018 des Finanzamtes Wien 12/13/14 Purkersdorf -  nunmehr Finanzamtes Österreich - vom 27. Februar 2019, Steuernummer 74-905/9339,  nach Durchführung einer mündlichen Verhandlung am 22. August 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Karim Ickstadt` (person)
- `Axel Jastrzemsky` (person)
- `Klemeyer + Heisterhagen Pharma GmbH` (organisation)
- `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG` (organisation)
- `Axel Jastrzemsky` (person)
- `Sandweg 7, 4782 Aigerding, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `74-905/9339` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/142456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142456.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Carla Jegers  in der Beschwerdesache Gisela Sramek,  Elsniggasse 69, 6364 Brixen im Thale, Österreich, vertreten durch ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG, Plüddemanngasse 87, 8010 Graz, betreffend Beschwerde vom 13. Juni  2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 2. Mai 2019   betreffend Zwangsstrafe gemäß § 111 BAO iVm §§ 5 und 16 WieREG   Steuernummer 18-269/6388  beschlossen:  Der Vorlageantrag wird gemäß § 262 Abs. 1 iVm § 264 Abs. 5 BAO als unzulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Carla Jegers` (person)
- `Gisela Sramek` (person)
- `Elsniggasse 69, 6364 Brixen im Thale, Österreich` (address)
- `ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG` (organisation)
- `Finanzamt  Österreich` (organisation)
- `18-269/6388` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Mag. Josef Ungericht, die Richterin Dr.  Gerhild Fellner und die weiteren Senatsmitglieder Karl-Heinz Dobler und Dr. Andreas Kickl, im  Beisein der Schriftführerin Claudia Zengin, in der Beschwerdesache der Zorglanzdorf-Bildung, Seidledtstraße 13, 9560 Tiffen, Österreich, vertreten durch Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH,  Schloßgraben 10, 6800 Feldkirch, über die Beschwerde vom 01.03.2019 gegen den  Aufhebungsbescheid gemäß § 299 BAO des Finanzamtes Feldkirch vom 6. Februar 2019  betreffend Körperschaftsteuer 2014, in der Sitzung vom 12. Dezember 2023 nach  Durchführung einer mündlichen Verhandlung, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Dr.  Gerhild Fellner` (person)
- `Dr. Andreas Kickl` (person)
- `Zorglanzdorf-Bildung` (organisation)
- `Seidledtstraße 13, 9560 Tiffen, Österreich` (address)
- `Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_35`)


Dieser Aspekt  erscheint vor allem deshalb bedeutsam, weil der hier gegenständliche Sachverhalt (steuerliche  Behandlung indischer Quellensteuern als Betriebsausgaben) in einem gleichzeitig mit der  Steuererklärung eingereichten Schreiben vom 28.04.2016 offengelegt worden ist und somit  diese Frage vom Finanzamt Feldkirch einmal bei Erlassung des Erstbescheides und in weiterer  Folge auch im Zuge eines Rechtsmittelverfahrens ganz offensichtlich abweichend von der jetzt  3 von 13 Seite 4 von 13

| Predicted | Gold |
|---|---|
| `Finanzamt Feldkirch` | `Finanzamt Feldkirch` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_99`)


Dieser Aspekt erscheint vor allem deshalb bedeutsam, weil der  hier gegenständliche Sachverhalt (steuerliche Behandlung indischer Quellensteuern als  Betriebsausgaben) in einem gleichzeitig mit der Steuererklärung eingereichten Schreiben vom  28.04.2016 offengelegt worden ist und somit diese Frage vom Finanzamt Feldkirch einmal bei  Erlassung des Erstbescheides und in weiterer Folge auch im Zuge eines Rechtsmittelverfahrens  ganz offensichtlich abweichend von der jetzt vertretenden Rechtsauffassung beurteilt worden  ist.“

| Predicted | Gold |
|---|---|
| `Finanzamt Feldkirch` | `Finanzamt Feldkirch` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/142996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142996.1_143`)


Der zum Ermessen erhobene Beschwerdeeinwand, wonach „der hier gegenständliche  Sachverhalt (steuerliche Behandlung indischer Quellensteuern als Betriebsausgaben) in einem  gleichzeitig mit der Steuererklärung eingereichten Schreiben vom 28.04.2016 offengelegt  worden ist und somit diese Frage vom Finanzamt Feldkirch einmal bei Erlassung des  Erstbescheides und in weiterer Folge auch im Zuge eines Rechtsmittelverfahrens ganz  offensichtlich abweichend von der jetzt vertretenden Rechtsauffassung beurteilt worden ist“,  ist im Hinblick auf die beträchtliche Höhe der indischen Quellensteuer bzw. der beantragten  Betriebsausgaben nicht in einem solchen Ausmaß gewichtig, um von der Vornahme einer  rechtsrichtigen Abgabenerhebung Abstand zu nehmen.

| Predicted | Gold |
|---|---|
| `Finanzamt Feldkirch` | `Finanzamt Feldkirch` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Urs Ahrenholz, Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich, vertreten durch HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG, Schloßgraben 10, 6800 Feldkirch,  über die Beschwerde vom 2. Oktober 2019 gegen den Bescheid des Finanzamtes Feldkirch vom  9. September 2019 betreffend Einkommensteuer 2017, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Urs Ahrenholz` (person)
- `Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich` (address)
- `HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/147075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Bruno Maquardt  in der Angelegenheit der Parteien Dr.  AN Bf, Rechtsanwältin in Stadt37, vertreten durch next Steuerberatung Wien GmbH, 1150  Wien, und Finanzamt Linz  als Amtspartei über die Beschwerde vom 27.9.2024 gegen den Bescheid  des Finanzamtes vom 27.8.2024 betreffend Einkommensteuer 2022  zu Recht erkannt:  Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Bruno Maquardt` (person)
- `next Steuerberatung Wien GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Manfred Stieldorf  in der Beschwerdesache Milena Maertin,  Bischofsrütti 17, 9863 Steinwand, Österreich, vertreten durch LGH - Wirtschaftstreuhand u. Bilanzbuchhalter GmbH,  Tigergasse 26-28 Tür 9, 1080 Wien, über die Beschwerde vom 11. Juni 2018 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 22. Mai 2018 betreffend Haftungs-  und Abgabenbescheid 22.05.2018 Steuernummer 34-322/0854  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die Haftung auf  nachstehende Abgaben im Gesamtbetrag von € 6.530,15 eingeschränkt:    Abgabenart Zeitraum Betrag in Euro  Lohnsteuer 2006 56,49  Lohnsteuer 2008 56,49  Lohnsteuer 01-12/2008 1010,69  Lohnsteuer 01-12/2009 2524,57  Lohnsteuer 01/2010 458,70  Lohnsteuer 02/2010 465,42  Lohnsteuer 03/2010 445,16  Lohnsteuer 04/2010 371,50  Lohnsteuer 05/2010 407,63  Lohnsteuer 06/2010 349,17  Lohnsteuer 07/2010 384,32  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 12/13/14 Purkersdorf` | `Finanzamtes Wien 12/13/14 Purkersdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Manfred Stieldorf` (person)
- `Milena Maertin` (person)
- `Bischofsrütti 17, 9863 Steinwand, Österreich` (address)
- `34-322/0854` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134456.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Linn Benli  in der Beschwerdesache Lewis Wiechard,  Platteckweg 9, 4731 Pertmannshub, Österreich, über die Beschwerde gegen den Bescheid des (damaligen) Finanzamtes  Feldkirch vom 20.5.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 61-563/9200, zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Feldkirch` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Linn Benli`(person)
- `Lewis Wiechard`(person)
- `Platteckweg 9, 4731 Pertmannshub, Österreich`(address)
- `Finanzamtes`(organisation)
- `61-563/9200`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/134512.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134512.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Diana Grambusch  in der Beschwerdesache Adalbert Gruenaeugl,  Schloßbauerweg 3, 2474 Gattendorf, Österreich, über die Beschwerde vom 24. Juni 2020 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Juni 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu  Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Finanzamtes  Feldkirch` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Diana Grambusch`(person)
- `Adalbert Gruenaeugl`(person)
- `Schloßbauerweg 3, 2474 Gattendorf, Österreich`(address)
- `Finanzamtes`(organisation)

</details>

---

## `Wiener Gemeinderates` 💣

**F1:** 0.006 | **Precision:** 0.915 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `bff9579e`  
**Description:**
Matches specific Austrian municipal bodies like 'Wiener Gemeinderates'.

**Content:**
```
\b(Wiener\s+Gemeinderates)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.915 | 0.003 | 0.006 | 59 | 54 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 54 | 5 | 16479 |

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

## `BMF and BFH` 💣

**F1:** 0.018 | **Precision:** 0.891 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `e1f782e8`  
**Description:**
Matches the abbreviations BMF and BFH.

**Content:**
```
\b(BMF|BFH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.891 | 0.009 | 0.018 | 183 | 163 | 20 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 163 | 20 | 17311 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_19`)


Mit Vorhalt vom 21.06.2016 teilte das BMF der Bf. mit, dass eine Entlastungsmaßnahme  gemäß § 48 BAO nur in Betracht komme, wenn eine echte internationale Doppelbesteuerung  vorliege, worunter die Erhebung gleicher oder gleichartiger Steuern von demselben  Steuerpflichtigen für denselben Steuergegenstand und denselben Zeitraum zu versehen sei.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_88`)


Das BMF hat die Beschwerde mitsamt den bezugshabenden Akten dem BFG als Direktvorlage  gemäß § 262 Abs. 4 i.V.m. § 265 BAO zur Entscheidung vorgelegt und dazu im Vorlagebericht  vom 20.04.2018 Folgendes ausgeführt:    „Der Unterlage „Online Gambling in Greece“ (Anhang zum Bericht FA10 vom 20.4.2017),  erstellt von Gambling Complience (https://gamblingcompliance.com), Stand März 2015,  zufolge, befand sich die Regulierung des Online-Wett- und Glücksspielmarktes in Griechenland  in einer Übergangsphase.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_15`)


Die Tatsache, dass für Zwecke der deutschen Besteuerung ein steuerfreier Betrag  der deutschen Alterspension ermittelt wird, ist für Zwecke des österreichischen  Progressionsvorbehalts unerheblich, da dieser nach österreichischem Recht  ermittelt wird (siehe Info auf BMF-Homepage unter https_//www.bmf.gv.at/steuern  /selbststaendige-unternehmer/einkommensteuer/est-faq-deutsche-pension.html)

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_121`)


ob im Zeitpunkt des abgeschlossenen Verfahrens diese Umstände der Partei bekannt waren  (BMF, AÖF 2006/192, Abschn.2.1.; aM VwGH 28.9.1998, 96/16/0158;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_71`)


Diese Schätzung stützt sich auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142- VI/6/2016, BMF-Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der  Besteuerung von Grundstücken und Kapitalvermögen durch das Steuerreformgesetz  2015/2016, BGBI. I Nr. 118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, wonach der  Grundanteil mit 20% des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  geschätzt werden kann.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_89`)


Unter Bezugnahme auf den BMF-Erlass vom 12. Mai 2016, BMF-010203/0142-VI/6/2016, BMF- Info zu den ertragsteuerlichen Änderungen im Zusammenhang mit der Besteuerung von  Grundstücken und Kapitalvermögen durch das Steuerreformgesetz 2015/2016, BGBI. I Nr.  118/2015 (BMF-Info StRefG 2015/16), Punkt 1.2.1, beabsichtigt das Finanzamt, den  Grundanteil mit 20 % des Verkaufserlöses und mit 20 % der seinerzeitigen Anschaffungskosten  zu schätzen, wobei 1.000 m2 steuerfrei bleiben und 1.144 m2 steuerpflichtig sind.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_38`)


8. Im Vorlageantrag samt nachgereichter gesonderter Begründung wird seitens des Bf,  vertreten durch C, Steuerberater in D/BB, ua. vorgebracht:  Abgesehen von der bestrittenen NoVA-Pflicht in Österreich sei der Pickup des Bf von der NoVA  befreit, da dieser lt. NoVA-Richtlinie bis 31.3.2007 als LKW einzustufen und lt. BMF vom  11.7.2007 weiterhin als solcher zu behandeln sei.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_39`)


In der Liste des BMF zu "Pritschenwagen"  gemäß VO aus 1996 und § 4 VO 2002, die als LKW gelten, seien "Nissan Navara" und "Nissan  Pickup" als Pritschenwagen aufgeführt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_105`)


Das BMF habe  sich bis dato nicht veranlasst gesehen, die Rz 705 der Gebührenrichtlinien 2007 zu ändern.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_75`)


Stellungnahme:   Vorweg ist an dieser Stelle festzuhalten, dass, auch wenn der § 26 (3) StuFöG 1992 mit  01.09.2017 (BGBl. I Nr. 54/2016) geändert worden ist, die bislang geltenden Kriterien für die  Beurteilung der Wegzeiten zur Erreichung des Studienortes weiterhin anzuwenden sind, weil  die VO des BMF zur Berufsausbildung des Kindes außerhalb des Wohnortes (BGBl. Nr.  624/1995 idgF) auf das Studienförderungsgesetz idF BGBl. I Nr. 50/2016 verweist.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_300`)


Eine den Progressionsvorbe- halt einräumende Bestimmung in einem DBA hat lediglich deklaratorische Bedeutung (vgl.  VwGH 29.7.2010, Zl. 2010/15/0021 unter Hinweis auf BFH 19.12.2001, I R 63/00 und BFH  10.12.2008, I B 60/08).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_240`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. im Verfahren  betreffend Vorjahre vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_88`)


Jakom/Baldauf, EStG8, § 34 Rz 90,  Stichwort "Kurreise" bzw Endfellner, Krankheit und Behinderung im Einkommensteuerrecht  [Wien 2012], 128 f ; vgl grundsätzlich gleichlautend auch BFH 14.8.1997, III R 67/96, BStBl II  1997, 732).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_88`)


Der deutsche Bundesfinanzhof (BFH) hat in seinem Urteil vom 12.12.2019, V R 3/19, die Frage  der umsatzsteuerlichen Ansässigkeit bei Vermietung im Inland durch eine im Ausland  wohnhafte Steuerpflichtige bereits behandelt.  Die in Italien lebende Klägerin hatte eine Wohnung in Deutschland, an der sie ein  Fruchtgenussrecht hatte, vermietet.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_90`)


Der BFH stützte seine Entscheidung auf die EuGH-Judikatur in der Rs Schmelz und kam zum  eindeutigen Ergebnis, dass „die Vermietung einer Wohnung jedenfalls für die Anwendung der  Kleinunternehmerregelung weder als ansässigkeits- noch als niederlassungsbegründend  anzusehen“ ist.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Missed by this rule (FN):**

- `Schmelz` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_17`)


Für die fremdfinanzierte Rentenversicherung sei das  Anwaltshonorar sehr wohl anzuerkennen, als Beweis diene ein Schreiben der Abteilung IV/7  des BMF vom 12.1.2001, in dem ausgeführt wird, dass Zinsen für Fremdkapital, das für den  Erwerb eines Rentenstammrechtes aufgenommen wurde, gemäß § 16 Abs 1 Z 1 EStG  Werbungskosten darstelle (Verweis auf EStR 2000 Rz 7018) und hinsichtlich des  Verlustausgleiches EStR 2000 Rz 151 ff zu beachten seien.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_64`)


Weshalb dieser Judikatur "als Folge der  Gesetzesänderung "der Boden entzogen sein soll", ist für das Bundesfinanzgericht nicht  ersichtlich, zumal Ritz und das Bundesministerium für Finanzen schon zur § 303 Abs. 1 BAO alte  Fassung nachstehende - von der Judikatur des Verwaltungsgerichtshofs abweichende -  Rechtsansicht vertreten haben (vgl. Ritz, BAO4, § 303 Tz 27 und vgl. Ritz, BAO5,§ 303 Tz 47):   "Für die Frage des Neuhervorkommens ist - ebenso wie für die amtswegige Wiederaufnahme -  der Kenntnisstand der Abgabenbehörde (im jeweiligen Verfahren) maßgebend, nicht jedoch,  ob im Zeitpunkt des abgeschlossenen Verfahrens diese Umstände der Partei bekannt waren  (BMF, AÖF 2006/192, Abschn.2.1.; aM VwGH 28.9.1998, 96/16/0158;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesministerium für Finanzen` (organisation)
- `Verwaltungsgerichtshofs` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_80`)


BFH 18. 4. 2002, III R 15/00).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_100`)


Der besondere Pflege- oder Betreuungsbedarf eines Behinderten (iSd § 35) ist nach LStR 2002  Rz 887 durch ein ärztliches Gutachten oder durch Bezug von Pflegegeld nachzuweisen, ein  amtsärztliches Gutachten ist nicht erforderlich (vgl BFH 9.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_295`)


Die nach Art. 67 VO 883/2004 i. V. m. Art. 60 Abs. 1 Satz 2 VO 987/2009 vorzunehmende  Fiktion bewirkt, dass die Wohnsituation auf Grundlage der im Streitzeitraum im anderen EU- Mitgliedstaat gegebenen Verhältnisse (fiktiv) ins Inland übertragen wird (Bundesfinanzhof in  der Folge abgekürzt mit BFH vom 10.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_297`)


Diese Fiktion besagt aber nur, dass zu unterstellen ist, dass alle Familienangehörige im  zuständigen Mitgliedstaat wohnen, nicht aber, dass diese – wenn dies nicht im  Wohnmitgliedstaat der Fall ist – im selben Haushalt wohnen (vgl. auch BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_300`)


Wer von den unionsrechtlich grundsätzlich als anspruchsberechtige Personen anzusehenden  Familienangehörigen tatsächlich primär oder sekundär (oder gar keinen) Anspruch auf  österreichische Familienleistungen hat, ist daher nach dem nationalen Recht zu beurteilen (vgl.  auch BFH 4.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_302`)


BFH 10. 3. 2016, III R 62/12 und BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_304`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_305`)


BFH 23.8.2016, V R 25/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_306`)


BFH 23.8.2016, V R 10/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_307`)


BFH  26.10.2016, III R 27/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_308`)


BFH 13.7.2016, XI R 23/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_309`)


BFH 23.8.2016, V R 40/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_310`)


BFH  23.8.2016, V R 16/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_311`)


BFH 7.7.2016, III R 46/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_312`)


BFH 23.8.2016, V R 31/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_313`)


BFH 23.8.2016,  V R 11/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_314`)


BFH 23.8.2016, V R 49/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_315`)


BFH 23.8.2016, V R 50/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_316`)


BFH 4.8.2016, III R 10/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_317`)


BFH 7.7.2016, III R 11/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_318`)


BFH 23.8.2016, V R 19/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_319`)


BFH 23.8.2016, V R 29/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_320`)


BFH  23.8.2016, V R 2/14;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_321`)


BFH 13.7.2016, XI R 33/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_322`)


BFH 15.6.2016, III R 67/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_323`)


BFH 13.7.2016,  XI R 28/12;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_324`)


BFH 13.7.2016, XI R 44/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_325`)


BFH 13.7.2016, XI R 7/15;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_326`)


BFH 21.7.2016, V R  46/11;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_327`)


BFH 28.4.2016, III R 45/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_328`)


BFH 28.4.2016, III R 65/13;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_329`)


BFH 13.4.2016, III R 14/13  sowie die Entscheidungen des Bundesfinanzgerichts BFG 19.8.2016, RV/7101889/2016  21 von 32 Seite 22 von 32

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `BFG` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_364`)


Da die Tochter des Bf. dem Haushalt ihrer Mutter M in Polen angehört, hat gemäß § 2 Abs. 2  Satz 1 FLAG 1967 daher die Mutter den vorrangigen Anspruch auf die österreichischen  Familienleistungen (Familienbeihilfe und Kinderabsetzbetrag) (vgl. auch BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_390`)


Der Familienleistungsanspruch des in Österreich wohnhaften Elternteils (hier: des leiblichen  Vaters) wird nach § 2 Abs. 2 Satz 1 FLAG 1967 i. V. m.  Art. 67 VO 883/2004 und  Art. 60 Abs. 1 Satz 2 VO 987/2009 durch den vorrangigen Familienleistungsanspruch des in  einem anderen Mitgliedstaat der Union (des EWR oder in der Schweiz) mit dem Kind im  gemeinsamen Haushalt lebenden Elternteils (hier: der Mutter) verdrängt  (vgl. BFH 28.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_263`)


Aufgrund dieser Abkommensrevision sind die vom steuerlichen Vertreter des Bf. mit der  Beschwerde vorgelegten EAS-Auskünfte des BMF betreffend Mitarbeiter des Schweizer  Verkehrsbüros vom 21.8.1996 bzw. betreffend österreichisches Sur-Place-Personal der  Schweizerischen Botschaft in Wien vom 21.12.2004 veraltet (da sie sich nicht auf die neue  Rechtslage beziehen) und es war daher nicht mehr weiter darauf einzugehen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_24`)


Zur Begründung wurde ausgeführt, die Rechtsprechung (bzw die Einkommensteuerrichtlinien  des BMF) sehe den Übergang des wirtschaftlichen Eigentums als entscheidend für die  Beurteilung einer Anschaffung im Sinne des § 10 EStG 1988 an.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_90`)


Im Rundschreiben 293/2007 der österreichischen Ärztekammer vom 07.12.2007 wird zur Frage  der Besteuerung der Bestattungsbeihilfe und Hinterbliebenenunterstützung (§§ 98 Abs 1 und  104 ÄrzteG) auf eine Mitteilung des BMF vom 04.12.2007, BMF-010222/0174-VI//7/2007,  hingewiesen, mit der eine Anfrage der Österreichischen Ärztekammer vom 30.08.2007  beantwortet wurde und der ua Folgendes zu entnehmen ist:  „Die von der Ärztekammer ausbezahlte Hinterbliebenenunterstützung und Bestattungsbeihilfe  ist unabhängig von der Gestaltung des jeweiligen Sachverhalts immer nach § 22 Z 4 iVm § 32 Z  2 EStG beim Rechtsnachfolger zu versteuern.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_97`)


……“  Die österreichische Ärztekammer hat diese Rechtsmeinung des BMF im Rundschreiben  293/2007 vom 07.12.2007 zustimmend kommuniziert.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_30`)


Da die Daten des GWR von der  Statistik Austria dem BMF zur Verfügung gestellt werden und das BMF eine andere Behörde als  das zuständige Finanzamt ist, würde eine Abfrage dieser Daten das Erfordernis einer nach  außen erkennbaren Amtshandlung erfüllen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_79`)


Die Erkennbarkeit im Bundesministerium für Finanzen (BMF)  reicht aber aus, weil das BMF eine andere Behörde als das Finanzamt für Gebühren,  Verkehrsteuern und Glücksspiel ist, sodass die Amtshandlung nach außen erkennbar war.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesministerium für Finanzen` (organisation)
- `Finanzamt für Gebühren` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_53`)


Die Mindesthöhe des Verspätungszuschlages von 0,1% könne  auch als angemessen erscheinen (vgl. Erlass des BMF, GZ BMF-010103/0030-V1/2006 vom  10.042006).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/135135.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135135.1_39`)


Sie ist dann anzunehmen, wenn objektiv ein Zusammenhang mit dem Beruf  besteht und subjektiv die Aufwendungen zur Förderung des Berufes, nämlich zur Erwerbung,  Sicherung und Erhaltung von Einnahmen im Rahmen der Einkunftsart gemacht werden (vgl.  BFH 28.11.1980, BStBl 1981 II 368).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_164`)


Nach dem Urteil des BFH vom 29.01.2015 V R 5/14 sei Schuldner der Einfuhrumsatzsteuer die  Person, die in eigenem Namen die Zollanmeldung abgibt oder in deren Namen eine  Zollanmeldung abgegeben wird.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_332`)


Die TNT hat jedoch nicht für Rechnung der Empfänger gehandelt, weil die zollrechtliche  Abwicklung unabhängig von der Befreiung von der Einfuhrumsatzsteuer durch die Übernahme  aller etwaig anfallenden Steuern und sonstiger Kosten durch die Beschwerdeführerin unter  keinem denkbaren Gesichtspunkt für die Empfänger wirtschaftliche Auswirkungen haben  konnte (siehe BFH Urteil vom 29.01.2015, V R 5/14 und BFH Urteil vom 16.06.2021, XI R  17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_344`)


Auf Grund der Klausel im Punkt 4.9 der AVB, dass die Beschwerdeführerin sämtliche Abgaben  und Gebühren betreffend die Einfuhr übernehmen werde, ist die Bevollmächtigung der  Beschwerdeführerin zur Einfuhr im Namen der Empfänger unwirksam (siehe BFH Urteil vom  29.01.2015, V R 5/14 und BFH Urteil vom 16.06.2021, XI R 17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_346`)


Der Beschwerdeführerin und folglich der TNT als Subunternehmerin, fehlt es nämlich an dem  für die allein in Betracht kommende direkte Vertretung zollrechtlich erforderlichen Handelns  für Rechnung eines anderen (Art. 5 Abs. 2 Teilstrich 1. ZK), da die Bf. sämtliche Abgaben und  Gebühren zu tragen hat (siehe auch BFH vom 29.01.2015, V R 5/14, vom 16.06.2015, XI R  17/13).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/136045.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136045.1_37`)


Im  Rahmen der Entsendung wurden Taggelder ausbezahlt, welche vom Dienstgeber (der  damaligen Erlassmeinung des BMF folgend) zum Teil steuerfrei und zum Teil steuerpflichtig  behandelt wurden.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_101`)


Sowohl  der Nachweis von Gelegenheiten zum Abschluss eines Vertrages als auch die Kontaktaufnahme  mit der anderen Partei oder das Verhandeln über die Einzelheiten der gegenseitigen Leistungen  setzen voraus, dass sich die Mittlertätigkeit auf ein einzelnes Geschäft, das vermittelt werden  soll, bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_105`)


Dies gilt jedoch nach der EuGH-Rechtsprechung nur, wenn es sich  bei der einzelnen Leistung um ein im Großen und Ganzen eigenständiges Ganzes handelt, das  die spezifischen und wesentlichen Funktionen der Vermittlung erfüllt. Da somit auch Leistungen  im Rahmen einer arbeitsteiligen Vermittlung als eigenständiges Ganzes die spezifischen und  wesentlichen Funktionen der Vermittlung erfüllen müssen, sind sie nur steuerfrei, wenn der  jeweilige Vermittler eine Mittlertätigkeit ausübt, die sich auf einzelne Wertpapier- oder  Anteilsumsätze bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_91`)


Denn eine Betriebsprüfung bei einem  Abgabepflichtigen wird nicht allein und eigens mit dem Ziel durchgeführt werden können, hier  die Verhältnisse Dritter zu erforschen (Stoll, BAO-Kommentar, § 147, unter Verweis auf die  Judikatur des (dt.) BFH).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_113`)


Die fehlende Angabe der  Wiederaufnahmsgründe in der Begründung des mit Beschwerde angefochtenen Bescheides ist  auch in der Beschwerdevorentscheidung nicht „nachholbar“ (vgl BMF, AÖF 2006/192, Abschn  4;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_153`)


Ein „Kurzgutachten“ (mit unvollständiger Befundaufnahme oder reduzierter  Gutachtensmethodik und -begründung) erfüllt diesen Standard nicht, kann daher auch nicht zur  Beweislastumkehr führen, sondern unterliegt ebenso wie ein Gutachten, das von einer anderen  Person als einem Immobiliensachverständigen erstellt wird, der freien Beweiswürdigung (BMF  vom 13. Mai 2016, 010206/0058-VI/5/2016).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/138980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138980.1_137`)


Aigner et al., DBA-Kommentar2, Seite 1510, führt aus, dass das BMF von einer konstitutiven  Wirkung des Progressionsvorbehaltes in den DBA ausgehe, während der VwGH von einer nur  deklaratorischen Klarstellung des Progressionsvorbehaltes in den DBA ausgehe.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_48`)


Auch nach  Doralt/Kirchmayr/Mayr/Zorn, EStG14, § 6, Tz 279, sind Fremdwährungsverbindlichkeiten  grundsätzlich mit dem Rückzahlungsbetrag anzusetzen, der sich aus dem Kurs im Zeitpunkt der  Darlehensaufnahme ergibt (BFH 23.4.2009 - IV R 62/06).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_69`)


Auch nach  Doralt/Kirchmayr/Mayr/Zorn, ESt 14, § 6, Tz 279, sind Fremdwährungsverbindlichkeiten  grundsätzlich mit dem Rückzahlungsbetrag anzusetzen, der sich aus dem Kurs im Zeitpunkt der  Darlehensaufnahme ergibt (BFH 23.4.2009 - IV R 62/06).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/139828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139828.1_22`)


Eine außergewöhnliche Belastung auf Grund  sittlicher Verpflichtung zur Übernahme von Begräbniskosten sei nicht ausgeschlossen (BFH  24.7.87, III R 208/82, BStBl II 87, 715), allerdings auf Fälle nicht bestehender bzw. nicht  durchsetzbarer Erstattungsansprüche beschränkt, zB bei Begräbniskosten für einen  vermögenslosen Lebensgefährten oder für einen vermögenslosen ehemaligen Ehegatten (BFG  15.4.15, RV/5100610/2013);

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/140219.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140219.1_225`)


In Anwendung der angeführten Judikatur des Höchstgerichtes sowie der Rechtsmeinung des  BMF laut den Einkommensteuerrichtlinien, der sich das Bundesfinanzgericht im konkreten Fall  anschließt, sind die geltend gemachten Anschaffungsnebenkosten laut Punkt 8. bis 12.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_76`)


Nach dem klaren Wortlaut der Gebührenrichtlinien des BMF sowie der Rechtsprechung des  VwGH führe die Vereinbarung aller denkmöglichen Kündigungsgründe des § 30 Abs. 2 MRG zur  gebührenrechtlichen Qualifizierung des Mietvertrages als auf „unbestimmte“ Zeit  abgeschlossen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_116`)


Medizinisch indiziert sei jedes diagnostische oder therapeutische Verfahren, dessen  Anwendung in einem Erkrankungsfall hinreichend gerechtfertigt sei, es sei denn, es liege ein  für jedermann offensichtliches Missverhältnis zwischen dem erforderlichen und dem  tatsächlichen Aufwand vor (vgl BFH 12.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_129`)


Als konkrete Rechercheergebnisse wurden dem Amtsvertreter mitgeteilt:  Im Doralt-Kommentar (§ 34 Tz 78) werde dazu ausgeführt: „Werden Aufwendungen ihrer  Natur nach nicht ausschließlich von Kranken, sondern mitunter auch von Gesunden getätigt,  um ihre Gesundheit zu erhalten, ihr Wohlbefinden zu steigern oder ihre Freizeit sinnvoll zu  gestalten, ist nach dem zum Besuch eines Fitnessstudios ergangenen Erk VwGH 4.9.2014,  2012/15/0136, ein sog „vorfeldweises“ ärztliches Gutachten erforderlich, um die  Zwangsläufigkeit dieser Kosten zu begründen (Verweis auf BFH 14.8.1997, III R 67/96, BStBl II  1997, 732, zu Aufwendungen für eine „medizinische Trainingstherapie“ in einem ärztlich  betreuten Sportstudio).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_131`)


An einem  „formalisierten Nachweisverlangen“ in Form eines vorfeldweisen Gutachtens hielt der BFH  wegen eines Widerspruchs zum Grundsatz der freien Beweiswürdigung auch nicht mehr fest  (zB BFH 11.11.2010, VI R 17/09, BStBl II 2011, 969; vgl zur Rechtsentwicklung in Deutschland –  auch zu einer nachfolgenden legistischen Einführung formalisierter Nachweiserfordernisse  durch das StVereinfG 2011, BStBl I 2011, 986, in § 64 Abs 1 Nr 1 ESt- Durchführungs¬verordnung – zB Schmidt/Loschelder, EStG, § 33 Rz 33f; zum Abzug von  8 von 30 Seite 9 von 30

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_132`)


Krankheits¬kosten als außergewöhnliche Belastung vgl bspw BFH 25.4.2017, VIII R 52/13, DStR  2017, 1693).“

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_324`)


Im Doralt-Kommentar (§ 34 Tz 78) werde dazu ausgeführt: „Werden Aufwendungen ihrer  Natur nach nicht ausschließlich von Kranken, sondern mitunter auch von Gesunden getätigt,  um ihre Gesundheit zu erhalten, ihr Wohlbefinden zu steigern oder ihre Freizeit sinnvoll zu  gestalten, ist nach dem zum Besuch eines Fitnessstudios ergangenen Erk VwGH 4.9.2014,  2012/15/0136, ein sog „vorfeldweises“ ärztliches Gutachten erforderlich, um die  Zwangsläufigkeit dieser Kosten zu begründen (Verweis auf BFH 14.8.1997, III R 67/96, BStBl II  1997, 732, zu Aufwendungen für eine „medizinische Trainingstherapie“ in einem ärztlich  betreuten Sportstudio).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_326`)


An einem  „formalisierten Nachweisverlangen“ in Form eines vorfeldweisen Gutachtens hielt der BFH  wegen eines Widerspruchs zum Grundsatz der freien Beweiswürdigung auch nicht mehr fest  (zB BFH 11.11.2010, VI R 17/09, BStBl II 2011, 969; vgl zur Rechtsentwicklung in Deutschland –  auch zu einer nachfolgenden legistischen Einführung formalisierter Nachweiserfordernisse  durch das StVereinfG 2011, BStBl I 2011, 986, in § 64 Abs 1 Nr 1 ESt- Durchführungs¬verordnung – zB Schmidt/Loschelder, EStG, § 33 Rz 33f; zum Abzug von  Krankheits¬kosten als außergewöhnliche Belastung vgl bspw BFH 25.4.2017, VIII R 52/13, DStR  2017, 1693).“  VwGH vom 22. Dezember 2004, 2001/15/0116, betraf eine Kur: An den - vom Steuerpflichtigen  zu führenden - Nachweis dieser Voraussetzungen müssen wegen der im allgemeinen  schwierigen Abgrenzung solcher Reisen von den ebenfalls der Gesundheit dienenden  Erholungsreisen strenge Anforderungen gestellt werden (vgl. das hg.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_360`)


Abschließend sei auf einige –wenn auch nicht verbindliche, so doch interessante-  Ausführungen des deutschen BFH in seinem Urteil vom 12.5.2011, VI R 37/10 (bei gleicher  Rechtslage wie in Österreich) hingewiesen:   Für die mitunter schwierige Trennung von echten Krankheitskosten einerseits und lediglich  gesundheitsfördernden Vorbeuge- oder Folgekosten andererseits forderte der BFH bislang  regelmäßig die Vorlage eines zeitlich vor der Leistung von Aufwendungen erstellten amts- oder  vertrauensärztlichen Gutachtens bzw. eines Attestes eines anderen öffentlich-rechtlichen  Trägers, aus dem sich die Krankheit und die medizinische Indikation der den Aufwendungen  zugrundeliegenden Behandlung zweifelsfrei entnehmen lässt.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |
| `BFH` | `BFH` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_361`)


Auch bei Aufwendungen für  Maßnahmen, die ihrer Art nach nicht eindeutig nur der Heilung oder Linderung einer Krankheit  dienen können und deren medizinische Indikation deshalb schwer zu beurteilen ist, verlangte  der BFH diesen formalisierten Nachweis.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_378`)


Zur Höhe des Aufwandes  Wanke in Wiesner u.a EStG Anm 78 zu § 34: Zur Heilbehandlung medizinisch indiziert ist jedes  diagnostische oder therapeutische Verfahren, dessen Anwendung in einem Erkrankungsfall  hinreichend gerechtfertigt ist, es sei denn, es liegt ein für jedermann offensichtliches  Missverhältnis zwischen dem erforderlichen und dem tatsächlichen Aufwand vor (vgl BFH 12.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_380`)


Aufwendungen außerhalb der eigentlichen Heilbehandlung sind  jedoch auf Notwendigkeit und Angemessenheit hin zu untersuchen (vgl BFH 30.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_423`)


Zieht man die Definition des deutschen BFH für das Vorliegen einer medizinischen Indikation  („einer angezeigten Behandlung“) heran, liegt diese bei jedem diagnostischen oder  therapeutischen Verfahren, dessen Anwendung in einem Erkrankungsfall hinreichend  gerechtfertigt (angezeigt) ist, vor.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/141397.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141397.1_223`)


Die Ausführungen des BMF würden die  Weiterentwicklung des Rechts widerspiegeln wie zB Verbleiben eines Existenzminimums als  maximale Zumutbarkeit zur Zuordnung des Steuerpflichtigen und danach die Übernahme der  restlichen Kosten aus sittlichen Gründen durch andere Personen, Wegfall von  Regressansprüchen, insbesondere in der Sozialgesetzgebung und Pflege mit Krankheitskosten  etc.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_41`)


g) Aus einer FA-Anfrage an das BMF v. 13.3.2014 geht hervor, dass Erika Puttfarken  seit Jänner 2012  die FB für vier Kinder bezieht;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Erika Puttfarken` (person)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_247`)


d) Laut Abfrage der aktuellen Grunddaten des BMF zum Bf (Stand 4.7.2023) scheint seit       9.8.2016 als Wohnsitz folgende Adresse auf: D-Ort8;

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_281`)


Die FB samt Kinderabsetzbeträgen (KG) für  alle vier Kinder wurde vom Finanzamt ab Dezember 2013 (bis März 2014) vorläufig einbehalten  (siehe lt. FA-Anfrage an das BMF v. 13.3.2014).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_98`)


2001, I-10237,  BFH/NV Beilage 2002, 35, UR 2002, 84, und Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617  die Vermittlung darin, das Erforderliche zu tun, damit zwei Parteien einen Vertrag über das  jeweilige Finanzprodukt abschließen.

**False Positives:**

- `BFH` — no gold match — likely missing annotation
- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_101`)


Sowohl  der Nachweis von Gelegenheiten zum Abschluss eines Vertrages als auch die Kontaktaufnahme  mit der anderen Partei oder das Verhandeln über die Einzelheiten der gegenseitigen Leistungen  setzen voraus, dass sich die Mittlertätigkeit auf ein einzelnes Geschäft, das vermittelt werden  soll, bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

**False Positives:**

- `BFH` — similar text (different position): `BFH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_102`)


Auch aus der Freiheit des Organisationsmodells (EuGH-Urteil Ludwig in BFH/NV Beilage 2007,  398, UR 2007, 617 Randnrn.

**False Positives:**

- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_105`)


Dies gilt jedoch nach der EuGH-Rechtsprechung nur, wenn es sich  bei der einzelnen Leistung um ein im Großen und Ganzen eigenständiges Ganzes handelt, das  die spezifischen und wesentlichen Funktionen der Vermittlung erfüllt. Da somit auch Leistungen  im Rahmen einer arbeitsteiligen Vermittlung als eigenständiges Ganzes die spezifischen und  wesentlichen Funktionen der Vermittlung erfüllen müssen, sind sie nur steuerfrei, wenn der  jeweilige Vermittler eine Mittlertätigkeit ausübt, die sich auf einzelne Wertpapier- oder  Anteilsumsätze bezieht (BFH-Urteil in BStBl II 2008, 641, BFH/NV 2008, 723).

**False Positives:**

- `BFH` — similar text (different position): `BFH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_106`)


Dementsprechend  bejaht der EuGH im Urteil Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617 die Steuerfreiheit,  wenn ein Untervermittler verbindliche Vertragsangebote einzelner Interessenten einholt und  diese an den Hauptvermittler übermittelt, der sie dann nach eigener Kontrolle an das  Finanzinstitut weiterleitet (EuGH-Urteil Ludwig in BFH/NV Beilage 2007, 398, UR 2007, 617  Rdnr. 10).

**False Positives:**

- `BFH` — no gold match — likely missing annotation
- `BFH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_44`)


h) Stellungnahme der Fachabteilung für Familienbeihilfe/BMF v. 25.3.2014, woraus ua.  hervorgeht:  Die Ehegatten B (verheiratet seit 29.2.2012) sind am 22.12.2011 von Deutschland nach  Österreich übersiedelt und haben seit Jänner 2012 ihren Mittelpunkt der Lebensinteressen in  Österreich.

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt` 💣

**F1:** 0.341 | **Precision:** 0.873 | **Recall:** 0.212  

**Format:** `regex`  
**Rule ID:** `a0b7b874`  
**Description:**
Matches 'Finanzamt' and its genitive form 'Finanzamtes' followed by specific locations (cities, districts) or just the word itself, excluding 'Österreich' unless part of a specific known entity like 'Finanzamt Österreich'.

**Content:**
```
\b(Finanzamt(?:es)?(?:\s+(?:Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Österreich))?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.873 | 0.212 | 0.341 | 4364 | 3808 | 556 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3808 | 556 | 14189 |

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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_9`)


Das Finanzamt hat die Berufung ohne Erlassung einer Berufungsvorentscheidung an den  Unabhängigen Finanzsenat vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Eingabe vom 17.01.2019 an das Finanzamt begehrte der Bf die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer und Einkommensteuer 2016.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_15`)


Das Finanzamt wies die Anträge auf Wiederaufnahme der Verfahren betreffend  Einkommensteuer und Umsatzsteuer 2016 mit Bescheiden vom 25.03.2019 ab, mit der  Begründung, dass angeforderte Unterlagen nicht beigebracht worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_18`)


Mit Beschwerdevorentscheidung vom 02.09.2019 - Berichtigung des Spruches mit Bescheid  vom 13.09.2018 - wies das Finanzamt die Beschwerden ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_21`)


Der Bf führte begründend aus, dass er im Jahr 2016 in Kroatien und dann in Deutschland  gewesen sei, sodass er die Steuererklärungen nicht rechtzeitig dem Finanzamt vorlegen  konnte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florenzia Claußing` (person)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich` (address)
- `10-95-558/8694` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_5`)


Bei der Veranlagung akzeptierte das Finanzamt lediglich Werbungskosten in Höhe von 215,94 €  (Sonstige Werbungskosten: Internet 50 % PA) (Bescheid vom 14.5.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_6`)


Gegen diesen Bescheid erhob die Beschwerdeführerin mit Schriftsatz vom 23.5.2019  (eingelangt beim Finanzamt am 27.5.2019) Beschwerde, legte eine Befürwortung des  Dienstgebers hinsichtlich der getätigten Fortbildungsmaßnahmen vor und beantragte die  Aufhebung des oben genannten Bescheides und eine entsprechende Neuveranlagung unter  Berücksichtigung der Werbungskosten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_8`)


Mit Beschwerdevorentscheidung vom 21.8.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_12`)


Mit Vorlagebericht vom 7.10.2019 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_9`)


Bei einer Befragung am 8.3.2007 hat der Bf beim Finanzamt Folgendes zu Protokoll gegeben:   "Zum Fahrzeug: Es handelt sich um einen XX mit dem Kennzeichen XY, Baujahr 2005.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_34`)


Im Rahmen der Erhebungen wurden dem Finanzamt mit Schreiben vom 27.3.2007 ua.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_52`)


3. Mit Bescheid vom 22.3.2010, StrNr, hat das Finanzamt – neben der NoVA - die Umsatzsteuer  für den Erwerb eines neuen Fahrzeuges für den Zeitraum August 2005 festgesetzt;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_54`)


Begründend führte das Finanzamt aus, der Bf sei seit 2.8.1991 mit Nebenwohnsitz in Adr1,  gemeldet, wo auch seine Gattin und die Kinder mit Hauptwohnsitz gemeldet seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_65`)


In der dagegen rechtzeitig erhobenen Berufung wird im Wesentlichen eingewendet,  hinsichtlich der nun erstmaligen Festsetzung der Umsatzsteuer für August 2005 sei bereits mit  31. Dezember 2008 Verjährung eingetreten, da die Umsatzsteuer als Verkehrssteuer nach drei  Jahren verjähre und keine entsprechenden Verlängerungshandlungen (erkennbare  Amtshandlungen) seitens des Finanzamtes gesetzt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_71`)


Wenn das Finanzamt in Zusammenhalt mit der Umsatzsteuer einen 20%igen Abschlag von der  Bemessungsgrundlage vornehme, welcher Wert einem Fahrzeug mit über 6.000 km  entspreche, so gehe es offenbar von einem gebrauchten Fahrzeug aus.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_73`)


Feststellungen des Finanzamtes, dass der Bf das Fahrzeug als neues Fahrzeug erworben habe  und wann dieses nach Österreich verbracht worden sei, fehlten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_77`)


RV/0506-I/10, der  Berufung hinsichtlich der Umsatzsteuer Folge gegeben, den Bescheid in diesem Umfang  aufgehoben und begründend ausgeführt, beim berufungsgegenständlichen Fahrzeug habe es  sich insofern um ein Gebrauchtfahrzeug gehandelt, als das Finanzamt selbst im Hinblick auf  den für ein benütztes Fahrzeug vorgenommenen Abschlag von 20 % ausgegangen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_79`)


6. Aufgrund einer vom Finanzamt dagegen erhobenen Amtsbeschwerde hat der  Verwaltungsgerichtshof mit Erkenntnis vom 19.4.2016, 2013/15/0288, die vorgenannte UFS-

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_82`)


auf die in Art. 1 Abs. 9 UStG 1994 genannten  Tatbestandsvoraussetzungen - aus, dass die vom Finanzamt zugrunde gelegte  4 von 15 Seite 5 von 15

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_132`)


Laut Erhebungen des Finanzamtes zu dem an der inländischen Wohnadresse abgestellten  Fahrzeug hatte sich der Bf im Zeitraum vom 1. bis 12. Februar 2007 an 7 Tagen zu  unterschiedlichsten Zeiten am Familienwohnsitz aufgehalten (Mitteilung der Steuerfahndung  vom 27.3.2007).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_148`)


Wie aus den eigenen Angaben des Bf bei seinem Erstkontakt mit dem Finanzamt im Zuge der  Ermittlungen zu allfällig in Österreich bestehenden Abgabepflichten in Zusammenhang mit  seinem Fahrzeug hervorgeht, wurde das Fahrzeug für die Fahrt zur Arbeit und zum Besuch der  Familie in Adr1 verwendet;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_188`)


Gibt der Erwerber  die Steueranmeldung nicht ab oder erweist sich die Selbstberechnung als nicht richtig, so kann  das Finanzamt die Steuer festsetzen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_201`)


Nach der Rechtsprechung des VwGH ist es zulässig, dass das Bundesfinanzgericht den dem  Erstbescheid zugrunde gelegten Sachverhalt rechtlich anders würdigt als das Finanzamt und  den Zeitpunkt der Entstehung der Steuerschuld anders ansetzt (vgl. VwGH vom 11.9.2014,  2013/16/0156, zur Änderung des Zeitraumes bei einer Normverbrauchsabgabe;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_205`)


Das Finanzamt hatte  am 22.3.2010 die Umsatzsteuer für das im Jahr 2005 vom Bf erworbene Fahrzeug festgesetzt,  weshalb die Festsetzung innerhalb der Verjährungsfrist erfolgte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_227`)


Der maßgebliche Sachverhalt, den das Finanzamt im Bescheid über die Festsetzung der  Umsatzsteuer für den Erwerb neuer Fahrzeuge (Fahrzeugeinzelbesteuerung) vom 22.3.2010  einer Fahrzeugeinzelbesteuerung unterworfen hat, ist die nicht erfolgte Erwerbsbesteuerung  des Fahrzeuges XX mit der Fahrgestellnummer 123xx in Österreich durch den  Beschwerdeführer.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_228`)


Das Finanzamt hat die Umsatzsteuer für den Zeitraum August 2005 festgesetzt, zu diesem  Zeitpunkt konnte der Bf jedoch noch nicht wie ein Eigentümer über das Fahrzeug verfügen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klarissa Kümml` (person)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_6`)


Am 11. Jänner 2016 erfolgte beim Finanzamt eine anonyme Anzeige.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_8`)


Dieses  Zusatzeinkommen habe der Bf. beim Finanzamt nicht erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_11`)


Begründend führte das Finanzamt jeweils  aus, Ermittlungen hätten ergeben, dass der Bf. entgegen seiner Abmeldung im Zentralen  Melderegister am 10. Dezember 2013 weiterhin bis zum 1. Dezember 2015 einen Wohnsitz in  Österreich (x2x Ort2, Straße 2) gehabt habe und somit während des streitgegenständlichen  Zeitraums in Österreich gewesen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_68`)


Ihm sei es unverständlich, dass er dem Finanzamt seine  Krankengeschichte übermitteln sollte, was seine persönliche Angelegenheit sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_136`)


Trotz Aufforderung legte der Bf. diesbezüglich dem Finanzamt weder Unterlagen zum  Beschäftigungsausmaß noch zur Höhe der Einkünfte (wie z.B. AHV – Auszug) vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_143`)


Das Finanzamt hat, nachdem der Bf. die  Einkünfte nicht nachwies oder bezifferte, diese griffweise mit monatlich CHF 2.000,00 (jährlich  CHF 24.000,00) geschätzt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Finanzamtes Kirchdorf Perg Steyr` | `Finanzamtes Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Feichtenschlager` (person)
- `Daisy Wegelein` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `61-004/6209` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_15`)


Diätanforderung nicht notwendig und die damit verbundenen Kosten nicht zu berücksichtigen  seien bzw. ob das Finanzamt auch die Arztbriefe mit dem Behandlungsverlauf erhalte, damit  die Diätverpflegung Relevanz bekomme.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_17`)


Mit Schreiben vom 05.12.2018 legte das Finanzamt die Rechtslage dar und hielt der  Beschwerdeführerin vor, dass sie abweichend von den Pauschalsätzen Kosten für die  Beschaffung von Lebensmitteln geltend mache, welche bestimmte Anforderungen erfüllen  würden (Biolebensmittel, glutenfrei, Gemüse), aus deren Artikelbezeichnung aber keinesfalls  geschlossen werden könne, dass sie ausschließlich wegen der bestehenden Behinderung  konsumiert werden müssten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_24`)


Gleichzeitig werde aber vom  Finanzamt gefordert, gerade diese Mehraufwendungen zu errechnen, weil ein Abzug von  normalen Kosten der Lebensführung nach den Bestimmungen des § 20 EStG nicht möglich ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_28`)


Die Beschwerdeführerin könne natürlich feststellen, dass das Finanzamt keine ärztliche  Expertise erstellen könne, welche Lebensmittel ursächlich mit der Krankheit in Zusammenhang  stünden und welche Kosten tatsächlich durch die Krankheit und nicht durch den normalen  Lebensunterhalt verursacht würden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_31`)


Mit Schreiben vom 18.12.2018 nahm die Beschwerdeführerin zum Ergänzungsersuchen des  Finanzamtes vom 05.12.2018 wie folgt Stellung: Es sei Zeit gewesen, aus 151 Kassazetteln  einzelne Posten herauszulesen und zu hinterfragen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_40`)


Die Beschwerdeführerin werde niemals zu einem Arzt gehen, um ihn befinden zu lassen, ob die  einzelnen Medikamente und Lebensmittel, die seitens des Finanzamtes in Frage gestellt  würden, mit ihrer Behinderung in Zusammenhang stünden oder nicht.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_44`)


Für die Art der Kommunikation, wie die Beschwerdeführerin sie vom Finanzamt erfahre, habe  offensichtlich nur ein Finanzamt Zeit und Geld zur Verfügung.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_46`)


Mit Beschwerdevorentscheidung vom 10.01.2019 wies das Finanzamt die Beschwerde als  unbegründet ab, beließ den Erstbescheid unverändertund führte begründend aus:  „Nach den Bestimmungen des § 35 EStG steht einem Steuerpflichtigen jeweils ein Freibetrag für  außergewöhnliche Belastungen durch eine eigene körperliche oder geistige Behinderung zu.  Diese Pauschalsätze sind im Abs. 3 dieser Bestimmung geregelt und betragen bei einer in Ihrem  Fall festgestellten Behinderung von 30 % € 75,-.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_57`)


Es gab  somit im Ermittlungsverfahren für das Finanzamt keine Möglichkeit, den tatsächlich durch Ihre  Behinderung verursachten Mehraufwand für die Diätverpflegung festzustellen, sodass nur der  bereits im Erstbescheid berücksichtigte Pauschalbetrag für die Diätverpflegung als steuerliche  Abzugspost anerkannt werden konnte.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_66`)


Dem Finanzamt seien sämtliche von Ärzten des  Krankenhauses KH erstellte Diagnosen vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_71`)


Sie könne von  keinem Arzt erwarten, dass er die von ihm verschriebenen Medikamente des Jahre 2017 für  das Finanzamt auflisten und sich und die Beschwerdeführerin damit vor dem Finanzamt  rechtfertigen würde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_74`)


Mit Vorlagebericht vom 21.06.2019 legte das Finanzamt die Beschwerdesache dem  Bundesfinanzgericht vor und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_78`)


Im angefochtenen Einkommensteuerbescheid 2017 berücksichtigte das Finanzamt das  Pauschale für Mehraufwendungen wegen Krankendiätverpflegung von 840,00 € und den  Freibetrag von 75,00 € für eine Behinderung zwischen 25 und 34 %.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_112`)


Darüber wurde die  Beschwerdeführerin vom Finanzamt wiederholt aufgeklärt und zum entsprechenden Nachweis  aufgefordert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_121`)


Der monatliche Pauschbetrag von  70,00 € (840,00 €/Jahr) steht daher unbestritten zu.  Dass die Beschwerdeführerin einen tatsächlichen, außergewöhnlichen  Verpflegungsmehraufwand, der über die ohnehin vom Finanzamt anerkannten Mehrkosten in  Höhe des in der Verordnung genannten Betrages von 840 Euro, hinausgeht, wurde nicht  nachgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_122`)


Vom Finanzamt wurde im Erstbescheid irrtümlich zusätzlich zu diesem  Pauschale ein Betrag von 285,98 € für glutenfreie Lebensmittel berücksichtigt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_123`)


Aus der  Bescheidbegründung ist eindeutig erkennbar, dass auch das Finanzamt die zutreffende  Rechtsmeinung vertritt, wonach über den Pauschalbetrag hinaus mangels entsprechender  Beweise keine Aufwendungen berücksichtigt werden können.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_124`)


In Zusammenhang mit den geltend Kosten in Höhe von 836,94 € für Medikamente,  Rezeptgebühren, Behandlungskosten und Arzthonoraren ist in Ergänzung der Ausführungen  des Finanzamtes Folgendes auszuführen:   Gemäß § 4 der VO für außergewöhnliche Belastungen sind Kosten der Heilbehandlung im  nachgewiesene Ausmaß ohne Selbstbehalt zu berücksichtigen, sofern sie mit der Behinderung  in Zusammenhang stehen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_139`)


Die Beschwerdeführerin wurde vom Finanzamt zu einer entsprechenden Beweisführung  aufgefordert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_47`)


Zum weiteren Vorhalt, dass aus den vorgelegten Einbringungsakten  des FA nicht ersichtlich sei, welcher KöSt Bescheid dem Haftungsbescheid beigelegt wurde, da  überhaupt keine Kopien vorhanden sind, führte der Vertreter des Finanzamtes aus, dass dies  für ihn nicht mehr nachvollziehbar ist.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_8`)


Verfahrensgang  Der Beschwerdeführer (in weiterer Folge kurz BF) reichte am 13.02.2019 elektronisch über  FinanzOnline die Erklärung zur Arbeitnehmerveranlagung für 2018 beim Finanzamt ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_9`)


Mit einem Ersuchen um Ergänzung vom 27.08.2019 wurde der BF vom Finanzamt aufgefordert,  hinsichtlich der beantragten Kosten für Familienheimfahrten verschiedenste Fragen zu  beantworten und entsprechende Nachweise vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_12`)


Am 22.10.2019 erging der Einkommensteuerbescheid 2018, wobei vom Finanzamt die  beantragten Kosten für Familienheimfahrten nicht anerkannt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_14`)


Mit Beschwerdevorentscheidung vom 06.02.2020 wurde die Beschwerde vom Finanzamt als  verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_16`)


In der Begründung wurde ausgeführt, dass  die 4-wöchige Frist dem BF bewusst gewesen sei und er deshalb telefonisch beim Finanzamt  um eine 1-wöchige Verlängerung gebeten und diese auch telefonisch von einem Mitarbeiter  des Finanzamtes bewilligt bekommen habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamtes` | `Finanzamtes` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_17`)


Am 15.06.2020 wurde die Beschwerde vom Finanzamt dem Bundesfinanzgericht zur  Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_20`)


Mit Postaufgabedatum 25.11.2019 brachte der BF eine Beschwerde gegen den  Einkommensteuerbescheid 2018 ein, welche mit Beschwerdevorentscheidung des Finanzamtes  vom 06.02.2020 als verspätet zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_24`)


Die obigen Sachverhaltsfeststellungen sind allesamt aktenkundig und ergeben sich aus den  vom BF und vom Finanzamt vorgelegten Unterlagen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_25`)


Ob eine vom BF behauptete telefonische  Verlängerung der Beschwerdefrist durch einen Mitarbeiter des Finanzamtes stattgefunden hat,  ist aus den unter „4. Rechtliche Beurteilung“ angeführten Gründen nicht relevant.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_53`)


Da im gegenständlichen Fall die vom BF behauptete Beschwerdefristverlängerung, so sie denn  stattgefunden hat, nur telefonisch zwischen dem Finanzamt und dem BF "vereinbart" wurde,  lag damit aber kein vor Ablauf der Beschwerdefrist im Sinne des § 245 Abs 3 iVm § 85 BAO  wirksam gestellter Antrag auf Erstreckung der Beschwerdefrist vor und konnte solcherart auch  der Lauf der Beschwerdefrist nach § 245 Abs 3 zweiter Satz BAO nicht gehemmt werden  (VwGH 17.11.2005, 2001/13/0279).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_28`)


Im Einkommensteuerbescheid für das Jahr 2016 anerkannte das Finanzamt die Aufwendungen  unter Anrechnung eines Selbstbehaltes in gleicher Höhe, sodass die geltend gemachten Kosten  2 von 6 Seite 3 von 6

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_72`)


Die im Zusammenhang mit der Behinderung der Tochter T stehenden Aufwendungen wurden  vom Finanzamt zu Recht als außergewöhnliche Belastung mit Selbstbehalt anerkannt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_7`)


1. Verfahrensgang, Sachverhalt  Das Finanzamt (kurz FA) erließ den bekämpften Einkommensteuerbescheid mit 8. Juli 2019  weitestgehend erklärungsgemäß, reduzierte allerdings die von der Beschwerdeführerin (kurz  Bf.) als außergewöhnliche Belastung ohne Abzug eines Selbstbehaltes in Anspruch  genommenen Zahlungen um EUR 1.854,71.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_53`)


Vom Finanzamt (kurz FA) wurden EUR 4.766,81  für Begräbniskosten für den verstorbenen Vater (Nachlassüberschuldung) erklärungsgemäß  anerkannt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_97`)


Das Bundesfinanzgericht hat – wie auch das Finanzamt - die abgabepflichtigen Fälle zu  erforschen und von Amts wegen die tatsächlichen und rechtlichen Verhältnisse zu ermitteln,  die für die Abgabepflicht und die Erhebung der Abgaben wesentlich sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_99`)


Eine in der Begründung einer Beschwerdevorentscheidung getroffene Feststellung des  Finanzamtes wirkt wie ein Vorhalt und es obliegt dem Abgabepflichtigen, die vom Finanzamt in  der Begründung der Beschwerdevorentscheidung getroffene Feststellung zu widerlegen bzw.  zumindest deren Unrichtigkeit zu behaupten (vgl. VwGH 8.10.1985, 83/14/0237 etc.).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 29.5.2018 wandte sich das Finanzamt an den Beschwerdeführer (Bf.) als  verantwortlichen Geschäftsführer der GmbH, weil es die Geltendmachung der  abgabenrechtlichen Haftung nach § 9 iVm.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_14`)


3. Da die unter Punkt 1 angeführten Abgabenbeträge während Ihrer Vertretungsperiode fällig  bzw. nicht entrichtet wurden, muss das Finanzamt bis zum Beweis des Gegenteils davon  ausgehen, dass Sie der Ihnen aufgetragenen Erfüllung der abgabenrechtlichen Pflichten der  Vertretenen nicht vorschriftsgemäß nachgekommen sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_24`)


Im Fall  der Nichterbringung dieser Nachweise muss das Finanzamt davon ausgehen, dass Sie die Ihnen  obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwalteten Mitteln zu  entrichten, schuldhaft verletzt haben, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_26`)


6. Wird der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liegt es im Ermessen des Finanzamtes, die Haftung für die unter Punkt 1 genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_28`)


Pflichtverletzung allfällige Einzelinteressen verdrängt (z.B. VwGH 10.10.2005, 2004/14/0112),  sähe sich das Finanzamt veranlasst, die gesetzliche Vertreterhaftung gegen Sie im  erforderlichen Ausmaß geltend zu machen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_87`)


Wird Lohnsteuer nicht  einbehalten und an das Finanzamt abgeführt, so ist nach ständiger Judikatur des  Verwaltungsgerichtshofes ungeachtet der wirtschaftlichen Schwierigkeiten der Gesellschaft  von einer schuldhaften Pflichtverletzung des Geschäftsführers auszugehen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_88`)


Nach der durch das  Erkenntnis eines verstärkten Senates vom 18.10.1995, 91/13/0037,0038, ausdrücklich  aufrechterhaltenen ständigen Rechtsprechung des Verwaltungsgerichtshofes fällt es nämlich  einem Vertreter im Sinne des § 80 BAO als Verschulden zur Last, wenn er Löhne auszahlt, aber  die darauf entfallende Lohnsteuer nicht an das Finanzamt entrichtet (VwGH 21.1.2004,  2002/13/0218).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_6`)


Im Zuge des Ermittlungsverfahrens durch das Finanzamt legte der Bf. das Anlagenverzeichnis  2014, die Aufgliederung der „Sonstigen Werbungskosten 2014“, die Aufgliederung der  Bürokosten 2014, der Reisekosten 2014 für Anwaltstermine in Graz und der Zahlungen an den  Anwalt in einer Gesamthöhe von € 30.433,50 vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_8`)


In einem weiteren Ergänzungsersuchen teilte das Finanzamt mit, dass Kosten eines  Zivilprozesses nur dann als Werbungskosten abzugsfähig seien, wenn der Prozessgegenstand  objektiv betrachtet mit den Einkünften aus nichtselbständiger Arbeit im Zusammenhang  stünde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_9`)


Für eine diesbezügliche Beurteilung ersuchte das Finanzamt um entsprechende  Unterlagen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_11`)


Das Finanzamt beabsichtige, diese  Ausgaben nicht anzuerkennen und die Aufwendungen für EDV-Geräte um einen Privatanteil in  Höhe von 40% zu kürzen.

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt für Gebühren`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Zeno Matyssek`(person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH`(organisation)
- `Finanzamt für Gebühren`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache QZKX Beratung, Lambacher Straße 9, 3123 Mittermerking, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 45-817/1493  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `QZKX Beratung`(organisation)
- `Lambacher Straße 9, 3123 Mittermerking, Österreich`(address)
- `Mag. Dieter Walla & Partner Steuerberater OG`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `45-817/1493`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn QZKX Beratung,  nunmehr QZKX Beratung (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `QZKX Beratung`(organisation)
- `QZKX Beratung`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_23`)


Beschwerdeerwägungen:  Dem angefochtenen Bescheid über die Festsetzung von Anspruchszinsen 2007 liegt der im  Einkommensteuerbescheid 2007 des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013  ausgewiesene Differenzbetrag von € 254.913,99 zugrunde.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_45`)


Wünschenswert wäre eine  Schulung der Finanzamtsmitarbeiter über neue Formen der Diätverordnungen, damit  Astronautennahrung nicht die einzige bekannte Diätform für alles Zukunft bleibe.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Alma Gaedecke, Höbelgasse 24, 9400 St. Thomas, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien  1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alma Gaedecke`(person)
- `Höbelgasse 24, 9400 St. Thomas, Österreich`(address)
- `Finanzamtes Wien  1/23`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rainer Leutheußer`(person)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich`(address)
- `Egger & Freidorfer Steuerberatungs-OG`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

</details>

---

## `Fa. GmbH abbreviation` 

**F1:** 0.001 | **Precision:** 0.769 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `8771c637`  
**Description:**
Matches entities starting with 'Fa.' (abbreviation for Firma) followed by the company name and GmbH, ensuring no trailing spaces.

**Content:**
```
\b(Fa\.[A-Z][A-Za-z0-9\s&\-]+(?:GmbH|m\.b\.H\.)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.769 | 0.001 | 0.001 | 13 | 10 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 3 | 13788 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_96`)


Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH eingesetzt als Subunternehmer im Jahr 2009 um  Scheinfirmen handelt im vollen Umfang zurück gewiesen.

| Predicted | Gold |
|---|---|
| `Fa.POU Bau GmbH` | `Fa.POU Bau GmbH` |

**Missed by this rule (FN):**

- `Y-Montage GmbH` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_6`)


Begründung  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa.West Altrader GmbH  Dorf, wurde von einem Kontrollorgan der Parkraumüberwachung der Landes- polizeidirektion am 9. April 2021 um 17:50 Uhr in der gebührenpflichtigen Kurzparkzone in  1160 Wien, Haberlgasse 10, beanstandet, da der zur Beanstandungszeit im Fahrzeug hinter- legte Parkschein Nr. 123 nach den Wahrnehmungen des Kontrollorgans Spuren von entfernten  Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_21`)


Mit E-Mail vom 17. Mai 2021 brachte die Fa.West Altrader GmbH bei der MA 67 folgendes Schreiben ein:  „An: MA 67 Lenkererhebung …  Es ist bei uns in der Firma leider ein IRRTUM passiert: Bei der Lenkererhebung – KO 681 EB vom  19.4.21 wurde leider eine falsche Person ausgefüllt. Anbei senden wir Ihnen nun die richtige  Person, welche das KFZ zu diesem Zeitpunkt gelenkt hat.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_39`)


Entgegen der Ansicht der Magistratsabteilung 67 kann der Schriftsatz der Fa.West Altrader GmbH nicht als  Beschwerde im Verwaltungsstrafverfahren des Gundula Doerfner  gewertet werden.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Missed by this rule (FN):**

- `Gundula Doerfner` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_40`)


Weder tritt die  Fa.West Altrader GmbH in seinem Namen auf, noch beruft sie sich auf eine diesbezügliche Vollmacht.

| Predicted | Gold |
|---|---|
| `Fa.West Altrader GmbH` | `Fa.West Altrader GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_20`)


Begründend wurde ausgeführt, da es sich um den gleichen Sachverhalt wie im Jahr 2011  handle (korrigierter Lohnzettel der Fa.Recycling Traderlog GmbH nach einer Lohnsteuerprüfung) werde die  gesetzliche Rechtsmittelfrist daher als ausreichend erachtet.

| Predicted | Gold |
|---|---|
| `Fa.Recycling Traderlog GmbH` | `Fa.Recycling Traderlog GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134768.1_25`)


Arbeitgeber  Fa.Recycling Traderlog GmbH  Aufgrund der dort festgestellten Sachverhalte wurde ein berichtiger Lohnzettel erstellt und  übermittelt (s. Einkommensteuerbescheid 2012 vom 19.06.2018)"

| Predicted | Gold |
|---|---|
| `Fa.Recycling Traderlog GmbH` | `Fa.Recycling Traderlog GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_49`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_38`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, hat das Schreiben der Fa.West Altrader GmbH vom  17. Mai 2021 als Beschwerde gegen das an Gundula Doerfner  als Beschuldigten ergangene  Straferkenntnis vom 7. Mai 2021 gewertet und dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Fa.West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)
- `Bundesfinanzgericht`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_41`)


Angesichts der Vorgeschichte und der eindeutigen Formulierung (vgl. Hengstschläger/Leeb,  AVG I (2. Ausgabe 2014) § 13 Rz 37) handelt es sich um eine Nachreichung im Verfahren der Fa.West Altrader GmbH betreffend Lenkerauskunft, wo eine im Nachhinein erfolgte Richtigstellung der am 23.  April 2021 erteilten Lenkerauskunft vorgenommen wurde.

**False Positives:**

- `Fa.West Altrader GmbH` — partial — gold is substring of pred: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Altrader GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_50`)


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

## `Landesgericht with city` 

**F1:** 0.001 | **Precision:** 0.667 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b71bf20`  
**Description:**
Matches 'Landesgericht' followed by a city name (capitalized word) as an organisation.

**Content:**
```
\bLandesgericht(?:es)?\s+([A-Z][A-Za-zäöüß]+(?:\s+[A-Z][A-Za-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.000 | 0.001 | 12 | 8 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 4 | 16417 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_27`)


Dies ergebe sich daraus, dass der über das  Vermögen der Gesellschaft eröffnete Konkurs mit Beschluss des Landesgerichtes Ort vom tt.  Juli 2014 nach der Schlussverteilung gemäß § 139 Insolvenzordnung (IO) aufgehoben worden  sei.

| Predicted | Gold |
|---|---|
| `Landesgerichtes Ort` | `Landesgerichtes Ort` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_91`)


Mit Beschluss des  Landesgerichtes Ort vom tt. Juni 2013 wurde über das Vermögen der Gesellschaft der Konkurs  eröffnet und am 4. Juli 2013 die Schließung des Unternehmens angeordnet.

| Predicted | Gold |
|---|---|
| `Landesgerichtes Ort` | `Landesgerichtes Ort` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_112`)


Mit Beschluss des Landesgerichtes Ort vom tt. Juli 2014 wurde der am tt. Juni 2013 über das  Vermögen der Gesellschaft eröffnete Konkurs nach der Schlussverteilung aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichtes Ort` | `Landesgerichtes Ort` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_49`)


Im Urteil des Landesgerichtes LG (yCgyy/yyy vom Datum_2; dieses Urteil wurde vom Obersten  Gerichtshof am Datum_1, xObxxx/xxx bestätigt) werde festgehalten, „... dass die beklagte  Partei für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden ... haftet“.

| Predicted | Gold |
|---|---|
| `Landesgerichtes LG` | `Landesgerichtes LG` |

**Missed by this rule (FN):**

- `Obersten  Gerichtshof` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_62`)


In diesem Verfahren entschied der Oberste Gerichtshof mit Urteil vom Datum_1, xObxxx/xxx,  zugunsten der Bf als Klägerin und bestätigte das Urteil des Landesgerichtes LG vom Datum_2,  yCgyy/yyy.

| Predicted | Gold |
|---|---|
| `Landesgerichtes LG` | `Landesgerichtes LG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_64`)


In weiterer Folge schlossen die Bf und der Bund am 15. September 2016 vor dem  Landesgericht LG einen gerichtlichen Vergleich betreffend Verdienstentgang iHv 73.234,55  Euro netto (Gehaltsdifferenzen netto und Prüfungsgebühren netto) sowie Zinsen iHv 5.760  Euro netto für den Zeitraum bis zum 30. September 2016 ab.

| Predicted | Gold |
|---|---|
| `Landesgericht LG` | `Landesgericht LG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_68`)


Das vom Obersten Gerichtshof bestätigte Urteil des Landesgerichtes LG diente in der Folge als  Rechtgrundlage für die weiteren Nettozahlungen der B an die Bf im streitgegenständlichen Jahr  2019.

| Predicted | Gold |
|---|---|
| `Landesgerichtes LG` | `Landesgerichtes LG` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_113`)


Darüber hinaus hat das Landesgericht LG im rechtskräftigen Zwischen- und Teilurteil vom  Datum_2, yCgyy/yyy, festgestellt, dass der Bund als beklagte Partei der Bf als klagender Partei  auch für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden aus den  Mobbinghandlungen haftet.

| Predicted | Gold |
|---|---|
| `Landesgericht LG` | `Landesgericht LG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Beschluss des Landesgerichtes XY vom tt.10.2018, Az.

**False Positives:**

- `Landesgerichtes XY` — partial — gold is substring of pred: `Landesgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_7`)


Mit Beschluss des Landesgerichtes XY vom tt.07.2020 AZ s wurde der Konkurs über die  Primärschuldnerin nach Schlussverteilung aufgehoben.

**False Positives:**

- `Landesgerichtes XY` — partial — gold is substring of pred: `Landesgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_87`)


Mit Beschluss des Landesgerichtes XY vom 25.10.2018,  Az.

**False Positives:**

- `Landesgerichtes XY` — partial — gold is substring of pred: `Landesgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_89`)


Mit Beschluss des  Landesgerichtes XY vom tt.07.2020 AZ s wurde der Konkurs über die Primärschuldnerin nach  Schlussverteilung einer Quote von 1,9% aufgehoben.

**False Positives:**

- `Landesgerichtes XY` — partial — gold is substring of pred: `Landesgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichtes`(organisation)

</details>

---

## `Verwaltungsgericht Wien` 💣

**F1:** 0.001 | **Precision:** 0.583 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a1ae13a8`  
**Description:**
Matches the specific entity 'Verwaltungsgericht Wien' and its genitive form 'Verwaltungsgerichtes Wien' or 'Verwaltungsgericht Wien'.

**Content:**
```
\bVerwaltungsgericht(?:es)?\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.583 | 0.000 | 0.001 | 12 | 7 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 5 | 10100 |

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

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_12`)


Der vorliegende Fall unterscheidet sich  durch die Nennung der zuständigen Behörde (Magistrat der Stadt Wien) im Bescheid von  demjenigen Fall, welcher der zurückweisenden Entscheidung des Verwaltungsgerichtes Wien  vom 5.1.2022, VGW-001/V/086/16561/2021 zugrundelag und welcher laut jener Entscheidung  durch die Nichtnennung der Behörde „Magistrat der Stadt Wien“ im Bescheid dieser Behörde  nicht zurechenbar wäre.

**False Positives:**

- `Verwaltungsgerichtes Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_27`)


C) Am 11. Mai 2020 brachte der Bf. einen Verfahrenshilfeantrag (auf einem Formular des  Verwaltungsgerichtes Wien) beim Magistrat der Stadt Wien zwecks Weiterleitung an das  Verwaltungsgericht ein.

**False Positives:**

- `Verwaltungsgerichtes Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_43`)


E) Das Verwaltungsgericht Wien beraumte zunächst eine mündliche Verhandlung über die  Beschwerde für den 17.11.2020 an, welche mit Schreiben des Verwaltungsgerichtes Wien vom  16.11.2020 wieder abberaumt wurde, und zwar mit folgender Begründung: „Der  gegenständliche Akt wird im Hinblick darauf, dass die Beschwerde sich gegen die Verweigerung  der Rückzahlung der pauschalierten Parkometerabgabe gemäß Wr. Parkometergesetz 2006  iVm der VO des Wiener Gemeinderates über die pauschale Entrichtung der Parkometerabgabe  (PauschaIierungsverordnung) richtet, gemäß § 6 AVG an das Bundesfinanzgericht  weitergeleitet und abgetreten.“  F) Die gegenständliche Beschwerde vom 8. Juli 2020 langte beim Bundesfinanzgericht ein.

**False Positives:**

- `Verwaltungsgerichtes Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgericht Wien`(organisation)
- `Wiener Gemeinderates`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/145527.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145527.1_17`)


Soweit sich die Beschwerde  gegen die Abweisung des Antrags auf Zahlungserleichterung hinsichtlich der (zwei)  Verkehrsstrafen nach der StVO 1960 richtet, wird auf die Zuständigkeit des  Verwaltungsgerichtes Wien verwiesen (Gesamtsumme € 176,00).

**False Positives:**

- `Verwaltungsgerichtes Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/146673.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146673.1_25`)


Die belangte Behörde übermittelte mittels E-Mail vom 13. Jänner 2025 den Beschluss des  Verwaltungsgerichtes Wien vom 25. Oktober 2025, mit welchem dessen Beschwerdeverfahren  eingestellt wurde, da der Beschwerdeführer die Beschwerde mit E-Mail vom 23. Oktober 2024  zurückgezogen hat.

**False Positives:**

- `Verwaltungsgerichtes Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Landesgericht standalone` 💣

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `4c1b3e04`  
**Description:**
Matches 'Landesgericht' and its genitive form 'Landesgerichts' when NOT followed by a city name, to avoid duplication with the new 'Landesgericht with city' rule.

**Content:**
```
\bLandesgericht(?:es)?\b(?!\s+[A-Z][A-Za-zäöüß])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 18 | 9 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 9 | 17592 |

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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_100`)


Als  Grundlage für diese Annahme wurden die vorliegenden, von Polizeihubschraubern aus,  aufgenommenen Luftbilder, die am Grundstück aufgenommenen Fotos, das für das  Landesgericht für Strafsachen abgegebene Gutachten der Abteilung für Wasserwirtschaft und  diverse Anzeigen herangezogen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_160`)


Am 10.9.2018 übermittelte das Finanzamt Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde gemäß § 100 Abs. 2 StPO den Zwischen- und Abschussbericht an die  Staatsanwaltschaft Wien beim Landesgericht für Strafsachen und diese legte am 15.7.2019 die  Anklageschrift dem Landesgericht für Strafsachen Wien vor.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen`
- `Landesgericht` — similar text (different position): `Landesgericht für Strafsachen`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Landesgericht für Strafsachen`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_174`)


Sachverhaltsmäßig steht fest, dass das Landesgericht für Strafsachen Wien auch betragsmäßig  die Sachverhaltsfeststellungen der Betriebsprüfung bestätigt hat und es als erwiesen  angenommen hat, dass der Bf. die oben angeführten Taten in objektiver und subjektiver  Hinsicht begangen hat.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_175`)


Unstrittig ist weiters, dass das Landesgericht für Strafsachen Wien bei Ermittlung des  Sachverhaltes von Amts wegen vorzugehen hatte.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_185`)


Das Landesgericht für Strafsachen Wien hat in seinem Urteil vom 23.9.2019 festgestellt, dass  der Bf. die oben angeführten Taten in objektiver und subjektiver Hinsicht begangen hat, und es  dabei billigend in Kauf nahm und sich damit abfand seine abgabenrechtliche Anzeige-,  Offenlegungs- bzw. Wahrheitspflicht zu verletzen und damit die im Spruch des Strafurteils  genannten Abgaben zu verkürzen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_186`)


Das Landesgericht für Strafsachen Wien hat die Abgabenforderungen, welche aufgrund der  Feststellungen der Betriebsprüfung, hinsichtlich Einkommensteuer und Umsatzsteuer,  festgesetzt wurden, bestätigt.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/143785.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143785.1_28`)


Dass der von der Sicherstellung betroffene  Abgabenmehrbetrag nicht korrekt berechnet worden ist, sei mittlerweile vom Landesgericht  für Strafsachen, von einem Gerichtssachverständigen im Strafverfahren und vom Spruchsenat  beim Amt für Betrugsbekämpfung festgestellt worden (Anmerkung: Die Beschwerde gegen den  Sicherstellungsauftrag ist mit Beschwerdevorentscheidung vom 23.07.2020 als unbegründet  abgewiesen worden; der Sicherstellungsauftrag ist rechtskräftig).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht  für Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht  für Strafsachen`(organisation)
- `Amt für Betrugsbekämpfung`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/145202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145202.1_39`)


Sie werden jeweils vom Landesgericht für Zivilrechtssachen in  Wien bekanntgegeben und jährlich vom BMF unter www.bmf.gv.at veröffentlicht.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen in  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen in  Wien`(organisation)
- `BMF`(organisation)

</details>

---

## `Landesgerichts standalone` 

**F1:** 0.000 | **Precision:** 0.400 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46bffd33`  
**Description:**
Matches 'Landesgerichts' (genitive) when NOT followed by a city name, to avoid duplication with the 'Landesgericht with city' rule and ensure it is captured.

**Content:**
```
\bLandesgerichts\b(?!\s+[A-Z][a-z]+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.000 | 0.000 | 5 | 2 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 3 | 6754 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/146692.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146692.1_38`)


Die Glücksspielabgaben für die  in diesen Glücksspielabgabenbescheiden ausgewiesenen Zeiträume sowie der Selbstberechnung  für 06/2018 sind bei der PS uneinbringlich, da das Konkursverfahren nach Schlussverteilung  aufgehoben wurde (14 S AZ des Landesgerichts XY).

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_27`)


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

## `GmbH after article` 💣

**F1:** 0.019 | **Precision:** 0.347 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `ffebdeda`  
**Description:**
Matches GmbH entities preceded by the definite article (der, die, das) ONLY when the article is immediately followed by the company name, explicitly excluding cases with hyphenated prefixes like 'Bf-', 'COFAG-', or 'COVID-19'.

**Content:**
```
(?<!\w)(?:der|die|das)\s+((?!Bf-|COFAG-|COVID-19)[A-Z][A-Za-z0-9\s&\-]+(?:GmbH|m\.b\.H\.)\s*(?:Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|Steuerberatungs- und Wirtschaftsprüfungsgesellschaft)?)(?=\s|$|[,;])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.347 | 0.010 | 0.019 | 507 | 176 | 331 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 176 | 331 | 17708 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_14`)


Die Beschwerdeführerin ist in der B & Co GmbH als kaufmännische Angestellte im  Arbeitsbereich Leitung Expedit und Lager beschäftigt und gleichzeitig als  Gefahrengutbeauftragte tätig.

| Predicted | Gold |
|---|---|
| `B & Co GmbH` | `B & Co GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_5`)


12.2015 wurde zwischen der See Wilbach Dienstleistungen GmbH als Verpächterin und Hrn. K sowie der Vincent und Zielinska Solar GmbH  als Pächter (= Bf) ein Pachtvertrag mit auszugsweise folgendem Inhalt abgeschlossen:     "Definitionen

| Predicted | Gold |
|---|---|
| `See Wilbach Dienstleistungen GmbH` | `See Wilbach Dienstleistungen GmbH` |

**Missed by this rule (FN):**

- `Vincent und Zielinska Solar GmbH` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_23`)


Am x.2008 wurde gegenüber der Unter Wilkel GmbH der  Konkurs eröffnet.

| Predicted | Gold |
|---|---|
| `Unter Wilkel GmbH` | `Unter Wilkel GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_25`)


Die Bf. nannte der AP als Ansprechperson bei der Unter Wilkel GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der Unter Wilkel GmbH noch deren  Vorgängerin, der P-GmbH angestellt. Die Bf. konnte den bereits in einem Schreiben vom  November 2007 erstmals erwähnten Geschäftskontakt nicht klären und war die genannte  Person, Herr K., für die AP weder im In- noch im Ausland auffindbar.

| Predicted | Gold |
|---|---|
| `Unter Wilkel GmbH` | `Unter Wilkel GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_6`)


Mit Verschmelzungsvertrag vom 27. September 2012 wurde die Bf als  übertragende Gesellschaft mit der Valsyn-Maschinenbau GmbH als übernehmende Gesellschaft rückwirkend per  31. Dezember 2011 verschmolzen und in weiterer Folge am 31. Oktober 2012 im Firmenbuch  gelöscht.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_38`)


Die angefochtenen Bescheide seien alle am 9. Juli 2013 an die "Alexandra Kesler" als  Bescheidadressat ausgestellt worden, obwohl diese Gesellschaft verschmelzungsbedingt  bereits am 31. Oktober 2012 im Firmenbuch gelöscht worden sei und damit eine  Gesamtrechtsnachfolge an die Valsyn-Maschinenbau GmbH eingetreten sei.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Alexandra Kesler` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_40`)


Über die Beschwerde wurde erwogen:    Entscheidungsrelevanter Sachverhalt  Mit Verschmelzungsvertrag vom 27. September 2012 wurde die Bf, dh die Schameitat Sanitär GmbH  mit  Wirkung zum 31. Dezember 2011 durch Übertragung ihres Vermögens als Ganzes mit der Valsyn-Maschinenbau GmbH im Wege der Gesamtrechtsnachfolge unter Inanspruchnahme der Begünstigungen des  Artikel I Umgründungssteuergesetz (UmgrStG) verschmolzen.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Schameitat Sanitär GmbH` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_52`)


Die angefochtenen Bescheide der belangten Behörde vom 9. Juli 2013 sind an die zu diesem  Zeitpunkt bereits mit der Valsyn-Maschinenbau GmbH verschmolzene Schameitat Sanitär GmbH ergangen.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Schameitat Sanitär GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Missed by this rule (FN):**

- `Spies&Wickert Solar GmbH€` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_95`)


Am 29.11.2012 wurde die Spies&Wickert Solar GmbH infolge rechtskräftiger Nichteröffnung eines  Insolvenzverfahrens mangels kostendeckenden Vermögens und Zahlungsunfähigkeit aufgelöst.

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

| Predicted | Gold |
|---|---|
| `Martinssen Versicherung GmbH` | `Martinssen Versicherung GmbH` |

**Missed by this rule (FN):**

- `KommR Eckard Gaiss, Bakk. phil.` (person)
- `09-07-088/5911` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_17`)


Am 12. August 2019 wurde unsere Mandantschaft telefonisch vom Finanzamt darüber  informiert, dass die UVA 05/2019 der Gerstbreu Umwelt GmbH nicht gemeldet wurde.

| Predicted | Gold |
|---|---|
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_24`)


Daraufhin hat unsere  Mandantschaft die UVA 05/2019 für die Gerstbreu Umwelt GmbH nochmals hochgeladen.

| Predicted | Gold |
|---|---|
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_31`)


Als Beilage dürfen wir Ihnen nachfolgende Unterlagen übermitteln:   XML-Datenträger UVA 05/2019 betreffend die Gerstbreu Umwelt GmbH  Fax an das Finanzamt 13.08.2019 inkl. UVA 05/2019 und Produktionsübermittlung  vom 12.Juli 2019 betreffend die Gerstbreu Umwelt GmbH inkl. Antrag betreffend die Übertragung  eines Geldbetrages für die KommR Eckard Gaiss, Bakk. phil.  und für die Martinssen Versicherung GmbH vom 15. Juli 2019 inkl.  Übermittlung der Rechnungen mit den größeren Vorsteuerbeträgen inkl.  Faxbestätigung vom 13. August 2019  Weiters stellen wir den Antrag den Säumniszuschlag in Höhe von EUR 9.843,92 herabzusetzen  bzw. nicht festzusetzen, da unserer Mandantschaft aus oben angeführten Gründen an der  Versäumnis kein grobes Verschulden trifft.

| Predicted | Gold |
|---|---|
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |
| `Gerstbreu Umwelt GmbH` | `Gerstbreu Umwelt GmbH` |
| `Martinssen Versicherung GmbH` | `Martinssen Versicherung GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `KommR Eckard Gaiss, Bakk. phil.` (person)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

| Predicted | Gold |
|---|---|
| `Martinssen Versicherung GmbH` | `Martinssen Versicherung GmbH` |

**Missed by this rule (FN):**

- `Gerstbreu Umwelt GmbH` (organisation)
- `KommR Eckard Gaiss, Bakk. phil.` (person)
- `09-07-088/5911` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_5`)


Verfahrensverlauf  Mir Haftungsvorhalt vom 1. Oktober 2014 teilte die belangte Behörde der Beschwerdeführerin  (in der Folge Bf) mit, dass beabsichtigt sei, sie für diverse Abgabenschuldigkeiten  (Umsatzsteuer, Körperschaftsteuer, Lohnsteuer, Dienstgeberbeitrag samt Zuschlag sowie  Nebenansprüche) betreffend den Zeitraum 2012 bis 2013 der Garten Taltralex GmbH (in der Folge  Gesellschaft), deren Geschäftsführerin die Bf gewesen sei, im Gesamtausmaß von 37.817,42  Euro als Haftungsverpflichtete in Anspruch zu nehmen.

| Predicted | Gold |
|---|---|
| `Garten Taltralex GmbH` | `Garten Taltralex GmbH` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_94`)


Die Bf war seit Gründung der Garten Taltralex GmbH Alleingesellschafterin und alleinige Geschäftsführerin  der Gesellschaft.

| Predicted | Gold |
|---|---|
| `Garten Taltralex GmbH` | `Garten Taltralex GmbH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_12`)


Der Bf. erhob Beschwerde gegen den Einkommensteuerbescheid für das Jahr 2013 und führte  aus, dass Löhne doppelt berücksichtigt worden seien, weil er den Lohn von 1.9. bis 17.10.2013  bei der IEF Service GmbH eingeklagt habe.

| Predicted | Gold |
|---|---|
| `IEF Service GmbH` | `IEF Service GmbH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_13`)


Der Bf. legte eine Aufstellung der IEF Service GmbH vom 8.8.2018 vor, aus welcher  Bruttoauszahlungen von € 4.735,91 und eine Nettoauszahlung von € 3.812,76 zu ersehen sind.

| Predicted | Gold |
|---|---|
| `IEF Service GmbH` | `IEF Service GmbH` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_15`)


Das Finanzamt erließ am 31.8.2018 eine abändernde Beschwerdevorentscheidung, in welcher  Bezüge aus nichtselbständiger Arbeit seitens der KGMBH in reduzierter Höhe von netto €  9.926,23 /brutto € 12.598,14, sowie unverändert gegenüber dem Erstbescheid Zahlungen der  IEF Service GmbH in Höhe von € 3.132,68 netto/ brutto € 4.735,91 enthalten sind.

| Predicted | Gold |
|---|---|
| `IEF Service GmbH` | `IEF Service GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thomas Drieschner  in der Beschwerdesache Gebhard Determann,  Mooseggweg 49, 9624 Fritzendorf, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` | `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Thomas Drieschner` (person)
- `Gebhard Determann` (person)
- `Mooseggweg 49, 9624 Fritzendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_6`)


weiters ein mit der Beischmidt KI GmbH am  2.9.2019 geschlossener Lehrvertrag zum Lehrberuf "Medienfachfrau", Dauer 3 Jahre,  vorgesehene Lehrzeit 3.9.2019 bis 28.1.2022.

| Predicted | Gold |
|---|---|
| `Beischmidt KI GmbH` | `Beischmidt KI GmbH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 04.06.2020 teilte die belangte Behörde der Beschwerdeführerin in  Wahrung des Parteiengehörs mit, dass sie laut einer amtlichen Feststellung vom 20. April 2017  im Betrieb der Lodewijks Pharma GmbH in V, drei Wettterminals gehalten habe, die nicht ordnungsgemäß zur  Wettterminalabgabe angemeldet gewesen seien.

| Predicted | Gold |
|---|---|
| `Lodewijks Pharma GmbH` | `Lodewijks Pharma GmbH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Mit "Kauf- und Wohnungseigentumsvertrag" vom 21.10.1998 hatte A (=  Beschwerdeführerin, Bf) von der Lemcon Entwicklung GmbH an der Liegenschaft in EZ1 (= Gst12 im  Gesamtausmaß von 734 m²) 25/481 ideelle Miteigentumsanteile erworben.

| Predicted | Gold |
|---|---|
| `Lemcon Entwicklung GmbH` | `Lemcon Entwicklung GmbH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_17`)


Gemäß Vertragspunkt III. übergibt die Zeitlhoefler Landwirtschaft GmbH 92/573 Miteigentumsanteile aus ihren Anteilen  in das Eigentum der Bf.   Sämtliche mit der Vertragserrichtung verbundenen Kosten, insbesondere die daraus  resultierende Grunderwerbsteuer, sind von der Bf zu tragen (Pkt. V.).

| Predicted | Gold |
|---|---|
| `Zeitlhoefler Landwirtschaft GmbH` | `Zeitlhoefler Landwirtschaft GmbH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_154`)


Ein Jahr später, unmittelbar nach Einreichung des Jahresabschlusses (JA) 2008 der Synkel-Versicherung GmbH im  Firmenbuch (FB), eröffnete das LGZ Graz am 21.Okt.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_156`)


2010 das Konkursverfahren über das Vermögen der Synkel-Versicherung GmbH  Nach  Konkursaufhebung mangels kostendeckenden Vermögens und zwei geringfügigen  Nachtragsverteilungen erfolgte am 18.Juli 2012 die amtswegige Löschung der Synkel-Versicherung GmbH im  Firmenbuch (Quelle: FB FN 999999z, abgabenbehördl.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_158`)


Bereits lange vor Gründung der Synkel-Versicherung GmbH betrieb der Bf den Handel mit und die Montage von  Fenstern und Türen, ab Juni 2005 als Komplementär einer KEG (FN 999996x, nachfolgend  L-KEG;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_163`)


Die verfahrensgegenständliche AP fand während des Insolvenzverfahrens der Synkel-Versicherung GmbH statt  (Okt.2011-Febr.2012).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_199`)


In den im AP-Verfahren von der Fa A.-Fenster zur L-KEG und der Synkel-Versicherung GmbH beigeschafften  Buchhaltungsunterlagen finden sich auf dem Kundenkonto der L-KEG bis Ende Mai 2007  Umsätze von rd. 44.300,- € (davon bezahlt rd 33.000,- €).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_202`)


Die Fa A.-Fenster bezahlte Rechnungen an die L-KEG (und auch später an die Synkel-Versicherung GmbH –  regelmäßig abzüglich Skonti sowie Haft-(HR)/Deckungsrücklässen (DR) - mittels elektron.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_206`)


Ein Kundenkonto für die Synkel-Versicherung GmbH war im Rechnungswesen der Fa A.-Fenster erst ab Sept.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_209`)


In der Folge wurde die  Geschäftsbeziehung der Fa A.-Fenster mit der Synkel-Versicherung GmbH buchhalterisch über dieses neue  Kundenkonto abgewickelt.  Abweichend vom Rechenwerk der Fa A.-Fenster scheinen in der Buchhaltung der Synkel-Versicherung GmbH auf  dem Konto „Erlöse für Bauleistungen § 19 UStG“ bereits ab 11.Juni 2007 Ausgangsrechnungen  (AR) mit fortlaufender ReNr ab 1/2007 auf, darunter auch jene Rechnungen, welche in der  Buchhaltung der Fa A.-Fenster bis 24.Aug.2007 auf dem Kundenkonto der L-KEG verbucht sind.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_210`)


Vor dem dargestellten Hintergrund geht das BFG davon aus, dass Letzteren Leistungen der Synkel-Versicherung GmbH zugrunde liegen und die zugehörigen Erlöse bei der Synkel-Versicherung GmbH versteuert wurden.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_211`)


Dem AP-Bericht ist nicht zu ersehen, dass bei der Synkel-Versicherung GmbH erfasste Erlöse aus AR des  3.Quartals 2007 an die Fa A.-Fenster im Zuge der AP aus den Besteuerungsgrundlagen 2007  ausgeschieden wurden.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_213`)


Dagegen entnahm  er die Erlöse der Synkel-Versicherung GmbH der Buchhaltung des geprüften Unternehmens (Kundenkonto A.- Fenster/ Kto K00100, AP-Akt OZ 29).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_23`)


Zu den Lohnabgaben führte das FA aus das  diese von der GmbH selbst bekannt gegeben worden seien.

**False Positives:**

- `FA aus das  diese von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_109`)


Der Haftungsbescheid wurde im Jahr 2016 und damit vor Eintritt der Verjährung der der  Haftung zugrunde gelegten Abgaben der GmbH erstellt.   Persönliche Haftungen werden durch Haftungsbescheid geltend gemacht.

**False Positives:**

- `Haftung zugrunde gelegten Abgaben der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_3`)


Der Beschwerde wird teilweise stattgegeben und der Beschwerdeführer für folgende Abgaben  als Geschäftsführer der AlpenMonwilderSoftware GmbH GmbH in Anspruch genommen:    Umsatzsteuer 10/2017 170,46  Umsatzsteuer 11/2017 4.559,13  Lohnsteuer 11/2017 1.005,18  Lohnsteuer 01/2018 147,92  Dienstgeberbeitrag (DB) 11/2017 693,46  Dienstgeberbeitrag 12/2017 48,42  Dienstgeberbeitrag 01/2018 66,92  Zuschlag zum DB (DZ) 11/2017 44,90  Zuschlag zum DB (DZ) 01/2018 5,80  Körperschaftsteuer 01-03/2018 117,88    6.860,07

**False Positives:**

- `AlpenMonwilderSoftware GmbH GmbH` — partial — gold is substring of pred: `AlpenMonwilderSoftware GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `AlpenMonwilderSoftware GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_38`)


Unter der Wahrnehmung der  steuerlichen Interessen der GmbH habe er einen Nervenzusammenbruch erlitten.

**False Positives:**

- `Wahrnehmung der  steuerlichen Interessen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Beschwerdesache Vincent und Zielinska Solar GmbH ` — partial — gold is substring of pred: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_5`)


12.2015 wurde zwischen der See Wilbach Dienstleistungen GmbH als Verpächterin und Hrn. K sowie der Vincent und Zielinska Solar GmbH  als Pächter (= Bf) ein Pachtvertrag mit auszugsweise folgendem Inhalt abgeschlossen:     "Definitionen

**False Positives:**

- `Vincent und Zielinska Solar GmbH ` — partial — gold is substring of pred: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See Wilbach Dienstleistungen GmbH`(organisation)
- `Vincent und Zielinska Solar GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_16`)


Die Bezahlung der Rechnung erfolgte durch Überweisung auf das auf der Rechnung der Unter Wilkel GmbH angeführte Bankkonto.

**False Positives:**

- `Rechnung der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_17`)


Im weiteren Prüfungsverlauf stellte die AP dazu fest, dass es sich beim rechnungsausstellenden  Unternehmen, der Unter Wilkel GmbH  vormals P-GmbH, um ein Unternehmen handelte, dass die  angegebenen Leistungen nicht erbracht haben konnte.

**False Positives:**

- `Unter Wilkel GmbH  vormals P-GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_21`)


Aus einem der AP vorliegenden Kontoauszug der Unter Wilkel GmbH  war ersichtlich, dass  dem Zahlungseingang, infolge der Überweisung der Bf. von Euro 180.000,00, eine  Barabhebung am nächsten Tag in nahezu gleicher Höhe (179.695,00) gegenüberstand.

**False Positives:**

- `AP vorliegenden Kontoauszug der Unter Wilkel GmbH ` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_25`)


Die Bf. nannte der AP als Ansprechperson bei der Unter Wilkel GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der Unter Wilkel GmbH noch deren  Vorgängerin, der P-GmbH angestellt. Die Bf. konnte den bereits in einem Schreiben vom  November 2007 erstmals erwähnten Geschäftskontakt nicht klären und war die genannte  Person, Herr K., für die AP weder im In- noch im Ausland auffindbar.

**False Positives:**

- `AP als Ansprechperson bei der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`
- `P-GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)
- `Unter Wilkel GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_27`)


Die AP kam nach umfassend durchgeführten Erhebungen und Prüfungen zum Schluss (siehe  dazu die Ausführungen im Bericht der AP), dass weder ein Nachweis noch die  Glaubhaftmachung der Leistungserbringung der Unter Wilkel GmbH vorgelegen war.

**False Positives:**

- `Glaubhaftmachung der Leistungserbringung der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_43`)


Es lasse  sich nicht ableiten, wie Herr K. in den Genuss der „Vorteilszuwendung“ gekommen sei, da die  Rechnung durch die Unter Wilkel GmbH ausgestellt und der Betrag an diese überwiesen worden sei.

**False Positives:**

- `Rechnung durch die Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_48`)


In der Stellungnahme der AP zum Rechtsmittel betreffend die Kapitalertragsteuer, war u.a.  festgehalten, dass für die AP eindeutig festgestanden sei, dass der Rechnung der Unter Wilkel GmbH  keine Leistung zugrunde gelegen sei.

**False Positives:**

- `Rechnung der Unter Wilkel GmbH ` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_63`)


Im gegenständlichen Fall wurden durch die Bf. Betriebsausgaben iHv Euro 180.000,00 geltend  gemacht, denen in der Rechnung der Unter Wilkel GmbH (Rechnungsdatum 8.3.2008) angeführte  Leistungen zugrunde lagen.

**False Positives:**

- `Rechnung der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_72`)


Der in Rechnung gestellte Betrag wurde von der Bf.  unstrittig durch Überweisung auf das Bankkonto der Rechnungsausstellerin, der Unter Wilkel GmbH  bezahlt. Der Betrag wurde nachweislich vom Konto dieses Unternehmens bar behoben.

**False Positives:**

- `Unter Wilkel GmbH ` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_78`)


Es lagen keine  Feststellungen der AP dazu vor inwieweit ein Naheverhältnis zwischen den für die Unter Wilkel GmbH  handelnden Personen und den Gesellschaftern der Bf. oder diesen nahestehenden Personen  bestanden hätte.

**False Positives:**

- `Unter Wilkel GmbH ` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_81`)


Auch wenn aufgrund der zur genannten Rechnung getroffenen Feststellungen Zweifel daran  bestanden, dass das auf den Überweisungsbelegen genannte Unternehmen, die Unter Wilkel GmbH  tatsächlich den Betrag erhalten und darüber verfügt hatte, so war dieser Zweifel ohne weitere  Beweise nicht ausreichend um von einem Rückfluss des Betrages an die Bf. auszugehen.

**False Positives:**

- `Unter Wilkel GmbH ` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_174`)


Mit Schreiben vom 25.2.2020 wurde an DI Zeuge2 eine schriftliche Zeugeneinvernahme zum  Beweisthema AfA-Satz von 3% für die auf der Liegenschaft EZGST bestehenden Gebäude laut  den Schreiben an die Alwerkmon-Pharma  GmbH vom 14.11.2011 und vom 29.2.2012 versendet.

**False Positives:**

- `Alwerkmon-Pharma  GmbH` — partial — gold is substring of pred: `Alwerkmon-Pharma`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alwerkmon-Pharma`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_35`)


In diesem Ausgabenbetrag seien Fremdleistungen von zwei Subunternehmen enthalten:  1.) Rechnungen der Firma C Bau GmbH € 228.630,13  2.)

**False Positives:**

- `Firma C Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_48`)


Die vom Bf. vorgelegten Unterlagen wurden seitens des Bundesfinanzgerichts dem Finanzamt  zur Stellungnahme übermittelt.  In der Stellungnahme führte das Finanzamt aus, dass die Firma Spies&Wickert Solar GmbH geprüft worden sei  und die UIDNR.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `Finanzamt`(organisation)
- `Finanzamt`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_51`)


Im Zuge einer Betriebsprüfung in einem  anderen Unternehmen seien die Rechnungen der Firma Spies&Wickert Solar GmbH überprüft und als  Scheinrechnungen beurteilt worden.

**False Positives:**

- `Rechnungen der Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_54`)


Alle Erhebungen der Betriebsprüfung hätten ergeben, dass die Firma Spies&Wickert Solar GmbH nur dazu diene,  Scheinrechnungen zu ermöglichen.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_58`)


Ergänzend legte das Finanzamt Teile des Betriebsprüfungsberichtes betreffend die Firma Spies&Wickert Solar GmbH in Ablichtung vor.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_60`)


Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma Spies&Wickert Solar GmbH führte der Bf. aus, dass am 29.11.2012 der Konkurs über das  Vermögen dieser Firma eröffnet und mangels Masse abgelehnt worden sei.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_62`)


es sei lediglich der Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma Ch angezweifelt worden.

**False Positives:**

- `Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

**False Positives:**

- `Fremdleistungen der Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH€`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_6`)


Beigelegt ist ein Antrag auf Übertragung eines Geldbetrages innerhalb der Finanzverwaltung  der Gerstbreu Umwelt GmbH vom 15. Juli 2019, mit dem ein Betrag von € 490.885,84 auf das Abgabenkonto  der Bf. übertragen werden sollte.

**False Positives:**

- `Finanzverwaltung  der Gerstbreu Umwelt GmbH` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_9`)


Im gegenständlichen Fall sei zwar am 15. Juli 2019 bei der Firma Gerstbreu Umwelt GmbH ein  Umbuchungsantrag eingebracht worden.

**False Positives:**

- `Firma Gerstbreu Umwelt GmbH` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_12`)


Im Vorlageantrag vom 27. September 2019 wurde die Beschwerde wie folgt ergänzt:  „Laut unserer Mandantschaft wurde betreffend die Firma Gerstbreu Umwelt GmbH  St.Nr. 09 die  Umsatzsteuervoranmeldung für 05/2019 am 12. Juli 2019 via Finanz Online hochgeladen.

**False Positives:**

- `Firma Gerstbreu Umwelt GmbH ` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_71`)


Im vorliegenden Fall wurde im Vorlageantrag ausgeführt, dass die Firma Gerstbreu Umwelt GmbH  St.Nr. 09 die  Umsatzsteuervoranmeldung für 05/2019 am 12. Juli 2019 via Finanz Online hochgeladen hätte  und sich aufgrund dieser Umsatzsteuervoranmeldung ein Guthaben in Höhe von EUR  827.110,75 ergeben hätte sollen.

**False Positives:**

- `Firma Gerstbreu Umwelt GmbH ` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_72`)


Unsere Mandantschaft (Anmerkung: gemeint sein soll hier  wohl die Gerstbreu Umwelt GmbH  eine andere Mandantschaft ist wohl auch die Bf.) hat diesbezüglich auch  eine Produktionsübermittlung erhalten, die beigelegt wurde.

**False Positives:**

- `Gerstbreu Umwelt GmbH ` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

**False Positives:**

- `Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_74`)


Unter Berücksichtigung der angeführten (höchst-)gerichtlichen Judikatur und in Würdigung der  Gesamtumstände des Einzelfalles ist davon auszugehen, dass die Bf. (ihr steuerlicher Vertreter)  in Kenntnis der Produktionsübermittlung der entsprechenden UVA der Firma Gerstbreu Umwelt GmbH davon  ausgegangen ist, dass zum Fälligkeitszeitpunkt 15. Juli 2019 ein entsprechender  Überrechnungsantrag gestellt wurde, der die Entrichtung der betreffenden Abgaben bewirken  würde.

**False Positives:**

- `Firma Gerstbreu Umwelt GmbH` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_21`)


Die Methode bzw. Vorgangsweise wurde wie folgt beschrieben:  Ad 1) die Erstellung von Unterlagen durch die Ferro Montagetechnik GmbH (i.d.F. FMT) nach  eigenen Vorgaben und Erkenntnissen der von der Güssing Energie Technologies (i.d.F. GET)  erzeugten Pilotanlage und den damit erzielten Ergebnissen;

**False Positives:**

- `Erstellung von Unterlagen durch die Ferro Montagetechnik GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_105`)


Allein die Beschreibung der Kaufartikel in Form von Abkürzungen war nicht ausreichend, die  Anschaffung von Büromaterial und damit einen Zusammenhang zwischen den Kosten bei der  Firma Saturn Vertriebs GmbH und den Einkünften aus nichtselbständiger Arbeit nachzuweisen.

**False Positives:**

- `Firma Saturn Vertriebs GmbH` — partial — gold is substring of pred: `Saturn Vertriebs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Saturn Vertriebs GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_60`)


In Bezug auf den Handel mit Gebrauchtwägen seien die Erlöse seitens der Außenprüfung  anhand des Auskunftsersuchen an die Firma XGmbH ermittelt worden, wobei aufgrund der  Ermittlungsergebnisse Grund zu der Annahme bestehe, dass der Bf auch bei anderen Händlern  Fahrzeuge gekauft habe.

**False Positives:**

- `Firma XGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_14`)


In der dagegen erhobenen Beschwerde wird Folgendes vorgebracht:  „Im Jahr 2011 informierte die Y Austria GmbH alle für das Unternehmen tätige selbständige  Kundenvermittler darüber, dass die Abrechnung der erwirtschafteten Provisionen über die  Schweizer Zentrale abgewickelt werden.

**False Positives:**

- `Y Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_18`)


Derzeit ist eine Betriebsprüfung bei der Y Austria GmbH anhängig.

**False Positives:**

- `Y Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_42`)


Die vorliegende Beschwerde bringt nur ganz allgemein gehalten vor, die Y Austria GmbH habe  im Jahr 2011 alle für das Unternehmen tätigen Kundenvermittler darüber informiert, dass die  Abrechnung der Provisionen über die Schweizer Zentrale abgewickelt würde.

**False Positives:**

- `Y Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_18`)


Über die Beschwerde wurde erwogen:  Das Bundesfinanzgericht geht von folgendem festgestellten entscheidungswesentlichen  Sachverhalt aus:  Der Bf. bezog im Jahr 2013 neben anderen nicht strittigen Bezügen, solche aus  nichtselbständiger Arbeit seitens der KGMBH und seitens der IEF Service GmbH.  Sowohl im Erstbescheid als auch in der Beschwerdevorentscheidung wurden Bruttobezüge in  Höhe von € 4.735,91 und Nettobezüge in Höhe von € 3.132,68 seitens der IEF GmbH  berücksichtigt.

**False Positives:**

- `IEF GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `IEF Service GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_27`)


Dem Begehren des Bf. in der Beschwerde wurde durch Reduzierung der Einkünfte aus der  KGMBH um den von der IEF Service GmbH erhaltenen Betrag mit der Berechnung in der  Beschwerdevorentscheidung vom 31.8.2018 bereits Rechnung getragen.

**False Positives:**

- `KGMBH um den von der IEF Service GmbH` — partial — gold is substring of pred: `IEF Service GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IEF Service GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_13`)


Das Vermögen der ersteBeteiligungsKG, FN FBnummerErsteBeteilKG (´AbkErsteBeteilKG´)  wurde laut Firmenbucheintragung vom Februar2007 gemäß § 142 UGB von ihrer bisherigen  Kommanditistin, der KommanditistGmbH übernommen.

**False Positives:**

- `KommanditistGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_34`)


Die  Berufung kann aber zwei berufungswerbenden Gesellschaften zugerechnet werden, nämlich  der KommanditistGmbH und der dritteBeteiligungsKG.

**False Positives:**

- `KommanditistGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_10`)


Laut Einsichtnahme des Finanzamtes in deren Sozialversicherungs(SV)-Daten (Stand Ende  Juni 2020) war die Bf bei der Beischmidt KI GmbH als "Angestelltenlehrling" vom 3.9.2019 bis 1.12.2019  zur Sozialversicherung angemeldet.

**False Positives:**

- `Bf bei der Beischmidt KI GmbH` — partial — gold is substring of pred: `Beischmidt KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Beischmidt KI GmbH`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_4`)


Der Beschwerdeführer (Bf.) war im Streitzeitraum 2012 und 2013 Prokurist der Firma GmbH  und bezog in dieser Funktion Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Firma GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_12`)


Dem Finanzamt wurde durch polizeiliche und eigene Ermittlungen bekannt, dass der Bf. in den  Jahren 2012 bis 2014 Eingangsrechnungen der Firma Software gefälscht hat, die  Rechnungslegung an die Firma GmbH fingiert hat und die Überweisung von  Rechnungsbeträgen an seine eigenen Sparbücher genehmigt hat und die Durchführung der  Überweisungen durch eine unwissende Angestellte veranlasst hat.

**False Positives:**

- `Rechnungslegung an die Firma GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_15`)


Ab April 2014 wurden vom Bf. auf sein Konto zu Lasten der Firma GmbH € 6.640,- verbucht.

**False Positives:**

- `Firma GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_32`)


Die zuständige Referentin des Finanzamtes sei bei der Hauptverhandlung betreffend den Bf.  am 8.9.2015 vor dem Landesgericht anwesend gewesen und daher in Kenntnis davon, dass der  Bf. bereits vor der Hauptverhandlung vom 8.9.2015 an die Firma GmbH eine Zahlung von €  40.000,- an Schadenswiedergutmachung gezahlt habe, dies sei im Verfahren nicht  berücksichtigt worden.

**False Positives:**

- `Firma GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Landesgericht`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_34`)


Am 29.9.2019 sei vom Bf. außerdem eine Vereinbarung betreffend Ratenzahlung an die Firma  GmbH zur Schadensgutmachung vorgelegt worden und dem Bf. mitgeteilt worden, dass der  Sachverhalt einer neuerlichen Prüfung durch die Fachabteilung unterzogen werde.

**False Positives:**

- `Firma  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_56`)


Ab April 2014 wurden vom Bf. auf sein Konto zu Lasten der Firma GmbH € 6.640,- verbucht.

**False Positives:**

- `Firma GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_43`)


An Sachverhalt zu beurteilen sind die im Kauf- und Wohnungseigentumsvertrag vom  21.10.1998 und im Änderungsvertrag zu diesem Wohnungseigentumsvertrag vom  8.5./23.5.2018 zwischen der Bf und der Zeitlhoefler Landwirtschaft GmbH getroffenen, obangeführten Vereinbarungen.

**False Positives:**

- `Bf und der Zeitlhoefler Landwirtschaft GmbH` — partial — gold is substring of pred: `Zeitlhoefler Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zeitlhoefler Landwirtschaft GmbH`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_27`)


(…)  T2. 2 Körperschaftsteuer  Gewinnhinzurechnungen  Am 28.11.2011 wurde dem ehemaligen GF der Beschwerdeführer GmbH, Hr. Patrick Kirschbauer  per e- mail und per RsB Brief, welcher am 30.11.2011 übernommen wurde, ein Vorhalt bezüglich  offener Fragen, die im Prüfungsverfahren auftauchten, übermittelt. Am 30.11.2011 erfolgte ein  Anruf einer Fr. T. von der T-Datenverarbeitungs GmbH in Wien, wobei ersucht wurde, die  gesetzte Frist (9.12.2011), zur Beantwortung der im Vorhalt gestellten Fragen bzw. Beibringung  der angeforderten Unterlagen bis zum 20.12.2011 zu verlängern.

**False Positives:**

- `T-Datenverarbeitungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Patrick Kirschbauer`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_29`)


Nachdem sich bis zum 7.2.2012 niemand mehr meldete, erfolgte eine telefonische Urgenz bei  der Datenverarbeitungs GmbH (Fr. T.) mit dem Ersuchen die Unterlagen umgehend ha. zu  2 von 32 Seite 3 von 32

**False Positives:**

- `Datenverarbeitungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_72`)


Während die nach der AP an den Masseverwalter der L- GmbH i.L. ergangenen Bescheide  unbekämpft in Rechtskraft erwuchsen, brachte die T-Datenverarbeitungs GmbH gegen die  KeSt-Bescheide 2007-2009 namens des Bf fristgerecht Berufung ein, die in einem  nachgereichten Schriftsatz wir folgt begründet wurde:  „Wir als Vertretung (Vollmacht liegt auf) und im Auftrag und Rücksprache mit Herrn  Patrick Kirschbauer, legen wir folgenden Sachverhalt dar:  Tz. 4 Kapitalertragssteuer verdeckte Gewinnausschüttung  Jahr 2007  1.)

**False Positives:**

- `AP an den Masseverwalter der L- GmbH` — no gold match — likely missing annotation
- `T-Datenverarbeitungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Patrick Kirschbauer`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_78`)


Denn diese hat es wiederum verabsäumt die Zahlungen auf  die GmbH um zu Buchen.

**False Positives:**

- `Zahlungen auf  die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_86`)


Sowohl von  den Lieferanten die nicht sofort den Firmenwortlaut ändern, ergibt sich schon durch ein Bespiel  der Fa. A.-Fenster, den die wussten schon auf Grund der Ausgangs-Rechnungen das es nicht  KEG sondern GmbH heißen soll.

**False Positives:**

- `Ausgangs-Rechnungen das es nicht  KEG sondern GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_106`)


Die Vorlageunterlagen beschränkten sich auf die angefochtenen Bescheide, den AP Bericht der Synkel-Versicherung GmbH  die Berufung samt gesonderter Begründung (ohne darin erwähnte Beilagen), eine  Anfrage des Firmenbuchgerichts vom April 2012 wegen beabsichtigter Löschung der Synkel-Versicherung GmbHi.L. sowie den oa. Ablehnungsbescheid gem. § 84 BAO.

**False Positives:**

- `Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbHi.L.`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_151`)


II. Der Bf war von März 2007 bis Okt 2009 geschäftsführender Alleingesellschafter der Synkel-Versicherung GmbH  FN 999999z mit Sitz in Wien, zu deren Geschäftsgegenstand u.a. die Montage von Fenstern  und Türen und der Innenausbau gehörte.

**False Positives:**

- `Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_153`)


In der Folge wurde der Sitz der Synkel-Versicherung GmbH in das Umland von X-Stadt verlegt (AP-Akt OZ 27a).

**False Positives:**

- `Folge wurde der Sitz der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_156`)


2010 das Konkursverfahren über das Vermögen der Synkel-Versicherung GmbH  Nach  Konkursaufhebung mangels kostendeckenden Vermögens und zwei geringfügigen  Nachtragsverteilungen erfolgte am 18.Juli 2012 die amtswegige Löschung der Synkel-Versicherung GmbH im  Firmenbuch (Quelle: FB FN 999999z, abgabenbehördl.

**False Positives:**

- `Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_160`)


Obwohl nicht formelle Rechtsvorgängerin der Synkel-Versicherung GmbH  wird die L-KEG im  GmbH-Abtretungsvertrag vom 29.Okt.

**False Positives:**

- `Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_162`)


Der Abgabenbehörde gegenüber waren sowohl die L-KEG als auch die Synkel-Versicherung GmbH steuerlich  unvertreten, doch hatten beide Gesellschaften und auch deren Gesellschafter einem  gemeinsamen Buchhaltungsbetrieb Zustellvollmacht zum Empfang abgabenbehördlicher  Schriftstücke erteilt. Im verfahrensgegenständlichen AP- und Rechtsmittelverfahren schritt für  den Bf - bis zur bescheidmäßigen Untersagung gem. § 84 (1) BAO im Mai 2012 - eine neue  Bilanzbuchhaltungsgesellschaft (im Folgenden Schottmueller + Werntges Planung GmbH  ein.

**False Positives:**

- `L-KEG als auch die Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Schottmueller + Werntges Planung GmbH`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_178`)


Die externe AP-Ermittlungstätigkeit zu den verfahrensgegenständlichen Streitpunkten  beschränkte sich nach den vorgelegten Unterlagen - neben Firmenbuchabfragen - im  Wesentlichen auf die Anforderung der Kundenkonten der L-KEG und der Synkel-Versicherung GmbH bei der Fa A.- Fenster (AP-Bericht Tz.4/1.) und den Sachverhalt zu AP-Bericht Tz.4/2.

**False Positives:**

- `Anforderung der Kundenkonten der L-KEG und der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_183`)


Im nachgereichten AP-Akt befinden sich wenige Fragmente aus der Buchhaltung des geprüften  Unternehmens (einzelne Buchhaltungskonten der Synkel-Versicherung GmbH  nur vereinzelt zugehörige Belege).

**False Positives:**

- `Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_191`)


Da dieser Differenzbetrag zugeflossen sein muss, stellt dieser eine vGA dar.“  b) BFG-Sachverhaltsfeststellung:  Geschäftsgegenstand sowohl der L-KEG als auch der Synkel-Versicherung GmbH war die Montage von Fenstern  und Türen.

**False Positives:**

- `L-KEG als auch der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_205`)


auf das Kundenkonto der Synkel-Versicherung GmbH wurde das ausgeglichene Kundenkonto der L-KEG in der  Buchhaltung der Fa A.-Fenster am 27.Sept.2007 geschlossen.

**False Positives:**

- `Kundenkonto der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_209`)


In der Folge wurde die  Geschäftsbeziehung der Fa A.-Fenster mit der Synkel-Versicherung GmbH buchhalterisch über dieses neue  Kundenkonto abgewickelt.  Abweichend vom Rechenwerk der Fa A.-Fenster scheinen in der Buchhaltung der Synkel-Versicherung GmbH auf  dem Konto „Erlöse für Bauleistungen § 19 UStG“ bereits ab 11.Juni 2007 Ausgangsrechnungen  (AR) mit fortlaufender ReNr ab 1/2007 auf, darunter auch jene Rechnungen, welche in der  Buchhaltung der Fa A.-Fenster bis 24.Aug.2007 auf dem Kundenkonto der L-KEG verbucht sind.

**False Positives:**

- `Buchhaltung der Synkel-Versicherung GmbH` — similar text (different position): `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_212`)


Einem Berechnungsentwurf im AP-Akt zur verdeckten Ausschüttung im Zusammenhang mit  der Fa A.-Fenster ist zu entnehmen, dass der Prüfer den Erlösen der L-KEG für 2007 auch jene  aus den bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem 3.Quartal 2007  zurechnete und den Gesamtbetrag als bezahlt behandelte (AP-Akt OZ 10).

**False Positives:**

- `L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_214`)


Da der Gesamtbetrag der dort verbuchten AR - neben  diversen AR an den zweiten Hauptauftraggeber der Synkel-Versicherung GmbH– u.a. jene in der A.- Fenster-Buchhaltung bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem  3.Quartal 2007 enthielt, wurden in diesem Berechnungsentwurf im Ergebnis die von der Fa A.- Fenster buchhalterisch der L-KEG zugeordneten Rechnungen der Synkel-Versicherung GmbH aus dem Zeitraum  Juni – August 2007 bei beiden Gesellschaften zum Ansatz gebracht.

**False Positives:**

- `L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`
- `L-KEG zugeordneten Rechnungen der Synkel-Versicherung GmbH` — similar text (different position): `Synkel-Versicherung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH–`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_215`)


Während im Rechenwerk der Fa A.-Fenster die zugehörigen Zahlungen bei der L-KEG zum  Ausgleich des Kundenkontos führten, blieb in der Buchhaltung der Synkel-Versicherung GmbH per 31.12.2007 ein  Betrag von rd. 63.000,- € als offene Forderung gegen die Fa A.-Fenster offen.

**False Positives:**

- `Buchhaltung der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

</details>

---

## `GmbH & Co KG/OG` 💣

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `60eed51e`  
**Description:**
Matches GmbH/AG/KG entities with & Co KG/OG suffixes, strictly requiring a word boundary before the name and excluding common non-entity prefixes like 'der', 'die', 'das', 'an', 'von'.

**Content:**
```
\b((?:[A-Z][A-Za-z0-9\s&\-]+(?:Steuerberatungs-?|Wirtschaftsprüfungs-?|Steuerberatungsgesellschaft|Wirtschaftstreuhandgesellschaft)?\s*(?:GmbH|AG|KG))\s*&\s*Co\s*(?:KG|OG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 27 | 9 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 18 | 16853 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Astoria Steuerberatung GmbH & Co KG` | `Astoria Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `HR Frederik Kleinmichel, MA` (person)
- `Haniflgasse 12, 4725 Stadl, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Scarlett Beverungen, Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 71-240/3156  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Uniconsult Steuerberatungs GmbH & Co KG` | `Uniconsult Steuerberatungs GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Scarlett Beverungen` (person)
- `Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `71-240/3156` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/141326.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141326.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Karim Ickstadt  in der Beschwerdesache   Axel Jastrzemsky, als Gruppenträgerin, V GmbH, als Gruppenmitglied und der Klemeyer + Heisterhagen Pharma GmbH  als von der  Teilnahme an der Unternehmensgruppe ausgeschlossene Körperschaft, jeweils vertreten durch  Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG, Linzer Bundesstraße 101, 5023  Salzburg-Gnigl, über die Beschwerde der Axel Jastrzemsky, Sandweg 7, 4782 Aigerding, Österreich, vom 28. März 2019 gegen  den Gruppenfeststellungsbescheid 2018 des Finanzamtes Wien 12/13/14 Purkersdorf -  nunmehr Finanzamtes Österreich - vom 27. Februar 2019, Steuernummer 74-905/9339,  nach Durchführung einer mündlichen Verhandlung am 22. August 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG` | `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Karim Ickstadt` (person)
- `Axel Jastrzemsky` (person)
- `Klemeyer + Heisterhagen Pharma GmbH` (organisation)
- `Axel Jastrzemsky` (person)
- `Sandweg 7, 4782 Aigerding, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `74-905/9339` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/142810.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142810.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marceline Weizenkorn  in der Beschwerdesache Georg Strüve,  Laubweg 96, 4300 St. Valentin, Österreich, vertreten durch Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG,  Hadeldorfstraße 30, 6830 Rankweil, über die Beschwerde vom 2. November 2022 gegen den  Bescheid des Finanzamt Purkersdorf  vom 28. September 2022 betreffend Feststellung von Einkünften  gemäß § 188 BAO für 2018, Steuernummer 36-621/8395, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO in Verbindung mit § 260 Abs. 1 lit. a BAO  als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG` | `Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Marceline Weizenkorn` (person)
- `Georg Strüve` (person)
- `Laubweg 96, 4300 St. Valentin, Österreich` (address)
- `Finanzamt Purkersdorf` (organisation)
- `36-621/8395` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/143366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Melina Wibelitz, Holzsteig 6, 2002 Nursch, Österreich, vertreten durch BKS Steuerberatung GmbH & Co KG, Untere Hauptstr 10, 3150  Wilhelmsburg an der Traisen, über die Beschwerde vom 28. Juli 2019 gegen die Bescheide des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 15. Juli 2019 betreffend Grunderwerbsteuer, Steuernummer 93-238/5183,  Erfassungsnummer 10-2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `BKS Steuerberatung GmbH & Co KG` | `BKS Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Wibelitz` (person)
- `Holzsteig 6, 2002 Nursch, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `93-238/5183` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/147633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147633.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Techn R Karola Grosse-Allermann, Bauernbergstraße 25, 4921 Langstadl, Österreich, vertreten durch FP FerTax Steuerberatungs GmbH  & Co KG, Graf-Starhemberg-Gasse 6 Tür 2, 1040 Wien, über die Beschwerde vom 14. Jänner  2023 gegen den Bescheid des Finanzamtes Österreich vom 15. Dezember 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer 93-739/6588, nach  Durchführung einer mündlichen Verhandlung am 2. April 2025 im Beisein der Schriftführerin  Andrea Newrkla zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO - im eingeschränkten Umfang - Folge gegeben.

| Predicted | Gold |
|---|---|
| `FP FerTax Steuerberatungs GmbH  & Co KG` | `FP FerTax Steuerberatungs GmbH  & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Julia Carola Cermak-Kapl MA` (person)
- `Techn R Karola Grosse-Allermann` (person)
- `Bauernbergstraße 25, 4921 Langstadl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-739/6588` (tax_number)
- `Andrea Newrkla` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Verena Khalidi  in der Beschwerdesache MedR Fiona Davydova,  St.-Anna-Park 16i, 5274 Unterhartberg, Österreich, vertreten durch Liepert Greussing Sturm Steuerberatung GmbH & Co KG,  Mühlgasse 21, 6700 Bludenz, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid  des FA Baden Mödling  vom 10. Jänner 2018 betreffend Haftungs- und Abgabenbescheid 2016  Steuernummer 96-418/3627  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Liepert Greussing Sturm Steuerberatung GmbH & Co KG` | `Liepert Greussing Sturm Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Verena Khalidi` (person)
- `MedR Fiona Davydova` (person)
- `St.-Anna-Park 16i, 5274 Unterhartberg, Österreich` (address)
- `FA Baden Mödling` (organisation)
- `96-418/3627` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/149445.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149445.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Beschwerdesache Anatol Schlimp, KLG Wasserwiese Gruppe 3, 8954 Mitterberg, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Handelsstraße 8/Stiege 2/Top 2, 3130 Herzogenburg, betreffend Beschwerde vom  24. Oktober 2023 gegen den Bescheid des Finanzamtes Österreich vom 28. September 2023  betreffend Einkommensteuer 2021 Steuernummer 26-775/1483  beschlossen:   Die Beschwerde vom 24. Oktober 2023 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `BKS Steuerberatung GmbH & Co  KG` | `BKS Steuerberatung GmbH & Co  KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gertraud Hausherr` (person)
- `Anatol Schlimp` (person)
- `KLG Wasserwiese Gruppe 3, 8954 Mitterberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `26-775/1483` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_107`)


Beim  anderen Produkt handelt es sich um eine Kupplung des Herstellers und Distributors von  Zubehör in den Produktbereichen Foto, Video, Audio, Computer und Telekommunikation,  nämlich der Firma Hama GmbH & Co KG, die zum Anschluss eines analogen Telefons an eine  TST-Anschlussdose geeignet ist.

**False Positives:**

- `Firma Hama GmbH & Co KG` — partial — gold is substring of pred: `Hama GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hama GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_42`)


In der Firma G... Bau GmbH & Co KG arbeite ich erst ab 20.02.2017.

**False Positives:**

- `Bau GmbH & Co KG` — partial — pred is substring of gold: `G... Bau GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... Bau GmbH & Co KG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_74`)


Inwiefern dieser Punkt eine Unzumutbarkeit begründen soll ist nicht ersichtlich, kann aber  dahingestellt bleiben, da im Hinblick auf die Unzumutbarkeit die Jahresbetrachtung gilt. Im  gegenständlichen Jahr 2018, war der Bf. ganzjährig bei der G... BAU GmbH & Co KG beschäftigt.

**False Positives:**

- `BAU GmbH & Co KG` — partial — pred is substring of gold: `G... BAU GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... BAU GmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_89`)


Seit 29. August 2016 ist der Bf. bei der Fa. G. Bau GmbH & Co KG nichtselbständig beschäftigt  (Abgabeninformationssystemabfrage).

**False Positives:**

- `Bau GmbH & Co KG` — partial — pred is substring of gold: `G. Bau GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G. Bau GmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_91`)


er arbeitet bei der Firma G. Bau  GmbH & Co KG erst ab 20. Februar 2017.

**False Positives:**

- `Bau  GmbH & Co KG` — partial — pred is substring of gold: `Firma G. Bau  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Firma G. Bau  GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_189`)


Gesellschafter-Geschäftsführers ist hiebei nicht maßgebend (zB VwGH 13.12.1977,1550/77,  betreffend die Geschäftsführung durch eine Komplementär-GmbH einer GmbH &Co KG).

**False Positives:**

- `GmbH einer GmbH &Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/135360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der KommR Dipl. Kff. Elvira Siegburg, Am Bürgerkogel 8, 3571 Stallegg, Österreich, vertreten durch die FreiTAX Wirtschaftsprüfungs- und  SteuerberatungsGmbH & Co KG, Rennweg 30, 6020 Innsbruck, über die Beschwerde vom  15. September 2021 gegen den Bescheid des Finanzamtes Österreich vom 26. August 2021  betreffend Abweisung des Antrages auf Berichtigung des Einkommensteuerbescheides 2018  gemäß § 293b BAO, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `SteuerberatungsGmbH & Co KG` — partial — pred is substring of gold: `FreiTAX Wirtschaftsprüfungs- und  SteuerberatungsGmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `KommR Dipl. Kff. Elvira Siegburg`(person)
- `Am Bürgerkogel 8, 3571 Stallegg, Österreich`(address)
- `FreiTAX Wirtschaftsprüfungs- und  SteuerberatungsGmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/142273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142273.1_68`)


Die Beschwerdeführerin ist eine Personengesellschaft in Form einer GmbH &Co KG.

**False Positives:**

- `Personengesellschaft in Form einer GmbH &Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_28`)


An die GmbH & Co KG erging am 15.1.2019 zur GZ RV/4100213/2012 eine Erledigung des BFG,  deren Spruch zufolge eine Beschwerde der GmbH & Co KG gegen die einheitliche und  gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2004 bis 2005 mangels  Bescheidqualität der angefochtenen Bescheide als unzulässig zurückgewiesen wurde.

**False Positives:**

- `An die GmbH & Co KG` — no gold match — likely missing annotation
- `Spruch zufolge eine Beschwerde der GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_30`)


Am 10.11.2021 erging an die GmbH & Co KG neuerlich eine Erledigung des BFG zur GZ  RV/4100213/2012, mit der die Beschwerde der GmbH & Co KG gegen die einheitliche und  gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2004 bis 2005 mangels  Bescheidqualität als unzulässig zurückgewiesen wurde.

**False Positives:**

- `Beschwerde der GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_86`)


Das BFG wollte mit seiner Erledigung vom 15.1.2019 die Beschwerde der GmbH & Co KG  betreffend die Feststellung von Einkünften gemäß § 188 BAO als unzulässig zurückweisen und  damit mit Rechtskraftwirkung für alle am Feststellungsverfahren Beteiligten aussprechen, dass  die vor ihm bekämpften Feststellungsbescheide nicht wirksam geworden waren.

**False Positives:**

- `Beschwerde der GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_87`)


Dennoch hat  das Bundesfinanzgericht seine im Rahmen von Feststellungsverfahren ergangene Erledigung  nur an die GmbH & Co KG und nicht an alle Gesellschafter adressiert und zugestellt. Mangels  eines Hinweises in der betreffenden Erledigung ist die Zustellwirkung im Sinne des § 101 Abs 3  zweiter Satz BAO gegenüber den Gesellschaftern, denen Einkünfte zugerechnet werden sollen,  nicht eingetreten.

**False Positives:**

- `Dennoch hat  das Bundesfinanzgericht seine im Rahmen von Feststellungsverfahren ergangene Erledigung  nur an die GmbH & Co KG` — partial — gold is substring of pred: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Barbara Straka, die Richterin  Mag. Irene Kohler sowie die fachkundigen Laienrichter Dip.Ing. Gerald Patschka und Mag.  Michael Heumesser in der Beschwerdesache Oleg Eckschmidt, Hausgrabengasse 1780, 4720 Straßhof, Österreich, vertreten durch  Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38,  1020 Wien, über die Beschwerde vom 22. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2023 betreffend Einkommensteuer 2013, Steuernummer  60-131/3835, in der Sitzung am 17. Jänner 2024, erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberatung GmbH & Co KG` — partial — pred is substring of gold: `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Barbara Straka`(person)
- `Mag. Irene Kohler`(person)
- `Dip.Ing. Gerald Patschka`(person)
- `Mag.  Michael Heumesser`(person)
- `Oleg Eckschmidt`(person)
- `Hausgrabengasse 1780, 4720 Straßhof, Österreich`(address)
- `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `60-131/3835`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/144821.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144821.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Julia Griesfelder, Dr.Karl Rennerstraße 27, 9121 Lasseinerbucht, Österreich, vertreten durch Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft, Hietzinger Kai 67-69, 1130 Wien, betreffend Beschwerde vom  9. Juni 2023 gegen die Bescheide des Finanzamtes Österreich vom 6. März 2023 betreffend  Umsatz- und Körperschaftsteuer 2019 Steuernummer 41-950/9771  beschlossen:   Der Vorlageantrag vom 28. Mai 2024 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

**False Positives:**

- `Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG` — partial — pred is substring of gold: `Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Julia Griesfelder`(person)
- `Dr.Karl Rennerstraße 27, 9121 Lasseinerbucht, Österreich`(address)
- `Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-950/9771`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Urs Ahrenholz, Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich, vertreten durch HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG, Schloßgraben 10, 6800 Feldkirch,  über die Beschwerde vom 2. Oktober 2019 gegen den Bescheid des Finanzamtes Feldkirch vom  9. September 2019 betreffend Einkommensteuer 2017, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatungs GmbH & Co KG` — partial — pred is substring of gold: `HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Urs Ahrenholz`(person)
- `Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich`(address)
- `HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Feldkirch`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/148936.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148936.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mirko Boeshenz  in der Beschwerdesache KommR Manuel Ruppoldt,  Hauptschulweg 5, 8563 Oberwald, Österreich, vertreten durch Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG, Karl-Emminger-Straße 23, 5020 Salzburg, über die Beschwerde vom 27. Juni 2022  gegen den Bescheid des Finanzamtes Österreich vom 19. Mai 2022 betreffend  Einkommensteuer 2020 Steuernummer 90-698/6357  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG` — partial — pred is substring of gold: `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mirko Boeshenz`(person)
- `KommR Manuel Ruppoldt`(person)
- `Hauptschulweg 5, 8563 Oberwald, Österreich`(address)
- `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `90-698/6357`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_364`)


An der Näffgen und Duchoslav Cloud GmbH & Co KG waren beteiligt:  Als Kommanditisten:  170.000 ATS…….erster Stratege (34%)  165.000 ATS…….zweiter Stratege (33%)  23 von 75 Seite 24 von 75

**False Positives:**

- `Duchoslav Cloud GmbH & Co KG` — partial — pred is substring of gold: `Näffgen und Duchoslav Cloud GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Näffgen und Duchoslav Cloud GmbH & Co KG`(organisation)

</details>

---

## `GmbH at sentence start or after punctuation` 💣

**F1:** 0.000 | **Precision:** 0.026 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2ddc65ad`  
**Description:**
Matches GmbH entities at the start of a string or after punctuation, ensuring the match starts immediately with the company name (capital letter) and excludes preceding text like 'Die Revision der'.

**Content:**
```
(?:^|(?<=[;:,]))\s*([A-Z][A-Za-z0-9\s&\-]+(?:GmbH|m\.b\.H\.)\s*(?:Steuerberatungsgesellschaft|Wirtschaftspr\u00fcfungsgesellschaft|Steuerberatungs- und Wirtschaftspr\u00fcfungsgesellschaft)?)(?=\s|$|[,;])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.026 | 0.000 | 0.000 | 154 | 4 | 150 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 150 | 17761 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_17`)


Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R- Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Herrn M.:   „Herrn   Ronald Jundt   B-Straße 4/7  9999 Wien  Betreff:Furtnex-Versand GmbH in Liqu.    Wien, 05.11.2019   9996 S-Straße 3/9   2 von 9 Seite 3 von 9

| Predicted | Gold |
|---|---|
| `Furtnex-Versand GmbH` | `Furtnex-Versand GmbH` |

**Missed by this rule (FN):**

- `M.` (person)
- `Ronald Jundt` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_113`)


„Herrn   Wilhelm Fißenewert, LLM   B-Straße  9999  Betreff:Hemken Automotive GmbH in Liqu.    Wien, 05.11.2019   9996 S.-Straße   St.Nr. 99-999/9999-BV 24   BESCHEID –  Leistungsgebot

| Predicted | Gold |
|---|---|
| `Hemken Automotive GmbH` | `Hemken Automotive GmbH` |

**Missed by this rule (FN):**

- `Wilhelm Fißenewert, LLM` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_72`)


Der GmbH wurden vom FA im Zuge von Prüfungshandlungen bis Dezember 2010  Umsatzsteuern in Gesamthöhe von ca. € 1,9 Mio aufgrund von Umsatzsteuerhinterziehungen  im Zusammenhang mit Heizölverkäufen vorgeschrieben.

**False Positives:**

- `Der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_89`)


Eine Akteneinsicht in die Akten der GmbH durch den Vertreter des BF wurde frühestens im  Dezember 2016 durchgeführt.

**False Positives:**

- `Eine Akteneinsicht in die Akten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_125`)


Weitere Abgabenschulden der GmbH  sind nicht Gegenstand dieses Verfahrens.

**False Positives:**

- `Weitere Abgabenschulden der GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_10`)


Am Konto der GmbH haften folgende Abgabenbeträge aus:  Umsatzsteuer 10/2017 15.12.2017 180,76  Umsatzsteuer 11/2017 15.01.2018 4.834,72  Lohnsteuer 11/2017 15.12.2017 1.398,21  Lohnsteuer 12/2017 15.01.2018 631,81  Lohnsteuer 01/2018 15.2.2018 308,73  Dienstgeberbeitrag (DB) 11/2017 15.12.2017 735,38  Dienstgeberbeitrag 12/2017 15.01.2018 300,47  Dienstgeberbeitrag 01/2018 15.02.2018 168,99  Zuschlag zum DB (DZ) 11/2017 15.12.2017 69,95  Zuschlag zum DB (DZ) 12/2017 15.01.2018 28,58  Zuschlag zum DB (DZ) 01/2018 15.02.2018 16,90  Körperschaftsteuer 01-03/2018 15.02.2018 125,00     8.799,53

**False Positives:**

- `Am Konto der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_45`)


Eine  abgabenrechtliche Pflichtverletzung als Vertreterin der GmbH wird mangels Verschuldens  bestritten, da der Sohn der Bf. die tatsächliche Geschäftsführung und auch die Wahrnehmung  der steuerlichen Interessen der Primärschuldnerin übernommen habe.

**False Positives:**

- `Eine  abgabenrechtliche Pflichtverletzung als Vertreterin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_22`)


Bei der Unter Wilkel GmbH fand im Juni 2008 eine AP statt.

**False Positives:**

- `Bei der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_64`)


Die Unter Wilkel GmbH war nach Abtretung der Anteile am 15.1.2008 und  Gesellschafterwechsel Nachfolgerin der vormaligen P-GmbH. Diese war im Einzelhandel tätig  und hatte sogenannte Ein-Euro-Shops betrieben.

**False Positives:**

- `Die Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_47`)


Bei der AGmbH war der Bf. in der Zeit des Bezuges des  Weiterbildungsgeldes geringfügig und während des restlichen Jahres vollbeschäftigt.

**False Positives:**

- `Bei der AGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_96`)


Die UID Nummer der Firma Spies&Wickert Solar GmbH war laut Finanzamtsunterlagen mit 15.8.2012 begrenzt.

**False Positives:**

- `Die UID Nummer der Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_172`)


Errichtung einer bulgarischen Einmann-GmbH mit dem identischen Gesellschaftsnamen der  österreichischen Gesellschaft einschließlich des Zusatzes der österreichischen Rechtsform  „BergLuftfahrt  GmbH Eood“) ist geeignet Verwechslungen herbeizuführen.

**False Positives:**

- `Errichtung einer bulgarischen Einmann-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BergLuftfahrt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

**False Positives:**

- `Betreffend die Martinssen Versicherung GmbH` — similar text (different position): `Martinssen Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

**False Positives:**

- `Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH` — similar text (different position): `Martinssen Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH` — positional overlap with gold: `Kuranstalt Vigaun GmbH & Co. KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_81`)


Mit der nachfolgenden Übersicht werden die Rechnungen der Firma DI-Tech dargestellt:     Die rechnungsausstellende Firma DiTech GmbH war eine österreichische Fachmarktkette, die  Smartphones, Tablets, PCs, Notebooks und IT-Zubehör vertrieben hatte.

**False Positives:**

- `Die rechnungsausstellende Firma DiTech GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_90`)


Über die Beschwerde wurde erwogen:    Entscheidungsrelevanter Sachverhalt  Die Garten Taltralex GmbH wurde mit Errichtungserklärung vom 23. April 2007 gegründet und am 24. Mai  2007 unter der Firmenbuchnummer xxxxxxy im Firmenbuch eingetragen.

**False Positives:**

- `Entscheidungsrelevanter Sachverhalt  Die Garten Taltralex GmbH` — partial — gold is substring of pred: `Garten Taltralex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Garten Taltralex GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_69`)


Im zu beurteilenden Fall sei der Zweck  einer Vermietungs-GmbH durch die Vermietung der Büro-und Geschäftsmöglichkeiten erreicht  worden.

**False Positives:**

- `Im zu beurteilenden Fall sei der Zweck  einer Vermietungs-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_18`)


Weiters wurden vom Autohaus XX GmbH nachweislich (siehe beil. Rechnungen)  gebrauchte Fahrzeuge erworben.

**False Positives:**

- `Weiters wurden vom Autohaus XX GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_39`)


Hinsichtlich des Gebrauchtwagenhandels seien im Rahmen eines  Auskunftsersuchens allein von der XGmbH für die Jahre 2013-2017 Rechnungen ausgefolgt  worden, aus denen der Verkauf von Gebrauchtwagen an den Abgabepflichtigen hervorgehe,  wobei aufgrund der Angaben der Auskunftspersonen davon auszugehen sei, dass auch bei  anderen Händlern Gebrauchtwägen zur Weiterveräußerung gekauft wurden.

**False Positives:**

- `Hinsichtlich des Gebrauchtwagenhandels seien im Rahmen eines  Auskunftsersuchens allein von der XGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_4`)


Diese Abgabenschuldigkeit beruht auf einer Nachforderung infolge einer bei der GmbH  durchgeführten Betriebsprüfung, bei der im Zusammenhang mit Umsatzsteuer festgestellt  worden war, dass zur Verschleierung von ausbezahlten „Schwarzlöhnen“ Rechnungen von  dubiosen Subunternehmern ohne tatsächliche Leistungserbringung als Fremdleistungsaufwand  verbucht worden seien und aus diesen Rechnungen zu Unrecht Vorsteuern geltend gemacht  worden wären.

**False Positives:**

- `Diese Abgabenschuldigkeit beruht auf einer Nachforderung infolge einer bei der GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_8`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den FA-Vorlageunterlagen, den nachgereichten Verfahrensunterlagen der Bf und dem  Ergebnis der finanzgerichtlichen Datenbankrecherchen (FA-Datenbanken, Firmenbuch, EKIS,  ZMR) ergibt sich folgender Sachverhalt als Entscheidungsgrundlage für das BFG:  Die Bf ist ein - seit 2008 in der Rechtsform einer GmbH geführtes - Transportunternehmen mit  Sitz in der Steiermark.

**False Positives:**

- `Die Bf ist ein - seit 2008 in der Rechtsform einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `BFG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_13`)


Die GmbH habe letztmalig im April 2008 Erlöse aus ihrer Handelstätigkeit erzielt. Seither seien  lediglich die Mieteinnahmen erklärt worden.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_69`)


Von der GmbH wird ein Büroraum mit einer Größe von 16 m² im Erdgeschoß betrieblich  genutzt.

**False Positives:**

- `Von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_23`)


Die  Barzahlungen an die Scheinfirma Y-Montage GmbH in Höhe von € 35.000,- erfolgten auch in  diesem Zeitraum, sodaß sich beim Verkauf der GmbH ein Kassastand von nur mehr € 8.724,-  ergab.

**False Positives:**

- `Die  Barzahlungen an die Scheinfirma Y-Montage GmbH` — partial — gold is substring of pred: `Y-Montage GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Y-Montage GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_26`)


Gesellschafter der Nexlex GmbH waren zu dieser Zeit auch  Hr. Beschwerdeführer und Hr. K.. Hr. K. war zu dieser Zeit gleichzeitig bei der  Beschwerdeführer GmbH als Bauleiter beschäftigt.

**False Positives:**

- `Gesellschafter der Nexlex GmbH` — partial — gold is substring of pred: `Nexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexlex GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_32`)


Alle steuerrelevanten Feststellungen sind im Zeitraum vor dem Verkauf der GmbH im  Jahre 2009 angesiedelt, sodaß die Haftung den ehemaligen Geschäftsführer, Hr. Patrick Kirschbauer,  trifft.

**False Positives:**

- `Alle steuerrelevanten Feststellungen sind im Zeitraum vor dem Verkauf der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Patrick Kirschbauer`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_236`)


Auch Erhebungen im Wege des Erwerbers der GmbH-Anteile oder des  Masseverwalters der Synkel-Versicherung GmbH sind nicht dokumentiert, ebensowenig der Versuch, eine Klärung  durch eine AP bei der L-KEG herbeizuführen oder zumindest die bezughabenden  Buchhaltungsunterlagen der L-KEG anzufordern.

**False Positives:**

- `Auch Erhebungen im Wege des Erwerbers der GmbH-Anteile oder des  Masseverwalters der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_240`)


Zugleich fehlt die als Rechtsmittelbeilage eingereichte Stellungnahme des ehemaligen  Buchhalters der Synkel-Versicherung GmbH  der offenbar Unzulänglichkeiten bei der Verbuchung einräumte  (verabsäumte Umbuchungen), trotz Aufforderung des BFG nach § 266 (4) BAO.

**False Positives:**

- `Zugleich fehlt die als Rechtsmittelbeilage eingereichte Stellungnahme des ehemaligen  Buchhalters der Synkel-Versicherung GmbH ` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `BFG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_260`)


Eine Reaktion der Synkel-Versicherung GmbH gegenüber der Fa A.-Fenster betreffend die offenen  Kundenforderungen ist nicht dokumentiert (keine Zahlungsaufforderungen o.ä.).

**False Positives:**

- `Eine Reaktion der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_271`)


Rechenwerk der Synkel-Versicherung GmbH zur Abdeckung der Kundenforderung gegen die Fa A.-Fenster  umzubuchen gewesen.

**False Positives:**

- `Rechenwerk der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_275`)


Ertragswirksame Auswirkungen bei der Synkel-Versicherung GmbH hätten aus den genannten Maßnahmen nicht  resultiert.

**False Positives:**

- `Ertragswirksame Auswirkungen bei der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_289`)


Die zu AP-Akt OZ 29 vorgelegten Fragmente aus der Buchhaltung der Synkel-Versicherung GmbH enthalten als  einzig in Frage kommendes Aufwandskonto das Wareneinsatzkonto mit verbuchten  Wareneingängen zum Zeitraum 21.Juni – 18.Sept.

**False Positives:**

- `Die zu AP-Akt OZ 29 vorgelegten Fragmente aus der Buchhaltung der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_333`)


Eine Verifizierung an Hand der Buchhaltung der Synkel-Versicherung GmbH ist dem BFG nicht möglich, da trotz  finanzgerichtlicher Aufforderung zur Vorlage der abgabenbehördlichen  Verfahrensunterlagen, - abgesehen von den Erlöskonten für das 1.Halbjahr 2009 - keines der  betroffenen (und im AP-Verfahren offensichtlich vorhandenen) Buchhaltungskonten vorgelegt  wurde (weder Kassakonto oder Konto Sonstige Verbindlichkeiten noch die Konten  Fremdleistungen und PRAP Fremdleistungen).

**False Positives:**

- `Eine Verifizierung an Hand der Buchhaltung der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `BFG`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_354`)


Namens-Papierschild der POU Bau GmbH lediglich an dem mit Spinnweben verhangenen, nur  über den Garten zugänglichen Kellerabteil).

**False Positives:**

- `Namens-Papierschild der POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_355`)


Die POU Bau GmbH war bei der KIAB-Kontrolle einer Baustelle in Korneuburg als  Sub-Auftragnehmerin einer als nicht existent bezeichneten Baugesellschaft mit Korneuburger  Adresse aufgefallen.

**False Positives:**

- `Die POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_376`)


Der Bf blieb die ihm zu den abgerechneten Leistungen der POU Bau GmbH allein aufgetragene  Vorlage der Arbeitsaufträge an die Synkel-Versicherung GmbH samt Leistungsverzeichnissen schuldig.

**False Positives:**

- `Der Bf blieb die ihm zu den abgerechneten Leistungen der POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_394`)


Abgesehen vom Scheinfirmencharakter der POU Bau GmbH begründete das FA die  Nichtanerkennung des Fremdleistungsaufwandes betreffend die POU Bau GmbH im Jahr 2008 mit  einem lediglich allgemein gehaltenen, standardisierten Werkvertrag, dem Fehlen von  Baubeschreibungen und Leistungsverzeichnissen sowie der Barzahlung der fünf  zugrundeliegenden Rechnungen, jeweils in Verbindung mit vorangegangenen Einlagen und  Bankbehebungen trotz ausreichenden Kassastandes.

**False Positives:**

- `Abgesehen vom Scheinfirmencharakter der POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `POU Bau GmbH`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_404`)


Laufende Leistungen der Synkel-Versicherung GmbH für die Groschang Holz GmbH im Jahr 2008 werden durch die  vorgelegten Buchhaltungsfragmente (Erlöskonto Bauleistungen § 19 UStG) bestätigt.

**False Positives:**

- `Laufende Leistungen der Synkel-Versicherung GmbH` — partial — gold is substring of pred: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Groschang Holz GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_412`)


Da die POU Bau GmbH nach den verfahrensgegenständlichen Sachverhaltsfeststellungen im Jahr  2008 keine Scheinfirma war und im Rahmen der in den Rechnungen ausgewiesenen BVH  Leistungen als Subunternehmerin der Synkel-Versicherung GmbH erbrachte, ist auf Basis der dem BFG  vorliegenden Unterlagen der fehlende Betriebsausgabencharakter der beanstandeten  Rechnungen der Z-Bau-GmbH nicht feststellbar.

**False Positives:**

- `Da die POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `BFG`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_421`)


Bereits zum Streitpunkt betreffend die POU Bau GmbH wurde ausgeführt, dass der Betrag von  35.000,- € aus der Rechnung der Noruniwerk Robotik GmbH nach diesen Aufzeichnungen - wohl im (bereits vom  Rechtsnachfolger des Bf erstellten) Jahresabschluss 2009 - mit der 2008 eingebuchten  RAP Fremdleistungen in Höhe von 55.000,- € gegenverrechnet wurde.

**False Positives:**

- `Bereits zum Streitpunkt betreffend die POU Bau GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_423`)


Wie bereits bei den beanstandeten Rechnungen der POU Bau GmbH ergibt sich ein Konnex der  strittigen Rechnung der Noruniwerk Robotik GmbH zur PRAP 2008 im Betrag von 55.000,- € nur aus diesen  (unklaren) Hinweisen in den Prüferaufzeichnungen.

**False Positives:**

- `Wie bereits bei den beanstandeten Rechnungen der POU Bau GmbH ergibt sich ein Konnex der  strittigen Rechnung der Noruniwerk Robotik GmbH` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_424`)


Wie bei den Rechnungen der POU Bau GmbH  hält das BFG diesen Zusammenhang auch bei der Rechnung der Noruniwerk Robotik GmbH vom 3.Juni 2009 für  nicht hinreichend erwiesen.

**False Positives:**

- `Wie bei den Rechnungen der POU Bau GmbH ` — partial — gold is substring of pred: `POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `POU Bau GmbH`(organisation)
- `BFG`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_430`)


Der zugeordnete Kassaeingangsbeleg der Noruniwerk Robotik GmbH vom 10.Juni 2009 über den Erhalt der  Restzahlung von 5.000,- € ist als Dokument aus dem Rechenwerk der Noruniwerk Robotik GmbH zum Nachweis  für einen entsprechenden Kassaausgang bei der Synkel-Versicherung GmbH schon dem Grunde nach nicht  geeignet.

**False Positives:**

- `Der zugeordnete Kassaeingangsbeleg der Noruniwerk Robotik GmbH` — partial — gold is substring of pred: `Noruniwerk Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_434`)


Andere Nachweise zum Geldfluss betreffend die Restzahlung zur Rechnung der Noruniwerk Robotik GmbH vom  3.Juni 2009 liegen nicht vor.

**False Positives:**

- `Andere Nachweise zum Geldfluss betreffend die Restzahlung zur Rechnung der Noruniwerk Robotik GmbH` — partial — gold is substring of pred: `Noruniwerk Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_435`)


Der Rechnung der Noruniwerk Robotik GmbH vom 3.Juni 2009 ist in den AP-Unterlagen ein zweiter Kassabeleg  zugeordnet.

**False Positives:**

- `Der Rechnung der Noruniwerk Robotik GmbH` — partial — gold is substring of pred: `Noruniwerk Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_439`)


Damit fehlt diesem Kassabeleg aber jeglicher Bezug zur Noruniwerk Robotik GmbH  Umso schwerer wiegt das Fehlen der Bezug habenden Buchhaltungskonten der Synkel-Versicherung GmbH  weil dadurch zugleich die Herkunft des Beleges aus dem Rechenwerk der L GmbH  nicht erwiesen ist.

**False Positives:**

- `Damit fehlt diesem Kassabeleg aber jeglicher Bezug zur Noruniwerk Robotik GmbH  Umso schwerer wiegt das Fehlen der Bezug habenden Buchhaltungskonten der Synkel-Versicherung GmbH  weil dadurch zugleich die Herkunft des Beleges aus dem Rechenwerk der L GmbH ` — partial — gold is substring of pred: `Noruniwerk Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_450`)


Zugleich konnte auch eine im Zusammenhang mit der Verbuchung der Rechnung der Noruniwerk Robotik GmbH  vom 3.Juni 2009 eintretende Gewinnminderung bei der Synkel-Versicherung GmbH zu keiner Bereicherung beim  Bf führen, da er am Gewinn des Jahres 2009 nicht mehr teilnahm.

**False Positives:**

- `Zugleich konnte auch eine im Zusammenhang mit der Verbuchung der Rechnung der Noruniwerk Robotik GmbH ` — partial — gold is substring of pred: `Noruniwerk Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_5`)


Alleingesellschafterin und Geschäftsführerin ist Frau Wahl   1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (kurz: Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Bf ist eine GmbH deren alleinige Gesellschafterin Frau Wahl ist.

**False Positives:**

- `Die Bf ist eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wahl`(person)
- `Wahl`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/134021.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134021.1_42`)


Über die Beschwerde wurde erwogen:    Entscheidungsrelevanter Sachverhalt  Die Waigl Umwelt GmbH wurde mit Gesellschaftsvertrag vom 10. Februar 2012 gegründet und am 23.  Februar 2012 unter der Firmenbuchnummer xxxxxxy im Firmenbuch eingetragen.

**False Positives:**

- `Entscheidungsrelevanter Sachverhalt  Die Waigl Umwelt GmbH` — partial — gold is substring of pred: `Waigl Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waigl Umwelt GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_64`)


Die GmbH habe daher  insgesamt EUR.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_95`)


Das FA entgegnete dem Bf im Vorlagebericht vom 06.05.2016 wie folgt:  Zu den Beschwerdepunkten EUR 17.679,27 als Teil der Betriebseinnahmen und deren  Berücksichtigung bei der Berechnung des Betriebsausgabenpauschales:  Die Zahlung des besagten Betrages an die Sozialversicherung der gewerblichen Wirtschaft  durch die GmbH sei einkommensseitig bei den Betriebseinnahmen des Bf zu berücksichtigen.

**False Positives:**

- `Die Zahlung des besagten Betrages an die Sozialversicherung der gewerblichen Wirtschaft  durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_102`)


Der Anspruch auf den wirtschaftlichen Vorteil durch die Zahlung der  GmbH entstehe erst bei Entstehen der Schuld des Bf gegenüber der Sozialversicherung, sei  unmittelbar damit verknüpft und lasse sich vor allem auch hinsichtlich ihrer Höhe erst dann  bestimmen.

**False Positives:**

- `Der Anspruch auf den wirtschaftlichen Vorteil durch die Zahlung der  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_135`)


Die Einbeziehung des von der GmbH für die Schulden des Bf bei der Sozialversicherung  bezahlten Beträge in die Betriebseinnahmen sei in Entsprechung der Beschwerde bereits im  neuerlich ergangenen Bescheid berücksichtigt worden.

**False Positives:**

- `Die Einbeziehung des von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

**False Positives:**

- `Die von der Firma Furtnex-Versand GmbH` — partial — gold is substring of pred: `Furtnex-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnex-Versand GmbH`(organisation)
- `Ronald Jundt`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_81`)


Im Jahr 2009 erwarb der Bf von der Firma X M Gesellschaft m.b.H. das Röntgengerät R samt  diversem Zubehör um einen Gesamtkaufpreis von 180.000 Euro.

**False Positives:**

- `Im Jahr 2009 erwarb der Bf von der Firma X M Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_14`)


Gesellschafter der GmbH sind und waren  auch zum Zeitpunkt der Einbringung zu jeweils 50% der Bf und seine Gattin.

**False Positives:**

- `Gesellschafter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_45`)


Aus diesem Grund sind die in den  Liegenschaften enthaltenen stillen Reserven auf Ebene der GmbH weiterhin steuerverfangen.

**False Positives:**

- `Aus diesem Grund sind die in den  Liegenschaften enthaltenen stillen Reserven auf Ebene der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_51`)


Gesellschafter der GmbH sind und waren auch zum Zeitpunkt der Einbringung zu  jeweils 50% der Bf und seine Gattin.

**False Positives:**

- `Gesellschafter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_71`)


Die GmbH hätte weder ihr Stammkapital erhöht noch  Gesellschaftsanteile oder andere Vorteile als Gegenleistung gewährt, weshalb die Einbringung  als unentgeltlicher Vorgang zu qualifizieren wäre und somit nicht der Immobilienertragsteuer  unterläge.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_74`)


Gesellschafter der GmbH sind der Bf und seine Gattin, wobei die beiden  Gesellschafter für die Einlage keine neuen GmbH-Anteile erhielten, da sie bereits zu jeweils  50% an der GmbH beteiligt waren und die Einlage der Immobilien aus dem Privatvermögen zu  gleichen Teilen erfolgte.

**False Positives:**

- `Gesellschafter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_109`)


Dass im vorliegenden Fall die eingelegten Wohnungen bei der GmbH bilanziell mit den  historischen Anschaffungskosten erfasst wurden, ändert an dieser Beurteilung nichts.

**False Positives:**

- `Dass im vorliegenden Fall die eingelegten Wohnungen bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/134614.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134614.1_13`)


Die D GmbH war – ebenso wie die KurznameBf – als Steuerpflichtiger im Sinne der Richtlinie  2006/112/EG des Rates vom 28. November 2006 über das gemeinsame  Mehrwertsteuersystem einzustufen.

**False Positives:**

- `Die D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/134648.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134648.1_9`)


Nach dieser Zeit wurde der Pkw wieder an  die Goswin Luftfahrt GmbH übergeben, was aus den vorliegenden Unterlagen ersichtlich ist.

**False Positives:**

- `Nach dieser Zeit wurde der Pkw wieder an  die Goswin Luftfahrt GmbH` — partial — gold is substring of pred: `Goswin Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Goswin Luftfahrt GmbH`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_54`)


Bei der X GmbH habe er 50  Stunden pro Woche, typischerweise zwischen 12:00 und 22.00 Uhr gearbeitet.

**False Positives:**

- `Bei der X GmbH` — partial — gold is substring of pred: `X GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `X GmbH`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_58`)


Laut Firmenbuch ist die Bf eine GmbH, deren Gesellschafter keine natürlichen Personen sind,  weshalb eine Meldeverpflichtung gemäß § 5 WiEReG bestand.

**False Positives:**

- `Laut Firmenbuch ist die Bf eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_96`)


Laut des an die Fa AG2 GmbH adressierten Schriftsatzes der  Bezirkshauptmannschaft O vom 27.08.1997 betreffend den Bf wird ua festgehalten, dass das  Land B sich verpflichtet dem Arbeitgeber zum Ausgleich der verminderten Arbeitsproduktivität  7 von 16 Seite 8 von 16

**False Positives:**

- `Laut des an die Fa AG2 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_139`)


Zuliefer- GmbH sowie einen Bezug von steuerfreiem Arbeitslosengeld (§ 3 Abs. 1 Z 5 lit a EStG  1988) im Zeitraum 1.Juli - 15.August 2017.

**False Positives:**

- `Zuliefer- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/136293.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136293.1_48`)


Stellt eine GmbH der Gesellschafter-Geschäftsführerin als Entlohnung für ihre  Geschäftsführungstätigkeit einen von der GmbH finanzierten Pkw für private Fahrten zur  Verfügung und erbringt sie damit kein unangemessen hohes Entgelt für ihr gegenüber  erbrachte Leistungen, ist dieses Entgelt als Entlohnung für die Geschäftsführertätigkeit zu  beurteilen und aufseiten der Gesellschaft betrieblich veranlasst (zB VwGH 30.12.2020, Ra  2019/15/0126).

**False Positives:**

- `Stellt eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_312`)


Der Bf gab hierzu bekannt (Antwort 5.5.2020, ad Pkt 4):  Wohnbauprojekt Stadt1:  Stadt1 am Straße5 Errichtungs GmbH in Liqu.) : Diese GmbH, deren Anteile zu 100% vom Bf  gehalten wurden, erklärte  0 €………........Umsatz 2013  -4.162 €………Verlust 2013  0€……….........Umsatz 2014  -35.391 €……..Einkünfte 2014  5,889.853 € ….Umsatz 2015  Keine Einkünfte 2015 erklärt  246.980 €……..Umsatz 2016  Keine Einkünfte 2016 erklärt  189.000 €……..Umsatz 2017  504.864 €……..Einkommen 2017 nach Abzug der Verlustvorträge  336 €…………..Umsatz 2018  31.430 €……….Einkommen 2018  Im Jahr 2019 wurde die im Jahr 2015 begonnene Liquidation beendet.

**False Positives:**

- `Diese GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_315`)


Auf der Straße3 Straße3 Errichtungs GmbH in Liqu.: Diese GmbH, deren Anteile zu 100% vom  Bf gehalten wurden, erklärte   Keinen Umsatz 2014  19 von 40 Seite 20 von 40

**False Positives:**

- `Diese GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_323`)


Auch bei diesem Projekt betreffend die Flugzeug1 Ort5-  und OrtOrt4 Errichtungs GmbH seien aktuelle Luftbilder zur Verkaufsunterstützung eingesetzt  worden.

**False Positives:**

- `Auch bei diesem Projekt betreffend die Flugzeug1 Ort5-  und OrtOrt4 Errichtungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_351`)


Im Zeitraum 2008-2012 bekam der Bf seine Aufträge, als Immobilienprojektmanager tätig zu  werden, von einer GmbH, deren Anteile zu 100% von seinem Bruder  gehalten wurden (idR: BF  Holding GmbH, vgl.

**False Positives:**

- `BF  Holding GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_450`)


Die Anteile an dieser GmbH wurden zunächst nach  außen hin von einer langjährigen Angestellten diverser Handelsgesellschaften des Bruders des  Bf und auch des Bf gehalten.

**False Positives:**

- `Die Anteile an dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_453`)


Alle  errichteten Wohnungen konnten von dieser GmbH zum Großteil 2019 verkauft werden.

**False Positives:**

- `Alle  errichteten Wohnungen konnten von dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_566`)


Das ist richtig  (Projekte Stadt1 am Straße5 GmbH GmbH in Liqu. 2013-2018, Auf der Straße3 Straße3 GmbH  in Liqu. 2014-2019, Flugzeug1 Ort5- und OrtOrt4 GmbH, Flugzeug1 Straße1straße GmbH ab  2011, jedoch noch in der Bauphase ).

**False Positives:**

- `Flugzeug1 Ort5- und OrtOrt4 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_621`)


Flugzeug1 GmbH, siehe oben b.)   2.231,25 €…………Differenz: Vorsteuer lt. BFG  107.399,96 € …….Summe steuerpflichtige Lieferungen und sonstige Leistungen  219,84 €…………….

**False Positives:**

- `Flugzeug1 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_36`)


Die KI Synlogtra GmbH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Brunhild Stanislav, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00  und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Die KI Synlogtra GmbH ` — partial — gold is substring of pred: `KI Synlogtra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Synlogtra GmbH`(organisation)
- `Brunhild Stanislav`(person)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_62`)


Die KI Synlogtra GmbH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Brunhild Stanislav, verhängten Geldstrafen von 3 x je € 520,00, 3 x je € 320,00 und 2  x je € 700,00 und die Verfahrenskosten in der Höhe von € 392,00 sowie für sonstige in Geld  bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.“

**False Positives:**

- `Die KI Synlogtra GmbH ` — partial — gold is substring of pred: `KI Synlogtra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Synlogtra GmbH`(organisation)
- `Brunhild Stanislav`(person)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_114`)


Die Haftung der KI Synlogtra GmbH  für die über den Beschuldigten, als deren Geschäftsführer der  Beschuldigte laut Akt bestellt war, zu Recht verhängten Geldstrafen samt Kosten ergibt sich  zwingend aus der Bestimmung des § 9 Abs. 7 VStG.

**False Positives:**

- `Die Haftung der KI Synlogtra GmbH ` — partial — gold is substring of pred: `KI Synlogtra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Synlogtra GmbH`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/139794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139794.1_36`)


Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:  Die Bf hat im September 2015 mit der Bausmann Luftfahrt GmbH einen Mietvertrag über  Geschäftsräumlichkeiten im Umfang von 579 m² abgeschlossen.

**False Positives:**

- `Die Bf hat im September 2015 mit der Bausmann Luftfahrt GmbH` — partial — gold is substring of pred: `Bausmann Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bausmann Luftfahrt GmbH`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/140017.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140017.1_5`)


Darunter ein von der Nieder Glanzber GmbH  als Leasinggeber, mit der Beschwerdeführerin (kurz: Bf), FN-h,  damals noch mit dem Firmennamen K-GmbH, als Leasingnehmer, abgeschlossener  Leasingvertrag.

**False Positives:**

- `Darunter ein von der Nieder Glanzber GmbH ` — partial — gold is substring of pred: `Nieder Glanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Glanzber GmbH`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_67`)


Die dazu im Rechenwerk der D- GmbH vorgefundene Rechnung vom 10.April 2012 hatte zwar  lediglich einen Betrag von 100.100,- € + 20% USt ausgewiesen, doch „kann man aufgrund der  vorgenommenen Ermittlungen davon ausgehen“, dass der IS den Betrag von 124.915,17 € auch  tatsächlich an die D- GmbH bezahlt hatte.

**False Positives:**

- `Die dazu im Rechenwerk der D- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_83`)


Auf Betreiben des MV der XY- GmbH verkaufte zudem der IS den TG-PP Nr 4 um 24.000,-  incl  20% USt an die Immobilien GmbH (KV 15.Okt.

**False Positives:**

- `Auf Betreiben des MV der XY- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_135`)


Aufgrund einer Teiloption der XY- GmbH nach § 6 (2) UStG 1994 enthielt der Kaufpreis  Umsatzsteuer in Höhe von 13.829,28 € (entfallend auf einen Teilkaufpreis von 69.146,41 €).

**False Positives:**

- `Aufgrund einer Teiloption der XY- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_174`)


Zudem wurden im Zuge der AP in den UVA des IS nur vereinzelt Vermietungsumsätze zum  Objekt B-Straße 88, jeweils mit mietenden Gesellschaften aus der sog. „IS.-Gruppe“ festgestellt  (IS-5 Projekt GmbH, IS-6 GmbH und XY- GmbH (8 u. 11/2012 sowie 4/2013) bzw. XY-  Projektentwicklung GmbH (2/2016).

**False Positives:**

- `IS-6 GmbH und XY- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_181`)


Der Firmensitz der XY- Projektentwicklung GmbH, FN 999996z (nachfolgend XY- Projekt GmbH)  befindet sich nach den AP-Feststellungen seit Juni 2013 „am eigentlichen Firmensitz der sog.  IS.-Gruppe“ in der nahegelegenen C-Straße 989 (AP-Bericht/B. 3 - 5).

**False Positives:**

- `Der Firmensitz der XY- Projektentwicklung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_191`)


Da die  XY- GmbH die aus der Option nach § 6 (2) UStG im Kaufvertrag vom 28.März 2012  resultierende USt iHv 52.517,47 € „erklärt und abgeführt“ habe, stehe der Vorsteuerabzug wie  in der UVA 4/2013 geltend gemacht zu.  Die Bf geht für den Zeitraum 4/2012 – 6/2017 von zumindest 131.553,42 € verbuchten  Mieteinnahmen aus und verweist auf im AP-Bericht unberücksichtigt gebliebene Teile der  Mieteinnahmen, die auf ein Kreditkonto geflossen bzw. auf dem Verrechnungskonto der  XY- GmbH erfasst gewesen seien.

**False Positives:**

- `Da die  XY- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_230`)


Denn mit der  XY- Projektentwicklung GmbH ging der letzte verbliebene Mieter (Mieter waren, wie bereits  erwähnt, ausschließlich Firmen aus dem Einflussbereich des Beschwerdeführers) im  August 2017 in Insolvenz.

**False Positives:**

- `Denn mit der  XY- Projektentwicklung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_35`)


Die Eheleute M und die Immo-GmbH waren jeweils zu einem Drittel Miteigentümer der  Liegenschaft in der R-Gasse.

**False Positives:**

- `Die Eheleute M und die Immo-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_36`)


Die Beschwerdeverfahren von Frau M und der Immo GmbH gegen die Inanspruchnahme als  Gesamtschuldner sind beim BFG zu den Zahlen RV/7100697/2022 bzw. RV/7101720/2021  erfasst.

**False Positives:**

- `Die Beschwerdeverfahren von Frau M und der Immo GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_45`)


Aktuell haftet auf dem Abgabenkonto der M-GmbH ein vollstreckbarer Rückstand von  25.778,30 € aus.

**False Positives:**

- `Aktuell haftet auf dem Abgabenkonto der M-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_69`)


Die M-GmbH als leistendes Unternehmen und die Miteigentumsgemeinschaft (MEG) der zu  bebauenden Liegenschaft als Leistungsempfängerin des verfahrensgegenständlichen  Bauauftrages waren im steuerlichen Sinn einander nahestehende Geschäftspartner.

**False Positives:**

- `Die M-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_75`)


Die M-GmbH  scheint als Planverfasserin und Bauführerin auf (GB BG 999, TZ 99998/2018 bzw.  TZ 99999/2020).

**False Positives:**

- `Die M-GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_97`)


Insgesamt erzielte die M-GmbH nach dem Ergebnis der durchgeführten abgabenbehördlichen  Überprüfungen aus den Rohbauleistungen in der R-Gasse bis 3/2019 einen Nettoumsatz von  1.015.689,43 € + 203.137,88 € USt.

**False Positives:**

- `Insgesamt erzielte die M-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_104`)


Dem BFG liegen keine im Sinne des AP-Ergebnisses berichtigten Rechnungen der M-GmbH vor.

**False Positives:**

- `Dem BFG liegen keine im Sinne des AP-Ergebnisses berichtigten Rechnungen der M-GmbH` — partial — gold is substring of pred: `BFG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_133`)


Der Bf brachte im Wege der XY WTH GmbH, fristgerecht „Beschwerde gegen den  Bescheid – Leistungsgebot“ vom 5.Nov.2021 ein und begehrte mit folgender Begründung die  Aufhebung der bekämpften Erledigung:  „Als Begründung ist anzuführen, dass Herr Wilhelm Fißenewert, LLM  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Hemken Automotive GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

**False Positives:**

- `Der Bf brachte im Wege der XY WTH GmbH` — partial — gold is substring of pred: `XY WTH GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XY WTH GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)
- `Hemken Automotive GmbH`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

**False Positives:**

- `Die von der Firma Hemken Automotive GmbH` — partial — gold is substring of pred: `Hemken Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hemken Automotive GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_276`)


Entsteht mangels Gefährdung gar keine Steuerschuld, bedarf es keiner Rechnungsberichtigung  (vgl. zuletzt EuGH 8.12.2022, C-378/21, Rs Mergel Bau GmbH und Zorn in RdW 2023, 225).

**False Positives:**

- `Rs Mergel Bau GmbH` — partial — gold is substring of pred: `Mergel Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mergel Bau GmbH`(organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_302`)


Mit einer Einbringlichkeit der im Mai 2019 vorgeschriebenen USt bei der M-GmbH war nicht zu  rechnen.

**False Positives:**

- `Mit einer Einbringlichkeit der im Mai 2019 vorgeschriebenen USt bei der M-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `m.b.H. entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e6052726`  
**Description:**
Matches entities ending in 'm.b.H.' (e.g., Steuerberatungsgesellschaft m.b.H.) or 'm.b.H. & Co. KG', ensuring the full company name is captured.

**Content:**
```
\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+Steuerberatungs-?\s+)?(?:Gesellschaft\s+m\.b\.H\.(?:\s+&\s+Co\.\s+KG)?|Steuerberatungsgesellschaft\s+m\.b\.H\.(?:\s+&\s+Co\.\s+KG)?))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steuerberatungsgesellschaft m.b.H.` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d9a6657c`  
**Description:**
Matches tax advisory firms ending in 'Steuerberatungsgesellschaft m.b.H.'.

**Content:**
```
\b([A-Z][A-Za-z0-9\s&\-]+\s+Steuerberatungsgesellschaft\s+m\.b\.H\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Snajdr E-Commerce GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d99b2255`  
**Description:**
Matches the specific entity 'Snajdr E-Commerce GmbH' including the special dash.

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

## `Landespolizeidirektion Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2fb493b0`  
**Description:**
Matches the specific entity 'Landespolizeidirektion Wien'.

**Content:**
```
\b(Landespolizeidirektion\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Wien full` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2aba0f49`  
**Description:**
Matches the full Vienna City Administration entity including department details.

**Content:**
```
\b(Magistrat\s+der\s+Stadt\s+Wien,\s+Magistratsabteilung\s+67)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kraftost-Digital AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `471a0925`  
**Description:**
Matches 'Kraftost-Digital AG' specifically, handling the dash and context.

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

## `Novotny Getränke GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5295f04e`  
**Description:**
Matches 'Novotny Getränke GmbH' specifically.

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

## `Hellfritsch Immobilien GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c972ae18`  
**Description:**
Matches 'Hellfritsch Immobilien GmbH' specifically.

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

## `xx GmbH Steuerberatung und Wirtschaftsprüfung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `edb58c13`  
**Description:**
Matches the specific long-form entity 'xx GmbH Steuerberatung und Wirtschaftsprüfung'.

**Content:**
```
\bxx\s+GmbH\s+Steuerberatung\s+und\s+Wirtschaftsprüfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `yy Wirtschaftstreuhand Gesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c82d6b3`  
**Description:**
Matches 'yy Wirtschaftstreuhand Gesellschaft mbH'.

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

## `FA Grieskirchen Wels` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a75a12dc`  
**Description:**
Matches 'FA Grieskirchen Wels'.

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

## `GmbH with date prefix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2646bc16`  
**Description:**
Matches GmbH entities preceded by a date and colon (e.g., '06.04.2023:Digital Lexwildon GmbH').

**Content:**
```
(?:\d{2}\.\d{2}\.\d{4}:)([A-Z][A-Za-z0-9\s&\-]+(?:GmbH|m\.b\.H\.)\s+(?:Wirtschaftsprüfungs- und Steuerberatungsgesellschaft|Steuerberatungs- und Wirtschaftsprüfungsgesellschaft|Steuerberatungsgesellschaft)?)(?=\s|$|[,;])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hoch-IT GmbH specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a9819114`  
**Description:**
Matches the specific entity 'Hoch-IT GmbH' to ensure it is captured correctly in all contexts.

**Content:**
```
\bHoch-IT GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `H SteuerberatungsGmbH specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f5ec51a`  
**Description:**
Matches the specific entity 'H SteuerberatungsGmbH' to ensure it is captured correctly.

**Content:**
```
\bH SteuerberatungsGmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dorffenlem Holz KG specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9e55411c`  
**Description:**
Matches the specific entity 'Dorffenlem Holz KG' to ensure it is captured correctly.

**Content:**
```
\bDorffenlem\s+Holz\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steuerberatung Dr. Alfred Sorger GmbH specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ca3147cb`  
**Description:**
Matches the specific entity 'Steuerberatung Dr. Alfred Sorger GmbH' to ensure it is captured correctly.

**Content:**
```
\bSteuerberatung\s+Dr\.\s+Alfred\s+Sorger\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Wien double space` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `44030b62`  
**Description:**
Specifically handles cases where 'Magistrat der Stadt Wien' has double spaces or irregular spacing, ensuring the full entity is captured.

**Content:**
```
\b(Magistrat(?:es)?\s{1,}\s+der\s{1,}\s+Stadt\s{1,}\s+Wien(?:,\s{1,}\s+Magistratsabteilung\s{1,}\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Derdonal-Garten AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ed40ac85`  
**Description:**
Matches the specific entity 'Derdonal-Garten AG' to ensure it is captured correctly in all contexts.

**Content:**
```
\b(Derdonal-Garten\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Post AG` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0fd0f88d`  
**Description:**
Matches the specific entity 'Post AG' which was previously missed.

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

## `SK Telecom` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `451a4551`  
**Description:**
Matches 'SK Telecom' and 'SK Telecom Co. Ltd' which are missing from the current rules.

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

## `Deutsche Telekom` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b31438cc`  
**Description:**
Matches 'Deutsche Telekom AG' and 'Deutschen Telekom AG' (genitive).

**Content:**
```
\b(?:Deutsche|Deutschen)\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgerichtes` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3e975426`  
**Description:**
Matches the genitive form 'Landesgerichtes' as an organisation.

**Content:**
```
\bLandesgerichtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Energie Verdorfwald GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e359ca68`  
**Description:**
Matches the specific entity 'Energie Verdorfwald GmbH'.

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

## `St. Johann Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c8da6130`  
**Description:**
Matches the specific entity 'St. Johann Steuerberatung GmbH' to ensure it is captured correctly.

**Content:**
```
\bSt\.\s+Johann\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schlaich Bau KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5a039dea`  
**Description:**
Matches the specific entity 'Schlaich Bau KG' to ensure it is captured correctly.

**Content:**
```
\bSchlaich\s+Bau\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt standalone` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16865c4d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' when not followed by a specific location name, to catch cases like 'das Finanzamt'.

**Content:**
```
\b(Finanzamt(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nieder Unisyn Manufaktur GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `701999e0`  
**Description:**
Matches the specific entity 'Nieder Unisyn Manufaktur GmbH'.

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

## `Frieb - Causa Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3bcd5e3c`  
**Description:**
Matches the specific entity 'Frieb - Causa Steuerberatung GmbH' including the special dash.

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

## `Fritzenwallner-Gandler Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f2912462`  
**Description:**
Matches the specific entity 'Fritzenwallner-Gandler Wirtschaftstreuhand- und Steuerberatungsgesellschaft mbH'.

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

## `Dreissigacker Möbel` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a3955abf`  
**Description:**
Matches the specific entity 'Dreissigacker Möbel'.

**Content:**
```
\bDreissigacker\s+Möbel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `I AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c3456cab`  
**Description:**
Matches the specific entity 'I AG' which was previously missed.

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

## `T-Mobile Austria GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `62243c5d`  
**Description:**
Matches 'T-Mobile Austria GmbH' specifically.

**Content:**
```
\bT-Mobile\s+Austria\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Klosterneuburg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `74ef3a71`  
**Description:**
Matches the specific entity 'FA Klosterneuburg'.

**Content:**
```
\bFA\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schniederjahn Software KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0127dd9d`  
**Description:**
Matches the specific entity 'Schniederjahn Software KG' to ensure it is captured correctly.

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

## `Unverdroß Planung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eb92df74`  
**Description:**
Matches the specific entity 'Unverdroß Planung GmbH' to ensure it is captured correctly.

**Content:**
```
\bUnverdro\u00df\s+Planung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirektion Niederösterreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8fe1e6f4`  
**Description:**
Matches the full entity 'Landespolizeidirektion Niederösterreich' to ensure the location is included.

**Content:**
```
\bLandespolizeidirektion\s+Nieder\u00f6sterreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fb9e895c`  
**Description:**
Matches the specific entity 'CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH'.

**Content:**
```
\bCENTURION\s+Wirtschaftsprüfungs\-\s+und\s+Steuerberatungs\s+GmbH\b
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

## `FA Wien 6/7/15` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7f904acb`  
**Description:**
Matches the specific entity 'FA Wien 6/7/15'.

**Content:**
```
\bFA\s+Wien\s+6/7/15\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ernst & Young Steuerberatungs-GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `485138c9`  
**Description:**
Matches the specific entity 'Ernst & Young Steuerberatungs-GmbH'.

**Content:**
```
\bErnst\s+&\s+Young\s+Steuerberatungs\-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Werkunival-Verlag GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0772c8d3`  
**Description:**
Matches the specific entity 'Werkunival-Verlag GmbH'.

**Content:**
```
\bWerkunival-Verlag\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SNWG Textil GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `34ad9f87`  
**Description:**
Matches the specific entity 'SNWG Textil GmbH' which was previously missed.

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

## `GOBBS Steuerberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7a5619eb`  
**Description:**
Matches the specific entity 'GOBBS Steuerberatungs GmbH' which was previously missed.

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

## `BDO Assurance GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1acdf1d8`  
**Description:**
Matches the specific entity 'BDO Assurance GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft' which was previously missed.

**Content:**
```
\bBDO\s+Assurance\s+GmbH\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `A1 Telekom Austria AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `24d9adf2`  
**Description:**
Matches the specific entity 'A1 Telekom Austria AG' which was previously missed.

**Content:**
```
\bA1\s+Telekom\s+Austria\s+AG\b
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

