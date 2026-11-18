# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-16T16:58:56.525631

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-16_v9/config.yaml 
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
| Accuracy (exact match) | 98.2% |
| True Positives | 745 |
| False Positives | 472 |
| False Negatives | 1106 |
| Total Gold Entities | 1851 |
| Micro Precision | 61.2% |
| Micro Recall | 40.2% |
| Micro F1 | 48.6% |
| Macro F1 | 48.6% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Honorifics Herr/Frau Context` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Complex Title Combinations` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Anonymized Names with Digits` | 1.5% | 100.0% | 0.8% | 14 | 14 | 0 |
| `Dr.in Pattern` | 1.5% | 93.3% | 0.8% | 15 | 14 | 1 |
| `Herr Name Context` | 5.2% | 86.2% | 2.7% | 58 | 50 | 8 |
| `Academic and Professional Titles Refined` | 35.2% | 82.5% | 22.4% | 502 | 414 | 88 |
| `Representative Context` | 1.7% | 80.0% | 0.9% | 20 | 16 | 4 |
| `Standalone Name in Complaint Context Refined` | 17.4% | 47.4% | 10.6% | 416 | 197 | 219 |
| `Anonymized Initials and Digits` | 2.5% | 45.3% | 1.3% | 53 | 24 | 29 |
| `Anonymous Initial Names Refined` | 0.4% | 40.0% | 0.2% | 10 | 4 | 6 |
| `Frau Name Context Refined` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `Prof. Title Pattern` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `Complex Title Combinations Refined` | 0.1% | 25.0% | 0.1% | 4 | 1 | 3 |
| `Von Name Context` | 0.5% | 21.7% | 0.3% | 23 | 5 | 18 |
| `Richter/Richterin Context` | 0.2% | 5.0% | 0.1% | 40 | 2 | 38 |
| `Complex Legal Titles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Simple First Name Only (Contextual)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymous Initial Name` | 0.0% | 0.0% | 0.0% | 11 | 0 | 11 |
| `Dr.Daisy Pattern` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `MMA Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arthur Jonas Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag.a Pattern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `VetR Prof.in Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HR Title Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Professional Role Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `seitens der Context` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Witness Name Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. A. Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OMedR Pattern` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Fr.PhD Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Single Word` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Complex Titles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Full Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name After Verb Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Herr Name Context Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name After Preposition On` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Name After Medical Context` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Single Word Name in Case Citation Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name with Suffix Pattern` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Single Word Name in Witness Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name with Suffix Pattern Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone Name in Witness/Subject Context` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Anonymous/Initial Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Signature/End Name Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Single Word Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single Initial Name Context` | 0.0% | 0.0% | 0.0% | 18 | 0 | 18 |
| `Single Word Name in Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Honorifics Herr/Frau Context` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `2dac22d0`  
**Description:**
Captures names preceded by 'Herr' or 'Frau' in contexts like 'des Herrn [Name]' or 'an Frau [Name]', ensuring full name capture.

**Content:**
```
(?:des Herrn|der Frau|an Frau)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

</details>

---

## `Complex Title Combinations` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `7fadc38b`  
**Description:**
Captures names with multiple consecutive titles (e.g., 'Hon.-Prof. VetR', 'HA Dr.') and suffixes like ', MA', ', LLB', ', Bakk. techn.' ensuring the full string is captured.

**Content:**
```
\b(?:Hon\.-Prof\.|VetR|HA|RgR)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Prof\.in|Prof\.|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|StR|OMedR)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |Bakk\. techn\. |LL\.B\. |LL\.M\.)+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Finn Rosen` | `Hon.-Prof. Dr. Finn Rosen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dragan Ohlff` (person)
- `Dr. Sven Rudolf Thorstensen LLM` (person)
- `Finanzamtes Baden Mödling` (organisation)

</details>

---

## `Anonymized Names with Digits` 🏆

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `827879b2`  
**Description:**
Captures anonymized names like 'Dr. Dok1', 'Dr. F1' where the name part contains digits, ensuring they are standalone entities.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.)\s+[A-Z][a-z]+[0-9]+(?:[ ]+[A-Z][a-z]+[0-9]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.015 | 14 | 14 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 14 | 0 | 1837 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_4`)


Dr. Dok1, Fachgebiet Allgemeinmedizin, erstellte nach Untersuchung von S. am 2. März 2021  folgendes Gutachten:  Anamnese:  Schwangerschaft und Geburt unauffällig  TE und Paukenröhrchen;

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_79`)


Die Bf. brachte am 25. August 2021 folgenden Vorlageantrag ein:  „In der Beschwerdevorentscheidung vom 20.07.2021 wird unter Zugrundelegung des  Sachverständigengutachtens von Dr. Dok1, der Allgemeinmediziner ist, davon ausgegangen,  dass bei S. X. keine Behinderung vorliegt: Der Sachverständige kommt zum Schluss, dass „kein  Grad der Behinderung zu ermitteln" wäre.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_85`)


Entgegen der Schlussfolgerung im Sachverständigengutachten von Dr. Dok1 ist der Umstand,  dass keine Therapien und keine ärztliche Verlaufsdokumentation vorgelegt wurden, nicht  geeignet darauf zu schließen, dass keine Behinderung vorliegt!

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_91`)


Entgegen den Ausführungen im Sachverständigengutachten von Dr. Dok1 haben sehr wohl  Therapien stattgefunden.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_92`)


Es wird auch darauf hingewiesen, dass die diagnostizierte Erkrankung  einen Dauer- bzw. Endzustand darstellt und daher das Ergebnis des  Sachverständigengutachtens von Dr. Dok1, dass die Diagnose nicht vorliege und auch kein Grad  der Behinderung gegeben wäre, in einem diametralen Widerspruch (den es im Ermitt- lungsverfahren aufzuklären gilt) zur klinisch fachspezifischen Diagnose steht.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_109`)


Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_167`)


Erst im Vorschulalter fallen Schwierigkeiten auf (u. a.  Kontaktprobleme, wiederkehrende Verhaltensmuster, Missachten von Regeln beim Spielen  etc.) (https://focus-arztsuche.de/magazin/krankheiten/psychische-erkrankungen/was-ist-das- asperger-syndrom-und-wie-erkennt-man-es )  Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest, dies mit der Begründung, dass zwar gutachterliche Diagnosen gestellt  worden seien, jedoch mangels Inanspruchnahme adäquater Therapien, eine, für die  Beurteilung alltagsrelevanter, anhaltender Einschränkungen erforder-liche, ärztliche  Verlaufsdokumentation, nicht vorhanden sei.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_138`)


M. wurde auf Grund der Beschwerde am 6. November 2021 ein weiteres Mal untersucht und  von Dr. Dok2 folgendes Gutachten erstellt:  "Anamnese:  letzte Begutachtung 7-2020 mit 30% wegen Asperger Syndrom  Nun Einspruch da sich ihr Zustand verschlechtert hätte  Schwangerschaft und Geburt unauffällig, nach der Geburt Unruhe und weinen aufgefallen, sie  hätte viel geweint.

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_219`)


Im Gutachten vom 6. November 2020 stellte Dr. Dok2, Arzt für Allgemeinmedizin, ebenfalls die  Diagnose Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 mit einem  Grad der Behinderung von 30 vH.

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_220`)


Dr. Dok2 wählte, wie schon Dr. Dok1, 2 Stufen über dem unteren Rahmensatz, da eine mäßige  Einschränkung der sozialen Fähigkeiten und die Absolvierung eines Studiums möglich sei.

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |
| `Dr. Dok1` | `Dr. Dok1` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_282`)


Dem mit dem zweiten Gutachten betrauten Sachverständigen, Dr. Dok2, Arzt für Allge- meinmedizin, lagen bei der Erstellung seines Gutachtens vom 6. November 2020 folgende  Befunde bzw. Unterlagen vor:  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_289`)


akustische Differen- zierungsschwäche  Dr. Dok2 reihte die Erkrankung, übereinstimmend mit Dr. Dok1, unter die Pos.Nr. 03.04.01 mit  einem Grad der Behinderung von 30 vH. und bescheinigte ebenfalls keine Erwerbsunfähigkeit,  dies mit der Begründung, dass keine zweifelsfrei dokumentierte Gesundheitsschädigung  vorliege, die die dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, zur Folge  habe.

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |
| `Dr. Dok1` | `Dr. Dok1` |

</details>

---

## `Dr.in Pattern` 🏆

**F1:** 0.015 | **Precision:** 0.933 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `5c08400b`  
**Description:**
Specifically targets the feminine academic title 'Dr.in' followed by a full name.

**Content:**
```
\bDr\.in\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.008 | 0.015 | 15 | 14 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 14 | 1 | 1837 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Dr.in Laurin Morgenschweis` | `Dr.in Laurin Morgenschweis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich` (address)
- `Fatima Beringschmidt` (person)
- `Finanzamtes Waldviertel` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Ottfried Theißl` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Kirstin Matiascheck` | `Dr.in Kirstin Matiascheck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Schwinge` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Edith Lohhausen` | `Dr.in Edith Lohhausen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Michael Haberl` (person)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sheila Nonnmacher` | `Dr.in Sheila Nonnmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr.in Linn Wolek` | `Dr.in Linn Wolek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Uwe Vaculik` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Janina Gruenaeugl, Geiereckstraße 27, 4720 Güttling, Österreich, Schweden, vertreten durch die Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H., Wagramer Straße 19, 1220  Wien, über die Beschwerde vom 9. Jänner 2017 gegen den Bescheid des Finanzamtes für  Großbetriebe (vormals Bruck Eisenstadt Oberwart) vom 13. April 2015 betreffend Abweisung  eines Antrages auf Rückzahlung Österreichischer Lohnsteuer,Einkommensteuer 2012  Steuernummer 65-008/8295  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janina Gruenaeugl` (person)
- `Geiereckstraße 27, 4720 Güttling, Österreich` (address)
- `Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H.` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `65-008/8295` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Chen Kruczyk  in der Beschwerdesache Olivia Trienes,  Kleingerharts 28, 4972 Dann, Österreich, über die Beschwerde vom 13. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 5. Mai 2022, Ordnungsbegriff X1, betreffend Abweisung des Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum ab März 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Chen Kruczyk` | `Dr.in Chen Kruczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Trienes` (person)
- `Kleingerharts 28, 4972 Dann, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ingeborg Brockmayer  in der Beschwerdesache des  Timothy Penzlin, Ötzeltgasse 264, 6252 Kleinsöll, Österreich, betreffend die Beschwerde vom 25. Jänner 2017 gegen den  Haftungsbescheid des FA Innsbruck  vom 21. Dezember 2016 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Ingeborg Brockmayer` | `Dr.in Ingeborg Brockmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Penzlin` (person)
- `Ötzeltgasse 264, 6252 Kleinsöll, Österreich` (address)
- `FA Innsbruck` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des FA Spittal Villach (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr.in Anneliese Furtmeier` | `Dr.in Anneliese Furtmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Werner Kachelek` (person)
- `Heideweg-Siedlung 7, 4030 Linz, Österreich` (address)
- `Eugen Josef Bertsch` (person)
- `FA Spittal Villach` (organisation)
- `Finanzamt  Österreich` (organisation)
- `85-278/4119` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Koolen  in der Beschwerdesache   Univ.-Prof. Brian Salemi, Ulrichskirchen 3, 4184 Neuschlag, Österreich, Philippinen, Steuernummer 63-391/9556  über die Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 1. Februar  2018 betreffend Vorsteuererstattung 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Koolen` | `Dr.in Regina Koolen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brian Salemi` (person)
- `Ulrichskirchen 3, 4184 Neuschlag, Österreich` (address)
- `63-391/9556` (tax_number)
- `Finanzamt Grieskirchen Wels` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Jonas Nußer  in der Beschwerdesache Dr.in Flora Lallemand,  Rochusplatz 224, 9530 Bad Bleiberg, Österreich, über die Beschwerde vom 5. November 2024 gegen die Bescheide des  FA Graz-Stadt  vom 27. August 2024 über den Ablauf einer Aussetzung der Einhebung, über die  Festsetzung von Aussetzungszinsen und vom 1. Oktober 2024 über die Abweisung eines  Aussetzungsantrags, Steuernummer 29-953/8923, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Flora Lallemand` | `Dr.in Flora Lallemand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Univ.-Prof. Jonas Nußer` (person)
- `Rochusplatz 224, 9530 Bad Bleiberg, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `29-953/8923` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_32`)


Der Substanzwert ist  der niedrigste für Gesellschaftsanteile an der Dr.in Flora Lallemand  anzusetzende Wert, selbst wenn man  das gesamte Potential an Mehrwertsteuerrückforderungen durch das Finanzamt berücksichtigt  (Gutachten von Mag. H., gerichtlich beeideter Sachverständiger ON 35 u 48).

| Predicted | Gold |
|---|---|
| `Dr.in Flora Lallemand` | `Dr.in Flora Lallemand` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Mag. H.` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_15`)


Mit Beschluss vom 24.10.2024 bewilligt der Verwaltungsgerichtshof der Dr.in Flora Lallemand  Verfahrenshilfe für die außerordentliche Revision gegen das Erkenntnis des  Bundesfinanzgerichts Außenstelle Linz vom 20.08.2024, RV/7100825/2024, betreffend  Umsatzsteuer und Körperschaftsteuer 2015.

**False Positives:**

- `Dr.in Flora Lallemand  Verfahrenshilfe` — partial — gold is substring of pred: `Dr.in Flora Lallemand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Dr.in Flora Lallemand`(person)
- `Bundesfinanzgerichts`(organisation)

</details>

---

## `Herr Name Context` 🏆

**F1:** 0.052 | **Precision:** 0.862 | **Recall:** 0.027  

**Format:** `regex`  
**Rule ID:** `1c0bac7e`  
**Description:**
Captures names following 'Herr' or 'des Herrn', ensuring the name is followed by a space, punctuation, or end of string, but NOT by another capitalized word (to avoid 'Hus Es').

**Content:**
```
(?:des Herrn|Herr)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.862 | 0.027 | 0.052 | 58 | 50 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 50 | 8 | 1801 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_71`)


…“ Auch ein  Passus im vorgelegten TÜV-Bericht über den Prüftermin am 24.6.2019 steht damit in Einklang:  „Sehr geehrter Herr Volchert  an Ihrem Fahrzeug wurden zum Zeitpunkt der Untersuchung keine  Mängel festgestellt. …“.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_99`)


…Herr Volchert ist hauptberuflich Angestellter der AG in d_Ort_2.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_105`)


Herr Eugen Volchert  ist polizeilich in der Adr, Plz_1  d_Ort_1 gemeldet und deshalb ist sein Fahrzeug auch in d_Ort_1 zugelassen.

| Predicted | Gold |
|---|---|
| `Eugen Volchert` | `Eugen Volchert` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)


12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr Aldewereld von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

| Predicted | Gold |
|---|---|
| `Aldewereld` | `Aldewereld` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_69`)


Herr Frikel ist ebenso Gesellschafter.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_84`)


Prima Abo 10,00  Gesamt 431,27  Arbeitsmittel:  1. 1. CD Herr Riese und sein Garten 21,00  5 von 26 Seite 6 von 26

| Predicted | Gold |
|---|---|
| `Riese` | `Riese` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

| Predicted | Gold |
|---|---|
| `Karina Burfeindt` | `Karina Burfeindt` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)


Herr Sahin konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

| Predicted | Gold |
|---|---|
| `Sahin` | `Sahin` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_165`)


In der Bestätigung der AG1 (Adr2) wurde durch den Geschäftsführer GF, bestätigt, dass Herr Luethgarth (geb. am Geb.) die Funktion eines Geschäftsführers in diesem Unternehmen innegehabt  habe.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_167`)


In der Bestätigung der AG2 (Adr3 / FN 1234) wurde durch den Geschäftsführer Gf2, bestätigt,  dass Herr Luethgarth (geb. am Geb.) als Geschäftsführer der AG2 tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)


Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr Ballschmieder laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/144646.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144646.1_44`)


Die  diesbezügliche Aufforderung (Bescheid vom 28.10.2021) hat Herr Jakob Dombrink  an das Finanzamt  retourniert und vermerkt, dass er eine Rente aus der Schweiz bekommt und diese zur Gänze in  die landwirtschaftliche Gesellschaft fließt (siehe "Schreiben Jakob Dombrink  v. 15.11.2021").

| Predicted | Gold |
|---|---|
| `Jakob Dombrink` | `Jakob Dombrink` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145368.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145368.1_34`)


Herr Gotthard Dinkelmann  hat in eigener Recherche noch herausgefunden, dass bei unbeschränkter  Schweizer Steuerpflicht nur ein sehr enger Kostenkatalog berücksichtigt werden könnte:  „Schuldzinsen, Beiträge in die Säule 2b und 3a, berufliche Weiterbildungskosten, bezahlte  Alimente, Unterstützungsbeiträge“ und bei beschränkter Steuerpflicht lediglich „Beiträge an  die Säule 2b und 3a sowie Wochenaufenthaltskosten“.

| Predicted | Gold |
|---|---|
| `Gotthard Dinkelmann` | `Gotthard Dinkelmann` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_726`)


In ihrer per Mail überreichten Vorhaltsbeantwortung vom 23. Mai 2024 (OZ. 111) nahm die  Bf. zu beiden Vorhalten (hg. GZ. RV/2100888/2022 vom 30. April 2024) und RV/2100046/2023  v. 23. April 2024) wie folgt Stellung:  „Sehr geehrter Herr Hartmut Berning   im Namen unseres o.a. Klienten und unter Berufung auf die uns erteilte Vollmacht können wir  zu Ihren Vorhalten vom 30.4.2024 (zugestellt am 6.5.2024) im Verfahren RV/2100888/2022  sowie vom 23.4.2024 (zugestellt am 26.4.2024) im Verfahren RV/2100046/2023 gerne wie  folgt Stellung nehmen:   1. Unternehmereigenschaft der Kunden   Wir haben von unserem Klienten keine weiteren Unterlagen betreffend die unternehmerischen  Leistungsempfänger erhalten, sodass wir keine weiterführenden Angaben zu diesen machen  können.

| Predicted | Gold |
|---|---|
| `Hartmut Berning` | `Hartmut Berning` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_13`)


Im Rahmen einer zweiten Stellungsuntersuchung vom  05.01.1989 wurde Herr Luna Fruechtenicht  als für den Präsenzdienst „untauglich“ eingestuft und dies  mit den festgestellten Diagnosen: Grand Mal Epilepsie, chronischer Alkoholabusus sowie  Oligrophenie begründet.

| Predicted | Gold |
|---|---|
| `Luna Fruechtenicht` | `Luna Fruechtenicht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

**False Positives:**

