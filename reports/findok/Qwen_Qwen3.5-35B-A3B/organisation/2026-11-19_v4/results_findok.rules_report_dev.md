# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-19T16:27:34.535461

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-11-19_v4/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 500 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 500 |
| Validation documents | 790 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 3754 |
| Validation sentences | 9322 |
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
| Critic Interval | 10 |
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
| Accuracy (exact match) | 97.2% |
| True Positives | 3149 |
| False Positives | 805 |
| False Negatives | 1894 |
| Total Gold Entities | 5043 |
| Micro Precision | 79.6% |
| Micro Recall | 62.4% |
| Micro F1 | 70.0% |
| Macro F1 | 70.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Social Security Agency` | 3.0% | 100.0% | 1.5% | 77 | 77 | 0 |
| `Employment Agency AMS` | 2.2% | 100.0% | 1.1% | 57 | 57 | 0 |
| `Federal Court of Finance` | 5.5% | 100.0% | 2.8% | 142 | 142 | 0 |
| `Pensions Insurance` | 1.0% | 100.0% | 0.5% | 25 | 25 | 0 |
| `Fraud Investigation Office` | 0.4% | 100.0% | 0.2% | 11 | 11 | 0 |
| `Municipal Council` | 1.2% | 100.0% | 0.6% | 31 | 31 | 0 |
| `Health Insurance` | 0.2% | 100.0% | 0.1% | 6 | 6 | 0 |
| `Administrative Court` | 2.1% | 100.0% | 1.1% | 54 | 54 | 0 |
| `Constitutional Court` | 0.9% | 100.0% | 0.5% | 23 | 23 | 0 |
| `Administrative Court Vienna` | 0.3% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Police Authority` | 0.6% | 100.0% | 0.3% | 16 | 16 | 0 |
| `Federal Ministry Finance` | 0.5% | 100.0% | 0.3% | 13 | 13 | 0 |
| `EU Court of Justice` | 0.9% | 100.0% | 0.5% | 23 | 23 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.1% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Federal Ministry Finance Genitive` | 0.8% | 100.0% | 0.4% | 19 | 19 | 0 |
| `City Magistrate` | 0.6% | 100.0% | 0.3% | 14 | 14 | 0 |
| `Wiener Linien` | 0.1% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Magistrats der Stadt Wien` | 0.5% | 100.0% | 0.3% | 13 | 13 | 0 |
| `Landespolizeidirektion Generic` | 1.0% | 100.0% | 0.5% | 26 | 26 | 0 |
| `Specific Company Names` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Finanzamt für Gebühren` | 0.4% | 100.0% | 0.2% | 10 | 10 | 0 |
| `Federal Ministry` | 0.8% | 95.2% | 0.4% | 21 | 20 | 1 |
| `Tax Authority Generic` | 62.5% | 87.5% | 48.6% | 2800 | 2449 | 351 |
| `SUVA` | 0.8% | 82.6% | 0.4% | 23 | 19 | 4 |
| `OECD` | 0.4% | 55.0% | 0.2% | 20 | 11 | 9 |
| `Abbreviated Tax Authority` | 0.7% | 51.4% | 0.4% | 37 | 19 | 18 |
| `Single Letter Company GmbH` | 0.2% | 18.8% | 0.1% | 32 | 6 | 26 |
| `Company Suffix GmbH & Partner KG` | 0.5% | 16.7% | 0.3% | 84 | 14 | 70 |
| `Company Suffix GmbH` | 1.2% | 13.1% | 0.7% | 251 | 33 | 218 |
| `Company Suffix AG` | 0.2% | 8.8% | 0.1% | 57 | 5 | 52 |
| `Technical University` | 0.0% | 0.0% | 0.0% | 47 | 0 | 47 |
| `Federal Court of Finance Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Steinval GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rs Dilly's Wellnesshotel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Burtscher Wachter GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex Company Name GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Railway Pension Service` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Energy Company Generic` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Fa. Company Abbreviation` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Company Suffix m.b.H` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Social Security Agency` 🏆

**F1:** 0.030 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Rule ID:** `131e25a4`  
**Description:**
Matches the Federal Office for Social Affairs and Disabled Persons (Bundesamt für Soziales und Behindertenwesen).

**Content:**
```
\bBundesamt(?:es)?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.015 | 0.030 | 77 | 77 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 77 | 0 | 4966 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_33`)


Bei der Beantwortung der Frage, welcher Grad der Behinderung ab welchem Zeitpunkt vorlag  ist die belangte Behörde bzw. das Bundesfinanzgericht an das der Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (Sozialministeriumservice) zugrunde liegende  Gutachten gebunden und darf dieses nur dahingehend prüfen, ob es schlüssig und vollständig  und im Fall mehrer Gutachten, diese nicht einander widersprechend sind (vgl. VwGH  29.9.2011, 2011/16/0063;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_37`)


Der Grad der Behinderung oder die voraussichtlich dauernde Erwerbsunfähigkeit ist nach der  geltenden Rechtslage § 8 Abs. 6 des Familienlastenausgleichsgesetzes 1967 in der Fassung  BGBl Nr. 105/2002 durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_56`)


Gemäß § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_57`)


Würdigung:   Eine unerlässliche Voraussetzung für den Bezug des Erhöhungsbetrages zur Familienbeihilfe  wegen erheblicher Behinderung ist, dass eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen vorliegt, welche bestätigt, dass der Grad der Behinderung eines Kindes  zumindest die vom Gesetz geforderten 50% erreicht.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_101`)


Am 21. Mai 2020 wurde der Sohn der Bf. im Auftrag des Bundesamtes für Soziales und  Behindertenwesen, Sozialministeriumservice, Landesstelle Wien, vom Arzt für  Allgemeinmedizin und Kinder- und Jugendheilkunde,Karina Burfeindt  in der Ordination untersucht  und folgendes Sachverständigengutachten erstellt:   Anamnese:   Entsprechend dem pädagogischen Gutachten der diplomierten Legasthenie Trainerin R. W.  05/2018 besteht bei A. eine Legasthenie mit Teilleistungsschwächen im Bereich der auditiven  Differenzierung und der akustischen Serialität.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Karina Burfeindt` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_161`)


Gemäß § 8 Abs. 6 FLAG 1967 in der Fassung BGBl. I Nr. 105/2002 ist der Grad der Behinderung  oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch  eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_165`)


Das Bundesfinanzgericht ist an die der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen zugrunde liegenden Gutachten grundsätzlich gebunden und darf diese nur  insoweit prüfen, ob sie schlüssig und vollständig und nicht einander widersprechend sind (vgl.  VwGH 29.9.2011, 2011/16/0063;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_169`)


Es besteht nach der Rechtsprechung beider Gerichtshöfe öffentlichen Rechts zu § 8 Abs. 6  FLAG 1967 jedoch keine unbedingte Bindung an die Bescheinigungen des Bundesamtes für  Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_10`)


Zum entscheidungsrelevanten Sachverhalt hielt das Finanzamt fest, dass laut  Gutachten des Bundesamtes für Soziales und Behindertenwesen vom 11. Februar 2020 beim  Sohn der Grad der Behinderung ab 1. März 2014 mit 30% festgelegt und die dauernde  Erwerbsunfähigkeit verneint worden sei.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_14`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Nachfolgend festgestellter Sachverhalt ergibt sich aus dem unstrittigen Inhalt des  Verwaltungsaktes bzw. den ärztlichen Sachverständigengutachten des Bundesamtes für  Soziales und Behindertenwesen:    

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_22`)


Nach den vorliegenden ärztlichen Sachverständigengutachten des Bundesamtes für  Soziales und Behindertenwesen leidet der Sohn an einer Entwicklungsstörung leichten  Grades sowie einer Aufmerksamkeitsstörung ohne Hyperaktivität und Lese- Rechtsschreib-Störung.

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_25`)


Der vom Bundesamt für Soziales und Behindertenwesen festgestellte Grad der  Behinderung beträgt ab März 2014 30%.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_42`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dabei durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen (Sozialministeriumservice) auf Grund eines ärztlichen  Sachverständigengutachtes nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_44`)


Bei der Antwort auf die Frage nach der Höhe des Grades der Behinderung bzw ob eine solche  körperliche oder geistige Behinderung, die zur Unfähigkeit, sich selbst den Unterhalt zu  verschaffen, führt, sind die Abgabenbehörde und das Bundesfinanzgericht an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden  Gutachten gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und vollständig  sind und im Falle mehrerer Gutachten nicht einander widersprechen (vgl etwa den Beschluss  des VwGH 16.12.2014, Ro 2014/16/0053, und die Erkenntnisse VwGH 22.12.2011,  2009/16/0307, und VwGH 22.12.2011, 2009/16/0310, mwN).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_45`)


Um dem Bundesamt für Soziales und Behindertenwesen eine zuverlässige Einschätzung des  Grades der Behinderung und den von diesem beauftragten ärztlichen Sachverständigen eine  umfassende Befundaufnahme zu ermöglichen, ist es unerlässlich, zur Untersuchung bei den  ärztlichen Sachverständigen entsprechend aussagekräftige Vorbefunde und Unterlagen über  bereits erfolgte Diagnoseerstellungen durch behandelnde (Fach)Ärzte vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_49`)


Es wäre also primär an der Beschwerdeführerin gelegen gewesen, durch eine substantiierte  Auseinandersetzung mit dem Inhalt der ärztlichen Gutachten und der Bescheinigungen des  Bundesamtes für Soziales und Behindertenwesen diese zu entkräften und die Beihilfenbehörde  oder das Bundesfinanzgericht in die Lage zu versetzen, an Hand konkreter Einwendungen und  Beweismittelvorlagen eine allfällige Ergänzung bzw Abänderung anzuregen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_9`)


Die belangte Behörde veranlasste die sachverständige Begutachtung der Bf durch das  Bundesamt für Soziales und Behindertenwesen (im Folgenden BASB).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_174`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_211`)


Lebensjahres) eingetreten ist, sind die Abgabenbehörde und das Bundesfinanzgericht an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden  Gutachten gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und vollständig sind  und im Falle mehrerer Gutachten nicht einander widersprechen“ (zB Beschluss VwGH  16.12.2014, Ro 2014/16/0053, und Erkenntnisse VwGH 22.12.2011, 2009/16/0307, VwGH  22.12.2011, 2009/16/0310, mwN, Hervorhebung durch BFG).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_29`)


Zugleich  wurde der Bf darauf hingewiesen, dass Kosten der Behinderung aufgrund einer ausländischen  Bescheinigung nicht berücksichtigt werden könnten, sondern eine Einschätzung der  Behinderung durch das Bundesamt für Soziales und Behindertenwesen erforderlich sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_41`)


- In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_8`)


Diese Angaben wurden sodann schriftlich mit Eingaben vom 27. November 2018 und  vom 29. Jänner 2019 wiederholt.  Das Finanzamt beauftragte das Bundesamt für Soziales und Behindertenwesen mit der  Erstellung einer Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_19`)


Das Finanzamt übermittelte die Beschwerde neuerlich an das Bundesamt für Soziales und  Behindertenwesen und ersuchte dieses eine neue Bescheinigung zu erstellen, wobei besonders  auf die Prüfung einer etwaigen dauernden Erwerbsunfähigkeit hingewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_36`)


Mit Vorhalt vom 6. April 2022 übermittelte das Bundesfinanzgericht die Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen samt ärztlichem Sachverständigengutachten  zur Kenntnis und hielt fest, dass eine zusätzliche ergänzende Stellungnahme, auf welche im  Vorlageantrag ohne Konkretisierung Bezug genommen wurde, im Verwaltungsakt nicht  enthalten ist.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_82`)


Der  Gesamtgrad der Behinderung beträgt 70 v.H.   f) Weder nach der auf einem ärztlichen Sachverständigengutachten vom 8. Juli 2019  basierenden Bescheinigung des Bundesamtes für Soziales und Behindertenwesen vom  11. Juli 2019, noch nach der auf einem ärztlichen Sachverständigengutachten vom  14. Juni 2020 basierenden Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen vom 18. Juni 2020 ist der Beschwerdeführer bereits vor Vollendung  des 21.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_106`)


Der Gesetzgeber hat für den Nachweis der entsprechenden Voraussetzung eine Bescheinigung  des Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens als einziges zulässiges Beweismittel vorgesehen (vgl dazu VfGH  10.12.2007, B 700/07, und VwGH 27.4.2005, 2003/14/0105, sowie VwGH 20.12.2006,  2003/13/0123, oder VwGH 18.11.2008, 2007/15/0019).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_139`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_149`)


Die voraussichtlich dauernde Unfähigkeit, sich  selbst den Unterhalt zu verschaffen, ist durch eine Bescheinigung des Bundesamtes für Soziales  und Behindertenwesen auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales  und Behindertenwesen` | `Bundesamtes für Soziales  und Behindertenwesen` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_153`)


Lebensjahres) eingetreten ist, sind die Abgabenbehörde und das Bundesfinanzgericht an  die der Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrunde  liegenden Gutachten gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und im Falle mehrerer Gutachten nicht einander widersprechen (vgl etwa den  Beschluss VwGH 16.12.2014, Ro 2014/16/0053, und die Erkenntnisse VwGH 22.12.2011,  2009/16/0307, und VwGH 22.12.2011, 2009/16/0310, mwN).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_154`)


Im vorliegenden Fall liegen zwei im Beihilfenverfahren erstellte ärztliche Gutachten und darauf  basierende Bescheinigungen des Bundesamtes für Soziales und Behindertenwesen vor, nach  welchen zum jeweiligen Erstellungszeitpunkt zwar eine Behinderung, jedoch keine  voraussichtlich dauernde Erwerbsunfähigkeit vorgelegen ist.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_162`)


Das Bundesfinanzgericht hat im vorliegenden Fall nach in freier Beweiswürdigung erfolgter  Beurteilung der Gutachten und Bescheinigungen des Bundesamtes für Soziales und  Behindertenwesen in Übereinstimmung mit der bestehenden und einhelligen Judikatur des  Verwaltungsgerichtshofes entschieden.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_4`)


Das Finanzamt wies dieses Begehren mit Bescheid vom 16. März 2020 unter Hinweis auf die  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen vom 12. März 2020, mit  welcher der Grad der Behinderung von 50% - in Übereinstimmung mit der Bescheinigung vom  6. Mai 2019 - (erst) ab Feber 2019 festgestellt worden sei, ab.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_8`)


Mit 28. August 2020 wurde neuerlich eine Bescheinigung durch das Bundesamt für Soziales  und Behindertenwesen erstellt. Wiederum wurde der Grad der Behinderung ab Feber 2019  bescheinigt.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_13`)


Mit 6. November 2020 erstellte das Bundesamt für Soziales und Behindertenwesen neuerlich  eine Bescheinigung;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_24`)


Zur Feststellung des Grades der Behinderung wurden durch das Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumsservice) folgende auf ärztlichen Gutachten basierende  Bescheinigungen ausgestellt:  Bescheinigung vom 6. Mai 2019 (ärztliches Gutachten vom 5. Mai 2019)  Funktionseinschränkung lt Pos.Nr. 02.02.03, GdB 50% ab 2/2019  Bescheinigung vom 12. März 2020 (ärztliches Gutachten vom 11. März 2020)  Funktionseinschränkung lt Pos.Nr. 02.02.03, GdB 50% ab 2/2019  Bescheinigung vom 28. August 2020 (ärztliches Gutachten vom 28. August 2020)  Funktionseinschränkung lt Pos.Nr. 10.03.14, GdB 60% ab 2/2019  Bescheinigung vom 6. November 2020 (ärztliches Gutachten vom 31. Oktober 2020)  Funktionseinschränkung lt Pos.Nr. 10.03.14, GdB 60% ab 2/2019  In den ärztlichen Gutachten wurden sämtliche von der Beschwerdeführerin vorgelegten  ärztlichen Unterlagen vollständig berücksichtigt und steht auch die Art der Erkrankung  unbestritten fest.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_38`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist nach § 8 Abs 6 FLAG 1967 durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_39`)


Bei der Antwort auf die Frage, ob eine Erkrankung zu Funktionseinschränkungen führt, die  einen Grad der Behinderung von 50% oder mehr erreichen bzw eine voraussichtlich dauernde  Unfähigkeit sich selbst den Unterhalt zu verschaffen bedingen, sind die Abgabenbehörde und  das Bundesfinanzgericht an die der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen zugrunde liegenden Gutachten gebunden und dürfen diese nur insoweit  prüfen, ob sie schlüssig und vollständig sind und im Falle mehrerer Gutachten nicht einander  widersprechen (vgl etwa den Beschluss VwGH 16.12.2014, Ro 2014/16/0053, und die  Erkenntnisse VfGH 10.12.2007, B 700/07, VwGH 9.9.2015, 2013/16/0049, VwGH 22.12.2011,  2009/16/0307, und VwGH 22.12.2011, 2009/16/0310, mwN).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_166`)


§ 8 Abs 6 FLAG 1967 bestimmt zur Lösung der Frage, ob das Kind voraussichtlich dauernd un- fähig ist, sich selbst den Unterhalt zu verschaffen, die Nachweisführung ausschließlich durch  eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen (Sozialministerium- service).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_168`)


Anhand des (Fach) Ärztlichen Gutachtens des Bundesamtes für Soziales und Behindertenwesen  (Sozialministeriumservice) vom 8.07.2020 beträgt der Grad der Behinderung für Ihre Tochter F.  M. 30% ab dem 1.11.2019.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_177`)


Mit Beschwerdevorentscheidung vom 06.09.2021 verweise die belangte Behörde auf die  beiden fachärztlichen Gutachten des Bundesamtes für Soziales und Behindertenwesen vom  8. Juli 2020 und vom 6. November 2021, laut derer der Grad der Behinderung für M. F. 30 % ab  dem 01.11.2019 betrage und keine dauernde Erwerbsunfähigkeit vorliege.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `M. F.` (person)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_179`)


Die belangte Behörde stütze ihre Begründung im Rahmen der Beschwerdevorentscheidung auf  die Ergebnisse der beiden vom Bundesamt für Soziales und Behindertenwesen gemäß § 4 Ein- schätzungsverordnung 2010 eingeholten Sachverständigengutachten, laut derer nur eine  mäßige Einschränkung der sozialen Fähigkeiten und die Möglichkeit der Absolvierung eines  Studiums gegeben sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_255`)


Lebensjahres) eingetreten  ist, sind die Abgabenbehörde und das Bundesfinanzgericht an die der Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (Sozialministeriumservice) zugrunde  liegenden Gutachten gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und im Falle mehrerer Gutachten nicht einander widersprechen (vgl. zB VwGH  22.12.2011, 2009/16/0307 und 2009/16/0310, VwGH 30.03.2017, Ra 2017/16/0023).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_73`)


Nach § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (nunmehr Sozialministeriumservice) auf  Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_92`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_97`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der Beweisführung  Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_68`)


Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel wegen dauerhafter  Mobilitätseinschränkung aufgrund einer Behinderung verfügen, als Nachweis über die  Berechtigungen nach Abs. 2 bis 4 auf Antrag vom Bundesamt für Soziales und  Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_154`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_165`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 zur Berufsausübung berechtigter Ärzte, die in  die bei dieser Behörde zu führende Sachverständigenliste eingetragen sind, als  Amtssachverständige bedient.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_75`)


§ 29b Abs. 1 StVO 1960 normiert:   "Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung "Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung"  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_47`)


Eine der Angabe der Bf. im Zuge des Vorlageantrages entsprechende  Bestätigung für die angestrebte neuerliche Untersuchung am Bundesamt für Soziales und  Behindertenwesen - Sozialministeriumservice und den diesbezüglichen Termin am 30.04.2017  sei trotz Aufforderung nicht vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_49`)


Mit Schreiben des BFG vom 17.07.2017 wurde die Bf. bezüglich ihres Augenleidens als Folge  der Nichtvorlage der im Vorlageantrag angesprochenen Bescheinigung des Bundesamts für  Soziales und Behindertenwesen - Sozialministeriumservice im Sinn des § 35 EStG 1988 ersucht,  sämtliche Beweismittel zwecks Veranlassung einer Anfrage an das Bundesamt für Soziales und  Behindertenwesen betreffend „Rückwirkung des Grads der Behinderung“ an das BFG zu  übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesamts für  Soziales und Behindertenwesen` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_50`)


In Entsprechung dieses Ersuchens wurden diverse Berichte und Befunde als  Beilage zum Schreiben der Bf. vom 10.10.2017 an das BFG zugesandt, die in weiterer Folge  dem an das Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice  adressierten Schreiben des BFG vom 27.10.2017 mit dem Ersuchen um u.a. a) Aufgliederung  des u.a. Gesamtgrades der Behinderung samt Begründung und b) Angabe des Prozentsatzes  der Sehstörung in den Streitjahren beigelegt wurden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_55`)


Infolge Fehlens von  Augenbefunden für den Zeitraum von Juni 2012 bis Oktober 2014 hat das Bundesamt für  Soziales und Behindertenwesen - Sozialministeriumservice (früher Bundessozialamt) den Grad  der Augenbehinderung bei der Bf. von 20% mit ausreichender Wahrscheinlichkeit für den  Zeitraum Jänner bis Oktober 2014 aufgrund des Sehvermögens rechts mit 0,3 und links mit 0,7  - wie im Befund von Juni 2012 angeführt - angenommen.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_56`)


Der Grad der Behinderung für den  nach der Laseroperation gelegenen Zeitraum der Monate November und Dezember jeweils des  Jahres 2014 ist vom Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice  mit 10% eingeschätzt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_91`)


Zuständige Stelle ist das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_125`)


Eine Bestätigung für die im  Vorlageantrag thematisierte neuerliche Untersuchung beim Bundesamt für Soziales und  Behindertenwesen - Sozialministeriumservice (früher Bundessozialamt) am 30.04.2017 mit  dem Ergebnis der Erfüllung der medizinischen Voraussetzungen für die Vornahme der  Zusatzeintragung „Die Untersuchte ist sehbehindert“ mit Rückwirkung auf das Jahr 2014 wurde  trotz Vorhalts in der abgabenbehördlichen Stellungnahme zum Vorlageantrag nicht  nachgereicht.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_126`)


Angesichts der Tatsache, dass das Bundesamt für Soziales und Behindertenwesen -  Sozialministeriumservice (früher Bundessozialamt) eine Bestätigung für die Bf. hinsichtlich  einer Sehbehinderung mit Rückwirkung für das Jahr 2014, die den Grad der Behinderung von  25% im Zeitraum vor und nach der Laseroperation unterschritten hatte, ausgestellt hatte, war  davon auszugehen, dass die medizinischen Voraussetzungen für die Vornahme der  Zusatzeintragung „Die Untersuchte ist sehbehindert“ im Behindertenausweis der Bf. aufgrund  der funktionellen Einschränkungen der Bf. im Jahr 2014 nicht gegeben waren.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_131`)


Aufgrund der Abhängigkeit der Antwort auf die Frage, ob die Voraussetzungen für die  Anerkennung der in Rede stehenden Kosten der Bf. als außergewöhnliche Belastung gemäß  § 34 Abs. 6 EStG 1988 in Verbindung mit § 35 Abs. 5 EStG 1988 im Streitjahr 2014 gegeben  waren, von Eintragungen im Behindertenausweis der Bf. und dem Ergebnis von Gutachten des  Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice war das Vorliegen  einer Rechtsfrage von grundsätzlicher Bedeutung im Sinne des Artikel 133 Abs. 4 B-VG zu  verneinen und spruchgemäß zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_118`)


– In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_36`)


Laut diesbezüglicher Bescheinigung des Bundesamtes für Soziales und Behindertenwesen ist  der Beschwerdeführer aufgrund einer vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_38`)


Der Grad der Behinderung  beträgt der Bescheinigung des Bundesamtes für Soziales und Behindertenwesen vom  17.09.2024 zufolge 50 % ab September 1982 und 100% ab März 2023.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_57`)


Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_60`)


Bei der Antwort auf die Frage, ob das Kind bzw die Vollwaise erheblich behindert ist und/oder  voraussichtlich dauernd außerstande ist, sich selbst den Unterhalt zu verschaffen, ist das  Bundesfinanzgericht nach der ständigen Rechtsprechung des VwGH an die der Bescheinigung  des Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden Gutachten  grundsätzlich gebunden und darf diese nur insoweit prüfen, ob sie schlüssig und vollständig  und nicht einander widersprechend sind (vgl VwGH 27.9.2012, 2010/16/0261;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_65`)


Lebensjahres auf der Grundlage des nach Vorlage der Beschwerde an das Bundesfinanzgericht  erstellten Sachverständigengutachtens vom 17.09.2024 durch das Bundesamt für Soziales und  Behindertenwesen bescheinigt.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_68`)


Die belangte Behörde geht ebenfalls davon aus, dass  dem Beschwerdeführer aufgrund der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen vom 17.09.2024 Familienbeihilfe (samt Erhöhungsbetrag) zusteht.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_116`)


Nach § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_140`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  10 von 15 Seite 11 von 15

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/149274.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149274.1_72`)


Ein Parkausweis gemäß § 29b StVO ist Inhaberinnen und Inhabern eines Behindertenpasses  nach dem Bundesbehindertengesetz, BGBl. Nr. 283/1990, mit der Zusatzeintragung  „Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel wegen dauerhafter  Mobilitätseinschränkung aufgrund einer Behinderung“ als Nachweis über die Berechtigungen  nach § 29b Abs 2 bis 4 StVO auf Antrag vom Sozialministeriumservice (ehemaliges Bundesamt  für Soziales und Behindertenwesen) auszufolgen (§ 29b Abs 1 StVO).

| Predicted | Gold |
|---|---|
| `Bundesamt  für Soziales und Behindertenwesen` | `Bundesamt  für Soziales und Behindertenwesen` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_44`)


Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt  zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_46`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_47`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der  anspruchsrelevanten Daten durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes  (BBG), BGBl. Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_65`)


Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_67`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_68`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der  anspruchsrelevanten Daten durch das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes  (BBG), BGBl. Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_73`)


BFG/Rema-Akt Dok.Nr. 11,  BASB (Bundesamt für Soziales und Behindertenwesen) – Bescheinigung vom 26.2.2025) ist der  Grad der Behinderung von 40% unverändert gegenüber dem Vorgutachten vom 3.10.2024.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_74`)


Ebenso unverändert ist, dass beim Sohn des Bf. keine Erwerbsunfähigkeit bescheinigt wird  (unverändert wie im Vorgutachten):  [...]  Aufgrund der o.a. Gesetzesnormen iVm dem Legalitätsprinzip hat das Bundesfinanzgericht  grundsätzlich die SVGA des Bundesamtes für Soziales und Behindertenwesen (BASB) der  Entscheidung zugrunde zu legen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

</details>

---

## `Employment Agency AMS` 🏆

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `d150a8cf`  
**Description:**
Matches the abbreviation AMS (Arbeitsmarktservice) when used as an organization.

**Content:**
```
\bAMS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 57 | 57 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 57 | 0 | 4986 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_10`)


Als Ergebnis eines unter anderem auf Vorlage der AMS-Karte abzielenden Vorhaltes wurde  eine derartige, – den Zeitraum vom 01.01.2017 bis zum 24.02.2019 umfassende - Karte sowie  eine ebenfalls diesen Zeitraum umfassende mit 11.10.2019 datierte AMS -Bezugsbestätigung  des Inhalts nachgereicht, dass der Bf. vom 01.01.2017 bis zum 24.04.2017; vom 27.04.2017 bis  zum 01.08.2017; vom 07.11.2017 bis zum 15.12.2017; vom 09.01.2018 bis zum 01.07.2018;  vom 15.12.2018 bis zum 31.12.2018 sowie vom 01.01.2019 bis zum 24.02.2019 Notstandshilfe  bezogen hat, bzw. diesem für den Zeitraum vom 25.10.2017 bis zum 06.11.2017 ein Vorschuss  Kündigungsentschädigung zugezählt worden ist.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_14`)


Begründung  Sachverhalt  „Sie sind polnischer Staatsbürger und in Österreich beschäftigt bzw. beziehen AMS Bezüge.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_386`)


Zu den persönlichen und wirtschaftlichen Verhältnissen des Beschuldigten wurde vom  Amtsbeauftragten in der mündlichen Verhandlung hingewiesen, dass der Beschuldigte seit  2015 durchgehend AMS-Bezüge erhält.  Bisher wurde die finanzstrafrechtliche Unbescholtenheit als mildernd gewertet, erschwerend  kein Umstand.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_14`)


1997 Wechsel zu Dienstgeberin, Bf. war Verkäuferin  01.12.2009  Mietvertrag über eine Wohnung in Ort CH-1 („Ort CH-1“),  bestehend aus einem Wohn-Schlafraum mit Küche, Bad  und WC  01.11.2011 Mietvertrag betreffend die Wohnung am Ort.CH-1,  bestehend aus Wohnraum und Küche, Schlafzimmer, Bad  und WC   13.05.2011-29.05.2011  und 28.10.2011 -  13.11.2011  AMS-Bezug in Ö  7.5. 2012 bis 29.5.2012,  1.11.2012 bis 8.11.2012  und   10.11.2012 bis 18.11.2012  AMS-Bezug in Ö   Mai 2012 Kauf eines Kfz in Ö, Marke X, und Zulassung dieses Kfz in Ö   9.11.2012 GKK-Bezug in Ö   2 von 24 Seite 3 von 24

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_15`)


14.6.2013 bis 30.6.2013  und  4.11.2013 bis 17.11.2013  AMS-Bezug in Ö  23.6.2014 bis 6.7.2014  1.11.2014 bis 17.11.2014  AMS-Bezug in Ö  01.06.2015 Abmeldung des Hauptwohnsitzes der Bf. in Ö, ab diesem  Tag Nebenwohnsitz (Abfrage ZMR)  01.06.2015 Datum des vorgelegten, unbefristet abgeschlossenen  Arbeitsvertrages als Abteilungsleiterin  Ab 01.06.2015  wird die Wohnsitzdauer aufgrund einer B-Bewilligung in  der CH bis auf Weiteres (gültig bis 31.05.2020) bestätigt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_22`)


die Bezüge der Gebietskrankenkasse  und des AMS würden für eine Ansässigkeit in Österreich sprechen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_51`)


Für die kurzen Zeiten habe sie in Österreich lediglich AMS-Geld bezogen,  das Haupteinkommen jedoch in der Schweiz.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_11`)


Seine AMS-Bemessung liege bei € 27,65 pro Tag  (€ 857,15 pro Monat) und so komme er mit allen Basiszahlungen wie Miete, Telefon, Strom,  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_31`)


Daraus ergibt sich, dass der Bf. vom AMS eine Notstandshilfe von tgl.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_32`)


€ 27,65 (d.s. rd. € 860,00  monatlich) bezieht (Schreiben des AMS vom 25. Juni 2021).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_71`)


Seine AMS-Bemessung liege bei € 27,65  täglich (€ 857,15 monatlich) und so komme er mit allen Basiszahlungen wie Miete, Telefon,  Strom, Gas und Rückzahlungen gerade einmal so über die Runden mit Verpflegung.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_76`)


Das Bundesfinanzgericht geht aufgrund folgender Umstände von der Zahlungsunfähigkeit des  Bf. aus:  Dem monatlichen AMS-Bezug von rd. € 860,00 stehen monatliche Belastungen von rund  € 800,00 gegenüber, wobei die Kosten des täglichen Lebens wie beispielsweise Ausgaben für  Lebensmittel, Medikamente, etc. dabei noch nicht berücksichtigt sind.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_6`)


Folgende Aufwendungen für das Jahr 2019 werden unter dem Titel Werbungskosten geltend  gemacht:  Rückzahlung der Bundespensionskasse-Auszahlung aus 2016 4.523,33 €  Rückzahlung der AMS-Leistungen aus 2016 6.194,10 €  Rückzahlung der AMS-Leistungen aus 2017 10.994,51 €  1 von 23 Seite 2 von 23

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_7`)


Rückzahlung der AMS-Leistungen aus 2019 5.070,45 €  Rückzahlung der WGKK-Leistungen aus 2016 150,16 €  Rückzahlung der WGKK Leistungen aus 2017 2.440,10 €  Rückzahlung der WGKK Leistungen aus 2018 337,86 €  Summe Werbungskosten 29.710,51 €  Die Rückzahlungen an das Arbeitsmarktservice im Jahr 2018 in Höhe von 12.839,94 € werden  als außergewöhnliche Belastung geltend gemacht.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)
- `WGKK` (organisation)
- `WGKK` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_8`)


Rückzahlung der AMS-Leistungen aus 2018 12.839,94 €  Darstellung der im Jahr 2019 getätigten Rückzahlungen:  Rückzahlung der Auszahlung der Bundespensionskasse 4.523,33 €  Summe Rückforderung AMS 35.099,00 €  Summe Rückzahlung WGKK 2.928,12 €  Summe Rückzahlungen 2019 42.550,45 €  Die Bf. sei mit der Wirkung vom 30.06.2016 von ihrer Arbeitgeberin (X) gekündigt worden,  woraufhin die Bf. eine Kündigungsanfechtungsklage beim Arbeitsgericht Wien anstrengte, bei  der sie sich auch letztlich erfolgreich durchsetzen konnte.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_22`)


Die Entgelt-Nachzahlungen im Jahre 2019 als Folge der erfolgreichen  Kündigungsanfechtung - der Hauptgrund für die Rückzahlung-Anforderungen des AMS und  der WGKK führten zu einer weit  höheren Steuerbelastung im Jahr 2019 als wenn sie unter  normalen Umstände mit den für alle Arbeitnehmer gültigen Steuertarif in den jeweiligen  Monaten/Jahren (2016 bis 2019) zur Auszahlung gebracht worden wären.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_27`)


 Rückforderungen in Kopie  o von der Pensionskasse Beilage A1; vom AMS Beilage A2; von der WGKK Beilage A3   Bestätigung der Rückzahlungen  o an die Pensionskasse Beilage B1; an das AMS Beilage B2; an die WGKK Beilage B3   Gehaltszettel von Juli und September2019 in Kopie  o Juli 2019 Beilage C1; September 2019 Beilage C2   Mitteilungen vom AMS und WGKK an Finanzamt:  o 2017 Beilage D1;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)
- `WGKK` (organisation)
- `WGKK` (organisation)
- `Finanzamt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_29`)


Gegen diesen Bescheid erhob die Bf. mit Eingabe vom 08.02.2021 innerhalb offener  Rechtsmittelfrist Beschwerde und führte begründend aus:  Beantragt werde die Anerkennung von Rückzahlungen von AMS- und WGGK-Leistungen für die  Jahre 2017 und 2018 als Werbungskosten.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_30`)


Rückzahlung der AMS-Leistungen vom 2017 10.994,51€  Rückzahlung der WGKK-Leistungen vom 2017 2.440,10 €  Rückzahlung der AMS-Leistungen vom 2018 12.839,94€  Rückzahlung der WGKK-Leistungen vom 2018 337,86 €  1) Werbungskosten gemäß § 16 EStG  Unbestritten sei es Tatsache, dass die Bf. März 2016 mit der Wirkung 30.06.2016 von ihrer  Arbeitgeberin X GmbH gekündigt wurde.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)
- `WGKK` (organisation)
- `X GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_83`)


Die AMS- bzw. WGKK- Zahlungen des Jahres 2017 in Höhe von 13.434,61 € hätten allerdings  ebenso aufgrund der Entscheidung des VwGH vom 22.6.2020, Ro 2018/13/0009 von der  Finanzbehörde als Werbungskosten berücksichtigt werden müssen, da es bei der Anwendung  der Umrechnungs-/Hinzurechnungs-Variante der zugeflossenen Arbeitslosenbeträge nicht  8 von 23 Seite 9 von 23

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_85`)


Da die Bf. im Jahre 2017 nicht ununterbrochen über das ganze Jahr AMS-Gelder bzw.  Krankengelder bezog (über 14 Tage im Jahr: keine AMS- oder WGKK- Zahlung, siehe auch  Einkommensbescheid für das Jahr 2017), sondern auch Einnahmen in Form von einer  Pensionsabfindung hatte, musste somit die Umrechnungsvariante mit anschließender  Hinzurechnungsvariante zur Kontrollrechnung gemäß § 3 Abs. 2 EStG 1988 durchgeführt  werden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_87`)


Bei der Kontrollrechnung nach der  Hinzurechnungsvariante mussten die AMS- bzw. WGKK- Zahlungen in Höhe von 13.434,61 €  berücksichtigt werden, welche nach Abzug der Sonderausgaben von 730 € und der  steuerfreien 11.000 € und der Berücksichtigung von 25% Steuer für den Rest (426,15 €) und  Abzug vom 400 € des Pensionistenabsetzbetrages einen Steuerbetrag vom 26,15 € ergeben  würde.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_125`)


Die AMS- bzw. WGKK- Zahlungen des Jahres 2017 in Höhe von 13.434,61 € hätten somit nach  der Entscheidung des VwGH vom 22.6.2020, Ro 2018/13/0009 ebenfalls als Werbungskosten  von der Finanzbehörde berücksichtigt werden müssen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_127`)


Nach den obigen Ausführungen unter dem Punkt „Arbeitslosengelder" werde bei der  Berücksichtigung der Zahlungen von AMS bzw. WGKK ohnehin nicht auf die Anwendung der  Umrechnungs-/Hinzurechnungs-Variante der § 3 Abs. 2 EStG 1988 ankommen, da diese von  der Bf. erhaltenen Beträge grundsätzlich steuerpflichtige Einnahmen im Jahr 2018 darstellten.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_129`)


Die AMS- bzw. WGKK-Zahlungen seien als steuerpflichtige Vorschussleistung zu bezeichnen,  deren Rückzahlung gemäß § 16 Abs. 2 EStG 1988 zu berücksichtigen sei.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_136`)


Diese steuerpflichtigen Einnahmen der Bf. im Jahre 2018 resultierend aus den AMS- bzw.  WGKK-Zahlungen führten allerdings zu keinem Lohnsteueraufkommen im Jahr 2018 (siehe  Einkommensteuerbescheid für das Jahr 2018), welche allerdings ihre Qualifikation als  steuerpflichtige Einnahmen nicht beeinträchtigt habe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_137`)


Es sei allerdings im Einkommensteuerbescheid vom 2018 erwähnt, dass die AMS- bzw. WGKK-  Zahlungen des Jahres 2018 bei der Ermittlung des Steuersatzes berücksichtigt worden seien,  womit auch im Jahr 2018 die Anwendung des § 3 Abs. 2 EStG 1988 bestätigt wurde.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_138`)


Die AMS- bzw. WGKK- Bezüge waren auch gemäß § 84 bzw. § 3 Abs. 2 EStG 1988 von der  bezugsauszahlenden Stelle (AMS bzw. WGKK) dem Finanzamt zu melden bzw. seien auch  entsprechend gemeldet geworden (siehe ebenfalls Einkommensteuerbescheid für das Jahr  2018).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)
- `WGKK` (organisation)
- `Finanzamt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_139`)


Da die Bf., wie vorhin erwähnt, auch im Jahr 2018 nach den rechtlichen Grundlagen  Dienstnehmer iSd EStG 1988 gewesen sei und gleichzeitig AMS- bzw. WGKK- Zahlungen bezog,  müsste nach § 3 Abs. 2 EStG 1988 vorgegangen werden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_147`)


Dass weder der Zeitpunkt des Zuflusses noch des Abflusses willkürlich waren, stehe aufgrund  der erfolgten Kündigungsanfechtung beim Arbeitsgericht fest und werde von der  Finanzbehörde auch nicht in Zweifel gezogen (nicht zuletzt wegen der Berücksichtigung der  AMS-Zahlungen für das Jahr 2016 als Werbungskosten im Einkommensteuerbescheid für das  Jahr 2019).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_148`)


Somit müssten auch diese Beträge der AMS- bzw. WGKK-Zahlungen vom Jahr 2018 in Höhe von  13.177,80 € als Werbungskosten im Jahre 2019 berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_149`)


Beweis:  • Beilage E: Lohnzettel 2018 mit SV-Beiträgen  Zusammenfassung:  Aufgrund der obigen Ausführungen beantragt die Bf. die Finanzbehörde um die  Berücksichtigung der AMS- bzw. WGKK-Rückzahlungen der Jahre 2017 und 2018 als  Werbungskosten im Einkommensteuerbescheid für das Jahr 2019 und somit um die  Neuberechnung des Steuerbescheides des Jahres 2019.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_165`)


Da sowohl im Jahr 2017 als auch im Jahr 2018 keine steuerpflichtigen Einkünfte vorlagen,  hatten sich die steuerfreien AMS- und WGKK-Bezüge gemäß § 3 Abs. 2 EStG nicht  steuererhöhend ausgewirkt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_178`)


Im Jahr 2019 machte die Bf. Rückzahlungen an das AMS für Leistungen aus den Jahren 2016,  2017 und 2019, an die WGKK für Leistungen aus den Jahren 2016, 2017 und 2018 und an die  Bundespensionskasse aus dem Jahr 2017 als Werbungskosten bzw. die Rückzahlungen der  AMS-Leistungen für das Jahr 2018 als außergewöhnliche Belastungen geltend.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_179`)


Die für das Jahr 2016 geleistete Rückzahlungen (AMS-Leistungen in Höhe von 6.194,10 € und  WGKK-Leistungen in Höhe von 150,16 €, in Summe 6.344,26 €) wurden im  Einkommensteuerbescheid 2019 als Werbungskosten steuermindernd berücksichtigt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_226`)


Ein späterer Rückersatz an das AMS ändert weder die Qualifikation der Leistung als  Arbeitslosengeld noch macht sie den ursprünglichen Zufluss des Arbeitslosengeldes iSd § 19  Abs. 1 EStG 1988 (und damit eine der Tatbestandsvoraussetzungen) rückgängig (BFG  05.08.2014, RV/7102918/2013;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_241`)


Die Rückzahlungen an das AMS und an die WGGK für die Jahre 2017 und 2018 und an die  Pensionskasse sind daher aus oben angeführten Gründen nicht als Werbungskosten zu  berücksichtigen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_242`)


Die für das Jahr 2016 getätigten Rückzahlungen, nämlich an das AMS in Höhe von 6.194,10 €  und an die WGKK in Höhe von 150,16 €, insgesamt somit 6.344,26 €, wurden bereits im  Einkommensteuerbescheid 2019 vom 15.01.2021 steuermindernd als Werbungskosten  berücksichtigt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_243`)


Die im Jahr 2019 zurückgezahlten AMS-Bezüge wirken sich steuerlich nicht aus,  da den Einnahmen vom AMS Werbungskosten in gleicher Höhe gegenüberstehen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/144700.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144700.1_22`)


Man hätte auch die Dienstnehmer zum AMS auslagern können, dann wären diese  Probleme nicht entstanden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/146676.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146676.1_28`)


steuerpflichtige Bezüge: 12.622,69 €, anrechenbare Lohnsteuer: 5.233,35 €  B. Stockburger Holz AG, 13.09.2021 bis 31.12.2021  steuerpflichtige Bezüge: 19.781,67 €, anrechenbare Lohnsteuer: 6.311,87 €  Weiters erhielt der Bf. für nachstehende Zeiträume vom AMS Notstandshilfe ausbezahlt:  Notstandshilfe für 154 Tage (01.01.2021 - 03.06.2021) 8.694,84 €  Notstandshilfe für 101 Tage (04.06.2021 – 12.09.2021) 5.702,46 €  Insgesamt (255 Tage) 14.397,30 €  2.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Stockburger Holz AG` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/146676.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146676.1_30`)


Die übermittelten Lohnzettel und AMS-Daten wurden eingesehen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_154`)


Dr. H FK 7,14  25.02.2013 60,00 TCM Akunktur Therp Dr. H xxx FK 197,4  Summe Aufwand € 209,70  Summe FK 219,32  Summe gesamt € 429,02   Bezüglich der verbleibenden € 21,42 sind in der Aufstellung des Bf. folgende Positionen  ausgewiesen:  08.02.2013, AMS-Termin, FK € 7,14  28.01.2013, AMS-Termin, FK € 7,14  30.03.2013, AMS-Termin, FK € 7,14  Ansicht FA:   Für das Finanzamt ist von den begehrten € 450,55 ein Betrag von € 419,02 belegmäßig  dokumentiert.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

## `Federal Court of Finance` 🏆

**F1:** 0.055 | **Precision:** 1.000 | **Recall:** 0.028  

**Format:** `regex`  
**Rule ID:** `15717463`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichts'.

**Content:**
```
\bBundesfinanzgericht(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.028 | 0.055 | 142 | 142 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 142 | 0 | 4901 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_39`)


Mit Schreiben vom 30.12.2019 nahm die Beschwerdeführerin bezugnehmend auf einen entsprechenden Vorhalt des Bundesfinanzgerichts unter anderem zu der Frage Stellung, wie hoch der wöchentliche Zeitaufwand der Tochter für die Vorbereitung auf die von ihr wahrgenommenen Prüfungstermine sowie für die Abfassung der sog vorwissenschaftlichen Arbeit im Zeitraum März 2018 bis Jänner 2019 gewesen sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_197`)


2. Auf Basis der zitierten ständigen Rechtsprechung des VwGH bestand bei dem im Beschwerdefall konkret festgestellten Sachverhalt nach Ansicht des Bundesfinanzgerichts aufgrund der im Vorlageantrag dargelegten glaubwürdigen beruflichen Gründe eine Notwendigkeit für die Nutzung eines betrieblich verwendeten Arbeitszimmers.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_15`)


Über die Beschwerde wurde erwogen: Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_30`)


Gegen das abweisende Erkenntnis vom 25.6.2019 des Bundesfinanzgerichts erhob der  rechtsfreundlich vertretene Bf Beschwerde gem. Art 144 B-VG an den Verfassungsgerichtshof.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_31`)


Mit Entscheidung vom 25.2.2020 hob der Verfassungsgerichtshof das Erkenntnis des  Bundesfinanzgerichts vom 25.6.2019 auf (VfGH vom 25.2.2020, E 2892/2019).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_60`)


Bei dem angefochtenen Bescheid vom 12.3.2013 handelt es sich jedoch nach Ansicht des  Bundesfinanzgerichts nicht um einen Aufhebungsbescheid gem. § 299 BAO im Sinne der  Bescheidbezeichnung, sondern um einen antragsgemäßen Aufhebungsbescheid gem. § 295  Abs. 4 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_64`)


Die Anführung des § 299 BAO in der dem Bescheidspruch vorangestellten Überschrift und in  der "Formularkennzeichnung" kommt keinerlei normativen Wirkung zu und beruht nach  Ansicht des Bundesfinanzgerichts aufgrund des eindeutigen Bescheidinhaltes offenkundig auf  einem Versehen der belangten Behörde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_112`)


Mit Schreiben vom 31.03.2020 beantwortete die Beschwerdeführerin den Vorhalt des  Bundesfinanzgerichts und führte dazu aus wie folgt:   "Die Nebentätigkeit "Erstellung von Werbetexten“ im Zuge meiner Tätigkeit im Bereich  Mediaberatung als Angestellte für das AG Druck und Verlags GmbH umfasste maximal 20  Arbeitsstunden pro Kalenderjahr!

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `AG Druck und Verlags GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_47`)


In weiterer Folge wurden am 26. Februar 2020 bei einer persönlichen Vorsprache der  Vertreterin der Bf. (laut ihren Angaben die ehemalige Lebensgefährtin des Vaters der Bf.) bei  der zuständigen Richterin des Bundesfinanzgerichts Zeugnisse (Unterlagen) der Bf. überreicht   (Kopien für Akt angefertigt).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_75`)


Wie schon im Erkenntnis des Bundesfinanzgerichts vom 9.1.2018 (welches in der  Beschwerdevorentscheidung vom 22.10.2018 zitiert wurde und den Vater der Bf. betrifft),  festgehalten wurde, ist der Antrag auf Direktzahlung nach § 14 Abs. 1 FLAG 1967 kein  Eigenantrag im Sinne des § 6 Abs. 5 FLAG 1967.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_153`)


Ein Fahrtenbuch muss nach  ständiger Rechtsprechung des VwGH und des Bundesfinanzgerichts fortlaufend und  übersichtlich geführt sein und Datum, Kilometerstrecke, Ausgangs- und Zielort sowie Zweck  jeder einzelnen Fahrt zweifelsfrei und klar angeben (vgl. VwGH 16.9.1970, 0373/70;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_169`)


IV Streitgegenstand und Rechtstandpunkte der Parteien  Der Streit geht im Kern darüber, ob Österreich Beschäftigungsstaat iSd Art 11 Abs 3 Buchstabe  a) VO 883/2004 ist und damit nach Art 67, 68 VO 883/2004 vorrangig verpflichtet ist sowie –  nach Ansicht des Bundesfinanzgerichts – alternativ darüber, ob § 13 Abs 1 EHG aF für die Bf  einen Anspruch nach rein nationalem Recht, also losgelöst vom Unionsrecht, begründet, was  die Frage aufwirft, ob § 13 Abs 1 EHG aF mittelbar diskriminierend ausgestaltet ist oder  mittelbar diskriminierend ausgelegt wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_395`)


Zur Indexierung der  Familienbeihilfe wird auf das zur EuGH-Zahl C-163/20 protokollierte  Vorabentscheidungsersuchen des Bundesfinanzgerichts hingewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_26`)


Die von der Behörde vertretene Ansicht widerspreche der Entscheidung  des Bundesfinanzgerichts (BFG 16.1.2015, RV/3100406/2013), wonach vom Begriff  „körperliche Wirtschaftsgüter“ auch elektrische Energie umfasst sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_59`)


Der festgestellte Sachverhalt ergibt sich aus den dem Bundesfinanzgericht von der  Abgabenbehörde vorgelegten Unterlagen, der E-Mail vom 03.06.2020 (Beantwortung des  Beschlusses des Bundesfinanzgerichts vom 11.05.2020) und der folgenden Beweiswürdigung:  2. Beweiswürdigung  In seiner Beschwerde vom 01.04.2019 gegen den Einkommensteuerbescheid 2018 vom  26.03.2019 machte der Bf erstmals Ausgaben für Arbeitsmittel in Höhe von 2.025 € als  Werbungskosten geltend.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_66`)


In seiner E-Mail vom 03.06.2020 zur Beantwortung des Beschlusses des Bundesfinanzgerichts  vom 11.05.2020, mit dem der Bf aufgefordert wurde, die berufliche Veranlassung jener  Arbeitsmittel nachzuweisen bzw glaubhaft zu machen, die als Werbungskosten geltend  gemacht, in der Beschwerdevorentscheidung aber nicht berücksichtigt worden seien, führte  der Bf aus, dass die mit den Rechnungen Nr. 4, 14, 17, 18, 19 und 25 erworbenen Arbeitsmittel  ausschließlich im Firmeninteresse, ohne Privatnutzen, erworben worden seien: Bei den  Rechnungen Nr. 4 und 25 handle es sich um Ausgaben für einen mobilen Router für seine USA  Reisen, damit auf einer Firmenbaustelle ein Hotspot mit Internet errichtet werden könne.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_84`)


Bezüglich der Aufforderung des Bundesfinanzgerichts im Beschluss vom 11.05.2020, jene  Ausgaben zu benennen, die laut Vorlageantrag „teilw. falsch bewertet“ worden seien, und  darzulegen, in welcher Höhe diese Ausgaben als Werbungskosten nach Meinung des Bf zu  berücksichtigen seien und dies nachvollziehbar – gegebenenfalls an Hand von Belegen – zu  begründen, führte der Bf in seiner E-Mail vom 03.06.2020 im Wesentlichen aus, dass er „seine  privaten Angelegenheiten größtenteils via mobilem Tablet inkl. separatem mobilem  Internetzugang abwickle, welches wie ein Laptop anzusehen sei, ohne beispielsweise Belege  dafür erbracht zu haben, dass er tatsächlich über ein privates Tablet und einen privaten  Internetzugang verfüge.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_628`)


2004 03.02.2006:   -6.157,13 € -5.612,51 € 544,62 €  Mehrergebnis   8.720,80 €  Auf die Bemessungsgrundlagen und Höhen der Abgaben für die Streitjahre, welche jenen  Berechnungsblättern zu entnehmen sind, die dem Erkenntnis des Bundesfinanzgerichts,  RV/7104420/2015, angefügt sind, sei verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_633`)


Von der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs wird mit diesem Erkenntnis des Bundesfinanzgerichts nicht  abgewichen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_875`)


Da das Erkenntnis des Bundesfinanzgerichts der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs folgt, war somit spruchgemäß zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_6`)


In seiner Beschwerde vom 4.9.2019 beantragte der Beschwerdeführer unter Verweis auf zwei  Erkenntnisse des Bundesfinanzgerichts, die Einkommensteuervorauszahlung für 2019 bei  Anwendung des § 124b Z 53 EStG auf die Auszahlung des Todesfallkapitals für ein zu  versteuerndes Einkommen von EUR 41.734,51 in Höhe von EUR 10.800,- festzusetzen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_101`)


Was die Rechtzeitigkeit der  Beschwerdeerhebung anlangt ist einerseits auf den klaren Gesetzestext sowie andererseits  darauf zu verweisen, dass eine in freier richterlicher Beweiswürdigung getroffene Feststellung  des Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof grundsätzlich  entzogen ist (vgl. VwGH 1.6.2017, Ra 2017/15/0037);

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_48`)


Die Bf führte ins Treffen, dass die Einschränkung der Energieabgabevergütung auf  Produktionsbetriebe durch das BBG 2011 wegen Verletzung des Bestimmtheitsgebotes des Art.  18 Abs. 1 B-VG als verfassungswidrig erachtet werde, und verwies zudem auf die Ausführungen  des Bundesfinanzgerichts (BFG 3.8.2016, RV/5100360/2013) zur möglichen  Verfassungswidrigkeit der Änderung des EnAbgVergG.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_118`)


Zur Frage des Bestandes einer Vereinbarung  zwischen der DG und dem Bf., wonach ersterer das in Österreich entstehende Steuerguthaben  zustehe, ist auf die Judikatur zu verweisen, wonach eine in freier Beweiswürdigung getroffene  Feststellung des Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof  grundsätzlich nicht zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_94`)


Diese  Rechtsansicht wird auch in der Rechtsprechung des Bundesfinanzgerichts vertreten (vgl. zB  BFG 14.07.2020, RV/5101090/2018;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_103`)


Seitens des Bundesfinanzgerichts wird die  Verwendung dieses Verkehrsmittels im Hinblick auf eine nur geringfügige Überschreitung einer  Fahrzeit von einer Stunde um 8 Minuten (Abfahrt Ort1 06:26 Uhr und Ankunft in Ort2 07:34  Uhr) auch nicht als unzumutbar erachtet.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_112`)


Diese Rechtsauffassung wird  auf Grundlage des Verordnungstextes des § 2 der Verordnung, BGBl. Nr. 624/1995, seitens des  Bundesfinanzgerichts für den gegenständlichen Fall nicht übernommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_113`)


Hinzuweisen ist auch  darauf, dass in später ergangener Rechtsprechung des Bundesfinanzgerichts als auch nach der  einschlägigen Literatur die Rechtsansicht vertreten wird, dass selbst dann, wenn die Fahrzeit  von einer Stunde nur in einer Richtung überschritten wird, keine Überschreitung des  Einzugsbereiches vorliegen würde, da die Fahrzeit in beiden Richtungen mehr als eine Stunde  betragen muss (vgl. BFG 18.07.2018, RV/7103548/2014;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_339`)


BFH 13.4.2016, III R 14/13  sowie die Entscheidungen des Bundesfinanzgerichts BFG 19.8.2016, RV/7101889/2016  betreffend im Haushalt der Mutter und des Stiefvaters in der Slowakei lebende Kinder;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_343`)


ferner die Entscheidungen des Bundesfinanzgerichts BFG  31.5.2017, RV/5100349/2016;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_130`)


Entscheidung des Bundesfinanzgerichts wegen Rechtswidrigkeit infolge Verletzung von  Verfahrensvorschriften auf und führte u.a. aus, wie er mit Erkenntnis vom heutigen Tag,  Ro 2018/15/0011, zu einem vergleichbaren Revisionsfall ausgesprochen hat, sei zur  Beantwortung der Frage, welcher der beiden Lieferungen die innergemeinschaftliche  Beförderung zuzuordnen ist, insbesondere zu klären, zu welchem Zeitpunkt die zweite  Übertragung der Befähigung, wie ein Eigentümer über den Gegenstand zu verfügen, zugunsten  des Endabnehmers stattgefunden hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_169`)


Die Bf. verwies in diesem  Zusammenhang auch auf zwei inzwischen vom VwGH aufgehobene Erkenntnisse des  Bundesfinanzgerichts (RV/2100470/2018 v. 27.4.2018 und RV/2101122/2016 v. 30.11.2017)  sowie ein in Kraft erwachsenes Erkenntnis (RV/2101353/2014 v. 2.6.2016).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_136`)


Nach einigen Entscheidungen des Unabhängigen Finanzsenats (UFS) bzw. des  Bundesfinanzgerichts (BFG) kommt es für den Werbungskostenabzug neben der beruflichen  Veranlassung auf die Werbewirksamkeit im Rahmen einer politischen oder werbenden  Veranstaltung oder in anderer Form an (UFS 06.08.2007, RV/2132-W/07;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzsenats` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_28`)


In Beantwortung der Schreiben des Bundesfinanzgerichts an die Arbeitgeberin übersandte  diese die gewünschten Unterlagen und nahm zu den an sie gerichteten Fragen wie folgt  Stellung:   In welchem Labor war die Bf. im strittigen Jahr tätig?

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_41`)


Mit Erkenntnis des Verwaltungsgerichtshofes vom  26.05.2021, Ra 2019/15/0046, wurde das am 6. Februar 2019 zu GZ. RV/3101071/2017  ausgefertigten Erkenntnis des Bundesfinanzgerichts, soweit es die Körperschaftsteuer betrifft,  wegen Rechtswidrigkeit seines Inhaltes aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_48`)


Der Verwaltungsgerichtshof hat das am 6. Februar 2019 zu GZ. RV/3101071/2017  ausgefertigten Erkenntnis des Bundesfinanzgerichts, soweit es die Körperschaftsteuer betrifft,  wegen Rechtswidrigkeit seines Inhaltes mit Erkenntnis VwGH 26.05.2021, Ra 2019/15/0046,  wegen Rechtswidrigkeit seines Inhaltes aufgehoben und begründend Folgendes ausgeführt:  2.1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_67`)


Den Sachverhaltsfeststellungen des Bundesfinanzgerichts ist zu entnehmen, dass die  mitbeteiligte Partei weiters jährlich eine große Anzahl von Grundstücken veräußert, die aus  Erbschaften stammen, welche zuvor professionell eingeworben wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_431`)


Finanzamtsvertreter: Das Protokoll ist insofern zu berichtigen, als das Faktum Fa. c auch von  der amtswegigen Ermittlungspflicht des Bundesfinanzgerichts umfasst ist und das  Bundesfinanzgericht die rechtliche Würdigung der Abgabenbehörde zu überprüfen hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_25`)


Zum Beschluss des Bundesfinanzgerichts vom 22.7.2021 wurde mit schriftlicher Stellungnahme  vom 27.7.2021 von der zuständigen Vertreterin des Finanzamtes vorgebracht, dass nach  Durchsicht des Steueraktes betreffend Aufliegen eines Vorlageantrages in Bezug auf die  Beschwerdevorentscheidung vom 24.02.2016 gegen die Bescheide über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012 und 2013 alle vom 09.11.2015 im Akt des Pflichtigen kein  Antrag mit den entsprechenden Daten aufzufinden war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_9`)


2. Beweiswürdigung  Der Sachverhalt ergibt sich aus dem Verwaltungsakt und dem Akt des Bundesfinanzgerichts  und ist unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_14`)


Durch die Bekanntgabe der Aufhebung der angefochtenen Bescheide lebt die Zuständigkeit  und die Entscheidungspflicht des Bundesfinanzgerichts gemäß § 300 Abs 5 BAO wieder auf.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_10`)


Beweiswürdigung  Der unstrittige Sachverhalt ergibt sich aus dem Akt der Finanzverwaltung und des  Bundesfinanzgerichts.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_11`)


Mit dem Beschluss vom 17.03.2021, Ra 2020/15/0113, wies der Verwaltungsgerichtshof im  zweiten Rechtsgang (siehe zuvor VwGH 19.04.2018, Ra 2017/15/0041) die Revision der Bf.  gegen das Erkenntnis des Bundesfinanzgerichts vom 13.02.2020, RV/1100190/2018, zurück.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_18`)


Mit Beschluss des Bundesfinanzgerichts vom 14. Februar 2022 wurde den Parteien dieser  Aktenstand vorgehalten und um Stellungnahme ersucht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_71`)


Mangels Beschwerde war daher die Unzuständigkeit des Bundesfinanzgerichts mit Beschluss  festzustellen und das Verfahren einzustellen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_40`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_80`)


Im gegenständlichen Fall geht der Verwaltungsgerichtshof von folgendem Sachverhalt aus:  „Mit dem am 14. Juni 2011 ergangenen Körperschaftsteuerbescheid 2010 wurde - nach den  Feststellungen des Bundesfinanzgerichts (BFG) – die Körperschaftsteuer der  revisionswerbenden GmbH festgesetzt und dabei eine steuerliche Tangente der EDGG Event GmbH&  atypisch Still in Höhe von Null berücksichtigt, woraus sich Einkünfte aus Gewerbebetrieb und ein  Einkommen der revisionswerbenden GmbH für das Jahr 2010 in Höhe von Null ergaben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `EDGG Event GmbH` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_17`)


Weiters könne er die seitens der belangten Behörde vertretene  Rechtsansicht, wonach das Erkenntnis des Bundesfinanzgerichts keine ausreichende  Begründung zur Wiederaufnahme des Verfahrens sei, nicht nachvollziehen, zumal andere  Finanzämter in genau dieser Angelegenheit bereits Rückzahlungen getätigt hätten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_15`)


Am 21.6.2021 erging das Erkenntnis des  Bundesfinanzgerichts zu GZ RV/3100362/2013.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_86`)


…“  Nach Ansicht des Bundesfinanzgerichts ist dem Bf. nun durchaus zuzugestehen, dass die Canon  Kamera inklusive Zubehör für Werbeaufnahmen bzw. für die vom Bf. angeführte  Internetplattform verwendet wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_87`)


Nach allgemeiner Lebenserfahrung und im Sinne der  Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht des Bundesfinanzgerichts aber  auch davon auszugehen, dass diese Kamera auch der privaten Nutzung diente.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_92`)


Nach Ansicht des Bundesfinanzgerichts ist auch davon auszugehen,  dass im Sinne des o.a. Erkenntnisses des VwGH 27.01.2011, 2010/15/0197, diesbezüglich bzw.  zum Zweck der erforderlichen (kurzfristigen) Buchungsabwicklung eine (nicht bloß  untergeordnete) anteilige Nutzung zur Einkünfteerzielung typischerweise unzweifelhaft  gegeben ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_122`)


Nach den  sachverhaltsmäßigen Gegebenheiten (Vermietung einer Ferienwohnung, Wohnsitz des Bf. an  der gleichen Adresse bzw. Wohnsitz der Mutter im unmittelbar gegenüberliegenden  Wohnhaus) ist nach Ansicht des Bundesfinanzgerichts zweifelsfrei von einer gemischt beruflich  und privaten Verwendung auszugehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_124`)


Nach Ansicht des  Bundesfinanzgerichts ist damit der berufliche Nutzungsanteil mit sehr hoher  Wahrscheinlichkeit nicht unterdeckt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_130`)


Somit waren seitens des Bundesfinanzgerichts in teilweise stattgebender Erledigung der  vorliegenden Beschwerde Aufwendungen für das Tablet in Höhe von 206,10 Euro als  Werbungskosten zu berücksichtigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_11`)


Aus dem weiteren Text dieser  Eingabe ist auch ersichtlich, dass gegen die Entscheidung des Bundesfinanzgerichts vom  7.12.2021 eine Revision eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_86`)


Die Rechtsvertretung ist der Feststellung des Bundesfinanzgerichts im Vorhalt, wonach der  Unterhalt (die Kosten der Unterbringung) des Bf. zur Gänze von der Stadt Wien getragen wird,  in der Vorhaltsbeantwortung nicht entgegengetreten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Heidemarie Winkler im  Beschwerdeverfahren des Siegfried Bentz, Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich, vom 13.02.2022 gegen den  Pfändungsgebührenbescheid des Magistrats der Stadt Wien Magistratssabteilung 6 Erhebungs-  und Vollstreckungsdienst, vom 31.01.2022, mit:  I. Nach Auffassung des Bundesfinanzgerichts ist in Bezug auf die Beschwerde vom 13.02.2022  gegen den Bescheid vom 31.01.2022 mit Beschwerdevorentscheidung abzusprechen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Mag. Heidemarie Winkler` (person)
- `Siegfried Bentz` (person)
- `Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_24`)


Dort sind auch die Erwägungen des Bundesfinanzgerichts  dargestellt. Vom Gerichtshof wurde für das Vorabentscheidungsverfahren die Zahl C-163/20  vergeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_33`)


Vertragsverletzungsverfahren  Klage der Europäischen Kommission vom 22. Juli 2020  Nach Stellung des Vorabentscheidungsersuchens des Bundesfinanzgerichts reichte die  Europäische Kommission mit Beschluss vom 14. Mai 2020 im Verfahren INFR(2018)2372 am  22. Juli 2020 Klage gegen die Republik Österreich beim Gerichtshof der Europäischen Union  ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Gerichtshof der Europäischen Union` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_54`)


Eine Entscheidung gemäß Art. 267 AEUV im Verfahren C-163/290 durch den Gerichtshof der  Europäischen Union sei daher im Beschwerdeverfahren vor dem Bundesfinanzgericht zu  RV/7101361/2020 für die Entscheidung des Bundesfinanzgerichts nicht mehr erforderlich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_48`)


Nach Ansicht des Bundesfinanzgerichts (BFG) ist es im Rahmen der freien Beweiswürdigung als  glaubwürdig zu erachten, dass das FH-Studium der Physiotherapie von vorneherein das  Wunschstudium des Sohnes war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Wladimir Leukhardt` (person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich` (address)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_73`)


Sie  sind keine für den Verwaltungsgerichtshof oder das Bundesfinanzgericht maßgebliche  Rechtsquellen (ständige Rechtsprechung des Verwaltungsgerichtshofes und des  Bundesfinanzgerichts, für viele VwGH 1.9.2015, Ra 2015/15/0035 mwN).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_71`)


Aus einer Vielzahl von Entscheidungen des Unabhängigen Finanzsenats und des  Bundesfinanzgerichts sei ersichtlich, dass sich derartige Betrugsunternehmen nach außen den  Anschein der Seriosität geben, sodass den Behörden zunächst ohne nähere Kenntnis der  tatsächlichen Sachverhalte das Agieren eines Betrugsunternehmens nicht auffalle (vgl. etwa  BFG 27.4.2015, RV/7104860/2014).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzsenats` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/140642.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140642.1_47`)


5. Die von der belangten Behörde mit der Einkommensteuererklärung für das Jahr 2020  erlangte Kenntnis darüber, dass die negativen betrieblichen Einkünfte für dieses Jahr nicht wie  prognostiziert € 166.193, sondern € 97.741,05 betragen, rechtfertigt nach Ansicht des  Bundesfinanzgerichts gemäß § 295a BAO keine Abänderung des Einkommensteuerbescheids  2019.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/140842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140842.1_112`)


Ist dieses Ziel wie im vorliegenden Fall  in Bezug auf die vorzunehmende Meldung zweimal nicht erreicht worden, so ist das  Kontrollsystem als unzureichend zu qualifizieren, weshalb bei Fristverstößen nach Ansicht des  Bundesfinanzgerichts nicht mehr von einer entschuldbaren Fehlleistung gesprochen werden  kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/141031.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141031.1_231`)


Eine in freier  Beweiswürdigung getroffene Feststellung des Bundesfinanzgerichts ist der Kontrolle durch den  Verwaltungsgerichtshof grundsätzlich nicht zugänglich;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/141184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141184.1_14`)


DAZU WIRD ERWOGEN:  Durch die Gründung des Bundesfinanzgerichts als Nachfolger des Unabhängigen Finanzsenates  im Zuge der Finanzverwaltungsgerichtsbarkeit sind am 1. Jänner 2014 dessen Zuständigkeiten  auf das Bundesfinanzgericht übergegangen und es sind seither Berufungen als Beschwerden im  Sinne des Art. 130 Abs. 1 BVG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_46`)


Der Meldung gem § 5 WiEReG  kommt angesichts des Zwecks der Verhinderung der Nutzung  des Finanzsystems für Geldwäscherei und Terrorismusfinanzierung, hohe Bedeutung zu.  Die Verhängung der Zwangsstrafe iHv 1.000 Euro (20% des möglichen Höchstbetrages) stellt  daher aus Sicht des Bundesfinanzgerichts keine Ermessensüberschreitung durch die belangte  Behörde dar (vgl BFG 27.03.2023, RV/7103434/2021).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_19`)


Über Ersuchen des Bundesfinanzgerichts um Ergänzung vom 24.3.2022 und vom 10.5.2023 gab  der Beschwerdeführer an, dass der Wirtschaftstreuhänder ihm den Haftungsvorhalt vom  9.11.2016 per Post übermittelt habe (Schreiben vom 12.4.2022) und dass er den  Haftungsbescheid vom 21.12.2016 „nicht in schriftlicher Form erhalten“ habe (Schreiben vom  6.6.2023).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_100`)


Der Verwaltungsgerichtshof hat ausgesprochen, dass eine Zuständigkeit des  Bundesfinanzgerichts nur dann gegeben ist, wenn zuvor von der belangten Behörde eine  Beschwerdevorentscheidung erlassen wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_127`)


Vorgelagert zum beschwerdegegenständlichen Streitpunkt, ob eine für den Vorsteuerabzug  berechtigende Rechnung gegeben ist, ist seitens des Bundesfinanzgerichts darauf hinzuweisen,  dass das Recht zur Ausübung des Vorsteuerabzugs zur Voraussetzung hat, dass es sich beim  Kauf der Eigentumswohnung um eine steuerpflichtige Lieferung an den Bf. handelt.   Gemäß § 6 Abs. 1 Z 9 lit. a UStG 1994 sind von den unter § 1 Abs. 1 Z 1 fallenden Umsätzen die  Lieferungen von Grundstücken steuerfrei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_141`)


Über ergänzende Rücksprache seitens des Bundesfinanzgerichts wurde vom zuständigen  Sachbearbeiter des Finanzamtes mit e-mail vom 26.09.2023 dem Bundesfinanzgericht  mitgeteilt: „… in Verbindung mit der Beschwerdevorlage betr.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_146`)


Diese  Feststellung wurde auch durch Einsichtnahme seitens des Bundesfinanzgerichts in die  elektronische Datenbank der Finanzverwaltung bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_150`)


Da somit von Vornherein die materiellen Voraussetzungen für den Vorsteuerabzug nicht  vorliegen (keine umsatzsteuerpflichtige Lieferung an den Bf.), ist die zwischen dem Finanzamt  und der steuerlichen Vertretung des Bf. thematisierte Streitfrage zum Vorliegen einer  Rechnung im Sinne des § 11 UStG 1994 für die Entscheidung des vorliegenden Beschwerdefalls  nicht mehr von Relevanz und konnte seitens des Bundesfinanzgerichts eine weitergehende  Auseinandersetzung mit diesem Beschwerdepunkt unterbleiben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_146`)


Aufgrund des oben zitierten Gerichtsbeschlusses (Beschluss vom 31.12.2021), wonach S. bei  der Kindesmutter seinen hauptsächlichen Aufenthalt hat sowie der Tatsache, dass der Bf. (trotz  Vorhalts des Bundesfinanzgerichts) keine Beweise für die überwiegende  Haushaltszugehörigkeit von S. (während des strittigen Zeitraums) bei ihm vorgelegt hat,  gelangt das erkennende Gericht in freier Beweiswürdigung gemäß § 167 BAO zu dem Ergebnis,  dass der Abweisungsbescheid vom 22. April 2022 sowie die Beschwerdevorentscheidung des  Finanzamts vom 10. Juni 2022 rechtsrichtig waren.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_25`)


Mit Vorhalt des Bundesfinanzgerichts vom 19.9.2023 wurde dem Bf. zur Einbringung des  Vorlageantrages am 5. Mai 2022 mitgeteilt, dass der Vorlageantrag als verspätet eingebracht  zu beurteilen sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_51`)


Außerdem reagierte der Bf. auf den Vorhalt vom 19.9.2023 des Bundesfinanzgerichts nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/142564.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142564.1_46`)


Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 28.2.2023  wurde die gegenständliche Rechtssache der mit 1.1.2023 neu besetzten Gerichtsabteilung  4013 zugewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/142990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142990.1_8`)


Zur Begründung wurde zusammengefasst ausgeführt, dass mit  Beschluss des Bundesfinanzgerichts vom 11.7.2019, RV/4100231/2012, die Beschwerde der AB  vom 10.12.2009 gegen den Feststellungsbescheid 2003 als unzulässig zurückgewiesen worden  sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/142990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142990.1_15`)


Zur Begründung wurde hinsichtlich der AB zusammengefasst ausgeführt, dass die  Beschwerde gegen die Bescheide betreffend Feststellung der Einkünfte gemäß § 188 BAO für  die Jahre 2003 bis 2005 mit Beschluss des Bundesfinanzgerichts vom 11.7.2019,  RV/4100231/2012, als unzulässig zurückgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_131`)


Was den Auskunftsbescheid als solchen betrifft, ist seitens des Bundesfinanzgerichts  darauf hinzuweisen, dass in der gegen diesen Auskunftsbescheid erhobenen Beschwerde vom  02.06.2016 u.a. ausgeführt wurde:   „Die Begründung des Auskunftsbescheides ist zwei geteilt. Im ersten Teil werden auf 26 Seiten  der Antrag samt Begründung und weiterer Beilagen wiedergegeben und auf den letzten 1 ,5  Seiten in einem mit dem Stichwort „Erwägungen“ eingeleiteten zweiten Teil die Gründe des  Bescheides angeführt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_150`)


5. Nach Ansicht des Bundesfinanzgerichts ist im Beschwerdeverfahren gegen den  Verwaltungskostenbeitragsbescheid grundsätzlich nicht über das im ergangenen  Auskunftsbescheid nach § 118 BAO beurteilte Rechtsproblem abzusprechen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_185`)


Das Bundesfinanzgericht vertritt dazu die Ansicht, dass in einem Fall, in dem im Antrag nach  § 118 BAO ein Sachverhalt aufgezeigt bzw. seitens des Finanzamtes dem Kern der Anfrage  vorab zugrunde gelegt wird, der nicht im naturalistischem Sinne gegeben, sondern das  Ergebnis ist, dass sachverhaltsmäßige Teilbereiche einer rechtlichen Würdigung zu unterziehen  sind (hier: Beurteilung der Ansässigkeit der Schwestergesellschaft in Liechtenstein), es nach  Ansicht des Bundesfinanzgerichts durchaus geboten ist, dass dieser „Teilsachverhalt“ vorab  einer rechtlichen Würdigung seitens des auskunftserteilenden Finanzamtes unterzogen wird  und im Begründungsteil angeführt wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_198`)


Die im Auskunftsbescheid angeführte  Begründung entspricht nach Ansicht des Bundesfinanzgerichts nicht diesem Erfordernis.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_201`)


Auf dieser  Grundlage und unter Berücksichtigung des Ziels des Gesetzgebers im Sinne der Schaffung von  mehr Rechtssicherheit (mehr Planungssicherheit) erscheint es nach Ansicht des  Bundesfinanzgerichts unverhältnismäßig und nicht sachgerecht, wenn im vorliegenden Fall der  Verwaltungskostenbeitrag nach § 18 Abs. 10 lit. e BAO in Höhe von 20.000,00 Euro festgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_203`)


In analoger Anwendung dieser Regelung war  der Verwaltungskostenbeitrag im vorliegenden Fall nach Ansicht des Bundesfinanzgerichts im  Sinne des in der Beschwerde angeführten Eventualbegehrens auf 500,00 Euro zu vermindern.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_15`)


Mit Schreiben des Bf. vom 29.09.2014 wurde der Vorlageantrag gemäß § 264 BAO betreff die  Einkommensteuer 2012 innerhalb der offenen Frist gestellt.   Mit dem Erkenntnis des Bundesfinanzgerichts vom 11.12.2018, RV/7105511/2014, wurde die  Beschwerde mit dem Antrag auf Abänderung des Einkommensteuerbescheides 2012  dahingehend, dass bei den Einkünften aus nichtselbständiger Tätigkeit ein Betrag von  41.087,58 € angesetzt und die Einkommensteuer 2012 auf dieser Basis neu berechnet werde,  abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_17`)


Mit Erkenntnis des Verwaltungsgerichtshofs vom 29.03.2021, Ra 2019/13/0050, wurde das  angefochtene Erkenntnis des Bundesfinanzgerichts vom 11.12.2018, RV/7105511/2014,  aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_18`)


Zum Verfahrensgang im bisherigen Verfahren sei daher auf die Ausführungen im  Erkenntnis des Bundesfinanzgerichts vom 11.12.2018, RV/7105511/2014, verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_46`)


Mit der gegen das Erkenntnis des Bundesfinanzgerichts vom 11.12.2018, RV/7105511/2014,  gerichteten außerordentlichen Revision wurde als Begründung für deren Zulässigkeit  vorgebracht, das Bundesfinanzgericht habe verkannt, dass durch die Optionsausübung zum   31.12.2012 Aktien tatsächlich erworben worden und für sehr kurze Zeit auch vom  Revisionswerber gehalten worden seien.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_49`)


Aufgrund des begründungslosen  Übergehens eines wesentlichen Parteivorbringens wurde das angefochtene Erkenntnis des  Bundesfinanzgerichts wegen Rechtswidrigkeit infolge Verletzung von Verfahrensvorschriften  gemäß § 42 Abs. 2 Z 3 lit. b und c VwGG aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_33`)


Da unmittelbar anwendbares Unionsrecht  Anwendungsvorrang genießt, ergibt sich nach Ansicht des Bundesfinanzgerichts auch kein  Verstoß gegen das objektive Nettoprinzip, wenn das EKBSG an Erträge bzw. Markterlöse  anstelle von Gewinnen anknüpft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_120`)


Diese Instrumente stehen nach Ansicht des Bundesfinanzgerichts  auch im Zusammenhang mit der Abschöpfung im Lichte des EKBSG.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_99`)


Nach der Rechtsprechung des Bundesfinanzgerichts und des Unabhängigen Finanzsenats ist  eine rückwirkende Ausstellung eines Behindertenpasses grundsätzlich nicht möglich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzsenats` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/144818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144818.1_107`)


Das Nichtbestehen der geschlechtlichen Gemeinschaft fällt bei der Beurteilung, ob eine  gemeinsame Lebensführung vorgelegen ist, nach Ansicht des Bundesfinanzgerichts nicht ins  Gewicht, da deren Fehlen nach dem festgestellten Sachverhalt, auf die Erkrankung des  Ehemanns zurückzuführen ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_34`)


Da unmittelbar anwendbares Unionsrecht  Anwendungsvorrang genießt, ergibt sich nach Ansicht des Bundesfinanzgerichts auch kein  Verstoß gegen das objektive Nettoprinzip, wenn das EKBSG an Erträge bzw. Markterlöse  anstelle von Gewinnen anknüpft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_121`)


Diese Instrumente stehen nach Ansicht des Bundesfinanzgerichts  auch im Zusammenhang mit der Abschöpfung im Lichte des EKBSG.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/145368.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145368.1_38`)


Seitens des Bundesfinanzgerichts (BFG) ist beabsichtigt, in der Entscheidung für das Streitjahr  2013 (gemeint 2014) die Werbungskosten, die der Arbeitgeber nicht berücksichtigen konnte, in  Höhe von € 3.280,80 anzusetzen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

## `Pensions Insurance` 🏆

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `b2e7cc4a`  
**Description:**
Matches Pensionsversicherungsanstalt (Pension Insurance Institution).

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.010 | 25 | 25 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 25 | 0 | 5018 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_7`)


Der  Beschwerdeführer erhalte Waisenrenten von der österreichischen  Pensionsversicherungsanstalt, der liechtensteinischen X-Versicherung und von der Y- Pensionskasse in Liechtenstein.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_14`)


Bezüge von der Pensionsversicherungsanstalt von EUR 682,- und eine  Waisenrente in Höhe von CHF 328,25 pro Monat sowie ein anteiliges Todesfallkapital in Höhe  von CHF 48.478,- von der Y-Pensionskasse in Liechtenstein.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_15`)


Dies ergibt sich aus den  vorgelegten Bestätigungen der auszahlenden liechtensteinischen Stellen und aus dem von der  Pensionsversicherungsanstalt übermittelten Lohnzettel.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_29`)


Die Qualifikation der monatlich zufließenden (Waisen-)Renten von der liechtensteinischen X- Versicherung, von der liechtensteinischen Y-Pensionskasse und von der  Pensionsversicherungsanstalt als Einkünfte aus nichtselbständiger Arbeit im Sinn des § 25 Abs.  1 Z 2 lit b EStG 1988 ist zwischen den Parteien unstrittig.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_58`)


Letztlich  stünden die Gutachten in eklatantem Widerspruch zu den Ergebnissen des Verfahrens vor der  Pensionsversicherungsanstalt, welches zum eindeutigen Ergebnis komme, dass der  Beschwerdeführer dauerhaft invalide sei.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_119`)


Unter Beachtung des oben Ausgeführten ist eine Unschlüssigkeit oder Ergänzungsbedürftigkeit  der ärztlichen Einschätzung nicht zu erkennen und sind die Gutachten und Bescheinigungen,  welche diesbezüglich auch mit den gutachterlichen Einschätzungen im Zusammenhang mit  dem Rehabilitationsgeld (aktenmäßige Beurteilung für die Pensionsversicherungsanstalt vom  4. Oktober 2018 mit Verweis auf ein Gutachten vom 22. August 2017 und die Berichte des  Casemanagers der zuständigen Krankenkasse sowie Bescheid der Pensionsversicherungsanstalt  vom 20. Oktober 2020, nach welchem medizinische Maßnahmen der Rehabilitation erst zu  diesem Zeitpunkt nicht mehr zweckmäßig sind) konform gehen, jedenfalls hinsichtlich des  Umstandes, dass beim Beschwerdeführer eine voraussichtlich dauernde Unfähigkeit sich selbst  den Unterhalt zu verschaffen bereits im Zeitpunkt der Vollendung des 21.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_156`)


Lebensjahres erstellt, befinden sich  im Einklang mit den in einem bei der Pensionsversicherungsanstalt abgeführten Verfahren und  sind daher (nicht nur) hinsichtlich der für dieses Verfahren relevanten Aussage schlüssig und  vollständig.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_11`)


Der Einspruch des Bf. vom 5. Februar 2023 (E-Mail) richtet sich ausschließlich gegen die Höhe  der Geldstrafe wegen seiner geringen Pension von monatlich 1.061,43 €, nachgewiesen durch  das Schreiben der Pensionsversicherungsanstalt vom Jänner 2023.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_22`)


Das Bundesfinanzgericht hat erwogen:  1) Sachverhalt   Der Beschwerdeführer Jason Oberbüscher  ist in Österreich ansässig und erzielte in 2022 Einkünfte von  der Pensionsversicherungsanstalt in Höhe von 15.379,53 € und von der Finanzamt Linz  R. AG in  Höhe von 5.065,83 €.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Jason Oberbüscher` (person)
- `Finanzamt Linz` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/144632.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144632.1_12`)


Auf eine Anfrage des Finanzamtes hat die Pensionsversicherungsanstalt mitgeteilt, dass der  Beschwerdeführer seit 01.12.1997 eine Rente aus der Schweiz erhält und dass diese im Jahr  2019 1.024,00 CHF monatlich betragen hat.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144632.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144632.1_13`)


Da der Beschwerdeführer keine Einkommensteuererklärung abgegeben hat wurden seine  ausländischen Rentenbezüge in Höhe der von der Pensionsversicherungsanstalt bekannt  gegebenen Beträge geschätzt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/144632.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144632.1_25`)


Auf Anfrage gab die  Pensionsversicherungsanstalt dem Finanzamt die Höhe der Schweizer Pension des  Beschwerdeführers bekannt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/144632.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144632.1_26`)


Das Finanzamt hat auf Grund der Angaben der  Pensionsversicherungsanstalt die Höhe des schweizer Pension geschätzt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/144632.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144632.1_27`)


2. Beweiswürdigung  Die Tatsache der Höhe der schweizer Pension des Beschwerdeführers ergibt sich aus der  Anfragebeantwortung der Pensionsversicherungsanstalt. Dieser wurde die Höhe der schweizer  Rente durch die zuständige Schweizer Rentenversicherungsanstalt bekannt gegeben, da auch  für die Schweiz seit 01.04.2012 die EU Verordnung 883/2004 anzuwenden ist.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/144646.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144646.1_45`)


2. Beweiswürdigung  Die Tatsache der Höhe der schweizer Pension des Beschwerdeführers ergibt sich aus der  Anfragebeantwortung der Pensionsversicherungsanstalt. Dieser wurde die Höhe der Schweizer  3 von 4 Seite 4 von 4

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Luna Fruechtenicht` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/148387.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148387.1_21`)


Die Beschwerdeführerin bezieht neben einer Pension von der Pensionsversicherungsanstalt  Einkünfte aus nichtselbstständigen Tätigkeiten von mehreren Arbeitgebern, sodass sich im  Zuge der Arbeitnehmerveranlagung regelmäßig Nachforderungen und daraus resultierend  entsprechende Einkommensteuer-Vorauszahlungen ergeben.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_10`)


Weiters begehrte die Beschwerdeführerin sowohl den  Gesamtbetrag der Einkünfte als auch die Sonderausgaben für freiwillige Weiterversicherungen  um 367,70 € herabzusetzen, da es sich bei dem Betrag in der Höhe von 464,82 €, die die  Pensionsversicherungsanstalt rücküberwies, nicht um Einkünfte aus einer nichtselbständigen  Arbeit handle, sondern um die Rückzahlung von Weiterversicherungsbeträgen, die die PVA  zuvor irrigerweise eingezogen hätte.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_34`)


Für das streitgegenständlichen Jahr 2020 lagen Lohnzettel (L 16) des Waldheimver Sicherheit AG, der  Analyse Ostalgart AG, der Pensionsversicherungsanstalt und der Berz Energie AG  vor.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Waldheimver Sicherheit AG` (organisation)
- `Analyse Ostalgart AG` (organisation)
- `Berz Energie AG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_35`)


Hierbei wurde auf dem Lohnzettel der Pensionsversicherungsanstalt unter der KZ 245 ein  Betrag von 464,82 € als steuerpflichtiger Bezug vermerkt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_36`)


Im Wege der elektronischen  Datenübermittlung wurden von der Pensionsversicherungsanstalt Sonderausgaben in der Höhe  von 832,52 € für das Jahr 2020 gemeldet.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_46`)


Die geleisteten Zahlungen an die Pensionsversicherungsanstalt waren aus den übermittelten  Kontoauszügen ersichtlich.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_47`)


Die Bestätigung über die Rückerstattung war dem Schreiben der  Pensionsversicherungsanstalt zu entnehmen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_116`)


Wie  aus den übermittelten Bankbelegen ersichtlich, wurden die Zahlungen an die  Pensionsversicherungsanstalt im Jahr 2020 (10.01.2020, 10.02.2020,10.03.2020 und  14.04.2020) getätigt.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `Fraud Investigation Office` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `a2fc42d1`  
**Description:**
Matches the Amt für Betrugsbekämpfung and Finanzpolizei.

**Content:**
```
\b(?:Amt\s+für\s+Betrugsbekämpfung|Finanzpolizei)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 5032 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_67`)


Der Beschwerdeführer sagte bei  seiner Befragung durch Organe der Finanzpolizei am 9.5.2017 unter anderem aus, dass er bis  26.5.2017 ein Firmenfahrzeug der AG genutzt habe, und weiter: „Dieses Fahrzeug muss ich am  26.5.2017 zurückgeben.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von Josefine Frikel (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der Verwaldgart GmbH bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Josefine Frikel` (person)
- `Verwaldgart GmbH` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_11`)


- Lichtbild der Finanzpolizei, woraus zu ersehen ist, dass das Fahrzeug      Kz W2 am 12.2.2010 um 14:58 Uhr am inländischen Hauptwohnsitz      des Bf geparkt ist.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_101`)


Erhebung der  Finanzpolizei).

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_111`)


Der Bf hat für dieses Fahrzeug  ab 1.11.2008 bei der X-Versicherung eine Vollkaskoversicherung abgeschlossen, die am  1.11.2009 storniert wurde (Angaben der X-Versicherung lt. Erhebung der Finanzpolizei; eigene  Angaben lt. Niederschrift).

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_116`)


Anhaltung im September  2009 mit Bf als Lenker lt. Finanzpolizei;

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_2`)


58D 3 Tür 5, 2355 Wiener Neudorf, wegen der  Finanzvergehen der Finanzordnungswidrigkeiten gemäß § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 26. Juni 2019 gegen  das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, nach  Durchführung einer mündlichen Verhandlung am 8. März 2022 in Anwesenheit des  Beschuldigten, seines Verteidigers, der Amtsbeauftragten sowie der Schriftführerin zu Recht  erkannt:  Der Beschwerde wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und das nunmehr beim Amt für Betrugsbekämpfung als Finanzstrafbehörde zur  Geschäftszahl FV geführte Finanzstrafverfahren gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_12`)


Mit 4.12.2019 wurde die Beschwerde dem Bundesfinanzgericht vorgelegt und vom Amt für  Betrugsbekämpfung als Finanzstrafbehörde wurde im Vorlagebericht beantragt, die  Beschwerde als unzulässig zurückzuweisen oder in eventu inhaltlich über die Beschwerde  abzusprechen und diese abzuweisen.

| Predicted | Gold |
|---|---|
| `Amt für  Betrugsbekämpfung` | `Amt für  Betrugsbekämpfung` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_41`)


Im Zuge von Kontrollen durch die Finanzpolizei (ehemals KIAB) des Finanzamtes Wien  12/13/14 Purkersdorf, durch das Marktamt Wien und die Wiener Gebietskrankenkasse wurde  festgestellt, dass die im Betrieb der Fa. A-KG angetroffenen Dienstnehmer zum Großteil nicht  bei der Sozialversicherung gemeldet waren.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `Wiener Gebietskrankenkasse` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/144646.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144646.1_25`)


Am 29. Februar 2024 wurde dem Beschwerdeführer der Mängelbehebungsauftrag vom  17. August 2023 durch die Finanzpolizei zugestellt. Der Mängelbehebungsauftrag hat im  Wesentlichen folgenden Wortlaut:  „Der beschwerdeführenden Partei wird gemäß § 85 Abs. 2 iVm § 2a BAO aufgetragen folgende  Mängel zu beheben:  Der Bescheidbeschwerde vom 21.06.2022 fehlt:  • die Erklärung, in welchen Punkten der Bescheid angefochten wird (§ 250 Abs. 1 lit. b BAO);

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_62`)


Die Darlegung hat, wenn die Handhabung der verletzten  Abgaben- oder Monopolvorschriften dem Zollamt Österreich obliegt, gegenüber diesem, sonst  gegenüber einem Finanzamt oder dem Amt für Betrugsbekämpfung zu erfolgen.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Zollamt Österreich` (organisation)
- `Finanzamt` (organisation)

</details>

---

## `Municipal Council` 🏆

**F1:** 0.012 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `105896f9`  
**Description:**
Matches Wiener Gemeinderat (Vienna Municipal Council).

**Content:**
```
\bWiener\s+Gemeinderat(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.012 | 31 | 31 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 0 | 5012 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_455`)


Gemäß § 6 der Verordnung des Wiener Gemeinderates über die pauschale Entrichtung der  Parkometerabgabe (Pauschalierungsverordnung), ABl. Nr. 29/2007 idF ABl.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_63`)


Nr. 71/2018, normiert:  (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen Kraft- fahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für dessen  Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu entrichten  war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß § 25 StVO  1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005, abgestellt  war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem bestimm- ten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_42`)


Über die Beschwerde wurde erwogen:  § 2 Wiener Parkometergesetz 2006 in der Fassung LGBl. für Wien Nr. 24/2012 normiert:   „(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrich-ten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_22`)


Nr. 09/2006 in der geltenden  Fassung, hat der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines  mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges  überlässt, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine  Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBI. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBI. l Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_227`)


Nr. 71/2018, normiert:  (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  17 von 22 Seite 18 von 22

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_10`)


Begründend führte die belangte Behörde aus:  „Gemäß § 2 Abs. 1 Gesetz über die Regelung der Benützung von Straßen durch abgestellte  mehrspurige Kraftfahrzeuge (Parkometergesetz 2006), LGBI. Nr. 09/2006 in der geltenden  Fassung, hat der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines  mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges  überlässt, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine  Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBl. l Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_46`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_47`)


Sichtbares Anbringen des Parkscheines/der Parkscheine  Gemäß § 3 Abs. 1 Verordnung des Wiener Gemeinderates über die Art der zu verwendenden  Kontrolleinrichtungen in Kurzparkzonen (Kontrolleinrichtungenverordnung) haben Abgabe- pflichtige, die ein mehrspuriges Kraftfahrzeug in einer Kurzparkzone abstellen, dafür zu sorgen,  dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und richtig  entwerteten Parkschein gekennzeichnet ist (vgl. hierzu auch das Erkenntnis des VwGH vom  26.01.1998, 96/17/0405).

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_64`)


Rechtsgrundlagen:  § 2 Wiener Parkometergesetz 2006 idF LGBl. für Wien Nr. 24/2012 normiert:  (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_56`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_57`)


Gemäß § 3 Abs. 1 Verordnung des Wiener Gemeinderates über die Art der zu verwendenden  Kontrolleinrichtungen in Kurzparkzonen (Kontrolleinrichtungenverordnung) haben Abgabe- pflichtige, die ein mehrspuriges Kraftfahrzeug in einer Kurzparkzone abstellen, dafür zu sorgen,  dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und richtig  entwerteten Parkschein gekennzeichnet ist.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_52`)


Damit galt das hinterlegte Schriftstück gemäß § 17 Abs. 3 ZustG am 16. Dezember 2021 (1. Tag  der Abholfrist) als zugestellt.  Das Schreiben wurde nicht behoben und binnen der zweiwöchigen gesetzlichen Frist keine  Lenkerauskunft erteilt.  Rechtslage:  § 2 Wiener Parkometergesetz 2006 in der Fassung LGBl. für Wien Nr. 24/2012 normiert:   (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen Kraft- fahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für dessen  Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu entrichten  war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß § 25 StVO  1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005, abgestellt  war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem bestimm- ten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_71`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_74`)


Dieses wird durch die Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_38`)


Rechtsgrundlagen:  § 2 Wiener Parkometergesetz 2006 idF LGBl. für Wien Nr. 24/2012 normiert:  (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen Kraft- fahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für dessen  Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu entrichten  war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß § 25 StVO  1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005, abgestellt  war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_76`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_30`)


Gemäß § 2 Abs. 1 Parkometergesetz hat der Zulassungsbesitzer und jeder, der einem Dritten  das Lenken eines mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen  Kraftfahrzeuges überlässt, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates  eine Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBl. I Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_37`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_90`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_96`)


Dieses wird durch die  Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen Kraft- fahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird (Parkometer- abgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_103`)


Dieses wird durch die Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_58`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_65`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_78`)


Rechtsgrundlagen:  § 2 Wiener Parkometergesetz 2006 lautet:  „(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_114`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_74`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_116`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_68`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird, sind Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung des Wiener  Gemeinderates über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABl Nr 2013/29).

| Predicted | Gold |
|---|---|
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/147867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147867.1_66`)


Rechtliche Beurteilung:  § 2 Wiener Parkometergesetz 2006 regelt folgendes:  „(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu  einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

</details>

---

## `Health Insurance` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `eb8982f3`  
**Description:**
Matches Wiener Gebietskrankenkasse (Vienna Regional Health Insurance).

**Content:**
```
\bWiener\s+Gebietskrankenkasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 5037 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_120`)


Die Bf und ihre Angehörigen werden laut Punkt  10 des Dienstvertrages von der Wiener Gebietskrankenkasse sozialversicherungsrechtlich  erfasst.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_125`)


Während der Zeit des Mutterschutzes hielt sich die Bf in  Deutschland auf und bezog von der Wiener Gebietskrankenkasse Wochengeld.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_258`)


Dass die Bf vom zuständigen  österreichischen Träger (Wiener Gebietskrankenkasse, WGKK) pflichtversichert wurde, beruht  daher nicht auf der Annahme, Österreich sei Beschäftigungsstaat iSd Unionsrechts.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_186`)


Dem Finanzamt wurden die im Jahr 2017 von der Bundespensionskasse AG, von der Wiener  Gebietskrankenkasse und vom Arbeitsmarktservice an die Bf. ausgezahlten Bezüge und im Jahr  2018 die vom Arbeitsmarktservice ausgezahlten Bezüge übermittelt.  Die Einkommensteuerbescheide 2017, 2018 und 2019 sind aktenkundig.

| Predicted | Gold |
|---|---|
| `Wiener  Gebietskrankenkasse` | `Wiener  Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Bundespensionskasse AG` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_30`)


Außerdem könnten die nötigen Unterlagen deshalb nicht  nachgereicht werden, da die Wiener Gebietskrankenkasse eine Anzeige erstattet habe und in  diesem Zusammenhang alle Unterlagen von der Wirtschaftspolizei in Form von Papier und  elektronischen Daten sichergestellt worden seien.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_41`)


Im Zuge von Kontrollen durch die Finanzpolizei (ehemals KIAB) des Finanzamtes Wien  12/13/14 Purkersdorf, durch das Marktamt Wien und die Wiener Gebietskrankenkasse wurde  festgestellt, dass die im Betrieb der Fa. A-KG angetroffenen Dienstnehmer zum Großteil nicht  bei der Sozialversicherung gemeldet waren.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Finanzpolizei` (organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

</details>

---

## `Administrative Court` 🏆

**F1:** 0.021 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `d6485a99`  
**Description:**
Matches Verwaltungsgerichtshof (Administrative Court).

**Content:**
```
\bVerwaltungsgerichtshof(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.021 | 54 | 54 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 54 | 0 | 4989 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_10`)


Aufgrund der außerordentlichen Revision der GmbH & Co. KG gegen das Erkenntnis des  BFG vom 15.09.2016, Zl. RV/7102261/2011, betreffend u.a. Umsatzsteuer für das Jahr  2009, mit dem die Beschwerde gegen den Umsatzsteuerbescheid 2009 als unbegründet  abgewiesen wurde, erging das Erkenntnis des Verwaltungsgerichtshofs vom 21.02.2018, Ra  2016/13/0052-6, mit dem das angefochtene Erkenntnis im Umfang der Anfechtung  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_96`)


Nach dem Erkenntnis des Verwaltungsgerichtshofs vom 24.06.2009, 2007/15/0192, mit Bezug  u.a. auf die §§ 12 UStG 1994, 8 Abs.2 KStG 1988 und die Entscheidungen des Europäischen  Gerichtshofs 62003CJ0434 Charles und Charles-Tijmens VORAB;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_115`)


Da eine Rechtsprechung des Verwaltungsgerichtshofs zu der Frage, ob Körperschaften  öffentlichen Rechts für zum Teil hoheitlich genutzte Gebäude eine Vorsteuerberichtigung  vornehmen können, fehlt, ist die Revision zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_33`)


Nach der in Ritz, BAO6, § 250 Tz 11 zitierten Rechtsprechung des Verwaltungsgerichtshofs soll  der Antrag die Behörde in die Lage versetzen, klar zu erkennen, welche Unrichtigkeit der  Beschwerdeführer dem Bescheid anlastet (vgl. VwGH 21.01.2004, 99/13/0120;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_42`)


Nach BAO6, § 85 Tz. 15 und der dort zitierten Rechtsprechung des Verwaltungsgerichtshofs  VwGH 27.04.1981, 17/2599/79;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_554`)


Beweiswürdigung:   Aufgrund des Verwaltungsakts, insbesondere des Berichts gemäß § 150 BAO, dem  Arbeitsbogen in Verbindung mit der im fortgesetzten Verfahren vorgelegten Kalkulation des  steuerlichen Vertreters, mit der sämtliche Mängel, die in der Parteibeschwerde im  verwaltungsgerichtlichen Verfahren sowie im Erkenntnis des Verwaltungsgerichtshofs vom  22.07.2015, 2012/13/0037 angeführt wurden, in Zahlen berücksichtigt wurden, ist als erwiesen  anzunehmen, dass mit den Verweisen auf die Tz.4 PB bis 6 PB in dem für die Begründung der  Wiederaufnahmebescheide bestimmten Teil des Prüfberichts die Mängel in den  Grundaufzeichnungen UND das Ergebnis der kalkulatorischen Schätzung gemäß § 184 BAO für  die Streitjahre als Wiederaufnahmegründe im Sinn des § 303 BAO Bestandteil der  angefochtenen Wiederaufnahmebescheide sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_597`)


Hinsichtlich der im Erkenntnis des Verwaltungsgerichtshofs, Gz. 2012/13/0037,  angesprochenen Abschnitte ist auf die Ergebnisse der verschiedenen Anstalten zu verweisen,  die Abschnitte von den Fleischproben innerhalb einer Bandbreite von 6% bis 35% belegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_625`)


Wie aus dem Erkenntnis des Verwaltungsgerichtshofs vom 10.05.1994,  94/14/0024, ersichtlich, ist aber bei der Beurteilung, ob ein in der Ermessensentscheidung  nach § 303 Abs. 4 BAO zu berücksichtigendes Missverhältnis zwischen Bedeutung des  Wiederaufnahmegrundes und den zu erwartenden tatsächlichen Bescheidänderungen vorliegt,  keine Saldierung von Umsatz- und Einkommensteuer schon aus finanzausgleichsrechtlichen  Gründen vorzunehmen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_633`)


Von der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs wird mit diesem Erkenntnis des Bundesfinanzgerichts nicht  abgewichen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_666`)


In Hinblick auf das kassatorische Erkenntnis des Verwaltungsgerichtshofs vom VwGH  22.07.2015, 2012/13/0037 war im fortgesetzten Verfahren daher auf das sehr spezifische  Vorbringen vor allem über die Zusammenhänge zwischen den Umsätzen und dem Anfall von  Fleischabfällen in der Betriebsstätte W-Platz einerseits und im nahegelegenen Betrieb der  Tochtergesellschaft andererseits konkret einzugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_687`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs zu § 166 BAO heißt beweisen, ein  behördliches Urteil über die Gewissheit des Vorliegens einer entscheidungsrelevanten  Tatsache herbeiführen (VwGH 14.12.1994, 93/16/0191;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_795`)


Wenn die Kalkulation der Betriebsprüfung die Daten der Gegenkalkulation der Bf. über größere  Portionen/einen erhöhten Warenverbrauch wegen Schwund und Personalverbrauch umfasst,  obwohl keine Aufzeichnungen bezüglich Schwund/Personalverbrauch vorgelegt worden sind,  ist es das kassatorische Erkenntnis des Verwaltungsgerichtshofs, welches Gewissheit darüber  50 von 63 Seite 51 von 63

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_823`)


Angesichts des letztzitierten Erkenntnis des Verwaltungsgerichtshofs in Verbindung mit dem  Bericht gemäß § 150 BAO betreffend die Abgaben für die Jahre 2012 bis 2016 war zu den im  Arbeitsbogen abgelegten Beweismittel, die dem Bericht gemäß § 150 BAO betreffend die  Abgaben für die Streitjahre zugrunde gelegen waren, festzustellen, dass dem von der  Betriebsprüfung zitierten Bericht im F-Magazin, erschienen im Compress-Verlag, insoweit  vorrangig Reklamecharakter zuzusprechen war, als das (Ende 2015 eingestellte)  Monatsmagazin in den das Beschwerdeverfahren betreffenden Streitjahren eine Publikation  jenes Compress-Verlages gewesen war, der für die Stadt Wien in den Streitjahren  Auslandsbüros in Europa betrieben hatte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_875`)


Da das Erkenntnis des Bundesfinanzgerichts der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs folgt, war somit spruchgemäß zu entscheiden.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_905`)


Im gegenständlichen Beschwerdepunkt ist eine Revision unzulässig, weil eine Rechtsfrage von  grundsätzlicher Bedeutung dadurch, dass das Bundesfinanzgericht im fortgesetzten Verfahren  der Entscheidung des Verwaltungsgerichtshofs über die Beschwerde der Bf. gegen die  Abgaben- und Haftungsbescheide für die Jahre 2003 bis 2005 (VwGH 22.07.2015,  2012/13/0037) gefolgt ist, nicht vorliegt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_71`)


Bei der Aufforderung zur Erteilung einer Lenkerauskunft handelt es sich um ein Administrativ- verfahren (vgl. VwGH 23.02.2000, 99/03/0314, ergangen zum vergleichbaren § 103 Abs. 2 KFG  nach ständiger Judikatur des Verwaltungsgerichtshofs (z.B. VwGH 23.02.2000, 99/03/0314).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_122`)


Judikatur des Verwaltungsgerichtshofs (z.B. VwGH 23.02.2000, 99/03/0314) um ein Admini- strativverfahren und somit um eine vom Vorwurf des Grunddeliktes unabhängige (admini- strative) Maßnahme, was bedeute, dass die Lenkeranfrage ein eigenständiges Verfahren bilde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_90`)


Nach der ständigen Judikatur des Verwaltungsgerichtshofs fällt einem Verpflichteten, der nicht  selbst in der Lage ist, für die Einhaltung der Verwaltungsvorschriften zu sorgen, nur dann kein  Verschulden zur Last, wenn er glaubhaft macht, dass er es bei der Auswahl der von ihm  Beauftragten und deren Überwachung nicht an der pflichtgemäßen Sorgfalt hat fehlen lassen  (Erkenntnis des Verwaltungsgerichtshofes vers.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_56`)


Nach den Erkenntnissen des Verwaltungsgerichtshofs vom 2. Juni 2004, 2003/13/0074,  13. September 1977, 2696, 2753, 2754/76, und 10. September 1998, 93/15/0051 kann ein  Steuerpflichtiger, der wegen seiner Körperbehinderung zur Fortbewegung auf einen PKW  angewiesen ist, die anteiligen Kfz-Kosten, die ihm durch die Mehrbenützung seines Kfz  gegenüber gesunden Abgabepflichtigen entstehen, als außergewöhnliche Belastung geltend  machen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_80`)


Eine nähere Definition des Vertreterbegriffs ist der Verordnung BGBL II 382/2001 idgF nicht zu  entnehmen, sodass nach der ständigen Rechtsprechung des Verwaltungsgerichtshofs auf die  Verkehrsauffassung abzustellen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_97`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  Lösung zur Anwendung zu bringen, mit welcher materiell am wenigsten in das nationale Recht  eingegriffen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_98`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH  24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_99`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  Lösung zur Anwendung zu bringen, mit welcher materiell am wenigsten in das nationale Recht  eingegriffen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_100`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH  24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_182`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  Lösung zur Anwendung zu bringen, mit welcher materiell am wenigsten in das nationale Recht  eingegriffen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_183`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH 24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_158`)


Studienbeginn wegen  eines Auswahlverfahrens erst nach diesem Verfahren möglich ist, steht für die Zeit zwischen  der Beendigung des Zivildienstes und dem Studienbeginn (des Wunschstudiums) die  Familienbeihilfe gemäß § 2 Abs. 1 lit e FLAG 1967 zu.  Das im WS 2021/22 begonnene FH-Studium der Physiotherapie wurde daher im Sinne der  oben dargestellten Rechtsprechung des Verwaltungsgerichtshofs zum frühestmöglichen  Zeitpunkt nach Beendigung des Zivildienstes und positiver Absolvierung des erforderlichen  Aufnahmeverfahrens begonnen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_53`)


Zulässigkeit einer Revision:  Die Revision ist nicht zulässig, weil die gegenständliche Rechtsfrage (Beurteilung des  Neuhervorkommen von Tatsachen aus der Sicht des Antragstellers bei der antragsgebundenen  Wiederaufnahme) durch die zitierte Rechtsprechung des Verwaltungsgerichtshofs bereits  geklärt ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_127`)


21.9.2005, 2001/13/0059,  0060, 0061) besteht bereits eine umfangreiche Rechtsprechung des Verwaltungsgerichtshofs.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/141586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141586.1_47`)


Im vorliegenden Fall liegt keine Rechtsfrage von grundsätzliche Bedeutung vor, da die  Entscheidung auf der einheitlichen, oben zitierten Rechtsprechung des  Verwaltungsgerichtshofs basiert.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/142831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142831.1_57`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofs ist die Beibehaltung des  Familienwohnsitzes aus der Sicht einer Erwerbstätigkeit, die in unüblicher Entfernung von  diesem Wohnsitz ausgeübt wird, niemals durch die Erwerbstätigkeit, sondern immer durch  Umstände veranlasst, die außerhalb dieser Erwerbstätigkeit liegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/142831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142831.1_62`)


Familienwohnsitz ist nach der Rechtsprechung des Verwaltungsgerichtshofs jener Ort, an  dem ein verheirateter Steuerpflichtiger mit seinem Ehepartner oder ein unverheirateter  Steuerpflichtiger mit seinem in eheähnlicher Gemeinschaft lebenden Partner einen Hausstand  unterhält, der den Mittelpunkt der Lebensinteressen dieser Personen bildet (VwGH 25.2.2022,  Ra 2022/13/0010).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_189`)


In Bezug auf den in der Liste angeführten Kostenersatz in  Höhe von € 16.951,00 im Zusammenhang mit einem Verfahren vor dem  Verwaltungsgerichtshof (ZI Ra 2015/13/0039) ist darauf zu verweisen, dass aus dem zweiten  Satz des Spruches der Entscheidung des Verwaltungsgerichtshofs hervorgeht, dass der Bund  der Revisionswerberin Aufwendungen in der Höhe von lediglich € 1.346,40 zu ersetzen hat.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_17`)


Mit Erkenntnis des Verwaltungsgerichtshofs vom 29.03.2021, Ra 2019/13/0050, wurde das  angefochtene Erkenntnis des Bundesfinanzgerichts vom 11.12.2018, RV/7105511/2014,  aufgehoben.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_19`)


Das kasssatorische Erkenntnis des Verwaltungsgerichtshofs vom 29.03.2021, Ra 2019/13/0050,  ging von folgenden Sachverhalt aus:    „Dem Revisionswerber wurden von seinem Arbeitgeber in den Jahren 2003 und 2006 Optionen  auf den Erwerb von Beteiligungen eingeräumt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_48`)


Das  Bundesfinanzgericht habe ein von ihm als wesentlich angenommenes Sachverhaltselement  entgegen den vorliegenden Nachweisen und entgegen dem Vorbringen des Revisionswerbers  beurteilt.    Mit dem Erkenntnis des Verwaltungsgerichtshofs vom 29.03.2021, Ra 2019/13/0050, wurde  unter Bezugnahme auf das Vorbringen des Bf. vor dem Bundesfinanzgericht, demnach der Bf.  im Rahmen der Ausübungsart „Exercise & Sell“ Aktien erworben habe, und  Transaktionsbestätigungen über die Optionsausübung vorgelegt hätte, in Verbindung mit der  Tatsache, dass das Bundesfinanzgericht sich demgegenüber auf die Aussage des  Finanzdirektors des Arbeitgebers gestützt hätte und aus dieser den Schluss gezogen hätte, dass  es zu keinem Erwerb der Aktien gekommen sei, bestätigt, dass die Beschreibung der  Ausübungsart „Exercise & Sell“ dahingehend, dass der Bf. den Bruttogewinn (Differenz  zwischen Ausübungspreis und aktuellem Marktpreis der Aktie) erhält, ein Indiz dafür, dass es  zu keinem Erwerb der Aktien gekommen sei, sein könne und dem Bundesfinanzgericht  vorgehalten, sich nicht mit den vorgelegten Transaktionsbestätigungen auseinandergesetzt  und dazu keine Feststellungen getroffen zu haben.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_135`)


Die Entscheidung hängt daher nicht  von der Lösung einer Rechtsfrage, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofs nicht einheitlich beantwortet wird, ab.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/144218.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144218.1_14`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofs ist die Unverhältnismäßigkeit des  Nachteils aus der Verpflichtung zu einer Geldleistung bereits im Antrag auf Zuerkennung der  aufschiebenden Wirkung durch zahlenmäßige Angaben über die gesamten wirtschaftlichen  Verhältnisse des Antragstellers zu konkretisieren (vgl bereits VwGH 25.2.1981, VwSlg  10.381/A).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_64`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs zu § 115 BAO ist die Behörde zur  Verwertung des ihr zugänglichen Aktenmaterials nach dem Grundsatz der Amtswegigkeit des  Verfahrens verpflichtet (VwGH 23.05.1990, 89/17/0109;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_71`)


Der Grundsatz der strikten Amtswegigkeit der Sachverhaltsermittlung tritt  nach Ansicht des Verwaltungsgerichtshofs generell bei Begünstigungsbestimmungen in den  Hintergrund (z.B. VwGH 18.11.2003, 98/14/0008;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_75`)


Zur diesbezüglichen Rechtsprechung betreffend  die Begünstigungsbestimmung des § 34 EStG 1988 sei auf die Erkenntnisse des   Verwaltungsgerichtshofs „VwGH 29.01.2003, 99/13/0179“;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_94`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs zu § 35 EStG 1988 ist unter einer  Behinderung nur eine längerfristige Einschränkung zu verstehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_416`)


Zweck der vom Gesetzgeber durch § 278 (1) BAO eingeräumten Möglichkeit einer Erledigung  durch Bescheidaufhebung und Zurückverweisung des Verfahrens an die Abgabenbehörde ist  die Beschleunigung des BFG-Rechtsmittelverfahrens und die Entlastung des  Verwaltungsgerichtshofs.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_161`)


Ist die diesbezügliche  Zuständigkeit auf eine andere Abgabenbehörde übergegangen, so steht die Entscheidung der  zuletzt zuständig gewordenen Abgabenbehörde zu.“  § 93a BAO bestimmt: „Die für Bescheide geltenden Bestimmungen (insbesondere die §§ 198  Abs. 2, 200 Abs. 2, 210, 295, 295a, 303) sind, soweit nicht anderes angeordnet ist, sinngemäß  auf Erkenntnisse und Beschlüsse der Verwaltungsgerichte sowie auf in der Sache selbst  ergangene Entscheidungen des Verwaltungsgerichtshofs anzuwenden.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_300`)


Umsatzschätzung als zu hoch erwiesen und würde der Ansatz, einen Aufschlag  auf sämtliche unrabattierte Roaming-Gebühren anzusetzen, nicht die wahren Gegebenheiten  widerspiegeln, wäre es Sache der Bf. gewesen, (spätestens) im Vorlageantrag (vgl.  Vorhaltscharakter der Beschwerdevorentscheidung, BFG vom 28.10.2021, RV/7103167/2013  bzw. VwGH 31.05.2011, 2008/15/0288, VwGH 23.05.1996, 94/15/0024 und VwGH 23.5.2012,  2008/17/0115, wonach der Berufungsvorentscheidung nach ständiger Rechtsprechung des  Verwaltungsgerichtshofs Vorhaltscharakter zukommt und auch der Vorschrift des § 183 Abs. 4  BAO entsprochen wird, wonach den Parteien vor Erlassung des abschließenden Sachbescheides  Gelegenheit zu geben ist, von den durchgeführten Beweisen und vom Ergebnis der  Beweisaufnahme Kenntnis zu nehmen und sich dazu zu äußern) nebst einer ordnungsmäßigen  Buchführung eine präzise und plausible Erläuterung, wie die  Umsatzsteuerbemessungsgrundlage ermittelt wurde, zB mithilfe von Auszügen aus dem  Rechnungswesen, Abrechnungen, sonstigen Aufzeichnungen etc., vorzulegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/145892.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145892.1_82`)


Ein  solcher Eventualantrag ist nach der Rechtsprechung des Verwaltungsgerichtshofs zulässig (vgl.  z.B. VwGH 06.02.1990, 89/14/0256 bzgl.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/146634.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146634.1_53`)


Judikatur des Verwaltungsgerichtshofs dann angemessen  im Sinne der Mängelbehebungsvorschriften, wenn die Fristbemessung den besonderen  Verhältnissen sachgerecht Rechnung trägt und die Berufungswerberin in die Lage versetzt  wird, dem Auftrag innerhalb der gesetzten Frist ordnungsgemäß nachzukommen (vgl.  VwGH 30.3.2006, 2006/15/0003).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_182`)


Mieters anschaffe bzw. errichte] nach der mittlerweile ständigen Rechtsprechung des  Verwaltungsgerichtshofs zur fremdüblichen Mietentgelthöhe von der Kapitalamortisation und  einer angemessenen Verzinsung bestimmt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_235`)


Unter Bezugnahme auf die Rechtsprechung des  Verwaltungsgerichtshofs sei daher das Mietverhältnis dadurch, dass die Umsatzsteuer die  Vorsteuer in einem Zeitraum von 20 Jahren nicht übersteige, nicht anzuerkennen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_260`)


Laut Erkenntnis des Verwaltungsgerichtshofs VwGH 16.02.2006, 2004/14/0082, sei von einer  Vermietung nach § 1 Abs. 1 LVO bei einem Gebäude, das mit fünf Wohnungen deutlich das  Ausmaß des in § 1 Abs. 2 LVO angesprochenen Wohnraums übersteige, auszugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_419`)


Nach der Rechtsprechung  des Verwaltungsgerichtshofs ist daher eine Kriterienprüfung bei der sogenannten „großen  Vermietung“ nicht anzustellen (VwGH 26.01.2017, Ro 2014/15/0006;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_437`)


Eine Prognoserechnung hat der Rechtsprechung des Verwaltungsgerichtshofs zufolge  Gewissheit darüber, dass die große Vermietung einen Gesamtüberschuss im absehbaren  Zeitraum erwarten lässt, zu verschaffen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_61`)


Die Anwendung eines Progressionsvorbehaltes, entspricht der ständigen Rechtssprechung des  Verwaltungsgerichtshofs und wurde auch konkret bezogen auf deutsche Pensionseinkünfte  durch den Verwaltungsgerichtshof bestätigt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_62`)


Das Bundesfinanzgericht weicht mit diesem  Erkenntnis nicht von der Rechtsprechung des Verwaltungsgerichtshofs ab und es liegt daher  keine Rechtsfrage von grundsätzlicher Bedeutung vor womit eine Revision nicht zuzulassen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

</details>

---

## `Constitutional Court` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `20e3dd2b`  
**Description:**
Matches 'Verfassungsgerichtshof' in various cases (nominative, genitive, etc.).

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 5020 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_37`)


Im  Fall einer Beschwerde gegen eine Entscheidung eines Verwaltungsgerichte3s, der ein auf  Antrag eingeleitetes Verwaltungsverfahren vorausgegangen ist, muss dieser  verfahrenseinleitende Antrag überdies vor Bekanntmachung des dem unter Pkt. 1 genannten  Erkenntnis zugrunde liegenden Prüfungsbeschlusses des Verfassungsgerichtshofes eingebracht  worden sein (VfSlg. 17.687/2005).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_40`)


Die Anträge gemäß § 295  Abs. 4 BAO wurden am 20. Dezember 2012 bzw. am 30. April 2013 gestellt, der dem unter Pkt.  1 genannten zugrunde liegende Prüfungsbeschluss des Verfassungsgerichtshofes wurde am 11.  Juli 2019 bekannt gemacht;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_41`)


die verfahrensleitenden Anträge wurden also vor Bekanntmachung  des Prüfungsbeschlusses des Verfassungsgerichtshofes eingebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_75`)


In Umsetzung des Erkenntnisses des Verfassungsgerichtshofes ist der letzte Satz des § 295 Abs.  4 BAO nicht anwendbar.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_42`)


Das Bundesfinanzgericht hat bereits wiederholt - in Anlehnung an die Rechtsprechung des  Verfassungsgerichtshofes - zum Ausdruck gebracht, dass es keine Zweifel an der  Verfassungsmäßigkeit des Bewertungsgesetzes hegt (vgl. BFG 10.01.2017, RV/4100647/2016;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_84`)


Nach Auffassung d es Verfassungsgerichtshofes ist im  Licht der geltend gemachten gleichheitsrechtlichen Bedenken nicht entscheidend, ob und  inwieweit sich der Begriff des Glücksspiels gemäß §58 Abs. 3 GSpG mit jenem in § 1 GSpG deckt;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_126`)


Dieser Rechtsansicht traten Ehrke-Rabel/Sumper, Länderübergreifende Preisausschreiben und  Glücksspielabgabe, taxlex 2017, 341 unter Verweis auf die obgenannten Entscheidungen des  Verfassungsgerichtshofes VfGH 12.12.2016 G 650/2015 entgegen: Es ist systematisch  nachvollziehbar, dass der Verfassungsgerichtshof Preisausschreiben als Glücksspiele qualifiziert.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_100`)


Die Familienbeihilfenbeträge werden  aufgrund einer Entscheidung des Verfassungsgerichtshofes in regelmäßigen Abständen  angehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_31`)


Nach der Rechtsprechung des Verfassungsgerichtshofes erfordert und erlaubt die Wendung  "dass zu entscheidende Rechtsfragen besondere Schwierigkeiten rechtlicher Art aufweisen"  eine Prüfung, ob im konkreten Einzelfall für den Antragsteller besondere Schwierigkeiten  bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_60`)


Besondere, in der Person des Einschreiters  liegende Umstände, die eine Bewilligung der Verfahrenshilfe vor dem Hintergrund der zitierten  Rechtsprechung des Verfassungsgerichtshofes notwendig machen würden, wurden nicht  vorgebracht und sind nicht auch nicht hervorgekommen: Dass der Einschreiter wegen einer  schweren Hypertonie und einem Rückenleiden die Fahrertätigkeit demnächst wieder aufgeben  müsse, deutet nicht darauf hin, dass seine Fähigkeiten, sein Anliegen wirksam zu verteidigen,  eingeschränkt wären.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_30`)


Die Norm unterliege umso strengeren Anforderungen der Bestimmtheit, je intensiver  der mit der Norm verbundene Eingriff in die Grundrechte der Normadressaten ausfällt.   Auch nach der Rechtsprechung des Verfassungsgerichtshofes widerspreche es dem  Rechtsstaatsprinzip, wenn man nur mit subtiler Sachkenntnis, außerordentlichen  methodischen Fähigkeiten und einer gewissen Lust zum Lösen von Denksportaufgaben  verstehen könne, welche Anordnungen in einem Gesetz getroffen werden (VfGH 29.6.1990, G  81/90).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_154`)


Das Formular für postalische oder persönliche Einbringung  liegt in der Geschäftsstelle des Verfassungsgerichtshofes auf;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_155`)


es kann auch von der Website  des Verfassungsgerichtshofes (www.vfgh.gv.at; im Bereich Kompetenzen und Verfahren /  Verfahrenshilfe) heruntergeladen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_157`)


Zur Vorgangsweise für die elektronische Einbringung und zu  weiteren Informationen wird auf die Website des Verfassungsgerichtshofes verwiesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_89`)


Judikatur des Verfassungsgerichtshofes  Der VfGH entschied im Erkenntnis vom 29.09.1988, dass die Bestimmung des § 103 Abs. 2 KFG  verfassungskonform ist und weder Art. 90 Abs. 2 B-VG noch Art. 6 EMRK verletzt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_142`)


Verfassungsgerichtshofes  (vgl. noch einmal das Erkenntnis des LVwG Linz vom 24.11.2020, LVwG-603901/9/KHa).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_77`)


Verordnung BGBl. Nr. 624/1995 idF BGBl. II Nr. 449/2001 muss es sich demnach - ungeachtet  dessen, ob der Auszubildende dieses auch tatsächlich benutzen kann - um ein solches handeln,  welches während des Tages Verkehrsverbindungen mit einer Fahrtdauer von höchstens einer  Stunde sicherstellt (vgl. VwGH 20.12.2016, Ra 2014/15/0011, Rn 21 f; vgl. auch VwGH  08.07.2009, 2007/15/0306, unter Hinweis auf das Erkenntnis des Verfassungsgerichtshofes  vom 11.12.1986, B 437/86).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_53`)


Dieser ist hinzunehmen, weil pauschalierende Regelungen, die der  Gesetz- oder Verordnungsgeber insbesondere im Interesse der Verwaltungsökonomie trifft,  nach der Rechtsprechung des Verfassungsgerichtshofes selbst dann zulässig sind, wenn dabei  Härtefälle entstehen können, sofern diese nicht in unverhältnismäßiger Weise ins Gewicht  fallen (VfGH 08.03.2002, G 308/01;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_101`)


Ist eine Verordnung wegen Gesetzwidrigkeit aufgehoben worden oder hat der  Verfassungsgerichtshof gemäß Art 139 Abs. 4 B-VG ausgesprochen, dass eine Verordnung  gesetzwidrig war, so sind alle Gerichte und Verwaltungsbehörden an den Spruch des  Verfassungsgerichtshofes gebunden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_90`)


29.4.2010, 2007/15/0227) und Verfassungsgerichtshofes (VfGH 30.9.1997,  B2/96).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_11`)


Aufgrund einer Empfehlung der  Finanzprokuratur wäre davon auszugehen, dass bei Einbringung einer Klage (Regressforderung)  gegen die Bediensteten, welche nach Rechtsprechung des Verfassungsgerichtshofes  (GZ A7/96-B 2844/95 vom 02.10.1996) vorgegeben sei, von einer dreijährigen Verjährungszeit  ab Zahlung des Dienstgebers (06.12.2018) auszugehen wäre und nicht von einer allgemeinen  (30-jährigen) Verjährungsfrist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_71`)


Diese Rechtsansicht des  Verwaltungsgerichtshofes gründet auf der Rechtsprechung des Verfassungsgerichtshofes,  wonach Aufwendungen, bei denen die in § 34 Abs. 6 EStG 1988 vorgesehene Anrechnung von  Pflegegeld besonders widersinnig und daher unsachlich wäre, erst durch die gesetzeskonforme  7 von 9 Seite 8 von 9

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/147744.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147744.1_49`)


von Rechtsauslegungen des Verfassungsgerichtshofes oder des Verwaltungsgerichtshofes  abweicht, wenn im Vertrauen auf die betreffende Rechtsprechung für die Verwirklichung des  die Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

</details>

---

## `Administrative Court Vienna` 

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `2e33eeab`  
**Description:**
Matches 'Verwaltungsgericht Wien'.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 5035 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_70`)


Die Beschwerde an das Verwaltungsgericht Wien ist daher zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_297`)


Die Beschwerde an das Verwaltungsgericht Wien ist daher zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_56`)


Nicht berücksichtigt wird, dass das Straferkenntnis MA67/GZ/2020 vom 26.01.2021  gleicher Zeitpunkt (Halten und Parken) bereits durch das Verwaltungsgericht Wien behoben  wurde und eine Ermahnung erteilt wurde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_34`)


Über Beschwerden in allen übrigen Fällen  entscheidet das Verwaltungsgericht Wien.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_24`)


Die beim Verwaltungsgericht Wien eingelangte Beschwerde wurde zuständigkeitshalber an das  Bundesfinanzgericht samt dem bezughabenden Verwaltungsakt weitergeleitet (Datum des  Einlangens: 21. Juli 2021).

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_15`)


Mit Eingabe des BF vom 22.08.2022 an das Verwaltungsgericht Wien (weitergeleitet an das  BFG am 08.09.2022) ersucht dieser um Bekanntgabe des Verfahrensstandes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_29`)


Diesen Bestimmungen zufolge wäre das Bundesfinanzgericht (Verwaltungsgericht des Bundes  für Finanzen) – und nicht das Verwaltungsgericht Wien – für die Entscheidung über die  Beschwerde des BF vom 13.02.2022 zuständig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_22`)


Er wird dem Magistrat der Stadt  Wien nicht vorgelegt, wohl aber dem Verwaltungsgericht Wien im Zuge eines allfälligen Be- schwerdeverfahrens.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

</details>

---

## `Police Authority` 

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `ae762155`  
**Description:**
Matches 'Landespolizeidirektion' followed by a location, stopping before verbs or punctuation.

**Content:**
```
\bLandespolizeidirektion\s+(?:Wien|Vorarlberg|Salzburg|Tirol|Steiermark|Kärnten|Oberösterreich|Niederösterreich|Burgenland)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 16 | 16 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 0 | 5027 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_8`)


- Einstellungsschein der Landespolizeidirektion Niederösterreich vom 28. März 2019 betreffend  den Sohn der Bf.: „Aufgrund Ihres Ansuchens um Aufnahme in die Bundespolizei werden Sie  mit Wirkung vom 13. Mai 2019 in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich eingestellt.   1 von 17 Seite 2 von 17

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Niederösterreich` | `Landespolizeidirektion  Niederösterreich` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Niederösterreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_57`)


Die Bf. brachte daraufhin den Vorlageantrag ein, mit dem sie die in der Beschwerde gemachten  Ausführungen wiederholt.   Die Beschwerdevorlage des Finanzamtes erfolgte mit nachstehendem Sachverhalt und  Anträgen:   Sachverhalt:   Der Sohn der Beschwerdeführerin … begann am 13.05.2019 die exekutivdienstliche Ausbildung  im Bildungszentrum Y.. Die Einstellung in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich erfolgte mit Sondervertrag nach § 36 VBG 1948.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Niederösterreich` | `Landespolizeidirektion  Niederösterreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_4`)


Weitere zur Beantragung der Familienbeihilfe gemachte Angaben:   Beruf der Antragstellerin: Auszubildender   Dienstgeber: Landespolizeidirektion Wien, [Adresse]  beschäftigt seit: 01.09.2018   Tätigkeit: Auszubildender  vorauss.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_65`)


Aus diesem Dienstvertrag ist insbesondere ersichtlich:   Organisationseinheit, die für den Bund abschließt, und Dienstbehörde: Landespolizeidirektion  Wien   Befristung: Dieser Dienstvertrag ist auf 24 Monate befristet   Beschäftigungsart: VB des Bundes mit Sondervertrag für die exekutivdienstliche Ausbildung   Entlohnungsschema: …   Besoldungsdienstalter: … Die in diesem Ausbildungsverhältnis zurückgelegte Dienstzeit wird im  Falle der Übernahme in ein öffentlich rechtliches Dienstverhältnis oder im Falle eines  unbefristeten Dienstverhältnisses nach dem VBG 1948 zur Gänze angerechnet.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_33`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien gelegt wurde, und in die  eingeholte Lenkerauskunft auf Grund der Aufforderung zur Bekanntgabe des Fahrzeugienkers  erhoben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_253`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige vom 04.07.2018 samt Fotos, welche  von einem Organ der Landespolizeidirektion Wien erstattet wurde sowie der Lenkerauskunft  vom 02.02.2019.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (in  Folge kurz Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2021 an, sie habe das  Fahrzeug am 26. Mai 2021 in der gebührenpflichtigen Kurzparkzone in 1180 Wien, Ranftlgasse  21 ggü, ohne einen für den Beanstandungszeitpunkt 18:57 Uhr gültigen Parkschein abgestellt,  da die Parkzeit überschritten gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_28`)


Bei den Parkraumüberwachungsorganen (Meldungsleger) handelt es sich um Kontrollorgane  der Landespolizeidirektion Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_8`)


Fröbelgasse 39, vom Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion  Wien beanstandet, da nach dessen Wahrnehmungen der im Fahrzeug hinterlegte Parkschein  Spuren von entfernten Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem in Deutschland wohnhaften  Beschwerdeführer (Bf.), unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (D)  (Fa. XY) eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2022 an, er habe das  Fahrzeug am 27. Mai 2022 in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Ausstellungstraße 33, ohne einen für den Beanstandungszeitpunkt 17:50 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_7`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans A204 der Parkraumüberwachung  der Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_19`)


Dazu werde Folgendes bemerkt:   Die Anzeigeangaben des anzeigelegenden Organes der Landespolizeidirektion Wien seien klar,  deutlich und frei von Widersprüchen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_7`)


Entscheidungsgründe  Verfahrensgang:  Verfahren 1) GZ. MA67/Zahl1/2023:   Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ1) am  2. März 2023 um 10:21 Uhr in 1010 Wien, Universitätsring gegenüber 4, zur Anzeige gebracht,  weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_58`)


Verfahren 2) GZ. MA67/Zahl2/2023:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ2) am 13.  März 2023 um 12:01 Uhr in 1010 Wien, Universitätsring vor Baum 2156, zur Anzeige gebracht,  weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_70`)


Verfahren 3) GZ. MA67/Zahl3/2023:   Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ3) am 20.  Februar 2023 um 15:23 Uhr in 1010 Wien, Universitätsring vor Park, zur Anzeige gebracht, weil  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_5`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen Kennz1 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 23.  Jänner 2025 um 19:50 Uhr in 1140 Wien, Stockhammerngasse gegenüber 19 beanstandet, da  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Federal Ministry Finance` 

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `36de29f8`  
**Description:**
Matches 'Bundesministerium für Finanzen'.

**Content:**
```
\bBundesministerium\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.005 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 5030 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_114`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_37`)


Am 20.08.2020 wurde die im Bundesministerium für Finanzen für die automationsunterstützte  Datenverarbeitung zuständige Sektion I aufgefordert, Fragen im Zusammenhang mit den  konkreten Bescheiderstellungen zu beantworten, sowie diesbezügliche Beweismittel  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_69`)


Dass die Einbringung  per Telefax erfolgte schadet aufgrund der Verordnung des Bundesministers für Finanzen über  die Zulassung von Telekopierern zur Einreichung von Anbringen an das Bundesministerium für  Finanzen, an die Verwaltungsgerichte sowie an die Finanzämter und Zollämter (BGBl. II  2013/447) nicht.

| Predicted | Gold |
|---|---|
| `Bundesministerium für  Finanzen` | `Bundesministerium für  Finanzen` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_45`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung  gestellte Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_85`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/145852.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145852.1_79`)


Das Bundesministerium für Finanzen ist ermächtigt, von der  Anwendung dieser Bestimmung bei Personen abzusehen, deren Aufenthalt im Inland nicht mehr  als ein Jahr beträgt, wenn diese im Inland weder ein Gewerbe betreiben noch einen anderen  Beruf ausüben.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_321`)


Die Absätze 1 bis 6 des § 3 der Verordnung des Bundesministers für Finanzen über die Kriterien  zur Ermittlung des Pendlerpauschales und des Pendlereuros, zur Einrichtung eines  Pendlerrechners und zum Vorliegen eines Familienwohnsitzes (Pendlerverordnung), BGBl. II  Nr. 276/2013 in der Fassung BGBl. II Nr. 154/2014 und Nr. 324/2019, bestimmen:  „(1) Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  21 von 28 Seite 22 von 28

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_25`)


Die belangte  Behörde bestätigte, dass es einen Button für Vorlageanträge gibt, dieser aber vom Bf nicht  gedrückt wurde, weil er den Einzeiler unter dem Button „Beschwerde“ nochmals eingegeben  hatte, führte aber auch aus, dass die belangte Behörde auf den FinanzOnline Verlauf im Detail  nicht zugreifen könne und bot an, zu diesem Zweck, mit dem Bundesministerium für Finanzen  diesbezüglich Kontakt aufzunehmen, um die Daten aus FinanzOnline für den gegenständlichen  Akt auswerten zu lassen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_28`)


Die belangte Behörde hätte nach  Auswertung durch das Bundesministerium für Finanzen festgestellt, dass die Beschwerde vom  27. Jänner 2024 sich gegen den Zurückweisungsbescheid vom 25. Jänner 2024 gerichtet hätte  und somit nicht als Vorlageantrag zu werten sei.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_273`)


Auch das Bundesministerium für Finanzen ging ursprünglich davon aus, dass die angeführte  Bestimmung des Einkommensteuergesetzes sich ausschließlich auf inländische Privatstiftungen  bezog.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/147744.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147744.1_50`)


2. in Widerspruch zu nicht offensichtlich unrichtigen Rechtsauslegungen steht, die  a) dem Abgabepflichtigen gegenüber von der für ihn zuständigen Abgabenbehörde erster  Instanz geäußert oder  b) vom Bundesministerium für Finanzen im Amtsblatt der österreichischen Finanzverwaltung  veröffentlicht wurden, wenn im Vertrauen auf die betreffende Äußerung bzw. Veröffentlichung  für die Verwirklichung des die Abgabepflicht auslösenden Sachverhaltes bedeutsame  Maßnahmen gesetzt wurden.“

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_86`)


Nach § 48 BAO idF vor BGBl. I Nr. 62/2019 kann das Bundesministerium für Finanzen bei  Abgabepflichtigen, die der Abgabenhoheit mehrerer Staaten unterliegen, soweit dies zur  Ausgleichung der in- und ausländischen Besteuerung oder zur Erzielung einer den Grundsätzen  der Gegenseitigkeit entsprechenden Behandlung erforderlich ist, anordnen, bestimmte  Gegenstände der Abgabenerhebung ganz oder teilweise aus der Abgabepflicht auszuscheiden  oder ausländische, auf solche Gegenstände entfallende Abgaben ganz oder teilweise auf die  inländischen Abgaben anzurechnen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_140`)


Gem § 48 BAO kann das Bundesministerium für Finanzen (nach  der VwGH-Judikatur richtig: der Bundesminister für Finanzen, vgl. zB VwGH vom 21.7.1993,  91/13/0119) anordnen, bei Abgabepflichtigen, die der Abgabenhoheit mehrerer Staaten  unterliegen, bestimmte Gegenstände aus der Abgabenerhebung ganz oder teilweise  auszuscheiden oder ausländische, auf solche Gegenstände entfallende Abgaben ganz oder  teilweise auf die inländischen Abgaben anzurechnen, soweit dies zur Ausgleichung der in- und  ausländischen Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit  entsprechenden Behandlung erforderlich ist.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

## `EU Court of Justice` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `23905f82`  
**Description:**
Matches 'Gerichtshof der Europäischen Union'.

**Content:**
```
\bGerichtshof\s+der\s+Europ\u00e4ischen\s+Union\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 5020 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker` (person)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_38`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  "- die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der Verordnung  (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004 zur  Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7 Abs.  2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5. April  2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat."

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_11`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  Der Gerichtshof der Europäischen Union (EuGH) hat mit Urteil vom 16. Juni 2022 in der  Rechtssache C-328/20 über eine Vertragsverletzungsklage der Europäischen Kommission nach  Art. 258 AEUV gegen die Republik Österreich in Ziffer 2 seines Urteilstenores bezughabend  ausgesprochen: „Die Republik Österreich hat durch die … Einführung eines  Anpassungsmechanismus in Bezug auf den Familienbonus Plus, … und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_17`)


Auch der Verstoß u.a. gegen Verordnungen der EU ist  eine Vertragsverletzung (vgl. aaO, § 258 Rn. 4 f.).   Art. 260 Abs. 1 AEUV bestimmt: „Stellt der Gerichtshof der Europäischen Union fest,  dass ein Mitgliedstaat gegen eine Verpflichtung aus den Verträgen verstoßen hat, so  hat dieser Staat die Maßnahmen zu ergreifen, die sich aus dem Urteil des Gerichtshofs  ergeben.“

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_55`)


Der Gerichtshof der Europäischen Union hat am 16. Juni 2022 betreffend Indexierung der  Familienbeihilfe sowie bestimmter familienbezogener Steuerbegünstigungen auf Grund einer  Klage der Europäischen Kommission entschieden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_61`)


Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung ist auch im gegenständlichen Beschwerdeverfahren vor dem Bundesfinanzgericht zu  beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_120`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_57`)


Der Gerichtshof der Europäischen Union hat am 16. Juni 2022 betreffend Indexierung der  Familienbeihilfe sowie bestimmter familienbezogener Steuerbegünstigungen auf Grund einer  Klage der Europäischen Kommission entschieden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_63`)


Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung ist auch im gegenständlichen Beschwerdeverfahren vor dem Bundesfinanzgericht zu  beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_122`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_22`)


4. 2020, RE/7100001/2020,  ecli:at:bfg:2020:re.7100001.2020, dem Gerichtshof der Europäischen Union gemäß Artikel 267  AEUV folgende Frage zur Vorabentscheidung vor:  "Sind Artikel 18 und Artikel 45 Absatz 1 des Vertrags über die Arbeitsweise der Europäischen  Union, Artikel 7 Absätze 1 und 2 der Verordnung (EG) Nr. 492/2011 des Europäischen  Parlaments und des Rates vom 5. April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb  der Union, Artikel 4, Artikel 5 Buchstabe b, Artikel 7 und Artikel 67 der Verordnung (EG) Nr.  883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004 zur Koordinierung  der Systeme der sozialen Sicherheit sowie Artikel 60 Absatz 1 Satz 2 der Verordnung (EG) Nr.  987/2009 des Europäischen Parlaments und des Rates vom 16. September 2009 zur Festlegung  der Modalitäten für die Durchführung der Verordnung (EG) Nr. 883/2004 über die  Koordinierung der Systeme der sozialen Sicherheit dahin auszulegen, dass sie der Anwendung  einer nationalen Regelung entgegenstehen, die vorsieht, dass Familienleistungen für ein Kind,  das sich nicht tatsächlich ständig in dem diese Familienleistungen zahlenden Mitgliedstaat,  sondern tatsächlich in einem anderen Mitgliedstaat der Europäischen Union, einer anderen  Vertragspartei des Abkommens über den Europäischen Wirtschaftsraum oder der Schweiz  aufhält, auf Basis der vom Statistischen Amt der Europäische Union veröffentlichten  vergleichenden Preisniveaus für den jeweiligen Staat im Verhältnis zu dem die  Familienleistungen zahlenden Mitgliedstaat anzupassen sind?"

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen  Union` (organisation)
- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_33`)


Vertragsverletzungsverfahren  Klage der Europäischen Kommission vom 22. Juli 2020  Nach Stellung des Vorabentscheidungsersuchens des Bundesfinanzgerichts reichte die  Europäische Kommission mit Beschluss vom 14. Mai 2020 im Verfahren INFR(2018)2372 am  22. Juli 2020 Klage gegen die Republik Österreich beim Gerichtshof der Europäischen Union  ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_43`)


6. 2022, C-328/20  Der Gerichtshof der Europäischen Union entschied mit Urteil EuGH 16.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_52`)


4. 2020, RE/7100001/2020 an den Gerichtshof der Europäischen Union  gemäß Art. 267 AEUV gestellte Ersuchen um Vorabentscheidung, ob die Indexierung von  Familienleistungen durch den österreichischen Gesetzgeber nach der Kaufkraft in den  einzelnen Mitgliedsstaaten bzw. Vertragsstaaten unionsrechtskonform ist, protokolliert zu C- 163/20, gemäß Artikel 100 Abs. 1 Verfahrensordnung des Gerichtshofs der Europäischen Union  und § 290 Abs. 3 BAO zurückgenommen.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_53`)


Mit dem Urteil EuGH 16. 6. 2022, C-328/20, ECLI:EU:C:2022:468, veröffentlicht auf der Website  des Gerichtshofs am selben Tag, habe der Gerichtshof der Europäischen Union im  Vertragsverletzungsverfahren gemäß Art. 258 AEUV auch die Auslegung der Verträge im Sinne  von Art. 267 AEUV klargestellt.  Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung sei auch im Beschwerdeverfahren vor dem Bundesfinanzgericht zu  RV/7101361/2020 zu beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_65`)


Entscheidung des EuGH  Der Gerichtshof der Europäischen Union wurde mit der Sache vom Bundesfinanzgericht mittels  des Vorabentscheidungsverfahrens gemäß Beschluss BFG 16.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_146`)


...  Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung ist auch im Beschwerdeverfahren vor dem Bundesfinanzgericht zu  RV/7102978/2021 zu beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_208`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_33`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der  Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004  zur Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7  Abs. 2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5.  April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_32`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der  Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004  zur Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7  Abs. 2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5.  April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139968.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139968.1_36`)


Die Europäische Kommission brachte beim Gerichtshof der Europäischen Union (EuGH) eine  Vertragsverletzungsklage gegen die Republik Österreich ein und beantragte, festzustellen, dass  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf die  Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in einem  anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 4, 7 und 67 der  Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004  zur Koordinierung der Systeme der sozialen Sicherheit (ABl. 2004, L 166, S. 1) sowie aus Art. 7  Abs. 2 der Verordnung (EU) Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5.  April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb der Union (ABl. 2011, L 141, S. 1)  verstoßen hat und  - die Republik Österreich durch die Einführung eines Anpassungsmechanismus in Bezug auf den  Familienbonus Plus, den Alleinverdienerabsetzbetrag, den Alleinerzieherabsetzbetrag und den  Unterhaltsabsetzbetrag für Wanderarbeitnehmer, deren Kinder ständig in einem anderen  Mitgliedstaat wohnen, gegen ihre Verpflichtungen aus Art. 7 Abs. 2 der Verordnung Nr.  492/2011 verstoßen hat.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Hon.-Prof.in Alice Siemglüß  in der Beschwerdesache   Wendy Schuch, Sörg 19, 5441 Erlfeld, Österreich,   betreffend Beschwerde vom 29. August 2024 gegen den Bescheid des Finanzamtes Österreich  vom 1. August 2024 betreffend Umsatzsteuer 2023 beschlossen:    I. Dem Gerichtshof der Europäischen Union werden gemäß Artikel 267 AEUV die Fragen  zur Vorabentscheidung vorgelegt, die die Auslegung der Richtlinie 2006/112/EG des  Rates vom 28. November 2006 über das gemeinsame Mehrwertsteuersystem (in der  Folge MwSt-Richtlinie) und der Achten Richtlinie 79/1072/EWG des Rates vom  6. Dezember 1979 betreffen:   1. Ist die Bekanntgabe einer MwSt-Identifikationsnummer eines anderen  Mitgliedstaates als des Mitgliedstaates, in dem die Versendung oder  Beförderung eines Gegenstandes beginnt, gemäß Art 138 Abs. 1 Buchst.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß` (person)
- `Wendy Schuch` (person)
- `Sörg 19, 5441 Erlfeld, Österreich` (address)

</details>

---

## `Mag. Ghesla Steuerberater GmbH` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `79d77a2c`  
**Description:**
Matches 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 5041 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Richard Reithmayer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  HR Manuela Buskotte, Schulboden 10, 8742 Kienberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2017 und 2018, 18-878/6086, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `HR Manuela Buskotte` (person)
- `Schulboden 10, 8742 Kienberg, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `18-878/6086` (tax_number)

</details>

---

## `Federal Ministry Finance Genitive` 🏆

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `a0f12804`  
**Description:**
Matches 'Bundesministeriums für Finanzen' (genitive) and 'Bundesministerium für Finanzen'.

**Content:**
```
\bBundesministerium(?:s)?\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 5024 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_245`)


Auf die Zulässigkeit eines täglichen Beginns der Nummerierung gemäß einem Erlass des  Bundesministeriums für Finanzen vom 1.04.2003 (AÖF 2003/65) wurde verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_86`)


Dass die angefochtenen Erledigungen  von der belangten Behörde (und nicht vom die Außenprüfung durchführenden Finanzamt  Graz-Stadt) genehmigt und folglich auch erlassen wurden (siehe dazu die Ausführungen unter  Punkt IV.3.), resultiert aus den Ausführungen des Bundesministeriums für Finanzen, Sektion I,  vom 22.09.2020 in Verbindung mit den Angaben der belangten Behörde im Schriftsatz vom  selben Tag: Demnach wurden die verfahrensgegenständlichen Erledigungen durch einen  Mitarbeiter der belangten Behörde, nämlich Name, freigegeben, sohin von diesem approbiert.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt  Graz-Stadt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_142`)


Den weiteren Ausführungen zur Unzuständigkeit im Zusammenhang mit dem Befüllen der  Eingabebögen durch den Prüfer des Finanzamtes Graz-Stadt ist der unzweifelhafte Inhalt der  Ausführungen des Bundesministeriums für Finanzen, Sektion I und der belangten Behörde,  10 von 15 Seite 11 von 15

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamtes Graz-Stadt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Mag. Dieter Fröhlich` (person)
- `Charlotte Hasslbauer` (person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich` (address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich` (address)
- `Procurator Treuhand- und Revisionsges.m.b.H.` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_12`)


Nach einer Auskunft des Bundesministeriums für Finanzen würde mit der elektronischen  Zustellung solange zugewartet, bis der Teilnehmer vom Wirksamwerden der Verpflichtung  entsprechend verständigt worden sei.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_15`)


Die spruchgegenständlichen mit 26. Juli 2019 datierten Bescheide wurden am 27. Juli 2019 um  5:10 Uhr gemeinsam mit einem Bericht über die Außenprüfung elektronisch in die Databox der  Beschwerdeführerin zugestellt.  Dies wurde einerseits durch die zuständige Stelle des Bundesministeriums für Finanzen  gegenüber dem Finanzamt bestätigt und ergibt sich anderseits auch aus dem Umstand, dass  die Zustellung in die Databox (Vorhaltswirkung der Beschwerdevorentscheidung) im  Vorlageantrag nicht nur nicht bestritten wurde, sondern in dessen Punkt 6 sogar ausdrücklich  zugestanden wird, dass es möglich sei, dass die Abgabenbescheide vom 26. Juli 2029 (richtig  2019) elektronisch in die Databox zugestellt worden sind und der Status in der Databox noch  immer "ungelesen" wäre.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_37`)


Mit dem Hinweis auf eine Auskunft des Bundesministeriums für Finanzen, dass mit einer  elektronischen Zustellung solange zugewartet werde, bis der jeweilige Teilnehmer vom  Wirksamwerden der Verpflichtung entsprechend verständigt worden sei, ist für die  Beschwerdeführerin ebenso nichts gewonnen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_38`)


Nicht nur, dass nicht näher konkretisierte  „Auskünfte“ des Bundesministeriums für Finanzen keinerlei verbindliche Wirkung entfalten  könnten, bezog sich diese Auskunft offenbar auf die hier noch nicht zur Anwendung  gelangende verpflichtende Teilnahme an der elektronischen Zustellung (ab 2020) und die  damit verbundene Abschaffung der Möglichkeit auf die elektronische Zustellung in  FinanzOnline verzichten zu können (§ 5b Abs 3 FOnV 2006 idF BGBl II 122/2020).

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_48`)


Festzuhalten ist, dass für politische Funktionäre hinsichtlich der Werbungskosten in den  Randzahlen (Rz) 383a ff der Lohnsteuerrichtlinien2002 (LStR) des Bundesministeriums für  Finanzen (BMF) besondere Bestimmungen festgelegt sind.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für  Finanzen` | `Bundesministeriums für  Finanzen` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_53`)


Während  des Streitjahres hatte der BF einen Wohnsitz und den Mittelpunkt seiner Lebensinteressen in  Schweden in s (Bestätigung der Swedish Tax Agency Östersund vom 19.11.2013 am  Rückzahlungsantrag: Formular ZS-RE1 des Bundesministeriums für Finanzen).

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_84`)


Es kann dahingestellt bleiben, ob der Erlass des Bundesministeriums für Finanzen vom 12. Juni  2016, BMF-010221/0362-IV/8/2014, von der Finanzverwaltung im vorliegenden Streitfall  anzuwenden war oder nicht.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_85`)


Dieser Erlass stellt mangels Kundmachung im Bundesgesetzblatt  lediglich einen Auslegungsbehelf dar, der im Interesse einer einheitlichen Vorgangsweise die  Rechtsansicht des Bundesministeriums für Finanzen zu den Änderungen bei der steuerlichen  Behandlung grenzüberschreitender Arbeitskräftegestellung im Hinblick auf die oben dargelegte  Rechtsprechung des Verwaltungsgerichtshofes wiedergibt.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_72`)


Daran vermag auch der wiederholte Hinweis des Beschwerdeführers,  verschiedene Erlässe würden das Finanzamt „verpflichten“, eine Wiederaufnahme von Amts  wegen auch zugunsten des Abgabepflichtigen zu verfügen, nichts zu ändern: Erlässe der  Finanzverwaltung begründen keine subjektiven Rechte und Pflichten der Steuerpflichtigen,  sondern stellen lediglich die Rechtsauffassung des Bundesministeriums für Finanzen dar.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/142566.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142566.1_56`)


Dementsprechend kann die beantragte Zeugeneinvernahme eines näher genannten  Mitarbeiters des Bundesministeriums für Finanzen entfallen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_35`)


Von der Abgabenbehörde wurden weder ein Pauschbetrag nach § 34 Abs. 8 EStG noch  tatsächliche Kosten (Schulgeld bzw. Heimkosten) als außergewöhnliche Belastungen für die  Ausbildung der Töchter berücksichtigt, mit der Begründung, dass die Ausbildungsstätten im  Einzugsbereich des Wohnortes liegen würden und auch die Voraussetzung des § 2 Abs. 3 der  Verordnung des Bundesministeriums für Finanzen zur Berufsausbildung eines Kindes außerhalb  des Wohnortes, BGBl. Nr. 624/1995 idgF, nicht erfüllt seien.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_38`)


Diese Ansicht wird noch verstärkt durch die technischen IT-Auswertungen des  Bundesministeriums für Finanzen, die die belangte Behörde übermittelt hat und die besagen,  dass via Finanzonline mit 27. Jänner 2024 zwar eine Beschwerde eingebracht wurde, diese  jedoch überhaupt nur gegen den 2. gegenständlichen Bescheid vom 25. Jänner 2024 – die  Beschwerdevorentscheidung – technisch eingebracht werden konnte, weil es technisch  anscheinend nicht möglich ist, zweimal eine Beschwerde gegen denselben Erstbescheid  einzubringen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_268`)


Die Stiftungsrichtlinien 2001, welche zum Zeitpunkt der Abgabe der  Einkommensteuererklärung 2007 die Rechtsansicht des Bundesministeriums für Finanzen  darstellten zitieren mehrfach aus den Bestimmungen des PSG.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_279`)


Die ausdrückliche Einbeziehung von ausländischen Stiftungen oder sonstigen  Vermögensmassen, die mit einer Privatstiftung vergleichbar sind, in § 27 Abs. 1 Z 7 mit dem  Schenkungsmeldegesetz kann im Hinblick auf die Begründung der Regierungsvorlage nur so  verstanden werden, dass nach Ansicht des Bundesministeriums für Finanzen und dem folgend  des Gesetzgebers Zuwendungen von ausländischen Privatstiftungen zum Zeitpunkt der hier  strittigen Zuwendung im Jahr 2007, also vor Inkrafttreten des Schenkungsmeldegesetzes 2008,  BGBl. I Nr. 85/2008, nicht als steuerpflichtig nach § 27 Abs. 1 Z 7 EStG 1988 anzusehen waren.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_454`)


Das Finanzamt konnte der Bf. keinen (bedingten) Vorsatz der Hinterziehung der auf die  Stiftungszuwendung entfallenden Einkommensteuer nachweisen, weil die Bf. und ihr  steuerlicher Vertreter in diesem Zusammenhang - wie bereits in der Beweiswürdigung näher  begründet wurde - in Übereinstimmung mit der damaligen Rechtsansicht des  Bundesministeriums für Finanzen davon ausging, dass Zuwendungen ausländischer Stiftungen  nicht unter § 27 Abs. 1 Z 7 EStG 1988 fallen.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

## `City Magistrate` 

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `d5dd2ece`  
**Description:**
Matches Magistrates of Vienna including department numbers, handling typos like 'Magistratssabteilung' and stopping before verbs or prepositions.

**Content:**
```
\b(Magistrat(?:es)?(?:\s+der\s+Stadt\s+Wien)(?:\s*,\s*(?:Magistratsabteilung|Magistratssabteilung|MA)\s+\d+)?)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 14 | 14 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 0 | 5029 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_3`)


Nr. 10/2013 über die Beschwerden des Beschuldigten vom 10. Juni  2019 gegen  1. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 13. März 2019,  Zahl MA-ZAHL1 sowie  2. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 14. Mai 2019,  Zahl MA-ZAHL2  zu Recht erkannt:  I. Gemäß § 50 in Verbindung mit § 38 VwGVG und § 45 Abs. 1 zweiter Satz VStG wird von der  Verhängung einer Strafe abgesehen und der beschwerdeführenden Partei unter Hinweis auf  die Rechtswidrigkeit ihres Verhaltens eine Ermahnung erteilt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die der  Beschwerdeführer keinen Beitrag zu den Kosten des verwaltungsgerichtlichen Strafverfahrens  zu tragen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_133`)


in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_358`)


Der Beschwerdeführer stellt daher den  A N T R A G,  1. in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_81`)


Über die Beschwerde wurde erwogen:  Sachverhalt und Beweiswürdigung:  Über die Bf. wurde mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67  vom 2.4.2019 zur GZ. MA-Zahl1 wegen des unter dem Punkt "Verfahrensgang" angeführten  Deliktes eine Geldstrafe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe in Höhe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien, Magistratsabteilung 67` | `Magistrates  der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Gertraud Hausherr` (person)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Timon Thoennißen` (person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)


über die Beschwerde der Balthasar Brendtke, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Balthasar Brendtke` (person)
- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Roland Rößle, Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich, über die Beschwerde des  Beschuldigten vom 7. April 2022 gegen den Zurückweisungsbescheid des Magistrates der Stadt  Wien vom 5. April 2022, Zahl: MA67/216700658355/2021, mit dem der Einspruch vom 18.  Februar 2022 gegen die Strafverfügung vom 3. September 2021 mit derselben Geschäftszahl  gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien` | `Magistrates der Stadt  Wien` |

**Missed by this rule (FN):**

- `Dr. Sebastian Pfeiffer LL.M.` (person)
- `Roland Rößle` (person)
- `Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_28`)


Im gegenständlichen Verfahren wird Ihnen nicht die Abstellung des Fahrzeuges an sich  vorgeworfen, sondern der Umstand, dass einem Auskunftsbegehren des Magistrates der Stadt  Wien innerhalb der gesetzlichen Frist von zwei Wochen nicht entsprochen wurde.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien` | `Magistrates der Stadt  Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien` | `Magistrates der  Stadt Wien` |

**Missed by this rule (FN):**

- `Dr. Sebastian Pfeiffer LL.M.` (person)
- `Annette Preußing` (person)
- `Am Neufeldersee 40, 3385 Uttendorf, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Wladimir Ferrarese  über die Beschwerde des Hademar Mühlenstedt,  Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich, vom 22. Juni 2025, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 20. Juni 2025, GZ. MA67/GZ1/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und dem Beschwerdeführer unter Hinweis  auf die Rechtswidrigkeit seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Mag. Wladimir Ferrarese` (person)
- `Hademar Mühlenstedt` (person)
- `Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/149274.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149274.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Moses Schelhase, Ritzendorf 15, 9064 Reigersdorf, Österreich, wegen der Verwaltungsübertretung  nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,  idF ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde der  Beschuldigten vom 31. Juli 2025 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 3. Juli 2025, Zahl: MA67/MA-GZ/2025 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Karoline Windsteig` (person)
- `Moses Schelhase` (person)
- `Ritzendorf 15, 9064 Reigersdorf, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149672.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149672.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Verwaltungsstrafsache  gegen Oswald Küstler, Doppel Straße 1543, 8421 Zehensdorf, Österreich, wegen der Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom  20. August 2025 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 7. August 2025, Zahl: MA67/MA-GZ/2025, in der mündlichen  Verhandlung am 24. Oktober 2025, im Beisein der Schriftführerin Nicole Schmid, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2. VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien,  Magistratsabteilung 67` | `Magistrates der Stadt Wien,  Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Oswald Küstler` (person)
- `Doppel Straße 1543, 8421 Zehensdorf, Österreich` (address)

</details>

---

## `Wiener Linien` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `774f8d17`  
**Description:**
Matches 'Wiener Linien' as a specific transport organization.

**Content:**
```
\bWiener\s+Linien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 5041 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/146445.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146445.1_162`)


2016 – Tickets für die Reise nach Österreich     Euro 1.630,00  12.12.2016 – Jahreskarte Wiener Linien      Euro 224,00  ASVG-Versicherung für Dezember 2016 und Jänner 2017    Euro 154,70  Insgesamt          Euro 7.153,13  März und April 2016   – Aufwendungen der Bf. im Zusammenhang mit Begräbnis des Vaters in China Euro 868,00  Außergewöhnliche Belastung lt. Erklärung beantragt – gesamt   Euro 8.021,13  Im Vorlageantrag wurde der Betrag um die im Dezember in Österreich geleisteten Zahlungen  iHv Euro 978,70 verringert und eine Anerkennung iHv    gesamt Euro 7.042,43  beantragt.

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/146445.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146445.1_182`)


Auch die Kosten der Reise nach Österreich, die Zahlungen für  eine „Visitor Insurance“ und eine ASVG-Versicherung der Mutter sowie eine Jahreskarte für die  Wiener Linien stellten mangels Vorliegen der gesetzlichen Voraussetzungen keine  außergewöhnliche Belastung dar.

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |

</details>

---

## `Magistrats der Stadt Wien` 

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `8c212b8d`  
**Description:**
Matches 'Magistrats der Stadt Wien' (genitive) and 'Magistrat der Stadt Wien' (nominative) with optional department info.

**Content:**
```
(?:^|\s|\b)(Magistrat(?:s)?(?:\s+der\s+Stadt\s+Wien)(?:\s*,\s*(?:Magistratsabteilung|Magistratssabteilung|MA)\s+\d+)?)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.005 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 5030 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt somit  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_51`)


Informativ wird mitgeteilt, dass die Einzahlung der verhängten Geldstrafe sowie die Kosten des  Verfahrens von der belangten Behörde auf folgendes Bankkonto des Magistrats der Stadt Wien  bei der UniCredit Bank Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 – Strafen;

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_103`)


Informativ wird mitgeteilt, dass die Einzahlung der Geldstrafe (€ 60,00) samt Kosten des  verwaltungsbehördlichen Verfahrens (€ 10,00) und des Beschwerdeverfahrens (€ 12,00) von  gesamt € 82,00 auf folgendes Bankkonto des Magistrats der Stadt Wien bei der UniCredit Bank  Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 - Verkehrsstrafen  IBAN: AT***, BIC: ***  Bitte die Geschäftszahl des Straferkenntnisses des Magistrats angeben: Zahl  Gemäß § 52 Abs. 6 VwGVG sind die §§ 14 und 54b Abs. 1 und 1a VStG sinngemäß anzuwenden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank  Austria AG` (organisation)
- `Magistrats` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  somit 82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_3`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lukas Escherle  in der Verwaltungsstrafsache gegen  Kirsten Schneppensiefen, Poppenreithstraße 26, 7461 Goberling, Österreich, vertreten durch Albert Höferlin  wegen der  Verwaltungsübertretung gemäß § 16 Abs 1 des Gebrauchsabgabegesetz, über die Beschwerde  der Beschuldigten vom 31.7.2023 gegen das Straferkenntnis des Magistrats der Stadt Wien  vom 14.7.2023 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe auf je € 20,00 (also EUR 100,00) herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Priv.-Doz. Lukas Escherle` (person)
- `Kirsten Schneppensiefen` (person)
- `Poppenreithstraße 26, 7461 Goberling, Österreich` (address)
- `Albert Höferlin` (person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/147867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147867.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

</details>

---

## `Landespolizeidirektion Generic` 🏆

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `c2bd9211`  
**Description:**
Matches 'Landespolizeidirektion' followed by any location or placeholder (e.g., X), stopping before verbs or punctuation.

**Content:**
```
\bLandespolizeidirektion\s+(?:Wien|Vorarlberg|Salzburg|Tirol|Steiermark|Kärnten|Oberösterreich|Niederösterreich|Burgenland|X|\d+)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.010 | 26 | 26 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 0 | 5017 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_8`)


- Einstellungsschein der Landespolizeidirektion Niederösterreich vom 28. März 2019 betreffend  den Sohn der Bf.: „Aufgrund Ihres Ansuchens um Aufnahme in die Bundespolizei werden Sie  mit Wirkung vom 13. Mai 2019 in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich eingestellt.   1 von 17 Seite 2 von 17

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Niederösterreich` | `Landespolizeidirektion Niederösterreich` |

**Missed by this rule (FN):**

- `Landespolizeidirektion  Niederösterreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_65`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der im Dezember 1998 geborene Sohn der Bf. ist bei seiner Mutter, der Bf., haushaltszugehörig  und begann – nach Beendigung des Zivildienstes mit 31. März 2019 – am 13. Mai 2019 die  Polizeigrundausbildung bei der Landespolizeidirektion Niederösterreich im Bildungszentrum  der Sicherheitsakademie Y. auf Grund eines mit Sondervertrag gemäß § 36 VBG 1948 für die  exekutivdienstliche Ausbildung begründeten privatrechtlichen Dienstverhältnisses zum Bund  (§ 1 Abs. 1 VBG).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Niederösterreich` | `Landespolizeidirektion Niederösterreich` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_29`)


Der Beschwerde war - wie erwähnt - eine Kopie des von der Landespolizeidirektion Wien mit  der Bf. am 1. September 2018 gemäß § 36 VBG 1948 abgeschlossenen Sondervertrages für die  exekutivdienstliche Ausbildung beigelegt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_63`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die im Jänner 1999 geborene Bf. begann am 1. September 2018 die Polizeigrundausbildung bei  der Landespolizeidirektion Wien im Bildungszentrum T. auf Grund eines mit Sondervertrag  gemäß § 36 VBG 1948 für die exekutivdienstliche Ausbildung begründeten privatrechtlichen  Dienstverhältnisses zum Bund (§ 1 Abs. 1 VBG).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31. Juli 2020 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 2. Juni 2020 in der  gebührenpflichtigen Kurzparkzone in 1030 Wien, Grailichgasse 3, ohne einem für den  Beanstandungszeitpunkt 17:47 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_11`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, sowie in die von diesem angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 15. Oktober  1 von 9 Seite 2 von 9

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_7`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien mit der  Dienstnummer DNr am 14. Mai 2021 um 10:55 Uhr in 1050 Wien, Reinprechtsdorfer Straße 1c  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_8`)


Landespolizeidirektion Wien mit Strafverfügung vom 16. September 2021 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 19. Juli 2021 um  14:31 Uhr ohne einem für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_13`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:   „Aus der dem Verfahren zugrundeliegenden Beanstandung, welche von einem Organ der  Landespolizeidirektion Wien mittels Organstrafverfügung vorgenommen wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug im Bereich der gebührenpflichtigen  Kurzparkzone abgestellt war, ohne dass die Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_34`)


Es bestehe für die erkennende Behörde keinerlei Veranlassung, die schlüssigen und wider- spruchsfreien Angaben des meldungslegenden Organs der Landespolizeidirektion Wien in  Zweifel zu ziehen, zumal einem derartigen Organ die Wahrnehmung und richtige Wiedergabe  maßgeblicher Sachverhalte, insbesondere bezüglich eines im ruhenden Verkehr befindlichen  Kraftfahrzeuges, wohl zugemutet werden könne.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_35`)


Es bestehe kein Grund, an der Objektivität  des meldungslegenden Organs der Landespolizeidirektion Wien zu zweifeln und ergebe sich  kein Anhaltspunkt, dass dieses eine ihm unbekannte Person wahrheitswidrig belasten habe  wollen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_8`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans Nr der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 30. Dezember 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 2. November 2022  um 09:18 Uhr in der der gebührenpflichtigen Kurzparkzone in 1070 Wien, Bernardgasse 42,  abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141222.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141222.1_9`)


Entscheidungsgründe  Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangter Behörde mit Bericht  vom 26. Mai 2023 dem Bundesfinanzgericht als zuständigem Verwaltungsgericht vorgelegten  Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Nummer ANr stellte  am 19. Jänner 2023 um 12:52 Uhr fest, dass das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1100 Wien,  Liesingbachstraße 73 gegenüber, abgestellt gewesen sei, ohne dass für seine Kennzeichnung  mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_4`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug Type mit dem behördlichen Kennzeichen 123 (A) wurde am 28.  Februar 2023 um 12:49 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien,  Liebenberggasse 6, vom Kontrollorgan der Parkraumüberwachung Nr der  Landespolizeidirektion Wien zur Anzeige gebracht, da es sich nach dessen eigenen  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_8`)


Landespolizeidirektion Wien mit Strafverfügung vom 7. September 2022 an , er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 11. Juli 2022 in einer  gebührenpflichtigen Kurzparkzone in 1210 Wien, Prager Straße 65 u. 67, ohne einen für den  Beanstandungszeitpunkt 11:21 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 12. Juni 2023 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 11. April 2023 in der  gebührenpflichtigen Kurzparkzone in 1130 Wien, Hietzinger Hauptstraße 50, ohne einen für  den Beanstandungszeitpunkt 09:31 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  nach einer bei der Zulassungsbesitzerin,MittelBruckuniuniEvent GmbH  eingeholten Lenkerauskunft und unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 12. April 2023 an , er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 13. Februar 2023 in  der gebührenpflichtigen Kurzparkzone in Gasse, abgestellt, ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt 12:04 Uhr gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `MittelBruckuniuniEvent GmbH` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_38`)


Begründend stellte die Behörde fest, dass aus der dem Verfahren zugrundeliegenden  Beanstandung, welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion  Wien mittels Organstrafverfügung vorgenommen worden sei, und dem Ermittlungsverfahren  hervorgehe, dass das Fahrzeug in einer gebührenpflichtigen Kurzparkzone gestanden sei, ohne  dass die Parkometerabgabe entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_13`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt, das Fahrzeug sei von einem  Organ der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung  beanstandet worden, weil es im Bereich einer gebührenpflichtigen Kurzparkzone ohne gültigen  Parkschein abgestellt gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_25`)


Begründend führte die Behörde aus, dass aus der dem Verfahren zugrundeliegenden Anzeige,  welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund  einer eigenen dienstlichen Wahrnehmung erstattet worden sei, hervorgehe, dass das vom Bf.  2 von 10 Seite 3 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/143412.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143412.1_8`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa. ZL, wurde vom Parkraumüberwachungsorgan KO der Landespolizeidirektion Wien am 11.  Mai 2023 um 17:28 Uhr in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Stumpergasse  24, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_4`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 6. April 2023  um 16:33 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Josef-Meinrad-Platz, bei  Tankstelle rechts beanstandet, da es ohne einen für den Beanstandungszeitpunkt gültigen  Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer unter  Zugrundelegung der Anzeigedaten des Kontrollorgans DNr der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 14. März 2024 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 16. Jänner 2024 um  08:59 Uhr in der gebührenpflichtigen Kurzparkzone in 1180 Wien, Währinger Straße gegenüber  81-83, abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben, da der Parkschein nicht entwertet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/149274.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149274.1_12`)


Das Straferkenntnis wurde wie folgt begründet:  „Aus der dem Verfahren zugrundeliegenden Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung erstattet wurde, geht hervor, dass das gegenständliche  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit und zur angeführten Zeit  in einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die Parkometerabgabe  entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/149672.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149672.1_23`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, in die von diesem angefertigten Foto.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Specific Company Names` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `df1af49a`  
**Description:**
Matches specific known company names from training data that were missed, including 'Combach Textil GmbH', 'Sacha Katzensteiner Blauensteiner Rechtsanwälte GmbH', 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG', 'Fa.Klahsen & Schehr Marine GmbH', 'Trasteinbruck Landwirtschaft GmbH', and 'Enns Talbachuni Planung'.

**Content:**
```
\b(?:Combach\s+Textil\s+GmbH|Sacha\s+Katzensteiner\s+Blauensteiner\s+Rechtsanw\u00e4lte\s+GmbH|Hallas\s+&\s+Partner\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\.?\s+KG|Fa\.Klahsen\s+&\s+Schehr\s+Marine\s+GmbH|Trasteinbruck\s+Landwirtschaft\s+GmbH|Enns\s+Talbachuni\s+Planung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 5042 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` | `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Alois Kleynsteuber` (person)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich` (address)
- `FA Wien 9/18/19  Klosterneuburg` (organisation)
- `79-708/0061` (tax_number)

</details>

---

## `Finanzamt für Gebühren` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `3e5b6851`  
**Description:**
Matches 'Finanzamt für Gebühren' specifically.

**Content:**
```
(?:^|\s|\b)(Finanzamt\s+f\u00fcr\s+Geb\u00fchren)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 0 | 5033 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin Elias Stiller (in der Folge als Bf bezeichnet) richtete am 27.11.2012 ein  als „Vorsichtsmeldung“ bezeichnetes Schreiben an die belangte Behörde, das Finanzamt für  Gebühren und Verkehrsteuern (in der Folge als belangte Behörde bezeichnet) mit dem Inhalt,  dass die Bf mit Pachtvertrag vom 1.10.2012 die Parzelle 223 vom Kleingartenverein „ABC“ in  der Adresse ABC in 1220 Wien gepachtet habe, wofür die Bf der Vorpächterin eine Ablöse für  deren Investitionen gezahlt hätte.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Gebühren` | `Finanzamt für  Gebühren` |

**Missed by this rule (FN):**

- `Elias Stiller` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_90`)


Der Verfahrensgang vor der belangten Behörde, dem Finanzamt für Gebühren, Verkehrsteuern  und Glücksspiel, sowie dem Unabhängigen Finanzsenat bzw. nunmehr Bundesfinanzgericht ist  durch den Gebührenbescheid, die als Bescheidbeschwerde zu behandelnde Berufung, die als  Beschwerdevorentscheidung zu behandelnde Berufungsvorentscheidung und den  Vorlageantrag sowie schließlich die Vorlage durch den Vorlagebericht der belangten Behörde  vor dem Bundesfinanzgericht evident.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_31`)


Der Verfahrensgang vor dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel sowie  dem Bundesfinanzgericht ist durch die Bescheide, die Bescheidbeschwerde, die  Beschwerdevorentscheidung sowie die Vorlage vor dem Bundesfinanzgericht evident.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_38`)


Für diesen todeswegigen Erwerb hat das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel mit Grunderwerbsteuerbescheiden vom 19.4.2016, zu Erfassungsnummer 10-2016:  a) der erbl.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_70`)


In dieser Entscheidung hat das Bundesfinanzgericht in Stattgebung des Rechtsmittels den vom  Finanzamt für Gebühren und Verkehrsteuern erlassenen Gebührenbescheid über die  Vorschreibung einer Rechtsgeschäftsgebühr nach § 33 TP 9 GebG 1957 für die dem  Beschwerdeführer und Witwer der Verstorbenen im Verlassenschaftsverfahren nach seiner im  Sommer 2010 verstorbenen Ehegattin in Abgeltung seines gesetzlichen Erbteiles im  Erbteilungsübereinkommen eingeräumten Dienstbarkeit des lebenslänglichen und  unentgeltlichen Wohnungsgebrauchsrechtes an Teilen des Wohnhauses als rechtswidrig  aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_36`)


Das Einkommensteuerfinanzamt leitete die Selbstanzeige an das Finanzamt für Gebühren,  Verkehrssteuern und Glücksspiel weiter.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_115`)


Das Finanzamt für Gebühren, Verkehrssteuern  und Glückspiel und der bundesweite Fachbereich seien eingeschaltet worden.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_245`)


In Übereinstimmung mit dem Finanzamt für Gebühren,  Verkehrssteuern und Glücksspiel und dem Wortlaut des Ausschüttungsbeschlusses wird davon  ausgegangen, dass die Zuwendung satzungsgemäß (nach dem Reglement) erfolgte.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_264`)


Auch das Einkommensteuerfinanzamt übermittelte die Selbstanzeige und die vorgelegten  Unterlagen zunächst dem Finanzamt für Gebühren, Verkehrssteuern und Glücksspiel zur  Prüfung einer allfälligen Schenkungssteuerpflicht.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_304`)


Die Steuerpflicht  sei keinesfalls klar gewesen, weil sich mit dieser Frage sowohl das Finanzamt Baden, das  Finanzamt für Gebühren, Verkehrssteuern und Glücksspiel und der bundesweite  Fachbereich befasst hätten.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

## `Federal Ministry` 💣

**F1:** 0.008 | **Precision:** 0.952 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `907540dd`  
**Description:**
Matches the Federal Minister for Labour, Social Affairs and Consumer Protection.

**Content:**
```
\bBundesministers?\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.952 | 0.004 | 0.008 | 21 | 20 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 1 | 5023 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_54`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_159`)


Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_39`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl Nr 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_171`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_137`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl II Nr 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_123`)


Für die Einschätzung des Grades der Behinderung  sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des Behinderten- einstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere Be- stimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_37`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl Nr 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl II Nr 261/2010, in der  jeweils geltenden Fassung anzuwenden (§ 8 Abs 5 FLAG 1967).

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_43`)


Wie bereits vom begutachtenden Arzt ausgeführt, ergibt  sich die Höhe des Grades der Behinderung nicht bereits aus der Tatsache, dass eine bestimmte  Erkrankung besteht, sondern aus den Auswirkungen der aus dieser Erkrankung resultierenden  Funktionsbeeinträchtigungen auf die Teilhabe am Leben in der Gesellschaft und im  Erwerbsleben (§ 1 Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung), BGBl II 2010/261 idF BGBl II 2012/151).

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_40`)


über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_233`)


jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_70`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des Behindertenein- stellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_104`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_69`)


Die näheren Bestimmungen über diesen Ausweis  sind durch Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz zu  treffen.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_152`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_76`)


Die näheren  Bestimmungen über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_54`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_114`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung/EVO) vom 18. August 2010, BGBl. II Nr. 261/2010, in  der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_17`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des   Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und   die Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend   nähere Bestimmungen über die Feststellung des Grades der Behinderung   (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils   geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_41`)


Für die  Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_62`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_70`)


Gemäß § 15 Abs. 2 Z. 2 EStG 1988 wird der Bundesminister für Finanzen ermächtigt, im  Einvernehmen mit dem Bundesminister für Arbeit, Soziales und Konsumentenschutz die Höhe  geldwerter Vorteile mit Verordnung festzulegen sowie in der Verordnung für Kraftfahrzeuge,  Krafträder und Fahrräder im Interesse ökologischer Zielsetzungen Ermäßigungen und  Befreiungen vorzusehen.

**False Positives:**

- `Bundesminister für Arbeit, Soziales und Konsumentenschutz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Authority Generic` 💣

**F1:** 0.625 | **Precision:** 0.875 | **Recall:** 0.486  

**Format:** `regex`  
**Rule ID:** `27b2ae14`  
**Description:**
Matches 'Finanzamt' and 'Finanzamtes' with optional location suffixes (including 'Österreich', 'Wien', etc.) using flexible context anchors.

**Content:**
```
(?:^|\s|\b)(Finanzamt(?:es)?(?:\s+(?:Österreich|Wien\s+\d+(?:/\d+)*|Graz-Stadt|Kitzb\u00fchel\s+Lienz|Linz|Braunau\s+Ried\s+Sch\u00e4rding|Kirchdorf\s+Perg\s+Steyr|St\.\s+Veit|Feldkirch|Salzburg|Neunkirchen\s+Wr\.\s+Neustadt|Wr\.\s+Neustadt|Gmunden|V\u00f6cklabruck|Innsbruck|Bruck|Eisenstadt|Oberwart|Vorarlberg|St\.\s+Johann|Tamsweg|Zell\s+am\s+See|Grieskirchen|Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Gro\u00dfbetriebe|\d+(?:/\d+)+|FA\s+\w+\s+\w+\s+\w+|FA\s+\w+\s+\w+|FA\s+\w+|Spittal\s+Villach|Purkersdorf|f\u00fcr\s+Geb\u00fchren))?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.875 | 0.486 | 0.625 | 2800 | 2449 | 351 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2449 | 351 | 2594 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_2`)


Entscheidungsgründe 1. Sachverhalt Mit Schreiben vom 15. Juli 2014 teilte der Bf. dem Finanzamt mit „Änderung Bewirtschaftung KG  URKJ Forschung KG , EZ x1, Grundstücke xx1 und xx2“ mit, dass der Weingarten Grundstück xx1 komplett gerodet worden sei und jetzt brachliege.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `URKJ Forschung KG` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_8`)


Name, Adresse und Geburtsdatum des Bf. Am 23. Juli 2014 erließ das Finanzamt einen Bescheid mit folgendem Inhalt: „Bescheid: Der Antrag von …. Bf. …. vom 15.7.2014, eingebracht am 22.7.2014 betreffend den Antrag auf Wertfortschreibung wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_14`)


“ Am 2. August 2014 langte beim Finanzamt ein Schreiben mit folgendem Inhalt ein: „Beschwerde gegen Bescheid vom 23.7.14 EZ x1  , Grundstücke xx1 u. xx2“….Ich bringe gegen den im Betreff angeführten Bescheid Beschwerde ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_18`)


Mit „Bescheid – Mängelbehebungsauftrag“ vom 29. August 2014  stellte das Finanzamt fest, dass die Eingabe des Bf. vom 2.8.2014 hinsichtlich der Form (§ 85 Abs. 2 BAO) folgende Mängel aufweise: Gemäß § 250 Abs. 1 BAO hat eine Bescheidbeschwerde folgende Punkte zu enthalten: 1. die Erklärung, in welchen Punkten der Bescheid angefochten wird, 2. die Erklärung, welche Änderungen beantragt werden;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_21`)


Mit dem Formular „Bescheid – Zurücknahme/Gegenstandsloserklärung“ vom 8. Oktober 2014   entschied das Finanzamt, dass die Beschwerde des Bf. vom 2. August 2014 betreffend Bescheid vom 23. Juli 2014 gemäß § 85 Abs. 2 BAO als zurückgenommen gilt. Als Begründung gab es an, dass der Bf. dem Auftrag, die Mängel der Beschwerde bis 29. September 2014 zu beheben, nicht entsprochen habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_22`)


Am 28. Oktober 2014 brachte der Bf. beim Bundesfinanzgericht einen „Vorlageantrag betreffend Berufungsvorentscheidung vom 8.10.2014 (vom Finanzamt fälschlicherweise als Bescheid – Zurücknahme/Gegenstandsloserklärung bezeichnet)“ ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_23`)


Gegen das Schreiben vom 29. August 2014 des Finanzamtes sei laut Rechtsmittelbelehrung kein Rechtsmittel zulässig gewesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_26`)


Im Vorlagebericht beantragte das Finanzamt, dass das Bundesfinanzgericht in der Sache selbst abweislich entscheide: „   Der Beschwerdeführer verlangt eine sofortige Fortschreibung des Einheitswertes wegen der im Juni 2014 erfolgten Rodung eines Weingartens.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_49`)


Seite 4 von 5 Das Finanzamt hat den Mängelbehebungsauftrag (vom 29. August 2014) auf § 250 Abs. 1 lit. b-d BAO gestützt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_60`)


Die Beschwerde (vom 2. August 2014) entspricht auch dieser Anforderung: das Finanzamt hat den Antrag des Bf. auf Wertfortschreibung mit der Begründung abgewiesen, dass es sich bei der Weingartenrodung des Bf. um keine Dauerrodung handle, da er bei der entsprechenden Meldung als Wiederbepflanzungsberechtigter aufscheine und mitgeteilt, dass eine Dauerrodung im Jahr 2014 erst zum 1.1.2015 berücksichtigt werden könne.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_62`)


Der Auffassung des Finanzamtes, dass die Beschwerde (vom 2. August 2014) den Bestimmungen des § 250 Abs. 1 BAO nicht Rechnung tragen würde, kann daher nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_5`)


Zum Streitpunkt Verjährung: Der Beschwerdeführer (Bf.) bezog im Berufungs(Beschwerde)zeitraum neben Einkünften aus nichtselbständiger Arbeit beim Finanzamt Mödling unter St.Nr. 111 einheitlich und gesondert festgestellte Einkünfte aus Vermietung und Verpachtung (als Beteiligter der aus ihm und seiner Ehegattin bestehenden Hausgemeinschaft "HG").

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_7`)


Nach Ergehen neuer Feststellungsbescheide vom 23.12.2010 (2001) bzw. 27.12.2010 (2002 bis 2008), welche die Einkünfte aus Vermietung und Verpachtung des Bf. mit Seite 2 von 15 788,28 € (bzw. 10.847,00 S, 2001), 940,38 € (2002), 975,45 € (2003), 1.141.04 € (2004), 1.328,63 € (2005), 77,30 € (2006), 2.172,21 € (2007) und 2.165,91 € (2008) feststellten, erließ das Finanzamt mit Datum 12.1.2011 gemäß § 295 BAO geänderte, den neuen Feststellungen Rechnung tragende Einkommensteuerbescheide 2000 bis 2008.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_9`)


In seiner abweisenden Berufungsvorentscheidung führt das Finanzamt Folgendes aus: "Die Verjährung beginnt gemäß § 208 Abs. 1 lit. d BAO in den Fällen des § 200 (vorläufige Festsetzung von Abgaben) mit dem Ablauf des Jahres, in dem die Ungewissheit beseitigt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_18`)


Mit Schreiben vom 21.12.1998 wurde seitens der Hausgemeinschaft HG um Anwendung der neuen Liebhaberei-Verordnung angesucht und nach neuerlicher Aufforderung seitens des Finanzamtes mit Vorhalt vom 6.6.2003 um ergänzende Abgabe einer Prognoserechnung, wurde von der Hausgemeinschaft schließlich eine grobe Darstellung der Ausgaben bis 2004 vorgelegt sowie darauf hingewiesen, dass das Haus unter Denkmalschutz stünde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_44`)


Das Finanzamt meint, dass erst mit dem Faktum der Betriebsprüfung die Ungewissheit beseitigt worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_45`)


Mit diesem Hinweis legt das Finanzamt lediglich dar, wann für das Finanzamt - subjektiv - die Ungewissheit beseitigt worden ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_46`)


Das Finanzamt hat sich im Rahmen des Ermittlungsverfahrens allenfalls Kenntnis über die objektiven Umstände über das Vorliegen der Einkunftsquelle verschafft, aber keine Fakten geschaffen, die Einfluss auf das Bestehen oder Nichtbestehen der Einkunftsquelle haben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_47`)


Die Erkenntnisse, die das Finanzamt bei der Betriebsprüfung gewonnen hat, hätten bei ordnungsgemäßen Ermittlungsverfahren auch bereits in den Streitjahren gewonnen werden können, spätestens jedoch mit der Beantwortung des Vorhaltes vom 6. Juni 2003."

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_124`)


Die vom Finanzamt Mödling in den Feststellungsbescheiden getroffene Feststellungen, die Hausgemeinschaft habe in den Jahren 2001 bis 2008 Einkünfte von 1.576,56 € (2001), 1.880,77 € (2002) 1.950,91 € (2003), 2.282,08 € (2004), 2.657,27 € (2005), 154,60 € (2006), 4.344,41 € (2007) und 4.344,81 € (2008) erzielt, sind daher für das Einkommensteuerverfahren des Bf. bindend.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_133`)


Einem im Einkünftefeststellungsakt des Finanzamtes Mödling einliegenden Vermerk vom 12. Juni 2003 ist zu entnehmen, dass die Feststellungsbescheide seit 1995 vorläufig und die Bescheide vorläufig zu belassen seien (es sei ein Beobachtungszeitraum von 20 Jahren (21.12.1998) gestellt worden).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_135`)


Am 4.5.2009 vermerkte das Finanzamt im Zuge der Überprüfung der vorläufigen Veranlagung, dass es sich um ein Haus handle, dass unter Denkmalschutz stehe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_145`)


Nach der Betriebsprüfung stellte das Finanzamt Mödling für die Jahre 2001 bis 2008 mit endgültigen Bescheiden vom 23.12.2010 (2001) und vom 27.12.2010 (2002 bis 2008) fest, dass nur hinsichtlich der vermieteten Putzerei eine Einkunftsquelle vorliege.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_149`)


In Anbetracht der vom der Hausgemeinschaft erklärten Werbungskostenüberschüsse ist das Finanzamt anlässlich der Erlassung der Feststellungsbescheide 2001 bis 2008 zum Ergebnis gekommen, dass bei der gegenständlichen Vermietung nicht von vornherein von Liebhaberei ausgegangen werden könne und hat daher vorläufige Feststellungsbescheide für die Jahre 2000 bis 2008 erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_153`)


Aufgrund der erklärten Werbungskostenüberschüsse konnte eine endgültige Qualifizierung der Vermietungstätigkeit der Bf. als Einkunftsquelle oder Liebhaberei nicht vorgenommen Seite 11 von 15 werden und lag aus damaliger Sicht für das Finanzamt eine die Vorläufigkeit rechtfertigende Ungewissheit im Tatsachenbereich zweifelsfrei vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_154`)


Das Finanzamt hat daher zu Recht zunächst vorläufige Bescheide erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_169`)


Es kommt nicht darauf an, wann das Finanzamt davon Kenntnis erlangte, sondern wann die Ungewissheit objektiv weggefallen ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_179`)


2. Zum Streitpunkt "Home Office": 2.1. Beweiswürdigung: Die obigen Sachverhaltsfeststellungen ergeben sich aus der Aktenlage des Finanzamtes und den Angaben des Bf. in der Berufung und im Vorlageantrag.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_8`)


Mit Erstbescheid vom 10. August 2017 veranlagte das Finanzamt (kurz FA) die Einkommensteuer 2015 auf Basis der elektronisch eingereichten Erklärung, ließ allerdings von insgesamt EUR 93.491,00 nur EUR 38.011,01 zum als freigebige Zuwendungen zum Sonderausgabenabzug zu. Bei der dafür ausschlaggebenden Berechnung der 10 % - Grenze brachte das FA im Rahmen des Gesamtbetrages der Einkünfte nur die im Inland Seite 2 von 6 steuerpflichtigen Einkünfte in Ansatz.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Mag. Mirha Karahodzic MA` (person)
- `Elisabeth Schafstall` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_7`)


Das Bundesfinanzgericht leitete den Antrag zuständigkeitshalber an  das Finanzamt weiter, wo der Antrag am 14.2.2020 fristgerecht einlangte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_9`)


Mit Bescheid vom 13.11.2000 veranlagte das Finanzamt den Bf zur Einkommensteuer für 1999  zunächst erklärungsgemäß.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_10`)


Aufgrund von abweichenden Mitteilungen des für die Einkünftefeststellung gem. § 188 BAO  der Beteiligung A und der Beteiligung C vom 1.12.2006 erließ das Finanzamt am 9.1.2007 einen  gem. § 295 Abs. 1 BAO geänderten Einkommensteuerbescheid 1999 und setzte darin die  Einkünfte aus Gewerbebetrieb neu lediglich mit der Beteiligung B fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_11`)


Aufgrund einer weiteren Mitteilung setzte das damals auch für die einheitliche und gesonderte  Einkünftefeststellung der B K(E)G zuständig gewesene Finanzamt Wien 8/16/17  das Wohnsitzfinanzamt des  Bf davon in Kenntnis, dass im Feststellungsverfahren dieser Personengesellschaft am  28.11.2006 ebenfalls ua Erledigungen betreffend das Unterbleiben von Einkünftefeststellungen  für die beteiligten Kommanditisten für die Jahre 1998-2001 ausgefertigt worden sind.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_12`)


Folglich dieser Mitteilung änderte das belangte Finanzamt den Einkommensteuerbescheid  1999 des Bf am 7.12.2007 erneut gem. § 295 Abs. 1 BAO dahingehend ab, dass in diesem  nunmehr Einkünfte aus Gewerbebetrieb iHv ATS 0,00 angesetzt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_14`)


Im Dezember 2006 legte die B KEG ua Berufungen gegen die an sie adressierten „Bescheide“  des FA Wien 8/16/17  vom 1.12.2006 betreffend Einkünftefeststellung gem. § 188 BAO für die Jahre  1988 – 2001 sowie gegen die an sie und an die Kommanditisten adressierten „Bescheide“ des  Finanzamt Wien 8/16/17  vom 28.11.2006 betreffend Unterbleiben der Feststellungen von Einkünften in  Bezug auf die Kommanditisten für den Zeitraum 1998 – 2001 ein.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Missed by this rule (FN):**

- `FA Wien 8/16/17` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_16`)


Verstoß gegen das für Grundlagenbescheide iSd § 188 BAO geltende Einheitlichkeitsgebot  insgesamt um Nichtbescheide handelt.  Mit schriftlichem Anbringen vom 20.12.2012, eingelangt beim Finanzamt am 28.12.2012,  beantragte die steuerliche Vertreterin des Bf ua den Einkommensteuerbescheid 1999 vom  7.12.2007 gem. § 295 Abs. 4 BAO aufzuheben, weil diesem auf Grundlage des § 295 Abs. 1 BAO  ergangenen Einkommensteuerbescheid laut Berufungsentscheidung des UFS vom 15.11.2012,  RV/0102-K/08 (betreffend Beteiligung KEG), ein Nichtbescheid mit Folge seiner  Rechtswidrigkeit zugrunde liege, und somit die Anspruchsvoraussetzungen iSd § 295 Abs. 4  BAO erfüllt seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_17`)


Mit offenkundig versehentlich als „Aufhebungsbescheid gem. § 299 BAO betiteltem  Sammelbescheid vom 12.3.2013 hob das belangte Finanzamt ua den  Einkommensteuerbescheid 1999 vom 7.12.2007 nach eindeutigem Bescheidspruch und damit  im Einklang stehender Begründung wie beantragt auf Grundlage des § 295 Abs. 4 BAO auf.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_19`)


Das Finanzamt hätte unrichtigerweise die  notwendigen ersetzenden Bescheide gem. § 299 Abs. 2 BAO nicht erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `James Hainig` (person)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `85-229/2263` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Schreiben vom 15.06.2016 wurden die Erklärungen betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 beim Finanzamt eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_37`)


Mit Bescheiden vom 21.12.2016 erließ das Finanzamt die Erstbescheide betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 in denen die  Berufsgruppenpauschale für VertreterInnen nicht gewährt wurde und begründete die  Bescheide wie folgt:   "Vertreter sind nach übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer  Kommentar, Tz 6 zu § 17 EStG), Verwaltungsübung LstRL RZ 406) und Entscheidungspraxis (zB  BFG 23.05.2014, RV/6100146/2013) Personen, die im Außendienst zum Zwecke der Anbahnung  und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_92`)


Inhaltlich  hätte sich das Finanzamt **** durch umfassendere Beweiswürdigung mit der tatsächlichen  Tätigkeit der Beschwerdeführerin auseinanderzusetzen gehabt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Jana Papenkord` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Antrag  Der Beschwerdeführerin (Bf.) beantragte mit dem am 21. März 2018 beim Finanzamt (FA)  eingelangtem Formular Beih 1 (datiert mit 12. Februar 2018) Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_12`)


Mit Bescheid vom 12. Juni 2018 wies das Finanzamt den Antrag vom 21.3.2018 auf  Familienbeihilfe für Jana Papenkord  ab Jänner 2011 ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Jana Papenkord` (person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_23`)


Beschwerdevorentscheidung   Mit Beschwerdevorentscheidung vom 22.10.2018 wies das Finanzamt die Beschwerde als  unbegründet ab:  „Gemäß § 5 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG 1967) in der ab 1. Jänner 2011  gültigen Fassung besteht für Kinder, die das 18.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_51`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Vom Finanzamt wurde folgender Sachverhalt festgehalten:  „Der Eigenantrag auf Familienbeihilfe wurde am 21.03.2018 eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Ali Jäckle` (person)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_6`)


Nach Durchführung umfangreicher Ermittlungen bei den steuerlichen Vertretern und der  Masseverwalterin des Ehemannes wies das Finanzamt die Beschwerde mit  Beschwerdevorentscheidung vom 12.7.2016 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_8`)


Das Finanzamt legte die Beschwerde dem Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_51`)


Im Anschluss an eine Außenprüfung für 2013 bis 2015 habe das Finanzamt auch für 2011  einen neuen Körperschaftsteuerbescheid erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_113`)


Diese ist zusammen mit  der Gewinn- und Verlustrechnung dem Finanzamt vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Marion Endrulat` (person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_10`)


…   Das Finanzamt erließ am 5. September 2019 den beschwerdegegenständlichen  Abweisungsbescheid wie folgt:   Ihr Antrag vom 5.4.2019 auf Familienbeihilfe wird abgewiesen für:   Name des Kindes VNR/Geb.dat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_15`)


Das Finanzamt Gänserndorf  Mistelbach hat mit Bescheid diesen Antrag abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_33`)


IV. Beschwerdeerklärung und Anträge   Ich erhebe daher gegen den Bescheid der belangten Behörde vom 05.09.2019, (ohne) GZ, in  offener Frist gem § 243 BAO iVm Art 130 Abs 1 Z 1 B-VG und Art 131 Abs 3 B-VG   Bescheidbeschwerde an das Verwaltungsgericht des Bundes für Finanzen und stelle den   Antrag das Verwaltungsgericht des Bundes für Finanzen möge   - den angefochtenen Bescheid vom 05.09.2019, (ohne) GZ, aufheben und die Angelegenheit  zur Erlassung eines neuen - meinem Antrag stattgebenden - Bescheides an das Finanzamt  Gänserndorf Mistelbach zurückverweisen,   - in eventu den angefochtenen Bescheid dahingehend abändern, dass meinem Antrag auf  Familienbeihilfe für meinen Sohn … ab April 2019 stattgegeben wird.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_34`)


Das Finanzamt erließ eine abweisende Beschwerdevorentscheidung mit folgender  Begründung:   Das Kind …, SVNR …, wurde mit Wirkung 13.05.2019 in den Polizeidienst eingestellt.   Der Bestätigung des Bildungszentrums der Sicherheitsakademie Y. -SIAK- entnehmbar  absolviert der Sohn … vom 13.05.2019 bis 12.05.2021 den Grundausbildungslehrgang Y-… für  den Exekutivdienst im Bildungszentrum der Sicherheitsakademie Y..   Mit Dienstvertrag – als Sondervertrag gem. § 36 VBG 1948 – vom 13.05.2019 wurde das  privatrechtliche Dienstverhältnis zum Bund (§ 1 Abs. 1 VBG 1948) begründet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_57`)


Die Bf. brachte daraufhin den Vorlageantrag ein, mit dem sie die in der Beschwerde gemachten  Ausführungen wiederholt.   Die Beschwerdevorlage des Finanzamtes erfolgte mit nachstehendem Sachverhalt und  Anträgen:   Sachverhalt:   Der Sohn der Beschwerdeführerin … begann am 13.05.2019 die exekutivdienstliche Ausbildung  im Bildungszentrum Y.. Die Einstellung in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich erfolgte mit Sondervertrag nach § 36 VBG 1948.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Landespolizeidirektion  Niederösterreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_157`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer Anzeige vom 20.4.2017 vernahm das Finanzamt den Beschwerdeführer am  9.5.2017 ein und verfasste darüber eine Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_12`)


Das Finanzamt setzte mit Bescheid vom 7.6.2017 die Normverbrauchsabgabe für das Fahrzeug  BMF 750d xDrive mit der Fahrgestellnummer 12345 und dem amtlichen Kennzeichen (D) XYZ in  1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_22`)


Mit Schreiben vom 16.10.2017 forderte das Finanzamt den Beschwerdeführer auf,  zweckdienliche Unterlagen zum Beweis des dauernden Standortes bzw. der weitaus  überwiegenden betrieblichen Verwendung des Fahrzeuges im Ausland und zum Beweis des  Mittelpunkts seiner Lebensinteressen im Ausland vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_23`)


Weiter forderte das Finanzamt  eine Aufstellung der betrieblich bzw privat gefahrenen Kilometer im In- und Ausland an.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_24`)


Das  Finanzamt verwies dabei auf zwei vorliegenden Tankrechnungen (eni Reutte vom 4.5.2017 und  Shell d_Ort_1 vom 28.4.2017).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_36`)


Mit Beschwerdevorentscheidung vom 22.3.2018 wies das Finanzamt die Beschwerde ab und  begründete dies damit, dass der Beschwerdeführer bei seiner Einvernahme am 9.5.2017  angegeben habe, der Besitzer und Verwender des gegenständlichen Fahrzeuges zu sein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_46`)


Im Vorlagebericht vom 25.5.2018 brachte das Finanzamt weiter vor, dass der  Beschwerdeführer die im Vorlageantrag angesprochene Anmeldebestätigung nicht vorgelegt  habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_226`)


Einwendungen gegen die vom  Finanzamt ermittelten Bemessungsgrundlagen und die Höhe der festgesetzten Abgaben hat  der Beschwerdeführer nicht erhoben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  2/20/21/22` | `Finanzamtes Wien  2/20/21/22` |

**Missed by this rule (FN):**

- `Sabine Tiedicke` (person)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_43`)


1. Anspruchsberechtigung auf Familienbeihilfe/Ausgleichszahlung für das Kind x im Zeitraum  vom 01.02.2016 bis zum 30.11.2017  Unter Bezugnahme auf die Ausführungen der belangten Behörde in  der Beschwerdevorentscheidung (BVE) vom 08.01.2020 sowie in der Ihnen  übermittelten Stellungnahme im Vorlagebericht des Finanzamtes vom 14.04.2020 werden Sie  nochmals darauf hingewiesen, dass in Ermangelung des Bestehens eines gemeinsamen  Haushalts mit obigem Kind eine Anspruchsberechtigung für nämlichen Zeitraum nicht zum  Tragen kommt.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  3/6/7/11/15` | `Finanzamtes Wien  3/6/7/11/15` |

**Missed by this rule (FN):**

- `Ing. Sascha Hilcker` (person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_5`)


Dauer der Tätigkeit: 31.08.2020  Bezeichnung der Schule: Sicherheitsakademie T.[Adresse]   Schulform: Sonstiges   Schuljahr: 2018/2019  Das Finanzamt erließ am 21. August 2019 den beschwerdegegenständlichen Bescheid, mit dem  der Antrag der Bf. vom 6. April 2019 auf Familienbeihilfe ab September 2018 abgewiesen  wurde;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_8`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 30. August 2019 wie folgt:   Die vom Finanzamt Wien 4/5/10 per 26. April 2019 mit Ersuchen um Ergänzung abverlangten  Unterlagen (Dienstvertrag) habe ich am 06. Mai 2019 (Frist bis 17. Mai 2019) mittels  „Einschreiben“, Sendungsnummer: RM 205067923AT, an das Finanzamt Wien 4/5/10  übermittelt.   Da ich in der Zwischenzeit (Anfang Juli 2019) umgezogen bin, habe ich via Finanzonline eine  Nachricht erhalten, dass von nun an das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf  zuständig sei.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 4/5/10` | `Finanzamt Wien 4/5/10` |
| `Finanzamt Wien 4/5/10` | `Finanzamt Wien 4/5/10` |

**Missed by this rule (FN):**

- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_9`)


Nun erhielt ich am 26.08.2019 einen Abweisungsbescheid vom Finanzamt Wien 3/6/7/11/15  Schwechat Gerasdorf mit der Begründung, dass ich die abverlangten Unterlagen nicht  eingebracht hätte.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 3/6/7/11/15` | `Finanzamt Wien 3/6/7/11/15` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_30`)


Das Finanzamt wies mit Beschwerdevorentscheidung vom 25. Oktober 2019, zugestellt durch  Hinterlegung am 30. Oktober 2019, die Beschwerde als unbegründet ab und begründete dies  wie folgt:   Gemäß § 2 Abs. 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die  im Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_56`)


Das Finanzamt Wien 3/6/7/11/15/ Schwechat Gerasdorf hat unzutreffend und rechtswidrig  5 von 17 Seite 6 von 17

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 3/6/7/11/15` | `Finanzamt Wien 3/6/7/11/15` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_62`)


In der Beschwerdevorlage wies das Finanzamt auf die exekutivdienstliche Ausbildung der Bf.  mit Sondervertrag für Vertragsbedienstete des Bundes sowie auf das Erkenntnis des VwGH  vom 18.12.2018, GZ Ra 2018/16/0203, hin und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_167`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_3`)


Begründung  Am 10.5.2019 erließ das Finanzamt gegenüber der Beschwerdeführerin (Bf.) die  Einkommensteuerbescheide (Arbeitnehmerveranlagung) für 2015 bis 2018 (die Bescheide der  Jahre 2015 bis 2017 ergingen im Rahmen einer beantragten Wiederaufnahme).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_4`)


Mit Eingabe vom 11.4.2020, die vom Finanzamt – nach Ansicht des BFG zutreffend – als Antrag  auf Aufhebung der Einkommensteuerbescheide 2015 bis 2018 gemäß § 299 BAO gewertet  wurde, bemängelte die Bf., dass in den Bescheiden die Mietkosten für ihren Sohn nicht als  außergewöhnliche Belastungen berücksichtigt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_8`)


Mit den angefochtenen Bescheiden wies das Finanzamt den Antrag der Bf. mit folgender  Begründung ab:  „Außergewöhnliche Belastungen müssen gemäß § 34 EStG 1988 folgende Voraussetzungen  erfüllen:  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_22`)


Die abweisenden Beschwerdevorentscheidungen begründete das Finanzamt wie folgt:  „Eine außergewöhnliche Belastung im Sinne des § 34 EStG 1988 liegt dann vor, wenn die  Ausgaben außergewöhnlich und zwangsläufig erwachsen sind und die wirtschaftliche  Leistungsfähigkeit beeinträchtigen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_71`)


Dazu kommt, dass in den Bescheiden des Finanzamtes lediglich auf die Abs. 1 bis 4 des § 34  EStG 1988 verwiesen wird.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_32`)


Nach Auffassung des Finanzamtes Baden Mödling ist dieser in Erledigung der Beschwerde ergangene Bescheid dennoch als formal rechtskonforme Beschwerdevorentscheidung im Sinne von § 263 Abs 1 lit b Bundesabgabenordnung anzusehen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Baden Mödling`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Alexander Hajicek`(person)
- `Mag. Helga Hochrieser`(person)
- `Mag. Michael Franz`(person)
- `Mag. Franz Josef Großin`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_177`)


Dies trifft jedoch nicht auf die Einkommensteuerbescheide für die Jahre 2003 bis 2008 zu, da es in den Jahren 2009 und 2010 nach außen erkennbare Amtshandlungen des Finanzamts gegeben hat, die die Verjährungsfrist gemäß § 209 Abs. 1 BAO verlängern.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

**False Positives:**

- `Finanzamtes Salzburg` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Jeannette Neuschwender`(person)
- `Zum Kogl 12, 4441 Penz, Österreich`(address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Peter Staudinger`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_17`)


2. Beweiswürdigung:  Der Sachverhalt ergab sich aus dem vorgelegten Finanzamtsakt, dem elektronischen  Steuerakt sowie den Eintragungen in FinanzOnline, in die über das "Verbundkomponente  Auskunftssystem 4.0" Einsicht genommen wurde.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_51`)


Vielmehr geht sein Vorbringen dahin, dass ihm nicht  bewusst gewesen sei, eine Zustimmung zur Zustellung seiner Finanzamtsbescheide mittels  FinanzOnline (in die Databox) erteilt zu haben.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Tirol Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dietlind Mahlstädt`(person)
- `Kai Pipers`(person)
- `Gottaweg 58, 9130 Annamischl, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamt Tirol Ost`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_58`)


Die Frage, ob die Bf. im Jahr 2013 ein den Betrag von 10.000 € übersteigendes Einkommen  (unter Berücksichtigung der Einschleifregelung) erzielt hat, ist bereits in der  Beschwerdevorentscheidung des Finanzamts bejaht worden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_81`)


Wie bereits oben festgehalten, ist die Bf. den Feststellungen des Finanzamts, dass sie im Jahr  2013 ein den Betrag von 10.000 € übersteigendes Einkommen erzielt hat, im ganzen bisherigen  Verfahren nicht entgegengetreten;

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_87`)


Ergänzend wird (zum Sachverhalt und zur rechtlichen Beurteilung) noch auf das BFG-Erkenntnis  RV/7102641/2016 vom 9.1.2018 sowie auf die Beschwerdevorentscheidung des Finanzamts  vom 22.10.2018 verwiesen, deren Ausführungen vom Bundesfinanzgericht ausdrücklich geteilt  werden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_14`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 15. September 2019 wie  folgt:   I. Sachverhalt:   Ich habe am 05.04.2019 für meinen Sohn … ab dem Zeitraum April 2019 die Familienbeihilfe  beim zuständigen Finanzamt Gänserndorf Mistelbach beantragt, da dieser seit Mai 2019 eine  Berufsausbildung (bis Ende März 2019 Zivildienst) absolviert.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_17`)


III. Rechtsverletzung und Beschwerdegründe:   Der Abweisungsbescheid des Finanzamtes Gänserndorf Mistelbach vom 05.09.2019, (ohne) GZ,  verletzt mich in meinem subjektiven Recht.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_29`)


Das Finanzamt Gänserndorf Mistelbach hat unzutreffend und rechtswidrig eine  Ausbildungsphase der fremden- und grenzpolizeilichen exekutivdienstlichen Ausbildung, die  keinen Anspruch auf Familienbeihilfe begründet (weil das FLAG 1967 den Begriff der  Ausbildungsphase nicht kennt), bei der 24-monatigen durchgehenden Ausbildung meines  Sohnes … angenommen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_8`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 30. August 2019 wie folgt:   Die vom Finanzamt Wien 4/5/10 per 26. April 2019 mit Ersuchen um Ergänzung abverlangten  Unterlagen (Dienstvertrag) habe ich am 06. Mai 2019 (Frist bis 17. Mai 2019) mittels  „Einschreiben“, Sendungsnummer: RM 205067923AT, an das Finanzamt Wien 4/5/10  übermittelt.   Da ich in der Zwischenzeit (Anfang Juli 2019) umgezogen bin, habe ich via Finanzonline eine  Nachricht erhalten, dass von nun an das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf  zuständig sei.

**False Positives:**

- `Finanzamt Wien 3/6/7/11/15` — partial — pred is substring of gold: `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 4/5/10`(organisation)
- `Finanzamt Wien 4/5/10`(organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_45`)


Der Vorlageantrag der Bf. vom 28. November 2019, fristgerecht eingebracht durch  Postaufgabe am 29. November 2019, enthält nachstehende Begründung:   Die Beschwerdevorentscheidung des Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf  vom 25.10.2019, verletzt mich in meinem subjektiven Recht.

**False Positives:**

- `Finanzamtes Wien 3/6/7/11/15` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Helge Göppele`(person)
- `GDJJ Versand`(organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich`(address)
- `Finanzamtes Graz`(organisation)

</details>

---

## `SUVA` 💣

**F1:** 0.008 | **Precision:** 0.826 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `0bbe7987`  
**Description:**
Matches 'SUVA' (Sozialversicherungsanstalt der Selbständigen).

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.826 | 0.004 | 0.008 | 23 | 19 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 4 | 5024 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_11`)


Dagegen erhob der Beschwerdeführer unter Anschluss einer Bescheinigung der SUVA über  die Höhe der Rente und den erfolgten Quellensteuerabzug sowie einer Verfügung der Eidge- nössischen Invalidenversicherung über den bestehenden Leistungsanspruch Beschwerde und  ersuchte um Neuberechnung der Einkommensteuer für das Jahr 2015 unter Berücksichtigung  der von der Invalidenversicherung tatsächlich bezogenen Rente in Höhe von 1.794,00 CHF mo- natlich.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_12`)


Die von der SUVA bezogene Invalidenrente resultiere aus einem Arbeitsunfall und sei  daher steuerfrei zu belassen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_15`)


4.  Mit Beschwerdevorentscheidung vom 5. Juli 2017 gab das Finanzamt der Beschwerde inso- weit teilweise Folge als nur mehr die von der Invalidenversicherung und der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe in Ansatz gebracht wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_16`)


Hinsichtlich der  Steuerpflicht der von der SUVA bezogenen Invalidenrente wurde unter Verweis auf das Er- kenntnis des Bundesfinanzgerichtes vom 9. Februar 2016, RV/1100448/2012, auf das Wesent- lichste zusammengefasst ausgeführt, dass es sich bei der von der SUVA ausgerichteten Unfall- rente nicht um dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen  Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspreche, handle, da  durch die schweizerische Invalidenrente – anders als in Österreich – nicht primär ein individuel- ler Schaden ersetzt werde, sondern der ausgefallene Verdienst und solche Renten somit ein  steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_17`)


5.  Mit Vorlageantrag beantragte die steuerliche Vertretung die Entscheidung über die Be- schwerde durch das Bundesfinanzgericht, wobei zusätzlich die Anrechnung des auf den steuer- pflichtigen Teil der Invalidenrente entfallenden Anteiles der von der SUVA einbehaltenen Quel- lensteuer in Höhe von 5.623,80 CHF geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_19`)


Das Bundesfinanzgericht sei in dem vom Finanz- amt angeführten Erkenntnis zum Schluss gekommen, dass die Leistungen der SUVA bereits  dem Grunde nach nicht mit jenen der AUVA vergleichbar seien, sodass eine Überprüfung der  Höhe nach unterblieben sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_43`)


Beim Beschwerdeführer sei von der SUVA aufgrund eines  Arbeitsunfalles im Jahr 2010 eine Beeinträchtigung der Erwerbsfähigkeit von 90% festgestellt  worden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_51`)


Hinsichtlich dieses nicht von der Steuerbefrei- ung umfassten Teiles der Rente werde beantragt, die von der SUVA einbehaltene Quellen- steuer (5.623,80 CHF) auf die sich darauf ergebene Einkommensteuer anzurechnen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_52`)


7.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_55`)


9.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen teilte die steuerliche Vertre- tung mit, dass der Antrag auf Rückerstattung der schweizerischen Quellensteuer abgewiesen  worden sei und legte ua. eine E-Mail des Steueramtes des Kantons Luzern vom 3. Februar 2022  vor, aus welcher hervorgeht, dass die Schweiz nach Art. 19 des Doppelbesteuerungsabkom- mens das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte Rente zu besteuern.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_58`)


Aufgrund der Folgen eines im Jahr 2010 erlittenen Arbeitsun- falles wurde nach den schweizerischen Bestimmungen eine Minderung der Erwerbsfähigkeit  (Grad der Behinderung) von 90% ermittelt. Im hier interessierenden Zeitraum bezog er eine  Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter Anrechnung  dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizerischen Unfall- versicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_59`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_92`)


Personen, für deren Ver- sicherung nicht die SUVA zuständig ist, werden nach Art. 68 Abs. 1 UVG durch private Versi- cherungsunternehmen (lit. a), öffentliche Unfallversicherungskassen (lit. b) oder Krankenkas- sen (lit. c) nach dem UVG gegen Unfall versichert.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_103`)


Ebenso hat das Bundesfinanzgericht hinsichtlich der von der SUVA ausbezahlten Unfallrenten  die Steuerfreiheit mehrfacht verneint (vgl. ua. BFG 9.2.2016, RV/1100448/2012, sowie jüngst  BFG 9.5.2022, RV/4100533/2020, BFG 26.4.2022, RV/4100192/2018, BFG 7.9.2021,  RV/1100015/2020, und BFG 30.9.2020, RV/1100476/2018).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_118`)


Damit ist auch die  Ermittlung der Einkommensteuervorauszahlungen für die Jahre 2017 sowie 2018 und Folge- jahre zu Recht unter Einbeziehung der von der SUVA bezogenen Invalidenrente erfolgt.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_139`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_143`)


Die einzig die Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffen- den Beschwerden gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervor- auszahlungsbescheide 2017 sowie 2018 und Folgejahre waren folglich als unbegründet abzu- weisen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_7`)


3.  Mit Erkenntnis vom 30. September 2022, RV/1100123/2020, verneinte das Bundesfinanz- gericht der in zahlreichen Erkenntnissen des Bundesfinanzgerichtes vertretenen Auffassung  folgend die Steuerfreiheit der von der SUVA bezogenen Rente und wies die Beschwerden als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_8`)


Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenauszahlung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der  Nichtvorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

**False Positives:**

- `SUVA` — partial — pred is substring of gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_91`)


Die Durchführung der obligatorischen Unfallversicherung obliegt für die in einem in Art. 66  Abs. 1 UVG angeführten bzw. in Art. 73 bis 89 UVV näher umschriebenen Berufszweige tätigen  Arbeitnehmer der Schweizerischen Unfallversicherungsanstalt (SUVA), einer öffentlich-recht- lichen Anstalt mit eigener Rechtspersönlichkeit (Art. 61 Abs. 1 UVG).

**False Positives:**

- `SUVA` — partial — pred is substring of gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schweizerischen Unfallversicherungsanstalt (SUVA)`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_5`)


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheiden vom 10. Juli 2019 setzte das Finanzamt die Einkommensteuer für die Jahre  2017 und 2018 fest, wobei eine von der Schweizerischen Unfallversicherungsanstalt (SUVA)  ausbezahlte Invalidenrente abweichend von den eingereichten Erklärungen zur Gänze als  steuerpflichtig behandelt wurde.

**False Positives:**

- `SUVA` — partial — pred is substring of gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_15`)


Die im Beschwerdefall strittige Frage, ob es sich bei einer infolge eines Arbeitsunfalles von der  Schweizerischen Unfallversicherungsanstalt (SUVA) ausbezahlten Invalidenrente um eine mit  einer Geldleistung aus einer inländischen gesetzlichen Unfallversorgung gleichartige ausländi- sche Leistung im Sinne des § 3 Abs. 1 Z 4 lit. c EStG 1988 handelt, ist durch das Erkenntnis des  2 von 3 Seite 3 von 3

**False Positives:**

- `SUVA` — partial — pred is substring of gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schweizerischen Unfallversicherungsanstalt (SUVA)`(organisation)

</details>

---

## `OECD` 💣

**F1:** 0.004 | **Precision:** 0.550 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `fffd7778`  
**Description:**
Matches the Organisation for Economic Co-operation and Development (OECD).

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.550 | 0.002 | 0.004 | 20 | 11 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 9 | 5032 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_108`)


Das Finanzamt vertrat im Verfahren vor dem BFG folgenden Standpunkt:  Unter Hinweis auf die Einbehaltung von Quellensteuer und auf das Erkenntnis des BFG vom  18.08.2017, RV/1100136/2015, vertrat es die Ansicht, dass Personen, die nur mit Einkünften  aus Quellen dieses Staates steuerpflichtig seien, demnach auch im Hinblick auf Art. 4 Abs. 1, 2.  Satz OECD-Musterabkommen nicht als in diesem Staat ansässig zu werten seien.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_117`)


OECD 1995, Tz. 2.8).

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_179`)


… Wassermayer (OECD  Musterabkommen - Kommentar 2. Auflage, MA Art. 1, Rz 21, S. 140) sieht die Prüfung der  Ansässigkeit des Ortes der Geschäftsleitung als Vorfrage für die weitere zwischenstaatliche  Beurteilung.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_127`)


Sie ist somit  gleichermaßen auf innerstaatliche wie auf zwischenstaatliche Sachverhalte ausgerichtet und  zielt – im Lichte aktueller internationaler Entwicklungen (BEPS Aktionsplan der OECD,  Empfehlungen der Code of Conduct-Gruppe der EU) – auch auf die Vermeidung konzerninterner  Gewinnverlagerungen mittels Zins- und Lizenzzahlungen in Niedrigsteuerländer oder in  besondere Steuerregime ab.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_128`)


Aufgrund dieses weiten Anwendungsbereiches steht die Regelung  im Einklang mit zwischenstaatlichen (Art. 24 der Doppelbesteuerungsabkommen, dem OECD- MA folgend) und unionsrechtlichen Regelungen (Unionsfreiheiten, Richtlinie des Rates vom 3.  Juni 2003 über eine gemeinsame Steuerregelung für Zahlungen von Zinsen und Lizenzgebühren  zwischen verbundenen Unternehmen verschiedener Mitgliedstaaten (2003/49/EG);

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_167`)


Sie ist somit gleichermaßen auf innerstaatliche wie auf zwischenstaatliche  Sachverhalte ausgerichtet und zielt – im Lichte aktueller internationaler Entwicklungen (BEPS  Aktionsplan der OECD, Empfehlungen der Code of Conduct-Gruppe der EU) – auch auf die  Vermeidung konzerninterner Gewinnverlagerungen mittels Zins- und Lizenzzahlungen in  Niedrigsteuerländer oder in besondere Steuerregime ab.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_260`)


Nach den Ausführungen in den Erläuternden Bemerkungen war schließlich zu prüfen, ob eine  Rechtfertigung aufgrund des Verweises auf aktuelle internationale Entwicklungen (BEPS- Aktionsplan der OECD, Empfehlungen der Code of Conduct-Gruppe der EU) möglich ist.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_261`)


Mit dem Erlass des Abzugsverbots handelte Österreich gegen die Handlungsempfehlung der  OECD.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_262`)


Die inländische Bestimmung des § 12 Abs. 1 Z 10 KStG 1988 erging als unilaterale  Maßnahme, ohne den Abschlussbericht der OECD abzuwarten.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_263`)


Die österreichische Regelung  entspricht auch nicht den empfohlenen Maßnahmen des Abschlussberichts der OECD zum  Aktionspunkt 4, weshalb nach Ansicht des Richters eine diesbezügliche Rechtfertigung nicht in  Frage kommt.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_168`)


Österreich verfügt über kein Doppelbesteuerungsabkommen mit Peru, weshalb keine dem  OECD Musterabkommen, Artikel 7, vergleichbare Regelung zur Abgrenzung des  Besteuerungsrechts des Betriebstättenergebnisses angewendet werden kann.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_73`)


Entscheidend ist nach Art 4/13 OECD-MK, dass die ständige Wohnstätte  natürlichen Personen jederzeit zur Verfügung steht und nicht gelegentlich für Aufenthalte, die  ihrem Anlass nach notwendigerweise nur von kurzer Dauer sein können (vgl. Tumpel/Luketina  in Aigner/Tumpel, DBA-Kommentar, Art 4 Rz 31f.).

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_139`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

**False Positives:**

- `OECD` — no gold match — likely missing annotation
- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `SUVA`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_168`)


Aufgrund dieses weiten  Anwendungsbereiches steht die Regelung im Einklang mit zwischenstaatlichen (Art. 24 der  Doppelbesteuerungsabkommen, dem OECD-MA folgend) und unionsrechtlichen Regelungen  (Unionsfreiheiten, Richtlinie des Rates vom 3. Juni 2003 über eine gemeinsame Steuerregelung  für Zahlungen von Zinsen und Lizenzgebühren zwischen verbundenen Unternehmen  verschiedener Mitgliedstaaten (2003/49/EG); zu letzterer EuGH vom 21.7.2011, Rs Scheuten  Solar Technology GmbH, Rs C-397/09).“

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_43`)


Damit ist als Zwischenergebnis  bereits feststehend, dass das Engagement der Tamara Gottschalch  in Peru Betriebsstätten sowohl im  Sinne des § 29 BAO als auch im Sinne des Art 5 OECD-MA darstellen.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tamara Gottschalch`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_47`)


Tatsächlich ist die Erfüllung des Betriebsstättenbegriffes weder im Verständnis des Art 5 OECD- MA noch im Verständnis des § 29 BAO von einer steuerlichen Registrierung im anderen Staat  abhängig.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_114`)


Es wurde  argumentiert, dass eine Betriebstätte gem § 29 BAO bzw Art 5 OECD-MA bestanden habe.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_124`)


Bei der Beschwerde vom 22.05.2018, eingebracht am 22.05.2018, wurde vorgebracht, dass von  Seiten der Betriebsprüfung die Existenz einer Betriebstätte in Peru nicht in Frage gestellt  würde, weshalb als Zwischenergebnis feststehe, dass eine Betriebstätte der Tamara Gottschalch  in Peru  sowohl im Sinne des § 29 BAO als auch iSd Art 5 OECD-MA bestehe.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tamara Gottschalch`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_169`)


Die Tamara Gottschalch  vertritt in der Beschwerde die Ansicht, dass in Peru eine Betriebstätte iS § 29  BAO als auch im Sinne des OECD-MA bestanden habe.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tamara Gottschalch`(person)

</details>

---

## `Abbreviated Tax Authority` 💣

**F1:** 0.007 | **Precision:** 0.514 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `d6ea78f8`  
**Description:**
Matches 'FA' followed by specific locations, including complex multi-word locations like 'Wien 1/23' or 'Bruck Eisenstadt Oberwart', and 'Österreich'.

**Content:**
```
\bFA(?:\s+Österreich|\s+(?:Wien\s+\d+/\d+|Linz|Braunau\s+Ried\s+Schärding|Kirchdorf\s+Perg\s+Steyr|St\.\s+Veit\s+Wolfsberg|Feldkirch|Salzburg\s+-\s+Land|Neunkirchen|Wr\.\s+Neustadt|Gmunden|Vöcklabruck|Innsbruck|Bruck\s+Eisenstadt\s+Oberwart|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.514 | 0.004 | 0.007 | 37 | 19 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 18 | 5024 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `Dr. Maria-Luise Wohlmayr` (person)
- `Lieselotte Reinicker` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Mag. Karin Pitzer` (person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger` (person)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `UNICONSULT Steuerberatungs GmbH & Co KG` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Nancy Stuckenschneider` (person)
- `Bruno Karahasan` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `12-630/0045` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Karina von Wnuck-Lipinski` (person)
- `Rosemarie Fortwängler` (person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Dr.in Hon.-Prof.in Hilde Hassenzahl` (person)
- `Gwendolin Rittmüller` (person)
- `Matzlröth 29, 3970 Reinprechts, Österreich` (address)
- `10-920/5174` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_19`)


In seinem Vorlageantrag vom 24.8.2021 brachte der Beschwerdeführer weiter vor: „…Das  FA Bruck Eisenstadt Oberwart  übersieht dabei, dass Österreich den Art 168a MwStSyst-RL bisher nicht in das  nationale Umsatzsteuerrecht … transferiert hat … Nach der Judikatur des VwGH stehen bei  Gebäuden eines Unternehmens das nur bis zu maximal 20 % ihrer Nutzfläche privat, im Übrigen  jedoch betrieblich genutzt werden, zwei Optionen zur Wahl … Option 1: voller Vorsteuerabzug  und Besteuerung des Eigenverbrauchs als Nutzungsentnahme mit 20 % USt;

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_22`)


Dies wurde vom BFG mit Erkenntnis … auch so festgestellt. Demnach hat im Jahr  2013 nicht wie im Umsatzsteuerbescheid des FA Bruck Eisenstadt Oberwart  angesetzt, eine Berichtigung der  Vorsteuer gemäß § 12 Abs. 1 UStG in Höhe von EUR 5.284,84 zu erfolgen, sondern muss  vielmehr ein 20 %-iger Eigenverbrauch in Höhe von EUR 1.390,06 (AfA iHv EUR 6.950,25 x 20 %)  angesetzt werden.

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_24`)


Da die Einführung des  Unternehmensserviceportals ohne entsprechende Begleitmaßnahmen, wie Information und  Schulung, dessen Bedienung dem Rechtssuchenden vorgesetzt wurde, ein Zugang und eine  Bedienung ohne Hilfe der Finanzbehörden nicht möglich ist und war, wurde mit  rekommandierten Schreiben vom 23.12.2018 dem FA Wien 1/23  bekanntgegeben, dass der  wirtschaftliche Eigentümer der Dario Kobben  Dr. Karl RA1 ist (siehe beigeschlossenes Schreiben  2 von 16 Seite 3 von 16

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Missed by this rule (FN):**

- `Dario Kobben` (person)
- `Dr. Karl` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_57`)


Beweis: Schreiben an das FA Wien 1/23  vom 23.12.2018, Zeuge1, als Zeugen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_43`)


In den gegenständlichen Beschwerdeverfahren, die vom FA Salzburg-Stadt dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `FA Salzburg-Stadt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ingeborg Brockmayer  in der Beschwerdesache des  Timothy Penzlin, Ötzeltgasse 264, 6252 Kleinsöll, Österreich, betreffend die Beschwerde vom 25. Jänner 2017 gegen den  Haftungsbescheid des FA Innsbruck  vom 21. Dezember 2016 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Dr.in Ingeborg Brockmayer` (person)
- `Timothy Penzlin` (person)
- `Ötzeltgasse 264, 6252 Kleinsöll, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_14`)


Die  Beschwerdevorentscheidung wurde dem Bf. am 2.12.2021 elektronisch durch Einbringung der  Daten in die Databox von Finanzonline zugestellt.  Die elektronische Signatur weist unter der Rubrik Datum/Zeit aus:  2021-12-02T20:22:41+01:00  Mit (undatierten) Schreiben wurde der Vorlageantrag am 5.5.2022 beim FA Österreich  (Briefkasten) eingebracht.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_21`)


Mit Vorlagebricht vom 15.9.2023 legte das FA Österreich die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_33`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Dem Bf. wurde am 2.12.2021 eine Beschwerdevorentscheidung in elektronischer Form  (Finanzonline, Databox) zugestellt.  Der Vorlageantrag wurde beim FA Österreich am 5.5.2022 (Briefkasten) eingebracht.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Bodo Heumaier  in der Angelegenheit der Parteien  KzlR HR Lothar Schoeberl, PLZ1 Stadt1 (Beschwerdeführerin), und FA Braunau Ried Schärding  als Amtspartei über die  Beschwerde vom 25.8.2022   gegen den Bescheid des Finanzamtes vom 4.8.2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016   zu Recht erkannt:  Der bekämpfte Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Mag. Bodo Heumaier` (person)
- `KzlR HR Lothar Schoeberl` (person)
- `Finanzamtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

| Predicted | Gold |
|---|---|
| `FA Feldkirch` | `FA Feldkirch` |

**Missed by this rule (FN):**

- `FA Spittal Villach` (organisation)
- `RHO Pharma` (organisation)
- `RHO Pharma` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146116.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146116.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Thomas Bäckert  in der Beschwerdesache Dr. Quentin Tessier,  Krottenhofweg 115, 4364 Großmaseldorf, Österreich, betreffend Beschwerde vom 18. Juni 2023 gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 15. Mai 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  Steuernummer 71-981/5443  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Dr. Thomas Bäckert` (person)
- `Dr. Quentin Tessier` (person)
- `Krottenhofweg 115, 4364 Großmaseldorf, Österreich` (address)
- `71-981/5443` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146422.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Elmira Walkenbach  in der Beschwerdesache der  JLFT Robotik, Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich, über die am 8.August 2023 eingebrachte Beschwerde gegen den  zur Steuernummer 38-455/9315  ergangenen Bescheid des FA Innsbruck  vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Elmira Walkenbach` (person)
- `JLFT Robotik` (organisation)
- `Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich` (address)
- `38-455/9315` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Yussuf Klingler  in der Beschwerdesache Volkmar Kircher vertreten  durch StB über die Beschwerde vom 18. Juli 2023 gegen die Bescheide des FA Braunau Ried Schärding  vom  27. Juni 2023 betreffend Feststellungstellungsbescheid Gruppenträger für die Jahre von 2018  bis 2020, Steuernummer 08-081/0335  zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Dr. Yussuf Klingler` (person)
- `Volkmar Kircher` (person)
- `08-081/0335` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_14`)


Im Dezember 2006 legte die B KEG ua Berufungen gegen die an sie adressierten „Bescheide“  des FA Wien 8/16/17  vom 1.12.2006 betreffend Einkünftefeststellung gem. § 188 BAO für die Jahre  1988 – 2001 sowie gegen die an sie und an die Kommanditisten adressierten „Bescheide“ des  Finanzamt Wien 8/16/17  vom 28.11.2006 betreffend Unterbleiben der Feststellungen von Einkünften in  Bezug auf die Kommanditisten für den Zeitraum 1998 – 2001 ein.

**False Positives:**

- `FA Wien 8/16` — partial — pred is substring of gold: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 8/16/17`(organisation)
- `Finanzamt Wien 8/16/17`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_67`)


Die Änderung erfolgte aufgrund der bescheidmäßigen  Feststellung des FA Wien 8/16/17  zu StNr **** (Beteiligung B) vom 28.11.2006.

**False Positives:**

- `FA Wien 8/16` — partial — pred is substring of gold: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 8/16/17`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_438`)


Berufungsentscheidung UFS 2.02.2012, GZ. RV/1022 bis 1026-W/10  Mit der Berufungsentscheidung des Unabhängigen Finanzsenates UFS 2.02.2012, GZ. RV/1022  bis 1026-W/10, wurde die Beschwerde gegen die Bescheide des FA Wien 9/18/19  Klosterneuburg vom 30. Oktober 2009 betreffend Umsatzsteuer für das Jahr 2002,  Umsatzsteuer und Körperschaftsteuer jeweils für die Jahre 2003 bis 2005, Wiederaufnahme  der Verfahren gemäß § 303 Abs. 4 BAO hinsichtlich der Umsatzsteuer für die Jahre 2002 bis  2004, Körperschaftsteuer für die Jahre 2003 bis 2004, samt den die Jahre 2003 bis 2005  betreffenden Haftungs- und Abgabenbescheiden des FA Wien 9/18/19 Klosterneuburg vom  30.10.2009 als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 9/18` — partial — pred is substring of gold: `FA Wien 9/18/19  Klosterneuburg`
- `FA Wien 9/18` — similar text (different position): `FA Wien 9/18/19  Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 9/18/19  Klosterneuburg`(organisation)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

**False Positives:**

- `FA Wien 8/16` — partial — pred is substring of gold: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ute Gspan`(person)
- `OMedR Ottfried Theißl`(person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich`(address)
- `FA Wien 8/16/17`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_80`)


Hr. BfA sei damals sogar persönlich beim Finanzamt (damaliges FA Wien  6/7/15) vorstellig geworden.

**False Positives:**

- `FA Wien  6/7` — partial — pred is substring of gold: `FA Wien  6/7/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `FA Wien  6/7/15`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 9/18` — partial — pred is substring of gold: `FA Wien 9/18/19  Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alois Kleynsteuber`(person)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich`(address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`(organisation)
- `FA Wien 9/18/19  Klosterneuburg`(organisation)
- `79-708/0061`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Abigail Dausener  in der Beschwerdesache HR OSR Samir Fatthauer,  Viehdorferstraße 27, 4192 Steinschild, Österreich, über die Beschwerde vom 16. Februar 2023 gegen die Bescheide des FA Wien 2/20/21/22  vom 11. Jänner 2023 betreffend Abweisung von Anträgen auf Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Einkommensteuer 2016 zu Recht erkannt:   I.)

**False Positives:**

- `FA Wien 2/20` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof.in Mag.a Abigail Dausener`(person)
- `HR OSR Samir Fatthauer`(person)
- `Viehdorferstraße 27, 4192 Steinschild, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_81`)


Die Beurteilung des FA Neunkirchen Wr. Neustadt in den Feststellungsbescheiden wird daher  als zutreffend angenommen.

**False Positives:**

- `FA Neunkirchen` — partial — pred is substring of gold: `FA Neunkirchen Wr. Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Neunkirchen Wr. Neustadt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_83`)


Im Jahr 2008 wurde am 9. Dezember 2008 im Rahmen der Ermittlungen zum  Feststellungsbescheid 2000 bis 2007 ein Ergänzungsersuchen des FA Neunkirchen Wiener  Neustadt an Müter u. Barkholt Software GmbH und Mitges.

**False Positives:**

- `FA Neunkirchen` — partial — pred is substring of gold: `FA Neunkirchen Wiener  Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Neunkirchen Wiener  Neustadt`(organisation)
- `Müter u. Barkholt Software GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Kimberly Willomeit  in der Beschwerdesache des  Christoph Hermsen, Krehmen 64, 4760 Riedlhof, Österreich, über die Beschwerde vom 14. Juli 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 22. Juni 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  zu Steuernummer 53-856/2225  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Gmunden` — partial — pred is substring of gold: `FA Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Kimberly Willomeit`(person)
- `Christoph Hermsen`(person)
- `Krehmen 64, 4760 Riedlhof, Österreich`(address)
- `FA Gmunden Vöcklabruck`(organisation)
- `53-856/2225`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_5`)


Gegen diesen Bescheid brachte der Beschwerdeführer Jason Oberbüscher  am 11. April 2023 das  Rechtsmittel der Beschwerde ein und führte begründend aus, dass seine   „unter Pkt. 2 angeführte Einkünfte von der ‚FA Linz  RS AG‘ keine Einkünfte aus Lohn- oder  selbstständiger Arbeit seien.

**False Positives:**

- `FA Linz` — partial — pred is substring of gold: `‚FA Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jason Oberbüscher`(person)
- `‚FA Linz`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 1. April 2022 zuständigen Richter Dr. Hans Blasina  in der Beschwerdesache Uwe Gudian, Tschrestal 27, 4150 Rohrbach, Österreich, über die Berufungen (nunmehr  Beschwerden, § 323 Abs 38 BAO) (1.) vom 15. Jänner 2013 gegen die Bescheide des FA Wien  9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich, § 323b BAO) vom 20. Dezember 2012  betreffend Feststellung und Nichtfeststellung von Einkünften 2009-2010 und gegen die  „Bescheide“ vom 19. Dezember 2012 betreffend Feststellung und Nichtfeststellung von  Einkünften sowie (2.) vom 24. Juli 2013 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg (nunmehr Finanzamt Österreich, § 323b BAO) vom 20. Juni 2013 betreffend  Feststellung und Nichtfeststellung von Einkünften 2011 und gegen den „Bescheid“ vom 27. Juni  2013 betreffend Feststellung von Einkünften 2011, Steuernummer 37-861/1218  zu Recht  erkannt:   I. zu Recht erkannt: Die angefochtenen Bescheide vom 20. Dezember 2012 sowie jener vom 20.  Juni 2013 werden gemäß § 279 BAO abgeändert.

**False Positives:**

- `FA Wien  9/18` — partial — pred is substring of gold: `FA Wien  9/18/19 Klosterneuburg`
- `FA Wien 9/18` — partial — pred is substring of gold: `FA Wien 9/18/19  Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hans Blasina`(person)
- `Uwe Gudian`(person)
- `Tschrestal 27, 4150 Rohrbach, Österreich`(address)
- `FA Wien  9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `FA Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `37-861/1218`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/143486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143486.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde des Danielle Conraths, Rollfährestraße 2I, 4132 Atzesberg, Österreich, vom 8. Mai 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 12. April 2022 betreffend Zahlungserleichterungen § 212 BAO 2022 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Gmunden` — partial — pred is substring of gold: `FA Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Daniela Regina Denk`(person)
- `Danielle Conraths`(person)
- `Rollfährestraße 2I, 4132 Atzesberg, Österreich`(address)
- `FA Gmunden Vöcklabruck`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Erhard Gruetter  in der Beschwerdesache René Kleser,  Dauerkleingärten 17M, 5112 Gresenberg, Österreich, vertreten durch Mag. Andreas Schnegg, Kalkofenstraße 24, 6425 Haiming, über  die Beschwerde vom 19. Februar 2022 gegen den Bescheid des FA Wien 8/16/17  vom 21. Jänner 2022  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer  85-777/9690, zu Recht erkannt:  I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `FA Wien 8/16` — partial — pred is substring of gold: `FA Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Erhard Gruetter`(person)
- `René Kleser`(person)
- `Dauerkleingärten 17M, 5112 Gresenberg, Österreich`(address)
- `Mag. Andreas Schnegg`(person)
- `FA Wien 8/16/17`(organisation)
- `85-777/9690`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Gerda Höfelmair  in der Beschwerdesache des  Ingolf Hillbig, über die Beschwerde vom 11. Jänner 2023 gegen den Bescheid des FA Wien 2/20/21/22  vom  15. Dezember 2022 betreffend Einkommensteuer 2021 zu Steuernummer 92-987/6769  nach der  mündlichen Verhandlung am 5. September 2024 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 2/20` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Gerda Höfelmair`(person)
- `Ingolf Hillbig`(person)
- `FA Wien 2/20/21/22`(organisation)
- `92-987/6769`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Xenia Oelschlagel, BSc, Franz-Adelpoller-Hof 124, 4932 Ried, Österreich, vom 2. Juli 2019 gegen den Bescheid des  FA Wien 2/20/21/22  vom 4. Juni 2019 betreffend Haftungsbescheid / Sonstige 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `FA Wien 2/20` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Daniela Regina Denk`(person)
- `Xenia Oelschlagel, BSc`(person)
- `Franz-Adelpoller-Hof 124, 4932 Ried, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

</details>

---

## `Single Letter Company GmbH` 💣

**F1:** 0.002 | **Precision:** 0.188 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `f369b88c`  
**Description:**
Matches single letter company names like 'X GmbH' which are common placeholders in legal texts.

**Content:**
```
\b[A-Z]\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.188 | 0.001 | 0.002 | 32 | 6 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 26 | 5037 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_56`)


Seit 1.10.2014 ist der BF bei der X GmbH (ab 1.10.2018 Imkeller Möbel GmbH  in Z als Dienstnehmer  beschäftigt (im Steuerakt einliegende Lohnzettel), und zwar in einem unbefristeten  Dienstverhältnis.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Missed by this rule (FN):**

- `Imkeller Möbel GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_30`)


Rückzahlung der AMS-Leistungen vom 2017 10.994,51€  Rückzahlung der WGKK-Leistungen vom 2017 2.440,10 €  Rückzahlung der AMS-Leistungen vom 2018 12.839,94€  Rückzahlung der WGKK-Leistungen vom 2018 337,86 €  1) Werbungskosten gemäß § 16 EStG  Unbestritten sei es Tatsache, dass die Bf. März 2016 mit der Wirkung 30.06.2016 von ihrer  Arbeitgeberin X GmbH gekündigt wurde.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Missed by this rule (FN):**

- `AMS` (organisation)
- `WGKK` (organisation)
- `AMS` (organisation)
- `WGKK` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_33`)


Seit diesem Zeitpunkt arbeite sie ununterbrochen und mit aufrechtem Dienstverhältnis für ihre  bisherige Arbeitgeberin Firma X GmbH weiter.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_51`)


Zusammenfassend bedeute das aber für den vorliegenden Fall, dass aufgrund der erfolgreichen  Kündigungsanfechtung und rückwirkender Aufhebung der Kündigung die Bf. ununterbrochen  ein aufrechtes Dienstverhältnis mit der Firma X GmbH gehabt habe und somit niemals  arbeitslos gewesen sei.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_172`)


Im Jahr 2016 wurde  die Bf. von ihrer Arbeitgeberin X GmbH per 30.06. gekündigt.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_24`)


Zum  Kauf des Motorschlittens wird der Beleg vom 1.10.2015 über den Kauf von Herrn *Name3*,  Bilder vom Skidoo und vom Anhänger sowie über den Verkauf dieses Skidoos am 23.01.2018  an die Firma *C GmbH*, *Straße6* übersendet.

| Predicted | Gold |
|---|---|
| `C GmbH` | `C GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_327`)


der Verrechnung Nieder Waldbach GmbH um Vorlage von Unterlagen als Nachweis für die  falsche Berechnung zwischen den beiden Betrieben ersucht worden sei; b) dies(e) Behauptung  "Kalkulationsdifferenzen können mit Verrechnung B GmbH erklärt werden" einen glatten  Widerspruch zu den Gegenargumenten zur Kalkulation darstelle;

**False Positives:**

- `B GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_164`)


Nicht ausreichend sind nach der Judikatur beispielsweise Zusätze wie „S GmbH  und Mitges“, „S GmbH und Mitgesellschafter“ (VwGH 17.10.2001, 96/13/0058) bzw. „Firma X  Immobilienverw und Mitges“ und „(Erstbeschwerdeführer) & atyp stille Gesellschaft“ (VwGH  02.08.2000, 99/13/0014).

**False Positives:**

- `S GmbH` — no gold match — likely missing annotation
- `S GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_194`)


GmbH und Mitges“, „S GmbH und Mitgesellschafter“ (VwGH 17.10.2001, 96/13/0058) bzw.  „Firma X Immobilienverw und Mitges“ und „(Erstbeschwerdeführer) & atyp stille Gesellschaft“  (VwGH 02.08.2000, 99/13/0014) im Adressfeld als nicht ausreichend angesehen werden um  einen individuellen Verwaltungsakt zu setzten, muss dies umso mehr für den gegenständlichen  Fall Gültigkeit besitzen, in dem sich im Adressfeld überhaupt kein Hinweis auf den Bestand  einer (atypisch) stillen Gesellschaft findet.

**False Positives:**

- `S GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_139`)


Erweise sich der  Begründungsmangel auch als relevant für den Verfahrensausgang (Vorsteuerabzug aus den  Rechnungen der M GmbH) habe dieser zur Folge, dass dem Verwaltungsgerichtshof die  inhaltliche Prüfung des Erkenntnisses verwehrt bleibe und daher führe der  Begründungsmangel zu dessen Aufhebung.

**False Positives:**

- `M GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_824`)


4. VwGH-Judikatur:  a) VwGH 25.6.2007, 2006/14/0107 (EMAG-Folgeentscheidung):  Zusammengefasst geht es um ein Liefergeschäft von den Niederlanden (Erstverkäufer) an die  österreichische Zwischenhändlerin (K GmbH), die die Waren letztlich an die österreichische  Abnehmerin (Bf.) verkaufte.

**False Positives:**

- `K GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_843`)


Wie sich aus dem schon eingangs erwähnten Erkenntnis vom heutigen Tag, Ro 2018/15/0011,  auf dessen Entscheidungsgründe insoweit gemäß § 43 Abs. 2 VwGG verwiesen wird, ergibt,  erweist sich der Begründungsmangel auch als relevant für den Verfahrensausgang  (Vorsteuerabzug aus den Rechnungen der M GmbH).

**False Positives:**

- `M GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_59`)


Mit Beschluss vom 28. September 2021 seitens des nunmehr zuständigen Richters wurde der  Beschwerdeführer aufgefordert, weitere Informationen bzw. Unterlagen vorzulegen:   < Entwicklung des Krankenverlaufes   < Einschränkung der Erwerbstätigkeit   < Kostenersätze  Mit Eingabe vom 12. Oktober 2021 wurde diesbezüglich ausgeführt, dass beispielsweise die  F GmbH, deren alleiniger Mitarbeiter der Beschwerdeführer sei, den Gewinn nach der  Genesung des Beschwerdeführers erheblich steigern hätte können (von rd. 11.000,00 € im Jahr  2019 auf rd. 73.000,00 €).

**False Positives:**

- `F GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_49`)


bis  21.09.2011 mit dem Kennzeichen W1 auf die T GmbH und ab 21.09.2011 mit dem Kennzeichen  K2 auf den BF zuglassen.

**False Positives:**

- `T GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_9`)


Krankenpflege in der Fachhochschule D GmbH (kurz: FH Sbg) anzumelden, habe sie sich für den  ehest möglichen Aufnahmetermin beworben und dieser sei nicht früher möglich gewesen, als  für das Sommersemester ab März 2021 (zuvor sei das Aufnahmeprozedere erfolgt).

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_4`)


Sachverhalt  Auf Grundlage der Feststellungen einer Außenprüfung wurden gegenüber der Gartfentri Heizung Institut GmbH  in Liquidation, Untere Siedlungsgasse 43, 3903 Echsenbach, Österreich (A GmbH) nach Wiederaufnahme der Verfahren neue  Umsatzsteuerbescheide vom 28. November 2018 für 2012 bis 2015 erlassen.

**False Positives:**

- `A GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gartfentri Heizung Institut GmbH`(organisation)
- `Untere Siedlungsgasse 43, 3903 Echsenbach, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_4`)


Aufgrund der  Feststellungen im Rahmen dieser Außenprüfung wurden die Veranlagungsjahre 2015 bis 2017  von der belangten Behörde durch die verfahrensgegenständlichen Bescheide  wiederaufgenommen und die Körperschaftsteuer insofern neu festgesetzt, als die  Fremdleistungen durch die Subunternehmen Trafen-Pflege GmbH  H OG, L GmbH,LSR Recycling GmbH  R GmbH und S  GmbH gem. § 162 BAO (Empfängerbenennung) nicht zum Abzug zugelassen wurden.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation
- `S  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Trafen-Pflege GmbH`(organisation)
- `LSR Recycling GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_144`)


Der steuerliche Vertreter der beschwerdeführenden Gesellschaft merkte an, dass hinsichtlich  der L GmbH Anmeldedaten der Arbeitnehmer sehr wohl dokumentiert worden seien.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_146`)


Insbesondere sei schon im Rahmen der  BVE darauf hingewiesen worden, dass die belangte Behörde vermute, dass die L GmbH als  Anmeldevehikel gedient habe.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_170`)


In der Belegsammlung der beschwerdeführenden Gesellschaft scheinen Rechnungen folgender  Subunternehmen auf:  F GmbH:  10 von 15 Seite 11 von 15

**False Positives:**

- `F GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_171`)


62.325,- Euro für den Zeitraum 02-05/2016  H OG:  114.209, Euro für den Zeitraum 03-08/2017  L GmbH:  25.390,40 Euro für den Zeitraum 10-11/2016  M GmbH:  161.440,40 Euro für den Zeitraum 04-12/2015  R GmbH:  1.373,31 Euro für den Zeitraum 12/2017  S GmbH:  99.929,60 Euro für den Zeitraum 05-12/2016  4.268,- Euro für den Zeitraum 01/2017  Die beschwerdeführende Gesellschaft ließ hinsichtlich dieser Subunternehmer die übliche  Sorgfalt im Bereich des Bauwesens nicht walten.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation
- `M GmbH` — no gold match — likely missing annotation
- `R GmbH` — no gold match — likely missing annotation
- `S GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_188`)


Auch die Dokumentation der Anmeldung von zwei Mitarbeitern bei der L GmbH führt zu  keiner anderen Beurteilung, da aufgrund der mangelnden Dokumentation durch die  beschwerdeführende Gesellschaft durch Bautagebücher etc. ungewiss geblieben ist, ob und in  welchem Umfang diese Beschäftigten tatsächlich an den beauftragten Projekten beteiligt  gewesen sind.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_23`)


Der Bf. war  - vom xx.xx.xxxx-xx.xx.xxxx bei der Traal E‑Commerce Dienstleistungen GmbH (FN xxxxx) in AdresseCGmbH,  - vom xx.xx.xxxx-xx.xx.xxxx bei der D GmbH (FN xxxxx) in AdresseDGmbH,  - vom xx.xx.xxxx-xx.xx.xxxx bei der E GmbH (FN xxxxx) in AdresseCGmbH und  - vom xx.xx.xxxx-xx.xx.xxxx bei der Bimbös&Döppenbecker Energie GmbH (FN xxxxx; vormals F_alt GmbH) in  AdresseFGmbH  je als Angestellter beschäftigt.

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation
- `E GmbH` — similar text (different position): `Bimbös&Döppenbecker Energie GmbH`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Traal E‑Commerce Dienstleistungen GmbH`(organisation)
- `Bimbös&Döppenbecker Energie GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_24`)


Weiters hatte er in der Zeit vom   - xx.xx.xxxx-xx.xx.xxxx bei der Traal E‑Commerce Dienstleistungen GmbH  - xx.xx.xxxx-xx.xx.xxxx bei der Bimbös&Döppenbecker Energie GmbH  - xx.xx.xxxx-xx.xx.xxxx bei der E GmbH sowie  - xx.xx.xxxx-xx.xx.xxxx bei der Nord Zorwaldstein GmbH (FN xxxxx)  je die Funktion des handelsrechtlichen Geschäftsführers inne.

**False Positives:**

- `E GmbH` — similar text (different position): `Bimbös&Döppenbecker Energie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traal E‑Commerce Dienstleistungen GmbH`(organisation)
- `Bimbös&Döppenbecker Energie GmbH`(organisation)
- `Nord Zorwaldstein GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/148420.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148420.1_72`)


Der Beschwerdeführer erwarb zwei sogenannte „Wetterderivate“ von der H GmbH und  bezahlte dafür am 8.1.2008 EUR 36.940,00.

**False Positives:**

- `H GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/148420.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148420.1_73`)


Im Jahr 2008 erhielt der Beschwerdeführer aus  diesen „Wetterderivaten“ von der H GmbH Zahlungen von insgesamt EUR 110.000,00.

**False Positives:**

- `H GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Suffix GmbH & Partner KG` 💣

**F1:** 0.005 | **Precision:** 0.167 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `d6f689ff`  
**Description:**
Matches compound company names ending in 'GmbH & Partner KG' or similar variations to prevent splitting.

**Content:**
```
\b[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+(?:\s+GmbH\s+&\s+Partner\s+KG|\s+GmbH\s+&\s+Co\.?\s+KG|\s+KG\s+&\s+Partner\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.003 | 0.005 | 84 | 14 | 70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 70 | 5029 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Astoria Stb GmbH & Co KG` | `Astoria Stb GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- `Leroy Sitterle` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_64`)


Auch warum aus dem Umstand, die Burglechner Touristik GmbH & Co KG sei ab dem  zweiten Halbjahr 2012 nicht mehr an der im Firmenbuch angegebenen Adresse befindlich  gewesen, der Schluss gezogen wird, dass dadurch ein tatsächlicher Leistungsaustausch  unmöglich gewesen sei, ist keineswegs nachvollziehbar.

| Predicted | Gold |
|---|---|
| `Burglechner Touristik GmbH & Co KG` | `Burglechner Touristik GmbH & Co KG` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_222`)


Steuerliche Auswirkungen  Zeitraum 2012 Körperschaftsteuer: Bilanzgewinn/Bilanzverlust 9.785,00  Tz. 8 Subfirma -Burglechner Touristik GmbH & Co KG  Im Belegordner "Subunternehmen" der Firma Starnberg Beratung GmbH liegen gezählt dreiunddreißig (33) im  Namen der WienElektro GmbH & Co KG geschriebene Eingangsrechnungen zuzüglich ebensovielen  Kassa-Eingang Belegen vor.

| Predicted | Gold |
|---|---|
| `Burglechner Touristik GmbH & Co KG` | `Burglechner Touristik GmbH & Co KG` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)
- `WienElektro GmbH & Co KG` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_237`)


Denn  hätte er dies getan, so hätte er erkennen müssen, dass der Geschäftspartner, die WienElektro GmbH & Co KG  nicht existiert.

| Predicted | Gold |
|---|---|
| `WienElektro GmbH & Co KG` | `WienElektro GmbH & Co KG` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `UNICONSULT Steuerberatungs GmbH & Co KG` | `UNICONSULT Steuerberatungs GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mag. Karin Pitzer` (person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger` (person)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `FA Braunau Ried Schärding` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_35`)


folgende Stellungnahme abzugeben:  Ehepaar D, Kinder von Y und Z D, Baumschule D erwarben mit Kaufvertrag vom 10.9.2012 von  der M Containerbaumschule GmbH & Co KG die ehemalige Betriebsliegenschaft samt  Folienhäuser, Folientunnel und Teile der Bewässerungsanlagen.

| Predicted | Gold |
|---|---|
| `M Containerbaumschule GmbH & Co KG` | `M Containerbaumschule GmbH & Co KG` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG` | `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG` |

**Missed by this rule (FN):**

- `Violetta Bailmann` (person)
- `Schlosserfeld 35, 9632 Hochwart, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)
- `82-877/4906` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Rein & Partner Steuerberatung GmbH & Co KG` | `Rein & Partner Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mag. Albert Salzmann` (person)
- `Denis Diekötter` (person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_34`)


a) Sachverhalt:  …  b) Steuerliche Würdigung:  Bei den angeführten „Modellentwicklungsaufwendungen“ handelt es sich um von der AbisJ  GmbH & Co KG an Dritte geleistete Ausgaben.

| Predicted | Gold |
|---|---|
| `AbisJ  GmbH & Co KG` | `AbisJ  GmbH & Co KG` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_37`)


Die  einzelnen Aufwendungen für die Modellentwicklung sind daher im Betrieb der steuerlichen  Mitunternehmerschaft AbisJ als Betriebsausgabe zur berücksichtigen und nicht anteilig bei den  einzelnen „Zielgesellschaften“, an denen sich die AbisJ GmbH & Co KG als atypisch stille  Gesellschafterin beteiligt.

| Predicted | Gold |
|---|---|
| `AbisJ GmbH & Co KG` | `AbisJ GmbH & Co KG` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG` | `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mag. Albert Salzmann` (person)
- `Ing. Marion Kloefkorn` (person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich` (address)
- `40-620/0106` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Armin Treichl, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter Mag. Eva-Maria Düringer und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin Isabella Längle zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG` | `Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mag. Armin Treichl` (person)
- `Dr.  Roman Galehr` (person)
- `Mag. Eva-Maria Düringer` (person)
- `Mag. Tino  Ricker` (person)
- `Dirk Hironymus` (person)
- `Am See IV 25, 3071 Hinterholz, Österreich` (address)
- `RHO Pharma` (organisation)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)
- `63-114/3997` (tax_number)
- `Isabella Längle` (person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146667.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146667.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Istvan  Kempfer  in der Beschwerdesache Anselm Arnhölter,  Neufahrner Straße 6, 3744 Mold, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG, Muthgasse 109, 1190 Wien, über die Beschwerde vom 6. Juni 2024 gegen den Bescheid  des Finanzamtes Österreich vom 26. Mai 2023 betreffend Einkommensteuer 2022 zu  Steuernummer 17-947/8635  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG` | `TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG` |

**Missed by this rule (FN):**

- `Priv.-Doz. Istvan  Kempfer` (person)
- `Anselm Arnhölter` (person)
- `Neufahrner Straße 6, 3744 Mold, Österreich` (address)
- `17-947/8635` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Karl Konstandin  in der Beschwerdesache Barbara West,  Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG, Landstraße 9, 4020  Linz, über die Beschwerde vom 27.11.2024 gegen den Bescheid des Finanzamtes Österreich  vom 6.11.2024 betreffend Abweisung eines Antrages auf bescheidmäßige Festsetzung des  Energiekrisenbeitrages-Strom (EKB-S) für den Zeitraum Jänner 2024 bis Juni 2024 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `BEURLE Rechtsanwälte GmbH & Co KG` | `BEURLE Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Univ.-Prof. Karl Konstandin` (person)
- `Barbara West` (person)
- `Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf.) ist die Komplementärin Charles Rybalka  in einer GmbH & Co. KG.

**False Positives:**

- `Komplementärin Charles Rybalka  in einer GmbH & Co. KG` — partial — gold is substring of pred: `Charles Rybalka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Charles Rybalka`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_10`)


Aufgrund der außerordentlichen Revision der GmbH & Co. KG gegen das Erkenntnis des  BFG vom 15.09.2016, Zl. RV/7102261/2011, betreffend u.a. Umsatzsteuer für das Jahr  2009, mit dem die Beschwerde gegen den Umsatzsteuerbescheid 2009 als unbegründet  abgewiesen wurde, erging das Erkenntnis des Verwaltungsgerichtshofs vom 21.02.2018, Ra  2016/13/0052-6, mit dem das angefochtene Erkenntnis im Umfang der Anfechtung  1 von 10 Seite 2 von 10

**False Positives:**

- `Aufgrund der außerordentlichen Revision der GmbH & Co. KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofs`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_37`)


II. Das Bundesfinanzgericht hat erwogen:  Sachverhalt:  Die Beschwerdeführerin (Bf.) ist die Komplementärin Charles Rybalka  in einer GmbH & Co. KG.

**False Positives:**

- `Komplementärin Charles Rybalka  in einer GmbH & Co. KG` — partial — gold is substring of pred: `Charles Rybalka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Charles Rybalka`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_21`)


– eine Rechnung von memoryking GmbH & Co KG, Berlin, vom 01.12.2018 über ein „deleyCON  2m Optisches Digital Audio Kabel SPDIF – 2x Toslink Stecker Digitalkabel Audiokabel LWL  Digitales Lichtwellenleiter Kabel – Schwarz/Blau“ in Höhe von 6,44 €, (= Rechnung Nr. 13 laut  Auflistung),  – eine Rechnung von amazon.de vom 22.07.2019 (Bestellung vom 17.10.2018) über ein  „Zubehör für Gopro, ccbetter Action Kamerahalterungen für Gopro hero 7 hero 2018 hero 6  Hero 4 Hero 5 Session Hero 1 2 3 3+ für die meisten Sportkameras mit Fall (Schwarz)“ in Höhe  von 19,27 €, (= Rechnung Nr. 14 laut Auflistung),  – eine Rechnung von AfB social & green IT, Ettlingen, vom 30.07.2018 über eine „Logitech 920- 003967 Wireless Combo MK330 – schnurlos Tastatur und Computermaus /2,4 GHz, USB,  QWERTZ deutsches Tastaturlayout) schwarz“ in Höhe von 44 €, (= Rechnung Nr. 15 laut  Auflistung),  – eine Rechnung von Yuanchuang e-business co.LTD., vom 21.05.2018, an C, Adresse2, über  einen „X-Sense CO03D CO Melder Kohlenmonoxid CO-Detektor Batteriebetrieben Sensor und  Alarm mit Digitalanzeige und Höchstwertspeicherung“ in Höhe von 29,99 €, (= Rechnung Nr. 16  laut Auflistung),  – eine Rechnung von SYNCWIRE UK LTD, Manchester, vom 02.04.2018 über ein „DisplayPort  Kabel – 2M Syncwire Vergoldetes DisplayPort zu DisplayPort Kabel High-Speed Auflösung Kabel  unterstützt Fire TV, Apple TV, Ethernet, Aud“ in Höhe von 8,99 €, (= Rechnung Nr. 17 laut  Auflistung),  – eine Rechnung von converter-shop.com, Berlin, vom 16.02.2018 über einen „Bronson++ HE-D  800 – 110 Volt Spannungswandler / Transformator – 800 Watt – In: EURO 220 – 240 Volt / Out:  USA 110 Volt – Ringkerntransformator 800W“ in Höhe von 79,99 €, (= Rechnung Nr. 18 laut  Auflistung),  – eine Rechnung vom RANKEI UK LTD, Manchester, vom 27.09.2018 über ein „Rankie  Verbindungskabel Displayport (DP) auf HDMI, 4K Auflösung Kabel, 1,8 m, Schwarz“ in Höhe von  7,99 €, (= Rechnung Nr. 19 laut Auflistung),  – eine Rechnung vom Hoomil, Shenzhen, vom 24.11.2018, an D, Adresse3, über eine „HOOLIL  Galaxy S7 Hülle, Premium Handy Schutzhülle für Samsung Galaxy S7 Hülle Leder Wallet Tasche  Flip Brieftasche Etui Schale, Schwarz (H3011)“ in Höhe von 12,35 €, (= Rechnung Nr. 20 laut  Auflistung),  – eine Rechnung vom John’s Handy, Wien, vom 27.07.2018, ohne Angabe des Namens und der  Anschrift des Abnehmers der Lieferung, über ein „Samsung galaxy s7 gold SN/IMEI:  356457097886024“ in Höhe von 339 €, (= Rechnung Nr. 21 laut Auflistung),  5 von 18 Seite 6 von 18

**False Positives:**

- `Rechnung von memoryking GmbH & Co KG` — partial — gold is substring of pred: `memoryking GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `memoryking GmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_11`)


Tatsächlich wurden aber Subunternehmer beauftragt, die tatsächlich nicht existent waren, wie  die Firmen Furtnor-Handel GmbH PGIV Umwelt Entwicklung GmbH oder Burglechner Touristik GmbH & Co KG  die wohl Rechnungen ausstellten, die  2 von 29 Seite 3 von 29

**False Positives:**

- `Handel GmbH PGIV Umwelt Entwicklung GmbH oder Burglechner Touristik GmbH & Co KG` — positional overlap with gold: `Furtnor-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnor-Handel GmbH`(organisation)
- `PGIV Umwelt Entwicklung GmbH`(organisation)
- `Burglechner Touristik GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_20`)


Die Burglechner Touristik GmbH & Co KG befand sich ab dem zweiten Halbjahr 2012 nicht mehr an der im  Firmenbuch angegebenen Adresse.

**False Positives:**

- `Die Burglechner Touristik GmbH & Co KG` — partial — gold is substring of pred: `Burglechner Touristik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Burglechner Touristik GmbH & Co KG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_60`)


Grundsätzlich richtig ist zwar, dass der Beschwerdeführer nicht über die erforderlichen  Arbeitskapazitäten verfügte, um die Arbeiten durchführen zu können und daher  Subunternehmer, namentlich u.a. die Furtnor-Handel GmbH  die PGIV Umwelt Entwicklung GmbH und die Burglechner Touristik GmbH & Co KG  beauftragte.

**False Positives:**

- `Handel GmbH  die PGIV Umwelt Entwicklung GmbH und die Burglechner Touristik GmbH & Co KG` — positional overlap with gold: `Furtnor-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnor-Handel GmbH`(organisation)
- `PGIV Umwelt Entwicklung GmbH`(organisation)
- `Burglechner Touristik GmbH & Co KG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

**False Positives:**

- `Burglechner Touristik GmbH & Co KG` — partial — pred is substring of gold: `GmbH;Burglechner Touristik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GmbH;Burglechner Touristik GmbH & Co KG`(organisation)
- `M.`(person)
- `Albert Sengeisen`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_174`)


Sämtlich angeführte Firmen – G. GmbH;PGIV Umwelt Entwicklung GmbH Burglechner Touristik GmbH & Co KG- stehen im Ruf von  Scheinfirmen und werden infolge behördlicher Ermittlungen ob typischer Merkmale hierfür als  Betrugsfirmen am Bau verdächtigt.

**False Positives:**

- `PGIV Umwelt Entwicklung GmbH Burglechner Touristik GmbH & Co KG` — positional overlap with gold: `GmbH;PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GmbH;PGIV Umwelt Entwicklung GmbH`(organisation)
- `Burglechner Touristik GmbH & Co KG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_185`)


Burglechner Touristik GmbH & Co KG  Der Geschäftssitz der WienElektro GmbH & Co KG befand sich seit dem 2.

**False Positives:**

- `Burglechner Touristik GmbH & Co KG  Der Geschäftssitz der WienElektro GmbH & Co KG` — partial — gold is substring of pred: `Burglechner Touristik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Burglechner Touristik GmbH & Co KG`(organisation)
- `WienElektro GmbH & Co KG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_193`)


C. GmbH;Burglechner Touristik GmbH & Co KG überhaupt  diesen zuordenbar sind, oder die Rechnungen von anderweitigen Autoren verfasst wurden, die  in keinem organischen Verhältnis mit den bezüglichen Firmen stehen, darüber lässt sich  letztlich infolge des verdunkelten Sachverhalts nur spekulieren.

**False Positives:**

- `Burglechner Touristik GmbH & Co KG` — partial — pred is substring of gold: `GmbH;Burglechner Touristik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GmbH;Burglechner Touristik GmbH & Co KG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_222`)


Steuerliche Auswirkungen  Zeitraum 2012 Körperschaftsteuer: Bilanzgewinn/Bilanzverlust 9.785,00  Tz. 8 Subfirma -Burglechner Touristik GmbH & Co KG  Im Belegordner "Subunternehmen" der Firma Starnberg Beratung GmbH liegen gezählt dreiunddreißig (33) im  Namen der WienElektro GmbH & Co KG geschriebene Eingangsrechnungen zuzüglich ebensovielen  Kassa-Eingang Belegen vor.

**False Positives:**

- `Namen der WienElektro GmbH & Co KG` — partial — gold is substring of pred: `WienElektro GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Burglechner Touristik GmbH & Co KG`(organisation)
- `Starnberg Beratung GmbH`(organisation)
- `WienElektro GmbH & Co KG`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_225`)


Der Geschäftssitz der WienElektro GmbH & Co KG befand sich seit dem 2.

**False Positives:**

- `Der Geschäftssitz der WienElektro GmbH & Co KG` — partial — gold is substring of pred: `WienElektro GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WienElektro GmbH & Co KG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_233`)


Sämtliche im Namen der Burglechner Touristik GmbH & Co KG an die Firma Starnberg Beratung GmbH ausgestellten Rechnungen  sind als arglistige Scheinrechnungen zu werten.

**False Positives:**

- `Sämtliche im Namen der Burglechner Touristik GmbH & Co KG` — partial — gold is substring of pred: `Burglechner Touristik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Burglechner Touristik GmbH & Co KG`(organisation)
- `Starnberg Beratung GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_242`)


Der mit verfahrensleitender Verfügung am 10.04.2014 - persönlich überreicht am 11.04.2014-  aufgetragenen Nennung der Empfänger von Zahlungen im Zusammenhang mit den Subfirmen Furtnor-Handel GmbH PGIV Umwelt Entwicklung GmbH und Burglechner Touristik GmbH & Co KG wurde nicht im gebotenen Maße entsprochen,  weshalb schätzungsweise anzunehmende Ausgaben für eventuell Honorare an Führer von  Arbeiterpartien, Lohnbefriedigung Schwarzarbeiter, Zahlungen für sonstige Leistungen, etc.  nicht zu berücksichtigen sind.

**False Positives:**

- `Handel GmbH PGIV Umwelt Entwicklung GmbH und Burglechner Touristik GmbH & Co KG` — positional overlap with gold: `Furtnor-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnor-Handel GmbH`(organisation)
- `PGIV Umwelt Entwicklung GmbH`(organisation)
- `Burglechner Touristik GmbH & Co KG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_65`)


Die Bf legte ihrer Beschwerde ferner die Stellungnahme des Fertighausunternehmens „UX  Teich1 Verwaltungs GmbH & Co KG“ vom 12.7.2021 bei.

**False Positives:**

- `Verwaltungs GmbH & Co KG` — partial — pred is substring of gold: `UX  Teich1 Verwaltungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UX  Teich1 Verwaltungs GmbH & Co KG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_136`)


Schreiben des   Fertighauszentrums „UX Teich1“ Verwaltungs GmbH & Co KG vom 12.7.2021).

**False Positives:**

- `Verwaltungs GmbH & Co KG` — partial — pred is substring of gold: `„UX Teich1“ Verwaltungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `„UX Teich1“ Verwaltungs GmbH & Co KG`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_144`)


Schreiben der UX Teich1 Verwaltungs GmbH & Co KG  vom 12.7.2022).

**False Positives:**

- `Verwaltungs GmbH & Co KG` — partial — pred is substring of gold: `UX Teich1 Verwaltungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UX Teich1 Verwaltungs GmbH & Co KG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_2`)


Steinkrafttra Heizung  GmbH & Co KG, Straße3, Ort,  2. STT Umwelt  GmbH & Co KG, Straße3, Ort,   3. Drau-Umwelt Entwicklung  GmbH & Co KG, Straße3, Ort,  4. UnterLemglanzlogHandel  GmbH & Co KG, Straße3, Ort und  5. NordImmobilien  GmbH & Co KG, Straße3, Ort,  alle vertreten durch yy Wirtschaftstreuhand Gesellschaft mbH, Straße2, Ort,  gegen den Bescheid des Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, § 323 b BAO)  vom 11. Dezember 2012 betreffend Feststellung der Einkünfte gemäß § 188 BAO für das Jahr  2010 (der Demircan Metall AG& atypisch stille Gesellschaft) zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`
- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`
- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`
- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`
- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)
- `UnterLemglanzlogHandel`(organisation)
- `NordImmobilien`(organisation)
- `yy Wirtschaftstreuhand Gesellschaft mbH`(organisation)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)
- `Demircan Metall AG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_19`)


den  atypisch stillen Gesellschafterinnen eine Zurechnung folgender Einkünfte beantragt:  1. Steinkrafttra Heizung  GmbH & Co KG:   Sonderbetriebsausgaben in Höhe von -€ 1.123,00,  2.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steinkrafttra Heizung`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_20`)


STT Umwelt  GmbH & Co KG:   2 von 29 Seite 3 von 29

**False Positives:**

- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `STT Umwelt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_22`)


Drau-Umwelt Entwicklung  GmbH & Co KG:    Sonderbetriebsausgaben in Höhe von -€ 6.097,75,  4.

**False Positives:**

- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Drau-Umwelt Entwicklung`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_23`)


UnterLemglanzlogHandel  GmbH & Co KG:   Sonderbetriebsausgaben in Höhe von -€ 7.942,46,  5.

**False Positives:**

- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_24`)


NordImmobilien  GmbH & Co KG:    Verlustzuweisungen in Höhe von -€ 2.470.000,00 und Sonderbetriebsausgaben in Höhe  von -€ 255.101,72.

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_62`)


…“  Mit Bescheid über die Feststellung von Einkünften gem. § 188 BAO für das Jahr 2010 vom 11.  Dezember 2012 wurde den atypisch stillen Gesellschafterinnen Einkünfte wie folgt  zugerechnet:   1. Steinkrafttra Heizung  GmbH & Co KG: € 0,00,  2. STT Umwelt  GmbH & Co KG: € 0,00,  3. Drau-Umwelt Entwicklung  GmbH & Co KG:  € 0,00,  4.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`
- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`
- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_63`)


UnterLemglanzlogHandel  GmbH & Co KG: € 0,00,  5. NordImmobilien  GmbH & Co KG:  ein Betrag von -€ 2.470.000,00 als Verlustzuweisung - wobei  angeführt wurde, dass diese als nicht ausgleichsfähige Verluste (eigener Betrieb) im Betrag  von € 2.470.000,00 bei der Veranlagung der Bf. zu berücksichtigen sind - zugerechnet.

**False Positives:**

- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`
- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)
- `NordImmobilien`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_92`)


1. Sachverhalt   1.1 Gesellschaftsstruktur und -beziehungen – Verträge - Verlustzuweisung  Zu den Bf.:   Steinkrafttra Heizung  GmbH & Co KG: Die stille Gesellschafterin wurde mit Gesellschaftsvertrag vom  3. Juli 2008 gegründet.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steinkrafttra Heizung`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_95`)


Mit Ablauf des Stichtages 31.  März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit  Buchwertfortführung gem. Art IV UmgrStG.   STT Umwelt  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008  gegründet.

**False Positives:**

- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `STT Umwelt`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_98`)


Mit Ablauf des Stichtages 30. September  2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit Buchwertfortführung  gem. Art IV UmgrStG.   Drau-Umwelt Entwicklung  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 15. April 2009  gegründet.

**False Positives:**

- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Drau-Umwelt Entwicklung`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_101`)


Mit Ablauf des Stichtages 31. März 2009  erfolgte rückwirkend ein Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art  IV UmgrStG.   UnterLemglanzlogHandel  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 4. November 2009  gegründet.

**False Positives:**

- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_104`)


Mit Ablauf des Stichtages 30. September  2009 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit Buchwertfortführung  gem. Art IV UmgrStG.   NordImmobilien  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 18. Mai 2010  gegründet.

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_121`)


Zusammenschlüsse in 2010 - Zusammenschlussvertrag – „Errichtung stille Gesellschaft“ –  NordImmobilien  GmbH & Co KG  Die mit Zusammenschlussvertrag vom 23. Dezember 2010 rückwirkend (Stichtag 31.03.2010)  errichtete Demircan Metall AG& atypisch stille Gesellschaft ist auf unbestimmte Zeit errichtet und frühestens  kündbar mit 31. Juni 2016 unter Einhaltung einer sechsmonatigen Frist.

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)
- `Demircan Metall AG`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_140`)


Gesellschaften mit gleicher Beteiligungs- sowie Gesellschafterstruktur, welche im  Prüfzeitraum (2008 bis 2009) an der operativ tätigen Demircan Metall AG als atypisch stille Gesellschafter  beteiligt waren:  2008:    Steinkrafttra Heizung  GmbH & Co KG  11 von 29 Seite 12 von 29

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)
- `Steinkrafttra Heizung`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_141`)


STT Umwelt  GmbH & Co KG   2009:    Steinkrafttra Heizung  GmbH & Co KG   STT Umwelt  GmbH & Co KG   Drau-Umwelt Entwicklung  GmbH & Co KG   UnterLemglanzlogHandel  GmbH & Co KG  Zu den Ausführungen zu den rückwirkend errichteten Zusammenschlussverträgen wird auf die  Ausführungen in der Entscheidung des BFG vom 29.9.2023, RV/1100433/2013 (Steinkrafttra Heizung  GmbH & Co KG und STT Umwelt  GmbH & Co KG) und in der Entscheidung des BFG vom  29.9.2023, RV/1100437/2013 (Drau-Umwelt Entwicklung  GmbH & Co KG und UnterLemglanzlogHandel  GmbH & Co KG)  verwiesen.

**False Positives:**

- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`
- `Steinkrafttra Heizung  GmbH & Co KG   STT Umwelt  GmbH & Co KG` — similar text (different position): `STT Umwelt`
- `Umwelt Entwicklung  GmbH & Co KG   UnterLemglanzlogHandel  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`
- `Steinkrafttra Heizung  GmbH & Co KG und STT Umwelt  GmbH & Co KG` — similar text (different position): `STT Umwelt`
- `Umwelt Entwicklung  GmbH & Co KG und UnterLemglanzlogHandel  GmbH & Co KG` — similar text (different position): `UnterLemglanzlogHandel`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `STT Umwelt`(organisation)
- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)
- `UnterLemglanzlogHandel`(organisation)
- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)
- `UnterLemglanzlogHandel`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_143`)


1.2. Sonderbetriebsausgaben  In der elektronisch eingelangten Erklärung zur einheitlichen und gesonderten  Gewinnfeststellung der Demircan Metall AG& atypisch stille Gesellschaft für das Jahr 2010 wurden von den  einzelnen atypisch stillen Gesellschafterinnen Sonderbetriebsausgaben in Abzug gebracht:  1. Steinkrafttra Heizung  GmbH & Co KG: -€ 1.123,00  2.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)
- `Steinkrafttra Heizung`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_144`)


STT Umwelt  GmbH & Co KG: -€ 4.402,47  3.

**False Positives:**

- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `STT Umwelt`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_145`)


Drau-Umwelt Entwicklung  GmbH & Co KG: -€ 6.097,75  4.

**False Positives:**

- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Drau-Umwelt Entwicklung`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_146`)


UnterLemglanzlogHandel  GmbH & Co KG: -€ 7.942,46  5.

**False Positives:**

- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_147`)


NordImmobilien  GmbH & Co KG:  -€ 255.101,72   Hierbei handelte es sich um anteilige Kosten aus der „Modellentwicklung“, welche bei der  atypisch stillen Gesellschafterin angefallen sind.

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_150`)


NordImmobilien  GmbH & Co KG:  Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der NordImmobilien  GmbH & Co  KG für das Jahr 2010:  12 von 29 Seite 13 von 29

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`
- `Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der NordImmobilien  GmbH & Co  KG` — similar text (different position): `NordImmobilien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)
- `NordImmobilien`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_173`)


Berechnung der anteilig im Jahr 2010 in Abzug gebrachten Sonderbetriebsausgaben –  NordImmobilien  GmbH & Co KG:   2010  Initialisierungsaufwand gesamt € 953.230,00  Verwaltungsaufwand gesamt € 106.423,28  BMGL Sonderbetriebsausgabe € 1.059.653,28  24,07 %  SBA anteilig (Beteiligung Demircan Metall AG

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)
- `Demircan Metall AG`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_174`)


€ 255.101,72  In den Erklärungen zur einheitlichen und gesonderten Gewinnfeststellungen der Demircan Metall AG&  atypisch stille Gesellschaft 2010 wurden von den anderen atypisch stillen Gesellschafterinnen  folgende Sonderbetriebsausgaben in Abzug gebracht:  – Steinkrafttra Heizung  GmbH & Co KG:     Verhältnis der Beteiligung:    36,53 % von € -3.074,19 (lt. GuV: Verwaltungsaufwand gesamt):    Anteilige Geltendmachung: € -1.123,00   Hinsichtlich der Berechnung des Verhältnisses der Beteiligung wird auf die  Entscheidung des BFG vom 29.9.2023, RV/1100433/2013 verwiesen.

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)
- `Steinkrafttra Heizung`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_175`)


– STT Umwelt  GmbH & Co KG:   Verhältnis der Beteiligung: 27,03 %    27,03 % von € -16.287,35 (lt. GuV: Verwaltungsaufwand gesamt):    Anteilige Geltendmachung: € -4.402,47   Hinsichtlich der Berechnung des Verhältnisses der Beteiligung wird auf die  Entscheidung des BFG vom 29.9.2023, RV/1100433/2013 verwiesen.

**False Positives:**

- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `STT Umwelt`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_176`)


– Drau-Umwelt Entwicklung  GmbH & Co KG:    Verhältnis der Beteiligung: 26,69 %    26,69 % von € -22.846,47 (lt. GuV: Verwaltungsaufwand gesamt):    Anteilige Geltendmachung: € -6.097,75   Hinsichtlich der Berechnung des Verhältnisses der Beteiligung wird auf die  Entscheidung des BFG vom 29.9.2023, RV/1100437/2013 verwiesen.

**False Positives:**

- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Drau-Umwelt Entwicklung`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_177`)


– UnterLemglanzlogHandel  GmbH & Co KG:    Verhältnis der Beteiligung: 37,69 %    37,69 % von € - 21.073,12 (lt. GuV: Verwaltungsaufwand gesamt):    Anteilige Geltendmachung: € -7.942,46  15 von 29 Seite 16 von 29

**False Positives:**

- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_184`)


Der Kapitalmarktprospekt der Steinkrafttra Heizung  GmbH & Co KG wurde am 23. Juli 2008, jener der  STT Umwelt  GmbH am 23. Jänner 2009, der der Drau-Umwelt Entwicklung  GmbH & Co KG am 24. April 2009,  jener der UnterLemglanzlogHandel  GmbH & Co KG am 10. Dezember 2009 und jener der NordImmobilien  GmbH &  Co KG am 28. Juni 2010 aufgelegt.

**False Positives:**

- `Der Kapitalmarktprospekt der Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`
- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`
- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`
- `NordImmobilien  GmbH &  Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)
- `UnterLemglanzlogHandel`(organisation)
- `NordImmobilien`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_188`)


Im Kapitalmarkprospekt der NordImmobilien  GmbH &  Co KG wird zudem darauf hingewiesen, dass rechtliche, steuerliche und wirtschaftliche  Rahmenbedingungen während der Laufzeit dieser langfristigen Beteiligung sich ändern  können.

**False Positives:**

- `Im Kapitalmarkprospekt der NordImmobilien  GmbH &  Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_192`)


Auf Seite 10 unter Punkt 2.4 der Kapitalmarktprospekte UnterLemglanzlogHandel  GmbH & Co KG und  NordImmobilien  GmbH & Co KG wird darauf hingewiesen, dass wenn das Gesellschaftskapital bis 30.  Juni 2010 nicht zumindest € 500.000,00 beträgt, der geschäftsführende Gesellschafter  berechtigt ist, mit Wirkung für alle Gesellschafter und ohne das Erfordernis der Zustimmung  der übrigen Gesellschafter die Gesellschaft gemäß § 16 Gesellschaftsvertrag zu beenden und zu  liquidieren.

**False Positives:**

- `Kapitalmarktprospekte UnterLemglanzlogHandel  GmbH & Co KG und  NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UnterLemglanzlogHandel`(organisation)
- `NordImmobilien`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_208`)


In den Erklärungen zur einheitlichen und gesonderten Gewinnfeststellung der Demircan Metall AG& atypisch  stille Gesellschaft 2010 wurden den atypisch stillen Gesellschafterinnen folgende Verluste  zugewiesen:  – Steinkrafttra Heizung  GmbH & Co KG:  € 0,00  – STT Umwelt  GmbH & Co KG: € 0,00  – Drau-Umwelt Entwicklung  GmbH & Co KG: € 0,00  – UnterLemglanzlogHandel  GmbH & Co KG: € 0,00  – NordImmobilien  GmbH & Co KG: -€ 2.470.000,00

**False Positives:**

- `Steinkrafttra Heizung  GmbH & Co KG` — partial — gold is substring of pred: `Steinkrafttra Heizung`
- `STT Umwelt  GmbH & Co KG` — partial — gold is substring of pred: `STT Umwelt`
- `Umwelt Entwicklung  GmbH & Co KG` — positional overlap with gold: `Drau-Umwelt Entwicklung`
- `UnterLemglanzlogHandel  GmbH & Co KG` — partial — gold is substring of pred: `UnterLemglanzlogHandel`
- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)
- `Steinkrafttra Heizung`(organisation)
- `STT Umwelt`(organisation)
- `Drau-Umwelt Entwicklung`(organisation)
- `UnterLemglanzlogHandel`(organisation)
- `NordImmobilien`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_297`)


(betroffene Bf.: NordImmobilien  GmbH & Co KG) geltend gemacht.

**False Positives:**

- `NordImmobilien  GmbH & Co KG` — partial — gold is substring of pred: `NordImmobilien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NordImmobilien`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_22`)


Die BF ist eine GmbH & Co KG, die ein Hotel betreibt.

**False Positives:**

- `Die BF ist eine GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Suffix GmbH` 💣

**F1:** 0.012 | **Precision:** 0.131 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `4ae7041b`  
**Description:**
Matches generic company names ending in 'GmbH' using context anchors that are less restrictive than verbs.

**Content:**
```
(?:^|\s|\b)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+)*\s+GmbH)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\)|\]|\n|$)|\s+(?:hat|ist|wurde|hatte|sind|waren|kann|konnte|muss|musste|wird|werden|haben|hatten|soll|sollte|dass|oder|und|zu|von|mit|auf|in|an|bei|f\u00fcr|\.|,|\)|\]|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.131 | 0.007 | 0.012 | 251 | 33 | 218 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 33 | 218 | 5010 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_16`)


Im wiederaufgenommenen Verfahren vom 31. Mai 2017 wurde der  Körperschaftsteuerbescheid 2011 der Klaaßens Versand GmbH mit folgender Begründung abgeändert:  Bei Einbringung des Einzelunternehmens des Alleingesellschafters in die Bf. zum 31. Dezember  2004 wurde in der unternehmensrechtlichen Bilanz ein Firmenwert iHv 514.229,34 € aktiviert,  der in weiterer Folge über 10 Jahre abgeschrieben wurde.

| Predicted | Gold |
|---|---|
| `Klaaßens Versand GmbH` | `Klaaßens Versand GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_16`)


D/XX, die VWWJ IT GmbH mit selber  Adresse.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_38`)


die Zulassung auf die VWWJ IT GmbH in D/XX am 3.12.2009, Kz W2;  - Prospekt zum Hotel Y-Hotel in A/Adr1, betrieben von der Verwaldgart GmbH  mit      dem Anbot ua. von xxx-Anwendungen;  - Urkunde des dten.

| Predicted | Gold |
|---|---|
| `Verwaldgart GmbH` | `Verwaldgart GmbH` |

**Missed by this rule (FN):**

- `VWWJ IT GmbH` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_42`)


Audi A6 v. 8.10.2007 an      A, Kaufpreis netto € 45.378,15;  - zwei deutsche Zulassungsbescheinigungen: Zulassung mit Kz W1 auf      A am 9.10.2007, mit Kz W2 auf die VWWJ IT GmbH am 3.12.2009;  - ein Schreiben des A v. 11.8.2011, worin dieser als GF bestätigt,      dass die GmbH seit Mitte 2009 operativ tätig sei, Geschäftsbeziehungen unterhalte     und mehrere Mitarbeiter in Teil- und Vollzeit beschäftige.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_102`)


Am 9.10.2007 haben der Bf und A, deutscher Staatsbürger, die VWWJ IT GmbH mit dem Sitz in D/XX  gegründet;

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_4`)


Die Gesellschafter der Bf. - die Pflege Nexwerkwald GmbH und N.N. - sind jeweils mit einer Stammeinlage von  40.000 € an der Bf. beteiligt.

| Predicted | Gold |
|---|---|
| `Pflege Nexwerkwald GmbH` | `Pflege Nexwerkwald GmbH` |

**Missed by this rule (FN):**

- `N.N.` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_259`)


Der Fleischabschnitt sei am W-Platz hängen geblieben, ohne der Nieder Waldbach GmbH zugeordnet zu  werden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_262`)


Angesichts der Nieder Waldbach GmbH als eine Tochtergesellschaft mit identem Betätigungsfeld [die  mittlerweile in die Bf. verschmolzen worden sei] sei es somit nicht nur aus  betriebswirtschaftlicher Sicht naheliegend gewesen, den Fleischeinkauf zentral über die Bf.  abzuwickeln und die Nieder Waldbach GmbH mit den entsprechenden Kosten anteilig zu belasten.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_496`)


RA verwies auf die anwesenden Auskunftspersonen S1 und S2 A. und Z.3 zur Fleischqualität in  den Streitjahren, wiederholte die bisherigen Ausführungen zu den nahe gelegenen Lokalen  samt den unterschiedlichen Entwicklungen beim Rohaufschlag und brachte zur Geschichte der  Lokale in den Streitjahren vor, dass Herr A., bedingt durch das sehr beschränkte Platzangebot  im Lokal W-Platz, beschlossen habe, die Nieder Waldbach GmbH zu übernehmen und das Geschäft  auszuweiten.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_652`)


Wider die  Schlüssigkeit der Kalkulationsdifferenzen wurden auch Warenbewegungen zwischen der Bf.  und der Nieder Waldbach GmbH ins Treffen geführt, die bei der vom steuerlichen Vertreter der Bf.  angewandten wirtschaftlichen Betrachtungsweise als Warenbewegungen innerhalb einer  wirtschaftlichen Einheit zu deuten sind.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_48`)


Die Vorgangsweise, die  erste Lieferung (zwischen Möbel Zorkelglanz GmbH und Bf.) als ruhend zu behandeln und die zweite Lieferung  zwischen der Bf. und deren Abnehmer als bewegte Lieferung zu sehen, sei richtig.

| Predicted | Gold |
|---|---|
| `Möbel Zorkelglanz GmbH` | `Möbel Zorkelglanz GmbH` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_98`)


Nach Vorlage der Beschwerden an das Bundesfinanzgericht durch die belangte Behörde am  27.7.2016 ergänzte die Bf. ihr Beschwerdevorbringen am 28.9.2016 und führte aus, es stelle  sich die Frage, ob überhaupt ein Reihengeschäft vorliege, da die Möbel Zorkelglanz GmbH in ihrem Werk in F.  (Österreich) Lagerräumlichkeiten zur Verfügung stellte, die exklusiv für die Produktlagerung  der an die Bf. verkauften Produkte genutzt werden und entsprechende Lagergebühren bezahlt  6 von 13 Seite 7 von 13

| Predicted | Gold |
|---|---|
| `Möbel Zorkelglanz GmbH` | `Möbel Zorkelglanz GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_6`)


Die  Beschwerdeführerin, eine bei der AG GmbH angestellte Anzeigenverkäuferin, beantragte die  Berufsgruppenpauschale für VertreterInnen für den Zeitraum 03.03.2014 bis 31.12.2014 und  01.01.2015 bis 31.12.2015.

**False Positives:**

- `AG GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_10`)


Mit Schreiben vom 28.11.2016 legte die Beschwerdeführerin, eine beim AG GmbH angestellte  Anzeigenverkäuferin, eine Bestätigung ihres Dienstgebers vor, mit dem folgenden Wortlaut:   "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit, als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom 01.01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

**False Positives:**

- `AG GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hainig`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_15`)


Die in der von der beschwerdeführenden GmbH im  Rahmen der gegen die Festsetzungsbescheide eingebrachten Beschwerde angeführten  Argumente blieben dabei unberücksichtigt.

**False Positives:**

- `Die in der von der beschwerdeführenden GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_57`)


Im Hinblick darauf, dass die erklärten Umsätze und Vorsteuerbeträge aufgrund der vorgelegten  Unterlagen plausibel erscheinen, war das Finanzamt – wie von diesem im Vorlagebericht auch  zutreffend erkannt wurde - nicht berechtigt, diese im Hinblick darauf, dass die Vertreter der  beschwerdeführenden GmbH zunächst ihrer Mitwirkungspflicht nicht nachgekommen waren,  zu schätzen.

**False Positives:**

- `Vertreter der  beschwerdeführenden GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_8`)


- weitere ZEVIS-Abfrage:     Demnach wurde selbiges Fahrzeug am 3.12.2009 unter dem deutschen      Kennzeichen W2 auf die Firma VWWJ IT GmbH     mit Sitz in D/XX zugelassen;

**False Positives:**

- `Firma VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_38`)


die Zulassung auf die VWWJ IT GmbH in D/XX am 3.12.2009, Kz W2;  - Prospekt zum Hotel Y-Hotel in A/Adr1, betrieben von der Verwaldgart GmbH  mit      dem Anbot ua. von xxx-Anwendungen;  - Urkunde des dten.

**False Positives:**

- `Zulassung auf die VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)
- `Verwaldgart GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_39`)


Notars über die GmbH-Gründung am 9.10.2007 samt      Gesellschaftsvertrag, woraus ua. hervorkommt:     Der Bf und A errichten die VWWJ IT GmbH    mit Sitz in D/XX, je zur Hälfte übernommenes Stammkapital € 25.000;      zum Geschäftsführer wird A bestellt. Unternehmensgegenstand ist      neben Liegenschaftserwerb- und –verwaltung ua. die Vermittlung und der Handel     mit Waren aus dem Bereich medica/wellness.

**False Positives:**

- `Der Bf und A errichten die VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_68`)


In der Folge wurde über das – anstelle seines persönlichen Erscheinens wegen der  zurückzulegenden Strecke von ca. 700 km - mit A am 23.11.2010 geführte Telefonat ein  Protokoll angefertigt, dieses ihm zur Stellungnahme und allfälligen Berichtigung übermittelt  und mit mail am 26.11.2010 teils korrigiert mit folgendem Inhalt dem Finanzamt retourniert:  "… Ich bin Geschäftsführer der VWWJ IT GmbH mit Sitz in D/XX.

**False Positives:**

- `Ich bin Geschäftsführer der VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `VWWJ IT GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_70`)


Die VWWJ IT GmbH wurde 2008 gegründet.

**False Positives:**

- `Die VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_76`)


Die Kunden der VWWJ IT GmbH sind zu 40 % in Österreich  angesiedelt, der Rest im Süddeutschen bzw. Südtiroler Raum.

**False Positives:**

- `Die Kunden der VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_79`)


Am 3.12.2009 wurde dann das KFZ auf das Kennzeichen W2 umgemeldet (auf die Fa.VWWJ IT GmbH  und scheint seit 2010 im Anlagevermögen der Firma auf.

**False Positives:**

- `VWWJ IT GmbH` — partial — pred is substring of gold: `Fa.VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.VWWJ IT GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_90`)


3. laut eigenen Angaben das Fahrzeug erst mit Dezember 2009 in das Betriebsvermögen der VWWJ IT GmbH aufgenommen worden und zuvor auf A angemeldet gewesen sei, welche Angaben  mangels mehrfach angefordeter, jedoch nicht vorgelegter Unterlagen (Bilanz,  Anlagenverzeichnis, Fahrtenbuch etc.) ebenso nicht überprüft werden konnten wie der  5 von 14 Seite 6 von 14

**False Positives:**

- `Betriebsvermögen der VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_112`)


Am 3.12.2009 erfolgte die Zulassung auf die VWWJ IT GmbH in D/XX mit  dem Kennzeichen W2 (siehe deutsche Zulassungsbescheinigungen).

**False Positives:**

- `Zulassung auf die VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_121`)


Gegenständliches Fahrzeug scheint – wenn überhaupt – lt. Aussage des GF A  (erst) seit 2010 im Anlagevermögen der VWWJ IT GmbH auf.

**False Positives:**

- `Anlagevermögen der VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_159`)


In diesem Zusammenhalt ist noch festzuhalten, dass bei einer Verwendung im Inland als  Privatfahrzeug deren Ausmaß irrelevant ist; zur behaupteten beruflichen/betrieblichen  Verwendung des Fahrzeuges für Kundenbesuche ua. im benachbarten Ausland im Rahmen  einer Tätigkeit für die deutsche GmbH wurde – trotz mehrfacher Aufforderung und teils Zusage  10 von 14 Seite 11 von 14

**False Positives:**

- `Ausland im Rahmen  einer Tätigkeit für die deutsche GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_162`)


es liegt lediglich die Aussage des GF A vor, dass das Fahrzeug (erst) seit 2010  im Anlagevermögen der GmbH aufscheine.

**False Positives:**

- `Anlagevermögen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_419`)


Auf einem der im Zuge der Beanstandung durch das Organ der Parkraumüberwachung  angefertigten Beweisfotos war ersichtlich, dass sich das Fahrzeug mit dem Kennzeichen  KENNZ2 bei der FIRMA GmbH in Reparatur befunden habe.

**False Positives:**

- `FIRMA GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_13`)


Die Gaststätte B-Platz ist Folge des Insolvenzverfahrens der Nieder Waldbach GmbH  Diese GmbH  wurde mit Generalversammlungsbeschluss vom 06.09.2007 als übertragende Gesellschaft mit  der Bf. als übernehmender Gesellschaft verschmolzen.

**False Positives:**

- `Platz ist Folge des Insolvenzverfahrens der Nieder Waldbach GmbH  Diese GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_14`)


Seit 2001 hält die Bf. 100% der  Geschäftsanteile an der Nieder Waldbach GmbH   Die Gesellschafter der Bf. sind die Fa.Adeler&Glasener Textil GmbH und V.A. (=V.A.).

**False Positives:**

- `Adeler&Glasener Textil GmbH` — partial — pred is substring of gold: `Fa.Adeler&Glasener Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)
- `Fa.Adeler&Glasener Textil GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_54`)


Ein 16%-Abschnitt trotz Entfernens von Fetträndern etc.  lasse den Schluss auf den Gefälligkeitscharakter der Bestätigung des Geschäftsführers der Lemost-Handel GmbH zu. Das dem "Schaukochen" zugrundegelegene Fleisch habe mangels Etikettierung nicht  eindeutig einem Lieferanten zugeordnet werden können und sei schon einige Tage alt  gewesen.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_57`)


*) Fleischqualität beim Schaukochen: Erhebungsfeststellungen bei der Lemost-Handel GmbH zufolge habe  es sich bei dem für das Schaukochen extra angelieferten Fleisch laut Auskunft einer  Angestellten um altes Fleisch, laut Auskunft des Lemost-Handel GmbH Geschäftsführers um eine Ware ohne  Wert gehandelt. Befragt nach dem Grund für die Bestellung von Fleisch mit so hohem  Fettgehalt, was dann weggeschnitten werde, obwohl wie beim Testkauf bestätigt, Fleisch ohne  Beinkette und mit geringem Fettgehalt geliefert werde, habe der steuerliche Vertreter erklärt:  Fleisch mit Fettrand und Beinkette sei viel saftiger.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)
- `Lemost-Handel GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_67`)


Laut Aussage des Geschäftsführers der Lemost-Handel GmbH vom 24.06.2008 sei Produktefleisch, Artikel  Nr.2190, bis Anfang 2006 geliefert worden.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_71`)


Die Betriebsprüfung habe bei dieser Kalkulation das bei der Betriebsbesichtigung vorgezeigte  Fleisch (Abschnitt 16%) trotz der Aussage des Geschäftsführers der Lemost-Handel GmbH vom 24.06.2008,  die eine Berücksichtigung von nur 6% Abschnitt rechtfertigen würde, berücksichtigt.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_88`)


Unglaubwürdigkeit des dem Schreiben vom 23.4.2009 beigelegten Gutachtens der C-Anstalt:  Laut den Aussagen laut Gutachten sei der Kauf für die Probe [Entnahme von zwei original  verpackten Stücken Schweinskarree Rose aus dem Lager bzw. zwei Stück Schweinskarree Rose  ohne Beinkette vom Arbeitsvorrat des zuständigen Mitarbeiters] zwischen 8:30 bis 12:30 Uhr  am 11.02.2009 bei der Lemost-Handel GmbH in A-Dorf gewesen.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_116`)


Betrieb B-Platz: Nach Erwerb der Anteile an der Nieder Waldbach GmbH im Insolvenzverfahren im Herbst  2001 habe die Bf. die Nieder Waldbach GmbH aus Haftungsgründen als 100%ige Tochtergesellschaft für den  Zeitraum von drei Jahren weitergeführt.

**False Positives:**

- `Nach Erwerb der Anteile an der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)
- `Nieder Waldbach GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_122`)


Den Bilanzdaten für die Nieder Waldbach GmbH zufolge seien die Rohaufschläge der Küchen von Jahr zu Jahr  linear mit zunehmendem Fleischkonsum gestiegen, während davon das Ergebnis W- Platz negativ beeinträchtigt worden wäre.

**False Positives:**

- `Den Bilanzdaten für die Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_123`)


Trotz Hinweis auf diesen Umstand sei das Ersuchen  der Prüfungsausdehnung auf die Nieder Waldbach GmbH im Zuge des Prüfungsverfahrens abgelehnt worden.

**False Positives:**

- `Trotz Hinweis auf diesen Umstand sei das Ersuchen  der Prüfungsausdehnung auf die Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_143`)


Mit der Lieferung des von der Lemost-Handel GmbH am Montag aufgearbeiteten Fleisches bei der Bf. im  Laufe des Dienstagvormittag sei das Fleisch schon zwischen zwölf und vierzehn Stunden  verpackt.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_179`)


Die Lieferung der Lemost-Handel GmbH von drei Tage alten Fleisch (Verpackungsdatum: 7.01.2008) vor   der Betriebsbesichtigung (siehe Lieferschein v. 9.01.2008): Die Betriebsprüfung bestritt,  behauptet zu haben, dass es sich hier um minderwertiges Fleisch handle, und verwies auf eine  Angestellte der Lemost-Handel GmbH  die dieses Fleisch als alt bezeichnet hätte, bzw. auf den  Geschäftsführer der Lemost-Handel GmbH  demnach dieses Fleisch eine Ware ohne Wert sei.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)
- `Lemost-Handel GmbH`(organisation)
- `Lemost-Handel GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_257`)


Bei einer Lieferung vom W-Platz an die Nieder Waldbach GmbH von hundert küchenfertigen  Produkten mit einem Gewicht von rund 250g/Produkt seien der GmbH 25 kg Fleisch in  Rechnung gestellt worden, ohne dass dabei berücksichtigt worden wäre, dass der Standort W- Platz für eine derartige Lieferung wegen der Zuschneidung der Produkte am W-Platz weitaus  mehr Fleisch benötigt habe.

**False Positives:**

- `Platz an die Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_261`)


Diesem Missverhältnis zwischen dem Umsatz  der Nieder Waldbach GmbH und dem gestiegenen, aber nicht weiterverrechneten Abschnitt am W-Platz habe  die Bf. keine Beachtung geschenkt, da sie nur den Gewinn insgesamt betrachtet und die  einzelnen Standorte und Gesellschaften als ein Unternehmen angesehen hätte.

**False Positives:**

- `Diesem Missverhältnis zwischen dem Umsatz  der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_273`)


Zu Tz.3 PB Kalkulationsdifferenzen: Die Ursache für das Absinken der Aufschläge sei in der  Übernahme der Nieder Waldbach GmbH im Jahr 2002 und der damit verbundenen Weiterbelastung der  Küchenwaren ohne Gewinnaufschlag gelegen.

**False Positives:**

- `Die Ursache für das Absinken der Aufschläge sei in der  Übernahme der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_280`)


Im  Bericht werde der Erwerb der Nieder Waldbach GmbH zu diesem Zeitpunkt samt den besagten Verrechnungen  in diesem Zeitraum ignoriert.

**False Positives:**

- `Im  Bericht werde der Erwerb der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_308`)


Die vom Geschäftsführer der Dorfleitner+Ternis Versicherung GmbH auf vorgehaltene Fotos des Prüfers hinauf wortwörtlich  protokollierte Zeugenaussage "Nein, einen so hohen Fettanteil hatten meine Produkte nie."  werde von der Prüfung unrichtig wiedergegeben.

**False Positives:**

- `Ternis Versicherung GmbH` — partial — pred is substring of gold: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_316`)


Angaben des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH zu Warenrückkäufen/zum errechneten Abschnitt  von 11,45 % im Prüfbericht: Der steuerliche Vertreter sprach sich gegen eine Gleichsetzung  des Rückkaufs mit dem Abschnitt aus, weil -abgesehen von erheblichen Fleischsaftverlusten-  nicht angenommen werden könne, dass jeder einzelne Abschnitt tatsächlich zurückgekauft  worden sei.

**False Positives:**

- `Ternis Versicherung GmbH` — partial — pred is substring of gold: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_359`)


Auf die Ignorierung der Ergebnisse des Gutachtens der C-Anstalt und die Ablehnung der  beantragten Prüfung der Nieder Waldbach GmbH wurde verwiesen.

**False Positives:**

- `Anstalt und die Ablehnung der  beantragten Prüfung der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_362`)


entgegen jeder Lebenserfahrung werde  angenommen, dass die von der Dorfleitner+Ternis Versicherung GmbH zurückgekaufte Menge mit dem Abschnitt  gleichzusetzen sei, aus der auf dem Gutachten der C-Anstalt vermerkten Uhrzeit der  Probenentnahme eine Fälschung des Gutachtens konstruiert werde.

**False Positives:**

- `Ternis Versicherung GmbH` — partial — pred is substring of gold: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_368`)


Mangelhafte Feststellung des Sachverhalts als Folge der Ablehnung des Vorschlags  zur Ausdehnung der Prüfung auf die Nieder Waldbach GmbH und den G-Platz  Der Anstieg der Rohaufschläge in der Betriebsstätte B-Platz verlaufe gleichlaufend mit dem  zunehmenden Fleischkonsum in der Betriebsstätte, während dies gleichzeitig das Ergebnis der  Betriebsstätte W-Platz negativ beeinträchtigt habe.

**False Positives:**

- `Mangelhafte Feststellung des Sachverhalts als Folge der Ablehnung des Vorschlags  zur Ausdehnung der Prüfung auf die Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_463`)


Die Fleischmenge, welche an den Lieferanten Dorfleitner+Ternis Versicherung GmbH im Jahre 2006 (Nachschauzeitraum) zurückverkauft worden wäre, wäre anhand der  vorliegenden Rechnungen zwar in Höhe von 11,5% ermittelt, aber trotzdem in Höhe von 16%  berücksichtigt worden.

**False Positives:**

- `Ternis Versicherung GmbH` — partial — pred is substring of gold: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_511`)


Die Lieferung  des bereits im Verarbeitungsbetrieb Lemost-Handel GmbH zugeputzten Fleischprodukts ohne Beinkette und  Fettanteil habe zu Erleichterungen für die Klopfer geführt.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_793`)


Über die Aussage des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH zum Rückkauf der  Fleischabschnitte hinauf hat die belangte Behörde jene Abschnitte, die für das Wirtschaftsjahr  2006 zurückgenommen worden sind, aus den vorgelegten elektronischen  Grundaufzeichnungen ermittelt und dem Gesamtverbrauch Schnitzelfleisch gegenübergestellt.  Aus der Noch-Entsprechung des im Wirtschaftsjahr 2006 (02/2005 bis 01/2006) verwendeten  Fleisches der im Prüfungszeitraum gelieferten Fleischqualität hat sich ein Fleischabschnitt von  11,45% errechnet.

**False Positives:**

- `Ternis Versicherung GmbH` — partial — pred is substring of gold: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_811`)


Zum Beweis dafür seien die Rechnungen der Bf. über die Verrechnung von Fleisch  und Wein mit der Nieder Waldbach GmbH ins Treffen geführt, aus denen die Weiterverrechnung lediglich des  Fleisch(gewicht)s im gesamten Prüfungszeitraum zu entnehmen ist.

**False Positives:**

- `Verrechnung von Fleisch  und Wein mit der Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_843`)


Die Anträge auf mündliche Gutachtenserörterung durch die namentlich genannten  Sachverständigen von der B-Anstalt und C-Anstalt, zu den Beweisthemen Gutachten, Ablauf bei  der Probenentnahme und Erstellung des jeweiligen Gutachtens und Einvernahme des  Geschäftsführers der Lemost-Handel GmbH zum Beweisthema Lieferfleischqualität, Höhe des Abschnitts  bzw. der verkaufbaren Fleischmenge waren dadurch, dass der Senat seiner Entscheidung im  fortgesetzten Verfahren die letztvorgelegte Kalkulation des steuerlichen Vertreters zu Grunde  legt, abzuweisen.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_876`)


Ad. Kapitalertragsteuer für die Jahre 2003 bis 2005  Verfahrensgang:  Der Gesellschafter der Bf. ist eine Holding GmbH mit einer Stiftung als Alleingesellschafter.

**False Positives:**

- `Holding GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_885`)


Der Gesellschafter der Bf. ist eine Holding GmbH mit einer Stiftung als Alleingesellschafter.

**False Positives:**

- `Holding GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_888`)


Die Adeler&Glasener Textil GmbH hat die  übrige Stammeinlage von 131.290 € gehalten.

**False Positives:**

- `Die Adeler&Glasener Textil GmbH` — partial — gold is substring of pred: `Adeler&Glasener Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Adeler&Glasener Textil GmbH`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_9`)


Als Begründung wurde Folgendes ausgeführt:   "Bei der Firma Starnberg Beratung GmbH waren seit März 2012 keine Arbeiter mehr angemeldet.

**False Positives:**

- `Bei der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_18`)


Am Firmensitz der PGIV Umwelt Entwicklung GmbH konnte ab März 2011 niemand mehr angetroffen werden.

**False Positives:**

- `Am Firmensitz der PGIV Umwelt Entwicklung GmbH` — partial — gold is substring of pred: `PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_63`)


Ebenso kann die vage Feststellung,  dass diverse Kontrollmitteilungen ergeben hätten, dass ab März 2011 zumindest 250  Scheinrechnungen der PGIV Umwelt Entwicklung GmbH im Umlauf gewesen seien, nichts zur Begründung des  Erkenntnisses beitragen.

**False Positives:**

- `Scheinrechnungen der PGIV Umwelt Entwicklung GmbH` — partial — gold is substring of pred: `PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_139`)


12/2013 sowie Außenprüfung (ohne Datum) wurde zum Thema Fremdleistungsfirmen (hier  zum besseren Verständnis der Ausgangslage wiedergegeben) schon Folgendes festgestellt:   Tz. 4 Fremdleistungsfirmen  Die Firma Starnberg Beratung GmbH hat keine Arbeiter angemeldet.

**False Positives:**

- `Fremdleistungsfirmen  Die Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_145`)


Die beiden nicht verbuchten "überzähligen" Ausgangsrechnungen wurden in  dem im Büro aufliegenden Belegordner der Firma Starnberg Beratung GmbH aufgefunden und dürften dem  Steuerberater "H." bei Erstellung der Buchhaltung offenbar nicht vorgelegen sein.

**False Positives:**

- `Ausgangsrechnungen wurden in  dem im Büro aufliegenden Belegordner der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_163`)


Im finalen Parteiengehör führte die Geschäftsführung der Firma Starnberg Beratung GmbH mit Email- Übertragung am 23.04.2014 im Zusammenhang mit der Firma Furtnor-Handel GmbH noch die Namen Herr  Z1, Herr Z2 an.

**False Positives:**

- `Im finalen Parteiengehör führte die Geschäftsführung der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)
- `Furtnor-Handel GmbH`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_176`)


Furtnor-Handel GmbH  Zur Furtnor-Handel GmbH wurde festgestellt, dass sie seit Stichtag 5.3.2012 weder als Dienstgeber noch als  Leistungserbringer mehr in Frage kam.

**False Positives:**

- `Handel GmbH` — similar text (different position): `Furtnor-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnor-Handel GmbH`(organisation)
- `Furtnor-Handel GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_180`)


Da  im Namen der Furtnor-Handel GmbH massive Malversationen getätigt wurden, wurde seitens der  Finanzprokuratur mit Schriftsatz am 31.8.2012 das Ersuchen um Konkurseröffnung gestellt.  Eröffnung des Konkurses: x.2012 HG  Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH aufliegenden Scheinrechnungen  konnten im Prüfungsverfahren mangels entsprechend zweckdienlicher Auskünfte durch die  Geschäftsleitung nicht in Erfahrung gebracht werden.

**False Positives:**

- `HG  Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnor-Handel GmbH`(organisation)
- `Starnberg Beratung GmbH`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_181`)


PGIV Umwelt Entwicklung GmbH  Ermittlungen zu Beginn der 2. Jahreshälfte 2012 ergaben, dass es sich bei der Firma PGIV Umwelt Entwicklung GmbH  für den Zeitraum ab Herbst 2011 um eine zu Betrugszwecken geführte Scheinfirma handelte:  Am Firmensitz (Substandartwohnung) konnte niemand angetroffen werden.

**False Positives:**

- `Firma PGIV Umwelt Entwicklung GmbH` — similar text (different position): `PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)
- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_184`)


Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH aufliegenden Scheinrechnungen  konnten im Prüfungsverfahren mangels entsprechend zweckdienlicher Auskünfte durch die  Geschäftsleitung nicht in Erfahrung gebracht werden.

**False Positives:**

- `Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_191`)


Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH aufliegenden Scheinrechnungen  konnten im Prüfungsverfahren mangels entsprechend zweckdienlicher Auskünfte durch die  Geschäftsleitung nicht in Erfahrung gebracht werden.

**False Positives:**

- `Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_192`)


Anmerkung:  Inwieweit die in den Firmenunterlagen der Firma Starnberg Beratung GmbH aufgefundenen  Rechnungslegungen im Namen der Firmen G. GmbH;

**False Positives:**

- `Inwieweit die in den Firmenunterlagen der Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)
- `G. GmbH`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_213`)


Bauvorhaben: Wien4 Bauträger  Die vorgebliche Fremdleistungsfirma PGIV Umwelt Entwicklung GmbH hatte ihre offizielle Geschäftsanschrift in  Firmensitz, wo auch deren angeblicher Alleingesellschafter und Geschäftsführer, Herr D. C.,  geb. 1952, unbekannten Aufenthalts, seinen gemeldeten Wohnsitz innehatte.

**False Positives:**

- `Bauträger  Die vorgebliche Fremdleistungsfirma PGIV Umwelt Entwicklung GmbH` — partial — gold is substring of pred: `PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_218`)


Das Rechnungsdesign der PGIV Umwelt Entwicklung GmbH wurde von offenbar unterschiedlichen Tätergruppen für  Urkundenfälschungen missbraucht.

**False Positives:**

- `Das Rechnungsdesign der PGIV Umwelt Entwicklung GmbH` — partial — gold is substring of pred: `PGIV Umwelt Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_277`)


Feststellung von Scheinrechnungen  In den Monaten Jänner + Februar 2014 waren keine Arbeiter auf die Firma Starnberg Beratung GmbH  angemeldet.

**False Positives:**

- `Arbeiter auf die Firma Starnberg Beratung GmbH` — partial — gold is substring of pred: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_29`)


III. Beweiswürdigung  Der vorstehende Sachverhalt basiert auf nachfolgender Beweiswürdigung:  Die Feststellungen zur Gründung der GmbH und deren Sitz fußen auf einer Einsicht des  Gerichtes in das offene Firmenbuch unter Berücksichtigung der dort hinterlegten historischen  Daten.

**False Positives:**

- `Die Feststellungen zur Gründung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_86`)


Diese Kenntnisverschaffung hat in  Fällen des § 248 BAO insbesondere durch Zusendung einer Ausfertigung (Ablichtung) des/der  Abgabenbescheide(s) an den Haftungspflichtigen, allenfalls durch konkrete Mitteilung des  Bescheidinhaltes zu geschehen, und ist selbst dann unerlässlich, wenn der Haftungspflichtige,  etwa, weil ihm die betreffenden Bescheide als Geschäftsführer einer GmbH zugestellt wurden,  vom Abgabenanspruch Kenntnis haben muss (Ritz, aaO, § 248 Rz. 8 und Rz. 9 mwN).

**False Positives:**

- `Bescheide als Geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_34`)


Nach erfolgreicher Realisierung des „vorgenannten Investitionsvorhabens“  hätte die Bf. Steuerberatungsgesellschaft mbH laut einer mit D getroffenen Vereinbarung  weiterhin sämtliche Beratungsleistungen für dessen Betriebe und der Schilift GmbH zu  erledigen gehabt.

**False Positives:**

- `Steuerberatungsgesellschaft mbH laut einer mit D getroffenen Vereinbarung  weiterhin sämtliche Beratungsleistungen für dessen Betriebe und der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_65`)


Der Beschwerdeführer war ausweislich des Firmenbuchs im Zeitraum 18.1.2007 bis 15.8.2008  Geschäftsführer und von 18.1.2007 bis zu ihrer Auflösung infolge Eröffnung des  Konkursverfahrens aufgrund des Beschlusses des Landesgerichts_1 vom 1.9.2010 zu GZ_1  Gesellschafter der Schilift GmbH mit der Firmenbuchnummer FN_1.

**False Positives:**

- `Gesellschafter der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_67`)


Der Beschwerdeführer hielt seine Beteiligung an der Schilift GmbH in seinem Privatvermögen.

**False Positives:**

- `Der Beschwerdeführer hielt seine Beteiligung an der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_86`)


Allerdings findet sich weder  in dieser noch in den übrigen Beilagen eine Erwähnung der Schilift GmbH oder der Tatsache,  dass der Beschwerdeführer in der Vergangenheit eine Beteiligung an dieser gehalten hatte.

**False Positives:**

- `Allerdings findet sich weder  in dieser noch in den übrigen Beilagen eine Erwähnung der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_109`)


Der Beschwerdeführer hat seine Beteiligung an der Schilift GmbH im Privatvermögen gehalten.

**False Positives:**

- `Der Beschwerdeführer hat seine Beteiligung an der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_116`)


Insofern der Beschwerdeführer vermeint, seine (unentgeltliche) Geschäftsführertätigkeit für  die Schilift GmbH stelle bei wirtschaftlicher Betrachtungsweise einen Zusammenhang zwischen  seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus selbständiger Arbeit  als (wesentlich beteiligter) Gesellschafter-Geschäftsführer seiner Wirtschaftstreuhand GmbH  her, ist dem Folgendes entgegenzuhalten: Nach dem Beschwerdevorbringen war die Erzielung  von Einkünften durch die Bf. Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH  von der Erhaltung der „langfristigen Werthaltigkeit der empfohlenen Investitionen und  Beteiligungen“ abhängig.

**False Positives:**

- `Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_108`)


Die Vereinbarungen hinsichtlich der Vermietung der  gegenständlichen Liegenschaft wurden zwischen der Johann Alkraft-Maschinenbau GmbH und A. W getroffen.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `Alkraft-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alkraft-Maschinenbau GmbH`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_8`)


Diese vertreibe weltweit Produkte für den Bereich von Erkundungsbohrungen, wobei ein Teil  der Produkte von der inländischen Möbel Zorkelglanz GmbH in Lohnfertigung ausschließlich für die Bf. erzeugt  werde.

**False Positives:**

- `Teil  der Produkte von der inländischen Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_16`)


Lieferkondition zwischen der Möbel Zorkelglanz GmbH und der Bf. laute laut Vertrag „EXW“ und auf den  Rechnungen werde diese mit „FCA“ bezeichnet.

**False Positives:**

- `Lieferkondition zwischen der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_18`)


Bei den innergemeinschaftlichen Geschäftsfällen sei wie folgt vorgegangen worden:  Die Bf. erhalte eine Kundenbestellung und beauftrage die Möbel Zorkelglanz GmbH mit der Produktion.

**False Positives:**

- `Kundenbestellung und beauftrage die Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_46`)


Im gegenständlichen Fall  habe der Erstlieferant Möbel Zorkelglanz GmbH auf Grund der ausgestellten CMR gewusst, dass die Ware von  der Bf. an eine andere Bf.- Konzerngesellschaft verkauft werde.

**False Positives:**

- `Im gegenständlichen Fall  habe der Erstlieferant Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_82`)


Betreffend Kommunikation und Transparenz zwischen der Möbel Zorkelglanz GmbH und Bf. wurde weiters  ausgeführt:  Die Möbel Zorkelglanz GmbH hätte bei den igL. analog den (beim do. Finanzamt angefragten)  5 von 13 Seite 6 von 13

**False Positives:**

- `Betreffend Kommunikation und Transparenz zwischen der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Möbel Zorkelglanz GmbH`(organisation)
- `Finanzamt`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_118`)


Daher  handle es sich bei den zwischen der Möbel Zorkelglanz GmbH und der Bf. um unter gemäß § 3 Abs. 7 UStG  1994 fallende „ruhende“ Lieferungen, weil sich die betreffenden Waren zum Zeitpunkt, indem  die Bf. die Verfügungsmacht erlangte, in Österreich befanden.

**False Positives:**

- `Daher  handle es sich bei den zwischen der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_125`)


In ihrem Antwortschreiben vom 10.10.2017 wird seitens der belangten Behörde auf die  bisherigen Vorbringen (Anfragebeantwortung des Finanzamtes an die Möbel Zorkelglanz GmbH vom  10.11.2011, Sachverhaltsdarstellung der Möbel Zorkelglanz GmbH vom 5.2.2015, Aktenvermerk vom  16.7.2015 und dem BP-Bericht vom 25.6.2015 sowie die Begründungen in den  Beschwerdevorentscheidungen sowie weiters darauf, dass Lagergebühren zu keiner Zeit  erkannt wurden) verwiesen.

**False Positives:**

- `Anfragebeantwortung des Finanzamtes an die Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Finanzamtes`
- `Sachverhaltsdarstellung der Möbel Zorkelglanz GmbH` — similar text (different position): `Möbel Zorkelglanz GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Möbel Zorkelglanz GmbH`(organisation)
- `Möbel Zorkelglanz GmbH`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_144`)


Abgesehen davon geht bereits aus der Anfrage der Möbel Zorkelglanz GmbH an das Finanzamt Villach-Spittal vom 7.11.2011 unmissverständlich hervor, dass die  Warenlieferung direkt an einen Kunden der Bf. ins das Drittland erfolgen werde.

**False Positives:**

- `Abgesehen davon geht bereits aus der Anfrage der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Finanzamt Villach-Spittal`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_155`)


Der in der  Anfrage der Möbel Zorkelglanz GmbH an das do. Finanzamt angeführte Sachverhalt entspreche nicht der  Vereinbarung und dem gesetzten Sachverhalt. Zu diesem Thema könnte auch Herrn DI O.C.  zeugenschaftlich befragt werden.

**False Positives:**

- `Der in der  Anfrage der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Finanzamt`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_159`)


Somit handle es sich bei der ersten  Lieferung der Möbel Zorkelglanz GmbH an die Bf. um die „ruhende Lieferung“ iSd. § 3 Abs. 7 UStG 1994.

**False Positives:**

- `Somit handle es sich bei der ersten  Lieferung der Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_165`)


Im vorliegenden Fall war die Möbel Zorkelglanz GmbH informiert, dass die Ware von der Bf. an andere Konzerngesellschaften weiterkauft  werde.

**False Positives:**

- `Im vorliegenden Fall war die Möbel Zorkelglanz GmbH` — partial — gold is substring of pred: `Möbel Zorkelglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Logzor-Event GmbH`
- `Event GmbH` — similar text (different position): `Logzor-Event GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Aron Pommeränke`(person)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_6`)


2. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juli 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Logzor-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_8`)


3. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im August 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Logzor-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_10`)


4. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im September 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Logzor-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_12`)


5. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Oktober 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Logzor-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_44`)


3.3. Argumentation des Unternehmens bzw. der steuerlichen Vertretung und Stellungnahme  dazu:  In einer Stellungnahme der steuerlichen Vertretung Steincon-Maschinenbau GmbH in Wien bezieht sich diese auf die  Entscheidung des BFG vom 02.06.2016, RV/2101353/2014, wonach es schon begrifflich nicht  3 von 59 Seite 4 von 59

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `Steincon-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steincon-Maschinenbau GmbH`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_90`)


BFG vom 30.11.2017:  Nach Ansicht der Bf. ist die Verfügungsmacht über die Ware bereits in Österreich von der Unter-Pflege GmbH auf sie und von ihr auf die EU-Warenempfänger übergegangen.

**False Positives:**

- `Pflege GmbH` — partial — pred is substring of gold: `Unter-Pflege GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter-Pflege GmbH`(organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_336`)


Als „delivery  Adress“ scheine die in der Ausgangsrechnung aufscheinende Wein- und Sektkellerei GmbH auf.

**False Positives:**

- `Sektkellerei GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Suffix AG` 💣

**F1:** 0.002 | **Precision:** 0.088 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `7ee7150a`  
**Description:**
Matches generic company names ending in 'AG' using context anchors that are less restrictive than verbs.

**Content:**
```
(?:^|\s|\b)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+)*\s+AG)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\)|\]|\n|$)|\s+(?:hat|ist|wurde|hatte|sind|waren|kann|konnte|muss|musste|wird|werden|haben|hatten|soll|sollte|dass|oder|und|zu|von|mit|auf|in|an|bei|f\u00fcr|\.|,|\)|\]|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.088 | 0.001 | 0.002 | 57 | 5 | 52 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 52 | 5038 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_183`)


Gegenüber ZWOP Cloud AG und den EU- Kunden ist Bf. stets mit ihrer österreichischen UID-Nummer aufgetreten, welche auch von ZWOP Cloud AG  in den Rechnungen angeführt wurde.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_207`)


- Verwendung der UID-Nummer  Bf. ist stets gegenüber ZWOP Cloud AG und ihren EU-Kunden mit ihrer österreichischen UID-Nummer  aufgetreten.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_460`)


Eingangsrechnung vom 2.2.2015 ZWOP Cloud AG an Bf. über 24.620 kg á 223,16 € = 5.494,20 € (netto)  zuzügl.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_473`)


Zum Rahmenvertrag vom 10.12.2014 zwischen der ZWOP Cloud AG und der Bf. ist auszuführen, während  der Laufzeit des Vertrages sind im „Rahmen der festgelegten Mengen“ diese durch den  Auftraggeber (Bf.) dem Auftragnehmer (J. AG) Bestellungen über SAP, E-Mail oder Fax zwei  Werktage vor dem geplanten Liefertermin zu übermitteln.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Missed by this rule (FN):**

- `J. AG` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der in Österreich ansässige Beschwerdeführer (Bf.) war in den Jahren 2015 bis 2017 bei der  Holz Nexglanz AG  in Auersbach  in Frankreich als technischer Geschäftsführer beschäftigt.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Missed by this rule (FN):**

- `Auersbach` (city)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_67`)


Dies war eine Tochtergesellschaft von AG mit 2,4 Milliarden Dollar Umsatz, 1200 Mitarbeitern, 14 Büros in 11 Zeitzonen, einer Fabrik und einer Forschungsstelle.

**False Positives:**

- `Dies war eine Tochtergesellschaft von AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_68`)


14 Manager dieser Niederlassung haben direkt an mich berichtet (fast tägliche Meetings, Fragen, Eskalationen) - alle anderen Mitarbeiter und Unterorganisationen waren diesen 14 Mitarbeitern unterstellt. Seite 6 von 15 Mit meinem damaligen Chef (der Leiter von AG in Ost- und Zentraleuropa, Mittlerer Osten, Afrika und die GUS Staaten) wurde vereinbart, dass ich eine Woche pro Monat von Wien aus arbeite und den Rest des Monats den Job in Russland oder reisebedingt in Drittländer ausübe.

**False Positives:**

- `Leiter von AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_71`)


Diese Aufgaben waren: o Kontakt zum Hauptquartier von AG in Wien aufrechtzuerhalten: Meetings bei mir oder bei AG Wien;

**False Positives:**

- `Kontakt zum Hauptquartier von AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_48`)


Mit Schreiben vom 19.01.2017 erhob die Beschwerdeführerin das Rechtsmittel der  Beschwerde und führte dazu aus:  "Hiermit erhebe ich Beschwerde gegen die Einkommensteuerbescheide 2014 und 2015 vom 21.  Dezember 2016 und beantrage die Berücksichtigung der Vertreterpauschale für 2014 und 2015  wie im Antrag vom 15. Juni 2016 ersichtlich, da ich seit März 2014 ausschließlich im  Anzeigenverkauf des AG für die Ort AG tätig bin."

**False Positives:**

- `Anzeigenverkauf des AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_59`)


In der am 19.01.2017 eingebrachten Beschwerde gegen die  Einkommensteuerbescheide 2014 und 2015 vom 21.12.2016 beantragt die Abgabepflichtige  neuerlich die Berücksichtigung des Vertreterpauschales, da sie seit März 2014 ausschließlich im  Anzeigenverkauf des AG für die Ort AG tätig ist.

**False Positives:**

- `Anzeigenverkauf des AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_70`)


• Optimale Umsetzung der festgelegten Verkaufs-Strategien für das Gebiet  • Einhaltung der festgelegten und vorgegebenen Preispolitik  • Optimale Beratung hinsichtlich Werbeauftritt und Mediaplanung, Promotions- und PR  Aktionen  • Erstellung von Offerten und Verträgen inkl. Vertragsverhandlungen mit Kunden (in  Absprache mit der Verkaufsleitung bzw. Anzeigenleitung)  • Optimales Handling von Reservierungen bzw. Unterstützung bei Veränderungen  • Regelmäßige Firmen- und Kundenbesuche  • Teilnahme an verkaufsfördernden Events und Kundenterminen  • Teilnahme an den vorgegebenen Verkaufs-Meetings in der eigenen Außenstelle bzw. in  anderen Außenstellen oder der Zentrale im AG in Stadt1  • Einfordern offener Außenstände bzw. anschließende Weitergabe an das Inkasso  • Durchführung des Key Account-Managements  • Forcierung der Neukundenacquisition in Zusammenarbeit mit der Verkaufsleitung bzw.  Anzeigenleitung  • Organisation und Durchführung von verkaufsfördernden Aktionen  • Marktbeobachtung und eventuelle Strategie-Anpassungen  • Analyse der Zuwächse bzw. Rückgänge punkto Umsatzzahlen sowie entsprechendes  Entgegenwirken  • Erledigung des Monatsberichtes und Übermittlung an die Verkaufsleitung  Kundenbetreuung  • Laufende Firmen- und Kundenbesuche  • Optimale Betreuung der Kunden am Telefon bzw. bei schriftlicher Korrespondenz  • Ständiger Kontakt zu Kunden inkl. Kontaktförderung (Give-Aways, Einladung zu Events)  • Teilnahme an verkaufsfördernden Events und Kundenterminen (Firmenjubiläen,  Hausmessen etc.)  • Betreuung von Laufkunden in der Außenstelle vor Ort   • Beschwerde- bzw. Reklamationsmanagement gemeinsam mit der Verkaufsleitung bzw.  Anzeigenleitung  • Erläuterung und Versand von Infomaterial und Mediadaten an interessierte Neukunden  und bestehende Kunden.

**False Positives:**

- `Außenstellen oder der Zentrale im AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_86`)


Daher beantrage ich, die Bestätigungen des AG anzuerkennen, diese dem  Verwaltungsgericht vorzulegen und einen neuen Bescheid zu erlassen."

**False Positives:**

- `Bestätigungen des AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_16`)


Er nutze das Fahrzeug als Dienstfahrzeug für seine Tätigkeit als  Regionaldirektor für Südbayern in einem abhängigen Arbeitsverhältnis bei der Firma AG in  d_Ort_2 an 6 Werktagen die Woche.

**False Positives:**

- `Er nutze das Fahrzeug als Dienstfahrzeug für seine Tätigkeit als  Regionaldirektor für Südbayern in einem abhängigen Arbeitsverhältnis bei der Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_60`)


Der Beschwerdeführer stand im Jahr 2017 in einem Dienstverhältnis zur AG in Plz_2 d_Ort_2  (Deutschland).

**False Positives:**

- `Dienstverhältnis zur AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_64`)


Beweiswürdigung  Die Angaben des Beschwerdeführers zu seiner nichtselbständigen Tätigkeit für die AG sind  angesichts des vorgelegten Lohnzettels für den Zeitraum Dezember 2016 glaubwürdig und  wurden sowohl von seiner als Zeugin einvernommenen Ehegattin als auch von seinem  Steuerberater bei dessen Befragung am 11.6.2018 an der Polizeiinspektion d_Ort_1 bestätigt.

**False Positives:**

- `Beweiswürdigung  Die Angaben des Beschwerdeführers zu seiner nichtselbständigen Tätigkeit für die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_99`)


…Herr Volchert ist hauptberuflich Angestellter der AG in d_Ort_2.

**False Positives:**

- `Herr Volchert ist hauptberuflich Angestellter der AG` — partial — gold is substring of pred: `Volchert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volchert`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_165`)


Vorbringen in der Beschwerde nutzt der Beschwerdeführer das gegenständliche Fahrzeug „als  Dienstfahrzeug für meine Tätigkeit als Regionaldirektor für Südbayern in einem abhängigen  Arbeitsverhältnis bei der Firma AG in d_Ort_2 an 6 Werktagen die Woche.

**False Positives:**

- `Dienstfahrzeug für meine Tätigkeit als Regionaldirektor für Südbayern in einem abhängigen  Arbeitsverhältnis bei der Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_73`)


Dies ist aufgrund der bei den vom Finanzamt  vorgelegten Akten befindlichen Schreiben der Traun-Handel AG vom 28.6.2010 und vom 13.7.2010 und  durch einen vom Beschwerdeführer am 10.2.2021 vorgelegten Bankauszug erwiesen.

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Traun-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Traun-Handel AG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_92`)


Insgesamt zeigt sich, dass dem Finanzamt die entscheidungswesentlichen  Sachverhaltselemente im Zusammenhang mit den Zahlungen an die Traun-Handel AG und an RA Dr. E bei  der Erstveranlagung nicht bekannt waren und dass das Finanzamt erst im  Außenprüfungsverfahren von diesen Sachverhaltselementen Kenntnis erlangt hat.

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Traun-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Traun-Handel AG`(organisation)
- `RA Dr. E`(person)
- `Finanzamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_116`)


Insofern der Beschwerdeführer vermeint, seine (unentgeltliche) Geschäftsführertätigkeit für  die Schilift GmbH stelle bei wirtschaftlicher Betrachtungsweise einen Zusammenhang zwischen  seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus selbständiger Arbeit  als (wesentlich beteiligter) Gesellschafter-Geschäftsführer seiner Wirtschaftstreuhand GmbH  her, ist dem Folgendes entgegenzuhalten: Nach dem Beschwerdevorbringen war die Erzielung  von Einkünften durch die Bf. Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH  von der Erhaltung der „langfristigen Werthaltigkeit der empfohlenen Investitionen und  Beteiligungen“ abhängig.

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Traun-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_118`)


Daher ist nicht einmal ein mittelbarer Zusammenhang  zwischen seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus  selbständiger Arbeit erkennbar.

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Traun-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) forderte die Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa.Dankwardt Wind AG  mit Schreiben vom 3. September 2019 gemäß § 2 Wiener Parkometergesetz 2006) auf,  der Behörde binnen zwei Wochen ab Zustellung des Schreibens Auskunft darüber zu erteilen,  wem das näher bezeichnete Fahrzeug am 5. Juli 2019 um 17:47 Uhr überlassen war, sodass es  in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Altgasse 25a, stand.

**False Positives:**

- `Dankwardt Wind AG` — partial — pred is substring of gold: `Fa.Dankwardt Wind AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Fa.Dankwardt Wind AG`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_176`)


Die Ware gelangte dabei direkt vom Werk von ZWOP Cloud AG in P. (Niederösterreich)  an die jeweiligen EUR-Kunden in verschiedenen EU-Mitgliedstaaten.

**False Positives:**

- `Die Ware gelangte dabei direkt vom Werk von ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_180`)


Sofern der EU-Kunde einen Abruf macht, informiert auch Bf.  den Lieferanten ZWOP Cloud AG und macht ihrerseits einen Abruf der bereits im Jahr 2014 vertraglich  gekauften Waren.

**False Positives:**

- `Lieferanten ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_183`)


Gegenüber ZWOP Cloud AG und den EU- Kunden ist Bf. stets mit ihrer österreichischen UID-Nummer aufgetreten, welche auch von ZWOP Cloud AG  in den Rechnungen angeführt wurde.

**False Positives:**

- `Gegenüber ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)
- `ZWOP Cloud AG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_192`)


Die beiden Lieferungen werden somit nicht dadurch  ausgeführt, dass der erste Unternehmer dem letzten Abnehmer in der Reihe unmittelbar die  Verfügungsmacht an dem Gegenstand verschafft (vgl. Ruppe/Achatz, UStG, 5. Auflage, § 3  Rz. 53 mwN), sondern es wird die Verfügungsmacht zuerst von ZWOP Cloud AG auf Bf. übertragen und  erst nachgelagert in einem zweiten Schritt von Bf. auf den EU-Kunden.

**False Positives:**

- `Verfügungsmacht zuerst von ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_195`)


Im Vertrag mit ZWOP Cloud AG wurde auch geregelt, dass die Lieferung mit Abgabe der Ware aus dem Füllstutzen als  ausgeführt gilt und in diesem Zeitpunkt der Eigentumsübergang erfolgt, aber auch Risiken des  Verlustes oder des zufälligen Untergangs übergehen.

**False Positives:**

- `Im Vertrag mit ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_196`)


Mit Abholung der Produkte bzw. bei  Beladung der LKWs geht somit vertraglich die Verfügungsmacht von ZWOP Cloud AG auf Bf. über.

**False Positives:**

- `Beladung der LKWs geht somit vertraglich die Verfügungsmacht von ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_198`)


Die Lieferungen von ZWOP Cloud AG sind folglich in Österreich steuerbar und  steuerpflichtig.

**False Positives:**

- `Die Lieferungen von ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_244`)


D.h. die Inrechnungstellung von österreichischer  Umsatzsteuer durch ZWOP Cloud AG ist zu Recht erfolgt, weil es sich bei dieser Lieferung mangels  Transportzuordnung nicht um die grenzüberschreitende innergemeinschaftliche Lieferung  handelt.  Als Zwischenergebnis kann somit festgehalten werden, dass unter Berücksichtigung aller  Umstände des Einzelfalles die Zuordnung des grenzüberschreitenden Transports zur zweiten  Lieferung, nämlich der von Bf. an den EU-Kunden, zu erfolgen hat.

**False Positives:**

- `Inrechnungstellung von österreichischer  Umsatzsteuer durch ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_246`)


Die Lieferung von ZWOP Cloud AG an Bf. ist folglich als ruhende Lieferung zu beurteilen, die gem. § 3  Abs. 7 UStG in Österreich steuerbar und steuerpflichtig ist.

**False Positives:**

- `Die Lieferung von ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_303`)


Die ruhende  Lieferung besteht zwischen ZWOP Cloud AG und Bf. (steuerbarer und steuerpflichtiger Umsatz von ZWOP Cloud AG.

**False Positives:**

- `Die ruhende  Lieferung besteht zwischen ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)
- `ZWOP Cloud AG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_305`)


In diesen Fällen ist von  einer bewegten Lieferung gem. § 3 Abs. 8 UStG zwischen ZWOP Cloud AG und Bf. auszugehen.ZWOP Cloud AG tätigt   daher in Österreich steuerbare und bei Vorliegen der Voraussetzungen gem. Art. 6 Abs. 1 i.V.m.  20 von 59 Seite 21 von 59

**False Positives:**

- `UStG zwischen ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)
- `.ZWOP Cloud AG`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_437`)


3/21: CMR 80723344 an Ko. (Polska) vom 13.6.2016  Anlage 4:  4/1: Letter of confirmation for VAT purposes Sektkellerei vom 28.6.2018 (in englischer  Sprache)  4/2: Letter of confirmation for VAT purposes Fro. vom 22.6.2018 (in englischer Sprache)  4/3: Übersetzung des Schreibens Sektkellerei vom 28.6.2018 (v. 26.6.2020)  4/4: Letter of confirmation for VAT purposes Sektkellerei vom 28.6.2018 (in englischer  Sprache)  4/5: Übersetzung des Schreiben Fro. vom 22.6.2018 (v. 26.6.2020)  4/6: Letter of confirmation for VAT purposes Fro. vom 22.6.2018  Anlage 5:  5/1: Letter of confirmation for VAT purposes C. Supply Company AG vom 22.9.2020  5/2: Übersetzung des Bestätigungsschreibens für Mehrwertsteuerzwecke vom 22.9.2020 (v.  29.9.2020)  5/3: Letter of confirmation for VAT purposes C. Supply Company AG vom 22.9.2020  5/4: CMR 80477538 an S. (Estland) vom 12.10.2015  Mit hg. Mail vom 20.10.2020 wurden die übersandten Anlagen mit der Maßgabe beanstandet,  dass das von der Bf. gewünschte Beweisergebnis nicht hergestellt werden könne.

**False Positives:**

- `Supply Company AG` — partial — pred is substring of gold: `C. Supply Company AG`
- `Supply Company AG` — similar text (different position): `C. Supply Company AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `C. Supply Company AG`(organisation)
- `C. Supply Company AG`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_11`)


Finanzamt an den Einkünften des Jahres 2014, in dem der Bf. noch bei der Alpen-Wind AG  in  Österreich beschäftigt war.

**False Positives:**

- `Wind AG` — partial — pred is substring of gold: `Alpen-Wind AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Alpen-Wind AG`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_23`)


Mit dem Antwortschreiben vom 14.11.2019 legte die Steuervertretung eine  Tätigkeitsbeschreibung durch die Holz Nexglanz AG  und die Kumulativjournale 2015 bis 2017 vor.

**False Positives:**

- `Steuervertretung eine  Tätigkeitsbeschreibung durch die Holz Nexglanz AG` — partial — gold is substring of pred: `Holz Nexglanz AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Holz Nexglanz AG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_39`)


 Seit 1.1.2015 ist er als technischer Geschäftsführer bei der Holz Nexglanz AG  in Auersbach  tätig, wo er die Bereiche Produktentwicklung, Technologieentwicklung und  das Qualitätsmanagement über hat.

**False Positives:**

- `Geschäftsführer bei der Holz Nexglanz AG` — partial — gold is substring of pred: `Holz Nexglanz AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Holz Nexglanz AG`(organisation)
- `Auersbach`(city)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_57`)


Ende 2021 änderte sich dies dahingehend, dass aufgrund einer  Umstrukturierung die in Deutschland ansässige KI Lexnor AG  und die in Österreich ansässige  Valgarttra-Sanitär GmbH  Gesellschafter der Bf wurden.

**False Positives:**

- `Umstrukturierung die in Deutschland ansässige KI Lexnor AG` — partial — gold is substring of pred: `KI Lexnor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexnor AG`(organisation)
- `Valgarttra-Sanitär GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_82`)


Aufgrund einer Umstrukturierung wurden Ende 2021 die in Deutschland ansässige KI Lexnor AG  und die in Österreich ansässige Valgarttra-Sanitär GmbH  Gesellschafter der Bf.

**False Positives:**

- `Deutschland ansässige KI Lexnor AG` — partial — gold is substring of pred: `KI Lexnor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexnor AG`(organisation)
- `Valgarttra-Sanitär GmbH`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_58`)


Der Bf. übermittelte mit gleichem Schreiben weiters eine Kopie einer Auftragsbestätigung der  Deniz-Bank AG auf der lediglich der Stempel paid-bezahlt sowie das Datum 30.12.2015  aufscheint.

**False Positives:**

- `Bank AG` — partial — pred is substring of gold: `Deniz-Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Deniz-Bank AG`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_50`)


Aus den niederschriftlichen Aussagen des Vorstandes der Demircan Metall AG ist klar erkennbar, dass es  zentrale Strategie sämtlicher Beteiligungsmodelle AbisJ ist, sich an solchen  Zielkapitalgesellschaften zu beteiligen, die im Jahr der Beteiligung Verlustzuweisungen in Höhe  von nahezu 200 % der atypisch stillen Einlage an AbisJ garantieren können, ja, dass das  Eingehen einer Beteiligung durch AbisJ an einer Zielgesellschaft von einer vorrangigen  Verlustzuweisung in der von den Modellinitiatoren geforderten Höhe abhängig gemacht wird.

**False Positives:**

- `Aus den niederschriftlichen Aussagen des Vorstandes der Demircan Metall AG` — partial — gold is substring of pred: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_61`)


Die an AbisJ zugewiesenen Verluste aus der atypisch stillen Beteiligung an Demircan Metall AG sind daher gem.  § 2 Abs. 2a EStG 1988 nicht ausgleichs- und vortragsfähig.

**False Positives:**

- `Die an AbisJ zugewiesenen Verluste aus der atypisch stillen Beteiligung an Demircan Metall AG` — partial — gold is substring of pred: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_79`)


Zentrales Element der Verhandlungen im Zuge des Abschlusses der atypisch stillen  Beteiligungen sei die Wertbestimmung der Demircan Metall AG und damit das Beteiligungsverhältnis der  Investoren gewesen.

**False Positives:**

- `Zentrales Element der Verhandlungen im Zuge des Abschlusses der atypisch stillen  Beteiligungen sei die Wertbestimmung der Demircan Metall AG` — partial — gold is substring of pred: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_115`)


Die Demircan Metall AG ist eine kleine Aktiengesellschaft im Sinne des § 221 UGB und hat ihren Sitz in Ort4, BL.

**False Positives:**

- `Die Demircan Metall AG` — partial — gold is substring of pred: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_136`)


Bezogen auf die tatsächlich geleistete Einlage von gesamt € 1.300.000,00 ausgehend vom  einvernehmlich zugrunde gelegten Verkehrswert der Demircan Metall AG in Höhe von € 70.143.518,50 zum  Stichtag des Zusammenschlusses – beträgt die Beteiligungsquote jedoch 1,8196 %.

**False Positives:**

- `Verkehrswert der Demircan Metall AG` — partial — gold is substring of pred: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Demircan Metall AG`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_252`)


Der Gewinn und Verlust der Mitunternehmerschaft wird somit gem. § 188 BAO einheitlich und  gesondert festgestellt. In diesem Feststellungsbescheid wird der steuerliche Gewinn bzw.  Verlust auf die AG und die stillen Mitunternehmerinnen aufgeteilt. Die Mitunternehmerschaft  ist hierbei Subjekt der Einkunftserzielung.

**False Positives:**

- `Verlust auf die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_12`)


Mit Beschwerdevorentscheidung vom 23. April 2019 wies die belangte Behörde die  Beschwerde als unbegründet ab und führte in einer gesonderten Bescheidbegründung aus, die  der ÖBB-Infrastruktur AG in § 50 Abs. 2 Bundesbahngesetz eingeräumte Befreiung erstrecke  sich in Bezug auf die Grunderwerbsteuer bei einem Grundstückserwerb durch [Hervorhebung  im Original] die ÖBB-Infrastruktur AG auch auf den Vertragspartner.

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB-Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB-Infrastruktur AG`(organisation)
- `ÖBB-Infrastruktur AG`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_13`)


In den erläuternden  Bemerkungen werde dazu ausgeführt, dass bei einem Grundstückserwerb durch die ÖBB- Infrastruktur AG von einem nicht abgabenbefreiten Verkäufer ansonsten die Abgabe vom  Verkäufer zu leisten wäre und würde daher entsprechend auf den Grundpreis umgelegt  werden (bzw würde auf Grund der vertraglichen Regelung, dass der Erwerber die  Grunderwerbsteuer zu zahlen hat, zivilrechtlich die ÖBB-Infrastruktur AG zur Leistung der  Abgabe verpflichtet sein).

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB- Infrastruktur AG`
- `Infrastruktur AG` — similar text (different position): `ÖBB- Infrastruktur AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB- Infrastruktur AG`(organisation)
- `ÖBB-Infrastruktur AG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_39`)


Zu Spruchpunkt I. (Abweisung)  Strittig ist im Beschwerdefall, ob die in § 50 Abs. 2 letzter Satz Bundesbahngesetz normierte  Abgabenbefreiung hinsichtlich der Grunderwerbsteuer nur aus Anlass der  Grundstückserwerbe, die durch die ÖBB-Infrastruktur AG anfallen, zur Anwendung gelangt  oder auch solche Grundstückserwerbe erfasst, bei denen der Erwerber von der ÖBB- Infrastruktur AG erwirbt.

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB-Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB-Infrastruktur AG`(organisation)
- `ÖBB- Infrastruktur AG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_40`)


§ 50 Abs. 2 Bundesbahngesetz in der auf den Beschwerdefall anzuwendenden Fassung BGBl. I  Nr. 95/2009 lautet (Hervorhebung durch das Bundesfinanzgericht):  „Die ÖBB-Infrastruktur AG ist von bundesgesetzlichen Abgaben mit Ausnahme der  Umsatzsteuer, von den Bundesverwaltungsabgaben sowie den Gerichts- und  Justizverwaltungsabgaben befreit, soweit sich diese Abgaben und Gebühren aus der Erfüllung  der jeweiligen in diesem Bundesgesetz vorgesehenen Aufgaben dieser Gesellschaft ergeben.

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB-Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB-Infrastruktur AG`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_42`)


Die Abgabenbefreiung erstreckt sich in  Bezug auf die Grunderwerbsteuer, die aus Anlass eines Grundstückserwerbes durch die ÖBB- Infrastruktur AG anfällt, auch auf den jeweiligen Vertragspartner.“

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB- Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB- Infrastruktur AG`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_43`)


In den Erläuternden Bemerkungen, 227 BlgNr XXIV. GP, S. 5f zu Z 27 (§ 50), zur Novelle BGBl. I  Nr. 95/2005, heißt es dazu:  „[…] Hinsichtlich des Erwerbes von Grundstücken durch die ÖBB-Infrastruktur AG soll schließlich  die Abgabenbefreiung bezüglich der Grunderwerbsteuer auch für die Vertragspartner der ÖBB- Infrastruktur AG gelten.

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB-Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB-Infrastruktur AG`(organisation)
- `ÖBB- Infrastruktur AG`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_44`)


Bei einem Grundstückserwerb durch die ÖBB-Infrastruktur AG von  einem nicht abgabenbefreiten Verkäufer wäre ansonsten die Abgabe vom Verkäufer zu leisten  und würde daher entsprechend auf den Grundpreis umgelegt werden.

**False Positives:**

- `Infrastruktur AG` — partial — pred is substring of gold: `ÖBB-Infrastruktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB-Infrastruktur AG`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/146676.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146676.1_76`)


Entsprechend der rechtlichen Ausführungen waren daher für das beschwerdegegenständliche  Veranlagungsjahr 2021 nachstehende Berechnungen (Hoch-/Umrechnung ohne Bezüge der  Oßwald Getränke AG  und Kontrollrechnung) anzustellen:  5 von 7 Seite 6 von 7

**False Positives:**

- `Umrechnung ohne Bezüge der  Oßwald Getränke AG` — partial — gold is substring of pred: `Oßwald Getränke AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oßwald Getränke AG`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/147920.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147920.1_48`)


Die Einkünfte der Bf als Angestellte der Post AG im Jahr 2018 stellen Einkünfte aus  nichtselbständiger Arbeit gemäß § 25 Abs 1 Z 1 lit a EStG 1988 dar.

**False Positives:**

- `Die Einkünfte der Bf als Angestellte der Post AG` — partial — gold is substring of pred: `Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Post AG`(organisation)

</details>

---

## `Technical University` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `13d33e0c`  
**Description:**
Matches Technical Universities (FH) like FH Kärnten, ensuring the name follows FH.

**Content:**
```
\bFH\s+[A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\s]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 47 | 0 | 47 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 47 | 5043 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_5`)


Der Bf. unterrichtete an der FH von  18.3.2019 bis 31.05.2019 Mikroökonomie im Umfang von 67 Lehreinheiten.

**False Positives:**

- `FH von  ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_18`)


Die Rückzahlung der im Zusammenhang mit der Lehrtätigkeit an der FH  Vorarlberg geleisteten Lohnsteuer sei auch in den Vorjahren stets anstandslos erfolgt.

**False Positives:**

- `FH  Vorarlberg geleisteten Lohnsteuer sei auch in den Vorjahren stets anstandslos erfolgt` — partial — gold is substring of pred: `FH  Vorarlberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH  Vorarlberg`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_19`)


Es gebe  keinen Grund weshalb das FA nun das Antragsjahr 2019 ablehnend behandelt.   Aus dem mit der FH abgeschlossenen Dienstvertrag für nebenberufliche Lehrbeauftragte  gemäß § 7 FHStG ergebe sich zweifelsfrei, dass dem Lehrbeauftragten die Abhaltung der  Lehrveranstaltungen auf selbständiger und eigenverantwortlicher Basis obliege und dieser sich  2 von 5 Seite 3 von 5

**False Positives:**

- `FH abgeschlossenen Dienstvertrag für nebenberufliche Lehrbeauftragte  ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_21`)


Die FH stelle  lediglich die Vorlesungsräume zur Verfügung.

**False Positives:**

- `FH stelle  lediglich die Vorlesungsräume zur Verfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_32`)


Da nach den Ermittlungsergebnissen des BFG keine Zweifel bestanden, dass dem Bf. im  Rahmen seiner Lehrtätigkeit an der Fachhochschule die Eigenschaft eines Grenzgängers im  Sinne des Art. 15 Abs. 6 DBA-Deutschland zukommt, wurde von der belangten Behörde das  ausdrückliche Einverständnis erteilt, dass aus diesem Rechtsgrunde im Jahr 2019 dem  Ansässigkeitsstaat Deutschland das Besteuerungsrecht an den nichtselbständigen Einkünften  aus der Tätigkeit bei der FH Dornbirn zukommt und demgemäß dem Antrag stattzugeben sei.

**False Positives:**

- `FH Dornbirn zukommt und ` — partial — gold is substring of pred: `FH Dornbirn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Dornbirn`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_39`)


Über die Streitfrage, ob die im Abzugswege erhobene Lohnsteuer aus der Lehrtätigkeit an der  FH Dornbirn im Jahr 2019 gemäß dem Antrag vom 3.3.2020 an den Bf. zurückzuzahlen ist,  wurde von den Streitparteien Einvernehmen erzielt.   Die „Nichtselbständigkeit“ einer Person ist ein spezieller steuerrechtlicher Ausdruck, der  gemäß Art 3 Abs. 2 DBA-Deutschland nach dem innerstaatlichen Steuerrecht des  Anwenderstaates auszulegen ist.

**False Positives:**

- `FH Dornbirn im Jahr ` — partial — gold is substring of pred: `FH Dornbirn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Dornbirn`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_55`)


Zusammenfassend ist festzuhalten, dass die nichtselbständigen Einkünfte des Bf. aus der  nebenberuflichen Lehrtätigkeit an der FH im Jahr 2019 auf Grund der Verwirklichung des  Tatbestandes nach Art. 15 Abs. 6 DBA-Deutschland (Grenzgänger) nicht der finalen  Besteuerung der Republik Österreich unterliegen und daher die von der Vergütung  einbehaltene Lohnsteuer gemäß Art 27 DBA-Deutschland antragsgemäß zurückzuzahlen ist.

**False Positives:**

- `FH im Jahr ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_14`)


Dagegen brachte die Bf. eine Beschwerde mit folgender Begründung ein:  „Meine Tochter S hat sowohl davor an der Uni Wien als auch in der Zeit von März 2017 bis  September 2019 an der FH St. Pölten soziale Arbeit studiert und die erforderlichen Prüfungen  absolviert.

**False Positives:**

- `FH St` — partial — pred is substring of gold: `FH St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH St. Pölten`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_29`)


Mit Wintersemester 2017/18 inskribierte sie an der FH St. Pölten den  Weiterbildungslehrgang „Sozialpädagogik", welcher noch besucht wird.

**False Positives:**

- `FH St` — partial — pred is substring of gold: `FH St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH St. Pölten`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_31`)


Erst mit dem Studium ab  September 2017 an der FH St. Pölten liegt wieder eine Berufsausbildung vor.

**False Positives:**

- `FH St` — partial — pred is substring of gold: `FH St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH St. Pölten`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_50`)


Ab September 2019 war S an der FH St. Pölten für den akademischen Lehrgang Sozialpädagogik  inskribiert.

**False Positives:**

- `FH St` — partial — pred is substring of gold: `FH St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH St. Pölten`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_83`)


Aus folgenden Gründen wurde der Nachweis für den Streitzeitraum März 2017 bis August 2017  nicht erbracht:  Da in diesem Zeitraum keine einzige Prüfung abgelegt wurde und die Tochter der Bf. ab  September 2017 an der FH St. Pölten ein anderes Studium begann und sich im November 2018  von diesem vorigen Studium abmeldete, vermochte die Bf. betreffend den  Beschwerdezeitraum März 2017 bis August 2017 nicht nachzuweisen, dass von ihrer Tochter   6 von 7 Seite 7 von 7

**False Positives:**

- `FH St` — partial — pred is substring of gold: `FH St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH St. Pölten`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_9`)


Krankenpflege in der Fachhochschule D GmbH (kurz: FH Sbg) anzumelden, habe sie sich für den  ehest möglichen Aufnahmetermin beworben und dieser sei nicht früher möglich gewesen, als  für das Sommersemester ab März 2021 (zuvor sei das Aufnahmeprozedere erfolgt).

**False Positives:**

- `FH Sbg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_10`)


Die  Anmeldung bei der FH Sbg sei im August bis September 2020 erfolgt und am 11.11.2020 habe  sie das Aufnahmegespräch online geführt.

**False Positives:**

- `FH Sbg sei im August bis September ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_13`)


So habe sie bereits im Vorfeld ein dreimonatiges Praktikum bei der GmbH  (kurz: P), einer Einrichtung für beeinträchtige Menschen, ausgeübt, um sich dieses für die  Ausbildung an der FH im Rahmen der Ausbildung anrechnen zu lassen, da im Curriculum des  Studienganges mehrere Pflichtpraktika vorgesehen seien.

**False Positives:**

- `FH im Rahmen der Ausbildung anrechnen zu lassen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_24`)


Anschluss daran bei der FH beworben, somit gelte die Ausbildung als begonnen.

**False Positives:**

- `FH beworben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_26`)


Mit Beschwerdevorentscheidung vom 07.02.2022 erfolgte die Abweisung der Beschwerde:  Die Absolvierung des Praktikums im Zeitraum 01.07.2020 bis 30.09.2020 bei P bzw die Arbeit  von 04.11.2020 bis 28.02.2021 bei der Stadt D im Gesundheitsamt seien nicht Voraussetzung  für eine Aufnahme in den Bachelor-Studiengang Gesundheits- und Krankenpflege der FH Sbg  und es handle sich dabei um keine schulischen oder kursmäßigen Ausbildungen.

**False Positives:**

- `FH Sbg  und es handle sich dabei um keine schulischen oder ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_33`)


Das BFG richtete an die Bf am 15.04.2022 einen Vorhalt folgenden Inhalts:  Sie werde ersucht, eine Bestätigung der FH Sbg über eine bereits erfolgte Anrechnung des von  ihrer Tochter T bei P absolvierte Praktikums für das Bachelorstudium „Gesundheits- und  Krankenpflege“ (Anrechnungsbescheid sowie ein Nachweis darüber, dass das Praktikum einen  verpflichtend zu absolvierenden Teil des Studiums darstellt/Eintragung in den Erfolgsnachweis)  oder eine Bestätigung der FH Sbg darüber, dass bzw in welchem (zukünftigen) Semester das  genannte Praktikum der Tochter aufgrund welcher Rechtsgrundlage konkret als zu  absolvierendes Pflichtpraktikum anrechenbar ist, vorzulegen.

**False Positives:**

- `FH Sbg über eine bereits erfolgte Anrechnung des von  ihrer Tochter T bei P absolvierte Praktikums für das Bachelorstudium` — no gold match — likely missing annotation
- `FH Sbg darüber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_41`)


Das Praktikum 1 sei daher am 20.09.2021 und Praktikum 2 am 23.03.2022 seitens der  FH eingetragen worden – siehe Erfolgsnachweis SS 2021 und WS 2021/2022.

**False Positives:**

- `FH eingetragen worden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_44`)


Die Praktikumsbestätigung der FH Sbg könne daher nicht im Vorhinein –  für zukünftige Semester bzw noch nicht absolvierte Semester erfolgen.

**False Positives:**

- `FH Sbg könne daher nicht im Vorhinein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_58`)


Die FH hätte daher  auch von den erbrachten Stunden im Zeitraum 01.07.2020 – 30.09.2020 (520 Stunden) 275  Stunden 11(ECTS) für das Praktikum 1 und Praktikum 2 anrechnen können.

**False Positives:**

- `FH hätte daher  auch von den erbrachten Stunden im Zeitraum ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_70`)


Der Vorhaltsbeantwortung der Bf vom 08.07.2022 ist dazu Folgendes zu entnehmen:  Anbei werde die Praktikumsbestätigung der FH Sbg , welches sich die Tochter T anrechnen  habe lassen, übermittelt. Diesbezüglich werde auf die letzte Vorhaltsbeantwortung verwiesen,  wonach die FH Sbg auch die erbrachten Stunden bzw einen Teil der Stunden vom Jahr 2020  hätte anrechnen können.

**False Positives:**

- `FH Sbg` — no gold match — likely missing annotation
- `FH Sbg auch die erbrachten Stunden bzw einen Teil der Stunden vom Jahr ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_73`)


Sollte dies aber notwendig sein, müsste die Bf sich einen Termin auf  der FH Sbg vereinbaren, um zu klären, warum dieser Aufwand betrieben werden sollte, sofern  es überhaupt noch möglich sei.

**False Positives:**

- `FH Sbg vereinbaren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_78`)


Übermittelt werde noch die Bestätigung über die Eignung der Praktikumsstelle, welche die FH  Sbg (Formular der FH Sbg) verlangt habe, was beweise, dass sich P als Praktikumsstelle eigne  und somit das Praktikum von der FH Sbg im Rahmen der Ausbildung/Studium verlangt  werde/worden sei.

**False Positives:**

- `FH  Sbg` — no gold match — likely missing annotation
- `FH Sbg` — no gold match — likely missing annotation
- `FH Sbg im Rahmen der Ausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_143`)


Nach Abbruch eines Studiums im Dezember 2019 ist T seit 01.03.2021 an der FH Sbg als  Studentin im Studiengang „Gesundheits- und Krankenpflege“ inskribiert.

**False Positives:**

- `FH Sbg als  Studentin im Studiengang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_145`)


Dieses Studium umfasst an der FH Sbg sechs Semester und sieht 2.300 Praktikumsstunden  studienbegleitend vor.

**False Positives:**

- `FH Sbg sechs Semester und sieht ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_147`)


Die Bewerbung für einen Studienplatz an der FH Sbg erfolgt ausschließlich online.

**False Positives:**

- `FH Sbg erfolgt ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_156`)


Die Anmeldung bei  der FH erfolgte in den Monaten August und September 2020 und am 11.11.2020 führte sie das  Aufnahmegespräch online.

**False Positives:**

- `FH erfolgte in den Monaten August und September ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_179`)


Ein(e)/e) Anrechnungsbescheid (-bestätigung) wurde von der FH Sbg nicht ausgestellt.  In der Zeit von 04.11.2020 bis 28.02.2021 arbeitete sie am Gesundheitsamt der Stadt D.  Während des Streitzeitraumes Februar 2020 bis Februar 2021 war T des Weiteren mehrfach als  geringfügig beschäftigt gemeldet.

**False Positives:**

- `FH Sbg nicht ausgestellt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_181`)


Seit März 2021 erfolgt wiederum die  Auszahlung der Familienbeihilfe für die Tochter T.  Dieser vom BFG als richtig angesehene Sachverhalt beruht auf folgenden unbedenklichen  Beweismitteln: Angaben der Bf, Inskriptionsbestätigung der FH vom 08.03.2021 und  Erfolgsnachweis der FH Sbg vom 29.10.2021 und vom 26.04.2022, Praktikumsbestätigung der P  vom 30.12.2021, eMail vom 27.10.2021 und vom 26.04.2022 der FH betreffend Anrechnung,  Praktikumsbestätigungen der FH Sbg vom 26.04.2022 und vom 07.07.2022, Verlaufsprotokoll,  Bestätigung Eignung der Praktikumsstelle, Praktikumsbeurteilung, Internetrecherche (P, D,  https://de.wikipedia.org/wiki/covid-19-Pandemie_in_Österreich,  https://de.statista.com/statistik/daten/studie/1103813/umfrage/erkrankungs-und- todesfaelle-aufgrund-des-coronavirus-in-spanien/, https://de.wikipedia.org/wiki/Au-pair),  Abfrage in der Familienbeihilfendatenbank, Bescheid über die Rückforderung zu Unrecht  bezogener Beträge vom 13.02.2020 und Sozialversicherungsabfrage.

**False Positives:**

- `FH vom ` — no gold match — likely missing annotation
- `FH Sbg vom ` — no gold match — likely missing annotation
- `FH betreffend Anrechnung` — no gold match — likely missing annotation
- `FH Sbg vom ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_230`)


Zusätzlich werden in § 7 FH GuK-AV Mindestanforderungen an die Praktikumsanleitung  festgeschrieben.

**False Positives:**

- `FH GuK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_236`)


Es kam im Zusammenhang mit diesem Praktikum allerdings nicht zu einer  förmlichen Beurteilung des Kompetenzerwerbs der Tochter anhand einer entsprechenden,  ebenfalls zu beurteilenden Dokumentation dieses Kompetenzerwerbs durch die Führung eines  Ausbildungsprotokolls (vgl § 41 Abs 2 Z 3 u 4 FH GuK-AV).

**False Positives:**

- `FH GuK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_238`)


Dies erklärt sich schon daraus, dass die  „erfolgreiche“, sprich nicht negative, Absolvierung sämtlicher Praktika (100%  Anwesenheitszeit) und auch die positive Beurteilung der Praktikumsdokumentation nach der  FH-GuK-AV Voraussetzung für die Zulassung zur kommissionellen Bachelorprüfung ist (vgl § 4  Abs 2 Z 5 FH GuK-AV).

**False Positives:**

- `FH GuK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_242`)


Damit entspricht dieses im Sommer 2020 noch vor Aufnahme des Bachelorstudiums  „Gesundheits- und Krankenpflege absolvierte Praktikum, das auch nicht Teil einer anderen  Ausbildung zu einem Gesundheitsberuf war (vgl § 60 GuKG), nicht den besonderen  Anforderungen, die in der FH GuK-AV festgelegt sind.

**False Positives:**

- `FH GuK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_41`)


Neben seiner Tätigkeit als Test Development Engineer absolviert der Bf. seit dem  Wintersemester 2019 das Studium Systems Engineering an der Fachhochschule Villach (kurz FH  Villach).

**False Positives:**

- `FH  Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_48`)


Bedingt durch die Lockdown-Maßnahmen ab März 2020 wurde das Studium ab 03/2020 im  Distance Learning abgewickelt. Lediglich für Prüfungsvorbereitungen, Prüfungen und  Laborübungen war eine Anwesenheit am Standort der FH Villach zugelassen.

**False Positives:**

- `FH Villach zugelassen` — partial — gold is substring of pred: `FH Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Villach`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_92`)


Kann also die Verpflegung am auswärtigen (Tätigkeits-)Ort zu den gleichen Bedingungen wie an  der ständigen Arbeitsstätte in Anspruch genommen werden, stehen Tagesgelder nicht zu.  3. Da seit Studienbeginn im Oktober 2019 an der FH Villach dieser Ort wiederholt angefahren  wurde, was erst mit Beginn des Lockdown im März 2020 reduziert wurde, war ab bzw. im  Jänner 2020 in Villach streitgegenständlich ein als weiterer Mittelpunkt der Tätigkeit zu  qualifizierender Ort gegeben.

**False Positives:**

- `FH Villach dieser Ort wiederholt angefahren  wurde` — partial — gold is substring of pred: `FH Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Villach`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_29`)


Absolvierte Fortbildungen   Ich absolvierte in den angeführten Veranlagungsjahren folgende Fortbildungen:   - FH des bfi Wien - 1.

**False Positives:**

- `FH des bfi Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_32`)


- FH WN - 2. Halbjahr 2011 bis 1. Halbjahr 2013: Ich studierte an der Fachhochschule  Wiener Neustadt den Studiengang „Wirtschaftsberatung und Unternehmensführung"  mit der Spezialisierung „Unternehmensrechnung und Revision".

**False Positives:**

- `FH WN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Fachhochschule  Wiener Neustadt`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_35`)


Während meines Studiums an der FH Wiener Neustadt absolvierte ich die folgenden drei  Leadership-Trainings:   3 von 13 Seite 4 von 13

**False Positives:**

- `FH Wiener Neustadt absolvierte ich die folgenden drei  Leadership` — partial — gold is substring of pred: `FH Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Wiener Neustadt`(organisation)

</details>

---

## `Federal Court of Finance Genitive` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b2011169`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive) and 'Bundesfinanzgericht'.

**Content:**
```
\bBundesfinanzgericht(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Verlag Steinval GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b97e2572`  
**Description:**
Matches the specific company 'Verlag Steinval GmbH' and its variation 'Verlag Steinval GmbH& Co KG'.

**Content:**
```
\bVerlag\s+Steinval\s+GmbH(?:\s+&\s+Co\.?\s+KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Rs Dilly's Wellnesshotel GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f3dd282`  
**Description:**
Matches the specific company 'Rs Dilly's Wellnesshotel GmbH'.

**Content:**
```
\bRs\s+Dilly's\s+Wellnesshotel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Burtscher Wachter GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7ed19300`  
**Description:**
Matches 'Burtscher Wachter Wirtschaftstreuhand und Steuerberatungs- GmbH'.

**Content:**
```
\bBurtscher\s+Wachter\s+Wirtschaftstreuhand\s+und\s+Steuerberatungs-?\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Complex Company Name GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fdfeac2d`  
**Description:**
Matches complex company names like 'fh-wirtschaftstreuhand GmbH Steuerberatungsgesellschaft'.

**Content:**
```
\b(?:[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s-]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s-]+)*\s+GmbH\s+Steuerberatungsgesellschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Railway Pension Service` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a92355e5`  
**Description:**
Matches 'ÖBB Pensionsservice' and similar railway pension entities.

**Content:**
```
\bÖBB\s+Pensionsservice\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

## `Energy Company Generic` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `372546b4`  
**Description:**
Matches company names ending in 'Energie' (e.g., Wagenführer Energie) only when preceded by a specific name or determiner, avoiding common nouns.

**Content:**
```
(?:^|\s|\b)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s-]+\s+Energie)(?=\s+(?:hat|ist|wurde|hatte|sind|waren|kann|konnte|muss|musste|wird|werden|haben|hatten|soll|sollte|dass|oder|und|zu|von|mit|auf|in|an|bei|f\u00fcr|\.|,|\)|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 5043 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_5`)


Für den Betrieb der Anlage bezieht die Bf elektrische Energie von der EVN.

**False Positives:**

- `Für den Betrieb der Anlage bezieht die Bf elektrische Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_157`)


Für die von der Bf selbst erzeugte und sodann gelieferte elektrische Energie hat die  Bf keine Vergütung beansprucht.

**False Positives:**

- `Für die von der Bf selbst erzeugte und sodann gelieferte elektrische Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_63`)


Laut der Anzeige war das Elektrofahrzeug des Bf. an die Ladesäule von Wien Energie  angeschlossen.

**False Positives:**

- `Ladesäule von Wien Energie` — partial — gold is substring of pred: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_443`)


Zudem gestattet die Verordnung das Beibehalten von erlassenen gleichwertigen nationalen  Maßnahmen, die zum 31. Dezember 2022 angenommen und veröffentlicht wurden und die zur  Erschwinglichkeit von Energie beitragen (Art 2 Z 21 iVm Art 14 Abs 2).

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_487`)


Diese werden nämlich in Art 2 Z 21 der Verordnung  als "erlassene gleichwertige nationale Maßnahme[n]" definiert, wenn es sich um eine bis zum  31. Dezember 2022 erlassene und veröffentlichte Rechts- oder Verwaltungsmaßnahme  handelt, die zur Erschwinglichkeit von Energie beiträgt, ohne dass für diese Einstufung weitere  Kriterien aufgestellt würden.

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_56`)


Die Versorgung mit elektrischer Energie     und Erdgas über die vorhandenen Anschüsse des örtlichen     Energieversorgungsunternehmens erfolgen.

**False Positives:**

- `Die Versorgung mit elektrischer Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Fa. Company Abbreviation` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5332c40b`  
**Description:**
Matches company names abbreviated with 'Fa.' (Firma) followed by a capitalized name and 'GmbH', handling cases like 'Fa. Klahsen & Schehr Marine GmbH' and 'Fa.Combach Textil GmbH'.

**Content:**
```
\bFa\.?\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+)*\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 5043 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_14`)


Im Außenprüfungsbericht vom 13.9.2012 finden sich unter Tz 5 folgende Ausführungen:  „…[Der Beschwerdeführer] hat für seine Geschäftsführertätigkeit von der Fa. Schilift GmbH nie  eine Geschäftsführervergütung bzw. nichtselbständige Einkünfte (Beteiligung = 9 %) erhalten.

**False Positives:**

- `Fa. Schilift GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145892.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145892.1_17`)


Eine Option iSd § 1  Abs. 4 EStG sei nicht möglich, da die Einkünfte, die nicht der österreichischen ESt unterliegen (=  ausländischer Anteil der Einkünfte bei der Fa. Huber Transporte GmbH), mehr als € 11.000  betragen würden.

**False Positives:**

- `Fa. Huber Transporte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_510`)


In der Pilzmischung der Fa. Orthotherapia GmbH ist  Lutein als Inhaltsstoff angeführt, von Theodora Hartzheim, BA Bakk. phil. wurde Lutamax (Inhaltsstoff ebenfalls Lutein) als 6  Monatskur verordnet.

**False Positives:**

- `Fa. Orthotherapia GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)

</details>

---

## `Company Suffix m.b.H` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `23001a21`  
**Description:**
Matches generic company names ending in 'm.b.H.' using context anchors that are less restrictive than verbs.

**Content:**
```
(?:^|\s|\b)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s&]+)*\s+Gesellschaft\s+m\.b\.H\.?)(?=\s+(?:vom|von|am|im|mit|auf|in|zu|bei|f\u00fcr|\d{1,2}\.\s*\w+\s*\d{4}|\.|,|\)|\]|\n|$)|\s+(?:hat|ist|wurde|hatte|sind|waren|kann|konnte|muss|musste|wird|werden|haben|hatten|soll|sollte|dass|oder|und|zu|von|mit|auf|in|an|bei|f\u00fcr|\.|,|\)|\]|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1893, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_106`)

Am  23. Dezember 2010 schloss die Bf. mit der **Demircan Metall AG** einen Zusammenschlussvertrag über die  9 von 29 Seite 10 von 29

- missed: `Demircan Metall AG` (organisation)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_545`)

nochmals auf die wiederholte – erfolglose – Beantragung einer  Prüfung bei der **Nieder Waldbach GmbH**  um aufzuzeigen, das Manipulationen zwischen den Standorten nicht  stattgefunden hätten.

- missed: `Nieder Waldbach GmbH` (organisation)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_65`)

In einem Aktenvermerk der steuerlichen Vertretung vom 20.8.2015 (s. Beil.) sei folgender  Sachverhalt festgehalten:  „Bei der Leroy Sitterle  handelt es sich um eine Personengesellschaft, die seit 2005 aus Biogas  Strom erzeugt und diesen zu 100 % an die Ömag (Abwicklungsstelle für **Ökostrom AG**) liefert.

- missed: `Ökostrom AG` (organisation)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_184`)

Dieser Wert bildete die Grundlage für die Berechnung der Einfuhrumsatzsteuer, welche vom  Zollamt vorgeschrieben und von der **RHO Pharma** Lamperstätten  bezahlt wurde.

- missed: `RHO Pharma` (organisation)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_205`)

In diesem Zusammenhang übermitteln wir Ihnen nunmehr zwei Aufstellungen (Beilage 4 und  5), die auf Basis eines von der Firma **Inn Trikraftglanz**  geführten Buches erstellt (das bereits im Zuge  der Außenprüfung vorgelegt wurde) wurden.

- missed: `Inn Trikraftglanz` (organisation)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_93`)

Auch weitere Ausführungen in dieser Entscheidung entsprechen nicht der Rechtsauffassung  der AP, so etwa:  "Die Bf. gab der Unter-Pflege GmbH ihre österreichische Umsatzsteuer-Identifikationsnummer bekannt,  damit konnte die **Unter-Pflege GmbH** ihre Lieferung nicht mehr als steuerfreie innergemeinschaftliche  Lieferung behandeln und stellte daher Umsatzsteuer in Rechnung."

- missed: `Unter-Pflege GmbH` (organisation)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_155`)

Der in der  Anfrage der **Möbel Zorkelglanz GmbH** an das do. Finanzamt angeführte Sachverhalt entspreche nicht der  Vereinbarung und dem gesetzten Sachverhalt. Zu diesem Thema könnte auch Herrn DI O.C.  zeugenschaftlich befragt werden.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: `Der in der  Anfrage der Möbel Zorkelglanz GmbH`, `Finanzamt`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_180`)

Da  im Namen der Furtnor-Handel GmbH massive Malversationen getätigt wurden, wurde seitens der  Finanzprokuratur mit Schriftsatz am 31.8.2012 das Ersuchen um Konkurseröffnung gestellt.  Eröffnung des Konkurses: x.2012 HG  Die tatsächlichen Urheber der bei der Firma **Starnberg Beratung GmbH** aufliegenden Scheinrechnungen  konnten im Prüfungsverfahren mangels entsprechend zweckdienlicher Auskünfte durch die  Geschäftsleitung nicht in Erfahrung gebracht werden.

- missed: `Starnberg Beratung GmbH` (organisation)
- predicted in sentence: `HG  Die tatsächlichen Urheber der bei der Firma Starnberg Beratung GmbH`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_110`)

Die von der RHO Pharma  eingeführten Arbeitsbühnen wurden in Österreich mit der Vermietung  an Kunden der **RHO Pharma**  zur Erzielung von steuerpflichtigen Umsätzen verwendet.

- missed: `RHO Pharma` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_438`)

Berufungsentscheidung UFS 2.02.2012, GZ. RV/1022 bis 1026-W/10  Mit der Berufungsentscheidung des Unabhängigen Finanzsenates UFS 2.02.2012, GZ. RV/1022  bis 1026-W/10, wurde die Beschwerde gegen die Bescheide des **FA Wien 9/18/19  Klosterneuburg** vom 30. Oktober 2009 betreffend Umsatzsteuer für das Jahr 2002,  Umsatzsteuer und Körperschaftsteuer jeweils für die Jahre 2003 bis 2005, Wiederaufnahme  der Verfahren gemäß § 303 Abs. 4 BAO hinsichtlich der Umsatzsteuer für die Jahre 2002 bis  2004, Körperschaftsteuer für die Jahre 2003 bis 2004, samt den die Jahre 2003 bis 2005  betreffenden Haftungs- und Abgabenbescheiden des FA Wien 9/18/19 Klosterneuburg vom  30.10.2009 als unbegründet abgewiesen.

- missed: `FA Wien 9/18/19  Klosterneuburg` (organisation)
- predicted in sentence: `FA Wien 9/18`, `FA Wien 9/18`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_17`)

Das (nunmehr zuständige) **Finanzamt für Großbetriebe** hat diesen Antrag mit Bescheid vom  11. Juli 2023 abgewiesen und diese Entscheidung wie folgt begründet: Gemäß § 205a Abs. 3  BAO stünden Beschwerdezinsen insoweit nicht zu, als ein Bescheid in Punkten angefochten  werde, in denen er von dem ihm zu Grunde liegenden Anbringen nicht abweiche.

- missed: `Finanzamt für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamt`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_183`)

Für jene Geräte, die  von Liechtenstein/Schweiz nach Österreich zur Firma **FA Spittal Villach** Lamperstätten  gebracht wurden,  wurden sogenannte "Proformarechnungen" ausgestellt, in welchen das jeweilige Leihgerät mit  dem Zeitwert angeführt wurde.

- missed: `FA Spittal Villach` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/148710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148710.1_12`)

Das **Finanzamt Landeck Reutte** hat zuständigkeitshalber die verfahrensgegenständlichen  Erstbescheide, datiert mit 15. März 2016 erlassen, mit welchen eine Festsetzung des  Dienstgeberbeitrages für die Jahre 2010 bis 2014 sowie von damit in Zusammenhang  stehenden Säumniszuschlägen erfolgte.

- missed: `Finanzamt Landeck Reutte` (organisation)
- predicted in sentence: `Finanzamt`

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_138`)

Die AMS- bzw. **WGKK**- Bezüge waren auch gemäß § 84 bzw. § 3 Abs. 2 EStG 1988 von der  bezugsauszahlenden Stelle (AMS bzw. WGKK) dem Finanzamt zu melden bzw. seien auch  entsprechend gemeldet geworden (siehe ebenfalls Einkommensteuerbescheid für das Jahr  2018).

- missed: `WGKK` (organisation)
- predicted in sentence: `AMS`, `AMS`, `Finanzamt`

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_280`)

Im  Bericht werde der Erwerb der **Nieder Waldbach GmbH** zu diesem Zeitpunkt samt den besagten Verrechnungen  in diesem Zeitraum ignoriert.

- missed: `Nieder Waldbach GmbH` (organisation)
- predicted in sentence: `Im  Bericht werde der Erwerb der Nieder Waldbach GmbH`

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_111`)

Zudem hat der **Europäische Gerichtshof** im Urteil  „Schmelz“, Rs C-97/09, die Ansicht der Generalanwältin nicht geteilt, wonach der Begriff  Ansässigkeit so  auszulegen sei, dass eine Person lediglich einen dauerhaften festen  Bezugspunkt in den betroffenen Staat haben müsse und der Eigentümer einer Immobilie als  ansässiger Steuerpflichtiger zu betrachten sei, auch wenn dieser die Immobilie nicht selbst als  Wohnung nutze.

- missed: `Europäische Gerichtshof` (organisation)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_249`)

(2) Die am 31. Dezember 2020 bei einem Finanzamt oder **Zollamt** anhängigen Verfahren  werden von der jeweils am 1. Jänner 2021 zuständigen Abgabenbehörde in dem zu diesem  Zeitpunkt befindlichen Verfahrensstand fortgeführt.

- missed: `Zollamt` (organisation)
- predicted in sentence: `Finanzamt`

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_79`)

Am 3.12.2009 wurde dann das KFZ auf das Kennzeichen W2 umgemeldet (auf die **Fa.VWWJ IT GmbH**  und scheint seit 2010 im Anlagevermögen der Firma auf.

- missed: `Fa.VWWJ IT GmbH` (organisation)
- predicted in sentence: `VWWJ IT GmbH`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_66`)

5. Anlagenverzeichnis und  Überschussrechnung (Bilanz) der **VWWJ IT GmbH** der Jahre 2007 bis 2009.

- missed: `VWWJ IT GmbH` (organisation)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_314`)

In der Zeugeneinvernahme sei dem Geschäftsführer der **Lemost-Handel GmbH** lediglich eine  Agrarmarktbeschreibung vorgehalten worden.

- missed: `Lemost-Handel GmbH` (organisation)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_118`)

Daher  handle es sich bei den zwischen der **Möbel Zorkelglanz GmbH** und der Bf. um unter gemäß § 3 Abs. 7 UStG  1994 fallende „ruhende“ Lieferungen, weil sich die betreffenden Waren zum Zeitpunkt, indem  die Bf. die Verfügungsmacht erlangte, in Österreich befanden.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: `Daher  handle es sich bei den zwischen der Möbel Zorkelglanz GmbH`

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_8`)

3. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr **Logzor-Event GmbH** in Liquidation) im August 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet habe.

- missed: `Logzor-Event GmbH` (organisation)
- predicted in sentence: `Event GmbH`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_29`)

Formelle Erledigungen wie jene gegenständlichen Beschwerdevorentscheidungen wirken sohin  nicht gemäß § 281 Abs 2 BAO gegenüber der **Gartfentri Heizung Institut GmbH**  Auf Grundlage des von der Gartfentri Heizung Institut GmbH gestellten Vorlageantrages, der als zulässiger Rechtsbehelf  gegen ihr gegenüber erlassenen Beschwerdevorentscheidungen zu werten ist, waren diese  spruchgemäß aufzuheben.

- missed: `Gartfentri Heizung Institut GmbH` (organisation)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_83`)

Im Jahr 2008 wurde am 9. Dezember 2008 im Rahmen der Ermittlungen zum  Feststellungsbescheid 2000 bis 2007 ein Ergänzungsersuchen des FA Neunkirchen Wiener  Neustadt an **Müter u. Barkholt Software GmbH** und Mitges.

- missed: `Müter u. Barkholt Software GmbH` (organisation)
- predicted in sentence: `FA Neunkirchen`, `Barkholt Software GmbH`

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)

Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von Josefine Frikel (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der **Verwaldgart GmbH** bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

- missed: `Verwaldgart GmbH` (organisation)
- predicted in sentence: `Finanzpolizei`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_27`)

**Wiener Gemeindebezirk**, Museumstraße,  Neustiftgasse, Kaiserstraße, Bernardgasse, Lerchenfelder Gürtel.

- missed: `Wiener Gemeindebezirk` (organisation)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_10`)

Entscheidungsgründe  Verfahrensgang:  Der **Magistrat der Stadt Wien, Magistratsabteilung 67** (MA 67) forderte die Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa.Dankwardt Wind AG  mit Schreiben vom 3. September 2019 gemäß § 2 Wiener Parkometergesetz 2006) auf,  der Behörde binnen zwei Wochen ab Zustellung des Schreibens Auskunft darüber zu erteilen,  wem das näher bezeichnete Fahrzeug am 5. Juli 2019 um 17:47 Uhr überlassen war, sodass es  in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Altgasse 25a, stand.

- missed: `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- predicted in sentence: `Dankwardt Wind AG`

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_97`)

 Schreiben des BFG vom 21.01.2024 mit angefügter Stellungnahme der **Nord Ostunisyn GmbH** vom 17.01.2024  Mit Schreiben des BFG vom 21.01.2024, welchem die Stellungnahme der Nord Ostunisyn GmbH vom  17.01.2024 zum Schreiben des BFG vom 2.01.2024 beigelegt war, erging die Mitteilung an die  Verfahrensparteien, dass die Vorlage von Lohnzettel des ehemaligen Dienstgebers des Bf. für  die Jahre 2012 bis 2015 aufgrund der Aktenlage auszuschließen sei, weshalb eine Stattgabe der  Beschwerde u.a. gegen den Einkommensteuerbescheid für das Jahr 2013 nicht zu begründen  sei.

- missed: `Nord Ostunisyn GmbH` (organisation)
- predicted in sentence: `Stellungnahme der Nord Ostunisyn GmbH`, `Stellungnahme der Nord Ostunisyn GmbH`

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_141`)

STT Umwelt  GmbH & Co KG   2009:    Steinkrafttra Heizung  GmbH & Co KG   STT Umwelt  GmbH & Co KG   Drau-Umwelt Entwicklung  GmbH & Co KG   UnterLemglanzlogHandel  GmbH & Co KG  Zu den Ausführungen zu den rückwirkend errichteten Zusammenschlussverträgen wird auf die  Ausführungen in der Entscheidung des BFG vom 29.9.2023, RV/1100433/2013 (Steinkrafttra Heizung  GmbH & Co KG und STT Umwelt  GmbH & Co KG) und in der Entscheidung des BFG vom  29.9.2023, RV/1100437/2013 (Drau-Umwelt Entwicklung  GmbH & Co KG und **UnterLemglanzlogHandel**  GmbH & Co KG)  verwiesen.

- missed: `UnterLemglanzlogHandel` (organisation)
- predicted in sentence: `STT Umwelt  GmbH & Co KG`, `Steinkrafttra Heizung  GmbH & Co KG   STT Umwelt  GmbH & Co KG`, `Umwelt Entwicklung  GmbH & Co KG   UnterLemglanzlogHandel  GmbH & Co KG`, `Steinkrafttra Heizung  GmbH & Co KG und STT Umwelt  GmbH & Co KG`, `Umwelt Entwicklung  GmbH & Co KG und UnterLemglanzlogHandel  GmbH & Co KG`

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_50`)

Im fortgesetzten Verfahren wurden mit dem Schreiben des BFG vom 17.07.2023   (1) das Schreiben der **Nord Ostunisyn GmbH** vom 15.01.2014 (Kopie),   (2) der Report über die Ausübung der Optionen (Kopie),   (3) Informationen über Stock Options (SIP) v. S.P. vom 3.12.2002 (Kopie), (4) die Ausarbeitung  von Deloitte Österreich betreff steuerliche Behandlung von Stock Options        (Kopie), und   5) die Transaktionsbestätigungen der ausgeübten Stock Options zum 31.12.2012 (Kopie), an  die Nord Ostunisyn GmbH versendet.

- missed: `Nord Ostunisyn GmbH` (organisation)
- predicted in sentence: `Schreiben der Nord Ostunisyn GmbH`

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_65`)

Bitte  geben Sie den wöchentlichen Zeitaufwand (in Stunden) bekannt, in dem sich Ihr Sohn im  Beschwerdezeitraum auf die Extremistenprüfung vorbereitet hat:  Hierzu wurden auch bereits schon in diversen Schreiben gegenüber dem Finanzamt Wien  ausführlich Stellungen genommen und verweise unter anderem auf mein Schreiben vom 20.  Juni 2018 an das **Finanzamt Wien Mitte**.

- missed: `Finanzamt Wien Mitte` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt`

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_141`)

Die im  bisherigen Verfahren von der Bf. vorgelegten Unterlagen lassen dies nicht erkennen, zumal  auch der 34-seitige in englischer Sprache vorgelegte Vertrag über den zweiten Umsatz keine  ausreichenden Informationen enthält. Er enthält lediglich Informationen über das  Beschaffungsgeschäft der Bf. bei der **Möbel Zorkelglanz GmbH**  Abgesehen davon hat der VwGH die  reklamierten Gefahrtragungsregelungen und von der bisherigen Verwaltungspraxis  maßgebliche Transportverantwortlichkeit einschließlich Handelsklauseln nicht weiter erörtert,  sondern sich lediglich auf die dem Bundesfinanzgericht damals noch nicht bekannten Rz. 70, 74  und 75 der Rs. Arex, EuGH v. 19.12.2018, C-414/17 gestützt.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_29`)

Die Planung unseres Hauses wurde  gemeinsam mit dem Architekten der **Fa.Nieder Uniost GmbH**  rein nach unseren Vorstellungen  vorgenommen, und wir hatten somit die Gestaltung der Gesamtkonstruktion in unserem  alleinigen Einfluss (VwGH 17.10.2001, 2001/16/0230 bzw. VwGH 29.7.2004, 2004/16/0053).

- missed: `Fa.Nieder Uniost GmbH` (organisation)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_3`)

Begründung  Strittig ist die Zulässigkeit der Inanspruchnahme des Beschwerdeführers als Haftungspflichtiger  für Abgabenschuldigkeiten der **Sudnortri GmbH**

- missed: `Sudnortri GmbH` (organisation)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_499`)

Im Arbeitsbogen sind auf den Seiten 79-90 Unterlagen zur Fa. c enthalten wie Abfragen aus der  Datenbank der Finanzverwaltung, Bescheide betreffend USt-Festsetzungen, Auszug aus dem  Gewerberegister vom 13.6.2013, Bescheid über die Erteilung der Umsatzsteuer- Identifikationsnummer vom 26. Juni 2013, Bescheid (**Zollamt Wien**) vom 8. Juli und 1. August  2013, Lieferatenkonto und eine Rechnung an die Bf. vom 16.8.2013.

- missed: `Zollamt Wien` (organisation)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_779`)

Auch der EuGH hat mit Urteil vom 15.4.2021, Rs C-593/19, "**SK Telecom Co. Ltd**" entschieden,  dass die Verordnung BGBl. II Nr. 383/2003 idF 221/2009 dem Unionsrecht entspricht.

- missed: `SK Telecom Co. Ltd` (organisation)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/147420.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147420.1_6`)

Aufgrund eines Auskunftsersuchens des **Finanzamtes für Großbetriebe** vom 27. Dezember  2022 wurde seitens der Bf. am 7. März 2023 die Berechnungsgrundlage gemäß § 2 StabAbgG  für die Stabilitätsabgabe u.a. für die Jahre 2019 bis 2021 übermittelt.  Daraus ergab sich, dass die Bf. bei Berechnung der Stabilitätsabgabe die in der Bilanz  ausgewiesene Forderung an das Zentralinstitut, entstanden aus der Erfüllung von  Liquiditätshaltungsbestimmungen, von der durchschnittlich unkonsolidierten Bilanzsumme iSd  1 von 6 Seite 2 von 6

- missed: `Finanzamtes für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_11`)

Das Bundesfinanzgericht erklärte die Beschwerde, soweit diese die nachträgliche buchmäßige  Erfassung von Eingangsabgaben (Zoll) betrifft, mit Beschluss vom 26. Mai 2017,  RV/6200002/2017, als zurückgenommen, weil die Bf einem Mängelbehebungsauftrag  (Musteranforderung) innerhalb der vom **Zollamt** gesetzten Frist nicht nachgekommen war, und  sprach aus, dass eine Revision nach Art 133 Abs 4 B-VG nicht zulässig ist.

- missed: `Zollamt` (organisation)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_386`)

Aus den zuvor dargestellten nicht abzugsfähigen „Krankheitskosten“ resultieren  Fahrtkostenkürzungen für nachfolgende Wegstrecken (Entfernungen lt. Bf-Aufstellungen):  - Dr-B: 128,8 km;  - ABC/Ort-10: 218,4 km;  - Ort-11/Krankenhaus an Bürotagen: 147 km (5x 29,4 km Wohnsitz/Arbeitsstätte);  - Ort-5/Privatklinik-X : 54,2 km;   - Ort-5/Physiotherapie (**ÖGK**-Ersatz 22.11.: 147 km/ 6x 29,4 km Wohnsitz/Arbeitsstätte);

- missed: `ÖGK` (organisation)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_728`)

2. Gutschriften/nachträgliche Rabatte Drau Albach Manufaktur GmbH  Das übermittelte Schreiben der **Drau Albach Manufaktur GmbH** betrifft Gutschriften aus den Jahren 2016 bis 2020;

- missed: `Drau Albach Manufaktur GmbH` (organisation)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  **Gueldner Garten**, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Gueldner Garten` (organisation)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_21`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf ist seit dem 4.9.2017 bei der **Vertraal-Technik AG** als Casino Techniker beschäftigt und resultierten  daraus im beschwerdegegenständlichen Jahr 2018 Einkünfte aus nichtselbständiger Arbeit.

- missed: `Vertraal-Technik AG` (organisation)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_251`)

Die gegenständliche Entscheidung ergeht daher an das **Finanzamt Österreich.**

- missed: `Finanzamt Österreich.` (organisation)
- predicted in sentence: `Finanzamt Österreich`

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_118`)

Festgestelltermaßen erklärte das Gruppenmitglied Firma D  derartige Umsätze, weshalb die Zuständigkeit des **Finanzamtes für Großbetriebe** zu bejahen ist.

- missed: `Finanzamtes für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_283`)

Die umfangreichen Ermittlungen der Abgabenbehörde haben ergeben, dass es sich bei den  drei genannten Firmen um Scheinfirmen handelt.   Anzumerken ist in diesem Zusammenhang, dass die in der Beschwerde erwähnte  abgabenrechtliche Beschwerde der **Starnberg Beratung GmbH** gegen den Haftungsbescheid mit ho.

- missed: `Starnberg Beratung GmbH` (organisation)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_25`)

In diesem Zusammenhang bemerkte die Bf., es sei gängige Praxis der **Möbel Zorkelglanz GmbH** gewesen,  sobald sie Kenntnis von einer UID ihrer Kunden erlange, diese in die Kundenstammdaten  aufnehme und entsprechend auf den Rechnungen aufdrucke.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_20`)

Im Zuge der Darlegung des Verfahrensganges erläutert die Bf., dass sie am 21. Februar 2018  von Seiten der **WGKK** rückwirkend für den Zeitraum 1. September 2016 bis 31. Jänner 2018,  somit für die 3 betroffenen Jahre 2016 bis 2018 eine Zahlung i.H.v. € 15.333,52 erhalten habe.

- missed: `WGKK` (organisation)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_43`)

Mit Gesellschaftsvertrag vom xx.xx.2006 wurde die OG (nunmehr OG; **LG Klagenfurt** zu FN  278781y) (erneut) mit dem Sitz in der politischen Gemeinde Ort und der Adresse in Adresse  von Herr B (geb. xx; Beteiligung am Vermögen: 34 %), Herr C (geb. xx; Beteiligung am  Vermögen: 33 %) und Herr A (geb. xx; Beteiligung am Vermögen: 33 %) je als unbeschränkt  haftende Gesellschafter errichtet.

- missed: `LG Klagenfurt` (organisation)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_313`)

Angaben des Geschäftsführers der **Lemost-Handel GmbH** betreffend geänderte Artikelnummern in  Zusammenhang mit der Untersuchung der A-Anstalt: Der steuerliche Vertreter verneinte,  dass der Geschäftsführer der Lemost-Handel GmbH die Entsprechung des Artikel 2190 dem untersuchten  Fleisch der A-Anstalt bestätigt hätte, mit der Begründung, dass dieser das von der A-Anstalt  untersuchte Fleisch ebensowenig wie die Bf. oder dessen steuerliche Vertretung jemals  gesehen habe.

- missed: `Lemost-Handel GmbH` (organisation)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_6`)

Gleichzeitig schlossen die österreichische **Unter-Luftfahrt Institut GmbH** und die liechtensteinische X.AG den  "Kooperationsvertrag K", wonach die X.AG von der Unter-Luftfahrt Institut GmbH mit der Erstellung eines Werbe-  und Marketingkonzepts sowie der Durchführung von Werbe- und Marketingmaßnahmen  1 von 13 Seite 2 von 13

- missed: `Unter-Luftfahrt Institut GmbH` (organisation)
- predicted in sentence: `Luftfahrt Institut GmbH`, `Luftfahrt Institut GmbH`

</details>

---

