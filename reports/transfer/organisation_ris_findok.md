# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-30T17:33:52.441651

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/transfer/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 800 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 640 |
| Validation documents | 160 |
| Test documents | 792 |
| Train sentences | 2892 |
| Validation sentences | 765 |
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
| Accuracy (exact match) | 84.9% |
| True Positives | 634 |
| False Positives | 748 |
| False Negatives | 17539 |
| Total Gold Entities | 18173 |
| Micro Precision | 45.9% |
| Micro Recall | 3.5% |
| Micro F1 | 6.5% |
| Macro F1 | 6.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Match Verfassungsgerichtshof` | 2.4% | 100.0% | 1.2% | 218 | 218 | 0 |
| `Match Landesgerichte (Regional Courts) - Extended` | 0.1% | 100.0% | 0.0% | 8 | 8 | 0 |
| `Match Bezirksgerichte (District Courts) - Extended Locations` | 0.0% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Match District Courts with Genitive Suffix` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Match Huber Swoboda Oswald Aixberger` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Match Pacher & Partner Rechtsanwälte GmbH & Co KG` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Match Magistrat der Stadt Wien` | 3.9% | 86.1% | 2.0% | 425 | 366 | 59 |
| `Match Oberste Gerichtshof variants` | 0.2% | 23.0% | 0.1% | 87 | 20 | 67 |
| `Match Specific Company Names with Special Characters` | 0.2% | 3.5% | 0.1% | 488 | 17 | 471 |
| `Match Oberlandesgerichte (Regional Courts of Appeal)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Handelsgerichte (Commercial Courts)` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Match District Courts (Extended Locations)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Lüneschloß&Toennessen Transport Limited` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match anwaltschriefl KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match District Courts for Commercial Matters` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Company Names with e.U. and OEG` | 0.0% | 0.0% | 0.0% | 11 | 0 | 11 |
| `Match Landesgerichte with Genitive Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Handelsgerichte with Genitive Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Associations (Verein)` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Match District Courts (Eferding, Leibnitz, Reutte, Bludenz, Vöcklabruck)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Associations (Verein) - Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match OGH abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match District Courts with Extended Locations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match LIT Daten Solutions` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Gesellschaft mbH variants` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Match Aktiengesellschaft variants` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Match Law Firms with Anwaltsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwaltsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwalts GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwalts KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwaltspartnerschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Law Firms with OG` | 0.0% | 0.0% | 0.0% | 87 | 0 | 87 |
| `Match Standard Companies (AG, GmbH, Limited, e.U., OEG, PartG, Stiftung) - Refined` | 0.0% | 0.0% | 0.0% | 34 | 0 | 34 |
| `Match Kairat Umwelt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Tessarzik Pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Graf & Pitkowitz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Wallermann Versand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Höhne, In der Maur & Partner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Bialaschewitz Touristik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Möbel Talostkel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match BergDaten GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Doschek Rechtsanwalts GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match BLS Rechtsanwälte Boller Langhammer Schubert GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Landesgerichtes Wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match WienTransport Werke -GesmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Versand Triost GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match GYP Immobilien Limited` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Poduschka Partner Anwaltsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match USW Metall Dienstleistungen AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Scheermann Forschung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Logfen Luftfahrt Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Säckel&Gaengler Robotik Gesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Partner Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Match Bollmann & Bollmann Rechtsanwaltspartnerschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Huemmer Event AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match VDIQ Sicherheit Services Aktiengesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Brandl Talos Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match RA Dr. Franz P. Oberlercher & RA Mag. Gustav H. Ortner Rechtsanwaltsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Ruggenthaler, Rest & Borsky Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Melicharek Rechtsanwalts GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Piaty Müller-Mezin Schoeller Rechtsanwälte GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Hildbrandt Immobilien AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Gabler Gibel & Ortner Rechtsanwälte GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Eger/Gründl Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Rothgeb Logistik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Harb & Postl Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match West-Sicherheit GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Likar Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Neisemeyer & Pfändler Lebensmittel -AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Fellner Wratzfeld & Partner, Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Schubert & Partner OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Schlager Rechtsanwalts KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Posch, Schausberger & Lutz Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match WGK Korp-Grünbart-Lison Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match InnHolz gesmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Graucob Pflege GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Reif und Partner Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Hoch-Bildung Vertrieb GesmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Käppeler+Baldschuhn Pflege GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Norkelnex Pharma Holding Versicherung AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Match Company Names with GmbH & Co KG - Refined` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Match Verfassungsgerichtshof` 🏆

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `75019c94`  
**Description:**
Captures the Constitutional Court in various cases (Nominative, Genitive, Dative, Accusative).

**Content:**
```
\b(Verfassungsgerichtshof|Verfassungsgerichtshofs|Verfassungsgerichtshofe|Verfassungsgerichtshöfe|Verfassungsgerichtshöfen|Verfassungsgerichtshofes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.024 | 218 | 218 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 218 | 0 | 17326 |

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

## `Match Landesgerichte (Regional Courts) - Extended` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c2d2cd23`  
**Description:**
Captures Regional Courts with city names including Eisenstadt, Mattersburg, Hall in Tirol, Korneuburg, and Spittal an der Drau, plus Graz for Zivilrechtssachen.

**Content:**
```
\b(Landesgerichts?\s+(?:f\u00fcr\s+Zivilrechtssachen\s+)?(?:f\u00fcr\s+Strafsachen\s+)?(?:Wien|Salzburg|St\.\s+P\u00f6lten|Wels|Graz|Leoben|Innsbruck|Linz|Klagenfurt|Feldkirch|Steyr|Ried\s+im\s+Innkreis|Wiener\s+Neustadt|Eisenstadt|Mattersburg|Hall\s+in\s+Tirol|Korneuburg|Krems\s+an\s+der\s+Donau|Spittal\s+an\s+der\s+Drau|Graz))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 6804 |

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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_68`)


Mit Beschluss des Landesgerichts Salzburg vom 20. August 2014 erfolgte hinsichtlich der Klemeyer + Heisterhagen Pharma GmbH die Eröffnung des Sanierungsverfahrens ohne Eigenverwaltung, welches mit Beschluss  vom 19. Dezember 2014 aufgrund der rechtskräftigen Bestätigung des Sanierungsplans  aufgehoben wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Klemeyer + Heisterhagen Pharma GmbH` (organisation)

</details>

---

## `Match Bezirksgerichte (District Courts) - Extended Locations` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3e0ecfb4`  
**Description:**
Captures District Courts with city names, including missing locations like Traun, Waidhofen an der Thaya, Oberwart, and handles genitive forms.

**Content:**
```
\b(Bezirksgerichts?\s+(?:Döbling|Purkersdorf|Josefstadt|Wien|Salzburg|Graz-West|Graz-Ost|Graz|Bregenz|Meidling|Ferlach|Wiener\s+Neustadt|Mattersburg|Eisenstadt|Hall\s+in\s+Tirol|Korneuburg|Kitzb\u00fchel|Innere\s+Stadt\s+Wien|Landeck|Liesing|Favoriten|Schwechat|Zell\s+am\s+See|Bruck\s+an\s+der\s+Mur|Linz|Innsbruck|Klagenfurt|Steyr|Feldkirch|Wels|Leoben|Hietzing|Dornbach|Simmering|Floridsdorf|Wieden|Maria\s+Einsiedel|Penzing|Rudolfsheim-F\u00fcnfhaus|Leopoldstadt|Landstra\u00dfe|W\u00e4hring|Alsergrund|Margareten|Neubau|Donaustadt|Hallein|Weiz|Urfahr|Zell\s+am\s+Ziller|Kufstein|Freistadt|St\.\s+Johann\s+im\s+Pongau|Spittal\s+an\s+der\s+Drau|St\.\s+P\u00f6lten|Melk|Mödling|F\u00fcnfhau|Baden|Schärding|Bad\s+Ischl|Neunkirchen|Grieskirchen|Gmunden|Villach|Eferding|Leibnitz|Reutte|Bludenz|Vöcklabruck|Neusiedl\s+am\s+See|Traun|Waidhofen\s+an\s+der\s+Thaya|Oberwart|Deutschlandsberg|Feldbach|Krems\s+an\s+der\s+Donau|Graz-Ost|Graz-West))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 6749 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142284.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142284.1_13`)


Es besteht daher berechtigt Grund zu der  Annahme, dass die KM nunmehr falsche Angaben macht und dies entgegen der  Vereinbarungen gemäß Unterhaltsbeschluss Bezirksgericht Wiener Neustadt vom 25.11.2019,  Zahl: 17 Pu 87/19t-86 mit der Begründung: „Vorstehende Beschlussfassung gründet sich auf  das Einverständnis der beteiligten Parteien, pflegschaftsgerichtliche Bedenken stehen nicht  entgegen“.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142284.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142284.1_30`)


Aus dieser Rechtsliteratur iVm. den tatsächlichen Gegebenheiten leitet sich für diese 2  Beschwerden ab:  1. Gemäß dem benannten geschlossenen Unterhaltsvergleich nach ON 86 vor dem  Bezirksgericht Wiener Neustadt war der Vater {hier Steuerzahler und Beschwerdeführer)  vereinbarungsgemäß berechtigt, für 2019 und 2020 den Familienbonus Plus zur Gänze geltend  zu machen, sohin EUR 3.000, - pro Jahr für beide Kinder.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

</details>

---

## `Match District Courts with Genitive Suffix` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `773ed925`  
**Description:**
Captures District Courts with city names in genitive case (e.g., 'Bezirksgerichts Salzburg') which were missed by the nominative-only pattern.

**Content:**
```
\b(Bezirksgerichts?\s+(?:D\u00f6bling|Purkersdorf|Josefstadt|Wien|Salzburg|Graz-West|Graz-Ost|Graz|Bregenz|Meidling|Ferlach|Wiener\s+Neustadt|Mattersburg|Eisenstadt|Hall\s+in\s+Tirol|Korneuburg|Kitzb\u00fchel|Innere\s+Stadt|Landeck|Liesing|Favoriten|Schwechat|Zell\s+am\s+See|Bruck\s+an\s+der\s+Mur|Linz|Innsbruck|Klagenfurt|Steyr|Feldkirch|Wels|Leoben|Hietzing|Dornbach|Simmering|Floridsdorf|Wieden|Maria\s+Einsiedel|Penzing|Rudolfsheim-F\u00fcnfhaus|Leopoldstadt|Landstra\u00dfe|W\u00e4hring|Alsergrund|Margareten|Neubau|Donaustadt|Hallein|Weiz|Urfahr|Zell\s+am\s+Ziller|Kufstein|Freistadt|Mattighofen|Graz-Ost))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 6816 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_36`)


Am **.10.2015 erfolgte am  Bezirksgericht Innere Stadt der Antrag auf die Eröffnung eines Schuldenregulierungsverfahrens  für den Bf.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt` | `Bezirksgericht Innere Stadt` |

</details>

---

## `Match Huber Swoboda Oswald Aixberger` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `73944d41`  
**Description:**
Captures the specific entity 'Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH' which was missed.

**Content:**
```
\bHuber\s+Swoboda\s+Oswald\s+Aixberger\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 8763 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_1`)


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

</details>

---

## `Match Pacher & Partner Rechtsanwälte GmbH & Co KG` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f1d414af`  
**Description:**
Captures the specific entity 'Pacher & Partner Rechtsanwälte GmbH & Co KG'.

**Content:**
```
\bPacher\s+&\s+Partner\s+Rechtsanwälte\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 5505 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/144019.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Theobald Steuder  in der Beschwerdesache Amy Benedict,  Otto-Probst-Platz 17, 4656 Wahl, Österreich, vertreten durch Pacher & Partner Rechtsanwälte GmbH & Co KG,  Kaiserfeldgasse 1/II/3.

| Predicted | Gold |
|---|---|
| `Pacher & Partner Rechtsanwälte GmbH & Co KG` | `Pacher & Partner Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Theobald Steuder` (person)
- `Amy Benedict` (person)
- `Otto-Probst-Platz 17, 4656 Wahl, Österreich` (address)

</details>

---

## `Match Magistrat der Stadt Wien` 🏆

**F1:** 0.039 | **Precision:** 0.861 | **Recall:** 0.020  

**Format:** `regex`  
**Rule ID:** `9f56aa51`  
**Description:**
Captures the specific entity 'Magistrat der Stadt Wien'.

**Content:**
```
\b(Magistrat\s+der\s+Stadt\s+Wien)\b
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

## `Match Oberste Gerichtshof variants` 🏆

**F1:** 0.002 | **Precision:** 0.230 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `856df2b4`  
**Description:**
Captures the Supreme Court (OGH) in various grammatical cases.

**Content:**
```
\b(Oberster\s+Gerichtshof|Oberste\s+Gerichtshof|Obersten\s+Gerichtshof|Obersten\s+Gerichtshofs|OGH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.230 | 0.001 | 0.002 | 87 | 20 | 67 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 67 | 17922 |

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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_49`)


Im Urteil des Landesgerichtes LG (yCgyy/yyy vom Datum_2; dieses Urteil wurde vom Obersten  Gerichtshof am Datum_1, xObxxx/xxx bestätigt) werde festgehalten, „... dass die beklagte  Partei für sämtliche zukünftigen, derzeit noch nicht bekannten Schäden ... haftet“.

| Predicted | Gold |
|---|---|
| `Obersten  Gerichtshof` | `Obersten  Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_62`)


In diesem Verfahren entschied der Oberste Gerichtshof mit Urteil vom Datum_1, xObxxx/xxx,  zugunsten der Bf als Klägerin und bestätigte das Urteil des Landesgerichtes LG vom Datum_2,  yCgyy/yyy.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_68`)


Das vom Obersten Gerichtshof bestätigte Urteil des Landesgerichtes LG diente in der Folge als  Rechtgrundlage für die weiteren Nettozahlungen der B an die Bf im streitgegenständlichen Jahr  2019.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Landesgerichtes LG` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/135942.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135942.1_28`)


Die Rechtsprechung des OGH zu der Auslegung des Begriffs „Wohnzwecke" im  Zusammenhang mit § 16 Abs 1 Z 1 MRG ist daher auch für § 33 TP 5 Abs 1 Z 4 heranzuziehen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_228`)


Dem von der Beschwerdeführerin vorgenommenen Verweis auf die Entscheidung des OGH  vom 16.1.2003, 2 Ob 311/02b, nach der sich ergebe, dass, wenn die ordentliche Kündigung  nicht erwähnt werde, dennoch auf die ordentliche Kündigung nicht verzichtet worden sei, und  das Recht zur ordentlichen Kündigung daher bestehen bleibe, tritt das Bundesfinanzgericht  damit entgegen, dass im Sachverhalt des zitierten OGH-Urteils offenbar überhaupt keine  Regelungen zur ordentlichen Kündigung getroffen wurden;

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_230`)


Darüber hinaus scheint  es einleuchtend, dass es im Fall eines Kreditkartenvertrags, zu dem die OGH-Entscheidung  erging, irgendeine Möglichkeit zur Auflösung gegeben sein muss, während im  beschwerdegegenständlichen Fall des Fahrzeugleasings ohnehin der Leasingnehmer ein  Interesse daran haben wird, den Vertrag nach einigen Jahren zu beenden, zumal der Wert des  geleasten Fahrzeugs permanent sinkt und sich die faktische Produktlebensdauer dem Ende  18 von 24 Seite 19 von 24

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/139351.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139351.1_33`)


Seines Wissens nach seien  derartige Prozesskosten "lt. OGH absetzbar", was ihm auch von Mitarbeitern des Finanzamtes  bestätigt worden sei.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/141978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141978.1_107`)


Davon  spricht man, wenn der Täter intellektuell erkannt hat, dass sein Verhalten zu einer  Steuerverkürzung führen kann und er diesen Erfolg billigend in Kauf nimmt (vgl. Kotschnigg in  Tannert/Kotschnigg, FinStrG § 33 Rz 216, und die dort zitierte OGH- bzw. VwGH- Rechtsprechung).

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_159`)