- `Aron` — partial — pred is substring of gold: `Aron Pommeränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Aron Pommeränke`(person)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Roland` — partial — pred is substring of gold: `Roland Rößle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Roland Rößle`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Ministerialrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl  MA67/Zahl/2022, wurde Herr Annette Preußing (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Annette` — partial — pred is substring of gold: `Annette Preußing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Annette Preußing`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_30`)


Herr Gf ist darüber hinaus  alleiniger Gesellschafter-Geschäftsführer der Carrasco Software GmbH  der 100%-igen Muttergesellschaft der  Bf.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Carrasco Software GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_151`)


Der Steuerberater von Frau NN1 – Herr Kollege Z von der öStb-Kanzlei – ist cc. gesetzt.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_152`)


Herr Kollege Z und ich konnten uns heute abstimmen.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_155`)


Diesem Verzicht stimmt Herr Kollege Z in Vertretung von Frau  NN1 zu.  11 von 34 Seite 12 von 34

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

</details>

---

## `Academic and Professional Titles Refined` 🏆

**F1:** 0.352 | **Precision:** 0.825 | **Recall:** 0.224  

**Format:** `regex`  
**Rule ID:** `f09fb52b`  
**Description:**
Captures names preceded by academic/professional titles, explicitly handling multiple consecutive titles and ensuring full name capture including hyphenated names and suffixes. Fixes truncation issues.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|Dipl\. Kfm\. StR|Dipl\. Kfm\.|Dipl\. Kff\.|StR|VetR|OMedR|RgR|HR)(?:\s+(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?))*\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.)+)?(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.825 | 0.224 | 0.352 | 502 | 414 | 88 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 414 | 88 | 1437 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_0`)


GZ. RV/5101724/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter Dr. Elias Derneden  in der Beschwerdesache über die Beschwerde vom 14.01.2019 gegen den Bescheid der belangten Behörde vom 04.01.2019 betreffend Familienbeihilfe für den Zeitraum ab März 2018 zu Recht: 1.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elias Derneden` | `Dr. Elias Derneden` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Hajicek` | `Dr. Alexander Hajicek` |
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Michael Franz` | `Mag. Michael Franz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Josef Großin` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Mag. Peter Staudinger` | `Mag. Peter Staudinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)
- `Finanzamtes Linz` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Kießerling` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.a Univ.-Prof.in Ada Schaeferlein` | `Mag.a Univ.-Prof.in Ada Schaeferlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leroy Sitterle` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |
| `Univ.-Prof.in Shoshana Leuther` | `Univ.-Prof.in Shoshana Leuther` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR OSR Leonie Ercklentz` (person)
- `Karnitzen 135, 9635 Kronhof, Österreich` (address)
- `LKP Steuerberatung OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theodora Urbanova, Bakk. iur.` (person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `54-205/5010` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Elias Voht` | `VetR Elias Voht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |
| `Hon.-Prof. Ruprecht Hauswerth` | `Hon.-Prof. Ruprecht Hauswerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Zarin Eckartz` | `Priv.-Doz.in Zarin Eckartz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Oortwyn` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sean Herdling` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Othmar Feuerbaum` | `Mag. Othmar Feuerbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingeborg Kollaczek` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Melina Bankratz` | `Priv.-Doz.in Melina Bankratz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lars Huesgen` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Bogdanowic` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Mag. Belinda  Maria Eder` | `Mag. Belinda  Maria Eder` |
| `Mag. Katharina Moravec` | `Mag. Katharina Moravec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Agneter` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Schoenrock, LLM` | `Hon.-Prof. Thassilo Schoenrock, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `06-88-920/2630` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |
| `Mag. Bruno  Sundl` | `Mag. Bruno  Sundl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Glashüttner` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ottfried Ficici` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jacqueline Dittus` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |
| `VetR Burkhard Krautschenko` | `VetR Burkhard Krautschenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Titus Ohlmer` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edwin Pfaefflin` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Diethard Ringhand` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Achmed Karolzak` | `Univ.-Prof. Achmed Karolzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lilia Löffelmann` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Olivia Ziegeler` | `Mag.a Olivia Ziegeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mike Reislehner` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dr.in Bianca Gerasimczuk` | `Priv.-Doz.in Dr.in Bianca Gerasimczuk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Diedering, Bakk. iur.` (person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich` (address)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marceline Flory` | `Univ.-Prof.in Marceline Flory` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Zeitlhuber` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |
| `StR Univ.-Prof. Alvin Paulikat` | `StR Univ.-Prof. Alvin Paulikat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Leonhard Hestermeyer` | `OMedR Leonhard Hestermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` (person)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich` (address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `73-948/8864` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Christoph Hasenfraz` | `Hon.-Prof. Christoph Hasenfraz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Sahlmüller` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Meyerhofer` | `Mag. Manuela Meyerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandra Fenn` (person)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Dr. Farid Rifaad` | `Dr. Farid Rifaad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Evelyn Antwerber` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |
| `StR Milena Neidig` | `StR Milena Neidig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Melinda Herrwerth` | `Dipl.-Ing. Melinda Herrwerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dürergasse 7, 4872 Windbichl, Österreich` (address)
- `40-459/9630` (tax_number)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `Lubomir Nakajima` (person)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hon.-Prof.in Laurence Vasylenko` | `Dr.in Hon.-Prof.in Laurence Vasylenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Graz` (organisation)
- `02-410/2351` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jonas Gutkauf` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tristan Potente` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Overlaender` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Maria-Luise Wohlmayr` | `Dr. Maria-Luise Wohlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lieselotte Reinicker` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |
| `Dipl. Kfm. Ing. Ing. Jonas Thumberger` | `Dipl. Kfm. Ing. Ing. Jonas Thumberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `UNICONSULT Steuerberatungs GmbH & Co KG` (organisation)
- `FA Braunau Ried Schärding` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Zoltan Dabrowski` | `Priv.-Doz. Zoltan Dabrowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Prof. Hartmut Szardemings` (person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Kuprian` | `Mag. Martin Kuprian` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Werner Böltl` (person)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Mag. Franz Josef` — partial — pred is substring of gold: `Mag. Franz Josef Großin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alexander Hajicek`(person)
- `Mag. Helga Hochrieser`(person)
- `Mag. Michael Franz`(person)
- `Mag. Franz Josef Großin`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `StR Samuel Fraesdorff` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`
- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

**False Positives:**

- `StR Samuel Fraesdorff` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leroy Kusznierz`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Maximilian Jasper`(person)
- `Gustav Nowak`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Dr.in Ing. Viktoria Weigart  Dieses Unternehmen` — partial — gold is substring of pred: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Dr.in Ing. Viktoria Weigart  Somit` — partial — gold is substring of pred: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

</details>

---

## `Representative Context` 🏆

**F1:** 0.017 | **Precision:** 0.800 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `f0ec9a87`  
**Description:**
Captures names of representatives mentioned after 'vertreten durch', strictly requiring a title or full name pattern and excluding generic terms.

**Content:**
```
(?:vertreten durch)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z][a-z]+(?:gmbH|KG|AG)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.009 | 0.017 | 20 | 16 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 16 | 4 | 1835 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Dr Vana Dr Kolbitsch Mag Breitenecker` | `Dr Vana Dr Kolbitsch Mag Breitenecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr Christian Burghardt` | `Dr Christian Burghardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `StR Univ.-Prof. Alvin Paulikat` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag Kerstin Friedrich` | `Mag Kerstin Friedrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Dr.in Edith Lohhausen` (person)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Erich Allbrand` | `Erich Allbrand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Robert Derici` (person)
- `Exlgasse 12, 9623 Karnitzen, Österreich` (address)
- `12-876/0077` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Schabel` | `Peter Schabel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Jeremias Kierstan` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Magistrats  der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paula Tschann  in der Beschwerdesache Merlin Dankwort,  Urtelgasse 9y, 8232 Stambach, Österreich  vertreten durch Valerian Stamataki, Schanze 29 12, 3661 Unterthalheim, Österreich, über die Beschwerde vom  6. September 2022 gegen den Bescheid des Finanzamtes Österreich vom 9. August 2022  betreffend Festsetzung eines ersten Säumniszuschlages, Steuernummer 88-049/5894  nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerian Stamataki` | `Valerian Stamataki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Paula Tschann` (person)
- `Merlin Dankwort` (person)
- `Urtelgasse 9y, 8232 Stambach, Österreich` (address)
- `Schanze 29 12, 3661 Unterthalheim, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-049/5894` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `Helga Kraus` | `Helga Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Cassandra Schmedtje` (person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dr. Martin Wadepfuhl  in der Beschwerdesache Renate Bürvenig,  Kreuzkapellenweg 7, 5151 Hochberg, Österreich, vertreten durch Ludmilla Flaumbaum, Herrengschwendt 3, 8761 Mühltal, Österreich, über die Beschwerde vom  15. Februar 2021 gegen die Bescheide des Finanzamtes Österreich vom 19. Jänner 2021  betreffend die Haftung für Lohnsteuer für 2015, 2016, 2017, 2018 und 2019, sowie den  Dienstgeberbeitrag zum FLAF für 2015, 2016, 2017, 2018 und 2019 und den Zuschlag zum  Dienstgeberbeitrag für 2015, 2016, 2017, 2018 und 2019 zu Steuernummer 74-041/7335  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ludmilla Flaumbaum` | `Ludmilla Flaumbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Dr. Martin Wadepfuhl` (person)
- `Renate Bürvenig` (person)
- `Kreuzkapellenweg 7, 5151 Hochberg, Österreich` (address)
- `Herrengschwendt 3, 8761 Mühltal, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `74-041/7335` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Georg Kunstmann  in der Beschwerdesache Gerhard Weinbergs,  Löwengrub 29, 8680 Hönigsberg, Österreich, vertreten durch Damian Eccardt, Unterort 18, 4673 Bernhartsdorf, Österreich, über die Beschwerde vom 8.  Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 4. April 2023 betreffend  Umsatzsteuer 2013 sowie über die Beschwerden vom 23. August 2023 gegen die Bescheide  des Finanzamtes Österreich vom 4. August 2023 betreffend Umsatzsteuer 2014, 2015, 2016  und 2017 zu Steuernummer 50-546/1107  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Damian Eccardt` | `Damian Eccardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Georg Kunstmann` (person)
- `Gerhard Weinbergs` (person)
- `Löwengrub 29, 8680 Hönigsberg, Österreich` (address)
- `Unterort 18, 4673 Bernhartsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `50-546/1107` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Caroline Bolzen, Patschweg 38, 9635 Nölbling, Österreich, vertreten durch Christine Maria Brunnthaller, Baumgarten 20 Tür  2, 3512 Mautern/Donau, über die Beschwerde vom 25. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 18. März 2024 betreffend Familienbeihilfe 07.2023-03.2024 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Maria Brunnthaller` | `Christine Maria Brunnthaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Caroline Bolzen` (person)
- `Patschweg 38, 9635 Nölbling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Franz Quapp  in der Beschwerdesache  Elvira Mathis, Claudiastraße 7, 2061 Hadres, Österreich, vertreten durch Wladimir Kreissl, Seibersdorf 3, 8141 Bierbaum, Österreich,  über die Beschwerde vom 13. Mai 2015 gegen den Bescheid des (damaligen) Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 9. April 2015  betreffend Säumniszuschlag 2015 Steuernummer 98-983/4004  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Kreissl` | `Wladimir Kreissl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Franz Quapp` (person)
- `Elvira Mathis` (person)
- `Claudiastraße 7, 2061 Hadres, Österreich` (address)
- `Seibersdorf 3, 8141 Bierbaum, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `98-983/4004` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des FA Spittal Villach (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Eugen Josef Bertsch` | `Eugen Josef Bertsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Anneliese Furtmeier` (person)
- `Werner Kachelek` (person)
- `Heideweg-Siedlung 7, 4030 Linz, Österreich` (address)
- `FA Spittal Villach` (organisation)
- `Finanzamt  Österreich` (organisation)
- `85-278/4119` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Jonathan Goessl` | `Jonathan Goessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Maja Lauers` (person)
- `Univ.-Prof. Mehmet Klasema` (person)
- `Labon 67, 4861 Looh, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `85-153/1153` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gregor Heumann, Weberweg 49, 4274 Steinbichl, Österreich, vertreten durch Stefan Josef Glechner, Am  Schwarzenbach 8, 4921 Hohenzell, über die Beschwerde vom 10. Februar 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. Jänner 2023 betreffend Feststellung der Einkünfte  § 188 BAO 2021 Steuernummer 31-405/5720  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stefan Josef Glechner` | `Stefan Josef Glechner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Gregor Heumann` (person)
- `Weberweg 49, 4274 Steinbichl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `31-405/5720` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Herrn  Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher BA LL.M.(WU) in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miriam Wurmehl` — partial — pred is substring of gold: `Miriam Wurmehl, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Annika Streicher BA LL.M.(WU)`(person)
- `Dimitri Gaessner`(person)
- `Sauerbrunnberg 15, 8124 Neuhof, Österreich`(address)
- `Miriam Wurmehl, Bakk. phil.`(person)
- `Windparkstraße 7, 5092 Gumping, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `90-683/6114`(tax_number)

</details>

---

## `Standalone Name in Complaint Context Refined` 🏆

**F1:** 0.174 | **Precision:** 0.474 | **Recall:** 0.106  

**Format:** `regex`  
**Rule ID:** `4a2abaac`  
**Description:**
Captures full names appearing after 'in der Beschwerdesache' or 'des/der' when no title is present, strictly excluding generic terms like 'Stadt', 'Bf', 'Beschuldigten', and addresses.

**Content:**
```
(?:in der Beschwerdesache|des|der)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z][a-z]+(?:gmbH|KG|AG)|$)(?!.*(?:Stadt.*Wien|Beschuldigten|Bf.*[,:]|Beschwerdeführerin))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.474 | 0.106 | 0.174 | 416 | 197 | 219 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 197 | 219 | 1654 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Pipers` | `Kai Pipers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Dietlind Mahlstädt` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Leroy Sitterle` | `Leroy Sitterle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Hermine Ruprich` | `Hermine Ruprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rosamunde Galanidis` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Oortwyn` | `Volkmar Oortwyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Zarin Eckartz` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sean Herdling` | `Sean Herdling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Ingeborg Kollaczek` | `Ingeborg Kollaczek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Othmar Feuerbaum` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Lars Huesgen` | `Lars Huesgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melina Bankratz` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Bogdanowic` | `Rudolf Bogdanowic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heike Dorrenbach` | `Heike Dorrenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Rauscher` (person)
- `Mag. Franz Glashüttner` (person)
- `Dr. Christian Haid` (person)
- `Mag. Bruno  Sundl` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_76`)


III. Beweiswürdigung  Der vorstehende Sachverhalt basiert auf dem von der belangten Behörde vorgelegten  Veranlagungsakt, den von den Beschwerdeführern vorgelegten Urkunden bzw. nachfolgender  Beweiswürdigung:  Die Feststellungen zur Gründung der Leroy Kusznierz, jene zum Gegenstand des Unternehmens, zu  den Beteiligungsverhältnisse sowie den Eintragungen im Firmenbuch gehen aus dem im Akt  erliegenden Gesellschaftsvertrag vom Datum sowie einer Einsicht des Gerichtes in das offene  Firmenbuch unter Berücksichtigung der dort hinterlegten historischen Daten hervor.

| Predicted | Gold |
|---|---|
| `Leroy Kusznierz` | `Leroy Kusznierz` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ottfried Ficici` | `Ottfried Ficici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Titus Ohlmer` | `Titus Ohlmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Annemarie Schwinge` | `Annemarie Schwinge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Kirstin Matiascheck` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mike Reislehner` | `Mike Reislehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Olivia Ziegeler` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Zeitlhuber` | `Stephan Zeitlhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marceline Flory` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Morgenbesser` | `Karl Morgenbesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susette Glaeßel` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sandra Fenn` | `Sandra Fenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Mag. Manuela Meyerhofer` (person)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_22`)


In der dagegen fristgerecht am eingebrachten Beschwerde des Amtsbeauftragten vom  3. Dezember 2020 wird wie folgt ausgeführt:  Angefochten werde die Einstellung gem. § 136 FinStrG hinsichtlich der Geschäftsführerin A B,  Adresse1, sowie des belangten Verbandes die Saskia Sinnwell, Franz-Michel-Willam-Weg 31, 3580 Groß Burgstall, Österreich  mit folgendem  Inhalt:  „Die Grundlage des Verfahrens bildet die Betriebsprüfung vom 09.10.2019 bei der Saskia Sinnwell,  bei welcher festgestellt wurde, dass ein Liegenschaftsverkauf im Juni 2019 nicht in der UVA  gemeldet wurde.

| Predicted | Gold |
|---|---|
| `Saskia Sinnwell` | `Saskia Sinnwell` |

**Missed by this rule (FN):**

- `Franz-Michel-Willam-Weg 31, 3580 Groß Burgstall, Österreich` (address)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Tristan Potente` | `Tristan Potente` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Kevin Damiani` | `Kevin Damiani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. René Neuendorf` (person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Timothy Overlaender` | `Timothy Overlaender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fatima Eichmayr` | `Fatima Eichmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieskapellenweg 10, 8047 Graz, Österreich` (address)
- `Dr. Klaus Plätzer,` (person)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-455/2359` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_39`)


Mit Schreiben vom 30.12.2019 nahm die Beschwerdeführerin bezugnehmend auf einen entsprechenden Vorhalt des Bundesfinanzgerichts unter anderem zu der Frage Stellung, wie hoch der wöchentliche Zeitaufwand der Tochter für die Vorbereitung auf die von ihr wahrgenommenen Prüfungstermine sowie für die Abfassung der sog vorwissenschaftlichen Arbeit im Zeitraum März 2018 bis Jänner 2019 gewesen sei.

**False Positives:**

