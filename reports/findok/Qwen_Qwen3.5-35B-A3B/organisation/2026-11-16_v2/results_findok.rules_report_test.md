# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-16T12:10:20.922668

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-11-16_v2/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 5 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 5 |
| Validation documents | 790 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 124 |
| Validation sentences | 20833 |
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
| Accuracy (exact match) | 97.3% |
| True Positives | 9844 |
| False Positives | 365 |
| False Negatives | 1952 |
| Total Gold Entities | 11796 |
| Micro Precision | 96.4% |
| Micro Recall | 83.5% |
| Micro F1 | 89.5% |
| Macro F1 | 89.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Courts - Verwaltungsgerichtshof` | 30.4% | 100.0% | 17.9% | 2112 | 2112 | 0 |
| `Courts - Verfassungsgerichtshof` | 2.9% | 100.0% | 1.5% | 172 | 172 | 0 |
| `City Authority - Magistrat der Stadt Wien` | 4.3% | 99.2% | 2.2% | 260 | 258 | 2 |
| `Courts - Bundesfinanzgericht` | 53.8% | 97.6% | 37.2% | 4495 | 4386 | 109 |
| `Tax Authority - Generic Finanzamt` | 33.4% | 95.2% | 20.2% | 2508 | 2387 | 121 |
| `Tax Authority - Finanzamt Locations` | 7.3% | 92.9% | 3.8% | 479 | 445 | 34 |
| `City Authority - Stadt Wien` | 1.4% | 45.9% | 0.7% | 183 | 84 | 99 |
| `Law Firm - Glatzhofer & Matschek` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company - GCX Möbel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company - VTX E‑Commerce Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company - RheinBildung Manufaktur GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Courts - Verwaltungsgerichtshof` 🏆

**F1:** 0.304 | **Precision:** 1.000 | **Recall:** 0.179  

**Format:** `regex`  
**Rule ID:** `45be7cd0`  
**Description:**
Matches the Administrative Court, handling genitive case endings.

**Content:**
```
\b(Verwaltungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.179 | 0.304 | 2112 | 2112 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2112 | 0 | 9684 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_25`)


Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_200`)


Vorsätzliches Handeln beruht nach ständiger Rechtsprechung des Verwaltungsgerichtshofes zwar auf einem nach außen nicht erkennbaren Willensvorgang, ist aber aus dem nach außen in Erscheinung tretenden Verhalten des Täters zu erschließen, wobei sich die diesbezüglichen Schlussfolgerungen als Ausfluss der freien Beweiswürdigung erweisen (VwGH 28.11.2007, 2007/15/0165).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_325`)


Zulässigkeit einer Revision Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_328`)


Die Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_4`)


Die im Kalenderjahr 2008 erzielten Einkünfte werden gemäß § 188 BAO wie folgt festgestellt: [...] III.  Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 B-VG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_107`)


V.     Zulässigkeit einer Revision Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_108`)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_110`)


Die ordentliche Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_111`)


Zur außerordentlichen Revision an den Verwaltungsgerichtshof siehe nachstehende Rechtsbelehrung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_60`)


Zur Unzulässigkeit der ordentlichen Revision Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_70`)


Wie der Verwaltungsgerichtshof ausgesprochen hat, steht der  Abgabenbehörde sowohl bei der Frage der Zuschlagsfestsetzung dem Grunde nach als auch bei  der Festlegung des Ausmaßes des Verspätungszuschlages Ermessen zu (vgl zB VwGH 12.8.2002,  98/17/0292;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_94`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine s olche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_96`)


Mit dem vorliegenden Erkenntnis weicht das Bundesfinanzgericht nicht von der Rechtsprechung  des Verwaltungsgerichtshofes ab, sondern folgt insbesondere dem Erkenntnis des VwGH vom  25.6.2007, 2006/14/0054, weshalb gemäß § 25a Abs 1 VwGG spruchgemäß zu entscheiden ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_74`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_134`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_77`)


Dass der Besuch von Seminaren zur  Kommunikationsverbesserung im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den  Bereich der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof  wiederholt bejaht (zB VwGH 29.1.2004, 2000/15/0009;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_81`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_83`)


Zum  § 16 liegt eine einheitliche Rechtsprechung des Verwaltungsgerichtshofes vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_3`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_36`)


Zur Revision:   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_124`)


V. Erwägungen:  1. Dauernder Standort, widerrechtliche Verwendung:   Nach der Judikatur des Verwaltungsgerichtshofes (siehe zB Erkenntnis 21.5.1996, 95/11/0378)  ist das Lenken von im Ausland zugelassenen Kraftfahrzeugen (und zwar in einem der  Mitgliedsstaaten eines der in § 82 Abs. 1 KFG 1967 genannten internationalen  Übereinkommen) nach Maßgabe des § 82 KFG 1967 erlaubt, also ohne dauernden Standort in  Österreich bis zu einer Höchstdauer von 1 Jahr (§ 79 Abs. 1 KFG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_167`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_169`)


Der Verwaltungsgerichtshof hat jedoch bereits mehrfach zum Ausdruck gebracht hat, dass bei  einem Barbetrieb mit angeschlossenen Separees (bzw. Zimmern) die Leistung des  Barbetreibers nach der Kundenerwartung nicht nur im Getränkeausschank, sondern  entscheidend auch in der Gelegenheit zum Separee-Besuch besteht.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_240`)


Zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_41`)


Subjektive Momente, wie Verschulden, Gutgläubigkeit oder die Verwendung  der Familienbeihilfe, sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die  Verpflichtung zur Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_71`)


Ein Studienwechsel im Sinne des § 17 StudFG liegt im Sinne der Judikatur des  Verwaltungsgerichtshofes vor, wenn der Studierende das von ihm begonnene und bisher  6 von 9 Seite 7 von 9

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_93`)


Dass der Sohn  des Bf. einen Wechsel des Studiums für zweckmäßiger oder sien persönlichen Vorstellungen  angemessener gehalten hat, bedeutet aber nicht, dass er zum Studienwechsel gezwungen  gewesen wäre, weil aus den Ausführungen des Bf nicht hervorgeht, dass es seinem Sohn aus  von ihm nicht zu vertretenden Gründen unmöglich gewesen wäre, das Studium  Wirtschaftrecht  weiter zu betreiben ( siehe auch das Erkenntnis des Verwaltungsgerichtshofes  VwGH vom 26.5.2011, 2011/16/0076).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_97`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_98`)


Im gegenständlichen Verfahren war weder eine Rechtsfrage von grundsätzlicher Bedeutung zu  lösen noch ist das Bundesfinanzgericht von der Rechtsprechung des Verwaltungsgerichtshofes  abgewichen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_98`)


Somit ist der Verweis des Finanzamtes auf die Erkenntnisse  des VwGH vom 29.4.2015, 2012/13/0012 und vom 20.11.2019, Ro 2018/15/0024 ist nicht  geeignet, sein Vorbringen zu stützen: In beiden Erkenntnissen hat der Verwaltungsgerichtshof  über die Abzugsfähigkeit von Unterhaltsleistungen an einen Elternteil im Zusammenhang mit  einer vorangegangenen Vermögensübertragung vom Elternteil auf Nachkommen  abgesprochen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_102`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_103`)


Die Frage, ob und in welchem  Ausmaß Aufwendungen für die Pflege des Ehegatten als außergewöhnliche Belastung  berücksichtigt werden können, ist durch das zitierte Erkenntnis des Verwaltungsgerichtshofes  geklärt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_32`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_47`)


4.2. Soweit das Finanzamt die Inanspruchnahme des Werkverkehrs in den Monaten Februar  und Juni für zumutbar gehalten und deshalb eine Kürzung des Pauschales vorgenommen  hat, ist festzuhalten:    Im Erkenntnis VwGH 27.07.2016, 2013/13/0088 hat der Verwaltungsgerichtshof klar- gestellt, dass die sich aus § 16 Abs. 1 Z 6 lit. b und c EStG 1988 ergebenden Pauschbe- träge auf Grund des Wortlautes des Gesetzes nicht schon dann nicht zustehen, wenn  der Arbeitnehmer im Werkverkehr befördert werden könnte und ihm dies auch zumut- bar wäre.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_66`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_69`)


Eine Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_145`)


Nach der ständigen  Rechtsprechung des Verwaltungsgerichtshofes muss jedoch in der Tatumschreibung gemäß  11 von 24 Seite 12 von 24

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_198`)


Verwiesen wird auf das Erkenntnis des Verwaltungsgerichtshofes vom 18.05.2004,  2002/17/0277, wo der Gerichtshof in einem vergleichbaren Fall feststellte, dass der Beginn der  Abstellzeit anzukreuzen sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_215`)


Nach der Judikatur des Verwaltungsgerichtshofes ist die bloße Erklärung eines Beschuldigten,  der Vorhalt der ihm zur Last gelegten Verwaltungsübertretung sei unrichtig, nicht ausreichend,  den von der Behörde festgestellten Sachverhalt zu widerlegen (vgl. ua. VwGH 30.09.1991,  91/19/0088, VwGH 30.10.1991, 91/09/0060, VwGH 29.04.1992, 91/17/0054, VwGH  19.01.1994, 93/03/0220, VwGH 13.11.1996, 96/03/0237, vgl. auch die bei Hauer/Leukauf,  Handbuch des österreichischen Verwaltungsverfahrens5, 890, zitierte Judikatur), sondern ist  vielmehr ein entsprechendes, ausreichend konkretes Sachsubstrat darzulegen (zB VwGH  20.05.1968, 0187/67, VwGH 14.10.1976, 1497/75;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_221`)


Nur so ist es dem Bescheidadressaten und auch dem  Verwaltungsgerichtshof möglich, den Bescheid auf seine Rechtsrichtigkeit zu überprüfen (vgl.  VwGH 18.06.2014, 2013/09/0172, unter Verweis auf VwGH 28.06.2002, 99/02/0084, vgl.  weiter zu § 60 AVG VwGH 23.05.2014, 2014/02/0013, VwGH 09.10.2014, 2013/02/0269).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_266`)


Schlussendlich wird diesbezüglich darauf hingewiesen, dass der Verwaltungsgerichtshof im  Erkenntnis vom 26.01.1998, 96/17/0354, zu § 1 Abs. 3 2. Satz des (Wiener)  Parkometergesetzes, LGBl.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_313`)


Zur Zulässigkeit der Revision   Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig, da bei  Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt werden darf  und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine Verletzung in  subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_314`)


Eine Revision durch die belangte Behörde ist gem. Art. 133 Abs. 4 B-VG nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_316`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_175`)


Zur Unzulässigkeit einer Revision  Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig,  da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt  werden darf und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine  Verletzung in subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_176`)


Eine Revision durch die belangte Behörde ist gem. Art. 133 Abs. 4 B-VG nicht zulässig,  da das Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche  Bedeutung zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung  des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu  lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes  nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_2`)


II. Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art 133  Abs 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_46`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der  bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_47`)


Mit dem vorliegenden Beschluss weicht das Bundesfinanzgericht nicht von der Rechtsprechung  des Verwaltungsgerichtshofes ab (vgl VwGH 22.10.2015, Ro 2015/15/0035), weshalb gemäß  § 25a Abs 1 VwGG spruchgemäß zu entscheiden ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art  133 Abs 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_40`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_227`)


Nach der Judikatur des Verwaltungsgerichtshofes (vgl. VwGH 04.07.2016, Ra 2016/04/0057)  hat der Antragsteller die Möglichkeit, Unvollständigkeiten und Unschlüssigkeiten eines  Gutachtens im Rahmen des Verfahrens der Behörde aufzuzeigen oder einem Gutachten (etwa  durch Beibringung eines eigenen Gutachtens) auf gleicher fachlicher Ebene entgegenzutreten.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_248`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Behörde an die der  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen zugrundeliegenden  Gutachten gebunden (vgl. VwGH 22.12.2011, 2009/16/0310, VwGH 16.12.2014, Ro  2014/16/0053) und darf diese nur insoweit prüfen, ob sie schlüssig und vollständig sind und -  im Falle mehrerer Gutachten - nicht einander widersprechen (vgl. VwGH 29.09.2011,  2011/16/0063, VwGH 25.11.2010, 2010/16/0068, Beschluss VwGH 16.12.2014, Ro  2014/16/0053, Erkenntnisse VwGH jeweils vom 22.12.2011, 2009/16/0307 und 2009/16/0310,  VwGH 30.03.2017, Ra 2017/16/0023, vgl. auch die bei Lenneis in Csaszar/Lenneis/Wanke,  FLAG, § 8 Rz 29 zitierte Rechtsprechung).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesamtes für Soziales und Behindertenwesen` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_254`)


Nach ständiger Rechtsprechung  des Verwaltungsgerichtshofes (Vgl. für viele VwGH 9.9.2004, 99/15/0250) ist von mehreren  Möglichkeiten jene als erwiesen anzunehmen, die gegenüber allen anderen Möglichkeiten eine  überragende Wahrscheinlichkeit für sich hat und alle anderen Möglichkeiten ausschließt oder  zumindest weniger wahrscheinlich erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_259`)


Die Gutachten entsprechend den Anforderungen, wie sie der Verwaltungsgerichtshof in seiner  ständigen Judikatur festgelegt hat.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_264`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_4`)


2. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_105`)


Nach der bisherigen Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 28.1.2015,  2010/13/0192) konnte ein Vorsteuerabzug nicht auf eine Rechnung gestützt werden, die nicht  die in § 11 UStG 1994 geforderten Angaben enthielt. Jüngst (vgl. VwGH 29.5.2018, Ra  2016/15/0068;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_106`)


21.11.2018, Ro 2016/13/0020) erklärte der Verwaltungsgerichtshof hingegen  unter Bezugnahme auf die in der Zwischenzeit ergangenen Urteile des EuGH, dass die  Steuerverwaltung das Recht auf Vorsteuerabzug nicht allein deswegen verweigern darf, weil  7 von 9 Seite 8 von 9

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_112`)


Der Verwaltungsgerichtshof hat in  seiner Rechtsprechung darauf hingewiesen, dass der Inhalt des Begriffs der „Vermietung und  Verpachtung“ in § 2 Abs. 3 UStG 1994 sich vom übrigen Vermietungsbegriff im UStG  unterscheidet und enger auszulegen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_131`)


Gegen eine Entscheidung des Bundesfinanzgerichts ist gemäß Art. 133 Abs. 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wurde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_132`)


Da sich das Erkenntnis auf die oben genannte Rechtsprechung des  Verwaltungsgerichtshofes stützt, ist keine Revision zuzulassen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_5`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133   Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_377`)


V. Erwägungen:  Nach der Judikatur des Verwaltungsgerichtshofes (siehe zB Erkenntnis 21.5.1996, 95/11/0378)  ist das Lenken von im Ausland zugelassenen Kraftfahrzeugen (und zwar in einem der  Mitgliedsstaaten eines der in § 82 Abs. 1 KFG 1967 genannten internationalen  Übereinkommen) nach Maßgabe des § 82 KFG 1967 erlaubt, also ohne dauernden Standort in  Österreich bis zu einer Höchstdauer von 1 Jahr (§ 79 Abs. 1 KFG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_441`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_14`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes beeinträchtigt die Auflösung  einer Personenhandelsgesellschaft und ihre Löschung im Firmenbuch jedenfalls solange ihre  Parteifähigkeit nicht, als ihre Rechtsverhältnisse zu Dritten noch nicht abgewickelt sind (VwGH  27.05.1999, 99/15/0014, mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_15`)


Von einem Verlust der Parteifähigkeit ist dann auszugehen, wenn die Personengesellschaft des  Unternehmensrechts beendet wird und ein Gesamtrechtsnachfolger vorhanden ist, wie dies  etwa nach der Rechtsprechung des Verwaltungsgerichtshofes bei einer Vermögensübernahme  nach § 142 UGB der Fall ist (VwGH 23.01.2019, Ra 2017/13/0033, mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_24`)


Er ist jedoch nicht an die X-KG, sondern an die Roxana Dellner  adressiert und daher inhaltlich  rechtswidrig, weil entgegen der Ansicht der belangten Behörde nach der Judikatur des  Verwaltungsgerichtshofes das Vorliegen einer Gesamtrechtsnachfolge zu verneinen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `X-KG` (organisation)
- `Roxana Dellner` (person)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_27`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_28`)


Das Bundesfinanzgericht folgt mit seinem Erkenntnis hinsichtlich der Frage, ob im Fall der  Einbringung eines Betriebes gemäß Art. III UmgrStG die übernehmende Gesellschaft  Rechtsnachfolgerin der Einbringenden wird, der Judikatur des Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_60`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_7`)


Die ordentliche Revision an den Verwaltungsgerichtshof nach Art 133 Abs 4 B-VG ist nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_84`)


Ein Betrag ist nach ständiger Rechtsprechung des Verwaltungsgerichtshofes unter dem  Gesichtspunkt des § 19 Abs 1 EStG als zugeflossen anzusehen, wenn der Empfänger über ihn  tatsächlich und rechtlich verfügen kann (VwGH 13.12.1995, 95/13/0246 mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_107`)


Zur Unzulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_173`)


D. Zulässigkeit einer Revision  Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art 133 Abs 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_174`)


Zur gegenständlichen Rechtsfrage existiert umfangreiche und eindeutige Judikatur des  Verwaltungsgerichtshofes, auf die sich das gegenständliche Erkenntnis stützt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_19`)


Ich hatte Ihnen in meinem Brief vom 12.4.2018 hierzu den Hinweis auf die Rechtsprechung des  Verwaltungsgerichtshofes gegeben, auf die ich mich berufe.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_39`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (siehe dazu die bei Doralt, EStG  Kommentar, § 16 Tz 220 "Versicherungen" angeführten Judikate, wie zB VwGH vom  22.10.1991, 91/14/0043) sind Prämien für eine Berufsunfähigkeitsversicherung lediglich dann  als Werbungskosten abzugsfähig, wenn ausschließlich die Berufsunfähigkeit infolge eines  typischen Berufsrisikos versichert wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_70`)


Zulässigkeit einer Revision   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_72`)


Das Bundesfinanzgericht orientierte  sich bei den zu lösenden Rechtsfragen an der zitierten eindeutigen Rechtsprechung des  Verwaltungsgerichtshofes, darüber hinaus hing die Entscheidung im Wesentlichen von den  Umständen des Einzelfalles ab.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_73`)


Die Revision an den Verwaltungsgerichtshof ist daher  unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

</details>

---

## `Courts - Verfassungsgerichtshof` 🏆

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Rule ID:** `fc0dac07`  
**Description:**
Matches the Constitutional Court, handling genitive case endings.

**Content:**
```
\b(Verfassungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.015 | 0.029 | 172 | 172 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 172 | 0 | 11624 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_25`)


Ist ein Gesetz wegen Verfassungswidrigkeit aufgehoben worden oder hat der  Verfassungsgerichtshof gemäß Art. 140 B-VG Abs. 4 ausgesprochen, dass ein Gesetz  verfassungswidrig war, so sind alle Gerichte und Verwaltungsbehörden an den Spruch des  Verfassungsgerichtshofes gebunden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_26`)


Auf die vor der Aufhebung verwirklichten Tatbestände  mit Ausnahme des Anlassfalles ist jedoch das Gesetz weiterhin anzuwenden, sofern der  Verfassungsgerichtshof nicht in seinem aufhebenden Erkenntnis anderes ausspricht (Art. 140  Abs. 7 B-VG).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_116`)


Der Verfassungsgerichtshof spricht aus, dass Verfahren verwehrt sind, die zu  zufallsabhängigen und willkürlichen Ergebnissen führen (VfSlG 18.093/2007).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_128`)


Auf Grund dieser Ausführungen des Verfassungsgerichtshofes hat das Bundesfinanzgericht  keine verfassungsrechtlichen Bedenken gegen die Bestimmungen Parkraumbewirtschaftung  der Stadt Wien, soweit sie im gegenständlichen Fall zur Anwendung gelangen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_250`)


Der Verfassungsgerichtshof äußerte in seinem Erkenntnis vom 10.12.2007, B 700/07, keine  verfassungsrechtlichen Bedenken gegen die Einschränkung der Beweisführung des Grades der  Behinderung oder der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu  verschaffen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_86`)


Zu den in der Beschwerde angedeuteten verfassungsrechtlichen Bedenken der Bf. war auf das  zur Thematik ergangene Erkenntnis des Verfassungsgerichtshofes vom 1.3.2001, G 109/00, zu  verweisen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_287`)


Gegen die Einschränkung der Beweisführung des Grades der Behinderung oder der  voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu verschaffen, hat der  Verfassungsgerichtshof im Erkenntnis vom 10.12.2007, B 700/07, keine verfassungsrechtlichen  Bedenken gesehen (vgl. VwGH 22.12.2011, 2009/16/0307) und weiters erkannt, dass von  Gutachten NUR nach "entsprechend qualifizierter Auseinandersetzung" abgegangen werden  20 von 21 Seite 21 von 21

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_19`)


Der Verfassungsgerichtshof hat in seiner Entscheidung vom 9. Dezember 2014 zu G 136/2014  unter Rz 105 angemerkt, dass „mit dem AbgÄG 2014 nicht nur die steuerliche Begünstigung  freiwilliger Abfertigungen iSd § 67 Abs. 6 EStG 1988 beim Empfänger eingeschränkt [wurde],  sondern in § 20 Abs. 1 Z 8 EStG 1988 auch deren Abzugsfähigkeit auf Seiten des Unternehmens  beschränkt wird.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_38`)


Judikatur des Verwaltungs- und Verfassungsgerichtshofes zum Abzugsverbot hinsichtlich  Managergehälter und „Golden Handshakes“ sowie auf Ansichten im Schrifttum.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_93`)


Zur der im Außenprüfungsbericht bzw in der Beschwerde angeführten Judikatur der  Höchstgerichte und des BFG ist vorab festzuhalten:  Der Verfassungsgerichtshof hat im Erkenntnis vom 9. Dezember 2014, G 136/2014-25, G  166/2014-20, G 186/2014-23, das Betriebsausgabenabzugsverbot für freiwillige Abfertigungen  als verfassungskonform bestätigt (siehe Rn 107).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_78`)


(Bei der vorliegenden Entscheidung des Bundesfinanzgerichtes tritt nach  herrschender Meinung mit der Zustellung sofort die Rechtskraft ein, weil die mögliche  Beschwerde an den Verfassungsgerichtshof kein ordentliches, sondern ein außerordentliches  Rechtsmittel wäre.)

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_14`)


Gegen diesen Beschluss habe er  einen Antrag auf Verfahrenshilfe beim Verfassungsgerichtshof gestellt. Er habe noch keine  Antwort vom Verfassungsgerichtshof bekommen, weder eine Ablehnung noch eine Zusage.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_54`)


Parken in einer gebührenpflichtigen Kurzparkzone am Gehsteig  Nach der höchstgerichtlichen Judikatur des Verfassungsgerichtshofes (VfGH) und des Ver- waltungsgerichtshofes (VwGH) dürfen innerhalb einer Kurzparkzone noch weitergehende  Verkehrsbeschränkungen wie Halte- oder Parkverbote erlassen werden, ohne dass das Gebiet  der Kurzparkzone dadurch unterbrochen wird (vgl. VfGH 06.12.1965, B 210/65, VwGH (vgl.  VwGH 14.02.1979, 892/78, VwGH 27.04.1995, 92/17/0300, VwGH 31.07.2003, 2003/17/0110).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_111`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_41`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Stattgabe)  Als Folge der Aufhebung der in § 295 Abs. 4 BAO idF BGBl. I Nr. 76/2011 bzw 70/2013  normierten Antragsfrist durch den Verfassungsgerichtshof mit Erkenntnis vom 4. Dezember  2019, G 159/2019 ua, hat der Gesetzgeber § 295 Abs. 4 BAO mit BGBl. I Nr. 3/2021 wie folgt  neu gefasst:  „(4) Wird eine Bescheidbeschwerde, die gegen ein Dokument, das Form und Inhalt   eines Feststellungsbescheides (§ 188) oder   eines Bescheides, wonach eine solche Feststellung zu unterbleiben hat,  gerichtet ist, als unzulässig zurückgewiesen, weil das Dokument kein Bescheid ist, sind auf das  Dokument gestützte Bescheide auf Antrag der Partei aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_62`)


Auf diese (vgl VwGH vom  24. September 2014, 2011/13/0061) hat auch der Verfassungsgerichtshof in seinen dem  Prüfungsbeschluss zu G 159/2019 zugrundeliegenden Bedenken (Pkt 3.2.4.) hingewiesen und  ausgeführt, dass in einem solchen Fall, „dieser ‚abgeleitete‘ Bescheid doch ohne  Rechtsgrundlage in die Rechtskraft des dem ‚abgeleiteten‘

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_76`)


Information für die Parteien  (Belehrung gemäß § 280 Abs. 4 BAO)  Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_112`)


Diese Rückwirkungsanordnung wurde vom Verfassungsgerichtshof mit Erkenntnis vom  2.12.2014, G 72/2014, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_87`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_8`)


Der Verfassungsgerichtshof habe die alternativlose  Individualbesteuerung bisher immer als verfassungskonform judiziert (VfSlg 13.067/1992 und  13.297/1992).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_10`)


Bei dieser Sichtweise habe der Verfassungsgerichtshof außer Acht gelassen, dass die elterliche  Unterhalts- und Fürsorgepflicht die „private Lebensgestaltung“ der Eltern in einer Weise  mitbestimme, dass von der privaten Lebensgestaltung nur wenig übrigbleibe.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_27`)


Abschließend regte der Beschwerdeführer das Bundesfinanzgericht an, dieses möge das  Einkommensteuergesetz gemäß Art 140 Abs 1 Z 1 lit a B-VG beim Verfassungsgerichtshof  anfechten, weil es für ein vormals erziehendes Elternpaar keine Splitting-Option vorsehe und  den verfahrensgegenständlichen Einkommensteuerbescheid für das Jahr 2017 entsprechend  abändern.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_37`)


Wie der OGH schon wiederholt erkannt hat, ist unabdingbare Voraussetzung der Anrufung des  Verfassungsgerichtshofes, dass das Gericht selbst Bedenken gegen die Verfassungsmäßigkeit  des anzuwendenden Gesetzes bzw. die Gesetzmäßigkeit der anzuwendenden Verordnung hat;  der Umstand allein, dass eine Partei solche Bedenken vorbringt (oder dass im Schrifttum  Bedenken geäußert worden sind), berechtigt oder verpflichtet das Gericht noch nicht zur  Normenprüfung.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_38`)


Der Verfassungsgerichtshof hat bereits für die insoweit vergleichbare Rechtslage des Jahres  2000 festgestellt, dass durch Transferzahlungen eine hinreichende Entlastungswirkung für  Familien vorliegt, unabhängig davon, welchem Elternteil die Transferleistungen ausbezahlt  würden (VfGH 12.12.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_46`)