Unter dem Halter ist nach der Rechtsprechung des OGH die Person zu verstehen, die das  Fahrzeug auf eigene Rechnung in Gebrauch und die Verfügungsgewalt darüber hat.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_191`)


sie hat das Kfz somit nicht, wie es die  Rechtsprechung des OGH zum Halterbegriff erfordert (siehe oben), auf eigene Rechnung in  Gebrauch gehabt.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/147476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147476.1_47`)


Solche Vergütungs- zinsen unterliegen der dreijährigen Verjährungsfrist gemäß § 1480 ABGB (vgl. ebenfalls die  soeben zitierte OGH-Entscheidung;

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/149096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149096.1_62`)


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

## `Match Specific Company Names with Special Characters` 🏆

**F1:** 0.002 | **Precision:** 0.035 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `e18f624c`  
**Description:**
Captures company names containing special characters like +, &, or umlauts that might be missed by generic patterns, ensuring a preceding name exists.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*(?:AG|GmbH|Limited|e\.U\.|OEG|PartG|Stiftung|KG|OG)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.035 | 0.001 | 0.002 | 488 | 17 | 471 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 471 | 17923 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_4`)


Entscheidungsgründe  Mit Erkenntnis des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  14. Februar 2018, Strafnummer StrNr, wurde die nunmehrige Beschwerdeführerin Chen Kürkcü  (in der Folge kurz Bf. genannt) für schuldig erkannt, sie habe als unbeschränkt haftende  Geschäftsführerin der Fa. „XY Ltd.“ welche unbeschränkt haftende Gesellschafterin der Fa. “Z.  Ltd. & Co KG“ sei, vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes entsprechenden Voranmeldungen eine Verkürzung von Umsatzsteuer  (Vorauszahlungen oder Gutschriften) bewirkt und dies nicht nur für möglich,  sondern für  gewiss gehalten zu haben und zwar:   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Z.  Ltd. & Co KG` | `Z.  Ltd. & Co KG` |

**Missed by this rule (FN):**

- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Chen Kürkcü` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_72`)


Der GmbH wurden vom FA im Zuge von Prüfungshandlungen bis Dezember 2010  Umsatzsteuern in Gesamthöhe von ca. € 1,9 Mio aufgrund von Umsatzsteuerhinterziehungen  im Zusammenhang mit Heizölverkäufen vorgeschrieben.

**False Positives:**

- `Der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_80`)


Dies ergibt sich aus den  Einbringungsakten betreffend die GmbH.  Die oben dargestellten Abgaben wurden in weiterer Folge dem BF als Haftungspflichtigem der  GmbH mit Bescheid vom 04.07.2016 vorgeschrieben.

**False Positives:**

- `Dies ergibt sich aus den  Einbringungsakten betreffend die GmbH.  Die oben dargestellten Abgaben wurden in weiterer Folge dem BF als Haftungspflichtigem der  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_89`)


Eine Akteneinsicht in die Akten der GmbH durch den Vertreter des BF wurde frühestens im  Dezember 2016 durchgeführt.

**False Positives:**

- `Eine Akteneinsicht in die Akten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_125`)


Weitere Abgabenschulden der GmbH  sind nicht Gegenstand dieses Verfahrens.

**False Positives:**

- `Weitere Abgabenschulden der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_10`)


Am Konto der GmbH haften folgende Abgabenbeträge aus:  Umsatzsteuer 10/2017 15.12.2017 180,76  Umsatzsteuer 11/2017 15.01.2018 4.834,72  Lohnsteuer 11/2017 15.12.2017 1.398,21  Lohnsteuer 12/2017 15.01.2018 631,81  Lohnsteuer 01/2018 15.2.2018 308,73  Dienstgeberbeitrag (DB) 11/2017 15.12.2017 735,38  Dienstgeberbeitrag 12/2017 15.01.2018 300,47  Dienstgeberbeitrag 01/2018 15.02.2018 168,99  Zuschlag zum DB (DZ) 11/2017 15.12.2017 69,95  Zuschlag zum DB (DZ) 12/2017 15.01.2018 28,58  Zuschlag zum DB (DZ) 01/2018 15.02.2018 16,90  Körperschaftsteuer 01-03/2018 15.02.2018 125,00     8.799,53

**False Positives:**

- `Am Konto der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_39`)


Dazu sei festzuhalten, dass die GmbH  mangels liquider Mittel ab November 2017 überhaupt keine Zahlungen mehr geleistet habe,  sodass von einer Zahlungseinstellung auszugehen sei.

**False Positives:**

- `Dazu sei festzuhalten, dass die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_38`)


Unter der Wahrnehmung der  steuerlichen Interessen der GmbH habe er einen Nervenzusammenbruch erlitten.

**False Positives:**

- `Unter der Wahrnehmung der  steuerlichen Interessen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_39`)


Die Bf. sei in keinster Weise in die GmbH einbezogen gewesen, vielmehr habe der Sohn die  Geschäfte geführt, der Ehemann sei überwiegend im Ausland gewesen, sie habe keinen  Einblick in die steuerlichen Agenden gehabt.

**False Positives:**

- `Die Bf. sei in keinster Weise in die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_45`)


Eine  abgabenrechtliche Pflichtverletzung als Vertreterin der GmbH wird mangels Verschuldens  bestritten, da der Sohn der Bf. die tatsächliche Geschäftsführung und auch die Wahrnehmung  der steuerlichen Interessen der Primärschuldnerin übernommen habe.

**False Positives:**

- `Eine  abgabenrechtliche Pflichtverletzung als Vertreterin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_88`)


Auf Grund der Tatsache, dass die GmbH auf Grund ihrer Tätigkeit  Umsatzgeschäfte abschloss und die streitgegenständlichen Abgaben anfielen, kann auch nicht  von einer völligen Geschäftsunfähigkeit (Diskretions- und Postulationsunfähigkeit) des Bf.  ausgegangen werden.

**False Positives:**

- `Auf Grund der Tatsache, dass die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH` — partial — gold is substring of pred: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_10`)


Im Bericht der AP vom 9. Juli 2010 waren die Feststellungen betreffend die Kapitalertragsteuer  unter Tz. 2 „Verdeckte Gewinnausschüttung“ unter Hinweis auf Tz. 1 „Eingangsrechnung der  M-GmbH“ angeführt.

**False Positives:**

- `Eingangsrechnung der  M-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_21`)


Aus einem der AP vorliegenden Kontoauszug der Unter Wilkel GmbH  war ersichtlich, dass  dem Zahlungseingang, infolge der Überweisung der Bf. von Euro 180.000,00, eine  Barabhebung am nächsten Tag in nahezu gleicher Höhe (179.695,00) gegenüberstand.

**False Positives:**

- `Aus einem der AP vorliegenden Kontoauszug der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_22`)


Bei der Unter Wilkel GmbH fand im Juni 2008 eine AP statt.

**False Positives:**

- `Bei der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_25`)


Die Bf. nannte der AP als Ansprechperson bei der Unter Wilkel GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der Unter Wilkel GmbH noch deren  Vorgängerin, der P-GmbH angestellt. Die Bf. konnte den bereits in einem Schreiben vom  November 2007 erstmals erwähnten Geschäftskontakt nicht klären und war die genannte  Person, Herr K., für die AP weder im In- noch im Ausland auffindbar.

**False Positives:**

- `Die Bf. nannte der AP als Ansprechperson bei der Unter Wilkel GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)
- `Unter Wilkel GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_64`)


Die Unter Wilkel GmbH war nach Abtretung der Anteile am 15.1.2008 und  Gesellschafterwechsel Nachfolgerin der vormaligen P-GmbH. Diese war im Einzelhandel tätig  und hatte sogenannte Ein-Euro-Shops betrieben.

**False Positives:**

- `Die Unter Wilkel GmbH` — partial — gold is substring of pred: `Unter Wilkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_8`)


In der Zeit des  Bezuges des Weiterbildungsgeldes war der Bf. bei der AGmbH geringfügig und während des  restlichen Jahres vollbeschäftigt.

**False Positives:**

- `In der Zeit des  Bezuges des Weiterbildungsgeldes war der Bf. bei der AGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_47`)


Bei der AGmbH war der Bf. in der Zeit des Bezuges des  Weiterbildungsgeldes geringfügig und während des restlichen Jahres vollbeschäftigt.

**False Positives:**

- `Bei der AGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_5`)


Verfahrensverlauf  Die Beschwerdeführerin (in der Folge abgekürzt Bf) wurde unter der Firma „A-GmbH“ am 14.  Juli 1999 beim Handelsgericht Wien zu Firmenbuchnummer xxxxxxs im Firmenbuch  eingetragen.

**False Positives:**

- `A-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_39`)


Somit sei am 9. Juli 2013 eine  rechtswirksame Bescheiderlassung an die "A-GmbH" nicht mehr möglich gewesen und die  angefochtenen Bescheide der Jahre 2009 bis 2011 stellten rechtsunwirksame Nichtbescheide  dar.

**False Positives:**

- `A-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_48`)


Die vom Bf. vorgelegten Unterlagen wurden seitens des Bundesfinanzgerichts dem Finanzamt  zur Stellungnahme übermittelt.  In der Stellungnahme führte das Finanzamt aus, dass die Firma Spies&Wickert Solar GmbH geprüft worden sei  und die UIDNR.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `Finanzamt`(organisation)
- `Finanzamt`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_51`)


Im Zuge einer Betriebsprüfung in einem  anderen Unternehmen seien die Rechnungen der Firma Spies&Wickert Solar GmbH überprüft und als  Scheinrechnungen beurteilt worden.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_54`)


Alle Erhebungen der Betriebsprüfung hätten ergeben, dass die Firma Spies&Wickert Solar GmbH nur dazu diene,  Scheinrechnungen zu ermöglichen.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_58`)


Ergänzend legte das Finanzamt Teile des Betriebsprüfungsberichtes betreffend die Firma Spies&Wickert Solar GmbH in Ablichtung vor.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_60`)


Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma Spies&Wickert Solar GmbH führte der Bf. aus, dass am 29.11.2012 der Konkurs über das  Vermögen dieser Firma eröffnet und mangels Masse abgelehnt worden sei.

**False Positives:**

- `Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_62`)


es sei lediglich der Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma Ch angezweifelt worden.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — positional overlap with gold: `Spies&Wickert Solar GmbH€`
- `Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH€`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_95`)


Am 29.11.2012 wurde die Spies&Wickert Solar GmbH infolge rechtskräftiger Nichteröffnung eines  Insolvenzverfahrens mangels kostendeckenden Vermögens und Zahlungsunfähigkeit aufgelöst.

**False Positives:**

- `Wickert Solar GmbH` — partial — pred is substring of gold: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_96`)


Die UID Nummer der Firma Spies&Wickert Solar GmbH war laut Finanzamtsunterlagen mit 15.8.2012 begrenzt.

**False Positives:**

- `Die UID Nummer der Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_161`)


Wie im konkreten Fall der vorangehend geschilderten  VfGH-Rspr (mit dem Gegensatz Vorstand AG und Geschäftsführer GmbH), ist auch im  vorliegenden Fall nicht auf etwaige Unterschiede in der Zielgruppe von § 67 Abs 6 und Abs 8 lit  f EStG abzustellen, sondern auf den Unterschied zwischen freiwilligen und zwingenden  Abfertigungen.

**False Positives:**

- `Wie im konkreten Fall der vorangehend geschilderten  VfGH-Rspr (mit dem Gegensatz Vorstand AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_172`)


Errichtung einer bulgarischen Einmann-GmbH mit dem identischen Gesellschaftsnamen der  österreichischen Gesellschaft einschließlich des Zusatzes der österreichischen Rechtsform  „BergLuftfahrt  GmbH Eood“) ist geeignet Verwechslungen herbeizuführen.

**False Positives:**

- `Errichtung einer bulgarischen Einmann-GmbH` — no gold match — likely missing annotation
- `BergLuftfahrt  GmbH` — partial — gold is substring of pred: `BergLuftfahrt`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `BergLuftfahrt`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_12`)


Im Vorlageantrag vom 27. September 2019 wurde die Beschwerde wie folgt ergänzt:  „Laut unserer Mandantschaft wurde betreffend die Firma Gerstbreu Umwelt GmbH  St.Nr. 09 die  Umsatzsteuervoranmeldung für 05/2019 am 12. Juli 2019 via Finanz Online hochgeladen.

**False Positives:**

- `Laut unserer Mandantschaft wurde betreffend die Firma Gerstbreu Umwelt GmbH` — partial — gold is substring of pred: `Gerstbreu Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG` — partial — gold is substring of pred: `Kuranstalt Vigaun GmbH & Co. KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_98`)


Gutachten gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014,  Ro 2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und  2009/16/0310, vgl. auch die bei Lenneis in Csaszar/Lenneis/Wanke, FLAG, § 8 Rz 29 zitierte  Rechtsprechung).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_112`)


Es liegt am Antragsteller, das Vorliegen dieses Umstandes klar und ohne Möglichkeit eines  Zweifels nachzuweisen (vgl. VwGH 30.05.2017, Ro 2017/16/0009, vgl. auch Lenneis in  Csaszar/Lenneis/Wanke, FLAG, § 8 Rz 32).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_150`)


Lebensjahres eingetretene dauernde Unfähigkeit, sich selbst  den Unterhalt zu verschaffen, klar und ohne Möglichkeiten eines Zweifels nachzuweisen (vgl.  Lenneis, in Csaszar/Lenneis/ Wanke, FLAG, § 8 Rz 32).

**False Positives:**

- `Lenneis/ Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_24`)


Auf Grund der Judikatur des  Verwaltungsgerichtshofes ergeben sich als wesentliche Merkmale einer Berufsausbildung im  Sinne des FLAG 1967 praktischer und theoretischer Unterricht, bei dem fachspezifisches, nicht  auf Allgemeinbildung ausgerichtetes Wissen vermittelt wird, eine angemessene  Unterrichtsdauer, sowie die Verpflichtung zur Ablegung einer Abschlussprüfung.

**False Positives:**

- `Auf Grund der Judikatur des  Verwaltungsgerichtshofes ergeben sich als wesentliche Merkmale einer Berufsausbildung im  Sinne des FLAG` — partial — gold is substring of pred: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_27`)


Bei einem reinen  Berufsschulbesuch liegt eine Berufsausbildung iSd FLAG nur dann vor, wenn die volle oder  überwiegende Zeit für die Ausbildung aufgewendet wird (vgl. UFS vom 14.3.2011, RV/0363- L/09;

**False Positives:**

- `Bei einem reinen  Berufsschulbesuch liegt eine Berufsausbildung iSd FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_48`)


Kurse, stellen eine Berufsausbildung im Sinnes des FLAG 1967 da.

**False Positives:**

- `Kurse, stellen eine Berufsausbildung im Sinnes des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_307`)


Für die rückwirkende Beurteilung der Frage, wann eine psychische Erkrankung eingetreten ist  und insbesondere wann diese Erkrankung ein Ausmaß erreicht hat, dass eine Erwerbstätigkeit,  mit der sich der Patient selbst den Unterhalt verschaffen kann, nicht mehr möglich ist,  gestaltet sich daher naturgemäß sehr schwierig und kann immer nur mit hoher  Wahrscheinlichkeit und nie mit Sicherheit festgestellt werden (vgl. Lenneis/Wanke, FLAG 2020,  2. Auflage, § 8 Tz 32).

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_328`)


Voraussetzung für das Zustehen des Erhöhungsbetrages ist nach dem klaren und eindeutigen  Gesetzestext der Anspruch auf den Grundbetrag an Familienbeihilfe (vgl VwGH 30.05.2017, Ro  2017/16/0009, unter Verweis auf Lenneis in Csaszar/Lenneis/Wanke, FLAG, § 8 Rzln 5 und 19  ff).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_385`)


• Bindung an die Gutachten des Sozialministeriumservice  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die  Gutachten des Sozialministeriumservice (früher: Bundesamt für Soziales und  Behindertenwesen) gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch Lenneis/Wanke (Hrsg.), FLAG, 2. Aufl.

**False Positives:**

- `Wanke (Hrsg.), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesamt für Soziales und  Behindertenwesen`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_399`)


Lebensjahr  eingetreten ist (vgl. VwGH 04.07.2016, Ra 2016/04/0057, VwGH 30.05.2017, Ro 2017/16/0009,  vgl. auch Lenneis/Wanke (Hrsg.), FLAG, 2. Aufl., 2020, § 8 Rz 32).