- `Frage Stellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Elisabeth Schafstall` — partial — gold is substring of pred: `Elisabeth Schafstall`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Emmerich Frydrychowski` — partial — gold is substring of pred: `Emmerich Frydrychowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Walter Summersberger`(person)
- `Emmerich Frydrychowski`(person)
- `Wassertheuer 21, 9112 Gletschach, Österreich`(address)
- `Zollamtes Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_73`)


„Der … Pkw steht im Eigentum der Einzelfirma Firma_1 an der Adresse Adr, D- Plz_1 d_Ort_1.

**False Positives:**

- `Adresse Adr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Merlin Feucht` — partial — gold is substring of pred: `Merlin Feucht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.DDr. Hedwig Bavenek-Weber`(person)
- `Merlin Feucht`(person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `57-396/6782`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

**False Positives:**

- `Kelderber Beratung Technologien` — type mismatch — same span as gold: `Kelderber Beratung Technologien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Silvia Gebhart`(person)
- `Kelderber Beratung Technologien`(organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich`(address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker`(person)
- `Mag Tatjana Kovacic`(person)
- `Dr  Heinrich Vana,`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `7867 150654`(social_security_number)
- `Europäischen Parlaments`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Theodora Urbanova` — positional overlap with gold: `Theodora Urbanova, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Theodora Urbanova, Bakk. iur.`(person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `54-205/5010`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_3`)


Nr. 10/2013 über die Beschwerden des Beschuldigten vom 10. Juni  2019 gegen  1. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 13. März 2019,  Zahl MA-ZAHL1 sowie  2. das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 14. Mai 2019,  Zahl MA-ZAHL2  zu Recht erkannt:  I. Gemäß § 50 in Verbindung mit § 38 VwGVG und § 45 Abs. 1 zweiter Satz VStG wird von der  Verhängung einer Strafe abgesehen und der beschwerdeführenden Partei unter Hinweis auf  die Rechtswidrigkeit ihres Verhaltens eine Ermahnung erteilt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die der  Beschwerdeführer keinen Beitrag zu den Kosten des verwaltungsgerichtlichen Strafverfahrens  zu tragen.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_133`)


in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_358`)


Der Beschwerdeführer stellt daher den  A N T R A G,  1. in dem Verfahren über diese Beschwerde eine mündliche Verhandlung abzuhalten und  2. der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 aufzuheben und das Verfahren einzustellen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_359`)


in eventu  der Beschwerde Folge zu geben und das angefochtene Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, dahin abzuändern, dass eine Ermahnung ausgesprochen  wird."

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_426`)


[...]  Die Bestätigung der Gesellschaft, in deren Werkstatt sich das Fahrzeug, für welches eine  Ausnahmebewilligung erteilt wurde, zu den Tatzeitpunkten befand, wurde dem Magistrat der  Stadt Wien, Magistratsabteilung 67, zur Kenntnis gebracht.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_21`)


– eine Rechnung von memoryking GmbH & Co KG, Berlin, vom 01.12.2018 über ein „deleyCON  2m Optisches Digital Audio Kabel SPDIF – 2x Toslink Stecker Digitalkabel Audiokabel LWL  Digitales Lichtwellenleiter Kabel – Schwarz/Blau“ in Höhe von 6,44 €, (= Rechnung Nr. 13 laut  Auflistung),  – eine Rechnung von amazon.de vom 22.07.2019 (Bestellung vom 17.10.2018) über ein  „Zubehör für Gopro, ccbetter Action Kamerahalterungen für Gopro hero 7 hero 2018 hero 6  Hero 4 Hero 5 Session Hero 1 2 3 3+ für die meisten Sportkameras mit Fall (Schwarz)“ in Höhe  von 19,27 €, (= Rechnung Nr. 14 laut Auflistung),  – eine Rechnung von AfB social & green IT, Ettlingen, vom 30.07.2018 über eine „Logitech 920- 003967 Wireless Combo MK330 – schnurlos Tastatur und Computermaus /2,4 GHz, USB,  QWERTZ deutsches Tastaturlayout) schwarz“ in Höhe von 44 €, (= Rechnung Nr. 15 laut  Auflistung),  – eine Rechnung von Yuanchuang e-business co.LTD., vom 21.05.2018, an C, Adresse2, über  einen „X-Sense CO03D CO Melder Kohlenmonoxid CO-Detektor Batteriebetrieben Sensor und  Alarm mit Digitalanzeige und Höchstwertspeicherung“ in Höhe von 29,99 €, (= Rechnung Nr. 16  laut Auflistung),  – eine Rechnung von SYNCWIRE UK LTD, Manchester, vom 02.04.2018 über ein „DisplayPort  Kabel – 2M Syncwire Vergoldetes DisplayPort zu DisplayPort Kabel High-Speed Auflösung Kabel  unterstützt Fire TV, Apple TV, Ethernet, Aud“ in Höhe von 8,99 €, (= Rechnung Nr. 17 laut  Auflistung),  – eine Rechnung von converter-shop.com, Berlin, vom 16.02.2018 über einen „Bronson++ HE-D  800 – 110 Volt Spannungswandler / Transformator – 800 Watt – In: EURO 220 – 240 Volt / Out:  USA 110 Volt – Ringkerntransformator 800W“ in Höhe von 79,99 €, (= Rechnung Nr. 18 laut  Auflistung),  – eine Rechnung vom RANKEI UK LTD, Manchester, vom 27.09.2018 über ein „Rankie  Verbindungskabel Displayport (DP) auf HDMI, 4K Auflösung Kabel, 1,8 m, Schwarz“ in Höhe von  7,99 €, (= Rechnung Nr. 19 laut Auflistung),  – eine Rechnung vom Hoomil, Shenzhen, vom 24.11.2018, an D, Adresse3, über eine „HOOLIL  Galaxy S7 Hülle, Premium Handy Schutzhülle für Samsung Galaxy S7 Hülle Leder Wallet Tasche  Flip Brieftasche Etui Schale, Schwarz (H3011)“ in Höhe von 12,35 €, (= Rechnung Nr. 20 laut  Auflistung),  – eine Rechnung vom John’s Handy, Wien, vom 27.07.2018, ohne Angabe des Namens und der  Anschrift des Abnehmers der Lieferung, über ein „Samsung galaxy s7 gold SN/IMEI:  356457097886024“ in Höhe von 339 €, (= Rechnung Nr. 21 laut Auflistung),  5 von 18 Seite 6 von 18

**False Positives:**

- `Wallet Tasche  Flip Brieftasche Etui Schale` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `memoryking GmbH & Co KG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_22`)


Dazu zählen insbesondere  Mittel der Bedarfsorientierten Mindestsicherung, Mittel der Grundversorgung, Mittel aufgrund  welcher die öffentliche Hand für einen entsprechenden Krankenversicherungsschutz des  Kindes  im Rahmen der gesetzlichen Pflichtversicherung sorgt.

**False Positives:**

- `Bedarfsorientierten Mindestsicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_15`)


Am 24.6.2019 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6 – BA 32, zur GZ. MA- Zahl1 wegen Nichtbezahlung der Strafe eine Vollstreckungsverfügung über die Geldstrafe in  Höhe von 60,00 Euro und setzte eine Mahngebühr von 5,00 Euro fest, die offene Forderung  betrug daher 65,00 Euro.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_22`)


Mit Bescheid vom 31.7.2019 wies der Magistrat der Stadt Wien, Magistratsabteilung 67, den  "Einspruch vom 05.07.2019 gegen die Strafverfügung vom 02.04.2019", GZ. MA-Zahl1 als  verspätet zurück.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_81`)


Über die Beschwerde wurde erwogen:  Sachverhalt und Beweiswürdigung:  Über die Bf. wurde mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67  vom 2.4.2019 zur GZ. MA-Zahl1 wegen des unter dem Punkt "Verfahrensgang" angeführten  Deliktes eine Geldstrafe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe in Höhe von 14 Stunden verhängt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_84`)


Am 24.6.2019 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6 – BA 32 wegen  Nichtbezahlung der Strafe eine Vollstreckungsverfügung über die Geldstrafe von 60,00 Euro  und eine Mahngebühr in Höhe von 5,00 Euro, insgesamt 65,00 Euro.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_86`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, ging aufgrund des Vorbringens der Bf.  von einem Einspruch gegen die Strafverfügung aus und wies diesen mit Bescheid vom  31.7.2019 als verspätet zurück.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_95`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, betrachtete diese E-Mail der Bf. als  Beschwerde gegen die Vollstreckungsverfügung vom 25.10.2019 und wies sie mit  Beschwerdevorentscheidung vom 21.11.2019 ab.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_138`)


Bei dem Schreiben vom 31.7.2019 handelt es sich um den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, mit welchem der Einspruch gegen die  Strafverfügung vom 2.4.2019 als verspätet zurückgewiesen wurde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

**False Positives:**

- `Xaver Plaumert` — partial — pred is substring of gold: `Xaver Plaumert, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Dr. Wolfgang Aigner`(person)
- `Erwin Agneter`(person)
- `Mag. Belinda  Maria Eder`(person)
- `Xaver Plaumert, BEd`(person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich`(address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Mag. Katharina Moravec`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_80`)


*) Printartikel: Laut Artikel von R.R. in der Zeitschrift Printartikel, würden laut Angaben des V.  A. ca. 150.000 A. Portionen pro Jahr umgesetzt werden.

**False Positives:**

- `Zeitschrift Printartikel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_445`)


Fortgesetztes Verfahren  Auskunftsschreiben des Geschäftsführers der Fachgruppe Gastronomie Wien, WKO Wien  Mit Mail des BFG vom 06.08.2020 wurde der Fachgruppengeschäftsführer der Fachgruppe  Gastronomie Wien, Wirtschaftskammer Wien, N.N. ersucht, bezüglich Fleischlieferungen an  Gastronomiebetriebe bekanntzugeben, ob es Daten betreffend das Verhältnis zwischen dem  gewerblich nutzbaren Fleischanteil und dem restlichen Fleischanteil in Gastronomiebetrieben  gebe.

**False Positives:**

- `Fachgruppe Gastronomie Wien` — no gold match — likely missing annotation
- `Fachgruppe  Gastronomie Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WKO Wien`(organisation)
- `BFG`(organisation)
- `N.N.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Gueldner Garten` — type mismatch — same span as gold: `Gueldner Garten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Tamara Steinmüller`(person)
- `Gueldner Garten`(organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich`(address)
- `FA Deutschlandsberg Leibnitz Voitsberg`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Bernhard Habdank`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_5`)


Der mit Einschreiben am 26. August 2020 eingebrachte Einspruch gegen diese Strafverfügung  wurde vom Magistrat der Stadt Wien, Magistratsabteilung 67, gemäß § 49 Abs. 1 VStG als  verspätet zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Beschwerdesache Jacqueline Dittus` — partial — gold is substring of pred: `Jacqueline Dittus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `Jacqueline Dittus`(person)
- `Sausal 90O, 4911 Schönfeld, Österreich`(address)
- `Anton Lammer  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_96`)


Aus dem Verwaltungsakt geht hervor, dass der Magistrat der Stadt Wien, MA 67, die  Versendung der Strafverfügung vom 2. Dezember 2019, Zahl, zunächst gemäß § 26 Abs. 1  Zustellgesetz (Zustellung ohne Zustellnachweis) an die Adresse Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich  und am 3. März  2020 die Versendung mit Rückscheinbrief veranlasst hat.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich`(address)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Beschwerdesache Edwin Pfaefflin` — partial — gold is substring of pred: `Edwin Pfaefflin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Edwin Pfaefflin`(person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich`(address)
- `Finanzamtes`(organisation)
- `35-514/8431`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

**False Positives:**

- `Herrn Raimund Ladwig` — partial — gold is substring of pred: `Raimund Ladwig`
- `Finanzamtes Bruck Eisenstadt Oberwart` — type mismatch — same span as gold: `Finanzamtes Bruck Eisenstadt Oberwart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Raimund Ladwig`(person)
- `Birkenring 18, 8451 Pernitsch, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Gregor Klocksin` — partial — gold is substring of pred: `Gregor Klocksin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Beschwerdesache Chiara Duchan` — partial — gold is substring of pred: `Chiara Duchan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter[...] in der Verwaltungsstrafsache gegen  Niklas Radschweit, Kaiserfeld 4, 8673 Steinhöf, Österreich, wegen der Verwaltungsübertretungen gemäß § 16 Abs. 1 des  Wiener Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBI. für Wien Nr. 20, in der  Fassung des LGBI. Nr. 71/2018 in der Fassung des LGBl für Wien Nr. 50/2013 in Verbindung mit  § 1 Abs. 1 GAG und Tarifposten B 1 und B 8 über die Beschwerde der Beschuldigten vom  15.11.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 -  Abgabenstrafen, vom 20.10.2020, Zahl: MA6/[...], zu Recht erkannt:  I.) Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2 VStG eingestellt.   II.) Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Niklas Radschweit`(person)
- `Kaiserfeld 4, 8673 Steinhöf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_126`)


Nach Überprüfung seitens der MA 37 am 12.11.2018 wurde der Bf. mit Bescheid des  Magistrates der Stadt Wien, MA 37-[...], vom 16.11.2018 aufgetragen, binnen zwei Monaten,  die unter dem Gehsteig (= öffentliches Gut) befindliche Füllstelle und Füllleitung zu entfernen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Harald Schwalbach`(person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Beschwerdesache Frauke Galleithner` — partial — gold is substring of pred: `Frauke Galleithner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_3`)


über die Beschwerde des Bf., Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich  vom 19. Februar 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 20. Jänner 2021, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) forderte die Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa.Dankwardt Wind AG  mit Schreiben vom 3. September 2019 gemäß § 2 Wiener Parkometergesetz 2006) auf,  der Behörde binnen zwei Wochen ab Zustellung des Schreibens Auskunft darüber zu erteilen,  wem das näher bezeichnete Fahrzeug am 5. Juli 2019 um 17:47 Uhr überlassen war, sodass es  in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Altgasse 25a, stand.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Fa.Dankwardt Wind AG`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `Beschwerdesache Heike Lehmensieck` — partial — gold is substring of pred: `Heike Lehmensieck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_15`)


Mit Straferkenntnis vom 9. März 2021 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig erkannt und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

**False Positives:**

- `Beschwerdesache Gebhard Klutentreter` — partial — gold is substring of pred: `Gebhard Klutentreter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Gebhard Klutentreter`(person)
- `Pfiferweg 136, 4906 Feichtet, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)


über die Beschwerde der Balthasar Brendtke, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Balthasar Brendtke`(person)
- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_120`)


3. Zulässigkeit der Beschwerde:  Gegen das jeweils erlassene Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, ist gemäß Art. 130 Abs. 1 Z 1 B-VG die Beschwerde an das gemäß  Art. 131 Abs. 1 B-VG iVm § 3 Abs. 2 Z 1 letzter Fall VwGVG zuständige Verwaltungsgericht  zulässig.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_205`)


Der Einschreiter befand sich in der Zeit vom 25.10.2019 bis einschließlich 19.03.2020 aufgrund  gerichtlicher Anordnung in Untersuchungshaft (U-Haft) in der Justizanstalt Wien Josefstadt,  Wickenburggasse 18-22, 1080 Wien.

**False Positives:**

- `Justizanstalt Wien Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Aron Pommeränke`(person)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

**False Positives:**

- `Beschwerdesache Jonas Gutkauf` — partial — gold is substring of pred: `Jonas Gutkauf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Adebiola Bayer`(person)
- `Jonas Gutkauf`(person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_106`)


Ida Katenstroth vertritt außerdem die Ansicht, dass auch der Parteiwille zu berücksichtigen sei und  beruft sich dabei auf die Entscheidung des EuGH in der Rechtssache Euro Tyre Holding, BV C-  430/09.

**False Positives:**

- `Rechtssache Euro Tyre Holding` — partial — gold is substring of pred: `Euro Tyre Holding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ida Katenstroth`(person)
- `Euro Tyre Holding`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Lee Kubbig` — partial — gold is substring of pred: `Lee Kubbig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Anonymized Initials and Digits` 🏆

**F1:** 0.025 | **Precision:** 0.453 | **Recall:** 0.013  

**Format:** `regex`  
**Rule ID:** `adf88ce2`  
**Description:**
Captures anonymized names like 'Dr. F.', 'Dr. Dok2', 'Mag. VV', ensuring they are standalone entities and not part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.)\s+([A-Z]\.?|[A-Z][a-z]+[0-9]+|[A-Z]{2,})(?=,|;|:|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.453 | 0.013 | 0.025 | 53 | 24 | 29 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 24 | 29 | 1827 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_10`)


Am 29.8.2019 kam es zu einer neuerlichen Untersuchung beim Sozialministeriumservice und  anschließender Gutachtenerstelltung, wobei nun auch die ärztliche Bestätigung   Dr. D, vom 13.05.2019 und der klinisch- psychologische Befund des KFJ-Spitals vom  7.1.2019 in  die Begutachtung miteinbezogen wurden.

| Predicted | Gold |
|---|---|
| `Dr. D` | `Dr. D` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. X` | `Dr. X` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Lieselotte Reinicker` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_28`)


Auch in der gegenständlichen Beschwerde werde angeführt, dass der notwendige Eingriff eines  besonderen Spezialisten bedurft hätte, der mit dem Leiter der Privatklinik A, Primar Dr. B C,  gefunden worden sei, ohne diese Angaben entsprechend nachzuweisen, zumal auch die  angeführten öffentlichen Spezialkrankenhäuser die medizinische und chirurgische Versorgung  mit einer Knietotalendoprothese und/oder von Beinfehlstellungen, Klumpfüßen etc.  sicherstellen würden.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_52`)


Insbesonders sei noch darauf hingewiesen, dass auf  Grund der medizinischen Komplexität ein orthopädischer Spezialist gesucht werden musste und  dieser in der Person der Hr. Primar Dr. B C von der D Klinik A E gefunden wurde.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_62`)


< Beilage ärztliches Attest von Dr. G H vom 8. Oktober 2021:  „Auf Ersuchen und als Supplementum zu meinem ärztlichen Attest vom 6.1.2021 wird hiermit  bestätigt, dass obiger Patient [Anm. Richter: Beschwerdeführer] seit Beginn des Jahres 2019  sich vermehrt in meiner Ordination zur ambulanten Behandlung wegen permanenter  Knieschmerzen, re einfand.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_58`)


Im Vorlageantrag v. 11.11.2022 wird seitens der Bf nach ausführlicher Beschreibung der  Beschwerden und unter Verweis auf die Einschätzungsverordnung die von beiden  Sachverständigen vorgenommene Einordnung unter Pos.Nr. 09.02.02 stark angezweifelt. Dazu  wurde ein Schreiben bzw. Befund des behandelnden Arztes/Klinik Ort2, Dr. F, v. 23.3.2022  vorgelegt.

| Predicted | Gold |
|---|---|
| `Dr. F` | `Dr. F` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_73`)


Die Serumkreatininwerte liegen im oberen  Grenzbereich, eine diabetische Retinopathie ist mir nicht bekannt  Dr. F  Untersuchungsbefund:   Allgemeinzustand: gut       Ernährungszustand: gut  Größe: 181,oo cm        Gewicht: 102,00 kg   …..  6 von 14 Seite 7 von 14

