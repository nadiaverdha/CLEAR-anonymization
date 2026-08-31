# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-31T09:27:57.943576

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-07-20/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 1000 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 800 |
| Validation documents | 200 |
| Test documents | 792 |
| Train sentences | 3245 |
| Validation sentences | 812 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 1 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 2 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 50 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 85.3% |
| True Positives | 783 |
| False Positives | 274 |
| False Negatives | 17390 |
| Total Gold Entities | 18173 |
| Micro Precision | 74.1% |
| Micro Recall | 4.3% |
| Micro F1 | 8.1% |
| Macro F1 | 8.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Oberste_Gerichtshof` | 0.0% | 100.0% | 0.0% | 3 | 3 | 0 |
| `Verfassungsgerichtshof` | 1.9% | 100.0% | 0.9% | 172 | 172 | 0 |
| `Landesgericht_City_Extended` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Landesgericht_Strafsachen` | 0.1% | 100.0% | 0.0% | 7 | 7 | 0 |
| `OGK_Abbreviation` | 0.4% | 97.5% | 0.2% | 40 | 39 | 1 |
| `Hyphenated_Ampersand_Corporate_Name` | 1.7% | 93.9% | 0.8% | 163 | 153 | 10 |
| `Magistrat_Wien` | 3.9% | 86.1% | 2.0% | 425 | 366 | 59 |
| `Law_Firm_Rechtsanwaelte_OG` | 0.0% | 50.0% | 0.0% | 6 | 3 | 3 |
| `Law_Firm_OG_KG_GmbH` | 0.0% | 26.7% | 0.0% | 15 | 4 | 11 |
| `Generic_KG_Entity` | 0.2% | 22.8% | 0.1% | 79 | 18 | 61 |
| `OGH_Abbreviation` | 0.2% | 20.2% | 0.1% | 84 | 17 | 67 |
| `Oberlandesgericht_City` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht_Handelsgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht_City_Extended` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verein_Organisation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht_Grieskirchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PVA_Abbreviation` | 0.0% | 0.0% | 0.0% | 60 | 0 | 60 |
| `SAK_Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizer_Ausgleichskasse_SAK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wien_Telekom_Betriebe_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gesellschaft_mbh_Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vorarlberger_Gebietskrankenkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht_Spittal_Güssing_Schärding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht_Krems` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Domain_Organisation` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Hyphenated_Gesellschaft_mbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgerichts_Leopoldstadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Slash_Separated_Corporate_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Oberste_Gerichtshof` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `69f4d34d`  
**Description:**
Matches the Supreme Court of Austria in nominative or genitive case.

**Content:**
```
\bOberste(?:n)?\s+Gerichtshof(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 13430 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_49`)


Im Urteil des Landesgerichtes LG (yCgyy/yyy vom Datum_2; dieses Urteil wurde vom Obersten  Gerichtshof am Datum_1, xObxxx/xxx bestätigt) werde festgehalten, „... dass die beklagte  Partei für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden ... haftet“.

| Predicted | Gold |
|---|---|
| `Obersten  Gerichtshof` | `Obersten  Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_62`)


In diesem Verfahren entschied der Oberste Gerichtshof mit Urteil vom Datum_1, xObxxx/xxx,  zugunsten der Bf als Klägerin und bestätigte das Urteil des Landesgerichtes LG vom Datum_2,  yCgyy/yyy.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_68`)


Das vom Obersten Gerichtshof bestätigte Urteil des Landesgerichtes LG diente in der Folge als  Rechtgrundlage für die weiteren Nettozahlungen der B an die Bf im streitgegenständlichen Jahr  2019.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

</details>

---

## `Verfassungsgerichtshof` 🏆

**F1:** 0.019 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `4f019849`  
**Description:**
Matches the Constitutional Court (Verfassungsgerichtshof) in nominative or genitive case.

**Content:**
```
\bVerfassungsgerichtshof(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.019 | 172 | 172 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 172 | 0 | 17372 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_25`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_28`)


Der Verfassungsgerichtshof hat in Bezug auf die zeitliche Anwendbarkeit des § 4 Abs. 2 Z 2  EStG 1988 mit Beschluss vom 8. Juni 2020, E 2108/2019-15, ausgesprochen, dass selbst wenn  der Bestimmung der Vorschrift des § 4 Abs. 2 Z 2 EStG materiell-rechtlicher Charakter  zuzumessen wäre, der Gleichheitssatz deren Anwendung auf die ab Inkrafttreten  durchgeführten Veranlagungen der Zeiträume ab 2003 nicht entgegen stehe, da die Vorschrift  in den Fällen der Bilanzberichtigung doch – je nach Sachlage zugunsten wie auch zulasten des  Steuerpflichtigen – der Erzielung einer richtigen Totalgewinnbesteuerung diene, die jener  entsprechen solle, wenn die Bilanz von vornherein richtig erstellt worden wäre.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_108`)


BFG 17.03.2014, RV/7100539/2014):  Festgehalten wird noch, dass der Verfassungsgerichtshof gegen die Einschränkung der  Beweisführung des Grades der Behinderung oder der voraussichtlichen dauerhaften  Unfähigkeit, sich selbst den Erwerb zu verschaffen, im Erkenntnis vom 10.12.2007, B 700/07,  keine verfassungsrechtlichen Bedenken geäußert (vgl. VwGH 22.12.2011, 2009/16/0307) und  weiters erkannt hat, dass von Gutachten NUR nach "entsprechend qualifizierter  Auseinandersetzung" abgegangen werden kann, wenn diese nicht schlüssig sind (vgl. VwGH  13.12.2012, 2009/16/0325;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_388`)


Der Verfassungsgerichtshof äußerte in seinem Erkenntnis vom 10.12.2007, B 700/07 keine  verfassungsrechtlichen Bedenken gegen die Einschränkung der Beweisführung des Grades der  Behinderung oder der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu  verschaffen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_72`)


In diesem Zusammenhang darf auch darauf hingewiesen werden, dass der  Verfassungsgerichtshof den Ausschluss der Familienbeihilfe bei ständigem Aufenthalt des  Kindes im Ausland (§ 5 Abs 3 FLAG 1967) als verfassungsrechtlich zulässig erachtet hat (vgl die  Erkenntnisse VfGH 15.6.2002, G 112/99, VfSlg 16.542, und VfGH 14.12.2001, B 2366/00, VfSlg  16.380).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_3`)


Begründung  In dem Verfahren, in dem die Beschwerdeführerin [...] (in der Folge als Antragstellerin  bezeichnet) den Antrag auf Verfahrenshilfe gestellt hatte, hatte einen handschriftlichen Antrag  auf Rückzahlung eines Betrages von 360 € vom 20.11.2019 an die belangte Behörde zum Inhalt.  Begründet wurde dieser damit, dass der Betrag zu Unrecht eingefordert wurde, weil eine  Beschwerde beim Verfassungsgerichtshof nicht von einem Rechtsanwalt unterfertigt worden  wäre und daher kein Gebührenanspruch entstanden wäre.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_15`)


In der rechtlichen  Würdigung wurde angemerkt wurde, dass selbst bei fristgerechter Einbringung der  Beschwerde eine Abweisung zu treffen gewesen wäre, da die Verpflichtung zur Zahlung einer  Eingabegebühr gem. § 17a VfGG unabhängig davon besteht, ob diese Einbringung den  formalen Voraussetzungen für Beschwerden an den Verfassungsgerichtshof entspricht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_22`)


Das Bundesfinanzgericht stellte mit Beschluss vom 20. Oktober 2020 an den  Verfassungsgerichtshof einen Normenprüfungsantrag hinsichtlich der Bestimmung des § 19  Abs 1 EStG 1988.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_25`)


Beim Verfassungsgerichtshof ist diesbezüglich unter der Zahl G 223/2020 ein weiterer  Normenprüfungsantrag anhängig, außerdem eine unter der Zahl E 513/2020 erfasste  Beschwerde gemäß Art. 144 Abs 1 B-VG.   B. Rechtslage  Gemäß § 292 Abs. 1 BAO ist auf Antrag einer Partei (§ 78), wenn zu entscheidende  Rechtsfragen besondere Schwierigkeiten rechtlicher Art aufweisen, ihr für das  Beschwerdeverfahren Verfahrenshilfe vom Verwaltungsgericht insoweit zu bewilligen,  1. als die Partei außerstande ist, die Kosten der Führung des Verfahrens ohne Beeinträchtigung  des notwendigen Unterhalts zu bestreiten und  2.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_51`)


Der Verfassungsgerichtshof wird sich in den anhängigen  Normenprüfungs- und Beschwerdeverfahren mit dieser Frage auseinandersetzen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_65`)


Weder offenbar aussichtslos noch mutwillig  Eine Beschwerde gegen den Einkommensteuerbescheid 2018 kann aufgrund der geschilderten  verfassungsrechtlichen Bedenken, über die der Verfassungsgerichtshof abzusprechen hat,  weder als offenbar aussichtslos noch als mutwillig iSd § 292 Abs. 5 BAO bezeichnet werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_59`)


Zur Rechtsnatur der Einkommensteuerrichtlinien ist auf das Erkenntnis des  Verwaltungsgerichtshofes vom 31.01.2018, Ra 2017/15/0038, hinzuweisen:  „Der Verfassungsgerichtshof ist in seinem Erkenntnis vom 28. Juni 2017, V 4/2017, von seiner  bisherigen Rechtsprechung zu Art. 89 B-VG und Art. 139 Abs. 3 bzw. Art. 140 Abs. 3 B-VG,  wonach nicht gehörig kundgemachte Verordnungen von den Gerichten auch ohne Anfechtung  vor dem Verfassungsgerichtshof von vorneherein nicht anzuwenden seien, abgegangen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_60`)


Er  vertritt nunmehr die Auffassung, dass auch Gerichte gesetzwidrig kundgemachte Verordnungen  anzuwenden haben und diese, wenn sie Bedenken gegen ihre rechtmäßige Kundmachung  haben, vor dem Verfassungsgerichtshof anzufechten haben;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_61`)


bis zur Aufhebung durch den  Verfassungsgerichtshof sind sie für jedermann verbindlich (vgl. Punkt 2.9 des genannten  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_90`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_180`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_18`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_142`)


In den zuletzt angeführten Erkenntnissen hat das Bundesfinanzgericht unter Verweis auf das  Erkenntnis BFG 13.7.2015, RV/5100538/2014, darüber hinaus auch festgehalten, dass die  Polizeigrundausbildung die vom Verfassungsgerichtshof herausgearbeiteten Kriterien eines  anerkannten Lehrverhältnisses im Sinne des § 5 Abs. 1 lit. b FLAG 1967 erfüllt und daher als ein  "anerkanntes Lehrverhältnis" anzusehen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_79`)


Eine Verletzung verfassungsrechtlicher Gebote sei vom Verfassungsgerichtshof bislang nicht  festgestellt worden, er habe die Behandlung entsprechender Beschwerden abgelehnt (siehe  diverse Beschlüsse vom 1.12.2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_108`)


Der Verfassungsgerichtshof hat zu den Zuschüssen zum Kinderbetreuungsgeld in seinem  Erkenntnis vom 26.02.2009, G128/08 ua Folgendes ausgeführt:  12 von 24 Seite 13 von 24

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_135`)


Der Verfassungsgerichtshof vermag diese Bedenken im Ergebnis nicht zu teilen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_151`)


Dass die Ermittlung des maßgeblichen Jahresbetrags auf dieser Basis für die potentiell  anspruchsberechtigten Bezieher von KBG unmöglich oder in verfassungswidriger Weise  erschwert sei, kann der Verfassungsgerichtshof nicht finden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_166`)


Solche Umstände hat der Verfassungsgerichtshof in dem (auch von den antragstellenden  Gerichten zitierten) Erkenntnis VfSlg.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_169`)


Zu  diesem Ergebnis kam der Verfassungsgerichtshof aber vor allem deswegen, weil die damals zu  beurteilende Regelung eine volle, den Betrag der eigenen Einkünfte (unter Umständen weit)  übersteigende Rückzahlungsverpflichtung beinhaltete.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_177`)


In einem anderen vor dem  Verfassungsgerichtshof zu § 18 Abs. 1 Z 1 KBGG geführten  Verfahren hat der Verfassungsgerichtshof in seinem Erkenntnis vom 04.03.2011,  Zl. G184/10 in der Begründung die Stellungnahme der Bundesregierung wie folgt  wiedergegeben:  „3.4. ...

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_181`)


Der Verfassungsgerichtshof hat sich dazu wie folgt geäußert:  „2.3.2. ...

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_183`)


Der Verfassungsgerichtshof schließt sich dieser  Auffassung an.“

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_189`)


Beschwerdeführenden Parteien steht das Recht zu, innerhalb von sechs Wochen ab Zustellung  dieser Entscheidung eine Beschwerde an den Verfassungsgerichtshof, 1010 Wien, Freyung 8,  zu erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_190`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_191`)


Die  Beschwerde an den Verfassungsgerichtshof muss - abgesehen von den gesetzlich bestimmten  Ausnahmen - durch eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten  Rechtsanwalt eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_198`)


Das Antragsformular samt  Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch, postalisch oder  persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_23`)


Im Erkenntnis vom 11. Oktober 2001,  G 12/00, habe der Verfassungsgerichtshof die Verfassungsbestimmung des § 126a Bundesver- gabegesetz 1997 idF BGBl. I Nr. 125/2000 aufgehoben, "weil es dem einfachen Verfassungsge- setzgeber nicht gestattet ist, die Bundesverfassung auch nur für einen Teilbereich der Rechts- ordnung in ihrer Wirkung schlechthin zu suspendieren."

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_34`)


§ 34 Abs. 7 Z 5 EStG 1988 verstoße somit gegen die verfassungsrechtliche Grundordnung und  sei daher zur Gänze verfassungswidrig, weshalb die Beantragung eines Gesetzesprüfungsver- fahrens beim Verfassungsgerichtshof durch das Bundesfinanzgericht angeregt werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_66`)


Diese Rechtsansicht wurde auch vom Verwaltungsgerichtshof geteilt  und sah sich dieser daher nicht dazu veranlasst, die Überprüfung der Verfassungsvorschrift  des § 34 Abs. 7 Z 5 EStG 1988 auf ihre Übereinstimmung mit den Baugesetzen der österreichi- schen Bundesverfassung beim Verfassungsgerichtshof zu beantragen (vgl. VwGH 10.8.2005,  2004/13/0170; in diesem Sinne auch VwGH 28.11.2007, 2007/15/0187).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_67`)


Damit vermag aber  auch das Bundesfinanzgericht keine Veranlassung zu erkennen, beim Verfassungsgerichtshof  5 von 7 Seite 6 von 7

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_60`)


Gemäß Art. 135 Abs. 4 B-VG iVm Art. 89 B-VG steht die Prüfung der Gültigkeit gehörig  kundgemachter Gesetze den Verwaltungsgerichten nicht zu. Hat ein solches Gericht gegen die  Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so hat es den  Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_73`)


Der Verfassungsgerichtshof (VfGH) war schon mehrfach mit den verschieden Verlustausgleichs-  und -vortragsbeschränkungen im betrieblichen und außerbetrieblichen Bereich befasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_498`)


Etwaige unterschiedliche Ergebnisse erkannte der  Verfassungsgerichtshof jedoch nicht als unsachlich (VfGH 8.6.1985, B 488/80).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_44`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit  Erkenntnis vom 2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Mit 20.01.2021 wurde der amtliche Befund über eine Verkürzung von Stempel- oder  Rechtsgebühren vom Verfassungsgerichtshof dem Finanzamt Österreich, Dienststelle für  Sonderzuständigkeiten, zur Anzeige gebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_19`)


Nach der Bestimmung des § 17a VfGG ist für beim Verfassungsgerichtshof eingebrachte  Beschwerden spätestens im Zeitpunkt der Überreichung eine Gebühr in Höhe von € 240.- zu  entrichten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_24`)


Mit dem Einlangen der Beschwerde beim Verfassungsgerichtshof ist der gebührenpflichtige  Tatbestand im Sinne des § 17a VfGG erfüllt (vgl. VwGH 22.10.2015, 2013/16/0101;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_26`)


Wie der Verfassungsgerichtshof letztendlich mit der Beschwerde  verfährt, hat auf das Entstehen der Gebührenschuld keinen Einfluss.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_136`)


Es sah sich daher nicht veranlasst, einen Gesetzesprüfungsantrag an den  Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_141`)


Die vom Bf aufgeworfene Frage der Verfassungskonformität einer gesetzlichen Bestimmung  stellt keine Rechtsfrage im Sinne der Subsumtion unter einen gesetzlichen Tatbestand dar, die  vom Verwaltungsgerichtshofzu überprüfen ist, sondern ist deren Prüfung dem  Verfassungsgerichtshof vorbehalten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_21`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_79`)


X Dauerzustand  2. Beweiswürdigung  Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele (BFG 17.07.2019, RV/7105214/2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_38`)


Die Begründung, (nur)  diese beiden Gutachten als Beweismittel heranzuziehen, ist folgende:  Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_137`)


Ad B, Urteile des Verfassungsgerichtshof welche die Anwendung des Nominalwertprinzips in  diesem Fall stützen sollen  Sie bringen die Urteile B 165/75 und B 193/77 des Verfassungsgerichtshofes auf, welche  aussagen sollen, dass das Nominalwertprinzip trotz der damit verbundenen Möglichkeit der  Besteuerung von Scheingewinnen verfassungskonform sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofes` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_188`)


Der Verfassungsgerichtshof (VfGH) hat mit Erkenntnissen vom 17. März 1976, B 165/75,  VfSlg 7770, zum EStG 1967, und vom 13.12.1982, B 193/77,G85/77, zum EStG 1972 die  Besteuerung des Einkommens nach dem Nominalwertprinzip trotz der damit verbundenen  Möglichkeit der Scheingewinnbesteuerung als mit der Verfassung im Einklang angesehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_202`)


Der Verfassungsgerichtshof geht vorläufig davon aus, dass es im rechtspolitischen  Gestaltungsspielraum des Gesetzgebers liegt, zu entscheiden, ob und inwieweit er die  Geldentwertung im Rahmen der Einkommensbesteuerung berücksichtigt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_89`)


Der Verfassungsgerichtshof hat im Erkenntnis VfGH 10.12.2007, B 700/07, ausgeführt, dass  sich aus Wortlaut und Entstehungsgeschichte des § 8 Abs. 6 FLAG ergebe, dass der  Gesetzgeber nicht nur die Frage des Grades der Behinderung, sondern (bereits seit 1994) auch  die (damit ja in der Regel unmittelbar zusammenhängende) Frage der voraussichtlich  dauernden Unfähigkeit, sich selbst den Unterhalt zu verschaffen, der eigenständigen  Beurteilung der Familienbeihilfenbehörden entzogen und dafür ein qualifiziertes  Nachweisverfahren eingeführt habe, bei dem eine für diese Aufgabenstellung besonders  geeignete Institution eingeschaltet werde und der ärztliche Sachverstand die  ausschlaggebende Rolle spiele (BFG 17.07.2019, RV/7105214/2018).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_59`)


Belehrung und Hinweise  Dem Antragsteller steht das Recht zu, innerhalb von sechs Wochen ab Zustellung dieser  Entscheidung eine Beschwerde an den Verfassungsgerichtshof (Freyung 8, 1010 Wien) zu  erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_60`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_61`)


Die Beschwerde  an den Verfassungsgerichtshof muss - abgesehen von den gesetzlichen Ausnahmen - durch  eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten Rechtsanwalt eingebracht  werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_66`)


Das  Antragsformular samt Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch,  postalisch oder persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_76`)


Das zuständige Verwaltungsgericht ist gemäß § 5 WAOR das  Bundesfinanzgericht, wie auch der Verfassungsgerichtshof in seinem Erkenntnis vom  27.2.2015, Zahl G 139/2014 bestätigt hat.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_86`)


Den beiden Parteien wird hiermit die Möglichkeit eingeräumt, zu diesem Vorhalt bis 31. Mai  2022 eine Stellungnahme beim Bundesfinanzgericht einzubringen …  Dieser Vorhalt ist ein verfahrensleitender Beschluss, gegen den weder eine abgesonderte  Revision an den Verwaltungsgerichtshof noch eine abgesonderte Beschwerde an den  Verfassungsgerichtshof zulässig ist (§ 25a Abs 3 VwGG, § 88a Abs 3 VfGG).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/138877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138877.1_46`)


Die Behandlung einer gegen dieses  Erkenntnis eingebrachten Verfassungsgerichtshofbeschwerde wurde vom  Verfassungsgerichtshof abgelehnt, eine Revision wurde nicht erhoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_229`)


Gegen die Einschränkung der Beweisführung des Grades der Behinderung oder  der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu verschaffen, hat der  Verfassungsgerichtshof im Erkenntnis vom 10.12.2007, B 700/07, keine verfassungsrechtlichen  Bedenken gesehen (vgl. VwGH 22.12.2011, 2009/16/0307).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_72`)


2. darüber belehrt, dass ein Antrag auf Ausfertigung des Erkenntnisses gemäß § 29 Abs. 4  VwGVG eine Voraussetzung für die Zulässigkeit der Revision beim Verwaltungsgerichtshof und  der Beschwerde beim Verfassungsgerichtshof darstellt.   Eine Ausfertigung der Niederschrift wurde den in der Verhandlung anwesenden Parteien  ausgefolgt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_73`)


Binnen zwei Wochen nach Ausfolgung bzw. Zustellung der Niederschrift über die mündliche  Verhandlung wurde von keiner Partei ein Antrag auf schriftliche Ausfertigung des  Erkenntnisses gemäß § 29 Abs. 4 VwGVG gestellt. Wird auf die Revision beim  Verwaltungsgerichtshof und die Beschwerde beim Verfassungsgerichtshof von den Parteien  verzichtet oder nicht binnen zwei Wochen nach Ausfolgung bzw. Zustellung der Niederschrift  gemäß § 29 Abs. 2a VwGVG eine Ausfertigung des Erkenntnisses gemäß § 29 Abs. 4 VwGVG  von mindestens einem der hiezu Berechtigten beantragt, so kann gemäß § 29 Abs. 5 VwGVG  das Erkenntnis in gekürzter Form ausgefertigt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_115`)


Zur Unzulässigkeit der Revision und Hinweis  Da von den Parteien auf die Revision an den Verwaltungsgerichtshof und die Beschwerde an  den Verfassungsgerichtshof verzichtet wurde bzw. nicht binnen zwei Wochen nach Ausfolgung  bzw. Zustellung der Niederschrift gemäß § 29 Abs. 2a VwGVG eine Ausfertigung des  Erkenntnisses gemäß § 29 Abs. 4 VwGVG beantragt wurde, ist gemäß § 29 Abs. 5 VwGVG die  Erhebung einer Revision beim Verwaltungsgerichtshof oder einer Beschwerde beim  Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/139725.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139725.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/139762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139762.1_74`)


Mit Erkenntnis vom 30. November 2017, G 183/2017, hat der Verfassungsgerichtshof die Wort- folge „oder § 30a Abs. 1“ in § 20 Abs. 2 EStG 1988 idF BGBl. I Nr. 22/2012 als verfassungswidrig  aufgehoben und ausgesprochen, dass die Aufhebung mit Ablauf des 31. Dezember 2018 in  Kraft tritt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/139802.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139802.1_14`)


Diese Vorgehensweise wurde damit begründete, dass der Verfassungsgerichtshof mit  Erkenntnis vom 24. September 2018 (Zl. V 60/2018) die Wortfolge „ausgenommen jene nach §  1 Z 9 (Vertreter)“ in § 4 Abs. 1 der Verordnung über die Aufstellung von Durchschnittssätzen  für Werbungskosten, BGBl. II Nr. 382/2001 idF BGBl. II Nr. 382/2015, als gesetzwidrig  aufgehoben habe.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/140032.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140032.1_29`)


Obige Bestimmung des Progressionsvorbehaltes wurde vom Verfassungsgerichtshof geprüft  und als verfassungskonform beurteilt (vgl. VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/140065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140065.1_2`)


II. Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/140478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140478.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_9`)


Ich rege an, das Bundesfinanzgericht möge gemäß Art. 140 Abs. 1 Z. 1 lit. a B-VG beim  Verfassungsgerichtshof die Aufhebung der gegenständlichen Bestimmung (§ 41 Abs. 3 letzter  Satz EStG) beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_33`)


Ich hoffe,  meine weiteren Ausführungen veranlassen — zusammen mit dem bereits erwähnten Artikel  von Frau Prof. Kanduth-Kristen — das Gericht dazu, meine Zweifel an der  Verfassungsmäßigkeit der gegenständlichen Regelung zu teilen und wie angeregt deren  Aufhebung beim Verfassungsgerichtshof zu beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_59`)


Es besteht daher kein Grund für den Senat gemäß Art. 140 Abs. 1 Z. 1 lit. a B-VG beim  Verfassungsgerichtshof die Aufhebung des § 41 Abs. 3 letzter Satz EStG zu beantragen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_63`)


Belehrung und Hinweise  Dem Antragsteller steht das Recht zu, innerhalb von sechs Wochen ab Zustellung dieser  Entscheidung eine Beschwerde an den Verfassungsgerichtshof (Freyung 8, 1010 Wien) zu  erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_64`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_65`)


Die Beschwerde  an den Verfassungsgerichtshof muss - abgesehen von den gesetzlichen Ausnahmen - durch  eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten Rechtsanwalt eingebracht  werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_69`)


