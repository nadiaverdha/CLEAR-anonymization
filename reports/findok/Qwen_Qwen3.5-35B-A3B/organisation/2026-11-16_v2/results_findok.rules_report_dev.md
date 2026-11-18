# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-16T12:10:10.384856

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
| Accuracy (exact match) | 96.2% |
| True Positives | 9807 |
| False Positives | 378 |
| False Negatives | 2803 |
| Total Gold Entities | 12610 |
| Micro Precision | 96.3% |
| Micro Recall | 77.8% |
| Micro F1 | 86.0% |
| Macro F1 | 86.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Courts - Verwaltungsgerichtshof` | 30.0% | 100.0% | 17.6% | 2223 | 2223 | 0 |
| `Courts - Verfassungsgerichtshof` | 1.9% | 100.0% | 0.9% | 118 | 118 | 0 |
| `Law Firm - Glatzhofer & Matschek` | 0.1% | 100.0% | 0.0% | 5 | 5 | 0 |
| `City Authority - Magistrat der Stadt Wien` | 3.2% | 99.0% | 1.6% | 206 | 204 | 2 |
| `Courts - Bundesfinanzgericht` | 53.6% | 98.2% | 36.8% | 4732 | 4646 | 86 |
| `Tax Authority - Finanzamt Locations` | 7.8% | 95.5% | 4.1% | 536 | 512 | 24 |
| `Tax Authority - Generic Finanzamt` | 27.1% | 91.9% | 15.9% | 2185 | 2007 | 178 |
| `City Authority - Stadt Wien` | 1.4% | 51.1% | 0.7% | 180 | 92 | 88 |
| `Company - GCX Möbel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company - VTX E‑Commerce Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company - RheinBildung Manufaktur GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Courts - Verwaltungsgerichtshof` 🏆

**F1:** 0.300 | **Precision:** 1.000 | **Recall:** 0.176  

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
| 1.000 | 0.176 | 0.300 | 2223 | 2223 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2223 | 0 | 10387 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_1`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_65`)


Zulässigkeit einer Revision Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_66`)


Zum Mängelbehebungsauftrag- zu dessen Rechtswirksamkeit bzw. zu den Rechtsfolgen von zu Unrecht ergangenen Mängelbehebungsaufträgen - gibt es eine Rechtsprechung des Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_1`)


2.Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art 133 Abs 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_63`)


Allgemein fallen unter den im Gesetz nicht definierten Begriff der Berufsausbildung iSd § 2 Abs 1 lit b FLAG 1967 nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes (jedenfalls) alle Arten schulischer oder kursmäßiger Ausbildungen, in deren Rahmen noch nicht berufstätigen Personen ohne Bezugnahme auf die spezifischen Tätigkeiten an einem konkreten Arbeitsplatz das für das künftige Berufsleben erforderliche Wissen vermittelt wird (vgl zB VwGH 15.12.2009, 2007/13/0125, mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_85`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B- VG die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung Seite 7 von 7 fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_86`)


Ob ein Kind eine Berufsausbildung absolviert, ist nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes eine Tatfrage, welche in freier Beweiswürdigung zu beantworten ist (vgl zB VwGH 18.11.2008, 2007/15/0050 mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_3`)


Die Bemessungsgrundlagen und die Höhe der Abgabe sind den beiliegenden Berechnungsblättern zu entnehmen  und bilden einen Bestandteil dieses Spruches . Eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) ist unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_32`)


Zur Vorläuﬁgkeit von Bescheiden ist im Übrigen auch auf die ständige Rechtsprechung des Verwaltungsgerichtshofes hinzuweisen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_35`)


Die in der Berufungsvorentscheidung zitierte Literatur steht im Widerspruch zum Rechtsverständnis des Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_40`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes kommt es auf die objektive Beseitigung der Ungewissheit an.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_116`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (z.B. VwGH 29.11.2010, 2010/17/0188) unterbrechen bzw. verlängern schriftliche Erledigungen die Verjährung nur dann, wenn sie (wirksam) zugestellt wurden.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_157`)


In seinem Erkenntnis vom 29.1.2015, 2012/15/0121 führte der Verwaltungsgerichtshof ua folgendes aus: "Das Verfahren zur Feststellung nach § 188 BAO zielt auf die Geltendmachung des Einkommensteueranspruches gegenüber den Beteiligten ab.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_187`)


5. Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist die Notwendigkeit eines Arbeitszimmers nach der Art der Tätigkeit des Steuerpflichtigen zu beurteilen (vgl. VwGH 2.9.2009, 2005/15/0049;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_3`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_64`)


Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_85`)


Hinsichtlich der Fragen, ob eine Zustellung des Einkommensteuerbescheides 2018 rechtmäßig  bewirkt wurde bzw. ob der darauf basierende Säumniszuschlag zu Recht festgesetzt wurde,  weicht die Entscheidung weder von der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes ab noch fehlt es an einer solchen Rechtsprechung, die im Übrigen  auch nicht als uneinheitlich zu beurteilen ist (vgl. 3.1.).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_84`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_149`)


4.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_151`)


Dieses Erkenntnis folgt der in diesem Erkenntnis zitierten, einheitlichen Rechtsprechung des  Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_12`)


Die von der Bf dagegen erhobene außerordentliche Revision hat der Verwaltungsgerichtshof  mit Beschluss vom 12. Juni 2020, Ra 2017/16/0116, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_15`)


Das Bundesfinanzgericht hat erwogen:  Der Verwaltungsgerichtshof hat im Erkenntnis vom 19. Oktober 2017, Ra 2017/16/0098,  ausgesprochen, dass die mit dem Abgabenänderungsgesetz 2015 erfolgte Novellierung ua des  § 108 ZollR-DG auf die Anpassung der Rechtslage an den am 1. Mai 2016 in Kraft getretenen  Zollkodex der Union - UZK abzielt. Es sei nicht ersichtlich;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_20`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  2 von 3 Seite 3 von 3

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_21`)


Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_46`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_3`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_6`)


Er habe sich jedoch die Kosten für eine a.o.  Revision beim Verwaltungsgerichtshof nicht leisten können.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_90`)


Zur Zulässigkeit der Revision (Spruchpunkt II)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_17`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision gemäß Art. 133 Abs. 4 iVm  Abs. 9 B-VG zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche  Bedeutung zukommt, insbesondere weil der Beschluss von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_5`)


2. Eine Revision gegen dieses Erkenntnis an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) ist zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_158`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_13`)


(siehe Erkenntnis des Verwaltungsgerichtshofes GZ Ra 2018/16/0203 vom 18.12.2018.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_20`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes fallen unter den Begriff der  "Berufsausbildung" alle Arten schulischer oder kursmäßiger Ausbildung, in deren Rahmen noch  nicht berufstätigen Personen ohne Bezugnahme auf die spezifischen Tätigkeiten an einem  konkreten Arbeitsplatz für das künftige Berufsleben erforderliches Wissen vermittelt wird  (VwGH 1.3.2007, 2006/15/0178, 20.2.2008, 2016/15/0076, 18.11.2008, 2007/15/0050).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_25`)


Der Verwaltungsgerichtshof hat sehr deutlich den Unterschied der im Bereich des  Bundesministeriums für Inneres vorhandenen exekutivdienstlichen Ausbildungen  aufgearbeitet:   Zur Verdeutlichung werden die Unterschiede der Ausbildungslaufbahn der ‘Grenzpolizisten‘  jenen der ‘Polizisten‘ (Exekutivdienst) überblicksmäßig gegenübergestellt:   Fremden- u. grenzpolizeilicher Exekutivdienst   (Erlass des BMI-SI1400/1082-SIAK-ZGA/2015  vom 09.12.2015)   Grundausbildung für den Exekutivdienst   (Verordnung des Bundesministers für Inneres über  die Grundausbildungen für den Exekutivdienst -   Grundausbildungsverordnung - Exekutivdienst BMI,  BGBl. II Nr. 153/2017)   Basisausbildung: 6 Monate (Lehrplan,  Stundentafel - Unterrichtseinheiten 880,  mündliche Prüfung, Zeugnis), Entgelt: 50,29%  des Referenzbetrages (§ 3 Abs. 4 GG)   Basisausbildung: 12 Monate (Lehrplan,  Stundentafel)   Entgelt: 50,29% des Referenzbetrages (§ 3  Abs. 4 GG) während der gesamten Ausbildung   Kursunterbrechung - Verwendung im  fremden- und grenzpolizeilichen Bereich   sowie Unterstützung im  sicherheitspolizeilichen Bereich   Entgelt: SONDERBESTIMMUNGEN -  Normalentgelt Exekutivdienstliche Zulagen  und Nebengebühren   Berufspraktikum I - 3 Monate   Kennenlernen des Dienstbetriebes ...

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `BMI` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_27`)


Dienstprüfung   Unterrichtseinheiten gesamt: 2046  Unterrichtseinheiten: gesamt 2612   Der Verwaltungsgerichtshof hat ferner festgehalten, dass es unstrittig ist, dass die  Basisausbildung der Grundausbildung für die exekutivdienstliche Verwendung im fremden- und  grenzpolizeilichen Bereich (Dauer 6 Monate) und die Ergänzungsausbildung zur  Grundausbildung für den Exekutivdienst (9 Monate) als Berufsausbildung im Sinne des  Familienlastenausgleichsgesetzes anzusehen sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_30`)


Dass im Zuge einer Berufsausbildung praktische und nicht nur theoretische Kenntnisse  vermittelt werden können und etwa im Praktikum zu vermittelnde praktische Grundkenntnisse  unter die Berufsausbildung fallen, hat der Verwaltungsgerichtshof etwa im Erkenntnis vom  22. Dezember 2011, 2009/16/0315, ausgesprochen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_40`)


Nach der  ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Ziel einer Berufsausbildung im  Sinn des FLAG 1967, die fachliche Qualifikation für die Ausübung des angestrebten Berufes zu  erlangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_44`)


Laut Verwaltungsgerichtshof können im Zuge einer Berufsausbildung auch praktische und nicht  nur theoretische Kenntnisse vermittelt werden (zB VwGH 22.12.2011, 2009/16/0315) und es  fällt auch ein „duales System“ der Ausbildung zu einem anerkannten Lehrberuf unter eine  Berufsausbildung iSd FLAG 1967 (zB VwGH 26.5.2011, 2011/16/0077).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_45`)


Laut Erkenntnis des Verwaltungsgerichtshofes vom 18.12.2018, Ra 2018/16/0203, stellt die  Ausbildungsphase/Grundausbildung eines (Grenz-)Polizisten keine Berufsausbildung im Sinne  des § 2 Abs. 1 lit b FLAG 1967 dar.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_46`)


Dieses Erkenntnis betrifft zwar den Zeitraum, in dem der Sohn des Revisionswerbers nach  Absolvierung der ersten Ausbildungsphase seinen Dienst als Grenzpolizist ausgeübt hat, jedoch  verneint der Verwaltungsgerichtshof in diesem Erkenntnis das Vorliegen einer  Berufsausbildung für die gesamte Grundausbildung oder Ausbildungsphase von öffentlich  Bediensteten und qualifiziert dies als Berufsausübung (vgl. Rz 16, 17).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_136`)


Der  Verwaltungsgerichtshof hat jedoch hierzu in seiner ständigen Rechtsprechung die wesentlichen  Kriterien entwickelt (vgl. etwa VwGH 18.11.2008, 2007/15/0050;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_211`)


Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_49`)


Aufgrund  der außerordentlichen Revision des Beschwerdeführers hob der Verwaltungsgerichtshof am  30.1.2020 das Erkenntnis vom 16.10.2019 wegen Rechtswidrigkeit infolge der Verletzung von  Verfahrensvorschriften auf, da in der Abstandnahme von der Einvernahme der zehn  angebotenen Zeugen eine Vorwegnahme der Ergebnisse der Beweisaufnahmen und eine  antizipierende Beurteilung des Beweiswertes der Aussagen an sich lag.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_190`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes treten bei der  diesbezüglichen Beurteilung wirtschaftliche Gesichtspunkte gegenüber persönlichen Aspekten  in den Hintergrund.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_193`)


Die  Rechtsprechung des Verwaltungsgerichtshofes, aber auch des Unabhängigen Finanzsenates  und des Bundesfinanzgerichtes orientiert sich dafür am Halterbegriff des Eisenbahn- und  Kraftfahrzeughaftpflichtgesetzes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_207`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes trifft in Fällen, in denen ein Sachverhalt mit  Auslandsbezug entscheidungsrelevant ist, die Partei eine erhöhte Mitwirkungspflicht (siehe  Ritz, BAO, 6.A., Rz 10 ff zu § 115 mit Judikaturnachweisen).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_229`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_230`)


Die rechtliche Würdigung folgt  der zitierten Judikatur des Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_118`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_7`)


Unterlagen und auf das Erkenntnis des Verwaltungsgerichtshofes vom 18.12.2018,  GZ Ra 2018/16/0203, hingewiesen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_15`)


Nach der  ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Ziel einer Berufsausbildung im  Sinn des FLAG 1967, die fachliche Qualifikation für die Ausübung des angestrebten Berufes zu  erlangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_33`)


Nach der  ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Ziel einer Berufsausbildung im  Sinn des FLAG 1967, die fachliche Qualifikation für die Ausübung des angestrebten Berufes zu  erlangen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_37`)


Laut Verwaltungsgerichtshof  3 von 17 Seite 4 von 17

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_39`)


Laut Erkenntnis des Verwaltungsgerichtshofes vom 18.12.2018, Ra 2018/16/0203, stellt die  Ausbildungsphase/Grundausbildung eines (Grenz-)Polizisten keine Berufsausbildung im Sinne  des § 2 Abs. 1 lit b FLAG 1967 dar.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_40`)


Dieses Erkenntnis betrifft zwar den Zeitraum, in dem der Sohn des Revisionswerbers nach  Absolvierung der ersten Ausbildungsphase seinen Dienst als Grenzpolizist ausgeübt hat, jedoch  verneint der Verwaltungsgerichtshof in diesem Erkenntnis das Vorliegen einer  Berufsausbildung für die gesamte Grundausbildung oder Ausbildungsphase von öffentlich  Bediensteten und qualifiziert dies als Berufsausübung (vgl. Rz 16, 17).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_48`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes fallen unter den Begriff der  "Berufsausbildung" alle Arten schulischer oder kursmäßiger Ausbildung, in deren Rahmen noch  nicht berufstätigen Personen ohne Bezugnahme auf die spezifischen Tätigkeiten an einem  konkreten Arbeitsplatz für das künftige Berufsleben erforderliches Wissen vermittelt wird  (VwGH 1.3.2007, 2006/15/0178, 20.2.2008, 2016/15/0076, 18.11.2008, 2007/15/0050).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_53`)


Der Verwaltungsgerichtshof hat sehr deutlich den Unterschied der im Bereich des  Bundesministeriums für Inneres vorhandenen exekutivdienstlichen Ausbildungen  aufgearbeitet:   Zur Verdeutlichung werden die Unterschiede der Ausbildungslaufbahn der „Grenzpolizisten“  jenen der „Polizisten“ (Exekutivdienst) überblicksmäßig gegenübergestellt:   Fremden- u. grenzpolizeilicher Exekutivdienst   (Erlass des BMI-SI1400/1082-SIAK-ZGA/2015  vom 09.12.2015)   Grundausbildung für den Exekutivdienst   (Verordnung des Bundesministers für Inneres über  die Grundausbildungen für den Exekutivdienst -   Grundausbildungsverordnung - Exekutivdienst BMI,  BGBl. II Nr. 153/2017)   Basisausbildung: 6 Monate (Lehrplan,  Stundentafel - Unterrichtseinheiten 880,  mündliche Prüfung, Zeugnis), Entgelt: 50,29%  des Referenzbetrages (§ 3 Abs. 4 GG)   Basisausbildung: 12 Monate (Lehrplan,  Stundentafel)   Entgelt: 50,29% des Referenzbetrages (§ 3  Abs. 4 GG) während der gesamten Ausbildung   Kursunterbrechung - Verwendung im  fremden- und grenzpolizeilichen Bereich   sowie Unterstützung im  sicherheitspolizeilichen Bereich   Entgelt: SONDERBESTIMMUNGEN -  Normalentgelt Exekutivdienstliche Zulagen  und Nebengebühren   Berufspraktikum I - 3 Monate   Kennenlernen des Dienstbetriebes ...

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `BMI` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_55`)


Dienstprüfung   Unterrichtseinheiten gesamt: 2046  Unterrichtseinheiten: gesamt 2612   Der Verwaltungsgerichtshof hat ferner festgehalten, dass es   unstrittig ist, dass die Basisausbildung der Grundausbildung für die exekutivdienstliche  Verwendung im fremden- und grenzpolizeilichen Bereich (Dauer 6 Monate) und die  Ergänzungsausbildung zur Grundausbildung für den Exekutivdienst (9 Monate) als  Berufsausbildung im Sinne des Familienlastenausgleichsgesetzes anzusehen sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_58`)


Dass im Zuge einer Berufsausbildung praktische und nicht nur theoretische Kenntnisse  vermittelt werden können und etwa im Praktikum zu vermittelnde praktische Grundkenntnisse  unter die Berufsausbildung fallen, hat der Verwaltungsgerichtshof etwa im Erkenntnis vom  22. Dezember 2011, 2009/16/0315, ausgesprochen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_146`)


Der  Verwaltungsgerichtshof hat jedoch hierzu in seiner ständigen Rechtsprechung die wesentlichen  Kriterien entwickelt (vgl. etwa VwGH 18.11.2008, 2007/15/0050;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_221`)


Zu Spruchpunkt II. (Revision)  Gemäß Art. 133 Abs. 4 B-VG ist die Revision gegen ein Erkenntnis des Verwaltungsgerichtes  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_90`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_3`)


Der Einheitswert wird im  Sinne der Berechnung der belangten Behörde im Rahmen der Beschwerdevorentscheidung mit  22.900,- Euro festgestellt.  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_64`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_70`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_3`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art 133 Abs 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_62`)


Zur Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_114`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_20`)


In Analogie zur Judikatur des  Verwaltungsgerichtshofes zum Verschulden von Kanzleiangestellten berufsmäßiger  Parteienvertreter (siehe Ritz, BAO, 6.A., Rz 17 zu § 308 mwN) wäre es den zur Vertretung des  Antragstellers berufenen Personen angesichts der behaupteten Delegierung ihrer Aufgaben an  den Kassier oblegen, dessen Tätigkeit zu überwachen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_26`)


Zur Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_5`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_61`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_62`)


Da im gegenständlichen Erkenntnis die Feststellung des der Entscheidung zugrunde zu  legenden Sachverhaltes im Vordergrund stand und die rechtliche Beurteilung des Vorliegens  einer Schätzungsbefugnis nach § 184 BAO im Sinne der herrschenden Judikatur des  Verwaltungsgerichtshofes getroffen wurde, war die Unzulässigkeit der ordentlichen Revision  auszusprechen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_34`)


Aufgrund der dagegen erhobenen Amtsrevision des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel habe der Verwaltungsgerichtshof  mit Beschluss vom 25.11.2015, A 2015/0011 -1 (R o 2015/16/0035 -4) an den  Verfassungsgerichtshof den Antrag gemäß Art. 140 Abs. 1 B-VG gestellt, § 58 Abs. 3 GSpG, BGBl.  620/1989, in der Fassung des Abgabenä nderungsgesetzes 2011, BGBl.  I Nr 76 zur Gänze, in  eventu in § 58 Abs. 3 GSpG in der genannten Fassung den Klammerbegriff „(auch)“ als  verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamtes für Gebühren` (organisation)
- `Verfassungsgerichtshof` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_36`)


In seinem Besch luss gehe der Verwaltungsgerichtshof grundsätzlich von  einem systematischen Verhältnis zwischen den §§  57 und  58 GSpG aus.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_37`)


Der  Verwaltungsgerichtshof hatte aber verfassungsrechtliche Bedenken, weil §  58 Abs. 3 GSpG den  Inlandsbezug für die Besteuerung nich t an eine Teilnahme am Glücksspiel vom Inland aus  anbindet.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_42`)


In einer weiteren Beschwerdesache betreffend §  58 Abs.  3 GSpG idF BGBl. I  2011/76 mit  „grenzüberschreitendem Sachverhalt“ habe das Bundesfinanzgericht unter Bezugnahme auf den  Beschluss des Verwaltungsgerichtshofes ebenfalls den Antrag gemäß Art. 140  Abs. 1 B -VG  gestellt, § 58 Abs. 3 GSpG, BGBl. Nr.620/1989, in der Fassung des Abgabenänderungsgesetzes  2011, BGBl. I Nr 76 zur Gänze, in eventu in §  58 Abs. 3 leg. cit.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_62`)


RdW 2014, 309-311, auf  den auch der Beschluss des Verwaltungsgerichtshofes 25.11.2015, A 2015/0011 -1 (Ro  2015/16/0035-4) verweise).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_66`)


Der Verwaltungsgerichtshof  habe in seinem Beschluss vom 25.11.2015, A  2015/0011 (Ro 2015/16/0035 -4) den Antrag  gestellt, § 58 Abs. 3 GSpG in der Fassung des Abgabenänderungsgesetzes 2011, BGBl. Nr. 76 –  AbgÄG 2011 zur Gänze aufzuheben.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_74`)


Der Verfassungsgerichtshof wies die Anträge des Verwaltungsgerichtshofes und  des Bundesfinanzgerichtes auf Aufhebung des § 58 Abs. 3 GSpG bzw. der Wort- und Zeichenfolge  „(auch)“ in § 58 Abs. 3 GSpG ab (VfGH 12.12.2016 G650/2015 ua.).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_91`)


Im Folgeerkenntnis VwGH 24.1.2017, Ro 2015/16/0035  gab der Verwaltungsgerichtshof der  Amtsrevision des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel statt, entschied in  7 von 11 Seite 8 von 11

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamtes für Gebühren` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_137`)


Der Verfassungsgerichtshof wies die genannten  Anträge des Verwaltungsgerichtshofes VwGH 25.11.2015, A  2015/0011 (Ro 2015/16/0035 -4)  und des Bundesfinanzgerichtes BFG 26.1.2016, RN/7100001/2015 auf Aufhebung des §  58  Abs. 3 GSpG „neue Version“ bzw. der Wort - und Zeichenfolge „(auch)“ in §  58 Abs. 3 GSpG ab  (VfGH 12.12.2016 G650/2015 ua.).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)
- `Bundesfinanzgerichtes` (organisation)
- `BFG` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_150`)


Unzulässigkeit der Revision  Gegen ein  Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts hofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechu ng des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_151`)


Das Bundesfinanzgericht ist der Rechtsprechung des Verfassungs - und  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_3`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach  Art 133 Abs 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_56`)


Ein Wahlrecht auf Berücksichtigung der Fahrtkosten  durch den Ansatz der amtlichen Kilometergelder an Stelle der tatsächlichen Aufwendungen  besteht nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes nicht (VwGH  27.8.2008, 2008/15/0196;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

## `Courts - Verfassungsgerichtshof` 🏆

**F1:** 0.019 | **Precision:** 1.000 | **Recall:** 0.009  

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
| 1.000 | 0.009 | 0.019 | 118 | 118 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 118 | 0 | 12492 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_30`)


Gegen das abweisende Erkenntnis vom 25.6.2019 des Bundesfinanzgerichts erhob der  rechtsfreundlich vertretene Bf Beschwerde gem. Art 144 B-VG an den Verfassungsgerichtshof.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_31`)


Mit Entscheidung vom 25.2.2020 hob der Verfassungsgerichtshof das Erkenntnis des  Bundesfinanzgerichts vom 25.6.2019 auf (VfGH vom 25.2.2020, E 2892/2019).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_32`)


Begründend  führte der Verfassungsgerichtshof aus:  "1.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_33`)


Der Verfassungsgerichtshof hat mit Erkenntnis vom 4. Dezember 2019, G 159/2019 ua. den  Satz 'Der Abtrag ist vor Ablauf der für Wiederaufnahmsanträge nach § 304 maßgeblichen Frist  zu stellen.' in § 295 Abs. 4, BGBl. 194/1961, idF BGBl I 70/2013 als verfassungswidrig  aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_36`)


Dem in Art. 140 Abs. 7 B-VG genannten Anlassfall (im engeren Sinn), anlässlich dessen das  Gesetzesprüfungsverfahren tatsächlich eingeleitet worden ist, sind all jene Beschwerdefälle  gleichzuhalten, die zum Zeitpunkt der mündlichen Verhandlung im Gesetzesprüfungsverfahren  (bei Unterbleiben einer mündlichen Verhandlung zu Beginn der nichtöffentlichen Beratung)  beim Verfassungsgerichtshof bereits anhängig waren (VfSlg. 10.616/1985, 11.711/1988).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_37`)


Im  Fall einer Beschwerde gegen eine Entscheidung eines Verwaltungsgerichte3s, der ein auf  Antrag eingeleitetes Verwaltungsverfahren vorausgegangen ist, muss dieser  verfahrenseinleitende Antrag überdies vor Bekanntmachung des dem unter Pkt. 1 genannten  Erkenntnis zugrunde liegenden Prüfungsbeschlusses des Verfassungsgerichtshofes eingebracht  worden sein (VfSlg. 17.687/2005).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_39`)


Die vorliegende Beschwerde ist beim Verfassungsgerichtshof am 5. August 2019 eingelangt,  war also zu Beginn der nichtöffentlichen Beratung schon anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_40`)