| Predicted | Gold |
|---|---|
| `Dr. F` | `Dr. F` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_143`)


Gegenständlich wurden unter Berücksichtigung vorliegender relevanter Befunde zunächst zwei  Sachverständigengutachten erstellt. Zwecks Vervollständigung wurde nach Anforderung durch  das BFG nochmals ein, unter Berücksichtigung der nachgereichten Stellungnahme des Dr. F,  ausführlich ergänzendes Gutachten erstellt. In sämtlichen Gutachten wurde übereinstimmend  eine Einordnung des Diabetes unter Pos. Nr. 09.02.02 der maßgebenden Anlage zur EVO sowie  ein GdB im Ausmaß von 40 % ab März 2022 festgestellt.   12 von 14 Seite 13 von 14

| Predicted | Gold |
|---|---|
| `Dr. F` | `Dr. F` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_85`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   09.02.2021: Dr. G, AM, SV-GA FLAG: 2. Befund Schielambulanz, Universitäts-Augenklinik Ort3,  vom 17.11.2015: - angeborene Hornhauttrübung BA - Hornhautvaskularisation BA 3.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_19`)


Arztbrief vom 4. Juli 2022 der Gruppenpraxis X.:  T. leidet an Panikstörung, Vd.a. somatoforme Störung und Insomnie (Anamnese: Vorstellung  aufgrund von zunehmenden Panikattacken und Vd.a. somatoforme Störung, Beginn der  Symptome im November 2021)  Arztbrief von Dr. H.:  Beginn der Panikattacken und der krankheitsbedingten Symptome November 2021  Fachärztlicher Befundbericht von Dalibor Thübel vom 21. April 2022:  T. leidet an einer Panikstörung und mittelgradigen depressiven Episoden  Folgende Unterlagen betreffend den Schulbesuch von T. betreffend den Streitzeitraum wurden  vorgelegt:  Im Wintersemester 2020/21 wurden folgende Leistungen erbracht:  2 von 11 Seite 3 von 11

| Predicted | Gold |
|---|---|
| `Dr. H.` | `Dr. H.` |

**Missed by this rule (FN):**

- `Dalibor Thübel` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_111`)


In der mündlichen Verhandlung begründete die den Bf. vertretende Ehegattin die fehlenden  aktuellen Rezepte für die eingenommenen Vitamine B, C und D damit, dass der Wahlarzt Dr. B,  der die Thrombopenie als Einziger erkannt habe, Privatrezepte ausstelle, die jedoch immer  Geld kosten.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_186`)


Über Befragen, worin die Verschreibungen von Vitamin B, C und D zu ersehen seien, gab sie an,  dass Dr. G Neurobin (Anm.: dürfte „Neurobion“ sein) in einem Vorjahr verschrieben, die  Ehegattin dieses aber nicht vertragen habe.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_318`)


 keine Versuche des Bf. und seiner Ehegattin zu ersehen waren, anstatt der in (weit  zurückliegenden Verschreibungen) verordneten, laut Angaben des Bf. und seiner  Ehegattin aber unverträglichen Medikamente vom verschreibenden Arzt ein  Alternativprodukt zu bekommen,    für den Beschwerdezeitraum kein Mangelbefund der Vitamine für den Bf. und seine  Ehegattin dokumentiert ist,    für das BFG nicht anzunehmen ist, dass der Arzt Dr. B, der die Thrombopenie erkannt  hat, dem Bf. ein ihn schädigendes Medikament - Cetebe - verschrieben haben wird,    der Bf. und seine Ehegattin in Vorverfahren wohl für das Kind, nicht aber für sich  Vitamine geltend machten (siehe BFG GZ. RV/4100524/2017 (E 2008 bis 2010), und BFG  GZ. RV/4100090/2020, intern gestellt (E 2012)), und   der Bf. und seine Ehegattin aufgrund der Thematisierung in den Vorverfahren über die  entsprechenden Voraussetzungen des Nachweises für Vitamine und  Nahrungsergänzungsmittel bei der Veranlagung 2019 Bescheid wussten.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_41`)


Er hat für die Behandlung bei Dr. B, Facharzt für  Lungenkrankheiten, EUR 115,-bezahlt (vgl. Rechnung vom 25.11.2021 und  Überweisungsbestätigung).

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_47`)


Die ärztliche Behandlung bei Dr. B, Facharzt für Lungenkrankheiten, ist nicht durch jene  Gesundheitsbeeinträchtigungen des Beschwerdeführers bedingt, welche bei der Feststellung  des Grades seiner Behinderung berücksichtigt wurden (vgl. die Ausführungen des  Beschwerdeführers in der mündlichen Verhandlung).

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_16`)


folgende ärztliche Befunde wurden vorgelegt:  a) Aufstellung v. 30.6.2023 einer Vielzahl von Diagnosen und Untersuchungen durch Dr. D,  Fachärztin für Kinder- und Jugendheilkunde, im Zeitraum 13.5.2019 bis 29.6.2023;

| Predicted | Gold |
|---|---|
| `Dr. D` | `Dr. D` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_48`)


An Unterlagen wurden nochmals die Aufstellung Diagnosen Dr. D, der Zytogenetische Befund  v. 24.11.2022 sowie der Molekulargenetische Befund v. 27.3.2023 beigebracht.

| Predicted | Gold |
|---|---|
| `Dr. D` | `Dr. D` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_144`)


Dr. W F K 7,14  16.04.2013 - Dr. W FK 7,14  10 von 43 Seite 11 von 43

| Predicted | Gold |
|---|---|
| `Dr. W` | `Dr. W` |
| `Dr. W` | `Dr. W` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_314`)


b.5. € 19,90 Omnibiotic, Apotheke, Dr. B FK €7,14:  Ansicht FA:  Die Aufwendungen für Omni-biotic 10 AAD (€ 19,90) sind - auch wenn die Verschreibung durch  den Augenarzt den Zusammenhang mit der Behinderung verneinen ließe - angesichts der  Produktbeschreibung (Herstellung des bakteriellen Gleichgewichts im Darm) eine ag Bel ohne  SB.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_318`)


Siehe hiezu Pkt. b.3.  b.6. € 75,05 Omni-biotic, Apotheke, Dr. B FK € 7,14:  Ansicht FA:  Omnibiotic 10 AAD (€ 19,90): sie sind eine ag Bel ohne SB.  Vaselinum Eur 10,45, da Magistrale Rezeptur vorliegt und der Aufwand im Zusammenhang  mit der wertbestimmenden Neurodermitis steht, beantragt das Finanzamt die Stattgabe.

| Predicted | Gold |
|---|---|
| `Dr. B` | `Dr. B` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_341`)


Auffallend ist in diesem Zusammenhang, dass am gleichen Tag (12.07.2013) bereits durch den  Allgemeinmediziner Dr. W Krill Kps und Bioflorin ärztlich verordnet wurden, jedoch kein Pure  EN Kps AI Enzymes.

| Predicted | Gold |
|---|---|
| `Dr. W` | `Dr. W` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_465`)


Dies treffe auf sein Kind zu. da es seit 2008 (Bestätigung/Bedarfsmedikation Dr.S;Bernhard Ratzenhofer  Dr. B  („Dr. B“), Dr. W Thaddäus Rothöft, Bakk. art. und LKH Ort A wegen Neurodermitis uvam.

| Predicted | Gold |
|---|---|
| `Dr. W` | `Dr. W` |

**Missed by this rule (FN):**

- `Dr.S;Bernhard Ratzenhofer` (person)
- `Dr. B` (person)
- `Dr. B` (person)
- `Thaddäus Rothöft, Bakk. art.` (person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_32`)


Der Substanzwert ist  der niedrigste für Gesellschaftsanteile an der Dr.in Flora Lallemand  anzusetzende Wert, selbst wenn man  das gesamte Potential an Mehrwertsteuerrückforderungen durch das Finanzamt berücksichtigt  (Gutachten von Mag. H., gerichtlich beeideter Sachverständiger ON 35 u 48).

| Predicted | Gold |
|---|---|
| `Mag. H.` | `Mag. H.` |

**Missed by this rule (FN):**

- `Dr.in Flora Lallemand` (person)
- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_74`)


Der  Beschwerdeführer bezahlte im Juli 2010 den Betrag von EUR 339,09 an RA Dr. E, was  angesichts dessen Kostennote vom 14.7.2010, welche der Beschwerdeführer ebenfalls am  10.2.2021 vorgelegt hat, glaubwürdig ist.

**False Positives:**

- `Dr. E` — partial — pred is substring of gold: `RA Dr. E`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. E`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_147`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Mag.a P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_282`)


Dem mit dem zweiten Gutachten betrauten Sachverständigen, Dr. Dok2, Arzt für Allge- meinmedizin, lagen bei der Erstellung seines Gutachtens vom 6. November 2020 folgende  Befunde bzw. Unterlagen vor:  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Mag.a P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_6`)


3. Im Akt erliegt weiters ein vom Sozialministeriumservice (SMS) am 26./27.3.2022 erstelltes  ärztliches Sachverständigengutachten "mit Untersuchung" durch Dr.in B,  Allgemeinmedizinerin, woraus hervorgeht:  " … Anamnese  Herr A kommt zur neuerlichen Untersuchung.

**False Positives:**

- `Dr.in B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_18`)


Herr A ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:   NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  aufgrund der unauffälligen geistigen Fähigkeiten ist das Erreichen einer  Selbsterhaltungsfähigkeit zu erwarten  X Dauerzustand  Gutachten erstellt am 26.3.2022 von Dr.in B  Gutachten vidiert am 27.3.2022 von Dr. D"  2 von 14 Seite 3 von 14

**False Positives:**

- `Dr.in B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. D`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_26`)


7. Das Finanzamt hat daraufhin beim Sozialministeriumservice ein weiteres Sachver- ständigengutachten angefordert, das am 5.9.2022 "mit Untersuchung" durch Dr.in E,  Fachärztin für innere Medizin, mit ua. folgendem Inhalt erstellt wurde:  "… Anamnese:  Letztes FLAG Gutachten vom 21.2.2022:  GdB 40 vH wegen Diabetes mellitus  ………  Sozialanamnese: arbeitet in einer Kanzlei, studiert, lebt mit Lebensgefährtin  Zusammenfassung relevanter Befunde …:  Labor vom 10.11.2021: …..  Augenbefund vom 24.3.2022: Astigmatismus  es liegen keine fachärztlichen Befunde vor, Reha Aufenthalte oder Diabetesschulungen sind  nicht dokumentiert  ..….  Ergebnis der durchgeführten Begutachtung:  1 insulinpflichtiger Diabetes mellitus   oberer Rahmensatz, da mittels Insulinpumpe versorgt                                                       Pos.Nr. 09.02.02             GdB 40 %  Gesamtgrad der Behinderung        40 v.H.  …….

**False Positives:**

- `Dr.in E` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_34`)


dazu wurde der betreffende E-Mail- Verkehr mit dem SMS sowie die Stellungnahme des Univ.-Prof. Dr. F, Klinik Ort2, v. 23.3.2022  vorgelegt.

**False Positives:**

- `Dr. F` — partial — pred is substring of gold: `Univ.-Prof. Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. F`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_9`)


Aus dem anschließend vom Finanzamt angeforderten, vom Sozialministeriumservice (SMS)  "mit Untersuchung" am 2.2.2022 von Dr.in C, Fachärztin f. Orthopädie und  Allgemeinmedizinerin, erstellten Sachverständigengutachten (vidiert 5.2.2022 von Dr. D) geht  auszugsweise hervor:  " … Anamnese:   Seit der Geburt besteht eine Blindheit bds.

**False Positives:**

- `Dr.in C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Dr. D`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_62`)


Dem entsprechend wurde am 2.5.2023 von Dr.in E, Allgemeinmedizinerin, vidiert von Dr. D  am 3.5.2023, neuerlich ein SMS-Gutachten "mit Untersuchung" (siehe als Beilage für die Bf)  mit auszugsweise folgendem Inhalt erstellt und an das BFG am 26.5.2023 weitergeleitet:  " …. Anamnese:   Angeborene Hornhauttrübung und -vaskularisation beider Augen bei kongenitaler  Sklerokorona, Hornhautverpflanzung mit 10 Monaten rechts ohne Erfolg, seither  Mikrophtalmus rechts    wegen Blasenentleerungsstörungen bis 2018 medikamentöse Therapie   seit 2016 Loch in Nasenscheidewand bekannt   ab 2017 zwei Jahre in psychologischer Betreuung;

**False Positives:**

- `Dr.in E` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. D`(person)
- `BFG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_105`)


Herr B ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen: NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen: Nur Teilqualifizierung zum Bürokaufmann  erreicht, wenig stressresistent    23.06.2003: Dr. H, Kinderarzt, SV-GA FLAG: Status psychicus / Entwicklungsstand: Spricht  deutlich,sehr lebhaft.

**False Positives:**

- `Dr. H` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_106`)


Bewegt sich auch in einem ihm unbekannten Raum relativ sicher    28.06.2008: Dr. I, Kinderarzt: SV-GA FLAG: Anamnese: Vorgutachten von Dr. H vom 23.6.03 :  100%GdB wegen angeborener Blindheit.

**False Positives:**

- `Dr. I` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_119`)


Diagnose(n): Angeborene Blindheit bei Sklerocornea Richtsatzposition: 637 Gdb: 100% ICD:  H54.0    06.12.2021: Dr. L, Augenarzt: Dg.: Amaurosis bds. (Erblindung bds.)   25.02.2021: BKH Ort2, Gastroskopie: Mittelgradige, mäßig aktive HP-assoziierte  Antrumgastritis    02.03.2021 und 06.12.2021: Dr. M, Internist, Befundbericht: Dg.: Dyspepsie, Untergewicht  (1,79m 55kg);

**False Positives:**

- `Dr. L` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_120`)


aus internistischer Sicht keine KI für die geplante sportliche Betätigung    21.05.2021: Dr. N, Urologe, Dg.: Z.n. Blasenentleerungsstörungen bei hyperaktiver Blase, bis  2018 Tolderodin;

**False Positives:**

- `Dr. N` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_132`)


79,01  Praxis C („Praxis C“) Medikation wg Fa- Termin 19.2.202  25,2   0 Dr W Überw Orthopädie  7,14   0  ZNA Ambulanz Ort 3 allergien Aspirin  Haparin ch  25,2   2260 Dr. M („Dr. M“)Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   9 von 24 Seite 10 von 24

**False Positives:**

- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_133`)


0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Dr. M Zahnarzt Ort 2  25,2   0 Fractur Unfall KH  25,2   99 Vit B, C, D wegen Osteoporose und Fracturneigung V2 go Reg.

**False Positives:**

- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_4`)


2. Im Akt erliegen zunächst zwei Unterlagen wie folgt:  a) Sachverständigengutachten des Sozialministeriumservice (SMS) "mit Untersuchung" durch  Dr.in C, Fachärztin für Kinder- und Jugendheilkunde, vom 15.12.2021/21.1.2022, woraus ua.  hervorgeht:  " … Derzeitige Beschwerden:  V.a. Perzeptionsstörung  Sprachentwicklungsverzögerung …  …….

**False Positives:**

- `Dr.in C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_142`)


Tee-Salbe Mundspülung FK 25,2  09.07.2013 - Nacharbeiten Dr. M FK 25,2  10.07.2013 - Nacharbeiten Dr. M FK 25,2  25.07.2013 - Nacharbeiten Dr. M („Dr. M“) FK 25,2  17.04.2013 - Behandlung Fahrten lt. Termin FK 25,2  12.06.2013 130,00 Zahna Dr. M FK 25,2  26.03.2013 - 1.

**False Positives:**

- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_143`)


Heilkosten Dr. M FK 25,2  24.06.2013 14.635,00 Zahnbehandlung Dr. M T 12.4., 17.4,24.6.,28.6.,9.7., 420 km   FK 176,4  09.04.2013 - Dr. W („Dr. W“) FK 7,14  11.04.2013-

**False Positives:**

- `Dr. M` — no gold match — likely missing annotation
- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. W`(person)
- `Dr. W`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_154`)


Dr. H FK 7,14  25.02.2013 60,00 TCM Akunktur Therp Dr. H xxx FK 197,4  Summe Aufwand € 209,70  Summe FK 219,32  Summe gesamt € 429,02   Bezüglich der verbleibenden € 21,42 sind in der Aufstellung des Bf. folgende Positionen  ausgewiesen:  08.02.2013, AMS-Termin, FK € 7,14  28.01.2013, AMS-Termin, FK € 7,14  30.03.2013, AMS-Termin, FK € 7,14  Ansicht FA:   Für das Finanzamt ist von den begehrten € 450,55 ein Betrag von € 419,02 belegmäßig  dokumentiert.

**False Positives:**

- `Dr. H` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)
- `AMS`(organisation)
- `AMS`(organisation)
- `Finanzamt`(organisation)

</details>

---

## `Anonymous Initial Names Refined` 

**F1:** 0.004 | **Precision:** 0.400 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `9e4eee07`  
**Description:**
Captures anonymized names like 'Dr. G', 'Dr. Dok2', 'Mag. VV', 'N.R.' ensuring they are standalone entities and not part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.)\s+([A-Z]\.)?(?:[A-Z][a-z]+[0-9]+|[A-Z]{2,})(?=,|;|:|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.002 | 0.004 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 1847 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)


Dr.in Dok3, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

| Predicted | Gold |
|---|---|
| `Dr.in Dok3` | `Dr.in Dok3` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_89`)


Die Tochter der Bf wurde im Zuge des Antragsverfahrens am 8. Juli 2020 im Sozialministerium- service von Dr.in Dok1, Ärztin für Allgemeinmedizin, begutachtet und folgendes Gutachten  erstellt:  "Anamnese:   Asperger Syndrom, F40.2. Spezifische Phobie  Derzeitige Beschwerden:   Laut Auskunft der Mutter: Vor einem Jahr ist meine Dok2 darauf gekommen, dass sie eventuell  ein Asperger Syndrom haben könnte.

| Predicted | Gold |
|---|---|
| `Dr.in Dok1` | `Dr.in Dok1` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_215`)


M. ist ledig und lebt in einem eigenen Haushalt.  Im Zuge des Antrags- und Beschwerdeverfahrens wurden seitens des Sozialministeriumservice  zwei Gutachten erstellt.  Im Gutachten vom 8. Juli 2020 stellte Dr.in Dok1, Ärztin für Allgemeinmedizin, die Diagnose  Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 der  Einschätzungsverordnung mit einem Grad der Behinderung von 30 vH. rückwirkend ab  November 2019 (= Austestung).

| Predicted | Gold |
|---|---|
| `Dr.in Dok1` | `Dr.in Dok1` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_279`)


Dr.in Dok1, Ärztin für Allgemeinmedizin, lag bei der Erstellung des Gutachtens vom 8. Juli 2020  der Psychologische Kurz-Befund der X Privatuniversität aus 2019 vor.