**False Positives:**

- `Wanke (Hrsg.), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH` — partial — gold is substring of pred: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_122`)


NoVAG noch des KfzStG "zuzulassen" gewesen, diesfalls der Tatbestand der widerrechtlichen  Verwendung gemäß § 1 Z 3 NoVAG bzw. gemäß § 1 Abs. 1 Z 3 KfzStG jeweils nicht verwirklicht  wurde.

**False Positives:**

- `NoVAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_69`)


Im zu beurteilenden Fall sei der Zweck  einer Vermietungs-GmbH durch die Vermietung der Büro-und Geschäftsmöglichkeiten erreicht  worden.

**False Positives:**

- `Im zu beurteilenden Fall sei der Zweck  einer Vermietungs-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_18`)


Weiters wurden vom Autohaus XX GmbH nachweislich (siehe beil. Rechnungen)  gebrauchte Fahrzeuge erworben.

**False Positives:**

- `Weiters wurden vom Autohaus XX GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_39`)


Hinsichtlich des Gebrauchtwagenhandels seien im Rahmen eines  Auskunftsersuchens allein von der XGmbH für die Jahre 2013-2017 Rechnungen ausgefolgt  worden, aus denen der Verkauf von Gebrauchtwagen an den Abgabepflichtigen hervorgehe,  wobei aufgrund der Angaben der Auskunftspersonen davon auszugehen sei, dass auch bei  anderen Händlern Gebrauchtwägen zur Weiterveräußerung gekauft wurden.

**False Positives:**

- `Hinsichtlich des Gebrauchtwagenhandels seien im Rahmen eines  Auskunftsersuchens allein von der XGmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_42`)


Die vorliegende Beschwerde bringt nur ganz allgemein gehalten vor, die Y Austria GmbH habe  im Jahr 2011 alle für das Unternehmen tätigen Kundenvermittler darüber informiert, dass die  Abrechnung der Provisionen über die Schweizer Zentrale abgewickelt würde.

**False Positives:**

- `Die vorliegende Beschwerde bringt nur ganz allgemein gehalten vor, die Y Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_64`)


Csaszar/Lenneis/Wanke, FLAG 2.

**False Positives:**

- `Csaszar/Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_71`)


Lebensjahres eingetretene dauernde Unfähigkeit, sich selbst  den Unterhalt zu verschaffen, klar und ohne Möglichkeit eines Zweifels nachzuweisen (vgl.  Csaszar/Lenneis/Wanke, FLAG 2.

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `Ob eine Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_13`)


Der Bf. legte eine Aufstellung der IEF Service GmbH vom 8.8.2018 vor, aus welcher  Bruttoauszahlungen von € 4.735,91 und eine Nettoauszahlung von € 3.812,76 zu ersehen sind.

**False Positives:**

- `Der Bf. legte eine Aufstellung der IEF Service GmbH` — partial — gold is substring of pred: `IEF Service GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IEF Service GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_88`)


Aus diesem Erlass geht somit hervor, dass eine ernsthafte und zielstrebige Berufsausbildung  iSd FLAG für höchstens vier Vorbereitungsmonate bis zur jeweiligen Teilprüfung anzunehmen  ist.

**False Positives:**

- `Aus diesem Erlass geht somit hervor, dass eine ernsthafte und zielstrebige Berufsausbildung  iSd FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_9`)


Die atypisch stille Beteiligung wurde mit Zusammenschlussvertrag vom 29.9.2006 rückwirkend  zum 31.12.2005 (Art. IV UmgrStG – Zusammenschluss, was natürlich nur bei Bestehen einer  Mitunternehmerschaft relevant wäre) von der ersteBeteiligungsKG, FN  FBnummerErsteBeteilKG (abkürzt: ´AbkErsteBeteilKG´) auf die dritteBeteiligungsKG, FN  FBnummerDritteBeteilKG (abgekürzt: ´AbkDritteBeteilKG´) übertragen.

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation
- `AbkDritteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_10`)


Die ´AbkErsteBeteilKG´ hatte als Gesellschafter: KomplementärinGmbH (unbeschränkt haftend,  Komplementärin) und KommanditistGmbH (Kommanditistin).

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_11`)


Die ´AbkDritteBeteilKG´ hat dieselben Gesellschafter.

**False Positives:**

- `AbkDritteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_12`)


Die atypisch stille Beteiligung wurde am 20.11.2006 rückwirkend zum 30.6.2006 gemäß Art. III  UmgrStG (Einbringung) in die alterFirmenwortlautExGeschäftsherrin eingebracht  (Gegenleistung: Anteile für ´AbkDritteBeteilKG´).

**False Positives:**

- `AbkDritteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_13`)


Das Vermögen der ersteBeteiligungsKG, FN FBnummerErsteBeteilKG (´AbkErsteBeteilKG´)  wurde laut Firmenbucheintragung vom Februar2007 gemäß § 142 UGB von ihrer bisherigen  Kommanditistin, der KommanditistGmbH übernommen.

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_14`)


Damit ist die ersteBeteiligungsKG,  FN FBnummerErsteBeteilKG (´AbkErsteBeteilKG´) ohne Liquidation erloschen und ihre  Gesamtrechtsnachfolgerin ist die KommanditistGmbH. (Vgl. auch Ritz, BAO6, § 19 Tz 1)

**False Positives:**

- `Damit ist die ersteBeteiligungsKG,  FN FBnummerErsteBeteilKG` — no gold match — likely missing annotation
- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_19`)


Steuerliche Vorgänge und Folgerungen:  In den drei Wirtschaftsjahren, die am 31.12.2003 bzw. am 31.12.2004 bzw. am 31.12.2005  endeten, waren die alterFirmenwortlautExGeschäftsherrin, St.Nr. StNrExGeschäftsherrin sowie  die ersteBeteiligungsKG, (´AbkErsteBeteilKG´), St.Nr. StNrErsteBeteilKG zunächst die beiden  relevanten Bestandteile der hier für die Jahre 2003 bis 2005 gegenständlichen  Personenvereinigung, wobei aber – wie erwähnt – die Eigenschaft als Mitunternehmerschaft  (und damit als abgabenverfahrensrechtlich parteifähig gewesene Personenvereinigung) strittig  ist.

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_20`)


(Später wurden ca. 230 treuhändisch an der ´AbkErsteBeteilKG´ beteiligte Gesellschafter  bekannt und für die Gestaltung der Bescheide relevant.)

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_22`)


In diesen Erklärungen wurden jeweils  ein Einkünfteanteil   der St.Nr. StNrErsteBeteilKG, d.h. der ersteBeteiligungsKG, FN FBnummerErsteBeteilKG  (´AbkErsteBeteilKG´) und   der St.Nr. StNrExGeschäftsherrin, d.h. der alterFirmenwortlautExGeschäftsherrin,  FN FBnummerExGeschäftsherrin  zugewiesen.

**False Positives:**

- `AbkErsteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_25`)


In dem am 30.6.2006 beendeten Wirtschaftsjahr waren die  alterFirmenwortlautExGeschäftsherrin, FN FBnummerExGeschäftsherrin,  St.Nr. StNrExGeschäftsherrin sowie (anders als in den Vorjahren) die dritteBeteiligungsKG,  FN FBnummerDritteBeteilKG (´AbkDritteBeteilKG´), St.Nr. StNrDritteBeilKG zunächst die beiden  relevanten Bestandteile der hier für das Jahr 2006 gegenständlichen Personenvereinigung.

**False Positives:**

- `AbkDritteBeteilKG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_4`)


Diese Abgabenschuldigkeit beruht auf einer Nachforderung infolge einer bei der GmbH  durchgeführten Betriebsprüfung, bei der im Zusammenhang mit Umsatzsteuer festgestellt  worden war, dass zur Verschleierung von ausbezahlten „Schwarzlöhnen“ Rechnungen von  dubiosen Subunternehmern ohne tatsächliche Leistungserbringung als Fremdleistungsaufwand  verbucht worden seien und aus diesen Rechnungen zu Unrecht Vorsteuern geltend gemacht  worden wären.

**False Positives:**

- `Diese Abgabenschuldigkeit beruht auf einer Nachforderung infolge einer bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_108`)


Nach der geltenden Rechtslage (vgl. Lenneis/Wanke in Lenneis/Wanke, FLAG 2.

**False Positives:**

- `Nach der geltenden Rechtslage (vgl. Lenneis/Wanke in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_110`)


Geburtstag  des Kindes fällt, Familienbeihilfe zu. Hiervon normieren die Bestimmungen des § 2 Abs. 1 lit. g  bis k FLAG 1967 fünf Ausnahmen (vgl. Lenneis in Lenneis/Wanke, FLAG 2.

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_28`)


Diese  wurden allesamt von der Mutter AG (FN xxxxxxx; in der Folge kurz: Y) gezeichnet und der  gesamte Ausgabebetrag geleistet.

**False Positives:**

- `Diese  wurden allesamt von der Mutter AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_29`)


Die mit Gesellschaftsvertrag vom xx.xx.2005 als „AB GmbH“ errichtete und im Firmenbuch des  Landesgerichtes xx unter der FN xxxxxxx eingetragene Bf. erwarb am xx.xx.2006 von der Y xxxx  Stück dieser Vorzugsaktien im Nennbetrag von je Euro xxxx (gesamter Nennbetrag sohin Euro  xxxx) um einen Abtretungspreis von Euro xxxx.

**False Positives:**

- `AB GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_54`)


Die Finanzierung dieses Aktienkaufes erfolgte (zumindest teilweise) durch ein (ebenfalls) bei  der Bank AG aufgenommenes Darlehen im Betrag von Euro xxxx, dessen Einbringung durch  Verpfändung der im Rahmen der Vorzugsaktien erworbenen Zwischenscheine abgesichert  wurde.

**False Positives:**

- `Die Finanzierung dieses Aktienkaufes erfolgte (zumindest teilweise) durch ein (ebenfalls) bei  der Bank AG` — partial — gold is substring of pred: `Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bank AG`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_55`)


Gleichzeitig trat die Bf. der Bank AG mit Vereinbarung vom xx.xx.2007 die Forderungen  gegenüber der Y sowie der X aus der Optionsvereinbarung zahlungshalber ab.

**False Positives:**

- `Gleichzeitig trat die Bf. der Bank AG` — partial — gold is substring of pred: `Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bank AG`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_66`)


Die Finanzierung dieses Aktienkaufs durch ein Darlehen der Bank AG sowie die festgestellten  Sicherungsmaßnahmen, resultieren aus dem vorliegenden Darlehensvertrag samt  Verpfändungserklärung vom xx.xx.2006.

**False Positives:**

- `Die Finanzierung dieses Aktienkaufs durch ein Darlehen der Bank AG` — partial — gold is substring of pred: `Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bank AG`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_93`)


Eine  gesellschaftsrechtliche Beteiligung liegt etwa im Falle von Gesellschaftsanteilen, wie Aktien  oder GmbH-Anteilen vor, erfasst sind sohin insbesondere Dividenden und GmbH-  Gewinnausschüttungen (Strimitzer/Vock, aaO, § 10 Rz 113ff).

**False Positives:**

- `Eine  gesellschaftsrechtliche Beteiligung liegt etwa im Falle von Gesellschaftsanteilen, wie Aktien  oder GmbH-Anteilen vor, erfasst sind sohin insbesondere Dividenden und GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_224`)


Nach dem  FLAG kann ein Anspruch auf Familienbeihilfe gemäß § 2 Abs. 2 zweiter Satz leg. cit. bestehen.

**False Positives:**

- `Nach dem  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_230`)


Nach den allgemeinen Regelungen des FLAG 1967 kann – außerhalb des Anwendungsbereichs  des Unionsrechts – die Führung des Haushaltes im Ausland für den haushaltsführenden  Elternteil keinen Anspruch auf die Familienbeihilfe begründen, weil die Grundvoraussetzung  des § 2 Abs. 1 FLAG 1967, nämlich ein Wohnsitz oder der gewöhnliche Aufenthalt in  Österreich, nicht gegeben ist.

**False Positives:**

- `Nach den allgemeinen Regelungen des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_244`)


Zwischen eigenen und aus der Stellung als Familienangehöriger abgeleiteten Rechten ist bei  Ansprüchen auf Familienleistungen nicht zu unterscheiden (vgl. Csazsar in  Csazsar/Lenneis/Wanke, FLAG § 53 Rz 90 m.w.N.).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_359`)


Das FLAG 1967 spricht nicht von "leiblichen Eltern", sondern  allgemein von "Eltern" (s Nowotny in Csaszar/Lenneis/Wanke, FLAG § 2a Rz 1).

**False Positives:**

- `Das FLAG` — no gold match — likely missing annotation
- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_374`)


Darunter ist – s: etwa Art. 11 Abs. 1 VO 987/2009 – im  Sinn des nationalen Rechts nicht bloß (irgendein) Wohnsitz i. S. d. § 26 Abs. 1 BAO zu  verstehen, sondern der Mittelpunkt der Lebensinteressen (§ 2 Abs. 8 Satz 2 FLAG 1967) bzw.  der Mittelpunkt der Lebensbeziehungen (§ 1 Abs. 8 Meldegesetz) dieser Person (vgl. Czaszar in  Csaszar/Lenneis/Wanke, FLAG § 53 Rz 81, unter Hinweis auf OGH 17.

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_414`)


(vgl.  Csaszar in Csaszar/Lenneis/Wanke, FLAG, Rz 19 und 20 zu § 53).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_419`)


Für die Definition des Begriffs „Familienangehörige“ im Sinne des Unionsrechtes ist gemäß  Art. 1 lit i 1. i) VO 883/2004 § 2 Abs. 2 und 3 FLAG 1967 heranzuziehen (Csaszar in  Csaszar/Lenneis/Wanke, FLAG, § 53, Rz 92 und 102).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_436`)


IV Anwendungsbereich der VO 883/2004:  Im beschwerdegegenständlichen Zeitraum ist die Verordnung (EG) 883/2004 anzuwenden (ab  Mai 2010, vgl Csaszar in Csaszar/Lenneis/Wanke, FLAG, Rz 19 und 20 zu § 53).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_443`)


Für die Definition des Begriffs „Familienangehörige“ im Sinne des Unionsrechtes ist gemäß  Art. 1 lit i 1. i) VO 883/2004 § 2 Abs. 2 und 3 FLAG 1967 heranzuziehen (Csaszar in  Csaszar/Lenneis/Wanke, FLAG, Rz 92 und 102 zu § 53).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_451`)


(Csaszar in Csaszar/Lenneis/Wanke, FLAG, Rz 45 zu § 53).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_458`)


(Csaszar in Csaszar/Lenneis/Wanke,  FLAG, Rz 46 zu § 53).

**False Positives:**

- `Lenneis/Wanke,  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_52`)


(siehe zu vor in: Lenneis/Wanke, FLAG-Kommentar, 2. Aufl., Rzen.

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_62`)


In diesem Zusammenhalt liegt eine Berufsausbildung iSd FLAG nach der Rechtsprechung des  Bundesfinanzgerichtes (BFG) – analog zum Besuch einer AHS oder BHS – generell nur dann vor,  wenn ein wöchentlicher Zeitaufwand für Kurse und Vorbereitungen von mindestens  30 Stunden anfällt. Das BFG nimmt bei Schulen für Berufstätige einen erforderlichen  wöchentlichen Zeitaufwand von durchschnittlich 20 bis 25 Stunden zuzüglich Hausaufgaben an,  dh. insgesamt einen Zeitaufwand von mindestens 30 Wochenstunden, um von einer  Berufsausbildung iSd FLAG zu sprechen (vgl. BFG 19.10.2017, RV/7102012/2016;

**False Positives:**

- `In diesem Zusammenhalt liegt eine Berufsausbildung iSd FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_74`)


Eine Berufsausbildung iSd FLAG war daher nach Beendigung der praktischen Lehrausbildung,  mangels Erfüllung der quantitativen/zeitlichen Komponente, nicht mehr gegeben.

**False Positives:**

- `Eine Berufsausbildung iSd FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_51`)


Die Materialien zum WWAG würden folgende Klarstellung vorsehen:  „…Mit der Formulierung „unmittelbar die Teilnahme an einer Wette ermöglicht“ soll klargestellt  werden, dass jene technischen Geräte, wo ausschließlich Personal des jeweiligen Unternehmens  für die Kundin und den Kunden Wetten eingeben kann, keine Wettterminals im Sinne des  Gesetzes darstellen (so z.B. in Trafiken, wo die Eingabe der Wette ausschließlich durch das  Verkaufspersonal erfolgt und der Annahmeschalter für Kundinnen und Kunden nicht frei  zugänglich sei).“

**False Positives:**

- `Die Materialien zum WWAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_65`)


Das  WWAG sehe vor, dass für das Halten eines Wettterminals eine Abgabe zu entrichten sei.

**False Positives:**

- `Das  WWAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_13`)


Die GmbH habe letztmalig im April 2008 Erlöse aus ihrer Handelstätigkeit erzielt. Seither seien  lediglich die Mieteinnahmen erklärt worden.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_69`)