Die vom Beschwerdeführer aufgeworfene Frage der Verfassungskonformität der gesetzlichen  Bestimmungen stellt keine Rechtsfrage im Sinne der Subsumption unter einen gesetzlichen  Tatbestand dar, die vom Verwaltungsgerichtshof zu überprüfen ist, sondern ist deren Prüfung  dem Verfassungsgerichtshof vorbehalten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_157`)


Abgesehen davon wird festgehalten, dass der Verfassungsgerichtshof in gleichgelagerten Fällen  (Internetglücksspiel) in Bezug auf die Glücksspielabgabe gern.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_199`)


Abgesehen davon wird festgehalten, dass der Verfassungsgerichtshof in gleichgelagerten Fällen  (Internetglücksspiel) in Bezug auf die Glücksspielabgabe gern.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_229`)


Abgesehen davon wird festgehalten, dass der Verfassungsgerichtshof in gleichgelagerten Fällen  (Internetglücksspiel) in Bezug auf die Glücksspielabgabe gern.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_281`)


Der Verfassungsgerichtshof hat in Fällen betreffend Online Glücksspiel/Wetten in Bezug auf die  Glücksspielabgabe gem. § 57 Abs. 1 und 2 GSpG bzw. die Wettgebühr gem. § 33 TP 17 GebG  und die Ausgestaltung der Abgabetatbestände („Teilnahme vom Inland aus“) keine Bedenken  und hat mit Beschlüssen jeweils vom 26.02.2018, E 3389/2017 und E 2913/2017 (Bezug zu BFG  RV/7100702/2016 und RV/7104383/2015) und die Beschluss vom 24.09.2018, E 2251/2017,  20 von 48 Seite 21 von 48

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_547`)


2. Zu den verfassungsrechtlichen Einwänden der Bf.   Gemäß Art. 140 Abs. 1 Z 1 lit. a B-VG erkennt der Verfassungsgerichtshof auf Antrag eines  Verwaltungsgerichtes über die Verfassungsmäßigkeit von Gesetzen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_548`)


Nach dem sinngemäß  anzuwendenden Art. 89 B-VG hat das Verwaltungsgericht bei verfassungsrechtlichen Bedenken  gegen die Anwendung einer innerstaatlichen Norm (Gesetz oder Verordnung) einen Antrag auf  Aufhebung dieser Norm beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_549`)


Ob Bedenken gegen die  Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit bestehen ist nach  objektiven Gesichtspunkten zu prüfen, wobei auch die Art der in Frage stehenden Norm und  ihre Position im Normenzusammenhang in Betracht zu ziehen und auf die bisherige  Rechtsprechung des Verfassungsgerichtshofes Bedacht zu nehmen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_555`)


Nach der ständigen  Rechtsprechung des Verfassungsgerichtshofes (zB VfSlg.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_558`)


Für eine verfassungsrechtliche Unbedenklichkeit der hier anzuwendenden Bestimmungen  spricht überdies, dass der Verfassungsgerichtshof in vergleichbaren Fällen betreffend  Wettgebühren und Glücksspielabgabe die Behandlung der jeweiligen Beschwerde abgelehnt  hat (ua VfGH 21.11.2013, B 618/2013;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_122`)


Darüberhinaus regte der Bf an, den Antrag an den Verfassungsgerichtshof zu stellen, die  Kundmachung des BMF zur GZ: BMF-010202/0100-VI/3/2014 und GZ.BMF-010202/0104-

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BMF` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_296`)


Vom Bf behauptete Verfassungswidrigkeit   Der Bf regte an, den Antrag an den Verfassungsgerichtshof zu stellen, die Kundmachung des  BMF zur GZ. BMF-010202/0100-VI/3/2014 und GZ. BMF-010202/0104-VI/3/2014 wegen  Gesetzwidrigkeit sowie die Bestimmung des § 38 Abs 1 BeWG wegen Verfassungswidrigkeit  aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BMF` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_309`)


In diesem Zusammenhang ist auch festzuhalten, dass das Bundesfinanzgericht immer wieder -  in Anlehnung an die Rechtsprechung des Verfassungsgerichtshofes - zum Ausdruck gebracht,  dass es keine Zweifel an der Verfassungsmäßigkeit des Bewertungsgesetzes hegt (vgl. BFG  10.01.2017, RV/4100647/2016, mwN;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_313`)


Nach Ansicht des Verfassungsgerichtshofes liegt es auch im rechtspolitischen Spielraum des  Steuergesetzgebers, Grundbesitz einer speziellen Vermögenssteuer zu unterwerfen, auch  wenn andere Vermögenswerte einer vergleichbaren Steuer nicht unterliegen und eine solche  Steuer als Objektsteuer – das bedeutet unabhängig von den persönlichen Verhältnissen des  Grundeigentümers – auszugestalten (siehe dazu VfGH 06.10.2010, B 298/10).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_314`)


Festzuhalten ist auch, dass der Verfassungsgerichtshof das System der Einheitsbewertung  daher nicht grundsätzlich in Frage gestellt hat, sondern nur die „historischen Einheitswerte“ als  ungeeignete Bemessungsgrundlage für die Abgabenbemessung angesehen hat (vgl. zB VfGH  02.03.2011, G 150/10).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_315`)


Der Verfassungsgerichtshof hat vielmehr klargestellt, dass ein Bewertungsverfahren, das das  Ziel verfolgt, Werte für bestimmte wirtschaftliche Einheiten oder Wirtschaftsgüter zu  bestimmten Stichtagen mit verbindlicher Wirkung für einen längeren Zeitraum und für  mehrere Abgaben festzustellen, vielmehr der Verwaltungsökonomie dient (VfGH 07.03.2007, G  54/06).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_316`)


Der vom Bf angeregte Antrag an den Verfassungsgerichtshof betreffend der Kundmachung des  BMF GZ. BMF-010202/0104-VI/3/2014 wegen Gesetzwidrigkeit erübrigt sich jedenfalls:   Der Verfassungsgerichtshof hat schon mit Beschluss VfGH vom 26.11.2018, E 479/2017 die  Behandlung einer Beschwerde, die gegen das Erkenntnis des BFG vom 10.1.2017,  RV/4100647/2016 eingebracht wurde, in der der Bf ua Verfassungswidrigkeit und Verletzung  des Gleichheitsgrundsatzes hinsichtlich genau dieser der Kundmachung des  Bundesministeriums für Finanzen vom 05.03.2014 (BZ. BMF-010202/0104-VI/3/2014)  behauptete, abgelehnt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BMF` (organisation)
- `BFG` (organisation)
- `Bundesministeriums für Finanzen` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_59`)


Soweit die Beschwerde verfassungsrechtliche - insbesondere gleichheitsrechtliche - Aspekte ins  Treffen führt, ist auf den Ablehnungsbeschluss des Verfassungsgerichtshofes vom  29. November 2011 zu verweisen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_98`)


Gegen die Einschränkung der Beweisführung des Grades der Behinderung oder  der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu verschaffen, hat der  Verfassungsgerichtshof im Erkenntnis vom 10.12.2007, B 700/07, keine verfassungsrechtlichen  Bedenken gesehen (vgl. VwGH 22.12.2011, 2009/16/0307).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_147`)


Diese beiden Merkmale gehen nach der vom Verfassungsgerichtshof in seinem  Erkenntnis vom 1. März 2001 zum Ausdruck gebrachten Sichtweise, der sich der  Verwaltungsgerichtshof anschließt, nicht in einem Oberbegriff der Weisungsunterworfenheit  auf.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_148`)


In den hg. Erkenntnissen vom 17. Mai 1989, 85/13/0110, Slg. NF. Nr. 6.403/F (zitiert im  genannten Erkenntnis des Verfassungsgerichtshofes), vom 31. Juli 1996, 95/13/0220, Slg. NF.  Nr. 7.111/F, vom 9. Juli 1997, 95/13/0289, vom 23. Mai 2000, 97/14/0167, vom 20. Dezember  2000, 99/13/0223, Slg. NF. Nr. 7.569/F, vom 25. Jänner 2001, 95/15/0074, und zuletzt vom 24.  Juni 2004, 2001/15/0113, hat der Verwaltungsgerichtshof ausgesprochen, dass (nur) in Fällen,  in denen die im Gesetz festgeschriebenen Kriterien der Weisungsgebundenheit und der  Eingliederung in den geschäftlichen Organismus des Betriebes des Arbeitgebers noch keine  klare Abgrenzung zwischen einer selbständig und einer nichtselbständig ausgeübten Tätigkeit  ermöglichen, auf weitere Abgrenzungskriterien (wie etwa auf das Fehlen eines  Unternehmerrisikos) Bedacht zu nehmen ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_35`)


Diese Rechtsauffassung (des BF) teile auch der Verfassungsgerichtshof in seiner Entscheidung  G 131/2017 vom 30.11.2017, mit welcher § 304 BAO (in der vom Finanzamt herangezogenen  Fassung) als verfassungswidrig aufgehoben worden sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_36`)


Der Verfassungsgerichtshof habe beanstandet, dass die aufgehobene Bestimmung eben nicht  der Tatsache Rechnung trage, dass - wie auch hier vorliegend - die Möglichkeit einer  Wiederaufnahme bei langer Verfahrensdauer in vielen Fällen faktisch ausgeschlossen sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_40`)


Es kann also laut Verfassungsgerichtshof leicht  der Fall eintreten, dass die Abgabe zu einem Zeitpunkt festgesetzt werde, in dem die  ununterbrochene 10-Jahresfrist bereits abgelaufen sei, was eben auch in concreto der Fall ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_51`)


Die Neuregelungen des § 304 BAO nach  Aufhebung durch den Verfassungsgerichtshof sei auf Grund einer Übergangsbestimmung erst  mit 1.1.2019 in Kraft getreten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_131`)


27.02.2017 Antrag auf Wiederaufnahme des Verfahrens betreffend  Einkommensteuer gemäß § 303 Abs. 1 BAO   21.11.2017  Bericht über das Ergebnis der Außenprüfung, die aus Anlass des  oben genannten Erkenntnisses bzw. Beschlusses und des  streitgegenständlichen Wiederaufnahmeantrages durchgeführt  worden ist  23. November  2017  Abweisung des Antrages gemäß § 303 Abs. 1 BAO unter Hinweis  auf den obigen Bericht wegen Verjährung  05. Dezember  2017  Antrag auf Bescheidbegründung  18. Dezember  2017  Mitteilung einer Bescheidbegründung  22. Dezember  2017  Beschwerde  26. März 2018 Beschwerdevorentscheidung  23. April 2018 Vorlageantrag  Der Vollständigkeit halber wird angemerkt, dass das Bundesfinanzgericht mittlerweile mit  Erkenntnis vom 04.10.2021, RV/4100940/2018, (u.a.) betreffend die Jahre 2003 – 2009 eine  Sachentscheidung getroffen hat, gegen die beim Verfassungsgerichtshof zur GZ. E 4202/2021  Beschwerde erhoben worden ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_157`)


Nun hat aber der Verfassungsgerichtshof – was auch im Vorlageantrag und in der mündlichen  Verhandlung hervorgehoben worden ist – die angesprochene Bestimmung mit Erkenntnis vom  30.11.2017, G 131/2917, G 286/201, als verfassungswidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_11`)


Mit Schreiben des Verfassungsgerichtshofes vom 12.10.2021 wurde dem Bf. der Beschluss des  Verfassungsgerichtshofes betreffend Normenprüfung vom 22.09.2021 übermittelt sowie die  Aufforderung, die noch offene Eingabengebühr von € 240,- binnen einer Woche zu bezahlen  und den Original-Einzahlungsbeleg innerhalb von 10 Tagen dem Verfassungsgerichtshof zu  übermitteln.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_12`)


Da dies nicht erfolgte wurde mit amtlichem Befund vom 01.12.2021, eingelangt am  07.12.2021, das Finanzamt Österreich, Dienststelle für Sonderzuständigkeiten, vom  Verfassungsgerichtshof über die Nichtentrichtung der Gebühr informiert.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_17`)


Dieser Antrag wurde dem Verfassungsgerichtshof zur Normenprüfung vorgelegt und erging am  22.09.2021 der Beschluss des Verfassungsgerichtshofes mit welchem der Antrag des Bf.  zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_18`)


Gleichzeitig wurde der Bf. aufgefordert die bereits fällige, aber noch nicht entrichtete  Eingabegebühr von € 240 für die Eingabe des Bf. an den VfGH zu überweisen und dazu den  Original-Einzahlungsbeleg innerhalb von 10 Tagen dem Verfassungsgerichtshof zu übermitteln.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_25`)


Zu Spruchpunkt I.   Bescheid betreffend Gebühr nach § 17a VfGG  Für Eingaben an den Verfassungsgerichtshof ist gemäß § 17a Verfassungsgerichtshofgesetz  eine Gebühr zu entrichten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_26`)


Nach dieser Bestimmung ist für beim Verfassungsgerichtshof eingebrachte Beschwerden  spätestens im Zeitpunkt der Überreichung eine Gebühr in der Höhe von € 240,00 zu  entrichten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_32`)


Wie der Verfassungsgerichtshof letztendlich mit der Beschwerde verfährt, ist auf das Entstehen  der Gebührenschuld ohne Einfluss.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_33`)


Somit vermag der Umstand, dass der Gerichtshof in  vorliegendem Fall die Beschwerde zurückgewiesen hat, an der Entstehung der Gebührenschuld  zum Zeitpunkt des Einlangens der Beschwerde beim Verfassungsgerichtshof nichts zu ändern.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_34`)


Die gegenständliche Beschwerde ist am 05.08.2021 beim Verfassungsgerichtshof eingelangt;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_36`)


Mit Schreiben vom 12.10.2021 wurde der Bf. vom Verfassungsgerichtshof aufgefordert, die  Eingabengebühr in Höhe von € 240 binnen einer Woche zu entrichten und den  Einzahlungsbeleg dem Verfassungsgerichtshof zu übermitteln.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_142`)


Der Verfassungsgerichtshof hob mit Erkenntnis vom 02.12.2014 (G 72/2014) hinsichtlich der  Rückwirkungsanordnung die Bestimmung des § 135 Abs 27 KFG 1967 als verfassungswidrig auf  und sprach aus, dass die aufgehobene Bestimmung nicht mehr anzuwenden sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_73`)


Die Einbeziehung des Wochengeldes in die Einkünftegrenze des § 33 Abs 4 Z 1  EStG erfolgte in Reaktion auf das Erkenntnis des Verfassungsgerichtshofes vom 12.12.1998,  G 198/98.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_74`)


Im zitierten Erkenntnis hat der Verfassungsgerichtshof Teile des seinerzeitigen § 33  Abs 4 Z 1 EStG 1988 aufgehoben und zum Ausdruck gebracht, ungeachtet des  einkommensteuerrechtlichen Grundsatzes, Einkommensersatz wie Erwerbseinkommen zu  besteuern, sei die Ausnahme der Steuerpflicht für das Wochengeld im Hinblick darauf  gerechtfertigt, dass es sich nach dem Nettoarbeitsverdienst bemesse.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Amtlicher Befund  Am 13.07.2022 langte beim Finanzamt Österreich, Dienststelle Sonderzuständigkeiten, ein  “Amtlicher Befund über eine Verkürzung von Stempel- und Rechtsgebühren“ des  Verfassungsgerichtshofes (kurz: VfGH) ein.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_14`)


Zur Begründung wurde vorgebracht, dass am 28.02.2022 beim  Verfassungsgerichtshof ein Antrag auf Bewilligung der Verfahrenshilfe in vollem Umfang samt  Gebührenbefreiung eingebracht worden sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_25`)


Da laut amtlichen Befund des Verfassungsgerichtshofs vom 29.06.2022 insgesamt zwei  Eingaben unter den Zahlen E 1037/2022 und G 148/2022 eingebracht wurden und trotz  Aufforderung vom Verfassungsgerichtshof vom 22.06.2022 kein Einzahlungsbeleg vorgelegt  wurde, war die Gebühr zu Recht mittels Gebührenbescheid samt Bescheid über eine  Gebührenerhöhung vorzuschreiben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofs` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_26`)


Der in der Beschwerde vom 10.11.2022 angeführte Antrag, auf Bewilligung der Verfahrenshilfe,  welcher am 28.02.2022 beim Verfassungsgerichtshof eingebracht wurde, wurde bereits mit  Beschluss vom 05.04.2022 vom Verfassungsgerichtshof abweislich entschieden und wurde  Ihnen dies nochmals mit Schreiben vom 06.07.2022 vom Verfassungsgerichtshof mitgeteilt.“

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_55`)


soweit eine andere  Form der Einbringung für zulässig erklärt ist (§ 14a Abs. 2), ist der Zeitpunkt des Einlangens in  den elektronischen Verfügungsbereich des Verfassungsgerichtshofes maßgeblich.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_69`)


Anträge nach § 15 Abs. 1 VfGG sind an den Verfassungsgerichtshof gemäß den Art. 126a, 127c  Z 1, 137 bis 145, 148f und 148i B-VG gerichtete Anträge.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_12`)


Wie bereits der Verfassungsgerichtshof in seinem Beschluss vom 26.01.2023, E 255/2023, zum  gleichlautenden Antrag auf aufschiebende Wirkung erkannt hat, ist das Vorbringen des  Revisionswerbers nicht geeignet, einen unverhältnismäßigen Nachteil durch den Vollzug des  angefochtenen Erkenntnisses darzutun, weil der Revisionswerber es verabsäumt hat, seine  konkreten Einkommens- und Vermögensverhältnisse darzulegen und zu bescheinigen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_78`)


von Rechtsauslegungen des Verfassungsgerichtshofes oder des Verwaltungsgerichtshofes  abweicht, wenn im Vertrauen auf die betreffende Rechtsprechung für die Verwirklichung des  die Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_82`)


Im Hinblick darauf wird auf das Erkenntnis des  Verfassungsgerichtshofes (VfGH 04.12.2001, B 2366/00) verwiesen, wonach gegen eine  Vorschrift, die bewirkt, dass Personen, die im Ausland (Drittland) lebenden Kindern gegenüber  zu Unterhaltsleistungen verpflichtet sind, keine Familienbeihilfe gewährt wird, keine  verfassungsrechtlichen Bedenken bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_45`)


Der Verfassungsgerichtshof hegte  gegen diese Erweiterung der automatisierten Datenverarbeitung keine verfassungsrechtlichen  Bedenken (VfGH 1. März 1974, B 331/73).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_46`)


Ebenso wenig hegte der Verfassungsgerichtshof  Bedenken gegen die dem § 96 BAO idF BGBl

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_49`)


Nach Ansicht des Verfassungsgerichtshofes beeinträchtigt es weder die rechtsstaatlichen  Funktionen des Bescheides noch wird der verfassungsrechtlich gewährleistete  Rechtsschutzstandard dadurch verringert, dass ein Bescheid kraft Gesetzes eines bestimmten  genehmigenden Organwalters oder dessen Benennung bzw Unterschrift entbehrt, solange die  Zurechnung des Bescheides zu einer bestimmten Behörde dadurch nicht gefährdet wird.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_58`)


E-Mail-Einbringung  Gemäß Art 135 Abs 4 B-VG iVm Art 89 B-VG steht die Prüfung der Gültigkeit gehörig  kundgemachter Verordnungen und Gesetze den Verwaltungsgerichten nicht zu. Hat ein solches  Gericht gegen die Anwendung einer Verordnung aus dem Grund der Gesetzwidrigkeit oder  eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so hat es den Antrag auf  Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_70`)


Dies insbesondere als der Verfassungsgerichtshof mit  Ablehnungsbeschluss vom 13. März 2019, E 375/2019-5 begründend wie folgt ausgeführt hat:   "Entgegen der Auffassung der Beschwerdeführer folgt aus der Zulässigkeit der Einreichung von  Anbringen unter Verwendung eines Telefaxgerätes (vgl. § 1 der VO BGBl. 494/1991 idF BGBl. II  395/2002) für den Verordnungsgeber kein verfassungsrechtliches Gebot, für das  Abgabenverfahren neben der Einreichung von Anbringen in automationsunterstützter Form im  Rahmen der FinanzOnline-Verordnung 2006 – FonV 2006, BGBl. II 97/2006 idF BGBl. II 82/2011,  Eingaben per E-Mail für zulässig zu erklären."

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_49`)


Daraus habe der  Verfassungsgerichtshof (VfGH) ein allgemeines und umfassendes verfassungsrechtliches  Sachlichkeitsgebot abgeleitet, dem jedes Staatshandeln entsprechen müsse.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_53`)


Der Verfassungsgerichtshof  hege keinen Zweifel daran, dass es sich bei Art 21 Abs. 1 GRC - vgl auch Art 7 Abs. 1 B-VG und  Art 14 EMRK - um eine Garantie der GRC handle, die in ihrer Formulierung und Bestimmtheit  verfassungsgesetzlich gewährleisteten Rechten der österreichischen Bundesverfassung gleiche,  mithin keine völlig unterschiedliche normative Struktur als diese aufweise.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_265`)


auch die von der Grundrechte-Charta garantierten Rechte vor dem Verfassungsgerichtshof als  verfassungsgesetzlich gewährleistete Rechte gemäß Art 144 bzw Art 144a B-VG geltend  gemacht werden könnten und sie im Anwendungsbereich der Grundrechte-Charta einen  Prüfungsmaßstab in Verfahren der generellen Normenkontrolle, insbesondere nach Art 139  und Art 140 B-VG bildeten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_274`)


Sollte das zuständige Verwaltungsgericht die verfassungsrechtlichen Bedenken der Bf gegen  die präjudiziellen Bestimmungen teilen, möge es an den Verfassungsgerichtshof gemäß Art 135  Abs 4 iVm Art 89 Abs 2 B-VG und Art 140 Abs 1 B-VG einen Antrag auf Aufhebung der  präjudiziellen Bestimmungen des EKBSG idgF wegen Verfassungswidrigkeit richten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_297`)


Gemäß Art. 89 Abs. 2 B-VG hat ein ordentliches Gericht, wenn es gegen die Anwendung eines  Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat, den Antrag auf Aufhebung  dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_346`)


Nach der ständigen Rechtsprechung des Verfassungsgerichtshofes  verletzen zwar gesetzliche Vorschriften, die nachträglich an früher verwirklichte Tatbestände  steuerliche Folgen knüpfen und dadurch die Rechtsposition des Steuerpflichtigen mit Wirkung  für die Vergangenheit verschlechtern, im Allgemeinen den Gleichheitssatz, wenn der Eingriff  von erheblichem Gewicht ist und der Steuerpflichtige in einem berechtigten Vertrauen auf die  Rechtslage enttäuscht wurde (z.B. VfGH 19.6.1996, B2756/94).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_357`)


Aus den dargelegten Gründen bestand kein Anlass, gemäß Art. 89 Abs. 2 B-VG einen  Aufhebungsantrag an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_127`)


Gegen dessen Entscheidung stehen Beschwerde an den  Verfassungsgerichtshof oder (nach Zulassung oder in Gestalt und unter den Voraussetzungen  einer außerordentlichen) Revision an den Verwaltungsgerichtshof offen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_200`)


Nach dem grundlegenden Erkenntnis des Verfassungsgerichtshofes vom  25. September 1996, B 4016/95, zur auf § 68 Abs. 1 AVG bezogenen „res judicata“ bleibt diese  Möglichkeit jedenfalls bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_236`)


Dies bedeutet - zuerst - dass diese, in der Diktion des Verfassungsgerichtshofes,  17 von 21 Seite 18 von 21

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/144676.1`) (sent_id: `deanon_BFG_20260814_TEST/144676.1_189`)


Aus den dargelegten Gründen besteht kein Anlass, gemäß Art. 89 Abs. 2 B-VG einen  Aufhebungsantrag an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/144931.1`) (sent_id: `deanon_BFG_20260814_TEST/144931.1_51`)


Außerdem  wäre ihm das Rechtsmittel der Entscheidungsbeschwerde an den Verfassungsgerichtshof offen  gestanden, wenn er sich in seinen verfassungsrechtlich gewährleisteten Rechten verletzt  gefühlt hätte.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_55`)


Schließlich ist der Anregung des Beschwerdeführers, das Bundesfinanzgericht möge einen  Antrag auf Normenkontrolle beim Verfassungsgerichtshof stellen, folgendermaßen zu  begegnen:   Nach Art 140 Abs 1 Z 1 lit a des Bundes-Verfassungsgesetzes (B-VG) erkennt der  Verfassungsgerichtshof auf Antrag eines Gerichtes über die Verfassungswidrigkeit von  Gesetzen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_61`)


Der Anregung des Beschwerdeführers, einen Normenprüfungsantrag beim  Verfassungsgerichtshof zu stellen, kann sohin nicht nachgekommen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_62`)


Der  Beschwerdeführer wird vielmehr auf die durch Art 144 B-VG eröffnete Möglichkeit der  Erhebung einer Erkenntnisbeschwerde an den Verfassungsgerichtshof verwiesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_48`)


Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig (vgl VwGH 20.9.2023,  Ro 2023/13/0015).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_333`)


Anregungen  Sollte das zuständige Verwaltungsgericht die verfassungsrechtlichen Bedenken der  beschwerdeführenden GmbH gegen die präjudiziellen Bestimmungen teilen, möge es an den  Verfassungsgerichtshof gem Art 135 Abs 4 iVm Art 89 Abs 2 B-VG und Art 140 Abs 1 B-VG einen  Antrag auf Aufhebung der präjudiziellen Bestimmungen des EKBSG idgF wegen  Verfassungswidrigkeit richte.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_437`)