Die Anträge gemäß § 295  Abs. 4 BAO wurden am 20. Dezember 2012 bzw. am 30. April 2013 gestellt, der dem unter Pkt.  1 genannten zugrunde liegende Prüfungsbeschluss des Verfassungsgerichtshofes wurde am 11.  Juli 2019 bekannt gemacht;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_41`)


die verfahrensleitenden Anträge wurden also vor Bekanntmachung  des Prüfungsbeschlusses des Verfassungsgerichtshofes eingebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_75`)


In Umsetzung des Erkenntnisses des Verfassungsgerichtshofes ist der letzte Satz des § 295 Abs.  4 BAO nicht anwendbar.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_42`)


Das Bundesfinanzgericht hat bereits wiederholt - in Anlehnung an die Rechtsprechung des  Verfassungsgerichtshofes - zum Ausdruck gebracht, dass es keine Zweifel an der  Verfassungsmäßigkeit des Bewertungsgesetzes hegt (vgl. BFG 10.01.2017, RV/4100647/2016;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_48`)


Der Verfassungsgerichtshof hat das System der Einheitsbewertung daher nicht in Frage  gestellt, sondern nur die "historischen Einheitswerte" als ungeeignete Bemessungsgrundlage  für die Abgabenbemessung angesehen (vgl. zB VfGH 02.03.2011, G 150/10).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_50`)


Mit Beschluss vom 20.11.2018, E 479/2017 hat der Verfassungsgerichtshof die Behandlung  einer Beschwerde (eingebracht gegen BFG 10.1.2017, RV/4100647/2016) abgelehnt, in der  hinsichtlich der pauschalen Hektarsätze ein Verordnungsprüfungsverfahren angeregt wurde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_31`)


Mit Beschluss BFG 21.4.2016, RN/7100001/2016 stellte das Bundesfinanzgericht einen  Normprüfungsantrag gemäß Art. 140 Abs.  1 iVm Abs. 4 B-VG betreffend Glücksspielabgabe für  Glücksspiele im Rahmen von Gewinnspielen (Preisausschreiben) gemäß § 58 Abs. 3 GSpG idF vor  dem AbgÄG 2011 zu den beim Verfassungsgerichtshof unter G  650/2015, G 20/2016 damals  anhängigen Normprüfungsantragsverfahren.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_34`)


Aufgrund der dagegen erhobenen Amtsrevision des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel habe der Verwaltungsgerichtshof  mit Beschluss vom 25.11.2015, A 2015/0011 -1 (R o 2015/16/0035 -4) an den  Verfassungsgerichtshof den Antrag gemäß Art. 140 Abs. 1 B-VG gestellt, § 58 Abs. 3 GSpG, BGBl.  620/1989, in der Fassung des Abgabenä nderungsgesetzes 2011, BGBl.  I Nr 76 zur Gänze, in  eventu in § 58 Abs. 3 GSpG in der genannten Fassung den Klammerbegriff „(auch)“ als  verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamtes für Gebühren` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_35`)


Dieser Antrag sei beim Verfassungsgerichtshof zur Zahl G  650/2015 anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_44`)


Dieser Antrag sei beim Verfassungsgerichtshof zur Zahl G 20/2016  anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_71`)


Die Bf. schloss sich in einer Äußerung an den Verfassungsgerichtshof im Wesentlichen den  Bedenken an und erachtete die durch das Finanzamt vorgenommene, nach ihrer Ansicht  exzessive Auslegung des § 58 Abs. 3 GSpG als dem Gleichheitssatz widersprechend an.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_72`)


Der Verfassungsgerichtshof wies den Normprüfungsantrag des BFG 26.4.2016 ,  RN/7100001/2016 hinsichtlich der Fassung des §  58 Abs. 3 GSpG, gültig vom 1.1.2011 bis  31.8.2011 (vor dem Abgabenänderungsgesetz 2011), zurück.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_74`)


Der Verfassungsgerichtshof wies die Anträge des Verwaltungsgerichtshofes und  des Bundesfinanzgerichtes auf Aufhebung des § 58 Abs. 3 GSpG bzw. der Wort- und Zeichenfolge  „(auch)“ in § 58 Abs. 3 GSpG ab (VfGH 12.12.2016 G650/2015 ua.).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_80`)


Erwägungen  3.1. Höchstgerichtliche Judikatur zum Normprüfungsantrag  Der Verfassungsgerichtshof wies mit Beschluss VfGH 24.11.2016, G 120/2016 den  Normprüfungsantrag des BFG 26.4.2016, RN/7100001/2016 hinsichtlich der Fassung des  § 58  Abs. 3 GSpG, gültig vom 1.1.2011 bis 31.8.2011 (vor dem Abgabenänderungsgesetz 2011),  zurück, weil das Bundesfinanzgericht diesem Gesetzesprüfungsantrag die Beschlüsse des VwGH  25.11.2015, A 2015/0011 (Ro 2015/16/0035-4) und des BFG  26.1.2016, RN/7100001/2015, die  zwar beim Verfassungsgerichtshof protokolliert waren, nicht beigelegt hatte und weil das  Bundesfinanzgericht nicht eigenständig und konkret dargelegt hatte, gegen welche  verfassungsrechtliche Norm §  58 Abs.  3 GSpG in der früheren Fassung verstoße bzw. aus  welchen Gründen der angefochtenen Gesetzesbestimmung (in ihrer konkreten Fassung) die  behauptete Verfassungswidrigkeit anzulasten sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_84`)


Nach Auffassung d es Verfassungsgerichtshofes ist im  Licht der geltend gemachten gleichheitsrechtlichen Bedenken nicht entscheidend, ob und  inwieweit sich der Begriff des Glücksspiels gemäß §58 Abs. 3 GSpG mit jenem in § 1 GSpG deckt;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_86`)


Eine solche Unsachlichkeit kann  der Verfassungsgerichtshof nicht finden: Preisausschreiben iSd § 58 Abs. 3 GSpG unterscheiden  sich zwar von herkömmlichen Glücksspielen darin, dass sie ohne vermögenswerte Leistung des  Teilnehmers erfolgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_126`)


Dieser Rechtsansicht traten Ehrke-Rabel/Sumper, Länderübergreifende Preisausschreiben und  Glücksspielabgabe, taxlex 2017, 341 unter Verweis auf die obgenannten Entscheidungen des  Verfassungsgerichtshofes VfGH 12.12.2016 G 650/2015 entgegen: Es ist systematisch  nachvollziehbar, dass der Verfassungsgerichtshof Preisausschreiben als Glücksspiele qualifiziert.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_136`)


4. Schlussfolgerung  Die ermäßigte Glücksspielabgabe gemäß §  58 Abs.  3 GSpG idF vor dem AbgÄG 2011 für  „Preisausschreiben“ für die Verlosung zweier von einer theaterähnlichen Organisation zur  Verfügung gestellter Tickets und die Verlosung des Ersatzes diverser Auslagen des täglichen  Lebens für ein Jahr im Monat Juni 2011 besteht zu Recht . Der Normprüfungsantrag BFG  21.4.2016, RN/7100001/2016 zu § 58 Abs. 3 GSpG „alte Version“, mit dem sich das BFG auf die  Normprüfungsanträge VwGH 25.11.2015, A  2015/0011-1 (Ro 2015/16/0035 -4) und BFG  26.1.2016, RN/7100001/2015 bezog, wurde vom Verfassungsgerichtshof zurückgewiesen  (Beschluss VfGH 24.11.2016, G 120/2016).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_137`)


Der Verfassungsgerichtshof wies die genannten  Anträge des Verwaltungsgerichtshofes VwGH 25.11.2015, A  2015/0011 (Ro 2015/16/0035 -4)  und des Bundesfinanzgerichtes BFG 26.1.2016, RN/7100001/2015 auf Aufhebung des §  58  Abs. 3 GSpG „neue Version“ bzw. der Wort - und Zeichenfolge „(auch)“ in §  58 Abs. 3 GSpG ab  (VfGH 12.12.2016 G650/2015 ua.).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Bundesfinanzgerichtes` (organisation)
- `BFG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_100`)


Die Familienbeihilfenbeträge werden  aufgrund einer Entscheidung des Verfassungsgerichtshofes in regelmäßigen Abständen  angehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_80`)


Auch  hätte der Verfassungsgerichtshof daran nichts auszusetzen gehabt (VfGH B 08.06.2010,  B 581/10).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_4`)


Begründet wurde dieser damit, dass dieser zu Unrecht eingefordert wurde, weil eine  Beschwerde beim Verfassungsgerichtshof nicht von einem Rechtsanwalt unterfertigt worden  wäre und daher kein Gebührenanspruch entstanden wäre.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_26`)


Angemerkt wurde seitens der zuständigen Richterin im Erkenntnis allerdings,  dass selbst bei fristgerechter Einbringung der Beschwerde eine Abweisung zu treffen gewesen  wäre, da die Verpflichtung zur Zahlung einer Eingabegebühr gem. § 17a VfGG unabhängig  davon besteht, ob diese Einbringung den formalen Voraussetzungen für Beschwerden an den  Verfassungsgerichtshof entspricht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_47`)


dass dies ausgeschlossen werden kann, weil diese Klärung bereits durch Erkenntnis des  Bundesfinanzgerichtes vom 5.5.2020, RV/7100080/2020 erfolgt ist, mit dem die diesbezügliche  Bescheidbeschwerde der Bf in Form von Zurückweisung erledigt wurde, allerdings explizit  angemerkt wurde, dass selbst bei fristgerechter Einbringung eine Abweisung erfolgt wäre, da  die Verpflichtung zur Zahlung einer Eingabegebühr gem. § 17a VfGG unabhängig davon  besteht, ob diese Einbringung den formalen Voraussetzungen für Beschwerden an den  Verfassungsgerichtshof entspricht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_31`)


Nach der Rechtsprechung des Verfassungsgerichtshofes erfordert und erlaubt die Wendung  "dass zu entscheidende Rechtsfragen besondere Schwierigkeiten rechtlicher Art aufweisen"  eine Prüfung, ob im konkreten Einzelfall für den Antragsteller besondere Schwierigkeiten  bestehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_60`)


Besondere, in der Person des Einschreiters  liegende Umstände, die eine Bewilligung der Verfahrenshilfe vor dem Hintergrund der zitierten  Rechtsprechung des Verfassungsgerichtshofes notwendig machen würden, wurden nicht  vorgebracht und sind nicht auch nicht hervorgekommen: Dass der Einschreiter wegen einer  schweren Hypertonie und einem Rückenleiden die Fahrertätigkeit demnächst wieder aufgeben  müsse, deutet nicht darauf hin, dass seine Fähigkeiten, sein Anliegen wirksam zu verteidigen,  eingeschränkt wären.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_5`)


Der Verfassungsgerichtshof lehnte die Behandlung der Beschwerde der Bf ab (VfGH  23.11.2012, B 1167/12).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_30`)


Die Norm unterliege umso strengeren Anforderungen der Bestimmtheit, je intensiver  der mit der Norm verbundene Eingriff in die Grundrechte der Normadressaten ausfällt.   Auch nach der Rechtsprechung des Verfassungsgerichtshofes widerspreche es dem  Rechtsstaatsprinzip, wenn man nur mit subtiler Sachkenntnis, außerordentlichen  methodischen Fähigkeiten und einer gewissen Lust zum Lösen von Denksportaufgaben  verstehen könne, welche Anordnungen in einem Gesetz getroffen werden (VfGH 29.6.1990, G  81/90).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_56`)


Darüber hinaus hatte sich auch der Verfassungsgerichtshof mit dem Ausschluss von  Dienstleistungsbetrieben von der Energieabgabenvergütung durch das Budgetbegleitgesetz  2011 zu befassen und erachtete die behauptete Verletzung des Gleichheitssatzes nicht als  gegeben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_57`)


Der Verfassungsgerichtshof merkte dazu explizit an, dass sich auch keine von der  Beschwerdeführerin nicht geltend gemachte Verletzung verfassungsgesetzlich gewährleisteter  Rechte ergeben habe (VfGH 4.10.2012, B 321/12).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_58`)


Dazu kommt noch, dass sich der Verfassungsgerichtshof bereits in der eigenen  Beschwerdesache der Bf gegen den Bescheid des UFS 31.8.2012, RV/2441-W/12, betreffend  Energieabgabenvergütung für 2011 geäußert hat.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_144`)


Rechtsmittelbelehrung und Hinweise  Beschwerdeführenden Parteien steht das Recht zu, innerhalb von sechs Wochen ab Zustellung  dieser Entscheidung eine Beschwerde an den Verfassungsgerichtshof, 1010 Wien, Freyung 8,  zu erheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_145`)


Die Beschwerde ist direkt beim Verfassungsgerichtshof einzubringen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_146`)


Die  Beschwerde an den Verfassungsgerichtshof muss - abgesehen von den gesetzlich bestimmten  Ausnahmen - durch eine bevollmächtigte Rechtsanwältin oder einen bevollmächtigten  Rechtsanwalt eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_153`)


Das Antragsformular samt  Vermögensbekenntnis kann beim Verfassungsgerichtshof elektronisch, postalisch oder  persönlich eingebracht werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_154`)


Das Formular für postalische oder persönliche Einbringung  liegt in der Geschäftsstelle des Verfassungsgerichtshofes auf;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_155`)


es kann auch von der Website  des Verfassungsgerichtshofes (www.vfgh.gv.at; im Bereich Kompetenzen und Verfahren /  Verfahrenshilfe) heruntergeladen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_157`)


Zur Vorgangsweise für die elektronische Einbringung und zu  weiteren Informationen wird auf die Website des Verfassungsgerichtshofes verwiesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_158`)


Gemäß § 82 Abs. 3b VfGG in Verbindung mit § 30 Z 4 VwGVG besteht die Möglichkeit, auf die  Beschwerde an den Verfassungsgerichtshof zu verzichten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_159`)


Der Verzicht auf die Beschwerde an  den Verfassungsgerichtshof ist bis zur Zustellung der Ausfertigung der Entscheidung dem  Bundesfinanzgericht, danach dem Verfassungsgerichtshof schriftlich bekanntzugeben oder zu  Protokoll zu erklären.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_160`)


Wurde der Verzicht auf die Beschwerde beim Verfassungsgerichtshof  nicht von einem berufsmäßigen Parteienvertreter oder im Beisein eines solchen abgegeben, so  kann er binnen drei Tagen schriftlich oder zur Niederschrift widerrufen werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_161`)


Der Verzicht  auf die Beschwerde beim Verfassungsgerichtshof hat zur Folge, dass das jeweilige Rechtsmittel  nicht mehr zulässig ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_164`)


Die für eine Beschwerde an den Verfassungsgerichtshof zu entrichtende Eingabengebühr  ergibt sich aus § 17a VfGG.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_89`)


Judikatur des Verfassungsgerichtshofes  Der VfGH entschied im Erkenntnis vom 29.09.1988, dass die Bestimmung des § 103 Abs. 2 KFG  verfassungskonform ist und weder Art. 90 Abs. 2 B-VG noch Art. 6 EMRK verletzt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_142`)


Verfassungsgerichtshofes  (vgl. noch einmal das Erkenntnis des LVwG Linz vom 24.11.2020, LVwG-603901/9/KHa).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_77`)


Verordnung BGBl. Nr. 624/1995 idF BGBl. II Nr. 449/2001 muss es sich demnach - ungeachtet  dessen, ob der Auszubildende dieses auch tatsächlich benutzen kann - um ein solches handeln,  welches während des Tages Verkehrsverbindungen mit einer Fahrtdauer von höchstens einer  Stunde sicherstellt (vgl. VwGH 20.12.2016, Ra 2014/15/0011, Rn 21 f; vgl. auch VwGH  08.07.2009, 2007/15/0306, unter Hinweis auf das Erkenntnis des Verfassungsgerichtshofes  vom 11.12.1986, B 437/86).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_53`)


Dieser ist hinzunehmen, weil pauschalierende Regelungen, die der  Gesetz- oder Verordnungsgeber insbesondere im Interesse der Verwaltungsökonomie trifft,  nach der Rechtsprechung des Verfassungsgerichtshofes selbst dann zulässig sind, wenn dabei  Härtefälle entstehen können, sofern diese nicht in unverhältnismäßiger Weise ins Gewicht  fallen (VfGH 08.03.2002, G 308/01;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_59`)


Für einen Antrag  auf Aufhebung des § 5 der Sachbezugswerteverordnung beim Verfassungsgerichtshof gemäß  Art. 135 Abs. 4 B-VG iVm Art. 89 B-VG liegt kein Grund vor.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_18`)


Der Verfassungsgerichtshof hat mit Erkenntnis vom 24.3.2021, Ra 2020/15/0029, das  angefochtene Erkenntnis wegen Rechtswidrigkeit seines Inhaltes aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_72`)


BGBL II 48/2018 vom 20.3.2018 lautet:  Der Verfassungsgerichtshof hat mit Erkenntnis vom 26. Februar 2018, V 45/2017-6, dem  Bundesminister für Finanzen zugestellt am 15. März 2018, zu Recht erkannt:  "Die Wortfolge ,ausgenommen jene nach § 1 Z 9 (Vertreter)' in § 4 Verordnung der  Durchschnittssätze für Werbungskosten, BGBl. II 382,2001, wird als gesetzwidrig aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_73`)


"   BGBL II 271/2018 vom 19.10.2018 lautet:  Der Verfassungsgerichtshof hat mit Erkenntnis vom 24. September 2018, V 60/2018-4, dem  Bundesminister für Finanzen zugestellt am 11. Oktober 2018, zu Recht erkannt:  "Die Wortfolge, ausgenommen jene nach § 1 Z 9 (Vertreter)' in § 4 Abs 1 Verordnung der  Durchschnittssätze für Werbungskosten, BGBl. II 382,2015, wird als gesetzwidrig aufgehoben."

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_97`)


Mit Erkenntnis vom 26. Februar 2018, V 45/2017, hat der Verfassungsgerichtshof die Vertreter  betreffende Wortfolge in § 4 der Verordnung in der Stammfassung BGBL II 382/2001  aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_99`)


Mit Erkenntnis vom 24. September 2018, V 60/2018, hat der Verfassungsgerichtshof nun auch  die Vertreter betreffende Wortfolge in § 4 Abs 1 der Verordnung (idF BGBL II 382/2015)  aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_101`)


Ist eine Verordnung wegen Gesetzwidrigkeit aufgehoben worden oder hat der  Verfassungsgerichtshof gemäß Art 139 Abs. 4 B-VG ausgesprochen, dass eine Verordnung  gesetzwidrig war, so sind alle Gerichte und Verwaltungsbehörden an den Spruch des  Verfassungsgerichtshofes gebunden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_102`)


Auf die vor der Aufhebung verwirklichten Tatbestände  mit Ausnahme des Anlassfalles ist jedoch die Verordnung weiterhin anzuwenden, sofern der  Verfassungsgerichtshof nicht in seinem aufhebenden Erkenntnis anderes ausspricht (Art 139  Abs. 6 B-VG).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_90`)


29.4.2010, 2007/15/0227) und Verfassungsgerichtshofes (VfGH 30.9.1997,  B2/96).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_249`)


Ein Anwendungsfall des § 29 Abs. 5 VwGVG (Verwaltungsgerichtsverfahrensgesetz) mit dem  System der verkürzten Ausfertigungen in Verbindung mit Verzicht auf Beschwerdeerhebung an  Verwaltungsgerichtshof oder Verfassungsgerichtshof, wie z.B. im Anwendungsbereich von  Verwaltungsstrafsachen des Magistrats, liegt nicht vor.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)
- `Magistrats` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_9`)


Gegen diesen Bescheid wurde mit Schreiben vom 18. Jänner 2021 fristgerecht Beschwerde  erhoben und unter Bezugnahme auf das damals beim Verfassungsgerichtshof unter der  Geschäftszahl E 1720/2020 anhängige Beschwerdeverfahren und unter Verweis auf Laudacher  und Casperi in ÖStZ 4/2020 ausschließlich verfassungsrechtliche Bedenken vorgebracht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_22`)


Auch der Verfassungsgerichtshof ging zuletzt im Erkenntnis vom 14.6.2021, E1743/2020 ua,  davon aus, dass durch das vom Beschwerdeführer ins Treffen geführte EuGH-Urteil vom  21.7.2016, Rs C- 493/14, Dilly's Wellnesshotel GmbH, lediglich zum Ausdruck gebracht wird,  dass die in einem weiten Sinn verstandene Genehmigung durch die Kommission in Form der  Veröffentlichung der Mitteilung im Amtsblatt der EU nicht den Vorgaben des Unionsrechts  entsprochen hat, und das Gruppenfreistellungsverfahren nach dem Zweck der Regelung des §  4 Abs. 7 ENAVG einer Genehmigung durch die Kommission gleichzuhalten ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Dilly's Wellnesshotel GmbH` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_23`)


Der Verfassungsgerichtshof folgert daraus, dass mit der Durchführung dieses Verfahrens die  Bedingung für die Anwendbarkeit der Beihilferegelung eingetreten ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_26`)


Hinsichtlich des von der steuerlichen Vertretung ins Treffen geführte Verfahren vor dem VfGH-  zur Zahl E 1720/2020 wird ergänzend angemerkt, dass der Verfassungsgerichtshof die  Behandlung der Beschwerde mit Beschluss vom 23.6.2021 abgelehnt hat.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_59`)


Information für die Parteien  (Belehrung gemäß § 280 Abs. 4 BAO)  Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_11`)


Aufgrund einer Empfehlung der  Finanzprokuratur wäre davon auszugehen, dass bei Einbringung einer Klage (Regressforderung)  gegen die Bediensteten, welche nach Rechtsprechung des Verfassungsgerichtshofes  (GZ A7/96-B 2844/95 vom 02.10.1996) vorgegeben sei, von einer dreijährigen Verjährungszeit  ab Zahlung des Dienstgebers (06.12.2018) auszugehen wäre und nicht von einer allgemeinen  (30-jährigen) Verjährungsfrist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/139070.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139070.1_3`)


II)  Gegen diesen Beschluss ist gemäß § 30a Abs 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_67`)


Information für die Parteien  (Belehrung gemäß § 280 Abs. 4 BAO)  Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_65`)


Der Verfassungsgerichtshof hat mit Erkenntnis vom 22.9.2016, E 2556/2015, die Entscheidung  des Bundesfinanzgerichtes vom 9.11.2015, RV/5100721/2013, wegen Verletzung des  verfassungsgesetzlich gewährleisteten Rechts auf Gleichheit aller Staatsbürger vor dem Gesetz  aufgehoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_67`)


Der Verfassungsgerichtshof hat im Wesentlichen dazu in oben zitiertem Erkenntnis ausgeführt:  „Gemäß § 5 Abs. 3 VO über außergewöhnliche Belastungen sind auch Aufwendungen gemäß  § 4 (nicht regelmäßig anfallende Aufwendungen für Hilfsmittel und Kosten der  Heilbehandlung) sowie das Entgelt für die Unterrichtserteilung in einer Sonder- oder  Pflegeschule oder für die Tätigkeit in einer Behindertenwerkstätte im nachgewiesenen Ausmaß  zu berücksichtigen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_71`)


Diese Rechtsansicht des  Verwaltungsgerichtshofes gründet auf der Rechtsprechung des Verfassungsgerichtshofes,  wonach Aufwendungen, bei denen die in § 34 Abs. 6 EStG 1988 vorgesehene Anrechnung von  Pflegegeld besonders widersinnig und daher unsachlich wäre, erst durch die gesetzeskonforme  7 von 9 Seite 8 von 9

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_79`)


Der Verfassungsgerichtshof zählt in seinem Erkenntnis vom 24.11.2011,  2011/16/0088, Fahrtkosten, die der Erzielung eines positiven therapeutischen Effektes dienen,  in gesetzeskonformer Interpretation zu den Kosten einer Heilbehandlung gemäß § 4 der VO  über außergewöhnliche Belastungen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_99`)


Gegen die Einschränkung der Beweisführung des Grades der Behinderung oder  der voraussichtlichen dauerhaften Unfähigkeit, sich selbst den Erwerb zu verschaffen, hat der  Verfassungsgerichtshof im Erkenntnis vom 10.12.2007, B 700/07, keine verfassungsrechtlichen  Bedenken gesehen (vgl. VwGH 22.12.2011, 2009/16/0307).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_93`)


Der Verfassungsgerichtshof hat § 180 Abs. 2 letzter Satz ABGB im Einklang mit Art. 8 EMRK so  ausgelegt, dass eine elterliche Vereinbarung einer zeitlich gleichteiligen Betreuung oder einer  entsprechenden gerichtlichen Festlegung in jenen Fällen, in denen dies aus der Sicht des  Gerichts dem Kindeswohl am besten entspricht, zulässig ist (VfGH 09.10.2015, G 152/2015).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_25`)


Letztlich gab er bekannt, dass er am 27.9.2023 gegen das  Erkenntnis vom 11.8.2023, RV/7102959/2022, eine Beschwerde beim Verfassungsgerichtshof  eingebracht habe.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/144218.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144218.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_131`)


Aus den dargelegten Gründen besteht daher für das Bundesfinanzgericht kein Anlass, einen  Aufhebungsantrag gemäß Art. 89 Abs. 2 B-VG an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_132`)


Aus den dargelegten Gründen besteht daher für das Bundesfinanzgericht kein Anlass, einen  Aufhebungsantrag gemäß Art. 89 Abs. 2 B-VG an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_49`)


Der Verfassungsgerichtshof hat mit Erkenntnis vom 17. Juni 2021, welches in BGBl. I 134/2021  am 13. Juli 2021 veröffentlich wurde, zu Recht erkannt:  4 von 7 Seite 5 von 7

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_133`)