Von der GmbH wird ein Büroraum mit einer Größe von 16 m² im Erdgeschoß betrieblich  genutzt.

**False Positives:**

- `Von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_76`)


Dieser Mitteilung kommt jedoch kein  Bescheidcharakter zu (Lenneis in Lenneis/Wanke, FLAG, 2. Aufl., § 12 Rz 5);

**False Positives:**

- `Dieser Mitteilung kommt jedoch kein  Bescheidcharakter zu (Lenneis in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/133037.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133037.1_11`)


Von den von der Haarmann+Noppeney Analyse GmbH und von der Fa. Y-GmbH in den Jahren 2010 bis 2012 in  Rechnung gestellten Beträgen seien im Schätzungswege lediglich 50% als Aufwand  anzuerkennen;

**False Positives:**

- `Von den von der Haarmann+Noppeney Analyse GmbH und von der Fa. Y-GmbH` — partial — gold is substring of pred: `Haarmann+Noppeney Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Haarmann+Noppeney Analyse GmbH`(organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_51`)


Würdigung:  Nach der Rechtsprechung des VwGH hängt die Antwort, inwieweit die Unterhaltskosten für die  Kinder überwiegend getragen werden, davon ab, ob überwiegend der Geldunterhalt geleistet  wurde (Reinalter in Lenneis/Wanke, FLAG 2.A. 2020 § 2 Rz 152 unter Hinweis VwGH  22.12.2011, 2011/16/0068 und VwGH 24.2.2010, 2009/13/0241).

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_23`)


Die  Barzahlungen an die Scheinfirma Y-Montage GmbH in Höhe von € 35.000,- erfolgten auch in  diesem Zeitraum, sodaß sich beim Verkauf der GmbH ein Kassastand von nur mehr € 8.724,-  ergab.

**False Positives:**

- `Die  Barzahlungen an die Scheinfirma Y-Montage GmbH` — partial — gold is substring of pred: `Y-Montage GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Y-Montage GmbH`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_26`)


Gesellschafter der Nexlex GmbH waren zu dieser Zeit auch  Hr. Beschwerdeführer und Hr. K.. Hr. K. war zu dieser Zeit gleichzeitig bei der  Beschwerdeführer GmbH als Bauleiter beschäftigt.

**False Positives:**

- `Gesellschafter der Nexlex GmbH` — partial — gold is substring of pred: `Nexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexlex GmbH`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_32`)


Alle steuerrelevanten Feststellungen sind im Zeitraum vor dem Verkauf der GmbH im  Jahre 2009 angesiedelt, sodaß die Haftung den ehemaligen Geschäftsführer, Hr. Patrick Kirschbauer,  trifft.

**False Positives:**

- `Alle steuerrelevanten Feststellungen sind im Zeitraum vor dem Verkauf der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Patrick Kirschbauer`(person)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_96`)


Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH eingesetzt als Subunternehmer im Jahr 2009 um  Scheinfirmen handelt im vollen Umfang zurück gewiesen.

**False Positives:**

- `Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH` — partial — gold is substring of pred: `Fa.POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.POU Bau GmbH`(organisation)
- `Y-Montage GmbH`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_98`)


Bei der Fa. Z- Bau Bau GmbH, kann dies sicher auch der damalige Auftraggeber der Bauvorhaben I-Straße,  9998 Wien und F-Gasse, 9997 Wien, die Fa. Zimmerei Groschang Holz GmbH  bestätigen.

**False Positives:**

- `Bei der Fa. Z- Bau Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Groschang Holz GmbH`(organisation)

</details>

---

## `Match Oberlandesgerichte (Regional Courts of Appeal)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1b37f16c`  
**Description:**
Captures Regional Courts of Appeal with city names.

**Content:**
```
\b(Oberlandesgerichts?\s+(?:Graz|Linz|Wien|Salzburg|Innsbruck|Klagenfurt|Vienna))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Handelsgerichte (Commercial Courts)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `96c70ec3`  
**Description:**
Captures Commercial Courts.

**Content:**
```
\b(Handelsgerichts?\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 17839 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_44`)


Nach Einbringung eines Vorlageantrages ohne ergänzendem Vorbringen ersuchte das  Bundesfinanzgericht den Bf. den Sachverhalt betreffend die Gerichtsverfahren beim  Handelsgericht Wien und beim Arbeitsgericht darzulegen und mit entsprechenden  Beweismitteln nachzuweisen;

**False Positives:**

- `Handelsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_5`)


Verfahrensverlauf  Die Beschwerdeführerin (in der Folge abgekürzt Bf) wurde unter der Firma „A-GmbH“ am 14.  Juli 1999 beim Handelsgericht Wien zu Firmenbuchnummer xxxxxxs im Firmenbuch  eingetragen.

**False Positives:**

- `Handelsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_23`)


Darüberhinaus sprechen auch die zum Zeitpunkt der vom Masseverwalter in der  Schlussrechnung/Verteilungsentwurf an das Handelsgericht Wien vom 6. Oktober 2011 über die  oa. Firma "Stein" angeführten gemeldeten "rund 500 Mitarbeiter" von der tatsächlichen  Ausführung der in den Rechnungen angeführten Leistungen, welche von der gegenständlichen  Firma "OStR Dipl. Kff. Martha Mattiesen" schließlich auch bezahlt wurden (bar).

**False Positives:**

- `Handelsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Dipl. Kff. Martha Mattiesen`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/140219.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140219.1_92`)


Die Ersteintragung der Bf erfolgte am 30. Dezember 1980 beim Handelsgericht  Wien, HRB Zahl, unter dem Firmenwortlaut KzlR Hedwig Gröpler, Bakk. phil.  Mit Einbringungsvertrag vom 30.  September 1981 wurde das Vermögen der Vorgängergesellschaft, der A-OHG, gemäß den  Bestimmungen des Strukturverbesserungsgesetztes in die Bf eingebracht.

**False Positives:**

- `Handelsgericht  Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KzlR Hedwig Gröpler, Bakk. phil.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/144019.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144019.1_37`)


Mit Beschluss des Handelsgerichts Wien vom 30.12.2016 (28 S 180/16y) wurde über das  Vermögen der Beschwerdeführerin der Konkurs eröffnet.

**False Positives:**

- `Handelsgerichts Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/144019.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144019.1_38`)


Mit Beschluss des Handelsgerichts Wien vom 27.3.2019 wurde der Konkurs nach Verteilung an  die Massegläubiger aufgehoben.

**False Positives:**

- `Handelsgerichts Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/148949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148949.1_17`)


Mit Beschluss des Handelsgerichts Wien vom 14. August 1998  wurde über die  Primärschuldnerin das Konkursverfahren eröffnet.

**False Positives:**

- `Handelsgerichts Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `14. August 1998`(date)

</details>

---

## `Match District Courts (Extended Locations)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9fa08fdf`  
**Description:**
Captures District Courts with city names, including hyphenated suffixes and previously missing locations like Landeck, Liesing, Favoriten, Schwechat, and multi-word locations.

**Content:**
```
\b(Bezirksgerichts?\s+(?:D\u00f6bling|Purkersdorf|Josefstadt|Wien|Salzburg|Graz-West|Graz-Ost|Graz|Bregenz|Meidling|Ferlach|Wiener\s+Neustadt|Mattersburg|Eisenstadt|Hall\s+in\s+Tirol|Korneuburg|Kitzb\u00fchel|Innere\s+Stadt\s+Wien|Landeck|Liesing|Favoriten|Schwechat|Zell\s+am\s+See|Bruck\s+an\s+der\s+Mur|Linz|Innsbruck|Klagenfurt|Steyr|Feldkirch|Wels|Leoben|Hietzing|Dornbach|Simmering|Floridsdorf|Wieden|Maria\s+Einsiedel|Penzing|Rudolfsheim-F\u00fcnfhaus|Leopoldstadt|Landstra\u00dfe|W\u00e4hring|Alsergrund|Margareten|Neubau|Donaustadt|Hallein|Weiz|Urfahr|Zell\s+am\s+Ziller|Kufstein|Freistadt|St\.\s+Johann\s+im\s+Pongau|Spittal\s+an\s+der\s+Drau|St\.\s+P\u00f6lten|Melk|M\u00f6dling|F\u00fcnfhau|Baden|Sch\u00e4rding|Saalfelden))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Lüneschloß&Toennessen Transport Limited` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f4d8f382`  
**Description:**
Captures the specific entity 'Lüneschloß&Toennessen Transport Limited'.

**Content:**
```
\b(L\u00fcneschlo\u00df&Toennessen\s+Transport\s+Limited)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match anwaltschriefl KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e0dc0954`  
**Description:**
Captures the specific entity 'anwaltschriefl KG'.

**Content:**
```
\b(anwaltschriefl\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match District Courts for Commercial Matters` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5c118368`  
**Description:**
Captures 'Bezirksgericht für Handelssachen Wien' and its genitive form.

**Content:**
```
\b(Bezirksgerichts?\s+f\u00fcr\s+Handelssachen\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Company Names with e.U. and OEG` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7d9d00f6`  
**Description:**
Captures companies ending in e.U. (Einzelunternehmer) and OEG (Offene Gesellschaft für das gesamte Vermögen) which are common in Austrian legal texts.

**Content:**
```
(?<![a-zA-Z])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*(?:e\.U\.|OEG))\b(?!\s+(?:in|von|mit|gegen|auf|bei|nach|\u00fcber|unter|aus|zu|als|durch|vertreten|Partei|Gesellschafter|Schuldner|Kl\u00e4ger|Beklagte|Antragsgegner|Antragsteller|Verfahren|Rechtssache|Sache|Gericht|Bezirksgericht|Landesgericht|Oberlandesgericht|Oberster Gerichtshof|Handelsgericht|Verwaltungsgericht|Verfassungsgerichtshof|VwGH|VfGH|Finanzgericht|Bundesgericht|Bundesverwaltungsgericht|Bundesgerichtshof|Arbeitsgericht|Sozialgericht|Gerichtshof|Senat|Kammer|Abteilung|Instanz|Rechtsmittel|Revisionsrekurs|Rekurs|Berufung|Klage|Urteil|Beschluss|Entscheidung|Verf\u00fcgung|Prozess|Recht|Rechtsstreit|Rechtsangelegenheit|Rechtsfrage|Rechtsverh\u00e4ltnis|Rechtsverletzung|Rechtsfolge|Rechtsanspruch|Rechtsbehelf|Rechtskraft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 11 | 14685 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Die beschwerdeführende Kommanditgesellschaft (Beschwerdeführerin, Bf.) hatte laut  Firmenbuch (FN Firmenbuchnummer) bis 28.9.2012 die Firmenbezeichnung  ursprFirmenwortlautOEG und sodann bis 9.7.2016 die Firmenbezeichnung  zwischenzeitlFirmenwortlautKG gehabt.

**False Positives:**

- `Firmenbezeichnung  ursprFirmenwortlautOEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_23`)


Die tatsächlichen Zahlungen der monatlichen Betriebskosten  seien aber vorerst von der S-OEG getätigt bzw. über das Verrechnungskonto der Bf verbucht  worden.

**False Positives:**

- `Zahlungen der monatlichen Betriebskosten  seien aber vorerst von der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_28`)


Tatsächliche  Zahlungen seien nur vereinzelt vom Bankkonto der S-OEG erfolgt.

**False Positives:**

- `Zahlungen seien nur vereinzelt vom Bankkonto der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_31`)


VJ 0,00 311,08 13.085,52 29.759,96 46.434,40  Zahlungen OEG 4.816,66 3.900,00 0,00 0,00 0,00  Forderung  31.12.

**False Positives:**

- `Zahlungen OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_35`)


In den Jahren 2007 und 2008 seien weitere Wohnungen für Arbeitnehmer der S-OEG  und weiterer verbundener Unternehmen angeschafft worden.

**False Positives:**

- `Arbeitnehmer der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_85`)


Die tatsächlichen Zahlungen der monatlichen Betriebskosten wurden vorerst von der S-OEG  getätigt bzw. über das Verrechnungskonto verbucht.

**False Positives:**

- `Zahlungen der monatlichen Betriebskosten wurden vorerst von der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_91`)


Tatsächliche Zahlungen/Überweisungen erfolgten nur vereinzelt vom Bankkonto der S-OEG  (Gesellschafter die Brüder MS und WS).

**False Positives:**

- `Bankkonto der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_95`)


VJ 0,00 311,08 13.085,52 29.759,96 46.434,40  Zahlungen OEG 4.816,66 3.900,00 0,00 0,00 0,00  Forderung  31.12.

**False Positives:**

- `Zahlungen OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_110`)


Die Mietzinszahlungen in den Jahren 2004 und 2005 wurden nicht von Herrn MS,  sondern von der S-OEG getätigt.

**False Positives:**

- `Herrn MS,  sondern von der S-OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_31`)


Mit Gesellschaftsvertrag vom 15./16.05.2006 wurde die M OEG (nunmehr M OG; LG Klagenfurt  zu FN xxxxxxx) (erneut) mit dem Sitz in der politischen Gemeinde Adresse und der Adresse in  Adresse Adresse von Ing. BB (geb. xx.xx.xxxx;

**False Positives:**

- `M OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `LG Klagenfurt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_390`)


Gründung, Gesellschafter  Im Mai 2006 gründeten die Gesellschafter der Bf (= Gesellschafter der Holding= drei Strategen)  auch die OG, deren alleinige Gesellschafter sie waren (OEG-Gesellschaftsvertrag vom  16.5.2006).

**False Positives:**

- `Strategen)  auch die OG, deren alleinige Gesellschafter sie waren (OEG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Match Landesgerichte with Genitive Suffix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2bd66946`  
**Description:**
Captures Regional Courts with city names in genitive case (e.g., 'Landesgerichts Salzburg') and specific types like 'für Zivilrechtssachen'.