Gemäß Art 89 Abs 2 B-VG hat ein ordentliches Gericht, wenn es gegen die Anwendung eines  Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat, den Antrag auf Aufhebung  dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_612`)


Resümee  Aus den dargelegten Gründen bestand kein Anlass, einen Aufhebungsantrag gemäß Art 89 Abs  2 B-VG betreffend das EKBSG an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `City Authority - Magistrat der Stadt Wien` 🏆

**F1:** 0.043 | **Precision:** 0.992 | **Recall:** 0.022  

**Format:** `regex`  
**Rule ID:** `c6362907`  
**Description:**
Matches the City Administration (Magistrat/Magistrates) with the full city name and optional extension.

**Content:**
```
\b(Magistrat(?:s)?(?:\s+der\s+Stadt\s+Wien)(?:\s*,\s*Magistratsabteilung\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.992 | 0.022 | 0.043 | 260 | 258 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 258 | 2 | 11538 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Mag. Alexander Rimser` (person)
- `Hermann` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_4`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (€ 12,00) ist zusammen mit der  Geldstrafe iHv € 60,00 und dem Beitrag zu den Kosten des erstinstanzlichen Verfahrens  (€ 10,00), insgesamt somit € 82,00, binnen einer Frist von zwei Wochen nach Zustellung des  Straferkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_9`)


Entscheidungsgründe  Verfahrensgang:   Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien mit Strafverfügung vom  25. April 2019 angelastet, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Vienna am 25. Februar 2019 um 14:35 Uhr in der gebührenpflichtigen  Kurzparkzone in 1090 Wien, Julius-Tandler-Platz 6, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die Parkometerabgabe  fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_22`)


Diese Zeitangabe ist deshalb  glaubwürdig, weil den Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die  Erfüllung der übertragenen Aufgaben elektronische Überwachungsgeräte (sog. PDA's) zur  Verfügung stehen, welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen Server  beziehen und vorgeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_279`)


Der Magistrat der Stadt Wien ging daher zu Recht von einer zumindest fahrlässigen Verkürzung  der Parkometerabgabe iSd § 4 Abs. 1 Wiener Parkometergesetz 2006 aus.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Verwaltungsstrafsache gegen  Andrea Thünnissen, Kellergasse Helfens 32, 8074 Raaba, Österreich, vom 23. Februar 2020, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Februar 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 17. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet  abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Andrea Thünnissen` (person)
- `Kellergasse Helfens 32, 8074 Raaba, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro)  sind gemeinsam mit der Geldstrafe (60,00 Euro) und dem Beitrag zu den Kosten der  belangten Behörde (10,00 Euro), insgesamt somit 82,00 Euro, binnen zwei Wochen  nach Zustellung des Straferkenntnisses an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_4`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als  Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_8`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien unter Zugrundelegung der  Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der Landespolizeidirektion  Wien mit Strafverfügung vom 24. Dezember 2019 angelastet, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. Oktober 2019 um 09:38 Uhr  in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Dresdner Straße 89, abgestellt, ohne  für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein  gesorgt zu haben, da der Parkschein unrichtig entwertet gewesen sei.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Landespolizeidirektion  Wien` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_25`)


Auf den Einwand des Bf. bezüglich der Strafbemessung bei Geschwindigkeitsübertretungen  könne nicht eingegangen werden, weil kein sachlicher Zusammenhang bestehe, zumal diese  Delikte nicht in die Zuständigkeit des Magistrats der Stadt Wien fallen würden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_34`)


Der Magistrat der Stadt Wien legte die Beschwerde samt dem dazugehörigen Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 5. März 2020).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_172`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Roxana Dellner` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `88-034/0292` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Nach einer bei der Woytekat & Köhlen Recycling KG durchgeführten gemeinsamen Prüfung der Lohnabgaben (GPLA)  setzte der Magistrat der Stadt Wien, Magistratsabteilung 6, Rechnungs- und Abgabenwesen,  mit Bescheid vom 09. März 2017 Kommunalsteuer für den Zeitraum 2012 und 2013 fest und  adressierte den Bescheid an die Beschwerdeführerin.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Woytekat & Köhlen Recycling KG` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_5`)


III: Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_11`)


Mit Strafverfügung vom 12.3.2019 lastete der Magistrat der Stadt Wien, Magistratsabteilung  67, Techn R Tosca Häfeli, in der Folge kurz mit Bf. bezeichnet, folgende Verwaltungsübertretung an:  "1. Datum/Zeit:  06.06.2018, 09:29 Uhr   Ort:   TATORT   betroffenes Fahrzeug: KENNZ (A)   Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den   Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder   Wochenpauschalkarte) gesorgt zu haben, da der im Fahrzeug angebrachte   Parkausweis für Behinderte gemäß § 29b der StVO kein Original war.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung  67` | `Magistrat der Stadt Wien, Magistratsabteilung  67` |

**Missed by this rule (FN):**

- `Techn R Tosca Häfeli` (person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_85`)


Das Magistrat der Stadt Wien, Magistratsabteilung 67, erließ am 6.11.2019 ein Straferkenntnis,  Zahl GESCHÄFTSZAHL, in welchem die dem Bf. zur Last gelegte Verwaltungsübertretung als  erwiesen angesehen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_441`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_5`)


Die Kosten des Beschwerdeverfahrens (zusammen € 24,00) sind gemeinsam mit den  Geldstrafen (zusammen € 120,00) und dem Beitrag zu den Kosten der belangten Behörde  (zusammen € 20,00), insgesamt somit € 164,00, binnen zwei Wochen nach Zustellung dieses  Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_12`)


Zu 1) MA67/196701153394/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/196701153394 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 1) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)


Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, Prof.in StR DDr.in Reneé Plein  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Prof.in StR DDr.in Reneé Plein` (person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_34`)


Zu 2) MA67/1967011579971/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/1967011579971 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 2) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_7`)


Da er die mit Anonymverfügung vorgeschriebene Geldstrafe nicht zahlte, warf der Magistrat  der Stadt Wien dem Beschwerdeführer(Bf.) in der Strafverfügung vom 02. Jänner 2020 vor, er  habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das mehrspurige  Kraftfahrzeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen  am 4. November 2019 um 17:31 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt,  ohne für seine Kennzeichnung mit einem zur Tatzeit gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_26`)


Im Straferkenntnis vom 26. März 2020 warf der Magistrat der Stadt Wien dem Bf. die be- reits in der Strafverfügung vom 02. Jänner 2020 vorgeworfene Verwaltungsübertretung vor,  verhängte über ihn eine Geldstrafe in Höhe von EUR 60,00;

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_28`)


Zur Sach- und Beweislage stellte der Magistrat der Stadt Wien im Wesentlichen fest, der nach  dem Tattag vorgelegte Parkschein beweise nicht, dass er am Tattag zur Tatzeit im hinteren Be- reich des Armaturenbretts lag, weshalb der Bf. das objektive Tatbild der verkürzten Parkome- terabgabe erfüllt habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_36`)


Die von mir in der Vernehmung vom 17.01.2020 im Magistrat der  Stadt Wien in … angeführten Angaben wurden keinesfalls ernst genommen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_45`)


Da  der nach dem Tattag dem Magistrat der Stadt Wien vorgelegte Parkschein nicht auf den Tatort- fotos zu sehen ist, ist als erwiesen anzusehen, dass der Bf. den Parkschein nicht ausgefüllt hat,  nachdem er das Fahrzeug in der gebührenpflichtigen Kurzparkzone geparkt hat.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_79`)


2. Beweiswürdigung  Der Sachverhalt ist auf Grund des Finanzamtsaktes sowie der Eingaben der Bf und der  schriftlichen Aussagen des Herrn C vor der KIAB (nunmehr Finanzpolizei) bzw. des  Strafverfahrens des Magistrats der Stadt Wien gegen die Geschäftsführerin der Bf wegen  illegaler Beschäftigung nach dem AuslBG als erwiesen anzusehen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzpolizei` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Heidemarie Lueckemeyer  in der Verwaltungsstrafsache gegen  Amber Demirdöven, Wiedneralm 4, 4906 Feichtet, Österreich, 1.) über die Beschwerde vom 07.09.2020 gegen das Straferkennt- nis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639161/2020, und 2.) über die Beschwerde vom 07.09.2020 gegen das Strafer- kenntnis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639163/2020, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der Stadt  Wien vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, als unbegründet abgewie- sen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |
| `Magistrats der Stadt  Wien` | `Magistrats der Stadt  Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Heidemarie Lueckemeyer` (person)
- `Amber Demirdöven` (person)
- `Wiedneralm 4, 4906 Feichtet, Österreich` (address)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_4`)


Ge- mäß § 25 Abs 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_7`)


II. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der  Stadt Wien vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, als unbegründet abge- wiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_10`)


Ge- mäß § 25 Abs 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_16`)


Da der Zulassungsbesitzer angab, seine Ehegattin habe sein Fahrzeug am 11.03.2020 um  10:54 Uhr und am 09.03.2020 um 13:31 Uhr ohne Parkschein in einer gebührenpflichtigen  Kurzparkzone abgestellt und da die Ehegattin die an sie adressierten und für diese Tattage und  Tatzeiten erlassenen Strafverfügungen fristgerecht angefochten hatte, erließ der Magistrat der  Stadt Wien am 24.08.2020 erstens ein an die Ehegattin adressiertes Straferkenntnis zur Ge- schäftszahl MA67/206700639161/2020 und zweitens ein an die Ehegattin adressiertes Strafer- kenntnis zur Geschäftszahl MA67/206700639163/2020.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_17`)


2. Im Straferkenntnis vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, warf der  Magistrat der Stadt Wien der in Folge als Beschwerdeführerin (Bf.) bezeichneten Ehegattin des  Zulassungsbesitzers vor, sie habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt,  dass sie das mehrspurige Kraftfahrzeug ihres Ehegatten mit dem im Straferkenntnis näher be- zeichneten behördlichen Kennzeichen am 11.03.2020 um 10:54 Uhr in einer gebührenpflichti- gen Kurzparkzone abgestellt habe, ohne für seine Kennzeichnung mit einem gültigen Park- schein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_29`)


Die Bf. habe den Magistrat der Stadt  Wien ersucht zu prüfen, ob statt Geldstrafen zu verhängen, Ermahnungen erteilt werden kön- nen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_30`)


Der Magistrat der Stadt Wien stellte fest, die Bf. hätte an beiden Tattagen jeweils einen  Parkschein im Fahrzeug hinterlegen müssen und da sie dies nicht tat, habe sie am 11.03.2020  um 10:54 Uhr und davor am 09.03.2020 um 13:31 Uhr die ihr vorgeworfenen Verwaltungs- übertretungen begangen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_39`)


4. Am 17.03.2020 erließ der Magistrat der Stadt Wien die Verordnung über die vorüberge- hende Aufhebung der Wiener Kurzparkzonen bis auf Widerruf.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_3`)


Am Ausspruch des Magistrats der Stadt Wien, dass der Beschwerdeführer gem. § 64 Abs. 2  VStG 1991 einen Beitrag zu den Kosten des erstinstanzlichen Strafverfahrens zu zahlen hat, tritt  keine Änderung ein.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_4`)


III. Der Magistrat der Stadt Wien wird gem. § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_5`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens i.H.v. 12 € ist zusammen mit der  Geldstrafe i.H.v. 60 € und dem Beitrag zu den Kosten des behördlichen Verfahrens i.H.v. 10 €,  somit insgesamt i.H.v. 82 €, an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_148`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_3`)


III. Der Beitrag zu den Kosten des Beschwerdeverfahrens ist zusammen mit der Geldstrafe und  dem Beitrag zu den Kosten des behördlichen Verfahrens an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als  Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_150`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_18`)


Im elektronisch vorgelegten Akt befinden sich Ablichtungen von (Schulbesuchs-)Bestätigungen  und Zeugnissen sowie die erste Seite eines Bescheides des Magistrats der Stadt Wien für den  streitgegenständlichen Zeitraum.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_66`)


Dem Bf wurde laut Bescheid des Magistrats der Stadt Wien vom 06.10.2015, Betreff:  „Mindestsicherung, Zuerkennung“ eine Leistung zur Deckung des Lebensunterhalts und der  Grundbetrag zur Deckung des Wohnbedarfs ab November 2015 bis jedenfalls August 2016  zuerkannt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Sulamith Hördegen` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_6`)


Diese Kosten (€ 22,00) sind binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den  Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_7`)


Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (Fa. ZB, Straße, 1220 Wien)  eingeholten Lenkerauskunft mit Strafverfügung vom 28. Oktober 2020, an, er habe das  Fahrzeug am 19. August 2020 in der gebührenpflichtigen Kurzparkzone in 1220 Wien,  Schüttaustraße 4-10, ohne einem für den Beanstandungszeitpunkt 14:34 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_18`)


Mit Straferkenntnis vom 17. Dezember 2020 erkannte der Magistrat der Stadt Wien,  Magistratsabteilung 67, den Bf. wegen der bereits näher bezeichneten Verwaltungsüber- tretung für schuldig und verhängte wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine  Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14  Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_17`)


Am 15. Oktober 2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, die  beschwerdegegenständliche Vollstreckungsverfügung, Zahl MA67/Zahl/2020 mit folgendem  Wortlaut:  Die mit der Strafverfügung vom 28. August 2020, Zahl MA67/Zahl/2020, verhängte  rechtskräftige Strafe sei bis heute nicht bezahlt worden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_38`)


Am 6. November 2019 langte die Beschwerde der Beschuldigten und der Haftenden beim  Magistrat der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen ein.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_49`)


Zwischenzeitig ist – da eine Verlängerung der Frist aufgrund von COVID-19-Maßnahmen  gesetzlich nicht (mehr) möglich ist – die im § 43 Abs. 1 VwGVG normierte Frist nach dem  6. Februar 2021 bereits abgelaufen, sodass das angefochtene Straferkenntnis des Magistrats  der Stadt Wien von Gesetzes wegen außer Kraft getreten und das Strafverfahren einzustellen  ist (vgl. VwGH 26.8.2014, Ro 2014/02/0106).

| Predicted | Gold |
|---|---|
| `Magistrats  der Stadt Wien` | `Magistrats  der Stadt Wien` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Moebus` (person)
- `Aichach 11m, 9375 Knappenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_3`)


Begründung  Mit Bescheid des Finanzamtes vom 17. Juli 2020 wurde der Antrag des durch den Magistrat der  Stadt Wien Kinder- und Jugendhilfe, Rechtsvertretung 16,17, 18, 19, vertretenen  minderjährigen Beschwerdeführers (kurz: Bf) auf Zuerkennung der Familienbeihilfe gemäß § 6  Abs. 5 FLAG 1967 ab Jänner 2016 abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_18`)


Mit Schriftsatz vom 07.01.2021 brachte der Bf, vertreten durch den Magistrat der Stadt Wien  Kinder- und Jugendhilfe Rechtsvertretung 16, 17, 18 , 19, einen Vorlageantrag ein und stellte  den Antrag den angefochtenen Abweisungsbescheid dahingehend abzuändern, dass die  Familienbeihilfe für den Zeitraum Jänner 2016 bis Februar 2018 gewährt werde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_20`)


Der Magistrat der Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_22`)


Dies  legitimiere den Magistrat der Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung 16, 17, 19,  19, zur Antragstellung auf Familienbeihilfe sowohl für laufende als auch für rückwirkende  Zeiträume.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_23`)


Zusätzlich stellte der Bf, vertreten durch den Magistrat der Stadt Wien Kinder- und Jugendhilfe  Rechtsvertretung 16, 17, 18, 19, mit Schriftsatz vom 21.08.2020, beim Finanzamt eingelangt  am 25.08.2020, einen weiteren Antrag auf Zuerkennung der Familienbeihilfe ab 01.03.2016.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_27`)


Der Magistrat der Stadt Wien Kinder- und Jugendhilfe habe seit  24.02.2016 die Obsorge im Bereich der Pflege und Erziehung inne.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_44`)


Dem Magistrat der Stadt Wien Kinder- und  4 von 7 Seite 5 von 7

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_53`)


Das Bundesfinanzgericht kommt daher zu dem Ergebnis, dass die im gegenständlichen Fall dem  Magistrat der Stadt Wien Kinder- und Jugendhilfe seit Jänner 2016 übertragene Obsorge im  Bereich Pflege und Erziehung für die Vertretung des Bf zur Geltendmachung des  Familienbeihilfenanspruchs, die Einbringung der Beschwerde gegen den Abweisungsbescheid  und die Einbringung des Vorlageantrags ausreicht und zwar auch für den rückwirkend ab  Jänner 2016 geltend gemachten Teil des Familienbeihilfeanspruchs.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_20`)


Der Magistrat der Stadt Wien wies in der Folge den Einspruch des Bf. vom 10.11.2020 gegen  die Strafverfügung vom 07.09.2020 mit Bescheid vom 08.01.2021 gemäß § 49 Abs. 1  Verwaltungsstrafgesetz 1991 (VStG) als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_40`)


Der Magistrat der Stadt Wien wies in der Folge den Einspruch des Bf. vom 10.11.2020 gegen  die Strafverfügung vom 08.10.2020 mit Bescheid vom 08.01.2021 gemäß § 49 Abs. 1  Verwaltungsstrafgesetz 1991 (VStG) als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_48`)


Der Magistrat der Stadt Wien legte die Beschwerden samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 3. Februar 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_4`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_5`)


Informativ wird mitgeteilt, dass der Beitrag zu den Kosten des behördlichen Verfahrens  (€ 10,00) zusammen mit der Geldstrafe (€ 36,00), insgesamt somit € 46,00, an den Magistrat  der Stadt Wien zu entrichten sind, wofür weitere Informationen am Ende dieser Entscheidung  des BFG und am Ende des angefochtenen Straferkenntnisses des Magistrates zu finden sind.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_84`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_5`)


Die verbleibende Geldstrafe (12,00 Euro) ist gemeinsam mit den Kosten des Beschwerdever- fahrens (12,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro),  insgesamt 34,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den  Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_12`)


Mit Anonymverfügung vom 27. Oktober 2020 schrieb der Magistrat der Stadt Wien der  Beschwerdeführerin (Bf.) wegen der Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006eine Geldstrafe von € 48,00 vor.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_13`)


Mit E-Mail vom 25. November 2020 teilte die Bf. dem Magistrat der Stadt Wien unter  Bezugnahme auf die an sie ergangene Anonymverfügung mit, dass sie ein "Parkpickerl" für den  3. Bezirk besitze, das jeweils ab 1. Oktober fällig sei.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_20`)


Mit Schreiben vom 27. November 2020 teilte der Magistrat der Stadt Wien zu der unter der  MA67/Zahl/2020 protokollierten Verwaltungsübertretung mit, dass die Zahlungsfrist der  Anonymverfügung bereits abgelaufen sei und in Kürze das Verwaltungsstrafverfahren  eingeleitet werde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_21`)


Zugleich teilte der Magistrat der Stadt Wien der Bf. mit, dass die  Ausnahmebewilligung von der Parkzeitbeschränkung ("Parkpickerl") keine rückwirkende  Gültigkeit entfaltet.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_22`)


Mit Strafverfügung vom 1. Dezember 2020 lastete der Magistrat der Stadt Wien der Bf.  sodann an, sie habe das in Rede stehende Fahrzeug am 1. Oktober 2020 in der  gebührenpflichtigen Kurzparkzone in 1030 Wien, Kardinal-Nagl-Platz 10-11 ggü, ohne einem  für den Beanstandungszeitpunkt 13:20 gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_28`)


Mit Straferkenntnis vom 18. Dezember 2020 erkannte der Magistrat der Stadt Wien, MA 67,  die Bf. wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig und  verhängte wegen der Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabever- ordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für  den Fall der Uneinbringlichkeit 14 Stunden Ersatzfreiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_47`)


Auf Grund ihres Antrages vom 8. Oktober 123 erteilte der Magistrat der Stadt Wien der Bf. mit  Bescheid vom 8. Oktober 123 gemäß § 45 Abs. 4 und § 43 Abs. 2a Z. 1 Bundesgesetz vom 6. Juli  1960 eine Ausnahmebewilligung von der Parkzeitbeschränkung der im 3.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_50`)


Mit Banküberweisung vom 3. Dezember 123 brachte die Bf. den in der Anonymverfügung vom  27. Oktober 123 verhängten Strafbetrag nunmehr – somit verspätet – zur Anweisung, nachdem  der Magistrat der Stadt Wien der Bf. im Schreiben vom 27. November 123 bekanntgegeben  hatte, dass die Zahlungsfrist bereits abgelaufen war und das Verwaltungsstrafverfahren  eingeleitet wird.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_26`)


Die Beiträge zu den  Kosten des Beschwerdeverfahrens (6x € 12,00) sind zusammen mit den Geldstrafen (6x € 60,00)  und den Beiträgen zu den Kosten des behördlichen Verfahrens (6x € 10,00) an den Magistrat  der Stadt Wien zu entrichten, der zu entrichtende Gesamtbetrag beträgt 6x € 82,00.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_28`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 9. Dezember 2020, an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 9. Oktober 2020  in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Stubenbrücke nächst Parkring, ohne  einen für den Beanstandungszeitpunkt 15:33 Uhr gültigen Parkschein abgestellt und demnach  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_15`)


Mit Straferkenntnis vom 13. Jänner 2021, MA67/Zahl/2020, wurde der Bf. vom Magistrat der  Stadt Wien, MA 67, wegen der bereits näher bezeichneten Verwaltungsübertretung für  schuldig befunden und wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  von € 60,00 sowie für den Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden  festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_10`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.) mit  Strafverfügung vom 7. Mai 2021 an, sie habe das mehrspurige Kraftfahrzeug mit dem behörd- lichen Kennzeichen Vienna am 9. März 2021 in der gebührenpflichtigen Kurzparkzone in  Alois Windisch-Straße 1, 5121 Hofweiden, Österreich  ohne einen für den Beanstandungszeitpunkt 10:30 Uhr gültigen Parkschein  abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Alois Windisch-Straße 1, 5121 Hofweiden, Österreich` (address)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_14`)


Mit Straferkenntnis vom 28. Juni 2021 wurde die Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig erkannt und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_115`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Michael Klingsohr` (person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich` (address)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_9`)


Diese  Beschwerde wurde vom Magistrat der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_3`)


Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine (ordentliche) Revision nach  Art. 133 Abs. 6 Z 2 iVm Abs. 9 B-VG durch den Magistrat der Stadt Wien nicht zulässig.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Missed by this rule (FN):**

- `Bodewein` (person)

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_16`)


Der Magistrat der Stadt Wien, MA 67, erließ an Herrn X einen mit 10. Mai 2021 datierten  Bescheid, mit welchem der Einspruch vom 21.03.2021 gegen die an Herrn Bodewein gerichtete  Strafverfügung vom 16.03.2021 infolge der Nichtvorlage der Vollmacht gemäß § 13 Abs. 3 AVG  als unzulässig zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bodewein` (person)

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_20`)


Da die mit der Strafverfügung vom 16.03.2021 zu Zahl MA67/Zahl1/2020 verhängte  rechtskräftige Strafe bislang nicht bezahlt worden sei, erließ der Magistrat der Stadt Wien eine  mit 13.09.2021 datierte Vollstreckungsverfügung.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

## `Courts - Bundesfinanzgericht` 🏆

**F1:** 0.538 | **Precision:** 0.976 | **Recall:** 0.372  

**Format:** `regex`  
**Rule ID:** `92446db6`  
**Description:**
Matches Bundesfinanzgericht with optional genitive endings (es, s) and optional (BFG) abbreviation.

**Content:**
```
\b(Bundesfinanzgericht(?:es|s)?(?:\s*\(BFG\))?|BFG\s*\(Bundesfinanzgericht\)|BFG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.976 | 0.372 | 0.538 | 4495 | 4386 | 109 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4386 | 109 | 7410 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Erich Schwaiger` (person)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Mag. Josef Nußbaumer` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_7`)


Der Bf. beantragte daraufhin die Vorlage der Beschwerde an das Bundesfinanzgericht und die Durchführung einer mündlichen Verhandlung (Vorlageantrag vom 23. Juni 2015).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_8`)


Seite 2 von 3 Das FA legte das Rechtsmittel und diverse Aktenteile am 8. Juli 2015 elektronisch an das Bundesfinanzgericht vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_9`)


Mit 9. November 2015 erließ das Bundesfinanzgericht einen Mängelbehebungsauftrag, dem der Bf. mit Schreiben vom 30. November 2015 nachkam.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_11`)


Über die Beschwerde wurde erwogen: 2.  Sachverhalt Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_22`)


Das Bundesfinanzgericht erlaubt sich den Hinweis, dass für die Aussetzung von Anspruchszinsen (§ 212a BAO) abgesehen von den sonstigen Voraussetzungen keine Beschwerde gegen den Anspruchszinsenbescheid selbst, sondern - da der Anspruchszinsenbescheid vom jeweiligen Einkommensteuerbescheid abhängt – nur eine Beschwerde gegen den zugrunde liegenden Einkommensteuerbescheid erforderlich ist (Ritz, BAO  5  , § 205 Tz 36 und § 212a Tz 7 unter Hinweis auf VwGH 27.3.2008, 2008/13/0036).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Dr. Heinz Neuner` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_62`)


------ Mit Vorhalt des Bundesfinanzgerichtes vom 9.4.2019 wurde der Beschuldigte  aufgefordert, die Mittelherkunft der behaupteter Weise von ihm in den Jahren 2012 und Seite 6 von 21 2013 geleisteten Barzahlungen an die Subfirmen X. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH anhand vorzulegender Kopien sämtlicher Kontenbewegungen oder anhand anderer geeigneter Unterlagen nachzuweisen bzw. glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Furtder Technologien GmbH` (organisation)
- `NEP Lebensmittel GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_85`)


Ich werde - so mir dies möglich ist - zur noch anzuberaumenden mündlichen Verhandlung vor dem Bundesfinanzgericht auch eine Bestätigung der Wiener Gebietskrankenkasse mitnehmen, aus der die Anzahl der bei mir in den Jahren 2012 und 2013 durchschnittlich beschäftigten Mitarbeiter ersichtlich ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Wiener Gebietskrankenkasse` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_108`)


------- In der mündlichen Verhandlung vor dem Senat des Bundesfinanzgerichtes führte der Beschuldigte ergänzend aus, er sei derzeit Angestellter einer Parkettbodenfirma und sein monatliches Nettogehalt betrage € 1.454,00, davon würden etwas mehr als € 300,00 für Zahlungen aufgrund Privatkonkurses einbehalten und abgeführt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_130`)


Auf den Vorhalt, im Rahmen der GPLA-Prüfungen vom 2.11.2017 für den Zeitraum 1.1.2012 bis 31.12.2014 und vom 14.12.2017 für den Zeitraum 1.1.2015 bis 9.11.2017 seien für das gegenständliche Verfahren relevante Abfuhrdifferenzen an lohnabhängigen Abgaben in Höhe von insgesamt € 5.821,93 festgestellt worden, wobei es sich dabei um auf den Lohnkonten selbst berechnete Beträge, die von ihm  nicht ans Finanzamt abgeführt wurden, handelte, führte der Beschuldigte in der mündlichen Verhandlung vor dem Bundesfinanzgericht aus: Die Abfuhrdifferenzen könne er sich überhaupt nicht erklären, die Lohnverrechnung sei durch den Steuerberater durchgeführt worden und alle Erlagscheine, die ihm von diesem übermittelt worden seien, habe er auch an das Seite 12 von 21 Finanzamt bezahlt. Er habe in diesem Zeitraum keine finanziellen Probleme gehabt und sei seinen Zahlungspflichten regelmäßig nachkommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_206`)