Hinsichtlich 2004, d.h. gegen Spruchpunkt I. ist kein Rechtsmittel an Verfassungsgerichtshof  oder Verwaltungsgerichtshof erhoben worden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_553`)


Vor diesem Hintergrund regen wir an, das BFG möge  • an den Verfassungsgerichtshof einen Normprüfungsantrag dahingehend stellen, ob die  Telekommunikationsdienste-VO BGBl II 383/2003 wegen Verstoßes gegen Art 6.1.3 des  Melbourne Agreements der ITU, BGBl III 1998/14, als gesetzwidrig aufzuheben ist, und  • dem EuGH zur Vorabentscheidung die Frage vorlegen, ob es sich bei Art 6.1.3 des Melbourne  Agreements der ITU, wenn dieses durch einen Mitgliedstaat ratifiziert und in nationales Recht  übernommen wurde, um einen völkerrechtlichen Vertrag handelt, der entsprechend den  Ausführungen des Gerichtshofes in Rn. 46 des Urteils vom EuGH 15.4.2021, C-593/19,  SK Telecom, einer Besteuerung der hier verfahrensgegenständlichen Umsätze durch einen  Mitgliedstaat entgegensteht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `SK Telecom` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/145897.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145897.1_53`)


Zu den eingewendeten verfassungsrechtlichen Bedenken wird ausgeführt, dass nach Ansicht  des erkennenden Gerichtes keine Bedenken aus dem Grund der Verfassungswidrigkeit gegen  die Anwendung des § 205 BAO bestehen, sodass nach Art 135 Abs 4 B-VG iVm Art 89 Abs 2 B- VG kein Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen  ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/146141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146141.1_23`)


Bei Bedenken gegen ihre rechtmäßige Kundmachung hat  das Bundesfinanzgericht diese Normen vor dem Verfassungsgerichtshof anzufechten, selbst  gesetzwidrig kundgemachte Verordnungen sind aber bis zur Aufhebung durch dieses  Höchstgericht für jedermann und damit auch die Gerichte verbindlich.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_61`)


Mit Schriftsatz vom 21.2.2024 erhob die Beschwerdeführerin gegen dieses Erkenntnis  Beschwerde an den Verfassungsgerichtshof (E 629/2024), da durch die verfassungswidrige  Auslegung des § 96 Abs. 2 BAO durch das Bundesfinanzgericht das Sachlichkeitsgebot, der  Schutz des Eigentums bei Festsetzung einer Abgabe, das Recht auf den gesetzlichen Richter  und das Rechtsstaatsgebot verletzt worden seien.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_63`)


Je nach  Ausgang des Verfahrens beim Verfassungsgerichtshof ist auch eine Befassung des  Verwaltungsgerichtshofes zu erwarten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_102`)


Zum Einwand der rechtlich nicht existent gewordenen Bescheide   Mit dieser Rechtsfrage hat sich das Bundesfinanzgericht bereits im Parallelverfahren (BFG  8.1.2024, RV/4100285/2021) ausführlich auseinandergesetzt und wurde gegen die  dahingehende abweisende Entscheidung Beschwerde an den Verfassungsgerichtshof  (E 629/2024) erhoben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_195`)


Zur Frage der Zulässigkeit der Vorsteuerberichtigung nach § 12 Abs. 10 UStG  1994  Mit dieser Rechtsfrage hat sich das Bundesfinanzgericht bereits im Parallelverfahren (BFG  8.1.2024, RV/4100285/2021) ausführlich auseinandergesetzt und hat die Beschwerdeführerin -  nach Beendigung des Verfahrens vor dem Verfassungsgerichtshof - gegen diese Entscheidung  eine Revision an den Verwaltungsgerichtshof in Aussicht gestellt. Das Bundesfinanzgericht  sieht nach eingehender Prüfung keinen Anlass an der Rechtsansicht im Parallelverfahren zu  zweifeln, zumal - übereinstimmend mit den Parteien - weitestgehend von einem identen  Sachverhalt ausgegangen wird.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `Verwaltungsgerichtshof` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_315`)


Anregungen  Sollte das zuständige Verwaltungsgericht die verfassungsrechtlichen Bedenken der Bf. gegen  die präjudiziellen Bestimmungen teilen, möge es an den Verfassungsgerichtshof gem Art 135  Abs 4 iVm Art 89 Abs 2 B-VG und Art 140 Abs 1 B-VG einen Antrag auf Aufhebung der  präjudiziellen Bestimmungen des EKBSG idgF wegen Verfassungswidrigkeit richten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_421`)


Gemäß Art 89 Abs 2 B-VG hat ein ordentliches Gericht, wenn es gegen die Anwendung eines  Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat, den Antrag auf Aufhebung  dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_601`)


Resümee  Aus den dargelegten Gründen bestand kein Anlass, einen Aufhebungsantrag gemäß Art 89 Abs  2 B-VG betreffend das EKBSG an den Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_616`)


Verwaltungsgerichtes beim Verfassungsgerichtshof wegen Gesetzwidrigkeit von Verordnungen  oder wegen Verfassungswidrigkeit von Gesetzen gestellt werden soll oder bei Annahme einer  Verdrängung nationalen Rechts durch Unionsrecht.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_183`)


In Anbetracht der Belastungskonzeption der Abgabe und der damit einhergehenden  verwaltungsökonomischen Vereinfachungen hegt der Verfassungsgerichtshof auch mit Blick auf  die zeitliche Begrenztheit der Regelung keine gleichheitsrechtlichen Bedenken dagegen, dass  der Gesetzgeber eine für alle Produktionstechnologien einheitliche Obergrenze vorgesehen und  nicht nach den Kostenstrukturen der jeweiligen Technologien differenzierende Obergrenzen  eingeführt hat.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/147193.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147193.1_37`)


Gegen diese Verständigung ist eine Revision an den Verwaltungsgerichtshof oder eine  Beschwerde an den Verfassungsgerichtshof nicht zulässig (vgl VwGH 20.9.2023,  Ro 2023/13/0015).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/147193.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147193.1_38`)


Belehrung und Hinweise  Gegen verfahrensleitende Beschlüsse ist eine abgesonderte Revision an den  Verwaltungsgerichtshof oder Beschwerde an den Verfassungsgerichtshof nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/147420.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147420.1_52`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs 4 hat ein Verwaltungsgericht dann, wenn es gegen die  Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat, den  Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/147517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147517.1_47`)


Gemäß Art 140 Abs 1 Z 1 lit a B-VG erkennt der Verfassungsgerichtshof über die  Verfassungswidrigkeit von Gesetzten auf Antrag eines Gerichts.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Law Firm - Glatzhofer & Matschek` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

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
| 1.000 | 0.000 | 0.001 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 12605 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` | `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Esra Nowy` (person)
- `Jeremias Stuck` (person)
- `Finanzamt Vorarlberg` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` | `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Martin Yüksekkaya` (person)
- `Bonnleiten 21S, 4724 Aigen, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `68-939/1151` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Wendelin Kasprowitz, Oberwinden 31, 8820 Kulm am Zirbitz, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für Großbetriebe je  vom 13. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  2013-2015 (Steuernummer 01-056/7050 ) nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` | `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Wendelin Kasprowitz` (person)
- `Oberwinden 31, 8820 Kulm am Zirbitz, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `01-056/7050` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Brian Nieclaassen, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

| Predicted | Gold |
|---|---|
| `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` | `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Brian Nieclaassen` (person)
- `Eiblweg 116, 4893 Brandstatt, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Othmar Garbe, Bf. Adresse, Ort in Kärnten, vertreten durch Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee,  über die Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 14. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 – 2015 (Steuernummer 29-838/1383) zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH` | `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Othmar Garbe` (person)
- `Finanzamtes für  Großbetriebe` (organisation)
- `29-838/1383` (tax_number)

</details>

---

## `City Authority - Magistrat der Stadt Wien` 🏆

**F1:** 0.032 | **Precision:** 0.990 | **Recall:** 0.016  

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
| 0.990 | 0.016 | 0.032 | 206 | 204 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 204 | 2 | 12406 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_140`)


Mit Strafverfügung vom 5.2.2019 verhängte das Magistrat der Stadt Wien, Magistratsabteilung  67, gemäß § 4 Abs. 1 Parkometergesetz 2006, über den Bf. eine Geldstrafe von 60,00 Euro, im  Fall deren Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung  67` | `Magistrat der Stadt Wien, Magistratsabteilung  67` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_426`)


[...]  Die Bestätigung der Gesellschaft, in deren Werkstatt sich das Fahrzeug, für welches eine  Ausnahmebewilligung erteilt wurde, zu den Tatzeitpunkten befand, wurde dem Magistrat der  Stadt Wien, Magistratsabteilung 67, zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien, Magistratsabteilung 67` | `Magistrat der  Stadt Wien, Magistratsabteilung 67` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_15`)


Am 24.6.2019 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6 – BA 32, zur GZ. MA- Zahl1 wegen Nichtbezahlung der Strafe eine Vollstreckungsverfügung über die Geldstrafe in  Höhe von 60,00 Euro und setzte eine Mahngebühr von 5,00 Euro fest, die offene Forderung  betrug daher 65,00 Euro.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_22`)


Mit Bescheid vom 31.7.2019 wies der Magistrat der Stadt Wien, Magistratsabteilung 67, den  "Einspruch vom 05.07.2019 gegen die Strafverfügung vom 02.04.2019", GZ. MA-Zahl1 als  verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_84`)


Am 24.6.2019 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6 – BA 32 wegen  Nichtbezahlung der Strafe eine Vollstreckungsverfügung über die Geldstrafe von 60,00 Euro  und eine Mahngebühr in Höhe von 5,00 Euro, insgesamt 65,00 Euro.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_86`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, ging aufgrund des Vorbringens der Bf.  von einem Einspruch gegen die Strafverfügung aus und wies diesen mit Bescheid vom  31.7.2019 als verspätet zurück.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_88`)


Mit Bescheid vom 25.10.2019 verfügte der Magistrat der Stadt Wien wegen Nichtbezahlung  des Strafbetrages von 60,00 Euro und des Kostenbeitrages (Mahngebühr) in Höhe von 5,00  Euro die Zwangsvollstreckung hinsichtlich des offenen Betrages von 65,00 Euro.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_95`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, betrachtete diese E-Mail der Bf. als  Beschwerde gegen die Vollstreckungsverfügung vom 25.10.2019 und wies sie mit  Beschwerdevorentscheidung vom 21.11.2019 ab.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt somit  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31. Juli 2020 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 2. Juni 2020 in der  gebührenpflichtigen Kurzparkzone in 1030 Wien, Grailichgasse 3, ohne einem für den  Beanstandungszeitpunkt 17:47 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_14`)


Mit Straferkenntnis vom 9. September 2020 erkannte der Magistrat der Stadt Wien, MA 67,  den Bf. wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig und  verhängte wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  iHv € 60,00 und für den Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_17`)


Diese Zeitangabe sei deshalb  glaubwürdig, weil den Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die  Erfüllung der übertragenen Aufgaben elektronische Überwachungsgeräte (sog. PDA's) zur  Verfügung stünden, welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen  Server beziehen und vorgeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_5`)


Der mit Einschreiben am 26. August 2020 eingebrachte Einspruch gegen diese Strafverfügung  wurde vom Magistrat der Stadt Wien, Magistratsabteilung 67, gemäß § 49 Abs. 1 VStG als  verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_5`)


Mit Strafverfügung vom 2. Dezember 2019, Zahl, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, dem Bf. an, er habe das näher bezeichnete Fahrzeug am 3. Oktober  2019 in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Linke Wienzeile 44 ggü Parkplatz  Reihe 1, ohne einem für den Beanstandungszeitpunkt 21:36 Uhr gültigen Parkschein abgestellt  und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_96`)


Aus dem Verwaltungsakt geht hervor, dass der Magistrat der Stadt Wien, MA 67, die  Versendung der Strafverfügung vom 2. Dezember 2019, Zahl, zunächst gemäß § 26 Abs. 1  Zustellgesetz (Zustellung ohne Zustellnachweis) an die Adresse Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich  und am 3. März  2020 die Versendung mit Rückscheinbrief veranlasst hat.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro),  insgesamt 82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an  den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) forderte die Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa.Dankwardt Wind AG  mit Schreiben vom 3. September 2019 gemäß § 2 Wiener Parkometergesetz 2006) auf,  der Behörde binnen zwei Wochen ab Zustellung des Schreibens Auskunft darüber zu erteilen,  wem das näher bezeichnete Fahrzeug am 5. Juli 2019 um 17:47 Uhr überlassen war, sodass es  in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Altgasse 25a, stand.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Fa.Dankwardt Wind AG` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_176`)


Hier erweist sich das  Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem Magistrat der Stadt  Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den (anderen) Verwaltungs- gerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele ausführlich BFG  13.05.2014, RV/7500356/2014 sowie Wanke/Unger, BFGG § 25 BFGG Anm. 6).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_6`)


Der Beschwerdeführer hat daher nur mehr  € 12,00 und den Kostenbeitrag der belangten Behörde von € 10,00 (§ 64 VStG), insgesamt  somit € 22,00, binnen einer Frist von zwei Wochen nach Zustellung dieses Erkenntnisses an den  Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_7`)


Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_12`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.) mit  Strafverfügung vom 2. Februar 2021 an, er habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 4. Dezember 2020 in der gebührenpflichtigen Kurz- parkzone in 1010 Wien, Am Hof 13 ggü, ohne einen für den Beanstandungszeitpunkt 17:54 Uhr  gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_15`)


Mit Straferkenntnis vom 9. März 2021 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig erkannt und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_99`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_11`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_280`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  21 von 22 Seite 22 von 22

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien, Magistratsabteilung 6` | `Magistrats der Stadt Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Aron Pommeränke` (person)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_26`)


Der Magistrat der Stadt Wien legte die Beschwerde vom 07. April 2021 samt  Verwaltungsstrafakt dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens:  14. April 2021).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_51`)


Informativ wird mitgeteilt, dass die Einzahlung der verhängten Geldstrafe sowie die Kosten des  Verfahrens von der belangten Behörde auf folgendes Bankkonto des Magistrats der Stadt Wien  bei der UniCredit Bank Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 – Strafen;

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_4`)


Entscheidungsgründe  Mit dem angefochtenen Straferkenntnis vom 21. Dezember 2020, Zahl MA67/Zahl/2020, hat  der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) angelastet, er habe als Zulassungsbesitzer des Fahrzeuges mit dem  behördlichen Kennzeichen 123 (A) dem ordnungsgemäß zugestellten Verlangen der Behörde  vom 6. Juli 2020 innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das  mehrspurige Kraftfahrzeuge mit dem näher genannten behördlichen Kennzeichen zu einem  näher bezeichneten Zeitpunkt überlassen gehabt habe, sodass es in einer näher bezeichneten  gebührenpflichtigen Kurzparkzone abgestellt war, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_6`)


Entscheidungsgründe  Der Beschwerdeführer (Bf.) stellte beim Magistrat der Stadt Wien, Magistratsabteilung 6, am  13. Mai 2021 einen Antrag, ihm zur Abstattung der gegen ihn wegen 34  Verwaltungsübertretungen nach dem Wiener Parkometergesetz 2006 rechtskräftig verhängten  Geldstrafen in Höhe von insgesamt € 2.233,95 Ratenzahlungen zu bewilligen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_4`)


Die Geldstrafe (€ 60,00) ist gemeinsam mit dem Beitrag zu den Kosten der belangten Behörde  (€ 10,00) und des Beschwerdeverfahrens (€ 12,00), insgesamt somit € 82,00, an den Magistrat  der Stadt Wien binnen einer Frist von zwei Wochen ab Zustellung dieses Straferkenntnisses zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (in  Folge kurz Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2021 an, sie habe das  Fahrzeug am 26. Mai 2021 in der gebührenpflichtigen Kurzparkzone in 1180 Wien, Ranftlgasse  21 ggü, ohne einen für den Beanstandungszeitpunkt 18:57 Uhr gültigen Parkschein abgestellt,  da die Parkzeit überschritten gewesen sei.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_19`)


Mit Straferkenntnis vom 13. Oktober 2021 wurde die Bf. vom Magistrat der Stadt Wien, MA  67, für schuldig befunden, das in Rede stehende Fahrzeug am 26. Mai 2021 in der gebühren- pflichtigen Kurzparkzone in 1180 Wien, Ranftlgasse 21 ggü, ohne einen ordnungsgemäß  2 von 10 Seite 3 von 10

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_103`)


Informativ wird mitgeteilt, dass die Einzahlung der Geldstrafe (€ 60,00) samt Kosten des  verwaltungsbehördlichen Verfahrens (€ 10,00) und des Beschwerdeverfahrens (€ 12,00) von  gesamt € 82,00 auf folgendes Bankkonto des Magistrats der Stadt Wien bei der UniCredit Bank  Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 - Verkehrsstrafen  IBAN: AT***, BIC: ***  Bitte die Geschäftszahl des Straferkenntnisses des Magistrats angeben: Zahl  Gemäß § 52 Abs. 6 VwGVG sind die §§ 14 und 54b Abs. 1 und 1a VStG sinngemäß anzuwenden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank  Austria AG` (organisation)
- `Magistrats` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_109`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Pjotr Astore` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  somit 82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_10`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte den Beschwerdeführer (Bf.) mit  Schreiben (Lenkererhebung) vom 2. August 2021, Zahl MA67/Zahl2/2021 als  Zulassungsbesitzer des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen 123  (A) gemäß § 2 Wiener Parkometergesetz 2006 auf, der Behörde binnen zwei Wochen ab  Zustellung des Schreibens Auskunft darüber zu erteilen, wem er das Fahrzeug am 14. Mai 2021  um 10:55 Uhr überlassen gehabt habe, sodass dieses in 1050 Wien, Reinprechtsdorfer Straße  1c gegenüber ONr. 12, gestanden ist.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_33`)


Mit Straferkenntnis vom 18. November 2021, Zahl MA67/Zahl1/2021, wurde der Bf. vom  Magistrat der Stadt Wien, MA 67, wegen der bereits angeführten Verwaltungsübertretung für  schuldig befunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_111`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_8`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Bf.  I. mit Strafverfügung vom 3. Jänner 2022, Z1, an, er habe das Fahrzeug am  8. November 2021 in der gebührenpflichtigen Kurzparkzone in 1030 Wien,  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_17`)


Der Magistrat der Stadt Wien erließ am 31. Jänner 2022 zwei getrennte Straferkenntnisse und  befand den Bf. wegen der bereits näher angeführten Verwaltungsübertretungen für schuldig  und verhängte wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerab- gabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von je € 48,00  und für den Fall der Uneinbringlich je 11 Stunden Ersatzfreiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_4`)


Am 4. Juni 2021 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, eine  Vollstreckungsverfügung, Zahl: MA67/216700111216/2021, da die mit der Strafverfügung vom  11. März 2021, Zahl: MA67/216700111216/2021, verhängte rechtskräftige Strafe nicht bezahlt  worden sei.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_10`)


Am 23. Juni 2021 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, eine  Vollstreckungsverfügung, Zahl: MA67/216700103138/2021, da die mit der Strafverfügung vom  2. April 2021, Zahl: MA67/216700103138/2021, verhängte rechtskräftige Strafe nicht bezahlt  worden sei.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_68`)


Da die Eingabe der Beschwerdeführerin aber nicht als Beschwerde im Sinne des  Art. 130 Abs. 1 B-VG gegen die Vollstreckungsverfügungen zu qualifizieren ist, besteht keine  Zuständigkeit des Bundesfinanzgerichtes, über das von der Verwaltungsbehörde (hier:  Magistrat der Stadt Wien) vorgelegte Anbringen zu entscheiden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_7`)


Entscheidungsgründe  I) Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  1 von 9 Seite 2 von 9

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_48`)


Über die Beschwerde wurde erwogen:  Feststellungen:  Der Magistrat der Stadt Wien, MA 67, veranlasste die Versendung der Lenkererhebung  (Schreiben vom 13. Dezember 2021) an den aufrechten Hauptwohnsitz des Bf. in 1130 Wien,  Gasse.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_95`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_5`)


Der mit E-Mail am 18. Februar 2022 eingebrachte Einspruch gegen diese Strafverfügung wurde  vom Magistrat der Stadt Wien gemäß § 49 Abs. 1 des Verwaltungsstrafgesetzes (VStG) als  verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Melinda Brotke` (person)
- `Jägerloch 26, 8443 Praratheregg, Österreich` (address)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_4`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_145`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Waiser` (person)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_9`)


Der Magistrat der Stadt Wien (MA 67) betrachtete den Inhalt dieser E-Mail vom 25.5.2022 als  Beschwerde der Beschuldigte gegen die Vollstreckungsverfügung vom 18.05.2022, und legte  die Beschwerde samt Verwaltungsakt mit Vorlagebericht vom 13. Juni 2022 dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_32`)


Gegen die Beschwerdevorentscheidung wurde am 26. Juni 2020 (eingelangt beim FA am 30.  Juni 2020) vom Magistrat der Stadt Wien, Wiener Kinder- und Jugendhilfe – Rechtsvertretung  Bezirk 22,  als gesetzlichen Vertreter des Minderjährigen ein Vorlageantrag eingebracht und   eingewendet, dass die entscheidende Behörde übersehe, dass sich der Bf. in einer  sozialpädagogischen Wohngemeinschaft der Sozialwerke Clara Fey befinde und die  Sozialwerke Clara Fey wesentlich auch durch Spenden finanziert werde (www.sozialwerke- clara-fey.at/spendenlhtml).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Heidemarie Winkler im  Beschwerdeverfahren des Siegfried Bentz, Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich, vom 13.02.2022 gegen den  Pfändungsgebührenbescheid des Magistrats der Stadt Wien Magistratssabteilung 6 Erhebungs-  und Vollstreckungsdienst, vom 31.01.2022, mit:  I. Nach Auffassung des Bundesfinanzgerichts ist in Bezug auf die Beschwerde vom 13.02.2022  gegen den Bescheid vom 31.01.2022 mit Beschwerdevorentscheidung abzusprechen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Siegfried Bentz` (person)
- `Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich` (address)
- `Bundesfinanzgerichts` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_3`)


II. Das Beschwerdeverfahren in Bezug auf die Beschwerde vom 13.02.2022 gegen den  Bescheid vom 31.01.2022 wird eingestellt.  Begründung  Bisheriger Verfahrensgang:  Die belangte Behörde (Magistrat der Stadt Wien, Rechnungs- und Abgabenwesen, Referat  Erhebungs- und Vollstreckungsdienst) forderte den Beschwerdeführer (in Folge kurz BF) mittels  6 Zahlungsaufforderungen (alle datiert mit 31.01.2022) zur Zahlung des aushaftenden  Rückstandes auf.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Zulassungsbesitzerin, ZL  GmbH, 1010 Wien, Gasse, des mehrspurigen Kraftfahrzeuges mit dem behördlichen  Kennzeichen Vienna mit Schreiben vom 8. April 2022 gemäß § 2 Wiener Parkometergesetz  2006 auf, der Behörde schriftlich binnen zwei Wochen nach Zustellung des Schreibens  Auskunft darüber zu erteilen, wem sie das Kraftfahrzeug am 9. Februar 2022 um 17:36 Uhr  überlassen habe, sodass dieses in 1020 Wien, Hedwiggasse 4, stand.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_24`)


Der Magistrat der Stadt Wien, MA 67, befand die Bf. mit Straferkenntnis vom 14. Juli 2022  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig und verhängte  wegen Verletzung der Rechtsvorschriften des § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz  2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine Ersatzfreiheits- strafe von 14 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_95`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats  der Stadt Wien` | `Magistrats  der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Jeremias Kierstan` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Peter Schabel` (person)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Gerstmayer, Wüsterstraße 92, 4972 Stelzham, Österreich, über die Beschwerde vom 13. Oktober 2014  gegen den Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser  vom 12. September 2014 betreffend Wasser- und Abwassergebühr, MA 31-130652/15, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Lee Gerstmayer` (person)
- `Wüsterstraße 92, 4972 Stelzham, Österreich` (address)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_3`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_9`)


Das Organ machte im Zuge der Anzeige folgenden Vermerk: „tse 290322 1715h Entfernte  Entwertung Tag: 14, 15, 24, 22, Stunde: 9, 13, 15, 20 erkannt an Restkreuze Stiftfarbe blau  Delikt-Text: Parknachweis wies Spuren von entfernten Entwertungen auf Parkschein(e):  268339VWZ“  Mit Strafverfügung vom 1. April 2022, MA67/Z1/2022 lastete der Magistrat der Stadt Wien, MA  67, zunächst N. die Verwaltungsübertretung an.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_17`)


Der Bf. teilte dem Magistrat der Stadt Wien, MA 67, mit Schreiben vom 19. Mai 2022  folgendes mit:  „1.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_22`)


Er wird dem Magistrat der Stadt  Wien nicht vorgelegt, wohl aber dem Verwaltungsgericht Wien im Zuge eines allfälligen Be- schwerdeverfahrens.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Missed by this rule (FN):**

- `Verwaltungsgericht Wien` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_30`)


Der Magistrat der Stadt Wien, MA 67, befand den Bf. mit Straferkenntnis vom 31. Mai 2022  wegen der bereits näher angeführten Verwaltungsübertretung für schuldig und verhängte  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Wiener Parkometerabgabeverordnung  iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe iHv € 140,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 1 Tag und 9 Stunden.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_135`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  9 von 11 Seite 10 von 11

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_4`)


III. Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_5`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (12,00 Euro) ist gemeinsam mit der  Geldstrafe (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro),  insgesamt 82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den  Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 10. März 2022, Zahl, hat der Magistrat der Stadt Wien,  Magistratsabteilung 67, als belangte Behörde dem Beschwerdeführer (Bf.) angelastet, er habe  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_75`)


Der Bf. wurde mit dem gegenständlichen Auskunftsverlangen - Schreiben des Magistrats der  Stadt Wien, Magistratsabteilung 67, vom 10. Jänner 2022 - als jene Person, der das ihr von der  Zulassungsbesitzerin zur Verfügung gestellte Kraftfahrzeug mit dem behördlichen Kennzeichen  123 (D) einem Dritten überlassen hat, aufgefordert Auskunft darüber zu erteilen, wem er das  genannte Kraftfahrzeug am 15. September 2021 um 19:20 Uhr überlassen gehabt habe, sodass  es zu diesem Zeitpunkt in 1020 Wien, Schiffamtsgasse 16 abgestellt gewesen sei.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien, Magistratsabteilung 67` | `Magistrats der  Stadt Wien, Magistratsabteilung 67` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_121`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 €) sind gemeinsam mit der Geldstrafe (60,00 €)  und dem Beitrag zu den Kosten der belangten Behörde (10,00 €), insgesamt 82,00 €, binnen  zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu ent- richten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, befand den Beschwerdeführer (Bf.) mit  Straferkenntnis vom 21. September 2022 für schuldig, das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna, Marke BMW, am 2. Mai 2022 in der gebührenpflichtigen  Kurzparkzone in 1100 Wien, Wirerstraße 2-4, ohne einen für den Beanstandungszeitpunkt  10:05 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe verkürzt zu  haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_86`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/139260.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139260.1_5`)


Begründung  1) MA67/Zahl1/2022  Der Magistrat der Stadt Wien, Magistratsabteilung 67, befand den Beschwerdeführer (Bf.) mit  Strafverkenntnis vom 5. Oktober 2022 für schuldig, das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 24. Mai 2022 in der gebührenpflichtigen Kurzpark-zone  in 1220 Wien, Pirquetgasse 5, ohne einen für die Beanstandungszeit 12:57 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/139260.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139260.1_6`)


2) MA67/Zahl2/2022  Mit Straferkenntnis vom 5. Oktober 2022 befand der Magistrat der Stadt Wien, Magistrats- abteilung 67, den Bf. für schuldig, dass er mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Vienna am 21. Juni 2022 in der gebührenpflichtigen Kurzparkzone in 1220 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrats` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/139260.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139260.1_43`)


Zum Ersuchen des Bf. um Strafminderung wird informationshalber mitgeteilt, dass für  Zahlungserleichterungen (zB Ratenzahlungen) der Magistrat der Stadt Wien, Magistrats- abteilung 6, zuständig ist.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrats` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 €) sind gemeinsam mit der Geldstrafe (60,00 €)  und dem Beitrag zu den Kosten der belangten Behörde (10,00 €), insgesamt 82,00 €, binnen  zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt Wien zu ent- richten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde be- stimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem in Deutschland wohnhaften  Beschwerdeführer (Bf.), unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (D)  (Fa. XY) eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2022 an, er habe das  Fahrzeug am 27. Mai 2022 in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Ausstellungstraße 33, ohne einen für den Beanstandungszeitpunkt 17:50 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Wien` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_50`)


Mit Straferkenntnis vom 12. Oktober 2022 wurde der Bf. vom Magistrat der Stadt Wien, MA  67, wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 verhängt und für den Fall  der Uneinbringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_27`)


Mit Straferkenntnis des Magistrats der Stadt Wien, MA 67, vom 20. Jänner 2021, wurde der Bf.  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz  2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine Ersatzfreiheits- strafe von 14 Stunden verhängt.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, MA 67`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_60`)


Über die Beschwerde wurde erwogen:  Das Bundesfinanzgericht legt seiner Entscheidung nachstehenden Sachverhalt zu Grunde:  Der Bf. wurde als Zulassungsbesitzer des mehrspurigen Kraftfahrzeuges mit dem behördlichen  Kennzeichen 123 (A) vom Magistrat der Stadt Wien MA 67, mit Schreiben vom 2. August 2021  zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer Frist von zwei  Wochen ab Zustellung des Schreibens aufgefordert.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Magistrat der Stadt Wien MA 67`(organisation)

</details>

---

## `Courts - Bundesfinanzgericht` 🏆

**F1:** 0.536 | **Precision:** 0.982 | **Recall:** 0.368  

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
| 0.982 | 0.368 | 0.536 | 4732 | 4646 | 86 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4646 | 86 | 7964 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag.Dr. Hedwig Bavenek-Weber` (person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_22`)


Am 28. Oktober 2014 brachte der Bf. beim Bundesfinanzgericht einen „Vorlageantrag betreffend Berufungsvorentscheidung vom 8.10.2014 (vom Finanzamt fälschlicherweise als Bescheid – Zurücknahme/Gegenstandsloserklärung bezeichnet)“ ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_26`)


Im Vorlagebericht beantragte das Finanzamt, dass das Bundesfinanzgericht in der Sache selbst abweislich entscheide: „   Der Beschwerdeführer verlangt eine sofortige Fortschreibung des Einheitswertes wegen der im Juni 2014 erfolgten Rodung eines Weingartens.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_37`)


Der vergleichbare Fall wurde zur Rechtslage vor dem 1.1.2014 mit Erkenntnis BFG 28.4.2015, RV/7101335/2010 entschieden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_43`)


Ziel dieser beiden Bestimmungen - des § 250 Abs. 1 BAO und des § 85 Abs. 2 BAO - ist, dass die Behörde bzw. das Bundesfinanzgericht in die Lage versetzt wird, eine Entscheidung über die Beschwerde treffen zu können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_63`)


Nach Auffassung des Bundesfinanzgerichtes haben daher die Voraussetzungen für die Erlassung eines  Mängelbehebungsauftrag gefehlt, sodass sich der Zurücknahmebescheid als rechtswidrig erweist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_65`)


Zulässigkeit einer Revision Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_67`)


Diese ist einheitlich und das Bundesfinanzgericht ist von dieser Rechtsprechung nicht abgewichen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_68`)


(siehe auch Erkenntnis BFG 28.4.2015, RV/7101335/2010).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_0`)


GZ. RV/5101724/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter Dr. Elias Derneden  in der Beschwerdesache über die Beschwerde vom 14.01.2019 gegen den Bescheid der belangten Behörde vom 04.01.2019 betreffend Familienbeihilfe für den Zeitraum ab März 2018 zu Recht: 1.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Elias Derneden` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_30`)


Die Zielstrebigkeit der Ausbildung ab März 2018 konnte nicht festgestellt werden .“ Mit Schreiben vom 27.5.2019, bei der belangten Behörde eingelangt am 11.6.2019, stellte die Beschwerdeführerin den Antrag, ihre Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_38`)


Am 29.11.2019 erfolgte die Vorlage der Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_39`)


Mit Schreiben vom 30.12.2019 nahm die Beschwerdeführerin bezugnehmend auf einen entsprechenden Vorhalt des Bundesfinanzgerichts unter anderem zu der Frage Stellung, wie hoch der wöchentliche Zeitaufwand der Tochter für die Vorbereitung auf die von ihr wahrgenommenen Prüfungstermine sowie für die Abfassung der sog vorwissenschaftlichen Arbeit im Zeitraum März 2018 bis Jänner 2019 gewesen sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_47`)


II. Das Bundesfinanzgericht hat erwogen: 1. Feststellungen Auf Basis des oben geschilderten Verwaltungsgeschehens und der aktenkundigen Unterlagen wird folgender entscheidungswesentlicher Sachverhalt festgestellt: Die 1998 geborene und im streitgegenständlichen Zeitraum somit bereits volljährige Tochter der Beschwerdeführerin wiederholte vom 12.9.2016 bis 28.4.2017 die 8. Klasse des Bundes-Oberstufenrealgymnasiums Jungroith.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Jungroith` (city)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_59`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen gemäß § 167 Abs 2 BAO als erwiesen annehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_74`)


Betreffend das quantitative Erfordernis kann in Übereinstimmung mit der in der Literatur vertretenen Ansicht ein dem Begriff der Berufsausbildung iSd § 2 Abs 1 lit b FLAG 1967 genügender Zeitaufwand generell nur dann vorliegen, wenn ein wöchentlicher Zeitaufwand für Kurse und Vorbereitungszeit von mindestens 30 Stunden anfällt (vgl Lenneis in Csazar/Lenneis/ Wanke      [   Hrsg   ]   , FLAG § 2 Rz 40; vgl zB auch BFG 12.11.2018, RV/7103779/2018 mwN).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_79`)


BFG 12.11.2018, RV/7103779/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_82`)


§ 2 Abs 1 lit b vierter und fünfter Satz FLAG 1967 ist nach seiner Stellung im Gesetz aber eindeutig nur dann anwendbar, wenn das Kind eine in § 3 Studienförderungsgesetz genannte Einrichtung besucht, nicht aber im gegenständlichen Fall des Besuchs eines Gymnasiums (vgl in diesem Zusammenhang zB auch BFG 8.1.2015, RV/7102968/2013).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_85`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B- VG die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung Seite 7 von 7 fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Alexander Hajicek` (person)
- `Mag. Helga Hochrieser` (person)
- `Mag. Michael Franz` (person)
- `Mag. Franz Josef Großin` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_168`)


Nach Ansicht des Bundesfinanzgericht war die Tatsache einer verlustbringenden Tätigkeit aufgrund der durchgehenden Verluste schon ab Beginn der Vermietungstätigkeit im Jahr 1994 gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_197`)


2. Auf Basis der zitierten ständigen Rechtsprechung des VwGH bestand bei dem im Beschwerdefall konkret festgestellten Sachverhalt nach Ansicht des Bundesfinanzgerichts aufgrund der im Vorlageantrag dargelegten glaubwürdigen beruflichen Gründe eine Notwendigkeit für die Nutzung eines betrieblich verwendeten Arbeitszimmers.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Erich Schwaiger` (person)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Mag. Peter Staudinger` (person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_15`)


Über die Beschwerde wurde erwogen: Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_60`)


Dafür vermag das Bundesfinanzgericht keine Anhaltspunkte zu finden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Mirha Karahodzic MA` (person)
- `Elisabeth Schafstall` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_6`)


Der Vorlageantrag zur Entscheidung durch das Bundesfinanzgericht langte am 13.2.2020 beim  Bundesfinanzgericht ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_7`)


Das Bundesfinanzgericht leitete den Antrag zuständigkeitshalber an  das Finanzamt weiter, wo der Antrag am 14.2.2020 fristgerecht einlangte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_8`)


Die Vorlage der  Beschwerde samt Akten an das Bundesfinanzgericht erfolgte am 18.2.2020.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_9`)


II. Das Bundesfinanzgericht hat erwogen:  1. Feststellungen:  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_68`)


Auf  das tatsächliche Einsehen der Databox durch den Teilnehmer, beispielsweise durch ein  Öffnen, Lesen oder Ausdrucken eines Bescheides, kommt es für die Bewirkung einer  Zustellung nicht an (vgl. etwa BFG 14.2.2019, RV/7100457/2019, bzw. die bei Ritz, aaO,  genannte Judikatur).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_74`)


Anhaltspunkte dafür sind auch für das Bundesfinanzgericht nicht  erkennbar.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr.in Dietlind Mahlstädt` (person)
- `Kai Pipers` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_21`)


Mit Erkenntnis vom 25.6.2019, RV/5100452/2013 wies das Bundesfinanzgericht die  Beschwerde als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_30`)


Gegen das abweisende Erkenntnis vom 25.6.2019 des Bundesfinanzgerichts erhob der  rechtsfreundlich vertretene Bf Beschwerde gem. Art 144 B-VG an den Verfassungsgerichtshof.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_31`)


Mit Entscheidung vom 25.2.2020 hob der Verfassungsgerichtshof das Erkenntnis des  Bundesfinanzgerichts vom 25.6.2019 auf (VfGH vom 25.2.2020, E 2892/2019).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_43`)


4. Das Bundesfinanzgericht wendete bei Erlassung des angefochtenen Erkenntnisses die als  verfassungswidrig aufgehobene Gesetzesbestimmung an.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_48`)


II. Das Bundesfinanzgericht hat erwogen:  Festgestellter Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_60`)


Bei dem angefochtenen Bescheid vom 12.3.2013 handelt es sich jedoch nach Ansicht des  Bundesfinanzgerichts nicht um einen Aufhebungsbescheid gem. § 299 BAO im Sinne der  Bescheidbezeichnung, sondern um einen antragsgemäßen Aufhebungsbescheid gem. § 295  Abs. 4 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_64`)


Die Anführung des § 299 BAO in der dem Bescheidspruch vorangestellten Überschrift und in  der "Formularkennzeichnung" kommt keinerlei normativen Wirkung zu und beruht nach  Ansicht des Bundesfinanzgerichts aufgrund des eindeutigen Bescheidinhaltes offenkundig auf  einem Versehen der belangten Behörde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_72`)


Sache des Verfahrens vor dem Bundesfinanzgericht ist deshalb ausschließlich die  Rechtmäßigkeit der Aufhebung vom 12.3.2013 des Einkommensteuerbescheides vom  7.12.2007.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_84`)


Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `James Hainig` (person)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_37`)


Mit Bescheiden vom 21.12.2016 erließ das Finanzamt die Erstbescheide betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 in denen die  Berufsgruppenpauschale für VertreterInnen nicht gewährt wurde und begründete die  Bescheide wie folgt:   "Vertreter sind nach übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer  Kommentar, Tz 6 zu § 17 EStG), Verwaltungsübung LstRL RZ 406) und Entscheidungspraxis (zB  BFG 23.05.2014, RV/6100146/2013) Personen, die im Außendienst zum Zwecke der Anbahnung  und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_61`)


Nach  übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer Kommentar, Tz 6 zu § 17 EStG  1988), Verwaltungsübung (Rz 406 LStR 2002) und Entscheidungspraxis (zB BFG vom  23.05.2014, RV/6100146/2013) sind Vertreter Personen, die im Außendienst zum Zwecke der  Anbahnung und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_82`)


Mit Schreiben vom 21.02.2017 stellte die Beschwerdeführerin den Antrag auf Vorlage der  Beschwerde zur Entscheidung an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_87`)


Mit Schreiben vom 24.02.2017 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und verwies in Ihrer Begründung auf die  Beschwerdevorentscheidung vom 23.01.2017.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_89`)


Mit Schreiben vom 23.08.2017 erstattete die Beschwerdeführerin ein ergänzendes  Beschwerdevorbringen an das Bundesfinanzgericht mit dem folgenden Inhalt:  "Inhaltlich führt die Beschwerdeführerin aus, dass die pauschalen Werbungskosten gemäß § 1 Z  9 der Verordnung BGBL II 2001/382 eine ausschließliche Außendiensttätigkeit im  Anzeigenverkauf umfassen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_110`)


Mit Schreiben vom 24.03.2020 forderte das Bundesfinanzgericht die Beschwerdeführerin auf,  bekannt zu geben, in welchem Ausmaß Nebentätigkeiten wie zB. die Erstellung von  Werbetexten im beschwerdegegenständlichen Zeitraum getätigt wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_111`)


Das  Bundesfinanzgericht ersuchte die Beschwerdeführerin, die Nebentätigkeiten zeitlich sowie im  Verhältnis des Umsatzes für die Jahre 2014 und 2015 zu präzisieren.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_112`)


Mit Schreiben vom 31.03.2020 beantwortete die Beschwerdeführerin den Vorhalt des  Bundesfinanzgerichts und führte dazu aus wie folgt:   "Die Nebentätigkeit "Erstellung von Werbetexten“ im Zuge meiner Tätigkeit im Bereich  Mediaberatung als Angestellte für das AG Druck und Verlags GmbH umfasste maximal 20  Arbeitsstunden pro Kalenderjahr!

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `AG Druck und Verlags GmbH` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_120`)


Erst im Vorhalteverfahren vor dem Bundesfinanzgericht wurde das Ausmaß der  Nebentätigkeiten ermittelt. Das Vorbringen der Beschwerdeführerin, dass die ausgeübten  Nebentätigkeiten nur in einem untergeordneten Ausmaß stattgefunden haben und  hauptsächlich dazu dienten, den Anzeigenverkauf zu fördern, ist glaubhaft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_149`)


4.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_150`)


Gegen dieses Erkenntnis des Bundesfinanzgerichtes ist die ordentliche Revision nicht zulässig,  da es nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Hon.-Prof. Adalbert Köseoglu` (person)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_11`)


Das Bundesfinanzgericht erklärte die Beschwerde, soweit diese die nachträgliche buchmäßige  Erfassung von Eingangsabgaben (Zoll) betrifft, mit Beschluss vom 26. Mai 2017,  RV/6200002/2017, als zurückgenommen, weil die Bf einem Mängelbehebungsauftrag  (Musteranforderung) innerhalb der vom Zollamt gesetzten Frist nicht nachgekommen war, und  sprach aus, dass eine Revision nach Art 133 Abs 4 B-VG nicht zulässig ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_13`)


Den Bescheid betreffend Festsetzung einer Abgabenerhöhung hat das Bundesfinanzgericht mit  Erkenntnis vom 11. Mai 2017, RV/6200004/2017, aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_15`)


Das Bundesfinanzgericht hat erwogen:  Der Verwaltungsgerichtshof hat im Erkenntnis vom 19. Oktober 2017, Ra 2017/16/0098,  ausgesprochen, dass die mit dem Abgabenänderungsgesetz 2015 erfolgte Novellierung ua des  § 108 ZollR-DG auf die Anpassung der Rechtslage an den am 1. Mai 2016 in Kraft getretenen  Zollkodex der Union - UZK abzielt. Es sei nicht ersichtlich;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_20`)


Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  2 von 3 Seite 3 von 3

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Walter Summersberger` (person)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_30`)


II. Das Bundesfinanzgericht hat erwogen:  § 201.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_46`)


Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Helga Hochrieser` (person)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_5`)


Dazu führte  sie im beiliegendem Schreiben (ebenfalls vom 12.2.2018) aus, dass ihrem Vater V. die im Jahr  2011 beantragte Familienbeihilfe („zu Unrecht“) für sie nicht bewilligt worden sei -  Entscheidung Bundesfinanzgericht vom 9.1.2018.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_19`)


Sie wurde mit und meinen Geschwistern von meinem Vater zur Verfügung  gestellt. Im Akt meines Vaters bzw. im Urteil des Bundesfinanzgericht RV/7102641/2016 sind  alle diesbezüglichen Unterlagen vorhanden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_42`)


Das Bundesfinanzgericht hat in  seiner Entscheidung vom 9.1.2018 im Wesentlichen nur die Haushaltszugehörigkeit geprüft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_43`)


In  einem Hinweis führt aber auch das Bundesfinanzgericht aus (Seite 18), dass ich mit der  Übermittlung des Formulars Beih 20 tatsächlich einen Eigenantrag stellen wollte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_47`)


In weiterer Folge wurden am 26. Februar 2020 bei einer persönlichen Vorsprache der  Vertreterin der Bf. (laut ihren Angaben die ehemalige Lebensgefährtin des Vaters der Bf.) bei  der zuständigen Richterin des Bundesfinanzgerichts Zeugnisse (Unterlagen) der Bf. überreicht   (Kopien für Akt angefertigt).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_75`)


Wie schon im Erkenntnis des Bundesfinanzgerichts vom 9.1.2018 (welches in der  Beschwerdevorentscheidung vom 22.10.2018 zitiert wurde und den Vater der Bf. betrifft),  festgehalten wurde, ist der Antrag auf Direktzahlung nach § 14 Abs. 1 FLAG 1967 kein  Eigenantrag im Sinne des § 6 Abs. 5 FLAG 1967.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_87`)


Ergänzend wird (zum Sachverhalt und zur rechtlichen Beurteilung) noch auf das BFG-Erkenntnis  RV/7102641/2016 vom 9.1.2018 sowie auf die Beschwerdevorentscheidung des Finanzamts  vom 22.10.2018 verwiesen, deren Ausführungen vom Bundesfinanzgericht ausdrücklich geteilt  werden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_90`)


Zur Zulässigkeit der Revision (Spruchpunkt II)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Ali Jäckle` (person)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_8`)


Das Finanzamt legte die Beschwerde dem Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_10`)


Mit Beschluss des Bundesfinanzgerichtes vom 4.5.2020 wurde der Bf. gemäß § 85 Abs. 2 iVm  § 2a BAO aufgetragen, den Mangel des Vorlageantrages vom 9.8.2016 (fehlende Unterschrift  des Vorlageantrages) innerhalb einer Frist von zwei Wochen ab Zustellung des Beschlusses zu  beheben, andernfalls der Vorlageantrag als zurückgenommen gelte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_17`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision gemäß Art. 133 Abs. 4 iVm  Abs. 9 B-VG zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche  Bedeutung zukommt, insbesondere weil der Beschluss von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)
- `Finanzamtes Linz` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_19`)


c. Die Beschwerde gegen die Wiederaufnahme der Körperschaftsteuer 2011 bis 2015 wurde  vom BFG mit Erkenntnis vom 3. Juli 2020, RV/5101382/2019, als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_103`)


5. Am 30. September 2019 wurde die Beschwerde dem Bundesfinanzgericht zur Entscheidung  übermittelt. Es handle sich um eine reine Rechtsfrage.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_106`)


Das BFG geht davon aus, dass Unternehmensbilanz und  MWR eine Einheit bilden, die nach § 4 Abs 2 Z 2 EStG zu einem Zuschlag führen kann.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_145`)


Das BFG hat in RV/5101382/2019 jene Gründe angeführt, die eine Wiederaufnahme ab  dem Jahr 2008 ermöglicht hätten.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_150`)


Das Bundesfinanzgericht schließt sich der in der österreichischen und deutschen Lehre  vertretenen Rechtsansicht an: Der erste Schritt von der Handelsbilanz zur Steuerbilanz besteht  in einer innerbilanziellen Korrektur der Handelsbilanz: Nur Handelsbilanz und MWR  gemeinsam führen zur (gedanklichen) Steuerbilanz.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_158`)


E. Zulassung zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Marion Endrulat` (person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_65`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der im Dezember 1998 geborene Sohn der Bf. ist bei seiner Mutter, der Bf., haushaltszugehörig  und begann – nach Beendigung des Zivildienstes mit 31. März 2019 – am 13. Mai 2019 die  Polizeigrundausbildung bei der Landespolizeidirektion Niederösterreich im Bildungszentrum  der Sicherheitsakademie Y. auf Grund eines mit Sondervertrag gemäß § 36 VBG 1948 für die  exekutivdienstliche Ausbildung begründeten privatrechtlichen Dienstverhältnisses zum Bund  (§ 1 Abs. 1 VBG).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Landespolizeidirektion Niederösterreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_178`)


Diese  Ausbildungsphase dient der Berufsausübung und kann demnach nicht als Berufsausbildung iSd  § 2 Abs. 1 lit. b FLAG 1967 gewertet werden (vgl. auch BFG 25.06.2019, RV/7101825/2019;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_185`)


BFG 06.03.2019, RV/7103766/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_190`)


In Rz 4 führt der VwGH nämlich u.a. aus:   „… Mit dem angefochtenen Erkenntnis gab das Bundesfinanzgericht der Beschwerde gemäß  § 279 BAO teilweise Folge, …Nach Darstellung des Verwaltungsgeschehens einschließlich der  Beweisergebnisse traf das Gericht zunächst die eingangs wiedergegebenen Feststellungen, …  um daran – in rechtlicher Hinsicht – anzuschließen: „… Zur Verdeutlichung werden die  Unterschiede der Ausbildungslaufbahn der „Grenzpolizisten“ jenen der „Polizisten“  (Exekutivdienst) überblicksmäßig gegenübergestellt: … . Unstrittig ist, dass die Basisausbildung  der Grundausbildung für die exekutivdienstliche Verwendung im fremden- und  grenzpolizeilichen Bereich (Dauer 6 Monate) und die Ergänzungsausbildung zur  Grundausbildung für den Exekutivdienst (9 Monate) als Berufsausbildung im Sinne des  Familienlastenausgleichsgesetzes anzusehen sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_193`)


Das vor dem  VwGH angefochtenene Erkenntnis des BFG wird in Rz 4 (weitgehend) wörtlich wiedergegeben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_195`)


Die vom BFG im in Beschwerde gezogenen Erkenntnis  allenfalls wiedergegebene Rechtsansicht (wobei angemerkt sei, dass Streitgegenstand des  zitierten Erkenntnisses des BFG lediglich der Zeitraum der „Kursunterbrechung“ war;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_200`)


Diese Beurteilung vertritt das BFG in nunmehr ständiger Rechtsprechung.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_201`)


Vgl. die Erkenntnisse:      - BFG 03.03.2020, RV/7100641/2020 (Senat)   Rs: Der VwGH hat klargestellt (vgl. Rz 16 ff des Erkenntnisses vom 18.12.2018,  Ra 2018/16/0203), dass im Falle des Eintritts in ein Dienstverhältnis zum Bund bereits von  einer Berufsausübung auszugehen ist, die einen Familienbeihilfenanspruch ausschließt, auch  wenn in dieser Zeit im Auftrag des Dienstgebers eine Grundausbildung oder Ausbildungsphase  absolviert wird.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_204`)