**Content:**
```
\b(Landesgerichts?\s+(?:f\u00fcr\s+Zivilrechtssachen\s+)?(?:f\u00fcr\s+Strafsachen\s+)?(?:Wien|Salzburg|St\.\s+P\u00f6lten|Wels|Graz|Leoben|Innsbruck|Linz|Klagenfurt|Feldkirch|Steyr|Ried\s+im\s+Innkreis|Wiener\s+Neustadt|Eisenstadt|Mattersburg|Hall\s+in\s+Tirol|Korneuburg|Krems\s+an\s+der\s+Donau|Graz))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Handelsgerichte with Genitive Suffix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `90b67c05`  
**Description:**
Captures Commercial Courts in genitive case (e.g., 'Handelsgerichts Wien').

**Content:**
```
\b(Handelsgerichts?\s+(?:Wien|Korneuburg))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Associations (Verein)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0be7101c`  
**Description:**
Captures associations starting with 'Verein' or 'Verband'.

**Content:**
```
\b(Verein\s+[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*|Verband\s+[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 15644 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_306`)


Die DRV stellt sich auf ihrer Web-Site (www.deutsche-rentenversicherung.de) selbst als  Zusammenschluss der Bundesversicherungsanstalt für Angestellte und dem Verband Deutscher  Rentenversicherungsträger dar, der die gesetzliche Rentenversicherung als Gesamtheit vertritt.

**False Positives:**

- `Verband Deutscher  ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133179.1_2`)


Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse 17, 1010 Wien, über die Beschwerde vom 24. Februar 2021 gegen die  Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 17. Juli 2020  betreffend  - Umsatzsteuer für die Jahre 2012 bis 2016 sowie  - Wiederaufnahme betreffend Umsatzsteuer für die Jahre 2012 bis 2016  zu Recht:  I. Der Beschwerde gegen die Wiederaufnahmsbescheide betreffend Umsatzsteuer 2012 bis  2016 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse ` — partial — gold is substring of pred: `Annkathrin Cattus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Annkathrin Cattus`(person)
- `AUDITREU Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/144724.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144724.1_29`)


Seine Lebenssituation in Österreich beschrieb der Bf den FinPol-Organen so:  Er sei bei der Firma A in Kärnten als Lagerarbeiter vollzeitbeschäftigt und spiele in seiner  Freizeit beim Club-B Fußball bzw. im Winter zudem beim Verein Sportclub-C.

**False Positives:**

- `Verein Sportclub-C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146475.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146475.1_254`)


Kostenentscheidung  Die Verfahrenskosten in Höhe von € 500,00 für den Beschuldigten und € 350,00 für den  belangten Verband Springholz  gründen sich auf § 185 Abs. 1 lit. a FinStrG, wonach pauschal ein  Kostenersatz im Ausmaß von 10% der verhängten Geldstrafe, maximal aber ein Betrag von  € 500,00 festzusetzen ist.

**False Positives:**

- `Verband Springholz  ` — partial — gold is substring of pred: `Springholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Springholz`(organisation)

</details>

---

## `Match District Courts (Eferding, Leibnitz, Reutte, Bludenz, Vöcklabruck)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3b6e7723`  
**Description:**
Captures District Courts with specific missing locations in nominative and genitive forms.

**Content:**
```
\b(Bezirksgerichts?\s+(?:Eferding|Leibnitz|Reutte|Bludenz|V\u00f6cklabruck))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Associations (Verein) - Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e60558f9`  
**Description:**
Captures associations starting with 'Verein' or 'Verband', excluding cases where 'Verein' is preceded by 'Partei'.

**Content:**
```
(?<![a-zA-Z])(Verein\s+[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*|Verband\s+[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match OGH abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb4fc99a`  
**Description:**
Captures the Supreme Court abbreviation 'OGH' specifically to prevent it from being matched as part of a larger phrase like 'Gericht OGH'.

**Content:**
```
\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match District Courts with Extended Locations` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9af24870`  
**Description:**
Captures District Courts with city names, including hyphenated suffixes and previously missing locations like Landeck, Liesing, Favoriten, Schwechat, and multi-word locations.

**Content:**
```
\b(Bezirksgerichts?\s+(?:D\u00f6bling|Purkersdorf|Josefstadt|Wien|Salzburg|Graz-West|Graz-Ost|Graz|Bregenz|Meidling|Ferlach|Wiener\s+Neustadt|Mattersburg|Eisenstadt|Hall\s+in\s+Tirol|Korneuburg|Kitzb\u00fchel|Innere\s+Stadt\s+Wien|Landeck|Liesing|Favoriten|Schwechat|Zell\s+am\s+See|Bruck\s+an\s+der\s+Mur|Linz|Innsbruck|Klagenfurt|Steyr|Feldkirch|Wels|Leoben|Hietzing|Dornbach|Simmering|Floridsdorf|Wieden|Maria\s+Einsiedel|Penzing|Rudolfsheim-F\u00fcnfhaus|Leopoldstadt|Landstra\u00dfe|W\u00e4hring|Alsergrund|Margareten|Neubau|Donaustadt|Hallein|Weiz|Urfahr|Zell\s+am\s+Ziller|Kufstein|Freistadt|St\.\s+Johann\s+im\s+Pongau))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match LIT Daten Solutions` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a6738a45`  
**Description:**
Captures the specific entity 'LIT Daten Solutions' which was missed.

**Content:**
```
\b(LIT\s+Daten\s+Solutions)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Gesellschaft mbH variants` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `caee1f0a`  
**Description:**
Captures 'Gesellschaft mbH' and 'gesellschaft mbH' with strict boundaries, allowing '&' and broader prefixes.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Gesellschaft\s+mbH|[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*gesellschaft\s+mbH)\b(?!\s+(?:in|von|mit|gegen|auf|bei|nach|\u00fcber|unter|aus|zu|als|durch|vertreten|Partei|Gesellschafter|Schuldner|Kl\u00e4ger|Beklagte|Antragsgegner|Antragsteller|Verfahren|Rechtssache|Sache|Gericht|Bezirksgericht|Landesgericht|Oberlandesgericht|Oberster Gerichtshof|Handelsgericht|Verwaltungsgericht|Verfassungsgerichtshof|VwGH|VfGH|Finanzgericht|Bundesgericht|Bundesverwaltungsgericht|Bundesgerichtshof|Arbeitsgericht|Sozialgericht|Gerichtshof|Senat|Kammer|Abteilung|Instanz|Rechtsmittel|Revisionsrekurs|Rekurs|Berufung|Klage|Urteil|Beschluss|Entscheidung|Verf\u00fcgung|Prozess|Recht|Rechtsstreit|Rechtsangelegenheit|Rechtsfrage|Rechtsverh\u00e4ltnis|Rechtsverletzung|Rechtsfolge|Rechtsanspruch|Rechtsbehelf|Rechtskraft|Dr\.\s+[A-Z]|Mag\.\s+[A-Z]|MMag\.\s+[A-Z]))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 17222 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_38`)


Zu der vermeintlich formalen  Meldung sei festgehalten, dass es sich bei der Bf. um eine Gesellschaft mbH handelt, an der  neben drei natürlichen Personen auch zwei Gesellschaften mit begrenzter Haftung beteiligt  sind.

**False Positives:**

- `Zu der vermeintlich formalen  Meldung sei festgehalten, dass es sich bei der Bf. um eine Gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/140870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140870.1_44`)


Im Streitjahr war der BF bei der S Gesellschaft mbH vom 01.01.2016 bis 05.01.2016 und vom  01.03.2016 bis 30.12.2016 als Kraftfahrer beschäftigt und bezog Einkünfte aus  nichtselbstständiger Arbeit.

**False Positives:**

- `Im Streitjahr war der BF bei der S Gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Match Aktiengesellschaft variants` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a2743b45`  
**Description:**
Captures 'Aktiengesellschaft' and 'AG' variants with strict boundaries, preventing capture of preceding legal context.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Aktiengesellschaft|[A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*AG)\b(?!\s+(?:in|von|mit|gegen|auf|bei|nach|\u00fcber|unter|aus|zu|als|durch|vertreten|Partei|Gesellschafter|Schuldner|Kl\u00e4ger|Beklagte|Antragsgegner|Antragsteller|Verfahren|Rechtssache|Sache|Gericht|Bezirksgericht|Landesgericht|Oberlandesgericht|Oberster Gerichtshof|Handelsgericht|Verwaltungsgericht|Verfassungsgerichtshof|VwGH|VfGH|Finanzgericht|Bundesgericht|Bundesverwaltungsgericht|Bundesgerichtshof|Arbeitsgericht|Sozialgericht|Gerichtshof|Senat|Kammer|Abteilung|Instanz|Rechtsmittel|Revisionsrekurs|Rekurs|Berufung|Klage|Urteil|Beschluss|Entscheidung|Verf\u00fcgung|Prozess|Recht|Rechtsstreit|Rechtsangelegenheit|Rechtsfrage|Rechtsverh\u00e4ltnis|Rechtsverletzung|Rechtsfolge|Rechtsanspruch|Rechtsbehelf|Rechtskraft|Dr\.\s+[A-Z]|Mag\.\s+[A-Z]|MMag\.\s+[A-Z]|Prof\.\s+[A-Z]|Univ\.\-Prof\.\s+[A-Z]))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 905 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_218`)


Bei der Aktiengesellschaft haben die Gesellschafter gem. § 221  AktG Mitbestimmungsrechte bei einer Verschmelzung.

**False Positives:**

- `Bei der Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Match Law Firms with Anwaltsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `83229b3c`  
**Description:**
Captures law firms ending in 'Anwaltsgesellschaft mbH' or 'Anwaltsgesellschaft GmbH' with strict boundaries to avoid preceding names.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*?Anwaltsgesellschaft\s+(?:mbH|GmbH))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwaltsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b8040432`  
**Description:**
Captures law firms ending in 'Rechtsanwaltsgesellschaft mbH' or 'Rechtsanwaltsgesellschaft GmbH' with strict boundaries.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*?Rechtsanwaltsgesellschaft\s+(?:mbH|GmbH))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `38b4d07e`  
**Description:**
Captures law firms ending in 'Rechtsanwälte GmbH' or 'Rechtsanwälte mbH' with a preceding name, avoiding partial matches.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Rechtsanwälte\s+(?:GmbH|mbH)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwalts GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bd94b1c4`  
**Description:**
Captures law firms ending in 'Rechtsanwalts GmbH' or 'Rechtsanwalts mbH'.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Rechtsanwalts\s+(?:GmbH|mbH)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwalts KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `daf0aded`  
**Description:**
Captures law firms ending in 'Rechtsanwalts KG'.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Rechtsanwalts\s+KG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwaltspartnerschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d159eb2`  
**Description:**
Captures law firms ending in 'Rechtsanwaltspartnerschaft'.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Rechtsanwaltspartnerschaft\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b9bef76b`  
**Description:**
Captures law firms ending in 'Rechtsanwälte OG' or 'Rechtsanwalts OG'.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*Rechtsanw\u00e4lte\s+OG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Law Firms with OG` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `734c7c9d`  
**Description:**
Captures law firms ending in 'OG' (Offene Gesellschaft) that are not 'Rechtsanwälte OG'.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*OG)\b(?!\s+(?:Rechtsanw\u00e4lte|Rechtsanwalts))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 87 | 11883 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_33`)


Nach der Rückkehr aus der Schweiz zog der Bf wieder in sein Elterhaus ein (Einfamilienhaus mit  einer Wohneinheit – EG mit Küche/Wohnzimmer, OG mit 3 Schlafzimmern) und bewohnt dort  seither - planmäßig bis zu seiner Gesundung - gegen einen Unkostenbeitrag ein Gästezimmer.

**False Positives:**

- `Wohnzimmer, OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_37`)


Die OG, die in den Streitjahren keine Dienstnehmer beschäftigte, leaste einerseits drei  Kraftfahrzeuge im eigenen Namen und auf eigene Rechnung und hielt andererseits  Wertpapiere in ihrem Betriebsvermögen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_54`)


Die OG erzielte in den Streitjahren weitere Umsätze aus der Erbringung von  Managementleistungen der 2 GmbH (FN xxxxxxx), der (vormaligen) 3 Bau GmbH (FN xxxxxxx),  der (vormaligen) 4 GmbH (FN xxxxxxx), der (vormaligen) 5 GmbH (FN xxxxxxx), und der 6 GmbH  (FN xxxxxxx, seit 06.04.2023:Reitzenstein Bildung GmbH  gegenüber, auf Basis – mit Ausnahme der Entlohnung -  inhaltsgleicher Managementvereinbarungen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `:Reitzenstein Bildung GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_64`)


Der festgestellte Inhalt des Gesellschaftsvertrages der OG geht aus der im Akt erliegenden  Vertragskopie hervor.

**False Positives:**

- `Der festgestellte Inhalt des Gesellschaftsvertrages der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_76`)


Unstrittig ist, dass Leistungen auf Basis der Managementvereinbarung/des  Managementvertrages von den Gesellschaftern der OG auch für die Bf. erbracht wurden.

**False Positives:**

- `Unstrittig ist, dass Leistungen auf Basis der Managementvereinbarung/des  Managementvertrages von den Gesellschaftern der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_94`)


Fakt ist, dass zwischen  der Bf. einerseits und der OG bzw. dessen (unter 25% beteiligten) Gesellschaftern Ing. AA und  CC andererseits, eine (persönliche) Weisungsungebundenheit nicht ausdrücklich, und in einer  jeden Zweifel ausschließenden Art und Weise bzw. auch nach außen in Erscheinung tretend  vereinbart worden ist.

**False Positives:**

- `Fakt ist, dass zwischen  der Bf. einerseits und der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_128`)


Die Honorarnoten der OG lassen schließlich auch offen, welche  konkreten Leistungen (nach Art, Zeit und Umfang bzw. Person des Leistungserbringers)  abgerechnet wurden.

**False Positives:**

- `Die Honorarnoten der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_141`)


Personengesellschaft) den an der M OG beteiligten natürlichen Personen, die im Streitzeitraum  über die M Holding GmbH wesentliche Beteiligungen iSd § 22 Z 2 2.

**False Positives:**

- `Personengesellschaft) den an der M OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_148`)


Deutlich abweichend vom Managementvertrag  hat die M OG im Streitzeitraum von der mitbeteiligten Partei Vergütungen von 101.500 Euro für  das Jahr 2010, 126.000 Euro für das Jahr 2011 und 91.000 Euro für das Jahr 2012 erhalten.

**False Positives:**

- `Deutlich abweichend vom Managementvertrag  hat die M OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_160`)


Abweichend von der  Managementvereinbarung hat die OG im Jahr 2009 von der Bf. jedoch eine Vergütung von  Euro 78.000,00, 2010 Euro 101.500,00, 2011 Euro 126.000,00 und 2012 Euro 91.000,00  erhalten, sohin de facto jeweils andere Beträge, als vereinbart.

**False Positives:**

- `Abweichend von der  Managementvereinbarung hat die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_121`)


Dieser in der BAO mehrfach verwendete Begriff erfasst u.a. offene Gesellschaften (OG) und  Kommanditgesellschaften (KG) nach dem Unternehmensgesetzbuch (UGB, früher: HGB) sowie  Gesellschaften nach bürgerlichem Recht sowie andere Mitunternehmerschaften zur Erzielung  betrieblicher Einkünfte (Personenvereinigungen) sowie andere Gebilde, welche  nichtbetriebliche Einkünfte erzielen oder keine Einkünfte erzielen (Personengemeinschaften).

**False Positives:**

- `Dieser in der BAO mehrfach verwendete Begriff erfasst u.a. offene Gesellschaften (OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_10`)


Die OG könne selbst keine Marktchancen nützen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_14`)


Die OG sei gegründet worden, um Beratungen im Baugewerbe anbieten zu können (S. 2).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_19`)


Die Funktion der OG sei die operative Unterstützung aller Gesellschaften gem.  Managementvertrag.

**False Positives:**

- `Die Funktion der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_49`)


Nur aus der OG flössen die Einkünfte im Zusammenhang mit beratenden Tätigkeiten  (NiS 2.6., S. 7).

**False Positives:**

- `Nur aus der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_53`)


Die OG sei nur eine Zahlstelle, um den DB und den DZ zu vermeiden (NiS. 2.6.S. 7).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_54`)


Die Zahlungen an die OG seien laufend übererfüllt worden (NiS 2.6., S. 12).

**False Positives:**

- `Die Zahlungen an die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_88`)


Die OG-Gesellschafter überlegten, wer was zu tun habe, es könne nicht jeder Geschäftsführer  der Tochtergesellschaften alleine diese Entscheidungen treffen, da käme nur ein Blödsinn  heraus (NiS. S. 5).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_98`)


Die OG sei dazu da, um neue Geschäftsfelder zu akquirieren (NiS. S. 6, 2. Stratege).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_115`)