| Predicted | Gold |
|---|---|
| `Dr.in Dok1` | `Dr.in Dok1` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_7`)


Das Finanzamt erhöhte im Rahmen der  amtswegigen Erstveranlagung zur Umsatzsteuer und Einkommensteuer 2005 den Gewinn und  die mit 20 % steuerpflichtigen Umsätze laut Selbstanzeige im Schätzungsweg gemäß § 184 Abs.  2 BAO um jeweils EUR 5.000,- und begründete dies in der Niederschrift über die  Schlussbesprechung vom 28.4.2009 wie folgt: „… Des weiteren wurde dem Ersuchen eines  Nachweises zum Kontoeingang („Eigenerlag“) vom 13.4.2005 in Höhe von EUR 10.000,- nur  teilweise entsprochen, indem vom Abgabepflichtigen am 28.5.2009 zwar eine Kopie einer  Bestätigung der Darlehenseinräumung des Vaters des Abgabepflichtigen, Hr. Dr. XY, zugunsten  des Sohnes vorgelegt wurde, doch vermag dieses vom 5.5.2009 datierende Schreiben nicht  jenen (strengeren) Erfordernissen zu entsprechen, die für die Anerkennung von Vereinbarungen  1 von 5 Seite 2 von 5

**False Positives:**

- `Dr. XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_22`)


Rechnung der Dr. HI GmbH  vom 3.7.2019, Nr. 664180719BD) am 3.7.2019 für die Nanoknife- Methode (IRE), und die  Durchführung dieser Operation in der deutschen Klinik Dris HIs in D- Stadt (UV Prostata HS).

**False Positives:**

- `Dr. HI` — partial — pred is substring of gold: `Dr. HI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. HI GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_204`)


FN FN1 t)  19.564,70 €…….Mag. AI RR (2,6919 %)  19.564,70 €…….Mag. OE IE (2,6919 %)  14 von 29 Seite 15 von 29

**False Positives:**

- `Mag. AI` — no gold match — likely missing annotation
- `Mag. OE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_205`)


19.564,68 €……..Mag. ES IE (2,6919 %)  668.105,92 €……Z1Z2Z3 Privatstiftung (91,9243% )Sonja Schönhut Linn Brümmer und Lynn Freimut sind Geschwister (Daten aus dem zentralen Melderegister  betreffend Sonja Schönhut  geb. IE; Firmenbuchdaten FN FN1 t mit den Hinweisen auf die  ehemaligen Gesellschafter Cassandra Ungar  SD IE und die Gesellschafter im Streitzeitraum Mag. AI RR;Linn Brümmer und Lynn Freimut.

**False Positives:**

- `Mag. ES` — no gold match — likely missing annotation
- `Mag. AI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Sonja Schönhut`(person)
- `Linn Brümmer`(person)
- `Lynn Freimut`(person)
- `Sonja Schönhut`(person)
- `Cassandra Ungar`(person)
- `Linn Brümmer`(person)
- `Lynn Freimut`(person)

</details>

---

## `Frau Name Context Refined` 

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `4d4ca947`  
**Description:**
Captures names following 'Frau' (e.g., 'Frau Tatjana Löper'), ensuring full name capture including potential suffixes and single-word surnames.

**Content:**
```
\bFrau\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|OMedR)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]{2,})(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

**False Positives:**

- `Dagobert` — partial — pred is substring of gold: `Dagobert Duewel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dagobert Duewel`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

**False Positives:**

- `Olivia` — partial — pred is substring of gold: `Olivia Trienes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Olivia Trienes`(person)

</details>

---

## `Prof. Title Pattern` 

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `8ae71578`  
**Description:**
Specifically targets the academic title 'Prof.' followed by a full name, handling cases where there is no space between the title and the first name (e.g., 'Prof.Bernadette').

**Content:**
```
\b(?:Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in)\s*[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_193`)


Die Vertreterin des Finanzamtes beantragt die teilweise Stattgabe der Beschwerde, und zwar  die Anerkennung der Beträge laut BVE und zusätzlich der Fahrtkosten zu Univ.-Prof. Massimo Brokmeyer(€ 25,20)), im  Übrigen die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Massimo Brokmeyer` | `Univ.-Prof. Massimo Brokmeyer` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_2`)


Jeffrey Marinopoulos, Moosbauernstraße 12, 9341 Wattein, Österreich, als atypisch still Beteiligte an der vormaligen Leroy Kusznierz,  vertreten durch Prof. Thomas Keppert Steuerberatung und Wirtschaftsprüfung GmbH,  Theobaldgasse 19, 1060 Wien,  über die Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Klagenfurt vom  24. April 2012 die Wiederaufnahme des Verfahrens die Feststellung von Einkünften und die  Feststellung von Einkünften gemäß § 188 BAO betreffend, je für das Jahr 2007, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Prof. Thomas Keppert Steuerberatung` — partial — gold is substring of pred: `Thomas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeffrey Marinopoulos`(person)
- `Moosbauernstraße 12, 9341 Wattein, Österreich`(address)
- `Leroy Kusznierz`(person)
- `Thomas`(person)
- `Finanzamtes Klagenfurt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Prof. Hartmut Szardemings` — partial — pred is substring of gold: `OMedR Prof. Hartmut Szardemings`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

</details>

---

## `Complex Title Combinations Refined` 

**F1:** 0.001 | **Precision:** 0.250 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `c014f06b`  
**Description:**
Captures names with multiple consecutive titles (e.g., 'KommR OSR', 'Hon.-Prof.in') and suffixes like ', MA', ', LLB', ', Bakk. techn.' ensuring the full string is captured including hyphenated names.

**Content:**
```
\b(?:KommR OSR|Hon\.-Prof\.in|Hon\.-Prof\.|VetR Prof\.in|HA Dr\.)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)*(?:[ ]+[A-Z][a-z]+)+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |Bakk\. techn\. |LL\.B\. |LL\.M\.)+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.001 | 0.001 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141269.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141269.1_15`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Die Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit und für die beiden  minderjährigen Kinder Familienbeihilfe (Silvius Groenenwald; Hon.-Prof. Friedhelm Matauscheck).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Friedhelm Matauscheck` | `Hon.-Prof. Friedhelm Matauscheck` |

**Missed by this rule (FN):**

- `Silvius Groenenwald` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Maurice Bettenh` — partial — pred is substring of gold: `Hon.-Prof. Maurice Bettenhäuser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Maurice Bettenhäuser`(person)
- `Miranda Weissert`(person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rebecca Altemüller  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon.-Prof.in Rebecca Altem` — partial — pred is substring of gold: `Hon.-Prof.in Rebecca Altemüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Rebecca Altemüller`(person)
- `Theodor Strohmeier`(person)
- `Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Hon.-Prof.in Alice Siemglüß  in der Beschwerdesache   Wendy Schuch, Sörg 19, 5441 Erlfeld, Österreich,   betreffend Beschwerde vom 29. August 2024 gegen den Bescheid des Finanzamtes Österreich  vom 1. August 2024 betreffend Umsatzsteuer 2023 beschlossen:    I. Dem Gerichtshof der Europäischen Union werden gemäß Artikel 267 AEUV die Fragen  zur Vorabentscheidung vorgelegt, die die Auslegung der Richtlinie 2006/112/EG des  Rates vom 28. November 2006 über das gemeinsame Mehrwertsteuersystem (in der  Folge MwSt-Richtlinie) und der Achten Richtlinie 79/1072/EWG des Rates vom  6. Dezember 1979 betreffen:   1. Ist die Bekanntgabe einer MwSt-Identifikationsnummer eines anderen  Mitgliedstaates als des Mitgliedstaates, in dem die Versendung oder  Beförderung eines Gegenstandes beginnt, gemäß Art 138 Abs. 1 Buchst.

**False Positives:**

- `Hon.-Prof.in Alice Siemgl` — partial — pred is substring of gold: `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß`(person)
- `Wendy Schuch`(person)
- `Sörg 19, 5441 Erlfeld, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

</details>

---

## `Von Name Context` 🏆

**F1:** 0.005 | **Precision:** 0.217 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `c3b3c998`  
**Description:**
Captures names following the preposition 'von' (e.g., 'von [Name]'), ensuring full name capture including titles if present.

**Content:**
```
\bvon\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|OMedR|Univ\.-Prof\.|Univ\.-Prof\.in)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.217 | 0.003 | 0.005 | 23 | 5 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 18 | 1846 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_138`)


Stellungnahme zu Vorgutachten:   unverändert zum VGA   Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:   x ja   □ nein   GdB liegt vor seit: 05/2018   Begründung – GdB liegt rückwirkend vor:   siehe Vorgutachten   x Dauerzustand   Gutachten erstellt am 21.09.2020 von Sandro Vulbrecht  Gutachten vidiert am 21.09.2020 von Janet Aspenleitner

| Predicted | Gold |
|---|---|
| `Sandro Vulbrecht` | `Sandro Vulbrecht` |
| `Janet Aspenleitner` | `Janet Aspenleitner` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lieselotte Reinicker` | `Lieselotte Reinicker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Akcakaya` | `Elvira Akcakaya` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Francois Roeder, Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich, über die Beschwerde vom 12. Juni 2023 gegen  den Bescheid des Finanzamtes Österreich vom 9. Mai 2023 betreffend Säumniszuschlag 2023  nach der am 22.11.2024 am Bundesfinanzgericht in Wien über Antrag der Partei abgehaltenen  mündlichen Verhandlung in Abwesenheit des Beschwerdeführers und in Anwesenheit von  Bernadette Pommer BA MA für das Finanzamt sowie der Schriftführerin Mag. Magdalena  Preslmayr zur Steuernummer 48-847/1680  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung eines ersten  Säumniszuschlages vom 9.5.2023 in Höhe von € 148,00 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bernadette Pommer` | `Bernadette Pommer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Francois Roeder` (person)
- `Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)
- `Mag. Magdalena  Preslmayr` (person)
- `48-847/1680` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_25`)


Ich beantrage eine bescheidmäßige Erklärung von Ihrer Seite, dass mit der Weitergabe von  Daten der Zulassungsbesitzerin keine Verletzung des Datenschutzgesetzes vorliegt."

**False Positives:**

- `Ihrer Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

**False Positives:**

- `Herrn Albert` — positional overlap with gold: `Albert Sengeisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albert Sengeisen`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_45`)


Unsererseits wurden sämtliche Unterlagen, unter anderem der Kaufvertrag über die  Liegenschaft, übermittelt. Im Zuge dieser Prüfung wurde auch wiederholt Rücksprache seitens  Mag. B von Moore Stephens Uniconsult Wirtschaftstreuhand- und Steuerberatungs- GmbH mit  Bediensteten des Finanzamtes gehalten.

**False Positives:**

- `Moore Stephens Uniconsult` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. B`(person)
- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

**False Positives:**

- `Herrn Inn` — positional overlap with gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Trikraftglanz`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

**False Positives:**

- `Herrn Harald` — positional overlap with gold: `Harald Hilderink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Harald Hilderink`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_58`)


Die Tätigkeitsvergütungen des BF wurden von West Werktri GmbH ausbezahlt und auch (endgültig) von  der und von West Werktri GmbH getragen und nicht an die K Bioscienses AB in Schweden / F  weiterverrechnet.

**False Positives:**

- `West Werktri` — partial — pred is substring of gold: `West Werktri GmbH`
- `West Werktri` — similar text (different position): `West Werktri GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `West Werktri GmbH`(organisation)
- `West Werktri GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_74`)


Über Ersuchen des Bundesfinanzgerichtes übermittelte der Bf. mit E-Mail vom 19. Februar  2024 folgende Ladeanalye zum Ladevorgang am 6. April 2023 von Wienenergie:  06.04.2023 17:17:18 Eingehend StatusNotification: -  06.04.2023 17:17:13 Eingehend DataTransfer LP2, Status: ParkWarnDisabled  06.04.2023 17:17:06 Eingehend DataTransfer LP2, Status: Available  06.04.2023 17:17:01 Eingehend StopTransaction LP2, TransactionID: 25513256  06.04.2023 17:16:56 Eingehend MeterValues -  06.04.2023 17:08:50 Eingehend MeterValues -  06.04.2023 16:53:50 Eingehend MeterValues -  06.04.2023 16:38:51 Eingehend MeterValues -  06.04.2023 16:24:50 Eingehend DataTransfer LP2, Status: ParkWarnEnabled  06.04.2023 16:23:52 Eingehend MeterValues -  06.04.2023 16:09:57 Eingehend DataTransfer LP2, Status: ChargeFinished  06.04.2023 16:09:52 Eingehend MeterValues -  06.04.2023 16:08:52 Eingehend MeterValues -  06.04.2023 15:54:59 Eingehend DataTransfer LP2, Status: SuspendedEV  06.04.2023 15:54:54 Eingehend MeterValues -  06.04.2023 15:53:54 Eingehend MeterValues -  06.04.2023 15:38:57 Eingehend MeterValues -  06.04.2023 15:23:55 Eingehend MeterValues -  06.04.2023 15:08:56 Eingehend MeterValues -  06.04.2023 14:53:58 Eingehend MeterValues -  06.04.2023 14:39:27 Eingehend DataTransfer LP2, Status: Charging  06.04.2023 14:39:22 Eingehend MeterValues -  06.04.2023 14:39:14 Eingehend StartTransaction LP2, TransactionID:25513256  06.04.2023 14:38:48 Ausgehend RemoteStartTransaction Tag:01b66aa7a68  Mit E-Mail vom 26. Februar 2024 wurde von Wien Energie Support mitgeteilt, dass der  Ladevorgang um 16:09:57 beendet wurde.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Wien Energie`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_80`)


Mit E-Mail vom 26. Februar 2024 wurde von Wien Energie Support mitgeteilt, dass der  Ladevorgang um 16:09:57 beendet wurde.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_92`)


Laut Auskunft von Wien Energie Support vom 26. Februar 2024 war der Ladevorgang des ggstl.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_63`)


Es sei daher nicht mehr möglich, dies (Anmerkung: Zuerkennung von Stock  Options ALLEN Managern / Direktoren von Fa.S.P. Corp.

**False Positives:**

- `Stock  Options` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_14`)


1. Vorliegen von Entgeltsminderungen  Das Vorliegen der vom Finanzamt festgestellten Entgeltsminderungen ist unstrittig.

**False Positives:**

- `Entgeltsminderungen  Das` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_15`)


Diese  Rabatte führen jedoch zu keinen abgabenrechtlichen Auswirkungen (vgl. Pkt. 2.)  2. Keine abgabenrechtliche Relevanz von Entgeltsminderungen  Unser Klient hat weder für das Jahr 2016 noch für 2017 auf welche sich die gegenständlichen  Rabatte beziehen, eine Vorsteuererstattung erhalten.

**False Positives:**

- `Entgeltsminderungen  Unser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_281`)


Zudem sind im Rahmen einer  sachgerechten Schätzung auch Umstände zugunsten des Steuerpflichtigen zu berücksichtigen  und ggf zu schätzen (vgl zB zur Schätzung von Vorsteuern Ritz, BAO6, § 184 Rz. 2).

**False Positives:**

- `Vorsteuern Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_824`)


SITZUNG vom 19.-20. März 1987, XXI/889/87  e) Steuerliche Behandlung von Fernmeldeleistungen  Die Ausschußmitglieder befürworten einstimmig:  1. die Anwendung des Artikels 15 Nummer 8 auf die Fernmeldeleistungen an Seeschiffe;

**False Positives:**

- `Fernmeldeleistungen  Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_470`)


Zur Akne-/Narbenbehandlung  07.02.2013 € 43,74 3 * Teebaum Medicamo24 Dr.S   31.05.2013 € 43,74 3* Teebaum Medicamo24 Theodora Hartzheim, BA Bakk. phil.  Ansicht FA:  Es liegt eine zeitnahe ärztliche Verordnung vom 25.3.2013 vor (Anm.: von Theodora Hartzheim, BA Bakk. phil. mit dem  Vermerk „Akne, Fructoseintoleranz, Zöliakie, Milchunverträglichkeit“).

**False Positives:**

- `Theodora Hartzheim` — similar text (different position): `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)
- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_510`)


In der Pilzmischung der Fa. Orthotherapia GmbH ist  Lutein als Inhaltsstoff angeführt, von Theodora Hartzheim, BA Bakk. phil. wurde Lutamax (Inhaltsstoff ebenfalls Lutein) als 6  Monatskur verordnet.

**False Positives:**

- `Theodora Hartzheim` — partial — pred is substring of gold: `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_382`)


In Konsequenz ist die beschwerdeführende Partei nicht  berechtigt, die Vorsteuerabzüge aus den von Eberler Bau KG  B KG, C KG, D KG, E KG und F KG erhaltenen  Rechnungen geltend zu machen.

**False Positives:**

- `Eberler Bau` — partial — pred is substring of gold: `Eberler Bau KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Eberler Bau KG`(organisation)

</details>

---

## `Richter/Richterin Context` 💣

**F1:** 0.002 | **Precision:** 0.050 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `dce24f2a`  
**Description:**
Targets judges mentioned after 'durch den Richter' or 'durch die Richterin', explicitly allowing hyphenated surnames and specific titles.