Das  Antragsformular samt Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch,  postalisch oder persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/141326.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141326.1_3`)


II)  Gegen diesen Beschluss ist gem. § 30a Abs 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_220`)


Der Verfassungsgerichtshof äußerte in seinem Erkenntnis vom VfGH 10.12.2007, B 700/07,  keine verfassungsrechtlichen Bedenken gegen die Einschränkung der Beweisführung des  Grades der Behinderung oder der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den  Erwerb zu verschaffen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/141625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141625.1_80`)


Der  Verfassungsgerichtshof hat ausgesprochen, dass Fahrtkosten zu einem Wohnheim für  beeinträchtigte Menschen - wenn sie nicht unter § 5 Abs. 3 der VO (Behindertenwerkstätte)  subsumiert werden können - als Kosten der Heilbehandlung anzusehen sind, weil sie einem  6 von 9 Seite 7 von 9

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/141625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141625.1_83`)


Der Verwaltungsgerichtshof und der Verfassungsgerichtshof haben demnach nicht sämtliche  Aufwendungen bzw. Fahrtkosten, die einer Verbesserung der Krankheit oder Behinderung  dienen könnten bzw. einen positiven therapeutischen Zweck haben, dem § 4 der angeführten  Verordnung subsumiert;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/141912.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141912.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/142010.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142010.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1  VwGG) oder eine Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 Z 2 VfGG) nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/142010.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142010.1_5`)


Dagegen erhob die Beschwerdeführerin zunächst Beschwerde an den Verfassungsgerichtshof.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/142010.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142010.1_6`)


Nachdem der Verfassungsgerichtshof mit Beschluss vom 28. Juni 2023 die Behandlung der  Beschwerde abgelehnt und über Antrag der Beschwerdeführerin mit weiterem Beschluss vom  14. Juli 2023 die Beschwerde dem Verwaltungsgerichtshof zur Entscheidung abgetreten hatte,  erhob die Beschwerdeführerin nunmehr auch außerordentliche Revision gegen das Erkenntnis  vom 15.11.2022.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_73`)


Information für die Parteien (Belehrung nach § 280 Abs 4 BAO)  Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/143468.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143468.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/144154.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144154.1_43`)


Zusätzlich wurde darauf  hingewiesen, dass die Behandlung der gegen diese Entscheidungen erhobenen Beschwerden  an den Verfassungsgerichtshof von diesem durchwegs abgelehnt wurde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/144154.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144154.1_73`)


Sofern gegen diese Entscheidungen  eine Beschwerde an den Verfassungsgerichtshof erhoben wurde, lehnte dieser die Behandlung  6 von 9 Seite 7 von 9

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/144352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144352.1_100`)


Zugleich ersuchte die Bf das angerufene Verwaltungsgericht (Bundesfinanzgericht) gemäß  Art 135 Abs 4 iVm Art 89 Abs 2 und Art 140 Abs 1 B-VG einen Antrag auf Aufhebung der  Bestimmung des § 1 Abs 3, § 3 Abs 1, § 3 Abs 5, und § 5 Abs 1 bis Abs 3 des Bundesgesetzes  über den Energiekrisenbeitrag-Strom an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/144352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144352.1_130`)


Gemäß Art. 89 Abs. 2 B-VG hat ein ordentliches Gericht, wenn es gegen die Anwendung eines  Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat, den Antrag auf Aufhebung  dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/144352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144352.1_269`)


Aus den dargelegten Gründen bestand kein Anlass, einen Aufhebungsantrag gemäß Art. 89  Abs. 2 B-VG betreffend das EKBSG an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/144400.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144400.1_49`)


Daraus habe der  Verfassungsgerichtshof (VfGH) ein allgemeines und umfassendes verfassungsrechtliches  Sachlichkeitsgebot abgeleitet, dem jedes Staatshandeln entsprechen müsse.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/144400.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144400.1_53`)


Der Verfassungsgerichtshof  hege keinen Zweifel daran, dass es sich bei Art 21 Abs. 1 GRC - vgl auch Art 7 Abs. 1 B-VG und  Art 14 EMRK - um eine Garantie der GRC handle, die in ihrer Formulierung und Bestimmtheit  verfassungsgesetzlich gewährleisteten Rechten der österreichischen Bundesverfassung gleiche,  mithin keine völlig unterschiedliche normative Struktur als diese aufweise.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/144400.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144400.1_265`)


auch die von der Grundrechte-Charta garantierten Rechte vor dem Verfassungsgerichtshof als  verfassungsgesetzlich gewährleistete Rechte gemäß Art 144 bzw Art 144a B-VG geltend  gemacht werden könnten und sie im Anwendungsbereich der Grundrechte-Charta einen  Prüfungsmaßstab in Verfahren der generellen Normenkontrolle, insbesondere nach Art 139  und Art 140 B-VG bildeten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/144400.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144400.1_274`)


Sollte das zuständige Verwaltungsgericht die verfassungsrechtlichen Bedenken der Bf gegen  die präjudiziellen Bestimmungen teilen, möge es an den Verfassungsgerichtshof gemäß Art 135  Abs 4 iVm Art 89 Abs 2 B-VG und Art 140 Abs 1 B-VG einen Antrag auf Aufhebung der  präjudiziellen Bestimmungen des EKBSG idgF wegen Verfassungswidrigkeit richten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Landesgericht_City_Extended` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d93c350a`  
**Description:**
Matches Regional Courts with city names, ensuring 'St. Pölten', 'Hermagor', 'Leoben', 'Salzburg', 'Graz', 'Wien', 'Linz', 'Innsbruck', 'Klagenfurt', 'Bregenz', 'Feldkirch', 'Leoben', 'Lienz', 'Villach', 'Wels', 'Schwechat', 'Liesing', 'Gmunden', 'Bad Ischl', 'Telfs', 'Neusiedl am See', 'Favoriten', 'Fünfthau', 'Josefstadt', 'Hietzing', 'Ried im Innkreis', 'Krems an der Donau', 'Eisenstadt', 'Korneuburg', 'Laa an der Thaya', 'Wiener Neustadt', 'Steyr' are included.

**Content:**
```
\bLandesgerichts?\s+(?:für\s+Zivilrechtssachen\s+(?:Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten)|Eisenstadt|Salzburg|Innsbruck|Korneuburg|Laa\s+an\s+der\s+Thaya|Wels|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Steyr|Wiener\s+Neustadt|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Feldkirch|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Hermagor)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 6658 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_68`)


Mit Beschluss des Landesgerichts Salzburg vom 20. August 2014 erfolgte hinsichtlich der Klemeyer + Heisterhagen Pharma GmbH die Eröffnung des Sanierungsverfahrens ohne Eigenverwaltung, welches mit Beschluss  vom 19. Dezember 2014 aufgrund der rechtskräftigen Bestätigung des Sanierungsplans  aufgehoben wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Klemeyer + Heisterhagen Pharma GmbH` (organisation)

</details>

---

## `Landesgericht_Strafsachen` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `29819c24`  
**Description:**
Matches Regional Courts for Criminal Matters (Landesgericht für Strafsachen).

**Content:**
```
\bLandesgerichts?\s+für\s+Strafsachen\s+(?:Wien|Linz|Salzburg|Innsbruck|Graz|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St.\s+Pölten|Eisenstadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 6805 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_160`)


Am 10.9.2018 übermittelte das Finanzamt Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde gemäß § 100 Abs. 2 StPO den Zwischen- und Abschussbericht an die  Staatsanwaltschaft Wien beim Landesgericht für Strafsachen und diese legte am 15.7.2019 die  Anklageschrift dem Landesgericht für Strafsachen Wien vor.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Landesgericht für Strafsachen` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_162`)


Am 23.9.2019 ist gegen den Bf. ein Urteil des Landesgerichts für Strafsachen Wien ergangen,  dessen Spruch auszugsweise wie folgt lautet:  „Ing. Bianca Karbow  ist schuldig, hat im Zeitraum 2008 bis 2013 im Bereich des Finanzamts Wien  9/18/19 Klosterneuburg als für die Wahrnehmung der abgabenrechtlichen Obliegenheiten  verantwortlicher Einzelunternehmer vorsätzlich unter Verletzung einer abgabenrechtlichen  Anzeige-, Offenlegungs- und Wahrheitspflicht eine Verkürzung von bescheidmäßig  festzusetzenden Abgaben bewirkt bzw zu bewirken versucht, und zwar,  I./ durch die Abgabe inhaltlich unrichtiger Steuererklärungen betreffend Einkommensteuer und  Umsatzsteuer, wobei er die Taten teils unter Verwendung falscher Beweismittel (§ 39 Abs 1 lit a  FinStrG), nämlich durch die Aufnahme von Schein- und Deckungsrechnungen, die gezielt zum  Zwecke der Abgabenhinterziehung produziert worden waren, in sein buchhalterisches  Rechenwerk aufnahm, derweil die Leistungen tatsächlich nicht bzw nicht im ausgewiesenen  Umfang stattgefunden hatten, beging, nämlich  1./ hinsichtlich Einkommensteuer  am 9.3.2010 für das Jahr 2008 EUR 57.486,09,  am 14.1.2011 für das Jahr 2009 EUR 49.150,22,  am 30.4.2012 für das Jahr 2010 EUR 15.424,-,  am 27.5.2013 für das Jahr 2011 EUR 22.581   am 1.12.2013 für das Jahr 2012 EUR 16.299,-,  am 16.1.2015 für das Jahr 2013 EUR 15.531,-,  SUMME EUR 176.471,31,  11 von 16 Seite 12 von 16

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Ing. Bianca Karbow` (person)
- `Finanzamts Wien  9/18/19` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_174`)


Sachverhaltsmäßig steht fest, dass das Landesgericht für Strafsachen Wien auch betragsmäßig  die Sachverhaltsfeststellungen der Betriebsprüfung bestätigt hat und es als erwiesen  angenommen hat, dass der Bf. die oben angeführten Taten in objektiver und subjektiver  Hinsicht begangen hat.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_175`)


Unstrittig ist weiters, dass das Landesgericht für Strafsachen Wien bei Ermittlung des  Sachverhaltes von Amts wegen vorzugehen hatte.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_185`)


Das Landesgericht für Strafsachen Wien hat in seinem Urteil vom 23.9.2019 festgestellt, dass  der Bf. die oben angeführten Taten in objektiver und subjektiver Hinsicht begangen hat, und es  dabei billigend in Kauf nahm und sich damit abfand seine abgabenrechtliche Anzeige-,  Offenlegungs- bzw. Wahrheitspflicht zu verletzen und damit die im Spruch des Strafurteils  genannten Abgaben zu verkürzen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_186`)


Das Landesgericht für Strafsachen Wien hat die Abgabenforderungen, welche aufgrund der  Feststellungen der Betriebsprüfung, hinsichtlich Einkommensteuer und Umsatzsteuer,  festgesetzt wurden, bestätigt.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_191`)


Bescheid betreffend Festsetzung von Umsatzsteuer für die Monate Jänner 2014 bis August  2014  Die im Zuge der Betriebsprüfung aufgedeckten und auch in den Vorjahren laut Urteil des  Landesgerichts für Strafsachen Wien gesetzten Handlungen (Schein- und Deckungsrechnungen)  wurden auch im Jahr 2014 fortgesetzt.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

</details>

---

## `OGK_Abbreviation` 🏆

**F1:** 0.004 | **Precision:** 0.975 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `ec038233`  
**Description:**
Matches the abbreviation ÖGK (Österreichische Gebietskrankenkasse).

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
| `organisation` | 39 | 1 | 15747 |

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

## `Hyphenated_Ampersand_Corporate_Name` 🏆

**F1:** 0.017 | **Precision:** 0.939 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `5952d33c`  
**Description:**
Matches corporate names where the name and suffix are connected by hyphens, plus signs, or ampersands without spaces (e.g., 'Kallenbach+Knackmuss Elektro GmbH', 'Höllerling&Voegtlin Logistik GmbH', 'See-Telekom Gruppe GmbH').

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+(?:GmbH|AG|Aktiengesellschaft|Gesellschaft\s+mbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.939 | 0.008 | 0.017 | 163 | 153 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 153 | 10 | 17672 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Irvin Kurrek  in der Beschwerdesache Alexandra Kesler,  Illyrerweg 5, 4073 Edramsberg, Österreich, (nunmehr Valsyn-Maschinenbau GmbH als Rechtsnachfolgerin der Schameitat Sanitär GmbH, vertreten durch StB,  über die Berufung (nunmehr Beschwerde) vom 21. August 2013 gegen die Bescheide des FA  vom 9. Juli 2013 betreffend Wiederaufnahme der Verfahren hinsichtlich der  Körperschaftsteuer für die Jahre 2009 und 2010 sowie die Körperschaftsteuer für die Jahre  2009 bis 2011 beschlossen:    I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) als nicht  zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Priv.-Doz. Irvin Kurrek` (person)
- `Alexandra Kesler` (person)
- `Illyrerweg 5, 4073 Edramsberg, Österreich` (address)
- `Schameitat Sanitär GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_6`)


Mit Verschmelzungsvertrag vom 27. September 2012 wurde die Bf als  übertragende Gesellschaft mit der Valsyn-Maschinenbau GmbH als übernehmende Gesellschaft rückwirkend per  31. Dezember 2011 verschmolzen und in weiterer Folge am 31. Oktober 2012 im Firmenbuch  gelöscht.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_38`)


Die angefochtenen Bescheide seien alle am 9. Juli 2013 an die "Alexandra Kesler" als  Bescheidadressat ausgestellt worden, obwohl diese Gesellschaft verschmelzungsbedingt  bereits am 31. Oktober 2012 im Firmenbuch gelöscht worden sei und damit eine  Gesamtrechtsnachfolge an die Valsyn-Maschinenbau GmbH eingetreten sei.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Alexandra Kesler` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_40`)


Über die Beschwerde wurde erwogen:    Entscheidungsrelevanter Sachverhalt  Mit Verschmelzungsvertrag vom 27. September 2012 wurde die Bf, dh die Schameitat Sanitär GmbH  mit  Wirkung zum 31. Dezember 2011 durch Übertragung ihres Vermögens als Ganzes mit der Valsyn-Maschinenbau GmbH im Wege der Gesamtrechtsnachfolge unter Inanspruchnahme der Begünstigungen des  Artikel I Umgründungssteuergesetz (UmgrStG) verschmolzen.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Schameitat Sanitär GmbH` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_52`)


Die angefochtenen Bescheide der belangten Behörde vom 9. Juli 2013 sind an die zu diesem  Zeitpunkt bereits mit der Valsyn-Maschinenbau GmbH verschmolzene Schameitat Sanitär GmbH ergangen.

| Predicted | Gold |
|---|---|
| `Valsyn-Maschinenbau GmbH` | `Valsyn-Maschinenbau GmbH` |

**Missed by this rule (FN):**

- `Schameitat Sanitär GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_4`)


Entscheidungsgründe  Strittig ist im anhängigen Verfahren die Rechtsmäßigkeit der nach einer bei der  Beschwerdeführer GmbH, FN 999999z (nachfolgend Synkel-Versicherung GmbH  gemäß § 150 BAO  durchgeführten Außenprüfung (AP) erfolgten Direktvorschreibung von Kapitalertragsteuer  (KeSt) für 2007 – 2009 an den Beschwerdeführer (Bf) als dem ehemaligen Alleingesellschafter- Geschäftsführer des geprüften Unternehmens.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_106`)


Die Vorlageunterlagen beschränkten sich auf die angefochtenen Bescheide, den AP Bericht der Synkel-Versicherung GmbH  die Berufung samt gesonderter Begründung (ohne darin erwähnte Beilagen), eine  Anfrage des Firmenbuchgerichts vom April 2012 wegen beabsichtigter Löschung der Synkel-Versicherung GmbHi.L. sowie den oa. Ablehnungsbescheid gem. § 84 BAO.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Synkel-Versicherung GmbHi.L.` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_151`)


II. Der Bf war von März 2007 bis Okt 2009 geschäftsführender Alleingesellschafter der Synkel-Versicherung GmbH  FN 999999z mit Sitz in Wien, zu deren Geschäftsgegenstand u.a. die Montage von Fenstern  und Türen und der Innenausbau gehörte.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_153`)


In der Folge wurde der Sitz der Synkel-Versicherung GmbH in das Umland von X-Stadt verlegt (AP-Akt OZ 27a).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_154`)


Ein Jahr später, unmittelbar nach Einreichung des Jahresabschlusses (JA) 2008 der Synkel-Versicherung GmbH im  Firmenbuch (FB), eröffnete das LGZ Graz am 21.Okt.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_156`)


2010 das Konkursverfahren über das Vermögen der Synkel-Versicherung GmbH  Nach  Konkursaufhebung mangels kostendeckenden Vermögens und zwei geringfügigen  Nachtragsverteilungen erfolgte am 18.Juli 2012 die amtswegige Löschung der Synkel-Versicherung GmbH im  Firmenbuch (Quelle: FB FN 999999z, abgabenbehördl.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_158`)


Bereits lange vor Gründung der Synkel-Versicherung GmbH betrieb der Bf den Handel mit und die Montage von  Fenstern und Türen, ab Juni 2005 als Komplementär einer KEG (FN 999996x, nachfolgend  L-KEG;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_160`)


Obwohl nicht formelle Rechtsvorgängerin der Synkel-Versicherung GmbH  wird die L-KEG im  GmbH-Abtretungsvertrag vom 29.Okt.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_162`)


Der Abgabenbehörde gegenüber waren sowohl die L-KEG als auch die Synkel-Versicherung GmbH steuerlich  unvertreten, doch hatten beide Gesellschaften und auch deren Gesellschafter einem  gemeinsamen Buchhaltungsbetrieb Zustellvollmacht zum Empfang abgabenbehördlicher  Schriftstücke erteilt. Im verfahrensgegenständlichen AP- und Rechtsmittelverfahren schritt für  den Bf - bis zur bescheidmäßigen Untersagung gem. § 84 (1) BAO im Mai 2012 - eine neue  Bilanzbuchhaltungsgesellschaft (im Folgenden Schottmueller + Werntges Planung GmbH  ein.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Schottmueller + Werntges Planung GmbH` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_163`)


Die verfahrensgegenständliche AP fand während des Insolvenzverfahrens der Synkel-Versicherung GmbH statt  (Okt.2011-Febr.2012).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_177`)


erfassten  verdeckten Ausschüttungen (Scheinfirmen) ist allerdings dokumentiert, dass die  beanstandeten Rechnungen nach Abschluss der AP an die (in Konkurs befindliche)Synkel-Versicherung GmbH  retourniert wurden, „sodass mir keine Unterlagen mehr zur Verfügung stehen“ (AP-Akt OZ 4).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_178`)


Die externe AP-Ermittlungstätigkeit zu den verfahrensgegenständlichen Streitpunkten  beschränkte sich nach den vorgelegten Unterlagen - neben Firmenbuchabfragen - im  Wesentlichen auf die Anforderung der Kundenkonten der L-KEG und der Synkel-Versicherung GmbH bei der Fa A.- Fenster (AP-Bericht Tz.4/1.) und den Sachverhalt zu AP-Bericht Tz.4/2.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_183`)


Im nachgereichten AP-Akt befinden sich wenige Fragmente aus der Buchhaltung des geprüften  Unternehmens (einzelne Buchhaltungskonten der Synkel-Versicherung GmbH  nur vereinzelt zugehörige Belege).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_191`)


Da dieser Differenzbetrag zugeflossen sein muss, stellt dieser eine vGA dar.“  b) BFG-Sachverhaltsfeststellung:  Geschäftsgegenstand sowohl der L-KEG als auch der Synkel-Versicherung GmbH war die Montage von Fenstern  und Türen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_192`)


Die als faktische Nachfolgerin der L-KEG im März 2007 gegründete Synkel-Versicherung GmbH war nach dem  Verfahrensergebnis ab Juni 2007 operativ tätig (lt. GPLA-Bericht 16.März 2011: Lohnabgaben  ab Juni 2007; lt. AP-Akt Oz 29: Rechnungslegung ab 11.Juni 2007, beginnend mit  ReNr 001/2007;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_199`)


In den im AP-Verfahren von der Fa A.-Fenster zur L-KEG und der Synkel-Versicherung GmbH beigeschafften  Buchhaltungsunterlagen finden sich auf dem Kundenkonto der L-KEG bis Ende Mai 2007  Umsätze von rd. 44.300,- € (davon bezahlt rd 33.000,- €).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_202`)


Die Fa A.-Fenster bezahlte Rechnungen an die L-KEG (und auch später an die Synkel-Versicherung GmbH –  regelmäßig abzüglich Skonti sowie Haft-(HR)/Deckungsrücklässen (DR) - mittels elektron.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_205`)


auf das Kundenkonto der Synkel-Versicherung GmbH wurde das ausgeglichene Kundenkonto der L-KEG in der  Buchhaltung der Fa A.-Fenster am 27.Sept.2007 geschlossen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_206`)


Ein Kundenkonto für die Synkel-Versicherung GmbH war im Rechnungswesen der Fa A.-Fenster erst ab Sept.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_209`)


In der Folge wurde die  Geschäftsbeziehung der Fa A.-Fenster mit der Synkel-Versicherung GmbH buchhalterisch über dieses neue  Kundenkonto abgewickelt.  Abweichend vom Rechenwerk der Fa A.-Fenster scheinen in der Buchhaltung der Synkel-Versicherung GmbH auf  dem Konto „Erlöse für Bauleistungen § 19 UStG“ bereits ab 11.Juni 2007 Ausgangsrechnungen  (AR) mit fortlaufender ReNr ab 1/2007 auf, darunter auch jene Rechnungen, welche in der  Buchhaltung der Fa A.-Fenster bis 24.Aug.2007 auf dem Kundenkonto der L-KEG verbucht sind.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_210`)


Vor dem dargestellten Hintergrund geht das BFG davon aus, dass Letzteren Leistungen der Synkel-Versicherung GmbH zugrunde liegen und die zugehörigen Erlöse bei der Synkel-Versicherung GmbH versteuert wurden.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_211`)


Dem AP-Bericht ist nicht zu ersehen, dass bei der Synkel-Versicherung GmbH erfasste Erlöse aus AR des  3.Quartals 2007 an die Fa A.-Fenster im Zuge der AP aus den Besteuerungsgrundlagen 2007  ausgeschieden wurden.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_212`)


Einem Berechnungsentwurf im AP-Akt zur verdeckten Ausschüttung im Zusammenhang mit  der Fa A.-Fenster ist zu entnehmen, dass der Prüfer den Erlösen der L-KEG für 2007 auch jene  aus den bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem 3.Quartal 2007  zurechnete und den Gesamtbetrag als bezahlt behandelte (AP-Akt OZ 10).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_213`)


Dagegen entnahm  er die Erlöse der Synkel-Versicherung GmbH der Buchhaltung des geprüften Unternehmens (Kundenkonto A.- Fenster/ Kto K00100, AP-Akt OZ 29).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_214`)


Da der Gesamtbetrag der dort verbuchten AR - neben  diversen AR an den zweiten Hauptauftraggeber der Synkel-Versicherung GmbH– u.a. jene in der A.- Fenster-Buchhaltung bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem  3.Quartal 2007 enthielt, wurden in diesem Berechnungsentwurf im Ergebnis die von der Fa A.- Fenster buchhalterisch der L-KEG zugeordneten Rechnungen der Synkel-Versicherung GmbH aus dem Zeitraum  Juni – August 2007 bei beiden Gesellschaften zum Ansatz gebracht.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Synkel-Versicherung GmbH–` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_215`)


Während im Rechenwerk der Fa A.-Fenster die zugehörigen Zahlungen bei der L-KEG zum  Ausgleich des Kundenkontos führten, blieb in der Buchhaltung der Synkel-Versicherung GmbH per 31.12.2007 ein  Betrag von rd. 63.000,- € als offene Forderung gegen die Fa A.-Fenster offen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_216`)


Diesem stand in  der Buchhaltung der Fa A.-Fenster eine offene Verbindlichkeit gegenüber der Synkel-Versicherung GmbH von nur  rd. 13.400,- € gegenüber (resultierend aus umgebuchten HR/DR vom Kundenkonto der L-KEG  und der Geschäftsbeziehung mit der Synkel-Versicherung GmbH im 4.Quartal 2007).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_219`)


Das BFG hat aufgrund der festgestellten buchhalterischen Vorgänge bei der Fa A.-Fenster und  der Synkel-Versicherung GmbH keine Bedenken, das Rechtsmittelvorbringen des Bf insofern für zutreffend zu  erachten, als den im AP-Bericht unter Tz.4/1.) als verdeckte Ausschüttung zugerechneten  Beträgen die ersten Geschäfte der Synkel-Versicherung GmbH mit der Fa A.-Fenster zugrunde liegen, die im  Unternehmen der Auftraggeberin fälschlich noch der L-KEG als der bisherigen  Geschäftspartnerin zugeordnet worden waren.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_220`)