- BFG 20.02.2020, RV/7100589/2020    Berufsausübung als Polizist keine Berufsausbildung iSd FLAG 1967   - BFG 12.02.2020, RV/7106079/2019    Grundausbildung einer Polizistin keine Berufsausbildung iSd FLAG 1967   - BFG 23.01.2020, RV/4100771/2019 (Senat)   - BFG 22.01.2020, RV/3100050/2020    Exekutivdienstliche Grundausbildung: Laut VwGH handelt es sich nicht um Berufsausbildung  iSd § 2 Abs. 1 lit. b FLAG 1967, sondern bereits um Berufsausübung   15 von 17 Seite 16 von 17

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_205`)


- BFG 17.01.2020, RV/3100894/2019   Rs: Die exekutivdienstliche Grundausbildung stellt ebenso wie weitere Ausbildungsschritte im  Rahmen des Dienstverhältnisses keine Berufsausbildung iSd FLAG 1967 dar.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_206`)


- BFG 15.01.2020, RV/3100858/2019   Exekutivdienstliche Grundausbildung: Laut aktueller VwGH-Judikatur handelt es sich um  "Berufsausübung"   - BFG 06.01.2020, RV/7105981/2019   Berufsausübung als Polizist keine Berufsausbildung iSd FLAG 1967   - BFG vom 02.01.2020, RV/3100895/2019   Polizei-Grundausbildung: Zufolge VwGH 18.12.2018, Ra 2018/16/0203, stellt die gesamte  Grundausbildung oder Ausbildungsphase des öffentlich Bediensteten KEINE Berufsausbildung  iSd § 2 Abs. 1 lit. b FLAG 1967 dar.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_207`)


- BFG 30.12.2019, RV/3100892/2019   Polizei-Grundausbildung: Laut VwGH 18.12.2018, Ra 2018/16/0203, liegt keine  Berufsausbildung iSd § 2 Abs. 1 lit. b FLAG 1967, sondern bereits eine Berufsausübung vor   - BFG 23.12.2019, RV/3100856/2019   Polizei-Grundausbildung im Rahmen eines Dienstverhältnisses ist keine Berufsausbildung iSd §  2 Abs. 1 lit. b FLAG 1967, sondern bereits Berufsausübung   - BFG 07.10.2019, RV/2101014/2019   Kein Familienbeihilfenanspruch für eine öffentlich Bedienstete (Exekutivdienst) in der  Ausbildungsphase

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_213`)


Es handelt  sich um keine Rechtsfrage von grundsätzlicher Bedeutung, da das Bundesfinanzgericht in  rechtlicher Hinsicht dem Erkenntnis VwGH 18.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Lieselotte Akdas` (person)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_39`)


In seinem Antrag vom 29.3.2018 auf Vorlage seiner Beschwerde an das Bundesfinanzgericht  brachte der Beschwerdeführer weiter vor, dass das Verfahren aufgrund der nicht erfolgten  Einvernahme von angebotenen Zeugen mangelhaft sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_48`)


Das Vorbringen zum Ausmaß der geschäftlichen Nutzung des Fahrzeuges lasse keine Schlüsse  auf den Ort der Verwendung zu.  Das Bundesfinanzgericht wies die Beschwerde mit Erkenntnis vom 16.10.2019 ab.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_50`)


Das Bundesfinanzgericht forderte den Beschwerdeführer am 25.9.2020 auf, die zehn im  Schreiben vom 13.11.2017 genannten, allesamt in Deutschland wohnhaften Zeugen am 16.,  17. und 18.6.2020 zur Einvernahme stellig zu machen, dies unter Hinweis darauf, dass das  Bundesfinanzgericht deren persönliches Erscheinen für erforderlich hält.  Mit Schreiben vom 9.6.2020 legte der Beschwerdeführer Protokolle über die Einvernahmen  der Zeugen Z1, Z2, Z3, Z4 und Z5 über Auftrag der BH Reutte im Strafverfahren wegen  3 von 14 Seite 4 von 14

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

## `Tax Authority - Finanzamt Locations` 🏆

**F1:** 0.078 | **Precision:** 0.955 | **Recall:** 0.041  

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
| 0.955 | 0.041 | 0.078 | 536 | 512 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 512 | 24 | 12098 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Mag. Peter Staudinger` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_11`)


Aufgrund einer weiteren Mitteilung setzte das damals auch für die einheitliche und gesonderte  Einkünftefeststellung der B K(E)G zuständig gewesene Finanzamt Wien 8/16/17  das Wohnsitzfinanzamt des  Bf davon in Kenntnis, dass im Feststellungsverfahren dieser Personengesellschaft am  28.11.2006 ebenfalls ua Erledigungen betreffend das Unterbleiben von Einkünftefeststellungen  für die beteiligten Kommanditisten für die Jahre 1998-2001 ausgefertigt worden sind.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_14`)


Im Dezember 2006 legte die B KEG ua Berufungen gegen die an sie adressierten „Bescheide“  des FA Wien 8/16/17  vom 1.12.2006 betreffend Einkünftefeststellung gem. § 188 BAO für die Jahre  1988 – 2001 sowie gegen die an sie und an die Kommanditisten adressierten „Bescheide“ des  Finanzamt Wien 8/16/17  vom 28.11.2006 betreffend Unterbleiben der Feststellungen von Einkünften in  Bezug auf die Kommanditisten für den Zeitraum 1998 – 2001 ein.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Missed by this rule (FN):**

- `FA Wien 8/16/17` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 8/16/17` | `Finanzamtes Wien 8/16/17` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker` (person)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Sean Herdling` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |
| `Finanzamtes Salzburg-Land` | `Finanzamtes Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melina Bankratz` (person)
- `Lars Huesgen` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 8/16/17` | `Finanzamtes Wien 8/16/17` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Rudolf Bogdanowic` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `90-074/8383` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Dr. Wolfgang Aigner` (person)
- `Erwin Agneter` (person)
- `Mag. Belinda  Maria Eder` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Mag. Katharina Moravec` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 8/16/17` | `Finanzamtes Wien 8/16/17` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Hon.-Prof. Thassilo Schoenrock, LLM` (person)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `06-88-920/2630` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Albert Sengeisen` (person)
- `Wallnerfeld 8, 3751 Sigmundsherberg, Österreich` (address)
- `Finanzamt  Wien 9/18/19` (organisation)
- `Albert Sengeisen` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Albert Sengeisen` (person)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_41`)


gegenständlichen Entscheidung des Spruchsenates beim Finanzamt Wien 9/18/19 vorliegende  Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19` | `Finanzamt Wien 9/18/19` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Braunau Ried` | `Finanzamtes Braunau Ried` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `KzlR Diethard Ringhand` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_8`)


Im Einkommensteuerbescheid für 2011 vom 10. Juli 2013 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

| Predicted | Gold |
|---|---|
| `Finanzamt  Salzburg-Land` | `Finanzamt  Salzburg-Land` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_9`)


Im Einkommensteuerbescheid für 2012 vom 30. April 2014 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

| Predicted | Gold |
|---|---|
| `Finanzamt  Salzburg-Land` | `Finanzamt  Salzburg-Land` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_10`)


Im Einkommensteuerbescheid für 2013 vom 22. Juli 2014 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

| Predicted | Gold |
|---|---|
| `Finanzamt  Salzburg-Land` | `Finanzamt  Salzburg-Land` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_11`)


Mit Ergänzungsersuchen des Finanzamtes Braunau Ried Schärding vom 26. März 2015  (betreffend die Einkommensteuererklärung 2014) wurde der Bf. aufgefordert, einen Nachweis  über den geleisteten Unterhalt der beiden Kinder K1 und K2 zu erbringen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Braunau Ried` | `Finanzamtes Braunau Ried` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_66`)


Im Vorhalteverfahren vor dem Bundesfinanzgericht übermittelte die Vertreterin des Bf. die  Vorhaltsbeantwortung an das Finanzamt Salzburg-Land vom 28. November 2013 betreffend  die Jahre 2009 bis 2012.

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_67`)


Aus dieser Vorhaltsbeantwortung und insbesondere aus dem dort angebrachten Vermerk der  Ex-Frau des Bf. ergibt sich, dass dem Finanzamt Salzburg-Land die Tatsache, dass der Bf. mit  den Kindern, für die er Unterhalt zu leisten hatte, nicht in einem gemeinsamen Haushalt gelebt  hatte, bereits am 28. November 2013 bekannt war.

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_68`)


Mit den nunmehr angefochtenen Wiederaufnahmebescheiden vom 21. August 2015 hat das  Finanzamt Braunau Ried Schärding Verfahren wiederaufgenommen, die vom Finanzamt  Salzburg-Land durchgeführt worden waren.

| Predicted | Gold |
|---|---|
| `Finanzamt  Salzburg-Land` | `Finanzamt  Salzburg-Land` |

**Missed by this rule (FN):**

- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt Oberwart` | `Finanzamtes Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_12`)


Mit Bescheid vom 10.07.2020 wies das Finanzamt Bruck Eisenstadt Oberwart (FA) den  Rückzahlungsantrag als unbegründet ab, weil nach Art. 3 Abs. 2 DBA-Deutschland für die  Beurteilung, ob diesbezüglich Einkünfte aus selbständiger oder aus nichtselbständiger Arbeit  vorliegen, die Bestimmungen des innerstaatlichen Rechts maßgebend seien.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximiliane Kotenbeutel` (person)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `69-367/5691` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Kirstin Matiascheck` (person)
- `Annemarie Schwinge` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `32-672/7699` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Chiara Duchan` (person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich` (address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hon.-Prof.in Elvira Thielsen` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` (person)
- `OMedR Leonhard Hestermeyer` (person)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `52-932/8889` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Heike Lehmensieck` (person)
- `Höllstein 11, 9852 Neuschitz, Österreich` (address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_80`)


IV. Rechtliche Beurteilung  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 tritt das Finanzamt Österreich am 01.01.2021  an die Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_81`)


Partei des  Verfahrens ist nunmehr das Finanzamt Österreich als belangte Behörde, deren Bezeichnung  war somit im Spruch entsprechend richtig zu stellen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Christoph Hasenfraz` (person)
- `Olivia Sahlmüller` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Bruck Eisenstadt  Oberwart` | `Finanzamtes Bruck Eisenstadt  Oberwart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandra Fenn` (person)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Mag. Manuela Meyerhofer` (person)
- `49-433/1564` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Dragan Carstens` (person)
- `StR Milena Neidig` (person)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Melinda Herrwerth` (person)
- `Dürergasse 7, 4872 Windbichl, Österreich` (address)
- `40-459/9630` (tax_number)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Lubomir Nakajima` (person)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_2`)


2.) über die Beschwerde vom 2. November 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 6. Oktober 2020 betreffend  Abweisung des Antrages vom 3. Juni 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den Zeitraum September 2015 bis April 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Lubomir Nakajima` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_2`)


Saskia Sinnwell, Wien1  beide vertreten durch Christoph Zitz MBA, murtax Steuerberatungs GmbH Kuenburgstraße 10,  5580 Tamsweg  wegen des Finanzvergehens der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG), beim Verband gemäß § 28a Abs. 2 FinStrG, über die Beschwerde  des Amtsbeauftragten vom 17. September 2019 (gemeint wohl richtig: 3. Dezember 2020)  gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19  Klosterneuburg als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. September 2020, SpS 2000, in der Sitzung am 27. Mai 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Saskia Sinnwell` (person)
- `Christoph Zitz MBA` (person)
- `murtax Steuerberatungs GmbH` (organisation)
- `Finanzamt Wien 9/18/19` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_4`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde  vom , Strafnummer 2019, SpS 2000, wurde das gegen   1) A B, Russland, derzeit in Karenz, wohnhaft Adresse1, und   2) Saskia Sinnwell, Wien;

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Saskia Sinnwell` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Jonas Gutkauf` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_14`)


Mit Beschwerdevorentscheidungen vom 13. Jänner 2021 hat das nunmehr zuständige  Finanzamt Österreich die Beschwerde abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden R1, die RichterinR2 sowie die  fachkundigen Laienrichter R3 und R4 in der Beschwerdesache C als Gottfried Kamperschroer, Allentsgschwendt 4W, 8741 Allersdorf, Österreich,  vertreten durch Schmidt & Schmidt KG, Bahnzeile 10, 2130 Mistelbach, über die Beschwerde  vom 13. Dezember 2012 gegen die gem. § 200 Abs. 2 BAO endgültigen Bescheide des  Finanzamtes Gänserndorf Mistelbach (nunmehr Finanzamt Österreich) vom 4. Oktober 2012  betreffend Einkommensteuer 2005 bis 2008, Steuernummer 84-352/6923, nach  Durchführung einer mündlichen Verhandlung am 10. Juni 2021 in Anwesenheit der  Schriftführerin S1, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gottfried Kamperschroer` (person)
- `Allentsgschwendt 4W, 8741 Allersdorf, Österreich` (address)
- `Schmidt & Schmidt KG` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `84-352/6923` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_2`)


Stock, 1220 Wien, über die  Beschwerde vom 16. Dezember 2015 gegen die Bescheide des Finanzamtes Baden Mödling  vom 12. November 2015 (nunmehr Finanzamt Österreich) betreffend Wiederaufnahme der  Verfahren hinsichtlich Umsatz- und Körperschaftsteuer für das Jahr 2013 sowie Umsatz- und  Körperschaftsteuer für die Jahre 2013 und 2014, nach Durchführung einer mündlichen  Verhandlung am 7. Juli 2021 in Anwesenheit der Schriftführerin S   I. zu Recht erkannt:   Der Beschwerde gegen die Bescheide betreffend Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Körperschaftsteuer für das Jahr 2013 sowie gegen die Bescheide  betreffend Umsatz- und Körperschaftsteuer für das Jahr 2014 wird gemäß § 279 BAO Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes Baden Mödling` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fatima Eichmayr` (person)
- `Wieskapellenweg 10, 8047 Graz, Österreich` (address)
- `Dr. Klaus Plätzer,` (person)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `67-455/2359` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Lee Kubbig` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Martin Kuprian` (person)
- `Ing. Werner Böltl` (person)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Finanzamt Vorarlberg` | `Finanzamt Vorarlberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Esra Nowy` (person)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_130`)


Beschwerdevorlage des Finanzamt Vorarlberg  vom 19.12.2019 betreffend die Rusnok IT GmbH (DB , DZ 2010- 2012).

| Predicted | Gold |
|---|---|
| `Finanzamt Vorarlberg` | `Finanzamt Vorarlberg` |

**Missed by this rule (FN):**

- `Rusnok IT GmbH` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `02-365/4052` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_44`)


Das E-Mail vom 6.9.2021, mit dem die Zurücknahme der Säumnisbeschwerden vom 23.8.2021  angekündigt wurde, wurde auch an eine Empfängerin des Finanzamtes Österreich gesendet.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_45`)


Das Finanzamt Österreich wurde vom Bundesfinanzgericht jedoch noch nicht über die  Säumnisbeschwerden vom 23.8.2021 in Kenntnis gesetzt, weil zunächst ein  Mängelbehebungsverfahren durchzuführen war.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_46`)


Aus diesem Grund erfolgt die Zustellung  dieses Beschlusses auch an das Finanzamt Österreich zur Kenntnis.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Feldkirch` | `Finanzamtes Feldkirch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Moses Dannebohm` (person)
- `Ruperta Schluckner` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_109`)


Rechtliche Beurteilung  1. Zuständigkeit  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 treten das Finanzamt Österreich und das  Finanzamt für Großbetriebe für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die  Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_113`)


Dies vorausgeschickt gilt sohin zu klären, ob im nunmehrigen Beschwerdeverfahren das  Finanzamt Österreich oder aber das Finanzamt für Großbetriebe belangte Behörde ist: Das  Finanzamt Österreich und das Finanzamt für Großbetriebe sind nach der Lehre nunmehr für  die Erledigung der zum 31.12.2020 anhängigen Verfahren (Prüfungen, offene  Beschwerdeverfahren, etc.) in ihrem jeweiligen Zuständigkeitsbereich zuständig.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_100`)


dieser Grund ist jedoch nicht als beachtlich anzusehen (vgl. dazu die im Zuge der rechtlichen  Beurteilung dargelegte höchstgerichtliche Judikatur)  1. IV.Rechtliche Beurteilung  1.1. Zuständigkeit  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 treten das Finanzamt Österreich und das  Finanzamt für Großbetriebe für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die  Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_104`)


Dies vorausgeschickt gilt sohin zu klären, ob im nunmehrigen Beschwerdeverfahren das  Finanzamt Österreich oder aber das Finanzamt für Großbetriebe belangte Behörde ist: Das  Finanzamt Österreich und das Finanzamt für Großbetriebe sind nach der Lehre nunmehr für  die Erledigung der zum 31.12.2020 anhängigen Verfahren (Prüfungen, offene  Beschwerdeverfahren, etc.) in ihrem jeweiligen Zuständigkeitsbereich zuständig.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_105`)


IV. Rechtliche Beurteilung  1. Zuständigkeit  Gemäß § 323 b Abs. 1 BAO idF BGBl. I 2020/99 treten das Finanzamt Österreich und das  Finanzamt für Großbetriebe für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die  Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamtes` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_109`)


Dies vorausgeschickt gilt sohin zu klären, ob im nunmehrigen Beschwerdeverfahren das  Finanzamt Österreich oder aber das Finanzamt für Großbetriebe belangte Behörde ist: Das  Finanzamt Österreich und das Finanzamt für Großbetriebe sind nach der Lehre nunmehr für  die Erledigung der zum 31.12.2020 anhängigen Verfahren (Prüfungen, offene  Beschwerdeverfahren, etc.) in ihrem jeweiligen Zuständigkeitsbereich zuständig.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt für Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `James Jantschke` (person)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_6`)


Das Finanzamt X (FA), jetzt Dienststelle des Finanzamtes Österreich, geht davon aus, dass die  (geringfügigen) slowenischen Pensionsbezüge des Beschwerdeführers (Bf) im Rahmen der  Arbeitnehmerveranlagung (ANV) als nichtselbständige Einkünfte (ohne Lohnsteuerabzug) der  Besteuerung in Österreich zu unterziehen sind.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Walter Monheim` (person)
- `Enrico Steudtle` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `10-940/7308` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Laurin Überschar` (person)
- `Albert Theiselmann` (person)
- `Hochmark 31g, 8323 Unterbuch, Österreich` (address)
- `Radike, Hammerl & Partner Steuerberatung GmbH` (organisation)
- `15-781/1702` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_3`)


Begründung  1. Sachverhalt  Mit Bescheiden des Finanzamtes Österreich vom 20. Mai 2021 wurde die Einkommensteuer für  die Jahre 2015 und 2016 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Riin` (person)
- `Karina Schliekau` (person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich` (address)
- `Finanzamt Wien 3/6/7/11/15` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `83-631/7208` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Ibrahim de Vrese, LLB, Kitzlermühle 3, 2754 Wopfing, Österreich, über die Beschwerde vom 07.06.2021 wegen behaupteter  Verletzung der Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Familienbeihilfe ab 09/2019 Sozialversicherungsnummer 2872011080  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Stephan` (person)
- `Ibrahim de Vrese, LLB` (person)
- `Kitzlermühle 3, 2754 Wopfing, Österreich` (address)
- `2872011080` (social_security_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache MedR Gertrude Hartges,  Hübing 15, 9535 Farrendorf, Österreich, über die Beschwerde vom 10. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Gertrude Hartges` (person)
- `Hübing 15, 9535 Farrendorf, Österreich` (address)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Alois Kleynsteuber` (person)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_45`)


Dem Finanzamt wurde im  Mai 2012 eine Kontrollmitteilung vom Finanzamt Salzburg-Land übermittelt aus der  hervorgeht, dass Sie Aktionär der Ges.1 waren und die Anschaffungskosten der Beteiligung laut  Einbringungsbilanz zum 31. August 2001 € - 102.094,62 betrugen.

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Dimitri Isakova` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `93-163/8536` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_6`)


Das Finanzamt XY, jetzt Finanzamt Österreich (FA) nimmt auf Basis einer Rechnung vom 30.Juni  2017 im Zusammenhang mit dem Transfer von Betriebsvermögen aus dem österreichischen  Betrieb der Bf in die Niederlande (NL) einen umsatzsteuerpflichtigen Vorgang an.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `KommR Nicola Sturzbecher` (person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich` (address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.` (organisation)
- `19-116/5774` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_2`)


Die Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes  Österreich vom 03. Juli 2013 bezüglich Wiederaufnahme der Verfahren die  Umsatzsteuer 2009-2011 betreffend wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_5`)


Die Beschwerde vom 03.Oktober 2013 gegen die Bescheide des Finanzamtes Österreich  vom 03. Juli 2013 bzw. 25. April 2017 die Umsatzsteuer 2009-2012 betreffend wird  gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_57`)


4. Rechtliche Beurteilung  Gemäß § 323b Abs. 1 BAO idF BGBl. I 2020/99 tritt das Finanzamt Österreich am 01.01.2021 an  die Stelle des jeweils am 31.12.2020 zuständig gewesenen Finanzamtes.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_58`)


Partei des Verfahrens  ist nunmehr das Finanzamt Österreich als belangte Behörde, deren Bezeichnung war somit im  Spruch entsprechend richtig zu stellen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_38`)


Gemäß § 323b Abs. 1 BAO trat das Finanzamt Österreich am 1. Jänner 2021 an die Stelle des  Finanzamtes Wien 12/13/14 Purkersdorf.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_39`)


Das Finanzamt Österreich erließ eine abweisende, mit 1. September 2021 datierte  Beschwerdevorentscheidung, welche laut Rückschein am 03.09.2021 zugestellt wurde und  welche folgendermaßen begründet wurde: „Das WiEReG trag[t] am 15.01.2018 in Kraft.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_64`)


Das Finanzamt Österreich legte die Beschwerde am 27. Dezember 2021 dem  Bundesfinanzgericht (BFG) vor und erstattete einen Vorlagebericht.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)
- `Dr. Stephan Riel` (person)
- `44-993/1626` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_3`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 20. April 2021 betreffend Pfändung einer  Geldforderung wurde festgehalten, dass die Mittel-Verlag (in weiterer Folge: Bf.), Am Rothenbühl 45, 4690 Ennsberg, Österreich  Abgaben einschließlich Nebengebühren in Höhe von € 138.702,89 schulde.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_15`)


Mit Beschwerdevorentscheidung des Finanzamtes Österreich vom 27. Mai 2021 wurde die  Beschwerde als unbegründet abgewiesen, mit folgender Begründung:  „Da keine Stundungsbewilligung gegeben wurde, sondern eine Ratenzahlung bewilligt wurde,  kommt die gesetzliche Stundung nicht zu tragen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_21`)


Vorlagebericht Finanzamt Österreich:  Mit Beschluss des Handelsgerichtes Wien wurde über die Firma Mittel-Verlag  ein  Sanierungsverfahren ohne Eigenverwaltung eröffnet.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Mittel-Verlag` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Dietmar Kachelmuss` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sulamith Jedwillat` (person)
- `Brandenbergweg 15, 8353 Pichla, Österreich` (address)
- `Mag. Michael Payr` (person)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)
- `41-852/7395` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Denis Diekötter` (person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich` (address)
- `Rein & Partner Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Ludger Endel` (person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich` (address)
- `63-868/1042` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Jedamczik` (person)
- `ÖkR Tobias Schönyan` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Mag. Gernot Thonhauser` (person)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_86`)


Zur Zwangsstrafe:  § 16 Abs 1 WiEReG lautet: „Wird die Meldung gemäß § 5 nicht erstattet, kann das Finanzamt  Österreich deren Vornahme durch Verhängung einer Zwangsstrafe gemäß § 111 BAO  erzwingen.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

**False Positives:**

- `Finanzamt  Wien 9/18/19 Klosterneuburg` — partial — gold is substring of pred: `Finanzamt  Wien 9/18/19`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Albert Sengeisen`(person)
- `Wallnerfeld 8, 3751 Sigmundsherberg, Österreich`(address)
- `Finanzamt  Wien 9/18/19`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Albert Sengeisen`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_17`)


Mit Bescheiden vom 21. August 2015 nahm das Finanzamt Braunau Ried Schärding das  Verfahren betreffend Einkommensteuer 2009, 2010, 2011, 2012 und 2013 gemäß  § 303 Abs. 1 BAO wieder auf.

**False Positives:**

- `Finanzamt Braunau Ried` — partial — pred is substring of gold: `Finanzamt Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau Ried Schärding`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_19`)


Im Einkommensteuerbescheid für 2009 vom 21. August 2015 berücksichtigte das Finanzamt  Braunau Ried Schärding im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungs- kosten, die der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 727,48 €.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_25`)


Diesfalls stehen weder Kosten für die doppelte Haushaltsführung noch für die Familien- heimfahrten zu.  Im Einkommensteuerbescheid für 2010 vom 21. August 2015 berücksichtigte das Finanzamt  Braunau Ried Schärding im Rahmen der Einkünfte aus nichtselbständiger Arbeit lediglich den  Pauschbetrag für Werbungskosten in Höhe von 132,00 €.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_26`)


In der Bescheidbegründung wurde die Begründung des Einkommensteuerbescheides für 2009  vom 21. August 2015 wiederholt.  Im Einkommensteuerbescheid für 2011 vom 21. August 2015 berücksichtigte das Finanzamt  Braunau Ried Schärding im Rahmen der Einkünfte aus nichtselbständiger Arbeit lediglich den  Pauschbetrag für Werbungskosten in Höhe von 132,00 €.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_27`)