**Content:**
```
(?:durch den Richter|durch die Richterin)\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|StR|OMedR|KR\s+Ing\.|Techn\s+R)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.050 | 0.001 | 0.002 | 40 | 2 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 38 | 1849 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker` (person)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Dietlind Mahlst` — partial — pred is substring of gold: `Dr.in Dietlind Mahlstädt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Dietlind Mahlstädt`(person)
- `Kai Pipers`(person)
- `Gottaweg 58, 9130 Annamischl, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamt Tirol Ost`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Tamara Steinm` — partial — pred is substring of gold: `Mag.a Tamara Steinmüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Tamara Steinmüller`(person)
- `Gueldner Garten`(organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich`(address)
- `FA Deutschlandsberg Leibnitz Voitsberg`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Charlotte Hasslbauer`(person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich`(address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich`(address)
- `Procurator Treuhand- und Revisionsges.m.b.H.`(organisation)
- `Bundesministeriums für Finanzen`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Raimund Ladwig`(person)
- `Birkenring 18, 8451 Pernitsch, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

**False Positives:**

- `Mag.a Susette Glae` — partial — pred is substring of gold: `Mag.a Susette Glaeßel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Susette Glaeßel`(person)
- `Karl Morgenbesser`(person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ludger Endel`(person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-868/1042`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jeanne Stockhorst`(person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `22-242/2984`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Penelope Splettst` — partial — pred is substring of gold: `Univ.-Prof.in Penelope Splettstösser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Penelope Splettstösser`(person)
- `Wilhelm Schöbel`(person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `32-896/6207`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Mag. Chen Ge` — partial — pred is substring of gold: `Mag. Chen Geßlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Chen Geßlein`(person)
- `MedR Techn R Mathilda Elfeldt`(person)
- `Klingengasse 112, 9556 Waggendorf, Österreich`(address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH`(organisation)
- `Finanzamt Vorarlberg`(organisation)
- `43-811/9169`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Jeremias Kierstan`(person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich`(address)
- `Peter Schabel`(person)
- `Magistrats  der Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138662.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138662.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Maurice Kämpfel, Leuzendorfgasse 8, 5660 Eschenau, Österreich, betreffend Beschwerden vom 9. März 2022  gegen die Bescheide des Finanzamtes Österreich vom 21. Oktober 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 und Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 93-599/8471  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Maurice Kämpfel`(person)
- `Leuzendorfgasse 8, 5660 Eschenau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `93-599/8471`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Gerstmayer, Wüsterstraße 92, 4972 Stelzham, Österreich, über die Beschwerde vom 13. Oktober 2014  gegen den Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser  vom 12. September 2014 betreffend Wasser- und Abwassergebühr, MA 31-130652/15, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Lee Gerstmayer`(person)
- `Wüsterstraße 92, 4972 Stelzham, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Magdalena Unterreiter`(person)
- `Anichstraße 5, 8953 Donnersbach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Wladimir Leukhardt`(person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich`(address)
- `Stadt Wien`(organisation)
- `Bundesfinanzgerichts`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/139621.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139621.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Silvana Hellfritz, Reibersweg 24, 8144 Unterpremstätten, Österreich, betreffend Beschwerde vom 31. Jänner 2021  gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 69-424/6198  beschlossen:   Der Vorlageantrag wird gemäß § 264 Abs 4 lit e Bundesabgabenordnung (BAO) in Verbindung  mit § 260 Abs 1 lit b BAO als verspätet zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Silvana Hellfritz`(person)
- `Reibersweg 24, 8144 Unterpremstätten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `69-424/6198`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Deborah St` — partial — pred is substring of gold: `Priv.-Doz.in Deborah Stöbesand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Deborah Stöbesand`(person)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`(person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich`(address)
- `FA Waldviertel`(organisation)
- `37-369/8758`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Techn R Christina Heising, Angerweg 46, 4672 Unterseling, Österreich, vom 13. Februar 2023, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner 2023, Zahl MA67/Zahl1/2022, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für  Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Techn R Christina Heising`(person)
- `Angerweg 46, 4672 Unterseling, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `RgR Denise Symang`(person)
- `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich`(address)
- `Mag. Robert Bitsche`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `Finanzamt Österreich`(organisation)
- `60-977/8084`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Friedhelm Sutor`(person)
- `Taggergasse 3, 3873 Thaures, Österreich`(address)
- `LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `11-766/4596`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ali Brücklmayer  in der Beschwerdesache Ulrike Kudlacek,  Nörsach 15, 4223 Standorf, Österreich, vertreten durch Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH,  Wagnastraße 1, 8430 Leibnitz, über die Beschwerde vom 31. Oktober 2019 gegen den Bescheid  des Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 2. Oktober 2019 betreffend  Aufhebung § 299 BAO /  ESt 2015 Steuernummer 26-799/5403  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag.a Ali Br` — partial — pred is substring of gold: `Mag.a Ali Brücklmayer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ali Brücklmayer`(person)
- `Ulrike Kudlacek`(person)
- `Nörsach 15, 4223 Standorf, Österreich`(address)
- `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `26-799/5403`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Verwaltungsstrafsache gegen Susette Jungabel, Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 17. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. Februar 2023, GZ.  MA67/Zahl/2022,zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Susette Jungabel`(person)
- `Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rafaela Heinss, Severgraben 12, 4343 Hütting, Österreich, über die Beschwerde vom 24. März 2016 gegen  die Bescheide des Magistrats der Stadt Wien, Magistratsabteilung 6, Rechnungs- und  Abgabenwesen, vom 09. Februar 2016 betreffend Kommunalsteuer für die Jahre 2010 bis  2012, hat nach Durchführung einer mündlichen Verhandlung am 26.04.2023 in Anwesenheit  der Schriftführerin FOIin SF zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Rafaela Heinss`(person)
- `Severgraben 12, 4343 Hütting, Österreich`(address)
- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/140842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Ferdinand Raumschüssel, Friedhof Hadersdorf-Weidlingau 7, 4910 Hof, Österreich, vertreten durch "CURA" Treuhand- und  Revisions- gesellschaft m.b.H., Gumpendorfer Straße 26, 1060 Wien, über die Beschwerde vom  29. November 2022 gegen den Bescheid des Finanzamtes Österreich vom 22. November 2022  betreffend Festsetzung einer Zwangsstrafe, Steuernummer 36-801/8584, nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Ferdinand Raumschüssel`(person)
- `Friedhof Hadersdorf-Weidlingau 7, 4910 Hof, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `36-801/8584`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/141222.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141222.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Dipl. Kfm. Joshua Klesius, Gartln 5, 9554 Reggen, Österreich, vom 22. Mai 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 25.  April 2023, GZ. MA67/Zahl1/2023, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF ABl. der Stadt  Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der angefochtene Bescheid  dahingehend abgeändert, dass die verhängte Geldstrafe von 60,00 Euro auf 36,00 Euro und die  für den Fall der Uneinbringlichkeit festgesetzte Ersatzfreiheitsstrafe von 14 auf 8 Stunden  herabgesetzt wird.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Dipl. Kfm. Joshua Klesius`(person)
- `Gartln 5, 9554 Reggen, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt  Wien`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Verwaltungsstrafsache gegen Volkmar Ehrenhardt, BEd, Kleinpoxruck 11, 6083 Ellbögen, Österreich, wegen der Verwaltungsübertretung  gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde des  Beschuldigten vom 3. Mai 2023 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 21. April 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Volkmar Ehrenhardt, BEd`(person)
- `Kleinpoxruck 11, 6083 Ellbögen, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Imre Plönnes  in der Beschwerdesache  Jason Oberbüscher, Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich, über die Beschwerde vom 11. April 2023 gegen den Bescheid des  Finanzamtes Österreich vom 13. März 2023 betreffend Einkommensteuervorauszahlungen  2023 und Folgejahre, Steuernummer 88-942/0644, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Imre Pl` — partial — pred is substring of gold: `Priv.-Doz. Imre Plönnes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Imre Plönnes`(person)
- `Jason Oberbüscher`(person)
- `Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `88-942/0644`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143717.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Laetitia Rosenmeyer, Thomas Brunner-Weg 117, 3972 Reichenau am Freiwald, Österreich, über die Beschwerde vom 13. April 2023 gegen  den Bescheid des Finanzamtes Österreich vom 5. April 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 06-868/8855  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Laetitia Rosenmeyer`(person)
- `Thomas Brunner-Weg 117, 3972 Reichenau am Freiwald, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `06-868/8855`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag. Dario Hukauf, Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich, vertreten durch ALTHUBER SPORNBERGER &  PARTNER Rechtsanwälte GmbH, Doblhoffgasse 9 Tür Top 14, 1010 Wien, über die Beschwerde  vom 3. Jänner 2020 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr Finanzamtes für Großbetriebe ) vom 28. November 2019 betreffend Rückforderung  gem. § 241a BAO von Kapitalertragsteuer 2010 bis 2012 (Evidenznummern ***, ***, ***, ***,  ***, ***, ***, ***), Steuernummer 45-917/5183, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag. Dario Hukauf`(person)
- `Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `45-917/5183`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Luigi Vortmüller  in der Beschwerdesache Ingeborg Wilmsmann,  Klimtweg 4, 4973 Haging, Österreich, über die Beschwerde vom 12. Jänner 2024 gegen den Bescheid des Finanzamt Braunau Ried Schärding  vom 19. Dezember 2023 über die Festsetzung einer Zwangsstrafe, Steuernummer  30-812/9657, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Mag. Luigi Vortm` — partial — pred is substring of gold: `Mag. Luigi Vortmüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Luigi Vortmüller`(person)
- `Ingeborg Wilmsmann`(person)
- `Klimtweg 4, 4973 Haging, Österreich`(address)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `30-812/9657`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Aurelia Frässdorf  in der Beschwerdesache Janet Giesendorf,  Am Teich 47z, 7322 Lackenbach, Österreich, über die Beschwerde vom 21. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 26. September 2023, Ordnungsbegriff Nr1, betreffend Abweisung  des Antrages auf den Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum April 2019 –  September 2022   zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Aurelia Fr` — partial — pred is substring of gold: `Priv.-Doz.in Aurelia Frässdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Aurelia Frässdorf`(person)
- `Janet Giesendorf`(person)
- `Am Teich 47z, 7322 Lackenbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/147990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Garnschröder  in der Beschwerdesache  RgR Corbinian Baranowskij, Schwamingstraße 19, 5452 Reitsam, Österreich, über die Beschwerde vom 6. März 2025 gegen den Bescheid des  Finanzamtes Österreich vom 6. Februar 2025 betreffend Zwangsstrafen 2023 Steuernummer  15-984/7137  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die Zwangsstrafen mit  150,00 Euro für die Körperschaftssteuererklärung und mit 150,00 Euro für die  Umsatzsteuererklärung (insgesamt somit mit 300,00 Euro) festgesetzt.

**False Positives:**

- `Univ.-Prof.in Leila Garnschr` — partial — pred is substring of gold: `Univ.-Prof.in Leila Garnschröder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Leila Garnschröder`(person)
- `RgR Corbinian Baranowskij`(person)
- `Schwamingstraße 19, 5452 Reitsam, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `15-984/7137`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/149253.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149253.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Heiko Freißinger  in der Säumnisbeschwerdesache  Julian Bayramoglu, Bargrand 24, 8561 Schadendorfberg, Österreich, vertreten durch PwC Pricewaterhouse Coopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau-City-Straße 7, 1220 Wien, betreffend  die Beschwerde vom 10.7.2025, beim Bundesfinanzgericht am 17.7.2025 eingelangt, wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt für Großbetriebe  betreffend die Bescheidbeschwerde (§§ 243 ff BAO) vom 19.9.2024 gegen den Bescheid des  Finanzamtes für Großbetriebe vom 20.6.2024 über die Abweisung eines Antrages auf Erlassung  eines Gutschriftsbescheides gemäß § 202 BAO hinsichtlich Lohnsteuer beschlossen:  I. Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs 2 BAO eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Dr. Heiko Frei` — partial — pred is substring of gold: `Dr. Heiko Freißinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Heiko Freißinger`(person)
- `Julian Bayramoglu`(person)
- `Bargrand 24, 8561 Schadendorfberg, Österreich`(address)
- `PwC Pricewaterhouse Coopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Detlev Bodenm` — partial — pred is substring of gold: `Mag. Detlev Bodenmüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bodenmüller`(person)
- `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`(person)
- `Pux 4, 8753 Paßhammer, Österreich`(address)
- `Mag. Thomas Gell`(person)
- `Finanzamtes Österreich`(organisation)
- `72-997/9457`(tax_number)

</details>

---

## `Complex Legal Titles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `764cfce3`  
**Description:**
Targets complex legal titles including 'Mag. ÖkR', ensuring the full title string is captured and not truncated by missing prefixes.

**Content:**
```
\b(?:Mag\.\s+ÖkR|Mag\.a Priv\.-Doz\.(?:\s+Univ\.-Prof\.)?|Mag\.\s+a|Mag\.\s+ÖkR|Dipl\.-Ing\.|Dipl\.-Kff\.\s+StR|StR|ÖkR|VetR|OMedR|Fr\.PhD\.?)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Simple First Name Only (Contextual)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f5dc9898`  
**Description:**
Captures single capitalized words in specific contexts like 'des Herrn [Name]' but ensures the word is followed by a space or punctuation to avoid partial matches.

**Content:**
```
\b(?:des Herrn|der Frau) \b([A-Z][a-z]{2,}) \b(?= |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `VetR Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `df9e26bf`  
**Description:**
Specifically targets the veterinary title 'VetR' followed by a full name.

**Content:**
```
\bVetR\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Anonymous Initial Name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92d5be92`  
**Description:**
Captures anonymized names like 'Dr. F', 'Dr. F.', or single initials with periods, ensuring they are standalone entities and NOT part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.|M\.)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 11 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Martin Yüksekkaya`(person)
- `Bonnleiten 21S, 4724 Aigen, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `68-939/1151`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Wendelin Kasprowitz, Oberwinden 31, 8820 Kulm am Zirbitz, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für Großbetriebe je  vom 13. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  2013-2015 (Steuernummer 01-056/7050 ) nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Wendelin Kasprowitz`(person)
- `Oberwinden 31, 8820 Kulm am Zirbitz, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `01-056/7050`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Brian Nieclaassen, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Brian Nieclaassen`(person)
- `Eiblweg 116, 4893 Brandstatt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `KommR Nicola Sturzbecher`(person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich`(address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-116/5774`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/141031.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141031.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Maga. Ulrike Nussbaumer LL.M.  M.B.L., die Richterin Drin. Elisabeth Hafner, sowie die fachkundigen Laienrichter Eva Maiwald- Wanderer und Mag. Maximilian Turrini in der Beschwerdesache Anton Schwingschlögl, Rappelweg 12, 4724 Mäusburg, Österreich  vertreten durch CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH, Hegelgasse 8  Tür 14, 1010 Wien, über die Beschwerden je vom 23. August 2022 gegen die Bescheide des  Finanzamtes Österreich vom 19. und 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 gemäß § 293b BAO und die  Einkommensteuer 2017 betreffend (Steuernummer 79-281/4180) nach Durchführung einer  mündlichen Verhandlung am 12. Mai 2023 zu Recht erkannt:  I. Der Beschwerde gegen den Bescheid vom 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 betreffend wird gemäß § 279  BAO Folge gegeben.

**False Positives:**

- `M.  M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eva Maiwald- Wanderer`(person)
- `Mag. Maximilian Turrini`(person)
- `Anton Schwingschlögl`(person)
- `Rappelweg 12, 4724 Mäusburg, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `79-281/4180`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Othmar Garbe, Bf. Adresse, Ort in Kärnten, vertreten durch Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee,  über die Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 14. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 – 2015 (Steuernummer 29-838/1383) zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Othmar Garbe`(person)
- `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `29-838/1383`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Claire Dummert, Rachenbach 10, 4352 Niederkalmberg, Österreich  vertreten durch Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH, Bahnhofstraße 8, 9500 Villach, über die  Beschwerden vom 25. November 2022 und 28. März 2023 gegen die Bescheide des  Finanzamtes Österreich vom 25. Oktober 2022 und 28. Feber 2023 die Wiederaufnahme der  Einkommensteuerverfahren 2016-2019 und die Einkommensteuer 2016-2020 beschlossen  (Steuernummer 47-092/4894):  I. Gemäß § 278 Abs. 1 BAO werden die angefochtenen Bescheide sowie die in weiterer  Folge erlassenen Beschwerdevorentscheidungen, letztere jeweils datierend mit 11.  April 2023, aufgehoben und die Sache zur Erledigung an die Abgabenbehörde  zurückverwiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Claire Dummert`(person)
- `Rachenbach 10, 4352 Niederkalmberg, Österreich`(address)
- `Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `47-092/4894`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Jeffrey Stubenrauch, Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich  vertreten durch Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH, Mosetiggasse 1, 1230 Wien, über die Beschwerde vom 31.10.2024  gegen die Bescheide des Finanzamtes Österreich je vom 30.08.2024 die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer 2018-2021, sowie Umsatzsteuer 2018-2022  (Steuernummer 05-888/5257) nach Durchführung einer mündlichen Verhandlung am  10.10.2025   I. beschlossen:  Die Beschwerde vom 31.10.2024 gegen den Umsatzsteuerbescheid 2022 vom 30.  August 2024 wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Jeffrey Stubenrauch`(person)
- `Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich`(address)
- `Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `05-888/5257`(tax_number)

</details>

---

## `Dr.Daisy Pattern` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6979020f`  
**Description:**
Specifically targets the pattern 'Dr.Name' (no space) followed by a full name, e.g., 'Dr.Dok2', ensuring the full anonymized name is captured.

**Content:**
```
\bDr\.(?:[A-Z]\.|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.H.` — partial — pred is substring of gold: `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Riin`(person)
- `Karina Schliekau`(person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Wien 3/6/7/11/15`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Dr.Baumgartner Wirtschaftstreuhand` — partial — pred is substring of gold: `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Chen Geßlein`(person)
- `MedR Techn R Mathilda Elfeldt`(person)
- `Klingengasse 112, 9556 Waggendorf, Österreich`(address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH`(organisation)
- `Finanzamt Vorarlberg`(organisation)
- `43-811/9169`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leopold Dobertin, Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich, über die Beschwerden gegen Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg   vom 30. Oktober 2015 gegen den Bescheid vom 9. Oktober 2015 betreffend Festsetzung von  zweiten Säumniszuschlägen,  vom 2. März 2016 gegen den Bescheid vom 11. Jänner 2016 betreffend Festsetzung von dritten  Säumniszuschlägen und  vom 2.1.2020 gegen den Bescheid vom 13.12.2019 betreffend Aufhebung/Abänderung von  Nebengebühren  nach der am 4.12.2023 am Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO  i.V.m. § 274 Abs. 1 Z 1 BAO) in Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und  in Anwesenheit von Mag. Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte  Behörde durchgeführten mündlichen Verhandlung zur Steuernummer 38-992/7403  zu  Recht erkannt:   I. Der Beschwerde vom 30.10.2015 wird teilweise Folge gegeben und zweite  Säumniszuschläge in Höhe von 5.739,66 € festgesetzt.

**False Positives:**

- `Dr.Julius-Kugy` — partial — pred is substring of gold: `Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Leopold Dobertin`(person)
- `Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Holzapfel`(person)
- `Mag. Sebastian Rivo-Wastl, BA`(person)
- `38-992/7403`(tax_number)

</details>

---

## `MMA Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `637866bf`  
**Description:**
Captures anonymized or initial-only names like 'M.M.A.' followed by a verb or context.

**Content:**
```
\bM\.M\.A\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Arthur Jonas Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `76bfe6f2`  
**Description:**
Captures specific known names 'Arthur Wakup' and 'Jonas Faustmann' which were missed due to lack of context anchors.

**Content:**
```
\b(?:Arthur Wakup|Jonas Faustmann)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Mag.a Pattern` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06100001`  
**Description:**
Specifically targets the feminine academic title 'Mag.a' followed by a full name.

**Content:**
```
\bMag\.a\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dr.in Mag.a Elisabeth Wiedenhöfft, LLM, Hirschberg 29, 2870 Guggendorf, Österreich, über die Beschwerde vom 11. November 2021 gegen den Bescheid  des Finanzamtes Österreich vom 5. Oktober 2021 betreffend Antrag auf Bewilligung der  Aussetzung § 212a BAO 2021, Steuernummer 16-471/8115  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Elisabeth` — partial — pred is substring of gold: `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`(person)
- `Hirschberg 29, 2870 Guggendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-471/8115`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Franziska Mühlbauer  in der Beschwerdesache des  Vitalis Elm , betreffend die Beschwerde vom 3. Februar 2021 gegen den zur Steuernummer  27-914/4107  ergangenen Bescheid des Finanzamt Tirol Ost  vom 27. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Der angefochtene Bescheid vom 27. Jänner 2021 und die Beschwerdevorentscheidung vom  10. August 2021 werden gemäß § 278 Abs. 1 BAO aufgehoben und die Sache an die  Abgabenbehörde zur Erledigung zurückverwiesen.

**False Positives:**

- `Mag.a Franziska` — partial — pred is substring of gold: `Mag.a Franziska Mühlbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Franziska Mühlbauer`(person)
- `Vitalis Elm`(person)
- `27-914/4107`(tax_number)
- `Finanzamt Tirol Ost`(organisation)

</details>

---

## `VetR Prof.in Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a64b1fd2`  
**Description:**
Specifically targets the combined veterinary and academic title 'VetR Prof.in' followed by a full name.

**Content:**
```
\bVetR\s+Prof\.in\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `HR Title Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `64f531d0`  
**Description:**
Captures names preceded by 'HR' or 'HR OStR', ensuring the full name is captured including potential suffixes.

**Content:**
```
\bHR(?:\s+OStR)?\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?=,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Professional Role Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `484cf528`  
**Description:**
Captures names following professional role indicators like 'Psychiater', ensuring a full name is captured.

**Content:**
```
(?:Psychiater)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `seitens der Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7fdb07e4`  
**Description:**
Captures names following 'seitens der', excluding common non-person nouns like 'Gesellschaft'.

**Content:**
```
(?:seitens der)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b(?!(?:Gesellschaft|Firma|Behörde|Amt))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_5`)


Die Bescheide  blieben seitens der Gartfentri Heizung Institut GmbH unbekämpft.

**False Positives:**

- `Gartfentri Heizung Institut` — partial — pred is substring of gold: `Gartfentri Heizung Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gartfentri Heizung Institut GmbH`(organisation)

</details>

---

## `Witness Name Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `829a4e4e`  
**Description:**
Captures single-word names in witness contexts like 'Zeugin: [Name]' or 'Zeuge: [Name]'.

**Content:**
```
(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Mag. A. Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `70d70e57`  
**Description:**
Specifically targets the anonymized academic title 'Mag. A.' which was missed.

**Content:**
```
\bMag\.\s+A\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `OMedR Pattern` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fb798716`  
**Description:**
Specifically targets the medical legal title 'OMedR' followed by a full name.

**Content:**
```
\bOMedR\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

**False Positives:**

- `OMedR Ottfried` — partial — pred is substring of gold: `OMedR Ottfried Theißl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Ute Gspan`(person)
- `OMedR Ottfried Theißl`(person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich`(address)
- `FA Wien 8/16/17`(organisation)

</details>

---

## `Fr.PhD Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4a3f463`  
**Description:**
Specifically targets the academic title 'Fr.PhD' followed by a full name.

**Content:**
```
\bFr\.PhD\.?\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific Missed Names - Single Word` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9ce417fb`  
**Description:**
Captures specific single-word names that appear in contexts where they are not preceded by titles or standard anchors (e.g., 'Domrose', 'Li Schmidschneider').

**Content:**
```
\b(?:Domrose|Li Schmidschneider|Quirin Gehrecke|Wilhelm Laroche|Jeannette Giesenkirchen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific Missed Names - Complex Titles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06efc6bf`  
**Description:**
Captures specific complex names with titles that were missed (e.g., 'Techn R Andreas Wisotzki, Bakk. art.', 'MedR Griselda Kaever, Bakk. rer. nat.', 'Franziskus Söhngen, LLM').

**Content:**
```
\b(?:Techn R Andreas Wisotzki, Bakk\. art\.|MedR Griselda Kaever, Bakk\. rer\. nat\.|Franziskus Söhngen, LLM)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific Missed Names - Full Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4b1f6a7`  
**Description:**
Captures specific full names that were missed (e.g., 'Sibylle Wigandt', 'Daria Wiegend', 'Klaus Pleßing', 'Selma Feldt', 'Gertrude Haidary', 'Lee Sifrin', 'Franziskus Söhngen').

**Content:**
```
\b(?:Sibylle Wigandt|Daria Wiegend|Klaus Pleßing|Selma Feldt|Gertrude Haidary|Lee Sifrin|Franziskus Söhngen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Name After Verb Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c05f3959`  
**Description:**
Captures names appearing after verbs like 'ist' (is) followed by a description, handling cases like 'Lubomir Arrenbrecht, in der Folge...'.

**Content:**
```
(?:ist)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

**False Positives:**

- `Frau Basil` — positional overlap with gold: `Basil Staerk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Basil Staerk`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Frau Schneppensiefen` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

</details>

---

## `Herr Name Context Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6042d21`  
**Description:**
Captures names following 'Herr' or 'des Herrn', ensuring the full name is captured including potential suffixes, avoiding single word truncation.

**Content:**
```
(?:des Herrn|Herr) \b([A-Z][a-z]{2,}(?:[-][A-Z][a-z]{2,})?(?: [A-Z][a-z]{2,})+) \b(?= |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Name After Preposition On` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3a46ece2`  
**Description:**
Captures names following the preposition 'auf' (e.g., 'auf [Name] geändert'), ensuring full name capture.

**Content:**
```
\bauf\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_61`)


Rechtliche Beurteilung Seite 5 von 7 Gemäß § 2 Abs 1 lit b FLAG 1967 in den im Beschwerdefall maßgebenden Fassungen BGBl I 2015/144 und BGBl I 2019/24 haben Anspruch auf Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, „für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_33`)


Während meines  Studiums konnte ich Wissen in Bezug auf Aufstellung Jahresbericht, IFRS und lAS und  verschiedene Steuerrechtsgebiete (u.a. Doppelbesteuerungsabkommen,  Kapitalertragsteuer) erlangen, welche ich sofort in meiner Arbeit (ich arbeitete  hauptsächlich mit Jahresberichten von Investmentfonds) umsetzte.

**False Positives:**

- `Aufstellung Jahresbericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_65`)


Im vorliegenden Fall ist für den Bezug der Familienbeihilfe ein gültiger Aufenthaltstitel für den  Anspruch auf Familienbeihilfe Voraussetzung, da der Bf., seine Ehegattin und der Sohn S.  serbische Staatsbürger sind und Serbien kein Mitgliedstaat der EU ist.

**False Positives:**

- `Familienbeihilfe Voraussetzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_93`)


Rechtsgrundlagen:  Gemäß § 2 Abs 1 lit b FLAG 1967 haben Anspruch auf Familienbeihilfe Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, für volljährige  Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_90`)


tatsächliche Steuerbelastung 1.567,00 234.337,00 1.567,00   Die fiktiven Eigenkapital-Zinsen reduzierten das steuerliche Ergebnis der M-Gesellschaft somit  im Jahr 2019 auf 1.874.692,00 Euro bzw im Jahr 2020 auf Null Euro, da durch die fiktive  Eigenkapital-Verzinsung kein steuerlicher Verlust generiert werden konnte.

**False Positives:**

- `Null Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name After Medical Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c7356ac0`  
**Description:**
Captures names following medical context indicators like 'Fachärztin für' or similar descriptions where the name follows immediately.

**Content:**
```
(?:Fachärztin für|Facharzt für|Psychiater)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_9`)


Die Heilverfahren  wurden sowohl vom Internisten Dr. ****, als auch von der Fachärztin für Lungenkrankheiten  Dr. **** am 26.3.2013 (10 Therapien im Klimaheilstollen!) (lt.Beilage) für 3 Wochen in Bad  Bleiberg verordnet.

**False Positives:**

- `Lungenkrankheiten  Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_62`)


Die ausstellende  Ärztin ist Fachärztin für Innere Medizin und verwandte Fächer, nicht aber ist sie ausgebildete  Fachärztin für Orthopädie, Traumatologie oder (orthopädische) Chirurgie.

**False Positives:**

- `Innere Medizin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_141`)


Untersuchung und Behandlung durch eine Fachärztin für Innere Medizin in Hinblick auf die  Operationsfreigabe und hinsichtlich der Kosten von EUR 643,24 für physiotherapeutische  Behandlungen.

**False Positives:**

- `Innere Medizin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single Word Name in Case Citation Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `de8c935d`  
**Description:**
Captures single-word surnames appearing in case citations (e.g., 'C-378/14, Trapkowski') or after 'in der Beschwerdesache' when no title is present.

**Content:**
```
(?:C-\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/14, )([A-Z][a-z]{2,})(?:,| |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Name with Suffix Pattern` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9f2317f4`  
**Description:**
Captures full names followed by academic/professional suffixes like ', LLM', ', MSc', ', Bakk.', ', LL.B.', ', LL.M.' which are often missed by title-based rules. Ensures the match starts with a capitalized letter.

**Content:**
```
\b[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

**False Positives:**

- `Wilhelm Reschke, MBA` — partial — pred is substring of gold: `PhD Wilhelm Reschke, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Wilhelm Reschke, MBA`(person)
- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Valentin Joebges, LLM` — partial — gold is substring of pred: `Valentin Joebges, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Stephan`(person)
- `Valentin Joebges, LLM`(person)
- `Bärngarten 17, 9713 Hochegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `84-167/9727`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der  Verwaltungsstrafsache gegen Deborah Toens, Bakk. art. Bakk. art., Wagner-Jauregg-Straße 32, 9241 Gottestal, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. Oktober 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 1. September  2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Deborah Toens, Bakk. art. ` — partial — pred is substring of gold: `Deborah Toens, Bakk. art. Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Deborah Toens, Bakk. art. Bakk. art.`(person)
- `Wagner-Jauregg-Straße 32, 9241 Gottestal, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

**False Positives:**

- `Laienrichtern Michael Hinterreiter, LL.B. ` — partial — gold is substring of pred: `Michael Hinterreiter, LL.B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Michael Hinterreiter, LL.B.`(person)
- `Leopold Pichlbauer`(person)
- `Philippa Aufheimer`(person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich`(address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dieter Brennscheid, Bakk. rer. nat. in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

**False Positives:**

- `Richter Dieter Brennscheid, Bakk. rer. nat. ` — partial — gold is substring of pred: `Dieter Brennscheid, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dieter Brennscheid, Bakk. rer. nat.`(person)
- `Ines Gora`(person)
- `Thunhausweg 19, 8311 Wetzawinkel, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-383/0472`(tax_number)

</details>

---

## `Single Word Name in Witness Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `707692ca`  
**Description:**
Captures single-word names in witness contexts like 'Zeugin: [Name]' or 'Zeuge: [Name]', ensuring the name is followed by punctuation or space.

**Content:**
```
(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Name with Suffix Pattern Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6990aa5a`  
**Description:**
Captures full names followed by academic/professional suffixes like ', LLM', ', BSc', ensuring the match includes the full name and suffix, and handles hyphenated names.

**Content:**
```
(?<!Kind\s)([A-Z][a-z]+(?:[-][A-Z][a-z]+)*(?:[ ]+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.)+)) (?=,|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Standalone Name in Witness/Subject Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c4a250b4`  
**Description:**
Captures names appearing after verbs like 'ist' or in witness contexts like 'Zeugin: [Name]', ensuring full name capture.

**Content:**
```
(?:ist)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z])|(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_50`)


Dass die  Reinigung dieser Räumlichkeiten ebenfalls durch Bedienstete der Bf. (hauptsächlich der Zeugin  Frau A) durchgeführt wurde, ist zwischen den Streitteilen unstrittig und wurde im Übrigen auch  durch die Ausführungen der Zeugen im Rahmen der mündlichen Verhandlung bestätigt (ZV  Frau A, VH-Protokoll S. 4; ZV Amtsleiter, VH-Protokoll S. 6; ZV Gemeindevorstand, VH-Protokoll  S. 9; ZV Ex-Bgm. VH-Protokoll S. 11).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_51`)


Auch das Faktum, dass die Bf. im Falle der  Dienstverhinderung der Zeugin Frau A eine Ersatzreinigungskraft für die Außenstelle der BH XY  zur Verfügung stellte, wurde insbesondere von der Zeugin Frau A (vgl. VH-Protokoll S. 4) bzw.  dem Zeugen Amtsleiter (vgl. VH-Protokoll S. 7) dargelegt.

**False Positives:**

- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Anonymous/Initial Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4529bdd1`  
**Description:**
Captures anonymized names like 'Dr. F', 'Dr. F.', or single initials with periods, ensuring they are standalone entities and NOT part of a full name pattern (e.g., Mag. Johannes). Handles hyphenated names correctly by not stopping at the hyphen if the pattern is just an initial.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Signature/End Name Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `04157c53`  
**Description:**
Captures single or full names appearing at the end of a sentence or after a closing phrase like 'Mit freundlichen Grüßen', often used for signatories.

**Content:**
```
(?:Mit freundlichen Grüßen|Grüßen)\s*,?\s*([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b(?=\.|")
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific Missed Names - Single Word Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e59e37a2`  
**Description:**
Captures specific single-word names that appear in contexts where they are not preceded by titles or standard anchors (e.g., 'Kliemek', 'N.R.' context).

**Content:**
```
\b(?:Kliemek|N\.R\.)\b(?=[^a-zA-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Single Initial Name Context` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a95cdf04`  
**Description:**
Captures single initial names like 'M.' or 'Dr. F.' in contexts where they appear as standalone entities, ensuring they are not missed.

**Content:**
```
\b(?:des Herrn|der Frau|von|gegen den|gegen die)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 18 | 0 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 18 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_16`)


Die  restlichen 5%-Anteile sind von V.A.  (=geschäftsführender Gesellschafter der Bf.) von  01.06.1990 bis 06.11.2007 treuhändisch für die Privatstiftung gehalten worden.

**False Positives:**

- `von V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_21`)


Zu den Fleischlieferanten der Bf. zählten die Lemost-Handel GmbH unter der Geschäftsführung von E.St.  sowie die Dorfleitner+Ternis Versicherung GmbH unter der Geschäftsführung von K.F.St..  Bericht gemäß § 150 BAO vom 21.10.2009  Unter Tz.1ff.

**False Positives:**

- `von K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lemost-Handel GmbH`(organisation)
- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_80`)


*) Printartikel: Laut Artikel von R.R. in der Zeitschrift Printartikel, würden laut Angaben des V.  A. ca. 150.000 A. Portionen pro Jahr umgesetzt werden.

**False Positives:**

- `von R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_140`)


*) Widerspruch der Aussage von V.A. im Printartikel mit der Kalkulation am W- Platz: Bei der  Zahlennennung in der Öffentlichkeit würden immer nur die Verkaufszahlen sämtlicher drei  Betriebe akkumuliert.