Obwohl keine Beweismittel zum Empfängerbankkonto vorliegen, rechtfertigen aus Sicht des  BFG unter den dargestellten Umständen die im Rechenwerk der Fa A.-Fenster verbuchten  ELBA-Zahlungen, die zum Ausgleich des Kundenkontos der L-KEG führten, iVm den offenen  Kundenforderungen in der Buchhaltung der Synkel-Versicherung GmbH den Schluss, dass die Fa A.-Fenster die  zugehörigen Überweisungen auf das bis dahin verwendete Bankkonto der L-KEG durchführte.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_221`)


Mit dem Eingang auf dem Bankkonto der L-KEG gelangten die Zahlungen der Fa A.-Fenster in  den Verfügungsbereich des Bf als vertretungsbefugten Komplementär der L-KEG und zugleich  geschäftsführender Alleingesellschafter der Synkel-Versicherung GmbH  Neben den Zahlungsvorgängen zu den oa.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_223`)


Weder das Kassakonto der Synkel-Versicherung GmbH noch das Verrechnungskonto des Bf befinden sich im  vorgelegten AP-Akt.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_224`)


In den Prüferaufzeichnungen ist vermerkt (AP-Akt OZ 13), dass bei der Synkel-Versicherung GmbH Kassaeinlagen  „in nicht geringem Ausmaß“ gegen das Verrechnungskonto des Bf gebucht wurden  (Verrechnungsverbindlichkeit der Synkel-Versicherung GmbH gegenüber dem Bf zum 31.12.2007 rd.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_227`)


Obwohl der Bf seine Anteile an der Synkel-Versicherung GmbH bereits zwei Jahre vor der AP veräußert hatte und  zudem bei der Synkel-Versicherung GmbH ein Insolvenzverfahren anhängig war, beschränkten sich die  AP-Erhebungen zur Klärung der Kassaeinlagen auf eine Aufforderung an den Bf zur Beibringung  der „Einzahlungsbelege“ bzw. der „entsprechenden Bankbehebungen (…) (Bankauszüge)“.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_229`)


Das Verfahrensergebnis bietet keinen Grund zur Annahme, dass die in Reaktion auf diesen  Vorhalt erstmals für den Bf einschreitende Schottmueller + Werntges Planung GmbH je mit der Buchhaltung der Synkel-Versicherung GmbH  befasst gewesen war.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Schottmueller + Werntges Planung GmbH` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_230`)


Dem Vorbringen der Schottmueller + Werntges Planung GmbH ist zu entnehmen, dass der Bf im Zeitpunkt der AP über keine  Buchhaltungsunterlagen der Synkel-Versicherung GmbH mehr verfügte (tel. RS 30.Nov.2011, AP-Akt OZ 9;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Schottmueller + Werntges Planung GmbH` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_234`)


Dem BFG erscheint dieser Einwand nach dem Verkauf der GmbH-Anteile und aufgrund des  laufenden Insolvenzverfahrens nachvollziehbar und zudem durch den Prüferhinweis auf die  Retournierung von AP-Unterlagen an die Synkel-Versicherung GmbH nach AP-Abschluss bestätigt (AP-Akt OZ 4).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_236`)


Auch Erhebungen im Wege des Erwerbers der GmbH-Anteile oder des  Masseverwalters der Synkel-Versicherung GmbH sind nicht dokumentiert, ebensowenig der Versuch, eine Klärung  durch eine AP bei der L-KEG herbeizuführen oder zumindest die bezughabenden  Buchhaltungsunterlagen der L-KEG anzufordern.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_239`)


Auch im nachgereichten AP-Akt fehlen für die Streitpunkte relevante Unterlagen, die dem  Prüfer offensichtlich zur Verfügung standen (so waren etwa für die Feststellungen betreffend  Kassaeinlagen das Kassakonto und das Verrechnungskonto des Bf aus der Buchhaltung der Synkel-Versicherung GmbH erforderlich).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_240`)


Zugleich fehlt die als Rechtsmittelbeilage eingereichte Stellungnahme des ehemaligen  Buchhalters der Synkel-Versicherung GmbH  der offenbar Unzulänglichkeiten bei der Verbuchung einräumte  (verabsäumte Umbuchungen), trotz Aufforderung des BFG nach § 266 (4) BAO.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_242`)


AP-Akt OZ 9) auch die Rückführung der von der Fa A.-Fenster  fälschlich auf das Bankkonto der L-KEG überwiesenen Zahlungen für Rechnungen der Synkel-Versicherung GmbH  durch den Bf als Geschäftsführer der Synkel-Versicherung GmbH enthielten.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_244`)


Auch die Unterlagen betreffend den Verkauf der Anteile an der Synkel-Versicherung GmbH aus dem Jahr 2009  erhärten die dargestellte Schlussfolgerung.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_246`)


Nach dem Inhalt des Anteilsabtretungsvertrages vom 29.Okt.2009 wurde die im JA 2008  ausgewiesene Forderung der Synkel-Versicherung GmbH gegen die Fa A.-Fenster um 45.700,- € vermindert  (AP-Akt OZ 27a).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_247`)


Einer vorangegangenen E-Mail-Kommunikation vom Juni 2009 zwischen dem Erwerber der  Anteile und dessen Buchhalterin ist zu entnehmen, dass für Forderungen an die Fa A.-Fenster  im Ausmaß von rd. 54.000,- €, deren Grundlage hauptsächlich Rechnungen der Synkel-Versicherung GmbH von  Juni/Juli 2007 waren, eine Bezahlung auf ein Bankkonto der L-KEG vermutet wurde (E-Mail  3.Juni 2009, AP-Akt OZ 28).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_248`)


Wenn einerseits in Punkt IV/b des Abtretungsvertrages festgehalten wird, dass die  Jahresabschlüsse der Gesellschaft zum 31.12.2007 und 31.12.2008 richtig und die im  Jahresabschluss zum 31.12.2008 ausgewiesenen Forderungen - abgesehen von der um  45.700,- € zu reduzierenden Forderung gegen die Fa A.-Fenster – „liquide und im vollen  Umfang werthaltig“ sind und anderseits im Zuge der verfahrensgegenständlichen AP in der  Bilanz 2008 die gewinnneutrale Erfassung eines Betrages von 55.000,- € als „sonstige  Verbindlichkeit“ ohne nachvollziehbare Unterlagen sowie zum 30.April 2009 die Ausbuchung  einer Verrechnungsverbindlichkeit der Synkel-Versicherung GmbH gegen den Bf im Umfang von 50.000,- € bei  gleichzeitiger Reduktion des „fiktiven“ Kassastandes festgestellt wurde (AP-Vorhalt  28.Nov.2011, AP-Akt OZ 9;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_250`)


BE Pkt II/5.), so erachtet es das BFG vor  dem Hintergrund der dargestellten Sachverhaltsfeststellungen auch jenseits der Rechtsfolgen  des § 266 Abs. 4 BAO als erwiesen, dass der Bf die von der Fa A.-Fenster fälschlich auf das  Bankkonto der L-KEG überwiesenen Beträge bereits im Jahr 2007 – verbucht als Kassaeinlagen  - wieder an die Rechnung legende Synkel-Versicherung GmbH rückführte (wo sie im Übrigen auch versteuert  wurden).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_251`)


Für die Annahme, dass der Bf die fraglichen Geldmittel-Zuführungen an die Synkel-Versicherung GmbH als deren  Gesellschafter (Kassaeinlage) und nicht in seiner Funktion als Geschäftsführer  (Forderungsinkasso) veranlasste, bietet das Verfahrensergebnis keine tragende Grundlage.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_252`)


Zusammenfassend geht das BFG davon aus, dass die dem Bf gemäß AP-Bericht Tz.4/1.)  zugerechnete verdeckte Ausschüttung auf Buchhaltungsdifferenzen zwischen der Synkel-Versicherung GmbH und  der Fa A.-Fenster betreffend AR der Synkel-Versicherung GmbH aus dem 3.Quartal 2007 zurückzuführen ist.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_254`)


Tatsächlich waren die betreffenden Erlöse jedoch der Synkel-Versicherung GmbH  zuzurechnen und wurden von dieser im Jahr 2007 auch versteuert.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_256`)


Geldzuführungen des Bf an die Synkel-Versicherung GmbH im Ausmaß von 78.700,- € im Zeitraum  März - Nov.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_260`)


Eine Reaktion der Synkel-Versicherung GmbH gegenüber der Fa A.-Fenster betreffend die offenen  Kundenforderungen ist nicht dokumentiert (keine Zahlungsaufforderungen o.ä.).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_262`)


Ende April 2009 erfolgte eine buchhalterische Berichtigung der Kassaeinlagen und zugleich  Reduktion des “fiktiven“ Kassenstandes bei der Synkel-Versicherung GmbH unter Ausbuchung der zugehörigen  Verrechnungsverbindlichkeiten gegenüber dem Bf.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_264`)


Dem Vorgang lagen  hauptsächlich Rechnungen der Synkel-Versicherung GmbH vom Juni/Juli 2007 zugrunde.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_265`)


c) Rechtliche Beurteilung:  Auf Basis der festgestellten Sach- und der dargestellten Rechtslage erweist sich die Zurechnung  einer verdeckten Ausschüttung an den Bf im Zusammenhang mit den im AP-Bericht Tz.4/1.)  erfassten Vorgängen betreffend die Fa A.-Fenster als nicht berechtigt, da insofern weder von  einer Vermögensverminderung bei der Synkel-Versicherung GmbH bzw. einer Bereicherung beim Bf auszugehen,  noch eine Zuwendungsabsicht der Synkel-Versicherung GmbH erwiesen ist.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_266`)


Vielmehr hält das BFG es - nicht nur aufgrund der Bestimmung des § 266 Abs. 4 BAO sondern  auch nach dem Ergebnis des finanzgerichtlichen Ermittlungsverfahrens -, dem  Beschwerdevorbringen folgend, für erwiesen, dass der angenommenen verdeckten  Ausschüttung tatsächlich im Wesentlichen eine fehlerhafte buchhalterische Darstellung im  Rechenwerk der Synkel-Versicherung GmbH zugrunde lag (Fehlerfassung von Zahlungseingängen als Kassaeinlage;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_268`)


Die Maßnahmen betreffend „Sonstige Verbindlichkeiten“ im Jahresabschluss 2008 der Synkel-Versicherung GmbH (beim FA eingereicht am 5.Mai 2009) bzw. die per 30.April 2009 durchgeführte buchhalterische  Berichtigung des Kassastandes und der Verrechnungsverbindlichkeiten gegenüber dem Bf  lassen iVm den Unterlagen zum Verkauf der GmbH-Anteile (Anteilsübergang per 30.Juni 2009)  darauf schließen, dass die unrichtige Verbuchung der Zahlungseingänge von der Fa A.-Fenster  als Kassaeinlagen erst bei der buchhalterischen Aufarbeitung im Vorfeld der Verhandlungen  zur Anteilsveräußerung (in deren Verlauf auch der Jahresabschluss 2008 erstellt wurde)  hervorkam und auf diese Weise berichtigt werden sollte.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_271`)


Rechenwerk der Synkel-Versicherung GmbH zur Abdeckung der Kundenforderung gegen die Fa A.-Fenster  umzubuchen gewesen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_275`)


Ertragswirksame Auswirkungen bei der Synkel-Versicherung GmbH hätten aus den genannten Maßnahmen nicht  resultiert.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_276`)


Auf Basis des als erwiesen angenommenen Sachverhalts trat somit im Zusammenhang mit den  unter Tz.4/1.) des AP-Berichts erfassten Vorgängen weder im Jahr 2007 noch später eine  Vermögensverminderung bei der Synkel-Versicherung GmbH oder eine Bereicherung des Bf ein.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_277`)


Da nach den vorliegenden Unterlagen die ersten Hinweise auf die überhöht ausgewiesene  offene Forderung der Synkel-Versicherung GmbH gegen die Fa A.-Fenster aus der Zeit der Vorbereitungen zur  GmbH-Anteilsveräußerung im Jahr 2009 stammen, lässt sich auch eine Bereicherungsabsicht  der Synkel-Versicherung GmbH zu Gunsten des Bf im Umfang der von der Fa A.-Fenster falsch veranlassten  Zahlungseingänge auf das Bankkonto der L-KEG vor dieser Zeit auf Grundlage des  Verfahrensergebnisses nicht schlüssig feststellen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_278`)


Die gewinnneutrale Einbuchung einer „Sonstigen Verbindlichkeit“ im Jahresabschluss 2008 und  die Reduktion der Verrechnungsverbindlichkeiten gegen den Bf bei gleichzeitiger  Verminderung der Kassaeinlagen - doch unverändert belassenem Stand der  Kundenforderungen - nach Entdeckung des Buchungsfehlers im April 2009, bieten ebenfalls  keine Stütze für die Feststellung einer beabsichtigten Zuwendung der betreffenden  Geldbeträge an den Bf. Tragfähige Anhaltspunkte anderer Art, die auf einen derartigen  Verzicht der Synkel-Versicherung GmbH gegenüber dem Bf schließen lassen, waren im Verfahren nicht  feststellbar.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_279`)


Für die Verwirklichung einer verdeckten Gewinnauswirkung fehlte es somit, neben einem  gewinnmindernden Vermögensabfluss bei der Synkel-Versicherung GmbH  auch am Nachweis der beabsichtigten  Zuwendung eines durch das Gesellschaftsverhältnis begründeten Vermögensvorteils an den Bf.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_288`)


c) Rechtliche Beurteilung:   Wie zur Feststellung in AP-Bericht Tz.4/1.) wendet der Bf im Rechtsmittel auch gegen die  Annahme einer verdeckten Ausschüttung zu AP-Bericht Tz.4/4.) – neben einer teilweisen  Doppelerfassung in den Buchhaltungen der Synkel-Versicherung GmbH und der Fa A.-Fenster - v.a. eine  verspätete Reaktion der Geschäftspartner auf den unterjährigen Wechsel von der L-KEG zur  L- GmbH ein.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_289`)


Die zu AP-Akt OZ 29 vorgelegten Fragmente aus der Buchhaltung der Synkel-Versicherung GmbH enthalten als  einzig in Frage kommendes Aufwandskonto das Wareneinsatzkonto mit verbuchten  Wareneingängen zum Zeitraum 21.Juni – 18.Sept.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_291`)


Aus Punkt II/1.) dieser Entscheidung ist bekannt, dass die Synkel-Versicherung GmbH in diesem Zeitraum bereits  sowohl über Personal als auch über Aufträge verfügte und Montagetätigkeiten ausführte.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_292`)


Die  unter Punkt II/1.) ausgeführten Feststellungen erhärten zudem die Rechtsmitteleinwendungen  zum gegenständlichen Streitpunkt sowohl betreffend Doppelerfassung als auch betreffend  Zuordenbarkeit zu Leistungen der Synkel-Versicherung GmbH  In Hinblick darauf und da Gegenteiliges durch die Verfahrensunterlagen nicht dargetan wird,  kann vom BFG nicht festgestellt werden, dass dem gegenständlichen Streitpunkt tatsächlich  Rechnungen über Lieferungen/Leistungen an die L-KEG zugrunde liegen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_293`)


Gemäß § 266 Abs. 4 BAO folgt das BFG unter diesen Umständen dem Rechtsmittelvorbringen  des Bf und geht von Rechnungen für Lieferungen/Leistungen an die Synkel-Versicherung GmbH aus.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_300`)


Die zugehörigen Buchhaltungsunterlagen der Synkel-Versicherung GmbH  insbesondere die Kundenkonten und  das Konto Schadensfälle, fehlen dagegen für den gesamten Prüfungszeitraum (ausgenommen  zwei Kundenkonten für 2008), obwohl die Betragsfeststellungen zu diesem Streitpunkt der  Buchhaltung der Synkel-Versicherung GmbH entnommen wurden (AP-Akt OZ 29;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_302`)


Nicht vorliegend ist auch eine „Aufstellung“ (offenbar der Schadenfälle), auf die  in den Buchhaltungsunterlagen der Synkel-Versicherung GmbH und den Prüferaufzeichnungen Bezug genommen  wird (AP-Akt OZ 29 bzw. OZ 13 u. OZ 24).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_313`)


Abgesehen von der Tatsache, dass in diesem Fall ein Zufluss an den Bf erst im Jahr 2009  anzunehmen wäre, ist in den Aufzeichnungen des Prüfers zu diesem Punkt eine „AR 84“  vermerkt, die nach der - dem BFG nicht vorliegenden - „Aufstellung“ von der Synkel-Versicherung GmbH als  Ausfall behandelt worden sein soll.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_314`)


Aufgrund der fehlenden Unterlagen ist weder feststellbar, welche AR der angenommenen  verdeckten Ausschüttung zu AP-Akt OZ 24/3.) tatsächlich zugrunde liegt, noch steht eine  Vereinnahmung des vom Prüfer anführten Betrages durch die Synkel-Versicherung GmbH oder den Bf fest.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_319`)


Da das BFG, mangels auswertbarer Verfahrensunterlagen, zu keinem der lt. AP-Bericht Tz.4/2.)  im Jahr 2008 „auf Konto Schadensfälle“ verbuchten Vorgänge eine Vereinnahmung durch die Synkel-Versicherung GmbH bzw. den Bf festzustellen vermag, fehlt es in Bezug auf den im AP-Bericht zu dieser  Textziffer erfassten Sachverhalt insgesamt an den Voraussetzungen für die Annahme einer  verdeckten Ausschüttung an den Bf.  Gemäß § 266 Abs. 4 BAO folgt das BFG unter diesen Umständen auch zu diesem Streitpunkt  dem Rechtsmittelvorbringen des Bf und geht davon aus, dass den im Rechenwerk 2008 der Synkel-Versicherung GmbH als Schadensfälle verbuchten Beträgen tatsächlich Einnahmenausfälle zugrunde  liegen, welche die Annahme einer verdeckten Ausschüttung und Vorschreibung einer darauf  entfallenden KeSt an den Bf nicht rechtfertigen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_322`)


2008 € 57.000,-  2009 € 35.000,-„  b) BFG-Sachverhaltsfeststellung/ rechtliche Beurteilung:  Vorweg ist festzuhalten, dass in den vorgelegten Verfahrensunterlagen keine Aufforderung zur  Empfängerbenennung nach § 162 BAO an die Synkel-Versicherung GmbH dokumentiert ist.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_324`)


Während des laufenden Insolvenzverfahrens der Synkel-Versicherung GmbH und zu einem Zeitpunkt als dem Bf  aufgrund des Verkaufs der GmbH-Anteile bereits seit mehr als zwei Jahren keine  Vertretungsbefugnis für die Synkel-Versicherung GmbH mehr zukam, erging in Bezug auf die Firmen POU Bau GmbH  und Y Montage GmbH die Aufforderung an den Bf, zur Vorlage der „Arbeitsaufträge an die L- GmbH“ sowie detaillierter Leistungsverzeichnisse betreffend die beiden Bauvorhaben (BVH),  auf welche sich die Rechnungen der beiden Subauftragnehmer beziehen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `POU Bau GmbH` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_333`)


Eine Verifizierung an Hand der Buchhaltung der Synkel-Versicherung GmbH ist dem BFG nicht möglich, da trotz  finanzgerichtlicher Aufforderung zur Vorlage der abgabenbehördlichen  Verfahrensunterlagen, - abgesehen von den Erlöskonten für das 1.Halbjahr 2009 - keines der  betroffenen (und im AP-Verfahren offensichtlich vorhandenen) Buchhaltungskonten vorgelegt  wurde (weder Kassakonto oder Konto Sonstige Verbindlichkeiten noch die Konten  Fremdleistungen und PRAP Fremdleistungen).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_335`)


Für die Zeit nach dem Übergang der Gesellschaftsanteile auf  den Rechtsnachfolger des Bf am 30.Juni 2009 liegen keine Erlöskonten der Synkel-Versicherung GmbH vor (AP-Akt  OZ 29).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_337`)


Faktum ist, dass bei der im AP-Bericht dargestellten Vorgangsweise der Gewinn des  Jahres 2008 der Synkel-Versicherung GmbH nur um den Differenzbetrag von 2.000,- € vermindert wurde.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_339`)


In diesem Zusammenhang ist daran zu erinnern, dass die Abgabenerklärungen 2008 der Synkel-Versicherung GmbH Anfang Mai 2009 beim FA eingereicht wurden, somit im zeitlichen Zusammenhang mit  der (ebenfalls gewinnneutralen) Reduktion der Verrechnungsverbindlichkeiten gegenüber dem  Bf und des „fiktiven“ Kassastandes im Rechenwerk der Synkel-Versicherung GmbH per 30.April 2009 um  50.000,- € (AP-Bericht Tz.1/3.).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_344`)


und 2008 ausgewiesenen Verrechnungsverbindlichkeiten der Synkel-Versicherung GmbH gegenüber dem Bf  (rd. 66.600,- bzw. 56.500,- €) und der Hinweis auf die Reduktion eines „fiktiven“ Kassastandes  Ende April 2009 (AP-Bericht Tz.1/3.) unterstützen diese Beurteilung ebenso, wie die im  AP-Bericht dargestellte Art der Ausbuchung dieses Betrages im Jahr 2009.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_374`)


Erhebungen zur Klärung der Umstände der Geschäftsanbahnung und –abwicklung zwischen  der Synkel-Versicherung GmbH und der POU Bau GmbH sind den AP-Unterlagen nicht zu entnehmen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `POU Bau GmbH` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_375`)


Wie festgestellt, unterblieb nach den Verfahrensunterlagen im AP-Verfahren eine  Unterlagenanforderung sowohl beim Masseverwalter als auch beim Rechtsnachfolger des Bf in  der Synkel-Versicherung GmbH gänzlich.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_376`)


Der Bf blieb die ihm zu den abgerechneten Leistungen der POU Bau GmbH allein aufgetragene  Vorlage der Arbeitsaufträge an die Synkel-Versicherung GmbH samt Leistungsverzeichnissen schuldig.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `POU Bau GmbH` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_377`)


Bezüglich  der im AP-Akt ebenfalls fehlenden Rechnungen der Synkel-Versicherung GmbH an ihre Auftraggeber sowie der  Arbeitsaufträge und Leistungsverzeichnisse zu den beanstandeten Rechnungen der POU Bau GmbH erging kein Auftrag an den Bf.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `POU Bau GmbH` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_378`)


Nach dem Inhalt der Mail vom 12.März 2012 an die Schottmueller + Werntges Planung GmbH (AP-Akt OZ 4), verfügte der  Prüfer im AP-Verfahren zu diesem Streitpunkt lediglich über die im vorgelegten AP-Akt  befindlichen fünf „Schlussrechnungen“ der POU Bau GmbH an die Synkel-Versicherung GmbH aus dem Zeitraum  20.Mai - 3.Dez.2008 (Leistungszeitraum 4-11/2008) mit dem Leistungsinhalt  „Trockenbauarbeiten in Pauschale“ samt zugeordneten Barzahlungsbelegen sowie einen  25 von 32 Seite 26 von 32

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Schottmueller + Werntges Planung GmbH` (organisation)
- `POU Bau GmbH` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_379`)


Werkvertrag vom 23.März 2008 zwischen der Synkel-Versicherung GmbH und der POU Bau GmbH  dessen  Unterfertigung von der FB-Musterzeichnung der POU Bau GmbH deutlich abweicht.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `POU Bau GmbH` (organisation)
- `POU Bau GmbH` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_381`)


Da weder die Geldkonten noch das Konto Fremdleistungen der Synkel-Versicherung GmbH zum Jahr 2008  vorliegen, sind die näheren Umstände der Verbuchung und insbesondere auch der  Zahlungsvorgänge für das BFG nicht feststellbar (Zeitpunkt der Rechnungsverbuchung;

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_383`)


Feststellbar ist in den vorliegenden Erlöskonten der Synkel-Versicherung GmbH allerdings, dass die Synkel-Versicherung GmbH von  Febr. – Dez 2008 laufend Bauleistungen für eine Fa ABC erbrachte und vereinzelt auch im  Jahr 2009 für dieses Unternehmen tätig war (lt. Rechtsmittel Fa Zimmerei Groschang Holz GmbH (nachfolgend Groschang Holz GmbH.  1.2.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Groschang Holz GmbH` (organisation)
- `Groschang Holz GmbH.` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_395`)


Wie festgestellt, beruht die abgabenbehördliche Nichtanerkennung des strittigen  Fremdleistungsaufwandes der Synkel-Versicherung GmbH nicht auf einem Ermittlungsverfahren nach § 162 BAO.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_396`)


Da die Aufforderung zur Nachreichung von zugehörigen Unterlagen im AP-Verfahren nicht an  den MV als den gesetzlichen Vertreter der insolventen Synkel-Versicherung GmbH bzw. an die von diesem  beauftragte, steuerliche Vertretung erging, kommt auch § 138 BAO als Rechtsgrundlage nicht  zum Tragen.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_400`)