Seite 18 von 21 Keine der Verfahrensparteien konnte - trotz Aufforderung in der mündlichen Verhandlung vor dem Bundesfinanzgericht - Personen als Zeugen namhaft machen, die Aussage darüber treffen hätten können, von wem (von welchen Arbeitern) in wessen Auftrag die hier in Rede stehenden Leistungen der drei genannten Subfirmen tatsächlich erbracht wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_212`)


Nach Ansicht des Bundesfinanzgerichtes kann im gegenständlichen Fall, aufgrund der vorliegenden Beweisergebnisse und der gegenüber dem Abgabenverfahren geänderten Beweislast, schon in objektiver Hinsicht nicht mit der für ein Finanzstrafverfahren erforderlichen Sicherheit der Nachweis der angeschuldigten Abgabenhinterziehung gemäß § 33 Abs. 1 FinStrG an Einkommensteuer 2012 und 2013 sowie der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG betreffend Nichtabfuhr von lohnabhängigen Abgaben (L, DB, DZ) 1/2012-09/2017 für schwarz beschäftigte (bei der Sozialversicherung nicht angemeldete) Dienstnehmer mit der für ein Finanzstrafverfahren erforderlichen Sicherheit erbracht werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_220`)


Zweifelsfrei kannte der Beschuldigte seine diesbezüglichen Entrichtungs- bzw. Meldepflichten zu den jeweiligen gesetzlichen Fälligkeitstagen und er hat sich vor dem Bundesfinanzgericht dahingehend gerechtfertigt, sämtliche von seinem Steuerberater monatlich berechneten und ihm bekanntgegebenen Lohnabgaben auch entrichtet zu haben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_195`)


Seite 15 von 23 Gemäß § 323 Abs. 38 Bundesabgabenordnung (BAO, idF des FVwGG 2012, BGBl. I 2013/14 ab 1.1.2014) sind die am 31. Dezember 2013 bei dem unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen Berufungen vom Bundesfinanzgericht als Beschwerde im Sinne des Art. 130 Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_273`)


Der Berechnung der fiktiven Anschaffungskosten im ersten Gutachten kann das Bundesfinanzgericht - unter Heranziehung der vorstehenden Rechtsprechung - nicht folgen, da in diesem Gutachten der Herstellungswert für Versicherungszwecken herangezogen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_283`)


Das Bundesfinanzgericht kann daher auch anhand dieses Gutachtens nicht die kürzere Nutzungsdauer für die Ru. von ca. 40 Jahre und für die Pf. von maximal 15 Jahre erkennen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_287`)


Das Bundesfinanzgericht kann unter Heranziehung der im Akt aufliegenden Unterlagen, auch der angeführten anderen Nutzungsdauern (42 Jahre) und den Zinssätze, die der nunmehrigen Berechnungen zugrunde gelegt wurde, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_297`)


Das Bundesfinanzgericht geht daher von einer Nutzungsdauer jährlich von 2 % aus, da die Liegenschaft (vorwiegend) bereits vor 1920 errichtet worden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_298`)


Eine kürzere Nutzungsdauer kann das Bundesfinanzgericht auf Grund der vorgelegten Gutachten nicht erkennen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_314`)


Das Bundesfinanzgericht teilt den von der belangten Behörde und im 2.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_319`)


Das Bundesfinanzgericht kommt auf Grund der nachfolgenden Berechnung zu der anerkannten AfA: Nutzungsdauer 50 Jahre AfA 2%

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_325`)


Zulässigkeit einer Revision Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_327`)


Das Bundesfinanzgericht orientiert sich bei den zu lösenden Rechtsfragen an der einheitlichen höchstgerichtlichen Judikatur, darüber hinaus hing die Entscheidung im Wesentlichen von den Umständen des Einzelfalles sowie auf der Ebene der Beweiswürdigung zu beantwortenden Sachfragen ab.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Alexander Schnelldorfer` (person)
- `Finanzamt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_15`)


4.     Gemäß § 323 Abs. 38 BAO sind die am 31. Dezember 2013 beim Unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen Berufungen vom Bundesfinanzgericht als Beschwerden im Sinne des Art. 130 Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_16`)


Solche Verfahren betreffende Anbringen wirken mit 1. Jänner 2014 auch gegenüber dem Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_17`)


5.     Die Beschwerde (Berufung) war beim Bundesfinanzgericht unter GZ. RV/3100022/2011 der Geschäftsabteilung 4004 zugeordnet, wurde dieser mit Verfügung des Geschäftsverteilungsausschusses vom 18. Februar 2019 abgenommen und mit Wirkung vom 6. März 2019 der Geschäftsabteilung 4019 zugeteilt. 6.     Die steuerliche Vertretung der Beschwerdeführerin hat mit Schreiben vom 09.10.2019 mitgeteilt, dass der Antrag auf Entscheidung durch den gesamten Senat und der Antrag auf Durchführung einer mündlichen Verhandlung zurückgezogen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_18`)


II.   Sachverhalt Seite 3 von 7 Folgender Sachverhalt ist für das Bundesfinanzgericht entscheidungswesentlich und erwiesen: 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_47`)


Mit Vorhalt vom 18.04.2019 hat das Bundesfinanzgericht die Beschwerdeführerin unter anderem aufgefordert, nachweislich den Mittelpunkt der Lebensinteressen für die unter Punkt II.9. genannten Personen sowie die tatsächliche Nutzung der Liegenschaft EZ*01 zu belegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_49`)


Das Antwortschreiben samt Beilagen wurde der Abgabenbehörde mit Schreiben des Bundesfinanzgerichts vom 03.07.2019 zur Kenntnis gebracht, Einwendungen dagegen hat sie nicht vorgebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_50`)


Somit geht auch das Bundesfinanzgericht davon aus, dass das Einfamilienhaus an der Adresse*** von D, G und E zwischen Oktober 2005 und April 2008 tatsächlich für Wohnzwecke genutzt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_90`)


Für das Bundesfinanzgericht steht fest, dass die Liegenschaft EZ*01 im Jahr 2008 nicht Betriebsvermögen der Beschwerdeführerin war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_97`)


Die Ansicht der Abgabenbehörde, die Liegenschaft habe "durch das kurzfristige Bewohnen […] nicht den Charakter als Betriebsvermögen verloren", teilt das Bundesfinanzgericht nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_107`)


V.     Zulässigkeit einer Revision Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)
- `Verwaltungsgerichtshof` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_42`)


-------- Die gegenständliche Beschwerde vom 16.01.2017 wurde dem Bundesfinanzgericht am 05.11.2019 zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_47`)


Überzeugt sich das Bundesfinanzgericht aus Anlass der Beschwerde, dass zum Nachteil eines anderen Beschuldigten oder Nebenbeteiligten, welcher keine Beschwerde eingebracht hat, das Gesetz unrichtig angewendet wurde, so hat es so vorzugehen, als wäre auch von diesen Personen eine Beschwerde eingebracht worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_57`)


Da dem angefochtenen Erkenntnis eine im Zeitpunkt der Erlassung des angefochtenen Erkenntnisses nicht mehr strafbare fahrlässige Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zugrunde gelegt wurde und dem Bundesfinanzgericht gemäß § 161 Abs. 3 FinStrG  eine strengere Qualifikation des Handelns des Bf. als grob fahrlässige Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG (BGBl. I Nr. 118/2015 ab 1.1.2016) bei zugunsten des Bf. eingebrachter Beschwerde rechtlich verwehrt ist (Verböserungsverbot), war das angefochtene Erkenntnis wegen inhaltlicher Rechtswidrigkeit aufzuheben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Susanne Zankl` (person)
- `RgR Amalia Schuetzke` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_3`)


Begründung  Zunächst ist festzuhalten:   Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichtes (BFG) vom  11.10.2019 wurde der streitgegenständliche Fall, der ursprünglich der Gerichtsabteilung 7005  des BFG zugeteilt war, nunmehr der Gerichtsabteilung 7019 des BFG zugeteilt. Damit bestand  für die nun zuständige Gerichtsabteilung 7019 des BFG erst ab 14.10.2019 (Inkrafttretung der  Umverteilung) die Möglichkeit, das streitgegenständliche Verfahren abzuführen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes (BFG)` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_52`)


Erst am 23.08.2018 brachte die Bf den Antrag ein, die Beschwerde dem Bundesfinanzgericht  (BVE) zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof. Günter Lehwaldt` (person)
- `Waltraud Hinterlandt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_18`)


Mit am 31.5.2017 bei der belangten Behörde eingelangtem Sch reiben wurde vom  Parteienvertreter beantragt, die oa Beschwerde dem Bundesfinanzgericht zur Entscheidung  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_23`)


Am 9.6.2017 erfolgte durch die belangte Behörde die Vorlage der gegenständlichen Beschwerde  an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_38`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen  gemäß § 167 Abs 2 BAO als erwiesen annehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_90`)


Unter Berücksichtigung aller oben angeführter Umstände erachtet das Bundesfinanzgericht die  Berechnung des Verspätungszuschlages mit 2% des Vorauszahlungsbetrages als angemessen  (vgl zB auch BFG 27.2.2014, RV/2100455/2012).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `BFG` | `BFG` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_94`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine s olche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_96`)


Mit dem vorliegenden Erkenntnis weicht das Bundesfinanzgericht nicht von der Rechtsprechung  des Verwaltungsgerichtshofes ab, sondern folgt insbesondere dem Erkenntnis des VwGH vom  25.6.2007, 2006/14/0054, weshalb gemäß § 25a Abs 1 VwGG spruchgemäß zu entscheiden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_10`)


Das Bundesfinanzgericht hat erwogen:  I. Unstrittig ist nach den abgabenbehördlichen Verfahrensunterlagen, dass der Bf zumindest ab  April 2012 und im Jahr 2013 ganzjährig ein Imbisslokal in Form eines Kebab-Standes betrieb,  dessen Gewinnermittlung weder durch Betriebsvermögensvergleich zu erfolgen hatte, noch  auf diese Weise erfolgte und dessen Jahresumsatz iSd § 125 BAO unter 255.000,- € lag.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_11`)


Nach den Angaben in den Abgabenerklärungen des Bf wurde der Gewinn dieses Betriebes  sowohl für das Jahr 2012 als auch für 2013 durch Pauschalierung ermittelt.   Im Zuge einer abgabenbehördlichen Außenprüfung (AP) für 2012/2013 wurde die  Gewinnermittlungsart für 2012 (BFG-Anmerkung: nach der  GaststättenpauschalierungsVO 1999) nicht beanstandet, eine Gewinnermittlung für 2013 nach  der GastgewerbepauschVO 2013 wurde dagegen als unzulässig erachtet (AP-Bericht 28.9.2015,  Tz 1 u. Tz 3).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_16`)


Hervorhebungen durch das BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_20`)


„Gastgewerbe in der Betriebsart "Imbiss" gemäß § 94 Z. 26 GewO 1994 mit der Berechtigung  gemäß § 111 Abs. 1 Z. 2 Gew0 1994, wobei ein Befähigungsnachweis gem. § 19 GewO 1994  erbracht wurde.“ (Hervorhebungen durch das BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_25`)


Entsprechend geht das BFG davon  aus, dass die Erbringung des Befähigungsnachweises (§ 19 GewO 1994) gegenüber der  Gewerbebehörde im Zuge der Zurücklegung und Neuvergabe der Gewerbeberechtigung im  Sept.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_36`)


Unbeschadet allfälliger  Ausübungsvorschriften ist für diese kein Befähigungsnachweis zu erbringen.“  § 111 GewO 1994 hatte im Jahr 2013 – soweit verfahrensrelevant – folgende Fassungen  (Hervorhebung durch das BFG):  1.Jänner bis 28.Mai 2013 (BGBl. I Nr. 42/2008):  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_74`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Ophelia Dutschka` (person)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_67`)


III. Das Bundesfinanzgericht hat erwogen:  1. Rechtslage

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_112`)


Die KG/OG als  Eigentümerin der Grundstücke (dokumentiert im Grundbuch) ist eine von den Gesellschaftern  zu unterscheidende und selbständige Rechtspersönlichkeit, dh. der Erwerb der  Liegenschaften durch den verbleibenden Gesellschafter im Zuge der Anwachsung nach § 142  UGB erfolgte nicht vom ausscheidenden Gesellschafter der KG/OG, sondern vielmehr von  Seiten der KG/OG als eigenständigem Rechtsträger (vgl. BFG 16.10.2014, RV/6100226/2008).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_133`)


3. Zur Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Gabriele Grossgut-Palotás` (person)
- `Lewis Rzehula` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_10`)


Mit Vorlageantrag vom 28.8.2019 ersuchte der Beschwerdeführer innerhalb verlängerter  Rechtsmittelfrist um Entscheidung über die Beschwerde durch das Bundesfinanzgericht;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_13`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_68`)


Das Bundesfinanzgericht verkennt nicht, dass die besuchten Seminare auch geeignet waren,  die beruflichen Kenntnisse und Fertigkeiten des Beschwerdeführers zu verbessern;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_75`)


Seitens des Bundesfinanzgerichtes wird nicht in Abrede gestellt, dass die besuchten Seminare  einen positiven Effekt auf die berufliche Tätigkeit des Beschwerdeführers hatten;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_81`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Dr. Kurt Bartold` (person)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_6`)


Strittig war vor dem BFG, ob dieser Antrag fristgerecht eingebracht wurde oder nicht.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_9`)


Das Bundesfinanzgericht hat erwogen:  In seinem Erkenntnis RV/2100723/2018 vom 6.9.2018 gelangte das BFG unter Hinweis auf  § 295 Abs. 4 iVm. § 304 BAO (zunächst) zu dem Schluss, der am 9.12.2014 eingebrachte Antrag  sei nach dem klaren Gesetzeswortlaut erst nach Eintritt der Verjährung – und damit verspätet -  eingebracht worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `BFG` | `BFG` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_27`)


Der VwGH hob in der Folge das BFG-Erkenntnis vom 6.9.2018, RV/2100723/2018, – unter  Verweis auf VfGH vom 4.12.2019, G 159/2019 ua. - mit Entscheidung vom 18.5.2020,  Ra 2018/15/0121, auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_29`)


Das BFG habe – so der VwGH – das angefochtene Erkenntnis  auf die aufgehobene Gesetzesbestimmung gestützt, die im Revisionsfall nicht (mehr)  anzuwenden sei.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_31`)


Nach § 279 Abs.1 BAO hat eine Aufhebung durch das BFG ua. zu erfolgen, wenn ein  verfahrensrechtlicher Bescheid (zB Zurückweisung eines Antrages) zu Unrecht erlassen wurde  (Ritz, BAO 6.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_36`)


Zur Revision:   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_37`)


Da das BFG auf Grund der oa. VfGH- bzw. VwGH-Judikatur spruchgemäß zu entscheiden hatte,  liegt keine Rechtsfrage iSd. Art. 133 Abs. 4 B-VG vor.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_71`)


3) BFG-Vorhaltschreiben vom 13.12.2019 an die Bf wie folgt:  "Im anhängigen Berufungs- bzw. nunmehr Beschwerdeverfahren ist im Wesentlichen strittig,  wer als "Steuerschuldner" in Betracht komme und wo sich der "dauernde Standort" des  Fahrzeuges Range Rover Sport befunden habe.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_86`)


In Beantwortung eines Urgenzschreibens des BFG hat der Rechtsvertreter nun letztlich im  Schreiben vom 1.7.2020 mitgeteilt, dass bislang keine Antwort der Bf bzw. beider Ehegatten Bf  vorliege und er mangels Kontakt zugleich mit beiliegendem, an die Bf (unter der eruierten  deutschen Adresse des Ehegatten) gerichteten Schreiben seine Vertretungs- und  Zustellvollmacht aufgekündigt hat.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_111`)


IV. Rechtslage:  Gemäß § 323 Abs. 38 Bundesabgabenordnung (BAO), BGBl 1961/194 idgF., sind die am 31.  Dezember 2013 beim Unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz  anhängigen Berufungen vom Bundesfinanzgericht als Beschwerden im Sinne des Art. 130  Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_130`)


Festzuhalten ist, dass eine diesbezüglich ausführliche Anfrage mit BFG-Vorhaltschreiben zur  weiteren Sachverhaltsabklärung trotz langwieriger und vielfacher Versuche durch den  Rechtsvertreter zwecks Beantwortung ohne Ergebnis geblieben ist.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_154`)


Abgesehen davon, dass im Gegenstandsfalle die Leasinggeberin Eigentümerin und  Zulassungsbesitzerin des Fahrzeuges ist, welchen Umständen wie auch der Frage nach dem  rechtmäßigen Besitzer oder auf wen die Zulassung im Inland erfolgen könnte aber nach  Obigem keine ausschlaggebende Bedeutung zukommt, kann nach dem Dafürhalten des BFG  die Bf nicht als Verwenderin im Sinne der "Halterin" des Fahrzeuges qualifiziert werden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_159`)


Nach dem Dafürhalten des BFG kann nahezu  ausgeschlossen werden, dass die Bf von ihrem Haushaltsgeld allein rund € 700 an mtl.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_167`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Mehmet Gessl` (person)
- `Donau-Elektro` (organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich` (address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_121`)


5)Entgelt für Zimmer:  Die Leistung besteht in der Ermöglichung der Ausübung der Prostitution in einem behördlich  bewilligten Bordellbetrieb.“  (4) Mit Ergänzungsersuchen vom 11.3.2020 brachte das BFG der Bf. die Stellungnahme des  Prüfers zur Kenntnis und ersuchte um Übermittlung der behördlichen Bewilligung nach den §§  4 des Stmk.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_156`)


Am 17.6.2020 fand vor dem Bundesfinanzgericht die beantragte mündliche Verhandlung  statt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_157`)


Das Bundesfinanzgericht hat erwogen:  Die Bf. betrieb in den Streitjahren eine Bar in der A-Gasse 8 in G mit vier (im Obergeschoß  befindlichen) Zimmern.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_164`)


Wir sind auch die beste Adresse für Transsexuelle! (…)“ (s. zB den vom  Prüfer seiner Stellungnahme zur Beschwerde beigelegten Ausdruck aus dem Sexmagazin vom  5.5.2017, welcher der Bf. vom BFG zur Stellungnahme übermittelt wurde).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_194`)


s. Beschwerde S. 5f. sowie  Vorbringen in der mündlichen Verhandlung vom 17.6.2020) nach Meinung des BFG jedenfalls  ein weiteres – hier jedoch letztlich nicht mehr entscheidungsrelevantes - Indiz dafür darstellt,  dass die Prostitutionserlöse der Bf. zuzurechnen sind.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_200`)


Letztlich  ändert aber auch ein Inkasso durch die Prostituierten bei Vorliegen eines Bordellbetriebes an  der Zurechnung des Gesamtentgeltes an die Bordellbetreiberin nichts (zB VwGH 20.5.2010,  2006/15/0290; in diesem Sinne auch etwa BFG 13.8.2019, RV/2100289/2018, uva.).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_226`)


Dies begründet  notwendig eine funktionelle Verknüpfung zwischen dem Bordellbetrieb und den  Sexualdienstleistungen und geht zugleich hinsichtlich jener (dem Bordell zugeordneten)  Räumlichkeiten, in welchen die Sexualdienstleistungen erbracht werden, weit über den  Rahmen einer bloßen „Wohnraummiete“ hinaus (so zB BFG 13.8.2019, RV/2100289/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_240`)


Zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_241`)


Das BFG konnte sich im vorliegenden Fall auf zahlreiche – oben zitierte – Erkenntnisse des  VwGH stützen, und zwar sowohl hinsichtlich der Zurechnung der Umsätze an die Bf. (als  Bordellbetreiberin) als auch der Besteuerung der Umsätze mit 20%.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Chen Walcker` (person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_3`)


Begründung  Zunächst ist festzuhalten:   Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichtes (BFG) vom  11.10.2019 wurde der streitgegenständliche Fall, der ursprünglich der Gerichtsabteilung 7005  des BFG zugeteilt war, nunmehr der Gerichtsabteilung 7019 des BFG zugeteilt. Damit bestand  für die nun zuständige Gerichtsabteilung 7019 des BFG erst ab 14.10.2019 (Inkrafttretung der  Umverteilung) die Möglichkeit, das streitgegenständliche Verfahren abzuführen.

**False Positives:**

- `Bundesfinanzgerichtes` — partial — pred is substring of gold: `Bundesfinanzgerichtes (BFG)`
- `BFG` — partial — pred is substring of gold: `Bundesfinanzgerichtes (BFG)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_10`)


Die Bf brachte am 23.08.2018 den Antrag ein, die Beschwerde dem Bundesfinanzgericht (BFG)  zur Entscheidung vorzulegen.

**False Positives:**

- `Bundesfinanzgericht` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`
- `BFG` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`
- `BFG` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Saphira Blazejewicz`(person)
- `Jeanne Weiermann`(person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich`(address)
- `Finanzamt`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

**False Positives:**

- `Bundesfinanzgericht` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`
- `BFG` — partial — pred is substring of gold: `Bundesfinanzgericht (BFG)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Finanzamt`(organisation)

</details>

---

## `Tax Authority - Generic Finanzamt` 🏆

**F1:** 0.334 | **Precision:** 0.952 | **Recall:** 0.202  

**Format:** `regex`  
**Rule ID:** `c6b25c8a`  
**Description:**
Matches generic Finanzamt when no specific location follows, ensuring it's not a partial match of a longer entity.

**Content:**
```
\b(Finanzamt(?:es)?)\b(?!\s+(?:Wien|Österreich|Salzburg-Land|Bruck|Hollabrunn|St\.\s+Johann|Vorarlberg|Braunau|Großbetriebe|Feldkirch|Neunkirchen|für))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.952 | 0.202 | 0.334 | 2508 | 2387 | 121 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2387 | 121 | 9409 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_58`)


Die Abfuhrdifferenzen ergeben sich auf Grund der dem Prüfer vorgelegten Lohnkonten zu den bisher dem Finanzamt gemeldeten Lohnabgaben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_76`)


Die von mir sohin gewählte und geübte Vorgangsweise mag (für das Finanzamt) möglicherweise befremdlich und unüblich erscheinen, allerdings habe ich mir diese so zur Gewohnheit gemacht und liegt dies sicher auch in meiner Mentalität begründet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_92`)


Dieser vom Finanzamt gegen mich erhobene Vorwurf bricht sohin schon dadurch Seite 9 von 21 in sich zusammen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_101`)


Wenn mir das Finanzamt letztlich vorwirft, dass die Furtder Technologien GmbH über eine UID-Nummer lediglich bis 9. Oktober 2012 und die NEP Lebensmittel GmbH über eine solche lediglich bis 30. August 2013 verfügt hatte und ich auch „nachher" noch Geschäfte mit diesen Unternehmen getätigt hätte, so ist dem zu entgegnen, dass einerseits nach ständiger Judikatur der anzulegende Sorgfaltsmaßstab nicht überspannt werden kann und darf und insbesondere andererseits Beauftragungen meiner Subunternehmer teilweise (sohin jeweils die letzten Aufträge) zu Zeitpunkten erfolgten, zu denen diese noch über die UlD-Nummer verfügt hatten, die Leistungserbringung aber (auch) in einen Zeitraum danach fiel und deren Rechnungen naturgemäß auch erst danach gelegt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Furtder Technologien GmbH` (organisation)
- `NEP Lebensmittel GmbH` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_103`)


Auftrag einen Leistungszeitraum auch noch nach dem 09. Oktober 2012 (bezeichnenderweise das Finanzamt Adresse3), bei der NEP Lebensmittel GmbH wurden nur 6 Rechnungen nach dem 30. August 2013 gelegt, drei davon noch im September 2013 (sohin innerhalb eines Monates), drei bis Mitte Oktober 2013 (sohin innerhalb von 6 Wochen).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `NEP Lebensmittel GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_130`)


Auf den Vorhalt, im Rahmen der GPLA-Prüfungen vom 2.11.2017 für den Zeitraum 1.1.2012 bis 31.12.2014 und vom 14.12.2017 für den Zeitraum 1.1.2015 bis 9.11.2017 seien für das gegenständliche Verfahren relevante Abfuhrdifferenzen an lohnabhängigen Abgaben in Höhe von insgesamt € 5.821,93 festgestellt worden, wobei es sich dabei um auf den Lohnkonten selbst berechnete Beträge, die von ihm  nicht ans Finanzamt abgeführt wurden, handelte, führte der Beschuldigte in der mündlichen Verhandlung vor dem Bundesfinanzgericht aus: Die Abfuhrdifferenzen könne er sich überhaupt nicht erklären, die Lohnverrechnung sei durch den Steuerberater durchgeführt worden und alle Erlagscheine, die ihm von diesem übermittelt worden seien, habe er auch an das Seite 12 von 21 Finanzamt bezahlt. Er habe in diesem Zeitraum keine finanziellen Probleme gehabt und sei seinen Zahlungspflichten regelmäßig nachkommen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_164`)


Die sich im Rechenwerk des Abgabepflichtigen befindlichen Rechnungen der in der Tz. 4 angeführten Subunternehmen sind mit sehr hoher Wahrscheinlichkeit "Deckungsrechnungen", die lediglich einerseits dazu dienten, die "schwarz" ausbezahlten Löhne in der Buchhaltung unterzubringen und andererseits den beim Finanzamt erklärten Gewinn zu "optimieren".

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_217`)


Selbst in dem zugrunde liegenden Bericht über die Außenprüfung wird davon gesprochen, dass mit sehr hoher Wahrscheinlichkeit "Deckungsrechnungen" vorliegen würden, die lediglich einerseits dazu dienten, die "schwarz" ausbezahlten Löhne in der Buchhaltung unterzubringen und andererseits den beim Finanzamt erklärten Gewinn zu "optimieren".

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_225`)