In der Bescheidbegründung wurde die Begründung des Einkommensteuerbescheides für 2009  vom 21. August 2015 wiederholt.  Im Einkommensteuerbescheid für 2012 vom 21. August 2015 berücksichtigte das Finanzamt  Braunau Ried Schärding im Rahmen der Einkünfte aus nichtselbständiger Arbeit lediglich den  Pauschbetrag für Werbungskosten in Höhe von 132,00 €.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_28`)


In der Bescheidbegründung wurde die Begründung des Einkommensteuerbescheides für 2009  vom 21. August 2015 wiederholt.  Im Einkommensteuerbescheid für 2013 vom 21. August 2015 berücksichtigte das Finanzamt  Braunau Ried Schärding im Rahmen der Einkünfte aus nichtselbständiger Arbeit lediglich den  Pauschbetrag für Werbungskosten in Höhe von 132,00 €.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_40`)


Mit Beschwerdevorentscheidungen vom 13. November 2015 wies das Finanzamt Braunau  Ried Schärding die Beschwerden gegen die Einkommensteuerbescheide 2009 bis 2014 als  unbegründet ab.

**False Positives:**

- `Finanzamt Braunau  Ried` — partial — pred is substring of gold: `Finanzamt Braunau  Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau  Ried Schärding`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_42`)


Mit Vorlagebericht vom 18. Dezember 2015 legte das Finanzamt Braunau Ried Schärding die  Beschwerden gegen Einkommensteuerbescheide vom 21. August 2015 betreffend die Jahre  2009 bis 2014 dem Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung  der Beschwerde.

**False Positives:**

- `Finanzamt Braunau Ried` — partial — pred is substring of gold: `Finanzamt Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau Ried Schärding`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_43`)


Mit Vorlagebericht vom 4. Dezember 2020 legte das Finanzamt Braunau Ried Schärding auch  die Beschwerden vom 16. September 2015, soweit sie sich gegen die Wiederaufnahme- bescheide für die Jahre 2009 bis 2013 richten, dem Bundesfinanzgericht zur Entscheidung vor  und beantragte die Abweisung der Beschwerde.

**False Positives:**

- `Finanzamt Braunau Ried` — partial — pred is substring of gold: `Finanzamt Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau Ried Schärding`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_49`)


Diese neuen Tatsachen wurden dem Finanzamt  Braunau Ried Schärding erst im Jahr 2015 im Zuge des Ergänzungsersuchens für die  Veranlagung des Kalenderjahres 2014 bekannt.

**False Positives:**

- `Finanzamt  Braunau Ried` — partial — pred is substring of gold: `Finanzamt  Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt  Braunau Ried Schärding`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_51`)


Aufgrund der neu in Erfahrung gebrachten Tatsachen,  veranlasste das Finanzamt Braunau Ried Schärding ebenfalls eine Wiederaufnahme des  Verfahrens der Jahre 2009-2013 gem. § 303 Abs. 1 BAO.

**False Positives:**

- `Finanzamt Braunau Ried` — partial — pred is substring of gold: `Finanzamt Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau Ried Schärding`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_68`)


Mit den nunmehr angefochtenen Wiederaufnahmebescheiden vom 21. August 2015 hat das  Finanzamt Braunau Ried Schärding Verfahren wiederaufgenommen, die vom Finanzamt  Salzburg-Land durchgeführt worden waren.

**False Positives:**

- `Finanzamt Braunau Ried` — partial — pred is substring of gold: `Finanzamt Braunau Ried Schärding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Braunau Ried Schärding`(organisation)
- `Finanzamt  Salzburg-Land`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_2`)


Saskia Sinnwell, Wien1  beide vertreten durch Christoph Zitz MBA, murtax Steuerberatungs GmbH Kuenburgstraße 10,  5580 Tamsweg  wegen des Finanzvergehens der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG), beim Verband gemäß § 28a Abs. 2 FinStrG, über die Beschwerde  des Amtsbeauftragten vom 17. September 2019 (gemeint wohl richtig: 3. Dezember 2020)  gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19  Klosterneuburg als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. September 2020, SpS 2000, in der Sitzung am 27. Mai 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt Wien 9/18/19  Klosterneuburg` — partial — gold is substring of pred: `Finanzamt Wien 9/18/19`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Saskia Sinnwell`(person)
- `Christoph Zitz MBA`(person)
- `murtax Steuerberatungs GmbH`(organisation)
- `Finanzamt Wien 9/18/19`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

</details>

---

## `Tax Authority - Generic Finanzamt` 🏆

**F1:** 0.271 | **Precision:** 0.919 | **Recall:** 0.159  

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
| 0.919 | 0.159 | 0.271 | 2185 | 2007 | 178 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2007 | 178 | 10603 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_7`)


Das Bundesfinanzgericht leitete den Antrag zuständigkeitshalber an  das Finanzamt weiter, wo der Antrag am 14.2.2020 fristgerecht einlangte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_9`)


Mit Bescheid vom 13.11.2000 veranlagte das Finanzamt den Bf zur Einkommensteuer für 1999  zunächst erklärungsgemäß.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_10`)


Aufgrund von abweichenden Mitteilungen des für die Einkünftefeststellung gem. § 188 BAO  der Beteiligung A und der Beteiligung C vom 1.12.2006 erließ das Finanzamt am 9.1.2007 einen  gem. § 295 Abs. 1 BAO geänderten Einkommensteuerbescheid 1999 und setzte darin die  Einkünfte aus Gewerbebetrieb neu lediglich mit der Beteiligung B fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_12`)


Folglich dieser Mitteilung änderte das belangte Finanzamt den Einkommensteuerbescheid  1999 des Bf am 7.12.2007 erneut gem. § 295 Abs. 1 BAO dahingehend ab, dass in diesem  nunmehr Einkünfte aus Gewerbebetrieb iHv ATS 0,00 angesetzt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_16`)


Verstoß gegen das für Grundlagenbescheide iSd § 188 BAO geltende Einheitlichkeitsgebot  insgesamt um Nichtbescheide handelt.  Mit schriftlichem Anbringen vom 20.12.2012, eingelangt beim Finanzamt am 28.12.2012,  beantragte die steuerliche Vertreterin des Bf ua den Einkommensteuerbescheid 1999 vom  7.12.2007 gem. § 295 Abs. 4 BAO aufzuheben, weil diesem auf Grundlage des § 295 Abs. 1 BAO  ergangenen Einkommensteuerbescheid laut Berufungsentscheidung des UFS vom 15.11.2012,  RV/0102-K/08 (betreffend Beteiligung KEG), ein Nichtbescheid mit Folge seiner  Rechtswidrigkeit zugrunde liege, und somit die Anspruchsvoraussetzungen iSd § 295 Abs. 4  BAO erfüllt seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_17`)


Mit offenkundig versehentlich als „Aufhebungsbescheid gem. § 299 BAO betiteltem  Sammelbescheid vom 12.3.2013 hob das belangte Finanzamt ua den  Einkommensteuerbescheid 1999 vom 7.12.2007 nach eindeutigem Bescheidspruch und damit  im Einklang stehender Begründung wie beantragt auf Grundlage des § 295 Abs. 4 BAO auf.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_19`)


Das Finanzamt hätte unrichtigerweise die  notwendigen ersetzenden Bescheide gem. § 299 Abs. 2 BAO nicht erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `James Hainig` (person)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `85-229/2263` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Schreiben vom 15.06.2016 wurden die Erklärungen betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 beim Finanzamt eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_37`)


Mit Bescheiden vom 21.12.2016 erließ das Finanzamt die Erstbescheide betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 in denen die  Berufsgruppenpauschale für VertreterInnen nicht gewährt wurde und begründete die  Bescheide wie folgt:   "Vertreter sind nach übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer  Kommentar, Tz 6 zu § 17 EStG), Verwaltungsübung LstRL RZ 406) und Entscheidungspraxis (zB  BFG 23.05.2014, RV/6100146/2013) Personen, die im Außendienst zum Zwecke der Anbahnung  und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_92`)


Inhaltlich  hätte sich das Finanzamt **** durch umfassendere Beweiswürdigung mit der tatsächlichen  Tätigkeit der Beschwerdeführerin auseinanderzusetzen gehabt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Antrag  Der Beschwerdeführerin (Bf.) beantragte mit dem am 21. März 2018 beim Finanzamt (FA)  eingelangtem Formular Beih 1 (datiert mit 12. Februar 2018) Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_12`)


Mit Bescheid vom 12. Juni 2018 wies das Finanzamt den Antrag vom 21.3.2018 auf  Familienbeihilfe für Jana Papenkord  ab Jänner 2011 ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Jana Papenkord` (person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_23`)


Beschwerdevorentscheidung   Mit Beschwerdevorentscheidung vom 22.10.2018 wies das Finanzamt die Beschwerde als  unbegründet ab:  „Gemäß § 5 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG 1967) in der ab 1. Jänner 2011  gültigen Fassung besteht für Kinder, die das 18.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_51`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Vom Finanzamt wurde folgender Sachverhalt festgehalten:  „Der Eigenantrag auf Familienbeihilfe wurde am 21.03.2018 eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_6`)


Nach Durchführung umfangreicher Ermittlungen bei den steuerlichen Vertretern und der  Masseverwalterin des Ehemannes wies das Finanzamt die Beschwerde mit  Beschwerdevorentscheidung vom 12.7.2016 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_8`)


Das Finanzamt legte die Beschwerde dem Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_51`)


Im Anschluss an eine Außenprüfung für 2013 bis 2015 habe das Finanzamt auch für 2011  einen neuen Körperschaftsteuerbescheid erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_113`)


Diese ist zusammen mit  der Gewinn- und Verlustrechnung dem Finanzamt vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marion Endrulat` (person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_10`)


…   Das Finanzamt erließ am 5. September 2019 den beschwerdegegenständlichen  Abweisungsbescheid wie folgt:   Ihr Antrag vom 5.4.2019 auf Familienbeihilfe wird abgewiesen für:   Name des Kindes VNR/Geb.dat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_15`)


Das Finanzamt Gänserndorf  Mistelbach hat mit Bescheid diesen Antrag abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_33`)


IV. Beschwerdeerklärung und Anträge   Ich erhebe daher gegen den Bescheid der belangten Behörde vom 05.09.2019, (ohne) GZ, in  offener Frist gem § 243 BAO iVm Art 130 Abs 1 Z 1 B-VG und Art 131 Abs 3 B-VG   Bescheidbeschwerde an das Verwaltungsgericht des Bundes für Finanzen und stelle den   Antrag das Verwaltungsgericht des Bundes für Finanzen möge   - den angefochtenen Bescheid vom 05.09.2019, (ohne) GZ, aufheben und die Angelegenheit  zur Erlassung eines neuen - meinem Antrag stattgebenden - Bescheides an das Finanzamt  Gänserndorf Mistelbach zurückverweisen,   - in eventu den angefochtenen Bescheid dahingehend abändern, dass meinem Antrag auf  Familienbeihilfe für meinen Sohn … ab April 2019 stattgegeben wird.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_34`)


Das Finanzamt erließ eine abweisende Beschwerdevorentscheidung mit folgender  Begründung:   Das Kind …, SVNR …, wurde mit Wirkung 13.05.2019 in den Polizeidienst eingestellt.   Der Bestätigung des Bildungszentrums der Sicherheitsakademie Y. -SIAK- entnehmbar  absolviert der Sohn … vom 13.05.2019 bis 12.05.2021 den Grundausbildungslehrgang Y-… für  den Exekutivdienst im Bildungszentrum der Sicherheitsakademie Y..   Mit Dienstvertrag – als Sondervertrag gem. § 36 VBG 1948 – vom 13.05.2019 wurde das  privatrechtliche Dienstverhältnis zum Bund (§ 1 Abs. 1 VBG 1948) begründet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_57`)


Die Bf. brachte daraufhin den Vorlageantrag ein, mit dem sie die in der Beschwerde gemachten  Ausführungen wiederholt.   Die Beschwerdevorlage des Finanzamtes erfolgte mit nachstehendem Sachverhalt und  Anträgen:   Sachverhalt:   Der Sohn der Beschwerdeführerin … begann am 13.05.2019 die exekutivdienstliche Ausbildung  im Bildungszentrum Y.. Die Einstellung in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich erfolgte mit Sondervertrag nach § 36 VBG 1948.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Landespolizeidirektion  Niederösterreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_157`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer Anzeige vom 20.4.2017 vernahm das Finanzamt den Beschwerdeführer am  9.5.2017 ein und verfasste darüber eine Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_12`)


Das Finanzamt setzte mit Bescheid vom 7.6.2017 die Normverbrauchsabgabe für das Fahrzeug  BMF 750d xDrive mit der Fahrgestellnummer 12345 und dem amtlichen Kennzeichen (D) XYZ in  1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `BMF` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_22`)


Mit Schreiben vom 16.10.2017 forderte das Finanzamt den Beschwerdeführer auf,  zweckdienliche Unterlagen zum Beweis des dauernden Standortes bzw. der weitaus  überwiegenden betrieblichen Verwendung des Fahrzeuges im Ausland und zum Beweis des  Mittelpunkts seiner Lebensinteressen im Ausland vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_23`)


Weiter forderte das Finanzamt  eine Aufstellung der betrieblich bzw privat gefahrenen Kilometer im In- und Ausland an.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_24`)


Das  Finanzamt verwies dabei auf zwei vorliegenden Tankrechnungen (eni Reutte vom 4.5.2017 und  Shell d_Ort_1 vom 28.4.2017).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_36`)


Mit Beschwerdevorentscheidung vom 22.3.2018 wies das Finanzamt die Beschwerde ab und  begründete dies damit, dass der Beschwerdeführer bei seiner Einvernahme am 9.5.2017  angegeben habe, der Besitzer und Verwender des gegenständlichen Fahrzeuges zu sein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_46`)


Im Vorlagebericht vom 25.5.2018 brachte das Finanzamt weiter vor, dass der  Beschwerdeführer die im Vorlageantrag angesprochene Anmeldebestätigung nicht vorgelegt  habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_226`)


Einwendungen gegen die vom  Finanzamt ermittelten Bemessungsgrundlagen und die Höhe der festgesetzten Abgaben hat  der Beschwerdeführer nicht erhoben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_43`)


1. Anspruchsberechtigung auf Familienbeihilfe/Ausgleichszahlung für das Kind x im Zeitraum  vom 01.02.2016 bis zum 30.11.2017  Unter Bezugnahme auf die Ausführungen der belangten Behörde in  der Beschwerdevorentscheidung (BVE) vom 08.01.2020 sowie in der Ihnen  übermittelten Stellungnahme im Vorlagebericht des Finanzamtes vom 14.04.2020 werden Sie  nochmals darauf hingewiesen, dass in Ermangelung des Bestehens eines gemeinsamen  Haushalts mit obigem Kind eine Anspruchsberechtigung für nämlichen Zeitraum nicht zum  Tragen kommt.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_5`)


Dauer der Tätigkeit: 31.08.2020  Bezeichnung der Schule: Sicherheitsakademie T.[Adresse]   Schulform: Sonstiges   Schuljahr: 2018/2019  Das Finanzamt erließ am 21. August 2019 den beschwerdegegenständlichen Bescheid, mit dem  der Antrag der Bf. vom 6. April 2019 auf Familienbeihilfe ab September 2018 abgewiesen  wurde;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_30`)


Das Finanzamt wies mit Beschwerdevorentscheidung vom 25. Oktober 2019, zugestellt durch  Hinterlegung am 30. Oktober 2019, die Beschwerde als unbegründet ab und begründete dies  wie folgt:   Gemäß § 2 Abs. 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die  im Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_62`)


In der Beschwerdevorlage wies das Finanzamt auf die exekutivdienstliche Ausbildung der Bf.  mit Sondervertrag für Vertragsbedienstete des Bundes sowie auf das Erkenntnis des VwGH  vom 18.12.2018, GZ Ra 2018/16/0203, hin und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_167`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_3`)


Begründung  Am 10.5.2019 erließ das Finanzamt gegenüber der Beschwerdeführerin (Bf.) die  Einkommensteuerbescheide (Arbeitnehmerveranlagung) für 2015 bis 2018 (die Bescheide der  Jahre 2015 bis 2017 ergingen im Rahmen einer beantragten Wiederaufnahme).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_4`)


Mit Eingabe vom 11.4.2020, die vom Finanzamt – nach Ansicht des BFG zutreffend – als Antrag  auf Aufhebung der Einkommensteuerbescheide 2015 bis 2018 gemäß § 299 BAO gewertet  wurde, bemängelte die Bf., dass in den Bescheiden die Mietkosten für ihren Sohn nicht als  außergewöhnliche Belastungen berücksichtigt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_8`)


Mit den angefochtenen Bescheiden wies das Finanzamt den Antrag der Bf. mit folgender  Begründung ab:  „Außergewöhnliche Belastungen müssen gemäß § 34 EStG 1988 folgende Voraussetzungen  erfüllen:  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_22`)


Die abweisenden Beschwerdevorentscheidungen begründete das Finanzamt wie folgt:  „Eine außergewöhnliche Belastung im Sinne des § 34 EStG 1988 liegt dann vor, wenn die  Ausgaben außergewöhnlich und zwangsläufig erwachsen sind und die wirtschaftliche  Leistungsfähigkeit beeinträchtigen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_71`)


Dazu kommt, dass in den Bescheiden des Finanzamtes lediglich auf die Abs. 1 bis 4 des § 34  EStG 1988 verwiesen wird.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_73`)


Da das Finanzamt – den vorgelegten Aktenteilen zufolge - jegliche Ermittlungstätigkeit  unterlassen hat, ist eine Zurückverweisung iSd. § 278 BAO jedenfalls zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_83`)


Es ist davon auszugehen, dass dem Finanzamt zumindest einige der oa.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_85`)


Das Finanzamt kann die erforderlichen Ermittlungen daher aufgrund  allenfalls bereits vorhandener Kenntnisse aus anderen Verfahren mit Sicherheit rascher und  kostensparender als das Bundesfinanzgericht durchführen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_15`)


Der Bf. erläutert darin, alle vom Finanzamt angeforderten Unterlagen vorgelegt zu haben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_19`)


Mit Ersuchen um Ergänzung (Schreiben des Finanzamtes vom 9. Mai 2019) wurde dem Bf.  aufgetragen darzulegen, ob er für seine Kinder D und W für den Zeitraum Jänner bis Dezember  2018 Kinderbeihilfen im Heimatland bezogen habe.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Basil Staerk` (person)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `60-450/8034` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_5`)


Am 05.10.2004 langte die Erklärung zur Arbeitnehmerverlangung 2003 der Bf beim Finanzamt  ein und mit Einkommensteuerbescheid 2003 vom 13.10.2004 wurde eine Nachforderung in  Höhe von 2.076,56 € festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_7`)


stellt gem. Art 10 des gegenständlichen Abkommens eine Selbstanzeige dar, die  streifbefreiende Wirkung jedoch nur insoweit entfaltet, als die Besteuerungsgrundlagen  innerhalb einer vom Finanzamt gesetzten Frist offengelegt und die verkürzten Abgaben  rechtzeitig entrichtet werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_54`)


Der am 21. Jänner 2015 beim Finanzamt eingelangte – als Beschwerde bezeichnete –  Vorlageantrag war somit als verspätet zu werten und ist nach § 260 BAO Abs 1 BAO als nicht  fristgerecht eingebracht zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_16`)


Im Hinblick auf Sanierungsarbeiten an dem Gebäude ab  dem Jahr 2000 und auf die nunmehr ausschließlich unternehmerische Nutzung des Gebäudes  durch die revisionswerbende Partei machte sie u.a. für das Streitjahr 2009 eine anteilige  Vorsteuerberichtigung geltend, wobei dem Finanzamt eine detaillierte Berechnung des Anteils  der unternehmerischen Nutzung in den Jahren vor 2008 (Werte zwischen 24% und 42%)  übermittelt und die Berichtigung für den dem Anteil der hoheitlichen Nutzung entsprechenden  Teil der entrichteten Umsatzsteuer begehrt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_18`)


Dem Vorbringen einer teilweise unternehmerischen Nutzung des A-Hauses zur Zeit der  Sanierungsarbeiten (in der Größenordnung der vorgelegten und nur in Details beanstandeten  Berechnungen) trat das Finanzamt in dieser Auseinandersetzung nicht entgegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_22`)


Unter Verweis auf diese Ausführungen ließ das Finanzamt die beantragte Berichtigung im  Bescheid vom 25.03.2011 über die Umsatzsteuer für das Jahr 2009 unberücksichtigt, wogegen  die Bf. mit Schriftsatz vom 12.04.2011 Berufung erhob.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_24`)


Außenprüfung bei der Kommanditistin der Bf. hatte die Prüferin inzwischen festgehalten, die  Gemeinde habe im Zuge dieser Prüfung erstmals den anteiligen „Vorsteuerabzug für den  unternehmerisch genutzten Bereich des Amtsgebäudes“ geltend gemacht, und dieser stehe ihr  in näher dargestellter Höhe für die Prüfungsjahre 2006 bis 2008 auch zu.  In der Stellungnahme zur Berufung der Revisionswerberin legte das Finanzamt dar, es gehe  „von einer bloß anteiligen Zuordnung des Amtsgebäudes zum Unternehmen aus“, weil eine  „Zuordnung des nicht unternehmerisch genutzten Anteiles“ zum Unternehmen, anders als bei  der „klassischen privaten Nutzung“, nicht vorgesehen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_26`)


Das daran anschließende  Vorbringen, die behauptete Aufteilung des Gebäudes in einen hoheitlichen und einen  unternehmerischen Bereich sei nicht erfolgt, bezog sich nicht auf die tatsächliche Verwendung,  sondern auf die vom Finanzamt behauptete gänzliche Zuordnung zum Hoheitsbereich, die  damit begründet wurde, dass die Gemeinde bis zu der sie betreffenden Außenprüfung nie  Vorsteuern für das A-Haus geltend gemacht habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_30`)


Die Gemeinde habe davor nie Vorsteuern geltend gemacht,  weshalb das Finanzamt davon ausgehe, „dass das A-Haus ursprünglich nicht betrieblich  genutzt“ worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_31`)


Den nachträglichen Antrag, „für die betrieblich genutzten Teile“  Vorsteuern zu berücksichtigen, werte das Finanzamt als Mitteilung einer Zuordnung im Sinne  des § 12 Abs. 2 Z 1 lit. b UStG 1994.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

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

- `Bundesfinanzgericht`(organisation)
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

- `Bundesfinanzgericht`(organisation)
- `Dr. Alexander Hajicek`(person)
- `Mag. Helga Hochrieser`(person)
- `Mag. Michael Franz`(person)
- `Mag. Franz Josef Großin`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Tirol Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Dietlind Mahlstädt`(person)
- `Kai Pipers`(person)
- `Gottaweg 58, 9130 Annamischl, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamt Tirol Ost`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Reneé Dreyssig`(person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich`(address)
- `Mag. Manfred Frühwirth`(person)
- `Finanzamtes Linz`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_14`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 15. September 2019 wie  folgt:   I. Sachverhalt:   Ich habe am 05.04.2019 für meinen Sohn … ab dem Zeitraum April 2019 die Familienbeihilfe  beim zuständigen Finanzamt Gänserndorf Mistelbach beantragt, da dieser seit Mai 2019 eine  Berufsausbildung (bis Ende März 2019 Zivildienst) absolviert.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_17`)


III. Rechtsverletzung und Beschwerdegründe:   Der Abweisungsbescheid des Finanzamtes Gänserndorf Mistelbach vom 05.09.2019, (ohne) GZ,  verletzt mich in meinem subjektiven Recht.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_29`)


Das Finanzamt Gänserndorf Mistelbach hat unzutreffend und rechtswidrig eine  Ausbildungsphase der fremden- und grenzpolizeilichen exekutivdienstlichen Ausbildung, die  keinen Anspruch auf Familienbeihilfe begründet (weil das FLAG 1967 den Begriff der  Ausbildungsphase nicht kennt), bei der 24-monatigen durchgehenden Ausbildung meines  Sohnes … angenommen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Helge Göppele`(person)
- `GDJJ Versand`(organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich`(address)
- `Finanzamtes Graz`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Waldviertel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Eduard Lembrechts`(person)
- `Charles Rybalka`(person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich`(address)
- `Finanzamtes  Baden Mödling`(organisation)

</details>

---

## `City Authority - Stadt Wien` 🏆

**F1:** 0.014 | **Precision:** 0.511 | **Recall:** 0.007  

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
| 0.511 | 0.007 | 0.014 | 180 | 92 | 88 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 92 | 88 | 12518 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_12`)


Flora Thierry, in der Folge mit Bf. bezeichnet, wurde seitens des Magistrates der Stadt Wien,  Magistratsabteilung 67, aufgefordert zur Rechtfertigung hinsichtlich einer  Verwaltungsübertretung nach § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Flora Thierry` (person)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_26`)


Mit Straferkenntnis vom 13.3.2019, Zahl MA-ZAHL1, legte der Magistrat dem Bf. folgende  Verwaltungsübertretung nach § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zur Last:  Datum/Zeit:   19.7.2018, 21:07 Uhr  Ort:    1040, ABSTELLPLATZ1  Betroffenes Fahrzeug: Kennzeichen KENNZ1 (A)  Abstellen des Fahrzeuges in einer gebührenpflichtigen Kurzparkzone, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrat` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_141`)


Dabei wurde dem Bf.  folgende Verwaltungsübertretung nach § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zur Last gelegt:  11 von 34 Seite 12 von 34

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_247`)