Die OG habe aber entgegen der Managementvereinbarung  von der Vereinbarung deutlich abweichende Beträge erhalten.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_146`)


Auf die Frage des Richters, was im Streitzeitraum die OG an die Bf geleistet habe, das die  Gesellschafter der OG nicht hätten leisten können;

**False Positives:**

- `Auf die Frage des Richters, was im Streitzeitraum die OG an die Bf geleistet habe, das die  Gesellschafter der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_149`)


Als Stabsstelle sei die OG eingerichtet worden (NiS. S. 5).

**False Positives:**

- `Als Stabsstelle sei die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_159`)


Auf die Frage des Richters, was habe im Streitzeitraum die OG an die Bf geleistet, das die  Gesellschafter der OG nicht hätten leisten können?

**False Positives:**

- `Auf die Frage des Richters, was habe im Streitzeitraum die OG an die Bf geleistet, das die  Gesellschafter der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_160`)


Wodurch unterscheide sich die  Leistungserbringung durch die OG von einer Leistungserbringung, die durch die Gesellschafter  der OG hätte erbracht werden können (NiS. S. 5)?

**False Positives:**

- `Wodurch unterscheide sich die  Leistungserbringung durch die OG von einer Leistungserbringung, die durch die Gesellschafter  der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_163`)


Auf die Frage des Richters, ob man das, was die OG getan habe, auch durch die Holding hätte  tun lassen können (NiS. S. 5):  Geschäftsführer: Das sei eine schwierige Frage.

**False Positives:**

- `Auf die Frage des Richters, ob man das, was die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_177`)


Es sei nie vorgesehen gewesen, dass jemand in die OG im Wege der Erbfolge  nachrücke (NiS. S. 6).

**False Positives:**

- `Es sei nie vorgesehen gewesen, dass jemand in die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_200`)


An der OG seien damals beteiligt gewesen:  13 von 75 Seite 14 von 75

**False Positives:**

- `An der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_216`)


An der OG seien damals beteiligt gewesen:  50%....erster Stratege  50%....zweiter Stratege  Alleiniger Geschäftsführer der Akcay u. Schrörs Elektro GmbH sei damals bis einschließlich 10.6.2012 der erste  Stratege gewesen.

**False Positives:**

- `An der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_225`)


Die Zahlungen der Bf an die OG seien zwar nicht vertragskonform erfolgt, gingen aber dennoch  nicht über das angemessene Ausmaß h inaus.

**False Positives:**

- `Die Zahlungen der Bf an die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_283`)


Wenn der zweite Stratege krank oder urlaubsbedingt abwesend gewesen ist, so habe er  deshalb nicht weniger Geld aus der OG erhalten (NiS. S. 7, 16.10.25).

**False Positives:**

- `Wenn der zweite Stratege krank oder urlaubsbedingt abwesend gewesen ist, so habe er  deshalb nicht weniger Geld aus der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_306`)


Die OG sei von Anfang an als perfekte Rechtsform gesehen  worden, in der jeder OG-Gesellschafter verpflichtet gewesen sei, mitzuarbeiten (NiS. S. 9, 10,  16.10.25)

**False Positives:**

- `Die OG sei von Anfang an als perfekte Rechtsform gesehen  worden, in der jeder OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_322`)


Der Zeuge sagte hiezu, der  OG-Vertrag habe völlig gereicht (S. 13).

**False Positives:**

- `Der Zeuge sagte hiezu, der  OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_341`)


Die OG-Gesellschafter hätten als Berater die  grundsätzlichen Konzepte und die Strategie für alle GmbHs der Unternehmensgruppe  entwickelt. Die Umsetzung sei durch die Fremdgeschäftsführer erfolgt (S. 2).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_342`)


Die OG-Gesellschafter hätten sich immer wechselseitig vertreten.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_345`)


Nie sei ein OG – Gesellschafter überwacht worden . Jedem OG-Gesellschafter sei es auch  immer freigestanden, auch andere Tätigkeiten auszuüben, z.B. auf kommunaler Ebene oder in  der Wirtschaftskammer (S. 3).

**False Positives:**

- `Nie sei ein OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_348`)


Alle OG- Gesellschafter trügen gemeinsam das gesamte unternehmerische Risiko.

**False Positives:**

- `Alle OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_352`)


Die Rechtsform der OG sei nicht aus steuerlichen Gründen gewählt worden (S. 4 und 5).

**False Positives:**

- `Die Rechtsform der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_391`)


Das Personal der OG, das im Namen der OG zu Gunsten aller  Konzerngesellschaften, darunter auch die Bf, handelte, bestand von Anfang an nur aus den  Gesellschaftern der OG (Vorlageantrag vom 23.7.2018, S. 5), die auch Gesellschafter der Bf  waren.

**False Positives:**

- `Das Personal der OG, das im Namen der OG zu Gunsten aller  Konzerngesellschaften, darunter auch die Bf, handelte, bestand von Anfang an nur aus den  Gesellschaftern der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_392`)


Der OG standen allerdings als Betriebsmittel auch 3 durch die OG geleaste  Kraftfahrzeuge mit gesamten Anschaffungskosten von 180.000 €, Mobiltelefone, PCs und  Arbeitskleidung zur Verfügung (Schreiben der steuerlichen Vertreterin vom 22.9.2016), die von  den Gesellschaftern der OG (=Strategen) genutzt wurden.

**False Positives:**

- `Der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_393`)


Die OG zahlte auch die GSVG- Sozialversicherungsbeiträge der OG-Gesellschafter.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_398`)


Das blieb so bis zum 31.12.2011  [Firmenbuchauszug OG;

**False Positives:**

- `Firmenbuchauszug OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_400`)


Gesellschafter der OG waren seit deren Gründung (2006) die Gesellschafter der Bf 1.Stratege,  2.Stratege und 3.Stratege (die drei Strategen) bis zum 31.12.2011 (Firmenbuchauszüge OG und  Bf).

**False Positives:**

- `Gesellschafter der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_404`)


Die Gewinnbeteiligung in der OG lautete daher ab  1.1.2012 50:50 zwischen dem 1.Strategen und 2.Strategen (Firmenbuchauszug OG;

**False Positives:**

- `Die Gewinnbeteiligung in der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_405`)


Jahresabschluss OG 2011, S.3 und JA OG 2012, S. 1)

**False Positives:**

- `Jahresabschluss OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_428`)


Auch das FA sieht daher in Wirklichkeit die Zahlungen an die OG als  Abgeltung von Geschäftsführungstätigkeiten.

**False Positives:**

- `Auch das FA sieht daher in Wirklichkeit die Zahlungen an die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_429`)


Die OG, vertreten durch die Strategen als Gesellschafter der OG hat in den  Managementverträgen sämtliche Aktivitäten der Unterstützung der laufenden  Geschäftsführung der Konzerngesellschaften, auch strategische Beratung zum Aufbau neuer  Geschäftsfelder, Unterstützung bei der Akquisition, beim Controlling, der Baustellenabwicklung  , der Personalrekrutierung und der Personalführung versprochen.

**False Positives:**

- `Die OG, vertreten durch die Strategen als Gesellschafter der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_453`)


Die OG hat den weitaus überwiegenden Großteil der Kosten jedes Strategen bezahlt, die bei  diesen Tätigkeiten (Lenkung, Überwachung, Unterstützung der Konzerngesellschaften)  angefallen sind (insbesondere KFZ-Kosten, vgl.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_455`)


Die OG hat alle diese Kosten  endgültig bezahlt, ohne für den Kostenanteil, der auf die Konzernlenkungstätigkeiten der  Strategen entfallen ist, einen finanziellen Ausgleich von den einzelnen Konzerngesellschaften  zu begehren (FA NiS. 2.6. S. 6- S. 9; Gesellschafter-Geschäftsführer NiS. 2.6. S. 6; RI NIS 2.6. S. 9  ).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_456`)


Die OG hat offensichtlich für die Kosten, die auf die Konzernlenkungstätigkeiten der  Strategen entfallen sind, von den anderen Konzerngesellschaften keinen Kostenersatz verlangt,  weil sie ohnedies die diese Kosten deutlich übersteigenden Entgelte erhalten hat.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_457`)


Die OG  bezahlte im Einvernehmen mit den Konzerngesellschaften, darunter die Bf, den weitaus  überwiegenden Anteil der Kosten, die im Zusammenhang mit den Tätigkeiten der Strategen  (Überwachungs-, Lenkungsaufgaben, Unterstützungstätigkeiten) für den Konzern, bestehend  aus den Konzerngesellschaften angefallen sind.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_459`)


Z.B. erhielt die OG von der Bf im  Streitzeitraum 2008-2012 durchschnittlich 121.800 € im Jahr und durchschnittlich 10.150 € pro  Monat;

**False Positives:**

- `Z.B. erhielt die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_472`)


Die  OG-Gesellschafter waren auch die beherrschenden Gesellschafter-Geschäftsführer der alle  anderen Konzerngesellschaften beherrschenden Muttergesellschaft (Holding GmbH) und sie  waren auch Gesellschafter-Geschäftsführer jeweils mindestens einer Tochtergesellschaft: Dies  indiziert, dass mit den Entgelten für die Tätigkeiten der OG- Gesellschafter im Namen der OG  auch Lenkungs- und Überwachungstätigkeiten abgegolten werden sollten.

**False Positives:**

- `Die  OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_476`)


Daher wurden die Entgelte durch die Konzerngesellschaften, darunter die Bf, an die OG  für diese Lenkungs- Überwachungs- und Unterstützungstätigkeiten der Strategen im Namen  der OG bezahlt.  Dass es sich bei all diesen Tätigkeiten um Geschäftsführungstätigkeiten für den Konzern,  bestehend aus den Konzerngesellschaften, darunter die Akcay u. Schrörs Elektro GmbH  handelte, ergibt sich aus der  Art der Tätigkeiten: Lenkungsaufgaben, Überwachungstätigkeiten betreffend den Konzern,  bestehend aus allen Konzerngesellschaften, darunter auch die Bf; Strategieplanung,  Erarbeitung neuer Geschäftsfelder, Verhandlungen mit Banken, Cash Management betreffend  alle Konzerngesellschaften, darunter auch die Bf (siehe oben Vorlageantrag S. 4, 5: Schreiben  StB 22.9.2016, 2. Seite).

**False Positives:**

- `Daher wurden die Entgelte durch die Konzerngesellschaften, darunter die Bf, an die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_484`)


Auch die anderen  Konzerngesellschaften leisteten der OG Zahlungen in gleicher Größenordnung.

**False Positives:**

- `Auch die anderen  Konzerngesellschaften leisteten der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_488`)


Dies folgt  daraus, dass jeder der Strategen bei der Verteilung der Gewinne der OG einen gleichen Anteil  erhielt (OG-Vertrag von 2006).

**False Positives:**

- `Dies folgt  daraus, dass jeder der Strategen bei der Verteilung der Gewinne der OG einen gleichen Anteil  erhielt (OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_492`)


Die OG sagte bereits im Managementvertrag vom 19.5.2006 zu, die zugesagten Aktivitäten  durch ihre Gesellschafter, die auch Gesellschafter der Bf und Gesellschafter der Holding waren,  oder durch andere geeignete Personen auszuführen (Managementvertrag 19.5.2006, 1. Seite).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_494`)


Die OG handelte immer nur durch ihre Gesellschafter (Vorlageantrag S. 5; 2. Stratege, NiS  6.7.21, S. 5; 2. Stratege, NiS 16.10.25, S. 5 -7).

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_497`)


Zahlungen  Die Bf versprach der OG im Jahr 2006 für die Tätigkeiten der OG ein Entgelt von 6.000 € + 20%  UST pro Monat (72.000 € + USt pro Jahr) (Managementvereinbarung vom 19.5.2006).

**False Positives:**

- `Zahlungen  Die Bf versprach der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_502`)


Durch diese Zahlungen der Konzerngesellschaften, u.a. auch der Bf, finanzierte die OG die  Tragung der oben erwähnten Kosten (insbesondere KFZ-Kosten und  Sozialversicherungsbeiträge im Gesamtausmaß von größenordnungsmäßig 100.000 € im Jahr).

**False Positives:**

- `Durch diese Zahlungen der Konzerngesellschaften, u.a. auch der Bf, finanzierte die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_504`)


Die Bf bezahlte an die OG Jahr für Jahr ( jedenfalls 2008-2014) wesentlich mehr, als dies der im  Managementvertrag vom 19.5.2006 vereinbarten Entgelthöhe (72.000 € + USt im Jahr)  entsprach:  Die tatsächliche Höhe der Zahlungen der Jahre 2008-2015 betrug jeweils lt. Konto 7901  Geschäftsführungskosten :  108.000 € + 20% USt……2008 (Konto 7901)  117.000 € + 20%

**False Positives:**

- `Die Bf bezahlte an die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_520`)


Dh  , die OG hat von der Akcay u. Schrörs Elektro GmbH im Jahr 2015  105.000 € bekommen, obwohl für diese Zeit  107.000 € vereinbart worden waren, und nicht  132.489,86 €.

**False Positives:**

- `Dh  , die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_521`)


Somit hat die OG im Streitzeitraum  2015 annähernd den Betrag von der Akcay u. Schrörs Elektro GmbH  erhalten, der mit der Akcay u. Schrörs Elektro GmbH vereinbart war.

**False Positives:**

- `Somit hat die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)
- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_595`)


Daher ist auch nicht glaubhaft,  dass die Strategen im Namen der OG mit der Akcay u. Schrörs Elektro GmbH tatsächlich im Zeitraum 2008-2014  abändernde Vereinbarungen auf Stundenbasis geschlossen haben könnten.

**False Positives:**

- `Daher ist auch nicht glaubhaft,  dass die Strategen im Namen der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_810`)


Zur Wahrnehmung der Kontroll- Lenkungs-, und Beratungsfunktionen sei die OG, bestehend  aus den Strategen, als Stabsstelle gegründet worden.

**False Positives:**

- `Zur Wahrnehmung der Kontroll- Lenkungs-, und Beratungsfunktionen sei die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_811`)


Durch diese OG seien sodann die  Kontroll-, Lenkungs- und Beratungstätigkeiten an die Konzerngesellschaften, darunter auch die  Bf fakturiert worden.

**False Positives:**

- `Durch diese OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_822`)


Die OG lenkte, überwachte und unterstützte durch ihre Gesellschafter alle  Konzerngesellschaften, insbesondere alle Tochtergesellschaften, darunter auch die Akcay u. Schrörs Elektro GmbH  Das einzige Personal der OG bestand aus ihren Gesellschaftern, den Strategen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_823`)


Die OG bezahlte  den weitaus überwiegenden Teil der Kosten der Tätigkeiten ihrer Gesellschafter, die diese im  Namen der OG für alle Konzerngesellschaften, darunter auch die Bf, leisteten (KFZ-Kosten und  GSVG-Sozialversicherungsbeiträge) in der Größenordnung von 100.000 € im Jahr.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_831`)


An der OG waren damals (1.1.2011-31.12.2011) (gewinn-) beteiligt:  34% …..erster Stratege  33 %.....zweiter Stratege  33%......dritter Stratege  Ab 1.1.2012 bis jedenfalls Ende 2015 lauteten die (Gewinn-Beteiligungsverhältnisse in der OG:  50%....erster Stratege  50%....zweiter Stratege

**False Positives:**

- `An der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_833`)


Die Gewinnbeteiligungen lauteten damals  lt. Jahresabschluss der OG 2011:  34%……erster Stratege  33%……zweiter Stratege  33%……dritter Stratege  57 von 75 Seite 58 von 75

**False Positives:**

- `Die Gewinnbeteiligungen lauteten damals  lt. Jahresabschluss der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_834`)


Ab dem Jahresabschluss der OG 2012 lauteten die Gewinnbeteiligungen wie folgt:  50%……erster Stratege  50%……zweiter Stratege  Die Geschäfte der OG und die Tätigkeiten, die der OG zuzurechnen waren, wurden damals  (2011) durch diese drei Gesellschafter/ Strategen, und ab 2012 durch die ersten beiden  Strategen geführt.

**False Positives:**

- `Ab dem Jahresabschluss der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_839`)


Zwar hat die OG sich gegenüber der Bf vertraglich (durch die Managementvereinbarung vom  19.5.2006) verpflichtet, für die Bf tätig zu werden.

**False Positives:**

- `Zwar hat die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_844`)