Keine Anhaltspunkt bieten die Aktenlage und die Ermittlungsergebnisse dafür, dass der Bf. geringere Beträge an Lohnabgaben, als von seinem Steuerberater berechnet, an das Finanzamt gemeldet du somit auch (bei jeweils vorhandenen Guthaben zu den Fälligkeitstagen) entrichtet hätte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_1`)


Die Beteiligten sind: H. F., D., Finanzamt****** StNr.: xx H. P., G., Finanzamt****** StNr.: xxx Die Einkünfte aus Vermietung und Verpachtung werden festgestellt: Jahr 2005 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2006 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2007 - 10.805,72 Aufteilung:   F.H. - 5.402,86 P.H. - 5.402,86 Jahr 2008 14.194,28 Aufteilung:   F.H. 7.097,14 P.H. 7.097,14 Seite 2 von 23 Jahr 2009 18.805,88 Aufteilung:   F.H. 9.402,94 P.H. 9.402,94 Jahr 2010 36.517,94 Aufteilung:   F.H. 16.258,97 P.H. 16.258,97 Jahr 2011 - 8.737,98 Aufteilung:   F.H. - 4.368,99 P.H. - 4.368,99 Gemäß § 101 Abs. 3 BAO sind schriftliche Ausfertigungen, die in einem Feststellungsverfahren an eine Personenvereinigung (Personengemeinschaft) ohne eigene Rechtspersönlichkeit gerichtet sind (§ 191 Abs. 1 lit. a und c BAO), einer nach § 81 BAO vertretungsbefugten Person zuzustellen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_10`)


Das Finanzamt richtete am 8. Juni 2011 folgendes Ergänzungsersuchen an die Bf.: Seite 3 von 23 "Die Personengesellschaft wurde mit 2008 steuerlich erfasst wegen der Vermietung des Objektes in Stadt*****, Ru. 11.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_26`)


Im Zuge einer Nachschau gem. § 144 BAO (am 03.05.2013) kürzte das Finanzamt den Gebäudewert nach einer Berechnung mittels Ertragswertverfahren auf 422.441 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_34`)


Bisherige AfA 20.244,60, AfA nach Nachschau 6.336,62, Differenz: 13.907,99 Das Finanzamt folgte den Ausführungen des Prüfers und erließ am 23.05.2013 neue Bescheide über die Feststellung von Einkünften gem. § 188 BAO für die Jahre 2005 - 2011 und berücksichtigte die AfA in Höhe von € 6.336,62 statt wie bisher von € 20.244,40 mit folgender Begründung: "1) Bewertung Liegenschaft Ru. 10 Als Bemessungsgrundlage für die Liegenschaft wurde ein Gutachten für Versicherungszwecke herangezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_77`)


Das Finanzamt gab mit Beschwerdevorentscheidung nur dem Begehren hinsichtlich eines jährlichen AfA-Satzes von 2% statt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_78`)


Weiters wies das Finanzamt die Beschwerde mit folgender Begründung ab: "Als AfA-Bemessungsgrundlage bei unentgeltlichem Erwerb sind bei Gebäuden, die vor dem 1.8.2008 übertragen wurden, die fiktiven Anschaffungskosten maßgebend.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_167`)


Das Finanzamt gab zum vorgelegten Gutachten im Vorlagebericht folgende Stellungnahme ab: "Zum vorgelegten Gutachten vom 28.10.2014 ist auszuführen, dass Instandhaltungskosten Kosten sind, die durch Hintanhaltung oder Beseitigung von baulichen Schäden aus Abnutzung, Ablagerung und Witterungseinflüssen entstehen (Kranewitter, Liegenschaftsbewertung 6 , 2010, 90).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_196`)


Über die Beschwerde wurde erwogen: Sachverhalt: Folgender Sachverhalt, der der Entscheidung zugrunde zu legen ist, ergibt sich aus den im Akt aufliegenden Unterlagen, den vom steuerlichen Vertreter vorgelegten 3 Gutachten, den Feststellungen des Finanzamtes und den Beschwerdeausführungen: Die Beschwerdeführerin (Bf.), die Personengesellschaft H. P. und F., vermietete das Grundstück in Stadt, Ru. 11, ab 2005 an die H.-GmbH. Laut Schreiben vom 5. August 2011 betrug die Miete monatlich 2.500 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_200`)


Im Zuge einer Nachschau gem. § 144 BAO (am 03.05.2013) kürzte das Finanzamt den Liegenschaftswert nach einer Berechnung mittels Ertragswertverfahren auf 422.441 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_214`)


In der BVE hielt das Finanzamt fest, dass betreffend die Höhe der AfA die Bausubstanz zu berücksichtigen ist und kam in der Berechnung des Ertragswertes und der AfA unter Zugrundelegung der Monatsmiete von € 3.000,-, einer Verzinsung von 4,5% und einer Restnutzungsdauer von 30 Jahre, somit Vervielfältiger von 16,29, zu einem Verkehrswert der Liegenschaft in Höhe von € 410.769,78 abzüglich 20% Grund und Boden auf € 328.615,82.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_215`)


Als AfA-Prozentsatz anerkannte das Finanzamt die von der Bf. angeführten 2%, somit eine AfA in Höhe von 6.572,32 Euro.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_289`)


betreffend die Bausubstanz wurde auf das Vorgutachten und der Nachschau des Finanzamtes verwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_291`)


Seite 21 von 23 Das Finanzamt hat bereits in der Beschwerdevorentscheidung dazu Stellung genommen und ausgeführt, dass im Gutachten vom Juni 2013 keine Feststellungen zur Qualität der Bauausführungen oder allenfalls bereits bestehender Schäden, etwa als Folge aufsteigender Feuchtigkeit angeführt sind, und damit eine kürzere Nutzungsdauer bedingen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexander Schnelldorfer` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_6`)


Dieser Erwerbsvorgang gem. § 1 GrEStG wäre bis zum 15. des zweitfolgenden Monats beim Finanzamt mit Abgabenerklärung und Kopie des Kaufvertrages anzuzeigen gewesen (§ 10 GrEStG).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_8`)


Der Erwerbsvorgang sei innerhalb der gesetzlichen Frist nicht beim Finanzamt angezeigt worden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_13`)


Ein solcher Rechtsvorgang sei gemäß § 10 Abs. 1 GrEStG bis zum 15. des dem Entstehen der Steuerschuld zweitfolgenden Monats dem zur Erhebung der Grunderwerbsteuer zuständigen Finanzamt mittels Abgabenerklärung anzuzeigen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_23`)


Seite 3 von 6 Bei Einhaltung der ihm als Käufer obliegenden Sorgfaltspflicht wäre es geboten und zumutbar gewesen, sich beim Finanzamt oder einem fachkundigen Parteienvertreter über die abgabenrechtlichen Konsequenzen der Kaufabrede in Kenntnis zu setzen und entsprechend dieser Kenntnis zu handeln.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_8`)


Mit Ergänzungsersuchen vom 11.07.2017 forderte das Finanzamt die Bf auf, eine Kopie der  Originalrechnung des Steinmetzbetriebes und eine der Verlassenschaftsabhandlung (Beschluss  vom Gericht), in der das Aktivvermögen angeführt ist, nachzureichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_42`)


Tag  (Fälligkeitstag) des auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden  Kalendermonates eine Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen  Finanzamt einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  (Vorauszahlung) oder den auf den Voranmeldungszeitraum entfallenden Überschuß unter  entsprechender Anwendung des § 20 Abs. 1 und 2 und des § 16 selbst zu berechnen hat.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_4`)


Das Finanzamt X (FA) verneint die Anwendbarkeit, weil der Betrieb des Bf im  Verfahrenszeitraum der Bestimmung des § 111 Abs. 2 GewO 1994 zuzuordnen gewesen und  damit nicht ganzjährig einer Verpflichtung zur Innehabung einer Gewerberechtigung  unterlegen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_4`)


Der Beschwerdeführer machte im Rahmen der Arbeitnehmerveranlagung 2017 nachstehende  Werbungskosten geltend:  Fachliteratur 419,16 €  Fortbildungs-, Ausbildungs- und Umschulungskosten 5.364,12 €  Werbungskosten gesamt 5.783,28 €  Bei der Veranlagung anerkannte das Finanzamt lediglich den Pauschbetrag für  Werbungskosten in Höhe von 132 €; (Bescheid vom 22.1.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_8`)


Mit Beschwerdevorentscheidung vom 11.7.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_38`)


Die Frage des Finanzamtes in seinem Vorhalt vom 22.10.2018 „Wollen Sie die erworbenen  Kenntnisse als selbständig Tätiger verwerten?“ hat der Beschwerdeführer folgendermaßen  beantwortet:  „Ich stelle Überlegungen an, die mit der laufenden Aus- bzw. Weiterbildung erworbenen  Kenntnisse auch als selbständig Tätiger zu verwerten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_15`)


Dagegen sei weder Berufung erhoben, noch seien seitens des Finanzamtes weitere  nach außen erkennbare (verjährungsverlängernde) Amtshandlungen gesetzt worden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_35`)


Da die als verfassungswidrig erkannte Befristung für den hier zu beurteilenden Beschwerdefall  keine Wirkung (mehr) zu entfalten vermag, war der Beschwerde gegen den  Zurückweisungsbescheid des Finanzamtes vom 2.3.2018 auf Grund der oa. VfGH- bzw. VwGH- Erkenntnisse stattzugeben und der Zurückweisungsbescheid aufzuheben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Siegfried Basyurt` (person)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_24`)


Im Akt erliegen zwei Internet-Abfragen des Finanzamtes (EurotaxGlass-Fahrzeugbewertung;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_26`)


Mit Bescheid vom 9.11.2010, StrNr, hat das Finanzamt der Bf für das Fahrzeug Range Rover  Sport 3.0 TDV6 HSE mit der Fahrgestellnummer X1:  a) ausgehend von der Bemessungsgrundlage € 57.090,64 die Normverbrauchsabgabe (NoVA)  im Ausmaß von 14 % unter Berücksichtigung von Malus (§ 6a NoVAG) und Abgabenerhöhung  (§ 6 Abs. 6 NoVAG) im Betrag von€

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_54`)


Das Finanzamt hat in der Folge, ohne eine Berufungsvorentscheidung zu erlassen, die Berufung  samt Verwaltungsakt dem Unabhängigen Finanzsenat zur Entscheidung vorgelegt und die  Abweisung der Berufung beantragt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_58`)


Es ist daher dem Finanzamt zu erläutern und nachzuweisen,  inwieweit die Frau falsche Angaben gemacht haben soll (bezüglich Familienwohnsitz,  Angestelltenverhältnis, Verwendung des PKWs etc.).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_60`)


…"  b) Mail-Schreiben des C vom 26.8.2010, mit dem in der Beilage der Leasingvertrag zum PKW  dem Finanzamt übermittelt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Basyurt` (person)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_73`)


Im Zeitpunkt der Unterfertigung der Niederschrift vor dem Finanzamt durch die Bf (= am  27.7.2010) habe der Tachostand des Fahrzeuges ca. 25.000 km betragen, der aufgrund der  Fahrten des Gatten D-A1-D zustande gekommen wäre;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_165`)


Die Beschwerde richtet sich primär dagegen, dass die Umsätze für die Sexdienstleistungen vom  Finanzamt der Bf. zugerechnet werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_214`)


Die Prostitutionserlöse waren daher vom Finanzamt zu Recht der Bf. zuzurechnen, da sie zum  Betrieb eines Bordells (mit den entsprechenden Auflagen) berechtigt war und sie in  einschlägigen Medien einerseits Werbung für „ihre Girls“ geschalten sowie andererseits –  mehrsprachig - Prostituierte für ihre Bar angeworben hat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_3`)


Entscheidungsgründe  Mit Bescheiden vom 6. Mai 2019 verfügte das Finanzamt die Pfändung und Überweisung einer  Geldforderung der Beschwerdeführerin an die X-Bank zur Hereinbringung der in Höhe von  € 7.870,70 (Abgabenschuldigkeiten in Höhe von € 7.786,22 zuzüglich Gebühren und  Barauslagen für diese Pfändung in Höhe von 84,48).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_4`)


Mit einem weiteren Bescheid vom 6. Mai 2019 setzte das Finanzamt gegenüber der Bf. für  diese Amtshandlung Pfändungsgebühren in Höhe von € 77,86 und Auslagenersätze in Höhe  von € 6,62 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_15`)


Mit Beschwerdevorentscheidungen von 22. Mai 2019 wies das Finanzamt die Beschwerden als  unbegründet ab und führte aus:  a) BVE zur Beschwerde gegen den Pfändungsbescheid  Die Pfändung einer Geldforderung sei gemäß § 65 AbgEO zu Recht erfolgt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_21`)


Informativ werde mitgeteilt, dass der Abzug von monatlich € 30,00 von der Pension nicht für  das Finanzamt erfolge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_31`)


Sofern nicht die  Bestimmung des § 67 zur Anwendung kommt, geschieht die Pfändung dadurch, dass das  Finanzamt dem Drittschuldner verbietet, an den Abgabenschuldner zu bezahlen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_38`)


Werden beschränkt pfändbare Geldforderungen auf ein Konto des Abgabenschuldners bei  einem Kreditinstitut oder der Österreichischen Postsparkasse überwiesen, so ist gemäß § 54  Abs. 1 AbgEO eine Pfändung des Guthabens auf Antrag des Abgabenschuldners vom  Finanzamt insoweit aufzuheben, als das Guthaben dem der Pfändung nicht unterworfenen  Teil der Einkünfte für die Zeit von der Pfändung bis zum nächsten Zahlungstermin entspricht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_40`)


Gemäß § 54 Abs. 3 AbgEO hat das Finanzamt die Pfändung des Guthabens über Antrag des  Abgabenschuldners für den Teil aufzuheben, dessen dieser bis zum nächsten Zahlungstermin  dringend bedarf, um seinen notwendigen Unterhalt zu bestreiten und seine laufenden  gesetzlichen Unterhaltspflichten zu erfüllen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_54`)


Das Finanzamt hat den aufgrund der Pfändung überwiesenen Betrag in Höhe von € 939,67  mittlerweile dem Bf. zurücküberwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_55`)


Das Bundesfinanzgericht geht wie das Finanzamt davon aus, dass die auf das Konto des Bf.  überwiesenen Beträge, dem Pfändungsschutz des § 292i EO unterliegen (vgl. OGH 28.06.2018,  9 Ob 22/18b).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_5`)


Das Finanzamt erließ am 21.8.2018  den Einkommensteuerbescheid 2016, berücksichtigte die geltend gemachten Krankheitskosten  darin nicht und begründete dies wie folgt: „Die Krankheitskosten der Ehegattin konnten nicht  berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_16`)


Mit Beschwerdevorentscheidung vom 27.11.2018 gab das Finanzamt der Beschwerde teilweise  statt und berücksichtigte EUR 724,95 als außergewöhnliche Belastungen mit folgender  Begründung: „Hat ein Pflegebedürftiger sein Vermögen (zB Wohnung, Sparbuch) noch nicht  übertragen, gehen die Pflegekosten zunächst zulasten dieses Vermögens.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_33`)


Das Finanzamt legte die Beschwerde am 20.3.2019 dem Bundesfinanzgericht vor und  beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_35`)


Mit Schreiben vom  10.7.2020 ergänzte das Finanzamt sein Vorbringen dahin, dass in Umsetzung des  Leistungsfähigkeitsprinzips Krankheitskosten für den Ehepartner insoweit als  außergewöhnliche Belastungen anzuerkennen seien, als diese Aufwendungen das Einkommen  des erkrankten Ehepartners unter das steuerliche Existenzminimum von EUR 11.000,- jährlich  herabmindern würden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_95`)


Wenn das Finanzamt vermeint, der freiwillige Verzicht auf eine Verwertung des Vermögens der  Ehegattin führe dazu, dass die Pflegekosten für die Ehegattin vom Beschwerdeführer freiwillig  getragen würden und daher keine Zwangsläufigkeit der Belastungen vorliegen könne, so ist  ihm Folgendes entgegenzuhalten:  Im Zivilrecht wird zwischen Unterhaltsansprüchen von Eltern gegenüber ihren Kindern und  solchen zwischen Ehegatten insofern differenziert, als einerseits die Unterhaltsverpflichtung  von Kinder gegenüber ihren Eltern (unter anderem) jener zwischen Ehegatten im Rang  nachsteht (vgl § 234 Abs. 2 ABGB) und sich andererseits (nur) der Unterhaltsanspruch eines  Elternteiles (unter anderem) insoweit mindert, als dem Elternteil die Heranziehung des  Stammes eigenen Vermögens zumutbar ist (vgl § 234 Abs. 3 ABGB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_98`)


Somit ist der Verweis des Finanzamtes auf die Erkenntnisse  des VwGH vom 29.4.2015, 2012/13/0012 und vom 20.11.2019, Ro 2018/15/0024 ist nicht  geeignet, sein Vorbringen zu stützen: In beiden Erkenntnissen hat der Verwaltungsgerichtshof  über die Abzugsfähigkeit von Unterhaltsleistungen an einen Elternteil im Zusammenhang mit  einer vorangegangenen Vermögensübertragung vom Elternteil auf Nachkommen  abgesprochen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_99`)


Auch das vom Finanzamt angezogene Argument, das dem Abgabenrecht immanente  Leistungsfähigkeitsprinzip würde neben der vorrangigen Verwertung eigenen Vermögens die  Berücksichtigung eines steuerlichen Existenzminimums von EUR 11.000,- bei der Ehegattin  gebieten, würde nach Ansicht des Bundesfinanzgerichts die Abzugsfähigkeit von  außergewöhnlichen Belastungen durch Unterhaltsaufwendungen für Ehegatten über Gebühr  und in einer nicht vom Gesetz gedeckten Weise einschränken.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_17`)


Das Finanzamt ging im  bekämpften Bescheid davon aus, dass er die Strecke vom Wohnort zum Dienstort  (insgesamt 20,2 km) in zwei Etappen zurücklegte, indem er zunächst vom Wohnort zum  Bahnhof_IP (1. Teilstrecke mit 3,4 km) und von dort weiter zum Bahnhof Bahnhof_L (2.  Teilstrecke) gefahren sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_20`)


Im Erstbescheid vom 17.07.2008 hat des Finanzamt „das große Pendlerpauschale bis 20  km“ iHv € 283,50 berücksichtigt (für die Teilstrecke Wohnung bis Bahnhof_IP).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_30`)


Das Finanzamt hat ausgehend von diesen  Unterlagen eine „Auswertung Fahrplan – Dienstzeit“ erstellt und dem BFG vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_31`)


Das  Finanzamt kommt in dieser Auswertung zum Ergebnis, dass das Begehren des  47Beschwerdeführers  zu Recht besteht und ein Pendlerpauschale in Höhe von 1.032 € zu  berücksichtigen ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_46`)


Da auch das Finanzamt (mit Ausnahme der  Monate Februar und Juni) zu diesem Ergebnis kam (vgl. die dem Bundesfinanzgericht  vorgelegte „Auswertung Pendlerpauschale“, in der die Berücksichtigung von Fahrt- kosten im Wege des großen Pendlerpauschales angeregt wurde), erübrigt sich eine  detailliertere Gegenüberstellung der Dienstzeiten und der Ankunfts- und Abfahrtszeiten  der Züge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_47`)


4.2. Soweit das Finanzamt die Inanspruchnahme des Werkverkehrs in den Monaten Februar  und Juni für zumutbar gehalten und deshalb eine Kürzung des Pauschales vorgenommen  hat, ist festzuhalten:    Im Erkenntnis VwGH 27.07.2016, 2013/13/0088 hat der Verwaltungsgerichtshof klar- gestellt, dass die sich aus § 16 Abs. 1 Z 6 lit. b und c EStG 1988 ergebenden Pauschbe- träge auf Grund des Wortlautes des Gesetzes nicht schon dann nicht zustehen, wenn  der Arbeitnehmer im Werkverkehr befördert werden könnte und ihm dies auch zumut- bar wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_23`)


Tag (Fälligkeitstag) des  auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden Kalendermonates eine  Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen Finanzamt  einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  2 von 4 Seite 3 von 4

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_25`)


Nach § 21 Abs 3 UStG 1994 hat das Finanzamt die Steuer festzusetzen, wenn der Unternehmer  die Einreichung der Voranmeldung pflichtwidrig unterlässt oder wenn sich die Voranmeldung  als unvollständig oder die Selbstberechnung als nicht richtig erweist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)
- `Bundesamtes für Soziales  und Behindertenwesen` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_36`)


Das Finanzamt wies den Antrag vom 10.08.2018 auf Familienbeihilfe und erhöhte  Familienbeihilfe mit Bescheid vom 16.01.2019 ab, führte begründend den § 6 Abs. 2 lit. d  FLAG 1967 an und verwies auf das vorstehend angeführte Gutachten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_44`)


Ich bin der Meinung, dass ich in der vom Finanzamt anberaumten  ärztlichen Untersuchung bzw. von der untersuchenden Ärztin nicht ernst genommen wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_85`)


Das Finanzamt wies die Beschwerde mit Beschwerdevorentscheidung ab und führte wie folgt  begründend aus:  „Begründung:  Gemäß § 8 Abs. 5 Familienlastenausgleichsgesetz 1967 (FLAG 1967) gilt ein Kind als erheblich  behindert, bei dem eine nicht nur vorübergehende Funktionsbeeinträchtigung im körperlichen,  geistigen oder psychischen Bereich oder in der Sinneswahrnehmung besteht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_93`)


Die erhöhte Familienbeihilfe steht daher nicht zu.  Im Zuge dieser Erledigung erstellte das Bundesamt für Soziales und Behindertenwesen im  Auftrag des Finanzamtes folgende Bescheinigung(en) über das Ausmaß der Behinderung, die  Ihnen zeitnah und mit separater Post zugesendet wird/werden.“

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesamt für Soziales und Behindertenwesen` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_122`)


Auf Grund des Vorlageantrages wurde über Aufforderung des Finanzamtes die Bf. abermals  untersucht und folgendes 3.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_22`)


Sie könne jedoch nachweisen, dass die Umsatzsteuer aus den betreffenden Rechnungen durch  Dl A B, der seinen Auftrag bei dem Bauprojekt noch nicht abgeschlossen habe, an das  Finanzamt abgeführt worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_47`)


2. Für jedes Projekt wurden sowohl mit der Baufirma als auch mit dem Architekten getrennte  Verträge abgeschlossen und voneinander unabhängige Rechnungen ausgestellt.  3. Die beim Finanzamt eingereichten Vorsteuern betreffen lediglich das Wohnheimprojekt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_50`)


Die Vorsteuern für das Projekt „Wohnheim“ wurden vom Finanzamt […] geprüft und als  vorsteuerabzugsberechtigt deklariert, weswegen wir die Vorsteuern für die Jahre 2017 bis 2019  zurückerhalten haben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_104`)


Gemäß § 11 Abs. 1 Z 3 UStG 1994 gehören zu den Angaben, die eine Rechnung enthalten muss,  u.a. der Name und die Anschrift des liefernden oder leistenden Unternehmers (lit. a), bei  Rechnungen, deren Gesamtbetrag EUR 10.000,00 übersteigt, weiters die dem  Leistungsempfänger vom Finanzamt erteilte Umsatzsteuer-Identifikationsnummer, wenn der  leistende Unternehmer im Inland einen Wohnsitz (Sitz), seinen gewöhnlichen Aufenthalt oder  eine Betriebsstätte hat und der Umsatz an einen anderen Unternehmer für dessen  Unternehmen ausgeführt wird (lit b.) sowie die dem Unternehmer vom Finanzamt erteilte  Umsatzsteuer-Identifikationsnummer, soweit der Unternehmer im Inland Lieferungen oder  sonstige Leistungen erbringt, für die das Recht auf Vorsteuerabzug besteht (lit. i).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_6`)


Entscheidungsgründe  I. Verfahrensgang  A) Verfahren vor dem Finanzamt:  1.)

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_18`)


Am 22.4.2015 wurde mit dem Bf am Finanzamt D zwecks "Abklärung des Sachverhaltes  bezüglich Verwendung eines Fahrzeuges mit ausländischem behördlichen Kennzeichen" eine  Niederschrift folgenden Inhaltes aufgenommen:  " … Ich bin im Jahr 2009 als Leasingarbeiter nach Österreich gekommen und habe für E  gearbeitet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_67`)


Anschließend erliegen im Akt – teils nach Ergänzungsersuchen und Schriftverkehr mit dem  Finanzamt – folgende Unterlagen:  a) Mietvertrag vom 26.5.2010, abgeschlossen zwischen dem Vermieter Fa. ABC und Herrn S  und dem Bf als Mieter:  Mietobjekt ist eine 3-Zimmer-Wohnung mit einer Fläche von ca. 93 m² in D/XX, Y-Str1; zwei  Mieter;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_83`)


Im Akt erliegen mehrere Internet-Abfragen des Finanzamtes (zu Angeboten bei  gebrauchtwagen.at, mobile.de) vom Juli 2015 zu vergleichbaren Pkw der Marke Ford Mustang,  Gebrauchtwagen, Benziner, Bj. 2005 oder 2006, Motorleistung 151 kW (= 205 PS) oder 154 kW,  4 von 29 Seite 5 von 29

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_86`)


Mit Festsetzungs-Bescheiden vom 6.8.2015, StrNr, hat das Finanzamt dem Bf:  A) für das Fahrzeug Ford Mustang mit der Fahrgestellnummer 123x  a) für den Zeitraum 05/2014 ausgehend von der Bemessungsgrundlage (= Netto- Kaufpreis/gemeiner Wert) € 10.866,42 die Normverbrauchsabgabe (NoVA) im Ausmaß von  16 % unter Berücksichtigung des Zuschlages gem. § 6 Abs. 6 NoVAG im Betrag von gesamt  € 2.086,36 vorgeschrieben;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_89`)


Zu allen Bescheiden wurden dem Bf in der Beilage detaillierte Abgaben-Berechnungsblätter  übermittelt. In der jeweiligen Bescheidbegründung führt das Finanzamt nach Darstellung der  bezughabenden gesetzlichen Bestimmungen im Wesentlichen aus:   Laut durchgeführten Erhebungen und eigenen Angaben des Bf sei dieser seit 23.4.2010  durchgehend in Österreich gemeldet und habe das Kfz der Marke Ford Mustang mit dem  ausländischen Kennzeichen X1 seit Oktober 2011 bzw. das Kfz der Marke VW Golf mit dem  ausländischen Kennzeichen Y2 seit 9.4.2015 überwiegend im Inland verwendet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_124`)


