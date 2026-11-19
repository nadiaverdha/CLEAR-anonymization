# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-19T16:28:12.755156

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
| Accuracy (exact match) | 98.0% |
| True Positives | 3357 |
| False Positives | 557 |
| False Negatives | 1242 |
| Total Gold Entities | 4599 |
| Micro Precision | 85.8% |
| Micro Recall | 73.0% |
| Micro F1 | 78.9% |
| Macro F1 | 78.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Social Security Agency` | 1.9% | 100.0% | 1.0% | 44 | 44 | 0 |
| `Employment Agency AMS` | 1.8% | 100.0% | 0.9% | 42 | 42 | 0 |
| `Federal Court of Finance` | 5.7% | 100.0% | 3.0% | 136 | 136 | 0 |
| `Pensions Insurance` | 0.9% | 100.0% | 0.5% | 21 | 21 | 0 |
| `Fraud Investigation Office` | 1.6% | 100.0% | 0.8% | 38 | 38 | 0 |
| `Municipal Council` | 1.3% | 100.0% | 0.7% | 30 | 30 | 0 |
| `Health Insurance` | 0.1% | 100.0% | 0.1% | 3 | 3 | 0 |
| `Administrative Court` | 0.8% | 100.0% | 0.4% | 19 | 19 | 0 |
| `Constitutional Court` | 1.6% | 100.0% | 0.8% | 38 | 38 | 0 |
| `Police Authority` | 1.2% | 100.0% | 0.6% | 28 | 28 | 0 |
| `Federal Ministry Finance` | 0.7% | 100.0% | 0.3% | 16 | 16 | 0 |
| `EU Court of Justice` | 0.5% | 100.0% | 0.2% | 11 | 11 | 0 |
| `Complex Company Name GmbH` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Federal Ministry Finance Genitive` | 0.3% | 100.0% | 0.2% | 7 | 7 | 0 |
| `City Magistrate` | 0.5% | 100.0% | 0.3% | 12 | 12 | 0 |
| `Wiener Linien` | 0.1% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Magistrats der Stadt Wien` | 0.9% | 100.0% | 0.5% | 21 | 21 | 0 |
| `Landespolizeidirektion Generic` | 0.7% | 100.0% | 0.3% | 16 | 16 | 0 |
| `Tax Authority Generic` | 73.1% | 92.1% | 60.6% | 3025 | 2785 | 240 |
| `Abbreviated Tax Authority` | 0.8% | 90.0% | 0.4% | 20 | 18 | 2 |
| `Federal Ministry` | 0.3% | 85.7% | 0.1% | 7 | 6 | 1 |
| `Finanzamt für Gebühren` | 0.7% | 84.2% | 0.3% | 19 | 16 | 3 |
| `OECD` | 0.3% | 63.6% | 0.2% | 11 | 7 | 4 |
| `Technical University` | 0.0% | 33.3% | 0.0% | 3 | 1 | 2 |
| `Single Letter Company GmbH` | 0.6% | 29.8% | 0.3% | 47 | 14 | 33 |
| `Company Suffix GmbH & Partner KG` | 0.3% | 14.9% | 0.2% | 47 | 7 | 40 |
| `Company Suffix GmbH` | 0.7% | 8.5% | 0.4% | 201 | 17 | 184 |
| `Company Suffix AG` | 0.0% | 2.9% | 0.0% | 35 | 1 | 34 |
| `Administrative Court Vienna` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Federal Court of Finance Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Steinval GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rs Dilly's Wellnesshotel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Burtscher Wachter GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SUVA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Railway Pension Service` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Energy Company Generic` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Fa. Company Abbreviation` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Specific Company Names` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Company Suffix m.b.H` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Social Security Agency` 🏆

**F1:** 0.019 | **Precision:** 1.000 | **Recall:** 0.010  

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
| 1.000 | 0.010 | 0.019 | 44 | 44 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 44 | 0 | 4555 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales  und Behindertenwesen` | `Bundesamtes für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_48`)


Sachverständigengutachten nach der Einschätzungsverordnung von Dr.in 2, Neurologin,  Bundesamt für Soziales und Behindertenwesen, am 07.05.2019 erstellt:  „Anamnese:  In einem Vorgutachten wurde eine Persönlichkeitsstörung (histrionisch), Panikstörung,  posttraumatische Belastungsstörung, chronische Kopfschmerzen mit 50% GdB rückwirkend an  Hand der Befunde ab 10/2012 beurteilt. Die Behinderung bestehe bereits vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_93`)


Die erhöhte Familienbeihilfe steht daher nicht zu.  Im Zuge dieser Erledigung erstellte das Bundesamt für Soziales und Behindertenwesen im  Auftrag des Finanzamtes folgende Bescheinigung(en) über das Ausmaß der Behinderung, die  Ihnen zeitnah und mit separater Post zugesendet wird/werden.“

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_191`)


Diagnose: emotional instabile Persönlichkeitsstörung mit histrionischen Zügen“  Die oa. 3 Sachverständigengutachten des Bundesamtes für Soziales und behindertenwesen  wurden im Zuge des Beschwerdeverfahrens erstellt.  Das Bundesfinanzgericht erachtet, die in den 3 Gutachten des Bundesamtes für Soziales und  Behindertenwesen nach der Einschätzungsverordnung getroffenen Feststellungen, dass bei der  Bf. vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_242`)


Zufolge den Bestimmungen des § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die  voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine  Bescheinigung des Sozialministeriumservice (früher Bundesamtes für Soziales und  Behindertenwesen) auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl.  VwGH 20.09.1995, 95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006,  2003/13/0123, VwGH 30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_248`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  Gutachten gebunden (vgl. VwGH 22.12.2011, 2009/16/0310, VwGH 16.12.2014, Ro  2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und vollständig sind und -  im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH 29.09.2011,  2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch die bei Lenneis in Csaszar/Lenneis/Wanke,  FLAG, § 8 Rz 29 zitierte Rechtsprechung).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_255`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt, eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_46`)


Am 25.06.2014 fand eine fachärztliche  Untersuchung aus dem Bereich der Neurologie des Beschwerdeführers beim Bundesamt für  Soziales und Behindertenwesen, zur Erstellung eines Sachverständigengutachtens, statt.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_273`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_279`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der  Beweisführung  Zufolge § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_280`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  Gutachten gebunden (vgl. 2007/15/0019, VwGH 22.12.2011, 2009/16/0310, VwGH  16.12.2014, Ro 2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und  vollständig sind und - im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH  29.09.2011, 2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  vgl. auch die bei Lenneis in Csaszar/Lenneis/Wanke, FLAG, § 8 Rz 29 zitierte Rechtsprechung).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_23`)


7.  Am 12. Dezember 2020 übermittelte der Beschwerdeführer ergänzend die vom Bundesfi- nanzgericht angeforderte Bescheinigung des Bundesamtes für Soziales und Behindertenwesen  über den Grad der Behinderung.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_34`)


Dem vorgelegten Sach- verständigengutachten des Bundesamtes für Soziales und Behindertenwesen zufolge leidet der  Beschwerdeführer an einer seit 20 Jahren bekannten Epilepsie, aufgrund welcher ein Grad der  Behinderung von 40% festgestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_74`)


Dem Beschwerdeführer wurde vom Bundesamt für Soziales und Behindertenwesen ein durch  die Epilepsie bedingter Gesamtgrad der Behinderung von 40% und ein durch die Erkrankung  des Verdauungssystems bedingter Grad der Behinderung von 10% bescheinigt, wobei eine  wechselseitige Beeinflussung nicht festgestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_10`)


Aus dem diesbezüglich vom Sozialministeriumservice (vormals Bundesamt für Soziales und  Behindertenwesen) am 12./13.3.2020 erstellten und der Bf übermittelten ärztlichen  Sachverständigengutachten "mit Untersuchung" durch Amanda Zacharek  Fachärztin für Kinder- und  Jugendheilkunde, geht auszugsweise Folgendes hervor:  "Anamnese:  Termingeburt, verzögerte Meilensteine der Entwicklung, freies Laufen mit 23 Monaten, Sitzen  mit 12 Monaten, Sprachentwicklungsverzögerung.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Amanda Zacharek` (person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_182`)


Nach § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen auf Grund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_210`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  als Amtssachverständige bedient, die in die bei dieser Behörde gem. § 90 KOVG 1957 zu  führende Sachverständigenliste, nicht aber in die Liste der allgemein beeideten und gerichtlich  12 von 18 Seite 13 von 18

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_36`)


Gemäß § 8 Abs. 6 FLAG 1967 in der Fassung BGBl. I Nr. 105/2002 ist der Grad der Behinderung  oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch  eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_22`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_72`)


Nach § 8 Abs. 6 FLAG ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (nunmehr Sozialministeriumservice) auf  Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_90`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_96`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der Beweisführung  Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 18. Oktober 2019 wies das Finanzamt den Antrag der Beschwerdeführerin  (Bf.) vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur Familienbeihilfe für  ihren im Mai 2007 geborenen Sohn A. - ab dem im Antrag genannten Zeitpunkt Juli 2019 - mit  dem Hinweis auf die im Zuge dieser Erledigung vom Bundesamt für Soziales und  Behindertenwesen im Auftrag des Finanzamtes erstellte Bescheinigung vom 15. Oktober 2019  über das Ausmaß der Behinderung des Sohnes mit der Begründung ab, es sei ein Grad der  Behinderung von 30% festgestellt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_14`)


Über Anforderung des Finanzamtes an das Bundesamt für Soziales und Behindertenwesen  wurde der Sohn der Bf. am 31. August 2020 durch einen Arzt für Kinder und Jugendheilkunde  ein weiteres Mal untersucht und ein Sachverständigengutachten erstellt.   (Die Sachverständigengutachten werden im Erwägungsteil wiedergegeben).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_104`)


Betreffend den Sohn der Bf. wurden durch Ärzte im Auftrag des Bundesamtes für Soziales und  Behindertenwesen folgende Untersuchungen durchgeführt und vier  Sachverständigengutachten erstellt:   • Begutachtung (Untersuchung) am 20. Juni 2016   Fachgebiet der Sachverständigen: Allgemeinmedizin   Anamnese:   Zustand nach Kinderkrankheiten   Derzeitige Beschwerden:   Bei A. besteht eine Entwicklungsauffälligkeit.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_174`)


Gemäß § 8 Abs. 6 FLAG 1967 in der Fassung BGBl. I Nr. 105/2002 ist der Grad der Behinderung  oder die voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch  eine Bescheinigung des Bundesamtes für Soziales und Behindertenwesen auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_179`)


Das Bundesfinanzgericht ist an die der Bescheinigung des Bundesamtes für Soziales und  Behindertenwesen zugrunde liegenden Gutachten grundsätzlich gebunden und darf diese nur  insoweit prüfen, ob sie schlüssig und vollständig und nicht einander widersprechend sind (vgl.  VwGH 29.9.2011, 2011/16/0063;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und  Behindertenwesen` | `Bundesamtes für Soziales und  Behindertenwesen` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_183`)


Es besteht nach der Rechtsprechung beider Gerichtshöfe öffentlichen Rechts zu § 8 Abs. 6  FLAG 1967 jedoch keine unbedingte Bindung an die Bescheinigungen des Bundesamtes für  Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_216`)


Der Sohn der Bf. wurde von Ärztinnen bzw. einem Arzt im Auftrag des Bundesamtes für  Soziales und Behindertenwesen vier Mal untersucht, und zwar im Juni 2016, im Mai und  Oktober 2019 sowie im August 2020 (und wurden die genannten BSA-Gutachten erstellt).

| Predicted | Gold |
|---|---|
| `Bundesamtes für  Soziales und Behindertenwesen` | `Bundesamtes für  Soziales und Behindertenwesen` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_296`)


Durch die Bescheinigung des Bundesamtes für Soziales und Behindertenwesen, der Grad der  Behinderung des Sohnes der Bf. ab 06/2019 betrage 30%, sind die gesetzlichen  23 von 24 Seite 24 von 24

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_81`)


In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_94`)


Das Bundesamt für Soziales und Behindertenwesen hat mit ausdrücklicher Einwilligung der  betroffenen Person dem zuständigen Finanzamt und dem Arbeitgeber, der Bezüge aus einer  gesetzlichen Sozialversicherung oder Ruhegenussbezüge einer Gebietskörperschaft im Sinne  des § 25 Abs. 1 Z 1, 3 oder 4 auszahlt, die vom Bundesamt für Soziales und Behindertenwesen  gespeicherten und für die Berücksichtigung von Freibeträgen im Sinne der Abs. 1 bis 3 und 7  erforderlichen personenbezogenen Daten elektronisch zu übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_105`)


Diese ist - abgesehen von im vorliegenden Fall nicht relevanten Ausnahmen - regelmäßig das  Bundesamt für Soziales und Behindertenwesen (nunmehr kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_108`)


Die Feststellung einer Behinderung und ihres Ausmaßes der Minderung der Erwerbsfähigkeit  bzw. des Grades der Behinderung, ist somit nicht von der Abgabenbehörde, sondern bindend  vom Bundesamt für Soziales und Behindertenwesen zu treffen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_120`)


Gemäß § 35 Abs. 1 EStG 1988 steht dem Steuerpflichtigen ein Freibetrag (Abs. 3) zu, wenn er  außergewöhnliche Belastungen bei Anspruch auf den Alleinverdienerabsetzbetrag durch eine   Behinderung des (Ehe-)Partners (§106 Abs. 3) hat und er keine pflegebedingte Geldleistung  (Pflegegeld, Pflegezulage oder Blindengeld) erhält.  Zuständige Stelle ist auch in diesem Fall gemäß § 35 Abs. 2 Z 2 EStG das Bundesamt für Soziales  und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_23`)


Vor diesem Hintergrund erwiesen sich, entgegen der Ansicht der Beschwerdeführerin, die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  Gutachten vom 25. März 2021 und die vom Bundesfinanzgericht angeforderte Ergänzung  (erstellt in Form einer Neuerstellung am 17. Mai 2021) in Bezug auf die Frage, ob eine  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen vorliegt, und bejahendenfalls,  wann dieser Umstand eingetreten ist, als schlüssig, wenn unter den gegebenen Umständen der  Gutachter den Eintritt der Erwerbsunfähigkeit mit 09/2016 feststellt, dem Zeitpunkt also, zu  welchem in der psychotherapeutischen Stellungnahme der Sachverständigen festgestellt  worden ist, dass die Beschwerdeführerin den Belastungen einer Berufstätigkeit aufgrund  2 von 21 Seite 3 von 21

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_61`)


Vor diesem Hintergrund erwiesen sich für das Bundesfinanzgericht die der Bescheinigung des  Sozialministeriumservice zugrundeliegenden Gutachten vom 22. (gemeint: 24.) März 2021 und  die vom Bundesfinanzgericht angeforderte Ergänzung (erstellt in Form einer Neuerstellung am  17. Mai 2021) in Bezug auf die Frage, ob eine dauernde Unfähigkeit, sich selbst den Unterhalt  zu verschaffen vorliegt, und bejahendenfalls, wann dieser Umstand eingetreten ist, als  schlüssig, wenn unter den gegebenen Umständen der Gutachter den Eintritt der  Erwerbsunfähigkeit mit 09/2016 feststellt.   Das Bundesfinanzgericht hat sodann als Ergebnis seiner Überlegungen zur Würdigung des  Sachverständigenbeweises, die durch diesen Beweis gewonnene Tatsache als erwiesen  angenommen, eine dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, liege erst  ab September 2016 vor und hat deshalb seiner Entscheidung die hierauf lautende  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen vom 16. Juli 2021 zu  Grunde gelegt.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_74`)


(2) der Inhalt der auf Basis des Gutachtens vom 17  Mai 2021 ausgestellten Bescheinigung des Bundesamtes für Soziales und Behindertenwesen  vom 16. Juli 2021 dem Erkenntnis des Bundesfinanzgerichtes vom 20. September 2021 zu  RV/3100448/2020 zu Grunde gelegt worden ist;

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_163`)


Lebensjahres) eingetreten ist, sind die Abgabenbehörde und das Bundesfinanzgericht an die  der Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrunde liegenden  Gutachten gebunden und dürfen diese nur insoweit prüfen, ob sie schlüssig und vollständig  sind und im Falle mehrerer Gutachten nicht einander widersprechen (VwGH 8.11.2023, Ra  2023/16/0086 unter Hinweis auf die Vorjudikatur).

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_107`)


Ob wirklich die voraussichtliche dauernde Unfähigkeit gegeben ist, ist durch Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamtes für Soziales und Behindertenwesen` | `Bundesamtes für Soziales und Behindertenwesen` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_166`)


§ 8 Abs. 6 FLAG 1967 normiert:  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen (Sozial- ministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_168`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_169`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der anspruchs- relevanten Daten durch das Bundesamt für Soziales und Behindertenwesen (Sozialministerium- service) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes (BBG), BGBl.  Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

</details>

---

## `Employment Agency AMS` 🏆

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

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
| 1.000 | 0.009 | 0.018 | 42 | 42 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 0 | 4557 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_4`)


Entscheidungsgründe  Verfahrensgang  Im Zuge einer GPLA stellte der Prüfer fest, dass über Auftrag des AMS von der  Beschwerdeführerin (Bf) Migranten als Lehrlinge in Deutsch unterrichtet wurden und auf eine  Lehrstelle in einem Betrieb vorbereitet wurden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_20`)


Die ausgezahlten Ausbildungsbeihilfen hätten  eine Höhe von € 240 pro Person und pro Monat betragen und seien vom AMS in genau  derselben Höhe ersetzt worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_25`)


Die Bf sucht als überbetriebliche Ausbildungseinrichtung im Auftrag des AMS für die  Ausbildungsteilnehmer Partner- und Praxisbetriebe, in denen die Ausbildung absolviert werden  kann.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_30`)


Teilnehmer, die nach Ablauf des Ausbildungszeitraumes noch keine Lehrstelle gefunden haben,  werden vom AMS weiterbetreut.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_22`)


Mit dem Bildungskonto wird die berufsorientierte Weiterbildung und Umschulung  (ausgenommen Umschulungen i.S.d. AMS) zur Arbeitsplatzsicherung gefördert.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_22`)


Sie lege aber die geforderten  Unterlagen diesem Schreiben noch einmal bei, nämlich die Kursbestätigung von [Vorname Kind  1] über den AMS Kurs hinsichtlich seiner Lehrabschlussprüfung und die Kursbestätigung von  [Vorname Kind 2].

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_24`)


In den  Kalenderjahren 2017 bis 2021 habe der Bf. vom AMS bzw von der österreichischen  Pensionsversicherungsanstalt insgesamt € 80.757,19, also durchschnittlich € 1.345,95  monatlich erhalten.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Pensionsversicherungsanstalt` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_40`)


Der Bf. bezog in der Folge (ab 03/2016) Arbeitslosengeld bzw. Notstandshilfe und wurde vom  AMS als „unvermittelbar“ eingestuft.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_127`)


Das von der Bf. im Jahre 2016 begonnene und im Beschwerdezeitraum sowie in den beiden  diesem nächstfolgenden Jahren betriebene beschwerdegegenständliche Studium stellt in  Ansehung des Umstandes, dass eine AHS-Matura sowohl nach der allgemeinen  Verkehrsauffassung als auch gemäß dem Berufslexikon des AMS – in diesem sind insgesamt  1.726 Berufe aufgelistet, die Begriffe AHS-Maturant oder AHS-Maturantin finden sich dort  nicht – zweifelsfrei eine Erstausbildung dar.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_10`)


Er besuche einen vom AMS bezahlten Kurs zur Vorbereitung auf die  Lehrabschlussprüfung (LAP).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_16`)


In Beantwortung des Ersuchens teilte der Bf. dem Finanzamt am 4. August 2022 mit, dass das  AMS nach dem Ende seines Präsenzdienstes seinem Wunsch nachgekommen sei und ihm  einen Vorbereitungskurs auf die Lehrabschlussprüfung ermöglicht habe (Verweis auf die  beiliegende Betreuungsvereinbarung, Seite 2 Mitte).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_20`)


Aus dem ebenfalls beigelegten Schreiben des AMS vom 23. Mai 2022 geht u.a. hervor, dass mit  dem Bf., um ihn bei der Lehrabschlussprüfung zu unterstützen, ein Vorbereitungskurs zur  Lehrabschlussprüfung beim Kursinstitut KUS von 4. Juli 2022 bis 9. September 2022 vereinbart  wurde.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_27`)


Im Sommer habe er einen vom AMS be- zahlten Vorbereitungskurs für diese Prüfung absolviert.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_43`)


2) Zeitraum zwischen 1. Mai und 2. Juni 2022:   a) Ich bin seit 13. April 2022 durchgehend am AMS als arbeitssuchend gemeldet (siehe  Dokument 4 a_LJ_Notstandshilfe.pdf).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_44`)


Wegen des noch fehlenden Lehrabschlusses konnte mir  das AMS noch keine Erwerbstätigkeit vermitteln, unterstützt mich aber bei der Vorbereitung  auf die LAP.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_62`)


4) AMS Leistungen  a)

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_66`)


Mein Einkommen vom AMS beträgt 9,14 Euro täglich.“  Beilagen:   Teilnahmebestätigung KUS-Netzwerk vom 05.10.2022, Vorbereitung auf die LAP,  04.07.2022-30.09.2022, 60 Unterrichtseinheiten   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 11.03.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 30.06.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 23.09.2021   Wiederholerprüfungsanmeldung Nr. 137827 vom 27.05.2022   Mitteilung über den Leistungsanspruch, AMS vom 09.06.2022:     4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_67`)


 Bestätigung Kurszeiten, AMS:     Mit E-Mail vom 12. März 2023 teilte der Bf. mit, dass es nun mit einer Anstellung bei der Fa.  Wright Robotik AG  als Handelsarbeiter geklappt habe und er von der WKO den Prüfungstermin  30.03.2023 erhalten habe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Wright Robotik AG` (organisation)
- `WKO` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_87`)


Die Kurstage gliederten sich  wie folgt:  Montag: 9-12 Uhr  Mittwoch: 8-12 Uhr  Freitag: 9-12 Uhr  Von 13. April 2022 bis 05. März war der Bf. am AMS als arbeitssuchend gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_91`)


Beweiswürdigung  Der unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt und den vom Bf.  vorgelegten Unterlagen (Schreiben des AMS vom 23. Mai 2022 betreffend  Betreuungsvereinbarung, Schreiben des AMS vom 09. Juni 2022 betreffend Gewährung von  Notstandshilfe, Präsenzdienstbestätigung vom 21. März 2022, Bescheid des Magistrates der  Stadt Wien, MA 40, vom 4. Juli 2022, Wiederholer-Prüfungsanmeldung 137827 vom 27. Mai  2022, div. Lehrabschlussprüfungszeugnisse).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Magistrates der  Stadt Wien` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_147`)


Dient ein vom AMS gefördertes Training dazu, die fachliche Qualifikation für die Ausübung  eines konkreten angestrebten Berufes zu erlangen und nimmt es die überwiegende Zeit in  Anspruch, liegt - anders als bei allgemeinen Qualifizierungsmaßnahmen des AMS -  Berufsausbildung i.S.d. FLAG 1967 vor (BFG vom 02.02.2022, RV/7105412/2019).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_162`)


- sie haben sich bei ihrem AMS arbeitslos gemeldet;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_60`)


Die am 2.4.2015 erfolgte Auszahlung des Pensionskassenguthabens sei in der Hochrechnung zu  belassen, weil es sich dabei um einen laufenden Bezug iSd § 41 EStG gehandelt habe, der  neben den laufenden AMS-Leistungen empfangen worden sei.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_15`)


Der Beschwerdeführer (Bf.) brachte Beschwerde mit folgender Begründung ein:   Ich war von April 2021 bis August 2021 im Kurs vom WIFI im Tourismuscenter und bringe auch  den Bescheid vom AMS mit und kann es daher auch beweisen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_21`)


Familienbeihilfe steht bei einer ernsthaften und zielstrebigen Ausbildung zu.   Wann gilt die Ausbildung als ernsthaft und zielstrebig?   • Das Kind verwendet die volle Zeit dafür   • Das Kind tritt in angemessener Zeit zu Prüfungen an   Bei Ihrem Kind trifft das nicht zu.   Aus dem vorgelegten Abschlussbericht des AMS Niederösterreich ist ersichtlich, dass Ihr Sohn  M... in der Zeit der Ausbildung von 17.5.2021 bis 30.07.2021 aufgrund "wiederkehrender  Krankenstände die erforderlichen Anwesenheiten nicht erfüllt hat und der Kurs daher  abgebrochen wurde" -- Zitat.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_38`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:   Sachverhalt:   Der Sohn des Beschwerdeführers (Bf.) besuchte von 27.01.2020 bis 31.08.2020 eine  überbetriebliche Lehrausbildung im Einzelhandel des WIFI NÖ im Auftrag des AMS.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_40`)


In der Antwort des Überprüfungsschreibens  legte der Bf. eine neue Kursbesuchsbestätigung über eine Lehrlingsausbildung am WIFI im  Rahmen des AMS-Tourismuscenters vor.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_46`)


Gegen den Bescheid wurde Beschwerde erhoben und vorgebracht, dass sich der Sohn des Bf.  von April 2021 bis August 2021 in einem WIFI / AMS Kurs Tourismuscenter befunden habe und  ein Abschlussbericht des WIFI / AMS über das Kursmodul vom 15.05.2021 bis 30.07.2021  vorgelegt, aus dem hervorgeht, dass der Sohn des Bf. aufgrund wiederkehrender  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Vom 27. Jänner 2020 bis (voraussichtlich) 31. August 2020 hatte der im Juni 1999 geborene  Sohn des Bf. – am Beginn des Rückforderungszeitraumes somit bereits volljährig – an einem  Ausbildungslehrgang im Rahmen der Überbetrieblichen Lehrausbildung des  Wirtschaftsförderungsinstitutes NÖ im Auftrag des AMS NÖ teilgenommen (WIFI- Bestätigung  vom 24.07.2020):   „Gemäß § 30 BAG ist-dieser Teilnehmer Lehrlingen gleichgestellt.   Die im Ausbildungslehrgang zurückgelegte Praktikumszeit ist der Lehrzeit im betreffenden  Lehrberuf gleichgestellt:   von 27.01.2020 bis voraussichtlich 31.08.2020 Einzelhandel – Einrichtungsberatung“   Am 25. September 2020 hatte der Sohn des Bf. eine Ausbildung im Rahmen des   AMS-Tourismuscenters begonnen, die im Mai 2022 enden sollte (WIFI- Bestätigung  vom 12.1.2021):   Ziel der Ausbildung ist die Ablegung der Lehrabschlussprüfung, welche voraussichtlich   im Mai 2022 stattfinden wird.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_63`)


Am 17. Mai 2021 begann der Sohn des Bf. den Kurs „Tourismuscenter 2020 - Grundmodule  KmS 1 (AMS Maßnahmen-/Veranstaltungsnummer …)“ – Aufbaumodul 2, und ergab sich  Folgendes:     Inhalt   Grundmodul KMS 1 mit Möglichkeit des Ausstiegs und Zertifikat zur Küchenhilfskraft   oder Servicemitarbeiterin   Gesamtdauer bis zur Lehrabschlussprüfung:   16 Monate.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_68`)


Der Sohn des Bf. bezog (im beschwerdegegenständlichen Zeitraum) vom AMS   (AMS- Bezugsbestätigungen vom 09.05.2022 und 29.08.2022):   von  bis  Leistungsart    T a g s a t z   30.03.2021   01.04.2021   Arbeitslosengeld - Schulung     7,88 EUR  30.03.2021   01.04.2021   Beihilfe Deckung Lebensunterhalt  19,38 EUR   30.03.2021   01.04.2021   pauschalierte Kursnebenkosten     2,11 EUR   03.04.2021   16.04.2021   Arbeitslosengeld - Schulung     7,88 EUR   03.04.2021   16.04.2021   Beihilfe Deckung Lebensunterhalt  19,38 EUR   03.04.2021   16.04.2021   pauschalierte Kursnebenkosten     2,11 EUR   18.04.2021   23.04.2021   Arbeitslosengeld - Schulung     7,88 EUR   18.04.2021   23.04.2021   Beihilfe Deckung Lebensunterhalt  19,38 EUR   18.04.2021   23.04.2021   pauschalierte Kursnebenkosten     2,11 EUR   25.04.2021   30.04.2021   Arbeitslosengeld - Schulung     7,88 EUR   5 von 8 Seite 6 von 8

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_70`)


2. Beweiswürdigung  Die im Einzelnen getroffenen Feststellungen beruhen auf den jeweils angeführten Grundlagen  bzw. den vorgelegten AMS-Bestätigungen und Datenbankauskünften.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_77`)


– Gewährung pauschalierter Kursnebenkosten bis 07.07.2021 durch das AMS   – Gewährung von Arbeitslosengeld bis 07.07.2021 (und in der Folge wiederum ab 03.09.2021      [ab Rückkehr aus dem Ausland])   lassen darauf schließen, dass der Sohn des Bf. zumindest ein paar Wochen, in den Monaten  Mai und Juni 2021 (vor dem Absolvieren des ersten Praxistages), den Kurs besucht hatte, ohne  dass in Abrede zu stellen ist, es habe in diesen Wochen eine ernsthafte und zielstrebige  Ausbildung bestanden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_30`)


-) bin derzeit beim AMS gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_71`)


2) beim AMS gemeldet sei und derzeit ein Schuldenregulierungsprogramm bei Gericht  anhängig sei;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145954.1`) (sent_id: `deanon_BFG_20260814_TEST/145954.1_42`)


Da wir finanziell gerade über die Runden  kommen - ich bin Hausfrau ohne eigenes Einkommen, mein Gatte wurde aus  Einsparungsgründen von seiner Firma gekündigt, war 2 Jahre AMS und ist derzeit 20 Stunden  wöchentlich beschäftigt - wollte ich Auskunft betreffend den Anspruch auf Familienbeihilfe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

</details>

---

## `Federal Court of Finance` 🏆

**F1:** 0.057 | **Precision:** 1.000 | **Recall:** 0.030  

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
| 1.000 | 0.030 | 0.057 | 136 | 136 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 136 | 0 | 4463 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_11`)


Über die Beschwerde wurde erwogen: 2.  Sachverhalt Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_49`)


Das Antwortschreiben samt Beilagen wurde der Abgabenbehörde mit Schreiben des Bundesfinanzgerichts vom 03.07.2019 zur Kenntnis gebracht, Einwendungen dagegen hat sie nicht vorgebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_29`)


Verwiesen werde auf das Erkenntnis des  Bundesfinanzgerichts vom 12.12.2016 zu GZ RV/2100836/2013.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_99`)


Auch das vom Finanzamt angezogene Argument, das dem Abgabenrecht immanente  Leistungsfähigkeitsprinzip würde neben der vorrangigen Verwertung eigenen Vermögens die  Berücksichtigung eines steuerlichen Existenzminimums von EUR 11.000,- bei der Ehegattin  gebieten, würde nach Ansicht des Bundesfinanzgerichts die Abzugsfähigkeit von  außergewöhnlichen Belastungen durch Unterhaltsaufwendungen für Ehegatten über Gebühr  und in einer nicht vom Gesetz gedeckten Weise einschränken.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_131`)


Gegen eine Entscheidung des Bundesfinanzgerichts ist gemäß Art. 133 Abs. 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_61`)


Über die Beschwerde wurde erwogen:  Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der aus den  vom Finanzamt vorgelegten Akten, dem Vorbringen des Bf. in der mündlichen Verhandlung  und den von ihm dem Gericht vorgelegten Unterlagen hervorgeht:  B. Sachverhalt und Beweiswürdigung  B/1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_10`)


Die fristgerecht dagegen erhobenen Beschwerden wurden mit Beschwerdevorentscheidungen  vom 02. Juli 2019 unter Hinweis auf die Entscheidung des Bundesfinanzgerichts vom 24. Juni  2019 als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_14`)


Gegen dieses Erkenntnis sei eine außerordentliche Revision beim Verwaltungsgerichtshof  eingebracht worden, welche sich auf das Erkenntnis des Bundesfinanzgerichts  GZ RV/2100552/2018 stütze, das in einem ident gelagerten Vermittlungsfall einen Kollegen des  Beschwerdeführers betreffend ergangen sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_23`)


Über Ersuchen des Bundesfinanzgerichts legte die steuerliche Vertretung des  Beschwerdeführers die für die Jahre 2014 bis 2016 gültigen Allgemeinen  Geschäftsbedingungen (Fassung April 2012), die Auszahlungsberichte betreffend die  Provisionsansprüche der Jahre 2014 bis 2016 sowie Auszüge aus den Kontoauszügen vor, aus  denen ersichtlich ist, dass die Überweisung der Provision in den Jahren 2014 bis 2016 von der  M-AG veranlasst worden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_142`)


Des  Weiteren verweist sie auf drei näher angeführte Entscheidungen des Bundesfinanzgerichts  (RV/2100784/2018, RV/2101113/2016 und RV/2101154/2017).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_302`)


C-580/16, Hans Bühler und die sich daran orientierenden Entscheidungen  des Bundesfinanzgerichts war insofern nicht näher einzugehen, dass die  sachverhaltsgegenständlichen strittigen Geschäftsfälle keine sogenannten „Dreiecksgeschäfte“  iSd. Art. 25 UStG 1994-BMR, sondern schlichte innergemeinschaftliche Erwerbe unter  Verwendung einer anderen Umsatzsteueridentifikationsnummer als die des Staates, indem die  innergemeinschaftliche Beförderung endet (Empfangsstaat), waren.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_135`)


Hinsichtlich einzelner Positionen ist nach Ansicht des Bundesfinanzgerichts der Bf. die  Glaubhaftmachung der Berufsbezogenheit u.a. durch die Anmerkungen zur Liste des  Finanzamts gelungen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_143`)


Die Ausbildung nahm daher aus der Sicht des Bundesfinanzgerichts nach allgemeiner  Lebenserfahrung im Wintersemester 2016/17 nicht die volle Zeit des Bf in Anspruch.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_33`)


Das Rechtsmittel gegen den nicht wirksam gewordenen Abweisungsbescheid ist daher mit  Beschluss des Bundesfinanzgerichts zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_278`)


Art. 23 Abs. 2 DBA-Schweiz ist (auch nach Ansicht des Bundesfinanzgerichts) nicht  einschränkend – also auf Einkünfte für in der Schweiz ausgeübte Arbeit aus öffentlichen Kassen  in der Schweiz – sondern erweiternd – neben der Einkünftebesteuerungsberechtigung für die  im Ansässigkeitsstaat ausgeübte Tätigkeit – auch auf diese anzusehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_201`)


Schließlich ist zur  Frage des Vorliegens der Voraussetzungen für den Vorsteuerabzug allgemein darauf zu  verweisen, dass eine in freier Beweiswürdigung getroffene Feststellung des  Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof grundsätzlich nicht  zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_75`)


Es darf dazu auf den Beschluss des Bundesfinanzgerichts vom 15.02.2021,  RV/7100157/2021, verwiesen werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_94`)


Der  in der Beschwerdevorentscheidung genannte Pensionsanspruch sei im Zuge einer  Entscheidung des Bundesfinanzgerichts vom 17.09.2018, RV/1100359/2016, noch einmal  behandelt worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_58`)


Diese Sachverhaltsfeststellungen basieren auf den jeweils erwähnten und als glaubhaft  erachteten Beweismitteln bzw den im vorgelegten Akt aufliegenden und nachgereichten,  ebenfalls glaubhaften Unterlagen und dem Ergebnis des seitens des Bundesfinanzgerichts  durchgeführten Ermittlungen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_175`)


Schließlich ist zur  Frage des Wohnsitzes bzw. dessen Aufgabe allgemein darauf zu verweisen, dass eine in freier  Beweiswürdigung getroffene Feststellung des Bundesfinanzgerichts der Kontrolle durch den  Verwaltungsgerichtshof grundsätzlich nicht zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_12`)


Durch die Aufhebung des Einkommensteuerbescheides 2013 gemäß § 300 Abs. 1 BAO im Sinne  des Beschlusses des Bundesfinanzgerichts vom 15.03.2021 innerhalb der gesetzten Frist, sowie  durch die gleichzeitige Erlassung des neuen Sachbescheides, wurde dem Beschwerdebegehren  Rechnung getragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_12`)


II. Das Bundesfinanzgericht hat erwogen:  Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_100`)


Dazu wird seitens des  Bundesfinanzgerichts die Rechtsansicht vertreten, dass es - unabhängig von  Sanierungsbemühungen des Geschäftsführers -  grundsätzlich darauf ankommt, ob der  Geschäftsführer im/ab dem Zeitpunkt der Fälligkeit der Umsatzsteuervorauszahlung 08/2011  über die finanziellen Mittel verfügte, um diese Abgabe als Geschäftsführer für die  Gemeinschuldnerin innerhalb des Zeitraumes ab Fälligkeit (15.10.2011) bis zur  7 von 11 Seite 8 von 11

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_119`)


Für den vorliegenden Fall ist seitens des Bundesfinanzgerichts unter Berücksichtigung der  vorliegenden Aktenlage sachverhaltsmäßig festzustellen, dass dem Bf. bzw. der von ihm  vertretenen Gemeinschuldnerin keine ausreichenden finanziellen Mittel zur Verfügung  standen, um die Umsatzsteuervorauszahlung 08/2011 am Fälligkeitstag zur Gänze zu bezahlen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_199`)


Die Anregung des steuerlichen Vertreters auf Wiederaufnahme des Verfahrens gemäß § 303  Abs.1 lit. c BAO laut Vorlageantrag vom 30.7.2020 fällt nicht in den Zuständigkeitsbereich des  Bundesfinanzgerichts.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_76`)


Mit Beschluss des Bundesfinanzgerichts vom 9. Februar 2021 wurde das Finanzamt Österreich  vor dem Hintergrund, dass bislang keine Unterlagen betreffend eine kalkulatorische Schätzung,  5 von 15 Seite 6 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_83`)


Mit Beschluss des Bundesfinanzgerichts vom 5. Juli 2021 wurden dem Beschwerdeführer  folgende Unterlagen zur Kenntnis gebracht: Niederschrift über die Schlussbesprechung  anlässlich der beim Beschwerdeführer durchgeführten Außenprüfung vom 23.3.2016;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_88`)


Der Antrag auf Zeugeneinvernahme des Beschwerdeführers wurde mit Beschluss des  Bundesfinanzgerichts vom 9. Februar 2021 abgelehnt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_142`)


Die beiliegenden, vom erkennenden Gericht erstellten Kalkulationen (Berechnungsblätter I bis  IV) sowie ergänzend dazu schriftliche Erläuterungen zur Wahl der Schätzungsmethode, zu den  Sachverhaltsannahmen, die der Schätzung zugrunde gelegt wurden, und zur Ableitung der  Schätzungsergebnisse wurden den Parteien mit Beschluss des Bundesfinanzgerichts vom 5. Juli  10 von 15 Seite 11 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_9`)


ergangenen Beschluss des Bundesfinanzgerichts vom 7. November 2017 und beantragte  seinem Antrag vom 29. Dezember 2016 nunmehr stattzugeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_37`)


ergangenen Beschluss des Bundesfinanzgerichts vom 7. November 2017 und beantragte  seinem Antrag vom 29. Dezember 2016 nunmehr stattzugeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_2`)


Bezirk vom 03. November 2016 betreffend Vorschreibung einer Ausgleichsabgabe  gemäß § 9 Wiener Baumschutzgesetz mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom  09. Dezember 2016 gegen den Bescheid vom 03. November 2016 ein Vorlageantrag nicht  eingebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_53`)


4. Antrag auf Senatsentscheidung  Gemäß § 272 Abs 2 Z 1 lit b BAO besteht die Möglichkeit, im Rahmen eines Vorlageantrags die  Entscheidung des Bundesfinanzgerichts durch Senat zu beantragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_112`)


Gegen die in der Beschwerdevorentscheidung zuerkannten Kosten in Höhe von zusätzlich  1.393,55 € (neben den bereits berücksichtigten 1.963,69 €) bestehen seitens des  Bundesfinanzgerichts keine Bedenken, wirken sich allerdings aufgrund der Höhe des bei den  außergewöhnlichen Belastungen bestehenden Selbstbehaltes (5.106,52 €) betraglich nicht aus.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_53`)


Diese Rechtssache wurde der ursprünglich zuständigen Gerichtsabteilung Y mit Verfügung des  Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 27.1.2022 abgenommen und  jener der nunmehr einschreitenden Richterin zum Stichtag 2.2.2022 übertragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_40`)


Über Ergänzungsersuchen des Bundesfinanzgerichts brachte der Beschwerdeführer mit  Schreiben vom 17.2.2022 weiter vor, er sei – da er sich jedes Jahr mehr als 90 Tage in  Großbritannien aufhalte – in Großbritannien steuerpflichtig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_48`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_46`)


Nach Ansicht des Bundesfinanzgerichts ist der  Verweis auf Einkünfte iSd § 27 Abs. 2 EStG 1988 steuersubjektübergreifend zu sehen und  hinsichtlich der aus dem gegenständlichen Wirtschaftsgut  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_106`)


4.2. Ermittlungen und Beschluss Bundesfinanzgericht inklusive Auftrag der  Zeugenvernehmung durch die belangte Behörde vom 26. April 2022  Im Zuge der Ermittlungen des Bundesfinanzgerichts waren einige Punkte offen und das  Bundesfinanzgericht richtete daher einen Vorhalt zur Ermittlung des Sachverhaltes an den Bf  und die belangte Behörde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_33`)


Angesichts der überlangen Verfahrensdauer wäre die erstinstanzliche Behörde verpflichtet  gewesen, in (verfassungskonformer) Auslegung des § 209 Abs. 1 BAO anzunehmen, dass es  (zeitlich) genügt habe, den Wiederaufnahmeantrag binnen eines Jahres nach Bekanntwerden  des Wiederaufnahmegrundes (Erkenntnis des Bundesfinanzgerichts vom 13.1.2017,  RV/4100613/2013) zu stellen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_15`)


Nach Stellung des diesbezüglichen Vorabentscheidungsersuchens eines Richters des  Bundesfinanzgerichts reichte die Europäische Kommission mit Beschluss vom 14.05.2020 im  Verfahren INFR (2018) 2372 am 22.07.2020 Klage gegen die Republik Österreich beim  Gerichtshof der Europäischen Union ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Gerichtshof der Europäischen Union` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_39`)


Die belangte Behörde ist nach Ansicht des Bundesfinanzgerichts zur Recht davon ausgegangen,  dass damit kein Wiederaufnahmegrund im Sinne des Neuerungstatbestandes (§ 303 Abs. 1 lit b  BAO) vorhanden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140554.1`) (sent_id: `deanon_BFG_20260814_TEST/140554.1_61`)


Die Bf. hat den am 30.01.2023 hinterlegten Beschluss des Bundesfinanzgerichts vom  24.01.2023 nicht behoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_188`)


Der erkennende Senat des  Bundesfinanzgerichts vertritt im Zweifel dazu nun die Ansicht, dass der Bf. bei der Einreichung  der Einkommensteuerklärung 2017, wie von diesem angegeben, von der gesetzlichen  Änderung des Steuerabkommens zwischen Liechtenstein und Österreich ab 2017 keine  Kenntnis hatte und liegen auch keine konkreten anders gelagerten Anhaltspunkte vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_189`)


Der Senat des Bundesfinanzgerichts gelangt daher anders als Spruchsenat in rechtlicher  Hinsicht zum Ergebnis, dass es iSd § 98 Abs. 3 FinStrG nicht erweislich ist, der Bf. habe es  zumindest für möglich gehalten und sich damit abgefunden, eine Verkürzung der von ihm  16 von 21 Seite 17 von 21

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_192`)


Allerdings ist der Senat des Bundesfinanzgerichts der Ansicht, dass sich der Bf. hinsichtlich der  nicht erklärten Kapitaleinkünfte aus Liechtenstein gemäß § 34 Abs. 1 FinStrG der grob  fahrlässigen Abgabenverkürzung schuldig gemacht hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_214`)


Nach Ansicht des Senates des Bundesfinanzgerichts war die Vermögensverwaltungsfirma  neben der Vertretung des Bf. bei den depotführenden Banken für eine möglichst ertragreiche  Veranlagung des Kapitalvermögens des Bf. verantwortlich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_241`)


In Abwägung dieser  Strafzumessungsgründe sowie unter Berücksichtigung des Schuld- und Unrechtsgehaltes der  Tat und einem Strafrahmen von € 33.356,00 erachtet der erkennende Senat des  Bundesfinanzgerichts eine Geldstrafe von € 5.000,00 als angemessen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_93`)


Davon abweichend ist nun  allerdings seitens des Bundesfinanzgerichts festzustellen, dass seitens der steuerlichen  Vertretung ein Rechtsmittelverzicht ausdrücklich im Namen des Bf. nicht erklärt wurde und  sind auch keine Umstände ersichtlich, woraus auf die Annahme eines von der steuerlichen  Vertretung in Vertretung für den Bf. erklärten Rechtsmittelverzichts geschlossen werden  könnte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_130`)


Hiezu  ist seitens des Bundesfinanzgerichts festzustellen, dass das Finanzamt gegen die in § 115 Abs. 1  BAO normierte Ermittlungspflicht verstoßen hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_211`)


Da das Fehlen einer UID-Nummer des Erwerbers im  Zeitpunkt des Leistungsbezuges dem Vorliegen einer steuerfreien innergemeinschaftlichen  Lieferung iSd Art. 7 UStG 1994 - wie schon ausgeführt - nicht entgegensteht, wenn die  materiellen Voraussetzungen hierfür erfüllt sind, wovon nach den Feststellungen des  Bundesfinanzgerichts auszugehen ist, schuldete der leistende Unternehmer die Umsatzsteuer  im Revisionsfall lediglich aufgrund der Rechnung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_11`)


Bereits im Erkenntnis des Bundesfinanzgerichts vom 21.7.2021, RV/7101544/2019, wurde auf  die bei der Beschwerdeführerin erfolgte Außenprüfung verwiesen, bei der in  beschwerderelevanter Hinsicht (ua im Bericht über das Ergebnis der Außenprüfung vom  31.10.2016) folgende Prüfungsfeststellungen getroffen wurden:  „Kurssicherungsgeschäfte   Zur Absicherung des Währungsrisikos aus dem in lokaler Währung geführten Eigenkapital  diverser NWB wurden Kurssicherungsgeschäfte abgeschlossen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_34`)


Mit Erkenntnis des Bundesfinanzgerichts vom 21.7.2021, RV/7101544/2019, wurden die  gegenständlichen Beschwerden zunächst stattgebend erledigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_72`)


Von Seiten des Bundesfinanzgerichts wurden somit nunmehr sowohl die sich ergebenen  Zinsaufwendungen und Zinserträge als auch erzielten Kursgewinne und Kursverluste aus dem  Sicherungsgeschäft berücksichtigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_145`)


15   Fragen der Berechnung des gemeinen Werts nach § 10 BewG 1955 sind grundsätzlich der  einzelfallbezogenen Beurteilung des Bundesfinanzgerichts zuzuordnen und können nur dann  eine Rechtsfrage grundsätzlicher Bedeutung darstellen, wenn die Beurteilung des  Bundesfinanzgerichts in einer die Rechtssicherheit beeinträchtigenden, unvertretbaren Weise  erfolgt wäre.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_31`)


Mit Vorhalt des Bundesfinanzgerichts vom 05.09.2023 wurde der Bf. die offenbar verspätete  Einbringung des Vorlageantrages (Fristablauf war am 15.12.2014 - siehe unten) mit dem  Ersuchen um allfällige Gegenäußerung binnen einer zweiwöchigen Frist vorgehalten sowie  auch der belangten Behörde zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_8`)


Der Abgabenbehörde wurde mit Beschlüssen des Bundesfinanzgerichts eine entsprechende,  einmal verlängerte Frist bis zum 30. September 2023 zur Aufhebung gesetzt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_15`)


2) Beweiswürdigung  Der Sachverhalt ergibt sich aus dem Verwaltungsakt und dem Akt des Bundesfinanzgerichts  und ist unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_29`)


Durch die Bekanntgabe der Aufhebung der angefochtenen Bescheide sowie der damit zu  verbindenden neuen Sachbescheide lebt die Zuständigkeit und die Entscheidungspflicht des  Bundesfinanzgerichts gemäß § 300 Abs 5 BAO wieder auf.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/142964.1`) (sent_id: `deanon_BFG_20260814_TEST/142964.1_68`)


Zudem erscheint – entgegen dem  betreffenden Einwand – die finanzielle Situation der Bf nach Ansicht des Bundesfinanzgerichts  insofern nicht als unsicher, als das derzeit ruhende Exekutionsverfahren für den Fall, dass der  Vater seiner Unterhaltspflicht nicht mehr nachkommen sollte, wiederum auflebt, dh. das  Gericht die Gehaltsexekution oä. jederzeit wieder verfügen könnte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/142998.1`) (sent_id: `deanon_BFG_20260814_TEST/142998.1_30`)


Mit Beschluss des Bundesfinanzgerichts vom 4. September wurde die belangte Behörde dazu  aufgefordert, die Akten des Verwaltungsverfahrens vollständig vorzulegen und dem  Bundesfinanzgericht sowie der beschwerdeführenden Partei einen Vorlagebericht zu  übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_16`)


In seiner Stellungnahme ebenfalls vom 22.6.2023 meinte der Bf, dass das zitierte Erkenntnis  des Bundesfinanzgerichts betreffend eine Kindesmutter mit zu geringem Einkommen in seinem  Fall nicht zutreffe, da die Mutter seiner Kinder gar kein Einkommen gehabt habe.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_11`)


Erwägungen des Bundesfinanzgerichts über die Säumnisbeschwerde:  Eine Verletzung der Entscheidungspflicht des FA in Bezug auf die Beschwerde vom 14.8.2023 ,  eingelangt beim FA am 16.8.2023 gegen den Anspruchszinsenbescheid 2021 lag am 17. Jänner  2024 noch nicht vor, und liegt auch bis heute nicht vor, da am 17. Jänner 2024 bis heute die  Frist von sechs Monaten, innerhalb der das FA die Beschwerde gegen den  Anspruchszinsenbescheid 2021 zu erledigen hatte (§ 284 Abs 1 BAO) noch nicht abgelaufen  war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_67`)


Nach Ansicht des  Bundesfinanzgerichts handle es sich bei den beiden Häusern um notwendiges Privatvermögen  der Revisionswerberin.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_70`)


Nach Ansicht des  Bundesfinanzgerichts wirke dieses Gutachten nicht auf die Jahre 2006 bis 2012 zurück.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_124`)


33 Die Revision tritt den Feststellungen des Bundesfinanzgerichts, dass es sich vorliegend um  Luxusimmobilien handelt, die auf die Bedürfnisse der Gesellschafter zugeschnitten seien, nicht  substantiiert entgegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_525`)


Demgegenüber teilt der erkennende Senat des  Bundesfinanzgerichts die Ansicht der Abgabenbehörde, dass schon im Hinblick auf die  luxuriöse Wohnlage, die äußerst großzügigen Wohnflächen (509m² und 420m²) und die  Ausstattung etwa mit Hallenbad bzw Outdoorpool Luxusimmobilien vorliegen, die auf die  Bedürfnisse der Gesellschafter bzw ihrer Familienangehörigen ausgerichtet wurden, stand  doch schon vor Beendigung der Bauphase bereits fest, dass die Häuser von der Familie  bezogen werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/143627.1`) (sent_id: `deanon_BFG_20260814_TEST/143627.1_6`)


Die mit dem angefochtenen Bescheid festgesetzte Umsatzsteuer von EUR 1.312.974,60 haftet  auf dem Abgabenkonto der Beschwerdeführerin nach wie vor unberichtigt aus, was aufgrund  der Einsichtnahme des Bundesfinanzgerichts in die elektronische Verfahrensdokumentation  „Zentrale Anwendungen“ festzustellen war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_27`)


Unternehmensangelegenheiten zu kümmern und im konkreten Fall das Schreiben des  Bundesfinanzgerichts früher abzuholen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_28`)


Am 16. Dezember, dem ersten Tag, an dem ich mich  wieder erheben durfte, habe ich als Erstes das Schreiben des Bundesfinanzgerichts abgeholt,  weil ich es als eine Priorität betrachtete.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/144676.1`) (sent_id: `deanon_BFG_20260814_TEST/144676.1_87`)


7.5. Die Kriterien des Art. 8 Abs. 1 lit. a EU-Notfallmaßnahmen-VO sind für die Herabsetzung  auf € 120/MWh ab Juni 2023 nach Ansicht des Bundesfinanzgerichts erfüllt: Weder verzerrt die  Maßnahme das Funktionieren der Stromgroßhandelsmärkte (vgl. Art. 8 Abs. 2 Buchst.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/144676.1`) (sent_id: `deanon_BFG_20260814_TEST/144676.1_128`)


Diese  Maßnahme steht nach Ansicht des Bundesfinanzgerichts auch im Zusammenhang mit dem  EKB-S.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/144676.1`) (sent_id: `deanon_BFG_20260814_TEST/144676.1_146`)


Da unmittelbar anwendbares Unionsrecht Anwendungsvorrang  genießt, ergibt sich nach Ansicht des Bundesfinanzgerichts auch kein Verstoß gegen das  objektive Nettoprinzip, wenn das EKBSG an Erträge bzw. Markterlöse anstelle von Gewinnen  anknüpft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_58`)


Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 28.2.2023  wurde die gegenständliche Rechtssache der mit 1.1.2023 neu besetzten Gerichtsabteilung  5010 zugewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_159`)


Die Feststellungen zu den Gesellschaftsverhältnissen der Bf. ergeben sich aus den vorliegenden  Verfahrensakten und der vorgenommenen Einsichtnahme des Bundesfinanzgerichts in das  Firmenbuch.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_195`)


Dieser Ansicht wird seitens des Bundesfinanzgerichts nicht gefolgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_35`)


Daher konnte der Sachverhalt  der rechtlichen Beurteilung des Bundesfinanzgerichts zugrunde gelegt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_50`)


In diesem Zusammenhang ist zu erwähnen, dass der Beschwerdeführer, wenn er das  Erkenntnis des Bundesfinanzgerichts für rechtswidrig gehalten hätte, das Rechtsmittel der  außerordentlichen Revision an den Verwaltungsgerichtshof erheben hätte können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_52`)


In beiden Rechtsmittelverfahren hätte eine höchstgerichtliche Kontrolle des  unterinstanzlichen Erkenntnisses des Bundesfinanzgerichts herbeigeführt werden können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_53`)


Aber selbst wenn man hypothetisch davon ausgehen würde, dass sich das damalige Erkenntnis  des Bundesfinanzgerichts durch eine spätere, klarstellende höchstgerichtliche Rechtsprechung  in einem gleichgelagerten Fall als tatsächlich unrichtig herausstellen sollte, wäre nach der  klaren Rechtsprechung des Verwaltungsgerichthofes keine Unbilligkeit iSd § 236 BAO gegeben  und eine Nachsicht nicht zulässig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_56`)


Der Vollständigkeit halber sei hier erwähnt, dass soweit ersichtlich bislang keine abschließende  höchstgerichtliche Klärung der ihm Ursprungsverfahren strittigen Rechtsfrage erfolgt ist und  lediglich divergierende Beurteilungen durch verschiedene Richter des Bundesfinanzgerichts  vorliegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_63`)


Für  die bloße Berücksichtigung einer vorgebrachten Ungleichbehandlung durch divergierende  Erkenntnisse des Bundesfinanzgerichts in vergleichbaren Fällen, ist daher im  Nachsichtverfahren kein Raum.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_96`)


Nach Dafürhalten des Bundesfinanzgerichts sind im gegenständlichen Fall die Voraussetzungen  für eine Androhung und in weiterer Folge die Festsetzung einer Zwangsstrafe gemäß § 111  BAO iVm § 16 WiEReG ohne Zweifel gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_34`)


Diese Einkünfte sind jedoch (nach Ansicht des Bundesfinanzgerichts) nicht in  das Einkommen gemäß § 33 Abs. 1 EStG, auf das in § 9a FLAG verwiesen wird, einzubeziehen,  da dieses nur Tarifeinkünfte umfasst.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_39`)


Von Seiten des Bundesfinanzgerichts wird diesbezüglich auf den klaren Gesetzeswortlaut des  § 9 Abs 3 KStG verweisen, wonach als Gruppenträger unbeschränkt steuerpflichtige  Kapitalgesellschaften und Erwerbs- und Wirtschaftsgenossenschaften, die unter § 7 Abs 3 KStG  fallen, unbeschränkt steuerpflichtige Versicherungsvereine auf Gegenseitigkeit im Sinne des  VAG 2016, unbeschränkt steuerpflichtige Kreditinstitute im Sinne des Bankwesengesetzes,  sowie beschränkt steuerpflichtige in der Anlage 2 zum EStG in der jeweils geltenden Fassung  genannten, den von den Teilstrichen 1 bis 4 umfassten inländischen Rechtsformen  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_65`)


3.2 Zu Spruchpunkt II. (Unzulässigkeit der Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichts ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch den Richter Mag. David Hell LL.B. LL.M. in der Beschwerde- sache Geraldine Loeper, Bakk. techn., Südstraße 6, 6471 Leins, Österreich, zur Beschwerde vom 20. November 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 16-579/1693, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde- vorentscheidung vom 15. Jänner 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2022 kein Vorlageantrag eingebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Mag. David Hell LL.B. LL.M.` (person)
- `Geraldine Loeper, Bakk. techn.` (person)
- `Südstraße 6, 6471 Leins, Österreich` (address)
- `16-579/1693` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_170`)


In diesem Lichte vermöge auch die Argumentation des Bundesfinanzgerichts nicht zu  überzeugen, welches zusammenfassend ausführe, dass kein Verstoß gegen den Gleichheitssatz  vorliege, weil Investitionen abgesetzt werden könnten und weil es durch die Krisensituation zu  Preissteigerungen gekommen sei, denen keine erhöhten Grenzkosten gegenüberstehen  würden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_548`)


Da die Begründung für die unterschiedlichen Bemessungsgrundlagen von EKB-S und  Solidaritätsbeitrag bereits in den Erwägungsgründen der EU-NotfallsmaßnahmenVO sachlich  begründet wurden, besteht bzw bestand nach Ansicht des Bundesfinanzgerichts keine  verfassungswidrige Ungleichbehandlung von Stromerzeugern und fossilen Energieträgern.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/146295.1`) (sent_id: `deanon_BFG_20260814_TEST/146295.1_6`)


Mit Erkenntnis des Bundesfinanzgerichts vom 9. April 2019 zu RV/7104981/2018, wurde  den Beschwerden der Bf. gegen die Abweisungsbescheide Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/146295.1`) (sent_id: `deanon_BFG_20260814_TEST/146295.1_8`)


Aufgrund des Erkenntnisses des Bundesfinanzgerichts vom 9. April 2019  seien dem Abgabenkonto Beträge in Höhe von insgesamt € 4.337.205,12 gutgeschrieben  worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/146295.1`) (sent_id: `deanon_BFG_20260814_TEST/146295.1_27`)


Nach einem Beschwerdeverfahren wurden die Dienstgeberbeiträge mit Erkenntnis des  Bundesfinanzgerichts vom 9. April 2019, GZ. RV/7104981/2018, mit Null festgesetzt, woraus  sich eine Gutschrift am Abgabenkonto in Höhe von insgesamt € 4.337.205,12 ergab.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_74`)


Es entspricht aber der Rechtsprechung des Verwaltungsgerichtshofes  (vgl. neuerlich VwGH 21.12.2016, Ro 2015/13/0008), dass die Erfüllung der Unterhaltspflichten  im Entscheidungszeitpunkt des Bundesfinanzgerichts zu beurteilen ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/146562.1`) (sent_id: `deanon_BFG_20260814_TEST/146562.1_9`)


Der Bf. bekämpfte den Einkommensteuerbescheid 2022 mit Beschwerde vom 23. August 2023,  welchem mit Erkenntnis des Bundesfinanzgerichts vom 18. Dezember 2024, RV/7102099/2024,  teilweise Folge gegeben und die Einkommensteuer auf EUR 1.880,00 reduziert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_159`)


Die vom Finanzamt in der Beschwerdevorentscheidung festgestellten  Einkunftsverhältnisse des Prokuristen (siehe I. Verfahrensgang Pkt. 3.1.) gelten auch für die  gegenständliche Beschwerdeentscheidung des Bundesfinanzgerichts als festgestellt. Die vom  Prokuristen in den Jahren 2014 und 2017 vorgenommenen Einlagen auf das  Verrechnungskonto des Prokuristen stammen nicht aus eigenen Vermögens- oder  Einkunftsquellen des Prokuristen und wurden mit nicht erklärten bzw. nicht verbuchten  Betriebseinnahmen der Bf. vorgenommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_164`)


Die Feststellungen zu den Gesellschaftsverhältnissen, zum Geschäftsführer und zum  Prokuristen der Univ.-Prof. Julian Czernitzki  ergeben sich aus den vorliegenden Verfahrensakten und wurden  durch Einsichtnahme des Bundesfinanzgerichts in das Firmenbuch bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Univ.-Prof. Julian Czernitzki` (person)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_173`)


Nach Ansicht des  Bundesfinanzgerichts handelt es sich bei diesem Beschwerdevorbringen um eine reine  Behauptung, die nicht nachgewiesen wurde und auch sonst durch keine Umstände  erschließbar wäre.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_175`)


Auf Grund dieser Beweisergebnisse ist nach Ansicht des  Bundesfinanzgerichts das Verrechnungskonto jedenfalls dem Prokuristen P. zuzurechnen, auf  dem auch die vom Prokuristen getätigten Entnahmen aus dem Vermögen der Bf. gebucht  wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_221`)


9. Auf dieser Grundlage ist es nach Ansicht des Bundesfinanzgerichts nicht zu beanstanden,  wenn das Finanzamt den zum 01.01.2014 auf dem Verrechnungskonto aufscheinenden Saldo  in Höhe von € 49.412,74 als verdeckte Ausschüttung beurteilt hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_230`)


Nach Ansicht des Bundesfinanzgerichts ist es nicht rechtswidrig, wenn das Finanzamt den  am 01.01.2014 auf dem Verrechnungskonto aushaftenden Saldo und die im Prüfungszeitraum  vom Prokuristen getätigten Entnahmen als verdeckte Ausschüttungen an den  Alleingesellschafter beurteilt hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

## `Pensions Insurance` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

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
| 1.000 | 0.005 | 0.009 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 4578 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_79`)


Die Beschwerdeführerin hat  im Jahr 2014 ihr Arbeitsverhältnis als Grenzgängerin im Alter von 59 Jahren beendet und eine  Pension der Pensionsversicherungsanstalt bezogen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_93`)


So hat zum Beispiel bei einer gemeinsamen Versteuerung mehrerer Pensionen, die durch eine  Pensionsversicherungsanstalt ausbezahlt werden, z.B. einer Eigen- und einer Witwenpension,  keine Pflichtveranlagung gemäß § 41 Abs. 1 Z 2 EStG 1988 zu erfolgen (vgl. Peyerl in Jakom  EStG, 14.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_20`)


5. Dazu wurde ein Bescheid der Pensionsversicherungsanstalt v. 31.8.2021 vorgelegt, woraus  hervorgeht, dass der Bf aufgrund festgestellter, nunmehr dauernder Arbeitsunfähigkeit  anstelle Reha-Geld ab 1.11.2021 die Invaliditätspension zusteht.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_148`)


Die abschließende Argumentation der Bf, "vor allem befinde ich mich seit 1.11.2021 auf Grund  meiner psychischen Erkrankung in der Invaliditätspension", geht von vorneherein völlig ins  Leere, weil damit seitens der Pensionsversicherungsanstalt die voraussichtlich dauerhafte  Arbeitsunfähigkeit der Bf nach Wiederbegutachtung überhaupt erst ab dieser Zeit, ab  November 2021, dh. erst viele Jahre nach Beendigung ihrer beruflichen Tätigkeit im Jahr 2013,  attestiert wird (siehe PV-Bescheid vom 31.8.2021).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_24`)


In den  Kalenderjahren 2017 bis 2021 habe der Bf. vom AMS bzw von der österreichischen  Pensionsversicherungsanstalt insgesamt € 80.757,19, also durchschnittlich € 1.345,95  monatlich erhalten.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `AMS` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_28`)


Er  bezog im gegenständlichen Jahr ganzjährig Einkünfte von der Pensionsversicherungsanstalt als  Pensionist.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_14`)


Ab  1.8. bis 31.12.2015 empfing er Pensionszahlungen von der Pensionsversicherungsanstalt in  Höhe von 1.459,95 Euro.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_41`)


Seit 1.8.2015 beziehe er eine Pension von  der Pensionsversicherungsanstalt. Am 2.4.2015 sei die Freizügigkeitsleistung ausbezahlt  worden.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_195`)


Das hat folgende Auswirkung auf die Berechnung der Einkommensteuer 2015:  Einkünfte aus nichtselbständiger  Arbeit   Pensionsversicherungsanstalt  1.459,95 €  Einkünfte ohne inländischen Steuerabzug (Obligatorium) 62.740,92 €  Pauschbetrag für Werbungskosten -132,00 €  Gesamtbetrag der Einkünfte   64.068,87 €  Sonderausgaben (§ 18 EStG 1988)   Pauschbetrag für Sonderausgaben -60,00 €  Sonderausgaben -360,00 €  Einkommen 63.648,87 €  Progressionsvorbehalt:  Hochzurechnende Einkünfte: 1.459,95 €  Umrechnungsbasis 1.459,95 €

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/143660.1`) (sent_id: `deanon_BFG_20260814_TEST/143660.1_7`)


Die belangte Behörde hat aufgrund von der Pensionsversicherungsanstalt übermittelter  Lohnzettel am 26.09.2022 betreffend den Beschwerdeführer (in weiterer Folge kurz BF) einen  Bescheid betreffend die Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2015  sowie einen Einkommensteuerbescheid 2015 (Sachbescheid), am 27.09.2022 einen Bescheid  betreffend die Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2016 sowie  einen Einkommensteuerbescheid 2016 (Sachbescheid) und am 30.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/144714.1`) (sent_id: `deanon_BFG_20260814_TEST/144714.1_31`)


Seit 1.6.2020 erhält der Sohn der Beschwerdeführerin Bezüge von der  Pensionsversicherungsanstalt.     2.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_118`)


Im Übrigen ist aus dem vom Beschwerdeführer  vorgelegten Bescheid der Pensionsversicherungsanstalt vom 3.7.2014 auch keine  Verminderung des Pflegegeldes um diesen Freibetrag ersichtlich.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/146562.1`) (sent_id: `deanon_BFG_20260814_TEST/146562.1_5`)


Entscheidungsgründe  I. Verfahrensgang  1. Festsetzung der ESt-Vorauszahlungen 2023:  Der Beschwerdeführer (in der Folge als Bf. bezeichnet) bezog im Jahre 2022 Pensionseinkünfte  im Gesamtbetrag von EUR 35.746,08 von der Pensionsversicherungsanstalt sowie von ORF und  erzielte darüber hinaus Einkünfte aus freier journalistischer Tätigkeit, welche mit  Einkommensteuerbescheid 2022 vom 9. August 2023 mit EUR 3.583,97 berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/146931.1`) (sent_id: `deanon_BFG_20260814_TEST/146931.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) bezog im Streitjahr neben einer von Seiten der  Pensionsversicherungsanstalt zu Auszahlung gebrachten inländischen Alterspension (€  32.398,24 brutto) auch deutsche Renteneinkünfte in Höhe von € 2.991,00 brutto (Bescheid des  Finanzamtes Neubrandenburg/BRD vom 17.6.2022).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_101`)


Laut ärztlichem Gutachten der Pensionsversicherungsanstalt Wien vom 18.08.2022 sowie laut  chefärztlicher Stellungnahme der Pensionsversicherungsanstalt Wien vom 01.09.20222 ist  Arbeitsfähigkeit am allgemeinen Arbeitsmarkt des Beschwerdeführers für voraussichtlich 24  Monate nicht gegeben.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_102`)


Beweis: beiliegendes ärztliches Gutachten samt chefärztlicher Stellungnahme der  Pensionsversicherungsanstalt Wien  7 von 16 Seite 8 von 16

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_61`)


Der Bf. hat am 8. September 2016 erstmals den Antrag bei der österreichischen  Pensionsversicherungsanstalt auf Überprüfung seiner Anspruchsvoraussetzungen gestellt  (Antrag auf „PRÜFUNG DER VERSICHERUNGSRECHTLICHEN ANSPRUCHSVORAUSSETZUNGEN  FÜR EINE LEISTUNG AUS DEN VERSICHERUNGSFÄLLEN DES ALTERS ZUM FRÜHESTMÖGLICHEN  ZEITPUNKT“).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_64`)


Die Feststellung im  Zusammenhang mit der österreichischen Pensionsversicherungsanstalt ergeben sich aus dem  Schreiben vom 15. Mai 2025, mit dem die österreichische Pensionsversicherungsanstalt ein  Amtshilfeersuchen des Bundesfinanzgericht vom 12. März 2025 beantwortete.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_128`)


Lebensjahres seit 01.11.2016 die  Korridorpension von der österreichischen Pensionsversicherungsanstalt.   8 von 9 Seite 9 von 9

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `Fraud Investigation Office` 🏆

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

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
| 1.000 | 0.008 | 0.016 | 38 | 38 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 38 | 0 | 4561 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_7`)


Im Februar 2015 wurde die Finanzpolizei seitens der Landespolizeidirektion zum "Verdacht  einer Übertretung nach § 82 Abs. 8 KFG" durch Sven Mitterhuber (= Beschwerdeführer, Bf)  verständigt und ua.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Landespolizeidirektion` (organisation)
- `Sven Mitterhuber` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_119`)


Entsprechend einem Erhebungsauftrag wurde von der Finanzpolizei am inländischen  Wohnsitz des Bf die Vermieterin befragt, die lt. Aktenvermerk am 25.2.2016 ua. angegeben  hat:  Der Bf bewohne im Gebäude ein Zimmer mit 5 m² in einer 2-Zimmer-Wohnung;

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_305`)


Es wurde in Deutschland unter dem Kz X1 auf ihn  zugelassen, vom Bf im Oktober 2011 nach Österreich eingebracht und hier verwendet  (Erhebungen der Finanzpolizei Feber 2015; eigene Angaben lt. Niederschrift v. 22.4.2015;

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_6`)


In einer Niederschrift mit der KIAB (nunmehrige Finanzpolizei) am 15.5.2008 gab Herr C  insbesondere an, dass die Brüder seit drei Jahren als „selbständige Arbeiter“ tätig seien, es  keine Werkverträge gebe und er die Qualitätskontrolle durchführe und das Material zur  Verfügung stelle.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_79`)


2. Beweiswürdigung  Der Sachverhalt ist auf Grund des Finanzamtsaktes sowie der Eingaben der Bf und der  schriftlichen Aussagen des Herrn C vor der KIAB (nunmehr Finanzpolizei) bzw. des  Strafverfahrens des Magistrats der Stadt Wien gegen die Geschäftsführerin der Bf wegen  illegaler Beschäftigung nach dem AuslBG als erwiesen anzusehen.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_42`)


Eine Anzeige an die Staatsanwaltschaft sowie Finanzpolizei sei erfolgt.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_6`)


Bei einer Anhaltung des Fahrzeuges der Marke AA mit dem deutschen Kennzeichen D1 im  März 2013 wurde von der Finanzpolizei festgestellt, dass das Fahrzeug auf Frau B mit Wohnsitz  in D-Ort1 seit 09/2007 zugelassen ist und von Florentine Mugge (= Beschwerdeführer, Bf), dieser mit  Wohnsitz im Inland in A-Ort2, Str1, gelenkt wird.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Florentine Mugge` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_22`)


Von der  Finanzpolizei wurden diese Subunternehmer im Zuge der Kontrolle vom 24.5.2016 nicht als  eigenständige Unternehmer anerkannt und wurden diese Subunternehmer als Dienstnehmer  der N eingestuft.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_80`)


Zu bemängeln sei, dass die GPLA-Prüfung nur jene Argumente aus den von der Finanzpolizei  erstellten Protokollen übernommen habe, die die Ansicht stützten, dass  Arbeitskräfteüberlassung vorliege.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_95`)


Die Aufzeichnungen der Arbeitszeiten der Mitarbeiter von M und N erfolge in Papierform  durch die jeweiligen Vorarbeiter (siehe dazu die Protokolle der Finanzpolizei).

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_252`)


Das Bundesfinanzgericht geht diesbezüglich – ebenso wie das Finanzamt – davon aus,  dass die im Zuge der finanzpolizeilichen Erhebungen zu den Verwaltungsakten  genommenen Verträge sowie die Inhalte der von Organen der Finanzpolizei  aufgenommenen Niederschriften (siehe Ausführungen des Finanzamtes in der  Vorhaltsbeantwortung vom 09. März 2020) auch die Gegebenheiten der Streitjahre  wiederspiegeln und legt seiner Entscheidung den sich daraus ergebenden Sachverhalt  zu Grunde.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_126`)


Ein Ansuchen um eine allfällige Zahlungserleichterung wäre bei der  Finanzstrafbehörde (Amt für Betrugsbekämpfung, Bereich Strafsachen) einzubringen.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_11`)


Bei einer Anhaltung durch die Finanzpolizei am 3.7.2012 wurde A (= Beschwerdeführer, Bf)  im Inland als Lenker des Fahrzeuges MarkeX mit dem italienischen Kennzeichen IT1, zugelassen  auf die Fa.Monal Bau Betriebe GmbH in I/Ort1, sowie an Fahrzeugdaten festgestellt: FIN Nr12, Kauf gebraucht,  Erstzulassung 14.12.2009, zugelassen auf Fa.Monal Bau Betriebe GmbH 23.11.2011, Diesel, 200 kW,  Kilometerstand bei Kauf 120.000 und derzeit 182.000, CO2-Wert 294 g/km.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Fa.Monal Bau Betriebe GmbH` (organisation)
- `Fa.Monal Bau Betriebe GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_35`)


Die dem Bundesfinanzgericht vorgelegten Aktenteile, namentlich der  Vorhalt vom 26.02.2018, der am 09.04.2019 ausgefertigte Einkommensteuerbescheid 2017,  das Ermittlungsergebnis vom 28.02.2022 zu den Erhebungen der Finanzpolizei und der email- Verkehr vom 03.05.2022 und 07.04.2022 enthalten keinen Hinweis auf eine unternehmerische  bzw. gewerbliche Tätigkeit des Beschwerdeführers.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_11`)


Die Anzeigerin sieht sich als Unterstützerin im Kampf gegen illegales Glückspiel mit einer  kontinuierlichen Marktbeobachtung und lässt zu diesem Zweck Lokale, in denen Glücksspiel  angeboten wird, besuchen und darüber Berichte erstellen bzw. Anzeigen bei den  Verwaltungsbehörden bzw. der Finanzpolizei wegen verbotenen Ausspielungen iSd § 2 Abs. 4  GSpG erstatten.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_10`)


I. Verfahrensgang  Nach einem von der Finanzpolizei durchgeführten Ermittlungsverfahren wurden vom  Finanzamt am 25.06.2013 die Bescheide betreffend Festsetzung der Umsatzsteuer für den  Erwerb neuer Fahrzeuge (Fahrzeugeinzelbesteuerung) für den PKW Ford Mondeo, Festsetzung  der Normverbrauchsabgabe 1/2012 sowie Kraftfahrzeugsteuer 1-12/2012 und 1-3/2013  erlassen.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_61`)


Diese Angaben wurden  offensichtlich auch von der belangten Behörde für glaubhaft erachtet, da in den vorgelegten  Akten auch eine Kontrollmitteilung der Finanzpolizei enthalten ist, in welcher der  Sachbearbeiter diese Angaben seinem festgestellten Sachverhalt zugrunde legt.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_22`)


Die für schriftliche Anbringen geltenden  Bestimmungen sind auch in diesen Fällen mit der Maßgabe anzuwenden, daß das Fehlen einer  Unterschrift keinen Mangel darstellt. Die Abgabenbehörde und das Verwaltungsgericht können  jedoch, wenn es die Wichtigkeit des Anbringens zweckmäßig erscheinen läßt, dem Einschreiter  die unterschriebene Bestätigung des Anbringens mit dem Hinweis auftragen, daß dieses nach  fruchtlosem Ablauf einer gleichzeitig zu bestimmenden angemessenen Frist als  zurückgenommen gilt.  Für Anbringen im Sinn des § 86a Abs. 1 erster Satz BAO, die in Abgaben-, Monopol- oder  Finanzstrafangelegenheiten an das Bundesministerium für Finanzen, an die  Verwaltungsgerichte, an ein Finanzamt, an das Zollamt Österreich oder an das Amt für  Betrugsbekämpfung gerichtet werden, wird die Einreichung unter Verwendung eines  Telekopierers (Telefaxgerätes) zugelassen.

| Predicted | Gold |
|---|---|
| `Amt für  Betrugsbekämpfung` | `Amt für  Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesministerium für Finanzen` (organisation)
- `Finanzamt` (organisation)
- `Zollamt Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_2`)


Wolfram Simma, Scheffelstraße 1, 6900 Bregenz, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die  Beschwerde des Beschuldigten (undatiertes Schreiben, eingegangen beim Finanzamt am  30.10.2020) gegen das Erkenntnis des Spruchsenates II beim Finanzamt Feldkirch als Organ des  Finanzamtes Bregenz als Finanzstrafbehörde (nunmehr Amt für Betrugsbekämpfung als  Finanzstrafbehörde) vom 24. September 2020, Strafnummer/Geschäftszahl FV-001134 032, in  der Sitzung vom 15. September 2022 nach Durchführung einer mündlichen Verhandlung in  Anwesenheit des Beschuldigten und der Amtsbeauftragten Mag. Nadine Lampert zu Recht  erkannt:  I. Der Beschwerde wird teilweise Folge gegeben und der Spruch des angefochtenen  Erkenntnisses wie folgt abgeändert:  VetR Vivian Hirtel  ist schuldig, er hat im Bereich des Finanzamtes Bregenz grob fahrlässig unter  Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht nämlich  durch Abgabe einer unrichtigen Einkommensteuererklärung für das Jahr 2017, in der er seine  aus Liechtenstein erzielten Einkünfte aus Kapitalvermögen nicht anführte, eine Verkürzung an  Einkommensteuer 2017 in Höhe von € 33.356,00 bewirkt.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt Feldkirch` (organisation)
- `Finanzamtes` (organisation)
- `Mag. Nadine Lampert` (person)
- `VetR Vivian Hirtel` (person)
- `Finanzamtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_247`)


Ein  Ansuchen um eine allfällige Zahlungserleichterung (z.B. Ratenzahlung oder Stundung) wäre bei  der Finanzstrafbehörde (per Fax an die Nr. 050 233 595 2104 oder postalisch an das Amt für  Betrugsbekämpfung, Postfach 252, 1000 Wien, Team Einhebung und Einbringung Finanzstrafen  Bereich Finanzstrafsachen) einzubringen.

| Predicted | Gold |
|---|---|
| `Amt für  Betrugsbekämpfung` | `Amt für  Betrugsbekämpfung` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_73`)


Die Finanzpolizei fand bei einer Kontrolle vom 9.5.2014 auf den 10.5.2014 Frau *** A, die zu  diesem Zeitpunkt nicht ordnungsgemäß angemeldet war, in der Bar in ihrer Tätigkeit als  Kellnerin vor.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Dieter Avemaria` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Dieter Avemaria` (person)
- `Engelbert Schefe` (person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_5`)


Gegen diesen Bescheid erhob  die Beschwerdeführerin am 25. April 2024 die am selben Tag beim Amt für Betrugsbekämpfung  als Finanzstrafbehörde eingelangte Beschwerde.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_10`)


Diese Beschwerde hat das Amt für Betrugsbekämpfung als Finanzstrafbehörde am 21. Juni  2024 vorgelegt.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_29`)


Am 08. Jänner 2024 versendete das Amt für Betrugsbekämpfung, Bereich Finanzstrafsachen  Team *TN*, ein über die auf dem Kuvert angeführte Geschäftszahl als Strafverfügung nach §  143 FinStrG identifizierbares Dokument mittels „RSa-Briefes“ an die Antragstellerin;

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_31`)


Dieses Dokument wurde vom  Zustelldienst am 10. Jänner 2024 mit dem Vermerk „unbekannt" an das Amt für  Betrugsbekämpfung rückgesendet und langte dort am 12. Jänner 2024 ein.

| Predicted | Gold |
|---|---|
| `Amt für  Betrugsbekämpfung` | `Amt für  Betrugsbekämpfung` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_32`)


Das Amt für  Betrugsbekämpfung versendete das Dokument daraufhin mittels RSa-Briefes an Merlin Gronmeyer, p.  A. *G*, *G Adr*.

| Predicted | Gold |
|---|---|
| `Amt für  Betrugsbekämpfung` | `Amt für  Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Merlin Gronmeyer` (person)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_10`)


Aufgrund dieser Wahrnehmungen sei die Bf durch die Finanzpolizei am 19.06.2020  niederschriftlich einvernommen und betreffend die Verwendung dieses Fahrzeuges in  Österreich befragt worden.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_17`)


Nach den Ermittlungen der Finanzpolizei hätte die Bf seit 28.1.2013 ihren ständigen Wohnsitz in  Österreich und seit 30.4.2018 in A. Auch ihre minderjährigen Kinder (2 Jahre und 2 Monate)  leben mit der Bf gemeinsam an derselben Adresse.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_40`)


Weiters werde in eventu beantragt, die Angelegenheit  zur neuerlichen Entscheidung an die Finanzpolizei C bzw. das Finanzamt „zurückverweisen“.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_46`)


In der Niederschrift vom 19.6.2020 gaben Sie der Finanzpolizei gegenüber an, dass  Sie das Fahrzeug aufgrund einer Nutzungsvereinbarung mit Ihrem Vater nutzen dürfen.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_60`)


Sie gaben in der Niederschrift durch die  Finanzpolizei an, dass Sie das Auto im Mai 2018 dauerhaft nach Österreich verbracht haben.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_82`)


In der Niederschrift vom 19.6.2020 gab die Bf der Finanzpolizei  gegenüber an, dass sie das Fahrzeug aufgrund einer Nutzungsvereinbarung mit ihrem Vater  nutzen darf.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_96`)


Die Bf gab in der Niederschrift durch die Finanzpolizei an,  dass sie das Auto im Mai 2018 dauerhaft nach Österreich verbracht hat.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_222`)


Auch in der Einvernahme vor der  Finanzpolizei (ON 19 Seite 4 von 8) hat die Bf bereits angegeben, dass ihr Vater ihr das  Fahrzeug dauerhaft auf Grund der Geburt ihrer Tochter geliehen hat bzw. dauerhaft zur  Verfügung gestellt hat, damit sie in Österreich ein Fahrzeug hat.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_320`)


In der Niederschrift der Finanzpolizei (OZ 19) gibt die Bf, befragt über den Kilometerstand des  Fahrzeuges zum Zeitpunkt der Einbringung nach Österreich, an: „ Das kann ich nicht mehr  genau sagen, ich denke es hatte ca. 120.000 km oben.“

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden des Finanzstrafsenates 6008-6  Mag. Johann Fischerlehner in der Finanzstrafsache gegen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich, wegen  der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 2a des Finanzstrafgesetzes  (FinStrG) über die Beschwerden der Beschuldigten vom 22.09.2023 und der Amtsbeauftragten  vom 09.10.2023 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung -  Team als Finanzstrafbehörde vom 14.07.2023 beschlossen:  Das angefochtene Erkenntnis des Spruchsenates vom 14.07.2023, Gz., Team wird gemäß § 161  Abs. 4 FinStrG aufgehoben und die Finanzstrafsache in ihrem gesamten Umfang an die  Finanzstrafbehörde zur neuerlichen Entscheidung zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Amt für Betrugsbekämpfung` | `Amt für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Mag. Johann Fischerlehner` (person)
- `Dipl.-Ing. Heinz Riechels` (person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

</details>

---

## `Municipal Council` 🏆

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.007  

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
| 1.000 | 0.007 | 0.013 | 30 | 30 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 30 | 0 | 4569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_71`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung  der Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für  das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer  Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem  Muster der Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_75`)


Dieses wird durch  die Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird  (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_391`)


Gemäß § 5 Abs. 2 der Verordnung des Wiener Gemeinderates, mit der für das Abstellen von  mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben  wird (Parkometerabgabeverordnung) idgF sind zur Entrichtung der Abgabe der Lenker, der  Besitzer und der Zulassungsbesitzer zur ungeteilten Hand verpflichtet.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_69`)


Rechtsgrundlagen:   § 2 Wiener Parkometergesetz 2006 normiert:   (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß §  25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_54`)


Rechtsgrundlagen  § 2 Wiener Parkometergesetz 2006 idF LGBl. für Wien Nr. 24/2012 normiert:   (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen Kraft- fahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für dessen  Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu entrichten  war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß § 25 StVO  1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005, abgestellt  war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem bestimm- ten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_125`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_130`)


Dieses wird durch die  Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahr- zeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird (Parkometerab- gabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_102`)


Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen Kraft- fahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für dessen  Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu entrichten  war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß § 25 StVO  1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005, abgestellt  war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem bestimm- ten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_48`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_53`)


Dieses wird durch die  Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen Kraft- fahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird (Parkometer- abgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_55`)


Dieses wird durch die Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_44`)


Gesetzliche Grundlagen:  § 2 Wiener Parkometergesetz 2006 idF LGBl. für Wien Nr. 24/2012 normiert:  (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_94`)


Gemäß § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird, Parkscheine nach dem Muster der Anlagen oder elektronische  Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_85`)


Gemäß § 5 der Verordnung des Wiener Gemeinderates über die Art der zu verwendenden  Kontrolleinrichtungen in Kurzparkzonen (Kontrolleinrichtungenverordnung) sind Parkscheine  bei mehrspurigen Kraftfahrzeugen mit Windschutzscheibe hinter dieser und durch diese gut  erkennbar, bei anderen mehrspurigen Kraftfahrzeugen an einer sonst geeigneten Stelle gut  wahrnehmbar anzubringen.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_58`)


Rechtsgrundlagen und Würdigung:  In § 2 Wiener Parkometergesetz 2006 ist angeordnet:   "(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl.I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_78`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  6 von 13 Seite 7 von 13

| Predicted | Gold |
|---|---|
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_79`)


die Entrichtung einer Abgabe vorgeschrieben wird, sind Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung des Wiener  Gemeinderates über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABl Nr 2013/29).

| Predicted | Gold |
|---|---|
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_83`)


Gemäß § 1 Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_52`)


Über die Beschwerde wurde erwogen:  Gemäß § 2 Parkometergesetz hat der er Zulassungsbesitzer und jeder, der einem Dritten das  Lenken eines mehrspurigen Kraftfahrzeuges oder die Verwendung eines mehrspurigen  Kraftfahrzeuges überlässt, für dessen Abstellen gemäß Verordnung des Wiener Gemeinderates  eine Parkometerabgabe zu entrichten war, falls das Kraftfahrzeug in einer gebührenpflichtigen  Kurzparkzone gemäß § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes  BGBl. I Nr. 99/2005, abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das  Kraftfahrzeug zu einem bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_20`)


Gemäß § 5 Abs. 2 der Parkometerabgabeverordnung des  Wiener Gemeinderates entstehe die Abgabepflicht bereits bei Beginn des Abstellens.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_31`)


§ 1 der Verordnung des Wiener Gemeinderates über die Art der zu verwendenden Kontroll- einrichtungen in Kurzparkzonen (Kontrolleinrichtungenverordnung), ABI. Nr. 33/2008, laute  wie folgt:   ‚Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), sind Park- scheine nach dem Muster der Anlagen oder elektronische Parkscheine zu verwenden.‘

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_34`)


Dieses werde  durch Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben werde  (Parkometerabgabeverordnung), festgesetzt.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_77`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_67`)


Rechtsgrundlage und Würdigung:  § 2 Wiener Parkometergesetz 2006 normiert:   „(1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß  § 25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

| Predicted | Gold |
|---|---|
| `Wiener Gemeinderates` | `Wiener Gemeinderates` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_55`)


Als Hilfsmittel zur Überwachung der Einhaltung der Vorschriften der Verordnung des Wiener  Gemeinderates, mit der für das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen  die Entrichtung einer Abgabe vorgeschrieben wird, sind Parkscheine nach dem Muster der  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_56`)


Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung, des Wiener  Gemeinderates über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABI Nr 2013/29).

| Predicted | Gold |
|---|---|
| `Wiener  Gemeinderates` | `Wiener  Gemeinderates` |

</details>

---

## `Health Insurance` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.001 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 4596 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_85`)


Ich werde - so mir dies möglich ist - zur noch anzuberaumenden mündlichen Verhandlung vor dem Bundesfinanzgericht auch eine Bestätigung der Wiener Gebietskrankenkasse mitnehmen, aus der die Anzahl der bei mir in den Jahren 2012 und 2013 durchschnittlich beschäftigten Mitarbeiter ersichtlich ist.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_98`)


Die Feststellung, dass er im Zeitpunkt der Ausstellung der Honorarnoten von einer  nichtselbständigen Tätigkeit ausgegangen ist, beruht auf nachstehenden Erwägungen:  Anlässlich einer Befragung am 28.04.2016 bei der Wiener Gebietskrankenkasse durch die  Beitragsprüferin gab der Bf. u.a. zu Protokoll, „ihm sei nicht bewusst gewesen, dass er für die  6 von 11 Seite 7 von 11

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_108`)


Vor dem  Hintergrund seiner Angaben im Rahmen der Verfahren vor dem Arbeits- und Sozialgericht und  der Wiener Gebietskrankenkasse lässt die Tatsache, dass der Bf. nicht zu Beginn seines  Arbeitsverhältnisses, sondern erst im August 2014 eine UID-Nummer beantragt hat, nach  Auffassung des erkennenden Senates nur den Schluss zu, dass er davon überzeugt war, keine  unternehmerische Tätigkeit auszuüben.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

</details>

---

## `Administrative Court` 🏆

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

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
| 1.000 | 0.004 | 0.008 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 4580 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_316`)


Da keine gesicherte Judikatur des Verwaltungsgerichtshofs zur Frage, ob Art. 3 Abs. 8 UStG  1994 ob bei Verwendung einer österreichischen UID im Abgangsstaat die Vorschreibung einer  Erwerbsteuer auslöst bis der tatsächliche Erwerb im Bestimmungsstaat nachweislich  besteuert/erklärt wurde, wie es die derzeitige Verwaltungspraxis annimmt, ist die (ordentliche)  Revision zuzulassen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_142`)


Rechtliche Erwägungen zum festgestellten Sachverhalt:  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofs ist zum Begriff des Vertreters  auf die Verkehrsauffassung abzustellen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_55`)


Auch das von der belangten  Behörde herangezogene Erkenntnis des Verwaltungsgerichtshofs, 2012/15/0127, vermag die  Rechtsansicht der belangten Behörde nicht zu stützen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_105`)


Der Wissensstand der Behörde bezüglich der vorhergehenden Jahre ist nach der  Rechtsprechung des Verwaltungsgerichtshofs nicht maßgebend.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_61`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs sind Werbungskosten grundsätzlich  von Amts wegen zu berücksichtigen (VwGH 08.02.2007, 2004/15/0102).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_71`)


Nach der Judikatur des Verwaltungsgerichtshofs hat das Fahrtenbuch die beruflichen und  privaten Fahrten zu enthalten (vgl. VwGH 28.02.1964, 2176/63).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_83`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  7 von 9 Seite 8 von 9

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_85`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH  24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_83`)


Da das vorliegende Erkenntnis  des Bundesfinanzgerichtes der zitierten Rechtsprechung des Verwaltungsgerichtshofs folgt,  liegt keine Rechtsfrage vor, der grundsätzliche Bedeutung beizumessen wäre.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_86`)


Gehört das Kind innerhalb eines Monats zeitlich hintereinander unterschiedlichen Haushalten  an, so hat nach der Rechtsprechung des Verwaltungsgerichtshofs unter Anwendung des  Überwiegenheitsprinzips diejenige Person Anspruch auf Familienbeihilfe, die den Haushalt für  den längeren Zeitraum geführt hat (VwGH vom 28.11.2007, 2007/15/0058).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_60`)


Von Seiten des Verwaltungsgerichtshofs wurde daraufhin klargelegt, dass  nicht nur die Zinsaufwendungen und Zinserträge, sondern auch die erzielten Kursgewinne und  Kursverluste aus dem Sicherungsgeschäft steuerlich zu berücksichtigen sind (vgl VwGH  22.6.2022, Ra 2021/13/0149).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_61`)


Auszugsweise aus dem Erkenntnis des Verwaltungsgerichtshofs:  „Im vorliegenden Fall sollte mit den Mitteln aus der Aufnahme der  Fremdwährungsverbindlichkeit keineswegs eine Beteiligung angeschafft werden.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141488.1`) (sent_id: `deanon_BFG_20260814_TEST/141488.1_91`)


Wie aus der  zitierten Rechtsprechung des Verwaltungsgerichtshofs hervorgeht, ist das Neuhervorkommen  von Tatsachen stets aus der Sicht des jeweiligen Verfahrens zu beurteilen und steht es einer  Wiederaufnahme eines Verfahrens bei einem Steuerpflichtigen nicht entgegen, wenn die für  die Wiederaufnahme maßgeblichen Tatsachen in einem Verfahren eines anderen  Steuerpflichtigen bereits bekannt waren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141488.1`) (sent_id: `deanon_BFG_20260814_TEST/141488.1_101`)


Erst durch die mit  verfahrensgegenständlichen Bescheid verfügte Wiederaufnahme des  Einkommensteuerverfahrens konnte ein insgesamt rechtsrichtiges Ergebnis herbeigeführt  werden und ist nach der Rechtsprechung des Verwaltungsgerichtshofs dem Prinzip der  Rechtsrichtigkeit der Vorrang vor dem Prinzip der Rechtsbeständigkeit einzuräumen  (Ritz/Koran, BAO7, § 303, Rz. 67).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_19`)


 Erkenntnis des VwGH vom 20. Oktober 2021, Ra 2019/13/0041   Darin wurde wie folgt ausgeführt:  „Entscheidungsgründe:  1 Zur Vorgeschichte wird auf das Erkenntnis des Verwaltungsgerichtshofs vom 28. Juni 2016,  2013/13/0080, verwiesen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_151`)


Insoweit entspreche das Verhältnis der Verwaltungsgerichte zu  den Verwaltungsbehörden dem bisherigen [Anm: nach der Rechtslage vor dem 1. 1. 2014] des  Verwaltungsgerichtshofs zu den Behörden.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_415`)


Zweck der vom Gesetzgeber durch § 278 (1) BAO eingeräumten Möglichkeit einer Erledigung  durch Bescheidaufhebung und Zurückverweisung des Verfahrens an die Abgabenbehörde ist  die Beschleunigung des BFG-Rechtsmittelverfahrens und die Entlastung des  Verwaltungsgerichtshofs.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_345`)


Den (abweisenden) Beschwerdevorentscheidungen kommen nach  ständiger Rechtsprechung des Verwaltungsgerichtshofs Vorhaltscharakter zu (VwGH  18 von 29 Seite 19 von 29

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/149201.1`) (sent_id: `deanon_BFG_20260814_TEST/149201.1_29`)


Im Beschwerdefall hat gemäß § 98 Abs. 2 BAO und der Judikatur des Verwaltungsgerichtshofs  die Frist zur Einbringung der Bescheidbeschwerde mit der elektronischen Zustellung des  angefochtenen Bescheids in die FinanzOnline-Databox der Beschwerdeführerin am 27.  September 2024 begonnen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

</details>

---

## `Constitutional Court` 🏆

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

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
| 1.000 | 0.008 | 0.016 | 38 | 38 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 38 | 0 | 4561 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_25`)


Ist ein Gesetz wegen Verfassungswidrigkeit aufgehoben worden oder hat der  Verfassungsgerichtshof gemäß Art. 140 B-VG Abs. 4 ausgesprochen, dass ein Gesetz  verfassungswidrig war, so sind alle Gerichte und Verwaltungsbehörden an den Spruch des  Verfassungsgerichtshofes gebunden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_128`)


Auf Grund dieser Ausführungen des Verfassungsgerichtshofes hat das Bundesfinanzgericht  keine verfassungsrechtlichen Bedenken gegen die Bestimmungen Parkraumbewirtschaftung  der Stadt Wien, soweit sie im gegenständlichen Fall zur Anwendung gelangen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_86`)


Zu den in der Beschwerde angedeuteten verfassungsrechtlichen Bedenken der Bf. war auf das  zur Thematik ergangene Erkenntnis des Verfassungsgerichtshofes vom 1.3.2001, G 109/00, zu  verweisen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_38`)


Judikatur des Verwaltungs- und Verfassungsgerichtshofes zum Abzugsverbot hinsichtlich  Managergehälter und „Golden Handshakes“ sowie auf Ansichten im Schrifttum.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_54`)


Parken in einer gebührenpflichtigen Kurzparkzone am Gehsteig  Nach der höchstgerichtlichen Judikatur des Verfassungsgerichtshofes (VfGH) und des Ver- waltungsgerichtshofes (VwGH) dürfen innerhalb einer Kurzparkzone noch weitergehende  Verkehrsbeschränkungen wie Halte- oder Parkverbote erlassen werden, ohne dass das Gebiet  der Kurzparkzone dadurch unterbrochen wird (vgl. VfGH 06.12.1965, B 210/65, VwGH (vgl.  VwGH 14.02.1979, 892/78, VwGH 27.04.1995, 92/17/0300, VwGH 31.07.2003, 2003/17/0110).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_37`)


Wie der OGH schon wiederholt erkannt hat, ist unabdingbare Voraussetzung der Anrufung des  Verfassungsgerichtshofes, dass das Gericht selbst Bedenken gegen die Verfassungsmäßigkeit  des anzuwendenden Gesetzes bzw. die Gesetzmäßigkeit der anzuwendenden Verordnung hat;  der Umstand allein, dass eine Partei solche Bedenken vorbringt (oder dass im Schrifttum  Bedenken geäußert worden sind), berechtigt oder verpflichtet das Gericht noch nicht zur  Normenprüfung.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_549`)


Ob Bedenken gegen die  Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit bestehen ist nach  objektiven Gesichtspunkten zu prüfen, wobei auch die Art der in Frage stehenden Norm und  ihre Position im Normenzusammenhang in Betracht zu ziehen und auf die bisherige  Rechtsprechung des Verfassungsgerichtshofes Bedacht zu nehmen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_555`)


Nach der ständigen  Rechtsprechung des Verfassungsgerichtshofes (zB VfSlg.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_309`)


In diesem Zusammenhang ist auch festzuhalten, dass das Bundesfinanzgericht immer wieder -  in Anlehnung an die Rechtsprechung des Verfassungsgerichtshofes - zum Ausdruck gebracht,  dass es keine Zweifel an der Verfassungsmäßigkeit des Bewertungsgesetzes hegt (vgl. BFG  10.01.2017, RV/4100647/2016, mwN;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_313`)


Nach Ansicht des Verfassungsgerichtshofes liegt es auch im rechtspolitischen Spielraum des  Steuergesetzgebers, Grundbesitz einer speziellen Vermögenssteuer zu unterwerfen, auch  wenn andere Vermögenswerte einer vergleichbaren Steuer nicht unterliegen und eine solche  Steuer als Objektsteuer – das bedeutet unabhängig von den persönlichen Verhältnissen des  Grundeigentümers – auszugestalten (siehe dazu VfGH 06.10.2010, B 298/10).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_59`)


Soweit die Beschwerde verfassungsrechtliche - insbesondere gleichheitsrechtliche - Aspekte ins  Treffen führt, ist auf den Ablehnungsbeschluss des Verfassungsgerichtshofes vom  29. November 2011 zu verweisen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_148`)


In den hg. Erkenntnissen vom 17. Mai 1989, 85/13/0110, Slg. NF. Nr. 6.403/F (zitiert im  genannten Erkenntnis des Verfassungsgerichtshofes), vom 31. Juli 1996, 95/13/0220, Slg. NF.  Nr. 7.111/F, vom 9. Juli 1997, 95/13/0289, vom 23. Mai 2000, 97/14/0167, vom 20. Dezember  2000, 99/13/0223, Slg. NF. Nr. 7.569/F, vom 25. Jänner 2001, 95/15/0074, und zuletzt vom 24.  Juni 2004, 2001/15/0113, hat der Verwaltungsgerichtshof ausgesprochen, dass (nur) in Fällen,  in denen die im Gesetz festgeschriebenen Kriterien der Weisungsgebundenheit und der  Eingliederung in den geschäftlichen Organismus des Betriebes des Arbeitgebers noch keine  klare Abgrenzung zwischen einer selbständig und einer nichtselbständig ausgeübten Tätigkeit  ermöglichen, auf weitere Abgrenzungskriterien (wie etwa auf das Fehlen eines  Unternehmerrisikos) Bedacht zu nehmen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_11`)


Mit Schreiben des Verfassungsgerichtshofes vom 12.10.2021 wurde dem Bf. der Beschluss des  Verfassungsgerichtshofes betreffend Normenprüfung vom 22.09.2021 übermittelt sowie die  Aufforderung, die noch offene Eingabengebühr von € 240,- binnen einer Woche zu bezahlen  und den Original-Einzahlungsbeleg innerhalb von 10 Tagen dem Verfassungsgerichtshof zu  übermitteln.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_17`)


Dieser Antrag wurde dem Verfassungsgerichtshof zur Normenprüfung vorgelegt und erging am  22.09.2021 der Beschluss des Verfassungsgerichtshofes mit welchem der Antrag des Bf.  zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_73`)


Die Einbeziehung des Wochengeldes in die Einkünftegrenze des § 33 Abs 4 Z 1  EStG erfolgte in Reaktion auf das Erkenntnis des Verfassungsgerichtshofes vom 12.12.1998,  G 198/98.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Amtlicher Befund  Am 13.07.2022 langte beim Finanzamt Österreich, Dienststelle Sonderzuständigkeiten, ein  “Amtlicher Befund über eine Verkürzung von Stempel- und Rechtsgebühren“ des  Verfassungsgerichtshofes (kurz: VfGH) ein.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_55`)


soweit eine andere  Form der Einbringung für zulässig erklärt ist (§ 14a Abs. 2), ist der Zeitpunkt des Einlangens in  den elektronischen Verfügungsbereich des Verfassungsgerichtshofes maßgeblich.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_78`)


von Rechtsauslegungen des Verfassungsgerichtshofes oder des Verwaltungsgerichtshofes  abweicht, wenn im Vertrauen auf die betreffende Rechtsprechung für die Verwirklichung des  die Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_82`)


Im Hinblick darauf wird auf das Erkenntnis des  Verfassungsgerichtshofes (VfGH 04.12.2001, B 2366/00) verwiesen, wonach gegen eine  Vorschrift, die bewirkt, dass Personen, die im Ausland (Drittland) lebenden Kindern gegenüber  zu Unterhaltsleistungen verpflichtet sind, keine Familienbeihilfe gewährt wird, keine  verfassungsrechtlichen Bedenken bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_49`)


Nach Ansicht des Verfassungsgerichtshofes beeinträchtigt es weder die rechtsstaatlichen  Funktionen des Bescheides noch wird der verfassungsrechtlich gewährleistete  Rechtsschutzstandard dadurch verringert, dass ein Bescheid kraft Gesetzes eines bestimmten  genehmigenden Organwalters oder dessen Benennung bzw Unterschrift entbehrt, solange die  Zurechnung des Bescheides zu einer bestimmten Behörde dadurch nicht gefährdet wird.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_346`)


Nach der ständigen Rechtsprechung des Verfassungsgerichtshofes  verletzen zwar gesetzliche Vorschriften, die nachträglich an früher verwirklichte Tatbestände  steuerliche Folgen knüpfen und dadurch die Rechtsposition des Steuerpflichtigen mit Wirkung  für die Vergangenheit verschlechtern, im Allgemeinen den Gleichheitssatz, wenn der Eingriff  von erheblichem Gewicht ist und der Steuerpflichtige in einem berechtigten Vertrauen auf die  Rechtslage enttäuscht wurde (z.B. VfGH 19.6.1996, B2756/94).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_200`)


Nach dem grundlegenden Erkenntnis des Verfassungsgerichtshofes vom  25. September 1996, B 4016/95, zur auf § 68 Abs. 1 AVG bezogenen „res judicata“ bleibt diese  Möglichkeit jedenfalls bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_236`)


Dies bedeutet - zuerst - dass diese, in der Diktion des Verfassungsgerichtshofes,  17 von 21 Seite 18 von 21

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146646.1`) (sent_id: `deanon_BFG_20260814_TEST/146646.1_102`)


Zur Bindungswirkung  § 87 Abs. 2 VfGG   Wenn der Verfassungsgerichtshof einer Beschwerde stattgegeben hat, sind die  Verwaltungsgerichte und die Verwaltungsbehörden verpflichtet, in der betreffenden  Rechtssache mit den ihnen zu Gebote stehenden rechtlichen Mitteln unverzüglich den der  Rechtsanschauung des Verfassungsgerichtshofes entsprechenden Rechtszustand herzustellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/146646.1`) (sent_id: `deanon_BFG_20260814_TEST/146646.1_122`)


Angemerkt werden darf noch, dass die Verpflichtung des Art. 87 Abs. 2 VfGG, in der  Beschwerdesache den der Rechtsanschauung des Verfassungsgerichtshofes entsprechenden  Rechtszustand herzustellen, nicht nur für die Verwaltungsgerichte, sondern auch für die  Verwaltungsbehörden gilt. Wenn das Erkenntnis des VfGH auch zur Beschwerdesache der Bf.  betreffend Einkommensteuer 2020 ergangen ist, sah sich das BFG verpflichtet, diese  Grundsätze auch für den im Wesentlichen gleich gelagerten Sachverhalt betreffend  Einkommensteuer 2021 anzuwenden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_126`)


Mit Beschluss des BFG vom 10.01.2025 wurde der beschwerdeführenden Partei die  Rechtsprechung des Verfassungsgerichtshofes vom 11.12.2024, G 85/2024, vom 11.12.2024,  E 1757/2024, sowie die Presseinformation des Verfassungsgerichtshofes vom 09.01.2025 zur  Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_132`)


Zur Rechtsprechung des Verfassungsgerichtshofes vom 11.12.2024, E 1757/2024,  hebt die beschwerdeführende Partei, folgende Aussagen als wesentlich hervor:  1.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_144`)


Aus der Entscheidung des Verfassungsgerichtshofes vom 11.12.2024, G 85/2024 gehe hervor,  dass die meisten Anträge als unzulässig zurückgewiesen worden wären, da sie zu eng  formuliert gewesen seien.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_294`)


Gesondert wird auf die aktuelle Rechtsprechung des Verfassungsgerichtshofes verwiesen, in  der sich der Verfassungsgerichtshof mit der Verfassungskonformität des EKBSG  auseinandergesetzt hat, VfGH vom 11.12.2024, G 85/2024;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_444`)


Dem Vorbringen der beschwerdeführenden Partei, aus der zitierten Rechtsprechung des  Verfassungsgerichtshofes ergebe sich die Notwendigkeit einer Differenzierung zwischen den  Kostenstrukturen aufgrund der Verlängerung der Maßnahme, kann nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_125`)


Überdies wurde die Rechtsprechung des  Verfassungsgerichtshofes vom 11.12.2024, G 85/2024, vom 11.12.2024, E 1757/2024, sowie  die Presseinformation des Verfassungsgerichtshofes vom 09.01.2025 zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_131`)


Zur Rechtsprechung des Verfassungsgerichtshofes vom 11.12.2024, E 1757/2024,  hebt die beschwerdeführende Partei, folgende Aussagen als wesentlich hervor:  1.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_144`)


Aus der Entscheidung des Verfassungsgerichtshofes vom 11.12.2024, G 85/2024 gehe hervor,  dass die meisten Anträge als unzulässig zurückgewiesen worden wären, da sie zu eng  formuliert gewesen seien.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_293`)


Gesondert wird auf die aktuelle Rechtsprechung des Verfassungsgerichtshofes verwiesen, in  der sich der Verfassungsgerichtshof mit der Verfassungskonformität des EKBSG  auseinandergesetzt hat, VfGH vom 11.12.2024, G 85/2024;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_444`)


Dem Vorbringen der beschwerdeführenden Partei, aus der zitierten Rechtsprechung des  Verfassungsgerichtshofes ergebe sich die Notwendigkeit einer Differenzierung zwischen den  Kostenstrukturen aufgrund der Verlängerung der Maßnahme, kann nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

</details>

---

## `Police Authority` 🏆

**F1:** 0.012 | **Precision:** 1.000 | **Recall:** 0.006  

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
| 1.000 | 0.006 | 0.012 | 28 | 28 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 0 | 4571 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_60`)


Im Verwaltungsstrafakt  ist nicht ersichtlich, wann genau (sekundengenau) das Parkraumüberwachungsorgan der  Landespolizeidirektion Wien die Übertretung festgestellt haben will.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_65`)


Selbst wenn, was bestritten wird, die Transaktionsbestätigung Sekunden später geschickt  wurde als das Parkraumüberwachungsorgan der Landespolizeidirektion Wien die angebliche  Übertretung festgestellt hat, ist Folgendes zu bedenken: Der in Art 7 B-VG normierte  Gleichheitsgrundsatz verbietet eine willkürliche, unsachliche Differenzierung auf den Gebieten  der Normsetzung und des Normvollzuges.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_84`)


Würde ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien nämlich um 14.41  Uhr den Lenker antreffen ist eine Bestrafung unzulässig, wenn dieser einen konventionellen  Parkschein ab 14.45 Uhr ausgefüllt hat.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_38`)


In der am 17. Juni 2020 durchgeführten mündlichen Verhandlung vor dem  Bundesfinanzgericht wurde das Kontrollorgan der MA 67 der Landespolizeidirektion Wien als  Zeuge vernommen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_95`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige vom 06.06.2018 samt Fotos, welche  von einem Organ der Landespolizeidirektion Wien erstattet wurde, der Lenkerauskunft vom  08.11.2018, wonach das Fahrzeug Ihnen von der Zulassungsbesitzerin (VN-F NN) überlassen  war sowie Ihrer Bekanntgabe vom 30.07.2019, wonach das Fahrzeug Vera Schliephacke überlassen  war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Vera Schliephacke` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_11`)


Das Fahrzeug wurde von einem Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien  1) am 22. Oktober 2019 um 16:21 Uhr in der gebührenpflichtigen Kurzparkzone in 1200  Wien, Brigittenauer Lände 134-136, und   2) am 23. Oktober 2019 um 09:48 Uhr in der gebührenpflichtigen Kurzparkzone in 1100  Wien, LaaerBerg-Straße 16-20,  beanstandet, da es zu den genannten Zeiten ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_7`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer wurde von der belangten Behörde, unter Zugrundelegung der Anzeige  eines Kontrollorganes der Landespolizeidirektion Wien, Abteilung für Parkraumüberwachung,  mit Strafverfügung vom 12.10.2020, MA67/Zahl/2020, angelastet, er habe das Fahrzeug mit  dem behördlichen Kennzeichen 123 (A) am 12.8.2020 um 11:40 Uhr in der gebührenpflichtigen  Kurzparkzone in 1150 Wien, Zinckgasse 25, abgestellt, ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_26`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:  „Das Fahrzeug wurde von einem Organ der Landespolizeidirektion Wien um 11:40 Uhr  beanstandet, da es an der im Spruch bezeichneten Örtlichkeit und zur dort angeführten  Zeit in einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dieses mit einem  gültig entwerteten Parkschein gekennzeichnet oder einen elektronischen Parkschein  aktiviert zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_111`)


Mit dem Beschwerdevorbringen, er habe kein Ticket vor Ort erhalten (gemeint wohl: keine  Organstrafverfügung), lässt sich für diesen nichts gewinnen, da dem Organ der öffentlichen  Aufsicht ein Wahlrecht eingeräumt ist, ob es eine Anonymverfügung gemäß § 49a (im Falle  eines Organs der Verwaltungsstrafbehörde selbst) bzw. eine Organstrafverfügung gemäß § 50  VStG (im Falle eines Organes der Landespolizeidirektion Wien) oder eine Anzeige erstattet  (Lewisch/Fister/Weilguni, Verwaltungsstrafgesetz, § 50 Tz 4), durch die das  Verwaltungsstrafverfahren gemäß §§ 40 ff VStG gegen eine bestimmte Person als Lenker des  Fahrzeuges eingeleitet wird.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (Fa. ZB, Straße, 1220 Wien)  eingeholten Lenkerauskunft mit Strafverfügung vom 28. Oktober 2020, an, er habe das  Fahrzeug am 19. August 2020 in der gebührenpflichtigen Kurzparkzone in 1220 Wien,  Schüttaustraße 4-10, ohne einem für den Beanstandungszeitpunkt 14:34 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_45`)


Am 10. Mai 2019 wurden beim zuständigen Finanzamt die Vereinsstatuten und am 12.  September 2019 der Bescheid der Landespolizeidirektion Wien betreffend die Einladung zur  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_141`)


Dass sie aber auch schon davor sub-untervermietet hätte, belegte der Bf anhand einer Kopie  der ersten Seite eines Bescheides der Landespolizeidirektion Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_185`)


Dass sie aber auch schon davor sub-untervermietet hätte,  belegte der Bf anhand einer Kopie der ersten Seite eines Bescheides der Landespolizeidirektion  Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_206`)


Zum dritten ist durch die Feststellungen der Landespolizeidirektion Wien als erwiesen  anzunehmen, dass im gegenständlichen Zeitraum jedenfalls ab 14. September 2017 Glücksspiel  vom Subuntermieter angeboten wurde, der das Lokal vom Untermieter, an den der  gegenständliche Bf vermietet hatte, in Subuntermiete gemietet hatte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_58`)


Begründend stellte die Behörde nach Wiedergabe des Verwaltungsgeschehens und der vom Bf.  im Zuge des Verfahrens vorgebrachten Einwendungen fest, dass aus der Anzeige des Park- raumüberwachungsorganes der Landespolizeidirektion Wien, welche als taugliches Beweis- mittel anzusehen sei (Verweis auf das Erkenntnis des Verwaltungsgerichtshofes vom  07.09.1990, ZI. 90/18/0079), eindeutig ersichtlich sei, dass das in Rede stehende Kraftfahrzeug  am 8. Juli 2021 um 09:24 Uhr in Holzrechengasse 17, 9907 Tristach, Österreich, in einer gebührenpflichtigen Kurzparkzone  abgestellt war, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben, da der Parkschein insofern unrichtig entwertet war, als  er die Entwertungen 09:30 Uhr getragen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Holzrechengasse 17, 9907 Tristach, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_61`)


Die Angaben des anzeigelegenden Parkraumüberwachungsorganes der Landespolizeidirektion  Wien seien klar, deutlich und frei von Widersprüchen gewesen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin (ZB) des  mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenker- auskunft mit Strafverfügung vom 20. Dezember 2022 an, er habe das Fahrzeug am 3. Oktober  2022 in der gebührenpflichtigen Kurzparkzone in Grub-Mallinger-Straße 6, 4782 Bubing, Österreich  ohne einen für den  Beanstandungszeitpunkt 12:20 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Grub-Mallinger-Straße 6, 4782 Bubing, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_8`)


Entscheidungsgründe  Verfahrensgang  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (ANr) am 10.  November 2022 um 15:01 Uhr in 1220 Wien, Bodmergasse 70, zur Anzeige gebracht, da ein  gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_47`)


Eine  Nachfrage bei der Landespolizeidirektion Wien, Parkraumüberwachungsgruppe habe ergeben,  dass der Meldungsleger zur Tatzeit in Wien 22 seinen Dienst versehen habe und daher ein  Irrtum bei der Angabe des Tatdatums auszuschließen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_7`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (X. GmbH) eingeholten  Lenkerauskunft mit Strafverfügung vom 9. März 2023 an, er habe das Fahrzeug am 27.  Dezember 2022 in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Gasse, ohne einen für  den Beanstandungszeitpunkt 21:21 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_4`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit Strafverfügung  vom 29. März 2023 an, sie habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Vienna am 8. März 2023 in der gebührenpflichtigen Kurzparkzone in 1010 Wien,  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_22`)


Dazu wird Folgendes festgestellt:  Der Anzeige des Parkraumüberwachungsorgans der Landespolizeidirektion Wien, welche auf  Grund einer eigenen dienstlichen Wahrnehmung gelegt wurde und welche als taugliches  Beweismittel anzusehen ist (Erkenntnis des Verwaltungsgerichtshofes vom 7.9.1990,  ZI.90/18/0079), ist zu entnehmen, dass das Fahrzeug in einer gebührenpflichtigen Kurzparkzone  gestanden ist, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültig  2 von 9 Seite 3 von 9

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_103`)


Mit dem Beschwerdeeinwand, die Bf. habe keine Organstrafverfügung am Fahrzeug  vorgefunden, lässt sich für die Bf. nichts gewinnen, da dem Organ der öffentlichen Aufsicht ein  Wahlrecht eingeräumt ist, ob es eine Anonymverfügung gemäß § 49a VStG (im Falle eines  Organs der Verwaltungsstrafbehörde selbst) bzw. eine Organstrafverfügung gemäß § 50 VStG  (im Falle eines Organes der Landespolizeidirektion Wien) oder eine Anzeige erstattet  (Lewisch/Fister/Weilguni, Verwaltungsstrafgesetz, § 50 Tz 4), durch die das  Verwaltungsstrafverfahren gemäß §§ 40 ff.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_5`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 15. April  2024 um 14:14 Uhr in 1020 Wien, Lusthausstraße nächst Baum 2048 zur Anzeige gebracht, da  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_8`)


Entscheidungsgründe  Verfahrensgang:   Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen Kennz1 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 5.  November 2024 um 08:56 Uhr in Haussteingasse 28, 8144 Attendorfberg, Österreich, beanstandet, da ein gültiger Parkschein  fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Haussteingasse 28, 8144 Attendorfberg, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_58`)


Beweiswürdigung:  Die Abstellung des Fahrzeuges in der gebührenpflichtigen Kurzparkzone ohne gültigen  Parkschein lässt sich aus der Anzeige des Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien und den im Akt aufliegenden, zum Beanstandungszeitpunkt  aufgenommenen Fotos ersehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_62`)


Dass der Bf. zum Beanstandungszeitpunkt der Zulassungsbesitzer des in Rede stehenden  Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A) war, ergibt sich aus der Anzeige  des Kontrollorgans der Parkraumüberwachung der Landespolizeidirektion Wien (Akt S 2).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_20`)


„Aus der dem Verfahren zugrundeliegenden Organstrafverfügung samt Fotos, welche von  einem Organ der Landespolizeidirektion Wien erstattet wurde, geht hervor, dass das von Ihnen  gelenkte Kraftfahrzeug beanstandet wurde, weil es ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Federal Ministry Finance` 💣

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

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
| 1.000 | 0.003 | 0.007 | 16 | 16 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 0 | 4583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_45`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte und für die Beurtei- lung, ob die Benützung eines Massenbeförderungsmittels zumutbar oder unzumutbar ist, ist  für Verhältnisse innerhalb Österreichs nach § 3 Abs. 1 der ua. aufgrund des § 16 Abs. 1 Z 6  EStG 1988 ergangenen Pendlerverordnung, BGBl. II Nr. 276/2013 idF BGBl. II Nr. 154/2014, der  vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte Pendlerrechner zu  verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_20`)


Dieses Erkenntnis ist in Rechtskraft erwachsen (E-Mail des Prüfers vom  11.07.2019 an das Bundesministerium für Finanzen).

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_32`)


Die steuerliche Vertretung des BF beantragte daraufhin mit Schreiben vom 16.8.2018 beim  Bundesministerium für Finanzen die Einleitung eines Verständigungsverfahrens mit Malta.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_71`)


Wie bereits im angefochtenen Bescheid ausgeführt wurde, normiert § 48 BAO Folgendes:  „Das Bundesministerium für Finanzen kann bei Abgabepflichtigen, die der Abgabenhoheit  mehrerer Staaten unterliegen, soweit dies zur Ausgleichung der in- und ausländischen  Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit entsprechenden  Behandlung erforderlich ist anordnen, bestimmte Gegenstände ganz oder teilweise aus der  5 von 12 Seite 6 von 12

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_74`)


Diese dem Bundesministerium für  Finanzen erteilte Ermächtigung erweist sich auf Grund der bisherigen Erfahrungen als  unbedingt erforderlich, um insbesondere im Verhältnis zu solchen Staaten, mit denen eine  staatsvertragliche Regelung zur Vermeidung von Doppelbesteuerungen nicht besteht oder  nicht zu erwarten ist, für die in Betracht kommenden Besteuerungsfälle Abhilfe gegen  Doppelbesteuerungen zu schaffen oder eine der Gegenseitigkeit entsprechende Behandlung zu  gewährleisten.

| Predicted | Gold |
|---|---|
| `Bundesministerium für  Finanzen` | `Bundesministerium für  Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_46`)


Am 20.08.2020 wurde die im Bundesministerium für Finanzen für die automationsunterstützte  Datenverarbeitung zuständige Sektion I aufgefordert, Fragen im Zusammenhang mit den  konkreten Bescheiderstellungen zu beantworten, sowie diesbezügliche Beweismittel  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_18`)


Im Vorlageantrag wiederholte der Bf. im Wesentlichen sein Vorbringen aus der Beschwerde  und verwies ergänzend auf eine vom Bundesministerium für Finanzen herausgegebene Bro- schüre, eine in Jakom/Baldauf 2012 zu § 34 Rz 87 vertretene Rechtsmeinung und den 1. Lohn- steuer-Wartungserlass 2011.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_101`)


Auf Grund einer Vereinbarung im Bundesministerium für Finanzen im Zuge der Einführung von  FinanzOnline und der Einführung der elektronischen Umsatzsteuervoranmeldungen werden im  automatisierten Verfahren seit dem Jahr 2003 folgende Verspätungszuschläge bei Nichtabgabe  von Umsatzsteuervoranmeldungen verhängt:  Bei einer Verspätung bis zu 10 Tagen: 0 Prozent  Bei einer Verspätung von 11 bis 15 Tagen: 2 Prozent  Bei einer Verspätung von 16 bis 25 Tage: 5 Prozent  Bei einer Verspätung von mehr als 25 Tagen: 8 Prozent

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_179`)


Die Merkmale der natürlichen und wirtschaftlichen Ertragsbedingungen dieses  Hauptvergleichsbetriebes sind vom Bundesministerium für Finanzen nach Beratung im  Bewertungsbeirat durch Verordnung rechtsverbindlich festzustellen und im „Amtsblatt zur  Wiener Zeitung“ kundzumachen (§ 44).

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_182`)


Um für die Bewertung aller in der Natur tatsächlich vorkommenden landwirtschaftlichen  Betriebe innerhalb des Bundesgebietes die Gleichmäßigkeit zu sichern und Grundlagen durch  feststehende Ausgangspunkte zu schaffen, stellt das Bundesministerium für Finanzen für  bestimmte Betriebe (Vergleichsbetriebe) nach Beratung im Bewertungsbeirat mit  rechtsverbindlicher Kraft das Verhältnis fest, in dem die Vergleichsbetriebe nach ihrer  Ertragsfähigkeit auf die Flächeneinheit (Hektar) bezogen zum Hauptvergleichsbetriebe stehen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_240`)


Nach Beratung im Bewertungsbeirat trifft das Bundesministerium für Finanzen über den  Gegenstand der Beratung die Entscheidung.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_73`)


Die in ausländischer Währung gezahlten gleichartigen ausländischen Beihilfen sind nach den  vom Bundesministerium für Finanzen auf Grund des § 4 Abs. 8 des Umsatzsteuergesetzes 1972,  BGBl. Nr. 223/1972, in der "Wiener Zeitung" kundgemachten jeweiligen Durchschnittskursen in  inländische Währung umzurechnen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_22`)


Die für schriftliche Anbringen geltenden  Bestimmungen sind auch in diesen Fällen mit der Maßgabe anzuwenden, daß das Fehlen einer  Unterschrift keinen Mangel darstellt. Die Abgabenbehörde und das Verwaltungsgericht können  jedoch, wenn es die Wichtigkeit des Anbringens zweckmäßig erscheinen läßt, dem Einschreiter  die unterschriebene Bestätigung des Anbringens mit dem Hinweis auftragen, daß dieses nach  fruchtlosem Ablauf einer gleichzeitig zu bestimmenden angemessenen Frist als  zurückgenommen gilt.  Für Anbringen im Sinn des § 86a Abs. 1 erster Satz BAO, die in Abgaben-, Monopol- oder  Finanzstrafangelegenheiten an das Bundesministerium für Finanzen, an die  Verwaltungsgerichte, an ein Finanzamt, an das Zollamt Österreich oder an das Amt für  Betrugsbekämpfung gerichtet werden, wird die Einreichung unter Verwendung eines  Telekopierers (Telefaxgerätes) zugelassen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Zollamt Österreich` (organisation)
- `Amt für  Betrugsbekämpfung` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_79`)


2. in Widerspruch zu nicht offensichtlich unrichtigen Rechtsauslegungen steht, die               a) dem Abgabepflichtigen gegenüber von der für ihn zuständigen Abgabenbehörde geäußert  oder                              b) vom Bundesministerium für Finanzen im Amtsblatt der österreichischen Finanzverwaltung  oder im Internet als Amtliche Veröffentlichung in der Findok veröffentlicht wurden, wenn im  Vertrauen auf die betreffende Äußerung bzw. Veröffentlichung für die Verwirklichung des die  Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_131`)


Das Finanzamt stützt sich in seiner Argumentation im Wesentlichen darauf, dass sich die  Verpflichtung zur Abgabe einer Meldung im vorliegenden Fall aus § 6 Abs. 6 WiEReG ergebe,  und verweist in seiner Stellungnahme auf die vom Bundesministerium für Finanzen erstellten  "FAQs zum Register der wirtschaftlichen Eigentümer", hier insbesondere auf die Frage 5 samt  Beantwortung mit dem Wortlaut:  "Frage 5: Durch einen Gesellschafterwechsel ist nachträglich eine Meldebefreiung eingetreten.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_84`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

## `EU Court of Justice` 💣

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

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
| 1.000 | 0.002 | 0.005 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 4588 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_42`)


Der Gerichtshof der Europäischen Union hat am 16. Juni 2022 betreffend Indexierung der  Familienbeihilfe sowie bestimmter familienbezogener Steuerbegünstigungen auf Grund einer  Klage der Europäischen Kommission entschieden.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_48`)


Die vom Gerichtshof der Europäischen Union mit Urteil EuGH 16. 6. 2022, C-328/20 getroffene  Auslegung ist auch im gegenständlichen Beschwerdeverfahren vor dem Bundesfinanzgericht zu  beachten.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_107`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_90`)


Der Familienbonus Plus gemäß Abs 3a; der Familienbonus Plus ist insoweit nicht  abzuziehen, als er jene Steuer übersteigt, die auf das gemäß Abs 1 zu versteuernde Einkommen  entfällt.  Der Gerichtshof der Europäischen Union entschied mit Urteil EuGH 16.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_155`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf den Alleinerzieherabsetzbetrag für Arbeitnehmer, deren Kinder  ständig in einem anderen Mitgliedstaat wohnen, mit dem Unionsrecht vereinbar ist, eindeutig  beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_102`)


Das Bundesfinanzgericht legte dem Gerichtshof der Europäischen Union gemäß Artikel 267  AEUV folgende Frage zur Vorabentscheidung vor:  "Sind Artikel 18 und Artikel 45 Absatz 1 des Vertrags über die Arbeitsweise der Europäischen  Union, Artikel 7 Absätze 1 und 2 der Verordnung (EG) Nr. 492/2011 des Europäischen  Parlaments und des Rates vom 5. April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb  der Union, Artikel 4, Artikel 5 Buchstabe b, Artikel 7 und Artikel 67 der Verordnung (EG) Nr.  883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004 zur Koordinierung  der Systeme der sozialen Sicherheit sowie Artikel 60 Absatz 1 Satz 2 der Verordnung (EG) Nr.  987/2009 des Europäischen Parlaments und des Rates vom 16. September 2009 zur Festlegung  der Modalitäten für die Durchführung der Verordnung (EG) Nr. 883/2004 über die Koordi- nierung der Systeme der sozialen Sicherheit dahin auszulegen, dass sie der Anwendung einer  nationalen Regelung entgegenstehen, die vorsieht, dass Familienleistungen für ein Kind, das  sich nicht tatsächlich ständig in dem diese Familienleistungen zahlenden Mitgliedstaat, sondern  tatsächlich in einem anderen Mitgliedstaat der Europäischen Union, einer anderen Vertrags- partei des Abkommens über den Europäischen Wirtschaftsraum oder der Schweiz aufhält, auf  Basis der vom Statistischen Amt der Europäische Union veröffentlichten vergleichenden Preis- niveaus für den jeweiligen Staat im Verhältnis zu dem die Familienleistungen zahlenden  Mitgliedstaat anzupassen?"

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Europäischen  Union` (organisation)
- `Europäischen Parlaments` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_15`)


Nach Stellung des diesbezüglichen Vorabentscheidungsersuchens eines Richters des  Bundesfinanzgerichts reichte die Europäische Kommission mit Beschluss vom 14.05.2020 im  Verfahren INFR (2018) 2372 am 22.07.2020 Klage gegen die Republik Österreich beim  Gerichtshof der Europäischen Union ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_18`)


Der Gerichtshof der Europäischen Union entschied mit Urteil EuGH 16 06.2022, C-328/20,  ECLI:EU:C:2022:468, im Vertragsverletzungsverfahren (die Indexierung nach der  unterschiedlichen Kaufkraft in den einzelnen Mitgliedstaaten bzw. Vertragsstaaten wird dort  als Anpassungsmechanismus bezeichnet):   „…  1.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_23`)


04. 2020, RE/7100001/2020 an den Gerichtshof der Europäischen Union  gemäß Art. 267 AEUV gestellte Ersuchen um Vorabentscheidung, ob die Indexierung von  Familienleistungen durch den österreichischen Gesetzgeber nach der Kaufkraft in den  einzelnen Mitgliedsstaaten bzw. Vertragsstaaten unionsrechtskonform ist, protokolliert zu C- 163/20, gemäß Artikel 100 Abs. 1 Verfahrensordnung des Gerichtshofs der Europäischen Union  und § 290 Abs 3 BAO zurückgenommen.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_25`)


III. Erwägungen  Der Gerichtshof der Europäischen Union wurde mit der Sache vom Bundesfinanzgericht mittels  des Vorabentscheidungsverfahrens gemäß Beschluss BFG 16.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_128`)


Der Gerichtshof der Europäischen Union hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

| Predicted | Gold |
|---|---|
| `Gerichtshof der Europäischen Union` | `Gerichtshof der Europäischen Union` |

</details>

---

## `Complex Company Name GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

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
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 4598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` | `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` |

**Missed by this rule (FN):**

- `Lisa Lindnau` (person)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-287/7417` (tax_number)

</details>

---

## `Federal Ministry Finance Genitive` 

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

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
| 1.000 | 0.002 | 0.003 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 4592 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_87`)


Dass die angefochtenen Erledigungen vom Finanzamt  yy (und nicht vom die Außenprüfung durchführenden Finanzamt xx) genehmigt und folglich  auch erlassen wurden (siehe dazu die Ausführungen unter Punkt IV.1.3.), resultiert aus den  Ausführungen des Bundesministeriums für Finanzen, Sektion I, vom 22.09.2020 in Verbindung  mit den Angaben der belangten Behörde im Schriftsatz vom selben Tag: Demnach wurden die  verfahrensgegenständlichen Erledigungen durch einen Mitarbeiter des Finanzamtes yy – C -  endgültig freigegeben, sprich approbiert.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_152`)


Den weiteren Ausführungen zur Unzuständigkeit im Zusammenhang mit dem Befüllen der  Eingabebögen durch den Prüfer des Finanzamtes xx ist der unzweifelhafte Inhalt der  Ausführungen des Bundesministeriums für Finanzen, Sektion I und der belangten Behörde,  jeweils vom 22.09.2020, entgegenzuhalten: Sowohl der Sach-, als auch der  Wiederaufnahmebescheid wurden in concreto von einem Organ des Finanzamtes yy  freigegeben, d.h. genehmigt;

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_40`)


Die Bf besteht nach den Eintragungen im elektronischen Akteninformationsssystem des  Bundesministeriums für Finanzen zumindest seit dem Jahr 2003, weil bis zu diesem Jahr  Eintragungen zurückverfolgt werden konnten.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_316`)


Der vom Bf angeregte Antrag an den Verfassungsgerichtshof betreffend der Kundmachung des  BMF GZ. BMF-010202/0104-VI/3/2014 wegen Gesetzwidrigkeit erübrigt sich jedenfalls:   Der Verfassungsgerichtshof hat schon mit Beschluss VfGH vom 26.11.2018, E 479/2017 die  Behandlung einer Beschwerde, die gegen das Erkenntnis des BFG vom 10.1.2017,  RV/4100647/2016 eingebracht wurde, in der der Bf ua Verfassungswidrigkeit und Verletzung  des Gleichheitsgrundsatzes hinsichtlich genau dieser der Kundmachung des  Bundesministeriums für Finanzen vom 05.03.2014 (BZ. BMF-010202/0104-VI/3/2014)  behauptete, abgelehnt.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_31`)


Punkt a):  Hingewiesen wird auf die Erlässe des Bundesministeriums für Finanzen zum Thema  Selbstberechnung, dort heißt es wörtlich:  Die für die Ermittlung der Bemessungsgrundlage außerhalb des elektronischen  Selbstberechnungsverfahrens erstellten Berechnungsblätter und/oder Ausdrucke von  automatischen Berechnungshilfen sind dem Selbstberechnungsakt beizuschließen und  gemeinsam mit der über den Rechtsvorgang ausgefertigten Schrift sieben Jahre  aufzubewahren.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_70`)


Nach Auskunft des Bundesministeriums für Finanzen in gleichgelagerten Fällen ist der im  Signaturblock angegebene Tag im Allgemeinen jener Tag, an welchem der Bescheid in die  Databox eingebracht wurde, weil diese Einbringung in der Regel innerhalb einer Stunde ab  Erstellung der Amtssignatur erfolgt.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_132`)


Gemäß § 7b Abs. 3 AVRAG treffen den Arbeitgeber im Sinne des Abs. 1 diverse Meldepflichten  gegenüber der Zentralen Koordinationsstelle für die Kontrolle der illegalen Beschäftigung nach  dem Ausländerbeschäftigungsgesetz und dem AVRAG des Bundesministeriums für Finanzen,  deren Verletzung gemäß Abs. 8 mit Geldstrafen geahndet werden.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

</details>

---

## `City Magistrate` 

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

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
| 1.000 | 0.003 | 0.005 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 0 | 4587 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_3`)


Nr.  10/2013 über die Beschwerde des Beschuldigten vom 20. November 2019 gegen das  Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 6. November 2019,  Zahl: MA 67/186700510526/2018 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien` | `Magistrates der  Stadt Wien` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `Susette Volmari` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_19`)


Mit Vorhalt vom 15.12.2020 ersuchte das Bundesfinanzgericht den Bf, nachstehende Fragen zu  beantworten und die angesprochenen Unterlagen vorzulegen:  1) Vorzulegen sei nicht nur das Deckblatt, sondern der gesamte Bescheid des Magistrates der  Stadt Wien vom 06.10.2015 betreffend „Mindestsicherung, Zuerkennung“.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien` | `Magistrates der  Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Rocco Choudhury` (person)
- `Wachtelgasse 7, 9543 Stadt, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 67` | `Magistrates der  Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Diana Sammer` (person)
- `Dipl.-Ing. KzlR Otto Thiesgen` (person)
- `Gränzing 2, 4841 Brunau, Österreich` (address)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Günter Möhlenfeld  in Vertretung des verhinderten  Richters Hon.-Prof. Kaspar Frantzius  in der Verwaltungsstrafsache gegen Elias Schwabeland, Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 22. November  2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  15. November 2021, GZ. MA67/Zahl/2021, nach Durchführung einer mündlichen Verhandlung  am 19. Dezember 2022, in Anwesenheit des Beschuldigten und der Schriftführerin IP, jedoch in  entschuldigter Abwesenheit einer Vertreterin/eines Vertreters der belangten Behörde, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat die beschwerdeführende Partei keinen Beitrag zu den Kosten  des Beschwerdeverfahrens zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Hon.-Prof. Günter Möhlenfeld` (person)
- `Hon.-Prof. Kaspar Frantzius` (person)
- `Elias Schwabeland` (person)
- `Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Katharina Bauckholt, Zirknitzberg 11, 3392 Lerchfeld, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 19. Dezember 2022, Zahl: MA67/226701238674/2022, mit dem der Einspruch  vom 1. Dezember 2022 gegen die Strafverfügung vom 10. November 2022 mit derselben  Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien` | `Magistrates der  Stadt Wien` |

**Missed by this rule (FN):**

- `Dr. Barbara Straka` (person)
- `Katharina Bauckholt` (person)
- `Zirknitzberg 11, 3392 Lerchfeld, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad über die Beschwerde des  Arthur Soyal, Josef-Prangl-Straße 16, 8342 Perlsdorf, Österreich, vom 23. Jänner 2024 gegen das Straferkenntnis des Magistrates  der Stadt Wien vom 27. Dezember 2023, Geschäftszahl MA67/111111/2023, betreffend  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung, ABl der Stadt  Wien 2005/51 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBI für Wien  2006/9 in der Fassung LGBl für Wien 2012/24, nach Durchführung einer mündlichen  Verhandlung am 21. Mai 2024, im Beisein des Schriftführers AD Rudolf Keinberger, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs  1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien` | `Magistrates  der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Gerhard Konrad` (person)
- `Arthur Soyal` (person)
- `Josef-Prangl-Straße 16, 8342 Perlsdorf, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Jeanne Pavlovitsch, Döbinggasse 9, 4153 Kirchbach, Österreich, vom 5. August 2024, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 31. Juli 2024, GZ. MA67/GZ/2024, mit  dem der Einspruch vom 12. Juni 2024 gegen die Strafverfügung vom 4. Juni 2024, mit  derselben Geschäftszahl, gemäß § 13 Abs. 3 AVG iVm § 24 VStG 1991 zurückgewiesen wurde,  zu Recht:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird der oben genannte, angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | `Magistrates der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Dieter Fröhlich` (person)
- `Jeanne Pavlovitsch` (person)
- `Döbinggasse 9, 4153 Kirchbach, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/148797.1`) (sent_id: `deanon_BFG_20260814_TEST/148797.1_11`)


Mit Beschluss vom 4. Februar 2025, GZ. RV/GZ2/2025, hat das Bundesfinanzgericht die  Beschwerde des Antragstellers vom 13. Jänner 2025 gegen das Straferkenntnis des Magistrates  der Stadt Wien vom 4. Dezember 2024, GZ. MA67/GZ1/2024, gemäß §§ 28 Abs. 1 und 31  VwGVG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrates  der Stadt Wien` | `Magistrates  der Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Angelika Nottebusch, Zickenberg 63, 2134 Ernsdorf bei Staatz, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018 über die Beschwerde des  Beschuldigten vom 18. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 3. September 2025, Zahl: MA67/MA-GZ/2025 zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit Folge gegeben, als die  Geldstrafe von € 175,00 auf € 40,00 und die für den Fall der Uneinbringlichkeit festgesetzte  Ersatzfreiheitsstrafe von 1 Tag und 17 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien, Magistratsabteilung 67` | `Magistrates der Stadt  Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Karoline Windsteig` (person)
- `Angelika Nottebusch` (person)
- `Zickenberg 63, 2134 Ernsdorf bei Staatz, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Hon.-Prof. Jeremias Leibolt, Ebnerwiese 46, 5211 Frauscherberg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 24. Oktober 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 16. Oktober 2025, Zahl: MA67/MA-GZ/2025 zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien, Magistratsabteilung 67` | `Magistrates der Stadt  Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Mag. Robert Pernegger` (person)
- `Hon.-Prof. Jeremias Leibolt` (person)
- `Ebnerwiese 46, 5211 Frauscherberg, Österreich` (address)

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
| `organisation` | 2 | 0 | 4597 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_71`)


Informationen, u.a. über  Verkaufsstellen für Parkscheine (Trafiken, Tankstellen, Zigarettenautomaten, Postfilialen,  Vorverkaufsstellen der Wiener Linien, Fahrscheinautomaten der Wiener Linien in allen Wiener  5 von 11 Seite 6 von 11

| Predicted | Gold |
|---|---|
| `Wiener Linien` | `Wiener Linien` |
| `Wiener Linien` | `Wiener Linien` |

</details>

---

## `Magistrats der Stadt Wien` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

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
| 1.000 | 0.005 | 0.009 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 4578 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_36`)


Die von mir in der Vernehmung vom 17.01.2020 im Magistrat der  Stadt Wien in … angeführten Angaben wurden keinesfalls ernst genommen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Heidemarie Lueckemeyer  in der Verwaltungsstrafsache gegen  Amber Demirdöven, Wiedneralm 4, 4906 Feichtet, Österreich, 1.) über die Beschwerde vom 07.09.2020 gegen das Straferkennt- nis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639161/2020, und 2.) über die Beschwerde vom 07.09.2020 gegen das Strafer- kenntnis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639163/2020, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der Stadt  Wien vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, als unbegründet abgewie- sen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |
| `Magistrats der Stadt  Wien` | `Magistrats der Stadt  Wien` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Heidemarie Lueckemeyer` (person)
- `Amber Demirdöven` (person)
- `Wiedneralm 4, 4906 Feichtet, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_7`)


II. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der  Stadt Wien vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, als unbegründet abge- wiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_16`)


Da der Zulassungsbesitzer angab, seine Ehegattin habe sein Fahrzeug am 11.03.2020 um  10:54 Uhr und am 09.03.2020 um 13:31 Uhr ohne Parkschein in einer gebührenpflichtigen  Kurzparkzone abgestellt und da die Ehegattin die an sie adressierten und für diese Tattage und  Tatzeiten erlassenen Strafverfügungen fristgerecht angefochten hatte, erließ der Magistrat der  Stadt Wien am 24.08.2020 erstens ein an die Ehegattin adressiertes Straferkenntnis zur Ge- schäftszahl MA67/206700639161/2020 und zweitens ein an die Ehegattin adressiertes Strafer- kenntnis zur Geschäftszahl MA67/206700639163/2020.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_18`)


Im elektronisch vorgelegten Akt befinden sich Ablichtungen von (Schulbesuchs-)Bestätigungen  und Zeugnissen sowie die erste Seite eines Bescheides des Magistrats der Stadt Wien für den  streitgegenständlichen Zeitraum.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_66`)


Dem Bf wurde laut Bescheid des Magistrats der Stadt Wien vom 06.10.2015, Betreff:  „Mindestsicherung, Zuerkennung“ eine Leistung zur Deckung des Lebensunterhalts und der  Grundbetrag zur Deckung des Wohnbedarfs ab November 2015 bis jedenfalls August 2016  zuerkannt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_49`)


Zwischenzeitig ist – da eine Verlängerung der Frist aufgrund von COVID-19-Maßnahmen  gesetzlich nicht (mehr) möglich ist – die im § 43 Abs. 1 VwGVG normierte Frist nach dem  6. Februar 2021 bereits abgelaufen, sodass das angefochtene Straferkenntnis des Magistrats  der Stadt Wien von Gesetzes wegen außer Kraft getreten und das Strafverfahren einzustellen  ist (vgl. VwGH 26.8.2014, Ro 2014/02/0106).

| Predicted | Gold |
|---|---|
| `Magistrats  der Stadt Wien` | `Magistrats  der Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_5`)


Informativ wird mitgeteilt, dass der Beitrag zu den Kosten des behördlichen Verfahrens  (€ 10,00) zusammen mit der Geldstrafe (€ 36,00), insgesamt somit € 46,00, an den Magistrat  der Stadt Wien zu entrichten sind, wofür weitere Informationen am Ende dieser Entscheidung  des BFG und am Ende des angefochtenen Straferkenntnisses des Magistrates zu finden sind.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_26`)


Die Beiträge zu den  Kosten des Beschwerdeverfahrens (6x € 12,00) sind zusammen mit den Geldstrafen (6x € 60,00)  und den Beiträgen zu den Kosten des behördlichen Verfahrens (6x € 10,00) an den Magistrat  der Stadt Wien zu entrichten, der zu entrichtende Gesamtbetrag beträgt 6x € 82,00.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) stellte mit Schreiben vom 27.12.2017, eingelangt beim Magistrat  der Stadt Wien am 2.1.2018, den Antrag, die Vergnügungssteuer für den Zeitraum vom  1.1.2012 bis 31.12.2015 bescheidmäßig festzusetzen, da die Bf die Rechtsansicht vertrete, dass  es aufgrund der Kollision der Rechtsnormen Glücksspielgesetz und dem Gesetz über die  Besteuerung von Vergnügen im Gebiet der Stadt Wien (Vergnügungssteuergesetz 2005) zu  einer Doppelbesteuerung komme.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 €) sind gemeinsam mit der Geldstrafe  (60,00 €) und dem Beitrag zu den Kosten der belangten Behörde (10,00 €), insgesamt  82,00 €, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_5`)


Die Kosten der Beschwerdeverfahren (je 12,00 €) sind gemeinsam mit den Geldstrafen (je  60,00 €) und den Beiträgen zu den Kosten der belangten Behörde (je 10,00 €), insgesamt  328,00 €, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_6`)


Informativ wird mitgeteilt, dass der Beitrag zu den Kosten des behördlichen Verfahrens  (10,00 Euro) zusammen mit der Geldstrafe (60,00 Euro) und dem Beitrag zu den Kosten des  Beschwerdeverfahrens (12,00 Euro), insgesamt somit 82,00 Euro, an den Magistrat der Stadt  Wien zu entrichten sind, wofür weitere Informationen am Ende dieser Entscheidung des BFG  und am Ende des angefochtenen Straferkenntnisses des Magistrates zu finden sind.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_103`)


Dazu ist zunächst festzustellen, dass der Bf mit rechtskräftigem Straferkenntnis  des Magistrats der Stadt Wien vom 7.11.2022, MA67/12345/2022, bereits anlässlich eines  Abstellvorgangs vom 29.4.2022 wegen einer durch Verwendung des gegenständlichen  Behindertenausweises bewirkten Verkürzung der Parkometerabgabe bestraft worden ist.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_3`)


Die Kosten des Beschwerdeverfahrens (15,00 Euro) sind gemeinsam mit der Geldstrafe  (75,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  100,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_3`)


Die Kosten des Beschwerdeverfahrens (15,00 Euro) sind gemeinsam mit der Geldstrafe  (75,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  100,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

</details>

---

## `Landespolizeidirektion Generic` 

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

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
| 1.000 | 0.003 | 0.007 | 16 | 16 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 0 | 4583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_8`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien unter Zugrundelegung der  Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der Landespolizeidirektion  Wien mit Strafverfügung vom 24. Dezember 2019 angelastet, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. Oktober 2019 um 09:38 Uhr  in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Dresdner Straße 89, abgestellt, ohne  für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein  gesorgt zu haben, da der Parkschein unrichtig entwertet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_37`)


Es besteht für die erkennende Behörde keinerlei Veranlassung, die schlüssigen und  widerspruchsfreien Angaben des meldungslegenden Organs der Landespolizeidirektion  Wien in Zweifel zu ziehen, zumal einem derartigen Organ die Wahrnehmung und  richtige Wiedergabe maßgeblicher Sachverhalte, insbesondere bezüglich eines im  ruhenden Verkehr befindlichen Kraftfahrzeuges, wohl zugemutet werden kann.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_38`)


Es  besteht kein Grund, an der Objektivität des meldungslegenden Organs der  Landespolizeidirektion Wien zu zweifeln und ergibt sich kein Anhaltspunkt, dass dieses  eine ihm unbekannte Person wahrheitswidrig belasten wollte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_15`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer dienstlichen  Wahrnehmung gelegt wurde, in die, von diesem angefertigten Fotos sowie in die  vorangegangenen Verfahren zu GZ MA67/Zahl2/2020 und MA67/Zahl3/2020.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_10`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 1. Oktober  2020 um 13:20 Uhr in der gebührenpflichtigen Kurzparkzone in 1030 Wien, Kardinal-Nagl-Platz  10-11, beanstandet, da es ohne einem für den Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 9. Dezember 2020, an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 9. Oktober 2020  in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Stubenbrücke nächst Parkring, ohne  einen für den Beanstandungszeitpunkt 15:33 Uhr gültigen Parkschein abgestellt und demnach  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_5`)


Begründung  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Autonummer (A) wurde am  16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Abstellort, von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion  Wien zur Anzeige gebracht, da zum Beanstandungszeitpunkt ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_15`)


Beweis wurde erhoben durch Einsichtnahme in das Organmandat vom 6.10.2021, welches von  einem Organ der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung  gelegt wurde, sowie in die von Ihnen vorgelegten ‚Handy-Parken‘ Auszüge und die m-parking  Dateien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_207`)


Es besteht kein Anlass  an diesen Feststellungen der Landespolizeidirektion Wien zu zweifeln.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_15`)


Das Straferkenntnis wurde folgendermaßen begründet:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung samt  Fotodokumentation, welche von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  geht hervor, dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug im  gebührenpflichtigen Kurzparkzonenbereich abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_10`)


Entscheidungsgründe  Verfahrensgang  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 15. Februar  2022 in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Aignerstraße 6, beanstandet, da  zur Beanstandungszeit 18:48 Uhr ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_11`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von  Kontrollorganen der Parkraumüberwachung der Landespolizeidirektion Wien in der  gebührenpflichtigen Kurzparkzone in 1120 Wien, Strohberggasse 34 u. 34a, am 12. Juli 2022,  16:08 Uhr, 13. Juli 2022, 14:04 Uhr, 14. Juli 2022, 09:05 Uhr und am 19. Juli 2022, 10:20 Uhr,  zur Anzeige gebracht, da kein gültiger Parknachweis vorlag.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 7. Oktober 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 10. August 2022 in  der gebührenpflichtigen Kurzparkzone in 1180 Wien, Edmund-Weiß-Gasse nächst ONr. 21,  ohne einen für den Beanstandungszeitpunkt 17:14 Uhr gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 2. Mai 2022 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 1. März 2022 in der  gebührenpflichtigen Kurzparkzone in 1080 Wien, Lerchenfelder Straße 30, ohne einen für den  Beanstandungszeitpunkt 12:32 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_14`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige,  welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund  einer eigenen dienstlichen Wahrnehmung gelegt wurde sowie in drei anlässlich der  Beanstandung angefertigte Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_12`)


In der Begründung wurde dargelegt, dass Beweis genommen wurde durch Einsichtnahme in  die Organstrafverfügung, welche von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien auf Grund einer eigenen dienstlichen Wahrnehmung gelegt  worden sei, sowie in die von diesem angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Tax Authority Generic` 💣

**F1:** 0.731 | **Precision:** 0.921 | **Recall:** 0.606  

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
| 0.921 | 0.606 | 0.731 | 3025 | 2785 | 240 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2785 | 240 | 1814 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_3`)


Entscheidungsgründe Mit Erkenntnis des Spruchsenates vom 5.12.2018, SpS *****, wurde das gegen den Beschuldigten N.N. geführte Finanzstrafverfahren, in dem ihm zur Last gelegt wurde, er habe im Amtsbereich des Finanzamtes Wien 4/5/10 vorsätzlich a) unter Verletzung einer abgabenrechtlichen Offenlegungs- und Wahrheitspﬂicht - nämlich durch Abgabe unrichtiger Einkommensteuererklärungen für die Jahre 2012 bis 2015 - bewirkt, dass bescheidmäßig festzusetzende Abgaben in folgender Höhe zu niedrig festgesetzt worden seien, und zwar ESt 2012 in der Höhe von € 76.952,83 ESt 2013 in der Höhe von € 21.355,87 insgesamt somit € 98.308,69 und hiedurch das Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 FinStrG begangen, sowie b) Lohnabgaben für die Zeiträume 2012 bis 2017 L, DB, DZ 1-12/2012 in der Höhe von € 17.472,98 Seite 2 von 21 L, DB, DZ 1-12/2013 in der Höhe von € 10.249,92 L, DB, DZ 1-12/2014 in der Höhe von € 447,44 L, DB, DZ 1-12/2015 in der Höhe von € 1.031,92 DB, DZ 1-12/2016 in der Höhe von € 332,81 L, DB, DZ 1-12/2017 in der Höhe von € 2.513,45 insgesamt somit € 32.048,51 nicht spätestens fünften Tag nach Fälligkeit entrichtet (abgeführt) und hiedurch die Finanzordnungswidrigkeit nach § 49 Abs. 1 lit a FinStrG begangen, gemäß § 136 FinStrG eingestellt. Zur Begründung wurde ausgeführt der Beschuldigte sei 1960 geboren, arbeite derzeit als Angestellter und verdiene monatlich € 1.500,00 netto.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 4/5/10` | `Finanzamtes Wien 4/5/10` |

**Missed by this rule (FN):**

- `N.N.` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_58`)


Die Abfuhrdifferenzen ergeben sich auf Grund der dem Prüfer vorgelegten Lohnkonten zu den bisher dem Finanzamt gemeldeten Lohnabgaben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_76`)


Die von mir sohin gewählte und geübte Vorgangsweise mag (für das Finanzamt) möglicherweise befremdlich und unüblich erscheinen, allerdings habe ich mir diese so zur Gewohnheit gemacht und liegt dies sicher auch in meiner Mentalität begründet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_92`)


Dieser vom Finanzamt gegen mich erhobene Vorwurf bricht sohin schon dadurch Seite 9 von 21 in sich zusammen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_101`)


Wenn mir das Finanzamt letztlich vorwirft, dass die Furtder Technologien GmbH über eine UID-Nummer lediglich bis 9. Oktober 2012 und die NEP Lebensmittel GmbH über eine solche lediglich bis 30. August 2013 verfügt hatte und ich auch „nachher" noch Geschäfte mit diesen Unternehmen getätigt hätte, so ist dem zu entgegnen, dass einerseits nach ständiger Judikatur der anzulegende Sorgfaltsmaßstab nicht überspannt werden kann und darf und insbesondere andererseits Beauftragungen meiner Subunternehmer teilweise (sohin jeweils die letzten Aufträge) zu Zeitpunkten erfolgten, zu denen diese noch über die UlD-Nummer verfügt hatten, die Leistungserbringung aber (auch) in einen Zeitraum danach fiel und deren Rechnungen naturgemäß auch erst danach gelegt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Furtder Technologien GmbH` (organisation)
- `NEP Lebensmittel GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_103`)


Auftrag einen Leistungszeitraum auch noch nach dem 09. Oktober 2012 (bezeichnenderweise das Finanzamt Adresse3), bei der NEP Lebensmittel GmbH wurden nur 6 Rechnungen nach dem 30. August 2013 gelegt, drei davon noch im September 2013 (sohin innerhalb eines Monates), drei bis Mitte Oktober 2013 (sohin innerhalb von 6 Wochen).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `NEP Lebensmittel GmbH` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_130`)


Auf den Vorhalt, im Rahmen der GPLA-Prüfungen vom 2.11.2017 für den Zeitraum 1.1.2012 bis 31.12.2014 und vom 14.12.2017 für den Zeitraum 1.1.2015 bis 9.11.2017 seien für das gegenständliche Verfahren relevante Abfuhrdifferenzen an lohnabhängigen Abgaben in Höhe von insgesamt € 5.821,93 festgestellt worden, wobei es sich dabei um auf den Lohnkonten selbst berechnete Beträge, die von ihm  nicht ans Finanzamt abgeführt wurden, handelte, führte der Beschuldigte in der mündlichen Verhandlung vor dem Bundesfinanzgericht aus: Die Abfuhrdifferenzen könne er sich überhaupt nicht erklären, die Lohnverrechnung sei durch den Steuerberater durchgeführt worden und alle Erlagscheine, die ihm von diesem übermittelt worden seien, habe er auch an das Seite 12 von 21 Finanzamt bezahlt. Er habe in diesem Zeitraum keine finanziellen Probleme gehabt und sei seinen Zahlungspflichten regelmäßig nachkommen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_164`)


Die sich im Rechenwerk des Abgabepflichtigen befindlichen Rechnungen der in der Tz. 4 angeführten Subunternehmen sind mit sehr hoher Wahrscheinlichkeit "Deckungsrechnungen", die lediglich einerseits dazu dienten, die "schwarz" ausbezahlten Löhne in der Buchhaltung unterzubringen und andererseits den beim Finanzamt erklärten Gewinn zu "optimieren".

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_217`)


Selbst in dem zugrunde liegenden Bericht über die Außenprüfung wird davon gesprochen, dass mit sehr hoher Wahrscheinlichkeit "Deckungsrechnungen" vorliegen würden, die lediglich einerseits dazu dienten, die "schwarz" ausbezahlten Löhne in der Buchhaltung unterzubringen und andererseits den beim Finanzamt erklärten Gewinn zu "optimieren".

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_225`)


Keine Anhaltspunkt bieten die Aktenlage und die Ermittlungsergebnisse dafür, dass der Bf. geringere Beträge an Lohnabgaben, als von seinem Steuerberater berechnet, an das Finanzamt gemeldet du somit auch (bei jeweils vorhandenen Guthaben zu den Fälligkeitstagen) entrichtet hätte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_1`)


Die Beteiligten sind: H. F., D., Finanzamt****** StNr.: xx H. P., G., Finanzamt****** StNr.: xxx Die Einkünfte aus Vermietung und Verpachtung werden festgestellt: Jahr 2005 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2006 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2007 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2008 14.194,28 Aufteilung:   F.H. 7.097,14 P.H. 7.097,14 Seite 2 von 23 Jahr 2009 18.805,88 Aufteilung:   F.H. 9.402,94 P.H. 9.402,94 Jahr 2010 36.517,94 Aufteilung:   F.H. 16.258,97 P.H. 16.258,97 Jahr 2011 - 8.737,98 Aufteilung:   F.H. - 4.368,99 P.H. - 4.368,99 Gemäß § 101 Abs. 3 BAO sind schriftliche Ausfertigungen, die in einem Feststellungsverfahren an eine Personenvereinigung (Personengemeinschaft) ohne eigene Rechtspersönlichkeit gerichtet sind (§ 191 Abs. 1 lit. a und c BAO), einer nach § 81 BAO vertretungsbefugten Person zuzustellen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_10`)


Das Finanzamt richtete am 8. Juni 2011 folgendes Ergänzungsersuchen an die Bf.: Seite 3 von 23 "Die Personengesellschaft wurde mit 2008 steuerlich erfasst wegen der Vermietung des Objektes in Stadt*****, Ru. 11.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_26`)


Im Zuge einer Nachschau gem. § 144 BAO (am 03.05.2013) kürzte das Finanzamt den Gebäudewert nach einer Berechnung mittels Ertragswertverfahren auf 422.441 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_34`)


Bisherige AfA 20.244,60, AfA nach Nachschau 6.336,62, Differenz: 13.907,99 Das Finanzamt folgte den Ausführungen des Prüfers und erließ am 23.05.2013 neue Bescheide über die Feststellung von Einkünften gem. § 188 BAO für die Jahre 2005 - 2011 und berücksichtigte die AfA in Höhe von € 6.336,62 statt wie bisher von € 20.244,40 mit folgender Begründung: "1) Bewertung Liegenschaft Ru. 10 Als Bemessungsgrundlage für die Liegenschaft wurde ein Gutachten für Versicherungszwecke herangezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_77`)


Das Finanzamt gab mit Beschwerdevorentscheidung nur dem Begehren hinsichtlich eines jährlichen AfA-Satzes von 2% statt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_78`)


Weiters wies das Finanzamt die Beschwerde mit folgender Begründung ab: "Als AfA-Bemessungsgrundlage bei unentgeltlichem Erwerb sind bei Gebäuden, die vor dem 1.8.2008 übertragen wurden, die fiktiven Anschaffungskosten maßgebend.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_167`)


Das Finanzamt gab zum vorgelegten Gutachten im Vorlagebericht folgende Stellungnahme ab: "Zum vorgelegten Gutachten vom 28.10.2014 ist auszuführen, dass Instandhaltungskosten Kosten sind, die durch Hintanhaltung oder Beseitigung von baulichen Schäden aus Abnutzung, Ablagerung und Witterungseinflüssen entstehen (Kranewitter, Liegenschaftsbewertung 6 , 2010, 90).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_196`)


Über die Beschwerde wurde erwogen: Sachverhalt: Folgender Sachverhalt, der der Entscheidung zugrunde zu legen ist, ergibt sich aus den im Akt aufliegenden Unterlagen, den vom steuerlichen Vertreter vorgelegten 3 Gutachten, den Feststellungen des Finanzamtes und den Beschwerdeausführungen: Die Beschwerdeführerin (Bf.), die Personengesellschaft H. P. und F., vermietete das Grundstück in Stadt, Ru. 11, ab 2005 an die H.-GmbH. Laut Schreiben vom 5. August 2011 betrug die Miete monatlich 2.500 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_200`)


Im Zuge einer Nachschau gem. § 144 BAO (am 03.05.2013) kürzte das Finanzamt den Liegenschaftswert nach einer Berechnung mittels Ertragswertverfahren auf 422.441 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_214`)


In der BVE hielt das Finanzamt fest, dass betreffend die Höhe der AfA die Bausubstanz zu berücksichtigen ist und kam in der Berechnung des Ertragswertes und der AfA unter Zugrundelegung der Monatsmiete von € 3.000,-, einer Verzinsung von 4,5% und einer Restnutzungsdauer von 30 Jahre, somit Vervielfältiger von 16,29, zu einem Verkehrswert der Liegenschaft in Höhe von € 410.769,78 abzüglich 20% Grund und Boden auf € 328.615,82.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_215`)


Als AfA-Prozentsatz anerkannte das Finanzamt die von der Bf. angeführten 2%, somit eine AfA in Höhe von 6.572,32 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_289`)


betreffend die Bausubstanz wurde auf das Vorgutachten und der Nachschau des Finanzamtes verwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_291`)


Seite 21 von 23 Das Finanzamt hat bereits in der Beschwerdevorentscheidung dazu Stellung genommen und ausgeführt, dass im Gutachten vom Juni 2013 keine Feststellungen zur Qualität der Bauausführungen oder allenfalls bereits bestehender Schäden, etwa als Folge aufsteigender Feuchtigkeit angeführt sind, und damit eine kürzere Nutzungsdauer bedingen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Alexander Schnelldorfer` (person)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_1`)


Entscheidungsgründe Mit Erkenntnis des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016 wurde der nunmehrige Beschwerdeführer N.N. (in der Folge kurz Bf. genannt) der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG für schuldig erkannt, er habe fahrlässig unter Verletzung der ihm gemäß § 10 Grunderwerbsteuergesetz obliegenden Anzeige-, Offenlegungs- und Wahrheitspflicht, indem er es als anzeigepﬂichtiger Erwerber unterlassen habe, den Kaufvertrag mit A.B. vom 07.01.2013 betreffend die Liegenschaft EZ Berg-Bildung KG  Ortsname bis zum 15.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Gebühren` | `Finanzamtes für Gebühren` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `A.B.` (person)
- `Berg-Bildung KG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_6`)


Dieser Erwerbsvorgang gem. § 1 GrEStG wäre bis zum 15. des zweitfolgenden Monats beim Finanzamt mit Abgabenerklärung und Kopie des Kaufvertrages anzuzeigen gewesen (§ 10 GrEStG).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_8`)


Der Erwerbsvorgang sei innerhalb der gesetzlichen Frist nicht beim Finanzamt angezeigt worden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_13`)


Ein solcher Rechtsvorgang sei gemäß § 10 Abs. 1 GrEStG bis zum 15. des dem Entstehen der Steuerschuld zweitfolgenden Monats dem zur Erhebung der Grunderwerbsteuer zuständigen Finanzamt mittels Abgabenerklärung anzuzeigen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_23`)


Seite 3 von 6 Bei Einhaltung der ihm als Käufer obliegenden Sorgfaltspflicht wäre es geboten und zumutbar gewesen, sich beim Finanzamt oder einem fachkundigen Parteienvertreter über die abgabenrechtlichen Konsequenzen der Kaufabrede in Kenntnis zu setzen und entsprechend dieser Kenntnis zu handeln.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_41`)


Aus den oben angeführten Gründen werde der höfliche Antrag gestellt, nach Abhaltung einer mündlichen Verhandlung der Beschwerde Folge zu geben, das Erkenntnis des Finanzamtes für Gebühren, Verkehrssteuern und Glücksspiel vom 05.12.2016 ersatzlos aufzuheben und das wider den Einschreiter geführte Finanzstrafverfahren einzustellen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Gebühren` | `Finanzamtes für Gebühren` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_8`)


Mit Ergänzungsersuchen vom 11.07.2017 forderte das Finanzamt die Bf auf, eine Kopie der  Originalrechnung des Steinmetzbetriebes und eine der Verlassenschaftsabhandlung (Beschluss  vom Gericht), in der das Aktivvermögen angeführt ist, nachzureichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_42`)


Tag  (Fälligkeitstag) des auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden  Kalendermonates eine Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen  Finanzamt einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  (Vorauszahlung) oder den auf den Voranmeldungszeitraum entfallenden Überschuß unter  entsprechender Anwendung des § 20 Abs. 1 und 2 und des § 16 selbst zu berechnen hat.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_4`)


Das Finanzamt X (FA) verneint die Anwendbarkeit, weil der Betrieb des Bf im  Verfahrenszeitraum der Bestimmung des § 111 Abs. 2 GewO 1994 zuzuordnen gewesen und  damit nicht ganzjährig einer Verpflichtung zur Innehabung einer Gewerberechtigung  unterlegen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Gebühren` | `Finanzamtes für Gebühren` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Ophelia Dutschka` (person)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_4`)


Der Beschwerdeführer machte im Rahmen der Arbeitnehmerveranlagung 2017 nachstehende  Werbungskosten geltend:  Fachliteratur 419,16 €  Fortbildungs-, Ausbildungs- und Umschulungskosten 5.364,12 €  Werbungskosten gesamt 5.783,28 €  Bei der Veranlagung anerkannte das Finanzamt lediglich den Pauschbetrag für  Werbungskosten in Höhe von 132 €; (Bescheid vom 22.1.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_8`)


Mit Beschwerdevorentscheidung vom 11.7.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_38`)


Die Frage des Finanzamtes in seinem Vorhalt vom 22.10.2018 „Wollen Sie die erworbenen  Kenntnisse als selbständig Tätiger verwerten?“ hat der Beschwerdeführer folgendermaßen  beantwortet:  „Ich stelle Überlegungen an, die mit der laufenden Aus- bzw. Weiterbildung erworbenen  Kenntnisse auch als selbständig Tätiger zu verwerten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Graz-Stadt` | `Finanzamtes  Graz-Stadt` |

**Missed by this rule (FN):**

- `Priv.-Doz. Dr. Kurt Bartold` (person)
- `Gruenleitner Event` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_15`)


Dagegen sei weder Berufung erhoben, noch seien seitens des Finanzamtes weitere  nach außen erkennbare (verjährungsverlängernde) Amtshandlungen gesetzt worden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_35`)


Da die als verfassungswidrig erkannte Befristung für den hier zu beurteilenden Beschwerdefall  keine Wirkung (mehr) zu entfalten vermag, war der Beschwerde gegen den  Zurückweisungsbescheid des Finanzamtes vom 2.3.2018 auf Grund der oa. VfGH- bzw. VwGH- Erkenntnisse stattzugeben und der Zurückweisungsbescheid aufzuheben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Siegfried Basyurt` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_24`)


Im Akt erliegen zwei Internet-Abfragen des Finanzamtes (EurotaxGlass-Fahrzeugbewertung;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_26`)


Mit Bescheid vom 9.11.2010, StrNr, hat das Finanzamt der Bf für das Fahrzeug Range Rover  Sport 3.0 TDV6 HSE mit der Fahrgestellnummer X1:  a) ausgehend von der Bemessungsgrundlage € 57.090,64 die Normverbrauchsabgabe (NoVA)  im Ausmaß von 14 % unter Berücksichtigung von Malus (§ 6a NoVAG) und Abgabenerhöhung  (§ 6 Abs. 6 NoVAG) im Betrag von€

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_54`)


Das Finanzamt hat in der Folge, ohne eine Berufungsvorentscheidung zu erlassen, die Berufung  samt Verwaltungsakt dem Unabhängigen Finanzsenat zur Entscheidung vorgelegt und die  Abweisung der Berufung beantragt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_58`)


Es ist daher dem Finanzamt zu erläutern und nachzuweisen,  inwieweit die Frau falsche Angaben gemacht haben soll (bezüglich Familienwohnsitz,  Angestelltenverhältnis, Verwendung des PKWs etc.).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_60`)


…"  b) Mail-Schreiben des C vom 26.8.2010, mit dem in der Beilage der Leasingvertrag zum PKW  dem Finanzamt übermittelt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Basyurt` (person)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_73`)


Im Zeitpunkt der Unterfertigung der Niederschrift vor dem Finanzamt durch die Bf (= am  27.7.2010) habe der Tachostand des Fahrzeuges ca. 25.000 km betragen, der aufgrund der  Fahrten des Gatten D-A1-D zustande gekommen wäre;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Graz-Stadt` | `Finanzamtes Graz-Stadt` |

**Missed by this rule (FN):**

- `Dr. Mehmet Gessl` (person)
- `Donau-Elektro` (organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich` (address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_165`)


Die Beschwerde richtet sich primär dagegen, dass die Umsätze für die Sexdienstleistungen vom  Finanzamt der Bf. zugerechnet werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_214`)


Die Prostitutionserlöse waren daher vom Finanzamt zu Recht der Bf. zuzurechnen, da sie zum  Betrieb eines Bordells (mit den entsprechenden Auflagen) berechtigt war und sie in  einschlägigen Medien einerseits Werbung für „ihre Girls“ geschalten sowie andererseits –  mehrsprachig - Prostituierte für ihre Bar angeworben hat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_3`)


Entscheidungsgründe  Mit Bescheiden vom 6. Mai 2019 verfügte das Finanzamt die Pfändung und Überweisung einer  Geldforderung der Beschwerdeführerin an die X-Bank zur Hereinbringung der in Höhe von  € 7.870,70 (Abgabenschuldigkeiten in Höhe von € 7.786,22 zuzüglich Gebühren und  Barauslagen für diese Pfändung in Höhe von 84,48).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_4`)


Mit einem weiteren Bescheid vom 6. Mai 2019 setzte das Finanzamt gegenüber der Bf. für  diese Amtshandlung Pfändungsgebühren in Höhe von € 77,86 und Auslagenersätze in Höhe  von € 6,62 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_15`)


Mit Beschwerdevorentscheidungen von 22. Mai 2019 wies das Finanzamt die Beschwerden als  unbegründet ab und führte aus:  a) BVE zur Beschwerde gegen den Pfändungsbescheid  Die Pfändung einer Geldforderung sei gemäß § 65 AbgEO zu Recht erfolgt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_21`)


Informativ werde mitgeteilt, dass der Abzug von monatlich € 30,00 von der Pension nicht für  das Finanzamt erfolge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_31`)


Sofern nicht die  Bestimmung des § 67 zur Anwendung kommt, geschieht die Pfändung dadurch, dass das  Finanzamt dem Drittschuldner verbietet, an den Abgabenschuldner zu bezahlen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_38`)


Werden beschränkt pfändbare Geldforderungen auf ein Konto des Abgabenschuldners bei  einem Kreditinstitut oder der Österreichischen Postsparkasse überwiesen, so ist gemäß § 54  Abs. 1 AbgEO eine Pfändung des Guthabens auf Antrag des Abgabenschuldners vom  Finanzamt insoweit aufzuheben, als das Guthaben dem der Pfändung nicht unterworfenen  Teil der Einkünfte für die Zeit von der Pfändung bis zum nächsten Zahlungstermin entspricht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_40`)


Gemäß § 54 Abs. 3 AbgEO hat das Finanzamt die Pfändung des Guthabens über Antrag des  Abgabenschuldners für den Teil aufzuheben, dessen dieser bis zum nächsten Zahlungstermin  dringend bedarf, um seinen notwendigen Unterhalt zu bestreiten und seine laufenden  gesetzlichen Unterhaltspflichten zu erfüllen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_54`)


Das Finanzamt hat den aufgrund der Pfändung überwiesenen Betrag in Höhe von € 939,67  mittlerweile dem Bf. zurücküberwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_55`)


Das Bundesfinanzgericht geht wie das Finanzamt davon aus, dass die auf das Konto des Bf.  überwiesenen Beträge, dem Pfändungsschutz des § 292i EO unterliegen (vgl. OGH 28.06.2018,  9 Ob 22/18b).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- `Mag. Damian Wiecher` (person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_5`)


Das Finanzamt erließ am 21.8.2018  den Einkommensteuerbescheid 2016, berücksichtigte die geltend gemachten Krankheitskosten  darin nicht und begründete dies wie folgt: „Die Krankheitskosten der Ehegattin konnten nicht  berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_16`)


Mit Beschwerdevorentscheidung vom 27.11.2018 gab das Finanzamt der Beschwerde teilweise  statt und berücksichtigte EUR 724,95 als außergewöhnliche Belastungen mit folgender  Begründung: „Hat ein Pflegebedürftiger sein Vermögen (zB Wohnung, Sparbuch) noch nicht  übertragen, gehen die Pflegekosten zunächst zulasten dieses Vermögens.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_33`)


Das Finanzamt legte die Beschwerde am 20.3.2019 dem Bundesfinanzgericht vor und  beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_35`)


Mit Schreiben vom  10.7.2020 ergänzte das Finanzamt sein Vorbringen dahin, dass in Umsetzung des  Leistungsfähigkeitsprinzips Krankheitskosten für den Ehepartner insoweit als  außergewöhnliche Belastungen anzuerkennen seien, als diese Aufwendungen das Einkommen  des erkrankten Ehepartners unter das steuerliche Existenzminimum von EUR 11.000,- jährlich  herabmindern würden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_95`)


Wenn das Finanzamt vermeint, der freiwillige Verzicht auf eine Verwertung des Vermögens der  Ehegattin führe dazu, dass die Pflegekosten für die Ehegattin vom Beschwerdeführer freiwillig  getragen würden und daher keine Zwangsläufigkeit der Belastungen vorliegen könne, so ist  ihm Folgendes entgegenzuhalten:  Im Zivilrecht wird zwischen Unterhaltsansprüchen von Eltern gegenüber ihren Kindern und  solchen zwischen Ehegatten insofern differenziert, als einerseits die Unterhaltsverpflichtung  von Kinder gegenüber ihren Eltern (unter anderem) jener zwischen Ehegatten im Rang  nachsteht (vgl § 234 Abs. 2 ABGB) und sich andererseits (nur) der Unterhaltsanspruch eines  Elternteiles (unter anderem) insoweit mindert, als dem Elternteil die Heranziehung des  Stammes eigenen Vermögens zumutbar ist (vgl § 234 Abs. 3 ABGB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_98`)


Somit ist der Verweis des Finanzamtes auf die Erkenntnisse  des VwGH vom 29.4.2015, 2012/13/0012 und vom 20.11.2019, Ro 2018/15/0024 ist nicht  geeignet, sein Vorbringen zu stützen: In beiden Erkenntnissen hat der Verwaltungsgerichtshof  über die Abzugsfähigkeit von Unterhaltsleistungen an einen Elternteil im Zusammenhang mit  einer vorangegangenen Vermögensübertragung vom Elternteil auf Nachkommen  abgesprochen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_99`)


Auch das vom Finanzamt angezogene Argument, das dem Abgabenrecht immanente  Leistungsfähigkeitsprinzip würde neben der vorrangigen Verwertung eigenen Vermögens die  Berücksichtigung eines steuerlichen Existenzminimums von EUR 11.000,- bei der Ehegattin  gebieten, würde nach Ansicht des Bundesfinanzgerichts die Abzugsfähigkeit von  außergewöhnlichen Belastungen durch Unterhaltsaufwendungen für Ehegatten über Gebühr  und in einer nicht vom Gesetz gedeckten Weise einschränken.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_17`)


Das Finanzamt ging im  bekämpften Bescheid davon aus, dass er die Strecke vom Wohnort zum Dienstort  (insgesamt 20,2 km) in zwei Etappen zurücklegte, indem er zunächst vom Wohnort zum  Bahnhof_IP (1. Teilstrecke mit 3,4 km) und von dort weiter zum Bahnhof Bahnhof_L (2.  Teilstrecke) gefahren sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_20`)


Im Erstbescheid vom 17.07.2008 hat des Finanzamt „das große Pendlerpauschale bis 20  km“ iHv € 283,50 berücksichtigt (für die Teilstrecke Wohnung bis Bahnhof_IP).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_30`)


Das Finanzamt hat ausgehend von diesen  Unterlagen eine „Auswertung Fahrplan – Dienstzeit“ erstellt und dem BFG vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_31`)


Das  Finanzamt kommt in dieser Auswertung zum Ergebnis, dass das Begehren des  47Beschwerdeführers  zu Recht besteht und ein Pendlerpauschale in Höhe von 1.032 € zu  berücksichtigen ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_46`)


Da auch das Finanzamt (mit Ausnahme der  Monate Februar und Juni) zu diesem Ergebnis kam (vgl. die dem Bundesfinanzgericht  vorgelegte „Auswertung Pendlerpauschale“, in der die Berücksichtigung von Fahrt- kosten im Wege des großen Pendlerpauschales angeregt wurde), erübrigt sich eine  detailliertere Gegenüberstellung der Dienstzeiten und der Ankunfts- und Abfahrtszeiten  der Züge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_47`)


4.2. Soweit das Finanzamt die Inanspruchnahme des Werkverkehrs in den Monaten Februar  und Juni für zumutbar gehalten und deshalb eine Kürzung des Pauschales vorgenommen  hat, ist festzuhalten:    Im Erkenntnis VwGH 27.07.2016, 2013/13/0088 hat der Verwaltungsgerichtshof klar- gestellt, dass die sich aus § 16 Abs. 1 Z 6 lit. b und c EStG 1988 ergebenden Pauschbe- träge auf Grund des Wortlautes des Gesetzes nicht schon dann nicht zustehen, wenn  der Arbeitnehmer im Werkverkehr befördert werden könnte und ihm dies auch zumut- bar wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_23`)


Tag (Fälligkeitstag) des  auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden Kalendermonates eine  Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen Finanzamt  einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  2 von 4 Seite 3 von 4

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_25`)


Nach § 21 Abs 3 UStG 1994 hat das Finanzamt die Steuer festzusetzen, wenn der Unternehmer  die Einreichung der Voranmeldung pflichtwidrig unterlässt oder wenn sich die Voranmeldung  als unvollständig oder die Selbstberechnung als nicht richtig erweist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 2/20/21/22` | `Finanzamtes Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Guntram Antepoth` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `70-875/4351` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Dr. Viktoria Blaser` (person)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)
- `Bundesamtes für Soziales  und Behindertenwesen` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_36`)


Das Finanzamt wies den Antrag vom 10.08.2018 auf Familienbeihilfe und erhöhte  Familienbeihilfe mit Bescheid vom 16.01.2019 ab, führte begründend den § 6 Abs. 2 lit. d  FLAG 1967 an und verwies auf das vorstehend angeführte Gutachten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_44`)


Ich bin der Meinung, dass ich in der vom Finanzamt anberaumten  ärztlichen Untersuchung bzw. von der untersuchenden Ärztin nicht ernst genommen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Salzburg` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_3`)


Entscheidungsgründe 1.  Verfahrensgang Nachdem das Finanzamt Salzburg-Land (kurz FA) eine Außenprüfung abgeschlossen hatte (Prüfungsauftrag vom 30. November 2011;

**False Positives:**

- `Finanzamt Salzburg` — partial — pred is substring of gold: `Finanzamt Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Salzburg-Land`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt Wien 9/18/19` — partial — pred is substring of gold: `Finanzamt Wien 9/18/19 Klosterneuburg`
- `Finanzamt Wien 9/18/19` — similar text (different position): `Finanzamt Wien 9/18/19 Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)
- `Dr. Heinz Neuner`(person)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_42`)


In der mündlichen Verhandlung vor dem Spruchsenat beim Finanzamt Wien 9/18/19 Klosterneuburg am 05. Dezember 2018 wurde das Verfahren gemäß § 136 FinStrG eingestellt. Zur Begründung der Einstellung siehe Anhang „20181220_Erkenntnis SPS 05122018“.

**False Positives:**

- `Finanzamt Wien 9/18/19` — partial — pred is substring of gold: `Finanzamt Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_107`)


Unter Verweis auf diese Ausführungen wird sohin gestellt der höfliche Antrag, der Beschwerde des FA 9/18/19 Klosterneuburg vom 07. Jänner 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9 / 18 / 19/ Klosterneuburg vom 5. Dezember 2018, SpS *****,  keine Folge zu geben."

**False Positives:**

- `Finanzamt Wien 9` — partial — gold is substring of pred: `Finanzamt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_22`)


Es habe auch keinen dezidierten Auftrag zur Einreichung einer Finanzamtsanzeige gegeben und der Bf. sei auch in Kenntnis gesetzt worden, dass die Kanzlei C. ,,in dieser Sache nichts mehr machen könne“.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

**False Positives:**

- `Finanzamtes Salzburg` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`
- `Finanzamtes  Salzburg` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Susanne Zankl`(person)
- `RgR Amalia Schuetzke`(person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamtes`(organisation)
- `22-967/4918`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Gmunden` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

**False Positives:**

- `Finanzamtes  Kitzbühel Lienz` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Cassandra Witzenhause`(person)
- `Siegfried Basyurt`(person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

**False Positives:**

- `Finanzamtes Wien  12/13/14` — partial — pred is substring of gold: `Finanzamtes Wien  12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Chen Walcker`(person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `63-698/2600`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien 12/13/14` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Regina Vogt`(person)
- `Hedwig Mackiewicz`(person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Baden Mödling`
- `Finanzamtes` — similar text (different position): `Finanzamtes Baden Mödling`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Gabriele Krafft`(person)
- `Daniel Parys`(person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamtes Baden Mödling`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Landeck Reutte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Li Schukardt`(person)
- `Ursula Buchholz`(person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich`(address)
- `Finanzamtes  Landeck Reutte`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Finanzamtes Gmunden` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Sven Oberstelehn`(person)
- `Chantal Eligüzel`(person)
- `Glittstein 70, 9072 Rupertiberg, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

</details>

---

## `Abbreviated Tax Authority` 💣

**F1:** 0.008 | **Precision:** 0.900 | **Recall:** 0.004  

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
| 0.900 | 0.004 | 0.008 | 20 | 18 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 2 | 4581 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Ada Forstner` (person)
- `Elias von Wnuk-Lipinski` (person)
- `Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich` (address)
- `Finanzamt` (organisation)
- `26-066/9346` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Missed by this rule (FN):**

- `Mag. Ronald Kulenkampf` (person)
- `Mag. Monika Schmalzl` (person)
- `06-334/4335` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Missed by this rule (FN):**

- `Mag. Basil Eberhards` (person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `Finanzamt Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_2`)


Beschwerde vom 7.9.2016 gegen die Bescheide des Finanzamtes Österreich - vormals des  FA Kirchdorf Perg Steyr - vom 3.8.2016 betreffend Umsatzsteuer (Vorsteuererstattung) 1-12/2015 und 1- 3/2016, Steuernummer 41-595/2429  und   2.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `41-595/2429` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Nadine Hupmann` (person)
- `Joachim Kotmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Frank Ruhleder  in der Beschwerdesache Dr. Luigi Mainholz  vertreten durch STB, über die mit Beschwerden angefochtenen Bescheide des FA Wien 1/23,  Steuernummer 61-747/1918, betreffend Einkommensteuer 2005, 2006, 2008, 2009, 2010  und 2011 zu Recht erkannt:    Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Missed by this rule (FN):**

- `Hon.-Prof. Frank Ruhleder` (person)
- `Dr. Luigi Mainholz` (person)
- `61-747/1918` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Roderich Stenczel, St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich, über die Beschwerde vom 20. August 2013 gegen die Bescheide  des FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Wiederaufnahme gemäß § 303 BAO  der Körperschaftsteuerbescheide 2008 bis 2010, Steuernummer 60-379/9146  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Dr. Helmut Mittermayr` (person)
- `Roderich Stenczel` (person)
- `St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich` (address)
- `60-379/9146` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Mag.a Philippa Beßerdich` (person)
- `Simone Philipzig` (person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich` (address)
- `Hofer Leitinger Steuerberatung GmbH` (organisation)
- `59-060/2086` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139879.1`) (sent_id: `deanon_BFG_20260814_TEST/139879.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Giacomello  in der Beschwerdesache Natascha Theys vertreten  durch StB über die Beschwerde vom 3. Oktober 2022 gegen den Bescheid des FA Linz  vom  9. September 2022 über die Festsetzung eines ersten Säumniszuschlages (Steuernummer  86-989/6915 ) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Missed by this rule (FN):**

- `Univ.-Prof. Wilfried Giacomello` (person)
- `Natascha Theys` (person)
- `86-989/6915` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Janet Köhle  in der Beschwerdesache der  Textil Bermon, Hans-Bachmann-Straße 4, 2872 Langegg, Österreich  vertreten durch RA-Vertreter, über die Beschwerde vom 31. Mai  2017 gegen die zur Steuernummer 91-124/4580  ergangenen Bescheide des FA St. Johann Tamsweg Zell am See (jetzt  Dienststelle des Finanzamtes Österreich) vom 30. März 2017 betreffend  Einkommensteuer 2009 – 2014 nach Durchführung einer mündlichen Verhandlung am  15.März 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Janet Köhle` (person)
- `Textil Bermon` (organisation)
- `Hans-Bachmann-Straße 4, 2872 Langegg, Österreich` (address)
- `91-124/4580` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_7`)


1. Nach Durchführung einer Außenprüfung (AP) nahm das für das abgabenbehördliche  Verfahren zuständige FA St. Johann Tamsweg Zell am See (FA) - ausgehend von einer unbeschränkten Steuerpflicht der  1 von 30 Seite 2 von 30

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Patrick Poppenheger, Steuernummer 23-019/0780,   Str.1, O1, vertreten durch Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft, Ruster Straße 91, 7000 Eisenstadt, vom 15.07.2020 gegen den  Einkommensteuerbescheid für das Jahr 2018 des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr FA Österreich), vom 29.06.2020, zugestellt am 02.07.2020, nach der im Beisein des  Schriftführers Dietmar Gratz am 29.06.2023 durchgeführten mündlichen Verhandlung  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der  angefochtene Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `Mag. Dieter Fröhlich` (person)
- `Patrick Poppenheger` (person)
- `23-019/0780` (tax_number)
- `Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_59`)


Dieser  Fristverlängerungsantrag wurde laut Eingangsstempel jedoch tatsächlich erst am 17.12.2014  beim Infocenter des Finanzamtes FA St. Johann Tamsweg Zell am See  und somit nach Ablauf der bis zum 15.12.2014  erstreckten Rechtsmittelfrist zur Stellung des Vorlageantrags, daher verspätet eingebracht.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Österreich` | `FA Österreich` |

**Missed by this rule (FN):**

- `Mag. Dieter Fröhlich` (person)
- `Mag. Christian Seywald` (person)
- `Johannes Steiner` (person)
- `Michael Kamper MSc` (person)
- `Ulrike Ackermaier, Bakk. iur.` (person)
- `Knödelhüttenstraße 12, 9184 Mühlbach, Österreich` (address)
- `Woditschka Steuerberatung GmbH` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `75-013/8302` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/144133.1`) (sent_id: `deanon_BFG_20260814_TEST/144133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Farina Solovieva  in der Beschwerdesache der  Folmer Sanitär, Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich, über die Beschwerde vom 27. Oktober 2022 gegen den Bescheid  des FA Bruck Eisenstadt Oberwart  vom 14. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 06-556/2153  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Farina Solovieva` (person)
- `Folmer Sanitär` (organisation)
- `Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich` (address)
- `06-556/2153` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Jacqueline Traxl` (person)
- `Gebhard Hannig` (person)
- `Nußdorfer Markt 4, 4776 Antersham, Österreich` (address)
- `Mag. Paulus Maria Christoph Papst` (person)
- `97-347/7690` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/145808.1`) (sent_id: `deanon_BFG_20260814_TEST/145808.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Silvia Aust   in der Beschwerdesache des Li Süssle, Zierreit 3, 9113 Lippitzbach, Österreich, betreffend den Bescheid des  FA Wien 1/23  vom 21. April 2020   hinsichtlich Einkommensteuervorauszahlungen 2020, Steuernummer 97-936/9955,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Silvia Aust` (person)
- `Li Süssle` (person)
- `Zierreit 3, 9113 Lippitzbach, Österreich` (address)
- `97-936/9955` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `FA Wien  4/5` — partial — pred is substring of gold: `FA Wien  4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Leander Hättrich`(person)
- `Edith Grotehenn`(person)
- `Karlhofstraße 20, 4212 Götschka, Österreich`(address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Wien  4/5/10`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `FA Wien 2/20` — partial — pred is substring of gold: `FA Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Hagen Atar`(person)
- `Priv.-Doz.in Laura Fromader`(person)
- `Oberpetersdorf 6, 4871 Egg, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)
- `60-848/5470`(tax_number)

</details>

---

## `Federal Ministry` 

**F1:** 0.003 | **Precision:** 0.857 | **Recall:** 0.001  

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
| 0.857 | 0.001 | 0.003 | 7 | 6 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 1 | 4593 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_246`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_260`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_180`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_28`)


Für die Einschätzung des Grades der Behinderung  sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des Behinderten- einstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere Be- stimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_172`)


Für die Einschätzung des Grades der  Behinderung sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_164`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_19`)


Für die Einschätzung des Grades der Behinderung sind § 14 Absatz 3 des  Behinderteneinstellungsgesetzes und die Verordnung des Bundesministers für Arbeit, Soziales  und Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades  der Behinderung (Einschätzungsverordnung) vom 18.8.2010 anzuwenden.

**False Positives:**

- `Bundesministers für Arbeit, Soziales  und Konsumentenschutz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt für Gebühren` 💣

**F1:** 0.007 | **Precision:** 0.842 | **Recall:** 0.003  

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
| 0.842 | 0.003 | 0.007 | 19 | 16 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 3 | 4583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `N.N.` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_29`)


In weiteren Schreiben durch unsere Kanzlei  vom 6.6.2018 sowie 26.6.2018 an das zuständige Finanzamt für Gebühren, Verkehrssteuern  und Glückspiel wurde der Sachverhalt nochmals konkret aufgezeigt und erläutert.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_43`)


Der Verfahrensgang vor dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel sowie  dem Bundesfinanzgericht ist evident.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_35`)


Am 19.12.2018 erließ die belangte Behörde, das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel vier Bescheide mit Verspätungszuschlägen von insgesamt 3.990 €.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_98`)


Am 19.12.2018 erließ die belangte Behörde, das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel vier Bescheide mit Verspätungszuschlägen von insgesamt 3.990 €, die wegen  verspäteter Selbstberechnung unter Berücksichtigung der objektiven Pﬂichtwidrigkeit des  säumigen Abgabepﬂichtigen sowie des Ausmaßes der Fristüberschreitung, der Höhe des durch  die verspätete Einreichung der Abgabenerklärung erzielten ﬁnanziellen Vorteiles und des  Grades des Verschuldens, mit 5 % in Ausübung des Ermessens als angemessen von der  belangten Behörde festgesetzt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_100`)


Der Verfahrensgang vor dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel sowie  dem Bundesfinanzgericht ist durch die Bescheide, die Bescheidbeschwerden, die  Beschwerdevorentscheidungen sowie die Vorlage vor dem Bundesfinanzgericht evident.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_13`)


Selbstanzeige beim (damaligen) Finanzamt für Gebühren,  Verkehrssteuern und Glücksspiel (nunmehr Finanzamt Österreich, Dienststelle für  Sonderzuständigkeiten, kurz FA) für die Glücksspielabgabe für den Zeitraum 01/2011 –  11/2016 sowie für Wettgebühren für den Zeitraum 01/2011 – 11/2016.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_507`)


des dem Entstehen der  Abgabenschuldfolgenden Kalendermonats (Fälligkeitstag) an das Finanzamt für Gebühren,  Verkehrsteuern und Glücksspiel zu entrichten.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Dr. F` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_24`)


Mit Mail vom 9.2.2015 teilt Herr Dr. F dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Dr. F` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_25`)


Sobald ihm diese vorliegen, wird er  diese Unterlagen unverzüglich an das Finanzamt für Gebühren Verkehrsteuern und Glücksspiel  weiterleiten.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_4`)


Mit Bescheiden vom 25.9.2019 hat das Finanzamt für Gebühren, Verkehrsteuern und  Glückspiel dem Beschwerdeführer eine Gebühr gemäß § 14 TP 6 GebG in Höhe von 14,30 €  sowie eine Gebührenerhöhung von 7,15 € gemäß § 9 Abs 1 GebG vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_5`)


X1-10) über die "Verkürzung von Stempel- oder Rechtsgebühren" hinsichtlich der "Meldung  des Ausflugsverkehrs" gemäß Tiroler Schischulgesetz 1995 für zehn namentlich genannte Schi-  und Snowboardlehrer (AA u.a.) durch die Prof.in Esra Konwischer (= Beschwerdeführerin, Bf), eine deutsche  Schneesportschule, erstellt und an das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz durch die Bf aus Jänner 2016 samt Beilagen  (Prüfungszertifikat des Dten.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Prof.in Esra Konwischer` (person)
- `Finanzamt Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_129`)


Stellen sie hiebei eine Verletzung der Gebührenvorschriften  fest, so haben sie hierüber einen Befund aufzunehmen und diesen dem Finanzamt für  Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich) zu übersenden.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Gebühren` | `Finanzamt für  Gebühren` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_10`)


IL-SCHI-AUS/B-1/Nr1-29) über die "Verkürzung von Stempel- oder Rechtsgebühren"  hinsichtlich der "Meldung des Ausflugsverkehrs gemäß Tiroler Schischulgesetz 1995" vom  16.12.2015 für gesamt 29 Schilehrer (AA u.a.) durch die Ski- und Snowboardschule XX (=  Beschwerdeführerin, Bf), eine deutsche Schischule, erstellt und an das Finanzamt für  Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz samt Beilagen und Kopien der  Lichtbildausweise der gemeldeten Lehrer sowie die schriftliche Erledigung durch die  Bezirkshauptmannschaft.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Gebühren` | `Finanzamt für  Gebühren` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_132`)


Stellen sie hiebei eine Verletzung der Gebührenvorschriften  fest, so haben sie hierüber einen Befund aufzunehmen und diesen dem Finanzamt für  Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich) zu übersenden.

| Predicted | Gold |
|---|---|
| `Finanzamt für  Gebühren` | `Finanzamt für  Gebühren` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_381`)


Wir weisen darauf hin, dass die im Ergänzungsersuchen angeforderten Daten dem Finanzamt  für Gebühren, Verkehrsteuern und Glücksspiel bereits im Zuge der Selbstanzeige vom 21.  Dezember 2016 übermittelt wurden.

**False Positives:**

- `Finanzamt  für Gebühren` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_44`)


Für das Finanzamt  für Gebühren, Verkehrsteuern und Glücksspiel ist nicht nachvollziehbar, anhand welchen  Zahlenmaterials diese Kaufpreisempfehlungen errechnet wurden.

**False Positives:**

- `Finanzamt  für Gebühren` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_17`)


In der Begründung führte das Finanzamt  für Gebühren, Verkehrsteuern und Glückspiel im Wesentlichen aus:  „Auf Grund des § 1 GebG 1957 unterliegen den Gebühren im Sinne des Gebührengesetzes ua.

**False Positives:**

- `Finanzamt  für Gebühren` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

</details>

---

## `OECD` 💣

**F1:** 0.003 | **Precision:** 0.636 | **Recall:** 0.002  

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
| 0.636 | 0.002 | 0.003 | 11 | 7 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 4 | 4592 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_36`)


Am 2.6.2016 erließ das Finanzamt eine abweisende Beschwerdevorentscheidung und führte in  der diesbezüglichen Begründung wörtlich wie folgt aus:  Gemäß Art 15 Abs 2 OECD-Musterabkommen sind Vergütungen, die eine in einem  Vertragsstaat ansässige Person für eine im anderen Vertragsstaat ausgeübte unselbstständige  Arbeit bezieht, nur im Ansässigkeitsstaat zu besteuern, wenn der Empfänger sich im anderen  Staat (Tätigkeitsstaat) nicht länger als 183 Tage innerhalb eines Zeitraums von 12 Monaten,  der während des betreffenden Steuerjahres beginnt und endet, aufhält und die Vergütungen  von einem Arbeitgeber oder für einen Arbeitgeber gezahlt werden, der nicht im anderen Staat  (Tätigkeitsstaat) ansässig ist, und die Vergütungen nicht von einer Betriebsstätte getragen  werden, die der Arbeitgeber im anderen Staat hat.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_50`)


Aus Sicht der OECD soll das Ausmaß der „Integration“ des  Arbeitnehmers entscheidend auf die Arbeitgeberqualifikation sein.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_50`)


Diese Auffassung wird im Übrigen auch durch die französische Fassung als eine der beiden  Originalfassungen des OECD-Musterabkommens (vgl. zur Bedeutung der Sprachfassungen  Lang, The Interpretation of Tax Treaties and Authentic Languages, in Guglielmo Maisto, Angelo  Nikolakakis and John M. Ulmer, eds., Essays on Tax Treaties: A Tribute to David A. Ward, 2013,  15, 17, sowie Vogel, Doppelbesteuerungsabkommen5, 2008, Einl.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_57`)


Dazu wird im OECD-Musterkommentar (2010) festgehalten, dass manche Staaten  die Möglichkeit eines Vortrags nicht verbrauchter Steueranrechnungsbeträge in Erwägung  ziehen oder sogar umgesetzt haben (Art. 23 B Rz. 66), es besteht diesbezüglich aber weder eine  einheitliche Staatenpraxis noch eine aus den Abkommen resultierende Verpflichtung.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_8`)


Insbesondere im Hinblick darauf, dass es sich im gegenständlichen Fall um ein junges  Unternehmen handelt, welches über keine auf die Beantragung öffentlicher Förderungen  spezialisierte Personalkapazität verfügt und auch die Tatsache, dass keine zusätzlichen  Erläuterungen und Demonstrationen unserer Produkte möglich waren, haben die über  FinanzOnline eingereichten Beschreibungen unsere Leistungen auf dem Gebiet der Forschung  und Entwicklung im Sinne des OECD Frascati-Manuals möglicherweise nicht ausreichend zum  Ausdruck gebracht.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_9`)


[…]  In der Beilage finden Sie daher die nunmehr überarbeiteten Projektbeschreibungen, welche  unseres Erachtens die Erfüllung der Kriterien des OECD Frascati-Manuals und der darauf  beruhenden inländischen Rechtsvorschriften ausreichend zum Ausdruck bringen, sodass uns  die Forschungsprämie gem. § 108c EStG 1988 für das Jahr 2012 zustehen sollte."

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/143317.1`) (sent_id: `deanon_BFG_20260814_TEST/143317.1_21`)


Nach Z.5.4  des OECD-Kommentars zu Art 5 begründet ein Berater, der innerhalb derselben Zweigstelle  eines Bankunternehmens wechselnde Räumlichkeiten benützt, für seinen Arbeitgeber eine  Betriebsstätte.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_167`)


Dies entspricht Art. 4 Abs. 1, 2. Satz OECD- Musterabkommen, in dem es zur Definition der „in einem Vertragsstaat ansässigen Person“  heißt: „Der Ausdruck umfasst jedoch nicht eine Person, die in diesem Staat nur mit Einkünften  aus Quellen in diesem Staat oder mit in diesem Staat gelegenem Vermögen steuerpflichtig ist“.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_42`)


Diese abkommensrechtliche  Verpflichtung zur Steuerfreistellung besteht auf Grund der "Methodenartikel" der Abkommen  (Art. 23A OECD-MA) allerdings nur dann, wenn auch der Tätigkeitsstaat (Beschäftigerstaat) den  Beschäftiger als Arbeitgeber im Sinn der abkommensrechtlichen 183-Tage-Klausel wertet und  wenn daher beide Staaten von einer Zuteilung des Besteuerungsrechtes an den Tätigkeitsstaat  ausgehen.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_79`)


Gemäß den angeführten Erläuterungen des OECD-MK gelten Zahlungen für ein Konkurrenz-  oder Wettbewerbsverbot nicht als Vergütungen für unselbständige Arbeit, die vor Beendigung  des Dienstverhältnisses in einem Staat ausgeübt worden ist.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_82`)


Dem Wortlaut des DBA Art. 15 und der Kommentierung des OECD-MA folgend sind die  Zahlungen aus der Konkurrenzklausel nicht als nachträgliches Entgelt für die seinerzeit in  Österreich erbrachten aktiven Arbeitsleistungen anzusehen, sondern stellen ein Entgelt für die  Unterlassung von wettbewerbsschädlichen Arbeitsaktivitäten nach Beendigung des  Dienstverhältnisses dar.

**False Positives:**

- `OECD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Technical University` 

**F1:** 0.000 | **Precision:** 0.333 | **Recall:** 0.000  

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
| 0.333 | 0.000 | 0.000 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 4598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_39`)


Da für dieses Studium kein  Studienerfolg nachgewiesen werden konnte, wurde der Familienbeihilfebezug mit September  2021 eingestellt.  Mit Februar 2022 (somit ab dem Sommersemester 2022) hat StR Armin Dürrwaechter  das Studium  gewechselt und studiert nunmehr an der FH Campus Wien („0599 FH-Bachelor Gesundheits-  und Krankenpflege).

| Predicted | Gold |
|---|---|
| `FH Campus Wien` | `FH Campus Wien` |

**Missed by this rule (FN):**

- `StR Armin Dürrwaechter` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_34`)


Dem Schreiben war eine Bestätigung des Studienerfolges  von der FH Campus Wien beigefügt, aus dem die positiv absolvierte Gesamtanzahl von 19,5  ECTS-Credits hervorgeht.

**False Positives:**

- `FH Campus Wien beigefügt` — partial — gold is substring of pred: `FH Campus Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Campus Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_65`)


Im vorliegenden Fall hat der Studierende StR Armin Dürrwaechter – wie aus dem festgestellten Sachverhalt  ersichtlich – zunächst für drei Semester (Wintersemester 2020 bis inklusive Wintersemester  2021) Biologie studiert, bevor er dann mit Februar 2022 (und somit ab dem Sommersemester  2022) das Studium „Gesundheits- und Krankenpflege“ an der FH Campus Wien begonnen hat.

**False Positives:**

- `FH Campus Wien begonnen hat` — partial — gold is substring of pred: `FH Campus Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Armin Dürrwaechter`(person)
- `FH Campus Wien`(organisation)

</details>

---

## `Single Letter Company GmbH` 💣

**F1:** 0.006 | **Precision:** 0.298 | **Recall:** 0.003  

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
| 0.298 | 0.003 | 0.006 | 47 | 14 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 33 | 4585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_40`)


Er ist seit xx.xx.xxxx als „3D Design Engineer“ bei der X GmbH, mit dem Sitz in Adresse  unselbständig erwerbstätig.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_48`)


Dass der Bf. bei der X GmbH zu den festgestellten Konditionen tätig war ist einerseits zwischen  den Parteien unstrittig und geht darüber hinaus aus dem vom Bf. selbst vorgelegten Auszug  des Dienstvertrages, sowie dessen Anhang 2 hervor.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Charles Dormayr (=Bf.) erwarb mit Kaufvertrag vom 25.01.2019 die Liegenschaften EZ BBB und  CCC je KG XX um einen Barbetrag von pauschal 100.000 Euro von der X GmbH (= X GmbH).

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Missed by this rule (FN):**

- `Charles Dormayr` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_11`)


aus den im Insolvenzverfahren der X GmbH geltend gemachten und gerichtlich anerkannten  Forderung der Bf. iHv 372.936,25 Euro.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_13`)


Die Bf. habe im Insolvenzverfahren der X GmbH eine Forderung iHv 513.875,98 Euro  angemeldet (davon festgesetzte Forderung 448.875,98 Euro) und sodann – um den  Sanierungsplan nicht zu gefährden – auf die ihr zugesprochene Barquote in Höhe von 20%  verzichtet.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_15`)


Seitens der X GmbH sei im Gegenzug eine Klage gegen die Bf. auf Löschung der einverleibten  Pfandrechte zugunsten der Bf.  gegen Zahlung eines Betrages von 100.098 Euro Zug um Zug  eingebracht worden.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_16`)


Mit Vereinbarung vom 21.12.2018 zw. der Bf. und der X GmbH sei vereinbart worden, dass die  gegenständlichen Liegenschaften zu einem Preis von pauschal 100.000 Euro von der X GmbH  an die Bf. veräußert werden und bei Umwidmung eines Teils der EZ CCC in Bauland der  Verkaufspreis dieser EZ je zur Hälfte der Bf. sowie dem Geschäftsführer der AB zufallen solle.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_28`)


Dagegen richtet sich der Vorlageantrag vom 13.01.2021, der keine weiteren Argumente  enthielt.   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Charles Dormayr (=Bf.) hatte der X GmbH 2 Kredite gewährt, welche auf den hier  gegenständlichen Liegenschaften EZ BBB sowie EZ CCC der KG XX mit Pfandrechten iHv  insgesamt 340.691,34 Euro sichergestellt wurden.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Missed by this rule (FN):**

- `Charles Dormayr` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_37`)


Dagegen erhob die X GmbH Rekurs sowie Klage auf Löschung der ob den gegenständlichen  Liegenschaften einverleibten Pfandrechten Zug um Zug gegen Bezahlung eines Betrages von  100.098 Euro.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_38`)


Am 21.12.2018 wurde eine Vereinbarung zwischen der Bf. und der X GmbH abgeschlossen  welche – neben einer weiteren Kreditvergabe der Bf. an die X GmbH - betreffend  gegenständlicher Liegenschaften festhielt, dass sich die X GmbH verpflichtete die  Liegenschaften EZ BBB und EZ CCC, KG XX, Bezirksgericht Weiz zu einem Pauschalkaufpreis von  100.000,00 Euro an die Bf. zu veräußern, das Verfahren vor dem LGZ Graz zu GZ Cg nach  Umsetzung dieser Vereinbarung ewig ruhend gestellt wird sowie mit Umsetzung dieser  Vereinbarung das beim Bezirksgericht Weiz zu GZ E eingeleitete  Zwangsversteigerungsverfahren eingestellt wird.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Missed by this rule (FN):**

- `Bezirksgericht` (organisation)
- `Bezirksgericht` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_39`)


Am 27.02.2019 wurde ein Kaufvertrag zwischen der Bf. und der X GmbH über die EZ BBB sowie  EZ CCC der KG XX mit einem Kaufpreis von pauschal 100.000 Euro in bar abgeschlossen.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)


Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG vor.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)
- `L GmbH &  Co`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_33`)


Die Gesellschafter/ Treugeber können sich in Gesellschafterversammlungen und  Beschlussfassungen nur durch einen anderen Gesellschafter, einen Ehegatten, einen Elternteil,  ein volljähriges Kind, einen Testamentsvollstrecker, seinen ständigen Generalbevollmächtigten,  einen anderen Treugeber oder einen Vertriebspartner der Gesellschaft/ L GmbH & Co vertreten  lassen.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_45`)


In der gesonderten zugestellten Bescheidbegründung wurde ausgeführt:  „Aus dem übermittelten „Reeder-Zertifikat“ Nr. 277 geht hervor, dass der Bf. an der Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG) beteiligt ist.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_122`)


Der Betrieb des Schiffes, wobei sich die Gesellschaft Dritter (Vertragsreeder) bedient, die für  die S GmbH & Co KG handeln, geht jedenfalls über eine Vermögensverwaltung hinaus.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `S GmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_179`)


Nach Ansicht des Bundesfinanzgerichtes hat die Abgabenbehörde in unbedenklicher Weise in  wirtschaftlicher Betrachtungsweise die gegenständliche Beteiligung an der Schifffahrtsgesell- schaft S GmbH & Co KG als eine Beteiligung nach Art eines stillen Gesellschafters qualifiziert  und die daraus erklärten negativen Einkünfte den nichtausgleichsfähigen Einkünften aus  Kapitalvermögen zugerechnet.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `S GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_8`)


Zu den nicht anerkannten Geschäftspartnern der Bf wird im Einzelnen angeführt:   U B GmbH: Leistungs- und Rechnungszeitraum Juni-November 2011, Konkurs Februar  2012;

**False Positives:**

- `B GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_15`)


 N G GmbH: Gf nicht in Österreich gemeldet;

**False Positives:**

- `G GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_25`)


 P S E GmbH: HFU-Auszug, Gewerbeschein, Firmenbuchauszug lagen vor, Bezahlung per  Überweisung;

**False Positives:**

- `E GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_30`)


 M D GmbH: kein Wissen mehr bei der Bf über die seinerzeitige Geschäftsanbahnung;

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_377`)


Dem im Juni 2000 bewilligten Einreichplan folgt im baubehördlichen Akt ein mit  5.Sept 2007 datierter „Austauschplan“ eines neuen Planverfassers (IS Ingenieurbüro D GmbH),  der sich vom bewilligten Einreichplan aus 7/2000 im Wesentlichen dadurch unterscheidet,  dass - bei unveränderten Außenmaßen des Wohnhauses - nunmehr sieben Wohneinheiten  (2x EG/ 5x „DG 1.Ebene“ mit Wohnungsbezeichnung W 1 - W 5) und ein Großraum mit Galerie  in einem neuen „DG 2.Ebene“ (ohne Wohnungsnummerierung) ausgeführt werden sollen.

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_466`)


2008 verrechnete die Elektro-X GmbH u.a. acht Stück „Tastereinsätze für Hotelcards“.

**False Positives:**

- `X GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_40`)


Der BF war von 2007 bis Juli 2012 Geschäftsführer der R GmbH, welche ihren Sitz an der  Adresse Adr Ö BF hatte und einen Campingplatz betrieb.

**False Positives:**

- `R GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_53`)


Dass der BF von 2007 bis Juli 2012 Geschäftsführer der R GmbH, welche ihren Sitz an der  Adresse Adr Ö BF hatte und einen Campingplatz betrieb, war, wurde vom BF in der  Niederschrift vom 25.07.2013 angegeben bzw. ergibt sich dies aus den vorgelegten Unterlagen.

**False Positives:**

- `R GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_68`)


Der Schwerpunkt der wirtschaftlichen Interessen des BF lag im maßgeblichen Zeitraum in  Österreich, da er bis Juli 2012 Geschäftsführer der R GmbH war.

**False Positives:**

- `R GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_41`)


Der BF hat schließlich mit Wirksamkeit ab 1.12.2022 in die Privatwirtschaft in ein  Dienstverhältnis mit der D GmbH gewechselt. Die GmbH baut International Einsatzleitzentralen  für die Feuerwehr und die Polizei, für Flughäfen und Industrie.

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_8`)


Die G1 ist Gruppenträger, zu deren Unternehmensgruppe außer dem Bauunternehmen A W  GmbH auch die G3 (FN X3) und die G4 (FN) gehören.

**False Positives:**

- `W  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_60`)


Aus der Lebensversicherung V2 wurden EUR 204.810,02 am  07.06.2018 und aus der Lebensversicherung V1 wurden EUR 241.046,47 am 16.11.2018 an die  A W GmbH überwiesen.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_17`)


Zur mangelhaften Zustellung führt die Bf. begründend aus, dass ein Bescheid über die  Festsetzung einer Zwangsstrafe in Höhe von € 1.000 gegen die W GmbH (StNr 123) erlassen  und dagegen fristgerecht Beschwerde erhoben worden sei.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_21`)


Gesellschafter der W GmbH ihrerseits wären die XX Immobilien Holding GmbH sowie FG – am  Stammkapital zu 72% bzw. 28% beteiligt.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_24`)


Mit Beschluss vom XX. Mai 2022 habe das HG Wien gemäß S 15a GmbHG AB zum  Notgeschäftsführer der W GmbH aus dem Grund bestellt, als seitens der W GmbH  Schadenersatzansprüche gegen ihren Geschäftsführer, XX, geltend gemacht werden sollten.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation
- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_28`)


Wie oben dargelegt, treffe die Bf. kein Verschulden daran, dass die Meldung der  wirtschaftlichen Eigentümer bisher noch nicht erfolgen konnte, weil dem Notgeschäftsführer  der W GmbH die dazu notwendigen Informationen nicht bekannt gewesen seien und er diese  bisher auch nicht in Erfahrung habe bringen können.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_57`)


Sachverhalt   Unbeschränkt haftender Gesellschafter der Beschwerde führenden Uwe Dörfl  ist die W GmbH.  Als Kommanditisten sind die XX Immobilien Holding GmbH und die A-Finanzvermittlung GmbH  beteiligt.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Uwe Dörfl`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_58`)


Geschäftsführerin der Bf. ist die W GmbH (FN ***).

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_59`)


An der W GmbH wiederum sind FG zu 28% sowie die XX Immobilien Holding GmbH zu 72% am  Stammkapital beteiligt.

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_60`)


Vertreten wird die W GmbH durch ihre (beiden) Geschäftsführer XX  und – seit dem 3. Mai 2022 – durch AB als Notgeschäftsführer gemäß § 15a GmbHG (FN ***).

**False Positives:**

- `W GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/147494.1`) (sent_id: `deanon_BFG_20260814_TEST/147494.1_30`)


Die BF erzielte in den Beschwerdejahren 2018 – 2020 Einkünfte aus nichtselbständiger Arbeit  von der O GmbH.  Die BF war in den Beschwerdejahren 2018 – 2020 auch für den S als Krankenschwester in  Alten- und Pflegeheimen tätig.

**False Positives:**

- `O GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_25`)


Begründung laut Niederschrift über die Schlussbesprechung und gleichlautend laut  Außenprüfungsbericht: „Am 16.06.2015 wurde mit Herrn X (Baumeister der E GmbH) eine  Niederschrift aufgenommen.

**False Positives:**

- `E GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_30`)


Auf der Baustelle  waren Arbeiter der D GmbH, einer Firma von Frau B, die die Arbeiten ausgeführt haben.

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_78`)


Es ist somit ungewöhnlich, dass die Bf., bei der Frau B 100% beteiligt ist,  Aufträge an die Mackwart und Reinink Automotive GmbH vergibt, welche wiederum Arbeiter von der D GmbH, bei der Frau B  auch 100% beteiligt ist, zur Verfügung gestellt bekommt.

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mackwart und Reinink Automotive GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_139`)


II. Zum Nichtvorliegen von Scheinrechnungen bzw Scheingeschäften  a) Argumentation des Finanzamtes  Die beiden tragenden Argumente auf Prüfer-/Behördenseite sind erstens die  Schwesterneigenschaft der [Bf.] und der D GmbH angesichts der gemeinsamen Machthaberin C  B und zweitens deren Ausnützen der von ihm eingestandenen Druckausübung "absoluten  Notsituation" des Herrn X.  b) Einwendungen

**False Positives:**

- `D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_201`)


Der VwGH hat dazu längst konstatiert (vgl  VwGH 18.03.2022, Ra°2020/13/0016 Rn 17):  "17 Die Revisionswerberin hat wiederholt ins Treffen geführt, dass bei der L GmbH eine  Zurechnung der Leistungen, die - behaupteterweise – an die Revisionswerberin erbracht worden  waren, stattgefunden hat und dieser diesbezüglich Steuern vorgeschrieben worden sind.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_202`)


Dazu  ist zu bemerken, dass gegenständlich zwar keine Bindung an die Beurteilung des Finanzamts in  Ansehung der L GmbH besteht.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Suffix GmbH & Partner KG` 💣

**F1:** 0.003 | **Precision:** 0.149 | **Recall:** 0.002  

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
| 0.149 | 0.002 | 0.003 | 47 | 7 | 40 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 40 | 4592 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_167`)


Kann kein Firmenwert entstehen, weil die operativen Geschäfte (Vertragsreederei mit  Unternehmerrisiko) nicht von der Schifffahrtsgesellschaft S GmbH & Co KG, sondern von der L  GmbH & Co und der Mohrlock Metall GmbH & Co KG durchgeführt werden und besteht deshalb der Wert der  Gesellschaft lediglich im Buchwert inklusive der stillen Reserven des Schiffes, so ist dies ein  weiterer Hinweis dafür, dass keine mitunternehmerische Beteiligung, sondern eine Beteiligung  nach Art eines stillen Gesellschafters vorliegt.

| Predicted | Gold |
|---|---|
| `Schifffahrtsgesellschaft S GmbH & Co KG` | `Schifffahrtsgesellschaft S GmbH & Co KG` |

**Missed by this rule (FN):**

- `Mohrlock Metall GmbH & Co KG` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` | `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` (person)
- `Felizitas Johanesson` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Astoria Wirtschaftstreuhand GmbH & Co KG` | `Astoria Wirtschaftstreuhand GmbH & Co KG` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Mag.a Heidrun Eifeler` (person)
- `Esra Luetje` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Chen Thiergarten, Recyclingstraße 4z, 9911 Vergein, Österreich, vertreten durch Lang & Partner Steuerberatung  GmbH & Co KG, Kapfenstein 123, 8353 Kapfenstein, über die Beschwerde der  beschwerdeführenden Partei vom 17. Juli 2023 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Bescheidaufhebung gem § 299 BAO vom 30. Dezember 2022 hinsichtlich der Bescheide  Umsatzsteuer 2019 und Feststellung von Einkünften gemäß § 188 BAO 2019, jeweils vom 7.  Jänner 2022, Steuernummer 91-654/5089  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lang & Partner Steuerberatung  GmbH & Co KG` | `Lang & Partner Steuerberatung  GmbH & Co KG` |

**Missed by this rule (FN):**

- `Dr. Martin C. WITTMANN` (person)
- `Chen Thiergarten` (person)
- `Recyclingstraße 4z, 9911 Vergein, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `91-654/5089` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_24`)


Nach detaillierten Ausführungen des bundesweiten Fachbereiches für Einkommen– und  Körperschaftssteuer vom 31. August 2012 und nach Schlussbesprechung vom 12. Oktober  2012 wurden im Bericht über das Ergebnis der abgabenbehördlichen Prüfung in hier  interessierender Hinsicht folgende steuerlichen Feststellungen getroffen:   „TZ 1. Sonderbetriebsausgaben  a) Sachverhalt:  …  b) Steuerliche Würdigung:  Bei den angeführten „Modellentwicklungsaufwendungen“ handelt es sich um von der AbisJ  GmbH & Co KG an Dritte geleistete Ausgaben.

| Predicted | Gold |
|---|---|
| `AbisJ  GmbH & Co KG` | `AbisJ  GmbH & Co KG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_27`)


Die  einzelnen Aufwendungen für die Modellentwicklung sind daher im Betrieb der steuerlichen  Mitunternehmerschaft AbisJ als Betriebsausgabe zur berücksichtigen und nicht anteilig bei den  einzelnen „Zielgesellschaften“, an denen sich die AbisJ GmbH & Co KG als atypisch stille  Gesellschafterin beteiligt.

| Predicted | Gold |
|---|---|
| `AbisJ GmbH & Co KG` | `AbisJ GmbH & Co KG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

| Predicted | Gold |
|---|---|
| `CONSULTATIO Steuerberatung GmbH & Co KG` | `CONSULTATIO Steuerberatung GmbH & Co KG` |

**Missed by this rule (FN):**

- `Dr.in Danielle Merte` (person)
- `Mag.a Susanne Groesche` (person)
- `Unternurpensalm 12, 5141 Moosdorf, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `76-369/9701` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` — partial — gold is substring of pred: `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_34`)


Im vorliegenden Fall ist nämlich der anwachsungsbedingte Erwerb des Grundstücks nicht  isoliert sondern in Zusammenschau mit dem Erwerb der Mitunternehmeranteile an der Wohlgemut Getränke GmbH & Co KG sowie des damit in Verbindung stehenden Sonderbetriebsvermögens zu sehen.

**False Positives:**

- `Im vorliegenden Fall ist nämlich der anwachsungsbedingte Erwerb des Grundstücks nicht  isoliert sondern in Zusammenschau mit dem Erwerb der Mitunternehmeranteile an der Wohlgemut Getränke GmbH & Co KG` — partial — gold is substring of pred: `Wohlgemut Getränke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_4`)


Darüber hinaus war er an der Schifffahrtsgesellschaft S GmbH & Co KG mit Sitz in H,  Deutschland, als Kommanditist beteiligt.

**False Positives:**

- `Darüber hinaus war er an der Schifffahrtsgesellschaft S GmbH & Co KG` — partial — gold is substring of pred: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_11`)


In der am 4.4.2014 beim Finanzamt eingelangten Einkommensteuererklärung für 2012 erklärte  der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `Beteiligung an der S GmbH & Co KG` — partial — gold is substring of pred: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_13`)


In der am 12.1.2015 beim Finanzamt eingelangten Einkommensteuererklärung für 2013  erklärte der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `Beteiligung an der S GmbH & Co KG` — partial — gold is substring of pred: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)


Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG vor.

**False Positives:**

- `Rudolphson Heizung GmbH & Co KG` — partial — pred is substring of gold: `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG` — partial — gold is substring of pred: `L GmbH &  Co`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)
- `L GmbH &  Co`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_45`)


In der gesonderten zugestellten Bescheidbegründung wurde ausgeführt:  „Aus dem übermittelten „Reeder-Zertifikat“ Nr. 277 geht hervor, dass der Bf. an der Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG) beteiligt ist.

**False Positives:**

- `Rudolphson Heizung GmbH & Co KG` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_48`)


Die Bereederung des Schiffes wurde durch 2 Verträge geregelt (technische Bereederung inkl.  Operating und Crewing durch Bürgin & Siedle Umwelt GmbH& Co KG; kaufmännische Bereederung durch QGM Technik GmbH & Co KG.

**False Positives:**

- `Bereederung durch QGM Technik GmbH & Co KG` — partial — gold is substring of pred: `QGM Technik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bürgin & Siedle Umwelt GmbH&`(organisation)
- `QGM Technik GmbH & Co KG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_71`)


Er beantragte die Anerkennung der Verlusttangente 2011 aus der Beteiligung an der S GmbH &  Co KG in Höhe von 34.275,23 €, die Zurücknahme der Endgültigkeitserklärung des  Einkommensteuerbescheides 2012 sowie die Erklärung des Einkommensteuerbescheides 2013  als gemäß § 200 Abs. 1 BAO vorläufiger Bescheid.

**False Positives:**

- `Beteiligung an der S GmbH &  Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_119`)


Im  kaufmännischen Reedervertrag mit der QGM Technik GmbH & Co KG nimmt der Vertragsreeder alle  Geschäfts- und Rechtshandlungen vor, die der kaufmännische Geschäftsbetrieb einer Reederei  gewöhnlich mit sich bringt und erfordert (Einsatz und Beschäftigung des Schiffes, Versicherung,  Interessenswahrnehmung).

**False Positives:**

- `Im  kaufmännischen Reedervertrag mit der QGM Technik GmbH & Co KG` — partial — gold is substring of pred: `QGM Technik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QGM Technik GmbH & Co KG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_120`)


Im technischen Reedervertrag mit der Mohrlock Metall GmbH & Co KG nimmt  der Vertragsreeder alle Geschäfts- und Rechtshandlungen vor, die der technische  8 von 13 Seite 9 von 13

**False Positives:**

- `Im technischen Reedervertrag mit der Mohrlock Metall GmbH & Co KG` — partial — gold is substring of pred: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_126`)


2. Beweiswürdigung  Strittig ist, ob es sich bei der Beteiligung an der Schifffahrtsgesellschaft S GmbH & Co KG um  eine mitunternehmerische Beteiligung handelt und damit Einkünfte aus Gewerbebetrieb  vorliegen oder um eine Beteiligung nach Art eines stillen Gesellschafters und damit Einkünfte  aus Kapitalvermögen vorliegen.

**False Positives:**

- `Beteiligung an der Schifffahrtsgesellschaft S GmbH & Co KG` — partial — gold is substring of pred: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_149`)


Aufgrund der Bestimmung des § 21 Abs. 1 BAO ist es durchaus zulässig, dass die Abgaben- behörde die Beteiligung als Kommanditist an einer deutschen GmbH & Co KG als eine  Beteiligung nach Art eines stillen Gesellschafters beurteilt und die aus dieser Beteiligung  10 von 13 Seite 11 von 13

**False Positives:**

- `Beteiligung als Kommanditist an einer deutschen GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_151`)


Die Abgabenbehörde beurteilt den Gesellschaftsvertrag, welcher zwischen der Dörfel u. Rudolphson Heizung GmbH & Co KG und dem Bf. abgeschlossen wurde, in wirtschaftlicher Betrachtungsweise als Vertrag, mit  welchem eine Beteiligung nach Art eines stillen Gesellschafters abgeschlossen wurde.

**False Positives:**

- `Rudolphson Heizung GmbH & Co KG` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_167`)


Kann kein Firmenwert entstehen, weil die operativen Geschäfte (Vertragsreederei mit  Unternehmerrisiko) nicht von der Schifffahrtsgesellschaft S GmbH & Co KG, sondern von der L  GmbH & Co und der Mohrlock Metall GmbH & Co KG durchgeführt werden und besteht deshalb der Wert der  Gesellschaft lediglich im Buchwert inklusive der stillen Reserven des Schiffes, so ist dies ein  weiterer Hinweis dafür, dass keine mitunternehmerische Beteiligung, sondern eine Beteiligung  nach Art eines stillen Gesellschafters vorliegt.

**False Positives:**

- `L  GmbH & Co und der Mohrlock Metall GmbH & Co KG` — partial — gold is substring of pred: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

**False Positives:**

- `Rothwangl & Partner Steuerberatungs GmbH & Co KG` — partial — pred is substring of gold: `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Wladimir Beheim`(person)
- `Bruno Rüttgers`(person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich`(address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG`(organisation)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_3`)


Grießhaber Finanzen  GmbH & Co KG, Göritzer Straße 96, 5662 Großsonnberg, Österreich  beide vertreten durch yy Wirtschaftstreuhand Gesellschaft mbH, Straße 2, Ort,   gegen den Bescheid des Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, § 323 b BAO)  vom 29. November 2012 betreffend Feststellung der Einkünfte gemäß § 188 BAO für das Jahr  2008 (der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft) zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)
- `Göritzer Straße 96, 5662 Großsonnberg, Österreich`(address)
- `yy Wirtschaftstreuhand Gesellschaft mbH`(organisation)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)
- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_14`)


[...]   Verfahrensgang  Nach Einreichung der Erklärungen samt Beilagen wurden den Bf. im Feststellungsbescheid der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft (in der Folge Zielgesellschaft) des Jahres 2008 folgende  Einkünfte zugerechnet:  1. Richsteiger Marine: ein Betrag von -€ 1.679.493,29 (Verlustzuweisung -€ 1.520.000,00 zzgl.  Sonderbetriebsausgaben in Höhe von -€ 159.493,29) und  2. Grießhaber Finanzen  GmbH & Co KG: ein Betrag von -€ 938.729,84 (Verlustzuweisung € - 838.138,16 zzgl. Sonderbetriebsausgaben in Höhe von -€ 100.591,68).

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_56`)


Nunmehr wurden im Feststellungsbescheid der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft Einkünfte wie folgt zugerechnet:   1. Richsteiger Marine: € -1.520.000,00 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 1.520.000,00 zu berücksichtigen  sind) und  2. Grießhaber Finanzen  GmbH & Co KG: € -838.138,16 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 838.138,16 zu berücksichtigen  sind).

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_85`)


Mit Ablauf des Stichtages 31.  März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit  Buchwertfortführung gem. Art IV UmgrStG.   Grießhaber Finanzen  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober  2008 gegründet.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_119`)


Zusammenschlussvertrag – „Errichtung stille Gesellschaft“ - Grießhaber Finanzen  GmbH & Co KG:  Die mit Zusammenschlussvertrag vom 23. Juni 2009 rückwirkend errichtete Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft ist auf unbestimmte Zeit errichtet und frühestens kündbar mit 1. Juli 2015  unter Einhaltung einer sechsmonatigen Frist.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)
- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_137`)


Gesellschaften mit gleicher Beteiligungs- sowie Gesellschafterstruktur, welche im  Prüfzeitraum an der operativ tätigen Gablonsky&Rethlefsen Gastronomie AG als atypisch stille Gesellschafter beteiligt waren:   2009:    die Richsteiger Marine   die Grießhaber Finanzen  GmbH & Co KG   die EF GmbH & Co KG   die GH GmbH & Co KG  Gesellschafter der Bf. (sowie der anderen AbisJ Gesellschaften) sind laut Firmenbuchauszug die Widdra & Koslowa Pharma GmbH als Komplementärin und die Pietzschke Chemie GmbH als Kommanditistin.

**False Positives:**

- `Richsteiger Marine   die Grießhaber Finanzen  GmbH & Co KG   die EF GmbH & Co KG   die GH GmbH & Co KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)
- `Widdra & Koslowa Pharma GmbH`(organisation)
- `Pietzschke Chemie GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_143`)


In der Erklärung zur einheitlichen und gesonderten Gewinnfeststellungen der Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft für das Jahr 2008 wurden bei den einzelnen atypisch stillen  Gesellschafterinnen folgende Sonderbetriebsausgaben in Abzug gebracht:  Richsteiger Marine: -€ 159.493,29   Grießhaber Finanzen  GmbH & Co KG: -€ 100.591,68  Hierbei handelte es sich um anteilige Kosten aus der „Modellentwicklung“, welche bei der  atypisch stillen Gesellschafterin angefallen sind.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_152`)


Grießhaber Finanzen  GmbH & Co KG:  Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der Bf. (atypisch stille  Gesellschafterin) für das Jahr 2008:     €  Initialisierungsaufwand 326.830,00  Verkehrssteuern 22.540,00  Lfd.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_165`)


Sonstiges (Gebühren, Spesen, etc.)  2.854,47     Verwaltungsaufwand gesamt  51.202,87   Der laufende Verwaltungsaufwand der Grießhaber Finanzen  GmbH & Co KG setzt sich im Jahr 2008 wie  folgt zusammen:     € Zahlung erfolgt  an  1  Gesellschaftsteuer ( 1 % von €  2.254.000,00)  22.540,00 Finanzamt für  die Treugeber  2 0,16 % Verwaltung der Einlagen pro Quartal €  4.252,80   10.819,20 Treuhand-  kommanditistin  3  GF-Vergütung pro Quartal € 3.000,00 12.000,00 Komplementärin    Sonstiges (Gebühren, Spesen, etc.)  0,00     Verwaltungsaufwand gesamt  45.359,20

**False Positives:**

- `Der laufende Verwaltungsaufwand der Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)
- `Finanzamt`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_168`)


Die Gesellschaftsteuer wird dem Treugeber  verrechnet und von der Gesellschaft (Komplementärin) als Steuerschuldner an das  Finanzamt abgeführt (vgl. Kapitalmarktprospekt Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co  KG Punkt 2.11).

**False Positives:**

- `Kapitalmarktprospekt Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co  KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_169`)


2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in  Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl.  Kapitalmarktprospekt Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co KG Punkt 2.14).

**False Positives:**

- `Kapitalmarktprospekt Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_171`)


Berechnung der anteilig geltend gemachten Sonderbetriebsausgaben 2008:   Richsteiger Marine Grießhaber Finanzen  GmbH & Co  KG  Initialisierungsaufwand gesamt € 385.410,00 € 326.830,00  Verwaltungsaufwand gesamt € 51.202,87  € 45.359,20  15 von 28 Seite 16 von 28

**False Positives:**

- `Richsteiger Marine Grießhaber Finanzen  GmbH & Co  KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_178`)


Der Kapitalmarktprospekt der Richsteiger Marine  wurde am 23. Juli 2008 und jener der Grießhaber Finanzen  GmbH & Co KG am 23. Jänner 2009 aufgelegt.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_198`)


2. Grießhaber Finanzen  GmbH & Co KG: Insgesamt wurden 126 private Anleger mit einer  Einlage im Betrag von gesamt € 2.254.000,00 angeworben.

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Grießhaber Finanzen`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_200`)


In den Erklärungen zur einheitlichen und gesonderten Gewinnfeststellung der Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft 2008 wurden den atypisch stillen Gesellschafterinnen folgende Verluste  zugewiesen:    Richsteiger Marine   €  Grießhaber Finanzen  GmbH & Co KG   €  1.520.000,00 838.138,16  17 von 28 Seite 18 von 28

**False Positives:**

- `Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Grießhaber Finanzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_207`)


Rechtliche Beurteilung  Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Richsteiger Marine  und der  Grießhaber Finanzen  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung einer  Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid  ergangen ist.

**False Positives:**

- `Rechtliche Beurteilung  Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Richsteiger Marine  und der  Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_238`)


Ist an einer Mitunternehmerschaft (I AG & atypische stille Gesellschaft) eine weitere  Mitunternehmerschaft (Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co KG) beteiligt, sind deren  Gesellschafter (natürliche und juristische Personen) Mitunternehmer der ersten  Mitunternehmerschaft (doppelstöckige Mitunternehmerschaft).

**False Positives:**

- `Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co KG` — partial — gold is substring of pred: `Richsteiger Marine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `I AG`(organisation)
- `Richsteiger Marine`(organisation)
- `Grießhaber Finanzen`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_80`)


Die Koppensteiner Schadenlogistik GmbH & Co KG ist keine gerichtlich beeidete  Sachverständige.

**False Positives:**

- `Die Koppensteiner Schadenlogistik GmbH & Co KG` — partial — gold is substring of pred: `Koppensteiner Schadenlogistik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Koppensteiner Schadenlogistik GmbH & Co KG`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_90`)


Durch den Sachverständigen M von der Koppensteiner Schadenslogistik  GmbH & Co KG wurde am Audi RS6 ein Totalschaden festgestellt. Inwiefern die in der  Beschwerde angeführten Fotos in der Lage wären, entgegen der Sachverständigenmeinung zu  einem anderen Ergebnis zu kommen, ist nicht nachvollziehbar.

**False Positives:**

- `Durch den Sachverständigen M von der Koppensteiner Schadenslogistik  GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Mit Erinnerung vom 6. Juni 2023 – zu Handen des Geschäftsführers XX – erfolgte unter  Androhung einer Zwangsstrafe von € 1.000,-- eine Aufforderung an die beschwerdeführende  GmbH & Co KG (Bf.), die Meldung der wirtschaftlichen Eigentümer gemäß § 5 WiEReG bis 28.  Juni 2023 nachzuholen (BFG-Akt AS 1).

**False Positives:**

- `Aufforderung an die beschwerdeführende  GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/145955.1`) (sent_id: `deanon_BFG_20260814_TEST/145955.1_5`)


Außerdem war er im Streitjahr 2004 u.a. an der FA Niederösterreich Mitte  GmbH & Co KG, St.nr.  07-776/8819, beteiligt.

**False Positives:**

- `FA Niederösterreich Mitte  GmbH & Co KG` — partial — gold is substring of pred: `FA Niederösterreich Mitte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Niederösterreich Mitte`(organisation)
- `07-776/8819`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/145955.1`) (sent_id: `deanon_BFG_20260814_TEST/145955.1_18`)


Der angefochtenen Einkommensteuer-Abänderungsbescheids für 2004 wurde u.a. von einer  am 1.6.2010 vom Finanzamt Klagenfurt erlassenen, als Feststellungs“bescheid“ gemäß § 188  BAO intendierte Erledigung vom 1.6.2010 betreffend die Finanzamt Niederösterreich Mitte  GmbH & Co KG, St.nr.  07-776/8819, abgeleitet, die ebenso rechtlich unwirksam war und sohin einen  „Nichtbescheid“ darstellte.

**False Positives:**

- `Finanzamt Niederösterreich Mitte  GmbH & Co KG` — partial — gold is substring of pred: `Finanzamt Niederösterreich Mitte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Klagenfurt`(organisation)
- `Finanzamt Niederösterreich Mitte`(organisation)
- `07-776/8819`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145955.1`) (sent_id: `deanon_BFG_20260814_TEST/145955.1_23`)


Festzuhalten ist, dass mit Beschluss vom 8.3.2017, GZ. RV/7102722/2013 das  Bundesfinanzgericht ausgesprochen hat, dass es sich bei der als Feststellungsbescheid gemäß  § 188 BAO intendierten Erledigung vom 2.4.2012 für das Jahr 2002 betreffend die FA Vorarlberg  AG & Mitges., St.nr. 53-058/7266  um einen „Nichtbescheid“ handelt.  Ebenso hat das Bundesfinanzgericht mit Beschluss vom 4.2.2019, GZ. RV/4100236/2012,  ausgesprochen, dass es sich bei der als Feststellungsbescheid gemäß § 188 BAO intendierten  Erledigung vom 1.6.2010 für das Jahr 2004 betreffend die Finanzamt Niederösterreich Mitte  GmbH & Co KG, St.nr.  07-776/8819  um einen „Nichtbescheid“ handelt.  Wird ein Änderungsbescheid gemäß § 295 Abs. 1 BAO erlassen (wie im vorliegenden Fall die  gemäß § 295 Abs. 1 BAO geänderten Einkommensteuerbescheide für 2002 und 2004 vom  30.11.2012), obwohl der hierfür herangezogene Grundlagenbescheid ins Leere gegangen ist  (hier: die als Feststellungs"bescheide" nach § 188 BAO intendierten Erledigungen der   Finanzämter, die beide „Nichtbescheide“ darstellen;

**False Positives:**

- `Finanzamt Niederösterreich Mitte  GmbH & Co KG` — partial — gold is substring of pred: `Finanzamt Niederösterreich Mitte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Vorarlberg`(organisation)
- `53-058/7266`(tax_number)
- `Finanzamt Niederösterreich Mitte`(organisation)
- `07-776/8819`(tax_number)

</details>

---

## `Company Suffix GmbH` 💣

**F1:** 0.007 | **Precision:** 0.085 | **Recall:** 0.004  

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
| 0.085 | 0.004 | 0.007 | 201 | 17 | 184 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 184 | 4582 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_11`)


Es handle sich dabei um die Firmen X. d.o.o. mit Sitz in L., die Furtder Technologien GmbH und die NEP Lebensmittel GmbH  Tatsächlich habe der Beschuldigte die jeweils Verantwortlichen auf den Baustellen kennengelernt, diese hätten nach Arbeit gefragt.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Missed by this rule (FN):**

- `NEP Lebensmittel GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_43`)


Entgegen den Ausführungen im Erkenntnis vom 05. Dezember 2018 konnte der Beschuldigte zu den drei betreffenden Firmen (X. d.o.o. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH  nicht die gleichen Unterlagen vorlegen, wie er es bei anderen Geschäftspartnern konnte.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Missed by this rule (FN):**

- `NEP Lebensmittel GmbH` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_97`)


So ergibt sich aus den vorgelegten Unterlagen, dass ich mir jeweils die Gewerbeberechtigungen der Subunternehmen ausfolgen ließ, im April 2012 (A-GmbH) bzw. im Jänner 2013 (B-GmbH) Firmenbuchauszüge eingeholt habe, bezüglich der Furtder Technologien GmbH am 06. Februar 2012 die Daten des Steuerkontos abgefragt habe und bezüglich der Furtder Technologien GmbH am 15.10.2011, 01.11.2011,15.02.2012, 15.03.2012 und 03.07 2012 sowie bezüglich der NEP Lebensmittel GmbH am 14.01.2013 und am 31.05.2013 Auszüge aus der HFU-Liste erstellt habe.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_99`)


Zu verweisen ist in diesem Zusammenhang auch noch darauf, dass die Furtder Technologien GmbH bereits im Jahr 2002 (und sohin bei Aufnahme der Geschäftstätigkeit 10 Jahre lang als werbendes Unternehmen existent!) und die NEP Lebensmittel GmbH im Frühjahr 2009 (und sohin bei Aufnahme der Geschäftstätigkeit auch bereits 4 Jahre lang als werbendes Unternehmen existiert) gegründet wurde.

| Predicted | Gold |
|---|---|
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Missed by this rule (FN):**

- `Furtder Technologien GmbH` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_103`)


Auftrag einen Leistungszeitraum auch noch nach dem 09. Oktober 2012 (bezeichnenderweise das Finanzamt Adresse3), bei der NEP Lebensmittel GmbH wurden nur 6 Rechnungen nach dem 30. August 2013 gelegt, drei davon noch im September 2013 (sohin innerhalb eines Monates), drei bis Mitte Oktober 2013 (sohin innerhalb von 6 Wochen).

| Predicted | Gold |
|---|---|
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_201`)


Nach den vorliegenden Beweisergebnissen konnten die Beschwerdeausführungen des Amtsbeauftragten zu den Eingangsrechnungen der Fa.NEP Lebensmittel GmbH, der Kisteler Telekom GmbH und der Fa. X. d.o.o aus Sicht des erkennenden Senates nicht dazu führen, den Nachweis einer Abgabenhinterziehung als erbracht anzusehen.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `Fa.NEP Lebensmittel GmbH` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_14`)


4.  Mit als Vorlageantrag gewertetem Schreiben vom 7. Oktober 2020 brachte der Beschwer- deführer vor, er habe für das Taxiunternehmen von BC, seit er bei der Kozlowska&Pfnier Medien GmbH angestellt sei,  nicht mehr gearbeitet.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_18`)


Das vom Beschwerdeführer  behauptete Anbringen, nämlich eine Beschwerde gegen den Bescheid über die  Wiederaufnahme des Verfahrens betreffend Umsatzsteuer für das Jahr 2006 der Gammersbach&Pelstring Telekom GmbH  vom 29.07.2009 wurde nicht erhoben und existiert daher nicht.

| Predicted | Gold |
|---|---|
| `Gammersbach&Pelstring Telekom GmbH` | `Gammersbach&Pelstring Telekom GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_342`)


2002 (bzw. jenes der Lemderwil Pflege GmbH im Mai 2003) beendet war, standen die Arbeiten beim Um-/Zubau des Wohnhauses  HNr 111 bis Herbst 2007 still.

| Predicted | Gold |
|---|---|
| `Lemderwil Pflege GmbH` | `Lemderwil Pflege GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_7`)


Am 19.04.2011 erging durch das Finanzamt ein Einkommensteuerbescheid in welchem dem Bf  ua Einkünfte aus nichtselbständiger Arbeit in der Höhe von gesamt EUR 50.057,02 der IEF  Service bzw. der IAF Service GmbH zugerechnet wurden.

| Predicted | Gold |
|---|---|
| `IAF Service GmbH` | `IAF Service GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_13`)


Mittels schriftlichem Ersuchen des Gerichts vom 25.08.2022 an die IEF Service GmbH wurden  dem Gericht die dem Insolvenz-Entgelt des Bf zugrundliegenden Bescheide übermittelt.   Die Zuerkennung der Leistungen aus dem IEF wurde aufgrund drei Teilbescheiden gewährt.

| Predicted | Gold |
|---|---|
| `IEF Service GmbH` | `IEF Service GmbH` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_45`)


Laut Firmenbuch — und vom Bf. unbe- stritten — sei er zum Zeitpunkt der Zustellung der Lenkererhebungen handelsrechtlicher Ge- schäftsführer der Gerdes Druck GmbH und als solcher zur Vertretung der Zulassungsbesitzerin nach außen  berufen gewesen.

| Predicted | Gold |
|---|---|
| `Gerdes Druck GmbH` | `Gerdes Druck GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_23`)


Hinsichtlich der Furtder Technologien GmbH und der NEP Lebensmittel GmbH habe der Beschuldigte durch seinen Verteidiger in der Spruchsenatsverhandlung durch Vorlage der Urkunden nachweisen können, dass er Firmenbuchauszug und HFU-Listen-Abfragen gemacht habe, sowie sich die Gewerbeberechtigung vorlegen habe lassen, die er in Kopie behalten habe.

**False Positives:**

- `Hinsichtlich der Furtder Technologien GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)
- `NEP Lebensmittel GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_62`)


------ Mit Vorhalt des Bundesfinanzgerichtes vom 9.4.2019 wurde der Beschuldigte  aufgefordert, die Mittelherkunft der behaupteter Weise von ihm in den Jahren 2012 und Seite 6 von 21 2013 geleisteten Barzahlungen an die Subfirmen X. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH anhand vorzulegender Kopien sämtlicher Kontenbewegungen oder anhand anderer geeigneter Unterlagen nachzuweisen bzw. glaubhaft zu machen.

**False Positives:**

- `Furtder Technologien GmbH und NEP Lebensmittel GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)
- `NEP Lebensmittel GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_97`)


So ergibt sich aus den vorgelegten Unterlagen, dass ich mir jeweils die Gewerbeberechtigungen der Subunternehmen ausfolgen ließ, im April 2012 (A-GmbH) bzw. im Jänner 2013 (B-GmbH) Firmenbuchauszüge eingeholt habe, bezüglich der Furtder Technologien GmbH am 06. Februar 2012 die Daten des Steuerkontos abgefragt habe und bezüglich der Furtder Technologien GmbH am 15.10.2011, 01.11.2011,15.02.2012, 15.03.2012 und 03.07 2012 sowie bezüglich der NEP Lebensmittel GmbH am 14.01.2013 und am 31.05.2013 Auszüge aus der HFU-Liste erstellt habe.

**False Positives:**

- `Daten des Steuerkontos abgefragt habe und bezüglich der Furtder Technologien GmbH` — similar text (different position): `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)
- `Furtder Technologien GmbH`(organisation)
- `NEP Lebensmittel GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_119`)


Zu den im Rahmen der Außenprüfung nicht zum Betriebsausgabenabzug anerkannten Eingangsrechnungen der Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH führte der Beschuldigte auf Befragung aus, er habe diese Firmen zwar am Beginn ihrer Tätigkeit dahingehend kontrolliert, dass er Firmenbuchauszug, Auszug aus dem Gewerberegister und der HFU- Liste sowie UID Nummern überprüft habe.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_122`)


Er könne somit auch keine Namen von Personen nennen, die namens der Firmen wie Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH tätig geworden seien und von ihm Aufträge in Empfang genommen hätten.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_157`)


Die geltend gemachten Rechnungen der Furtder Technologien GmbH sind daher nicht anzuerkennen.

**False Positives:**

- `Die geltend gemachten Rechnungen der Furtder Technologien GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_161`)


Die geltend gemachten Rechnungen wurden daher erst danach ausgestellt. Die NEP Lebensmittel GmbH ist darüber hinaus in den letzten Jahren immer wieder im Zuge von Außenprüfungen als Betrugsfirma in Erscheinung getreten.

**False Positives:**

- `Die NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_162`)


Die Rechnungen der NEP Lebensmittel GmbH sind daher nicht anzuerkennen.

**False Positives:**

- `Die Rechnungen der NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_171`)


Für das gegenständliche Verfahren ergibt sich aufgrund der Nichtanerkennung der Fremdleistungen der Firmen Furtder Technologien GmbH in Höhe von € 220.314,31 ein fiktiver Lohnaufwand von € 110.170,65.

**False Positives:**

- `Für das gegenständliche Verfahren ergibt sich aufgrund der Nichtanerkennung der Fremdleistungen der Firmen Furtder Technologien GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_173`)


Im Zuge der Betriebsprüfung wurden die Fremdleistungen der Firma NEP Lebensmittel GmbH im KJ 2013 nicht anerkannt.

**False Positives:**

- `Im Zuge der Betriebsprüfung wurden die Fremdleistungen der Firma NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_216`)


Anhaltspunkte oder Beweismittel dahingehend, dass der Beschuldigte mit den rechnungsausstellenden Personen der Firmen NEP Lebensmittel GmbH und der Kisteler Telekom GmbH zusammengewirkt, von diesen Scheinrechnungen, denen tatsächlich keine Leistungen der Subunternehmer zugrunde gelegen wären, erworben hätte und der Beschuldigten die hier in Rede stehenden Leistungen mit eigenen schwarz beschäftigten Arbeitnehmern erbracht hätte, liegen nicht vor.

**False Positives:**

- `Beschuldigte mit den rechnungsausstellenden Personen der Firmen NEP Lebensmittel GmbH und der Kisteler Telekom GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_21`)


Anfang 2010 war der Familienstreit endgültig geklärt und beigelegt und es kam auf Ebene der GmbH zu einem Eigentümerwechsel des 50% Eigentümers.

**False Positives:**

- `Familienstreit endgültig geklärt und beigelegt und es kam auf Ebene der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_14`)


Der Beschwerdeführer ist im Ausmaß von 38 Wochenstunden als Grundbildungspädagoge bei  der Veral-Maschinenbau GmbH im Projekt Basisbildung NÖ angestellt. In dieser Funktion vermittelt er den  Teilnehmenden (mit oft auch einer Teilleistungsschwäche), die das Pflichtschulalter  überschritten haben, Grundkompetenzen wie Schreiben und Rechtsschreibung, Lesen und  sinnerfassendes Lesen, Kenntnisse der Mathematik bis Hauptschulniveau, Umgang mit  digitalen Medien (Grundkenntnisse der Informationstechnologie).

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `Veral-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Veral-Maschinenbau GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_18`)


Es wurden EUR 200,00 an Vorsteuern im Zusammenhang mit der  vorgelegten Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 anstatt EUR 11.220,00 anerkannt.

**False Positives:**

- `Vorsteuern im Zusammenhang mit der  vorgelegten Rechnung der Kraußkopf Chemie GmbH` — partial — gold is substring of pred: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_126`)


Somit waren bereits im beschwerdegegenständlichen Zeitraum die materiellen  Voraussetzungen für die Entstehung des Vorsteuerabzuges erfüllt.  Deshalb und da die Anerkennung des Vorsteuerabzuges iHv EUR 200,00 aus der Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 unstrittig war, war spruchgemäß zu entscheiden.

**False Positives:**

- `Rechnung der Kraußkopf Chemie GmbH` — partial — gold is substring of pred: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_19`)


Diese Leasingfirma ist in Konkurs gegangen und aus diesem Grund hat mich die Fa.NiederImmobilien Institut GmbH im Oktober 2012 übernommen und bin seitdem Vollzeit mit 42,5 Stunden pro Woche  beschäftigt.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_152`)


c) Abfrage der Sozialversicherungs-Daten:  Demnach war der Bf ab 22.10.2012 – 16.4.2016 und ist seit 6.6.2016 laufend als Arbeiter bei  der Fa.NiederImmobilien Institut GmbH in B (Ö) als Arbeiter beschäftigt, Bruttogehalt 2014/2015 jährlich rund €  33.000.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_186`)


2. Berufliche/wirtschaftliche Nahebeziehung:  Fest steht nach dem Akteninhalt und bisher durchgeführten Erhebungen, dass der  Beschwerdeführer Sven Mitterhuber (Bf) ab 2009 im Inland berufstätig bzw. jedenfalls im strittigen  Zeitraum durchgehend bei der Fa.NiederImmobilien Institut GmbH in Vollzeit (42,5 Stunden/Woche) beschäftigt war  und laut Abfrage der Sozialversicherungsdaten nach wie vor ist.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sven Mitterhuber`(person)
- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_26`)


Als Leistungsempfänger der beschwerdegegenständlichen  Vermittlungsleistungen trat in den Streitjahren die unternehmerisch tätige Muttergesellschaft  M-AG und nicht die Tochtergesellschaft Zäsar u. Cankurt Analyse GmbH auf.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_33`)


L wird in Österreich durch die Zäsar u. Cankurt Analyse GmbH mit Sitz AdresseT-GmbH (im  Folgenden " T-GmbH" genannt) vertreten.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_48`)


Ist ein Gesellschafter einer GmbH nicht als Geschäftsführer, sondern in der GmbH in einer  anderen Funktion tätig, so kann seine persönliche Abhängigkeit - unter dem Aspekt seiner  rechtlichen Einflussmöglichkeiten auf die Geschäftsführung der GmbH aufgrund seiner  Beteiligungsrechte - erst dann verneint werden, wenn er kraft dieser Beteiligung die Ausübung  der dem Geschäftsführer als Vertreter der GmbH ihm als Beschäftigtem der GmbH gegenüber  zukommenden Weisungsmacht bestimmen oder verhindern kann.

**False Positives:**

- `Aspekt seiner  rechtlichen Einflussmöglichkeiten auf die Geschäftsführung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_27`)


Der Beirat hat die Geschäftsführung der GmbH zu überwachen und bei allen wichtigen  Angelegenheiten zu beraten.

**False Positives:**

- `Der Beirat hat die Geschäftsführung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nina Rasem`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_7`)


2. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im April 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die Gebrauchsabgabe  entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_9`)


3. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Mai 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die Gebrauchsabgabe  entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_11`)


4. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Juni 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die Gebrauchsabgabe  entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_13`)


5. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Juli 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die Gebrauchsabgabe  entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_15`)


6. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im August 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die Gebrauchsabgabe  2 von 6 Seite 3 von 6

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_18`)


7. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_20`)


8. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im April 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_22`)


9 sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Mai 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_24`)


10. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Juni 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_26`)


11. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im Juli 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_29`)


12. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im August 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, eine Baustofflagerung im Ausmaß von 64,00 m² vorgenommen gehabt, wobei  sie hiefür bis zum 16. November 2018 weder eine Gebrauchserlaubnis erwirkt, noch die  Gebrauchsabgabe entrichtet habe.

**False Positives:**

- `Wien als handelsrechtliche Geschäftsführerin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_5`)


Im Zuge eines Vorhalteverfahrens vor dem Finanzamt legte der Beschwerdeführer die  Familienstandsbescheinigung E 401 vom 13.06.2016, wonach er mit seiner Ehegattin und den  beiden Kindern in einem Haushalt in Land lebt, das Formular E 9, wonach seine Ehegattin im  Jahr 2015 Einkünfte in Höhe von 651.740 HUF (umgerechnet ca. 2072 €) erzielte, und einen  Mietvertrag zwischen der Vermieterin X GmbH und dem Mieter Name über die Wohnung in  Adr. vom 01.07.2013 bis 30.06.2016, vor.

**False Positives:**

- `Mietvertrag zwischen der Vermieterin X GmbH` — partial — gold is substring of pred: `X GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `X GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_18`)


Zu seinen  Aufgabengebieten zählen laut Schreiben der OCT Planung Gruppe GmbH vom 5.4.2013 folgende Tätigkeiten:  Anbahnung neuer Geschäftspartner, Herbeiführung von Geschäftsabschlüssen, Betreuung der  Lieferanten, Repräsentant der Firma bei Messen und Kongressen.

**False Positives:**

- `Zu seinen  Aufgabengebieten zählen laut Schreiben der OCT Planung Gruppe GmbH` — partial — gold is substring of pred: `OCT Planung Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OCT Planung Gruppe GmbH`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_6`)


2. Seitens des Finanzamtes erging ein mit 14.01.2013 datierter Schriftsatz an den Bf. betreffend  „Vorhalt im Haftungsverfahren“ bzw. „Heranziehung zur Haftung gemäß § 9  Bundesabgabenordung“ für Abgabenschuldigkeiten der NordGetränke GmbH  mit welchem dem Bf. nach  Anführung der auf dem Abgabenkonto der Gemeinschuldnerin ausgewiesenen  Abgabenschuldigkeiten (Umsatzsteuer 07/2011 und 08/2011, Lohnsteuer, Dienstgeberbeitrag  und Zuschlag zum Dienstgeberbeitrag 08/2011 und 09/2011, Dienstgeberbeitrag und Zuschlag  1 von 11 Seite 2 von 11

**False Positives:**

- `Abgabenschuldigkeiten der NordGetränke GmbH` — partial — gold is substring of pred: `NordGetränke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `NordGetränke GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_9`)


Seitens des Finanzamtes wurde ausgeführt, dass der Bf. in der Zeit ab 11.05.2007  Geschäftsführer der NordGetränke GmbH und somit deren gesetzlicher Vertreter gewesen sei.

**False Positives:**

- `Geschäftsführer der NordGetränke GmbH` — partial — gold is substring of pred: `NordGetränke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `NordGetränke GmbH`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_453`)


Die IT GmbH ist infolge Eröffnung des Konkursverfahrens aufgelöst.

**False Positives:**

- `Die IT GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_613`)


(Punkt 1.2): Die CMS GmbH ist eine Gesellschaft die sogenannte Managed-Hosting-Pakete  anbietet.

**False Positives:**

- `Die CMS GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_119`)


Hinsichtlich der Frage, ob die Vergütungen von einem Arbeitgeber oder für einen Arbeitgeber  gezahlt wurden, der nicht im anderen Staat ansässig war, ist festzuhalten, dass im  gegenständlichen Verfahren die Sachverhaltsermittlungen ergaben, dass die A Österreich  GmbH im Rahmen der Entsendung nach "Type A with D&C Country" zwar eine "Gebühr" an die  aufnehmende Gesellschaft verrechnet, aber ein Nachweis über deren Höhe bzw. dafür, dass  die auf die Tätigkeit in Deutschland entfallenden Kosten tatsächlich (allenfalls auch in Form  9 von 10 Seite 10 von 10

**False Positives:**

- `A Österreich  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_11`)


Bei einer Anhaltung durch die Finanzpolizei am 3.7.2012 wurde A (= Beschwerdeführer, Bf)  im Inland als Lenker des Fahrzeuges MarkeX mit dem italienischen Kennzeichen IT1, zugelassen  auf die Fa.Monal Bau Betriebe GmbH in I/Ort1, sowie an Fahrzeugdaten festgestellt: FIN Nr12, Kauf gebraucht,  Erstzulassung 14.12.2009, zugelassen auf Fa.Monal Bau Betriebe GmbH 23.11.2011, Diesel, 200 kW,  Kilometerstand bei Kauf 120.000 und derzeit 182.000, CO2-Wert 294 g/km.

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzpolizei`(organisation)
- `Fa.Monal Bau Betriebe GmbH`(organisation)
- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_25`)


Fahrzeugkauf und Service an die Fa.Monal Bau Betriebe GmbH zum     og.

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_55`)


Er sei Geschäftsführer  der Fa.Monal Bau Betriebe GmbH in I-Ort1, die im Inland eine Betriebsstätte habe.

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_58`)


Unabhängig von der Zulassung der Fahrzeuge auf die Fa.Monal Bau Betriebe GmbH  und auch deren Kostentragung (Service etc.) sei der Bf als Verwender und damit  Steuerschuldner anzusehen.

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_64`)


Zwecks  Erbringung des Gegenbeweises iSd § 82 Abs. 8 KFG seien die telepass-Abrechnungen der  "Autostrade per lÌtalia SPA" der Fa.Monal Bau Betriebe GmbH für alle Fahrzeuge des Unternehmens vorgelegt  worden.

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_73`)


- eine lückenlose Aufstellung der italienischen Monats-Mautabrechnungen für die      mehreren Fahrzeuge der Fa.Monal Bau Betriebe GmbH für den Zeitraum 29.7.2011 bis 18.4.2014,      wonach ua. für das Fahrzeug mit der telepass-Card Nr. 123xx in jedem Monat eine      Vielzahl von in Italien/Land2 durchgeführten wie auch über die Brennergrenze nach      oder von Österreich kommende Fahrten erfasst sind;

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_76`)


Daneben ist er ua. Geschäftsführer der Fa.Monal Bau Betriebe GmbH mit Sitz in Ort1/Italien (italien.  Firmenbuchauszug), die im Inland eine Betriebsstätte unterhält (inländ. Firmenbuchauszug).

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_131`)


Damit wären zunächst nach der vormals herrschenden Rechtsansicht sämtliche  Tatbestandsvoraussetzungen nach § 82 Abs. 8 KFG - dauernder Standort und Verwendung der  Fahrzeuge mit ausländischen Kennzeichen im Inland - erfüllt. Es läge demnach vorderhand eine  "widerrechtliche Verwendung" iSd § 1 Z 3 NoVAG und nach § 1 Abs. 1 Z 3 KfzStG vor, wobei  allerdings nach Ansicht des BFG noch abzuklären und zu beurteilen gewesen wäre, wer  überhaupt als "Verwender" bzw. Halter iSd § 5 Abs. 1 EKHG und damit als zutreffender  Abgabenschuldner – die Fa.Monal Bau Betriebe GmbH oder der Bf – in Betracht kommt (vgl. dazu:  OGH 18.12.2000, 9 Ob A 150/00z;

**False Positives:**

- `Monal Bau Betriebe GmbH` — partial — pred is substring of gold: `Fa.Monal Bau Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Monal Bau Betriebe GmbH`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_17`)


Im Vorlagebericht wies die belangte Behörde ergänzend darauf hin, die Bf. arbeitete vom  Jänner bis März 2018 für die WP GmbH und bezog ab März 2018 Wochengeld und ab Ende  April 2018 Kinderbetreuungsgeld.

**False Positives:**

- `WP GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Kaufvertrag  Mit Kaufvertrag vom 10./11./14./17.07.2017 erwarben der Beschwerdeführer (in der Folge  kurz: Bf) und Frau M von der Wachsmann u. Rönnepagel Marine GmbH (in der Folge kurz:Wachsmann u. Rönnepagel Marine GmbH  im Rahmen des  Baulandsicherungsmodells A die neu gebildeten Grundstücke 10/25, KG-S, sowie 322/3, KG-V,  je zur ideellen Hälfte.

**False Positives:**

- `Rönnepagel Marine GmbH` — similar text (different position): `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)
- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_24`)


Gemäß Punkt 9 des Treuhandvertrages vom 16.12.2015 zwischen Wachsmann u. Rönnepagel Marine GmbH und der  Marktgemeinde A ist festgehalten, dass in den Kaufverträgen dafür vorzusorgen ist, dass die  letztendlichen Käufer noch entstehende Gemeinkosten anteilig zu tragen haben.

**False Positives:**

- `Rönnepagel Marine GmbH` — partial — pred is substring of gold: `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_57`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Wachsmann u. Rönnepagel Marine GmbH ist eine Gesellschaft des Landes mit dem Geschäftszeig ‘Baulandsicherung‘ (siehe  Firmenbuch und www.salzburg.gv.at).

**False Positives:**

- `Rönnepagel Marine GmbH` — partial — pred is substring of gold: `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_62`)


In der Regel werden bei den Projekten der Wachsmann u. Rönnepagel Marine GmbH  die notwendigen Aufschließungsarbeiten von der S-GmbH durchgeführt (siehe  Anfragebeantwortung des Landeshauptmann-Stellvertreters Dr. Stöckl betreffend Tätigkeit der Wachsmann u. Rönnepagel Marine GmbH vom 25.03.2015, Nr. xxx der Beilagen zum stenographischen Protokoll des Salzburger  Landtages, 3. Session der 15. GP).

**False Positives:**

- `Rönnepagel Marine GmbH` — similar text (different position): `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)
- `Dr. Stöckl`(person)
- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_64`)


Aus dem Protokoll der Gemeindevertretungssitzung der Marktgemeinde A am 23.06.2015  betreffend Abänderung des Flächenwidmungsplanes und Umwidmung von Teilstücken in  Zusammenhang mit dem geplanten Baulandsicherungsmodell geht hervor, dass die  Kaufabwicklung über die Wachsmann u. Rönnepagel Marine GmbH bereits vorbereitet und eine weitere Besprechung mit der Wachsmann u. Rönnepagel Marine GmbH und der S-GmbH stattfinden wird.

**False Positives:**

- `Rönnepagel Marine GmbH` — similar text (different position): `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)
- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_65`)


Am 16.12.2015 hat die Wachsmann u. Rönnepagel Marine GmbH mit der Gemeinde einen Treuhandvertrag über die Flächen des  Baulandsicherungsmodells abgeschlossen.

**False Positives:**

- `Rönnepagel Marine GmbH` — partial — pred is substring of gold: `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_105`)


Die angefallenen Ankaufs- und Nebenkosten sollten auf die Käufer  überwälzt werden (siehe § 9 des Treuhandvertrages zwischen Wachsmann u. Rönnepagel Marine GmbH und Gemeinde).

**False Positives:**

- `Rönnepagel Marine GmbH` — partial — pred is substring of gold: `Wachsmann u. Rönnepagel Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wachsmann u. Rönnepagel Marine GmbH`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_27`)


Die Behauptung, bei Kaufvertragsabschluss wäre bereits eine vertragliche Bindung bestanden,  ein Haus bei der Firma MH-Bau GmbH zu erwerben bzw. von dieser Firma errichten zu lassen,  ist nicht nachvollziehbar.

**False Positives:**

- `Bau GmbH` — partial — pred is substring of gold: `MH-Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)


Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  MH-Bau GmbH am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

**False Positives:**

- `Bau GmbH` — partial — pred is substring of gold: `MH-Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_70`)


Der Verkauf der Doppelwohnhäuser in A/L wurde von der MH-Bau GmbH und der MH-Immo  GmbH beworben.

**False Positives:**

- `Bau GmbH` — partial — pred is substring of gold: `MH-Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MH-Bau GmbH`(organisation)
- `MH-Immo  GmbH`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_74`)


Der  Verkauf der Doppelhaushälften (“Doppelhausanlage A/L“) wurde von der MH-Bau GmbH und  der MH-Immo GmbH beworben.

**False Positives:**

- `Bau GmbH` — partial — pred is substring of gold: `MH-Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MH-Bau GmbH`(organisation)
- `MH-Immo GmbH`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_124`)


Der von der Bauführerin der MH- Bau GmbH für die Käufer am 24.02.2016 erstellte Austauschplan - und zwar nur für die  Wohneinheit TOP 16, also die Hälfte des Doppelhauses - kann daher nur geringfügige  Änderungen im Sinne der oben dargestellten Rechtsprechung betroffen haben, da die  Gesamtkonstruktion des Doppelhauses unverändert übernommen wurde.

**False Positives:**

- `Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_39`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. war im Streitjahr 2014 beim österreichischen Unternehmen PGZO Lebensmittel Betriebe GmbH  mit Sitz in  Leopoldsdorf nichtselbständig beschäftigt und übte seine Tätigkeit auf diversen Baustellen in  Wien und in ganz Österreich aus.

**False Positives:**

- `Unternehmen PGZO Lebensmittel Betriebe GmbH` — partial — gold is substring of pred: `PGZO Lebensmittel Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PGZO Lebensmittel Betriebe GmbH`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_12`)


Eine Beschwerde hinsichtlich des Bescheides über die Wiederaufnahme des Verfahrens  hinsichtlich der Umsatzsteuer für das Jahr 2006 (Bescheid vom 29.08.2007) gemäß  § 303 Abs. 4 BAO der Gammersbach&Pelstring Telekom GmbH vom 29.07.2009 wurde nicht erhoben.

**False Positives:**

- `BAO der Gammersbach&Pelstring Telekom GmbH` — partial — gold is substring of pred: `Gammersbach&Pelstring Telekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gammersbach&Pelstring Telekom GmbH`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_33`)


 Ab dem 18. Jänner 2021 besucht [Name Kind 1], Sohn der Beschwerdeführerin eine  Ausbildung zum Elektrotechniker im Rahmen des [Ausbildungsstelle 1] (Bestätigung  Kursbesuch Lehrabschluss der [Ausbildungsstelle 1] Gemeinnützigen GmbH vom  18. Jänner 2021).

**False Positives:**

- `Gemeinnützigen GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_71`)


Da die Gesellschafter zwei Funktionen auszuüben hatten, nämlich die Geschäfte der  Fitnessstudio GmbH zu organisieren als auch ihrer physiotherapeutischen Tätigkeit  nachzukommen und die beiden Geschäftsbereiche miteinander zu verschränken und im  positiven Sinne „anzustecken“ war es eine logische Konsequenz als Physiotherapeut keine Miete  für die Benutzung der Räumlichkeiten zu bezahlen dafür aber die Geschäftsführungstätigkeit  der GmbH unentgeltlich auszuüben.

**False Positives:**

- `Geschäfte der  Fitnessstudio GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_85`)


An Kosten sind folgende Positionen bei der GmbH angefallen:  • Mietaufwendungen an die F und D OG  • Personalaufwand für die Empfangsassistentin, die zum Teil die Termine koordiniert hat

**False Positives:**

- `An Kosten sind folgende Positionen bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_327`)


Unter diesen Umständen geht das BFG davon aus, dass sich die Leistungsmängel der A/B-Bau  GmbH auf den Eingangsbereich der Garagendecke beschränkten.

**False Positives:**

- `Bau  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_338`)


Die amtswegige Löschung erfolgte zwei Jahre nach „Gründung“ der A Bau GmbH  am 23.Juli 2003.

**False Positives:**

- `A Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_400`)


Das BFG geht  davon aus, dass diese Planversion auch einem im anhängigen finanzgerichtlichen  Ermittlungsverfahren vom steuerlichen Vertreter des Bf vorgelegten Deckblatt zu einem Plan  der IS Ingenieurbüro D GmbH vom 21.

**False Positives:**

- `Planversion auch einem im anhängigen finanzgerichtlichen  Ermittlungsverfahren vom steuerlichen Vertreter des Bf vorgelegten Deckblatt zu einem Plan  der IS Ingenieurbüro D GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1173`)


Da die Firmenbucheintragung jener grundlegenden Änderungen der Gesellschaftsverhältnisse,  durch welche die Befugnis der A Bau GmbH zur Ausführung eines Bauauftrages für den Bf  entstand, erst am Tag der Bauverhandlung erfolgte, ist erwiesen, dass der Bf entweder das  Firmenbuch nicht konsultierte oder den Auftrag im Wissen um die fehlende Befugnis des  Unternehmens erteilte.

**False Positives:**

- `Befugnis der A Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_7`)


Angemerkt wird, dass auf der Homepage des im vorigen Absatz erwähnten Unternehmens u.a.  wörtlich wie folgte ausgeführt wurde: „Die DonauLogistik GmbH ist exklusiver Arbeitskräfteüberlasser in der  1 von 12 Seite 2 von 12

**False Positives:**

- `Die DonauLogistik GmbH` — partial — gold is substring of pred: `DonauLogistik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DonauLogistik GmbH`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_8`)


Dagegen erhob der Bf am 23.05.2011  fristgerecht Berufung (nunmehr Beschwerde) und begehrte die Versteuerung der Lohnzettel  IEF Service GmbH und IAF Service GmbH mit steuerpflichtigen Bezügen von EUR 13.219,66 und  1 von 7 Seite 2 von 7

**False Positives:**

- `Versteuerung der Lohnzettel  IEF Service GmbH und IAF Service GmbH` — partial — gold is substring of pred: `IEF Service GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IEF Service GmbH`(organisation)
- `IAF Service GmbH`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_25`)


Von der IAF Service GmbH wurde ein Lohnzettel gem. § 69 Abs 6 EStG 1988 in Höhe von EUR  36.837,36 sowie von der nunmehrigen IEF Service GmbH ein weiterer Lohnzettel in Höhe von  EUR 13.219,66 an das Finanzamt übermittelt.  Beide Beträge wurden vom belangten Finanzamt der Einkommensteuer 2009 zu Grunde  gelegt.

**False Positives:**

- `Von der IAF Service GmbH` — partial — gold is substring of pred: `IAF Service GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IAF Service GmbH`(organisation)
- `IEF Service GmbH`(organisation)
- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_35`)


Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus den vorgelegten Aktenteilen des Finanzamtes und  des Beschwerdeführers sowie aus den von der IEF Service GmbH zum Akt genommenen neuen  Jahreslohnzetteln 2009 und 2010.

**False Positives:**

- `Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus den vorgelegten Aktenteilen des Finanzamtes und  des Beschwerdeführers sowie aus den von der IEF Service GmbH` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `IEF Service GmbH`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_59`)


Für die gegenständliche Beschwerde bedeutet dies, dass unbestrittener Weise – den  Beschwerdezeitraum 2009 betreffend - Insolvenz-Entgelt von der IEF Service GmbH in der  Höhe von EUR 43.618,25,- zur Auszahlung gelangte.

**False Positives:**

- `Entgelt von der IEF Service GmbH` — partial — gold is substring of pred: `IEF Service GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IEF Service GmbH`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_6`)


Gemäß § 9 Abs. 7 VStG haftet die Gerdes Druck GmbH für die mit diesem Bescheid über den zur  Vertretung nach außen Berufenen, HR Tiffany Vacha  Kabic verhängte Geldstrafe von 240,00 €, die  Verfahrenskosten der belangten Behörde in Höhe von 40,00 € und für den Beiträgen zu den  Kosten des Beschwerdeverfahrens von 48,00 € sowie für sonstige in Geld bemessene  Unrechtsfolgen, zur ungeteilten Hand.

**False Positives:**

- `VStG haftet die Gerdes Druck GmbH` — partial — gold is substring of pred: `Gerdes Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerdes Druck GmbH`(organisation)
- `HR Tiffany Vacha`(person)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_65`)


Das Bundesfinanzgericht hat erwogen:  I. Sachverhalt:  Die – steuerlich vertretene - Bf, geb. im Juli 1938, ist österreichische Staatsbürgerin und war bis  Juli 1994 Dienstnehmerin der XY Österreich GmbH in Wien.

**False Positives:**

- `Dienstnehmerin der XY Österreich GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_68`)


Neben den österreichischen Pensionsbezügen erhält die Bf aufgrund einer 7jährigen  Auslandstätigkeit für den XY Konzern seit August 1998 auch eine Sozialversicherungsrente der  „Deutsche Rentenversicherung Bund“ (nachfolgend SV-Rente) und - aufgrund einer  Direktzusage des ehemaligen Dienstgebers in Deutschland - eine Betriebsrente der Tal Waldvalver Gruppe GmbH   Die Betriebsrente der Tal Waldvalver Gruppe GmbH wurde ursprünglich zum Teil ohne  Rechtsanspruch gewährt.

**False Positives:**

- `Betriebsrente der Tal Waldvalver Gruppe GmbH   Die Betriebsrente der Tal Waldvalver Gruppe GmbH` — partial — gold is substring of pred: `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Deutsche Rentenversicherung Bund`(organisation)
- `Tal Waldvalver Gruppe GmbH`(organisation)
- `Tal Waldvalver Gruppe GmbH`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_143`)


Dies  betrifft, neben Angaben/Unterlagen zu ihrem Wohnsitz bzw. ihren Lebensverhältnissen in  Nürnberg, insbesondere Teile der Rechtsgrundlage für die Betriebsrente der Tal Waldvalver Gruppe GmbH (Regelungen zur Ansparphase sowie zur Auszahlung durch die Claaß E‑Commerce GmbH  und die  Rechtsgrundlagen zu ihrem Rentenanspruch gegen den XY Pensionsfonds (Vereinbarungen der Tal Waldvalver Gruppe GmbH mit dem Konzernbetriebsrat bzw. der XY Deutschland  Pensionsfonds AG).

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Claaß E‑Commerce GmbH`
- `Vereinbarungen der Tal Waldvalver Gruppe GmbH` — similar text (different position): `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Tal Waldvalver Gruppe GmbH`(organisation)
- `Claaß E‑Commerce GmbH`(organisation)
- `Tal Waldvalver Gruppe GmbH`(organisation)
- `XY Deutschland  Pensionsfonds AG`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_151`)


Eine Übertragung der Verpflichtung auf oder Auszahlung im Wege einer Claaß E‑Commerce GmbH ist in der  vorgelegten Betriebsvereinbarung nicht erwähnt.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Claaß E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Claaß E‑Commerce GmbH`(organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_169`)


Die Auszahlung des auf den XY Pensionsfonds übertragenen  Rententeiles erfolgt als Bruttorente ohne Abzug von Lohnsteuer, Solidaritätszuschlag und ggfs  Kirchensteuer, wenn auch weiterhin gemeinsam mit dem beim Dienstgeber verbliebenen  Rententeil im Wege des Lohnverrechnungsservice der Tal Waldvalver Gruppe GmbH  Sofern bis 2010  eine Abfuhr von Beiträgen zur Kranken- und Pflegeversicherung der Rentner erfolgte, wird  diese auch für den auf den XY Pensionsfonds übertragenen Rententeil fortgeführt (Mitteilung  der Tal Waldvalver Gruppe GmbH an die Bf v. 10.Dez.2010).

**False Positives:**

- `Mitteilung  der Tal Waldvalver Gruppe GmbH` — similar text (different position): `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tal Waldvalver Gruppe GmbH`(organisation)
- `Tal Waldvalver Gruppe GmbH`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_175`)


Seit 2011 enthalten die monatlichen Rentenüberweisungen des  Personalverrechnungsservice der Tal Waldvalver Gruppe GmbH anstelle der Leistungen der Claaß E‑Commerce GmbH die Bezugsteile des XY Pensionsfonds als Bruttorente.

**False Positives:**

- `Rentenüberweisungen des  Personalverrechnungsservice der Tal Waldvalver Gruppe GmbH` — partial — gold is substring of pred: `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tal Waldvalver Gruppe GmbH`(organisation)
- `Claaß E‑Commerce GmbH`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_272`)


Auch die vom Finanzamt  Nürnberg-Süd übermittelten Lohnsteuerbescheinigungen der Tal Waldvalver Gruppe GmbH und jene  zur SV-Renten der Bf weisen keine Aufwendungen iSd österreichischen  Werbungskostenbegriffs aus.

**False Positives:**

- `Süd übermittelten Lohnsteuerbescheinigungen der Tal Waldvalver Gruppe GmbH` — partial — gold is substring of pred: `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Tal Waldvalver Gruppe GmbH`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_333`)


Mangels Vorlage einer Rechtsgrundlage zur Unterstützungskasse der Tal Waldvalver Gruppe GmbH  und gegenteiliger Regelungen zur Ansparphase in der vorgelegten Betriebsvereinbarung vom  Dez.

**False Positives:**

- `Mangels Vorlage einer Rechtsgrundlage zur Unterstützungskasse der Tal Waldvalver Gruppe GmbH` — partial — gold is substring of pred: `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tal Waldvalver Gruppe GmbH`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_379`)


Wie festgestellt, werden sowohl die deutsche SV-Rente als auch die Betriebsrente der Tal Waldvalver Gruppe GmbH und die Rente des XY Pensionsfonds monatlich ausbezahlt. Dass die  Rechtgrundlagen dieser Rentenbezüge Sonderzahlungen iSd § 67 EStG vorsehen, hat das  Ermittlungsverfahren nicht hervorgebracht.

**False Positives:**

- `Rente als auch die Betriebsrente der Tal Waldvalver Gruppe GmbH` — partial — gold is substring of pred: `Tal Waldvalver Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tal Waldvalver Gruppe GmbH`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_69`)


Gesellschafter der Jeanne Kraenzlin  Vermietungs- & Verpachtungs GmbH ist der Bf. (100 %).

**False Positives:**

- `Verpachtungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeanne Kraenzlin`(person)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_94`)


Der von der steuerlichen Vertretung abgegebene Rechtsmittelverzicht steht  sachverhaltsmäßig mit der vorgenommenen Betriebsprüfung bei der Touristik Werkvalbach GmbH im  Zusammenhang und ergibt sich auch aus der über den Rechtsmittelverzicht aufgenommenen  6 von 11 Seite 7 von 11

**False Positives:**

- `Der von der steuerlichen Vertretung abgegebene Rechtsmittelverzicht steht  sachverhaltsmäßig mit der vorgenommenen Betriebsprüfung bei der Touristik Werkvalbach GmbH` — partial — gold is substring of pred: `Touristik Werkvalbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Touristik Werkvalbach GmbH`(organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_3`)


Begründung  Bereits mit Haftungsbescheid vom 23. März 2022 hatte das Finanzamt den ehemaligen  Geschäftsführer Evamaria Watenphul  als Haftungspflichtigen für aushaftende Abgabenschuldigkeiten der  Özyilmaz Recycling GmbH  in Anspruch genommen.

**False Positives:**

- `Finanzamt den ehemaligen  Geschäftsführer Evamaria Watenphul  als Haftungspflichtigen für aushaftende Abgabenschuldigkeiten der  Özyilmaz Recycling GmbH` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH`(organisation)

</details>

---

## `Company Suffix AG` 💣

**F1:** 0.000 | **Precision:** 0.029 | **Recall:** 0.000  

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
| 0.029 | 0.000 | 0.000 | 35 | 1 | 34 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 34 | 4598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_158`)


Im Dez 2010 wurde die XY Deutschland Pensionsfonds AG zur „Auslagerung der  Versorgungszusagen“ gegründet.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_23`)


Mit Übergabevertrag vom 12. Juli 2012 habe der Bf. die Wohnung wiederum seinem Sohn zu  einem Übergabepreis in Höhe der per 26. Juni 2012 offenen Kreditforderung der Bank AG mit  einem offenen Saldo von EUR 110.461,17 übergeben.

**False Positives:**

- `Kreditforderung der Bank AG` — partial — gold is substring of pred: `Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bank AG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_89`)


Der Übernehmer erklärt ferner in Kenntnis  des zwischen der Bank AG und dem Übergeber bestehenden Kreditvertrages zu sein und  verpflichtet sich ausdrücklich, in sämtliche Rechte und Pflichten aus dem Kreditvertrag  einzutreten.“

**False Positives:**

- `Der Übernehmer erklärt ferner in Kenntnis  des zwischen der Bank AG` — partial — gold is substring of pred: `Bank AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bank AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_32`)


Sie sind bereits seit November 2012 bei der Firma AG in A-P beschäftigt.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

**False Positives:**

- `Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG` — partial — gold is substring of pred: `Magistrats der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der  Stadt Wien`(organisation)
- `UniCredit Bank Austria AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_16`)


Ergänzend sei darauf hingewiesen, dass der Beschwerdeführer niemals Umsatzsteuer  ausgewiesen habe bzw. die Gutschriftsabrechnungen der L Schweiz AG immer ohne  (österreichische) Umsatzsteuer erstellt habe.

**False Positives:**

- `Gutschriftsabrechnungen der L Schweiz AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

**False Positives:**

- `Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG` — partial — gold is substring of pred: `Magistrats der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der  Stadt Wien`(organisation)
- `UniCredit Bank Austria AG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_30`)


Dabei muss bei der Übergabe insbesondere die Tankstelle der OMV AG zur  Gänze entfernt und deren Betriebsanlage aufgelassen sein.

**False Positives:**

- `Dabei muss bei der Übergabe insbesondere die Tankstelle der OMV AG` — partial — gold is substring of pred: `OMV AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMV AG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_28`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  3 von 5 Seite 4 von 5

**False Positives:**

- `Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG` — partial — gold is substring of pred: `Magistrats der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der  Stadt Wien`(organisation)
- `UniCredit Bank Austria AG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_171`)


Und darüber hinaus, dass sämtliche  Fehler mit dem AG zu behandeln und die geeigneten Maßnahmen gemeinsam festzulegen  seien.

**False Positives:**

- `Fehler mit dem AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_175`)


Diese waren  ihrerseits den Weisungen der BF unterstellt und bildeten ein Bindeglied zwischen dem AG  und den Arbeitern der AN, was schon die sprachliche Verständigung erforderte.

**False Positives:**

- `Diese waren  ihrerseits den Weisungen der BF unterstellt und bildeten ein Bindeglied zwischen dem AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_263`)


Die Beistellung für die Arbeiten erforderlichen Werkstatträume, sowie Aufenthalts- Garderoben und Waschräume seitens AG ist kostenlos.

**False Positives:**

- `Garderoben und Waschräume seitens AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_296`)


 Sämtliche Fehler unabhängig des Ursprungs sind mit dem AG zu behandeln und die  geeigneten Maßnahmen gemeinsam festzulegen.

**False Positives:**

- `Sämtliche Fehler unabhängig des Ursprungs sind mit dem AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_306`)


Die Beistellung von Grundmaterial, Kraftstoff mit Anschlüssen, Beleuchtung, Gas,  Sauerstoff, Wasser sowie Hebezeugen seitens AG ist kostenlos.

**False Positives:**

- `Wasser sowie Hebezeugen seitens AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_338`)


 Sämtliche Fehler unabhängig des Ursprung sind mit dem AG zu behandeln und die  geeigneten Maßnahmen gemeinsam festzulegen über sämtliche Fehler oder  Probleme ist ein schriftliches Protokoll zu führen, welches dem Fehler beschreibt  und die Folgemaßnahmen festhält   …   Abnahme:  Nach Beendigung der Arbeiten "  Betreffend die konkrete Leistungsbeschreibung wird auf bestimmt bezeichnete  Rohrleitungen hingewiesen.

**False Positives:**

- `Sämtliche Fehler unabhängig des Ursprung sind mit dem AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_37`)


Die Feststellungen zur Schlafstelle in  Schwechat gründen sich auf die diesbezügliche Bestätigung der Bachtra-Immobilien AG  vom 28.11.2017.

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Bachtra-Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachtra-Immobilien AG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_12`)


Dass die Arbeitnehmerveranlagung 2021 am Tag ihrer Unterfertigung beim Postamt in  Feldkirchen aufgegeben wurde, geht aus der vom Bf. übermittelten Rechnungskopie  (Rechnungsnummer 50550020200918) der Österreichischen Post AG vom 28.02.2022 hervor;

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen Post AG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_10`)


Die gegenständlichen Verfahrenskosten stünden im  Zusammenhang mit der Tätigkeit der Bf. als einer der beiden Vorstände der Firma AG und  seien somit betrieblich veranlasst.

**False Positives:**

- `Vorstände der Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_42`)


Das Bundesfinanzgericht hat erwogen:  Die Bf. war vom 30. Dezember 1988 bis zum 28. April 2011 Vorsitzende des Vorstandes der AG  für den Bereich Technik und Produktion.

**False Positives:**

- `Vorsitzende des Vorstandes der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_74`)


In Österreich erfolgten für die Bf ab 1994 Pflichtveranlagungen nach § 41 Abs. 1 Z 2 EStG unter  Einbeziehungen der Bezüge der XY Pensionskasse AG in Wien und Abzug von Sonderausgaben  für Personenversicherungen in Höhe des so genannten „Topf-Sonderausgaben“- Höchstbetrages.

**False Positives:**

- `EStG unter  Einbeziehungen der Bezüge der XY Pensionskasse AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_289`)


6. Das FA bezog in den angefochtenen Bescheiden – ohne Sachverhaltsermittlung - die Rente  der XY Deutschland Pensionsfonds AG in Hinblick auf § 25 (1) Z 2 lit b Satz 2 EStG 1988 nur im  Ausmaß von 25% der Bruttobezüge in die Besteuerung ein.

**False Positives:**

- `Rente  der XY Deutschland Pensionsfonds AG` — partial — gold is substring of pred: `XY Deutschland Pensionsfonds AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XY Deutschland Pensionsfonds AG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_24`)


Im Anlassfall wurde Wohnraum begünstigt an viele Dienstnehmer zur Verfügung gestellt,  weshalb zu untersuchen war, ob dies einen geldwerten Vorteil darstellt. Die unentgeltliche  Zurverfügungstellung einer Dienstwohnung stellt nur dann keinen geldwerten Vorteil dar, wenn  der AN sie ausschließlich im Interesse des AG in Anspruch nimmt und seine bisherige Wohnung  beibehält (VwGH 19.

**False Positives:**

- `AN sie ausschließlich im Interesse des AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_66`)


Wenn nunmehr das BFG – obwohl weder von der  belangten Behörde noch von der Beschwerdeführerin beanstandet – die Rechtsmeinung  vertritt, dass der Vorsteuerabzug aus den Eingangsrechnungen von Wien Consud AG zu verneinen sei und  insoweit eine Verböserung vornimmt, ist seitens der Beschwerdeführerin beabsichtigt, den  Instanzenzug zu beschreiten, und zwar aus folgenden Gründen:  Anders als in ihrer Email angeführt ist der Entscheidung des VwGH an keiner Stelle zu  5 von 18 Seite 6 von 18

**False Positives:**

- `Vorsteuerabzug aus den Eingangsrechnungen von Wien Consud AG` — partial — gold is substring of pred: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_67`)


entnehmen, dass die Rechtsansicht, wonach der Vorsteuerabzug aus den Eingangsrechnungen  von Wien Consud AG zu versagen sei, geteilt wird.

**False Positives:**

- `Vorsteuerabzug aus den Eingangsrechnungen  von Wien Consud AG` — partial — gold is substring of pred: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_68`)


Auch hat der VwGH oder der EuGH bisher zu einem wie  dem hier vorliegenden Sachverhalt, bei dem einerseits eine innergemeinschaftliche Lieferung  aufgrund der Mitteilung einer inländischen UID-Nummer als steuerpflichtig behandelt wurde  (bzw. werden musste) und andererseits ein fiktiver ig Erwerb vorgeschrieben wurde, nicht  explizit zur Frage des Vorsteuerabzuges für die als steuerpflichtig behandelte Lieferung  geurteilt, sodass genau zu dieser Frage einschlägige Rechtsprechung durch den VwGH und  EuGH fehlt. Denn auch wenn es sich bei den Lieferungen von Wien Consud AG (A) um  innergemeinschaftliche Lieferungen handelt, die bei Vorliegen aller Voraussetzungen  grundsätzlich hätten steuerbefreit sein können, bedeutet dies nicht, dass diese im konkreten  auch steuerbefreit waren und somit zu Unrecht österreichische Umsatzsteuer von Wien Consud AG in  Rechnung gestellt wurde, für die kein Recht auf Vorsteuerabzug besteht.

**False Positives:**

- `Unrecht österreichische Umsatzsteuer von Wien Consud AG` — similar text (different position): `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)
- `Wien Consud AG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_41`)


Aus den niederschriftlichen Aussagen des Vorstandes der Gablonsky&Rethlefsen Gastronomie AG ist klar erkennbar, dass es  zentrale Strategie sämtlicher Beteiligungsmodelle AbisJ ist, sich an solchen  Zielkapitalgesellschaften zu beteiligen, die im Jahr der Beteiligung Verlustzuweisungen in Höhe  von nahezu 200 % der atypisch stillen Einlage an AbisJ garantieren können, ja, dass das  Eingehen einer Beteiligung durch AbisJ an einer Zielgesellschaft von einer vorrangigen  Verlustzuweisung in der von den Modellinitiatoren geforderten Höhe abhängig gemacht wird.

**False Positives:**

- `Aus den niederschriftlichen Aussagen des Vorstandes der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_52`)


Die an AbisJ zugewiesenen Verluste aus der atypisch stillen Beteiligung an Gablonsky&Rethlefsen Gastronomie AG sind daher gem.  § 2 Abs. 2a EStG 1988 nicht ausgleichs- und vortragsfähig.

**False Positives:**

- `Die an AbisJ zugewiesenen Verluste aus der atypisch stillen Beteiligung an Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_69`)


Zentrales Element der Verhandlungen im Zuge des Abschlusses der atypisch stillen Beteiligung  sei die Wertbestimmung der Gablonsky&Rethlefsen Gastronomie AG und damit das Beteiligungsverhältnis der Investoren  gewesen.

**False Positives:**

- `Zentrales Element der Verhandlungen im Zuge des Abschlusses der atypisch stillen Beteiligung  sei die Wertbestimmung der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_95`)


Die Gablonsky&Rethlefsen Gastronomie AG ist eine kleine Aktiengesellschaft im Sinne des § 221 UGB und hat ihren Sitz in Ort4, BL.

**False Positives:**

- `Die Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_115`)


Anzumerken ist, dass bezogen auf die tatsächlich geleistete Einlage von gesamt € 800.000,00  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG in Höhe von €  65.845.751,50 zum Stichtag des Zusammenschlusses – die Beteiligungsquote 1,2003 % beträgt.

**False Positives:**

- `Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_120`)


Laut § 1 des Vertrages stellt die Bf. als atypisch stille Gesellschafterin und Beteiligungsgeberin  eine Einlage, welche dem wirtschaftlichen Eigenkapital der Gablonsky&Rethlefsen Gastronomie AG zugerechnet wird, von  zumindest € 400.000,00 bis zu € 925.000,00 zur Verfügung.

**False Positives:**

- `Eigenkapital der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_127`)


Sie ergibt sich  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG in Höhe von €  67.593.518,50 zum Stichtag des Zusammenschlusses, bezogen auf eine Einlage von €  10 von 28 Seite 11 von 28

**False Positives:**

- `Sie ergibt sich  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_243`)


Der Gewinn und Verlust der Mitunternehmerschaft wird somit gem. § 188 BAO einheitlich und  gesondert festgestellt. In diesem Feststellungsbescheid wird der steuerliche Gewinn bzw.  Verlust auf die AG und die stillen Mitunternehmer aufgeteilt. Die Mitunternehmerschaft ist  hierbei Subjekt der Einkunftserzielung.

**False Positives:**

- `Verlust auf die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_247`)


Sonderbetriebsausgaben  In einem zweiten Schritt wird sodann der Gewinn oder der Verlust der einzelnen  Mitunternehmer ermittelt:   Strittig ist, ob ein anteiliger Abzug der Sonderbetriebsaufwendungen –  „Modellentwicklungskosten“ als Sonderbetriebsausgaben im Rahmen der einheitlichen und  gesonderten Gewinnfeststellung der Gablonsky&Rethlefsen Gastronomie AG und atypisch stillen Gesellschaft, möglich ist.

**False Positives:**

- `Sonderbetriebsausgaben im Rahmen der einheitlichen und  gesonderten Gewinnfeststellung der Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_168`)


23 Das BFG hat im angefochtenen Erkenntnis die Feststellung getroffen, die Geschäfte, die von  der Revisionswerberin und der E GmbH in den Jahren 1987 bis 1997 mit den Schweizer  Gesellschaften Dorfderlem-Solar AG und Sudlem-Chemie AG abgewickelt worden sind, seien von einer umfassenden  Außenprüfung im Februar 1999 als Scheingeschäfte qualifiziert worden.

**False Positives:**

- `Solar AG` — partial — pred is substring of gold: `Dorfderlem-Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfderlem-Solar AG`(organisation)
- `Sudlem-Chemie AG`(organisation)

</details>

---

## `Administrative Court Vienna` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 4599 |

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
| `organisation` | 0 | 0 | 4599 |

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
| `organisation` | 0 | 0 | 4599 |

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
| `organisation` | 0 | 0 | 4599 |

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
| `organisation` | 0 | 0 | 4599 |

</details>

---

## `Mag. Ghesla Steuerberater GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 4599 |

</details>

---

## `SUVA` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 4599 |

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
| `organisation` | 0 | 0 | 4599 |

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
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 4599 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_25`)


Zur Überbrückung wurde ebenso ernsthaft und mit voller Energie bei  nachweislichem Studienerfolg das Wirtschafts- und Sozialwissenschaften, bzw.  Wirtschaftsrechtsstudium vorangetrieben.

**False Positives:**

- `Zur Überbrückung wurde ebenso ernsthaft und mit voller Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_460`)


Zudem gestattet die Verordnung das Beibehalten von erlassenen gleichwertigen nationalen  Maßnahmen, die zum 31. Dezember 2022 angenommen und veröffentlicht wurden und die zur  Erschwinglichkeit von Energie beitragen (Art 2 Z 21 iVm Art 14 Abs 2).

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_503`)


Diese werden nämlich in Art 2 Z 21 der Verordnung  als "erlassene gleichwertige nationale Maßnahme[n]" definiert, wenn es sich um eine bis zum  31. Dezember 2022 erlassene und veröffentlichte Rechts- oder Verwaltungsmaßnahme  handelt, die zur Erschwinglichkeit von Energie beiträgt, ohne dass für diese Einstufung weitere  Kriterien aufgestellt würden.

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_318`)


Zudem gestattet die Verordnung das Beibehalten von erlassenen gleichwertigen nationalen  Maßnahmen, die zum 31.12.2022 angenommen und veröffentlicht wurden und die zur  Erschwinglichkeit von Energie beitragen (Art 2 Z 21 iVm Art 14 Abs. 2).

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_373`)


Diese werden nämlich in Art 2 Z 21 der Verordnung  als „erlassene gleichwertige nationale Maßnahme[n]“ definiert, wenn es sich um eine bis zum  31.12.2022 erlassene und veröffentlichte Rechts- oder Verwaltungsmaßnahme handelt, die zur  Erschwinglichkeit von Energie beiträgt, ohne dass für diese Einstufung weitere Kriterien  aufgestellt würden.

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_319`)


Zudem gestattet die Verordnung das Beibehalten von erlassenen gleichwertigen nationalen  Maßnahmen, die zum 31.12.2022 angenommen und veröffentlicht wurden und die zur  Erschwinglichkeit von Energie beitragen (Art 2 Z 21 iVm Art 14 Abs. 2).

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_373`)


Diese werden nämlich in Art 2 Z 21 der Verordnung  als „erlassene gleichwertige nationale Maßnahme[n]“ definiert, wenn es sich um eine bis zum  31.12.2022 erlassene und veröffentlichte Rechts- oder Verwaltungsmaßnahme handelt, die zur  Erschwinglichkeit von Energie beiträgt, ohne dass für diese Einstufung weitere Kriterien  aufgestellt würden.

**False Positives:**

- `Erschwinglichkeit von Energie` — no gold match — likely missing annotation

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
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 5 | 4599 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_51`)


Vom 02.01.2010 bis  03.01.2010 absolvierte er zwei (unbezahlte) Schnuppertage bei der Fa. Pertzel Beratung GmbH  in  Berlin, nach dem 2.

**False Positives:**

- `Fa. Pertzel Beratung GmbH` — partial — gold is substring of pred: `Pertzel Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pertzel Beratung GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_54`)


Im Jahr 2010 war er bei  der Fa. Wildon GmbH  in Schrems (Österreich) als Angestellter beschäftigt.

**False Positives:**

- `Fa. Wildon GmbH` — partial — gold is substring of pred: `Wildon GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wildon GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_67`)


war der Bf. laut Versicherungsdatenauszug  doch im Jahr 2010 durchgehend bei der Fa. Wildon GmbH  in Schrems beschäftigt und übte  seine Tätigkeit – wie auch in den Jahren davor und danach - in Österreich aus.

**False Positives:**

- `Fa. Wildon GmbH` — partial — gold is substring of pred: `Wildon GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wildon GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1207`)


Zunächst erinnert der Vorwurf massiver Leistungsmängel, deren Umfang in den nachfolgenden  Gerichtsverfahren nicht bestätigt wurde, an die Zuschreibung umfangreicher Statikmängel  gegenüber der Fa A Bau GmbH, deren behauptetes Ausmaß im Verfahren nicht erwiesen  wurde.

**False Positives:**

- `Fa A Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_27`)


Über Ersuchen des BFG übermittelte die Fa. MH GmbH eine Lohnsteuerbescheinigung für 2018  (Bescheinigungszeitraum 1.3.-31.3.), aus welcher hervorgeht, dass der strittige Betrag von  € 27.482,76 als „steuerfreier Arbeitslohn nach DBA“ ausbezahlt wurde.

**False Positives:**

- `Fa. MH GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Specific Company Names` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 4599 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Janosch Herr  in der Beschwerdesache des  René Schiekel, MSc, Auf der Kröß 1, 2151 Altmanns, Österreich, vertreten durch Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH, Gartenaugasse 3, 3500 Krems/Donau, über die Beschwerde vom 11. Juni 2019 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH` — partial — pred is substring of gold: `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Herr`(person)
- `René Schiekel, MSc`(person)
- `Auf der Kröß 1, 2151 Altmanns, Österreich`(address)
- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`(organisation)

</details>

---

## `Company Suffix m.b.H` 

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
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 4599 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_24`)


Da die Bauunternehmung T.. VN Fn Gesellschaft m.b.H. in Zukunft nicht das  wirtschaftliche Risiko aus der Unterdeckung der zugesagten Firmenpension tragen  möchte, ist T.. S. als Geschäftsführer der Bauunternehmung T.. G2 an T.. VN Fn mit dem  Wunsch herangetreten, auf die Auszahlung der lebenslangen monatlichen Pension in  Höhe von € 1.452 gegen Zahlung einer einmaligen Entschädigungszahlung zu  verzichten.

**False Positives:**

- `VN Fn Gesellschaft m.b.H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1242, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)

Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des **Magistrats der  Stadt Wien** bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

- missed: `Magistrats der  Stadt Wien` (organisation)
- predicted in sentence: `Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land **Finanzamtes**  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

- missed: `Finanzamtes` (organisation)
- predicted in sentence: `Finanzamtes Salzburg`, `Finanzamtes  Salzburg`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_553`)

In der nachfolgenden neuerlichen Entscheidung des **LG ZRS Graz** von 23.Febr.2012 wurde die  Klage der Fa XY – ohne Ergänzung der Beweisaufnahme betreffend Hohlräume - aufgrund von  Mängeln im Außenbereich (EG/Ostterrasse) als unbegründet abgewiesen.

- missed: `LG ZRS Graz` (organisation)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des **Magistrats der Stadt Wien**,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Magistrats der Stadt Wien` (organisation)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_73`)

Sämtliche Doppelwohnhäuser in der Anlage wurden von der **MH-Bau GmbH** errichtet.

- missed: `MH-Bau GmbH` (organisation)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_26`)

Laut Bestätigung der Veterinärmedizinischen **Universität Wien** hat die Tochter im Studienjahr  2019/20 im Bachelorstudium Pferdewissenschaften (in chronologischer Abfolge) bis zum  25.05.2020 folgende Prüfungen/Lehrveranstaltungen positiv abgelegt bzw. mit Erfolg  teilgenommen:    Titel Note Semesterstunden ECTS Punkte Prüfungs- /  Anerkennungsdatum  Pferderassen und  Pferdebeurteilung  mit Erfolg  teilgenommen  1,00 0,00 20.11.2019  Organisation des Reit- und  Rennsports  1 1,00 1,50 03.12.2019  Pferdezucht- und Gestütmedizin mit Erfolg  teilgenommen  1,00 0,00 04.12.2019  Geschichte der Reiterei und  Pferdezucht  2 0,00 1,50 10.12.2019  Geschichte der Reiterei und  Pferdezucht  mit Erfolg  teilgenommen  1,00 0,00 10.12.2019  Pferderassen und  Pferdebeurteilung  1 0,00 1,50 11.12.2019  Pferdezucht und Gestütmedizin 2 1,00 1,50 18.12.2019  Naturwissenschaftliche  Grundlagen-Physik  mit Erfolg  teilgenommen  1,00 0,00 23.01.2020  Naturwissenschaftliche  Grundlagen-Chemie  3 0,00 4,50 30.01.2020  Naturwissenschaftliche  Grundlagen-Chemie  mit Erfolg  teilgenommen  3,00 0,00 30.01.2020  Ethologie des Pferdes 4 1,00   1,50  30.01.2020  Zoologie für  Pferdewissenschaften  3 2,00 3,00  26.02.2020  Klassische Reitlehre und  Pferdeausbildung  mit Erfolg  teilgenommen  1,00 1,00 25.05.2020  3 von 7 Seite 4 von 7

- missed: `Universität Wien` (organisation)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_55`)

Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus dem vom Finanzamt vorgelegten Veranlagungsakt  und dem Urteil des **Landesgerichtes** X, vom XX.X.2020, Gz xx.

- missed: `Landesgerichtes` (organisation)
- predicted in sentence: `Finanzamt`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/145955.1`) (sent_id: `deanon_BFG_20260814_TEST/145955.1_23`)

Festzuhalten ist, dass mit Beschluss vom 8.3.2017, GZ. RV/7102722/2013 das  Bundesfinanzgericht ausgesprochen hat, dass es sich bei der als Feststellungsbescheid gemäß  § 188 BAO intendierten Erledigung vom 2.4.2012 für das Jahr 2002 betreffend die **FA Vorarlberg**  AG & Mitges., St.nr. 53-058/7266  um einen „Nichtbescheid“ handelt.  Ebenso hat das Bundesfinanzgericht mit Beschluss vom 4.2.2019, GZ. RV/4100236/2012,  ausgesprochen, dass es sich bei der als Feststellungsbescheid gemäß § 188 BAO intendierten  Erledigung vom 1.6.2010 für das Jahr 2004 betreffend die Finanzamt Niederösterreich Mitte  GmbH & Co KG, St.nr.  07-776/8819  um einen „Nichtbescheid“ handelt.  Wird ein Änderungsbescheid gemäß § 295 Abs. 1 BAO erlassen (wie im vorliegenden Fall die  gemäß § 295 Abs. 1 BAO geänderten Einkommensteuerbescheide für 2002 und 2004 vom  30.11.2012), obwohl der hierfür herangezogene Grundlagenbescheid ins Leere gegangen ist  (hier: die als Feststellungs"bescheide" nach § 188 BAO intendierten Erledigungen der   Finanzämter, die beide „Nichtbescheide“ darstellen;

- missed: `FA Vorarlberg` (organisation)
- predicted in sentence: `Finanzamt Niederösterreich Mitte  GmbH & Co KG`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_29`)

Die Bf. habe den **Magistrat der Stadt  Wien** ersucht zu prüfen, ob statt Geldstrafen zu verhängen, Ermahnungen erteilt werden kön- nen.

- missed: `Magistrat der Stadt  Wien` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_135`)

Dem **FAÖ** zufolge sei sie für [Bf.] weder leistungserbringend noch Empfänger/Gläubiger der ihr  bezahlten Gelder gewesen.

- missed: `FAÖ` (organisation)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_95`)

Dass der Bf. an die **Nexgart-Textil GmbH**  für die erbrachten Leistungen Honorarnoten  ausgestellt hat und dafür eine fremde bzw. eine ungültige UID-Nummer verwendet hat, ergibt  sich aus den vorliegenden Rechnungen.

- missed: `Nexgart-Textil GmbH` (organisation)
- predicted in sentence: `Textil GmbH`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_49`)

Herr F übertrug von Todes wegen unentgeltlich dieses  Sonderbetriebsvermögen (Baurechtseinlage EZ 2 KG XY) der Wohlgemut Getränke GmbH& Co KG bei gleichzeitiger  Zuwendung von 100% der Mitunternehmeranteile der **Wohlgemut Getränke GmbH&** Co an Frau A. Der Begriff  Sonderbetriebsvermögen  in § 3 Abs. 1 Z 2 lit a zweiter Teilstrich GrEStG ist ertragsteuerlich zu definieren.

- missed: `Wohlgemut Getränke GmbH&` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_45`)

Nachdem das Baurecht an die **Wohlgemut Getränke GmbH**& Co KG entgeltlich zur Nutzung  überlassen wurde stellte dieses in Bezug auf Herrn F (99%) Sonderbetriebsvermögen der Wohlgemut Getränke GmbH& Co KG dar.

- missed: `Wohlgemut Getränke GmbH` (organisation)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_45`)

In der gesonderten zugestellten Bescheidbegründung wurde ausgeführt:  „Aus dem übermittelten „Reeder-Zertifikat“ Nr. 277 geht hervor, dass der Bf. an der Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr **S GmbH & Co KG**) beteiligt ist.

- missed: `S GmbH & Co KG` (organisation)
- predicted in sentence: `Rudolphson Heizung GmbH & Co KG`, `S GmbH`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)

Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  **MH-Bau GmbH** am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

- missed: `MH-Bau GmbH` (organisation)
- predicted in sentence: `Bau GmbH`

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_67`)

war der Bf. laut Versicherungsdatenauszug  doch im Jahr 2010 durchgehend bei der Fa. **Wildon GmbH**  in Schrems beschäftigt und übte  seine Tätigkeit – wie auch in den Jahren davor und danach - in Österreich aus.

- missed: `Wildon GmbH` (organisation)
- predicted in sentence: `Fa. Wildon GmbH`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_29`)

Die Beschwerdeführerin verfügt über kein aktives Vermögen und wurde mit Beschluss des  **LG Ried im Innkreis**  vom 25. Januar 1989  im Firmenbuch gemäß § 40 FBG infolge Vermögenslosigkeit  gelöscht.

- missed: `LG Ried im Innkreis` (organisation)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_58`)

Für den Zeitraum März 2008 bis November 2014 wurde FB + KG für alle Kinder an die Gattin  des Bf ausbezahlt.   Mit Bescheid vom 12.12.2014 wurden **FB + KG** von der Gattin für den Zeitraum Jänner 2009 bis  November 2014 im Betrag von gesamt € 62.483,40 zurückgefordert.

- missed: `FB + KG` (organisation)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des **Finanzamtes Gmunden Vöcklabruck**  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

- missed: `Finanzamtes Gmunden Vöcklabruck` (organisation)
- predicted in sentence: `Finanzamtes Gmunden`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/147296.1`) (sent_id: `deanon_BFG_20260814_TEST/147296.1_3`)

Entscheidungsgründe  Mit Bescheid vom 9. Mai 2019 hat das **Finanzamt Salzburg-Land** gegenüber der  Steuergemeinschaft Doris Weierstahl (nachstehend mit „Bf“ bezeichnet) einen ersten  Säumniszuschlag in Höhe von EUR 89,15 festgesetzt, weil die Umsatzsteuer 2017 nicht bis  15. Februar 2015 entrichtet worden ist.

- missed: `Finanzamt Salzburg-Land` (organisation)
- predicted in sentence: `Finanzamt Salzburg`

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_381`)

Wir weisen darauf hin, dass die im Ergänzungsersuchen angeforderten Daten dem **Finanzamt**  für Gebühren, Verkehrsteuern und Glücksspiel bereits im Zuge der Selbstanzeige vom 21.  Dezember 2016 übermittelt wurden.

- missed: `Finanzamt` (organisation)
- predicted in sentence: `Finanzamt  für Gebühren`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_13`)

Dem Schreiben beigelegt waren ein Versicherungsdatenasuzug für die Jahre 2011 bis 2016, der  Bescheid der GKK vom 20.02.2017, mit welchem festgestellt wurde, dass der Bf. auf Grund  seiner Beschäftigung bei der GmbH in den Jahren 2011 bis 2014 der Vollversicherungspflicht  gem. § 4 Abs. 1 Z 1 iVm § 4 Abs. 2 ASVG und der Arbeitslosenversicherungspflicht gem. § 1 Abs.  1 lit. a AlVG unterliegt, und die Klage des Bf. vom 27.10.2016 an das **Arbeits- und Sozialgericht  Wien** betreffend ausständige Gehaltszahlungen.

- missed: `Arbeits- und Sozialgericht  Wien` (organisation)
- predicted in sentence: `Grund  seiner Beschäftigung bei der GmbH`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_60`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die P-GmbH (die Verkäuferin) war grundbücherliche Eigentümerin der Liegenschaft EZ-1,  KG XY, **Bezirksgericht A**, ob welcher Liegenschaft unter anderem die Grundstücke Nr. 433/2,  433/4, 433/5, 433/6 und 433/7 vorgetragen waren (siehe Kaufvertrag vom 15./19.01.2015, VP.  I. ALLGEMEINES).

- missed: `Bezirksgericht A` (organisation)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_127`)

Sie ergibt sich  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der **Gablonsky&Rethlefsen Gastronomie AG** in Höhe von €  67.593.518,50 zum Stichtag des Zusammenschlusses, bezogen auf eine Einlage von €  10 von 28 Seite 11 von 28

- missed: `Gablonsky&Rethlefsen Gastronomie AG` (organisation)
- predicted in sentence: `Sie ergibt sich  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_81`)

Weder wurden irgendwelche schriftlichen  Aufzeichnungen über die angeblich erbrachten Leistungen - ein im Geschäftsleben unüblicher  Vorgang - noch hat Hr. X in der Ergänzung nachvollziehbar dargestellt, welche Zahlungen und  in welcher Höhe die **Mackwart und Reinink Automotive GmbH** für die angebliche Leistungserbringen erhalten hat.

- missed: `Mackwart und Reinink Automotive GmbH` (organisation)
- predicted in sentence: `Zahlungen und  in welcher Höhe die Mackwart und Reinink Automotive GmbH`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138911.1`) (sent_id: `deanon_BFG_20260814_TEST/138911.1_4`)

Entscheidungsgründe  Der **Magistrat der Stadt Wien, Magistratsabteilung 67**, befand die Beschwerdeführerin (Bf.) mit  Straferkenntnis vom 1. August 2022, GZ. MA67/Zahl/2022, für schuldig, das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 9. Juni 2022 in der  gebührenpflichtigen Kurzparkzone in 1160 Wien, Sandleitengasse 16 ggü, ohne einen für den  Beanstandungszeitpunkt 11:37 Uhr gültigen Parkschein abgestellt zu haben, da der Parkschein  Nr. XY Spuren von entfernten Entwertungen aufgewiesen habe.

- missed: `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_63`)

Dem Beschuldigten wurde wie folgt vorgehalten: Laut Bericht über die Außenprüfung vom 11.10.2017 unter Tz 2 wurden nicht anzuerkennende Fremdleistungen aufgrund von Scheinrechnungen der Fa. X. für das Jahr  2012 iHv € 74.884,49 und für 2013 iHv € 18.550,91 festgestellt. Weiters wurden nach den Feststellungen im Bericht über die Außenprüfung vom 11.10.2017 unter Tz. 4 Fremdleistungen aufgrund von auf den Namen der Kisteler Telekom GmbH lautenden Rechnungen im Jahr 2012 iHv € 220.314,31 sowie auf den Namen der **Fa.NEP Lebensmittel GmbH** lautenden Rechnungen im Jahr 2013 iHv € 115.236,61 als Betriebsausgaben geltend gemacht.

- missed: `Fa.NEP Lebensmittel GmbH` (organisation)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_9`)

Seitens des Finanzamtes wurde ausgeführt, dass der Bf. in der Zeit ab 11.05.2007  Geschäftsführer der **NordGetränke GmbH** und somit deren gesetzlicher Vertreter gewesen sei.

- missed: `NordGetränke GmbH` (organisation)
- predicted in sentence: `Finanzamtes`, `Geschäftsführer der NordGetränke GmbH`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_100`)

Im Rahmen des beim **Arbeits- und Sozialgericht Wien** zur GZ 9 Cga 125/16s geführten  Verfahrens gab der Bf. an, dass sich die Art seiner Tätigkeit in keiner Weise von jener der  anderen, bei der Firma angestellten Kollegen unterschieden habe und dass er seit Beginn der  Zusammenarbeit mit der Firma ein Angestelltenverhältnis gelebt habe.

- missed: `Arbeits- und Sozialgericht Wien` (organisation)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_340`)

Die zu den führenden Pensionsfonds in Deutschland zählende **XY Deutschland  Pensionsfonds AG** ordnet das BFG auf Basis der von der Bf übermittelten Unterlagen, des  unionsrechtlichen Hintergrunds zur betrieblichen Altersvorsorge und der dargestellten  deutschen Rechtslage den Einrichtungen im Sinne des § 5 Z 4 PKG zu.  Mit der Übertragung des bis dahin ohne Rechtsanspruch ausbezahlten Teiles der Betriebsrente  auf die XY Deutschland Pensionsfonds AG erlangte die Bf einen gesetzlich geregelten  Rentenanspruch, der grundsätzlich zu einem Vorteil aus dem Dienstverhältnis führte.

- missed: `XY Deutschland  Pensionsfonds AG` (organisation)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des **Finanzamtes Waldviertel** vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

- missed: `Finanzamtes Waldviertel` (organisation)
- predicted in sentence: `Astoria Wirtschaftstreuhand GmbH & Co KG`, `Finanzamtes`, `Finanzamtes`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_4`)

Entscheidungsgründe  In der Folge werden für die im Erkenntnis angeführten Gesellschaften nachstehende  Abkürzungen verwendet:  Firma FN Abkürzung  P-GmbH 1-t P-GmbH  G-GmbH 2-x G-GmbH  MH-Bau GmbH 3-f MH-Bau GmbH  MH-Immo GmbH 4-h **MH-Immo GmbH**

- missed: `MH-Immo GmbH` (organisation)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_273`)

Die in den Lohnsteuerbescheinigungen 2013/2014 zur Direktrente der **Tal Waldvalver Gruppe GmbH**  unter Z. 28 ausgewiesenen „Beiträge zur privaten Krankenversicherung und  Pflegepflichtversicherung (gffs. Mindestvorsorgepauschale)“ von 393,90 € bzw. 404,64 €  wurden in die deutschen ESt-Bescheide nicht übernommen.

- missed: `Tal Waldvalver Gruppe GmbH` (organisation)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)

Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der **Mohrlock Metall GmbH & Co KG** vor.

- missed: `Mohrlock Metall GmbH & Co KG` (organisation)
- predicted in sentence: `Finanzamtes`, `Rudolphson Heizung GmbH & Co KG`, `S GmbH`, `Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_12`)

Mit Straferkenntnis vom 9. Mai 2023 befand der **Magistrat der Stadt Wien, Magistratsabteilung  67**, den Bf. wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig und  verhängte wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabe- verordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für  den Fall der Uneinbringlichkeit 14 Stunden Ersatzfreiheitsstrafe.

- missed: `Magistrat der Stadt Wien, Magistratsabteilung  67` (organisation)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_126`)

2. Beweiswürdigung  Strittig ist, ob es sich bei der Beteiligung an der **Schifffahrtsgesellschaft S GmbH & Co KG** um  eine mitunternehmerische Beteiligung handelt und damit Einkünfte aus Gewerbebetrieb  vorliegen oder um eine Beteiligung nach Art eines stillen Gesellschafters und damit Einkünfte  aus Kapitalvermögen vorliegen.

- missed: `Schifffahrtsgesellschaft S GmbH & Co KG` (organisation)
- predicted in sentence: `Beteiligung an der Schifffahrtsgesellschaft S GmbH & Co KG`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_68`)

Aus dem beigefügten Arbeiterdienstvertrag mit seinem neuen  Arbeitgeber **Wright Robotik AG**  geht hervor, dass als Dienstantritt der 6. März 2023 vereinbart wurde.

- missed: `Wright Robotik AG` (organisation)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch **Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.**, Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

- missed: `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.` (organisation)
- predicted in sentence: `Finanzamt  Österreich`

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/149737.1`) (sent_id: `deanon_BFG_20260814_TEST/149737.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mag. Timon Wandschneider  in der Beschwerdesache Linn Seebade,  Volkenstorferweg 19, 9863 Pron, Österreich, über die Beschwerde vom 23. April 2025 gegen den Bescheid des **FA Freistadt Rohrbach Urfahr**  vom 14. April 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 43-163/0517, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `FA Freistadt Rohrbach Urfahr` (organisation)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_102`)

Das Bundesfinanzgericht legte dem Gerichtshof der Europäischen Union gemäß Artikel 267  AEUV folgende Frage zur Vorabentscheidung vor:  "Sind Artikel 18 und Artikel 45 Absatz 1 des Vertrags über die Arbeitsweise der Europäischen  Union, Artikel 7 Absätze 1 und 2 der Verordnung (EG) Nr. 492/2011 des Europäischen  Parlaments und des Rates vom 5. April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb  der Union, Artikel 4, Artikel 5 Buchstabe b, Artikel 7 und Artikel 67 der Verordnung (EG) Nr.  883/2004 des **Europäischen Parlaments** und des Rates vom 29. April 2004 zur Koordinierung  der Systeme der sozialen Sicherheit sowie Artikel 60 Absatz 1 Satz 2 der Verordnung (EG) Nr.  987/2009 des Europäischen Parlaments und des Rates vom 16. September 2009 zur Festlegung  der Modalitäten für die Durchführung der Verordnung (EG) Nr. 883/2004 über die Koordi- nierung der Systeme der sozialen Sicherheit dahin auszulegen, dass sie der Anwendung einer  nationalen Regelung entgegenstehen, die vorsieht, dass Familienleistungen für ein Kind, das  sich nicht tatsächlich ständig in dem diese Familienleistungen zahlenden Mitgliedstaat, sondern  tatsächlich in einem anderen Mitgliedstaat der Europäischen Union, einer anderen Vertrags- partei des Abkommens über den Europäischen Wirtschaftsraum oder der Schweiz aufhält, auf  Basis der vom Statistischen Amt der Europäische Union veröffentlichten vergleichenden Preis- niveaus für den jeweiligen Staat im Verhältnis zu dem die Familienleistungen zahlenden  Mitgliedstaat anzupassen?"

- missed: `Europäischen Parlaments` (organisation)
- predicted in sentence: `Gerichtshof der Europäischen Union`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_52`)

Das Einkommen 2007 und die darauf entfallende Abgabe waren wie folgt zu berechnen:    Einkommensteuer für 2007  Einkünfte aus nichtselbständiger Arbeit  Übermittelte Lohnzettel (KZ 245)  **ÖBB** 25.324,62 €  Sonstige Werbungskosten ohne Anrechnung  Auf den Pauschbetrag -1.125,00 €  Pauschbetrag für Werbungskosten -132,00 € 24.067,62 €  Einkünfte aus Vermietung und Verpachtung  -1.688,49 €   -----------------  4 von 6 Seite 5 von 6

- missed: `ÖBB` (organisation)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_170`)

3. Die geschäftsführende Komplementärin erhält für die Geschäftsführung und Haftung  eine Vergütung von € 1.000,00 pro Monat zuzüglich gesetzlicher Umsatzsteuer (vgl.  Kapitalmarktprospekt **Richsteiger Marine**  und Richsteiger Marine  Punkt 2.14).

- missed: `Richsteiger Marine` (organisation)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_405`)

Der zweite Wert enthält neben Fahrten zum Hausarzt bzw. zu zwei Ärzten,  zu deren Behandlungskosten dem Bf von der **ÖGK** eine Teilkostenerstattung gewährt wurde,  auch 232,8 km betreffend Fahrten, für deren Zweck der Bf trotz FA-Aufforderung zur  vollständigen Belegvorlage vom 20.Aug.2020 keinerlei Belege übermittelt hatte (23.5. Dr- E/Ort-2, 29.10.

- missed: `ÖGK` (organisation)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)

Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die **Firma2 GmbH & CoKG**, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

- missed: `Firma2 GmbH & CoKG` (organisation)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_16`)

Laut Stellungnahme des Unternehmens vom 22.7.2015 waren die  Absicherungsgeschäfte für **Raiffeisen-Rionalbank Gänserndorf**  Spot-Geschäfte.

- missed: `Raiffeisen-Rionalbank Gänserndorf` (organisation)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des **Finanzamt Waldviertel**  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

- missed: `Finanzamt Waldviertel` (organisation)
- predicted in sentence: `Finanzamt`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  **FA Wien 2/20/21/22**  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `FA Wien 2/20/21/22` (organisation)
- predicted in sentence: `FA Wien 2/20`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des **Finanzamtes Wien 9/18/19 Klosterneuburg** vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

- missed: `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- predicted in sentence: `Finanzamtes Wien 9/18/19`, `Finanzamtes Wien 9/18/19`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_4`)

Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid des **Zollamtes Feldkirch Wolfurt** vom 26.11.2019 wurde gemäß Art. 89 iVm Art.  92 UZK eine Sicherheit für eine möglicherweise nach Art. 79 UZK entstandene Abgabenschuld  in der Höhe von EUR 8.138,68 eingehoben.

- missed: `Zollamtes Feldkirch Wolfurt` (organisation)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Reinhold Jonasius, Johann Tagwerker-Straße 17, 5760 Pabing, Österreich, vertreten durch **Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH**, Zieglergasse 27/2/9, 1070  Wien, über die Beschwerde vom 28.08.2015 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 22. Juni 2015  betreffend Festsetzung der Kapitalertragsteuer 2011 – 2013, Steuernummer 81-937/8981  nach Durchführung einer mündlichen Verhandlung am 31. Jänner 2025 zu Recht erkannt:   I. Der Beschwerde wird als teilweise Folge gegeben.

- missed: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH` (organisation)
- predicted in sentence: `Finanzamtes Wien  3/6/7/11/15`, `Finanzamt Österreich`

</details>

---