Die OG hat sich in der Managementvereinbarung gegen Bezahlung eines jährlichen Entgeltes  von 72.000 € verpflichtet, die Akcay u. Schrörs Elektro GmbH bei der Durchführung von Geschäftsführungstätigkeiten  zu unterstützen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_853`)


Die  OG ist daher ohne vertragliche Vereinbarung zwischengeschaltet (dh zwischen die Akcay u. Schrörs Elektro GmbH  und die die Lenkungstätigkeiten ausführenden Gesellschafter der OG) worden.

**False Positives:**

- `Die  OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_857`)


Die zwischengeschaltete Gesellschaft (OG) hat daher gegenüber der die Tätigkeiten in Auftrag  gebenden Akcay u. Schrörs Elektro GmbH keine aus steuerlicher Sicht anzuerkennende vertragliche Verpflichtung  übernommen, und nur das Geld in Empfang genommen.

**False Positives:**

- `Die zwischengeschaltete Gesellschaft (OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_858`)


Die OG ist daher als bloße Zahlstelle i S der Zahlstellen-Erkenntnisse des VwGH anzusehen.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_877`)


An der OG waren damals beteiligt (siehe oben Pkt 3):  34% Erster Stratege  33%

**False Positives:**

- `An der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_903`)


An der OG waren damals beteiligt (siehe oben Pkt 3 a. aa.):   50%...... erster Stratege  50%......zweiter Stratege  Alleiniger organschaftlich bestellter Geschäftsführer der Akcay u. Schrörs Elektro GmbH war damals bis einschließlich  10.6.2012 der erste Stratege.

**False Positives:**

- `An der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_942`)


Daraus ergab sich, dass die Bf der OG jährlich, daher auch im Jahr 2012 72.000 €  bezahlen hätte müssen.

**False Positives:**

- `Daraus ergab sich, dass die Bf der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_945`)


Daraus ergab sich,  dass die Bf der OG im Jahr 2012 104.000 € bezahlt hat.

**False Positives:**

- `Daraus ergab sich,  dass die Bf der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_968`)


Dieselbe vertragliche Konstruktion gab es  zwischen der OG und jeder anderen Konzerngesellschaft.

**False Positives:**

- `Dieselbe vertragliche Konstruktion gab es  zwischen der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_974`)


Die Konzerngesellschaften , darunter die Bf, bezahlten diese  OG, weil diese, vertreten durch die Strategen (= OG – Gesellschafter), den Konzern, bestehend  aus allen Konzerngesellschaften, lenkte, überwachte und bestmöglich unterstützte.

**False Positives:**

- `Die Konzerngesellschaften , darunter die Bf, bezahlten diese  OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_976`)


Nur aus den Gewinnverteilungen der OG  erhielten die Strategen Geld.

**False Positives:**

- `Nur aus den Gewinnverteilungen der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_979`)


Die OG erhielt dafür von der Akcay u. Schrörs Elektro GmbH und jeder  anderen Konzerngesellschaft ein Entgelt, das allerdings deutlich höher als das im  Managementvertrag vereinbarte Entgelt war.

**False Positives:**

- `Die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_980`)


Die Gesellschafter der OG waren gleichzeitig auch die beherrschenden Gesellschafter der Akcay u. Schrörs Elektro GmbH und auch die beherrschenden Gesellschafter jeder anderen Konzerngesellschaft.

**False Positives:**

- `Die Gesellschafter der OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_1002`)


Da die OG Gesellschafter  (Strategen) regelmäßig den Konzern, bestehend aus allen Konzerngesellschaften, darunter  auch die Akcay u. Schrörs Elektro GmbH lenkten, waren sie in den Geschäftsbetrieb aller Konzerngesellschaften, auch  der Akcay u. Schrörs Elektro GmbH eingegliedert.

**False Positives:**

- `Da die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)
- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_1004`)


Soweit die OG-Gesellschafter an der Akcay u. Schrörs Elektro GmbH wesentlich  beteiligt waren – das war nicht in Bezug auf alle OG – Gesellschafter in Bezug auf alle Jahre der  Fall – waren die Zahlungen jedenfalls DB- und DZ-pflichtig gem. § 22 Z 2, zweiter TS EStG 1988  (VwGH 29.6.2022, Ro 2021/15/0026).

**False Positives:**

- `Soweit die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_1005`)


Soweit die OG- Gesellschafter an der Akcay u. Schrörs Elektro GmbH nicht wesentlich beteiligt waren, hat sich im  Verfahren herausgestellt:  Der dritte Stratege, ein an der GmbH 2011 zum Teil wesentlich, zum Teil nicht wesentlich  beteiligter Gesellschafter, hat bereits im Jahr 2010 das 60.

**False Positives:**

- `Soweit die OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Akcay u. Schrörs Elektro GmbH`(organisation)

</details>

---

## `Match Standard Companies (AG, GmbH, Limited, e.U., OEG, PartG, Stiftung) - Refined` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `61c9f708`  
**Description:**
Captures standard company names with suffixes, allowing lowercase starts and common prefixes like 'Gesellschaft', 'Anwalt', 'Rechtsanwalt', and '&' symbols, with strict boundaries.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*?(?:AG|GmbH|GesmbH|Limited|e\.U\.|OEG|PartG|Stiftung))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 34 | 0 | 34 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 34 | 16741 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_83`)


Auch eine  unrichtige Auszahlung, die ausschließlich auf einer Fehlleistung der Abgabenbehörde beruht,  steht einer Rückforderung nicht entgegen (vgl Wanke in Lenneis/Wanke (Hrsg), FLAG2 § 26  Rz 16, unter Hinweis auf zB VwGH 19.12.2013, 2012/16/0047).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_84`)


Aus § 26 Abs 1 FLAG 1967  ergibt sich nämlich eine rein objektive Rückzahlungspflicht (vgl zB das vorstehend erwähnte  Erkenntnis vom 19. Dezember 2013) und sind subjektive Elemente unbeachtlich (vgl Wanke in  Lenneis/Wanke (Hrsg), FLAG2 § 26 Rz 12f, und die dort angeführte Judikatur).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_96`)


Laut des an die Fa AG2 GmbH adressierten Schriftsatzes der  Bezirkshauptmannschaft O vom 27.08.1997 betreffend den Bf wird ua festgehalten, dass das  Land B sich verpflichtet dem Arbeitgeber zum Ausgleich der verminderten Arbeitsproduktivität  7 von 16 Seite 8 von 16

**False Positives:**

- `Laut des an die Fa AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_164`)


Lebensjahres, eingetretene dauernde Unfähigkeit, sich  selbst den Unterhalt zu verschaffen, steht weder Grund- noch Erhöhungsbetrag an  Familienbeihilfe zu. (Vgl. Lenneis in Lenneis/Wanke, FLAG2, § 8 Rz 19).

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_178`)


(Vgl Lenneis in Lenneis/Wanke (Hrsg), FLAG2, § 8 Rz 32)

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_25`)


Die Beweisregelung des § 8 Abs 6 FLAG 1967 geht als Spezialnorm den allgemeinen  Bestimmungen des § 166 BAO betreffend Beweismittel und des § 177 BAO betreffend den  Sachverständigenbeweis vor (vgl. Lenneis in Lenneis/Wanke (Hrsg), FLAG2 § 8 Rz 12 m. w. N.),  schließt deren ergänzende Anwendung aber nicht aus (vgl. BFG 2. 10. 2019,  RV/7101860/2018).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_28`)


VwGH 25. 11. 2010, 2010/16/0068, und die bei Lenneis in Lenneis/Wanke  (Hrsg), FLAG2 § 8 Rz 29 zitierte Rechtsprechung).

**False Positives:**

- `Wanke  (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/137334.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137334.1_108`)


Nur wenn einem Antrag auf Familienbeihilfe nicht oder nicht zur  Gänze stattzugeben ist, ist hinsichtlich des (monatsbezogenen) Abspruchs über die Abweisung  gemäß § 13 Satz 2 FLAG 1967 ein Bescheid (Abweisungsbescheid) auszufertigen (vgl. Wanke in  Lenneis/Wanke, FLAG2 2020 § 26 Rz 3 m. w. N.).

**False Positives:**

- `Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_126`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `Lenneis/Reinalter in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_142`)


Liegt im Sinne des § 17 Abs. 2 Z 1  StudFG daher kein Studienwechsel vor, weil die Vorstudienzeit eingerechnet wird, zählen die  eingerechneten Semester auf die weitere Dauer der Familienbeihilfe, dh. die Anspruchsdauer  des neuen Studiums wird um die angerechneten Semester verkürzt  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 101).

**False Positives:**

- `Lenneis/Reinalter in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_107`)


Um ein Kind, das sich außerhalb der gemeinsamen Wohnung der Familie aufhält, noch als  haushaltszugehörig ansehen zu können, darf der anderweitige Aufenthalt des Kindes gemäß  § 2 Abs 5 lit a FLAG 1967 nur ein „vorübergehender“ sein (Vgl Reinalter in Lenneis/Wanke  (Hrsg), FLAG2, § 2 Rz 145 f).

**False Positives:**

- `Wanke  (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_124`)


(Vgl Reinalter in Lenneis/Wanke (Hrsg), FLAG2, § 2 Rz 148)  Laut Pkt 1 Sachverhalt betragen die Kosten für die Unterbringung des Sohnes der Bf in der  Kinderwohngemeinschaft der Pro Juventute im Rahmen einer vollen Erziehung derzeit 205,48  Euro täglich, somit 6.164,40 Euro monatlich.

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/139705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139705.1_92`)


Letztlich ist es aber nicht entscheidend, ob und aus welchen Gründen in den Jahren 2016 und  den Folgejahren (abgesehen von den Zeiten mit Bezug von Arbeitslosengeld und  Notstandshilfe) Dienstverhältnisse mit einer herabgesetzten Arbeitszeit (bei der [AG] GmbH  lt vorgelegtem Dienstvertrag mit 30 Wochenstunden, bei den anderen Dienstgebern  lt Lohnzettel nicht näher quantifizierte „Teilbeschäftigung“) ausgeübt wurden, da es im  gegenständlichen Fall ausschließlich entscheidend ist, ob die Beschwerdeführerin (auf Grund  des Zeitpunktes der Beendigung der Lehre) bereits zum 31. August 2011 voraussichtlich  dauernd außer Stande war, sich selbst den Unterhalt zu verschaffen (vgl Lenneis in  Lenneis/Wanke (Hrsg), FLAG2 § 8 Rz 19ff).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/140338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140338.1_28`)


Nur in  Ausnahmefällen, nämlich bei Vollwaisen (und sog. Sozialwaisen) besteht ein Eigenanspruch des  Kindes auf Familienbeihilfe (vgl. Lenneis in Lenneis/Wanke (Hrsg), FLAG² § 6 Rz 1 f).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_107`)


siehe in: Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke (Hrsg), FLAG², § 2  Rz 45 – Stichwort Lehrausbildung beim "ABC der Berufsausbildung").

**False Positives:**

- `Lenneis/Reinalter in Lenneis/Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_117`)


Die Ausbildung muss aber als Vorbereitung für die  spätere konkrete Berufsausübung anzusehen sein und überdies die volle Zeit des Kindes in  Anspruch nehmen (vgl. Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke (Hrsg), FLAG², § 2  Rz 35f).

**False Positives:**

- `Lenneis/Reinalter in Lenneis/Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_118`)


Ob tatsächlich eine Berufsausbildung im Sinne des Familienlastenausgleichgesetzes (FLAG)  vorliegt, kann in der Regel nur im Einzelfall beurteilt werden (siehe Hebenstreit/Lenneis/  Reinalter in Lenneis/Wanke (Hrsg), FLAG², § 2 Rz 37).

**False Positives:**

- `Lenneis/  Reinalter in Lenneis/Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_134`)


Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke  (Hrsg), FLAG², § 2 Rz 40 mwN).

**False Positives:**

- `Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke  (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_153`)


Nach § 26 Abs. 1 FLAG 1967 hat, wer Familienbeihilfe zu Unrecht  bezogen hat, die entsprechenden Beträge zurückzuzahlen (vgl. Wanke in Lenneis/Wanke  (Hrsg), FLAG², § 26 Rz 20f).

**False Positives:**

- `Wanke  (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_157`)


Die Rückforderung ist auch keine Ermessensentscheidung der  Abgabenbehörde (vgl. Wanke in Lenneis/Wanke (Hrsg), FLAG², § 26 Rz 12ff mwN).

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_158`)


In Anlehnung an die bei Reinalter in Lenneis/Wanke (Hrsg), FLAG2 § 5 Rz 9 ff dargestellte  Rechtsprechung zu einem ständigen Auslandsaufenthalt des Kindes und an die Regelung des  § 26 Abs 2 BAO betreffend den gewöhnlichen Aufenthalt ist davon auszugehen, dass ein  Aufenthalt außerhalb des Haushaltes von - geplant - höchstens sechs Monaten die Haushalts- zugehörigkeit nicht beendet, ein darüberhinausgehender Aufenthalt hingegen schon (vgl. BFG  02.05.2022, RV/3100075/2022).

**False Positives:**

- `In Anlehnung an die bei Reinalter in Lenneis/Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_168`)


VwGH 25.11.2010,  2010/16/0068, vgl. auch Lenneis in Csaszar/Lenneis/Wanke, FLAG2, § 8 Rz 29 und die dort  zitierte Rechtsprechung).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_170`)


Liegen keine Befunde vor einem bestimmten Zeitraum vor, ist es einem Gutachter nicht  möglich, bereits davor eine voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, festzustellen, sofern kein Leidenszustand vorliegt, der eindeutig eine  Erwerbsfähigkeit bereits von vorneherein ausschließt (vgl. Lenneis in Lenneis/Wanke (Hrsg),  FLAG2 § 8 Rz 20 unter Hinweis auf BFG 17.7.2019, RV/7105214/2018).

**False Positives:**

- `Wanke (Hrsg),  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_175`)


Im Erkenntnis vom 17.03.2020, RV/7106245/2019, erwog das Bundesfinanzgericht:   Liegen keine Befunde vor einem bestimmten Zeitraum vor, ist es einem Gutachter nicht  möglich, bereits davor eine voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, festzustellen, sofern kein Leidenszustand vorliegt, der eindeutig eine  Erwerbsfähigkeit bereits von vorneherein ausschließt (vgl. Lenneis in Lenneis/Wanke (Hrsg),  FLAG2 § 8 Rz 20 unter Hinweis auf BFG 17.7.2019, RV/7105214/2018).

**False Positives:**

- `Wanke (Hrsg),  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `BFG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_209`)


Lebensjahres (vgl Lenneis in Lenneis/Wanke, FLAG2 aaO).

**False Positives:**

- `Lebensjahres (vgl Lenneis in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_140`)


VwGH 25.11.2010,  2010/16/0068, vgl. auch Lenneis in Csaszar/Lenneis/Wanke, FLAG2, § 8 Rz 29 und die dort  zitierte Rechtsprechung).

**False Positives:**

- `Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_142`)


Liegen keine Befunde vor einem bestimmten Zeitraum vor, ist es einem Gutachter nicht  möglich, bereits davor eine voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, festzustellen, sofern kein Leidenszustand vorliegt, der eindeutig eine  Erwerbsfähigkeit bereits von vorneherein ausschließt (vgl. Lenneis in Lenneis/Wanke (Hrsg),  FLAG2 § 8 Rz 20 unter Hinweis auf BFG 17.7.2019, RV/7105214/2018).

**False Positives:**

- `Wanke (Hrsg),  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_148`)


Im Erkenntnis vom 17.03.2020, RV/7106245/2019, erwog das Bundesfinanzgericht:  Liegen keine Befunde vor einem bestimmten Zeitraum vor, ist es einem Gutachter nicht  möglich, bereits davor eine voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, festzustellen, sofern kein Leidenszustand vorliegt, der eindeutig eine  Erwerbsfähigkeit bereits von vorneherein ausschließt (vgl. Lenneis in Lenneis/Wanke (Hrsg),  FLAG2 § 8 Rz 20 unter Hinweis auf BFG 17.7.2019, RV/7105214/2018).

**False Positives:**

- `Wanke (Hrsg),  FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `BFG`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/146167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146167.1_166`)


Lebensjahres (vgl Lenneis in Lenneis/Wanke, FLAG2 aaO).

**False Positives:**

- `Lebensjahres (vgl Lenneis in Lenneis/Wanke, FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/148390.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148390.1_19`)