Im Ergänzungsersuchen vom 17.3.2016 hat das Finanzamt zunächst festgehalten, dass der  Bf seit Mai 2008 nahezu durchgehend in Österreich beschäftigt und mit Wohnsitz gemeldet  gewesen sei und hat vom Bf eine Vielzahl an Unterlagen – darunter Nachweise zu deutschen  Mietzahlungen, zum Verkauf des Ford Mustang, Service- und Reparaturrechnungen der  Fahrzeuge, zu einem allfälligen deutschen Handyvertrag und Girokonto - , die zum  Gegenbeweis dienen könnten, angefordert.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_150`)


Vom Finanzamt wurden weitere Erhebungen durchgeführt durch:  a) Einsichtnahme in das facebook-Profil des Bf, wo er angibt: "Wohnt in A/XX".

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Baden Mödling`
- `Finanzamtes` — similar text (different position): `Finanzamtes Baden Mödling`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Krafft`(person)
- `Daniel Parys`(person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamtes Baden Mödling`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Landeck Reutte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Li Schukardt`(person)
- `Ursula Buchholz`(person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich`(address)
- `Finanzamtes  Landeck Reutte`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Sven Oberstelehn`(person)
- `Chantal Eligüzel`(person)
- `Glittstein 70, 9072 Rupertiberg, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Landeck Reutte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

</details>

---

## `Tax Authority - Finanzamt Locations` 🏆

**F1:** 0.073 | **Precision:** 0.929 | **Recall:** 0.038  

**Format:** `regex`  
**Rule ID:** `4653df20`  
**Description:**
Matches Finanzamt with specific locations, including complex names and genitive forms.

**Content:**
```
\b(Finanzamt(?:es)?(?:\s+(?:Wien\s+(?:8/16/17|9/18/19(?:\s+Klosterneuburg)?|Klosterneuburg)|Österreich|Salzburg-Land|Bruck\s+Eisenstadt\s+Oberwart|Hollabrunn\s+Korneuburg\s+Tulln|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Vorarlberg|Braunau\s+Ried|Großbetriebe|Feldkirch|Neunkirchen\s+Wr\.\s+Neustadt|für\s+Gebühren\s+Verkehrsteuern\s+und\s+Glücksspiel)))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.929 | 0.038 | 0.073 | 479 | 445 | 34 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 445 | 34 | 11351 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Mag. Josef Nußbaumer` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_3`)


Entscheidungsgründe 1.  Verfahrensgang Nachdem das Finanzamt Salzburg-Land (kurz FA) eine Außenprüfung abgeschlossen hatte (Prüfungsauftrag vom 30. November 2011;

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `N.N.` (person)
- `Dr. Heinz Neuner` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_42`)


In der mündlichen Verhandlung vor dem Spruchsenat beim Finanzamt Wien 9/18/19 Klosterneuburg am 05. Dezember 2018 wurde das Verfahren gemäß § 136 FinStrG eingestellt. Zur Begründung der Einstellung siehe Anhang „20181220_Erkenntnis SPS 05122018“.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `RgR Amalia Schuetzke` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Hollabrunn Korneuburg Tulln` | `Finanzamtes Hollabrunn Korneuburg Tulln` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `VetR OMedR Constantin Wiedewilt` (person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich` (address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19  Klosterneuburg` | `Finanzamtes Wien 9/18/19  Klosterneuburg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn` (person)
- `Floriane Rötker` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_80`)


Der Verfahrensgang vor dem Finanzamt Wien 9/18/19 Klosterneuburg sowie dem  Unabhängigen Finanzsenat bzw. dem Bundesfinanzgericht ist durch die Bescheide, die   7 von 14 Seite 8 von 14

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Braunau Ried` | `Finanzamtes Braunau Ried` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Simone Zemanek, MSc` (person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich` (address)
- `15-763/9594` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Eleonore Sawadzki, Bakk. art.` (person)
- `Weintraubengasse 36, 9073 Aich, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Eugen Burgschweiger` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Bernarda Egli` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kai Rüben` (person)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Sulamith Hördegen` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_6`)


Mit Ersuchen vom 17.12.2018 des Finanzamtes Linz (nunmehr: Finanzamt Österreich) wurde  der Bf. ersucht zum beantragten Vertreterpauschale die nachstehend angeführten Fragen zu  beantworten und dazu Unterlagen beizubringen:  1. Vorlage einer genauen Beschreibung der gesamten beruflichen Tätigkeit des Bf.; samt  Bestätigung der gemachten Angaben durch den Dienstgeber  1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes Linz` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elisabeth Sarigiannis` (person)
- `Klesenza 7, 9587 Erlendorf, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH` (organisation)
- `84-729/8666` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `PhD Mag. Heinrich Hambücher` (person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich` (address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Moebus` (person)
- `Aichach 11m, 9375 Knappenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Techn R Volker Nissle` (person)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Basil Eberhards` (person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `FA Linz` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Pawel Schuwirth` (person)
- `Griselda Hälmle` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `49-622/1059` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Xaver Hüttenroth` (person)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `57-139/5207` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_10`)


Das Finanzamt Neunkirchen Wr. Neustadt richtete an die Bf. ein mit 3. Dezember 2019  datiertes Ergänzungsersuchen u.a. betreffend die zusätzlichen Krankheitskosten aus der  Behinderung.

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr. Neustadt` | `Finanzamt Neunkirchen Wr. Neustadt` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_12`)


Das Finanzamt Neunkirchen Wr. Neustadt berücksichtigte in dem mit 20. Jänner 2020  datierten Einkommensteuerbescheid 2015 folgende außergewöhnliche Belastungen:   80,00 € neutralisiert durch Selbstbehalt in derselben Höhe;

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr. Neustadt` | `Finanzamt Neunkirchen Wr. Neustadt` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_41`)


Das Finanzamt Neunkirchen Wr. Neustadt erließ eine abweisende, mit 27. Februar 2020  datierte Beschwerdevorentscheidung, welche u.a. wie folgt begründet war: „Der Entschluss,  sich im Falle einer Operation an den Arzt des Vertrauens bzw. an ein Privatkrankenhaus zu  wenden, ist durchaus verständlich und nachvollziehbar.

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr. Neustadt` | `Finanzamt Neunkirchen Wr. Neustadt` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_55`)


Das Finanzamt Neunkirchen Wr. Neustadt legte die Beschwerde mit einem Vorlagebericht am  21. Oktober 2020 an das Bundesfinanzgericht vor.

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr. Neustadt` | `Finanzamt Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_60`)


Am 1. Jänner 2021 trat das Finanzamt Österreich gemäß § 323b Abs. 1 BAO an die Stelle des  Finanzamtes Neunkirchen Wr. Neustadt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt Oberwart` | `Finanzamtes Bruck Eisenstadt Oberwart` |
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melchior Englmaier` (person)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melchior Harasymiw` (person)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_37`)


Gegen diese Bescheide vom 18. und 24. November 2020 brachte der Bf. am 25. November  2020 und 7. Dezember 2020 die hier verfahrensgegenständlichen Bescheidbeschwerden ein,  und verwies jeweils zur Begründung „auf meine Ausführungen im Antrag und in der  Beschwerde.“  ****  Mit Beschwerdevorentscheidungen vom 21. Dezember 2020 und 27. Jänner 2021 wies das  Finanzamt Wien 1/23, bzw. das Finanzamt Österreich als Rechtsnachfolger des Finanzamtes  Wien 1/23 die Beschwerden vom 25. November 2020 und 7. Dezember 2021 als unbegründet  ab.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt Wien 1/23` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Romana Stavrakis` (person)
- `Untersameting 4, 4894 Römerhof, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_135`)


IV. Rechtliche Beurteilung  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 tritt das Finanzamt Österreich am 01.01.2021  an die Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_136`)


Partei des  Verfahrens ist nunmehr das Finanzamt Österreich als belangte Behörde, deren Bezeichnung  war somit im Spruch entsprechend richtig zu stellen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holger Buchmüller` (person)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_10`)


Der schriftliche Antrag des Bf an das Finanzamt Salzburg-Land, die Beschwerde zur  Entscheidung dem Bundesfinanzgericht vorzulegen, wurde am 26.03.2019 bei der Post  aufgegeben (Vorlageantrag, Poststempel).

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `James Eisenbürger` (person)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt Oberwart` | `Finanzamtes Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Esra Schlink` (person)
- `Dipl. Kff. Sibylle Wahlscheid` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adam Rueßbült` (person)
- `Timon Reinhertz` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `15-325/9824` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_74`)


Ich beantrage die Entscheidung durch das Bundesfinanzgericht, nach Bedarf auch eine  mündliche Verhandlung.“  II. Das Bundesfinanzgericht hat erwogen:  Gemäß § 323b Abs. 1 BAO treten das Finanzamt Österreich und das Finanzamt für  Großbetriebe für ihren jeweiligen Zuständigkeitsbereich am 1. Jänner 2021 an die Stelle des  jeweils am 31. Dezember 2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt für  Großbetriebe` (organisation)
- `Finanzamtes` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  8/16/17` | `Finanzamtes Wien  8/16/17` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marcel Rac` (person)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `42-508/7924` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Richard Schwanken` (person)
- `Alexandra Hettrich` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Eckard Eizenhammer` (person)
- `KommR Ashley Tönisen` (person)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `16-543/4492` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Aloisa Antoni` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_5`)


Das Finanzamt Österreich trat am 1. Jänner 2021 an die Stelle des Finanzamtes Salzburg-Land  (§ 323b Abs. 1 BAO).

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` (person)
- `Florentine Mugge` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `59-679/2034` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Mag. Susanne Haim` (person)
- `Mag Stefan Raab` (person)
- `Leopold Pichlbauer` (person)
- `Bettina Domigall, Bakk. iur.` (person)
- `Zickhöhe 66, 3361 Biberbach, Österreich` (address)
- `Tanja Grottenthaler` (person)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_14`)


Summe Abzugsteuer lt. Bescheid 353.659,34 370.726,61 432.960,86  Mit einem Antrag vom 27.03.2017, eingereicht beim Finanzamt Bruck Eisenstadt Oberwart  (nunmehr Finanzamt für Großbetriebe), Evidenz-Nr. 1, begehrte die M die Rückzahlung diser  Abzugsteuern von in Summe Euro 921.510,64.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_15`)


Mit drei Anträgen vom 17.12.2018 begehrte die N beim Finanzamt Bruck Eisenstadt Oberwart  (nunmehr Finanzamt für Großbetriebe) jeweils gesondert für die Streitjahre 2013 bis 2015 die  Rückzahlung der Abzugsteuern wie oben dargestellt.  Diese Rückzahlungsanträge sind im Hinblick auf das vorliegende Rechtsmittel noch unerledigt.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien  9/18/19 Klosterneuburg` | `Finanzamt Wien  9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Petra Port` (person)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)
- `Petra Port` (person)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Finanzamtes Waldviertel` (organisation)
- `Petra Port` (person)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_6`)


Bereich des damaligen Finanzamtes Hollabrunn Korneuburg Tulln als Einzelunternehmer  vorsätzlich   a) unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht  hinsichtlich folgender Abgaben eine Verkürzung bewirkt:  Einkommensteuer 2012 in Höhe von € 7.465,00   b) unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht  hinsichtlich folgender Abgaben eine Verkürzung zu bewirken versucht:  Einkommensteuer 2013 in Höhe von € 26.069,00   c) durch die Nichtabgabe der Einkommensteuererklärung 2014, ohne hiedurch den Tatbestand  eines anderen Finanzvergehens zu erfüllen, eine abgabenrechtliche Anzeige-, Offenlegungs-  oder Wahrheitspflicht verletzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Hollabrunn Korneuburg Tulln` | `Finanzamtes Hollabrunn Korneuburg Tulln` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_9`)


Durch das Finanzamt Hollabrunn Korneuburg Tulln wurde festgestellt, dass der Beschuldigte  für das Jahr 2012 zu wenig Einkünfte erklärt hat, wodurch sich für das Jahr 2012 an  Einkommensteuer eine Differenz von € 7.465,00 ergibt.

| Predicted | Gold |
|---|---|
| `Finanzamt Hollabrunn Korneuburg Tulln` | `Finanzamt Hollabrunn Korneuburg Tulln` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_2`)


Beschwerde vom 7.9.2016 gegen die Bescheide des Finanzamtes Österreich - vormals des  FA Kirchdorf Perg Steyr - vom 3.8.2016 betreffend Umsatzsteuer (Vorsteuererstattung) 1-12/2015 und 1- 3/2016, Steuernummer 41-595/2429  und   2.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `FA Kirchdorf Perg Steyr` (organisation)
- `41-595/2429` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_27`)


Zu Spruchpunkt I. (Abweisung)  § 323b Abs. 1 BAO: Das Finanzamt Österreich und das Finanzamt für Großbetriebe treten für  ihren jeweiligen Zuständigkeitsbereich am 1. Jänner 2021 an die Stelle des jeweils am  31. Dezember 2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Babette Bernett` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_76`)


Mit Beschluss des Bundesfinanzgerichts vom 9. Februar 2021 wurde das Finanzamt Österreich  vor dem Hintergrund, dass bislang keine Unterlagen betreffend eine kalkulatorische Schätzung,  5 von 15 Seite 6 von 15

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_78`)


Darüber hinaus wurde  das Finanzamt Österreich um Vorlage der entsprechenden Berechnungsunterlagen ersucht.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_86`)


Begleitschreiben des Finanzamtes Österreich vom 8.3.2021 zur  vorgenannten Rohaufschlagskalkulation.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_87`)


Darüber hinaus wurden dem Beschwerdeführer sowie dem Finanzamt Österreich als Partei  gem § 265 Abs 5 BAO mehrere Berechnungsblätter, in denen eine vom Bundesfinanzgericht  auf der Grundlage der derzeitigen Aktenlage durchgeführte Schätzung abgebildet war, sowie  ergänzend dazu schriftliche Erläuterungen zur Wahl der Schätzungsmethode, zu den  Sachverhaltsannahmen, die der Schätzung zugrunde gelegt wurden, und zur Ableitung der  Schätzungsergebnisse zur Kenntnis gebracht und wurden die Parteien um Übermittlung einer  Stellungnahme zu dieser Schätzung ersucht.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Ingrid Dohrmaier` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `41-654/1190` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Edwin Teiwes` (person)
- `MedR Francois Distefano` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `83-092/9347` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Alice Schöpfel` (person)
- `Walter Guggenmoos` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `79-464/0427` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Jeanne Sohns` (person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich` (address)
- `Gutwirth Consulting Steuerberatungs GmbH,` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Braunau Ried` | `Finanzamtes Braunau Ried` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Carla Winterkorn` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `43-645/1612` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_70`)


Ob diese Zuständigkeit als Annexmaterie zu der expliziten  Sonderzuständigkeit des Finanzamtes für Großbetriebe gemäß § 61 Abs. 4 BAO für  Rückzahlungen von Abgaben und Erstattungen von KESt und Abzugssteuern gehört oder in die  umfassende subsidiäre Zuständigkeit des Finanzamtes Österreich nach § 61 Abs. 1 BAO fällt,  5 von 7 Seite 6 von 7

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes für Großbetriebe` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Juri Siebgen` (person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich` (address)
- `MITTEREGGER Steuerberatungs  GmbH` (organisation)
- `35-670/1415` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Astrid Gänsl` (person)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich` (address)
- `74-872/6854` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Dipl.-Ing. Astrid Gänsl` (person)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_14`)


Mit Beschwerdevorentscheidung des Finanzamtes Österreich vom 7. September 2021 wurde  die Beschwerde als unbegründet abgewiesen und begründend ausgeführt:  „Aufgrund der Wiederaufnahme des Verfahrens betreffend Umsatzsteuer 2015 wurde mit  Bescheid vom 5. August 2021 eine Nachforderung an Umsatzsteuer für 2015 in Höhe von  € 14.970,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  StR OSR Roxana Petkov, Bakk. phil., Am Ramberg 28, 3553 Schiltern, Österreich, über die Beschwerde vom 21. April 2016 gegen den Bescheid des  Finanzamtes Feldkirch vom 1. April 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 Steuernummer 48-815/6843  zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `StR OSR Roxana Petkov, Bakk. phil.` (person)
- `Am Ramberg 28, 3553 Schiltern, Österreich` (address)
- `48-815/6843` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `98-011/6615` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Prof. Leander Pfleumer, LLM` (person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Linz` (organisation)
- `11-306/0925` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Silvius Jaros` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `97-301/3674` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag.Dr. Ingrid Fehrer` (person)
- `Ramon Reissdorf` (person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich` (address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `86-314/1061` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Lieselotte Stiglat` (person)
- `Sibylle Roßmayr` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `58-418/2406` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_13`)


Selbstanzeige beim (damaligen) Finanzamt für Gebühren,  Verkehrssteuern und Glücksspiel (nunmehr Finanzamt Österreich, Dienststelle für  Sonderzuständigkeiten, kurz FA) für die Glücksspielabgabe für den Zeitraum 01/2011 –  11/2016 sowie für Wettgebühren für den Zeitraum 01/2011 – 11/2016.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Gebühren` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Björn Stover` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `57-952/0912` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. September 2020 des Beschwerdeführers Klarissa Fuhljahn, Adr Bf, Steuernummer  21-178/1143, vertreten durch den mit Zustellvollmacht ausgewiesenen Martin Friedl, 4650  Lambach, Marktplatz 2 gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr (nunmehr  Finanzamt Österreich) vom 17. August 2020 betreffend Haftung für Lohnsteuer 2012 – 2017  sowie Festsetzung von Dienstgeberbeiträgen und Festsetzung von Zuschlägen zu den  Dienstgeberbeiträgen für die Jahre 2011 – 2017:  I)

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Klarissa Fuhljahn` (person)
- `21-178/1143` (tax_number)
- `Martin Friedl` (person)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Klaus Krupok` (person)
- `Ernst Eschenbrenner` (person)
- `Irenental 58, 4871 Tiefenbach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `80-953/9265` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_144`)


Der Verfahrensgang vor der belangten Behörde, nunmehr Finanzamt Österreich, sowie dem  Bundesfinanzgericht durch den Einheitswertbescheid, die Bescheidbeschwerde, die  Beschwerdevorentscheidung, den Vorlageantrag und schließlich die Vorlage vor dem  Bundesfinanzgericht und die Zurückziehung des Antrags auf mündliche Verhandlung evident.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dipl.-Ing. Jeanne Handke, Vornbacherweg 166, 5142 Weinberg, Österreich, über die Beschwerde vom 23. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Juli 2021 betreffend Grunderwerbsteuer, Steuernummer 82-448/5450,  Erfassungsnummer 2017, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Jeanne Handke` (person)
- `Vornbacherweg 166, 5142 Weinberg, Österreich` (address)
- `82-448/5450` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dr. Valerius Somuncu, Seelache 250, 2294 Schloßhof, Österreich, vertreten durch Dr-K, Rechtsanwalt in A, über die Beschwerde vom 22. Dezember  2017 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel  (nunmehr: Finanzamt Österreich) vom 23. November 2017 betreffend Grunderwerbsteuer,  Steuernummer 84-691/1997, Erfassungsnummer 10-2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Valerius Somuncu` (person)
- `Seelache 250, 2294 Schloßhof, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `84-691/1997` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Lewis Fröhner` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Marion Schlesing` (person)
- `Dimitri Seewaldt` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `93-757/0582` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_5`)


Das Finanzamt X, jetzt Finanzamt Österreich (FA), verweigert den Abzug mit dem Hinweis auf  die sogenannte „Gegenwerttheorie“.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 7. Mai 2021 der Beschwerdeführerin Liu Maackens, LLM Bakk. techn., Alfons-Petzold-Hof 4, 2042 Grund, Österreich  vertreten durch die mit  Zustellvollmacht ausgewiesene WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG,  Blumauerstraße 35, 4020 Linz, gegen den Bescheid des Finanzamtes Österreich vom 8. April  2021 betreffend Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand gem. §  308 BAO betreffend Erklärung des Widerrufs des Regelbesteuerungsantrages gem. § 6 Abs 3  UStG 1994  zu Recht:    I)  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Liu Maackens, LLM Bakk. techn.` (person)
- `Alfons-Petzold-Hof 4, 2042 Grund, Österreich` (address)
- `WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dora Grobstich` (person)
- `Raul Türkkan` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `24-623/5745` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mag. Niels Rustemeier` (person)
- `Nicoletta Walch` (person)
- `Polheimerweg 2, 3464 Schmida, Österreich` (address)
- `65-653/8677` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

**False Positives:**

- `Finanzamtes  Salzburg-Land` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `RgR Amalia Schuetzke`(person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamtes`(organisation)
- `22-967/4918`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Braunau Ried` — partial — pred is substring of gold: `Finanzamtes  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Karina Ditzler`(person)
- `Hochkoglweg 21, 9560 Nadling, Österreich`(address)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

**False Positives:**

- `Finanzamtes  Hollabrunn Korneuburg Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Linn Förstle`(person)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich`(address)
- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Braunau Ried` — partial — pred is substring of gold: `Finanzamtes  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Priv.-Doz. Timothy Oldenbüttel, Kohlreitweg 2, 4092 Winterhof, Österreich, vertreten durch EHC Wirtschaftstreuhand- gesellschaft m.b.H., Schulgasse 10, 2000  Stockerau, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 5. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Finanzamtes  Hollabrunn Korneuburg Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Timothy Oldenbüttel`(person)
- `Kohlreitweg 2, 4092 Winterhof, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_16`)


Die Höhe des  strafbestimmenden Wertbetrages beruht auf der Betriebsprüfung des Finanzamtes Hollabrunn  Korneuburg Tulln.

**False Positives:**

- `Finanzamtes Hollabrunn  Korneuburg Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_70`)


Zu der als Wiedereinsetzungsantrag bezeichneten Eingabe der Bf vom 12.9.2021 ist zu  bemerken, dass die Entscheidung über den Antrag auf Wiedereinsetzung in den vorigen Stand  jener Behörde obliegt, bei der die versäumte Handlung vorzunehmen war (§ 310 Abs 1 BAO),  sohin dem Finanzamt Österreich.

**False Positives:**

- `Finanzamt Österreich` — partial — pred is substring of gold: `Finanzamt Österreich.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich.`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Susanne Türner, Viehdorfer Straße 25, 9853 Burgwiese, Österreich, gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg  Tulln vom 25. November 2011 betreffend Körperschaftsteuer und Umsatzsteuer 2007,  Steuernummer 16-353/9813  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Hollabrunn Korneuburg  Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Susanne Türner`(person)
- `Viehdorfer Straße 25, 9853 Burgwiese, Österreich`(address)
- `Finanzamtes`(organisation)
- `16-353/9813`(tax_number)

</details>

---

## `City Authority - Stadt Wien` 🏆

**F1:** 0.014 | **Precision:** 0.459 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `0d5c05ff`  
**Description:**
Matches the city entity 'Stadt Wien' when not part of a Magistrat phrase.

**Content:**
```
\b(Stadt\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.459 | 0.007 | 0.014 | 183 | 84 | 99 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 84 | 99 | 11712 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_33`)


Die Abgabe ist mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt Wien  vom 22.12.2005, Heft Nr. 51).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_137`)


Sie haben dadurch folgende Rechtsvorschrift(en() verletzt:   § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung...

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_128`)


Auf Grund dieser Ausführungen des Verfassungsgerichtshofes hat das Bundesfinanzgericht  keine verfassungsrechtlichen Bedenken gegen die Bestimmungen Parkraumbewirtschaftung  der Stadt Wien, soweit sie im gegenständlichen Fall zur Anwendung gelangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofes` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_13`)


Verwaltungsübertretung(en) nach:  1. § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der   geltenden Fassung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,   LGBl. für Wien Nr.9/2006 in der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_33`)


Mit Schreiben vom 4.10.2019 verständigte der Magistrat den Bf. vom Ergebnis der  Beweisaufnahme wie folgt:  "Wir teilen Ihnen mit, dass in folgender Angelegenheit eine Beweisaufnahme stattgefunden  hat:  Vorfall vom 06.06.2018 um 09:29 Uhr, TATORT, Übertretung gem. § 5 Abs. 2  Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006,  in der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrat` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_88`)


Er habe dadurch folgende Rechtsvorschrift(en) verletzt:  § 5 Abs. 2 Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_24`)


Laut Aktenvermerk vom 27. Februar 2020 (Akt Seite 41/58) teilte der Bf. dem Ma- gistrat der Stadt Wien mit, dass er sich dazu nicht äußere.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_18`)


Die dadurch verletzten Rechtsvorschriften waren § 5 Abs 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idgF in Verbindung mit § 4  Abs 1 Wiener Parkometergesetz 2006 LGBl. für Wien Nr. 9/2006 idgF.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_21`)


Im Straferkenntnis vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, warf der Ma- gistrat der Stadt Wien der Bf. vor, sie habe die Wiener Parkometerabgabe dadurch fahrlässig  verkürzt, dass sie das mehrspurige Kraftfahrzeug ihres Ehegatten mit dem im Straferkenntnis  näher bezeichneten behördlichen Kennzeichen am 09.03.2020 um 13:31 Uhr in einer gebüh- renpflichtigen Kurzparkzone abgestellt habe, ohne für seine Kennzeichnung mit einem gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_22`)


Die dadurch verletzten Rechtsvorschriften waren § 5 Abs 2 Wie- ner Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idgF in Verbindung mit § 4  Abs 1 Wiener Parkometergesetz 2006 LGBl. für Wien Nr. 9/2006 idgF.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_9`)


Entscheidungsgründe  Mit Strafverfügung vom 6. Juli 2020 zu Zahl MA67/Zahl1/2020, wurde der Beschwerdeführer  (Bf.) schuldig erkannt, er habe am 06. Mai 2020 um 16:33 Uhr in einer näher genannten  Kurzparkzone in 1030 Wien, Guglgasse 1, mit dem mehrspurigen Kraftfahrzeug mit dem  behördlichen Kennzeichen W-123 (A) durch Abstellen des Fahrzeuges ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültig entwerteten Parkschein  gesorgt zu haben, eine Verwaltungsübertretung gem. § 5 Abs. 2  Parkometerabgabeverordnung, Abl. der Stadt Wien Nr. 51/2005, in der geltenden Fassung, in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, begangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_39`)