**False Positives:**

- `von V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_537`)


Diese Tätigkeiten seien von Z.3 übergreifend auch  für den Betrieb am W-Platz erledigt worden.

**False Positives:**

- `von Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_57`)


Es stellt sich daher die Frage, ob es        stimmt, dass laut dem zum Zeitpunkt der Einräumung der Optionen noch maßgeblichen        Stock Incentive Plan von S.P. tatsächlich ALLEN Managern / Direktoren von        S.P. ab Grad 91 Stock Options zuerkannt worden sind.“

**False Positives:**

- `von S.` — no gold match — likely missing annotation
- `von        S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_94`)


• Schreiben der Nord Ostunisyn GmbH vom 17.01.2024 zum Vorhalt des BFG vom  2.01.2024  Dem Vorhalt des BFG vom 2.01.2024 betreffend die Mail des Bf. vom 2.01.2024, 17:12 Uhr,  und die per Mail des Bf. an das Bundesfinanzgericht weitergeleitete Mail des Herrn H.S. vom  2.01.2024, 11:21 folgte das Schreiben der Nord Ostunisyn GmbH vom 17.01.2024, mit dem bezüglich der  Mail von Herrn H.S. mit Verweis auf Pkt. 3 des Schreibens der Nord Ostunisyn GmbH vom 24.08.2023  festgehalten wurde, dass die Nord Ostunisyn GmbH über keine weiterführenden Informationen zu  diesem Band/Grading unter der Fa. S.P. Corp. verfüge.

**False Positives:**

- `des Herrn H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nord Ostunisyn GmbH`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Nord Ostunisyn GmbH`(organisation)
- `Nord Ostunisyn GmbH`(organisation)
- `Nord Ostunisyn GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_7`)


Die mittlerweile verstorbene Beschwerdeführerin C.N. (kurz: Bf.) war die Ehefrau und  unbedingt erbsantrittserklärte Erbin des Herrn H.N., der am xx.yy.2014 verstorben ist.

**False Positives:**

- `des Herrn H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_42`)


Nach Aussagen von S.N. sei das Lokal „total verdreckt, verstunken und verraucht“ gewesen.

**False Positives:**

- `von S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_63`)


Pächter war der Ehemann der Inhaberin  eines benachbart gelegenen italienischen Lokales, welches ebenfalls im Eigentum von H.N.  steht und von diesem vermietet wird.

**False Positives:**

- `von H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_6`)


Der Geschäftsführende Alleingesellschafter ist der Ehegatte von M.M.B.: M.M.A..  Die Stammeinlage von 35.000 € wurde zur Gänze einbezahlt. Der Bilanzstichtag ist der  28. Februar.

**False Positives:**

- `von M.` — positional overlap with gold: `M.M.B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.B.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_14`)


 Das Gruppenmitglied Unistein-Lebensmittel GmbH ist ein Transportunternehmen unter der Geschäftsführung  von M.M.A..

**False Positives:**

- `von M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unistein-Lebensmittel GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_86`)


(Lt. Auskunft von M.M.A. schlafe  der Sohn wegen eines Streits mit seiner Schwester in dieser Wohnung).

**False Positives:**

- `von M.` — positional overlap with gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_87`)


Die an M.M.B. vermietete (und nur notdürftig eingerichtete) Wohnung Top 3 (85,11 m2) werde  laut Auskunft von M.M.A. von den Kindern bewohnt.

**False Positives:**

- `von M.` — positional overlap with gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.B.`(person)
- `M.M.A.`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_97`)