In Hinblick auf das Ausscheiden des Bf aus der Synkel-Versicherung GmbH zwei Jahre vor der  Unterlagenanforderung im AP-Verfahren und vor dem Hintergrund des laufenden  Insolvenzverfahrens erscheint es umso weniger vertretbar, die Kürzung des  Fremdleistungsaufwandes auf das Fehlen der ausschließlich beim Bf angeforderten  Arbeitsaufträge der Synkel-Versicherung GmbH und Leistungsverzeichnisse zu stützen (die Anforderung von  „Baubeschreibungen“ ist nicht dokumentiert).

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_403`)


Ermittlungen durch das FA, darunter auch die in der Beschwerde angeregte Erhebung beim  Auftraggeber der Synkel-Versicherung GmbH  der Groschang Holz GmbH   Nach dem Rechtsmittelvorbringen, auf das sich das BFG gem. § 266 (4) BAO stützt  (entsprechend erübrigt sich die angeregte Befragung des damaligen Auftraggebers), betraf der  im AP-Verfahren nicht anerkannte Fremdleistungsaufwand zwei Bauvorhaben (BVH) der Groschang Holz GmbH  auf welchen die POU Bau GmbH im Jahr 2008 als „aktuelle und aktive“  Subunternehmerin der Synkel-Versicherung GmbH tätig war.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Groschang Holz GmbH` (organisation)
- `BFG` (organisation)
- `Groschang Holz GmbH` (organisation)
- `POU Bau GmbH` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_404`)


Laufende Leistungen der Synkel-Versicherung GmbH für die Groschang Holz GmbH im Jahr 2008 werden durch die  vorgelegten Buchhaltungsfragmente (Erlöskonto Bauleistungen § 19 UStG) bestätigt.

| Predicted | Gold |
|---|---|
| `Synkel-Versicherung GmbH` | `Synkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Groschang Holz GmbH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rabel & Partner GmbH` — partial — pred is substring of gold: `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alois Pichler`(person)
- `Donald Paulovits`(person)
- `Tröbach 41, 9130 Leibsdorf, Österreich`(address)
- `Mag. Achmed Ghazal Aswad`(person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `95-720/4312`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_174`)


Mit Schreiben vom 25.2.2020 wurde an DI Zeuge2 eine schriftliche Zeugeneinvernahme zum  Beweisthema AfA-Satz von 3% für die auf der Liegenschaft EZGST bestehenden Gebäude laut  den Schreiben an die Alwerkmon-Pharma  GmbH vom 14.11.2011 und vom 29.2.2012 versendet.

**False Positives:**

- `Alwerkmon-Pharma  GmbH` — partial — gold is substring of pred: `Alwerkmon-Pharma`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alwerkmon-Pharma`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Hermann Bloehdorn, Bierbaum 35, 8983 Bad Mitterndorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerden vom 9. und 13. Jänner 2014 sowie vom 25. September 2015 und vom 20.  Oktober 2017 gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt  Österreich) vom 6. Dezember 2013, sowie vom 26. August 2015 und vom 11. September 2017  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 bis 2014, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Alpen-Treuhand GmbH` — partial — pred is substring of gold: `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Hermann Bloehdorn`(person)
- `Bierbaum 35, 8983 Bad Mitterndorf, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_214`)


Da der Gesamtbetrag der dort verbuchten AR - neben  diversen AR an den zweiten Hauptauftraggeber der Synkel-Versicherung GmbH– u.a. jene in der A.- Fenster-Buchhaltung bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem  3.Quartal 2007 enthielt, wurden in diesem Berechnungsentwurf im Ergebnis die von der Fa A.- Fenster buchhalterisch der L-KEG zugeordneten Rechnungen der Synkel-Versicherung GmbH aus dem Zeitraum  Juni – August 2007 bei beiden Gesellschaften zum Ansatz gebracht.

**False Positives:**

- `Synkel-Versicherung GmbH` — similar text (different position): `Synkel-Versicherung GmbH–`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH–`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_330`)


Der verbleibende PRAP-Restbetrag von 20.000,- € soll aufgrund  der fehlenden Rechnung nach der Übernahme der Synkel-Versicherung GmbH- somit vom Rechtsnachfolger des  Bf in der Synkel-Versicherung GmbH- als Erlös aus Bauleistungen behandelt worden sein (AP-Bericht Tz.2/5.; AP- Akt OZ 13).

**False Positives:**

- `Synkel-Versicherung GmbH` — partial — pred is substring of gold: `Synkel-Versicherung GmbH-`
- `Synkel-Versicherung GmbH` — similar text (different position): `Synkel-Versicherung GmbH-`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH-`(organisation)
- `Synkel-Versicherung GmbH-`(organisation)

</details>

---

## `Magistrat_Wien` 🏆

**F1:** 0.039 | **Precision:** 0.861 | **Recall:** 0.020  

**Format:** `regex`  
**Rule ID:** `b3f6167e`  
**Description:**
Matches the Magistrat der Stadt Wien.

**Content:**
```
\bMagistrat\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.861 | 0.020 | 0.039 | 425 | 366 | 59 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 366 | 59 | 17777 |

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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_6`)


Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft (§ 2 Wiener Parkometergesetz 2006) mit Strafverfügung  vom 18. Dezember 2019, MA 67/123/2019, angelastet, er habe das Fahrzeug am 11. Oktober  2019 um 13:54 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Theodor-Sickel- Gasse ggü 14, ohne einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_25`)


Der Magistrat der Stadt Wien wies in der Folge den Einspruch des Bf. vom 11. Jänner 2020  gegen die Strafverfügung vom 18. Dezember 2019 mit Bescheid vom 4. März 2020 gemäß § 49  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_38`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Mai 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_23`)


Der Magistrat der Stadt Wien lastete der Bf. mit zwei Straferkenntnissen, beide vom  25.02.2020, die bereits näher bezeichneten Verwaltungsübertretungen an und verhängte  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung  iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 jeweils eine Geldstrafe von € 60,00 und für den  Fall der Uneinbringlichkeit jeweils eine Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_48`)


Der Magistrat der Stadt Wien legte die Beschwerden samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_11`)


Wegen Verletzung des § 2 Wiener Parkometergesetz 2006 verhängte der Magistrat der Stadt  Wien gemäß § 4 Abs. 2 Wiener Parkometergesetz 2006 über den Bf. jeweils eine Geldstrafe in  Höhe von 60,00 Euro (Ersatzfreiheitsstrafe: jeweils 14 Stunden) und schrieb gemäß § 64 VStG  jeweils einen Beitrag zu den Kosten des Strafverfahrens von 10,00 Euro vor, womit sich der zu  zahlende Gesamtbetrag auf jeweils 70,00 Euro belief.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_101`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_5`)


Die Geldstrafe von € 36,00 ist zusammen mit dem Beitrag zu den Kosten des Strafverfahrens  (§ 64 Abs. 1 und 2 VStG) von € 10,00, insgesamt somit € 46,00, binnen zwei Wochen ab  Zustellung des Straferkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete der Beschwerdefüherin (Bf.) unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31.10.2019 an, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 02.09.2019 um 14:43 Uhr in der  gebührenpflichtigen Kurzparkzone in 1140 Wien, Penzinger Straße 157, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt.  Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1  Wiener Parkometergesetz 2006 wurde über die Bf. eine Geldstrafe iHv € 60,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_17`)


Der Magistrat der Stadt Wien erkannte die Bf. mit Straferkenntnis vom 26.11.2019 wegen der  bereits näher bezeichnete Verwaltungsübertretung für schuldig und verhängte wegen  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_39`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 17.12.2019).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_108`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_6`)


Im Straferkenntnis vom 9. März 2020 warf der Magistrat der Stadt Wien dem Beschwerde- führer (Bf.) vor, er habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das  mehrspurige Kraftfahrzeug mit dem im Straferkenntnis näher bezeichneten behördlichen  Kennzeichen am 14. November 2019 um 14:51 Uhr in einer gebührenpflichtigen Kurzparkzone  abgestellt habe, ohne einen gültigen Fahrschein in das Fahrzeug zu legen oder einen elektroni- schen Parkschein zu aktivieren.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_11`)


Der Magistrat der Stadt Wien legte seiner Entscheidung die Anzeige vom 14. November 2019,  die Lenkerauskunft der Zulassungsbesitzerin und den Einspruch des Bf. gegen die an die Zulas- sungsbesitzerin adressierte Anonymverfügung zugrunde, worin der Bf. angegeben habe, dass  er zwischen 14:00 Uhr und 16:00 Uhr zwei Mal kurz und weniger als 10 Minuten in diesem  Areal zwar gehalten aber das Fahrzeug nicht abgestellt habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_13`)


Zu diesem Vorbringen stelle der Magistrat der Stadt Wien fest, dass der Meldungsleger wählen  könne, ob er eine Organstrafverfügung ausstelle oder eine Anzeige erstatte.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_30`)


3.3. Im Einspruch vom 07. Jänner 2020 gegen die als „Verfügung“ bezeichnete Lenkererhe- bung vom 20. Dezember 2019 gab der Bf. an, dass er „dort“ nicht geparkt habe und wies da- rauf hin, dass dem Magistrat der Stadt Wien seine Daten bekannt seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_33`)


3.5. Am 15. Jänner 2020 sandte der Bf. folgende Mail an den Magistrat der Stadt Wien: „Hier- mit beeinspruche ich die Verfügung vom 20.12.2019: Habe ich dort nicht geparkt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_39`)


B. Der Entscheidung wird folgende aus den Verwaltungsakten sich ergebende Sachlage zu- grunde gelegt: Im Straferkenntnis vom 9. März 2020 hat der Magistrat der Stadt Wien dem Bf.  eine Verwaltungsübertretung vorgeworfen, die er ihm auch in der Strafverfügung vom 08.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_7`)


Die Geldstrafe von € 48,00 ist gemeinsam mit den Kosten des Verwaltungsstrafverfahrens  (€ 10,00), insgesamt somit € 58,00 binnen zwei Wochen nach Zustellung dieses  Straferkenntnisses an den Magistrat der Stadt Wien zu bezahlen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_8`)


Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_15`)


Mit Strafverfügung vom 4. August 2020 wurde Bf1 (Beschwerdeführer, kurz Bf.) vom Magistrat  der Stadt Wien, Magistratsabteilung 67, angelastet, er habe das verfahrensgegenständliche  Fahrzeug am 5. Juni 2020 um 14:14 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Taborstraße 21a ggü, abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_27`)


Mit Straferkenntnis vom 25. August 2020 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung und wegen Verletzung des § 5  Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006  eine Geldstrafe von € 60,00 und für den Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von  14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Franz Trockenbrot,  Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich  vom 15. März 2020, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 10. März 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 9 Abs. 2 Wiener  Kontrolleinrichtungenverordnung iVm § 4 Abs. 3 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 30. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Erkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Trockenbrot` (person)
- `Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_3`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (€ 12,00) ist gemeinsam mit der  Geldstrafe (€ 60,00) und dem Beitrag zu den Kosten der belangten Behörde (€ 10,00) binnen  zwei Wochen ab Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_5`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_23`)


Mit Strafverfügung vom 12. Februar 2020 lastete der Magistrat der Stadt Wien dem Bf. an, er  habe das verfahrensgegenständliche Fahrzeug am 12. Dezember 2019 um 14:52 Uhr in der  gebührenpflichtigen Kurzparkzone in 1110 Wien, Simmeringer Hauptstraße 59 - 61, abgestellt,  wobei elektronische Parkscheine mit einer fünfzehn Minuten nicht übersteigenden Abstellzeit  unmittelbar aufeinander folgend aktiviert worden seien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_31`)


Mit Straferkenntnis vom 10. März 2020 wurde dem Bf. vom Magistrat der Stadt Wien die  bereits näher bezeichnete Verwaltungsübertretung angelastet und wegen Verletzung der  Rechtsvorschriften des § 9 Abs. 2 Wiener Kontrolleinrichtungenverordnung iVm § 4 Abs. 3  Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_63`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 23. April 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_242`)


Hier erweist sich die Bestimmung des Magistrat der Stadt Wien als Vollstreckungsbehörde als  zweckmäßig, da dem Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die  Vollstreckung der von den (anderen) Verwaltungsgerichten erlassenen Erkenntnissen und  Beschlüssen obliegt (vgl. für viele ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_6`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) folgende, die Verwaltungsstrafsache  MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich möchte  Ihnen mitteilen, dass am 24.10.2019 das Fahrzeug … folgende Person gelenkt hat: …“  Über eine am 24.10.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 30.12.2019 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  1 von 4 Seite 2 von 4

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_10`)


Mit Vollstreckungsverfügung vom 10.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 30.12.2019 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_13`)


Am 19.06.2020 sandte die Beschwerdeführerin (Bf.) auch folgende, die Verwaltungsstrafsa- che MA67/196701166656/2019 betreffende, Mail an den Magistrat der Stadt Wien: „Ich  möchte Ihnen mitteilen, dass ich am 06.10.2020 bereits Einspruch mittels E-Mail auf die Straf- verfügung erhoben habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_14`)


Das Fahrzeug … hat am 21.11.2019 folgende Person gelenkt: …“  Über eine am 21.11.2019 begangene Verwaltungsübertretung hatte der Magistrat der Stadt  Wien folgende Entscheidungen getroffen:  In der Strafverfügung vom 20.01.2020 warf der Magistrat der Stadt Wien der Bf. vor, sie habe  die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass sie das mehrspurige Kraftfahr- zeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen am  21.11.2019 um 17:49 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt habe, ohne für  seine Kennzeichnung mit einem richtig entwerteten Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_18`)


Mit Vollstreckungsverfügung vom 11.04.2020 stellte der Magistrat der Stadt Wien erstens  fest, dass die Bf. die mit der Strafverfügung vom 20.01.2020 verhängte Geldstrafe (EUR 60,00)  nicht bezahlt hatte, weshalb die offene Forderung inklusive Mahngebühr (EUR 5,00) in Summe  EUR 65,00 betrage und verfügte zweitens, diese EUR 65,00 zwangszuvollstrecken.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_5`)


III. Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_6`)


Die Geldstrafe von € 48,00 ist gemeinsam mit dem Beitrag zu den Kosten der belangten  Behörde von € 10,00 (§ 64 VStG 1991), insgesamt somit € 58,00, binnen zwei Wochen nach  Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67, erkannte den Beschwerdeführer (Bf.) mit  Straferkenntnis vom 18. Juni 2020, MA67/000/2020, für schuldig, das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 3. Jänner 2020 um 21:37 Uhr in  der gebührenpflichtigen Kurzparkzone in 1010 Wien, Bellariastraße 8, Nebenfahrbahn, ohne  einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_62`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 13. August 2020,  MA67/206700430919/2020, angelastet, sie habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 20. Mai 2020 in der gebührenpflichtigen Kurzparkzone in  1110 Wien, Simmeringer Hauptstraße 152, ohne einem für den Beanstandungszeitpunkt 15:11  Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_6`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_83`)


Die Strafe wurde daher nicht ordnungsgemäß bezahlt. In der Folge leitete der Magistrat der  Stadt Wien mit der Strafverfügung vom 19.08.2020 das ordentliche Verwaltungsstrafverfahren  ein, welches letztlich zur verfahrensgegenständlichen Beschwerde gegen das o.a.  Straferkenntnis führte.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_116`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Samuel Hegenbart` (person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_4`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_23`)


Mit Straferkenntnis vom 8. Jänner 2021 wurde der Bf. vom Magistrat der Stadt Wien wegen  der bereits näher bezeichnete Verwaltungsübertretung für schuldig befunden und wegen der  Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm  § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe iHv € 140,00 und für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 1 Tag und 9 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_50`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsstrafakt dem Bundes- finanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Jänner 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_114`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_5`)


Der am 10. November 2020 beim Magistrat der Stadt Wien eingelangte Einspruch gegen diese  Strafverfügung wurde gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_36`)


Der Einspruch gegen die verfahrensgegenständliche Strafverfügung langte am 10. November  2020 beim Magistrat der Stadt Wien ein und wurde von diesem zu Recht als verspätet  3 von 4 Seite 4 von 4

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_36`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 24. März 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_13`)


Mit Straferkenntnis vom 6. April 2021 wurde die Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe verhängt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_111`)


II.4. Bauvorhaben „2“  Die Bf. beteiligte sich als Mitglied einer Bietergemeinschaft (in der Folge kurz: BIEGE) an der  vom Magistrat der Stadt Wien (Magistratsabteilung 31, Wiener Wasser; in der Folge kurz: MA  31) als Auftraggeberin im offenen Verfahren durchgeführten Ausschreibung von Erd- und  Baumeisterarbeiten das Projekt „Ersatzstollen Neubrucker 2 Umgebung 3270 Scheibbs“  (Projektnummer MA 31-177525/12), durch Legung eines Angebotes am 29.01.2014.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_152`)


Am 09.12.2015 erfolgte an Ort und Stelle die mängelfreie Abnahme der  Innenschalenoberfläche zwischen der (nunmehrigen) ARGE und dem Magistrat der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_155`)


Die gesamten ausschreibungsgegenständlichen Erd- und Baumeisterarbeiten wurden am  31.05.2016 vom Magistrat der Stadt Wien übernommen;

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_8`)


In der Folge wurde Gundula Doerfner  vom Magistrat der Stadt Wien, MA 67, mit Strafverfügung vom  23. April 2021 angelastet, dass er das in Rede stehende Fahrzeug an der bereits genannten  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Gundula Doerfner` (person)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_13`)


Mit Straferkenntnis vom 7. Mai 2021 wurde Gundula Doerfner  vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 140,00 und für den Fall der Un- einbringlichkeit 1 Tag und 9 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Gundula Doerfner` (person)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete dem Beschwerdeführer (Bf.) mit Strafverfügung  vom 31. März 2021 an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kenn- zeichen Vienna am 1. Februar 2021 in der gebührenpflichtigen Kurzparkzone in 1180 Wien,  Hofmanngasse 1, ohne einen für den Beanstandungszeitpunkt 13:23 Uhr gültigen Parkschein  abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_117`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_4`)


Der zu zahlende Gesamtbetrag von € 82,00, bestehend aus der Geldstrafe (€ 60,00), dem  Beitrag zu den Kosten des Verwaltungsverfahrens (€ 10,00) und den Kosten des  Beschwerdeverfahrens (€ 12,00) ist gemäß § 52 Abs. 6 VwGVG in Verbindung mit § 54b Abs. 1  VStG binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_81`)


Der Magistrat der Stadt Wien legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 2. Juni 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_108`)


Der festgestellte Sachverhalt ergibt sich aus dem vom Magistrat der Stadt Wien übermittelten  Akt sowie den Angaben der Bf.  Rechtsgrundlagen und Würdigung:  Gemäß § 1 Wiener Parkometerabgabeverordnung ist für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen (§ 25 StVO 1960) eine Abgabe zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_182`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_25`)


Mit Straferkenntnis vom 7. Juli 2021 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig erkannt und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_116`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_7`)


Die Geldstrafe von je € 20,00 ist gemeinsam mit dem Beitrag zu den Kosten der belangten  Behörde von je € 10,00 (§ 64 VStG 1991), insgesamt somit € 120,00, binnen zwei Wochen  nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_8`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_17`)


Am 29.10.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte  Behörde die beschwerdegegenständliche Vollstreckungsverfügung, GZ. MA67/Zahl/2020, da  die mit obigem Straferkenntnis verhängte rechtskräftige Strafe bislang nicht bezahlt worden  sei, weshalb zur Einbringung des festgesetzten Gesamtbetrages in Höhe von € 75,00 (inkl. €  5,00 Mahngebühren) gemäß den §§ 3 und 10 Verwaltungsvollstreckungsgesetz 1991 (VVG) die  Zwangsvollstreckung verfügt wurde.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_5`)


Am 11.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700867324/2019, da die mit GZ.  MA67/196700867324/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  1 von 5 Seite 2 von 5

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_9`)


Am 11.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700891928/2019, da die mit GZ.  MA67/196700891928/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  Verwaltungsvollstreckungsgesetz 1991 (VVG) und § 10 VVG die Zwangsvollstreckung verfügt  wurde.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_12`)


Am 14.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700890302/2019, da die mit GZ.   MA67/196700890302/2019 rechtskräftig verhängte Strafe bislang nicht bezahlt worden sei,  weshalb zur Einbringung des festgesetzten Gesamtbetrages i.H. von € 65.- gem. § 3  Verwaltungsvollstreckungsgesetz 1991 (VVG) und § 10 VVG die Zwangsvollstreckung verfügt  wurde.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_15`)


Am 25.1.2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, als belangte Behörde  die Vollstreckungsverfügung GZ. MA67/196700930712/2019, da die mit GZ.  2 von 5 Seite 3 von 5

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_9`)


Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) lastete dem Beschwerdeführer  (Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüber- wachung der Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit  Strafverfügung vom 17. August 2020, Zahl, an, er habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 28. April 2020 in der gebührenpflichtigen Kurzparkzone  in 1030 Wien, Landstraßer Hauptstraße 136, ohne einem für den Beanstandungszeitpunkt  19:40 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig  verkürzt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133286.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133286.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten eines Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 8. März 2021 an, sie habe das mehr- spurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 8. Jänner 2021 in der  gebührenpflichtigen Kurzparkzone in 1020 Wien, Rustenschacherallee 44-56, ohne einen für  den Beanstandungszeitpunkt 10:18 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_38`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, hat das Schreiben der Fa.West Altrader GmbH vom  17. Mai 2021 als Beschwerde gegen das an Gundula Doerfner  als Beschuldigten ergangene  Straferkenntnis vom 7. Mai 2021 gewertet und dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `West Altrader GmbH`(0)
- `Gundula Doerfner`(person)
- `Bundesfinanzgericht`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Olivia Gassner, Schafberggasse 104, 9654 Wiesen, Österreich, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 67, als Abgabenstrafbehörde vom 22. April 2021, Zahl MA67/Zahl/2021,  wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, nach  Durchführung einer mündlichen Verhandlung am 04. August 2021, im Beisein des  Schriftführers AD SF, zu Recht erkannt:    I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Olivia Gassner`(person)
- `Schafberggasse 104, 9654 Wiesen, Österreich`(address)
- `Magistrat der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133971.1_99`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte den Bf. mit Schreiben vom  11. Jänner 2021 zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/134187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134187.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach eingeholter Lenkerauskunft mit Strafverfügung vom 19.  März 2021 an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen  Vienna am 17. Dezember 2020 in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Brehmstraße 16, ohne einen für den Beanstandungszeitpunkt 11:23 Uhr gültigen Parkschein  abgestellt, da sich im Fahrzeug der Parkschein Nr. 123 (Fünfzehn-Minuten-Parkschein) mit den  Entwertungen 10:40 Uhr befand und die Parkzeitzeit somit überschritten worden sei.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_41`)


Mit Straferkenntnis vom 24. August 2021, Z3, wurde der Bf. vom Magistrat der Stadt Wien,  Magistratsabteilung 67, für schuldig befunden, das in Rede stehende Fahrzeug am 7. Dezember  2020 in der gebührenpflichtigen Kurzparkzone in 1030 Wien, Marokkanergasse 18, ohne einen  für den Beanstandungszeitpunkt 12:32 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67`(organisation)

</details>

---

## `Law_Firm_Rechtsanwaelte_OG` 

**F1:** 0.000 | **Precision:** 0.500 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a5f09bd3`  
**Description:**
Matches law firms ending in 'Rechtsanwälte OG' with flexible name structures including hyphens and '&' or 'und'.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+)\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.000 | 0.000 | 6 | 3 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 3 | 18049 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corazza Kocholl Laimer Rechtsanwälte OG` | `Corazza Kocholl Laimer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer` (person)
- `Muran Waldhans, BEd` (person)
- `Am Tegel 5, 9831 Waben, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Imre & Schaffer Rechtsanwälte OG` | `Imre & Schaffer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Nadja Rossetto` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-716/2059` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142450.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142450.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin in der Beschwerdesache  Georgette Beinke, Hohe-Wand-Gasse 10, 9173 Trieblach, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG,  Ludersdorf 201, 8200 Gleisdorf, über die Beschwerde vom 3. September 2021 gegen die  Bescheide des Finanzamtes Österreich vom 24. August 2021 betreffend Anspruchszinsen  (§ 205 BAO) 2013, 2014 und 2016 sowie den Bescheid des Finanzamtes Österreich vom  25. August 2021 betreffend Anspruchszinsen (§ 205 BAO) 2015, Steuernummer**** zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Imre & Schaffer Rechtsanwälte OG` | `Imre & Schaffer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Georgette Beinke` (person)
- `Hohe-Wand-Gasse 10, 9173 Trieblach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Priv.-Doz.in Laetitia Pöstges, Krist 12, 3843 Riegers, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Achammer & Mennel Rechtsanwälte OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Priv.-Doz.in Laetitia Pöstges`(person)
- `Krist 12, 3843 Riegers, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141790.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141790.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Alana Gyßen, Kellergasse Kammern 20, 9161 Gaisach, Österreich, vertreten durch Hintermeier Brandstätter  Engelbrecht Rechtsanwälte OG, Andreas-Hofer-Straße 8, 3100 St. Pölten, über die Beschwerde  vom 10. April 2019 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 12. März 2019, Steuernummer 81-912/6532, betreffend Gebühren nach  Durchführung einer mündlichen Verhandlung zu Recht:   I. Der angefochtene Bescheid wird gemäß § 279 BAO dahingehend abgeändert, dass für  das beschwerdegegenständliche Rechtsgeschäft (Mietvertrag zwischen der  Beschwerdeführerin und der DZQF Versand GmbH vom 1. September 2017) die Gebühr gemäß § 33  TP 5 Abs. 1 Z 1 GebG ausgehend von den von der Bestandnehmerin zu erbringenden  Leistungen (Beträge in Euro) für  Mietzins (6.300 Euro / Jahr x 18) 113.400  Errichtungskosten lt Bekanntgabe inkl 20%