Im angefochtenen Straferkenntnis der MA 67 vom 18. September 2020 zur Zahl  MA67/Zahl1/2020 wird zum Einspruch vom 23. Juli 2020 wie folgt ausgeführt:  Der Bf. habe am 06. Mai 2020 um 16:33 Uhr in einer gebührenpflichtigen Kurzparkzone in 1030  Wien, Guglgasse 1, mit dem nach dem behördlichen Kennzeichen W-123 (A) bezeichneten  mehrspurigen Kfz durch Abstellen des Fahrzeuges ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben eine  Verwaltungsübertretung gem. § 5 Abs. 2 Parkometerabgabeverordnung, Abl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, begangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_57`)


Der Bf. habe dadurch folgende Rechtsvorschriften verletzt:  § 5 Abs. 2 Parkometerabgabeverordnung, Abl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_91`)


Als Beweis  in der Anlage finden Sie: Fotos vom Beanstandungsort, Google Maps Plan und Park Plan der  Stadt Wien sowie den ursprünglichen Einspruch und das Straferkenntnis.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_98`)


Die vom Bf. ins Treffen geführten von ihm vorgelegten  Fotos vom Beanstandungsort, sein Hinweis auf Google Maps Plan und auf den Park Plan der  Stadt Wien ändern an dieser Feststellung nichts.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Susette Volmari` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_13`)


Das betreffende Kind befand sich ab 6.2.2019 in voller Erziehung der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_37`)


Sie befinden sich seit April 2019 in voller Erziehung der Stadt Wien und sind in einer  sozialpädagogischen Einrichtung Fremduntergebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_54`)


Das betreffende Kind befand sich ab 6.2.2019 in voller Erziehung der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_75`)


Der Bf. befindet sich seit 16.05.2019 im Krisenzentrum Pleischlgasse, einer  sozialpädagogischen Einrichtung der Stadt Wien, und erzielte seit Ende September 2019 eine  Lehrlingsentschädigung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_92`)


II. Das Bundesfinanzgericht hat erwogen:  Der durch den Kinder- und Jugendhilfeträger Wien (Regionalstelle Rechtsvertretung Bezirke  13,14, 15) vertretene Bf. befand sich im beschwerdegegenständlichen Zeitraum - Mai 2019 bis  Juli 2020 -in voller Erziehung der Stadt Wien und war in einer sozialpädagogischen Einrichtung  fremduntergebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_98`)


Dieser Sachverhalt ist unstrittig und ergibt sich aus dem oben wiedergegebenen Akteninhalt.  Die Beurteilung, ob der Kinder- und Jugendhilfeträger Wien als Vertreter des Bf. zu Recht für  den vergangenen Zeitraum Mai 2019 bis Juli 2020 – in welchem sich der Bf. bereits in voller  Erziehung der Stadt Wien befunden hatte und in einer sozialpädagogischen Einrichtung  fremduntergebracht war (!) – Familienbeihilfe geltend machen konnte oder nicht, ergibt  Folgendes:  Dem Beschluss des Obersten Gerichtshofes vom 20.05.2020, 6 Ob 62/20s (der Bescheid vom  11. August 2020 nennt das Datum 20.5.2020, keine GZ), lag Folgendes zugrunde:  Am 16.7.2019 beantragte der Kinder- und Jugendhilfeträger (KJHT) seine Betrauung mit der  Vermögensverwaltung im Umfang der Beantragung und Verwaltung des Eigenanspruchs des  Kindes auf Familienbeihilfe;

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_149`)


Im Hinblick auf den Umstand, dass sich der Bf. im beschwerdegegenständlichen ‚vergangenen  Zeitraum‘ Mai 2019 bis Juli 2020 bereits in voller Erziehung der Stadt Wien befunden hatte und  in einer sozialpädagogischen Einrichtung fremduntergebracht war, lassen die  höchstgerichtlichen Entscheidungen keinen Zweifel an der Richtigkeit des in der Beschwerde  bzw. im Vorlageantrag vertretenen Standpunktes.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Regina Manegold` (person)
- `Dr.in KzlR Helge Erwied` (person)
- `Unterfeichten 5, 4055 Sipbach, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nina Rasem` (person)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Mag. Peter  Mayerhofer` (person)
- `Magistrates  der Stadt Wien` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_31`)


Sie habe dadurch folgende Rechtsvorschrift(en) verletzt:   § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG)  vom 8. Juli 1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt Wien  Nr. 52/2016, in Zusammenhalt mit § 9 Abs. 1 des Verwaltungsstrafgesetzes 1991 - VStG.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_28`)


Beide Eltern hätten bis  inklusive Februar 2018 Kostenbeiträge an die Stadt Wien geleistet und bis dahin hätten auch  immer wieder Besuche der Kinder bei ihren Eltern stattgefunden.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_43`)


Dazu ist  Folgendes auszuführen:  Der Bf befindet sich aufgrund der mit den Eltern abgeschlossenen Vereinbarung seit  27.01.2016 in voller Erziehung der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rocco Choudhury` (person)
- `Wachtelgasse 7, 9543 Stadt, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_17`)


In Zuge des daraufhin gegen Sie unter der GZ MA67/Zahl3/2020 eingeleiteten Verfahrens kam  hervor (von Ihnen selbst wurde sogar in Ihrem Schreiben vom 19.11.2020 darauf aufmerksam  gemacht), dass zum Beanstandungszeitpunkt keine Übertretung des § 9 Abs. 1  Kontrolleinrichtungenverordnung, ABI. der Stadt Wien Nr. 33/2008 idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, idgF, sondern vielmehr eine  Übertretung des § 5 Abs. 2 Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005  2 von 8 Seite 3 von 8

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_35`)


Die Abgabe ist mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt Wien  vom 22.12.2005, Heft Nr. 51).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Florentin Blatner` (person)
- `Hetzerstraße 11, 4712 Armau, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_86`)


In der Regel erhalten Personen, die bereits über ein Parkpickerl verfügen und bei denen der  Hauptwohnsitz und das Fahrzeugkennzeichen gleich geblieben sind, von der Stadt Wien zwei  Monate vor Ablauf der Gültigkeit zwei Zahlungsanweisungen zugeschickt (Anm.: eine Zahlungs- anweisung für die Verlängerung um ein Jahr, die andere für die Verlängerung um zwei Jahre).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_88`)


Auszug der genannten Homepage  https://www.wien.gv.at/amtshelfer/verkehr/parken/kurzparkzone/parkpickerl.html  "Tipp:  Wenn Sie schon ein Parkpickerl haben und Ihr Hauptwohnsitz und das Kennzeichen des Autos  gleich geblieben sind, schickt Ihnen die Stadt Wien zwei Monate vor Ablauf der Gültigkeit zwei  Zahlungsanweisungen zu. Das Auto muss außerdem auf Sie und ihren Hauptwohnsitz zuge- lassen sein (ausgenommen Firmenfahrzeuge).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_3`)


über die Beschwerde des Lukas Niedergesess, Staudenstraße 7, 3834 Eisenreichs, Österreich, Deutschland, vom 16. Februar 2021, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometer- gesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Lukas Niedergesess` (person)
- `Staudenstraße 7, 3834 Eisenreichs, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der Bodo Saday, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bodo Saday` (person)
- `Alois Windisch-Straße 1, 5121 Hofweiden, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Estelle Ivankovic, Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich, vom 27. Jänner 2022, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, als Abgabenstrafbehörde vom 3. Jänner 2022, Zahl MA67/Zahl/2021, betreffend  eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4  Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl. für  Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Estelle Ivankovic` (person)
- `Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich` (address)
- `Magistrat der  Stadt Wien` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_18`)


Die Abgabe ist mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung, kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) stellte mit Schreiben vom 27.12.2017, eingelangt beim Magistrat  der Stadt Wien am 2.1.2018, den Antrag, die Vergnügungssteuer für den Zeitraum vom  1.1.2012 bis 31.12.2015 bescheidmäßig festzusetzen, da die Bf die Rechtsansicht vertrete, dass  es aufgrund der Kollision der Rechtsnormen Glücksspielgesetz und dem Gesetz über die  Besteuerung von Vergnügen im Gebiet der Stadt Wien (Vergnügungssteuergesetz 2005) zu  einer Doppelbesteuerung komme.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrat  der Stadt Wien` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Diana Sammer` (person)
- `Dipl.-Ing. KzlR Otto Thiesgen` (person)
- `Gränzing 2, 4841 Brunau, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_11`)


Die Bf. habe dadurch die Rechtsvorschrift des § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden Fassung, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung, verletzt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_55`)


§ 4 Pauschalierungsverordnung (Amtsblatt der Stadt Wien Nr. 29/2007, zuletzt geändert durch  die Verordnung Amtsblatt der Stadt Wien Nr. 29/2013) lautet:  (1) Wird die Abgabe in pauschaler Form (§ 2 und § 3 Abs. 1) entrichtet, hat dies durch  Einzahlung des Abgabenbetrages in bar oder nach Maßgabe der der Abgabenbehörde zur  Verfügung stehenden technischen Mittel im bargeldlosen Zahlungsverkehr zu erfolgen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Reifs` (person)
- `Hub an der Mank 8, 9300 Draschelbach, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad über die Beschwerde  des Wilhelm Möncher, Hernalser Gürtel 1, 3192 Furthof, Österreich, vom 4. Juli 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26. Juni 2023, GZ.  MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und das angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Wilhelm Möncher` (person)
- `Hernalser Gürtel 1, 3192 Furthof, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_92`)


Es war daher festzuhalten, dass der Beschwerdeführer sein Kfz in einer ordnungsgemäß  kundgemachten Kurzparkzone ohne gültig entwerteten Parkschein abgestellt hat und daher  eine Verwaltungsübertretung nach § 5 Abs 2 (Wiener) Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 begangen hat.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Theodora Berenwinkel` (person)
- `Klam 26, 8673 Steinhöf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_16`)


Verfahren 1) und 2):  Gegen die (zwei) Strafverfügungen vom 3. November 2023 erhob die Beschwerdeführerin mit  Schreiben vom 27. Dezember 2023 fristgerecht Einspruch und brachte Folgendes vor:  „Strafverfügungen   GZ: MA67/GZ1/2023   GZ: MA67/GZ2/2023   GZ: MA67/GZ3/2023 [Anmerkung BFG: nicht gegenständlich]   Kennzeichen: 123  Sehr geehrte Damen und Herren,   gegen die Strafverfügungen vom 03. November 2023, hier eingegangen am 22. Dezember  2023, zu oben genannten Aktenzeichen erhebe ich hiermit Einspruch und begründe diesen wie  folgt:   Am Montag, den 28. August 2023 bin ich mit meiner Tochter nach über 20 Jahren wieder  einmal für ein paar Tage in die schöne Stadt Wien gereist.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald über die  Beschwerde der Uwe Rossberg, Stadels 61, 8990 Reith, Österreich, vom 1. Februar 2024, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, als Abgabenstrafbehörde vom 24. Jänner  2024, GZ. MA67/GZ/2023, betreffend eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt  Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt  Wien` | `Stadt  Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Mag. Christian Seywald` (person)
- `Uwe Rossberg` (person)
- `Stadels 61, 8990 Reith, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_20`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_21`)


Für höchstens fünfzehn Minuten dauernde Abstellungen sei keine Gebühr zu entrichten, aber  jedenfalls ein Fünfzehn-Minuten-Parkschein zu entwerten bzw. zu aktivieren (vgl. § 2  Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt Wien vom 22.12.2005,  Heft Nr. 51, in Verbindung mit § 2 Abs. 2 der Kontrolleinrichtungenverordnung, Amtsblatt der  Stadt Wien Nr. 29/2013, in der geltenden Fassung).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Verwaltungsstrafsache gegen  Andrea Thünnissen, Kellergasse Helfens 32, 8074 Raaba, Österreich, vom 23. Februar 2020, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Februar 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 17. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet  abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Andrea Thünnissen`(person)
- `Kellergasse Helfens 32, 8074 Raaba, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_3`)


Nr.  10/2013 über die Beschwerde des Beschuldigten vom 20. November 2019 gegen das  Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 6. November 2019,  Zahl: MA 67/186700510526/2018 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_8`)


Entscheidungsgründe  Mit Schreiben des Magistrates der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung, wurde VN-F NN als Zulassungsbesitzerin gemäß § 2 Parkometergesetz  2006, LBGl. für Wien Nr. 9/2006 in der geltenden Fassung aufgefordert, bekanntzugeben, wem  1 von 28 Seite 2 von 28

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_31`)


Mit Schreiben des Magistrates der Stadt Wien, Magistratsabteilung 67, wurde der Bf. als jene  Person, die das ihr vom Zulassungsbesitzer des mehrspurigen Kraftfahrzeuges mit dem  behördlichen Kennzeichen KENNZ zur Verfügung gestellte Fahrzeug einem Dritten überlassen  hat, gemäß § 2 Parkometergesetz 2006, LBGl. für Wien Nr. 9/2006 in der geltenden Fassung  aufgefordert, bekanntzugeben, wem sie das mehrspurige Kraftfahrzeug mit dem genannten  Kennzeichen am 6.6.2018 um 09:29 Uhr überlassen gehabt habe, sodass es zu diesem  Zeiptunkt in TATORT gestanden sei.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Daisy Hoopt`(person)
- `Prof.in StR DDr.in Reneé Plein`(person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)


in der Verwaltungsstrafsache gegen  Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Detlev Griessmer`(person)
- `Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Detlev Griessmer`(person)
- `Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Verwaltungsstrafsache gegen  Heidrun Engehausen, Weinzierlstraße 31, 2292 Engelhartstetten, Österreich, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  über die Beschwerde vom 13. Oktober 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67- Parkraumüberwachung, als Abgabenstrafbehörde vom  18. September 2020, Zahl: MA67/Zahl1/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrates der  Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Heidrun Engehausen`(person)
- `Weinzierlstraße 31, 2292 Engelhartstetten, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `Susette Volmari`(person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_19`)


Mit Vorhalt vom 15.12.2020 ersuchte das Bundesfinanzgericht den Bf, nachstehende Fragen zu  beantworten und die angesprochenen Unterlagen vorzulegen:  1) Vorzulegen sei nicht nur das Deckblatt, sondern der gesamte Bescheid des Magistrates der  Stadt Wien vom 06.10.2015 betreffend „Mindestsicherung, Zuerkennung“.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Magistrates der  Stadt Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Regina Manegold`(person)
- `Dr.in KzlR Helge Erwied`(person)
- `Unterfeichten 5, 4055 Sipbach, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Shoshana Döllmann`(person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 15. Juli 2020,  Zahl MA67/Zahl/2020, wurde der Beschwerdeführer (in weiterer Folge: Bf.) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nina Rasem`(person)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `Mag. Peter  Mayerhofer`(person)
- `Magistrates  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Nina Rasem`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_34`)


Im vorgelegten Akt befinden sich noch folgende Unterlagen:  Vereinbarung der vollen Erziehung vom 24.02.2016, Antrag auf Betrauung mit der  Vermögensverwaltung vom 09.03.2020, Vereinbarung über den Kostenersatz vom 10.03.2016  und Schriftsatz des Magistrates der Stadt Wien, Rechtsvertretung 17,18,19, vom 01.02.2016.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_55`)


Die Vertretungsbefugnis des Magistrates der Stadt Wien Kinder- und Jugendhilfe  Rechtsvertretung 16, 17, 18, 19, ist damit zu bejahen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rocco Choudhury`(person)
- `Wachtelgasse 7, 9543 Stadt, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_9`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wurde über den  Beschwerdeführer eine Geldstrafe in Höhe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt, weil er das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 21. Juli 2020 um 15:19 Uhr in einer gebührenpflichtigen  Kurzparkzone in 1160 Wien, Paltaufgasse 6, abgestellt habe ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Florentin Blatner`(person)
- `Hetzerstraße 11, 4712 Armau, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt  Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hademar Sachteleben, MSc`(person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_2`)


Beschw. vom Zahl VVF VVF vom Zahl Erk. BFG Erk. BFG vom  1) 04.03.2021 MA67/Zahl1/2020 01.03.2021 RV/RV/2020 13.10.2020  2) 04.03.2021 MA67/Zahl2/2020 01.03.2021 RV/RV/2020 13.10.2020  zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) werden die zwei Beschwerden als unbegründet  abgewiesen und werden die angefochtenen zwei Vollstreckungsverfügungen des Magistrates  der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)
- `Magistrates  der Stadt Wien`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Bundesfinanzgerichtes vom 13.10.2020, RV/RV/2020 zu den Zahlen 1)  MA67/Zahl1/2020, 2) MA67/Zahl2/2020 und weitere, nicht gegenständliche Zahlen, wurden  gegenüber dem Beschwerdeführer (Bf.) seine Beschwerden vom 1) 21.09.2020 und 2)  29.09.2020 gegen die Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung  67 vom 1) 17.09.2020, MA67/Zahl1/2020 und 2) 25.09.2020, MA67/Zahl2/2020 als  unbegründet abgewiesen und die Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_3`)


über die Beschwerde des Lukas Niedergesess, Staudenstraße 7, 3834 Eisenreichs, Österreich, Deutschland, vom 16. Februar 2021, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometer- gesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lukas Niedergesess`(person)
- `Staudenstraße 7, 3834 Eisenreichs, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der Bodo Saday, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bodo Saday`(person)
- `Alois Windisch-Straße 1, 5121 Hofweiden, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache (§ 4 Abs. 1  Parkometergesetz 2006) hinsichtlich Hon.-Prof. Reinhard Bodewein, Klein Greinsfurth 49, 9063 Kading, Österreich, über dessen Anbringen vom  15. September 2021 in Zusammenhang mit   Strafverfügung des Magistrates der Stadt Wien, MA 67, vom 16.03.2021,   Vollstreckungsverfügung des Magistrates der Stadt Wien, MA 6 – BA 32, vom  13.09.2021,  jeweils zu GZ. MA67/Zahl1/2020, gemäß § 5 des Gesetzes über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) sowie  § 24 Abs. 1 Satz 2 Bundesfinanzgerichtsgesetz (BFGG) in Verbindung mit (iVm) § 31 Abs. 1  Verwaltungsgerichtsverfahrensgesetz (VwGVG) den Beschluss gefasst:  I.) Beim Anbringen vom 15. September 2021 handelt es sich um keine Beschwerde im Sinne  des Art. 130 Abs. 1 Z 1 Bundes-Verfassungsgesetz (B-VG).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Reinhard Bodewein`(person)
- `Klein Greinsfurth 49, 9063 Kading, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_6`)


Mit Schreiben des Magistrates der Stadt Wien, der Magistratsabteilung (MA) 67 vom 8. März  2021 wurde die Firma xKG, als Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem  behördlichen Kennzeichen Autonummer (A) aufgefordert, binnen zwei Wochen nach  1 von 5 Seite 2 von 5

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_14`)


Mit Schreiben des Magistrates der Stadt Wien, MA 67 vom 21. April 2021  (Verfahrensanordnung – Nachreichung Unterschrift bzw. Vollmachtsvorlage) wurde die Firma  X_KG zur Vorlage einer Vollmacht, aus welcher das Vertetungsverhältnis zu Herrn Bodewein sowie die  Berechtigung zur Einbringung des Rechtsmittels hervorgehe, binnen zwei Wochen nach  Zustellung des Schreibens aufgefordert.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Bodewein`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_18`)


Mit Erkenntnis des Bundesfinanzgerichtes zu GZ. RV/7500480/2021 vom 4. August 2021 wurde  die von X als Geschäftsführer der X_KG eingebrachte Beschwerde vom 21. Mai 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 10. Mai 2021, mit dem der  Einspruch gegen die an Bf ergangene Strafverfügung vom 16. März 2021 zurückgewiesen  2 von 5 Seite 3 von 5

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bodewein`(person)
- `Magistrates der Stadt Wien`(organisation)
- `BFG`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `Dipl.-Ing. KzlR Otto Thiesgen`(person)
- `Gränzing 2, 4841 Brunau, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_127`)


Über die Beschwerde wurde erwogen:  Beweis wurde erhoben durch Einsichtnahme in den Verwaltungsstrafakt des Magistrates der  Stadt Wien, Zahl MA67/Zahl1/2022, die darin aufliegenden drei Fotografien in scharfer  Bildqualität und dem aktenkundigen Bescheid des Magistratischen Bezirksamtes für den 16.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  Pjotr Kristall, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Pjotr Kristall`(person)
- `Schöngrabenweg 12I, 4870 Mösendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138909.1`) (sent_id: `deanon_BFG_20260814_TEST/138909.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter in der Verwaltungsstrafsache Lee Guthöhrlein,  Elisabethinergasse 2, 3041 Paisling, Österreich, über die Beschwerde der Beschuldigten vom 24. September 2022, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Juli 2022, GZ.  MA67/Zahl/2022, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, den Beschluss  gefasst:  Die Beschwerde vom 24. September 2022 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als  verspätet zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lee Guthöhrlein`(person)
- `Elisabethinergasse 2, 3041 Paisling, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138909.1`) (sent_id: `deanon_BFG_20260814_TEST/138909.1_19`)


Das Bundesfinanzgericht hat erwogen:  Feststellungen:  Das Straferkenntnis des Magistrates der Stadt Wien, MA 67, vom 28. Juli 2022 wurde der Bf.  durch Hinterlegung bei der Post-Geschäftsstelle 1082 Wien, Maria-Treu-Gasse 4, am 1. August  2022 zugestellt (Beginn der Abholfrist: Dienstag, 2. August 2022).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138911.1`) (sent_id: `deanon_BFG_20260814_TEST/138911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde der Mag.a Selina Kreutle, Kaposigasse 101, 4906 Pumberg, Österreich, vom 6. September 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 1. August 2022, GZ. MA67/Zahl/2022, wegen einer der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, zu Recht erkannt:  Die Beschwerde vom 6. September 2022 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als  verspätet zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Selina Kreutle`(person)
- `Kaposigasse 101, 4906 Pumberg, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/138911.1`) (sent_id: `deanon_BFG_20260814_TEST/138911.1_20`)


Beweiswürdigung und rechtliche Beurteilung:  Aus dem Verwaltungsakt der belangten Behörde, insbesondere aus dem Übernahmeabschnitt  RSb, ergeben sich folgende Feststellungen:  Die Bf. hat das Straferkenntnis des Magistrates der Stadt Wien, MA 67, vom 1. August 2022 am  3. August 2022 übernommen und die Übernahme mit Unterschrift bestätigt hat.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Günter Möhlenfeld  in Vertretung des verhinderten  Richters Hon.-Prof. Kaspar Frantzius  in der Verwaltungsstrafsache gegen Elias Schwabeland, Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 22. November  2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  15. November 2021, GZ. MA67/Zahl/2021, nach Durchführung einer mündlichen Verhandlung  am 19. Dezember 2022, in Anwesenheit des Beschuldigten und der Schriftführerin IP, jedoch in  entschuldigter Abwesenheit einer Vertreterin/eines Vertreters der belangten Behörde, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat die beschwerdeführende Partei keinen Beitrag zu den Kosten  des Beschwerdeverfahrens zu entrichten.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Günter Möhlenfeld`(person)
- `Hon.-Prof. Kaspar Frantzius`(person)
- `Elias Schwabeland`(person)
- `Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Katharina Bauckholt, Zirknitzberg 11, 3392 Lerchfeld, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 19. Dezember 2022, Zahl: MA67/226701238674/2022, mit dem der Einspruch  vom 1. Dezember 2022 gegen die Strafverfügung vom 10. November 2022 mit derselben  Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Barbara Straka`(person)
- `Katharina Bauckholt`(person)
- `Zirknitzberg 11, 3392 Lerchfeld, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Katharina Bauckholt`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_61`)


Nach dem im Akt aufliegenden Zustellnachweis (AS 16 und 20) wurde die Strafverfügung des  Magistrates der Stadt Wien vom 10. November 2022, Zahl: MA67/226701238674/2022, bei der  Post Geschäftsstelle 0000 hinterlegt und ab dem 15. November 2022 zur Abholung  bereitgehalten, nachdem am 14. November 2022 an der Abgabestelle des Beschwerdeführers  ein erfolgloser Zustellversuch unternommen und die Verständigung von der Hinterlegung in die  Abgabeeinrichtung eingelegt worden war.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen HR Tiffany Vacha, Deutsch-Wagramer Straße 30, 3382 Steinparz, Österreich, wegen der Verwaltungsübertretung  gemäß § 2 in Verbindung mit § 4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde  des Beschuldigten vom 30. Jänner 2023 gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Jänner 2023, GZlen.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `HR Tiffany Vacha`(person)
- `Deutsch-Wagramer Straße 30, 3382 Steinparz, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Verwaltungsstraf- sache gegen Sandra Massin, Grub-Mallinger-Straße 6, 4782 Bubing, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 27. Februar 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. Jänner 2023, GZ.  MA67/226701097306/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 36,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 8 Stunden herabgesetzt  wird.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Renate Schohaj`(person)
- `Sandra Massin`(person)
- `Grub-Mallinger-Straße 6, 4782 Bubing, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_39`)


Der Bf. stellte   1. den Antrag auf Anberaumung einer mündlichen Verhandlung,  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates  der Stadt Wien, MA 67, aufzuheben und das Verfahren einzustellen, in eventu  3. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis dahingehend  abzuändern, dass eine Ermahnung ausgesprochen werde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates  der Stadt Wien`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_43`)


Mit Bescheid des Magistrates der Stadt Wien, Magistratisches Bezirksamt für den 4. und  5. Bezirk vom 4. Oktober 2022, GZ. 123-2022 wurde dem Bf. auf Grund seines Antrages für das  verfahrensgegenständliche Fahrzeug eine Ausnahmebewilligung von der Parkzeitbeschränkung  der im 4. und 5.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_47`)