Mit Straferkenntnis vom 14.5.2019, Zahl MA-ZAHL2, legte der Magistrat dem Bf. folgende  Verwaltungsübertretung nach § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zur Last:  Datum/Zeit:   4.7.2018, 12:51 Uhr  Ort:    1040, ABSTELLPLATZ2 NUMMER gegenüber  Betroffenes Fahrzeug: Kennzeichen KENNZ1 (A)  Abstellen des Fahrzeuges ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Magistrat` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_6`)


Verwaltungsübertretung(en) nach:  1. § 9 Abs. 2 Kontrolleinrichtungenverordnung, ABl. der Stadt Wien Nr. 33/2008, idgF, in  Verbindung mit § 4 Abs. 3 Parkometergesetz 2006, LBGl. für Wien Nr. 9/2006 in der geltenden  Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_823`)


Angesichts des letztzitierten Erkenntnis des Verwaltungsgerichtshofs in Verbindung mit dem  Bericht gemäß § 150 BAO betreffend die Abgaben für die Jahre 2012 bis 2016 war zu den im  Arbeitsbogen abgelegten Beweismittel, die dem Bericht gemäß § 150 BAO betreffend die  Abgaben für die Streitjahre zugrunde gelegen waren, festzustellen, dass dem von der  Betriebsprüfung zitierten Bericht im F-Magazin, erschienen im Compress-Verlag, insoweit  vorrangig Reklamecharakter zuzusprechen war, als das (Ende 2015 eingestellte)  Monatsmagazin in den das Beschwerdeverfahren betreffenden Streitjahren eine Publikation  jenes Compress-Verlages gewesen war, der für die Stadt Wien in den Streitjahren  Auslandsbüros in Europa betrieben hatte.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_824`)


Dieser Verlag war ein zentraler Bestandteil der  strategischen Führung der Stadt Wien im Rathaus, in deren Rahmen die Stadt Wien im  Rathaus nach innen und außen als dynamische Wirtschaftskraft erscheinen sollte.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_826`)


Dies stand ganz im Sinne des von der  Stadt Wien im Rathaus angestrebten Nutzens gegenüber der Bf., Wien in Europa auch als  Wirtschaftsstandort und Zielpunkt für Kosmopoliten zu porträtieren.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)


Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Rosalia Schmieter, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosalia Schmieter` (person)
- `Collmannstraße 3, 3335 Lindau, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_54`)


Hiezu wird Folgendes festgestellt:   Im Anlassfall liegt eine Anzeige eines Kontrollorganes der Stadt Wien vor und ist der  festgestellte Sachverhalt - der gar nicht bestritten wurde - klar umschrieben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Timon Thoennißen` (person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_7`)


§ 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_29`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, haben dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert ist  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien Nr.  33/2008).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_2`)


über die Beschwerde des Louisa Kannengiser, Pfaffensteig 10, 3595 Atzelsdorf, Österreich, vom 15. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. März 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016 in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise Folge gegeben als die von der belangten Behörde mit € 60,00 verhängte Geldstrafe  auf € 48,00 und die für den Fall der Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfrei- heitsstrafe auf 10 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Louisa Kannengiser` (person)
- `Pfaffensteig 10, 3595 Atzelsdorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache Aron Pommeränke,  Seenplattenweg 7, 4190 Oberstiftung, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit §  16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für  Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, über die  Beschwerde des Beschuldigten vom 26. Jänner 2021 gegen das Erkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 29. Dezember 2020, GZ. MA6/2019,  beschlossen:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 28 Abs. 1  VwGVG, § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG), § 13 Allgemeines  Verwaltungsverfahrensgesetz 1991 (AVG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird das Beschwerdeverfahren eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aron Pommeränke` (person)
- `Seenplattenweg 7, 4190 Oberstiftung, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_14`)


Er habe dadurch folgende Rechtsvorschriften verletzt:   1 – 5: § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes  (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt  Wien Nr. 52/2016, in Zusammenhalt mit § 9 Abs. 1 des Verwaltungsstrafgesetzes 1991 – VStG.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, vom 7. April 2021 gegen das Straferkenntnis des Magistrates der Stadt Wien vom 25.  Februar 2021, Zahl MA67/Zahl/2020,  betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016 in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, den Beschluss gefasst:  Die Beschwerde vom 7. April 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ivan Thöner` (person)
- `Landlerweg 28, 4273 Kaltenberg, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Theobald Atacan, Göschl 12, 3544 Eisenberg, Österreich, vom 22. November 2021, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 13. Oktober  2021, Zl. MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 3 Abs. 1  Kontrolleinrichtungenverordnung, Abl. der Stadt Wien Nr. 33/2018, idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF, zu Recht:  Die Beschwerde wird gemäß § 50 VwGVG in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Theobald Atacan` (person)
- `Göschl 12, 3544 Eisenberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_87`)


Mit ihrer keinesfalls als unbedeutend einzustufenden Tat gefährdete die Beschuldigte das  Interesse der Stadt Wien an der entsprechenden Parkraumbewirtschaftung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_2`)


Z1 und Z2,  wegen der Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl.  der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde stattgegeben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_13`)


2. In der Eingabe der Beschwerdeführerin vom 3. Februar 2022 wurde ausgeführt:  „Unsere Nachmieterin in der Wohnung in […], wo wir seit November 2021 nicht mehr gemeldet  sind hat uns mitgeteilt, dass ein Exekutor der Stadt Wien angeklopft habe.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_42`)


Als wir dann plötzlich von unseren Nachmietern darüber verständigt wurden, dass ein Exekutor  der Stadt Wien bei uns angeläutet hat, sind wir zunächst aus allen Wolken gefallen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Melinda Brotke` (person)
- `Jägerloch 26, 8443 Praratheregg, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_109`)


Verwaltungsübertretung nach § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 begangen hat.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_41`)


Auf der Homepage der Sozialwerke Clara Fey der Schwestern vom armen Kinde Jesus  http://www.sozialwerke-clara-fey.at/wohnen-kinder.html steht Folgendes:  „Diese Einrichtung arbeitet im Auftrag und mit Mitteln der Wiener Kinder- und Jugendhilfe“  sowie „Anerkannte Einrichtung nach den Förderrichtlinien des Fonds Soziales Wien, gefördert  aus Mitteln der Stadt Wien“.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Fonds Soziales Wien` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_42`)


Das Bundesfinanzgericht geht daher davon aus, dass der Unterhalt (die Kosten der  Unterbringung) zur Gänze von der Stadt Wien getragen wird, zumal im Antrag auf Gewährung  von Familienbeihilfe vom 23.12.2019 festgehalten wurde, dass der Stadt Wien täglich Kosten  von mindestens € 80,00 für den Mj. entstehen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_58`)


Der Kinder- und Jugendhilfe der Stadt Wien  entstehen Kosten von mindestens € 80 täglich.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_59`)


Der Unterhalt (die Kosten der Unterbringung) werden zur Gänze von der Kinder- und  Jugendhilfe der Stadt Wien getragen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_64`)


Dass der Kinder- und Jugendhilfe der Stadt Wien Kosten von mindestens € 80 täglich  entstehen, hat diese als Vertreter des Bf. selbst vorgebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_66`)


Dass der Unterhalt zur Gänze von der Kinder- und Jugendhilfe der Stadt Wien getragen wird,   ergibt sich aus der Homepage der Wohngemeinschaft und dem Vorbringen der Wiener Kinder-   und Jugendhilfe über die Kostentragung von mindestens € 80.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_67`)


Dass das BFG von diesem Sachverhalt ausgeht, wurde der Kinder- und Jugendhilfe der Stadt  Wien vorgehalten und blieb unwidersprochen.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_78`)


Angesichts des Umstandes, dass von der Kinder- und Jugendhilfe der Stadt Wien trotz  Aufforderung keinerlei Unterlagen vorgelegt wurden, und der im Vorhalt vom BFG auf Grund  der  Aktenlage angenommene und der Stadt Wien mitgeteilte Sachverhalt im Wesentlichen  unbestritten blieb, war von diesem Sachverhalt auszugehen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_86`)


Die Rechtsvertretung ist der Feststellung des Bundesfinanzgerichts im Vorhalt, wonach der  Unterhalt (die Kosten der Unterbringung) des Bf. zur Gänze von der Stadt Wien getragen wird,  in der Vorhaltsbeantwortung nicht entgegengetreten.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_96`)


Deswegen geht das Bundesfinanzgericht in freier Beweiswürdigung im vorliegenden Fall davon  aus, dass der Unterhalt bzw. die Kosten der Unterbringung des Bf. im Streitzeitraum zur Gänze  von der Stadt Wien getragen wurden.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_19`)


Mit Beschwerdevorentscheidung vom 09.01.2015 wurde die Beschwerde als unbegründet  abgewiesen und nach Zitat der Bezug habenden gesetzlichen Bestimmungen ausgeführt, aus  der Aktenlage sei kein Verschulden der Stadt Wien oder einer in ihrem Auftrag handelnden  Person ersichtlich, weshalb eine Herabsetzung der Wasserbezugsgebühr nicht möglich sei.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_26`)


Sie brachte ergänzend vor, es möge dahin gestellt bleiben, ob  bezüglich der offenbar nur zeitweisen Erhöhung des Wasserdrucks über die „Toleranzgrenze“  des Sicherheitsventils ein Verschulden der Stadt Wien oder handelnder Personen vorliege.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_45`)


Dass Wassermengen ohne Verschulden des Wasserabnehmers durch ein von der Stadt Wien  bzw. durch in ihrem Auftrag handelnde Personen verschuldetes Gebrechen an der  Wasserzähleranlage als verbraucht angezeigt wurden, kann nicht festgestellt werden.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_56`)


Zu Spruchpunkt I.  § 3 WVG lautet:  „Jeder Wasserabnehmer bzw. jede Wasserabnehmerin, für den bzw. die ein Anschluss an die  öffentlichen Wasserversorgungsanlagen der Stadt Wien hergestellt wurde, hat nach Maßgabe  der allgemeinen und örtlichen Versorgungslage Anspruch auf die Belieferung mit gesundheitlich  einwandfreiem Wasser.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_58`)


Das Wasser wird grundsätzlich über einen von der Stadt Wien beigestellten Wasserzähler  abgegeben, nach dessen Angaben die bezogene Wassermenge ermittelt wird.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_63`)


Der Wasserzähler bleibt  Eigentum der Stadt Wien und wird von ihr instandgehalten;

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_90`)


Der Gebührenpflicht unterliegt die unmittelbare oder mittelbare Einleitung von  Abwässern von innerhalb der Stadt Wien gelegenem Grundbesitz (§ 1 Grundsteuergesetz 1955)  in einen öffentlichen Straßenkanal.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_113`)


Gemäß § 11 Abs. 1 WVG ist bei Vorhandensein eines von der Stadt Wien bereitgestellten  (funktionstüchtigen) Wasserzählers die bezogene gebührenpflichtige Wassermenge nach den  Angaben des Wasserzählers, also durch Gegenüberstellung des am Wasserzähler  ausgewiesenen Standes bei der Ablesung mit dem Stand bei der letzten Ablesung zu ermitteln  (vgl. VwGH 28.2.1986, 84/17/0070;

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_133`)


Das Vorbringen der Beschwerdeführerin, das defekte Sicherheitsventil sei auf einen erhöhten  Wasserdruck zurückzuführen, lässt keinen Schluss auf ein Verschulden der Stadt Wien bzw.  einer in ihrem Auftrag handelnden Person zu, da im oben zitierten § 3 WVG ausdrücklich  bestimmt wird, dass die Wasserabnehmerin keinen Anspruch auf eine bestimmte  Wasserbeschaffenheit oder einen bestimmten Wasserdruck hat.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Wladimir Leukhardt` (person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich` (address)
- `Bundesfinanzgerichts` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_125`)


BFG 24.07.2020, RV/7500049/2020, s. auch die  Homepage der Stadt Wien, https://www.stadt-wien.at/wien/parken-in- wien/handyparken.html, welche zum Parken in Wien hilfreiche Informationen enthält).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Techn R Christina Heising, Angerweg 46, 4672 Unterseling, Österreich, vom 13. Februar 2023, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner 2023, Zahl MA67/Zahl1/2022, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für  Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Techn R Christina Heising` (person)
- `Angerweg 46, 4672 Unterseling, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_12`)


Auch der Online-Stadtplan der Stadt Wien zeige für die besagte Adresse eindeutig das  Bestehen der Überlappungszone.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_13`)


Der Vorhalt des zuständigen Mitarbeiters der Stadt Wien, es  seien an dieser Adresse nur das Haus und der Gehsteig Teil der Zone, nicht aber die  Parkflächen, sei als unsachlich zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_49`)


Auch der Online-Stadtplan der Stadt Wien zeigt für die besagte Adresse  eindeutig das Bestehen der Überlappungszone (Beweis: siehe Anhang, erneut abgerufen am  13.2.2023, https://www.wien.gv.at/stadtplan/grafik.aspx?Iang=de-AT&bookmark- NIMgRliNGUbHotdFXEw2Re5RphIRVXXeKGeqeeS6vakfe6mv).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_50`)


Der Vorhalt des zuständigen  Mitarbeiters der Stadt Wien, es seien an dieser Adresse nur das Haus und der Gehsteig Teil der  Zone, nicht aber die Parkflächen, ist als unsachlich zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_79`)


Daher war festzuhalten, dass der Bf. sein Fahrzeug in einer ordnungsgemäß kundgemachten  Kurzparkzone ohne gültig entwerteten Parkschein abgestellt hat und daher eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 begangen hat.

| Predicted | Gold |
|---|---|
| `Stadt  Wien` | `Stadt  Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_3`)


Nr. 10/2013 über die Beschwerden des Beschuldigten vom 10. Juni  2019 gegen  1. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 13. März 2019,  Zahl MA-ZAHL1 sowie  2. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 14. Mai 2019,  Zahl MA-ZAHL2  zu Recht erkannt:  I. Gemäß § 50 in Verbindung mit § 38 VwGVG und § 45 Abs. 1 zweiter Satz VStG wird von der  Verhängung einer Strafe abgesehen und der beschwerdeführenden Partei unter Hinweis auf  die Rechtswidrigkeit ihres Verhaltens eine Ermahnung erteilt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die der  Beschwerdeführer keinen Beitrag zu den Kosten des verwaltungsgerichtlichen Strafverfahrens  zu tragen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_8`)


Mit Schreiben des Magistrates der Stadt Wien vom 2.11.2018 betreffend Lenkererhebung  wurde VN4 NN als Zulassungsbesitzerin des Kraftfahrzeuges mit dem behördlichen  Kennzeichen KENNZ1 gemäß § 2 des Parkometergesetzes 2006, LBGl. für Wien Nr. 9/2006 in  der geltenden Fassung aufgefordert, der Behörde schriftlich Auskunft darüber zu erteilen, wem  sie das Kraftfahrzeug mit dem oben genannten Kennzeichen in 1040 Wien, ABSTELLPLATZ1  überlassen gehabt habe, sodass es dort am 19.7.2018 um 21:07 Uhr gestanden sei.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_12`)


Flora Thierry, in der Folge mit Bf. bezeichnet, wurde seitens des Magistrates der Stadt Wien,  Magistratsabteilung 67, aufgefordert zur Rechtfertigung hinsichtlich einer  Verwaltungsübertretung nach § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Flora Thierry`(person)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_133`)


in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_134`)


in eventu  der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, dahin abzuändern, dass eine Ermahnung ausgesprochen  wird."  ad 2.:  Mit Schreiben des Magistrates der Stadt Wien vom 31.10.2018 betreffend Lenkererhebung  wurde VN4 NN als Zulassungsbesitzerin des Kraftfahrzeuges mit dem behördlichen  Kennzeichen KENNZ1 gemäß § 2 des Parkometergesetzes 2006, LBGl. für Wien Nr. 9/2006 in  der geltenden Fassung aufgefordert, der Behörde schriftlich Auskunft darüber zu erteilen, wem  sie das Kraftfahrzeug mit dem oben genannten Kennzeichen in 1040 Wien, ABSTELLPLATZ2  gegenüber NUMMER, überlassen gehabt habe, sodass es dort am 4.7.2018 um 12:51 Uhr  gestanden sei.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_137`)


Mit Schreiben des Magistrates der Stadt Wien vom 17.1.2019 betreffend Lenkererhebung  wurde der Bf. als jene Person, die das ihr von der Zulassungsbesitzerin des Kraftfahrzeuges mit  dem behördlichen Kennzeichen KENNZ1 zur Verfügung gestellte Fahrzeug einem dritten  überlassen hat, gemäß § 2 des Parkometergesetzes 2006, LBGl. für Wien Nr. 9/2006 in der  geltenden Fassung aufgefordert, der Behörde schriftlich Auskunft darüber zu erteilen, wem er  das Kraftfahrzeug mit dem oben genannten Kennzeichen in 1040 Wien, ABSTELLPLATZ2  NUMMER, gegenüber überlassen gehabt habe, sodass es dort am 4.7.2018 um 12:51 Uhr  gestanden sei.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_358`)


Der Beschwerdeführer stellt daher den  A N T R A G,  1. in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_359`)


in eventu  der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, dahin abzuändern, dass eine Ermahnung ausgesprochen  wird."

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, GZ. MA-Zahl1,  vom 2.4.2019 wurde über Dagmar Gärttner, Bakk. art., in der Folge kurz mit Bf. bezeichnet, eine Geldstrafe von  60,00 Euro, im Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden wegen  folgender Verwaltungsübertretung verhängt:  Datum/Zeit:   1.2.2019, 9:57 Uhr  Ort:    1050 Wien, Wiedner Hauptstraße 112  Betroffenes Fahrzeug: Kennzeichen: KFZ-Kennz  Sie haben das mehrspurige Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone abgestellt,  wobei elektronische Parkscheine mit einer fünfzehn Minuten nicht übersteigenden Abstellzeit  unmittelbar aufeinander folgend aktiviert wurden.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dagmar Gärttner, Bakk. art.`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_81`)


Über die Beschwerde wurde erwogen:  Sachverhalt und Beweiswürdigung:  Über die Bf. wurde mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67  vom 2.4.2019 zur GZ. MA-Zahl1 wegen des unter dem Punkt "Verfahrensgang" angeführten  Deliktes eine Geldstrafe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe in Höhe von 14 Stunden verhängt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_138`)


Bei dem Schreiben vom 31.7.2019 handelt es sich um den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, mit welchem der Einspruch gegen die  Strafverfügung vom 2.4.2019 als verspätet zurückgewiesen wurde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)


Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Rosalia Schmieter, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rosalia Schmieter`(person)
- `Collmannstraße 3, 3335 Lindau, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gertraud Hausherr`(person)
- `Bernhard Habdank`(person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Bernhard Habdank`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Puntigam`(person)
- `Jaden Holzfuss`(person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter[...] in der Verwaltungsstrafsache gegen  Niklas Radschweit, Kaiserfeld 4, 8673 Steinhöf, Österreich, wegen der Verwaltungsübertretungen gemäß § 16 Abs. 1 des  Wiener Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBI. für Wien Nr. 20, in der  Fassung des LGBI. Nr. 71/2018 in der Fassung des LGBl für Wien Nr. 50/2013 in Verbindung mit  § 1 Abs. 1 GAG und Tarifposten B 1 und B 8 über die Beschwerde der Beschuldigten vom  15.11.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 -  Abgabenstrafen, vom 20.10.2020, Zahl: MA6/[...], zu Recht erkannt:  I.) Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2 VStG eingestellt.   II.) Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Niklas Radschweit`(person)
- `Kaiserfeld 4, 8673 Steinhöf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_4`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 - Abgabenstrafen,  vom 20.11.2020, Zahl: MA6/[...], wurde der nunmehrige Beschwerdeführer [...] (in weiterer  Folge kurz Bf. genannt) der Verwaltungsübertretungen gemäß § 16 Abs. 1 des Wiener  Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBI. für Wien Nr. 20, in der Fassung des  LGBI. Nr. 71/2018 in der Fassung des LGBl für Wien Nr. 50/2013 in Verbindung mit § 1 Abs. 1  GAG und Tarifposten B 1 und B 8 für schuldig befunden,   1. Datum: 20.11.2018  Ort: [...] (Front [...])   1 von 13 Seite 2 von 13

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_126`)


Nach Überprüfung seitens der MA 37 am 12.11.2018 wurde der Bf. mit Bescheid des  Magistrates der Stadt Wien, MA 37-[...], vom 16.11.2018 aufgetragen, binnen zwei Monaten,  die unter dem Gehsteig (= öffentliches Gut) befindliche Füllstelle und Füllleitung zu entfernen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_127`)


Mit Bescheid des Magistrates der Stadt Wien vom 20.11.2018, MA 46-[...], erfolgte die  Festsetzung der Gebrauchsabgabe für die Jahre 2013-2018 für eine Rohrleitung und einen  Einfüllschacht in Höhe von insgesamt € 179,40  Der Umstand, dass der Öleinfüllschacht sowie die Rohrleitung nicht mehr zur Betankung einer  Ölfeuerungsanlage verwendet worden sind, ist für das Entstehen der Verpflichtung zur  Entrichtung der Gebrauchsabgabe nicht maßgeblich, da der Tatbestand des § 9 Abs. 1a GAG  auf die Nutzung des öffentlichen Grundes abstellt. Der öffentliche Grund wurde im  Beschwerdefall aber durch die Anbringung und das fortgesetzte Bestehen von besagtem  Öleinfüllschacht samt Rohrleitung, also durch die Gebrauchsarten der Tarifpost B 1 und der  Tarifpost B 8, im Sinne des GAG 1966 benutzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_3`)


über die Beschwerde des Bf., Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich  vom 19. Februar 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 20. Jänner 2021, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_2`)


über die Beschwerde des Louisa Kannengiser, Pfaffensteig 10, 3595 Atzelsdorf, Österreich, vom 15. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. März 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016 in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise Folge gegeben als die von der belangten Behörde mit € 60,00 verhängte Geldstrafe  auf € 48,00 und die für den Fall der Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfrei- heitsstrafe auf 10 Stunden herabgesetzt wird.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Louisa Kannengiser`(person)
- `Pfaffensteig 10, 3595 Atzelsdorf, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)


über die Beschwerde der Balthasar Brendtke, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Balthasar Brendtke`(person)
- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Evelyn Antwerber`(person)
- `Hertzstraße 25, 5134 Spieglern, Österreich`(address)
- `Dr. Farid Rifaad`(person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_8`)


jeweils wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, nach  Durchführung einer mündlichen Verhandlung am 12. April 2021 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  werden die sechs Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_120`)


3. Zulässigkeit der Beschwerde:  Gegen das jeweils erlassene Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, ist gemäß Art. 130 Abs. 1 Z 1 B-VG die Beschwerde an das gemäß  Art. 131 Abs. 1 B-VG iVm § 3 Abs. 2 Z 1 letzter Fall VwGVG zuständige Verwaltungsgericht  zulässig.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache Aron Pommeränke,  Seenplattenweg 7, 4190 Oberstiftung, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit §  16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für  Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, über die  Beschwerde des Beschuldigten vom 26. Jänner 2021 gegen das Erkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 29. Dezember 2020, GZ. MA6/2019,  beschlossen:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 28 Abs. 1  VwGVG, § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG), § 13 Allgemeines  Verwaltungsverfahrensgesetz 1991 (AVG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird das Beschwerdeverfahren eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Aron Pommeränke`(person)
- `Seenplattenweg 7, 4190 Oberstiftung, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, vom 7. April 2021 gegen das Straferkenntnis des Magistrates der Stadt Wien vom 25.  Februar 2021, Zahl MA67/Zahl/2020,  betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016 in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, den Beschluss gefasst:  Die Beschwerde vom 7. April 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ivan Thöner`(person)
- `Landlerweg 28, 4273 Kaltenberg, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 25. Februar 2021, Zahl MA67/Zahl,  wurde der nunmehrige Beschwerdeführer (Bf.) Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, bestraft, weil er das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 02.11.2020 um  10:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Beheimgasse gegenüber 32  abgestellt habe, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Ivan Thöner`(person)
- `Landlerweg 28, 4273 Kaltenberg, Österreich`(address)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_15`)


Mit Vorhalt (Beschluss) des Bundesfinanzgerichtes vom 26. April 2021 wurde der Bf. innerhalb  einer Frist von zwei Wochen ab Zustellung dieses Beschlusses aufgefordert, die nachstehenden  Verfahrenshandlungen vorzunehmen:   „Mit E-Mail vom 07. April 2021 wurde seitens des Beschwerdeführers gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 25. Februar 2021, Zahl MA67/Zahl/2020, Beschwerde  erhoben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hilde Schorpp`(person)
- `Wandschaml 94, 4625 Grub, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_3`)