**False Positives:**

- `Engelbrecht Rechtsanwälte OG` — partial — pred is substring of gold: `Hintermeier Brandstätter  Engelbrecht Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Alana Gyßen`(person)
- `Kellergasse Kammern 20, 9161 Gaisach, Österreich`(address)
- `Hintermeier Brandstätter  Engelbrecht Rechtsanwälte OG`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `81-912/6532`(tax_number)
- `DZQF Versand GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142456.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Carla Jegers  in der Beschwerdesache Gisela Sramek,  Elsniggasse 69, 6364 Brixen im Thale, Österreich, vertreten durch ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG, Plüddemanngasse 87, 8010 Graz, betreffend Beschwerde vom 13. Juni  2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 2. Mai 2019   betreffend Zwangsstrafe gemäß § 111 BAO iVm §§ 5 und 16 WieREG   Steuernummer 18-269/6388  beschlossen:  Der Vorlageantrag wird gemäß § 262 Abs. 1 iVm § 264 Abs. 5 BAO als unzulässig  zurückgewiesen.

**False Positives:**

- `Huber-Erlenwein  Rechtsanwälte OG` — partial — pred is substring of gold: `ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Carla Jegers`(person)
- `Gisela Sramek`(person)
- `Elsniggasse 69, 6364 Brixen im Thale, Österreich`(address)
- `ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamt  Österreich`(organisation)
- `18-269/6388`(tax_number)

</details>

---

## `Law_Firm_OG_KG_GmbH` 💣

**F1:** 0.000 | **Precision:** 0.267 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ac276403`  
**Description:**
Matches law firms identified by suffixes OG, KG, or GmbH, allowing for slashes, hyphens, and 'und'/'&' in names, ensuring full name capture including 'GmbH & Co KG'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+|[A-Za-z]+(?:/[A-Za-z]+)+)\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft)\s+(?:OG|KG|GmbH|mbH|GmbH\s+&\s+Co\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.267 | 0.000 | 0.000 | 15 | 4 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 11 | 18154 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jank Weiler Operenyi Rechtsanwälte GmbH` | `Jank Weiler Operenyi Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Zeno Matyssek` (person)
- `Finanzamt für Gebühren` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/139038.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Mitglieder Mag. Elisabeth Traxler, Mag. Franz Gross und Mag. Gerd Wiehart in der  Beschwerdesache Olivia Meyerhöfer, Untermarktstraße 28A, 4715 Ragering, Österreich, vertreten durch Herbst Kinsky Rechtsanwälte  GmbH, Dr. Karl Lueger-Platz 5, 1010 Wien, über die Beschwerden vom 2. August 2018 gegen  die Bescheide des Finanzamtes Wien 1/23 vom 3. Juli 2018 betreffen Haftung zur Einbehaltung  und Abfuhr der Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds  für Familienbeihilfen für die Kalenderjahre 2012, 2013, 2014, 2015 und 2016 nach der am  18. Oktober 2022 durchgeführten mündlichen Verhandlung zu Recht erkannt:  Die angefochtenen Bescheide werden wie folgt abgeändert:  Lohnsteuer 2012: € 13.257,06 (bisher € 10.246,96)  Lohnsteuer 2013: € 10.467,93 (bisher € 11.559,76)  Lohnsteuer 2014: € 15.690,02 (bisher € 10.982,06)  Lohnsteuer 2015: € 16.143,78 (bisher € 10.416,39)  Lohnsteuer 2016: € 7.304,82 (bisher € 7.809,71)  Dienstgeberbeitrag 2012: Bemessungsgrundlage € 3.214.721,96 (bisher € 3.207.480,00),  Dienstgeberbeitrag € 144.662,49 (bisher € 144.336,60)  Dienstgeberbeitrag 2013: Bemessungsgrundlage € 3.620.052,21 (bisher € 3.622.388,44),  Dienstgeberbeitrag € 162.902,35 (bisher € 163.007,48)  Dienstgeberbeitrag 2014: Bemessungsgrundlage € 3.041.967,20 (bisher € 3.029.183,55),  Dienstgeberbeitrag € 136.888,52 (bisher € 136.313,26)  Dienstgeberbeitrag 2015: Bemessungsgrundlage € 3.081.592,83 (bisher € 3.059.469,77),  Dienstgeberbeitrag € 138.671,67 (bisher € 137.676,14)  Dienstgeberbeitrag 2016: Bemessungsgrundlage € 3.007.628,39 (bisher € 3.009.072,44),  Dienstgeberbeitrag € 135.343,27 (bisher € 135.408,26)  Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Herbst Kinsky Rechtsanwälte  GmbH` | `Herbst Kinsky Rechtsanwälte  GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Mag. Elisabeth Traxler` (person)
- `Mag. Franz Gross` (person)
- `Mag. Gerd Wiehart` (person)
- `Olivia Meyerhöfer` (person)
- `Untermarktstraße 28A, 4715 Ragering, Österreich` (address)
- `Dr. Karl` (person)
- `Finanzamtes Wien 1/23` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Brunhild Stanislav, Johann Hoffer-Weg 990, 8385 Neuhaus am Klausenbach, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` | `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Brunhild Stanislav` (person)
- `Johann Hoffer-Weg 990, 8385 Neuhaus am Klausenbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Clarissa Maak, Haidenweg 21, 5321 Koppl, Österreich, vertreten durch Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH, Gartenaugasse 3, 3500 Krems/Donau, über  die Beschwerde vom 28. Dezember 2020 gegen die Bescheide des Finanzamtes Hollabrunn  Korneuburg Tulln (nunmehr Finanzamt Österreich,   § 323b BAO) vom 30. November 2020 betreffend Wiederaufnahme der Verfahren  Einkommensteuer 2014 und 2015 gemäß § 303 BAO sowie betreffend Einkommensteuer 2014  und 2015 (Steuernummer 35-947/5347 ) nach Durchführung einer mündlichen  Verhandlung am 21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH` | `Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Mag. Monika Ahorn` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Dipl. Ing.  Thomas Hrdinka` (person)
- `Clarissa Maak` (person)
- `Haidenweg 21, 5321 Koppl, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-947/5347` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134395.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dario Berenz, Haller 74, 8444 Michlgleinz, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH,  Gauermanngasse 2-4, 1010 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich)  vom 25. Oktober 2018 betreffend Einkommensteuer 2016, Steuernummer 68-155/5685  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Dario Berenz`(person)
- `Haller 74, 8444 Michlgleinz, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)
- `Finanzamt Österreich`(organisation)
- `68-155/5685`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/138766.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138766.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Sophie Szcygiel  in der Beschwerdesache Veronika Krenzin, LLM,  Allramstraße 3, 3925 Dietrichsbach, Österreich, vertreten durch ARNOLD Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerden vom 14. Juni 2019 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel als Vorgängerorganisation des Finanzamts  Österreich, Dienststelle Sonderzuständigkeiten, vom 9. Mai 2019 betreffend   50 Säumniszuschläge für die Monate   Jänner 2014 bis Februar 2017 und Mai 2017 bis April 2018,  Steuernummer 33-539/1315  zu Recht erkannt:     I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `ARNOLD Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Sophie Szcygiel`(person)
- `Veronika Krenzin, LLM`(person)
- `Allramstraße 3, 3925 Dietrichsbach, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `Finanzamts  Österreich`(organisation)
- `33-539/1315`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/140274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140274.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Stephanie Stöfhas  in der Beschwerdesache Techn R Cedric Greuel, MBA,  Breitenschützing 2, 9651 Aigen, Österreich, vertreten durch DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger  Straße 2-4, 1090 Wien, über die Beschwerde vom 14. Februar 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Vorgängerorganisation des  Finanzamts Österreich Dienststelle Sonderzuständigkeiten vom 11. Jänner 2019 betreffend   Zahlungerserleichterungsansuchen für Glücksspielabgaben und Wettgebühren 2012  Steuernummer 93-237/4757  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `DSC Doralt Seist Csoklich Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Stephanie Stöfhas`(person)
- `Techn R Cedric Greuel, MBA`(person)
- `Breitenschützing 2, 9651 Aigen, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamts Österreich`(organisation)
- `93-237/4757`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Fabian Träubler, Dr.-Stumpf-Straße 18, 4720 Sumeding, Österreich, vertreten durch DORDA Rechtsanwälte GmbH,  Universitätsring 10, 1010 Wien, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr Finanzamt  Österreich) vom 19. April 2017 betreffend Gebühren 18.12.2015, Erf. Nr. ***, Steuernummer  ***, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `DORDA Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Fabian Träubler`(person)
- `Dr.-Stumpf-Straße 18, 4720 Sumeding, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/144019.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Theobald Steuder  in der Beschwerdesache Amy Benedict,  Otto-Probst-Platz 17, 4656 Wahl, Österreich, vertreten durch Pacher & Partner Rechtsanwälte GmbH & Co KG,  Kaiserfeldgasse 1/II/3.

**False Positives:**

- `Pacher & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Pacher & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Theobald Steuder`(person)
- `Amy Benedict`(person)
- `Otto-Probst-Platz 17, 4656 Wahl, Österreich`(address)
- `Pacher & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/144400.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Roswitha Augustiny  in der Beschwerdesache Miriam Hillger,  Marktsiedlung 44, 4924 Nußbaum am Kobernaußer Walde, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 14-958/5389, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Proksch Manak Kraft Rechtsanwälte  GmbH` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Roswitha Augustiny`(person)
- `Miriam Hillger`(person)
- `Marktsiedlung 44, 4924 Nußbaum am Kobernaußer Walde, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`(organisation)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `14-958/5389`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/145629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145629.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter[...] in der Beschwerdesache Ulrike Philippzig, Klimaweg 7, 8543 Graschach, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH,  Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 21.6.2024 gegen den Bescheid des  Finanzamtes für Großbetriebe vom 28.5.2024 mit dem der Antrag vom 25.10.2023 auf  bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom iSd Bundesgesetz über den  Energiekrisenbeitrag-Strom (EKBSG) BGBl I 220/2022 idgF für den Zeitraum 12/2022 bis  06/2023 gemäß § 201 Abs 3 Z 1 BAO abgewiesen wurde, Steuernummer [...], zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Proksch Manak Kraft Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Philippzig`(person)
- `Klimaweg 7, 8543 Graschach, Österreich`(address)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/146200.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146200.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Dr. Gregor Lohwaßer  in der Beschwerdesache  Hermann Kirchenbaur, Bradirn 5, 4841 Schmidham, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  12. Juni 2024 gegen den Bescheid des Finanzamtes Österreich vom 16. Mai 2024,  Steuernummer 67-467/1130, betreffend Festsetzung Energiekrisenbeitrag-Strom Juli bis  Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Proksch Manak Kraft  Rechtsanwälte GmbH` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gregor Lohwaßer`(person)
- `Hermann Kirchenbaur`(person)
- `Bradirn 5, 4841 Schmidham, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `67-467/1130`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/147805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Janet Borjes,  Karl Höfinger-Promenade 26O, 5500 Winkl, Österreich, vertreten durch  Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Teinfaltstraße 8/5.01,  1010 Wien, über die Beschwerde vom 3. Dezember 2024 gegen den Bescheid des Finanzamtes  Österreich vom 7. November 2024 betreffend Festsetzung des Energiekrisenbeitrag-Strom  (EKB-S) für den Zeitraum 1. Jänner 2024 bis 30. Juni 2024, Steuernummer 52-122/5024, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Proksch Manak Kraft Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Janet Borjes`(person)
- `Karl Höfinger-Promenade 26O, 5500 Winkl, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `52-122/5024`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/148988.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148988.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Corbinian Stumm  in der Beschwerdesache Irene Bödiger,  Roller 8, 3151 St. Pölten, Österreich, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG, Landstraße 9, 4020  Linz, betreffend die Beschwerde vom 22.4.2025 gegen den Bescheid des Finanzamtes  Österreich vom 24.3.2025 betreffend Abweisung eines Antrages auf bescheidmäßige  Festsetzung des Energiekrisenbeitrages-Strom (EKB-S) für den Zeitraum Jänner 2024 bis Juni  2024 beschlossen:  I. Gemäß § 278 Abs 1 BAO wird der angefochtene Bescheid vom 24.3.2025 aufgehoben und die  Sache zur Erledigung an das Finanzamt zurückverwiesen.

**False Positives:**

- `BEURLE Rechtsanwälte GmbH` — partial — pred is substring of gold: `BEURLE Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Corbinian Stumm`(person)
- `Irene Bödiger`(person)
- `Roller 8, 3151 St. Pölten, Österreich`(address)
- `BEURLE Rechtsanwälte GmbH & Co KG`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `Finanzamt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Miroslav Spandl  in der Beschwerdesache Rebecca Wölzlein, LLM,  Lahnsattel 29x, 5203 Köstendorf, Österreich, vertreten durch Niederhuber & Partner Rechtsanwälte GmbH, Metahofgasse  16, 8020 Graz, über die Beschwerde vom 16. Juni 2023 gegen den Bescheid des Zollamtes  Österreich vom 12. Mai 2023, Zl. 230000/204741/03/2023, betreffend die Aussetzung der  Einhebung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Niederhuber & Partner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Miroslav Spandl`(person)
- `Rebecca Wölzlein, LLM`(person)
- `Lahnsattel 29x, 5203 Köstendorf, Österreich`(address)
- `Zollamtes  Österreich`(organisation)

</details>

---

## `Generic_KG_Entity` 🏆

**F1:** 0.002 | **Precision:** 0.228 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `2d7a84d3`  
**Description:**
Matches generic corporate entities ending in KG (Kommanditgesellschaft) which were previously missing.

**Content:**
```
(?<![\w])(?:[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.228 | 0.001 | 0.002 | 79 | 18 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 61 | 18094 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_161`)


Der Beschwerdeführer hat gemeinsam mit X am Verkauf eines in Ort_2 gelegenen Grundstücks  an die HUKB Medien Services KG mitgewirkt.

| Predicted | Gold |
|---|---|
| `HUKB Medien Services KG` | `HUKB Medien Services KG` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_41`)


Die  Liegenschaft in Ort1 (vorgetragen in der Nexkel KG xxxxx Ort1) steht im Alleineigentum der  Schwiegermutter der Bf., Frau M, geb. am xx.xx.xxxx, die in einem abgeschlossenen Bereich im  3 von 12 Seite 4 von 12

| Predicted | Gold |
|---|---|
| `Nexkel KG` | `Nexkel KG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_14`)


Unter dieser Steuernummer sei am genannten Tag eine an die RDTM Gastronomie KG gerichtete  behördliche Erledigung ergangen, die als Feststellungsbescheid gem. § 188 BAO gedacht  gewesen sei.

| Predicted | Gold |
|---|---|
| `RDTM Gastronomie KG` | `RDTM Gastronomie KG` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_15`)


Für die Beurteilung der Verjährung sei wesentlich, dass auf Ebene dieser Gesellschaft zuletzt  nur die folgenden als Feststellungsbescheide gem. § 188 BAO gedachten behördlichen  Erledigungen für das Jahr 2013 ergangen sind:  • 01.08.2017  • 27.05.2021  • 16.02.2022  Da somit im Jahr 2019 weder auf Ebene des Bf. noch auf Ebene der RDTM Gastronomie KG Amtshandlungen  erfolgt seien, sei das Recht zur Festsetzung der Einkommensteuer 2013 tatsächlich bereits mit  Ablauf des 31. Dezember 2019 verjährt.

| Predicted | Gold |
|---|---|
| `RDTM Gastronomie KG` | `RDTM Gastronomie KG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_20`)


So weise die in der Begründung als Grundlagenbescheid genannte, an die RDTM Gastronomie KG gerichtete  behördliche Erledigung zur Steuernummer X vom 16. Februar 2022 keine elektronische  Signatur auf (siehe Beilage 1).

| Predicted | Gold |
|---|---|
| `RDTM Gastronomie KG` | `RDTM Gastronomie KG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_26`)


Diesbezüglich wurde nach Rücksprache mit dem Prüfer der RDTM Gastronomie KG (Steuernummer X) in  Erfahrung gebracht, dass bei der lt. Unterschrift am Prüfungsauftrag mit 18.12.2018  begonnenen Außenprüfung über die Jahre 2012 bis 2017 sowohl 2019 als auch 2020 diverse  Verlängerungshandlungen gesetzt wurden (zB Mail vom 4. Februar 2019 von der B an den  Prüfer mit Übermittlung einer Vielzahl an Unterlagen, Mail des Prüfers an die B vom 27.  Februar 2019 mit dem Ersuchen um Übermittlung diverser Unterlagen, Mail vom 16.10.2020  mit Verzicht auf Abhaltung einer Schlussbesprechung).

| Predicted | Gold |
|---|---|
| `RDTM Gastronomie KG` | `RDTM Gastronomie KG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_31`)


(gedacht als an die RDTM Gastronomie KG  StNr X gerichteter Feststellungsbescheid gem. § 188 BAO) die  elektronische Signatur fehle.

| Predicted | Gold |
|---|---|
| `RDTM Gastronomie KG` | `RDTM Gastronomie KG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_41`)


1. Flurbereinigungsverfahren BZ  Der Bf. vertauschte im Rahmen eines Flurbereinigungsübereinkommens 60/14.358stel  Anteilsrechte an der AG A Waldgenossenschaft,Moosbrucker Druck KG gegen einen Teil des Grundstückes Nr.  m/n im Flächenausmaß von ca. 1,06 ha.

| Predicted | Gold |
|---|---|
| `Moosbrucker Druck KG` | `Moosbrucker Druck KG` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Im Feststellungsverfahren der (damaligen) NiederLemwaldChemie Entwicklung KG, an welcher der Beschwerdeführer (in  weiterer Folge Bf.) im streitgegenständlichen Jahr beteiligt war, fand eine Betriebsprüfung  statt.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_15`)


Mit Beschwerdevorentscheidung vom 16. März 2017 wies das Finanzamt die Beschwerde als  unbegründet ab und führte in der Begründung im Wesentlichen aus, dass im gegenständlichen  Fall eine Investitionsmöglichkeit in Form einer Beteiligung als Kommanditist bei der NiederLemwaldChemie Entwicklung KG  beworben worden sei.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_20`)


Die objektive Tatseite sei somit erfüllt.  Hinsichtlich der subjektiven Tatseite führte das Finanzamt im Wesentlichen aus, dass nach  Ansicht der Außenprüfung die NiederLemwaldChemie Entwicklung KG  zur Ausnutzung steuerlicher Vorteile gegründet  worden sei.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_28`)


Die subjektive Tatseite sei daher ebenfalls erfüllt.  Am 12. April 2017 brachte der Bf. den Vorlageantrag ein und brachte im Wesentlichen vor,  dass die Einkommensteuer 2005 bereits am 1. Jänner 2012 verjährt sei, da   - im Feststellungsverfahren der NiederLemwaldChemie Entwicklung KG  die einzige nach außen gehende Amtshandlung die  Erlassung des Feststellungsbescheides am 23. Oktober 2006 gewesen sei,   - und auf Ebene des Einkommensteuerverfahrens lediglich am 8. Juni 2008  (Einkommensteuerbescheid) und am 24. Februar 2010 (Änderung des  Einkommensteuerbescheide gemäß § 295 Abs. 1 BAO) nach außen gehende Amtshandlungen  betreffend die Einkommensteuer 2005 erfolgt seien und  - weil keine hinterzogenen Abgaben im Sinne des § 207 Abs. 2 BAO vorlägen.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_33`)


Mit Erkenntnis vom 27. August 2024 gab das Bundesfinanzgericht ua. der Beschwerde gegen  den Bescheid betreffend Wiederaufnahme des Feststellungsverfahren 2005 betreffend  NiederLemwaldChemie Entwicklung KG  statt und hob den Wiederaufnahmebescheid auf, da laut Mitteilung an das  Bundesfinanzgericht vom Finanzamt neu angestellte Prognoserechungen ergeben hätten, dass  die Rendite nach Steuern nicht doppelt so hoch wie vor Steuern liegen würde und somit kein  Anwendungsfall des § 2 Abs. 2a EStG vorliege.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_37`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. war im streitgegenständlichen Jahr 2005 Kommanditist der (damaligen) NiederLemwaldChemie Entwicklung KG  (Steuernummer 83-459/7957).

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `83-459/7957` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_39`)


Im Feststellungsverfahren 2005 der NiederLemwaldChemie Entwicklung KG  ergingen folgende Bescheide:  23. Oktober 2006 Erlassung des Feststellungsbescheides  18. Dezember 2015 Bescheid über die Wiederaufnahme des Feststellungsverfahrens     betreffend 2005  18. Dezember 2015 Erlassung des neuen Feststellungebescheides  27. August 2024 Erkenntnis des BFG, mit welchem der Beschwerde gegen die      Wiederaufnahme stattgegeben wird  27. August 2024 Beschluss des BFG, mit welchem die Beschwerde gegen den      Feststellungsbescheid gegenstandslos erklärt wird.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_40`)


Im Jahr 2015 erfolgte eine Betriebsprüfung bei der NiederLemwaldChemie Entwicklung KG  hinsichtlich Feststellung von  Einkünften gemäß § 188 BAO betreffend ua. das Jahr 2005.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_58`)


Dieser  Bescheid wurde wiederum mit (angefochtenem) Bescheid vom 22. Dezember 2015 aufgrund  des Feststellungsbescheides der (damaligen) NiederLemwaldChemie Entwicklung KG  vom 18. Dezember 2015 gemäß § 295  Abs. 1 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_59`)


Im Feststellungsverfahren der (damaligen) NiederLemwaldChemie Entwicklung KG  wurde am 23. Oktober 2006 ein  Feststellungsbescheid erlassen, fand im Jahr 2015 eine Betriebsprüfung statt und wurde am 18.  Dezember 2015 das Feststellunsgsverfahren 2005 wiederaufgenommen und ein neuer  Feststellungsbescheid erlassen.

| Predicted | Gold |
|---|---|
| `NiederLemwaldChemie Entwicklung KG` | `NiederLemwaldChemie Entwicklung KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_7`)


Feststellungsbescheid 2007 der QZKX Beratung  KG sowie den Einkommensteuerbescheid 2007 des  Bf. richtet, wurde im Schriftsatz vom 2. August 2013 – soweit es die Anspruchszinsen 2007  anbelangt – ausgeführt, dass die Bescheide über die Wiederaufnahme des Verfahrens, der  Feststellungsbescheid sowie der darauf abgeleitete Einkommensteuerbescheid 2007  rechtswidrig seien bzw. Nichtbescheide vorliegen, weshalb auch der Bescheid über die  Anspruchszinsen dem Inhalt nach rechtswidrig sei, da dieser gar nicht erlassen werden hätte  können.

**False Positives:**

- `QZKX Beratung  KG` — partial — gold is substring of pred: `QZKX Beratung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QZKX Beratung`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dienstl & Partner  KG` — partial — pred is substring of gold: `Mag. Walter Dienstl & Partner  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Vivian Malek`(person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich`(address)
- `Mag. Walter Dienstl & Partner  KG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_107`)


Beim  anderen Produkt handelt es sich um eine Kupplung des Herstellers und Distributors von  Zubehör in den Produktbereichen Foto, Video, Audio, Computer und Telekommunikation,  nämlich der Firma Hama GmbH & Co KG, die zum Anschluss eines analogen Telefons an eine  TST-Anschlussdose geeignet ist.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Hama GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hama GmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_42`)


In der Firma G... Bau GmbH & Co KG arbeite ich erst ab 20.02.2017.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `G... Bau GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... Bau GmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_74`)


Inwiefern dieser Punkt eine Unzumutbarkeit begründen soll ist nicht ersichtlich, kann aber  dahingestellt bleiben, da im Hinblick auf die Unzumutbarkeit die Jahresbetrachtung gilt. Im  gegenständlichen Jahr 2018, war der Bf. ganzjährig bei der G... BAU GmbH & Co KG beschäftigt.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `G... BAU GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... BAU GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_89`)


Seit 29. August 2016 ist der Bf. bei der Fa. G. Bau GmbH & Co KG nichtselbständig beschäftigt  (Abgabeninformationssystemabfrage).

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `G. Bau GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G. Bau GmbH & Co KG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_91`)


er arbeitet bei der Firma G. Bau  GmbH & Co KG erst ab 20. Februar 2017.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Firma G. Bau  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Firma G. Bau  GmbH & Co KG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_3`)


Entscheidungsgründe  Am 3.April 2015 wurde zwischen der Bf., als Mieterin, und der V, als Vermieterin, ein  Mietvertrag über die Anmietung von Büroflächen, in dem, im Eigentum der Vermieterin  stehenden Büro-und Geschäftsgebäude der Liegenschaft KG bbb, BG Innere Stadt Wien,  (Adresse:  ccc) abgeschlossen.