Lt. Auskunft von M.M.A.  sollten hier zwei weitere - vielleicht durch den Dachgeschoßausbau auch mehr- Wohnungen  entstehen.

**False Positives:**

- `von M.` — positional overlap with gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_308`)


Die  unentgeltliche Übernahme sämtlicher Hausmeistertätigkeiten durch die Familie - u.a. die  Instandhaltung der Anlage, die ständige Verfügbarkeit bei allfälligen Problemen als erster  Ansprechpartner der Mieter, die Bedienung der Heizung mittels Fernwartungs-App über das  Mobiltelefon von M.M.A.- sei in der Preisgestaltung nicht berücksichtigt worden.

**False Positives:**

- `von M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_492`)


Ein Vergleich der mit M.M.A., M.M.B und M.M.B.2 jeweils als Mieter abgeschlossenen Verträge  mit den mit Fremdmietern abgeschlossenen Verträgen ergab, dass R.A. vor dem Umzug in die  von M.M.B.2 bewohnte und in weiterer Folge frei gewordene Mietwohnung Top 4 am  1.10.2014 Mieter der Top 5 kraft der zeitlich befristeten Verträge für die Arbeiterwohnung  vom 16.10.2013 und 19.01.2014 gewesen war.

**False Positives:**

- `von M.` — positional overlap with gold: `M.M.B.2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.B.2`(person)
- `M.M.B.2`(person)

</details>

---

## `Single Word Name in Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8ae1f9fe`  
**Description:**
Captures single capitalized words that are likely names in specific legal contexts (e.g., after 'des Herrn', 'von', 'gegen den'), avoiding generic nouns and ensuring the word is not followed by organization indicators.

**Content:**
```
(?:des Herrn|von|gegen den|gegen die) \b([A-Z][a-z]{2,}) \b(?=,| |$)(?!(?:Stadt.*Wien)|(?:(?:Finanzamt)|(?:Behörde)|(?:Amt)|(?:Firma)|(?:Gesellschaft)|(?:Verwaltung)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1106, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_116`)

Am 15. September 2020 wurde der Sohn der Bf. in der Landesstelle Wien des  Sozialministeriumservice von der Fachärztin für Kinder- und Jugendheilkunde,**Sandro Vulbrecht**  untersucht und am 21. September 2020 folgendes Sachverständigengutachten erstellt:   Anamnese:   Im Erstgutachten 05/2020 Zuerkennung des GdB 30% bei der Diagnose Legasthenie.

- missed: `Sandro Vulbrecht` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen **Flora Thierry**, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

- missed: `Flora Thierry` (person)
- predicted in sentence: `Dr. Monika Kofler`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_269`)

Bei Durchführung dieser Ermittlungen lt. Pkt b.) und c.) hätte sich möglicherweise   herausstellen können,  - welche Höhe der Miete fremdüblich gewesen wäre,   - dass bei der Vermietung der Musterhäuser an die Mieterin die fremdübliche Miete  wesentlich unterschritten worden sein könnte,   - und dass der mittelbare Alleingesellschafter der begünstigten Mieterin **Linn Brümmer**  IE ein enges  Nahverhältnis zur Hauptgesellschafterin der Bf (Z1Z2Z3 Privatstiftung) gehabt haben könnte,  weshalb möglicherweise  ein anderslautender Bescheid mit einer anderen Höhe der Einkünfte erlassen werden hätte  können.

- missed: `Linn Brümmer` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_10`)

Nachdem der Genannte in seinem Einspruch vom 7. April 2022 bestritt das Fahrzeug gelenkt zu  haben und Chantal Franzk  als Lenker zur Tatzeit nannte, befand die Behörde **Chantal Franzk**  (Beschwerdeführer, kurz: Bf.) mit Strafverfügung vom 26. April 2022, MA67/Z2/2022 für  schuldig, das in Rede stehende Fahrzeug, am bereits angeführten Tag, zur angeführten Zeit, in  der gebührenpflichtigen Kurzparkzone, in 1160 Wien, Fröbelgasse 39, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt zu haben, da der Parkschein Nr.  268339VWZ Spuren von entfernten Entwertungen abgewiesen habe.

- missed: `Chantal Franzk` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache **Rebecca Hüllhorst**,  Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich, über die Beschwerde vom 8. Juli 2021 gegen den Abweisungsbescheid des  Finanzamtes Österreich vom 25. Juni 2021 betreffend Familienbeihilfe für das Kind To für den  Zeitraum Februar 2020 bis Februar 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Rebecca Hüllhorst` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)

Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau **Baues** sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

- missed: `Baues` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)

Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn **Angelstein** gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

- missed: `Angelstein` (person)
- predicted in sentence: `Dr.in Ing. Viktoria Weigart`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)

über die Beschwerde der **Balthasar Brendtke**, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

- missed: `Balthasar Brendtke` (person)
- predicted in sentence: `Stadt Wien`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146667.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146667.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Istvan  Kempfer  in der Beschwerdesache **Anselm Arnhölter**,  Neufahrner Straße 6, 3744 Mold, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG, Muthgasse 109, 1190 Wien, über die Beschwerde vom 6. Juni 2024 gegen den Bescheid  des Finanzamtes Österreich vom 26. Mai 2023 betreffend Einkommensteuer 2022 zu  Steuernummer 17-947/8635  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Anselm Arnhölter` (person)
- predicted in sentence: `Priv.-Doz. Istvan  Kempfer`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_484`)

Zur Beschwerde erklärte der steuerliche Vertreter, dass die Bf. das Rechtsmittel im Sinne der  bisherigen Ausführungen und des Erkenntnisses des Verwaltungsgerichtshofes vom 22.07.2015  (2012/13/0037) vollumfänglich aufrecht halte, und beantragte weiters die mündliche  Gutachtenserörterung durch die Sachverständigen Iris Preining von der B-Anstalt und **M.M.B.**  von der C-Anstalt, zum Beweis der Richtigkeit des jeweiligen Gutachtens, den Ablauf bei der  Probenentnahme und Erstellung des jeweiligen Gutachtens und damit der Unrichtigkeit der  Kalkulationsgrundlagen der Behörde sowie die Einvernahme des Geschäftsführers der Lemost-Handel GmbH  E.St., zum Beweis für die tatsächlich gelieferte Fleischqualität im Prüfungszeitraum und  damit zur Höhe des tatsächlichen Fleischabschnitts un der Fleischmenge, die verkaufbar  gewesen wäre.

- missed: `M.M.B.` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der **Xaver Plaumert, BEd**, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

- missed: `Xaver Plaumert, BEd` (person)
- predicted in sentence: `Dr. Wolfgang Pavlik`, `Dr. Wolfgang Aigner`, `Mag. Belinda  Maria Eder`, `Xaver Plaumert`, `Mag. Katharina Moravec`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)

1) Mit Schreiben vom 13.05.2020 wurde von Herrn **Angelstein** mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

- missed: `Angelstein` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_170`)

Bei der Erstellung des Aktengutachtens vom 31. Jänner 2022 lag der Sachverständigen **Dr.in  Dok3** das Privatgutachten von MMag. W., MSc, vom 5. Oktober 2021 vor.

- missed: `Dr.in  Dok3` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_24`)

Parallel dazu sei ebenfalls durch das Finanzamt Wien 1/23 mit Datum vom 03.12.2020 der  Bescheid über die teilweise Abweisung eines Rückzahlungsantrages ergangen, welcher mit  10.12.2020 beim **Jaden Knauss**  eingegangen sei und gegen den sich nun die vorliegende  Beschwerde richte.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_194`)

Der **Gertrude Holzmenger**  ist in zweistufiger Sektor mit der Dorothea Hasslocher  als Zentralinstitut und den  angeschlossenen Dimitri Dancker  als Primärinstitute.

- missed: `Gertrude Holzmenger` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_162`)

Verwaltungsverfahrensrechtes DDr.  Walter, **DDr. Maier**, Seite 131).

- missed: `DDr. Maier` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache **Jaden Grothmann**  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Jaden Grothmann` (person)
- predicted in sentence: `Univ.-Prof. Massimo Friedhoff`

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Francois Roeder, Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich, über die Beschwerde vom 12. Juni 2023 gegen  den Bescheid des Finanzamtes Österreich vom 9. Mai 2023 betreffend Säumniszuschlag 2023  nach der am 22.11.2024 am Bundesfinanzgericht in Wien über Antrag der Partei abgehaltenen  mündlichen Verhandlung in Abwesenheit des Beschwerdeführers und in Anwesenheit von  Bernadette Pommer BA MA für das Finanzamt sowie der Schriftführerin Mag. Magdalena  Preslmayr zur Steuernummer 48-847/1680  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung eines ersten  Säumniszuschlages vom 9.5.2023 in Höhe von € 148,00 wird gemäß § 279 BAO als  unbegründet abgewiesen.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: `Mag. Markus Knechtl`, `Beschwerdesache Francois Roeder`, `Bernadette Pommer`, `Mag. Magdalena  Preslmayr`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)

Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - **MR Dr. Heidi Pacher** vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

- missed: `MR Dr. Heidi Pacher` (person)
- predicted in sentence: `Dr. Heidi Pacher`, `Mag.  Dr. Juliane Bogner`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_539`)

Dem von der Betriebsprüfung bei der Bf. thematisierten Anteil der Schwiegermutter des  **M.M.A.** am Keller war zu entgegnen, dass die in Quadratmetern auszudrückende Nutzfläche  gemäß § 17 Abs. 2 MRG in der Fassung des BGBl. I Nr. 36/2000 die gesamte Bodenfläche einer  Wohnung oder eines sonstigen Mietgegenstandes abzüglich der Wandstärken und der im  Verlauf der Wände befindlichen Durchbrechungen (Ausnehmungen) ist.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)

VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des **Wladimir Leukhardt**, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

- missed: `Wladimir Leukhardt` (person)
- predicted in sentence: `Mag. Anna Mechtler`

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Hon.-Prof. Adalbert Köseoglu**  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hon.-Prof. Adalbert Köseoglu` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  **Ibrahim de Vrese, LLB**, Kitzlermühle 3, 2754 Wopfing, Österreich, über die Beschwerde vom 07.06.2021 wegen behaupteter  Verletzung der Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Familienbeihilfe ab 09/2019 Sozialversicherungsnummer 2872011080  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Ibrahim de Vrese, LLB` (person)
- predicted in sentence: `Mag. Ulrike Stephan`

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dieter Brennscheid, Bakk. rer. nat.** in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

- missed: `Dieter Brennscheid, Bakk. rer. nat.` (person)
- predicted in sentence: `Richter Dieter Brennscheid, Bakk. rer. nat. `, `Ines Gora`

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_211`)

Bei letzterer war dies  Ausfluss einer Außenprüfung, die diesbezüglich festhielt: „Die einzelnen Aufwendungen für die  Modellentwicklung sind daher im Betrieb der steuerlichen Mitunternehmerschaft Uwe Gudian  als  Betriebsausgabe zu berücksichtigen und nicht anteilig bei den einzelnen Zielgesellschaften, an  denen sich **Uwe Gudian**  als atypisch stille Gesellschafterin beteiligt.“

- missed: `Uwe Gudian` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache **Brian Nieclaassen**, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

- missed: `Brian Nieclaassen` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`, `M. M.`, `Rechtssache Brian Nieclaassen`

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_38`)

Das Bundesfinanzgericht richtete am 2020 folgenden Vorhalt an die Rechtsvertretung des Bf.:  „In der von der Wiener Kinder- und Jugendhilfe, Rechtsvertretung Bezirk 22, gegen den  Abweisungsbescheid des Finanzamtes erhobenen Beschwerde wird vorgebracht, dass sich der  mj. **OSR Eugenia Balikci**  im abweisenden Zeitraum ab Jänner 2016 in einer sozialpädagogischen  Wohngemeinschaft der Sozialwerke Clara Fey befand und die Sozialwerke Clara Fey wesentlich  auch durch Spenden finanziert würden.

- missed: `OSR Eugenia Balikci` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_17`)

… Während **Fabios** Osterferien entfällt im Übrigen das Regelkontaktrecht zu beiden Kindern.

- missed: `Fabios` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)

Die Auskunft könne Herr **Russbüldt** als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

- missed: `Russbüldt` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_25`)

Beim nächsten Kontrollbesuch bei **Dr. A3** habe die Bf. erfahren, dass für diesen  Zweck eine Einfachbrille, zugerichtet auf den cm-Abstand vom Bildschirm zweckmäßiger sei.

- missed: `Dr. A3` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)

Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr **Russbüldt** nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

- missed: `Russbüldt` (person)
- predicted in sentence: `Angelstein`

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143717.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143717.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Laetitia Rosenmeyer, Thomas Brunner-Weg 117, 3972 Reichenau am Freiwald, Österreich, über die Beschwerde vom 13. April 2023 gegen  den Bescheid des Finanzamtes Österreich vom 5. April 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 06-868/8855  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`, `Beschwerdesache Laetitia Rosenmeyer`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde des  **Desiree Hannecken**, Lasseestraße 13, 5144 Handenberg, Österreich, vom 5. Oktober 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 28. September 2023, GZ. MA67/Zahl/2023,  wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung  in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Desiree Hannecken` (person)
- predicted in sentence: `Mag. Irene Kohler`, `Stadt Wien`

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_299`)

Festgehalten wird, dass bei **M.** auf Grund ihrer Erkrankung am Asperger-Syndrom zweifellos  psychosoziale Beeinträchtigungen, welche sich auf verschiedenste Lebensbereiche, so auch  den beruflichen Lebensbereich erstrecken, bestehen.

- missed: `M.` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)

Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur **Gustav Nowak**.

- missed: `Gustav Nowak` (person)
- predicted in sentence: `StR Samuel Fraesdorff`

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_465`)

Dies treffe auf sein Kind zu. da es seit 2008 (Bestätigung/Bedarfsmedikation Dr.S;Bernhard Ratzenhofer  Dr. B  („**Dr. B**“), Dr. W Thaddäus Rothöft, Bakk. art. und LKH Ort A wegen Neurodermitis uvam.

- missed: `Dr. B` (person)
- predicted in sentence: `Dr. W`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache **Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.**,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.` (person)
- predicted in sentence: `Mag. Detlev Bodenm`, `Univ.-Prof.in Eva Gund`, `Mag. Thomas Gell`

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_6`)

Diese Bescheide wurden an den Bf. adressiert und an Dr. X als Erwachsenenvertreter des Bf. in  dessen Databox zugestellt. **Dr. X** war vom Bezirksgericht Salzburg im Jahr 2004 als Sachwalter  (nunmehr: Erwachsenenvertreter) zur Einkommensverwaltung des Bf. sowie zu dessen  Vertretung vor Ämtern und Behörden bestellt worden.

- missed: `Dr. X` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_20`)

Die Diagnose der Fachordination von **Dr. A2** sei die gleiche  wie jene von Dr. A1 gewesen (Beilage).

- missed: `Dr. A2` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Univ.-Prof.in Marion Weßalowski**  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` (person)
- predicted in sentence: `OMedR Leonhard Hestermeyer`

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`, `Beschwerdesache Friedhelm Sutor`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_2`)

Das Bundesfinanzgericht hat durch den Richter Dr. Erhard Gruetter  in der Beschwerdesache **René Kleser**,  Dauerkleingärten 17M, 5112 Gresenberg, Österreich, vertreten durch Mag. Andreas Schnegg, Kalkofenstraße 24, 6425 Haiming, über  die Beschwerde vom 19. Februar 2022 gegen den Bescheid des FA Wien 8/16/17  vom 21. Jänner 2022  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer  85-777/9690, zu Recht erkannt:  I. Der Beschwerde wird teilweise Folge gegeben.

- missed: `René Kleser` (person)
- predicted in sentence: `Dr. Erhard Gruetter`, `Mag. Andreas Schnegg`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Penelope Splettstösser**  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Penelope Splettstösser` (person)
- predicted in sentence: `Univ.-Prof.in Penelope Splettst`

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Dieter Fröhlich** in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Dieter Fröhlich` (person)
- predicted in sentence: `Mag. Dieter Fr`

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_44`)

II. Sachverhalt  Die **Leroy Kusznierz**  wurde mit Gesellschaftsvertrag vom Datum mit dem Sitz in der politischen  Gemeinde Ort1 errichtet;

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit Eingabe vom 28.09.2020 beantragte das **Jaden Knauss** (=Bf.) die Rückzahlung des nach  Bewilligung der gleichzeitig beantragten Aussetzung der Einhebung nachstehender Abgaben  auf seinem Abgabenkonto in Höhe von € 2.274.683,82 ausgewiesenen Guthabens:  Haftungsbescheid nach § 82 EStG für Lohnsteuer 2012 € 527.441,45  Haftungsbescheid nach § 82 EStG für Lohnsteuer 2013 € 544.483,24  Haftungsbescheid nach § 82 EStG für Lohnsteuer 2014 € 484.672,08  Haftungsbescheid nach § 82 EStG für Lohnsteuer 2015 € 508,797,58  Gesamt Haftungsbescheide  € 2.065.394,35  1 von 7 Seite 2 von 7

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_97`)

Aus den getroffenen Feststellungen, wonach der BF und seine geschiedene Gattin Frau **MT** je  zur Hälfte Eigentümer der in P, BF-P, gelegenen Liegenschaft mit dem darauf befindlichen  Wohnhaus sind und das p. Bezirksgericht im Scheidungsurteil bestimmt hat, dass die  geschiedene Gattin MT berechtigt ist, nur die Räume im Erdgeschoß des Hauses zu nutzen und  der BF berechtigt ist, den ersten Stock des Hauses zu nutzen, ergibt sich weiters, dass ein  Verkauf des Hauses aufgrund der Eigentumsverhältnisse und der Benutzungsregelungen durch  den BF äußerst erschwert bzw wenn überhaupt nur unter erheblichen Vermögenseinbußen  möglich und die Anschaffung einer adäquaten Wohnung am Beschäftigungsort aus dem  Veräußerungserlös ausgeschlossen wäre.

- missed: `MT` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Andrea Müller-Dobler MBA MSc** in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Mag. Andrea Müller-Dobler MBA MSc` (person)
- predicted in sentence: `Stadt Wien`

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)

6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn **Angelstein** angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

- missed: `Angelstein` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_256`)

Es hätte 2016 eine neuerliche Einschätzung erfolgen sollen, es wurde  die gesamte Familie zum Behindertenanwalt eingeladen, weil ihr Kind beantragt hatte, von  Gutachtern, wie **Dr. Kuderna** oder Dr. Widhalm begutachtet zu werden.

- missed: `Dr. Kuderna` (person)
- predicted in sentence: —

</details>

---