über die Beschwerde des Ludmilla Czimmerninks,  Sennemahd 7, 9832 Latzendorf, Österreich, vom 30. Juni 2021, gegen den Bescheid des Magistrates der Stadt Wien,  Magistratsabteilung 6, vom 7. Juni 2021, GZ. MA67/Zahl/2020, betreffend Abweisung des  Antrages vom 14. Mai 2021 auf Bewilligung eines Zahlungsaufschubes bzw. Ratenansuchens,  nach Durchführung einer mündlichen Verhandlung am 2. September 2021, in Anwesenheit des  Beschwerdeführers und der Schriftführerin IP, zu Recht erkannt:  Die Beschwerde wird gemäß § 50 VwGVG als unbegründet abgewiesen und der ange- fochtene Bescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ludmilla Czimmerninks`(person)
- `Sennemahd 7, 9832 Latzendorf, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 6`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Theobald Atacan, Göschl 12, 3544 Eisenberg, Österreich, vom 22. November 2021, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 13. Oktober  2021, Zl. MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 3 Abs. 1  Kontrolleinrichtungenverordnung, Abl. der Stadt Wien Nr. 33/2018, idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF, zu Recht:  Die Beschwerde wird gemäß § 50 VwGVG in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `Theobald Atacan`(person)
- `Göschl 12, 3544 Eisenberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Juliana Fassmer`(person)
- `Tillisweg 11, 8773 Sparsbach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_3`)


Begründung  1.a. Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 11. März  2021, Zahl: MA67/216700111216/2021, wurde Frau MedR Uwe Vaculik (in weiterer Folge:   Beschwerdeführerin) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung 2006 für schuldig erkannt und über sie nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer   Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `MedR Uwe Vaculik`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_9`)


Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 2. April  2021, Zahl: MA67/216700103138/2021, wurde die Beschwerdeführerin der Begehung einer  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung 2006 für  schuldig erkannt und über sie nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Henriette Pöpken, Stromsiedlung IV.R 11, 8510 Neurath, Österreich, Deutschland, vom 22. Mai 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. April 2022, Zl. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz  2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Renate Schohaj`(person)
- `Henriette Pöpken`(person)
- `Stromsiedlung IV.R 11, 8510 Neurath, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Roland Rößle, Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich, über die Beschwerde des  Beschuldigten vom 7. April 2022 gegen den Zurückweisungsbescheid des Magistrates der Stadt  Wien vom 5. April 2022, Zahl: MA67/216700658355/2021, mit dem der Einspruch vom 18.  Februar 2022 gegen die Strafverfügung vom 3. September 2021 mit derselben Geschäftszahl  gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Roland Rößle`(person)
- `Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Magistrates der Stadt  Wien`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Roland Rößle`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_26`)


Nach dem im Akt aufliegenden Zustellnachweis (AS 15) hat ein Mitbewohner an der  Abgabestelle des Beschwerdeführers die Strafverfügung des Magistrates der Stadt Wien vom  3. September 2021, Zahl: MA67/216700658355/2021, am 12. Oktober 2021 übernommen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Melinda Brotke`(person)
- `Jägerloch 26, 8443 Praratheregg, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt  Wien`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elvira Akcakaya`(person)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Waiser`(person)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_4`)


Verfahrensgang    Für den mj. Beschwerdeführer (Bf.), geb. am tt.mm.2009, wurde durch den Vormund Wiener   Kinder und Jugendhilfe, Magistratsabteilung 11 des Magistrates der Stadt Wien, am 18.12.2019  ein Antrag auf Gewährung der Familienbeihilfe rückwirkend ab Jänner 2016 gestellt.    Mit Bescheid vom 25. Februar 2020 wurde der Antrag vom 23.12.2019 auf Familienbeihilfe für  den mj. OSR Eugenia Balikci  den Zeitraum ab Jänner 2016 abgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `OSR Eugenia Balikci`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde der Adriana Wottge,  Ferstelgasse 22, 3282 Forsthub, Österreich, vom 20. Juli 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 14. Juli 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Adriana Wottge`(person)
- `Ferstelgasse 22, 3282 Forsthub, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Chantal Franzk,  Feldererweg 14 - 20, 5166 Rudersberg, Österreich, vom 14. Juni 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 31. Mai 2022, GZ MA 67/Z2/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit §  4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Berufungsverhandlung am 19. September 2022, im  Beisein der Schriftführerin IP, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chantal Franzk`(person)
- `Feldererweg 14 - 20, 5166 Rudersberg, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_60`)


BESCHWERDEANTRAG  es wolle meiner Beschwerde gegen das Straferkenntnis des Magistrates der Stadt Wien, MA 67,  vom 31.05.2022 Folge gegeben werden, dieses behoben und das Verwaltungsstrafverfahren  eingestellt werden.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Magdalena Unterreiter`(person)
- `Anichstraße 5, 8953 Donnersbach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_28`)


Im gegenständlichen Verfahren wird Ihnen nicht die Abstellung des Fahrzeuges an sich  vorgeworfen, sondern der Umstand, dass einem Auskunftsbegehren des Magistrates der Stadt  Wien innerhalb der gesetzlichen Frist von zwei Wochen nicht entsprochen wurde.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt  Wien`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  OMedR Tanja Kubatsch, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `OMedR Tanja Kubatsch`(person)
- `Sand/Bundesstraße 2, 4170 Damreith, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/139260.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139260.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache Univ.-Prof. RgR Werner Burkholdt,  Am Thalbach 7, 6075 Tulfes, Österreich, über die Beschwerde des Beschuldigten vom 21. November 2022 gegen die  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 5. Oktober  2022, GZlen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. RgR Werner Burkholdt`(person)
- `Am Thalbach 7, 6075 Tulfes, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde des  Lubomir Vaist, Sulzbachfelderstraße 3, 9361 Judendorf, Österreich, vom 4. Jänner 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 12. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Lubomir Vaist`(person)
- `Sulzbachfelderstraße 3, 9361 Judendorf, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Annette Preußing`(person)
- `Am Neufeldersee 40, 3385 Uttendorf, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl  MA67/Zahl/2022, wurde Herr Annette Preußing (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Annette Preußing`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_22`)


Nach dem im Akt aufliegenden Zustellnachweis (AS 16/34) hat der Beschwerdeführer die  Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl MA67/Zahl/2022,  persönlich am 10. November 2022 übernommen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Techn R Christina Heising, Angerweg 46, 4672 Unterseling, Österreich, vom 13. Februar 2023, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner 2023, Zahl MA67/Zahl1/2022, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für  Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates  der Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates  der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Techn R Christina Heising`(person)
- `Angerweg 46, 4672 Unterseling, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Verwaltungsstrafsache gegen Susette Jungabel, Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 17. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. Februar 2023, GZ.  MA67/Zahl/2022,zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Susette Jungabel`(person)
- `Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

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
| `organisation` | 0 | 0 | 12610 |

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
| `organisation` | 0 | 0 | 12610 |

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
| `organisation` | 0 | 0 | 12610 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (2803, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des **FA Spittal Villach** (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

- missed: `FA Spittal Villach` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamt  Österreich`

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_307`)

Überdies ist er als zweiter Geschäftsführer der Firma **Starnberg Beratung GmbH** sowieso in das  Abgabenverfahren involviert, weil für das Gebaren der Gesellschaft mitverantwortlich.

- missed: `Starnberg Beratung GmbH` (organisation)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_6`)

Das **Finanzamt Wien 2/20/21/22** (=belangte Behörde) erließ an den Bf. den angefochtenen, mit  14. April 2020 datierten Einkommensteuerbescheid 2019, welcher eine Gutschrift aus der  Arbeitnehmerveranlagung in Höhe von 467,00 € auswies, d.h. die Einkommensteuer wurde für  2019 mit -467,00 € festgesetzt.

- missed: `Finanzamt Wien 2/20/21/22` (organisation)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_26`)

Mit 27.01.2016 ist die Körperschaftsteuererklärung 2014 elektronisch beim **Finanzamt Wien  12/13/14 Purkersdorf** eingelangt.

- missed: `Finanzamt Wien  12/13/14 Purkersdorf` (organisation)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_112`)

Die Schaffung  eines **Finanzamtes Österreichs** einerseits bzw. des Finanzamtes für Großbetriebe andererseits  als Folge der Modernisierung der Finanzverwaltung stellen jedoch weder einen Fall der  Übertragung der Zuständigkeit gemäß § 57 BAO, noch einen solchen des Überganges der  Zuständigkeit nach § 58 BAO dar.

- missed: `Finanzamtes Österreichs` (organisation)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_302`)

Gesellschafter-Geschäftsführer **Steblein Wind GmbH2.6.2021**, S. 5, 11 und  12).

- missed: `Steblein Wind GmbH2.6.2021` (organisation)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des **Magistrates der Stadt Wien, Magistratsabteilung 67** vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Stadt Wien`, `Stadt Wien`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_185`)

**Burglechner Touristik GmbH & Co KG**  Der Geschäftssitz der WienElektro GmbH & Co KG befand sich seit dem 2.

- missed: `Burglechner Touristik GmbH & Co KG` (organisation)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_62`)

Für die Einschätzung des Grades der Behinderung  sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des **Bundesministers für Arbeit, Soziales und  Konsumentenschutz** betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

- missed: `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_202`)

Zum Zeitpunkt der Einfuhr von Geräten, welche im Eigentum der  Finanzamt Spittal Villach  in Amberg  oder Struden  bzw. Finanzamt Graz-Stadt  standen, war die Firma  **RHO Pharma** Lamperstätten  nicht der usti Verfügungsberechtigte und somit vom Vorsteuerabzug  ausgeschlossen.

- missed: `RHO Pharma` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des **Finanzamtes Wien 1/23** vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Finanzamtes Wien 1/23` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_54`)

Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des **Bundesministers für Arbeit, Soziales und  Konsumentenschutz** betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

- missed: `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_58`)

Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des **Wiener Gemeinderates**, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  4 von 9 Seite 5 von 9

- missed: `Wiener Gemeinderates` (organisation)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_111`)

Der Bf hat für dieses Fahrzeug  ab 1.11.2008 bei der X-Versicherung eine Vollkaskoversicherung abgeschlossen, die am  1.11.2009 storniert wurde (Angaben der X-Versicherung lt. Erhebung der **Finanzpolizei**; eigene  Angaben lt. Niederschrift).

- missed: `Finanzpolizei` (organisation)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_76`)

Die Kunden der **VWWJ IT GmbH** sind zu 40 % in Österreich  angesiedelt, der Rest im Süddeutschen bzw. Südtiroler Raum.

- missed: `VWWJ IT GmbH` (organisation)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)

IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim **Finanzamt  Wien 9/18/19** Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

- missed: `Finanzamt  Wien 9/18/19` (organisation)
- predicted in sentence: `Bundesfinanzgerichtes`, `Finanzamt  Wien 9/18/19 Klosterneuburg`, `Finanzamtes Wien 9/18/19 Klosterneuburg`, `Finanzamt Wien 9/18/19 Klosterneuburg`

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_215`)

Vorlageantrag 23.7.2018, S. 3-5; StB **lt.Steblein Wind GmbH2.6.** S 3  16 von 38 Seite 17 von 38

- missed: `lt.Steblein Wind GmbH2.6.` (organisation)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_457`)

Zurechnung der Einkünfte im ursächlichen Zusammenhang mit dem Managementvertrag  zwischen der Rusnok IT GmbH und der OG an die OG  Die **Rusnok IT GmbH** schloss ebenso wie alle anderen Konzerngesellschaften (siehe oben Pkt 1) mit der  OG einen Managementvertrag (2006), auf Grund dessen die OG durch ihre Gesellschafter alle  Konzerngesellschaften, darunter auch die Rusnok IT GmbH  lenkte, überwachte und unterstützte.

- missed: `Rusnok IT GmbH` (organisation)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_63`)

Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der **Möhlmeyer Immobilien GmbH** als Gruppenträgerin war, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

- missed: `Möhlmeyer Immobilien GmbH` (organisation)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_14`)

Die Bf stellte daraufhin durch die Erwachsenenvertretung B. den Antrag die Beschwerde dem  **Bundesfinanzgericht (BFG)** zur Entscheidung vorzulegen (siehe dazu Vorlageantrag vom  27.04.2024).

- missed: `Bundesfinanzgericht (BFG)` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `BFG`

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)

Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von Josefine Frikel (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der **Verwaldgart GmbH** bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

- missed: `Verwaldgart GmbH` (organisation)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_20`)

Im Zuge der Darlegung des Verfahrensganges erläutert die Bf., dass sie am 21. Februar 2018  von Seiten der **WGKK** rückwirkend für den Zeitraum 1. September 2016 bis 31. Jänner 2018,  somit für die 3 betroffenen Jahre 2016 bis 2018 eine Zahlung i.H.v. € 15.333,52 erhalten habe.

- missed: `WGKK` (organisation)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_35`)

folgende Stellungnahme abzugeben:  Ehepaar D, Kinder von Y und Z D, Baumschule D erwarben mit Kaufvertrag vom 10.9.2012 von  der **M Containerbaumschule GmbH & Co KG** die ehemalige Betriebsliegenschaft samt  Folienhäuser, Folientunnel und Teile der Bewässerungsanlagen.

- missed: `M Containerbaumschule GmbH & Co KG` (organisation)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/148387.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148387.1_9`)

Zudem benötige sie eine neue Brille um  rd. € 1.000,00, ohne die sie nicht arbeiten könne und deren Kosten weder die **ÖGK** übernehme  1 von 5 Seite 2 von 5

- missed: `ÖGK` (organisation)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_202`)

Zum Zeitpunkt der Einfuhr von Geräten, welche im Eigentum der  Finanzamt Spittal Villach  in Amberg  oder Struden  bzw. **Finanzamt Graz-Stadt**  standen, war die Firma  RHO Pharma Lamperstätten  nicht der usti Verfügungsberechtigte und somit vom Vorsteuerabzug  ausgeschlossen.

- missed: `Finanzamt Graz-Stadt` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139968.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139968.1_30`)

Für Kinder, die sich ständig außerhalb eines Mitgliedstaates der Europäischen Union, eines  Staates des Europäischen Wirtschaftsraumes oder der Schweiz aufhalten, steht kein  Kinderabsetzbetrag zu.  2. Für Kinder, die sich ständig in einem anderen Mitgliedstaat der EU oder Hoheitsgebiet einer  anderen Vertragspartei des Abkommens über den Europäischen Wirtschaftsraum oder der  Schweiz aufhalten, ist die Höhe des Kinderabsetzbetrages auf Basis der vom Statistischen Amt  der **Europäischen Union** veröffentlichten vergleichenden Preisniveaus für jeden einzelnen  Mitgliedstaat der EU, jede Vertragspartei des Europäischen Wirtschaftsraumes und die Schweiz  im Verhältnis zu Österreich zu bestimmen:  a)

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_234`)

Fazit: Die Ansicht (NiS. 2.6.Kämpker&Mooslechner Holz GmbHS. 6 -9), nur beratende Tätigkeiten der Strategen im  Namen der OG beruhten auf dem Managementvertrag , und die lenkenden und  überwachenden , dh geschäftsführenden Tätigkeiten der Strategen seien nicht auf Grund des  Managementvertrages erfolgt und auch nicht auf der Grundlage des Managementvertrages  oder sonstwie abgegolten worden, ist nicht überzeugend, weil   -der StB selbst die Lenkungs- und Überwachungstätigkeiten der Strategen im Zusammenhang  mit den Managementverträgen erwähnt hat (Schreiben des Steuerberaters vom 22.9.2016),  - weil man die Tätigkeiten der Strategen, die dem Konzern, bestehend aus den  Konzerngesellschaften, gedient haben (Lenkungs- Überwachungstätigkeiten, sonstige  unterstützende Tätigkeiten wie z.B. Beratungen lt. Vorlageantrag S. 3-5, lt. Schreiben des   Steuerberaters vom 22.9.2016, lt **Unilemder-Versand GmbH2.6.2021**, S. 7 und lt. Gesellschafter- Geschäftsführer Steblein Wind GmbH2.6. S. 11 und 12) nicht trennen kann.

- missed: `Unilemder-Versand GmbH2.6.2021` (organisation)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_46`)

Zu den beim Sozialministeriumservice (SMS) bisher vom FAÖ angeforderten Gutachten/  Bescheinigungen (werden vom **FAÖ** gesondert übermittelt):  a) Gestützt auf mehrere Vorgutachten/relevante Befunde kommt SV Dr.in C im SMS-Gutachten  v. 2.2./5.2.2022 zum Ergebnis, dass der Sohn der Bf ab Geburt blind ist und ein GdB von 100 %  vorliegt (Anm.: richtiges Datum zu "GdB liegt vor seit" wäre: 07/1998).

- missed: `FAÖ` (organisation)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_856`)

C-593/19, „**SK Telecom**“, Rn. 3 angegebenen unionsrechtlichen Rahmen):  „Sämtliche Telekommunikationsdienstleistungen, die in der Europäischen Union in Anspruch  genommen werden, sollten besteuert werden, um Wettbewerbsverzerrungen in diesem Bereich  vorzubeugen.

- missed: `SK Telecom` (organisation)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch **Rein & Partner Steuerberatung GmbH & Co KG** in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

- missed: `Rein & Partner Steuerberatung GmbH & Co KG` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes`, `Finanzamt Österreich`

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_25`)

Der Verwaltungsgerichtshof hat sehr deutlich den Unterschied der im Bereich des  Bundesministeriums für Inneres vorhandenen exekutivdienstlichen Ausbildungen  aufgearbeitet:   Zur Verdeutlichung werden die Unterschiede der Ausbildungslaufbahn der ‘Grenzpolizisten‘  jenen der ‘Polizisten‘ (Exekutivdienst) überblicksmäßig gegenübergestellt:   Fremden- u. grenzpolizeilicher Exekutivdienst   (Erlass des BMI-SI1400/1082-SIAK-ZGA/2015  vom 09.12.2015)   Grundausbildung für den Exekutivdienst   (Verordnung des Bundesministers für Inneres über  die Grundausbildungen für den Exekutivdienst -   Grundausbildungsverordnung - Exekutivdienst **BMI**,  BGBl. II Nr. 153/2017)   Basisausbildung: 6 Monate (Lehrplan,  Stundentafel - Unterrichtseinheiten 880,  mündliche Prüfung, Zeugnis), Entgelt: 50,29%  des Referenzbetrages (§ 3 Abs. 4 GG)   Basisausbildung: 12 Monate (Lehrplan,  Stundentafel)   Entgelt: 50,29% des Referenzbetrages (§ 3  Abs. 4 GG) während der gesamten Ausbildung   Kursunterbrechung - Verwendung im  fremden- und grenzpolizeilichen Bereich   sowie Unterstützung im  sicherheitspolizeilichen Bereich   Entgelt: SONDERBESTIMMUNGEN -  Normalentgelt Exekutivdienstliche Zulagen  und Nebengebühren   Berufspraktikum I - 3 Monate   Kennenlernen des Dienstbetriebes ...

- missed: `BMI` (organisation)
- predicted in sentence: `Verwaltungsgerichtshof`

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_48`)

Die Vorgangsweise, die  erste Lieferung (zwischen **Möbel Zorkelglanz GmbH** und Bf.) als ruhend zu behandeln und die zweite Lieferung  zwischen der Bf. und deren Abnehmer als bewegte Lieferung zu sehen, sei richtig.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_72`)

**Wiener  Gemeindebezirk** gelegen sind, als Teil dieser Kurzparkzonen.

- missed: `Wiener  Gemeindebezirk` (organisation)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_23`)

Gemäß § 1 Abs. 1 BAO gelten die Bestimmungen der Bundesabgabenordnung in  Angelegenheiten der öffentlichen Abgaben (mit Ausnahme der Verwaltungsabgaben des  Bundes, der Länder und der Gemeinden) sowie der auf Grund unmittelbar wirksamer  Rechtsvorschriften der **Europäischen Union** zu erhebenden öffentlichen Abgaben, in  Angelegenheiten der Eingangs- und Ausgangsabgaben jedoch nur insoweit, als in den  2 von 5 Seite 3 von 5

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: **FA Österreich**) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `FA Österreich` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes`

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_471`)

Das Bundesfinanzgericht ist durch die Mitgliedschaft Österreichs zur Europäischen Union auch  ein Gericht der **Europäischen Union** und daher an die Rsp des EuGH gebunden.

- missed: `Europäischen Union` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_169`)

2.)Gründung der bf Jeremias Stuck (Firmenbuchauszug **Rusnok IT GmbH**  Die Rusnok IT GmbH wurde am 4.8.2005 gegründet.

- missed: `Rusnok IT GmbH` (organisation)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_52`)

7.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der **SUVA** bezogenen Invalidenrente fest.

- missed: `SUVA` (organisation)
- predicted in sentence: `Finanzamt`

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_184`)

Die tatsächlichen Urheber der bei der Firma **Starnberg Beratung GmbH** aufliegenden Scheinrechnungen  konnten im Prüfungsverfahren mangels entsprechend zweckdienlicher Auskünfte durch die  Geschäftsleitung nicht in Erfahrung gebracht werden.

- missed: `Starnberg Beratung GmbH` (organisation)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_15`)

Dies ergibt sich aus den  vorgelegten Bestätigungen der auszahlenden liechtensteinischen Stellen und aus dem von der  **Pensionsversicherungsanstalt** übermittelten Lohnzettel.

- missed: `Pensionsversicherungsanstalt` (organisation)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_40`)

Zur Amtpartei ab 01.01.2021:  Gemäß § 323b Abs.1 BAO treten das Finanzamt Österreich und das **Finanzamt für Großbetriebe**  für ihren jeweiligen Zuständigkeitsbereich am 01.01.2021 an die Stelle des jeweils am  31.12.2020 zuständig gewesenen Finanzamtes.

- missed: `Finanzamt für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamt Österreich`, `Finanzamtes`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_60`)

Grundsätzlich richtig ist zwar, dass der Beschwerdeführer nicht über die erforderlichen  Arbeitskapazitäten verfügte, um die Arbeiten durchführen zu können und daher  Subunternehmer, namentlich u.a. die Furtnor-Handel GmbH  die PGIV Umwelt Entwicklung GmbH und die **Burglechner Touristik GmbH & Co KG**  beauftragte.

- missed: `Burglechner Touristik GmbH & Co KG` (organisation)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_72`)

Dies Folgerung wird nicht zuletzt auch dadurch gestützt, dass die **West Werktri GmbH** in Österreich auch (als Arbeitgeber) einen Lohnzettel an die österreichische  Finanzverwaltung übermittelt hat.

- missed: `West Werktri GmbH` (organisation)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_39`)

Die Republik Österreich hat durch die Einführung eines Anpassungsmechanismus in Bezug  auf die Familienbeihilfe und den Kinderabsetzbetrag für Erwerbstätige, deren Kinder ständig in  einem anderen Mitgliedstaat wohnen, gegen ihre Verpflichtungen  - aus Art. 7 und 67 der Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des  Rates vom 29. April 2004 zur Koordinierung der Systeme der sozialen Sicherheit sowie  - aus Art. 4 der Verordnung Nr. 883/2004 und Art. 7 Abs. 2 der Verordnung (EU) Nr. 492/2011  des **Europäischen Parlaments** und des Rates vom 5. April 2011 über die Freizügigkeit der  Arbeitnehmer innerhalb der Union  verstoßen.

- missed: `Europäischen Parlaments` (organisation)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Wladimir Schaeffer  in der Beschwerdesache  Scarlett Ever, Felle 6, 4264 Unterrauchenödt, Österreich, vertreten durch **Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH**, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom  10. Oktober 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom 18. September  2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 1. Juli  2023 bis 31. Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- predicted in sentence: `Bundesfinanzgericht`

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_3`)

Entscheidungsgründe  Die Beschwerdeführerin (Bf.), eine in Liechtenstein ansässige Aktiengesellschaft, ist  Rechtsnachfolgerin der österreichischen **Unter-Luftfahrt Institut GmbH**  die mit dem Verschmelzungsvertrag vom  22.12.2015 steuerlich rückwirkend per 30.09.2015 grenzüberschreitend auf die Bf. mit der  Wirkung der Gesamtrechtsnachfolge verschmolzen wurde.

- missed: `Unter-Luftfahrt Institut GmbH` (organisation)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_20`)

Ergänzungsersuchen des FA vom 27.06.2018:  Sie werden ersucht, binnen oben genannter Frist, folgende Nachweise in deutscher Sprache und  Kopie für das Kalenderjahr 2017 zu erbringen:  1. Angabe des Familienwohnsitzes in Ungarn und Nachweis der Wohnungskosten am  Familienwohnsitz (z.B. Grundbuchsauszug, Mietvertrag etc.)  2. Ihren Einkommensnachweis in Ungarn (Bescheinigung EU/ EWR der ungarischen  Steuerbehörde zur Einkommensteuererklärung für Staatsangehörige von Mitgliedstaaten der  **Europäischen Union** und des Europäischen Wirtschaftsraums - Formular E9 für das Kalenderjahr  2017)  3.

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_29`)

Hinsichtlich der Einkünfte aus der Tätigkeit für die **Finanzamt Linz**  R. AG folgt der erkennende  Richter den vom Beschwerdeführer mit dem Vorlageantrag beigebrachten  Abrechnungsbelegen jeweils für April bis Juni 2022 und 2023.

- missed: `Finanzamt Linz` (organisation)
- predicted in sentence: `Finanzamt`

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_21`)

Im Zuge der Außenprüfung  wurden die Belege vorgelegt und es wurde erstmalig folgender Sachverhalt festgestellt:  Die Firma RHO Pharma  in Lamperstätten  und die Firmen FA Spittal Villach  in FL Amberg, FA Spittal Villach  in  CH Struden (ab 27. April 2016 Maierdorf) und **Finanzamt Graz-Stadt**  in CH Kleindurlas  vermieten in  Österreich, Liechtenstein und der Schweiz Hebe-, Scheren- und Teleskopbühnen sowie Stapler  und andere Geräte.

- missed: `Finanzamt Graz-Stadt` (organisation)
- predicted in sentence: `Finanzamt`

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_69`)

Dass die Einbringung  per Telefax erfolgte schadet aufgrund der Verordnung des Bundesministers für Finanzen über  die Zulassung von Telekopierern zur Einreichung von Anbringen an das **Bundesministerium für  Finanzen**, an die Verwaltungsgerichte sowie an die Finanzämter und Zollämter (BGBl. II  2013/447) nicht.

- missed: `Bundesministerium für  Finanzen` (organisation)
- predicted in sentence: —

</details>

---