**False Positives:**

- `Liegenschaft KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Astoria Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)
- `Astoria Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_4`)


Entscheidungsgründe  Mit Erkenntnis des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  14. Februar 2018, Strafnummer StrNr, wurde die nunmehrige Beschwerdeführerin Chen Kürkcü  (in der Folge kurz Bf. genannt) für schuldig erkannt, sie habe als unbeschränkt haftende  Geschäftsführerin der Fa. „XY Ltd.“ welche unbeschränkt haftende Gesellschafterin der Fa. “Z.  Ltd. & Co KG“ sei, vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes entsprechenden Voranmeldungen eine Verkürzung von Umsatzsteuer  (Vorauszahlungen oder Gutschriften) bewirkt und dies nicht nur für möglich,  sondern für  gewiss gehalten zu haben und zwar:   1 von 11 Seite 2 von 11

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Z.  Ltd. & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Chen Kürkcü`(person)
- `Z.  Ltd. & Co KG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Scarlett Beverungen, Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 71-240/3156  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Uniconsult Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Scarlett Beverungen`(person)
- `Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich`(address)
- `Uniconsult Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Braunau Ried`(organisation)
- `71-240/3156`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Delia Kavelmann  in der Beschwerdesache Larissa Rastätter,  Wendelgraben 27, 6563 Galtür, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und PhD Isaak Joern wird  abgewiesen.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Delia Kavelmann`(person)
- `Larissa Rastätter`(person)
- `Wendelgraben 27, 6563 Galtür, Österreich`(address)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)
- `PhD Isaak Joern`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_189`)


Gesellschafter-Geschäftsführers ist hiebei nicht maßgebend (zB VwGH 13.12.1977,1550/77,  betreffend die Geschäftsführung durch eine Komplementär-GmbH einer GmbH &Co KG).

**False Positives:**

- `GmbH &Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_25`)


Das Finanzamt Österreich beantwortete das Ersuchen um Amtshilfe mit folgender Auskunft:  „Aufgrund der Errichtung eines Kleinhauses auf der Liegenschaft EZ Schummers Textil KG KG wurde mit  Einheitswertbescheid vom 25.11.2019 der Einheitswert zum Stichtag 1.1.2014 festgestellt sowie  mit Grundsteuermessbescheid vom 25.11.2019 der Grundsteuermessbetrag festgesetzt.

**False Positives:**

- `Liegenschaft EZ Schummers Textil KG KG` — partial — gold is substring of pred: `Schummers Textil KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `Schummers Textil KG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134910.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Alva Karp  in der Beschwerdesache Sheila Nagell,  Horner Straße 104, 3623 Ernst, Österreich, vertreten durch Pölzleithner Wirtschaftstreuhand KG  Steuerberatungsgesellschaft, Dr Scheiber Str 20, 4870 Vöcklamarkt, betreffend Beschwerde  vom 4. August 2014 gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck (nunmehr  Finanzamt Österreich) vom 21. Juli 2014 betreffend Einkommensteuer 2012 Steuernummer  29-285/1127  beschlossen:   Der Vorlageantrag vom 29. September 2014 wird gemäß § 256 Abs. 3 BAO in Verbindung mit §  264 Abs. 4 BAO als gegenstandslos erklärt.

**False Positives:**

- `Wirtschaftstreuhand KG` — partial — pred is substring of gold: `Pölzleithner Wirtschaftstreuhand KG  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alva Karp`(person)
- `Sheila Nagell`(person)
- `Horner Straße 104, 3623 Ernst, Österreich`(address)
- `Pölzleithner Wirtschaftstreuhand KG  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `29-285/1127`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135360.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/137456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Siegfried Herboldt  in der Beschwerdesache der Frau  Erich Vossebrink, Voestalpine-Straße 28, 2813 Pengersdorf, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Siegfried Herboldt`(person)
- `Erich Vossebrink`(person)
- `Voestalpine-Straße 28, 2813 Pengersdorf, Österreich`(address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_48`)


weiters auf dem Stick: Kopie einer handschriftlichen Notiz vom 7.11.2013 der "OStR Dipl. Kff. Martha Mattiesen  KG"  über Auszahlungsmodalitäten 2013, 2012 und 2011), wurde erstmals offengelegt bzw. war  ersichtlich, dass Auszahlungsbestätigungen an bzw. in weiterer Folge dann von einem gewissen  "J" oder "M" T existieren (siehe unten, Pkt: -2g).

**False Positives:**

- `Martha Mattiesen  KG` — positional overlap with gold: `OStR Dipl. Kff. Martha Mattiesen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Dipl. Kff. Martha Mattiesen`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/139570.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139570.1_5`)


Die Antragstellerin Antragstellerin hat durch ihre rechtsfreundliche Vertretung am 18.10.2021,  beim Bundesfinanzgericht eingelangt am 21.10.2021, einen Antrag auf Akteneinsicht in den Akt  GZ. RV/71017775/2019 unter Hinweis auf den Unterbrechungsbeschluss vom 28.5.2019  gestellt.    Beschwerdeverfahren des gegenständlichen Aktes, in den Einsicht begehrt wurde  Das dem Antrag auf Akteneinsicht zu Grunde liegende Beschwerdeverfahren zwischen der  beschwerdeführenden Partei MD PWS Waldtriost  GmbH und Co KG und der zuständigen  Abgabenbehörde – mittlerweile Finanzamt Österreich – wurde gemäß § 122 Abs. 11 WKG 1998  unterbrochen und zur Klärung der Frage, ob die beschwerdeführende Partei in den Jahren  2003 bis 2015 Mitglied der Antragstellerin war, dem Präsidenten der Antragstellerin zur  Entscheidung vorgelegt.

**False Positives:**

- `GmbH und Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Waldtriost`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad in der Verwal- tungsstrafsache gegen DDr. Frank Paulowski, Ramaseck 9, 4055 Zeitlham, Österreich, vertreten durch Dr. Reinitzer Rechtsanwalts  KG, Theobaldgasse 15/21, 1060 Wien, wegen der Verwaltungsübertretung gemäß § 5 Abs 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs 1 Wiener Parkometergesetz 2006, über die  Beschwerde der Beschuldigten vom 22. Dezember 2022 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 19. Dezember 2022, GZ.  MA67/Zahl/2022, zu Recht:  I. Gemäß § 50 VwGVG wird der Beschwerde insofern teilweise stattgegeben als die  Geldstrafe von 60,00 €  auf 48,00 € und die Ersatzfreiheitsstrafe von 14 Stunden auf  10 Stunden herabgesetzt wird.

**False Positives:**

- `Reinitzer Rechtsanwalts  KG` — partial — pred is substring of gold: `Dr. Reinitzer Rechtsanwalts  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `DDr. Frank Paulowski`(person)
- `Ramaseck 9, 4055 Zeitlham, Österreich`(address)
- `Dr. Reinitzer Rechtsanwalts  KG`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_8`)


Als Ergebnis der AP-Verfahren erlassene Abgabenbescheide an - zumeist als  GmbH bzw. GmbH & Co KG geführte - Gesellschaften des geprüften Firmenkomplexes bzw.  1 von 30 Seite 2 von 30

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/141490.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141490.1_15`)


In der vom Bf. übermittelten E- Mailnachricht vom 02.09.2015 der KG wird ausgeführt:  Der Bf. habe der Firma KG Nachrangdarlehen mit fester Laufzeit gewährt.

**False Positives:**

- `Firma KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141490.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141490.1_39`)


Vorlageantrag vom 03.03.2020  Im Vorlageantrag wird – unter Verweis auf die E-Mailnachricht vom 02.09.2015 - ergänzend  begründet, dass eine Auszahlung jedweder Gelder nur für Notfälle vorgesehen gewesen sei,  und die Definition der Notfälle von der Firma KG interpretiert wurde.

**False Positives:**

- `Firma KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141490.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141490.1_48`)


Prospekte, der (Darlehens)Vertrag und ein allfällig weiterer Schriftverkehr mit der Firma KG  konnten nicht vorgelegt werden.

**False Positives:**

- `Firma KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/141580.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141580.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Erinnerungsschreiben vom 15.7.2022 forderte das Finanzamt die Beschwerdeführerin (Bf.),  bei der es sich um eine GmbH & Co KG handelt, dazu auf, die "Erstmeldung oder Meldung nach  Fälligkeit der jährlichen Überprüfung der wirtschaftlichen Eigentümer entsprechend den  Bestimmungen des § 5 Wirtschaftliche Eigentümer Registergesetz (WiEReG)" bis längstens  5.9.2022 nachzuholen.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/142086.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142086.1_12`)


Im April 2022 zog er zurück in seine ehemalige Heimat und verlegte seinen meldebehördlichen  Hauptwohnsitz (HW) nach Orchideenweg 172, 4894 Gewerbegebiet-Salzweg, Österreich (lt. ZMR Unterkunftgeberin Frau-A, geb. 5.Okt.1939,  Alleineigentümerin der Liegenschaft KG 88888, EZ 888).

**False Positives:**

- `Liegenschaft KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Orchideenweg 172, 4894 Gewerbegebiet-Salzweg, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/142273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ingolf Schloßnickel  in der Beschwerdesache Dr.in Ing. Frauke Mühlenthaler,  Kettensteggasse 37a, 5261 Sonnleiten, Österreich, vertreten durch Kitzbühler WTH Dkfm Dr Karl Koller KG, Josef-Pirchl-Straße 18,  6370 Kitzbühel, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 11. Mai 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  74-573/4900,  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `WTH Dkfm Dr Karl Koller KG` — partial — gold is substring of pred: `Dkfm Dr Karl Koller KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Ingolf Schloßnickel`(person)
- `Dr.in Ing. Frauke Mühlenthaler`(person)
- `Kettensteggasse 37a, 5261 Sonnleiten, Österreich`(address)
- `Dkfm Dr Karl Koller KG`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `74-573/4900`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/142273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142273.1_68`)


Die Beschwerdeführerin ist eine Personengesellschaft in Form einer GmbH &Co KG.

**False Positives:**

- `GmbH &Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Karim Ickstadt  in der Beschwerdesache   Axel Jastrzemsky, als Gruppenträgerin, V GmbH, als Gruppenmitglied und der Klemeyer + Heisterhagen Pharma GmbH  als von der  Teilnahme an der Unternehmensgruppe ausgeschlossene Körperschaft, jeweils vertreten durch  Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG, Linzer Bundesstraße 101, 5023  Salzburg-Gnigl, über die Beschwerde der Axel Jastrzemsky, Sandweg 7, 4782 Aigerding, Österreich, vom 28. März 2019 gegen  den Gruppenfeststellungsbescheid 2018 des Finanzamtes Wien 12/13/14 Purkersdorf -  nunmehr Finanzamtes Österreich - vom 27. Februar 2019, Steuernummer 74-905/9339,  nach Durchführung einer mündlichen Verhandlung am 22. August 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Karim Ickstadt`(person)
- `Axel Jastrzemsky`(person)
- `Klemeyer + Heisterhagen Pharma GmbH`(organisation)
- `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG`(organisation)
- `Axel Jastrzemsky`(person)
- `Sandweg 7, 4782 Aigerding, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamtes Österreich`(organisation)
- `74-905/9339`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_27`)


Der Bf war im Jahr 2004 an der Firma (im Folgenden kurz: GmbH & Co KG) als atypisch stiller  Gesellschafter beteiligt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_28`)


An die GmbH & Co KG erging am 15.1.2019 zur GZ RV/4100213/2012 eine Erledigung des BFG,  deren Spruch zufolge eine Beschwerde der GmbH & Co KG gegen die einheitliche und  gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2004 bis 2005 mangels  Bescheidqualität der angefochtenen Bescheide als unzulässig zurückgewiesen wurde.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation
- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_30`)


Am 10.11.2021 erging an die GmbH & Co KG neuerlich eine Erledigung des BFG zur GZ  RV/4100213/2012, mit der die Beschwerde der GmbH & Co KG gegen die einheitliche und  gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2004 bis 2005 mangels  Bescheidqualität als unzulässig zurückgewiesen wurde.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation
- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_86`)


Das BFG wollte mit seiner Erledigung vom 15.1.2019 die Beschwerde der GmbH & Co KG  betreffend die Feststellung von Einkünften gemäß § 188 BAO als unzulässig zurückweisen und  damit mit Rechtskraftwirkung für alle am Feststellungsverfahren Beteiligten aussprechen, dass  die vor ihm bekämpften Feststellungsbescheide nicht wirksam geworden waren.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_87`)


Dennoch hat  das Bundesfinanzgericht seine im Rahmen von Feststellungsverfahren ergangene Erledigung  nur an die GmbH & Co KG und nicht an alle Gesellschafter adressiert und zugestellt. Mangels  eines Hinweises in der betreffenden Erledigung ist die Zustellwirkung im Sinne des § 101 Abs 3  zweiter Satz BAO gegenüber den Gesellschaftern, denen Einkünfte zugerechnet werden sollen,  nicht eingetreten.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/142810.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142810.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marceline Weizenkorn  in der Beschwerdesache Georg Strüve,  Laubweg 96, 4300 St. Valentin, Österreich, vertreten durch Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG,  Hadeldorfstraße 30, 6830 Rankweil, über die Beschwerde vom 2. November 2022 gegen den  Bescheid des Finanzamt Purkersdorf  vom 28. September 2022 betreffend Feststellung von Einkünften  gemäß § 188 BAO für 2018, Steuernummer 36-621/8395, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO in Verbindung mit § 260 Abs. 1 lit. a BAO  als unzulässig zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Marceline Weizenkorn`(person)
- `Georg Strüve`(person)
- `Laubweg 96, 4300 St. Valentin, Österreich`(address)
- `Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamt Purkersdorf`(organisation)
- `36-621/8395`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/143190.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143190.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner in der Beschwerdesache  Muran de Franceschi, Im Lagerfeld 323T, 4891 Haidach, Österreich, vertreten durch KWT Klagenfurter Wirtschaftstreuhand &  Steuerberatungs KG, Kempfstraße 23, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom  9. Mai 2018 gegen die Bescheide des Finanzamtes Klagenfurt (nunmehr Finanzamt Österreich)  vom 10. April 2018 betreffend die Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2014, Einkommensteuer 2014 sowie über die Festsetzung von  Anspruchszinsen 2014, Steuernummer 51-879/1950 ,  I. zu Recht erkannt:  1.)

**False Positives:**

- `Wirtschaftstreuhand &  Steuerberatungs KG` — partial — pred is substring of gold: `KWT Klagenfurter Wirtschaftstreuhand &  Steuerberatungs KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Muran de Franceschi`(person)
- `Im Lagerfeld 323T, 4891 Haidach, Österreich`(address)
- `KWT Klagenfurter Wirtschaftstreuhand &  Steuerberatungs KG`(organisation)
- `Finanzamtes Klagenfurt`(organisation)
- `Finanzamt Österreich`(organisation)
- `51-879/1950`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/143366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Melina Wibelitz, Holzsteig 6, 2002 Nursch, Österreich, vertreten durch BKS Steuerberatung GmbH & Co KG, Untere Hauptstr 10, 3150  Wilhelmsburg an der Traisen, über die Beschwerde vom 28. Juli 2019 gegen die Bescheide des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 15. Juli 2019 betreffend Grunderwerbsteuer, Steuernummer 93-238/5183,  Erfassungsnummer 10-2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `BKS Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Melina Wibelitz`(person)
- `Holzsteig 6, 2002 Nursch, Österreich`(address)
- `BKS Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)
- `93-238/5183`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Barbara Straka, die Richterin  Mag. Irene Kohler sowie die fachkundigen Laienrichter Dip.Ing. Gerald Patschka und Mag.  Michael Heumesser in der Beschwerdesache Oleg Eckschmidt, Hausgrabengasse 1780, 4720 Straßhof, Österreich, vertreten durch  Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38,  1020 Wien, über die Beschwerde vom 22. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2023 betreffend Einkommensteuer 2013, Steuernummer  60-131/3835, in der Sitzung am 17. Jänner 2024, erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

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

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_5`)


Begründend führte das Finanzamt aus, dass die  Änderung gem. § 295 BAO aufgrund der bescheidmäßigen Feststellungen des Finanzamtes  Österreich zu Steuernummer X (Fa.RDTM Gastronomie KG  vom 16.02.2022 erfolgt sei.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `Fa.RDTM Gastronomie KG`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_43`)


Im Zuge des Verfahrens vor dem Bundesfinanzgericht wurde der Prüfer der Fa.RDTM Gastronomie KG ersucht,  das E-Mail vom 24.09.2020 (Betreff Terminvereinbarung Schlussbesprechung) zu übermitteln.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fa.RDTM Gastronomie KG`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_50`)


Die Änderung erfolgte  aufgrund der bescheidmäßigen Feststellungen des Finanzamtes Österreich vom 16.02.2022 zu  Steuernummer X, betreffend Fa.RDTM Gastronomie KG  An den Bf. sind für das Jahr 2013 folgende Einkommensteuerbescheide ergangen:  Erstbescheid 13.11.2014   Folgeänderung gem. § 295 Abs. 1 BAO 10.03.2015  Folgeänderung gem. § 295 Abs. 1 BAO 30.04.2015  Folgeänderung gem. § 295 Abs. 1 BAO 31.07.2015  Folgeänderung gem. § 295 Abs. 1 BAO 02.06.2021  Folgeänderung gem. § 295 Abs.1 BAO 23.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Fa.RDTM Gastronomie KG`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_71`)


Im vorliegenden Fall wurden im Rahmen einer Außenprüfung u.a. nachstehende nach außen  erkennbare Amtshandlungen bei der Fa.RDTM Gastronomie KG getätigt:  - Unterschrift des steuerlichen Vertreters am Prüfungsauftrag mit 18.12.2018 (für  Außenprüfung Umsatzsteuer und Feststellung der Einkünfte für die Jahre 2012 bis 2017),  - Mail des Prüfers vom 27.02.2019 an die für die Erstellung der Buchhaltung beauftragte  C  GmbH mit dem Ersuchen um Übermittlung diverser Unterlagen,  - Mail vom 24.09.2020 des Prüfers betreffend Terminvereinbarung für die Abhaltung einer  Schlussbesprechung,  - Bericht über die Außenprüfung vom 21.05.2021 und  - Beschwerdevorentscheidung vom 16.02.2022  Das bedeutet auf den vorliegenden Fall bezogen:  Die Verjährung der Einkommensteuer 2013 des Bf. begann gemäß § 208 Abs. 1 lit. a BAO mit  dem Ablauf des Jahres, in welchem der Einkommensteueranspruch entstanden ist, d.h. gemäß  § 4 Abs. 2 Z 2 BAO mit Ablauf des Jahres 2013.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_78`)


Durch das Mail des Prüfers vom 27.02.2019 an die Buchhaltung der Fa.RDTM Gastronomie KG (mit dem  Ersuchen um Übermittlung diverser Unterlagen) wurde eine weitere nach außen erkennbare  Amtshandlung zur Geltendmachung des Abgabenanspruches gesetzt, wodurch sich die  Verjährungsfrist zunächst auf sieben Jahre (Ablauf Ende 2020) verlängert.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_79`)


Durch das Mail des Prüfers vom 24.09.2020 im Rahmen der Außenprüfung der Fa.RDTM Gastronomie KG  betreffend Terminvereinbarung Schlussbesprechung wurde eine nach außen erkennbare  Amtshandlung gesetzt, wodurch sich die Verjährungsfrist weiter auf acht Jahre (Ablauf Ende  2021) verlängert.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_80`)


Durch den Bericht über die Außenprüfung bei der Fa.RDTM Gastronomie KG datiert vom 21.05.2021 und durch  den Bescheid über die Feststellung von Einkünften gem. § 188 BAO für das Jahr 2013 datiert  vom 27.05.2021, wurden nach außen erkennbare Amtshandlungen gesetzt, wodurch sich die  Verjährungsfrist auf neun Jahre (Ablauf Ende 2022) verlängert.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_81`)


Durch die Beschwerdevorentscheidung vom 16. Februar 2022 betreffend Bescheid über die  Feststellung von Einkünften gem. § 188 BAO für das Jahr 2013 der Fa.RDTM Gastronomie KG wurde ebenfalls  eine nach außen erkennbare Amtshandlung gesetzt, wodurch sich die Verjährungsfrist auf zehn  Jahre (Ablauf Ende 2023) verlängert.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_86`)


Im Vorlageantrag vom 23. Mai 2023 ging der steuerliche Vertreter des Bf. nicht mehr auf die  Verjährung ein und brachte lediglich vor, dass auf dem Grundlagenbescheid  (Feststellungsbescheid gem. § 188 BAO Fa.RDTM Gastronomie KG vom 16. Februar 2022) die elektronische  Signatur fehle und diese behördliche Erledigung daher als Nichtbescheid einzustufen sei.

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/143446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143446.1_111`)


In der Beschwerde gegen  den Bescheid gem. § 295 Abs. 1 BAO wird aber vorgebracht, dass der als Grundlagenbescheid  herangezogenen behördlichen Erledigung vom 16. Februar 2022 (gedacht als an die Fa.RDTM Gastronomie KG  gerichteter Feststellungsbescheid gem. § 188 BAO) die elektronische Signatur fehle und diese  10 von 12 Seite 11 von 12

**False Positives:**

- `RDTM Gastronomie KG` — partial — pred is substring of gold: `Fa.RDTM Gastronomie KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RDTM Gastronomie KG`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_34`)


Die Agrargemeinschaft A Waldgenossenschaft, bestehend aus der Liegenschaft Moosbrucker Druck KG  ist gem.  § 2 Abs. 2 der Verwaltungssatzung eine juristische Person, die nach außen durch ihre  Verwaltungsorgane vertreten wird.

**False Positives:**

- `Liegenschaft Moosbrucker Druck KG` — partial — gold is substring of pred: `Moosbrucker Druck KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Moosbrucker Druck KG`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_46`)


Flurbereinigungsverfahren zu AZ tauschte der Bf. seine Anteilsrechte (11/14.358tel) an  der A Waldgenossenschaft Moosbrucker Druck KG gegen einen Teil des Grundstücks Nr. x/y.

**False Positives:**

- `Waldgenossenschaft Moosbrucker Druck KG` — partial — gold is substring of pred: `Moosbrucker Druck KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Moosbrucker Druck KG`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_81`)


Im konkreten Fall erfolgte jeweils der Tausch eines Grundstücksanteiles gegen Anteile an der  Agrargemeinschaft A Waldgenossenschaft, die aus der Liegenschaft Moosbrucker Druck KG besteht.

**False Positives:**

- `Liegenschaft Moosbrucker Druck KG` — partial — gold is substring of pred: `Moosbrucker Druck KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Moosbrucker Druck KG`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_92`)


Gem. § 4 der Verwaltungssatzungen inkl. Holzauszeige –Instruktion der Agrargemeinschaft A  Waldgenossenschaft Moosbrucker Druck KG sind Anteilsrechte an die berechtigten Liegenschaften gebunden  und können von diesen ohne Zustimmung der Aufsichtsbehörde nicht rechtswirksam  abgesondert werden.

**False Positives:**

- `Waldgenossenschaft Moosbrucker Druck KG` — partial — gold is substring of pred: `Moosbrucker Druck KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Moosbrucker Druck KG`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/144821.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144821.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Julia Griesfelder, Dr.Karl Rennerstraße 27, 9121 Lasseinerbucht, Österreich, vertreten durch Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft, Hietzinger Kai 67-69, 1130 Wien, betreffend Beschwerde vom  9. Juni 2023 gegen die Bescheide des Finanzamtes Österreich vom 6. März 2023 betreffend  Umsatz- und Körperschaftsteuer 2019 Steuernummer 41-950/9771  beschlossen:   Der Vorlageantrag vom 28. Mai 2024 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

**False Positives:**