Dabei sind  alle in dieses Kalenderjahr fallenden Zeiten zu berücksichtigen, für die Anspruch auf  Familienbeihilfe (etwa nach § 2 Abs. 1 lit. b FLAG 1967) besteht (vgl. Reinalter in  Lenneis/Wanke (Hrsg), FLAG2 § 5 FLAG Rz 1;

**False Positives:**

- `Wanke (Hrsg), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_31`)


Übergabezeitpunkt die bestehende offene Kaufpreisverbindlichkeit gegenüber der O GesmbH  mitübernommen und darüber hinaus sei zwischen der MedR Fiona Davydova  und Frau A K vereinbart  worden, dass nach Abdeckung der „Kaufpreisverbindlichkeit O GesmbH“ auch die von der  MedR Fiona Davydova  an die O GesmbH geleisteten Zahlungen zu ersetzen seien.

**False Positives:**

- `Kaufpreisverbindlichkeit O GesmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Fiona Davydova`(person)
- `MedR Fiona Davydova`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_35`)


Die  Ratenzahlungen an die O GesmbH seien mit Ende März 2018 beendet worden, ab April 2018  seien Ratenzahlungen an die MedR Fiona Davydova  vorgesehen.

**False Positives:**

- `Die  Ratenzahlungen an die O GesmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Fiona Davydova`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_58`)


Die O GesmbH hat ihren Sitz in Dornbirn  4 von 10 Seite 5 von 10

**False Positives:**

- `Die O GesmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_64`)


Lenneis/Wanke (Hrsg.), FLAG2 § 3 Rz 273).

**False Positives:**

- `Lenneis/Wanke (Hrsg.), FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Match Kairat Umwelt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `161e319f`  
**Description:**
Captures the specific entity 'Kairat Umwelt' which was missed.

**Content:**
```
\bKairat\s+Umwelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Tessarzik Pharma` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d3697a7`  
**Description:**
Captures the specific entity 'Tessarzik Pharma' which was missed, ensuring trailing punctuation is excluded.

**Content:**
```
\bTessarzik\s+Pharma\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Graf & Pitkowitz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e03e1257`  
**Description:**
Captures the specific entity 'Graf & Pitkowitz, Rechtsanwälte' which was missed.

**Content:**
```
\bGraf\s+&\s+Pitkowitz,\s+Rechtsanwälte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Wallermann Versand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `47181533`  
**Description:**
Captures the specific entity 'Wallermann Versand GmbH' which was missed.

**Content:**
```
\bWallermann\s+Versand\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Höhne, In der Maur & Partner` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d22b231`  
**Description:**
Captures the specific entity 'Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG' which was missed.

**Content:**
```
\bHöhne,\s+In\s+der\s+Maur\s+&\s+Partner\s+Rechtsanwälte\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Bialaschewitz Touristik GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fd030e86`  
**Description:**
Captures the specific entity 'Bialaschewitz Touristik GmbH' which was missed.

**Content:**
```
\bBialaschewitz\s+Touristik\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Möbel Talostkel AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e7f268c4`  
**Description:**
Captures the specific entity 'Möbel Talostkel AG' which was missed.

**Content:**
```
\bMöbel\s+Talostkel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match BergDaten GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d07cd4e`  
**Description:**
Captures the specific entity 'BergDaten GmbH' which was missed.

**Content:**
```
\bBergDaten\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Doschek Rechtsanwalts GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `da826801`  
**Description:**
Captures the specific entity 'Doschek Rechtsanwalts GmbH' which was missed.

**Content:**
```
\bDoschek\s+Rechtsanwalts\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match BLS Rechtsanwälte Boller Langhammer Schubert GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9a6ed9ce`  
**Description:**
Captures the specific entity 'BLS Rechtsanwälte Boller Langhammer Schubert GmbH' which was missed.

**Content:**
```
\bBLS\s+Rechtsanwälte\s+Boller\s+Langhammer\s+Schubert\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Landesgerichtes Wels` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a07637b3`  
**Description:**
Captures the specific entity 'Landesgerichtes Wels' (genitive) which was missed.

**Content:**
```
\bLandesgerichtes\s+Wels\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match WienTransport Werke -GesmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `50ff4030`  
**Description:**
Captures the specific entity 'WienTransport Werke -GesmbH' which was missed.

**Content:**
```
\bWienTransport\s+Werke\s+-GesmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Versand Triost GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ebf8996e`  
**Description:**
Captures the specific entity 'Versand Triost GmbH' which was missed.

**Content:**
```
\bVersand\s+Triost\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `035b6b33`  
**Description:**
Captures the specific entity 'Gottgeisl Leinsmer Weber Rechtsanwälte GmbH' which was missed.

**Content:**
```
\bGottgeisl\s+Leinsmer\s+Weber\s+Rechtsanw\u00e4lte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match GYP Immobilien Limited` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6929a19d`  
**Description:**
Captures the specific entity 'GYP Immobilien Limited' which was missed.

**Content:**
```
\bGYP\s+Immobilien\s+Limited\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Poduschka Partner Anwaltsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d184bf4`  
**Description:**
Captures the specific entity 'Poduschka Partner Anwaltsgesellschaft mbH' which was missed.

**Content:**
```
\bPoduschka\s+Partner\s+Anwaltsgesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match USW Metall Dienstleistungen AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d85ca2a7`  
**Description:**
Captures the specific entity 'USW Metall Dienstleistungen AG' which was missed.

**Content:**
```
\bUSW\s+Metall\s+Dienstleistungen\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Scheermann Forschung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `584cfd50`  
**Description:**
Captures the specific entity 'Scheermann Forschung GmbH' which was missed.

**Content:**
```
\bScheermann\s+Forschung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Logfen Luftfahrt Planung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `320c2d96`  
**Description:**
Captures the specific entity 'Logfen Luftfahrt Planung GmbH' which was missed.

**Content:**
```
\bLogfen\s+Luftfahrt\s+Planung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Säckel&Gaengler Robotik Gesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4aa38dcc`  
**Description:**
Captures the specific entity 'Säckel&Gaengler Robotik Gesellschaft mbH' which was missed.

**Content:**
```
\bS\u00e4ckel\u0026Gaengler\s+Robotik\s+Gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Partner Rechtsanwälte GmbH` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a880caf1`  
**Description:**
Captures the specific entity 'Partner Rechtsanwälte GmbH' which was missed.

**Content:**
```
\bPartner\s+Rechtsanw\u00e4lte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1122 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/149106.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149106.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Miroslav Spandl  in der Beschwerdesache Rebecca Wölzlein, LLM,  Lahnsattel 29x, 5203 Köstendorf, Österreich, vertreten durch Niederhuber & Partner Rechtsanwälte GmbH, Metahofgasse  16, 8020 Graz, über die Beschwerde vom 16. Juni 2023 gegen den Bescheid des Zollamtes  Österreich vom 12. Mai 2023, Zl. 230000/204741/03/2023, betreffend die Aussetzung der  Einhebung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Partner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Miroslav Spandl`(person)
- `Rebecca Wölzlein, LLM`(person)
- `Lahnsattel 29x, 5203 Köstendorf, Österreich`(address)
- `Zollamtes  Österreich`(organisation)

</details>

---

## `Match Bollmann & Bollmann Rechtsanwaltspartnerschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f3903060`  
**Description:**
Captures the specific entity 'Bollmann & Bollmann Rechtsanwaltspartnerschaft'.

**Content:**
```
\bBollmann\s+&\s+Bollmann\s+Rechtsanwaltspartnerschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Huemmer Event AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `471d9f31`  
**Description:**
Captures the specific entity 'Huemmer Event AG'.

**Content:**
```
\bHuemmer\s+Event\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match VDIQ Sicherheit Services Aktiengesellschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d34dcc5d`  
**Description:**
Captures the specific entity 'VDIQ Sicherheit Services Aktiengesellschaft'.

**Content:**
```
\bVDIQ\s+Sicherheit\s+Services\s+Aktiengesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Brandl Talos Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9558c394`  
**Description:**
Captures the specific entity 'Brandl Talos Rechtsanwälte GmbH'.

**Content:**
```
\bBrandl\s+Talos\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9632bfe5`  
**Description:**
Captures the specific entity 'Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH'.

**Content:**
```
\bPressl\s+Endl\s+Heinrich\s+Bamberger\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match RA Dr. Franz P. Oberlercher & RA Mag. Gustav H. Ortner Rechtsanwaltsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d3bb958c`  
**Description:**
Captures the specific entity 'RA Dr. Franz P. Oberlercher & RA Mag. Gustav H. Ortner Rechtsanwaltsgesellschaft mbH'.

**Content:**
```
\bRA\s+Dr\.\s+Franz\s+P\.\s+Oberlercher\s+&\s+RA\s+Mag\.\s+Gustav\s+H\.\s+Ortner\s+Rechtsanwaltsgesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Ruggenthaler, Rest & Borsky Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `52e62487`  
**Description:**
Captures the specific entity 'Ruggenthaler, Rest & Borsky Rechtsanwälte OG'.

**Content:**
```
\bRuggenthaler,\s+Rest\s+&\s+Borsky\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Melicharek Rechtsanwalts GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9b99dac0`  
**Description:**
Captures the specific entity 'Melicharek Rechtsanwalts GmbH'.

**Content:**
```
\bMelicharek\s+Rechtsanwalts\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Piaty Müller-Mezin Schoeller Rechtsanwälte GmbH & Co KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c12fc804`  
**Description:**
Captures the specific entity 'Piaty Müller-Mezin Schoeller Rechtsanwälte GmbH & Co KG'.

**Content:**
```
\bPiaty\s+Müller-Mezin\s+Schoeller\s+Rechtsanwälte\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Hildbrandt Immobilien AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `43e7770c`  
**Description:**
Captures the specific entity 'Hildbrandt Immobilien AG'.

**Content:**
```
\bHildbrandt\s+Immobilien\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Gabler Gibel & Ortner Rechtsanwälte GmbH & Co KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c960c448`  
**Description:**
Captures the specific entity 'Gabler Gibel & Ortner Rechtsanwälte GmbH & Co KG'.

**Content:**
```
\bGabler\s+Gibel\s+&\s+Ortner\s+Rechtsanwälte\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Eger/Gründl Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `753e6844`  
**Description:**
Captures the specific entity 'Eger/Gründl Rechtsanwälte OG'.

**Content:**
```
\bEger/Gründl\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Rothgeb Logistik GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `53aa2b78`  
**Description:**
Captures the specific entity 'Rothgeb Logistik GmbH'.

**Content:**
```
\bRothgeb\s+Logistik\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Harb & Postl Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4edae5f1`  
**Description:**
Captures the specific entity 'Harb & Postl Rechtsanwälte OG'.

**Content:**
```
\bHarb\s+&\s+Postl\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match West-Sicherheit GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3c29c154`  
**Description:**
Captures the specific entity 'West-Sicherheit GmbH'.

**Content:**
```
\bWest-Sicherheit\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Likar Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `56397193`  
**Description:**
Captures the specific entity 'Likar Rechtsanwälte GmbH'.

**Content:**
```
\bLikar\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Neisemeyer & Pfändler Lebensmittel -AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b872fe8`  
**Description:**
Captures the specific entity 'Neisemeyer & Pfändler Lebensmittel -AG'.

**Content:**
```
\bNeisemeyer\s+&\s+Pfändler\s+Lebensmittel\s+-AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Fellner Wratzfeld & Partner, Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `01e3b978`  
**Description:**
Captures the specific entity 'Fellner Wratzfeld & Partner, Rechtsanwälte GmbH'.

**Content:**
```
\bFellner\s+Wratzfeld\s+&\s+Partner,\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Schubert & Partner OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f3555e5c`  
**Description:**
Captures the specific entity 'Schubert & Partner OG'.

**Content:**
```
\bSchubert\s+&\s+Partner\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Schlager Rechtsanwalts KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7164351b`  
**Description:**
Captures the specific entity 'Schlager Rechtsanwalts KG'.

**Content:**
```
\bSchlager\s+Rechtsanwalts\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Posch, Schausberger & Lutz Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `454786ce`  
**Description:**
Captures the specific entity 'Posch, Schausberger & Lutz Rechtsanwälte GmbH'.

**Content:**
```
\bPosch,\s+Schausberger\s+&\s+Lutz\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match WGK Korp-Grünbart-Lison Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `08c9c7b3`  
**Description:**
Captures the specific entity 'WGK Korp-Grünbart-Lison Rechtsanwälte GmbH'.

**Content:**
```
\bWGK\s+Korp-Grünbart-Lison\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match InnHolz gesmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b4ecb537`  
**Description:**
Captures the specific entity 'InnHolz gesmbH'.

**Content:**
```
\bInnHolz\s+gesmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `678f1ba0`  
**Description:**
Captures the specific entity 'Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG'.

**Content:**
```
\bDr\.\s+Zsizsik\s+&\s+Dr\.\s+Prattes\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Graucob Pflege GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `40269f76`  
**Description:**
Captures the specific entity 'Graucob Pflege GmbH'.

**Content:**
```
\bGraucob\s+Pflege\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Reif und Partner Rechtsanwälte OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fdfe7c2d`  
**Description:**
Captures the specific entity 'Reif und Partner Rechtsanwälte OG'.

**Content:**
```
\bReif\s+und\s+Partner\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Hoch-Bildung Vertrieb GesmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `90362902`  
**Description:**
Captures the specific entity 'Hoch-Bildung Vertrieb GesmbH'.

**Content:**
```
\bHoch-Bildung\s+Vertrieb\s+GesmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Käppeler+Baldschuhn Pflege GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `276e5c12`  
**Description:**
Captures the specific entity 'Käppeler+Baldschuhn Pflege GmbH'.

**Content:**
```
\bKäppeler\+Baldschuhn\s+Pflege\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Norkelnex Pharma Holding Versicherung AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bb196d00`  
**Description:**
Captures the specific entity 'Norkelnex Pharma Holding Versicherung AG'.

**Content:**
```
\bNorkelnex\s+Pharma\s+Holding\s+Versicherung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Match Company Names with GmbH & Co KG - Refined` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d003eec9`  
**Description:**
Captures 'GmbH & Co KG' structures, ensuring the full name is captured including the prefix, and handles trailing punctuation.

**Content:**
```
(?<![a-zA-Z\s\.\,\'\(\)\-])([A-Z][a-zA-Z\s\.\-\&\+\/\,\'\(\)]*?GmbH\s+&\s+Co\s+KG)(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 16728 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_42`)


In der Firma G... Bau GmbH & Co KG arbeite ich erst ab 20.02.2017.

**False Positives:**

- `In der Firma G... Bau GmbH & Co KG` — partial — gold is substring of pred: `G... Bau GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... Bau GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_8`)


Als Ergebnis der AP-Verfahren erlassene Abgabenbescheide an - zumeist als  GmbH bzw. GmbH & Co KG geführte - Gesellschaften des geprüften Firmenkomplexes bzw.  1 von 30 Seite 2 von 30

**False Positives:**

- `Als Ergebnis der AP-Verfahren erlassene Abgabenbescheide an - zumeist als  GmbH bzw. GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_28`)


An die GmbH & Co KG erging am 15.1.2019 zur GZ RV/4100213/2012 eine Erledigung des BFG,  deren Spruch zufolge eine Beschwerde der GmbH & Co KG gegen die einheitliche und  gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2004 bis 2005 mangels  Bescheidqualität der angefochtenen Bescheide als unzulässig zurückgewiesen wurde.

**False Positives:**

- `An die GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_87`)


Dennoch hat  das Bundesfinanzgericht seine im Rahmen von Feststellungsverfahren ergangene Erledigung  nur an die GmbH & Co KG und nicht an alle Gesellschafter adressiert und zugestellt. Mangels  eines Hinweises in der betreffenden Erledigung ist die Zustellwirkung im Sinne des § 101 Abs 3  zweiter Satz BAO gegenüber den Gesellschaftern, denen Einkünfte zugerechnet werden sollen,  nicht eingetreten.

**False Positives:**

- `Dennoch hat  das Bundesfinanzgericht seine im Rahmen von Feststellungsverfahren ergangene Erledigung  nur an die GmbH & Co KG` — partial — gold is substring of pred: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

</details>

---