Beweiswürdigung:  Die Feststellungen ergeben sich aus den eigenen Wahrnehmungen und Anzeigedaten des  Kontrollorgans der Parkraumüberwachung, den zur Beanstandungszeit angefertigten Fotos  sowie aus den Bescheiden des Magistrates der Stadt Wien, Magistratisches Bezirksamt für den  4. und 5. Bezirk.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der Ver- waltungsstrafsache gegen StR Frederike Dalek, Margaretengürtel 113, 3110 Pultendorf, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 22. Februar 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 20. Jänner  2023, GZ. MA67/Zahl/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Frederike Dalek`(person)
- `Margaretengürtel 113, 3110 Pultendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_91`)


Beweiswürdigung  Der unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt und den vom Bf.  vorgelegten Unterlagen (Schreiben des AMS vom 23. Mai 2022 betreffend  Betreuungsvereinbarung, Schreiben des AMS vom 09. Juni 2022 betreffend Gewährung von  Notstandshilfe, Präsenzdienstbestätigung vom 21. März 2022, Bescheid des Magistrates der  Stadt Wien, MA 40, vom 4. Juli 2022, Wiederholer-Prüfungsanmeldung 137827 vom 27. Mai  2022, div. Lehrabschlussprüfungszeugnisse).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `AMS`(organisation)
- `AMS`(organisation)
- `Magistrates der  Stadt Wien`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Klara Hienz, Oberfrödenegg 16W, 4952 Appersting, Österreich, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit §  4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 24. März  2023 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  24. November 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Klara Hienz`(person)
- `Oberfrödenegg 16W, 4952 Appersting, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cornelia Reifs`(person)
- `Hub an der Mank 8, 9300 Draschelbach, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache gegen Birgit Aytekin, Grabenmühlweg 44, 4161 Stollnberg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 26. Mai 2023 gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 9. Mai 2023, GZ.  MA67/[...]/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Birgit Aytekin`(person)
- `Grabenmühlweg 44, 4161 Stollnberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Istvan  Melniczenko, Stritzelberggasse 69, 9142 Jaunstein, Österreich, über die Beschwerde des Beschuldigten vom 16. Juni 2022 gegen  den Zurückweisungsbescheid des Magistrates der Stadt Wien vom 2. Juni 2022, Zahl:  MA67/XX/2021, mit dem der Einspruch vom 3. Mai 2022 gegen die Strafverfügung vom 29.  November 2021 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Istvan  Melniczenko`(person)
- `Stritzelberggasse 69, 9142 Jaunstein, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Istvan  Melniczenko`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Verwaltungsstraf- sache gegen Olivia Zumbruch, Hans Haid-Straße 15, 5233 Hart, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde der Beschuldigten vom 22. Mai 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. April 2023, GZ. MA67/Zahl/2023,  zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren nach § 45 Abs. 1 Z 1 VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Olivia Zumbruch`(person)
- `Hans Haid-Straße 15, 5233 Hart, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad über die Beschwerde  des Wilhelm Möncher, Hernalser Gürtel 1, 3192 Furthof, Österreich, vom 4. Juli 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26. Juni 2023, GZ.  MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und das angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `Wilhelm Möncher`(person)
- `Hernalser Gürtel 1, 3192 Furthof, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_130`)


An dieser Stelle ist festzuhalten, dass die in der Begründung des angefochtenen Bescheides  (Straferkenntnisses) des Magistrates der Stadt Wien angeführten Verweise auf § 99 Abs. 3 lit. a  StVO und den Strafrahmen von 726,00 Euro verfehlt sind, aber keine Auswirkung auf die von  der belangten Behörde verhängte Geld- und Ersatzfreiheitsstrafe hatten, denn 60,00 Euro bzw.  14 Stunden Ersatzfreiheitsstrafe sind genau das Standardstrafmaß, welches die belangte  Behörde erfahrungsgemäß verhängt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad in der  Verwaltungsstrafsache gegen Gudrun Joehnk, Lichtenberger Straße 9, 4751 Obernparz, Österreich, über die Beschwerde der  Beschuldigten vom 15. Mai 2024 gegen den Bescheid des Magistrates der Stadt Wien vom 24.  April 2024, GZ. MA67/GZ/2023, mit dem der Einspruch vom 8. April 2024 gegen die  Strafverfügung vom 8. Februar 2024, mit derselben Geschäftszahl, gemäß § 49 Abs 1 VStG als  verspätet zurückgewiesen wurde, zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen und der angefochtene  Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `Gudrun Joehnk`(person)
- `Lichtenberger Straße 9, 4751 Obernparz, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Gudrun Joehnk`(person)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_26`)


Nach dem im Akt aufliegenden Zustellnachweis (AS 14) wurde die Strafverfügung des  Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023, der Beschwerdeführerin  nach einem erfolglosen Zustellversuch vom 18. März 2024 am 19. März 2024 durch  Hinterlegung zugestellt (und der Beschwerdeführerin persönlich am 21. März 2024 ausgefolgt).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

</details>

---

## `Law Firm - Glatzhofer & Matschek` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1eeac4f2`  
**Description:**
Matches the specific law firm entity.

**Content:**
```
\b(Glatzhofer\s+&\s+Matschek\s+Steuerberatungsgesellschaft\s+mbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 11796 |

</details>

---

## `Company - GCX Möbel GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `280e3fe9`  
**Description:**
Matches the specific company GCX Möbel GmbH.

**Content:**
```
\b(GCX\s+Möbel\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 11796 |

</details>

---

## `Company - VTX E‑Commerce Planung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8800e748`  
**Description:**
Matches the specific company VTX E‑Commerce Planung GmbH.

**Content:**
```
\b(VTX\s+E‑Commerce\s+Planung\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 11796 |

</details>

---

## `Company - RheinBildung Manufaktur GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2a5fdf82`  
**Description:**
Matches the specific company RheinBildung Manufaktur GmbH.

**Content:**
```
\b(RheinBildung\s+Manufaktur\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 11796 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1952, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_22`)

Dieser entspreche laut **BMF**-Erlass vom 11.11.2014, GZ. BMF-010206/0101- VI/5/2014, bei einer Baurechtsdauer von zumindest 50 Jahren dem gemeinen Wert des  Grundstückes.

- missed: `BMF` (organisation)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)

Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der **Universität Wien** vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

- missed: `Universität Wien` (organisation)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_39`)

Da das Gebäude im Zeitpunkt der Erbschaft komplett an die **NiederTextil GmbH** vermietet wurde, eignet sich hier das Ertragswertverfahren zur Berechnung der fiktiven Anschaffungskosten am besten.

- missed: `NiederTextil GmbH` (organisation)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)

Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim **Amt für Betrugsbekämpfung** als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

- missed: `Amt für Betrugsbekämpfung` (organisation)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_28`)

Fahrzeug Kz IT1 sowie zu einem      weiteren Fahrzeug MarkeX, FIN Nr34, zugelassen auf die      Fa. B-GmbH/Ort1 auf das italienische Kz IT2 am 31.7.2012, EZ 3.11.2011;  - Kaufantrag/Bestellung der **Fa.Monal Bau Betriebe GmbHv.** 6.7.2012, woraus hervorgeht, dass      das erstgenannte Fahrzeug für den Kauf des Zweitfahrzeuges (Kz IT2) eingetauscht      wurde;  - Übernahmebestätigung zum zweitgenannten Fahrzeug vom 2.8.2012;  - Nachweise betr. die Vorschreibung bzw. Entrichtung der italien.

- missed: `Fa.Monal Bau Betriebe GmbHv.` (organisation)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_54`)

Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des **Wiener Gemeinderates**, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

- missed: `Wiener Gemeinderates` (organisation)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_10`)

Aus dem diesbezüglich vom Sozialministeriumservice (vormals **Bundesamt für Soziales und  Behindertenwesen**) am 12./13.3.2020 erstellten und der Bf übermittelten ärztlichen  Sachverständigengutachten "mit Untersuchung" durch Amanda Zacharek  Fachärztin für Kinder- und  Jugendheilkunde, geht auszugsweise Folgendes hervor:  "Anamnese:  Termingeburt, verzögerte Meilensteine der Entwicklung, freies Laufen mit 23 Monaten, Sitzen  mit 12 Monaten, Sprachentwicklungsverzögerung.

- missed: `Bundesamt für Soziales und  Behindertenwesen` (organisation)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_120`)

Diese Entscheidung ergeht von:  **Bundesfinanzgericht, Außenstelle Salzburg**, Aigner Straße 10, 5026 Salzburg

- missed: `Bundesfinanzgericht, Außenstelle Salzburg` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_57`)

Dass der StV vergessen habe einen  ausdrücklichen schriftlichen Optionsantrag gemäß § 22 Abs. 6 UStG beim **Finanzamt** für das  Veranlagungsjahr 2017 und Folgejahre einzureichen, sei von diesem in seiner  Vorhaltsbeantwortung vom 12.06.2019 auch eingeräumt worden.

- missed: `Finanzamt` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_57`)

Der **Magistrat** legte die Beschwerden samt den dazugehörigen Verwaltungsakten dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Mai 2020).

- missed: `Magistrat` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_56`)

Nunmehr wurden im Feststellungsbescheid der **Gablonsky&Rethlefsen Gastronomie AG**& atypisch stille Gesellschaft Einkünfte wie folgt zugerechnet:   1. Richsteiger Marine: € -1.520.000,00 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 1.520.000,00 zu berücksichtigen  sind) und  2. Grießhaber Finanzen  GmbH & Co KG: € -838.138,16 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 838.138,16 zu berücksichtigen  sind).

- missed: `Gablonsky&Rethlefsen Gastronomie AG` (organisation)
- predicted in sentence: —

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_7`)

In der u.a. gegen diesen Bescheid erhobenen Beschwerde führte der Bf. aus, im Hinblick auf die  Vorgangsweise des **Finanzamtes** für das Jahr 2017 habe er für 2018 und 2019 eine  entsprechende Jahreserklärung und keinen Vorsteuererstattungsantrag eingereicht.

- missed: `Finanzamtes` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_37`)

Dagegen erhob die **X GmbH** Rekurs sowie Klage auf Löschung der ob den gegenständlichen  Liegenschaften einverleibten Pfandrechten Zug um Zug gegen Bezahlung eines Betrages von  100.098 Euro.

- missed: `X GmbH` (organisation)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_9`)

Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  **Landespolizeidirektion Wien** mit Strafverfügung vom 7. Oktober 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 10. August 2022 in  der gebührenpflichtigen Kurzparkzone in 1180 Wien, Edmund-Weiß-Gasse nächst ONr. 21,  ohne einen für den Beanstandungszeitpunkt 17:14 Uhr gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

- missed: `Landespolizeidirektion Wien` (organisation)
- predicted in sentence: `Magistrat der Stadt Wien, Magistratsabteilung 67`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_57`)

Auch in dem der Entscheidung des Unabhängigen **Finanzsenats** vom 10.7.2012, RV/2144-W/11  (vgl. FINDOK) zu Grunde liegenden Fall ging es u.a. wie beim vorliegenden Fall um die  Berufsunfähigkeits-Zusatzversicherung eines Piloten bei der Gothaer Lebensversicherung a.G.

- missed: `Finanzsenats` (organisation)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_99`)

Auf Grund der im fortgesetzten Verfahren durchgeführten abgabenbehördlichen Ermittlungen  war festzustellen, dass die von der ersten Unternehmerin **Wien Consud AG** (A) in Rechnung gestellte  (inländische) Umsatzsteuer auch abgeführt und nicht wieder berichtigt wurde.

- missed: `Wien Consud AG` (organisation)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_39`)

2022 übermittelte die Bf. dem Bundesfinanzgericht den  Protokollsvermerk und die gekürzte Urteilsausfertigung des **Landesgerichtes** St. Pölten, in dem  sie gemäß § 259 Z 3 StPO vom Anklagevorwurf freigesprochen wurde.

- missed: `Landesgerichtes` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_63`)

2014 war die Basis der Gewerbeausübung des Bf gemäß  §§ 339f GewO 1994 die aufgrund seiner Anmeldung (Anzeige) erfolgte Eintragung in das  Gewerberegister gewesen, die ihm am 27.Febr.2012 gemäß § 340 GewO 1994 durch  Übermittlung eines Auszugs aus dem Gewerberegister durch das **Magistrat** Graz/Referat  Gewerbeverfahren mitgeteilt worden war.

- missed: `Magistrat` (organisation)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des **Finanzamtes Gmunden Vöcklabruck**  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

- missed: `Finanzamtes Gmunden Vöcklabruck` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_316`)

Mit Mail vom 26.8.2020 übermittelte die Richterin dem Bf. per Mail die Beweisfotos, das  Schreiben, welches der **Magistrat** an Dr. YYY gerichtet hatte, den Rückschein, die Niederschrift  über die mündliche Verhandlung und ein Schreiben, dessen Inhalt in der Folge wiedergegeben  wird:  "Anbei wird die Niederschrift der heutigen mündlichen Verhandlung übermittelt, in welcher die  Zeugin (das Organ der Parkraumüberwachung, welches die Anzeige gelegt hat, Frau ZEUGIN)  einvernommen wurde.

- missed: `Magistrat` (organisation)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_74`)

Ich beantrage die Entscheidung durch das Bundesfinanzgericht, nach Bedarf auch eine  mündliche Verhandlung.“  II. Das Bundesfinanzgericht hat erwogen:  Gemäß § 323b Abs. 1 BAO treten das Finanzamt Österreich und das **Finanzamt für  Großbetriebe** für ihren jeweiligen Zuständigkeitsbereich am 1. Jänner 2021 an die Stelle des  jeweils am 31. Dezember 2020 zuständig gewesenen Finanzamtes.

- missed: `Finanzamt für  Großbetriebe` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Bundesfinanzgericht`, `Finanzamt Österreich`, `Finanzamtes`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)

Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals **Finanzamt Lilienfeld St. Pölten**) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

- missed: `Finanzamt Lilienfeld St. Pölten` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Österreich`, `Finanzamt`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140311.1`) (sent_id: `deanon_BFG_20260814_TEST/140311.1_5`)

Mit Bescheid des **Finanzamtes Wien 4/5/10** vom 5. Juni 2019 wurde das Ansuchen um  Bewilligung einer Zahlungserleichterung mit der Begründung abgewiesen, das Ansuchen  enthalte keine Begründung.

- missed: `Finanzamtes Wien 4/5/10` (organisation)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_130`)

Der sich nach Zurechnung gemäß Abs. 1 ergebende Betrag ist gemäß § 15 Abs. 2 LuF-PauschVO  2015 um den Wert der Ausgedingelasten (Geld- und Sachleistungen), um Beiträge, die an die  **Sozialversicherungsanstalt der Bauern** entrichtet wurden, um bezahlte Schuldzinsen und um  bezahlte Pachtzinse zu vermindern, wobei der Abzug der bezahlten Pachtzinse 25% des auf die  zugepachteten Flächen entfallenden Einheitswertes nicht übersteigen darf.

- missed: `Sozialversicherungsanstalt der Bauern` (organisation)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_1`)

Entscheidungsgründe Mit Erkenntnis des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016 wurde der nunmehrige Beschwerdeführer N.N. (in der Folge kurz Bf. genannt) der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG für schuldig erkannt, er habe fahrlässig unter Verletzung der ihm gemäß § 10 Grunderwerbsteuergesetz obliegenden Anzeige-, Offenlegungs- und Wahrheitspflicht, indem er es als anzeigepﬂichtiger Erwerber unterlassen habe, den Kaufvertrag mit A.B. vom 07.01.2013 betreffend die Liegenschaft EZ **Berg-Bildung KG**  Ortsname bis zum 15.

- missed: `Berg-Bildung KG` (organisation)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_66`)

Mein Einkommen vom AMS beträgt 9,14 Euro täglich.“  Beilagen:   Teilnahmebestätigung KUS-Netzwerk vom 05.10.2022, Vorbereitung auf die LAP,  04.07.2022-30.09.2022, 60 Unterrichtseinheiten   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 11.03.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 30.06.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 23.09.2021   Wiederholerprüfungsanmeldung Nr. 137827 vom 27.05.2022   Mitteilung über den Leistungsanspruch, **AMS** vom 09.06.2022:     4 von 16 Seite 5 von 16

- missed: `AMS` (organisation)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_43`)

Mit Beschwerdevorentscheidung vom 3.11.2020 berücksichtigte das **Finanzamt** für das Jahr  2019 Kosten der doppelten Haushaltsführung iHv.

- missed: `Finanzamt` (organisation)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_60`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Vom 27. Jänner 2020 bis (voraussichtlich) 31. August 2020 hatte der im Juni 1999 geborene  Sohn des Bf. – am Beginn des Rückforderungszeitraumes somit bereits volljährig – an einem  Ausbildungslehrgang im Rahmen der Überbetrieblichen Lehrausbildung des  Wirtschaftsförderungsinstitutes NÖ im Auftrag des AMS NÖ teilgenommen (WIFI- Bestätigung  vom 24.07.2020):   „Gemäß § 30 BAG ist-dieser Teilnehmer Lehrlingen gleichgestellt.   Die im Ausbildungslehrgang zurückgelegte Praktikumszeit ist der Lehrzeit im betreffenden  Lehrberuf gleichgestellt:   von 27.01.2020 bis voraussichtlich 31.08.2020 Einzelhandel – Einrichtungsberatung“   Am 25. September 2020 hatte der Sohn des Bf. eine Ausbildung im Rahmen des   **AMS**-Tourismuscenters begonnen, die im Mai 2022 enden sollte (WIFI- Bestätigung  vom 12.1.2021):   Ziel der Ausbildung ist die Ablegung der Lehrabschlussprüfung, welche voraussichtlich   im Mai 2022 stattfinden wird.

- missed: `AMS` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142534.1`) (sent_id: `deanon_BFG_20260814_TEST/142534.1_6`)

und der **Unter Dorfverfurt GmbH**  als Pächterin, mit € 188.100,00 vorläufig gemäß § 200 Abs. 1 BAO festgesetzt.

- missed: `Unter Dorfverfurt GmbH` (organisation)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_178`)

Der Kapitalmarktprospekt der **Richsteiger Marine**  wurde am 23. Juli 2008 und jener der Grießhaber Finanzen  GmbH & Co KG am 23. Jänner 2009 aufgelegt.

- missed: `Richsteiger Marine` (organisation)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_10`)

Entscheidungsgründe  Verfahrensgang  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der **Landespolizeidirektion Wien** am 15. Februar  2022 in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Aignerstraße 6, beanstandet, da  zur Beanstandungszeit 18:48 Uhr ein gültiger Parkschein fehlte.

- missed: `Landespolizeidirektion Wien` (organisation)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_4`)

Entscheidungsgründe  Verfahrensgang  Im Zuge einer GPLA stellte der Prüfer fest, dass über Auftrag des **AMS** von der  Beschwerdeführerin (Bf) Migranten als Lehrlinge in Deutsch unterrichtet wurden und auf eine  Lehrstelle in einem Betrieb vorbereitet wurden.

- missed: `AMS` (organisation)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_23`)

04. 2020, RE/7100001/2020 an den Gerichtshof der Europäischen Union  gemäß Art. 267 AEUV gestellte Ersuchen um Vorabentscheidung, ob die Indexierung von  Familienleistungen durch den österreichischen Gesetzgeber nach der Kaufkraft in den  einzelnen Mitgliedsstaaten bzw. Vertragsstaaten unionsrechtskonform ist, protokolliert zu C- 163/20, gemäß Artikel 100 Abs. 1 Verfahrensordnung des Gerichtshofs der **Europäischen Union**  und § 290 Abs 3 BAO zurückgenommen.

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_72`)

Folglich handelte es sich  bei der in Rechnung gestellten Umsatzsteuer um eine gesetzlich geschuldete (siehe dazu  ausführlich Haller, Vorsteuerabzug bei innergemeinschaftlichen Lieferungen, SWK 25/2019,  1046 mit Hinweis auf VwGH 30.6.2005, 2003/15/0059 und **BMF** 28.

- missed: `BMF` (organisation)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_64`)

Zwecks  Erbringung des Gegenbeweises iSd § 82 Abs. 8 KFG seien die telepass-Abrechnungen der  "Autostrade per lÌtalia SPA" der **Fa.Monal Bau Betriebe GmbH** für alle Fahrzeuge des Unternehmens vorgelegt  worden.

- missed: `Fa.Monal Bau Betriebe GmbH` (organisation)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_84`)

Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom **Bundesministerium für Finanzen** im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

- missed: `Bundesministerium für Finanzen` (organisation)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_138`)

Das **Bundesfinanzgericht (BFG)** erkennt vor diesem Hintergrund keine Unionsrechtswidrigkeit  der Gebührenerhebung im Zusammenhang mit der Anzeigepflicht nach dem Tiroler  Schischulgesetz, da die hier anzuwendenden Tatbestände des Gebührengesetzes keine  Differenzierung danach enthalten, ob sie von in- oder ausländischen Rechtssubjekten  verwirklicht werden.

- missed: `Bundesfinanzgericht (BFG)` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `BFG`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_66`)

Betreffend die Kisteler Telekom GmbH legte der Beschuldigte einen abverlangten Firmenbuchauszug vom 6.4.2012, Gewerberechtsbescheid vom 1.9.2011, Daten des Steueraktes für 2012 vom 6.2.2012 und 5 Auszüge aus der HFU-Liste, eine MIAS-Abfrage vom 24.4.2012 sowie die an die **Furtder Technologien GmbH** gelegten Rechnungen samt Zahlungsbestätigungen und Ersatzschecks (Barabhebungen) im Betrag von € 126.000,00 vor.

- missed: `Furtder Technologien GmbH` (organisation)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_108`)

Bei Fernwärme hätten Österreichs Energieversorger die Preise innerhalb der  **Europäischen Union** am deutlichsten erhöht.

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_33`)

Zudem hielt er im Privatvermögen sämtliche Anteile an der **Lemuni Bau GmbH**, FN ***, mit dem  Geschäftszweig Eisstrahl-Dienstleistungen, Fahrzeughandel, Handelsagent, Handelsgewerbe  mit Ausnahme der reglementierten Handelsgewerbe, Baustoffhandel und Baustoffproduktion,  Transport und Spedition.

- missed: `Lemuni Bau GmbH` (organisation)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_109`)

Dem Beschluss des **Obersten Gerichtshofes** vom 24.10.2012, 8 Ob 99/12k, lag Folgendes  zugrunde:  Mit Eingabe vom 21.7.2011 stellte der Jugendwohlfahrtsträger Wien namens des  Minderjährigen den Antrag auf Erhöhung des Unterhaltsbeitrags des Vaters ab 1.10.2010 auf  monatlich 650 EUR.

- missed: `Obersten Gerichtshofes` (organisation)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_169`)

2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in  Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl.  Kapitalmarktprospekt Richsteiger Marine  und **Grießhaber Finanzen**  GmbH & Co KG Punkt 2.14).

- missed: `Grießhaber Finanzen` (organisation)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_47`)

Von diesem Vorwurf wurden die beiden Angeklagten nach durchgeführter Hauptverhandlung  mit Urteil des **Landesgerichts St. Pölten** vom 2. März 2022 freigesprochen, weil das  Landesgericht die in der Anklage vorgeworfenen Unternehmensentscheidungen im Konzern als  fremdüblich vertretbar beurteilte.

- missed: `Landesgerichts St. Pölten` (organisation)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_75`)

Auch wenn die Käufer im Jänner 2015 den Kaufvertrag und ca. 1 Monat später den  Werkvertrag unterzeichneten, so ergibt sich    aufgrund der Vorausplanung,   dem Gesamtkonzept der Anlage, in das die MH-Bau GmbH bereits eingebunden war  (siehe Energieausweise), und   dem Umstand, dass die **MH-Bau GmbH** die gesamte Doppelhausanlage als Bauführerin  errichtet hat,  dass der Kauf des gegenständlichen Grundstückes im unbebauten Zustand nicht möglich war.

- missed: `MH-Bau GmbH` (organisation)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_32`)

In einer solchen Situation  hinsichtlich der Vertretungsbefugnis danach zu differenzieren, ob der Antrag nur laufende  Perioden ab Antragstellung oder in gewissem Umfang auch - von der Antragstellung her  betrachtet - rückwirkende Perioden betrifft, steht einerseits nicht im Einklang mit der  genannten Rechtsprechung des **Obersten Gerichtshofes** und steht andererseits auch den  praktischen Bedürfnissen an einer einheitlichen Zuordnung der Vertretungsbefugnis und damit  einer raschen Abwicklung ohne zwingenden Grund entgegen.

- missed: `Obersten Gerichtshofes` (organisation)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_7`)

Die Zustellung des Erkenntnisses RV/RV/2020 wurde vom Bundesfinanzgericht mit  Rückscheinbrief RSb angeordnet, wurde gemäß aktenkundiger Übernahmebestätigung RSb  nachweislich vom Bf. am 21.10.2020 übernommen und galt mit 21.10.2020 als zugestellt.  Mit Datum 01.03.2020 erließ der **Magistrat** unter Berufung auf die §§ 3 und 10  Verwaltungsvollstreckungsgesetz (VVG) die beschwerdegegenständlichen  Vollstreckungsverfügungen 1) bis 2) und forderte den Bf. auf, die rechtskräftigen Geldstrafen in  Höhe von jeweils € 60,00 – Strafkosten iHv jeweils € 10,00, VKII – Beschwerdekosten BFG iHv  jeweils € 12,00 und Mahngebühr iHv jeweils € 5,00 zu bezahlen, wodurch sich die offene  Forderung inklusive Mahngebühren gemäß § 54b Abs. 1a VStG auf jeweils € 87,00 belief.

- missed: `Magistrat` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `BFG`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_165`)

Auf die von der Beschwerdeführerin bereits im vormaligen verwaltungsgerichtlichen Verfahren  ins Treffen geführte Entscheidung des **Obersten Gerichtshofes** vom 24. Juni 2019, 2 Ob  221/18s war mit Fokus auf die Sache des gegenständlichen Verfahrens primär auf die Thematik  der Bindungswirkung des „Vorprozesses“ einzugehen;

- missed: `Obersten Gerichtshofes` (organisation)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_70`)

Der Verkauf der Doppelwohnhäuser in A/L wurde von der **MH-Bau GmbH** und der MH-Immo  GmbH beworben.

- missed: `MH-Bau GmbH` (organisation)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_95`)

Beweis wurde erhoben durch Einsichtnahme in die Anzeige vom 06.06.2018 samt Fotos, welche  von einem Organ der **Landespolizeidirektion Wien** erstattet wurde, der Lenkerauskunft vom  08.11.2018, wonach das Fahrzeug Ihnen von der Zulassungsbesitzerin (VN-F NN) überlassen  war sowie Ihrer Bekanntgabe vom 30.07.2019, wonach das Fahrzeug Vera Schliephacke überlassen  war.

- missed: `Landespolizeidirektion Wien` (organisation)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Dorothea Grosseholz  in der Beschwerdesache Miroslav Runau,  Neu Amerika 13, 4623 Fernreith, Österreich, über die Beschwerde vom 19. Juni 2019 gegen den Einkommensteuerbescheid  2018 des **FA Steiermark Mitte**  vom 18. Juni 2019, Steuernummer 89-067/6879, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `FA Steiermark Mitte` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

</details>

---