- `GmbH & Co  KG` — partial — pred is substring of gold: `Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Julia Griesfelder`(person)
- `Dr.Karl Rennerstraße 27, 9121 Lasseinerbucht, Österreich`(address)
- `Djuric & Oberger Wirtschaftstreuhand GmbH & Co  KG Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-950/9771`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Urs Ahrenholz, Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich, vertreten durch HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG, Schloßgraben 10, 6800 Feldkirch,  über die Beschwerde vom 2. Oktober 2019 gegen den Bescheid des Finanzamtes Feldkirch vom  9. September 2019 betreffend Einkommensteuer 2017, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Urs Ahrenholz`(person)
- `Zum Pfarrfeld 8, 3262 Thurhofwang, Österreich`(address)
- `HERBURGER FREI & PARTNER  Wirtschaftsprüfungs- und Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Feldkirch`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/147633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147633.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Techn R Karola Grosse-Allermann, Bauernbergstraße 25, 4921 Langstadl, Österreich, vertreten durch FP FerTax Steuerberatungs GmbH  & Co KG, Graf-Starhemberg-Gasse 6 Tür 2, 1040 Wien, über die Beschwerde vom 14. Jänner  2023 gegen den Bescheid des Finanzamtes Österreich vom 15. Dezember 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer 93-739/6588, nach  Durchführung einer mündlichen Verhandlung am 2. April 2025 im Beisein der Schriftführerin  Andrea Newrkla zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO - im eingeschränkten Umfang - Folge gegeben.

**False Positives:**

- `GmbH  & Co KG` — partial — pred is substring of gold: `FP FerTax Steuerberatungs GmbH  & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Julia Carola Cermak-Kapl MA`(person)
- `Techn R Karola Grosse-Allermann`(person)
- `Bauernbergstraße 25, 4921 Langstadl, Österreich`(address)
- `FP FerTax Steuerberatungs GmbH  & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `93-739/6588`(tax_number)
- `Andrea Newrkla`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/148936.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148936.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mirko Boeshenz  in der Beschwerdesache KommR Manuel Ruppoldt,  Hauptschulweg 5, 8563 Oberwald, Österreich, vertreten durch Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG, Karl-Emminger-Straße 23, 5020 Salzburg, über die Beschwerde vom 27. Juni 2022  gegen den Bescheid des Finanzamtes Österreich vom 19. Mai 2022 betreffend  Einkommensteuer 2020 Steuernummer 90-698/6357  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `GmbH  & Co KG` — partial — pred is substring of gold: `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mirko Boeshenz`(person)
- `KommR Manuel Ruppoldt`(person)
- `Hauptschulweg 5, 8563 Oberwald, Österreich`(address)
- `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `90-698/6357`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Verena Khalidi  in der Beschwerdesache MedR Fiona Davydova,  St.-Anna-Park 16i, 5274 Unterhartberg, Österreich, vertreten durch Liepert Greussing Sturm Steuerberatung GmbH & Co KG,  Mühlgasse 21, 6700 Bludenz, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid  des FA Baden Mödling  vom 10. Jänner 2018 betreffend Haftungs- und Abgabenbescheid 2016  Steuernummer 96-418/3627  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung  teilweise Folge gegeben.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Liepert Greussing Sturm Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Verena Khalidi`(person)
- `MedR Fiona Davydova`(person)
- `St.-Anna-Park 16i, 5274 Unterhartberg, Österreich`(address)
- `Liepert Greussing Sturm Steuerberatung GmbH & Co KG`(organisation)
- `FA Baden Mödling`(organisation)
- `96-418/3627`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149445.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149445.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Beschwerdesache Anatol Schlimp, KLG Wasserwiese Gruppe 3, 8954 Mitterberg, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Handelsstraße 8/Stiege 2/Top 2, 3130 Herzogenburg, betreffend Beschwerde vom  24. Oktober 2023 gegen den Bescheid des Finanzamtes Österreich vom 28. September 2023  betreffend Einkommensteuer 2021 Steuernummer 26-775/1483  beschlossen:   Die Beschwerde vom 24. Oktober 2023 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `GmbH & Co  KG` — partial — pred is substring of gold: `BKS Steuerberatung GmbH & Co  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gertraud Hausherr`(person)
- `Anatol Schlimp`(person)
- `KLG Wasserwiese Gruppe 3, 8954 Mitterberg, Österreich`(address)
- `BKS Steuerberatung GmbH & Co  KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-775/1483`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_364`)


An der Näffgen und Duchoslav Cloud GmbH & Co KG waren beteiligt:  Als Kommanditisten:  170.000 ATS…….erster Stratege (34%)  165.000 ATS…….zweiter Stratege (33%)  23 von 75 Seite 24 von 75

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Näffgen und Duchoslav Cloud GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Näffgen und Duchoslav Cloud GmbH & Co KG`(organisation)

</details>

---

## `OGH_Abbreviation` 🏆

**F1:** 0.002 | **Precision:** 0.202 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `ad43d7bd`  
**Description:**
Matches the abbreviation OGH (Oberster Gerichtshof).

**Content:**
```
\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.202 | 0.001 | 0.002 | 84 | 17 | 67 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 67 | 17925 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_68`)


(Koppensteiner GmbHG, § 15 Tz. 7 unter Verweis auf OGH in RdW  1993, 243 u. a.)

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Koppensteiner GmbHG` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_195`)


Bei Beurteilung, ob dies der Fall ist, führt er  aus, dass „weder in der Fachliteratur noch in der Rechtsprechung des OGH davon ausgegangen  wird, dass die dem amerikanischen Franchising in Europa nachgebildeten Franchise-Verträge  so gestaltet sind, dass der Franchise-Nehmer nichts anderes als eine Gewerbeberechtigung in  das Vertragsverhältnis einbringt und alles andere einschließlich des vom Franchise-Nehmer zu  führenden Unternehmens beigestellt wird.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_67`)


Der  Kündigungsgrund der Z 9 (Eigenbedarf) könne zwar-nach der Rechtsprechung des OGH- auch  für eine juristische Person zutreffen, allerdings nur unter der Voraussetzung, dass diese die  betreffenden Räumlichkeiten zur Erfüllung ihres Zweckes dringend benötige; und es müsse die  dringende Notwendigkeit bestehen, den derzeitigen Zustand sobald als möglich zu beheben,  was nur durch Aufkündigung des Bestandverhältnisses erreicht werden kann.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_218`)


Davon spricht man,  wenn der Täter intellektuell erkannt hat, dass sein Verhalten zu einer Steuerverkürzung führen  kann und er diesen Erfolg billigend in Kauf nimmt (vgl. Kotschnigg in Tannert/Kotschnigg,  FinStrG, § 33, Rz. 216 und die dort zitierte OGH- und VwGH-Rechtsprechung).

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_633`)


Zur Eigenverantwortlichkeit und auch zur Haftung des Vertretungsarztes werde auf eine  Entscheidung des OGH vom 22.1.2008, 4 Ob 210/07 verwiesen, der ebendort ausführe:   „…Es fehle auch an jeder Abhängigkeit des Urlaubsvertreters von dem auf Urlaub befindlichen  Arzt;

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_635`)


Die Vertretung eines Arztes durch einen anderen Arzt sei  daher nicht Gehilfenschaft iSd § 1313a ABGB, sondern Substitution, bei der man nur für  Auswahlverschulden hafte…“   Aufgrund dieser Ausführungen von Dr. Emberger iVm der Entscheidung des OGH vertrat das  Bundesfinanzgericht die Auffassung, dass die Vertretungsärzte eigenverantwortlich tätig seien  und daher auch zur Haftung herangezogen werden könnten, was einem Unternehmerrisiko  gleichkomme.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_661`)


Das BFG hätte einen wesentlichen Gesichtspunkt unbehandelt gelassen:   “… nach der Rechtsprechung des OGH könne der in der Ordination des Vertretenen tätig  werdende Praxisvertreter eines niedergelassenen Arztes dessen Erfüllungsgehilfe bei der  Behandlung der Patienten sein, wenn diese der Meinung sein mussten, "entweder vom  Ordinationsinhaber persönlich oder zumindest innerhalb seines Verantwortungsbereichs  behandelt zu werden".

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/135942.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135942.1_28`)


Die Rechtsprechung des OGH zu der Auslegung des Begriffs „Wohnzwecke" im  Zusammenhang mit § 16 Abs 1 Z 1 MRG ist daher auch für § 33 TP 5 Abs 1 Z 4 heranzuziehen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_228`)


Dem von der Beschwerdeführerin vorgenommenen Verweis auf die Entscheidung des OGH  vom 16.1.2003, 2 Ob 311/02b, nach der sich ergebe, dass, wenn die ordentliche Kündigung  nicht erwähnt werde, dennoch auf die ordentliche Kündigung nicht verzichtet worden sei, und  das Recht zur ordentlichen Kündigung daher bestehen bleibe, tritt das Bundesfinanzgericht  damit entgegen, dass im Sachverhalt des zitierten OGH-Urteils offenbar überhaupt keine  Regelungen zur ordentlichen Kündigung getroffen wurden;

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_230`)


Darüber hinaus scheint  es einleuchtend, dass es im Fall eines Kreditkartenvertrags, zu dem die OGH-Entscheidung  erging, irgendeine Möglichkeit zur Auflösung gegeben sein muss, während im  beschwerdegegenständlichen Fall des Fahrzeugleasings ohnehin der Leasingnehmer ein  Interesse daran haben wird, den Vertrag nach einigen Jahren zu beenden, zumal der Wert des  geleasten Fahrzeugs permanent sinkt und sich die faktische Produktlebensdauer dem Ende  18 von 24 Seite 19 von 24

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/139351.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139351.1_33`)


Seines Wissens nach seien  derartige Prozesskosten "lt. OGH absetzbar", was ihm auch von Mitarbeitern des Finanzamtes  bestätigt worden sei.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/141978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141978.1_107`)


Davon  spricht man, wenn der Täter intellektuell erkannt hat, dass sein Verhalten zu einer  Steuerverkürzung führen kann und er diesen Erfolg billigend in Kauf nimmt (vgl. Kotschnigg in  Tannert/Kotschnigg, FinStrG § 33 Rz 216, und die dort zitierte OGH- bzw. VwGH- Rechtsprechung).

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_159`)


Unter dem Halter ist nach der Rechtsprechung des OGH die Person zu verstehen, die das  Fahrzeug auf eigene Rechnung in Gebrauch und die Verfügungsgewalt darüber hat.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_191`)


sie hat das Kfz somit nicht, wie es die  Rechtsprechung des OGH zum Halterbegriff erfordert (siehe oben), auf eigene Rechnung in  Gebrauch gehabt.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_47`)


Solche Vergütungs- zinsen unterliegen der dreijährigen Verjährungsfrist gemäß § 1480 ABGB (vgl. ebenfalls die  soeben zitierte OGH-Entscheidung;

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/149096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149096.1_62`)


Wie der OGH schon wiederholt erkannt hat, ist unabdingbare  Voraussetzung der Anrufung des Verfassungsgerichtshofes, dass das Gericht selbst Bedenken  gegen die Verfassungsmäßigkeit des anzuwendenden Gesetzes bzw. die Gesetzmäßigkeit der  anzuwendenden Verordnung hat; der Umstand allein, dass eine Partei solche Bedenken  vorbringt (oder dass im Schrifttum Bedenken geäußert worden sind), berechtigt oder  verpflichtet das Gericht noch nicht zur Normenprüfung.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_192`)


(OGH 26.4.1994, 4  Ob 535/94, Miet 46.088/11 mwN).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_21`)


Selbst eine Wendung wie "vertreten durch ...", die ohnedies nicht zwingend auf eine erteilte  Bevollmächtigung schließen lassen würde (OGH 24.3.1992, 5 Ob 25/92;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131109.1_102`)


Eine gesicherte Rechtsprechung besteht bereits bei Vorliegen eines begründeten Erkenntnisses  (OGH 1.8.2012, 4 Ob 119/12x)

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_141`)


Eine gesicherte Rechtsprechung besteht bereits bei Vorliegen eines begründeten Erkenntnisses  (vgl. OGH 1.8.2012, 4 Ob 119/12x)  10 von 11 Seite 11 von 11

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_22`)


Nach Auskunft seines Steuerberaters gebe es  für die Möglichkeit der Berücksichtigung in solchen Angelegenheiten entsprechende  Erkenntnisse des OGH.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_205`)


dies gilt auch für den bedingten Vorsatz  (vgl. OGH 26.3.1982, Zl. 10 Os 35/82;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_117`)


Welser in Rummel,  ABGB I3, § 549 Rz 4; OGH EvBl 1966/90).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_19`)


In den Beschwerdevorentscheidungen vom 22.05.2017 (zugestellt am 29.05.2017) verneinte  die belangte Behörde insbesondere unter Hinweis auf das Urteil des OGH vom 12.04.2016, 11  Os 53/15a erneut die Anwendbarkeit des Befreiungstatbestandes des § 10 Abs. 1 Z. 1 KStG.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_61`)


OGH 18.10.2007, 2 Ob 96/07t, NZ 2008,  151).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_124`)


Maßgebend ist, dass der Halter tatsächlich in  der Lage ist, die Verfügungsgewalt über das Fahrzeug auszuüben (vgl. OGH 18.12.2000, 9 Ob A  150/00z;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_374`)


Darunter ist – s: etwa Art. 11 Abs. 1 VO 987/2009 – im  Sinn des nationalen Rechts nicht bloß (irgendein) Wohnsitz i. S. d. § 26 Abs. 1 BAO zu  verstehen, sondern der Mittelpunkt der Lebensinteressen (§ 2 Abs. 8 Satz 2 FLAG 1967) bzw.  der Mittelpunkt der Lebensbeziehungen (§ 1 Abs. 8 Meldegesetz) dieser Person (vgl. Czaszar in  Csaszar/Lenneis/Wanke, FLAG § 53 Rz 81, unter Hinweis auf OGH 17.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_61`)


Die Änderung der Eigentumsverhältnisse bedarf vielmehr der  Einverleibung im Grundbuch, die wiederum nur aufgrund eines gültigen Titels erfolgen kann  (vgl. OGH 23.10.2001, 5 Ob 176/01w).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_90`)


die Änderung der Eigentumsverhältnisse bedarf vielmehr der Einverleibung im Grundbuch,  die wiederum nur aufgrund eines gültigen Titels erfolgen kann (vgl. OGH 23.10.2001, 5 Ob  176/01w).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_430`)


Begründet wurde dies damit, dass sie  als begutachtende und auch Befund erstellende Supervisorin tätig gewesen sei, deren  Vertragsinhalt die Herstellung eines ordnungsgemäßen Befundes des gynäkologischen  Abstrichs durch Supervision gewesen wäre, was in jedem Fall abgrenzbar, überprüfbar und  einer Gewährleistung bzw. Haftung zugänglich gewesen wäre, wobei bei der Herstellung von  Befunden nach der höchstgerichtlichen Rechtsprechung (OGH 23.05.1984, 1 Ob 550/84) ein  Werkvertrag vorliege.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_662`)


Werden die Patienten aber "mittels entsprechender Maßnahmen   (z.B. Anbringen eines entsprechenden Hinweises am Ordinationsschild oder an der Eingangstür  zum Behandlungsraum, Anweisung an den Vertreter oder sein Personal, die Patienten  entsprechend zu informieren)" vor Beginn der Behandlung über den Vertretungsfall aufgeklärt,  so kommt der (in der Regel konkludent abgeschlossene) Behandlungsvertrag nicht mit dem  (diesfalls nicht im rechtlichen Sinn) Vertretenen, sondern mit dem Praxisvertreter selbst  zustande (OGH 22.1.2008, 4 Ob 210/07x; vgl.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_54`)


Finanzstrafrechtlich ungeeignet sind jedenfalls Globalschätzungen oder die  Anwendung eines Sicherheitszuschlags (zB OGH 28.10.2015, 13 Os 3/15p).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_176`)


Mangels entsprechender  Beschwerde des Amtsbeauftragten, der eine Beschwerde zwar angemeldet, aber nicht  ausgeführt hat, war es aufgrund des Verböserungsverbotes des § 161 Abs. 3 FinStrG dem  Finanzstrafsenat verwehrt, den Ausspruch über die Geldstrafe und – zufolge des untrennbaren  Zusammenhangs – auch jener über die Ersatzfreiheitsstrafe aufzuheben und insoweit in der  Sache selbst zu erkennen (vgl. OGH vom 17.6.2020, 13 Os 100/19h).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_75`)


Zudem wirkt eine Bevollmächtigung jeweils nur für jenes  Verfahren, in dem sich der Bevollmächtigte entweder durch eine schriftliche Vollmacht  ausgewiesen oder sich wirksam auf die Bevollmächtigung berufen hat (vgl. OGH 5.8.2016,  2 Ob 55/16a;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_76`)


OGH 26.5.2014, 8 Ob 45/14;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_77`)


OGH 21.9.2006, 2 Ob 171/06;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_78`)


OGH 16.4.1993,  5 Ob 1020/93;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_98`)


OGH 24.03.1992, 5 Ob 25/92;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_105`)


OGH 21.9.2006, 2 Ob 171/06), sieht das BFG keine Veranlassung,  an der fehlenden Legitimation der einschreitenden Mur-Sanitär GmbH zur Erhebung des  verfahrensgegenständlichen Rechtsmittels zu zweifeln.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Mur-Sanitär GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_111`)


Eine gesicherte Rechtsprechung besteht bereits bei Vorliegen eines begründeten Erkenntnisses  (vgl. OGH 1.8.2012, 4 Ob 119/12x).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_200`)


(Vgl OGH 14.08.2014, 40/14b,  OGH 30.01.2014, 13 Os 78/13i, OGH 30.08.2012, 13 Os 70/12m)  Gemäß § 33 Abs 3 lit a zweiter Fall FinStrG ist eine Abgabenverkürzung nach § 33 Abs 1 FinStrG  bewirkt, wenn Abgaben, die bescheidmäßig festzusetzen sind, infolge Unkenntnis der  Abgabenbehörde von der Entstehung des Abgabenanspruchs mit Ablauf der gesetzlichen  Erklärungsfrist nicht festgesetzt werden konnten.

**False Positives:**

- `OGH` — no gold match — likely missing annotation
- `OGH` — no gold match — likely missing annotation
- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_203`)


(Vgl OGH 30.08.2012,  13 Os 70/12m, Pkt 2).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_5`)


demnach habe – lt. OLG und OGH – zwischen dem Bf und   DrB ein echtes und folglich gem. § 47 Abs. 2 EStG lohnsteuerpflichtiges Dienstverhältnis  bestanden.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/137334.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137334.1_68`)


sie schaffen objektives Recht (vgl. OGH 29.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_28`)


Nach Auffassung der Beschwerdeführerin stehe hingegen beiden Parteien sowohl nach den  AGB 2006 als auch nach den AGB 2011 ein Kündigungsrecht zu. Auch wenn die Möglichkeit der  ordentlichen Kündigung in den AGB nicht explizit erwähnt sei, komme der Beschwerdeführerin  (mit Hinweis auf OGH 16.1.2003, 2 Ob 3011/02) dennoch das Recht zu, den Leasingvertrag zu  kündigen.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_193`)


Nach der nach § 864a ABGB durchzuführenden Geltungskontrolle ergibt sich, dass die in Rede  stehende Klausel weder ungewöhnlich, benachteiligend oder überraschend ist (es liegt kein  „Überrumpelungs- oder gar Übertölpelungseffekt“ im Sinne der Rechtsprechung des OGH vor –  vgl etwa OGH 24.5.1989, 1 Ob 558/89);

**False Positives:**

- `OGH` — no gold match — likely missing annotation
- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_197`)


OGH  1 Ob 214/17b).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_41`)


26.11.2015, Ro 2015/07/0018; vgl auch OGH 24.11.2015,  1 Ob 127/15f).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/138133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138133.1_99`)


Gruber, ARD 6403/4/2014; vgl. idZ auch OGH 23.4.2014, 10 ObS 27/14i zu einer Nachzahlung  als laufender Bezug bei Errechnung der Zuverdienstgrenze gem. § 8 KBGG).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/139661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139661.1_112`)


26.11.2015, Ro 2015/07/0018; vgl auch OGH 24.11.2015, 1 Ob 127/15f).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/140710.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140710.1_176`)


Dies jedoch bloß  unter der Voraussetzung, dass die vermieteten Räumlichkeiten zur Zweckerfüllung dringend  benötigt werden und die vorliegende unabweisliche Notwendigkeit nur durch Aufkündigung  des Bestandverhältnisses erreicht werden kann (vgl OGH 19.1.2011, 7 Ob 242/10d).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_208`)


Andere als behinderungskausale Gründe (wie zB mangelnde oder nicht spezifische Ausbildung,  die Arbeitsplatzsituation, Arbeitswilligkeit oÄ - siehe zu einer vergleichbaren Rechtslage im  Bereich der Invaliditätspension OGH 19.9.2000, 10ObS240/00t) dürfen für die Beurteilung  ebensowenig herangezogen werden, wie eine Verschlechterung des Gesundheitszustandes  (etwa auch durch eine Verschlimmerung des Leidens oder durch Folgeschäden) nach  Vollendung des 21.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_152`)


in diesem Fall soll erst durch  die Treuhandvereinbarung die Verschiebung der wirtschaftlichen Zugehörigkeit bewirkt  werden, also der bisher auf eigene Rechnung gehaltene Geschäftsanteil in Hinkunft auf  Rechnung des Treugebers gehalten werden (vgl. OGH 28.8.2003, 8 Ob 259/02z;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/143723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143723.1_50`)


OGH 30.10.2018, 2 Ob 94/18i;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/143723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143723.1_51`)


OGH 21.9.2018,  3 Ob 149/18k, je mwN).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/144543.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144543.1_166`)


Nach der jüngsten Rechtsprechung des OGH (vgl. OGH 18.1.2023, 15 Os 111/22w, Rz 9), ist die  gegenständliche Tat sowohl unter „[...] § 146 StGB als auch § 4 Abs. 1 Wiener  Parkometergesetz 2006 subsumierbar.

**False Positives:**

- `OGH` — no gold match — likely missing annotation
- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/144695.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144695.1_6`)


Mit dem Urteil des OGH  vom 28.06.2023, 13 Os 119/22g, wurde die vom Bf. gegen das Urteil des Landesgerichtes  eingebrachte Nichtigkeitsbeschwerde zurückgewiesen).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/144916.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144916.1_52`)


erteilt wurde (vgl. OGH 13.10.1992, 10 ObS  133/92;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_162`)


der Lage ist, die Verfügung über das Fahrzeug auszuüben (OGH 18.10.2000, 9 Ob A 150/00z).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/145202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145202.1_38`)


Die Regelbedarfsätze sind abstrakte (nicht an die konkrete Einkommenssituation der Eltern  angelehnte) Werte und sollen die durchschnittlichen Grundbedürfnisse (Wohnung, Nahrung,  Kleidung etc.) eines Kindes in Österreich, gestaffelt nach dem Alter des Kindes, repräsentieren  (OGH 9.2.1995, 2 Ob 512/95).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/145809.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145809.1_139`)


Kietaibl in Tomandl, ArbVG § 29 Rz 8 bzw zur vergleichbaren Regelung nach dem BRG 1947  bereits OGH 16.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_165`)


Andere als behinderungskausale Gründe (wie zB mangelnde oder nicht spezifische Ausbildung,  die Arbeitsplatzsituation, Arbeitswilligkeit oÄ - siehe zu einer vergleichbaren Rechtslage im  Bereich der Invaliditätspension OGH 19.9.2000, 10ObS240/00t) dürfen für die Beurteilung  ebensowenig herangezogen werden, wie eine Verschlechterung des Gesundheitszustandes  (etwa auch durch eine Verschlimmerung des Leidens oder durch Folgeschäden) nach  Vollendung des 21.

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_197`)


wenn aus diesem Grund die Einleitung eines abgabenrechtlichen Verfahrens überhaupt  unterbleibt oder wegen der Verweigerung der gesetzlich vorgeschriebenen Mitwirkung des  Abgabenschuldners am Veranlagungsverfahren die Einschätzung durch das Finanzamt zu  einem zum Nachteil des Fiskus unrichtigen, der wahren wirtschaftlichen Lage des  Steuerpflichtigen nicht entsprechenden Ergebnis führt (OGH 20.10.1982, 11 Os 145, 146/82).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_198`)


Kommt eine Schätzung zum sachlich zutreffenden Ergebnis oder liegt dieses sogar über der  richtigen Bemessungsgrundlage, so kann eine Abgabenverkürzung gar nicht zustande kommen,  Die bloß verspätete Erfüllung einer Abgabenschuldigkeit ist nur bei den vom Abgabepflichtigen  selbst zu berechnenden Abgaben, z.B. bei Vorauszahlungen an Umsatzsteuer und auch hier  lediglich als Finanzordnungswidrigkeit strafbar (OGH 15.4.1982, 13 Os 182/81).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_240`)


Die Feststellungswirkung eines Schuldspruchs gegen eine natürliche Person erstreckt sich dann  auf einen Verband, wenn dieser im Verfahren gegen die natürliche Person die Möglichkeit  hatte, zu den Vorwürfen, für die er verantwortlich erklärt werden könnte, Stellung zu nehmen  und die Strafentscheidung über seinen Entscheidungsträger oder Mitarbeiter - im Umfang des  betreffenden Schuldspruchs - auf gleiche Weise wie dieser zu bekämpfen, und der  Schuldspruch sowohl gegenüber dem Verband als auch gegenüber allen weiteren  Anfechtungsberechtigten in Rechtskraft erwachsen ist (vgl OGH 19.5.2021, 13 Os 128/20b;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_242`)


Die Entscheidung hat über die Verantwortlichkeit des belangten Verbands allein für die vom  Schuldspruch gegen den Entscheidungsträger umfasste(n) Tat(en) abzusprechen [vgl. OGH  07.06.2021, 13Os3/21x (13Os4/21v)].

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/147363.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147363.1_122`)


Die Anzeigepflicht gilt für ausländische wie auch für Schischulen aus anderen  österreichischen Bundesländern in gleicher Weise (OGH 24.1.2006, 4 Ob 240/05f;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/147401.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147401.1_129`)


Die Anzeigepflicht gilt für ausländische wie auch für Schischulen aus anderen  österreichischen Bundesländern in gleicher Weise (OGH 24.1.2006, 4 Ob 240/05f;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_46`)


es ordnet nämlich die  Anwendung des § 1333 ABGB an.“; z.B. OGH 21.11.2023, 4 Ob 210/23w).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/148292.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148292.1_67`)


Demnach endet die  Rechtsfähigkeit der Limited nach Maßgabe des englischen Gesellschaftsrechts konstitutiv  bereits mit der Löschung im Gesellschaftsregister (OGH 13.9.2007, 6 Ob 146/06y).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/148971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148971.1_95`)


Nach der jüngsten Rechtsprechung des OGH (vgl. OGH 18.1.2023, 15 Os 111/22w, Rz 9), ist die  gegenständliche Tat sowohl unter "[...] § 146 StGB als auch § 4 Abs. 1 Wiener  Parkometergesetz 2006 subsumierbar.

**False Positives:**

- `OGH` — no gold match — likely missing annotation
- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_117`)


Fehlende  Selbsterhaltungsfähigkeit liegt auch bei unzureichender Altersversorgung oder bei  Pflegebedürftigkeit vor (OGH 1Ob156/97s).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_125`)


Die Heranziehung des Stammes des eigenen Vermögens muss zumutbar  sein (OGH 09.06.2009, 1Ob88/09m).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_126`)


Vermögenslosigkeit ist schon dann anzunehmen, wenn  der Unterhaltsbedürftige zwar Vermögen hat, jedoch nur solches, das zur Bestreitung des  Unterhaltes nicht verwertbar ist (OGH 07.11.1951, 2Ob718/51).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_127`)


Bei der Festsetzung des  Unterhalts ist zu berücksichtigen, dass Unterhaltsansprüche gegen Nachkommen nach der  Wertung des § 143 ABGB eher einen Ausnahmefall darstellen (OGH 21.11.2006, 4Ob192/06y;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_128`)


OGH 15.12.2009, 9Ob18/09a;

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_129`)


OGH 21.11.2006, 4Ob49/13d).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_477`)


Diese Arten von Tätigkeiten zählen typischerweise zur Führung der  Geschäfte eines Unternehmens (vgl. OGH 25.11.2020 6Ob209/20h).

**False Positives:**

- `OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Oberlandesgericht_City` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7d387332`  
**Description:**
Matches Regional High Courts with city names, ensuring 'Graz' is included.

**Content:**
```
\bOberlandesgerichts?\s+(?:Wien|Linz|Innsbruck|Salzburg|Graz|Klagenfurt|Eisenstadt|St.\s+Pölten|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|Linz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht_Handelsgericht` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `abcf145d`  
**Description:**
Matches District Courts for Commercial Matters (Handelssachen).

**Content:**
```
\bBezirksgerichts?\s+für\s+Handelssachen\s+(?:Wien|Linz|Salzburg|Innsbruck|Graz|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St.\s+Pölten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht_City_Extended` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bb537474`  
**Description:**
Matches District Courts with city names, including specific missing cities like Ried im Innkreis, Mödling, Floridsdorf, and districts.

**Content:**
```
\bBezirksgerichts?\s+(?:Melk|Steyr|Feldbach|Rohrbach|Enns|Donaustadt|Fünfthau|Innere\s+Stadt\s+Wien|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Josefstadt|Hietzing|Graz-West|Graz-Ost|Kirchdorf\s+an\s+der\s+Krems|Amstetten|Vöcklabruck|Döbling|St\.\s+Pöltten|Kufstein|Laa\s+an\s+der\s+Thaya|Schwaz|Hall|Dornbirn|Bludenz|Lustenau|Hohenems|Rankweil|Schaan|Vaduz|Balzers|Triesen|Triesenberg|Eschen|Mauren|Gamprin|Planken|Schellenberg|Au|Ruggell|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Graz|Wien|Linz|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pöltten|Schwaz|Hall|Innsbruck|Dornbirn|Bludenz|Feldkirch|Bregenz|Lustenau|Dornbirn|Hohenems|Rankweil|Schaan|Vaduz|Balzers|Triesen|Triesenberg|Eschen|Mauren|Gamprin|Planken|Schellenberg|Au|Ruggell|Ried\s+im\s+Innkreis|Mödling|Floridsdorf|Fürstenfeld|Grieskirchen|Neulengbach|Deutschlandsberg|Hermagor|Freistadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verein_Organisation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d6aad400`  
**Description:**
Matches organizations starting with 'Verein' (Association) capturing the full name.

**Content:**
```
\bVerein\s+für\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht_Grieskirchen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d4143cce`  
**Description:**
Matches District Court Grieskirchen specifically.

**Content:**
```
\bBezirksgerichts?\s+Grieskirchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PVA_Abbreviation` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f8d063bd`  
**Description:**
Matches the abbreviation PVA (Pensionsversicherungsanstalt).

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 60 | 0 | 60 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 60 | 17049 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_7`)


Angefochten ist der Einkommensteuerbescheid 2013, mit dem die lohnsteuerpflichtigen  Einkünfte [= 15.849,60 € (PVA) + 4.851,59 € (A-OG) abzgl.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Sachwalter bzw. gerichtliche Erwachsenenvertreter der Beschwerdeführerin (Bf.) stellte  am 12. Dezember 2018 folgende Anträge:   Antrag auf Zuerkennung der Familienbeihilfe für die Bf. sowie auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe wegen erheblicher Behinderung ab dem Zeitpunkt des  Eintrittes der erheblichen Behinderung, den die/der medizinische Sachverständige feststellt im  Höchstausmaß von rückwirkend fünf Jahren ab Antragstellung   mit u.a. folgenden Angaben:  Geburtsdatum: [TT/MM/1961]  Staatsbürgerschaft: Österreich   Personenstand: ledig  Für dieses Kind wird Pflegegeld bezogen: ja; seit [blank]; pflegegeldauszahlende Stelle: PVA  Den Anträgen waren Geburtsurkunde, Bestätigung der Meldung und Urkunde der Bestellung  des Sachwalters angeschlossen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_11`)


In weiterer Folge wäre seiner Gattin seitens der  Pensionsversicherungsanstalt rückwirkend die Pension für das gesamte Jahr 2011 zuerkannt  und ein diesbezüglicher Lohnzettel seitens der PVA an das Finanzamt übermittelt worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)
- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_17`)


Hinsichtlich des Jahres 2011 gab es von der PVA  vorerst nur einen Lohnzettel für die Monate Jänner bis März, darüber hinaus hat die Ehegattin  Zahlungen vom AMS bezogen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_18`)


Im Jahr 2012 wurde der Gattin des Beschwerdeführers  rückwirkend eine Pension für das gesamte Jahr 2011 zuerkannt und ein diesbezüglicher  Lohnzettel seitens der PVA an das Finanzamt übermittelt.  Dieser Sachverhalt ergibt sich aufgrund der Aktenlage, der Beschwerdeausführungen, der  Lohnzettel der PVA sowie der Bestätigungen des AMS.

**False Positives:**

- `PVA` — no gold match — likely missing annotation
- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Finanzamt`(organisation)
- `AMS`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_16`)


Am 8. August 2020 stellte Bf mit FinanzOnline einen Vorlageantrag und führte sinngemäß im  Wesentlichen Folgendes aus:  Nach seiner langjährigen Suchterkrankung habe die PVA nach mehreren abgelehnten Anträgen  und Klagen die gesundheitsbezogene Rehabilitation genehmigt und das Rehabilitationsgeld  zwar rückwirkend bis 2016 aber an die auszahlenden Stellen AMS und Sozialamt  ausbezahlt,  jedoch 2018 verbucht.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_160`)


Im Bescheid vom 30. Juni 2017 verpflichtete die Bezirkshauptmannschaft Bf sodann zum  regelmäßigen Nachweis über das Gerichtsverfahren auf Grund der Klage betreffend die  Invaliditätspension und hat Mindestsicherung bis zur Ende August 2017 erwarteten  Entscheidung der PVA zuerkannt.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_9`)


Das Finanzamt erließ daraufhin eine teilweise stattgebende Beschwerdevorentscheidung mit  im Wesentlichen folgender Begründung:  „Da betreffend der beantragten Kurkosten (2.713,50 Euro) nur eine Ablehnung auf Bewilligung  eines Kurantrages der PVA aus dem Jahr 2016 vorgelegt wurde, konnten die Kurkosten  mangels einer ärztlichen Verordnung nicht anerkannt werden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_16`)


Siehe  beiliegendesSchreiben der PVA.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_20`)


Dies ist unzutreffend, weil es eine ärztliche Verordnung gab und die PVA die Bezahlung der  Rehab ablehnte.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_21`)


Siehe Beilage „Ablehnung Heilverfahrensantrag vom 15.5.2018 der PVA"  2 von 9 Seite 3 von 9

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_28`)


Seitens der PVA sei am 18. Mai 2018 entsprechend dem Antrag für die Dauer von  29 Tagen ein Aufenthalt in der Einrichtung "YC" am Toten Meer bewilligt worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_32`)


Da die Dauer seitens der PVA als auch des DMZ für 29 Tage  angesetzt worden sei, könne auch für diesen Zeitraum eine Zwangsläufigkeit der  Aufwendungen für diese Reise und genau für diesen Zeitraum gewährt werden, aber nicht  eben für diese Verlängerung, die einem Erholungsurlaub nahekomme und somit Kosten der  Lebensführung darstelle.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_49`)


Die Kosten für den Aufenthalt am Toten Meer sei  von der PVA für den üblichen Zeitraum von 28 Tagen zum Teil übernommen worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_51`)


Seitens der PVA sei natürlich nur eine Aufenthaltsbestätigung von 28 Tagen, eben deren  Bewilligungszeitraum, ausgestellt worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_53`)


Aus der Anlage sei die Aufenthaltsbestätigung seitens PVA, der Antrag auf Verlängerung  seitens DMZ/IL und die Liste der vorgeschriebenen Arztbesuchstermine ersichtlich!

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_61`)


Seitens der PVA seien auf Grund der Regelung (zwei Aufenthalte innerhalb 5 Jahre) keine  Kosten übernommen worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_63`)


Nach Absolvierung der Behandlung in IL hätte sich der  Beschwerdeführer unverzüglich der Untersuchung einer Vertrauensärztin der PVA gestellt, um  den Heilerfolg zu bestätigen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_72`)


Im Folgenden erfolgt die Wiedergabe weiterer Details aus den Veranlagungsakten:   Einkommensteuer 2018:   < Schreiben der PVA vom 18. Mai 2018:   Bewilligung des Antrages für die Dauer von 29 Tagen am YC am Toten Meer.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_75`)


Die PVA übernimmt die Kosten für Hin- und Rückflug, Transfer sowie  Auslandskrankenversicherung (4.187,00 € lt. Rechnung vom 8.3.2018).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_88`)


Krankenstandes vom 30.1. bis 22.2.2019 zum Zwecke einer Klimabehandlung nach Sri Lanka  reist.“   < Mail vom 30. Jänner 2019 von der Krankenkasse:   „Nach Vorliegen der Einverständniserklärung ihres Dienstgebers bezüglich des Aufenthaltes im  Ausland wurde die Zeit ihres Aufenthaltes auf Sri Lanka als Krankenstandszeit als  Einzelfallentscheidung genehmigt.“   < Schreiben der PVA an den Beschwerdeführer vom 9. September 2019 betreffend  Heilverfahrensantrag vom 15.5.2019:  „Die PVA bedauert ihnen mitteilen zu müssen, dass nach medizinischer Prüfung ihrem Antrag  nicht statt gegeben werden kann.

**False Positives:**

- `PVA` — no gold match — likely missing annotation
- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_106`)


Die Kosten in Höhe von  4.187,00 € hat die PVA getragen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_112`)


< einen Klimaaufenthalt von 30.1. bis 22.2.2019 auf Sri Lanka (tatsächliche Behandlungen  konnten hier nicht nachgewiesen werden): 2.250,02 €   < einen Kuraufenthalt in Israel von 8.7. bis 5.8.2019 (tatsächliche Behandlungen konnten hier  nicht nachgewiesen werden): 5.269,88 €  Die Kosten für die Reisen im Jahr 2019 hat der Beschwerdeführer zur Gänze selbst getragen, da  seitens der PVA einem Heilverfahrensantrag nicht stattgegeben wurde.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_115`)


< Schreiben PVA vom 18.5.2018: Bewilligung Aufenthalt in Israel für 29 Tage   < Rechnungen vom YC über die Höhe der Kosten   < Rechnungen über Flug und Unterkunft auf Sri Lanka   < Mails über Krankenstand mit Ortsveränderung   < Befürwortung der Reisen durch eine Ärztin für Allgemeinmedizin  8 von 13 Seite 9 von 13

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_16`)


In Folgejahren seien Mehrfachbezüge in Österreich und auf Grundlage einer Bestätigung der  PVA wonach Krankenversicherungsbeiträge für ausländische Pensionsbezüge angefallen  waren, Werbungskosten erklärt worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_24`)


- im Zuge der Arbeitnehmerveranlagung 2017 (Einbringung der Erklärung am 21. März 2018)  sei dem Finanzamt eine Bestätigung der PVA vom 16. Februar 2018 beigelegt worden, die  neben dem ausländischen Bezug auch die darauf entfallende Krankenversicherung (§73a  ASVG) ausweise;

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_40`)


Im Gegensatz zu den Ausführungen der Behörde sei die Bestätigung der PVA der  Abgabenerklärung beigelegt worden und der Bezug einer ausländischen Rente mit zwei  weiteren Berufungen der Behörde nachgewiesen und zur Kenntnis gebracht worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_42`)


Der Arbeitnehmerveranlagung 2017 seien 2 Beilagen, einerseits die Bestätigung der PVA dass  für eine ausländische Rente Krankenversicherungsbeiträge gemäß § 73a ASVG bezahlt worden  seien und die andererseits Sonderausgaben betreffen würde, beigefügt worden.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_68`)


Die Bf. behauptet in ihrer Beschwerde vom 21. Februar 2020 ua., dass sie der Erklärung zur  Arbeitnehmerveranlagung eine Bestätigung der PVA vom 16. Februar 2018 beigelegt hat und  darin der ausländische Bezug und die darauf entfallende Krankenversicherung ausgewiesen  war.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_70`)


Das Schreiben der PVA vom 16. Februar 2018 enthält im Gegensatz zur Darstellung der Bf.  keinen (direkten) Hinweis auf ausländische Einkünfte.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_72`)


Es ist ohne Bedeutung, ob das Schreiben der PVA der Einkommensteuererklärung beigelegt  wurde oder nicht, die Bf. wäre verpflichtet gewesen, ihre Einkünfte in der  Einkommensteuererklärung 2017 (Formular L17 dazu Ausfüllhilfe L17a) darzulegen und der  Behörde damit ein klares Bild über die für die Abgabenerhebung maßgeblichen Umstände zu  verschaffen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_83`)


Eine solcher Fall läge beispielsweise dann vor, wenn der Behörde nur die Mitteilung der PVA  (Schreiben vom 16. Februar 2018) vorgelegen wäre, wonach bei der Bf. Beiträge an  Krankenversicherungen gemäß § 73a ASVG i.H.v. € 109,68 als Werbungskosten zu  berücksichtigen sind.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_22`)


Mit Schreiben vom 11.03.2021 begehrte der Bf. die Vorlage der Beschwerde gegen den  Einkommensteuerbescheid 2019 an das Bundesfinanzgericht und führte u.a. aus:   „Ich bin seit 01.08.2019 in Pension und es war nicht mein Verschulden, dass Ihnen die PVA den  Lohnzettel erst ein halbes Jahr später übermittelt hat.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/136913.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136913.1_25`)


Im Vorlagebericht beantragte das Finanzamt die Abweisung der Beschwerde, da die  Übermittelung des neuen Lohnzettels der PVA eine Änderung bei der Höhe des Einkommens  gem. § 2 Abs 2 EStG ergeben hat, die eine neue Berechnung der steuerlichen Bezüge im Zuge  der Veranlagung 2019 zur Folge hatte.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_94`)


Der Bezug der Invaliditätspension geht aus dem Schreiben der PVA vom 15.12.2021 hervor.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_47`)


Der Bf verwies darauf, dass er in seiner Beschwerde bereits Kopien des Bescheides der  PVA vom Jänner 2020 sowie eine Auflistung der einbehaltenen monatlichen Beträge für SV und  Lohnsteuer überreicht hätte.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_62`)


Der Bf wies darauf hin, dass er keine Unterlagen, Kontoauszüge bzw  Verständigungen der PVA über eventuell rückerstattete Lohnsteuerbeträge habe.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_64`)


Mit Schriftsatz vom 21.07.2022 übermittelte der Bf der Abgabenbehörde ein Schreiben mit  dem selben Datum an die Pensionsversicherungsanstalt, in dem er die Pensionsversicherung  ersuchte, aufzuklären, weshalb die einbehaltene Lohnsteuer im Lohnzettel mit 6.100,68 €  ausgewiesen werde, während in der Auflistung der monatlichen Überweisungen der PVA an  den Bf die Summe der einbehaltenen Lohnsteuer mit 6.363,21 € angegeben werde.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_71`)


Zudem verwies die Abgabenbehörde darauf,  dass der Krankenversicherungsbeitrag für die ausländische Leistung von der PVA mit 4,66 € pro  Monat (ds 55,92 € p.a.) angegeben worden sei und dieser als Werbungskosten von den  ausländischen Einkünften abzuziehen sei.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_4`)


Die Beschwerde gegen den Einkommensteuerbescheid 2020  richtet sich gegen die betragsmäßige Höhe der einbehaltenen Lohnsteuer am Lohnzettel der  Pensionsversicherungsanstalt (kurz: PVA).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_22`)


Anmerkung zum Sachverhalt: Die aktenführende Dienststelle des  Finanzamt Vorarlberg  hat sich an das für die PVA zuständige Finanzamt für Großbetriebe (kurz: FAG) mit  der Bitte um Prüfung dieses Lohnzettels gewendet.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Vorarlberg`(organisation)
- `Finanzamt für Großbetriebe`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_23`)


Das FAG hat mitgeteilt (siehe auch  Aktenteil Antwort FAG LZ Prüfung), dass die PVA im Kalenderjahr 2020 zwei Aufrollungen der  Lohnsteuer durchgeführt hat, die zu Überweisungen der zu viel einbehaltenen Lohnsteuer  geführt haben.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_25`)


Dieses Ergebnis und die Ansicht, dass eine Änderung bzw.  Korrektur des Lohnzettels der PVA nicht vorzunehmen ist, ist der Bf. seitens des Finanzamtes  mit Schreiben vom 22.11.2022 mitgeteilt worden (vgl. FA-Akt 2020/ Aktenteil Mitteilung  Ergebnis LZ Prüfung).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_43`)


Wie oben bereits ausgeführt wurde hat das FAG mitgeteilt, dass die PVA im Kalenderjahr 2020  zwei Aufrollungen der Lohnsteuer durchgeführt hat, die zu Überweisungen der zu viel  einbehaltenen Lohnsteuer geführt haben.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_45`)


Diese Ergebnis und die Ansicht, dass eine  Änderung bzw. Korrektur des Lohnzettels der PVA nicht vorzunehmen ist, ist der Bf. seitens des  Finanzamtes mit Schreiben vom 22.11.2022 mitgeteilt worden (vgl. FA-Akt 2020/ Aktenteil  Mitteilung Ergebnis LZ Prüfung).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_5`)


Im Antrag wurde angegeben, für das Kind (die Bf.) werde Pflegegeld bezogen seit … [blank];  pflegegeldauszahlende Stelle: PVA Wien.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_17`)


Beweise:  Psychiatrisch neurologisches Gutachten, Univ.-Prof-Dr. Otto L., vom 20.04.2018  Nervenfachärztliches Sachverständigengutachten Maurice Drübert  vom 28.01.2004  Behindertenpass, neu ausgestellt am 12.07.2021, unbefristet gültig  Abweisungsbescheid des Finanzamt Österreich vom 11.03.2022, ho. eingelangt am 18.03.2022  PVA: Bescheid Berufsunfähigkeitspension, vom 21.03.2019  Weiters wurde in der Beschwerde unter Pkt. 4 „Beschwerdegründe“ von der Erwachsenen- vertreterin vorgebracht, dass das Finanzamt Kenntnis gehabt habe, dass die Bf. eine  Erwachsenenvertretung habe und die gerichtliche Erwachsenenvertretung unter anderem die  Vertretung vor Behörden umfasse.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maurice Drübert`(person)
- `Finanzamt Österreich`(organisation)
- `Finanzamt`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_112`)


Das Gutachten der PVA vom 20. Februar 2019 stellt eine Behinderung seit dem ersten  Dienstverhältnis fest.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_11`)


Die Kosten werden nicht zur Gänze aus Mitteln der Kinder- und Jugendhilfe getragen, da die  betroffene Minderjährige nach ihrer verstorbenen Mutter Halbwaisenpension von der PVA  bezieht (siehe Anhang).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_29`)


Seitens der PVA wurde der minderjährigen Bf nach ihrer verstorbenen Mutter die  Halbwaisenpension sowie aufgrund ihrer chronischen Erkrankung auch Pflegegeld zuerkannt.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_118`)


Trotz  Arbeitsunfähigkeitsbescheid der PVA habe sie im April 2022 (lt. Nachweis) – ohne dauerhaften  Erfolg – versucht, einer regulären Beschäftigung nachzugehen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_10`)


In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_11`)


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SENECURA`(organisation)
- `SENECURA`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_12`)


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SENECURA`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_13`)


Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SeneCura Laurentius-Park Bludenz`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_59`)


Davon wurde ein Selbstbetrag von der PVA direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten iHv 1.086,53 Euro  überwiesen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_60`)


Der Restbetrag (lt Verständigung über die Leistungshöhe zum 01.01.2017 der PVA  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb bei der Mutter der Bf als  „Taschengeld“.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_76`)


2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.

**False Positives:**

- `PVA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `SAK_Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `93985d06`  
**Description:**
Matches the abbreviation SAK (Schweizer Ausgleichskasse).

**Content:**
```
\bSAK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizer_Ausgleichskasse_SAK` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `88d65288`  
**Description:**
Matches the full name 'Schweizer Ausgleichskasse SAK' including the abbreviation.

**Content:**
```
\bSchweizer\s+Ausgleichskasse\s+(?:SAK|\(SAK\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wien_Telekom_Betriebe_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66a6c49d`  
**Description:**
Matches the specific entity 'Wien-Telekom Betriebe GmbH'.

**Content:**
```
\bWien\-[Tt]elekom\s+Betriebe\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gesellschaft_mbh_Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `19ebbf47`  
**Description:**
Specifically matches 'Gesellschaft mbH' (lowercase g) which the generic rule might miss if the name structure is complex, e.g., 'Kress Möbel gesellschaft mbH'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vorarlberger_Gebietskrankenkasse` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `faeb40bb`  
**Description:**
Matches the specific entity 'Vorarlberger Gebietskrankenkasse'.

**Content:**
```
\bVorarlberger\s+Gebietskrankenkasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht_Spittal_Güssing_Schärding` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ec998e7c`  
**Description:**
Matches District Courts for specific missing cities: Spittal an der Drau, Güssing, Schärding.

**Content:**
```
\bBezirksgerichts?\s+(?:Spittal\s+an\s+der\s+Drau|Güssing|Schärding)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht_Krems` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a11c5340`  
**Description:**
Matches Regional Courts for Krems an der Donau.

**Content:**
```
\bLandesgerichts?\s+(?:Krems\s+an\s+der\s+Donau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Domain_Organisation` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8d2a6af2`  
**Description:**
Matches organization names ending in .at (e.g., 'Logderfurt-Logistik.at', 'YNKW Elektro.at').

**Content:**
```
\b[A-Z][a-zA-Z]+(?:[-+&][A-Z][a-zA-Z]+)*\.at\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 17044 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_63`)


Wie aus BIC.at. - die Online Plattform für  die Vermittlung von Berufsinformationen der Wirtschaftskammern- ersichtlich, befassen sich  Philologen beruflich mit klassischen und modernen Sprachen unter literatur- und  sprachwissenschaftlichen Aspekten und betreiben vergleichende Literaturwissenschaft;

**False Positives:**

- `BIC.at` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/148615.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148615.1_24`)


Siehe dazu auch die Erklärung des Bundeskanzleramtes (Quelle:  https://www.bundeskanzleramt.Rv.at/agenda/familie.html):   Familienbeihilfe:   Die Familienbeihilfe ist eines der wichtigsten Instrumente bei der Förderung von Familien in  Österreich.

**False Positives:**

- `Rv.at` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Hyphenated_Gesellschaft_mbh` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b649abaa`  
**Description:**
Matches hyphenated corporate names ending in 'Gesellschaft mbH' (lowercase), e.g., 'WienTransport Werke -GesmbH'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s*-GesmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgerichts_Leopoldstadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a858714a`  
**Description:**
Matches 'Bezirksgerichts Leopoldstadt' specifically to handle the missing case in the extended city list.

**Content:**
```
\bBezirksgerichts?\s+Leopoldstadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Slash_Separated_Corporate_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `38c29e5b`  
**Description:**
Matches corporate names with slash-separated components (e.g., 'urbanek/lind/schmied/reisch Rechtsanwälte OG').

**Content:**
```
(?<![\w])([A-Za-z]+(?:/[A-Za-z]+)+)\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft)\s+(?:OG|KG|GmbH|mbH|GmbH\s+&\s+Co\s+KG)\b
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

