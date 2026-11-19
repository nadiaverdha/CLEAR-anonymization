# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-19T13:16:06.451045

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-11-19/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 200 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 200 |
| Validation documents | 790 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 1567 |
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
| Batch size | 50 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.1% |
| True Positives | 3462 |
| False Positives | 742 |
| False Negatives | 1137 |
| Total Gold Entities | 4599 |
| Micro Precision | 82.4% |
| Micro Recall | 75.3% |
| Micro F1 | 78.7% |
| Macro F1 | 78.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `german_courts` | 9.6% | 98.3% | 5.1% | 237 | 233 | 4 |
| `german_police_admin` | 1.9% | 97.8% | 1.0% | 45 | 44 | 1 |
| `german_specific_orgs` | 4.9% | 95.8% | 2.5% | 120 | 115 | 5 |
| `german_tax_authorities` | 72.6% | 90.8% | 60.4% | 3063 | 2780 | 283 |
| `german_company_ag` | 3.1% | 66.1% | 1.6% | 109 | 72 | 37 |
| `german_company_gmbh` | 8.3% | 34.6% | 4.7% | 630 | 218 | 412 |
| `german_company_e_commerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `german_courts` 🏆

**F1:** 0.096 | **Precision:** 0.983 | **Recall:** 0.051  

**Format:** `regex`  
**Rule ID:** `8abcded5`  
**Description:**
Matches specific German courts and administrative bodies including genitive forms (-s, -es) and specific names.

**Content:**
```
\b(Bundesfinanzgericht(?:s)?|Verwaltungsgerichtshof(?:s)?|Verfassungsgerichtshof(?:s)?|Pensionsversicherungsanstalt(?:s)?|AMS(?:\s+[A-Z])?|Landesgericht(?:s)?|Bezirksgericht\s+[A-Z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.983 | 0.051 | 0.096 | 237 | 233 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 233 | 4 | 4366 |

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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_316`)


Da keine gesicherte Judikatur des Verwaltungsgerichtshofs zur Frage, ob Art. 3 Abs. 8 UStG  1994 ob bei Verwendung einer österreichischen UID im Abgangsstaat die Vorschreibung einer  Erwerbsteuer auslöst bis der tatsächliche Erwerb im Bestimmungsstaat nachweislich  besteuert/erklärt wurde, wie es die derzeitige Verwaltungspraxis annimmt, ist die (ordentliche)  Revision zuzulassen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_135`)


Hinsichtlich einzelner Positionen ist nach Ansicht des Bundesfinanzgerichts der Bf. die  Glaubhaftmachung der Berufsbezogenheit u.a. durch die Anmerkungen zur Liste des  Finanzamts gelungen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_143`)


Die Ausbildung nahm daher aus der Sicht des Bundesfinanzgerichts nach allgemeiner  Lebenserfahrung im Wintersemester 2016/17 nicht die volle Zeit des Bf in Anspruch.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_33`)


Das Rechtsmittel gegen den nicht wirksam gewordenen Abweisungsbescheid ist daher mit  Beschluss des Bundesfinanzgerichts zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_142`)


Rechtliche Erwägungen zum festgestellten Sachverhalt:  Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofs ist zum Begriff des Vertreters  auf die Verkehrsauffassung abzustellen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_278`)


Art. 23 Abs. 2 DBA-Schweiz ist (auch nach Ansicht des Bundesfinanzgerichts) nicht  einschränkend – also auf Einkünfte für in der Schweiz ausgeübte Arbeit aus öffentlichen Kassen  in der Schweiz – sondern erweiternd – neben der Einkünftebesteuerungsberechtigung für die  im Ansässigkeitsstaat ausgeübte Tätigkeit – auch auf diese anzusehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_201`)


Schließlich ist zur  Frage des Vorliegens der Voraussetzungen für den Vorsteuerabzug allgemein darauf zu  verweisen, dass eine in freier Beweiswürdigung getroffene Feststellung des  Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof grundsätzlich nicht  zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_75`)


Es darf dazu auf den Beschluss des Bundesfinanzgerichts vom 15.02.2021,  RV/7100157/2021, verwiesen werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_94`)


Der  in der Beschwerdevorentscheidung genannte Pensionsanspruch sei im Zuge einer  Entscheidung des Bundesfinanzgerichts vom 17.09.2018, RV/1100359/2016, noch einmal  behandelt worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_58`)


Diese Sachverhaltsfeststellungen basieren auf den jeweils erwähnten und als glaubhaft  erachteten Beweismitteln bzw den im vorgelegten Akt aufliegenden und nachgereichten,  ebenfalls glaubhaften Unterlagen und dem Ergebnis des seitens des Bundesfinanzgerichts  durchgeführten Ermittlungen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_175`)


Schließlich ist zur  Frage des Wohnsitzes bzw. dessen Aufgabe allgemein darauf zu verweisen, dass eine in freier  Beweiswürdigung getroffene Feststellung des Bundesfinanzgerichts der Kontrolle durch den  Verwaltungsgerichtshof grundsätzlich nicht zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_4`)


Entscheidungsgründe  Verfahrensgang  Im Zuge einer GPLA stellte der Prüfer fest, dass über Auftrag des AMS von der  Beschwerdeführerin (Bf) Migranten als Lehrlinge in Deutsch unterrichtet wurden und auf eine  Lehrstelle in einem Betrieb vorbereitet wurden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_20`)


Die ausgezahlten Ausbildungsbeihilfen hätten  eine Höhe von € 240 pro Person und pro Monat betragen und seien vom AMS in genau  derselben Höhe ersetzt worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_25`)


Die Bf sucht als überbetriebliche Ausbildungseinrichtung im Auftrag des AMS für die  Ausbildungsteilnehmer Partner- und Praxisbetriebe, in denen die Ausbildung absolviert werden  kann.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_30`)


Teilnehmer, die nach Ablauf des Ausbildungszeitraumes noch keine Lehrstelle gefunden haben,  werden vom AMS weiterbetreut.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_12`)


Durch die Aufhebung des Einkommensteuerbescheides 2013 gemäß § 300 Abs. 1 BAO im Sinne  des Beschlusses des Bundesfinanzgerichts vom 15.03.2021 innerhalb der gesetzten Frist, sowie  durch die gleichzeitige Erlassung des neuen Sachbescheides, wurde dem Beschwerdebegehren  Rechnung getragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_12`)


II. Das Bundesfinanzgericht hat erwogen:  Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_100`)


Dazu wird seitens des  Bundesfinanzgerichts die Rechtsansicht vertreten, dass es - unabhängig von  Sanierungsbemühungen des Geschäftsführers -  grundsätzlich darauf ankommt, ob der  Geschäftsführer im/ab dem Zeitpunkt der Fälligkeit der Umsatzsteuervorauszahlung 08/2011  über die finanziellen Mittel verfügte, um diese Abgabe als Geschäftsführer für die  Gemeinschuldnerin innerhalb des Zeitraumes ab Fälligkeit (15.10.2011) bis zur  7 von 11 Seite 8 von 11

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_119`)


Für den vorliegenden Fall ist seitens des Bundesfinanzgerichts unter Berücksichtigung der  vorliegenden Aktenlage sachverhaltsmäßig festzustellen, dass dem Bf. bzw. der von ihm  vertretenen Gemeinschuldnerin keine ausreichenden finanziellen Mittel zur Verfügung  standen, um die Umsatzsteuervorauszahlung 08/2011 am Fälligkeitstag zur Gänze zu bezahlen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_199`)


Die Anregung des steuerlichen Vertreters auf Wiederaufnahme des Verfahrens gemäß § 303  Abs.1 lit. c BAO laut Vorlageantrag vom 30.7.2020 fällt nicht in den Zuständigkeitsbereich des  Bundesfinanzgerichts.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_76`)


Mit Beschluss des Bundesfinanzgerichts vom 9. Februar 2021 wurde das Finanzamt Österreich  vor dem Hintergrund, dass bislang keine Unterlagen betreffend eine kalkulatorische Schätzung,  5 von 15 Seite 6 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_83`)


Mit Beschluss des Bundesfinanzgerichts vom 5. Juli 2021 wurden dem Beschwerdeführer  folgende Unterlagen zur Kenntnis gebracht: Niederschrift über die Schlussbesprechung  anlässlich der beim Beschwerdeführer durchgeführten Außenprüfung vom 23.3.2016;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_88`)


Der Antrag auf Zeugeneinvernahme des Beschwerdeführers wurde mit Beschluss des  Bundesfinanzgerichts vom 9. Februar 2021 abgelehnt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_142`)


Die beiliegenden, vom erkennenden Gericht erstellten Kalkulationen (Berechnungsblätter I bis  IV) sowie ergänzend dazu schriftliche Erläuterungen zur Wahl der Schätzungsmethode, zu den  Sachverhaltsannahmen, die der Schätzung zugrunde gelegt wurden, und zur Ableitung der  Schätzungsergebnisse wurden den Parteien mit Beschluss des Bundesfinanzgerichts vom 5. Juli  10 von 15 Seite 11 von 15

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_9`)


ergangenen Beschluss des Bundesfinanzgerichts vom 7. November 2017 und beantragte  seinem Antrag vom 29. Dezember 2016 nunmehr stattzugeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_37`)


ergangenen Beschluss des Bundesfinanzgerichts vom 7. November 2017 und beantragte  seinem Antrag vom 29. Dezember 2016 nunmehr stattzugeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_55`)


Auch das von der belangten  Behörde herangezogene Erkenntnis des Verwaltungsgerichtshofs, 2012/15/0127, vermag die  Rechtsansicht der belangten Behörde nicht zu stützen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_2`)


Bezirk vom 03. November 2016 betreffend Vorschreibung einer Ausgleichsabgabe  gemäß § 9 Wiener Baumschutzgesetz mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom  09. Dezember 2016 gegen den Bescheid vom 03. November 2016 ein Vorlageantrag nicht  eingebracht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_22`)


Mit dem Bildungskonto wird die berufsorientierte Weiterbildung und Umschulung  (ausgenommen Umschulungen i.S.d. AMS) zur Arbeitsplatzsicherung gefördert.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_53`)


4. Antrag auf Senatsentscheidung  Gemäß § 272 Abs 2 Z 1 lit b BAO besteht die Möglichkeit, im Rahmen eines Vorlageantrags die  Entscheidung des Bundesfinanzgerichts durch Senat zu beantragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_79`)


Die Beschwerdeführerin hat  im Jahr 2014 ihr Arbeitsverhältnis als Grenzgängerin im Alter von 59 Jahren beendet und eine  Pension der Pensionsversicherungsanstalt bezogen.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_112`)


Gegen die in der Beschwerdevorentscheidung zuerkannten Kosten in Höhe von zusätzlich  1.393,55 € (neben den bereits berücksichtigten 1.963,69 €) bestehen seitens des  Bundesfinanzgerichts keine Bedenken, wirken sich allerdings aufgrund der Höhe des bei den  außergewöhnlichen Belastungen bestehenden Selbstbehaltes (5.106,52 €) betraglich nicht aus.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_105`)


Der Wissensstand der Behörde bezüglich der vorhergehenden Jahre ist nach der  Rechtsprechung des Verwaltungsgerichtshofs nicht maßgebend.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_53`)


Diese Rechtssache wurde der ursprünglich zuständigen Gerichtsabteilung Y mit Verfügung des  Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 27.1.2022 abgenommen und  jener der nunmehr einschreitenden Richterin zum Stichtag 2.2.2022 übertragen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_40`)


Über Ergänzungsersuchen des Bundesfinanzgerichts brachte der Beschwerdeführer mit  Schreiben vom 17.2.2022 weiter vor, er sei – da er sich jedes Jahr mehr als 90 Tage in  Großbritannien aufhalte – in Großbritannien steuerpflichtig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_6`)


I. Verfahrensgang  Kaufvertrag, Werkvertrag  Mit Kaufvertrag vom 15./19.01.2015 erwarben die Beschwerdeführerin (kurz: Bf) und Herr CE  von der P-GmbH, als Verkäuferin, das neu gebildete Grundstück Nr. 433/20, vorgetragen ob  der Liegenschaft EZ-1, Grundbuch XY, Bezirksgericht A, jeweils zur Hälfte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht A` | `Bezirksgericht A` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die P-GmbH (die Verkäuferin) war grundbücherliche Eigentümerin der Liegenschaft EZ-1,  KG XY, Bezirksgericht A, ob welcher Liegenschaft unter anderem die Grundstücke Nr. 433/2,  433/4, 433/5, 433/6 und 433/7 vorgetragen waren (siehe Kaufvertrag vom 15./19.01.2015, VP.  I. ALLGEMEINES).

| Predicted | Gold |
|---|---|
| `Bezirksgericht A` | `Bezirksgericht A` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_41`)


Unter Aufwendungen für Hilfsmittel im Sinne von § 4 der VO zu § 35 EStG sind nach dem  Erkenntnis des Verfassungsgerichtshofs, VfGH 13.3.2003, B 785/02, generell auch  behinderungsbedingte Ein- und Umbauten in Gebäuden zu verstehen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_48`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_61`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs sind Werbungskosten grundsätzlich  von Amts wegen zu berücksichtigen (VwGH 08.02.2007, 2004/15/0102).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_71`)


Nach der Judikatur des Verwaltungsgerichtshofs hat das Fahrtenbuch die beruflichen und  privaten Fahrten zu enthalten (vgl. VwGH 28.02.1964, 2176/63).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_93`)


So hat zum Beispiel bei einer gemeinsamen Versteuerung mehrerer Pensionen, die durch eine  Pensionsversicherungsanstalt ausbezahlt werden, z.B. einer Eigen- und einer Witwenpension,  keine Pflichtveranlagung gemäß § 41 Abs. 1 Z 2 EStG 1988 zu erfolgen (vgl. Peyerl in Jakom  EStG, 14.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_3`)


Begründung  Der Beschwerdeführer (Bf) wurde mit Urteil des Landesgerichts Salzburg vom Zahl, Datum  unter anderem schuldig gesprochen, zur Abgabenhinterziehung nach § 33 Abs 1 FinStrG und  nach § 33 Abs 2 lit a FinStrG der S. zur Steuernummer Nummer in Bezug auf die  Kapitalertragsteuer für die Jahre 2010 (€ 229,06), 2011 (€ 112,16), 2012 (€ 152,44) und 2014  (740,44), somit in Höhe von gesamt € 1.234,44 beigetragen zu haben.

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_4`)


In weiterer Folge wurde der Bf mit Haftungsbescheid vom 19.10.2021 als rechtskräftig  verurteilter Täter hinsichtlich der im Spruch des Urteils des Landesgerichts angeführten  hinterzogenen Abgaben gem. § 11 BAO im Ausmaß von € 1.234,44 zur Haftung herangezogen.

| Predicted | Gold |
|---|---|
| `Landesgerichts` | `Landesgerichts` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_46`)


Nach Ansicht des Bundesfinanzgerichts ist der  Verweis auf Einkünfte iSd § 27 Abs. 2 EStG 1988 steuersubjektübergreifend zu sehen und  hinsichtlich der aus dem gegenständlichen Wirtschaftsgut  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_22`)


Sie lege aber die geforderten  Unterlagen diesem Schreiben noch einmal bei, nämlich die Kursbestätigung von [Vorname Kind  1] über den AMS Kurs hinsichtlich seiner Lehrabschlussprüfung und die Kursbestätigung von  [Vorname Kind 2].

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_83`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  7 von 9 Seite 8 von 9

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_85`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH  24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_20`)


5. Dazu wurde ein Bescheid der Pensionsversicherungsanstalt v. 31.8.2021 vorgelegt, woraus  hervorgeht, dass der Bf aufgrund festgestellter, nunmehr dauernder Arbeitsunfähigkeit  anstelle Reha-Geld ab 1.11.2021 die Invaliditätspension zusteht.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_148`)


Die abschließende Argumentation der Bf, "vor allem befinde ich mich seit 1.11.2021 auf Grund  meiner psychischen Erkrankung in der Invaliditätspension", geht von vorneherein völlig ins  Leere, weil damit seitens der Pensionsversicherungsanstalt die voraussichtlich dauerhafte  Arbeitsunfähigkeit der Bf nach Wiederbegutachtung überhaupt erst ab dieser Zeit, ab  November 2021, dh. erst viele Jahre nach Beendigung ihrer beruflichen Tätigkeit im Jahr 2013,  attestiert wird (siehe PV-Bescheid vom 31.8.2021).

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_106`)


4.2. Ermittlungen und Beschluss Bundesfinanzgericht inklusive Auftrag der  Zeugenvernehmung durch die belangte Behörde vom 26. April 2022  Im Zuge der Ermittlungen des Bundesfinanzgerichts waren einige Punkte offen und das  Bundesfinanzgericht richtete daher einen Vorhalt zur Ermittlung des Sachverhaltes an den Bf  und die belangte Behörde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_33`)


Angesichts der überlangen Verfahrensdauer wäre die erstinstanzliche Behörde verpflichtet  gewesen, in (verfassungskonformer) Auslegung des § 209 Abs. 1 BAO anzunehmen, dass es  (zeitlich) genügt habe, den Wiederaufnahmeantrag binnen eines Jahres nach Bekanntwerden  des Wiederaufnahmegrundes (Erkenntnis des Bundesfinanzgerichts vom 13.1.2017,  RV/4100613/2013) zu stellen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_83`)


Da das vorliegende Erkenntnis  des Bundesfinanzgerichtes der zitierten Rechtsprechung des Verwaltungsgerichtshofs folgt,  liegt keine Rechtsfrage vor, der grundsätzliche Bedeutung beizumessen wäre.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_47`)


Von diesem Vorwurf wurden die beiden Angeklagten nach durchgeführter Hauptverhandlung  mit Urteil des Landesgerichts St. Pölten vom 2. März 2022 freigesprochen, weil das  Landesgericht die in der Anklage vorgeworfenen Unternehmensentscheidungen im Konzern als  fremdüblich vertretbar beurteilte.

| Predicted | Gold |
|---|---|
| `Landesgericht` | `Landesgericht` |

**Missed by this rule (FN):**

- `Landesgerichts St. Pölten` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_24`)


In den  Kalenderjahren 2017 bis 2021 habe der Bf. vom AMS bzw von der österreichischen  Pensionsversicherungsanstalt insgesamt € 80.757,19, also durchschnittlich € 1.345,95  monatlich erhalten.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_40`)


Der Bf. bezog in der Folge (ab 03/2016) Arbeitslosengeld bzw. Notstandshilfe und wurde vom  AMS als „unvermittelbar“ eingestuft.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_6`)


Mit Beschluss vom 17.03.2021 zu 19 S x wies das Bezirksgericht A den Antrag des Bf. ab,  wogegen dieser mit Schreiben vom 05.04.2021 Einspruch erhob.

| Predicted | Gold |
|---|---|
| `Bezirksgericht A` | `Bezirksgericht A` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_15`)


Nach Stellung des diesbezüglichen Vorabentscheidungsersuchens eines Richters des  Bundesfinanzgerichts reichte die Europäische Kommission mit Beschluss vom 14.05.2020 im  Verfahren INFR (2018) 2372 am 22.07.2020 Klage gegen die Republik Österreich beim  Gerichtshof der Europäischen Union ein, die zur Zahl C-328/20 protokolliert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Gerichtshof der Europäischen Union` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_127`)


Das von der Bf. im Jahre 2016 begonnene und im Beschwerdezeitraum sowie in den beiden  diesem nächstfolgenden Jahren betriebene beschwerdegegenständliche Studium stellt in  Ansehung des Umstandes, dass eine AHS-Matura sowohl nach der allgemeinen  Verkehrsauffassung als auch gemäß dem Berufslexikon des AMS – in diesem sind insgesamt  1.726 Berufe aufgelistet, die Begriffe AHS-Maturant oder AHS-Maturantin finden sich dort  nicht – zweifelsfrei eine Erstausbildung dar.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_28`)


Er  bezog im gegenständlichen Jahr ganzjährig Einkünfte von der Pensionsversicherungsanstalt als  Pensionist.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_25`)


Da laut amtlichen Befund des Verfassungsgerichtshofs vom 29.06.2022 insgesamt zwei  Eingaben unter den Zahlen E 1037/2022 und G 148/2022 eingebracht wurden und trotz  Aufforderung vom Verfassungsgerichtshof vom 22.06.2022 kein Einzahlungsbeleg vorgelegt  wurde, war die Gebühr zu Recht mittels Gebührenbescheid samt Bescheid über eine  Gebührenerhöhung vorzuschreiben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_86`)


Gehört das Kind innerhalb eines Monats zeitlich hintereinander unterschiedlichen Haushalten  an, so hat nach der Rechtsprechung des Verwaltungsgerichtshofs unter Anwendung des  Überwiegenheitsprinzips diejenige Person Anspruch auf Familienbeihilfe, die den Haushalt für  den längeren Zeitraum geführt hat (VwGH vom 28.11.2007, 2007/15/0058).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_39`)


Die belangte Behörde ist nach Ansicht des Bundesfinanzgerichts zur Recht davon ausgegangen,  dass damit kein Wiederaufnahmegrund im Sinne des Neuerungstatbestandes (§ 303 Abs. 1 lit b  BAO) vorhanden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/140554.1`) (sent_id: `deanon_BFG_20260814_TEST/140554.1_61`)


Die Bf. hat den am 30.01.2023 hinterlegten Beschluss des Bundesfinanzgerichts vom  24.01.2023 nicht behoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_188`)


Der erkennende Senat des  Bundesfinanzgerichts vertritt im Zweifel dazu nun die Ansicht, dass der Bf. bei der Einreichung  der Einkommensteuerklärung 2017, wie von diesem angegeben, von der gesetzlichen  Änderung des Steuerabkommens zwischen Liechtenstein und Österreich ab 2017 keine  Kenntnis hatte und liegen auch keine konkreten anders gelagerten Anhaltspunkte vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_189`)


Der Senat des Bundesfinanzgerichts gelangt daher anders als Spruchsenat in rechtlicher  Hinsicht zum Ergebnis, dass es iSd § 98 Abs. 3 FinStrG nicht erweislich ist, der Bf. habe es  zumindest für möglich gehalten und sich damit abgefunden, eine Verkürzung der von ihm  16 von 21 Seite 17 von 21

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_192`)


Allerdings ist der Senat des Bundesfinanzgerichts der Ansicht, dass sich der Bf. hinsichtlich der  nicht erklärten Kapitaleinkünfte aus Liechtenstein gemäß § 34 Abs. 1 FinStrG der grob  fahrlässigen Abgabenverkürzung schuldig gemacht hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_214`)


Nach Ansicht des Senates des Bundesfinanzgerichts war die Vermögensverwaltungsfirma  neben der Vertretung des Bf. bei den depotführenden Banken für eine möglichst ertragreiche  Veranlagung des Kapitalvermögens des Bf. verantwortlich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_241`)


In Abwägung dieser  Strafzumessungsgründe sowie unter Berücksichtigung des Schuld- und Unrechtsgehaltes der  Tat und einem Strafrahmen von € 33.356,00 erachtet der erkennende Senat des  Bundesfinanzgerichts eine Geldstrafe von € 5.000,00 als angemessen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_93`)


Davon abweichend ist nun  allerdings seitens des Bundesfinanzgerichts festzustellen, dass seitens der steuerlichen  Vertretung ein Rechtsmittelverzicht ausdrücklich im Namen des Bf. nicht erklärt wurde und  sind auch keine Umstände ersichtlich, woraus auf die Annahme eines von der steuerlichen  Vertretung in Vertretung für den Bf. erklärten Rechtsmittelverzichts geschlossen werden  könnte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_130`)


Hiezu  ist seitens des Bundesfinanzgerichts festzustellen, dass das Finanzamt gegen die in § 115 Abs. 1  BAO normierte Ermittlungspflicht verstoßen hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_10`)


Er besuche einen vom AMS bezahlten Kurs zur Vorbereitung auf die  Lehrabschlussprüfung (LAP).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_16`)


In Beantwortung des Ersuchens teilte der Bf. dem Finanzamt am 4. August 2022 mit, dass das  AMS nach dem Ende seines Präsenzdienstes seinem Wunsch nachgekommen sei und ihm  einen Vorbereitungskurs auf die Lehrabschlussprüfung ermöglicht habe (Verweis auf die  beiliegende Betreuungsvereinbarung, Seite 2 Mitte).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_20`)


Aus dem ebenfalls beigelegten Schreiben des AMS vom 23. Mai 2022 geht u.a. hervor, dass mit  dem Bf., um ihn bei der Lehrabschlussprüfung zu unterstützen, ein Vorbereitungskurs zur  Lehrabschlussprüfung beim Kursinstitut KUS von 4. Juli 2022 bis 9. September 2022 vereinbart  wurde.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_27`)


Im Sommer habe er einen vom AMS be- zahlten Vorbereitungskurs für diese Prüfung absolviert.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_43`)


2) Zeitraum zwischen 1. Mai und 2. Juni 2022:   a) Ich bin seit 13. April 2022 durchgehend am AMS als arbeitssuchend gemeldet (siehe  Dokument 4 a_LJ_Notstandshilfe.pdf).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_44`)


Wegen des noch fehlenden Lehrabschlusses konnte mir  das AMS noch keine Erwerbstätigkeit vermitteln, unterstützt mich aber bei der Vorbereitung  auf die LAP.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_62`)


4) AMS Leistungen  a)

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_66`)


Mein Einkommen vom AMS beträgt 9,14 Euro täglich.“  Beilagen:   Teilnahmebestätigung KUS-Netzwerk vom 05.10.2022, Vorbereitung auf die LAP,  04.07.2022-30.09.2022, 60 Unterrichtseinheiten   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 11.03.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 30.06.2021   Zeugnis nicht bestandene LAP im Lehrberuf Mechatroniker, Büro- und EDV- Systemtechnik (Hauptmodul) vom 23.09.2021   Wiederholerprüfungsanmeldung Nr. 137827 vom 27.05.2022   Mitteilung über den Leistungsanspruch, AMS vom 09.06.2022:     4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_67`)


 Bestätigung Kurszeiten, AMS:     Mit E-Mail vom 12. März 2023 teilte der Bf. mit, dass es nun mit einer Anstellung bei der Fa.  Wright Robotik AG  als Handelsarbeiter geklappt habe und er von der WKO den Prüfungstermin  30.03.2023 erhalten habe.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Wright Robotik AG` (organisation)
- `WKO` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_87`)


Die Kurstage gliederten sich  wie folgt:  Montag: 9-12 Uhr  Mittwoch: 8-12 Uhr  Freitag: 9-12 Uhr  Von 13. April 2022 bis 05. März war der Bf. am AMS als arbeitssuchend gemeldet.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_91`)


Beweiswürdigung  Der unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt und den vom Bf.  vorgelegten Unterlagen (Schreiben des AMS vom 23. Mai 2022 betreffend  Betreuungsvereinbarung, Schreiben des AMS vom 09. Juni 2022 betreffend Gewährung von  Notstandshilfe, Präsenzdienstbestätigung vom 21. März 2022, Bescheid des Magistrates der  Stadt Wien, MA 40, vom 4. Juli 2022, Wiederholer-Prüfungsanmeldung 137827 vom 27. Mai  2022, div. Lehrabschlussprüfungszeugnisse).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Missed by this rule (FN):**

- `Magistrates der  Stadt Wien` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_147`)


Dient ein vom AMS gefördertes Training dazu, die fachliche Qualifikation für die Ausübung  eines konkreten angestrebten Berufes zu erlangen und nimmt es die überwiegende Zeit in  Anspruch, liegt - anders als bei allgemeinen Qualifizierungsmaßnahmen des AMS -  Berufsausbildung i.S.d. FLAG 1967 vor (BFG vom 02.02.2022, RV/7105412/2019).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_162`)


- sie haben sich bei ihrem AMS arbeitslos gemeldet;

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_211`)


Da das Fehlen einer UID-Nummer des Erwerbers im  Zeitpunkt des Leistungsbezuges dem Vorliegen einer steuerfreien innergemeinschaftlichen  Lieferung iSd Art. 7 UStG 1994 - wie schon ausgeführt - nicht entgegensteht, wenn die  materiellen Voraussetzungen hierfür erfüllt sind, wovon nach den Feststellungen des  Bundesfinanzgerichts auszugehen ist, schuldete der leistende Unternehmer die Umsatzsteuer  im Revisionsfall lediglich aufgrund der Rechnung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_14`)


In Übereinstimmung mit dem Beschluss des Verfassungsgerichtshofs vom 26.01.2023,  E 255/2023 , konnte daher dem Antrag nicht stattgegeben werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/141293.1`) (sent_id: `deanon_BFG_20260814_TEST/141293.1_11`)


Bereits im Erkenntnis des Bundesfinanzgerichts vom 21.7.2021, RV/7101544/2019, wurde auf  die bei der Beschwerdeführerin erfolgte Außenprüfung verwiesen, bei der in  beschwerderelevanter Hinsicht (ua im Bericht über das Ergebnis der Außenprüfung vom  31.10.2016) folgende Prüfungsfeststellungen getroffen wurden:  „Kurssicherungsgeschäfte   Zur Absicherung des Währungsrisikos aus dem in lokaler Währung geführten Eigenkapital  diverser NWB wurden Kurssicherungsgeschäfte abgeschlossen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_60`)


Wie die Einstellung sowohl der beim  Landesgericht Wiener Neustadt als auch beim Spruchsenat des Finanzamtes Wien gegen den  BF angestrengten Finanzstrafverfahren erweise, habe der BF zu keinem Zeitpunkt die Absicht  gehabt, Steuern vorsätzlich zu hinterziehen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_69`)


Es handle sich dabei um eine  Drittschuldnererklärung, die an das Bezirksgericht E. und an Rechtsanwalt Roxana Hiltenbrand, MA versendet  wurde.

**False Positives:**

- `Bezirksgericht E` — partial — gold is substring of pred: `Bezirksgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht`(organisation)
- `Roxana Hiltenbrand, MA`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_47`)


Von diesem Vorwurf wurden die beiden Angeklagten nach durchgeführter Hauptverhandlung  mit Urteil des Landesgerichts St. Pölten vom 2. März 2022 freigesprochen, weil das  Landesgericht die in der Anklage vorgeworfenen Unternehmensentscheidungen im Konzern als  fremdüblich vertretbar beurteilte.

**False Positives:**

- `Landesgerichts` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Landesgericht`(organisation)

</details>

---

## `german_police_admin` 🏆

**F1:** 0.019 | **Precision:** 0.978 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `9e06e6f3`  
**Description:**
Matches police and administrative bodies with location suffixes, including genitive forms.

**Content:**
```
\b(Landespolizeidirektion\s+Wien|Magistrat(?:s)?\s+der\s+Stadt\s+Wien(?:\s+Magistratsabteilung\s+\d+)?|Wiener\s+Gemeinderat(?:s)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.978 | 0.010 | 0.019 | 45 | 44 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 44 | 1 | 4555 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_8`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien unter Zugrundelegung der  Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der Landespolizeidirektion  Wien mit Strafverfügung vom 24. Dezember 2019 angelastet, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 25. Oktober 2019 um 09:38 Uhr  in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Dresdner Straße 89, abgestellt, ohne  für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein  gesorgt zu haben, da der Parkschein unrichtig entwertet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_38`)


In der am 17. Juni 2020 durchgeführten mündlichen Verhandlung vor dem  Bundesfinanzgericht wurde das Kontrollorgan der MA 67 der Landespolizeidirektion Wien als  Zeuge vernommen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_95`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige vom 06.06.2018 samt Fotos, welche  von einem Organ der Landespolizeidirektion Wien erstattet wurde, der Lenkerauskunft vom  08.11.2018, wonach das Fahrzeug Ihnen von der Zulassungsbesitzerin (VN-F NN) überlassen  war sowie Ihrer Bekanntgabe vom 30.07.2019, wonach das Fahrzeug Vera Schliephacke überlassen  war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Vera Schliephacke` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_11`)


Das Fahrzeug wurde von einem Kontrollorgan der Parkraumüberwachung der  Landespolizeidirektion Wien  1) am 22. Oktober 2019 um 16:21 Uhr in der gebührenpflichtigen Kurzparkzone in 1200  Wien, Brigittenauer Lände 134-136, und   2) am 23. Oktober 2019 um 09:48 Uhr in der gebührenpflichtigen Kurzparkzone in 1100  Wien, LaaerBerg-Straße 16-20,  beanstandet, da es zu den genannten Zeiten ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_7`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer wurde von der belangten Behörde, unter Zugrundelegung der Anzeige  eines Kontrollorganes der Landespolizeidirektion Wien, Abteilung für Parkraumüberwachung,  mit Strafverfügung vom 12.10.2020, MA67/Zahl/2020, angelastet, er habe das Fahrzeug mit  dem behördlichen Kennzeichen 123 (A) am 12.8.2020 um 11:40 Uhr in der gebührenpflichtigen  Kurzparkzone in 1150 Wien, Zinckgasse 25, abgestellt, ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_26`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:  „Das Fahrzeug wurde von einem Organ der Landespolizeidirektion Wien um 11:40 Uhr  beanstandet, da es an der im Spruch bezeichneten Örtlichkeit und zur dort angeführten  Zeit in einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dieses mit einem  gültig entwerteten Parkschein gekennzeichnet oder einen elektronischen Parkschein  aktiviert zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_37`)


Es besteht für die erkennende Behörde keinerlei Veranlassung, die schlüssigen und  widerspruchsfreien Angaben des meldungslegenden Organs der Landespolizeidirektion  Wien in Zweifel zu ziehen, zumal einem derartigen Organ die Wahrnehmung und  richtige Wiedergabe maßgeblicher Sachverhalte, insbesondere bezüglich eines im  ruhenden Verkehr befindlichen Kraftfahrzeuges, wohl zugemutet werden kann.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_38`)


Es  besteht kein Grund, an der Objektivität des meldungslegenden Organs der  Landespolizeidirektion Wien zu zweifeln und ergibt sich kein Anhaltspunkt, dass dieses  eine ihm unbekannte Person wahrheitswidrig belasten wollte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_111`)


Mit dem Beschwerdevorbringen, er habe kein Ticket vor Ort erhalten (gemeint wohl: keine  Organstrafverfügung), lässt sich für diesen nichts gewinnen, da dem Organ der öffentlichen  Aufsicht ein Wahlrecht eingeräumt ist, ob es eine Anonymverfügung gemäß § 49a (im Falle  eines Organs der Verwaltungsstrafbehörde selbst) bzw. eine Organstrafverfügung gemäß § 50  VStG (im Falle eines Organes der Landespolizeidirektion Wien) oder eine Anzeige erstattet  (Lewisch/Fister/Weilguni, Verwaltungsstrafgesetz, § 50 Tz 4), durch die das  Verwaltungsstrafverfahren gemäß §§ 40 ff VStG gegen eine bestimmte Person als Lenker des  Fahrzeuges eingeleitet wird.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (Fa. ZB, Straße, 1220 Wien)  eingeholten Lenkerauskunft mit Strafverfügung vom 28. Oktober 2020, an, er habe das  Fahrzeug am 19. August 2020 in der gebührenpflichtigen Kurzparkzone in 1220 Wien,  Schüttaustraße 4-10, ohne einem für den Beanstandungszeitpunkt 14:34 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_15`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer dienstlichen  Wahrnehmung gelegt wurde, in die, von diesem angefertigten Fotos sowie in die  vorangegangenen Verfahren zu GZ MA67/Zahl2/2020 und MA67/Zahl3/2020.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_10`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 1. Oktober  2020 um 13:20 Uhr in der gebührenpflichtigen Kurzparkzone in 1030 Wien, Kardinal-Nagl-Platz  10-11, beanstandet, da es ohne einem für den Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 9. Dezember 2020, an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 9. Oktober 2020  in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Stubenbrücke nächst Parkring, ohne  einen für den Beanstandungszeitpunkt 15:33 Uhr gültigen Parkschein abgestellt und demnach  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_45`)


Am 10. Mai 2019 wurden beim zuständigen Finanzamt die Vereinsstatuten und am 12.  September 2019 der Bescheid der Landespolizeidirektion Wien betreffend die Einladung zur  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_5`)


Begründung  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Autonummer (A) wurde am  16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Abstellort, von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion  Wien zur Anzeige gebracht, da zum Beanstandungszeitpunkt ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_15`)


Beweis wurde erhoben durch Einsichtnahme in das Organmandat vom 6.10.2021, welches von  einem Organ der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung  gelegt wurde, sowie in die von Ihnen vorgelegten ‚Handy-Parken‘ Auszüge und die m-parking  Dateien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_141`)


Dass sie aber auch schon davor sub-untervermietet hätte, belegte der Bf anhand einer Kopie  der ersten Seite eines Bescheides der Landespolizeidirektion Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_185`)


Dass sie aber auch schon davor sub-untervermietet hätte,  belegte der Bf anhand einer Kopie der ersten Seite eines Bescheides der Landespolizeidirektion  Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_206`)


Zum dritten ist durch die Feststellungen der Landespolizeidirektion Wien als erwiesen  anzunehmen, dass im gegenständlichen Zeitraum jedenfalls ab 14. September 2017 Glücksspiel  vom Subuntermieter angeboten wurde, der das Lokal vom Untermieter, an den der  gegenständliche Bf vermietet hatte, in Subuntermiete gemietet hatte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_207`)


Es besteht kein Anlass  an diesen Feststellungen der Landespolizeidirektion Wien zu zweifeln.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_15`)


Das Straferkenntnis wurde folgendermaßen begründet:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung samt  Fotodokumentation, welche von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  geht hervor, dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug im  gebührenpflichtigen Kurzparkzonenbereich abgestellt war, ohne dass die  Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_10`)


Entscheidungsgründe  Verfahrensgang  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 15. Februar  2022 in der gebührenpflichtigen Kurzparkzone in 1200 Wien, Aignerstraße 6, beanstandet, da  zur Beanstandungszeit 18:48 Uhr ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_58`)


Begründend stellte die Behörde nach Wiedergabe des Verwaltungsgeschehens und der vom Bf.  im Zuge des Verfahrens vorgebrachten Einwendungen fest, dass aus der Anzeige des Park- raumüberwachungsorganes der Landespolizeidirektion Wien, welche als taugliches Beweis- mittel anzusehen sei (Verweis auf das Erkenntnis des Verwaltungsgerichtshofes vom  07.09.1990, ZI. 90/18/0079), eindeutig ersichtlich sei, dass das in Rede stehende Kraftfahrzeug  am 8. Juli 2021 um 09:24 Uhr in Holzrechengasse 17, 9907 Tristach, Österreich, in einer gebührenpflichtigen Kurzparkzone  abgestellt war, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben, da der Parkschein insofern unrichtig entwertet war, als  er die Entwertungen 09:30 Uhr getragen habe.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Holzrechengasse 17, 9907 Tristach, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_61`)


Die Angaben des anzeigelegenden Parkraumüberwachungsorganes der Landespolizeidirektion  Wien seien klar, deutlich und frei von Widersprüchen gewesen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_11`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von  Kontrollorganen der Parkraumüberwachung der Landespolizeidirektion Wien in der  gebührenpflichtigen Kurzparkzone in 1120 Wien, Strohberggasse 34 u. 34a, am 12. Juli 2022,  16:08 Uhr, 13. Juli 2022, 14:04 Uhr, 14. Juli 2022, 09:05 Uhr und am 19. Juli 2022, 10:20 Uhr,  zur Anzeige gebracht, da kein gültiger Parknachweis vorlag.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin (ZB) des  mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna eingeholten Lenker- auskunft mit Strafverfügung vom 20. Dezember 2022 an, er habe das Fahrzeug am 3. Oktober  2022 in der gebührenpflichtigen Kurzparkzone in Grub-Mallinger-Straße 6, 4782 Bubing, Österreich  ohne einen für den  Beanstandungszeitpunkt 12:20 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Grub-Mallinger-Straße 6, 4782 Bubing, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 7. Oktober 2022 an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 10. August 2022 in  der gebührenpflichtigen Kurzparkzone in 1180 Wien, Edmund-Weiß-Gasse nächst ONr. 21,  ohne einen für den Beanstandungszeitpunkt 17:14 Uhr gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 2. Mai 2022 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 1. März 2022 in der  gebührenpflichtigen Kurzparkzone in 1080 Wien, Lerchenfelder Straße 30, ohne einen für den  Beanstandungszeitpunkt 12:32 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_8`)


Entscheidungsgründe  Verfahrensgang  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (ANr) am 10.  November 2022 um 15:01 Uhr in 1220 Wien, Bodmergasse 70, zur Anzeige gebracht, da ein  gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_47`)


Eine  Nachfrage bei der Landespolizeidirektion Wien, Parkraumüberwachungsgruppe habe ergeben,  dass der Meldungsleger zur Tatzeit in Wien 22 seinen Dienst versehen habe und daher ein  Irrtum bei der Angabe des Tatdatums auszuschließen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_7`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (X. GmbH) eingeholten  Lenkerauskunft mit Strafverfügung vom 9. März 2023 an, er habe das Fahrzeug am 27.  Dezember 2022 in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Gasse, ohne einen für  den Beanstandungszeitpunkt 21:21 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_4`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach durchgeführter Lenkererhebung mit Strafverfügung  vom 29. März 2023 an, sie habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Vienna am 8. März 2023 in der gebührenpflichtigen Kurzparkzone in 1010 Wien,  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_14`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige,  welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund  einer eigenen dienstlichen Wahrnehmung gelegt wurde sowie in drei anlässlich der  Beanstandung angefertigte Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_22`)


Dazu wird Folgendes festgestellt:  Der Anzeige des Parkraumüberwachungsorgans der Landespolizeidirektion Wien, welche auf  Grund einer eigenen dienstlichen Wahrnehmung gelegt wurde und welche als taugliches  Beweismittel anzusehen ist (Erkenntnis des Verwaltungsgerichtshofes vom 7.9.1990,  ZI.90/18/0079), ist zu entnehmen, dass das Fahrzeug in einer gebührenpflichtigen Kurzparkzone  gestanden ist, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültig  2 von 9 Seite 3 von 9

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_12`)


In der Begründung wurde dargelegt, dass Beweis genommen wurde durch Einsichtnahme in  die Organstrafverfügung, welche von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien auf Grund einer eigenen dienstlichen Wahrnehmung gelegt  worden sei, sowie in die von diesem angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_103`)


Mit dem Beschwerdeeinwand, die Bf. habe keine Organstrafverfügung am Fahrzeug  vorgefunden, lässt sich für die Bf. nichts gewinnen, da dem Organ der öffentlichen Aufsicht ein  Wahlrecht eingeräumt ist, ob es eine Anonymverfügung gemäß § 49a VStG (im Falle eines  Organs der Verwaltungsstrafbehörde selbst) bzw. eine Organstrafverfügung gemäß § 50 VStG  (im Falle eines Organes der Landespolizeidirektion Wien) oder eine Anzeige erstattet  (Lewisch/Fister/Weilguni, Verwaltungsstrafgesetz, § 50 Tz 4), durch die das  Verwaltungsstrafverfahren gemäß §§ 40 ff.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_5`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 15. April  2024 um 14:14 Uhr in 1020 Wien, Lusthausstraße nächst Baum 2048 zur Anzeige gebracht, da  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_8`)


Entscheidungsgründe  Verfahrensgang:   Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen Kennz1 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 5.  November 2024 um 08:56 Uhr in Haussteingasse 28, 8144 Attendorfberg, Österreich, beanstandet, da ein gültiger Parkschein  fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Haussteingasse 28, 8144 Attendorfberg, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_58`)


Beweiswürdigung:  Die Abstellung des Fahrzeuges in der gebührenpflichtigen Kurzparkzone ohne gültigen  Parkschein lässt sich aus der Anzeige des Kontrollorgans der Parkraumüberwachung der  Landespolizeidirektion Wien und den im Akt aufliegenden, zum Beanstandungszeitpunkt  aufgenommenen Fotos ersehen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_62`)


Dass der Bf. zum Beanstandungszeitpunkt der Zulassungsbesitzer des in Rede stehenden  Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A) war, ergibt sich aus der Anzeige  des Kontrollorgans der Parkraumüberwachung der Landespolizeidirektion Wien (Akt S 2).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_20`)


„Aus der dem Verfahren zugrundeliegenden Organstrafverfügung samt Fotos, welche von  einem Organ der Landespolizeidirektion Wien erstattet wurde, geht hervor, dass das von Ihnen  gelenkte Kraftfahrzeug beanstandet wurde, weil es ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

**False Positives:**

- `Magistrat der Stadt  Wien Magistratsabteilung 67` — partial — gold is substring of pred: `Magistrat der Stadt  Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pjotr Niessl`(person)
- `Magistrat der Stadt  Wien`(organisation)

</details>

---

## `german_specific_orgs` 🏆

**F1:** 0.049 | **Precision:** 0.958 | **Recall:** 0.025  

**Format:** `regex`  
**Rule ID:** `9bbf5818`  
**Description:**
Matches specific known organizations including ministries, federal offices, and universities.

**Content:**
```
\b(ÖGK|Wirtschaftsuniversität\s+Wien|Bundesministerium\s+für\s+Finanzen|Bundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen|Deutschen\s+Rentenversicherung\s+Bund|Magistrat(?:s)?\s+der\s+Stadt\s+Wien|Wiener\s+Gemeinderat(?:s)?|Bundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.958 | 0.025 | 0.049 | 120 | 115 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 115 | 5 | 4484 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_6`)


Im Wintersemester 2015/16 begann er mit dem Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der Wirtschaftsuniversität Wien.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_32`)


Unstrittig ist, dass der Sohn des Bf. im Wintersemester 2017/2018 mit dem Studium der  Humanmedizin an der Universität Wien begann und davor, beginnend  mit dem  Sommersemester 2016, das Bachelorstudium Wirtschaftsrecht an der Wirtschaftsuniversität  Wien betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität  Wien` | `Wirtschaftsuniversität  Wien` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_22`)


Diese Zeitangabe ist deshalb  glaubwürdig, weil den Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die  Erfüllung der übertragenen Aufgaben elektronische Überwachungsgeräte (sog. PDA's) zur  Verfügung stehen, welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen Server  beziehen und vorgeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_25`)


Auf den Einwand des Bf. bezüglich der Strafbemessung bei Geschwindigkeitsübertretungen  könne nicht eingegangen werden, weil kein sachlicher Zusammenhang bestehe, zumal diese  Delikte nicht in die Zuständigkeit des Magistrats der Stadt Wien fallen würden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_48`)


Sachverständigengutachten nach der Einschätzungsverordnung von Dr.in 2, Neurologin,  Bundesamt für Soziales und Behindertenwesen, am 07.05.2019 erstellt:  „Anamnese:  In einem Vorgutachten wurde eine Persönlichkeitsstörung (histrionisch), Panikstörung,  posttraumatische Belastungsstörung, chronische Kopfschmerzen mit 50% GdB rückwirkend an  Hand der Befunde ab 10/2012 beurteilt. Die Behinderung bestehe bereits vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_93`)


Die erhöhte Familienbeihilfe steht daher nicht zu.  Im Zuge dieser Erledigung erstellte das Bundesamt für Soziales und Behindertenwesen im  Auftrag des Finanzamtes folgende Bescheinigung(en) über das Ausmaß der Behinderung, die  Ihnen zeitnah und mit separater Post zugesendet wird/werden.“

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_246`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_255`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt, eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Roxana Dellner` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `88-034/0292` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_46`)


Am 25.06.2014 fand eine fachärztliche  Untersuchung aus dem Bereich der Neurologie des Beschwerdeführers beim Bundesamt für  Soziales und Behindertenwesen, zur Erstellung eines Sachverständigengutachtens, statt.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_260`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_7`)


Da er die mit Anonymverfügung vorgeschriebene Geldstrafe nicht zahlte, warf der Magistrat  der Stadt Wien dem Beschwerdeführer(Bf.) in der Strafverfügung vom 02. Jänner 2020 vor, er  habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das mehrspurige  Kraftfahrzeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen  am 4. November 2019 um 17:31 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt,  ohne für seine Kennzeichnung mit einem zur Tatzeit gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_36`)


Die von mir in der Vernehmung vom 17.01.2020 im Magistrat der  Stadt Wien in … angeführten Angaben wurden keinesfalls ernst genommen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_79`)


2. Beweiswürdigung  Der Sachverhalt ist auf Grund des Finanzamtsaktes sowie der Eingaben der Bf und der  schriftlichen Aussagen des Herrn C vor der KIAB (nunmehr Finanzpolizei) bzw. des  Strafverfahrens des Magistrats der Stadt Wien gegen die Geschäftsführerin der Bf wegen  illegaler Beschäftigung nach dem AuslBG als erwiesen anzusehen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzpolizei` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_7`)


II. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der  Stadt Wien vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, als unbegründet abge- wiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_16`)


Da der Zulassungsbesitzer angab, seine Ehegattin habe sein Fahrzeug am 11.03.2020 um  10:54 Uhr und am 09.03.2020 um 13:31 Uhr ohne Parkschein in einer gebührenpflichtigen  Kurzparkzone abgestellt und da die Ehegattin die an sie adressierten und für diese Tattage und  Tatzeiten erlassenen Strafverfügungen fristgerecht angefochten hatte, erließ der Magistrat der  Stadt Wien am 24.08.2020 erstens ein an die Ehegattin adressiertes Straferkenntnis zur Ge- schäftszahl MA67/206700639161/2020 und zweitens ein an die Ehegattin adressiertes Strafer- kenntnis zur Geschäftszahl MA67/206700639163/2020.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_29`)


Die Bf. habe den Magistrat der Stadt  Wien ersucht zu prüfen, ob statt Geldstrafen zu verhängen, Ermahnungen erteilt werden kön- nen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_3`)


Am Ausspruch des Magistrats der Stadt Wien, dass der Beschwerdeführer gem. § 64 Abs. 2  VStG 1991 einen Beitrag zu den Kosten des erstinstanzlichen Strafverfahrens zu zahlen hat, tritt  keine Änderung ein.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_45`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte und für die Beurtei- lung, ob die Benützung eines Massenbeförderungsmittels zumutbar oder unzumutbar ist, ist  für Verhältnisse innerhalb Österreichs nach § 3 Abs. 1 der ua. aufgrund des § 16 Abs. 1 Z 6  EStG 1988 ergangenen Pendlerverordnung, BGBl. II Nr. 276/2013 idF BGBl. II Nr. 154/2014, der  vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte Pendlerrechner zu  verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_74`)


Dem Beschwerdeführer wurde vom Bundesamt für Soziales und Behindertenwesen ein durch  die Epilepsie bedingter Gesamtgrad der Behinderung von 40% und ein durch die Erkrankung  des Verdauungssystems bedingter Grad der Behinderung von 10% bescheinigt, wobei eine  wechselseitige Beeinflussung nicht festgestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_18`)


Im elektronisch vorgelegten Akt befinden sich Ablichtungen von (Schulbesuchs-)Bestätigungen  und Zeugnissen sowie die erste Seite eines Bescheides des Magistrats der Stadt Wien für den  streitgegenständlichen Zeitraum.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_66`)


Dem Bf wurde laut Bescheid des Magistrats der Stadt Wien vom 06.10.2015, Betreff:  „Mindestsicherung, Zuerkennung“ eine Leistung zur Deckung des Lebensunterhalts und der  Grundbetrag zur Deckung des Wohnbedarfs ab November 2015 bis jedenfalls August 2016  zuerkannt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_37`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  (Die Bf.) bezieht neben ihrer österreichischen Pension von der "Versicherungsanstalt für  Eisenbahnen und Bergbau" eine Pension von der Deutschen Rentenversicherung Bund.

| Predicted | Gold |
|---|---|
| `Deutschen Rentenversicherung Bund` | `Deutschen Rentenversicherung Bund` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_20`)


Dieses Erkenntnis ist in Rechtskraft erwachsen (E-Mail des Prüfers vom  11.07.2019 an das Bundesministerium für Finanzen).

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_32`)


Die steuerliche Vertretung des BF beantragte daraufhin mit Schreiben vom 16.8.2018 beim  Bundesministerium für Finanzen die Einleitung eines Verständigungsverfahrens mit Malta.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_71`)


Wie bereits im angefochtenen Bescheid ausgeführt wurde, normiert § 48 BAO Folgendes:  „Das Bundesministerium für Finanzen kann bei Abgabepflichtigen, die der Abgabenhoheit  mehrerer Staaten unterliegen, soweit dies zur Ausgleichung der in- und ausländischen  Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit entsprechenden  Behandlung erforderlich ist anordnen, bestimmte Gegenstände ganz oder teilweise aus der  5 von 12 Seite 6 von 12

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_74`)


Diese dem Bundesministerium für  Finanzen erteilte Ermächtigung erweist sich auf Grund der bisherigen Erfahrungen als  unbedingt erforderlich, um insbesondere im Verhältnis zu solchen Staaten, mit denen eine  staatsvertragliche Regelung zur Vermeidung von Doppelbesteuerungen nicht besteht oder  nicht zu erwarten ist, für die in Betracht kommenden Besteuerungsfälle Abhilfe gegen  Doppelbesteuerungen zu schaffen oder eine der Gegenseitigkeit entsprechende Behandlung zu  gewährleisten.

| Predicted | Gold |
|---|---|
| `Bundesministerium für  Finanzen` | `Bundesministerium für  Finanzen` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_46`)


Am 20.08.2020 wurde die im Bundesministerium für Finanzen für die automationsunterstützte  Datenverarbeitung zuständige Sektion I aufgefordert, Fragen im Zusammenhang mit den  konkreten Bescheiderstellungen zu beantworten, sowie diesbezügliche Beweismittel  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_49`)


Zwischenzeitig ist – da eine Verlängerung der Frist aufgrund von COVID-19-Maßnahmen  gesetzlich nicht (mehr) möglich ist – die im § 43 Abs. 1 VwGVG normierte Frist nach dem  6. Februar 2021 bereits abgelaufen, sodass das angefochtene Straferkenntnis des Magistrats  der Stadt Wien von Gesetzes wegen außer Kraft getreten und das Strafverfahren einzustellen  ist (vgl. VwGH 26.8.2014, Ro 2014/02/0106).

| Predicted | Gold |
|---|---|
| `Magistrats  der Stadt Wien` | `Magistrats  der Stadt Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_3`)


Begründung  Mit Bescheid des Finanzamtes vom 17. Juli 2020 wurde der Antrag des durch den Magistrat der  Stadt Wien Kinder- und Jugendhilfe, Rechtsvertretung 16,17, 18, 19, vertretenen  minderjährigen Beschwerdeführers (kurz: Bf) auf Zuerkennung der Familienbeihilfe gemäß § 6  Abs. 5 FLAG 1967 ab Jänner 2016 abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_5`)


Informativ wird mitgeteilt, dass der Beitrag zu den Kosten des behördlichen Verfahrens  (€ 10,00) zusammen mit der Geldstrafe (€ 36,00), insgesamt somit € 46,00, an den Magistrat  der Stadt Wien zu entrichten sind, wofür weitere Informationen am Ende dieser Entscheidung  des BFG und am Ende des angefochtenen Straferkenntnisses des Magistrates zu finden sind.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_121`)


Konto, Weiterversicherung bei der ÖGK,  inländ.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_26`)


Die Beiträge zu den  Kosten des Beschwerdeverfahrens (6x € 12,00) sind zusammen mit den Geldstrafen (6x € 60,00)  und den Beiträgen zu den Kosten des behördlichen Verfahrens (6x € 10,00) an den Magistrat  der Stadt Wien zu entrichten, der zu entrichtende Gesamtbetrag beträgt 6x € 82,00.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_28`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_10`)


Aus dem diesbezüglich vom Sozialministeriumservice (vormals Bundesamt für Soziales und  Behindertenwesen) am 12./13.3.2020 erstellten und der Bf übermittelten ärztlichen  Sachverständigengutachten "mit Untersuchung" durch Amanda Zacharek  Fachärztin für Kinder- und  Jugendheilkunde, geht auszugsweise Folgendes hervor:  "Anamnese:  Termingeburt, verzögerte Meilensteine der Entwicklung, freies Laufen mit 23 Monaten, Sitzen  mit 12 Monaten, Sprachentwicklungsverzögerung.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Amanda Zacharek` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_180`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_210`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  als Amtssachverständige bedient, die in die bei dieser Behörde gem. § 90 KOVG 1957 zu  führende Sachverständigenliste, nicht aber in die Liste der allgemein beeideten und gerichtlich  12 von 18 Seite 13 von 18

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_15`)


Mit Straferkenntnis vom 13. Jänner 2021, MA67/Zahl/2020, wurde der Bf. vom Magistrat der  Stadt Wien, MA 67, wegen der bereits näher bezeichneten Verwaltungsübertretung für  schuldig befunden und wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  von € 60,00 sowie für den Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden  festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_18`)


Im Vorlageantrag wiederholte der Bf. im Wesentlichen sein Vorbringen aus der Beschwerde  und verwies ergänzend auf eine vom Bundesministerium für Finanzen herausgegebene Bro- schüre, eine in Jakom/Baldauf 2012 zu § 34 Rz 87 vertretene Rechtsmeinung und den 1. Lohn- steuer-Wartungserlass 2011.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Michael Klingsohr` (person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich` (address)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Missed by this rule (FN):**

- `Bodewein` (person)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Missed by this rule (FN):**

- `Bodewein` (person)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Estelle Ivankovic, Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich, vom 27. Jänner 2022, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, als Abgabenstrafbehörde vom 3. Jänner 2022, Zahl MA67/Zahl/2021, betreffend  eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4  Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl. für  Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Missed by this rule (FN):**

- `Estelle Ivankovic` (person)
- `Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich` (address)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_8`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 67, vom 3. Jänner  2022, Zahl MA67/Zahl/2021, wurde über die Beschwerdeführerin (in der Folge kurz Bf.  genannt) eine Geldstrafe in Höhe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt, weil sie das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 6. Oktober 2021 um 18:35 Uhr in einer  gebührenpflichtigen Kurzparkzone in 1010 Wien, Adresse, abgestellt habe ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_101`)


Auf Grund einer Vereinbarung im Bundesministerium für Finanzen im Zuge der Einführung von  FinanzOnline und der Einführung der elektronischen Umsatzsteuervoranmeldungen werden im  automatisierten Verfahren seit dem Jahr 2003 folgende Verspätungszuschläge bei Nichtabgabe  von Umsatzsteuervoranmeldungen verhängt:  Bei einer Verspätung bis zu 10 Tagen: 0 Prozent  Bei einer Verspätung von 11 bis 15 Tagen: 2 Prozent  Bei einer Verspätung von 16 bis 25 Tage: 5 Prozent  Bei einer Verspätung von mehr als 25 Tagen: 8 Prozent

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_179`)


Die Merkmale der natürlichen und wirtschaftlichen Ertragsbedingungen dieses  Hauptvergleichsbetriebes sind vom Bundesministerium für Finanzen nach Beratung im  Bewertungsbeirat durch Verordnung rechtsverbindlich festzustellen und im „Amtsblatt zur  Wiener Zeitung“ kundzumachen (§ 44).

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_182`)


Um für die Bewertung aller in der Natur tatsächlich vorkommenden landwirtschaftlichen  Betriebe innerhalb des Bundesgebietes die Gleichmäßigkeit zu sichern und Grundlagen durch  feststehende Ausgangspunkte zu schaffen, stellt das Bundesministerium für Finanzen für  bestimmte Betriebe (Vergleichsbetriebe) nach Beratung im Bewertungsbeirat mit  rechtsverbindlicher Kraft das Verhältnis fest, in dem die Vergleichsbetriebe nach ihrer  Ertragsfähigkeit auf die Flächeneinheit (Hektar) bezogen zum Hauptvergleichsbetriebe stehen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_240`)


Nach Beratung im Bewertungsbeirat trifft das Bundesministerium für Finanzen über den  Gegenstand der Beratung die Entscheidung.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Christine Kralova` (person)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Anton Fleischhacker` (person)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) stellte mit Schreiben vom 27.12.2017, eingelangt beim Magistrat  der Stadt Wien am 2.1.2018, den Antrag, die Vergnügungssteuer für den Zeitraum vom  1.1.2012 bis 31.12.2015 bescheidmäßig festzusetzen, da die Bf die Rechtsansicht vertrete, dass  es aufgrund der Kollision der Rechtsnormen Glücksspielgesetz und dem Gesetz über die  Besteuerung von Vergnügen im Gebiet der Stadt Wien (Vergnügungssteuergesetz 2005) zu  einer Doppelbesteuerung komme.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_28`)


Für die Einschätzung des Grades der Behinderung  sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des Behinderten- einstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere Be- stimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_22`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_4`)


2. Beigeschlossen waren ein Bescheid des Bundessozialamtes vom 5.12.2013, wonach der Bf  auf ihren Antrag v. 8.11.2013 gemäß Verbrechensopfergesetz "zwecks Aufarbeitung der 1982  erlittenen psychischen Gesundheitsschädigungen die Übernahme der entstehenden Kosten für  eine psychotherapeutische Krankenbehandlung …." bewilligt wird, sowie ein Schreiben der ÖGK  vom 8.10.2020 über die Zuerkennung von Rehabilitationsgeld ab 1.6.2015.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_54`)


Sie hat ab 1.6.2015 bis 31.10.2021 Rehabilitationsgeld, dies zwecks Wiederherstellung der  Arbeitsfähigkeit durch Reha-Maßnahmen, erhalten (siehe Schreiben ÖGK v. 8.10.2020 und PV- Bescheid 31.8.2021).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Sascha de Kort` (person)
- `Matthew McCarthy` (person)
- `Stichlberg 18, 4742 Klinget, Österreich` (address)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_73`)


Die in ausländischer Währung gezahlten gleichartigen ausländischen Beihilfen sind nach den  vom Bundesministerium für Finanzen auf Grund des § 4 Abs. 8 des Umsatzsteuergesetzes 1972,  BGBl. Nr. 223/1972, in der "Wiener Zeitung" kundgemachten jeweiligen Durchschnittskursen in  inländische Währung umzurechnen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 €) sind gemeinsam mit der Geldstrafe  (60,00 €) und dem Beitrag zu den Kosten der belangten Behörde (10,00 €), insgesamt  82,00 €, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 18. Oktober 2019 wies das Finanzamt den Antrag der Beschwerdeführerin  (Bf.) vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur Familienbeihilfe für  ihren im Mai 2007 geborenen Sohn A. - ab dem im Antrag genannten Zeitpunkt Juli 2019 - mit  dem Hinweis auf die im Zuge dieser Erledigung vom Bundesamt für Soziales und  Behindertenwesen im Auftrag des Finanzamtes erstellte Bescheinigung vom 15. Oktober 2019  über das Ausmaß der Behinderung des Sohnes mit der Begründung ab, es sei ein Grad der  Behinderung von 30% festgestellt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_14`)


Über Anforderung des Finanzamtes an das Bundesamt für Soziales und Behindertenwesen  wurde der Sohn der Bf. am 31. August 2020 durch einen Arzt für Kinder und Jugendheilkunde  ein weiteres Mal untersucht und ein Sachverständigengutachten erstellt.   (Die Sachverständigengutachten werden im Erwägungsteil wiedergegeben).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_172`)


Für die Einschätzung des Grades der  Behinderung sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_5`)


Die Kosten der Beschwerdeverfahren (je 12,00 €) sind gemeinsam mit den Geldstrafen (je  60,00 €) und den Beiträgen zu den Kosten der belangten Behörde (je 10,00 €), insgesamt  328,00 €, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_228`)


2. Nach den Bestimmungen des DBA-Deutschland ist die BRD somit nur für eine Besteuerung  des Rentenbezuges von der Deutschen Rentenversicherung Bund zuständig.

| Predicted | Gold |
|---|---|
| `Deutschen Rentenversicherung Bund` | `Deutschen Rentenversicherung Bund` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_22`)


Die für schriftliche Anbringen geltenden  Bestimmungen sind auch in diesen Fällen mit der Maßgabe anzuwenden, daß das Fehlen einer  Unterschrift keinen Mangel darstellt. Die Abgabenbehörde und das Verwaltungsgericht können  jedoch, wenn es die Wichtigkeit des Anbringens zweckmäßig erscheinen läßt, dem Einschreiter  die unterschriebene Bestätigung des Anbringens mit dem Hinweis auftragen, daß dieses nach  fruchtlosem Ablauf einer gleichzeitig zu bestimmenden angemessenen Frist als  zurückgenommen gilt.  Für Anbringen im Sinn des § 86a Abs. 1 erster Satz BAO, die in Abgaben-, Monopol- oder  Finanzstrafangelegenheiten an das Bundesministerium für Finanzen, an die  Verwaltungsgerichte, an ein Finanzamt, an das Zollamt Österreich oder an das Amt für  Betrugsbekämpfung gerichtet werden, wird die Einreichung unter Verwendung eines  Telekopierers (Telefaxgerätes) zugelassen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Zollamt Österreich` (organisation)
- `Amt für  Betrugsbekämpfung` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_92`)


Hier erweist sich das  Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem Magistrat der Stadt  Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den (anderen) Verwaltungs- gerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_81`)


In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_94`)


Das Bundesamt für Soziales und Behindertenwesen hat mit ausdrücklicher Einwilligung der  betroffenen Person dem zuständigen Finanzamt und dem Arbeitgeber, der Bezüge aus einer  gesetzlichen Sozialversicherung oder Ruhegenussbezüge einer Gebietskörperschaft im Sinne  des § 25 Abs. 1 Z 1, 3 oder 4 auszahlt, die vom Bundesamt für Soziales und Behindertenwesen  gespeicherten und für die Berücksichtigung von Freibeträgen im Sinne der Abs. 1 bis 3 und 7  erforderlichen personenbezogenen Daten elektronisch zu übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_105`)


Diese ist - abgesehen von im vorliegenden Fall nicht relevanten Ausnahmen - regelmäßig das  Bundesamt für Soziales und Behindertenwesen (nunmehr kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_108`)


Die Feststellung einer Behinderung und ihres Ausmaßes der Minderung der Erwerbsfähigkeit  bzw. des Grades der Behinderung, ist somit nicht von der Abgabenbehörde, sondern bindend  vom Bundesamt für Soziales und Behindertenwesen zu treffen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_120`)


Gemäß § 35 Abs. 1 EStG 1988 steht dem Steuerpflichtigen ein Freibetrag (Abs. 3) zu, wenn er  außergewöhnliche Belastungen bei Anspruch auf den Alleinverdienerabsetzbetrag durch eine   Behinderung des (Ehe-)Partners (§106 Abs. 3) hat und er keine pflegebedingte Geldleistung  (Pflegegeld, Pflegezulage oder Blindengeld) erhält.  Zuständige Stelle ist auch in diesem Fall gemäß § 35 Abs. 2 Z 2 EStG das Bundesamt für Soziales  und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_79`)


2. in Widerspruch zu nicht offensichtlich unrichtigen Rechtsauslegungen steht, die               a) dem Abgabepflichtigen gegenüber von der für ihn zuständigen Abgabenbehörde geäußert  oder                              b) vom Bundesministerium für Finanzen im Amtsblatt der österreichischen Finanzverwaltung  oder im Internet als Amtliche Veröffentlichung in der Findok veröffentlicht wurden, wenn im  Vertrauen auf die betreffende Äußerung bzw. Veröffentlichung für die Verwirklichung des die  Abgabepflicht auslösenden Sachverhaltes bedeutsame Maßnahmen gesetzt wurden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_6`)


Informativ wird mitgeteilt, dass der Beitrag zu den Kosten des behördlichen Verfahrens  (10,00 Euro) zusammen mit der Geldstrafe (60,00 Euro) und dem Beitrag zu den Kosten des  Beschwerdeverfahrens (12,00 Euro), insgesamt somit 82,00 Euro, an den Magistrat der Stadt  Wien zu entrichten sind, wofür weitere Informationen am Ende dieser Entscheidung des BFG  und am Ende des angefochtenen Straferkenntnisses des Magistrates zu finden sind.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_8`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrats der Stadt Wien (belangte Behörde), Magistratsabteilung 67,  vom 24. Jänner 2024, GZ. MA67/GZ/2023, wurde über die Beschwerdeführerin (in der Folge  kurz Bf. genannt) eine Geldstrafe in Höhe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt, weil sie das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 29. September 2023 um 17:30 Uhr in einer  gebührenpflichtigen Kurzparkzone in 1130 Wien, xStraße gegenüber 2, abgestellt habe, ohne  für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein  gesorgt zu haben, da sich im Fahrzeug lediglich der Parkschein Nr. PSNr befunden habe,  welcher insofern unrichtig entwertet gewesen sei, als er die Entwertungen 17:35 Uhr getragen  habe.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/144290.1`) (sent_id: `deanon_BFG_20260814_TEST/144290.1_12`)


Diese Erwerbsvorgänge wurden von der Grundverkehrsbehörde, dem Magistrat der Stadt  Wien, mit den Bescheiden vom 10.10.2022 genehmigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri. über die zwei (gleichlautenden)  Beschwerden des Edwin Formanski, Menschenrechtsplatz 2, 3441 Gollarn, Österreich, vom 28. Mai 2024, als gemäß § 9 Abs. 1 VStG zur  Vertretung nach außen berufene Person der Firma Firma mit Sitz in AdrFirma, gegen die zwei  Straferkenntnisse des Magistrats der Stadt Wien, Magistratsabteilung 67, als  Abgabenstrafbehörde, vom 24. Mai 2024, GZ. 1) MA67/GZ1/2024 und GZ. 2) MA67/GZ2/2024,  beide wegen einer Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird den zwei Beschwerden  insoweit teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 60,00 Euro auf  jeweils 36,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten  Ersatzfreiheitsstrafen von jeweils 14 auf jeweils 10 Stunden herabgesetzt werden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Edwin Formanski` (person)
- `Menschenrechtsplatz 2, 3441 Gollarn, Österreich` (address)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_5`)


Am 20.2.2024 übermittelte die Österreichische Gesundheitskasse (ÖGK) einen weiteren  Lohnzettel betreffend den Bf. für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_10`)


seien die jeweiligen ÖGK-Beträge zu hoch bemessen worden und nach Ablauf des Jahres 2022  im Jahr 2023 im Betrag von 1.784,33€ rückerstattet worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_13`)


Mit Schreiben vom 15.5.2024 begehrte der Bf. die Vorlage der Beschwerde an das  Bundesfinanzgericht mit dem Hinweis, dass er sich nicht vorstellen könne, dass der Lohnzettel  der ÖGK innerhalb der gesetzlichen Frist eingebracht worden sei und ihm überdies der  Familienbonus von 2.000 € zustehe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_14`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Übermittlung des Lohnzettels des ÖGK an das FA erfolgte – wie sich aus der Einsichtnahme  in die elektronischen Datenbestände für den Bf. erkennen lassen – am 20.2.204 um 01:47:38  via ELDA.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_22`)


ÖGK), welcher zusätzliche steuerpflichtige Bezüge ausweist bildet einen derartigen  Wiederaufnahmegrund.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_34`)


Aus den Ausführungen zu den Gründen für die Rückzahlung zuviel bezahlter Beiträge durch die  ÖGK ist festzuhalten, dass die erhöhten SV-Beträge zunächst als Werbungkosten die  Bemessungsgrundlage für die Einkommensteuer (Lohnsteuer) 2022 gemindert haben und die  Rückzahlung 2023 diese Minderung der Bemessungsgrundlage für die Einkommensteuer 2022  nunmehr rückführt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_131`)


Das Finanzamt stützt sich in seiner Argumentation im Wesentlichen darauf, dass sich die  Verpflichtung zur Abgabe einer Meldung im vorliegenden Fall aus § 6 Abs. 6 WiEReG ergebe,  und verweist in seiner Stellungnahme auf die vom Bundesministerium für Finanzen erstellten  "FAQs zum Register der wirtschaftlichen Eigentümer", hier insbesondere auf die Frage 5 samt  Beantwortung mit dem Wortlaut:  "Frage 5: Durch einen Gesellschafterwechsel ist nachträglich eine Meldebefreiung eingetreten.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_84`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_368`)


Für nachfolgende Aufwendungen fehlt es nach dem vorliegenden Ermittlungsergebnis an den  Voraussetzungen für einen Abzug als außergewöhnliche Belastung:   2018:  Behandlungs-/Therapiekosten, Medikamentenaufwand:  - 49,- € Dr-A (lt. Bf 17.2.2018): trotz FA-Anforderung vom 27.Aug.2020 kein Nachweis durch  Rechnung, Zahlungsbeleg oder ÖGK-Kostenersatz;  - 395,- € Dr-B (Zahlung 24.7.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch  Rechnung oder ÖGK-Kostenersatz ;  - 190,- € MRT Privatklinik-X (Zahlung 12.3.2018): trotz FA-Anforderung vom 27.Aug.2020 weder  Nachweis durch Rechnung/ ÖGK-Kostenersatz noch über die medizinische Notwendigkeit der  umgehenden Durchführung in einer Privateinrichtung;

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_372`)


kein ÖGK-Kostenersatz oder sonstiger Nachweis der medizinischen Notwendigkeit iSd  VwGH-Judikatur;   - 742,- € M. M. für Physiotherapie/Heilmassage/osteopath.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_373`)


Behandlung (lt. Bf Zahlung  8.Febr.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch Rechnung, Zahlung  oder ÖGK-Kostenersatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_374`)


Bei zwei Rechnungen des Physiotherapeuten aus 2018 ÖGK-Teilersatz (jeweils Ersatz für  Kosten der Physiotherapie/Heilmassage v. 201,60 €, nicht aber für osteopath.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_385`)


Aus den zuvor dargestellten nicht abzugsfähigen „Krankheitskosten“ resultieren  Fahrtkostenkürzungen für die nachfolgenden Wegstrecken (Entfernung lt. Bf-Aufstellungen):  - Dr-B: 128,8 km;  - ABC/Ort-10: 218,4 km;  - Ort-11/Krankenhaus an Bürotagen: 147 km (5x 29,4 km Wohnsitz/Arbeitsstätte);  - Ort-5/Privatklinik-X : 54,2 km;   - Ort-5/Physiotherapie (ÖGK-Ersatz 22.11.: 147 km/ 6x 29,4 km Wohnsitz/Arbeitsstätte);

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_386`)


(ÖGK-Ersatz 16.8.: keine betroffenen Bürotage/ keine Kürzung);

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_391`)


Des Weiteren ist die Zulässigkeit eines Abzuges als außergewöhnliche Belastung für die vom  ÖGK-Ersatz nicht umfassten 58 Fahrten zum Physiotherapeuten in Ort-5 mangels Nachweises  der medizinischen Notwendigkeit der vom Therapeuten bestätigten  „Elektrostimulationstherapie“ nicht erwiesen (Bf-Eing.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_401`)


Dazu kommen 19,66 € (anteilige Kosten Dr-D für  2019 lt. ÖGK-Ersatz 9.3.2020), insgesamt somit 974,25 €.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_405`)


Der zweite Wert enthält neben Fahrten zum Hausarzt bzw. zu zwei Ärzten,  zu deren Behandlungskosten dem Bf von der ÖGK eine Teilkostenerstattung gewährt wurde,  auch 232,8 km betreffend Fahrten, für deren Zweck der Bf trotz FA-Aufforderung zur  vollständigen Belegvorlage vom 20.Aug.2020 keinerlei Belege übermittelt hatte (23.5. Dr- E/Ort-2, 29.10.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_407`)


Unter den Fahrten zum Physiotherapeuten waren auch fünf Fahrten erfasst, die im  Zusammenhang mit einer Teilkostenerstattung der ÖGK standen (6. - 28.Febr 2019, jeweils an  „Bürotagen“, mit Fahrtkostenberechnung ab Arbeitsstätte).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_19`)


Für die Einschätzung des Grades der Behinderung sind § 14 Absatz 3 des  Behinderteneinstellungsgesetzes und die Verordnung des Bundesministers für Arbeit, Soziales  und Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades  der Behinderung (Einschätzungsverordnung) vom 18.8.2010 anzuwenden.

**False Positives:**

- `Bundesministers für Arbeit, Soziales  und Konsumentenschutz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred is substring of gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Arthur Soyal`(person)

</details>

---

## `german_tax_authorities` 🏆

**F1:** 0.726 | **Precision:** 0.908 | **Recall:** 0.604  

**Format:** `regex`  
**Rule ID:** `e6a387e2`  
**Description:**
Matches Finanzamt variations including genitive endings, specific locations, and 'für' constructions.

**Content:**
```
\b(Finanzamt(?:es)?(?:\s+(?:Wien\s+3/6/7/11/15\s+Schwechat\s+Gerasdorf|Österreich|Baden\s+Mödling|Linz|Bruck\s+Eisenstadt\s+Oberwart|Großbetriebe|für\s+Gebühren|Innsbruck))?|Zollamt(?:es)?(?:\s+Klagenfurt)?|Finanzpolizei)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.908 | 0.604 | 0.726 | 3063 | 2780 | 283 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2780 | 283 | 1819 |

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

- `Alexander Schnelldorfer` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `N.N.` (person)

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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Dr. Susanne Zankl` (person)
- `RgR Amalia Schuetzke` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `22-967/4918` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_8`)


Mit Ergänzungsersuchen vom 11.07.2017 forderte das Finanzamt die Bf auf, eine Kopie der  Originalrechnung des Steinmetzbetriebes und eine der Verlassenschaftsabhandlung (Beschluss  vom Gericht), in der das Aktivvermögen angeführt ist, nachzureichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_42`)


Tag  (Fälligkeitstag) des auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden  Kalendermonates eine Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen  Finanzamt einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  (Vorauszahlung) oder den auf den Voranmeldungszeitraum entfallenden Überschuß unter  entsprechender Anwendung des § 20 Abs. 1 und 2 und des § 16 selbst zu berechnen hat.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_4`)


Das Finanzamt X (FA) verneint die Anwendbarkeit, weil der Betrieb des Bf im  Verfahrenszeitraum der Bestimmung des § 111 Abs. 2 GewO 1994 zuzuordnen gewesen und  damit nicht ganzjährig einer Verpflichtung zur Innehabung einer Gewerberechtigung  unterlegen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Gebühren` | `Finanzamtes für Gebühren` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Ophelia Dutschka` (person)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_29`)


In weiteren Schreiben durch unsere Kanzlei  vom 6.6.2018 sowie 26.6.2018 an das zuständige Finanzamt für Gebühren, Verkehrssteuern  und Glückspiel wurde der Sachverhalt nochmals konkret aufgezeigt und erläutert.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_4`)


Der Beschwerdeführer machte im Rahmen der Arbeitnehmerveranlagung 2017 nachstehende  Werbungskosten geltend:  Fachliteratur 419,16 €  Fortbildungs-, Ausbildungs- und Umschulungskosten 5.364,12 €  Werbungskosten gesamt 5.783,28 €  Bei der Veranlagung anerkannte das Finanzamt lediglich den Pauschbetrag für  Werbungskosten in Höhe von 132 €; (Bescheid vom 22.1.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_8`)


Mit Beschwerdevorentscheidung vom 11.7.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_38`)


Die Frage des Finanzamtes in seinem Vorhalt vom 22.10.2018 „Wollen Sie die erworbenen  Kenntnisse als selbständig Tätiger verwerten?“ hat der Beschwerdeführer folgendermaßen  beantwortet:  „Ich stelle Überlegungen an, die mit der laufenden Aus- bzw. Weiterbildung erworbenen  Kenntnisse auch als selbständig Tätiger zu verwerten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_15`)


Dagegen sei weder Berufung erhoben, noch seien seitens des Finanzamtes weitere  nach außen erkennbare (verjährungsverlängernde) Amtshandlungen gesetzt worden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_35`)


Da die als verfassungswidrig erkannte Befristung für den hier zu beurteilenden Beschwerdefall  keine Wirkung (mehr) zu entfalten vermag, war der Beschwerde gegen den  Zurückweisungsbescheid des Finanzamtes vom 2.3.2018 auf Grund der oa. VfGH- bzw. VwGH- Erkenntnisse stattzugeben und der Zurückweisungsbescheid aufzuheben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Siegfried Basyurt` (person)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_24`)


Im Akt erliegen zwei Internet-Abfragen des Finanzamtes (EurotaxGlass-Fahrzeugbewertung;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_26`)


Mit Bescheid vom 9.11.2010, StrNr, hat das Finanzamt der Bf für das Fahrzeug Range Rover  Sport 3.0 TDV6 HSE mit der Fahrgestellnummer X1:  a) ausgehend von der Bemessungsgrundlage € 57.090,64 die Normverbrauchsabgabe (NoVA)  im Ausmaß von 14 % unter Berücksichtigung von Malus (§ 6a NoVAG) und Abgabenerhöhung  (§ 6 Abs. 6 NoVAG) im Betrag von€

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_54`)


Das Finanzamt hat in der Folge, ohne eine Berufungsvorentscheidung zu erlassen, die Berufung  samt Verwaltungsakt dem Unabhängigen Finanzsenat zur Entscheidung vorgelegt und die  Abweisung der Berufung beantragt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_58`)


Es ist daher dem Finanzamt zu erläutern und nachzuweisen,  inwieweit die Frau falsche Angaben gemacht haben soll (bezüglich Familienwohnsitz,  Angestelltenverhältnis, Verwendung des PKWs etc.).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_60`)


…"  b) Mail-Schreiben des C vom 26.8.2010, mit dem in der Beilage der Leasingvertrag zum PKW  dem Finanzamt übermittelt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Basyurt` (person)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_73`)


Im Zeitpunkt der Unterfertigung der Niederschrift vor dem Finanzamt durch die Bf (= am  27.7.2010) habe der Tachostand des Fahrzeuges ca. 25.000 km betragen, der aufgrund der  Fahrten des Gatten D-A1-D zustande gekommen wäre;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_165`)


Die Beschwerde richtet sich primär dagegen, dass die Umsätze für die Sexdienstleistungen vom  Finanzamt der Bf. zugerechnet werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_214`)


Die Prostitutionserlöse waren daher vom Finanzamt zu Recht der Bf. zuzurechnen, da sie zum  Betrieb eines Bordells (mit den entsprechenden Auflagen) berechtigt war und sie in  einschlägigen Medien einerseits Werbung für „ihre Girls“ geschalten sowie andererseits –  mehrsprachig - Prostituierte für ihre Bar angeworben hat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_3`)


Entscheidungsgründe  Mit Bescheiden vom 6. Mai 2019 verfügte das Finanzamt die Pfändung und Überweisung einer  Geldforderung der Beschwerdeführerin an die X-Bank zur Hereinbringung der in Höhe von  € 7.870,70 (Abgabenschuldigkeiten in Höhe von € 7.786,22 zuzüglich Gebühren und  Barauslagen für diese Pfändung in Höhe von 84,48).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_4`)


Mit einem weiteren Bescheid vom 6. Mai 2019 setzte das Finanzamt gegenüber der Bf. für  diese Amtshandlung Pfändungsgebühren in Höhe von € 77,86 und Auslagenersätze in Höhe  von € 6,62 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_15`)


Mit Beschwerdevorentscheidungen von 22. Mai 2019 wies das Finanzamt die Beschwerden als  unbegründet ab und führte aus:  a) BVE zur Beschwerde gegen den Pfändungsbescheid  Die Pfändung einer Geldforderung sei gemäß § 65 AbgEO zu Recht erfolgt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_21`)


Informativ werde mitgeteilt, dass der Abzug von monatlich € 30,00 von der Pension nicht für  das Finanzamt erfolge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_31`)


Sofern nicht die  Bestimmung des § 67 zur Anwendung kommt, geschieht die Pfändung dadurch, dass das  Finanzamt dem Drittschuldner verbietet, an den Abgabenschuldner zu bezahlen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_38`)


Werden beschränkt pfändbare Geldforderungen auf ein Konto des Abgabenschuldners bei  einem Kreditinstitut oder der Österreichischen Postsparkasse überwiesen, so ist gemäß § 54  Abs. 1 AbgEO eine Pfändung des Guthabens auf Antrag des Abgabenschuldners vom  Finanzamt insoweit aufzuheben, als das Guthaben dem der Pfändung nicht unterworfenen  Teil der Einkünfte für die Zeit von der Pfändung bis zum nächsten Zahlungstermin entspricht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_40`)


Gemäß § 54 Abs. 3 AbgEO hat das Finanzamt die Pfändung des Guthabens über Antrag des  Abgabenschuldners für den Teil aufzuheben, dessen dieser bis zum nächsten Zahlungstermin  dringend bedarf, um seinen notwendigen Unterhalt zu bestreiten und seine laufenden  gesetzlichen Unterhaltspflichten zu erfüllen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_54`)


Das Finanzamt hat den aufgrund der Pfändung überwiesenen Betrag in Höhe von € 939,67  mittlerweile dem Bf. zurücküberwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_55`)


Das Bundesfinanzgericht geht wie das Finanzamt davon aus, dass die auf das Konto des Bf.  überwiesenen Beträge, dem Pfändungsschutz des § 292i EO unterliegen (vgl. OGH 28.06.2018,  9 Ob 22/18b).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Dr. Gabriele Krafft` (person)
- `Daniel Parys` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_17`)


Das Finanzamt ging im  bekämpften Bescheid davon aus, dass er die Strecke vom Wohnort zum Dienstort  (insgesamt 20,2 km) in zwei Etappen zurücklegte, indem er zunächst vom Wohnort zum  Bahnhof_IP (1. Teilstrecke mit 3,4 km) und von dort weiter zum Bahnhof Bahnhof_L (2.  Teilstrecke) gefahren sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_20`)


Im Erstbescheid vom 17.07.2008 hat des Finanzamt „das große Pendlerpauschale bis 20  km“ iHv € 283,50 berücksichtigt (für die Teilstrecke Wohnung bis Bahnhof_IP).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_30`)


Das Finanzamt hat ausgehend von diesen  Unterlagen eine „Auswertung Fahrplan – Dienstzeit“ erstellt und dem BFG vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_31`)


Das  Finanzamt kommt in dieser Auswertung zum Ergebnis, dass das Begehren des  47Beschwerdeführers  zu Recht besteht und ein Pendlerpauschale in Höhe von 1.032 € zu  berücksichtigen ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_46`)


Da auch das Finanzamt (mit Ausnahme der  Monate Februar und Juni) zu diesem Ergebnis kam (vgl. die dem Bundesfinanzgericht  vorgelegte „Auswertung Pendlerpauschale“, in der die Berücksichtigung von Fahrt- kosten im Wege des großen Pendlerpauschales angeregt wurde), erübrigt sich eine  detailliertere Gegenüberstellung der Dienstzeiten und der Ankunfts- und Abfahrtszeiten  der Züge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_47`)


4.2. Soweit das Finanzamt die Inanspruchnahme des Werkverkehrs in den Monaten Februar  und Juni für zumutbar gehalten und deshalb eine Kürzung des Pauschales vorgenommen  hat, ist festzuhalten:    Im Erkenntnis VwGH 27.07.2016, 2013/13/0088 hat der Verwaltungsgerichtshof klar- gestellt, dass die sich aus § 16 Abs. 1 Z 6 lit. b und c EStG 1988 ergebenden Pauschbe- träge auf Grund des Wortlautes des Gesetzes nicht schon dann nicht zustehen, wenn  der Arbeitnehmer im Werkverkehr befördert werden könnte und ihm dies auch zumut- bar wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_23`)


Tag (Fälligkeitstag) des  auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden Kalendermonates eine  Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen Finanzamt  einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  2 von 4 Seite 3 von 4

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_25`)


Nach § 21 Abs 3 UStG 1994 hat das Finanzamt die Steuer festzusetzen, wenn der Unternehmer  die Einreichung der Voranmeldung pflichtwidrig unterlässt oder wenn sich die Voranmeldung  als unvollständig oder die Selbstberechnung als nicht richtig erweist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)
- `Bundesamtes für Soziales  und Behindertenwesen` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_36`)


Das Finanzamt wies den Antrag vom 10.08.2018 auf Familienbeihilfe und erhöhte  Familienbeihilfe mit Bescheid vom 16.01.2019 ab, führte begründend den § 6 Abs. 2 lit. d  FLAG 1967 an und verwies auf das vorstehend angeführte Gutachten.

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

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

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

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Salzburg-Land`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 9/18/19 Klosterneuburg`
- `Finanzamt` — similar text (different position): `Finanzamt Wien 9/18/19 Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)
- `Dr. Heinz Neuner`(person)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_3`)


Entscheidungsgründe Mit Erkenntnis des Spruchsenates vom 5.12.2018, SpS *****, wurde das gegen den Beschuldigten N.N. geführte Finanzstrafverfahren, in dem ihm zur Last gelegt wurde, er habe im Amtsbereich des Finanzamtes Wien 4/5/10 vorsätzlich a) unter Verletzung einer abgabenrechtlichen Offenlegungs- und Wahrheitspﬂicht - nämlich durch Abgabe unrichtiger Einkommensteuererklärungen für die Jahre 2012 bis 2015 - bewirkt, dass bescheidmäßig festzusetzende Abgaben in folgender Höhe zu niedrig festgesetzt worden seien, und zwar ESt 2012 in der Höhe von € 76.952,83 ESt 2013 in der Höhe von € 21.355,87 insgesamt somit € 98.308,69 und hiedurch das Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 FinStrG begangen, sowie b) Lohnabgaben für die Zeiträume 2012 bis 2017 L, DB, DZ 1-12/2012 in der Höhe von € 17.472,98 Seite 2 von 21 L, DB, DZ 1-12/2013 in der Höhe von € 10.249,92 L, DB, DZ 1-12/2014 in der Höhe von € 447,44 L, DB, DZ 1-12/2015 in der Höhe von € 1.031,92 DB, DZ 1-12/2016 in der Höhe von € 332,81 L, DB, DZ 1-12/2017 in der Höhe von € 2.513,45 insgesamt somit € 32.048,51 nicht spätestens fünften Tag nach Fälligkeit entrichtet (abgeführt) und hiedurch die Finanzordnungswidrigkeit nach § 49 Abs. 1 lit a FinStrG begangen, gemäß § 136 FinStrG eingestellt. Zur Begründung wurde ausgeführt der Beschuldigte sei 1960 geboren, arbeite derzeit als Angestellter und verdiene monatlich € 1.500,00 netto.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_42`)


In der mündlichen Verhandlung vor dem Spruchsenat beim Finanzamt Wien 9/18/19 Klosterneuburg am 05. Dezember 2018 wurde das Verfahren gemäß § 136 FinStrG eingestellt. Zur Begründung der Einstellung siehe Anhang „20181220_Erkenntnis SPS 05122018“.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_107`)


Unter Verweis auf diese Ausführungen wird sohin gestellt der höfliche Antrag, der Beschwerde des FA 9/18/19 Klosterneuburg vom 07. Jänner 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9 / 18 / 19/ Klosterneuburg vom 5. Dezember 2018, SpS *****,  keine Folge zu geben."

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

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

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien  12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Chen Walcker`(person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `63-698/2600`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Regina Vogt`(person)
- `Hedwig Mackiewicz`(person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Landeck Reutte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Li Schukardt`(person)
- `Ursula Buchholz`(person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich`(address)
- `Finanzamtes  Landeck Reutte`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gmunden Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Sven Oberstelehn`(person)
- `Chantal Eligüzel`(person)
- `Glittstein 70, 9072 Rupertiberg, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hans Blasina`(person)
- `Guntram Antepoth`(person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `70-875/4351`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Neunkirchen Wr. Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Viktoria Blaser`(person)
- `Techn R Lilia Schöpcke`(person)
- `In der Klaus 8, 5651 Winkl, Österreich`(address)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

</details>

---

## `german_company_ag` 🏆

**F1:** 0.031 | **Precision:** 0.661 | **Recall:** 0.016  

**Format:** `regex`  
**Rule ID:** `9a8e6f9f`  
**Description:**
Matches AG companies, requiring a valid name start and excluding common articles.

**Content:**
```
\b(?<!\w)(?:(?:Fa\.|[A-Z][a-zA-Z0-9\-+&]*(?:\s+[A-Z][a-zA-Z0-9\-+&]*)*)\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.661 | 0.016 | 0.031 | 109 | 72 | 37 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 72 | 37 | 4527 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_23`)


Mit Übergabevertrag vom 12. Juli 2012 habe der Bf. die Wohnung wiederum seinem Sohn zu  einem Übergabepreis in Höhe der per 26. Juni 2012 offenen Kreditforderung der Bank AG mit  einem offenen Saldo von EUR 110.461,17 übergeben.

| Predicted | Gold |
|---|---|
| `Bank AG` | `Bank AG` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_89`)


Der Übernehmer erklärt ferner in Kenntnis  des zwischen der Bank AG und dem Übergeber bestehenden Kreditvertrages zu sein und  verpflichtet sich ausdrücklich, in sämtliche Rechte und Pflichten aus dem Kreditvertrag  einzutreten.“

| Predicted | Gold |
|---|---|
| `Bank AG` | `Bank AG` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `UniCredit Bank Austria AG` | `UniCredit Bank Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der  Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `UniCredit Bank Austria AG` | `UniCredit Bank Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der  Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_30`)


Dabei muss bei der Übergabe insbesondere die Tankstelle der OMV AG zur  Gänze entfernt und deren Betriebsanlage aufgelassen sein.

| Predicted | Gold |
|---|---|
| `OMV AG` | `OMV AG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_7`)


Entscheidungsgründe  In den Streitjahren bezog der Beschwerdeführer (Bf.) nichtselbständige Einkünfte aus einem  Dienstverhältnis mit der X Versicherung AG (Dienstort St. Pölten).

| Predicted | Gold |
|---|---|
| `X Versicherung AG` | `X Versicherung AG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_60`)


Sein Dienstort befand sich in den Streitjahren seit dem 1.2.2018 in Adr.-St.  Pölten (X* Versicherung AG).

| Predicted | Gold |
|---|---|
| `Versicherung AG` | `Versicherung AG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_28`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `UniCredit Bank Austria AG` | `UniCredit Bank Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der  Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_27`)


Im Jahr 2015 bezog der Beschwerdeführer ausschließlich Einkünfte aus nichtselbständiger  Arbeit von der Bachtra-Immobilien AG, Steinmauer 22, 8334 Bergl, Österreich  (Baumeister/Zimmerer/Spengler/Dachdecker/Containerdienst).

| Predicted | Gold |
|---|---|
| `Bachtra-Immobilien AG` | `Bachtra-Immobilien AG` |

**Missed by this rule (FN):**

- `Steinmauer 22, 8334 Bergl, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_36`)


2. Beweiswürdigung  Die Feststellungen zu den Einkünften des Beschwerdeführers bei der Bachtra-Immobilien AG  gründen  sich auf die Erklärung zur Arbeitnehmerveranlagung sowie auf die, einen Bestandteil des  angefochtenen Bescheides bildenden Lohnzettel.

| Predicted | Gold |
|---|---|
| `Bachtra-Immobilien AG` | `Bachtra-Immobilien AG` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_37`)


Die Feststellungen zur Schlafstelle in  Schwechat gründen sich auf die diesbezügliche Bestätigung der Bachtra-Immobilien AG  vom 28.11.2017.

| Predicted | Gold |
|---|---|
| `Bachtra-Immobilien AG` | `Bachtra-Immobilien AG` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_32`)


Der Beschwerdeführer war 38 Jahr lang bei der ZIW IT AG, Deutschland beschäftig.

| Predicted | Gold |
|---|---|
| `ZIW IT AG` | `ZIW IT AG` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_60`)


Im finanzgerichtlichen Verfahren wurden umfangreiche ergänzende  Sachverhaltsermittlungen durchgeführt, die neben der Feststellung der Lebensumstände der Bf  in Deutschland, insbesondere die Beischaffung ihrer Besteuerungsunterlagen aus Deutschland  und der Rechtsgrundlagen zur Betriebsrente der Tal Waldvalver Gruppe GmbH bzw. der Rente von der  XY Deutschland Pensionsfonds AG betrafen.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Missed by this rule (FN):**

- `Tal Waldvalver Gruppe GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_69`)


Die Rentenleistungen zu dem von vorne herein mit Rechtsanspruch gegen den Dienstgeber  ausgestatteten Teil der Betriebsrente erbrachte im gesamten Verfahrenszeitraum die Tal Waldvalver Gruppe GmbH   Die Auszahlung des freiwillig geleisteten Rententeiles erfolgte bis 2010 im Wege einer  XY Deutschland Unterstützungskasse GmbH (nachfolgend Claaß E‑Commerce GmbH. Nach einer  Übertragung der ohne Rechtsanspruch gewährten Rentenverpflichtungen auf die  XY Deutschland Pensionsfonds AG (nachfolgend auch XY Pensionsfonds), verfügt die Bf seit  2011 auch für diesen Teil ihrer Betriebsrente über einen Rechtsanspruch, der nun gegenüber  dem XY Pensionsfonds besteht.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Missed by this rule (FN):**

- `Tal Waldvalver Gruppe GmbH` (organisation)
- `Claaß E‑Commerce GmbH` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_143`)


Dies  betrifft, neben Angaben/Unterlagen zu ihrem Wohnsitz bzw. ihren Lebensverhältnissen in  Nürnberg, insbesondere Teile der Rechtsgrundlage für die Betriebsrente der Tal Waldvalver Gruppe GmbH (Regelungen zur Ansparphase sowie zur Auszahlung durch die Claaß E‑Commerce GmbH  und die  Rechtsgrundlagen zu ihrem Rentenanspruch gegen den XY Pensionsfonds (Vereinbarungen der Tal Waldvalver Gruppe GmbH mit dem Konzernbetriebsrat bzw. der XY Deutschland  Pensionsfonds AG).

| Predicted | Gold |
|---|---|
| `XY Deutschland  Pensionsfonds AG` | `XY Deutschland  Pensionsfonds AG` |

**Missed by this rule (FN):**

- `Tal Waldvalver Gruppe GmbH` (organisation)
- `Claaß E‑Commerce GmbH` (organisation)
- `Tal Waldvalver Gruppe GmbH` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_158`)


Im Dez 2010 wurde die XY Deutschland Pensionsfonds AG zur „Auslagerung der  Versorgungszusagen“ gegründet.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_289`)


6. Das FA bezog in den angefochtenen Bescheiden – ohne Sachverhaltsermittlung - die Rente  der XY Deutschland Pensionsfonds AG in Hinblick auf § 25 (1) Z 2 lit b Satz 2 EStG 1988 nur im  Ausmaß von 25% der Bruttobezüge in die Besteuerung ein.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_290`)


Die Anwendung dieser Bestimmung setzt einerseits voraus, dass die XY Deutschland  Pensionsfonds AG als Einrichtung im Sinne des § 5 Z 4 PKG zu qualifizieren ist und anderseits,  dass den Rentenbezügen in der Ansparphase Arbeitnehmerbeiträge gegenüberstanden,  welche die in- oder ausländischen Einkünfte der Bf bzw. deren Einkommen im Ausland nicht  vermindert haben (vgl. VwGH 26.11.2015, 2013/15/0123 mit Verweis auf die Erläuterungen zur  RV zu BGBl. I Nr 34/2005).

| Predicted | Gold |
|---|---|
| `XY Deutschland  Pensionsfonds AG` | `XY Deutschland  Pensionsfonds AG` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_340`)


Die zu den führenden Pensionsfonds in Deutschland zählende XY Deutschland  Pensionsfonds AG ordnet das BFG auf Basis der von der Bf übermittelten Unterlagen, des  unionsrechtlichen Hintergrunds zur betrieblichen Altersvorsorge und der dargestellten  deutschen Rechtslage den Einrichtungen im Sinne des § 5 Z 4 PKG zu.  Mit der Übertragung des bis dahin ohne Rechtsanspruch ausbezahlten Teiles der Betriebsrente  auf die XY Deutschland Pensionsfonds AG erlangte die Bf einen gesetzlich geregelten  Rentenanspruch, der grundsätzlich zu einem Vorteil aus dem Dienstverhältnis führte.

| Predicted | Gold |
|---|---|
| `XY Deutschland  Pensionsfonds AG` | `XY Deutschland  Pensionsfonds AG` |
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_346`)


Die von der  XY Deutschland Pensionsfonds AG bezogene Rente ist daher in den angefochtenen Bescheiden  mit den Bruttobeträgen zur Gänze in die Besteuerung einzubeziehen, wobei die Bestimmung  des § 67 (1) EStG mangels Zuflusses von Sonderzahlungen nicht zum Tragen kommt.

| Predicted | Gold |
|---|---|
| `XY Deutschland Pensionsfonds AG` | `XY Deutschland Pensionsfonds AG` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_67`)


 Bestätigung Kurszeiten, AMS:     Mit E-Mail vom 12. März 2023 teilte der Bf. mit, dass es nun mit einer Anstellung bei der Fa.  Wright Robotik AG  als Handelsarbeiter geklappt habe und er von der WKO den Prüfungstermin  30.03.2023 erhalten habe.

| Predicted | Gold |
|---|---|
| `Wright Robotik AG` | `Wright Robotik AG` |

**Missed by this rule (FN):**

- `AMS` (organisation)
- `WKO` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_88`)


Seit dem 06. März ist der Bf. bei der Fa. Wright Robotik AG  als Handelsarbeiter beschäftigt (Vollzeit).

| Predicted | Gold |
|---|---|
| `Wright Robotik AG` | `Wright Robotik AG` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_49`)


Mit Schreiben vom 4.1.2023 forderte das Bundesfinanzgericht die belangte Behörde auf,  Nachfolgendes sachverhaltsmäßig zu ergänzend:  „In diesem Zusammenhang wäre daher festzustellen, in wie weit die Vorlieferungen hinsichtlich  der hier strittigen DDP-Lieferungen der Bf. der Lieferantin der Bf. (=Wien Consud AG  A) tatsächlich  versteuert worden bzw. geblieben sind d.h. ob die Leistungserbringerin (J. AG, A) auch nach  dem BP-Verfahren bei der Bf. keine wie immer geartete abgabenwirksamen Umsatz- oder  Rechnungsberichtigungen, der nach Ansicht des Finanzamtes materiell-rechtlichen „bewegten  und grundsätzlich steuerbefreiten innergemeinschaftlichen Lieferungen“ durchgeführt hat bzw.  nachträglich die Steuerbefreiung geltend gemacht hat.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Missed by this rule (FN):**

- `J. AG` (organisation)
- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_50`)


Unter der Prämisse, dass der Umsatz  der Wien Consud AG (A) im Zusammenhang mit den hier strittigen DDP-Lieferungen der Bf. an EU- Unternehmer im Inland letztendlich versteuert geblieben ist, wäre im fortgesetzten Verfahren  aus den Gründen der Verhältnismäßigkeit von einer Erwerbsbesteuerung nach Art. 3 Abs. 8  zweiter Satz UStG 1994 Abstand zu nehmen.“

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_51`)


In ihrer Anwortnote vom 14.2.2023 führt die belangte Behörde u.a. aus:  „Nachschauergebnis:  Im Rahmen der Nachschau wurden die mittlerweile rechtskräftig gewordenen  Umsatzsteuerbescheide der Jahre 2015 und 2016 von Wien Consud AG abgefragt.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_55`)


Überdies wurden von der steuerlichen Vertretung der Wien Consud AG (BDO Austria GmbH Wpr u. Stber.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_59`)


Diese konnten mit den von Wien Consud AG erklärten Beträgen  abgestimmt werden und ergaben deren korrekte Erfassung in der KZ029.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_60`)


Überdies wurde  stichprobenartig die Erfassung von Einzelbelegen bei Wien Consud AG  aus welchen T. (= Bf., B) die  Vorsteuer geltend machte und die AP hierzu Zusatzerwerbe feststellte, geprüft und für richtig  befunden.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_61`)


Aus diesem Grund konnte die tatsächliche Versteuerung bzw. deren Verbleib in den  Jahren 2015 und 2016 durch Wien Consud AG nachgewiesen werden.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_62`)


…“  Zur weiteren strittigen Rechtsfrage, ob die von der Wien Consud AG (A) mit inländischem  Umsatzsteuerausweis die Bf. zum Vorsteuerabzug berechtigen, wie es das Bundesfinanzgericht  im Gegensatz zur belangten Behörde verneint hat, hat sich der VwGH nicht weiter geäußert.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_63`)


Im Zusammenhang zum gegenständlichen fortgesetzten Verfahren führte die steuerliche  Vertreterin u.a. Folgendes aus:  „…  Bezugnehmend auf Ihre Email vom 4.1.2023 können wir Sie nach Rücksprache mit unserer  Mandantschaft wie folgt informieren:  Nach Maßgabe des Urteils des VwGH vom 19.10.2022, Ro 2021/15/0034 wurde das Erkenntnis  des BFG zur Gänze wegen Rechtswidrigkeit des Inhalts aufgehoben, sodass nun die  ursprüngliche Rechtslage nach der vom Finanzamt ausgestellten Bescheide für die Jahre 2015  und 2016 wieder gilt. Die Rechtslage aufgrund dieser Bescheide des Finanzamts, in welchen die  Feststellungen der Betriebsprüfung eingearbeitet wurden, ist dergestalt, dass der  Vorsteuerabzug aus den Rechnungen von Wien Consud AG gewährt und auch nicht von der Behörde  beanstandet wurde und fiktive innergemeinschaftliche Erwerbe (ohne Vorsteuerabzug)  aufgrund der Verwendung der österreichischen UID-Nummer festgesetzt wurden.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_64`)


Die gegen  diese Rechtauffassung eingebrachte Beschwerde richtete sich gegen die Festsetzung der  fiktiven innergemeinschaftlichen Erwerbe, da diese – wie nun auch vom VwGH unter  Bezugnahme auf die Rechtsprechung des EuGH bestätigt – rechtswidrig war, weil die  Lieferungen von Wien Consud AG nicht steuerbefreit waren.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_66`)


Wenn nunmehr das BFG – obwohl weder von der  belangten Behörde noch von der Beschwerdeführerin beanstandet – die Rechtsmeinung  vertritt, dass der Vorsteuerabzug aus den Eingangsrechnungen von Wien Consud AG zu verneinen sei und  insoweit eine Verböserung vornimmt, ist seitens der Beschwerdeführerin beabsichtigt, den  Instanzenzug zu beschreiten, und zwar aus folgenden Gründen:  Anders als in ihrer Email angeführt ist der Entscheidung des VwGH an keiner Stelle zu  5 von 18 Seite 6 von 18

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_67`)


entnehmen, dass die Rechtsansicht, wonach der Vorsteuerabzug aus den Eingangsrechnungen  von Wien Consud AG zu versagen sei, geteilt wird.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_68`)


Auch hat der VwGH oder der EuGH bisher zu einem wie  dem hier vorliegenden Sachverhalt, bei dem einerseits eine innergemeinschaftliche Lieferung  aufgrund der Mitteilung einer inländischen UID-Nummer als steuerpflichtig behandelt wurde  (bzw. werden musste) und andererseits ein fiktiver ig Erwerb vorgeschrieben wurde, nicht  explizit zur Frage des Vorsteuerabzuges für die als steuerpflichtig behandelte Lieferung  geurteilt, sodass genau zu dieser Frage einschlägige Rechtsprechung durch den VwGH und  EuGH fehlt. Denn auch wenn es sich bei den Lieferungen von Wien Consud AG (A) um  innergemeinschaftliche Lieferungen handelt, die bei Vorliegen aller Voraussetzungen  grundsätzlich hätten steuerbefreit sein können, bedeutet dies nicht, dass diese im konkreten  auch steuerbefreit waren und somit zu Unrecht österreichische Umsatzsteuer von Wien Consud AG in  Rechnung gestellt wurde, für die kein Recht auf Vorsteuerabzug besteht.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |
| `Wien Consud AG` | `Wien Consud AG` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_70`)


Mangels Bekanntgabe  einer ausländischen UID-Nummer war es jedoch Wien Consud AG nicht möglich die erforderlichen  Nachweise für die Voraussetzungen einer steuerbefreiten innergemeinschaftlichen Lieferung zu  führen.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_76`)


Wie oben bereits ausgeführt, wurde gegen die Festsetzung der sog. fiktiven ig Erwerbe  Beschwerde eingebracht und wurde die der Beschwerde zugrundeliegende Ansicht, dass eine  Festsetzung im vorliegenden Sachverhalt (bei der die Lieferungen von Wien Consud AG nicht steuerbefreit  wurden) nicht rechtmäßig ist, vom VwGH bestätigt.

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_187`)


Der von der Bf. aus den Rechnungen der Wien Consud AG (A) vorgenommene Vorsteuerabzug war  abzuerkennen, weil er nicht aus steuerbaren und steuerpflichtigen (ruhenden)  Inlandslieferungen an die Bf., sondern aus steuerbaren, aber steuerbefreiten  innergemeinschaftlichen Lieferungen resultierte (VwGH 5.3.2020, Ro 2018/15/0004).

| Predicted | Gold |
|---|---|
| `Wien Consud AG` | `Wien Consud AG` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/141421.1`) (sent_id: `deanon_BFG_20260814_TEST/141421.1_10`)


Am 02.06.2022, beim FA eingelangt am 07.06.2022, beantwortete der Bf dieses  Überprüfungsschreiben des FA und legte Unterlagen vor: 1 Mietvertrag, Salzburg AG  Stromkosten, Hutchison, Telefonaufwand, Dienstvertrag, Schulbesuchsbestätigungen 2018/19,  2021/22 und von 09/2019 bis 07/2022.

| Predicted | Gold |
|---|---|
| `Salzburg AG` | `Salzburg AG` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_17`)


Diese  Pensionszusage wurde durch zwei Lebensversicherungen (Polizzen Nummer V1 und V2) bei der   Versicherung AG rückgedeckt.

| Predicted | Gold |
|---|---|
| `Versicherung AG` | `Versicherung AG` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_3`)


Grießhaber Finanzen  GmbH & Co KG, Göritzer Straße 96, 5662 Großsonnberg, Österreich  beide vertreten durch yy Wirtschaftstreuhand Gesellschaft mbH, Straße 2, Ort,   gegen den Bescheid des Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, § 323 b BAO)  vom 29. November 2012 betreffend Feststellung der Einkünfte gemäß § 188 BAO für das Jahr  2008 (der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft) zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Grießhaber Finanzen` (organisation)
- `Göritzer Straße 96, 5662 Großsonnberg, Österreich` (address)
- `yy Wirtschaftstreuhand Gesellschaft mbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_14`)


[...]   Verfahrensgang  Nach Einreichung der Erklärungen samt Beilagen wurden den Bf. im Feststellungsbescheid der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft (in der Folge Zielgesellschaft) des Jahres 2008 folgende  Einkünfte zugerechnet:  1. Richsteiger Marine: ein Betrag von -€ 1.679.493,29 (Verlustzuweisung -€ 1.520.000,00 zzgl.  Sonderbetriebsausgaben in Höhe von -€ 159.493,29) und  2. Grießhaber Finanzen  GmbH & Co KG: ein Betrag von -€ 938.729,84 (Verlustzuweisung € - 838.138,16 zzgl. Sonderbetriebsausgaben in Höhe von -€ 100.591,68).

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_15`)


Im Zeitraum von Dezember 2009 bis November 2011 fand betreffend einheitlicher und  gesonderter Gewinnfeststellung der Jahre 2008 und 2009 eine Außenprüfung (Bescheid über  einen Prüfungsauftrag vom 28. Juni 2011 und Prüfbeginn 12. Juli 2011) bei der Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft statt.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_19`)


Am 7. Oktober 2011 erfolgte eine Einvernahme des Vorstandes der Zielgesellschaft (I AG) -  unter anderem zur unterschiedlichen Regelung des § 2 des Zusammenschlussvertrages.

| Predicted | Gold |
|---|---|
| `I AG` | `I AG` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_41`)


Aus den niederschriftlichen Aussagen des Vorstandes der Gablonsky&Rethlefsen Gastronomie AG ist klar erkennbar, dass es  zentrale Strategie sämtlicher Beteiligungsmodelle AbisJ ist, sich an solchen  Zielkapitalgesellschaften zu beteiligen, die im Jahr der Beteiligung Verlustzuweisungen in Höhe  von nahezu 200 % der atypisch stillen Einlage an AbisJ garantieren können, ja, dass das  Eingehen einer Beteiligung durch AbisJ an einer Zielgesellschaft von einer vorrangigen  Verlustzuweisung in der von den Modellinitiatoren geforderten Höhe abhängig gemacht wird.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_52`)


Die an AbisJ zugewiesenen Verluste aus der atypisch stillen Beteiligung an Gablonsky&Rethlefsen Gastronomie AG sind daher gem.  § 2 Abs. 2a EStG 1988 nicht ausgleichs- und vortragsfähig.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_56`)


Nunmehr wurden im Feststellungsbescheid der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft Einkünfte wie folgt zugerechnet:   1. Richsteiger Marine: € -1.520.000,00 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 1.520.000,00 zu berücksichtigen  sind) und  2. Grießhaber Finanzen  GmbH & Co KG: € -838.138,16 (wobei bei der Veranlagung der Bf. diese als nicht  ausgleichsfähige Verluste (eigener Betrieb) im Betrag von € 838.138,16 zu berücksichtigen  sind).

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_66`)


Würden die gewünschten  Forschungsergebnisse gar nicht oder nicht im erforderlichen Zeitraum realisiert, bestehe die  Gefahr, dass die Gablonsky&Rethlefsen Gastronomie AG die atypisch stille Einlage nie mehr zurückzahlen könne.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_69`)


Zentrales Element der Verhandlungen im Zuge des Abschlusses der atypisch stillen Beteiligung  sei die Wertbestimmung der Gablonsky&Rethlefsen Gastronomie AG und damit das Beteiligungsverhältnis der Investoren  gewesen.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_71`)


Im  Vordergrund stehendes Motiv der Beteiligung an der Gablonsky&Rethlefsen Gastronomie AG sei die Möglichkeit gewesen, den  Kapitaleinsatz tatsächlich zu vervielfachen.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_84`)


Am 29. Dezember 2008 schloss die Bf. mit der Gablonsky&Rethlefsen Gastronomie AG einen Zusammenschlussvertrag  über die Errichtung einer atypisch stillen Gesellschaft ab.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_87`)


Am 23. Juni 2009 schloss die Bf. mit der Gablonsky&Rethlefsen Gastronomie AG einen Zusammenschlussvertrag  über die Errichtung einer atypisch stillen Gesellschaft ab.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_101`)


Im Beschwerdejahr 2008 waren an der operativ tätigen Gablonsky&Rethlefsen Gastronomie AG die Bf. als atypisch stille  Gesellschafter beteiligt:  Zusammenschlussvertrag – „Errichtung stille Gesellschaft“ - Richsteiger Marine  Die mit Zusammenschlussvertrag vom 28. Dezember 2008 rückwirkend errichtete Gablonsky&Rethlefsen Gastronomie AG&  atypisch stille Gesellschaft ist auf unbestimmte Zeit errichtet und frühestens kündbar mit 31.  Dezember 2015 unter Einhaltung einer sechsmonatigen Frist.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_102`)


Laut § 1 des Vertrages stellt die Bf. als atypisch stille Gesellschafterin und Beteiligungsgeberin  eine Einlage, welche dem wirtschaftlichen Eigenkapital des Beteiligungsnehmers (I AG)  zugerechnet wird, von zumindest € 800.000,00 bis zu € 1.725.000,00 zur Verfügung.

| Predicted | Gold |
|---|---|
| `I AG` | `I AG` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_115`)


Anzumerken ist, dass bezogen auf die tatsächlich geleistete Einlage von gesamt € 800.000,00  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG in Höhe von €  65.845.751,50 zum Stichtag des Zusammenschlusses – die Beteiligungsquote 1,2003 % beträgt.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_119`)


Zusammenschlussvertrag – „Errichtung stille Gesellschaft“ - Grießhaber Finanzen  GmbH & Co KG:  Die mit Zusammenschlussvertrag vom 23. Juni 2009 rückwirkend errichtete Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft ist auf unbestimmte Zeit errichtet und frühestens kündbar mit 1. Juli 2015  unter Einhaltung einer sechsmonatigen Frist.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Grießhaber Finanzen` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_120`)


Laut § 1 des Vertrages stellt die Bf. als atypisch stille Gesellschafterin und Beteiligungsgeberin  eine Einlage, welche dem wirtschaftlichen Eigenkapital der Gablonsky&Rethlefsen Gastronomie AG zugerechnet wird, von  zumindest € 400.000,00 bis zu € 925.000,00 zur Verfügung.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_127`)


Sie ergibt sich  ausgehend vom einvernehmlich zugrunde gelegten Verkehrswert der Gablonsky&Rethlefsen Gastronomie AG in Höhe von €  67.593.518,50 zum Stichtag des Zusammenschlusses, bezogen auf eine Einlage von €  10 von 28 Seite 11 von 28

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_137`)


Gesellschaften mit gleicher Beteiligungs- sowie Gesellschafterstruktur, welche im  Prüfzeitraum an der operativ tätigen Gablonsky&Rethlefsen Gastronomie AG als atypisch stille Gesellschafter beteiligt waren:   2009:    die Richsteiger Marine   die Grießhaber Finanzen  GmbH & Co KG   die EF GmbH & Co KG   die GH GmbH & Co KG  Gesellschafter der Bf. (sowie der anderen AbisJ Gesellschaften) sind laut Firmenbuchauszug die Widdra & Koslowa Pharma GmbH als Komplementärin und die Pietzschke Chemie GmbH als Kommanditistin.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)
- `Widdra & Koslowa Pharma GmbH` (organisation)
- `Pietzschke Chemie GmbH` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_143`)


In der Erklärung zur einheitlichen und gesonderten Gewinnfeststellungen der Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft für das Jahr 2008 wurden bei den einzelnen atypisch stillen  Gesellschafterinnen folgende Sonderbetriebsausgaben in Abzug gebracht:  Richsteiger Marine: -€ 159.493,29   Grießhaber Finanzen  GmbH & Co KG: -€ 100.591,68  Hierbei handelte es sich um anteilige Kosten aus der „Modellentwicklung“, welche bei der  atypisch stillen Gesellschafterin angefallen sind.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_175`)


Ein Zusammenhang mit etwaigen Leistungsbeziehungen zwischen der  Bf. und der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft ist nicht erkennbar.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_200`)


In den Erklärungen zur einheitlichen und gesonderten Gewinnfeststellung der Gablonsky&Rethlefsen Gastronomie AG& atypisch  stille Gesellschaft 2008 wurden den atypisch stillen Gesellschafterinnen folgende Verluste  zugewiesen:    Richsteiger Marine   €  Grießhaber Finanzen  GmbH & Co KG   €  1.520.000,00 838.138,16  17 von 28 Seite 18 von 28

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_212`)


Die Bf. waren an der Gablonsky&Rethlefsen Gastronomie AG als atypisch stille Gesellschafterinnen beteiligt und es wurden ihnen  im Feststellungsbescheid Einkünfte/Verluste zugerechnet bzw. nicht zugerechnet.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_238`)


Ist an einer Mitunternehmerschaft (I AG & atypische stille Gesellschaft) eine weitere  Mitunternehmerschaft (Richsteiger Marine  und Grießhaber Finanzen  GmbH & Co KG) beteiligt, sind deren  Gesellschafter (natürliche und juristische Personen) Mitunternehmer der ersten  Mitunternehmerschaft (doppelstöckige Mitunternehmerschaft).

| Predicted | Gold |
|---|---|
| `I AG` | `I AG` |

**Missed by this rule (FN):**

- `Richsteiger Marine` (organisation)
- `Grießhaber Finanzen` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_241`)


Auch die Kapitalgesellschaft -Gablonsky&Rethlefsen Gastronomie AG war Mitunternehmerin der stillen Mitunternehmerschaft.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_247`)


Sonderbetriebsausgaben  In einem zweiten Schritt wird sodann der Gewinn oder der Verlust der einzelnen  Mitunternehmer ermittelt:   Strittig ist, ob ein anteiliger Abzug der Sonderbetriebsaufwendungen –  „Modellentwicklungskosten“ als Sonderbetriebsausgaben im Rahmen der einheitlichen und  gesonderten Gewinnfeststellung der Gablonsky&Rethlefsen Gastronomie AG und atypisch stillen Gesellschaft, möglich ist.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_252`)


Ein direkter Zusammenhang  aus etwaigen Leistungsbeziehungen zwischen den Bf. und der Gablonsky&Rethlefsen Gastronomie AG& atypisch stille Gesellschaft  ist hierbei nicht erkennbar.

| Predicted | Gold |
|---|---|
| `Gablonsky&Rethlefsen Gastronomie AG` | `Gablonsky&Rethlefsen Gastronomie AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_32`)


Sie sind bereits seit November 2012 bei der Firma AG in A-P beschäftigt.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_15`)


Darin habe das BFG die operative Tätigkeit der L  Schweiz AG als erwiesen angesehen und auf Unterlagen seitens der Schweizer Steuerbehörde  verwiesen.

**False Positives:**

- `L  Schweiz AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_16`)


Ergänzend sei darauf hingewiesen, dass der Beschwerdeführer niemals Umsatzsteuer  ausgewiesen habe bzw. die Gutschriftsabrechnungen der L Schweiz AG immer ohne  (österreichische) Umsatzsteuer erstellt habe.

**False Positives:**

- `L Schweiz AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_94`)


b) Beiträge zu den zusätzlichen Pensionsversicherungen, die vom Pensionsinstitut der Linzer  Elektrizitäts-, Fernwärme- und Verkehrsbetriebe AG, vom Pensionsinstitut für Verkehr und  öffentliche Einrichtungen und nach der Bundesforste-Dienstordnung durchgeführt werden.

**False Positives:**

- `Verkehrsbetriebe AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)


Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG vor.

**False Positives:**

- `T AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)
- `L GmbH &  Co`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_46`)


Laut dem ebenfalls übermittelten  Treuhandvertrag wurde diese Beteiligung treuhändig erworben (Treugeber: T AG).

**False Positives:**

- `T AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_24`)


Betrachtet man die zugrundeliegenden Lohnzettel der LZ2 und der LZ1 AG stellt sich die  entscheidungsrelevante Frage, ob hier steuerfreie Einkünfte gemäß § 3 Abs. 1 Z 4 lit a EStG  1988 vorliegen.

**False Positives:**

- `LZ1 AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Bei dem in den Beschwerdejahren bei der Firma AG als Kellner beschäftigten  Beschwerdeführer (Bf) nahm das Finanzamt unter Zugrundelegung der übermittelten  Lohnzettel die Arbeitnehmerveranlagungen 2010 bis 2014 vor.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_30`)


Weiters wurde die Berücksichtigung des beantragten  Pendlerpauschales und des Unterhaltsabsetzbetrages außer Streit gestellt.    II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den Beschwerdejahren bis zum 14. August 2014 bei der Firma AG als Kellner  beschäftigt.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_23`)


Der Arbeitgeber  übermittelte folgenden Jahreslohnzettel 2017 an das deutsche Betriebsstättenfinanzamt:  Steuerfreier Arbeitslohn nach DBA 76.028,31  AG-Anteil zur gesetzlichen Rentenversicherung 6.960,91  AN-Anteil zur gesetzlichen Rentenversicherung 6.960,91  steuerfreie AG-Zuschüsse zur gesetzlichen Krankenversicherung 3.810,60  Steuerfreie AG-Zuschüsse zur gesetzlichen Pflegeversicherung 665,52  AN-Beiträge zur gesetzlichen Krankenversicherung 8.091,00  AN-Beiträge zur sozialen Pflegeversicherung 1.331,16  AN-Beiträge zur Arbeitslosenversicherung 1.116,73  Grundsätzlich sind in Deutschland auch die sonstigen Bezüge in die Bemessungsgrundlage für  die gesetzliche Kranken- Pflege-, Renten und Arbeitslosenversicherung miteinzubeziehen.

**False Positives:**

- `Steuerfreie AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer war im Streitzeitraum unter anderem an der S AG(im Folgenden S-AG)  als atypisch stiller Gesellschafter beteiligt.

**False Positives:**

- `S AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_33`)


Der Beschwerdeführer war im Streitzeitraum unter anderem an der S AG (im Folgenden S-AG)  als atypisch stiller Gesellschafter beteiligt.

**False Positives:**

- `S AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_10`)


1. 80 % dieser WK PK AG-Abfertigung in Höhe von € 3.662,50 sowie   2.

**False Positives:**

- `WK PK AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_7`)


II. Sachverhalt  Der am xxxxxxx in x geborene und seit dem Jahr 1999 in Ort wohnhafte Bf., übergab die an das  „Finanzamt Österreich, Postfach 260, 1000 Wien“ gerichtete Erklärung zur  Arbeitnehmerveranlagung 2021 am 28.02.2022 der Österreichischen Post AG (Postfiliale y),  1 von 4 Seite 2 von 4

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `Österreichischen Post AG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_12`)


Dass die Arbeitnehmerveranlagung 2021 am Tag ihrer Unterfertigung beim Postamt in  Feldkirchen aufgegeben wurde, geht aus der vom Bf. übermittelten Rechnungskopie  (Rechnungsnummer 50550020200918) der Österreichischen Post AG vom 28.02.2022 hervor;

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen Post AG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_14`)


Wenn die belangte Behörde in diesem Zusammenhang ausführt, dass die  verfahrensgegenständliche Erklärung nicht bei ihr eingelangt sei, so ist ihr der auf der  Homepage der Österreichischen Post AG unter der konkreten Sendungsnummer enthaltene  Inhalt entgegenzuhalten, aus dem sich klar ergibt, dass die Zustellung am 02.03.2022 und  15:00 Uhr erfolgt ist.

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichischen Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen Post AG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_10`)


Die gegenständlichen Verfahrenskosten stünden im  Zusammenhang mit der Tätigkeit der Bf. als einer der beiden Vorstände der Firma AG und  seien somit betrieblich veranlasst.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_11`)


Im Jahr 2018 wurde gegen die Bf. und den zweiten Vorstand  der der Firma AG Anklage wegen betrügerischer Krida nach § 156 Abs. 1 und Abs. 2 StGB idF  BGBl I 2015/112 erhoben.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_17`)


Die AG sei im  November 2011 infolge eines Konkursverfahrens aufgelöst worden.

**False Positives:**

- `Die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_66`)


Seit August 1994 fließen ihr  Pensionsbezüge der an derselben Adresse situierten XY Pensionskasse AG, FN 999999x zu. Seit  Mai 1995 erhält die Bf zudem eine Sozialversicherungspension der PVA (nachfolgend  SV-Pension), die gemäß der Verordnung über die gemeinsame Versteuerung mehrere  Pensionen, BGBl II 2001/55, gemeinsam mit der Pension aus der XY Pensionskasse AG  ausbezahlt und versteuert wird.

**False Positives:**

- `XY Pensionskasse AG` — no gold match — likely missing annotation
- `XY Pensionskasse AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_74`)


In Österreich erfolgten für die Bf ab 1994 Pflichtveranlagungen nach § 41 Abs. 1 Z 2 EStG unter  Einbeziehungen der Bezüge der XY Pensionskasse AG in Wien und Abzug von Sonderausgaben  für Personenversicherungen in Höhe des so genannten „Topf-Sonderausgaben“- Höchstbetrages.

**False Positives:**

- `XY Pensionskasse AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_160`)


In Bezug auf bereits laufende Rentenauszahlungen wurden die bisher „mittelbar über die  XY Unterstützungskasse durchgeführten Versorgungszusagen“ samt dem Vermögen zur Gänze  und mit Zweckbindung für die Rentenzahlungen auf die Pensionsfonds AG übertragen.

**False Positives:**

- `Pensionsfonds AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_172`)


Die XY Deutschland Pensionsfonds AG betreibt lt. dHRB das Geschäft eines Pensionsfonds im  Sinne der Bestimmungen des Versicherungsaufsichtsgesetzes (§§ 112 ff. dVAG) und gehört  aktuell zu den fünf größten Pensionsfonds in Deutschland (vgl. wikipädia.org/ Bundesverband  der Rechtsberater für betriebliche Altersversorgung und Zeitwertkonten e.V.).

**False Positives:**

- `Die XY Deutschland Pensionsfonds AG` — partial — gold is substring of pred: `XY Deutschland Pensionsfonds AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XY Deutschland Pensionsfonds AG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_68`)


Aus dem beigefügten Arbeiterdienstvertrag mit seinem neuen  Arbeitgeber Wright Robotik AG  geht hervor, dass als Dienstantritt der 6. März 2023 vereinbart wurde.

**False Positives:**

- `Arbeitgeber Wright Robotik AG` — partial — gold is substring of pred: `Wright Robotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wright Robotik AG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_80`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Eine österreichische Gesellschaft Wien Consud AG (A) verkaufte an die Bf.(B), die als belgisches  Unternehmen sowohl über eine belgische als auch über eine österreichische Umsatzsteuer- Identifikationsnummer verfügte, Waren, die diese als mittleres Unternehmen (B) an EU- Gesellschaften (C) weiterveräußerte.

**False Positives:**

- `Gesellschaft Wien Consud AG` — partial — gold is substring of pred: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_99`)


Auf Grund der im fortgesetzten Verfahren durchgeführten abgabenbehördlichen Ermittlungen  war festzustellen, dass die von der ersten Unternehmerin Wien Consud AG (A) in Rechnung gestellte  (inländische) Umsatzsteuer auch abgeführt und nicht wieder berichtigt wurde.

**False Positives:**

- `Unternehmerin Wien Consud AG` — partial — gold is substring of pred: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_12`)


Der obligatorische Anteil in Höhe von 67.805,80 CHF wurde zunächst von der Pensionskasse  über Auftrag des Bf. auf ein Konto der Freizügigkeitsstiftung der UBS AG überwiesen.

**False Positives:**

- `UBS AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Regina Mockry  in der Beschwerdesache Gablonsky&Rethlefsen Gastronomie AG&  atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafter  1.

**False Positives:**

- `Beschwerdesache Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Regina Mockry`(person)
- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `xx GmbH Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_65`)


Gegen eine Subsumierung des gegenständlichen Sachverhaltes unter § 2 Abs. 2a EStG 1988  spreche:  Die Gablonsky&Rethlefsen Gastronomie AG sei unstrittigerweise - wie das Finanzamt selbst festgestellt habe - im Bereich der  Forschung tätig und erziele seit Jahren Jahresverluste.

**False Positives:**

- `Die Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)
- `Finanzamt`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_95`)


Die Gablonsky&Rethlefsen Gastronomie AG ist eine kleine Aktiengesellschaft im Sinne des § 221 UGB und hat ihren Sitz in Ort4, BL.

**False Positives:**

- `Die Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_148`)


Berechnung des Verhältnisses der Beteiligung:  Finanzanlagen € 2.190.000,00  davon an der Gablonsky&Rethlefsen Gastronomie AG€ 800.000,00  Verhältnis in % 36,53 %

**False Positives:**

- `Gablonsky&Rethlefsen Gastronomie AG` — partial — pred is substring of gold: `Gablonsky&Rethlefsen Gastronomie AG€`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG€`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_154`)


Berechnung des Verhältnisses der Beteiligung:  Finanzanlagen € 1.850.000,00  davon an der Gablonsky&Rethlefsen Gastronomie AG€ 500.000,00  Verhältnis in % 27,03 %

**False Positives:**

- `Gablonsky&Rethlefsen Gastronomie AG` — partial — pred is substring of gold: `Gablonsky&Rethlefsen Gastronomie AG€`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG€`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_173`)


SBA anteilig (Beteiligung Gablonsky&Rethlefsen Gastronomie AG  36,53 %  € 159.493,29  27,03 %  € 100.591,68

**False Positives:**

- `Beteiligung Gablonsky&Rethlefsen Gastronomie AG` — partial — gold is substring of pred: `Gablonsky&Rethlefsen Gastronomie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gablonsky&Rethlefsen Gastronomie AG`(organisation)

</details>

---

## `german_company_gmbh` 🏆

**F1:** 0.083 | **Precision:** 0.346 | **Recall:** 0.047  

**Format:** `regex`  
**Rule ID:** `8f8e291f`  
**Description:**
Matches GmbH companies, requiring a valid name start (letter or 'Fa.') and excluding common articles like 'Die' or 'Der'.

**Content:**
```
\b(?<!\w)(?:(?:Fa\.|[A-Z][a-zA-Z0-9\-+&]*(?:\s+[A-Z][a-zA-Z0-9\-+&]*)*)\s+GmbH(?:\s+&\s+CO\s+KG)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.346 | 0.047 | 0.083 | 630 | 218 | 412 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 218 | 412 | 4381 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_11`)


Es handle sich dabei um die Firmen X. d.o.o. mit Sitz in L., die Furtder Technologien GmbH und die NEP Lebensmittel GmbH  Tatsächlich habe der Beschuldigte die jeweils Verantwortlichen auf den Baustellen kennengelernt, diese hätten nach Arbeit gefragt.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_23`)


Hinsichtlich der Furtder Technologien GmbH und der NEP Lebensmittel GmbH habe der Beschuldigte durch seinen Verteidiger in der Spruchsenatsverhandlung durch Vorlage der Urkunden nachweisen können, dass er Firmenbuchauszug und HFU-Listen-Abfragen gemacht habe, sowie sich die Gewerbeberechtigung vorlegen habe lassen, die er in Kopie behalten habe.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_43`)


Entgegen den Ausführungen im Erkenntnis vom 05. Dezember 2018 konnte der Beschuldigte zu den drei betreffenden Firmen (X. d.o.o. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH  nicht die gleichen Unterlagen vorlegen, wie er es bei anderen Geschäftspartnern konnte.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_62`)


------ Mit Vorhalt des Bundesfinanzgerichtes vom 9.4.2019 wurde der Beschuldigte  aufgefordert, die Mittelherkunft der behaupteter Weise von ihm in den Jahren 2012 und Seite 6 von 21 2013 geleisteten Barzahlungen an die Subfirmen X. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH anhand vorzulegender Kopien sämtlicher Kontenbewegungen oder anhand anderer geeigneter Unterlagen nachzuweisen bzw. glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_63`)


Dem Beschuldigten wurde wie folgt vorgehalten: Laut Bericht über die Außenprüfung vom 11.10.2017 unter Tz 2 wurden nicht anzuerkennende Fremdleistungen aufgrund von Scheinrechnungen der Fa. X. für das Jahr  2012 iHv € 74.884,49 und für 2013 iHv € 18.550,91 festgestellt. Weiters wurden nach den Feststellungen im Bericht über die Außenprüfung vom 11.10.2017 unter Tz. 4 Fremdleistungen aufgrund von auf den Namen der Kisteler Telekom GmbH lautenden Rechnungen im Jahr 2012 iHv € 220.314,31 sowie auf den Namen der Fa.NEP Lebensmittel GmbH lautenden Rechnungen im Jahr 2013 iHv € 115.236,61 als Betriebsausgaben geltend gemacht.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `Fa.NEP Lebensmittel GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_66`)


Betreffend die Kisteler Telekom GmbH legte der Beschuldigte einen abverlangten Firmenbuchauszug vom 6.4.2012, Gewerberechtsbescheid vom 1.9.2011, Daten des Steueraktes für 2012 vom 6.2.2012 und 5 Auszüge aus der HFU-Liste, eine MIAS-Abfrage vom 24.4.2012 sowie die an die Furtder Technologien GmbH gelegten Rechnungen samt Zahlungsbestätigungen und Ersatzschecks (Barabhebungen) im Betrag von € 126.000,00 vor.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_97`)


So ergibt sich aus den vorgelegten Unterlagen, dass ich mir jeweils die Gewerbeberechtigungen der Subunternehmen ausfolgen ließ, im April 2012 (A-GmbH) bzw. im Jänner 2013 (B-GmbH) Firmenbuchauszüge eingeholt habe, bezüglich der Furtder Technologien GmbH am 06. Februar 2012 die Daten des Steuerkontos abgefragt habe und bezüglich der Furtder Technologien GmbH am 15.10.2011, 01.11.2011,15.02.2012, 15.03.2012 und 03.07 2012 sowie bezüglich der NEP Lebensmittel GmbH am 14.01.2013 und am 31.05.2013 Auszüge aus der HFU-Liste erstellt habe.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_98`)


Bezüglich der Furtder Technologien GmbH habe ich zusätzlich am 24. April 2012 das MwSt - Informationsaustauschsystem abgefragt, bei der NEP Lebensmittel GmbH ließ ich mir: die Bestätigung des DLZ-AGH vom 07.03.2013 (Aufnahme in die Liste der haftungsfreistellenden Unternehmen) ausfolgen.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_99`)


Zu verweisen ist in diesem Zusammenhang auch noch darauf, dass die Furtder Technologien GmbH bereits im Jahr 2002 (und sohin bei Aufnahme der Geschäftstätigkeit 10 Jahre lang als werbendes Unternehmen existent!) und die NEP Lebensmittel GmbH im Frühjahr 2009 (und sohin bei Aufnahme der Geschäftstätigkeit auch bereits 4 Jahre lang als werbendes Unternehmen existiert) gegründet wurde.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_101`)


Wenn mir das Finanzamt letztlich vorwirft, dass die Furtder Technologien GmbH über eine UID-Nummer lediglich bis 9. Oktober 2012 und die NEP Lebensmittel GmbH über eine solche lediglich bis 30. August 2013 verfügt hatte und ich auch „nachher" noch Geschäfte mit diesen Unternehmen getätigt hätte, so ist dem zu entgegnen, dass einerseits nach ständiger Judikatur der anzulegende Sorgfaltsmaßstab nicht überspannt werden kann und darf und insbesondere andererseits Beauftragungen meiner Subunternehmer teilweise (sohin jeweils die letzten Aufträge) zu Zeitpunkten erfolgten, zu denen diese noch über die UlD-Nummer verfügt hatten, die Leistungserbringung aber (auch) in einen Zeitraum danach fiel und deren Rechnungen naturgemäß auch erst danach gelegt wurden.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_102`)


Seite 10 von 21 Bei der Furtder Technologien GmbH betrifft ein einziger (bereits fast zwei Jahre alter laufender!)

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_103`)


Auftrag einen Leistungszeitraum auch noch nach dem 09. Oktober 2012 (bezeichnenderweise das Finanzamt Adresse3), bei der NEP Lebensmittel GmbH wurden nur 6 Rechnungen nach dem 30. August 2013 gelegt, drei davon noch im September 2013 (sohin innerhalb eines Monates), drei bis Mitte Oktober 2013 (sohin innerhalb von 6 Wochen).

| Predicted | Gold |
|---|---|
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_106`)


Beim Auftrag Furtder Technologien GmbH Adresse3 handelte es sich überhaupt um einen zugrunde liegenden Auftrag über zwei Jahre, bereits die erste von der Furtder Technologien GmbH gelegte Rechnung 18/2012 vom 06.02.2012 wie auch so gut wie alle anderen beiliegenden Rechnungen der Furtder Technologien GmbH weist (weisen) als Leistungsgegenstand das BVH Adresse3 aus.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_119`)


Zu den im Rahmen der Außenprüfung nicht zum Betriebsausgabenabzug anerkannten Eingangsrechnungen der Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH führte der Beschuldigte auf Befragung aus, er habe diese Firmen zwar am Beginn ihrer Tätigkeit dahingehend kontrolliert, dass er Firmenbuchauszug, Auszug aus dem Gewerberegister und der HFU- Liste sowie UID Nummern überprüft habe.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `Fa.NEP Lebensmittel GmbH` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_122`)


Er könne somit auch keine Namen von Personen nennen, die namens der Firmen wie Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH tätig geworden seien und von ihm Aufträge in Empfang genommen hätten.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `Fa.NEP Lebensmittel GmbH` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_155`)


Auffällig ist auch, dass es mindestens 3 verschiedene Erscheinungsbilder von Rechnungen gibt, auf denen die Furtder Technologien GmbH als leistendes Unternehmen aufscheint.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_157`)


Die geltend gemachten Rechnungen der Furtder Technologien GmbH sind daher nicht anzuerkennen.

| Predicted | Gold |
|---|---|
| `Furtder Technologien GmbH` | `Furtder Technologien GmbH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_162`)


Die Rechnungen der NEP Lebensmittel GmbH sind daher nicht anzuerkennen.

| Predicted | Gold |
|---|---|
| `NEP Lebensmittel GmbH` | `NEP Lebensmittel GmbH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_201`)


Nach den vorliegenden Beweisergebnissen konnten die Beschwerdeausführungen des Amtsbeauftragten zu den Eingangsrechnungen der Fa.NEP Lebensmittel GmbH, der Kisteler Telekom GmbH und der Fa. X. d.o.o aus Sicht des erkennenden Senates nicht dazu führen, den Nachweis einer Abgabenhinterziehung als erbracht anzusehen.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `Fa.NEP Lebensmittel GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_216`)


Anhaltspunkte oder Beweismittel dahingehend, dass der Beschuldigte mit den rechnungsausstellenden Personen der Firmen NEP Lebensmittel GmbH und der Kisteler Telekom GmbH zusammengewirkt, von diesen Scheinrechnungen, denen tatsächlich keine Leistungen der Subunternehmer zugrunde gelegen wären, erworben hätte und der Beschuldigten die hier in Rede stehenden Leistungen mit eigenen schwarz beschäftigten Arbeitnehmern erbracht hätte, liegen nicht vor.

| Predicted | Gold |
|---|---|
| `Kisteler Telekom GmbH` | `Kisteler Telekom GmbH` |

**Missed by this rule (FN):**

- `NEP Lebensmittel GmbH` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_16`)


Nach dem Tod von F. (sen) H. wurde der Bäckereibetrieb per 31.12.2001 in die NiederTextil GmbH eingebracht (unter Rückbehalt der Immobilie) und die Immobilie wurde Teil des Verlassenschaftsverfahrens.

| Predicted | Gold |
|---|---|
| `NiederTextil GmbH` | `NiederTextil GmbH` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_19`)


Da aber die GmbH das Geschäftslokal innen massiv umbaute und einer der Ex-Erben (und Brüder) in der Familie drohte, die Erbübereinkunft anzufechten, wurde die Miete auf Ebene der GmbH 2005-2007 einstweilen nur rückgestellt, aber nicht ausgezahlt (€ 112.000 Wert der Rückstellung in NiederTextil GmbH Jahresabschluss zum 31.12.2007 II Miete 2005 - 2007 abzüglich Fassadenrenovierung), da die Mehrheit der Gesellschafterversammlung (75%) der Auszahlung aufgrund der Streitigkeiten nicht zustimmte (nur ein Vermieter ist mit 25% an der GmbH beteiligt gewesen).

| Predicted | Gold |
|---|---|
| `NiederTextil GmbH` | `NiederTextil GmbH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_39`)


Da das Gebäude im Zeitpunkt der Erbschaft komplett an die NiederTextil GmbH vermietet wurde, eignet sich hier das Ertragswertverfahren zur Berechnung der fiktiven Anschaffungskosten am besten.

| Predicted | Gold |
|---|---|
| `NiederTextil GmbH` | `NiederTextil GmbH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_14`)


Der Beschwerdeführer ist im Ausmaß von 38 Wochenstunden als Grundbildungspädagoge bei  der Veral-Maschinenbau GmbH im Projekt Basisbildung NÖ angestellt. In dieser Funktion vermittelt er den  Teilnehmenden (mit oft auch einer Teilleistungsschwäche), die das Pflichtschulalter  überschritten haben, Grundkompetenzen wie Schreiben und Rechtsschreibung, Lesen und  sinnerfassendes Lesen, Kenntnisse der Mathematik bis Hauptschulniveau, Umgang mit  digitalen Medien (Grundkenntnisse der Informationstechnologie).

| Predicted | Gold |
|---|---|
| `Veral-Maschinenbau GmbH` | `Veral-Maschinenbau GmbH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `TPA Steuerberatung GmbH` | `TPA Steuerberatung GmbH` |

**Missed by this rule (FN):**

- `Mag. Manuela Fischer` (person)
- `Isidor Czebulla` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `PROCURA Steuerberatung  GmbH` | `PROCURA Steuerberatung  GmbH` |

**Missed by this rule (FN):**

- `Dr. Wolfgang Freilinger` (person)
- `Hon.-Prof. Clemens Mooß` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_5`)


Das Finanzamt brachte im Einkommensteuerbescheid 2019 abweichend von der eingereich- ten Erklärung zur Arbeitnehmerveranlagung, in der die Anzahl der inländischen Arbeitgeber  mit "1" angegeben wurde, neben dem aus seiner ganzjährig ausgeübten Tätigkeit bei der Kozlowska&Pfnier Medien GmbH resultierenden Bezug auch von einer weiteren Arbeitgeberin ausbezahlte Beträge in  Höhe von 420,00 € als Einkünfte aus nichtselbständiger Arbeit in Ansatz.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_6`)


2. In der gegen den Einkommensteuerbescheid 2019 erhobenen Beschwerde brachte der Be- schwerdeführer vor, er sei seit dem Jahr 2018 bei der Kozlowska&Pfnier Medien GmbH als Arbeiter beschäftigt, bezahle  monatlich Lohnsteuer und sei daher nicht einkommensteuerpflichtig.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_12`)


Der Beschwer- deführer habe im Jahr 2019 neben den Bezügen von der Kozlowska&Pfnier Medien GmbH auch solche von einem  Taxiunternehmen erhalten und sei nach § 41 EStG 1988 daher zwingend eine Veranlagung  durchzuführen gewesen.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_14`)


4.  Mit als Vorlageantrag gewertetem Schreiben vom 7. Oktober 2020 brachte der Beschwer- deführer vor, er habe für das Taxiunternehmen von BC, seit er bei der Kozlowska&Pfnier Medien GmbH angestellt sei,  nicht mehr gearbeitet.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_29`)


Der Beschwerdeführer bezog im Streitjahr Einkünfte aus nichtselbständiger Arbeit aus einer bei  der Kozlowska&Pfnier Medien GmbH ganzjährig ausgeübten Tätigkeit.

| Predicted | Gold |
|---|---|
| `Kozlowska&Pfnier Medien GmbH` | `Kozlowska&Pfnier Medien GmbH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bernhart Steuerberatungs GmbH` | `Bernhart Steuerberatungs GmbH` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Daisy Große-Bölting` (person)
- `Serena Leutl` (person)
- `Wanderweg 7, 2763 Thal, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-306/6017` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Treuhand Steuerberatung GmbH` — partial — pred is substring of gold: `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_63`)


Dem Beschuldigten wurde wie folgt vorgehalten: Laut Bericht über die Außenprüfung vom 11.10.2017 unter Tz 2 wurden nicht anzuerkennende Fremdleistungen aufgrund von Scheinrechnungen der Fa. X. für das Jahr  2012 iHv € 74.884,49 und für 2013 iHv € 18.550,91 festgestellt. Weiters wurden nach den Feststellungen im Bericht über die Außenprüfung vom 11.10.2017 unter Tz. 4 Fremdleistungen aufgrund von auf den Namen der Kisteler Telekom GmbH lautenden Rechnungen im Jahr 2012 iHv € 220.314,31 sowie auf den Namen der Fa.NEP Lebensmittel GmbH lautenden Rechnungen im Jahr 2013 iHv € 115.236,61 als Betriebsausgaben geltend gemacht.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kisteler Telekom GmbH`(organisation)
- `Fa.NEP Lebensmittel GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_67`)


Im Bezug auf die Fa.NEP Lebensmittel GmbH legte der Beschuldigte in Beantwortung des Vorhalts einen Firmenbuchauszug vom 14.1.2013, eine ZMR-Auskunft vom 26.2.2013, einen Auszug aus dem Gewerberegister vom 22.2.2013, 3 Auszüge aus der HFU-Liste sowie Rechnungen samt Zahlungsbestätigungen und Ersatzschecks (Barabhebungen) im Betrag von € 43.500,00 bei.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_104`)


Es ist daher unverständlich, wieso das FA 4/5/10 in seiner Niederschrift und Bericht über das Ergebnis der Außenprüfung vom 11.10.2017 auf Seite 6, Mitte, zum Tatbestand P.NEP Lebensmittel GmbH ausführen kann, dass „ die geltend gemachten Rechnungen erst danach ..." (Anm.: nach dem 30. August 2013) ausgestellt wurden.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `P.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `P.NEP Lebensmittel GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_105`)


Tatsächlich datieren 16 der insgesamt 22 (beiliegenden) Rechnungen der P.NEP Lebensmittel GmbH vor dem 30. August 2013, wobei - noch einmal - die „Vorlaufzeit“ bezüglich auch der anderen 6 Rechnungen (von der Auftragserteilung bis zur tatsächlichen Rechnungslegung) rund vier bis acht Wochen (!) beträgt.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `P.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `P.NEP Lebensmittel GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_106`)


Beim Auftrag Furtder Technologien GmbH Adresse3 handelte es sich überhaupt um einen zugrunde liegenden Auftrag über zwei Jahre, bereits die erste von der Furtder Technologien GmbH gelegte Rechnung 18/2012 vom 06.02.2012 wie auch so gut wie alle anderen beiliegenden Rechnungen der Furtder Technologien GmbH weist (weisen) als Leistungsgegenstand das BVH Adresse3 aus.

**False Positives:**

- `Beim Auftrag Furtder Technologien GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)
- `Furtder Technologien GmbH`(organisation)
- `Furtder Technologien GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_119`)


Zu den im Rahmen der Außenprüfung nicht zum Betriebsausgabenabzug anerkannten Eingangsrechnungen der Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH führte der Beschuldigte auf Befragung aus, er habe diese Firmen zwar am Beginn ihrer Tätigkeit dahingehend kontrolliert, dass er Firmenbuchauszug, Auszug aus dem Gewerberegister und der HFU- Liste sowie UID Nummern überprüft habe.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_122`)


Er könne somit auch keine Namen von Personen nennen, die namens der Firmen wie Fa.NEP Lebensmittel GmbH und der Kisteler Telekom GmbH tätig geworden seien und von ihm Aufträge in Empfang genommen hätten.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_161`)


Die geltend gemachten Rechnungen wurden daher erst danach ausgestellt. Die NEP Lebensmittel GmbH ist darüber hinaus in den letzten Jahren immer wieder im Zuge von Außenprüfungen als Betrugsfirma in Erscheinung getreten.

**False Positives:**

- `Die NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_167`)


Mit weiteren Bericht vom 2.11.2017 (ABNr. ****/16) wurde eine Prüfung der lohnabhängigen Abgaben für den Zeitraum 1.1.2012-31.12.2014 abgeschlossen, im Rahmen derer folgende für das gegenständliche Beschwerdeverfahren relevante Feststellungen getroffen wurden: "Pauschale Nachrechnung Finanz 2012 Sachverhaltsdarstellung Im Zuge der Betriebsprüfung wurden die Fremdleistungen der Firmen Furtder Technologien GmbH  D- GmbH und E-GmbH im KJ 2012 nicht anerkannt.

**False Positives:**

- `Firmen Furtder Technologien GmbH  D- GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_171`)


Für das gegenständliche Verfahren ergibt sich aufgrund der Nichtanerkennung der Fremdleistungen der Firmen Furtder Technologien GmbH in Höhe von € 220.314,31 ein fiktiver Lohnaufwand von € 110.170,65.

**False Positives:**

- `Firmen Furtder Technologien GmbH` — partial — gold is substring of pred: `Furtder Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtder Technologien GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_173`)


Im Zuge der Betriebsprüfung wurden die Fremdleistungen der Firma NEP Lebensmittel GmbH im KJ 2013 nicht anerkannt.

**False Positives:**

- `Firma NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_189`)


Die Firma wurde als eine ein Mann GmbH gegründet, beschäftigte keine Arbeitnehmer und bediente sich keiner Hilfskräfte.

**False Positives:**

- `Mann GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_201`)


Nach den vorliegenden Beweisergebnissen konnten die Beschwerdeausführungen des Amtsbeauftragten zu den Eingangsrechnungen der Fa.NEP Lebensmittel GmbH, der Kisteler Telekom GmbH und der Fa. X. d.o.o aus Sicht des erkennenden Senates nicht dazu führen, den Nachweis einer Abgabenhinterziehung als erbracht anzusehen.

**False Positives:**

- `NEP Lebensmittel GmbH` — partial — pred is substring of gold: `Fa.NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_216`)


Anhaltspunkte oder Beweismittel dahingehend, dass der Beschuldigte mit den rechnungsausstellenden Personen der Firmen NEP Lebensmittel GmbH und der Kisteler Telekom GmbH zusammengewirkt, von diesen Scheinrechnungen, denen tatsächlich keine Leistungen der Subunternehmer zugrunde gelegen wären, erworben hätte und der Beschuldigten die hier in Rede stehenden Leistungen mit eigenen schwarz beschäftigten Arbeitnehmern erbracht hätte, liegen nicht vor.

**False Positives:**

- `Firmen NEP Lebensmittel GmbH` — partial — gold is substring of pred: `NEP Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NEP Lebensmittel GmbH`(organisation)
- `Kisteler Telekom GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `Steuerberatungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Partner Steuerberatung GmbH` — partial — pred is substring of gold: `ECA Mag. Pichler & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Partner GmbH` — partial — pred is substring of gold: `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof.in Ophelia Dutschka`(person)
- `Diepolding 3, 3754 Trabenreith, Österreich`(address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Steuerberatung GmbH` — partial — pred is substring of gold: `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_18`)


Es wurden EUR 200,00 an Vorsteuern im Zusammenhang mit der  vorgelegten Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 anstatt EUR 11.220,00 anerkannt.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_31`)


Die GmbH sei am Datum1 amtswegig im Firmenbuch gelöscht worden.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_82`)


Am TTMM 2016 erging eine an die Bf. gerichtete Rechnung der Kraußkopf Chemie GmbH iHv EUR 1.000,00  netto zuzüglich EUR 200,00 Umsatzsteuer.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_126`)


Somit waren bereits im beschwerdegegenständlichen Zeitraum die materiellen  Voraussetzungen für die Entstehung des Vorsteuerabzuges erfüllt.  Deshalb und da die Anerkennung des Vorsteuerabzuges iHv EUR 200,00 aus der Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 unstrittig war, war spruchgemäß zu entscheiden.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_9`)


Bei einer Kontrolle am  18.2.2015, 15:15 Uhr, befand sich das Fahrzeug in B am Parkplatz der Fa.NiederImmobilien Institut GmbH  Der Bf sei  von April 2010 bis Juni 2013 – dh. im Zeitraum der Einbringung des Fahrzeuges - an  1 von 29 Seite 2 von 29

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_19`)


Diese Leasingfirma ist in Konkurs gegangen und aus diesem Grund hat mich die Fa.NiederImmobilien Institut GmbH im Oktober 2012 übernommen und bin seitdem Vollzeit mit 42,5 Stunden pro Woche  beschäftigt.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_46`)


Auf  die Frage, warum ich dieses KFZ in Deutschland angemeldet habe, gebe ich an, dass ich nicht  weiß, wie lange ich hier bleibe, da es sein kann, dass ich bei der Fa.NiederImmobilien Institut GmbH kündigen werde.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_77`)


e) Bestätigung der Sozialversicherung v. Oktober 2012:  Demnach ist der Bf ab 22.10.2012 bei der Fa.NiederImmobilien Institut GmbH als Arbeiter/Hilfskraft vollbeschäftigt (=  40 Wochenstunden) und erhält einen Monatslohn von brutto € 1.513,60.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_90`)


Aufgrund der  seit 22.10.2012 bestehenden Vollzeitbeschäftigung bei der Fa.NiederImmobilien Institut GmbH liege ein quantitativ  überwiegender Aufenthalt samt Wohnsitz im Inland vor, weshalb sich der Mittelpunkt der  Lebensinteressen des Bf in Österreich befinde.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_142`)


c) 1 Konvolut an monatlichen Arbeitszeitnachweislisten des Bf bei der Fa.NiederImmobilien Institut GmbH  Zeitraum  Jänner 2014 – Dezember 2015:  Eine nähere Überprüfung durch das BFG hat in Gegenüberstellung des Arbeitszeitnachweises  (siehe untentstehend 2 rechte Spalten) zu den vom Bf vorgelegten Aufzeichnungen seiner  "Heimfahrten" Ö-D-Ö (siehe untenstehend die 2 linken Spalten) folgende Divergenzen  ergeben:    Fahrten Ö-D-Ö lt.  Aufzeichnung Bf    Lt. Zeitnachweisliste  des Arbeitgebers

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_152`)


c) Abfrage der Sozialversicherungs-Daten:  Demnach war der Bf ab 22.10.2012 – 16.4.2016 und ist seit 6.6.2016 laufend als Arbeiter bei  der Fa.NiederImmobilien Institut GmbH in B (Ö) als Arbeiter beschäftigt, Bruttogehalt 2014/2015 jährlich rund €  33.000.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_166`)


3.) Einsicht in die Sozialversicherungs-Daten:  Der Bf war mit kurzzeitigen Unterbrechungen, in denen meist Arbeitslosengeld bezogen  wurde, ab 5.5.2008 bis 21.10.2012 bei E und ab 22.10.2012 bei der Fa.NiederImmobilien Institut GmbH beschäftigt.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_186`)


2. Berufliche/wirtschaftliche Nahebeziehung:  Fest steht nach dem Akteninhalt und bisher durchgeführten Erhebungen, dass der  Beschwerdeführer Sven Mitterhuber (Bf) ab 2009 im Inland berufstätig bzw. jedenfalls im strittigen  Zeitraum durchgehend bei der Fa.NiederImmobilien Institut GmbH in Vollzeit (42,5 Stunden/Woche) beschäftigt war  und laut Abfrage der Sozialversicherungsdaten nach wie vor ist.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sven Mitterhuber`(person)
- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_189`)


Im Rahmen einer Betrachtung der beruflichen und wirtschaftlichen Beziehungen wäre daher  nach Ansicht des BFG insgesamt von einer weitaus überwiegenden Nahebeziehung zu  Österreich auszugehen, die insbesondere aufgrund der langjährigen und durchgehenden  beruflichen Tätigkeit bei der Fa.NiederImmobilien Institut GmbH bereits seit vielen Jahren besteht.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_296`)


Insolvenz und schlechter Arbeitslage in D) zunächst 2008 als Leasingarbeiter  bei Fa. E nach Österreich gekommen und ist seit Oktober 2012 bei der Fa.NiederImmobilien Institut GmbH als Arbeiter  in Vollzeit im Umfang von 40 h, lt. eigenen Angaben mit 42,5 h (siehe Niederschrift v.  22.4.2015) nahezu durchgehend tätig.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_403`)


Er war ab 2008 zunächst als  Leiharbeiter und ist seit Oktober 2012 als Arbeiter bei der Fa.NiederImmobilien Institut GmbH nahezu durchgehend im  Inland berufstätig, bezieht daraus seither Einkünfte aus nichtselbständiger Arbeit und hat ua.  die Arbeitnehmerveranlagung durchführen lassen.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Consulting GmbH` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_10`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna war zu den  Beanstandungszeiten (22. und 23. Oktober 2019) auf die Fa.RIL Planung GmbH  Dorf, zugelassen.

**False Positives:**

- `RIL Planung GmbH` — partial — pred is substring of gold: `Fa.RIL Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RIL Planung GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_12`)


In der Begründung  sei ausgeführt worden, die Kundengewinnung durch den Beschwerdeführer stelle eine  Vermittlungsleistung dar, Leistungsempfänger sei die Zäsar u. Cankurt Analyse GmbH  da diese im eigenen Namen  auftrete.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_17`)


Die Schweizer M-AG oder auch die im Erkenntnis  RV/7100189/2015 angeführte Tochtergesellschaft Zäsar u. Cankurt Analyse GmbH als vermeintliche  Leistungsempfängerin habe daher niemals einen spiegelbildlichen Vorsteuerabzug gehabt,  sodass die einseitige Vorschreibung von Umsatzsteuer auf Ebene des Beschwerdeführers aus  den erhaltenen Nettohonoraren gegen die Mehrwertsteuersystemrichtlinie idF RL 2010/45/EU  2 von 7 Seite 3 von 7

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_26`)


Als Leistungsempfänger der beschwerdegegenständlichen  Vermittlungsleistungen trat in den Streitjahren die unternehmerisch tätige Muttergesellschaft  M-AG und nicht die Tochtergesellschaft Zäsar u. Cankurt Analyse GmbH auf.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_33`)


L wird in Österreich durch die Zäsar u. Cankurt Analyse GmbH mit Sitz AdresseT-GmbH (im  Folgenden " T-GmbH" genannt) vertreten.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wthrd GmbH` — partial — pred is substring of gold: `Heinz Neuböck Wthrd GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_4`)


Darüber hinaus war er an der Schifffahrtsgesellschaft S GmbH & Co KG mit Sitz in H,  Deutschland, als Kommanditist beteiligt.

**False Positives:**

- `Schifffahrtsgesellschaft S GmbH` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_11`)


In der am 4.4.2014 beim Finanzamt eingelangten Einkommensteuererklärung für 2012 erklärte  der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_13`)


In der am 12.1.2015 beim Finanzamt eingelangten Einkommensteuererklärung für 2013  erklärte der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)


Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG vor.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`
- `L GmbH` — partial — pred is substring of gold: `L GmbH &  Co`
- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)
- `L GmbH &  Co`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_24`)


Die GmbH unterrichtet die Gesellschafter und den Beirat über die Entwicklung der  Geschäfte…  2 von 13 Seite 3 von 13

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_33`)


Die Gesellschafter/ Treugeber können sich in Gesellschafterversammlungen und  Beschlussfassungen nur durch einen anderen Gesellschafter, einen Ehegatten, einen Elternteil,  ein volljähriges Kind, einen Testamentsvollstrecker, seinen ständigen Generalbevollmächtigten,  einen anderen Treugeber oder einen Vertriebspartner der Gesellschaft/ L GmbH & Co vertreten  lassen.

**False Positives:**

- `L GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_45`)


In der gesonderten zugestellten Bescheidbegründung wurde ausgeführt:  „Aus dem übermittelten „Reeder-Zertifikat“ Nr. 277 geht hervor, dass der Bf. an der Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG) beteiligt ist.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_48`)


Die Bereederung des Schiffes wurde durch 2 Verträge geregelt (technische Bereederung inkl.  Operating und Crewing durch Bürgin & Siedle Umwelt GmbH& Co KG; kaufmännische Bereederung durch QGM Technik GmbH & Co KG.

**False Positives:**

- `Siedle Umwelt GmbH` — partial — pred is substring of gold: `Bürgin & Siedle Umwelt GmbH&`
- `QGM Technik GmbH` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bürgin & Siedle Umwelt GmbH&`(organisation)
- `QGM Technik GmbH & Co KG`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_71`)


Er beantragte die Anerkennung der Verlusttangente 2011 aus der Beteiligung an der S GmbH &  Co KG in Höhe von 34.275,23 €, die Zurücknahme der Endgültigkeitserklärung des  Einkommensteuerbescheides 2012 sowie die Erklärung des Einkommensteuerbescheides 2013  als gemäß § 200 Abs. 1 BAO vorläufiger Bescheid.

**False Positives:**

- `S GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_119`)


Im  kaufmännischen Reedervertrag mit der QGM Technik GmbH & Co KG nimmt der Vertragsreeder alle  Geschäfts- und Rechtshandlungen vor, die der kaufmännische Geschäftsbetrieb einer Reederei  gewöhnlich mit sich bringt und erfordert (Einsatz und Beschäftigung des Schiffes, Versicherung,  Interessenswahrnehmung).

**False Positives:**

- `QGM Technik GmbH` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QGM Technik GmbH & Co KG`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_120`)


Im technischen Reedervertrag mit der Mohrlock Metall GmbH & Co KG nimmt  der Vertragsreeder alle Geschäfts- und Rechtshandlungen vor, die der technische  8 von 13 Seite 9 von 13

**False Positives:**

- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_122`)


Der Betrieb des Schiffes, wobei sich die Gesellschaft Dritter (Vertragsreeder) bedient, die für  die S GmbH & Co KG handeln, geht jedenfalls über eine Vermögensverwaltung hinaus.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `S GmbH & Co KG`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_126`)


2. Beweiswürdigung  Strittig ist, ob es sich bei der Beteiligung an der Schifffahrtsgesellschaft S GmbH & Co KG um  eine mitunternehmerische Beteiligung handelt und damit Einkünfte aus Gewerbebetrieb  vorliegen oder um eine Beteiligung nach Art eines stillen Gesellschafters und damit Einkünfte  aus Kapitalvermögen vorliegen.

**False Positives:**

- `Schifffahrtsgesellschaft S GmbH` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_151`)


Die Abgabenbehörde beurteilt den Gesellschaftsvertrag, welcher zwischen der Dörfel u. Rudolphson Heizung GmbH & Co KG und dem Bf. abgeschlossen wurde, in wirtschaftlicher Betrachtungsweise als Vertrag, mit  welchem eine Beteiligung nach Art eines stillen Gesellschafters abgeschlossen wurde.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_167`)


Kann kein Firmenwert entstehen, weil die operativen Geschäfte (Vertragsreederei mit  Unternehmerrisiko) nicht von der Schifffahrtsgesellschaft S GmbH & Co KG, sondern von der L  GmbH & Co und der Mohrlock Metall GmbH & Co KG durchgeführt werden und besteht deshalb der Wert der  Gesellschaft lediglich im Buchwert inklusive der stillen Reserven des Schiffes, so ist dies ein  weiterer Hinweis dafür, dass keine mitunternehmerische Beteiligung, sondern eine Beteiligung  nach Art eines stillen Gesellschafters vorliegt.

**False Positives:**

- `Schifffahrtsgesellschaft S GmbH` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`
- `L  GmbH` — no gold match — likely missing annotation
- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_179`)


Nach Ansicht des Bundesfinanzgerichtes hat die Abgabenbehörde in unbedenklicher Weise in  wirtschaftlicher Betrachtungsweise die gegenständliche Beteiligung an der Schifffahrtsgesell- schaft S GmbH & Co KG als eine Beteiligung nach Art eines stillen Gesellschafters qualifiziert  und die daraus erklärten negativen Einkünfte den nichtausgleichsfähigen Einkünften aus  Kapitalvermögen zugerechnet.

**False Positives:**

- `S GmbH` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `S GmbH & Co KG`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_5`)


Mit dem – unter Verweis auf eine beiliegende Bescheidkopie - als „Einspruch gegen den  Einkommensteuerbescheid 2010“ titulierten Schriftsatz begehrte der Bf die Anpassung der  Höhe seiner Einkünfte aus selbständiger Arbeit nach Abschluss eines Gerichtsverfahrens, in  welchem am 27.Jänner 2020 die Ungültigkeit eines Gesellschafterbeschlusses der  Tourismus- GmbH (WWW-GmbH) vom 8.Sept.2010 über die Höhe seiner  Geschäftsführerentschädigung festgestellt worden sei.

**False Positives:**

- `Tourismus- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)


Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die Firma2 GmbH & CoKG, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

**False Positives:**

- `Firma1 GmbH` — no gold match — likely missing annotation
- `Firma2 GmbH` — partial — pred is substring of gold: `Firma2 GmbH & CoKG`
- `Firma3  GmbH` — partial — pred is substring of gold: `Firma3  GmbH & CoKG`
- `Firma4 GmbH` — no gold match — likely missing annotation
- `Die Firma1 GmbH` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 3

**Gold Entities:**

- `Firma2 GmbH & CoKG`(organisation)
- `Firma3  GmbH & CoKG`(organisation)
- `PhD Mag. Heinrich Hambücher`(person)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_42`)


bis zur Bescheidausfertigung durch die BRZ GmbH seien somit keine Handlungen mehr  verblieben, die von der zuständigen belangten Behörde tatsächlich hätten vorgenommen  werden können.

**False Positives:**

- `BRZ GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_53`)


Firma5 GmbH (FN xxxxxxxxx) - diese jedoch als reine Arbeitsgesellschafterin – auf.

**False Positives:**

- `Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_56`)


Mit Vertrag vom xx.xx.xxxx nahm die Rechtsvorgängerin & CoKG als Geschäftsherrin die Firma6  GmbH (FN xxxxxx) als atypisch stille Gesellschafterin mit einer Einlage von insgesamt Euro xxxx  auf, wobei das Gesellschaftsverhältnis auf Grundlage des Artikels IV Umgründungssteuergesetz  vereinbart worden war.

**False Positives:**

- `Firma6  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_57`)


Die Firma6 GmbH ihrerseits hielt sämtliche Einlagen lediglich  treuhändig;

**False Positives:**

- `Die Firma6 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_69`)


Ob die belangte Behörde der Firma2  Firma5 GmbH & CoKG für den Zukauf der mit Rechnungen vom xx.xx.xxxx an die Bf.  verrechneten Leistungen die Vorsteuer gewährt hat, ist ebenfalls nicht feststell-, jedoch auch  nicht ausschließbar.

**False Positives:**

- `Firma2  Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_71`)


Ob die Firma4 GmbH - wie mit Rechnung vom xx.xx.xxxx (Rechnungsnummer 2007-0013)  abgerechnet - Beratungsleistungen im Ausmaß von gesamt Euro xx (brutto) erbrachte, kann  nicht festgestellt werden.

**False Positives:**

- `Firma4 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_72`)


Den Rechnungen der Freizeit Immobilien-Firma5 GmbH & Co KEG vom xx.xx.xxxx  (Rechnungsnummer 2007-0001 und Rechnungsnummer 2007-0002;

**False Positives:**

- `Freizeit Immobilien-Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_74`)


Am xx.xx.xxxx schied die Firma5 GmbH als unbeschränkt haftende Gesellschafterin aus;

**False Positives:**

- `Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_78`)


Die Beteiligung der Firma6 GmbH als (atypisch) stille Gesellschafterin ist zwischen den  Streitteilen unstrittig und resultieren die diesbezüglichen Feststellungen auch aus der im Akt  erliegenden Mitteilung vom 30.05.2008 an das Finanzamt xx sowie dem ebenfalls vorliegenden  Gesellschaftsvertrag vom xx.xx.xxxx.

**False Positives:**

- `Firma6 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_89`)


Wie  aus der Analyse hervorgeht, wurden diese Unterlagen zwar von der Firma1 GmbH erstellt,  jedoch in Kooperation mit der Firma2 Firma5 GmbH & Co. KG, der späteren Rechnungslegerin.

**False Positives:**

- `Firma1 GmbH` — no gold match — likely missing annotation
- `Firma2 Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_90`)


Das ebenfalls beiliegende Verkehrswertgutachten nennt als Auftraggeber ebenfalls die Firma2  Firma5 GmbH & Co. KG.

**False Positives:**

- `Firma2  Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_93`)


Für das erkennende  Gericht ergibt sohin eine Zusammenschau zwischen der Rechnung vom xx.xx.xxxx, der - 12  Seiten umfassenden - Objektinvestitions- und Finanzierungsanalyse, sowie dem - 67 Seiten  umfassenden - Verkehrswertgutachten keinen Zweifel, dass zwischen der Firma2 Firma5 GmbH  & Co. KG und der Bf. ein Leistungsaustausch stattgefunden hat;

**False Positives:**

- `Firma2 Firma5 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_99`)


Was die weiteren festgestellten Leistungen anlangt, so steht deren Erbringung nicht nur  aufgrund des Angebots der Firma1 GmbH vom xx.xx.xxxx sowie der Annahme desselben durch  die Bf. am xx.xx.xxxx fest, sondern ergibt sich unstrittig auch aus den vorgelegten Analysen.

**False Positives:**

- `Firma1 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_104`)


Hingegen konnte ein Leistungsaustausch im Zusammenhang mit der vorgelegten Rechnung  vom xx.xx.xxxx (Rechnungsnummer 2007-0013) deshalb nicht festgestellt werden, da darin  einerseits lediglich ein Pauschalbetrag für „Beratungsleistungen im Zeitraum September- Dezember 2007“verrechnet wurde und andererseits aus den dazu von der Bf. vorgelegten  Unterlagen („Immobilien Development Beteiligung 2007“ Informationsfolder, Angebot zum  Abschluss einer Treuhandvereinbarung, Gesellschaftsvertrag atypisch stille Beteiligung 2007,  Treuhandvereinbarung zur atypisch stillen Beteiligung 2007 und Schriftverkehr) kein  Zusammenhang zwischen der Firma4 GmbH und der Bf. herstellbar ist.

**False Positives:**

- `Firma4 GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_company_e_commerce` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e91d48ca`  
**Description:**
Matches specific E-Commerce company patterns.

**Content:**
```
\b([A-Z][a-zA-Z0-9\-]+\s+u\.\s+[A-Z][a-zA-Z0-9\-]+\s+E‑?Commerce)\b
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

</details>

---

<details>
<summary>❌ False Negatives (1137, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)

Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des **Magistrates der Stadt  Wien, Magistratsabteilung 67**, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des **Finanzamtes Wien  12/13/14 Purkersdorf** vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

- missed: `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_17`)

Dieser Antrag wurde dem Verfassungsgerichtshof zur Normenprüfung vorgelegt und erging am  22.09.2021 der Beschluss des **Verfassungsgerichtshofes** mit welchem der Antrag des Bf.  zurückgewiesen wurde.

- missed: `Verfassungsgerichtshofes` (organisation)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138259.1`) (sent_id: `deanon_BFG_20260814_TEST/138259.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Otto Pavlikova  in der Angelegenheit der Parteien  Oskar Wood (Beschwerdeführer) und Finanzamt Österreich als Amtspartei und als  Gesamtrechtsnachfolger des FA Niederösterreich Mitte  über die Beschwerde vom  22.6.2020 gegen den Bescheid des **FA Niederösterreich Mitte**  vom 22.5.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019         zu Recht erkannt:  Der Beschwerde wird Folge gegeben.

- missed: `FA Niederösterreich Mitte` (organisation)
- predicted in sentence: `Finanzamt Österreich`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_39`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. war im Streitjahr 2014 beim österreichischen Unternehmen **PGZO Lebensmittel Betriebe GmbH**  mit Sitz in  Leopoldsdorf nichtselbständig beschäftigt und übte seine Tätigkeit auf diversen Baustellen in  Wien und in ganz Österreich aus.

- missed: `PGZO Lebensmittel Betriebe GmbH` (organisation)
- predicted in sentence: `Unternehmen PGZO Lebensmittel Betriebe GmbH`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_37`)

Gegen diese Bescheide vom 18. und 24. November 2020 brachte der Bf. am 25. November  2020 und 7. Dezember 2020 die hier verfahrensgegenständlichen Bescheidbeschwerden ein,  und verwies jeweils zur Begründung „auf meine Ausführungen im Antrag und in der  Beschwerde.“  ****  Mit Beschwerdevorentscheidungen vom 21. Dezember 2020 und 27. Jänner 2021 wies das  Finanzamt Wien 1/23, bzw. das Finanzamt Österreich als Rechtsnachfolger des **Finanzamtes  Wien 1/23** die Beschwerden vom 25. November 2020 und 7. Dezember 2021 als unbegründet  ab.

- missed: `Finanzamtes  Wien 1/23` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt Österreich`, `Finanzamtes`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher **Finanzamt Wien 2/20/21/22**) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Finanzamt Wien 2/20/21/22` (organisation)
- predicted in sentence: `Finanzamtes  Österreich`, `Finanzamt`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_25`)

In der abweisenden BVE betreffend Umsatzsteuer 2015 vertrat das Finanzamt die Ansicht,  dass nach § 7 Abs. 4 der Verordnung des **BM für Finanzen**, BGBl. II Nr. 125/2013 idF BGBl. II  Nr. 164/2014 über die Aufstellung von Durchschnittssätzen für die Ermittlung des Gewinnes  aus Land- und Forstwirtschaft (LuF-PauschVO 2015) die Be- oder Verarbeitung von  Urprodukten durch einen Land- und Forstwirt unter den dort aufgezählten Kriterien  (insbesondere bei Überschreitung der Einnahmengrenze von € 33.000,00) mangels  wirtschaftlicher Unterordnung im Verhältnis zum land- und forstwirtschaftlichen Hauptbetrieb  nicht den Einkünften aus Land- und Forstwirtschaft zugeordnet werden.

- missed: `BM für Finanzen` (organisation)
- predicted in sentence: `Finanzamt`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_151`)

Die Abgabenbehörde beurteilt den Gesellschaftsvertrag, welcher zwischen der **Dörfel u. Rudolphson Heizung GmbH & Co KG** und dem Bf. abgeschlossen wurde, in wirtschaftlicher Betrachtungsweise als Vertrag, mit  welchem eine Beteiligung nach Art eines stillen Gesellschafters abgeschlossen wurde.

- missed: `Dörfel u. Rudolphson Heizung GmbH & Co KG` (organisation)
- predicted in sentence: `Rudolphson Heizung GmbH`

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des **Finanzamtes für Großbetriebe** je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Finanzamtes für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  **Finanzamtes Gmunden Vöcklabruck** vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

- missed: `Finanzamtes Gmunden Vöcklabruck` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_52`)

Das Einkommen 2007 und die darauf entfallende Abgabe waren wie folgt zu berechnen:    Einkommensteuer für 2007  Einkünfte aus nichtselbständiger Arbeit  Übermittelte Lohnzettel (KZ 245)  **ÖBB** 25.324,62 €  Sonstige Werbungskosten ohne Anrechnung  Auf den Pauschbetrag -1.125,00 €  Pauschbetrag für Werbungskosten -132,00 € 24.067,62 €  Einkünfte aus Vermietung und Verpachtung  -1.688,49 €   -----------------  4 von 6 Seite 5 von 6

- missed: `ÖBB` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des **FA St. Johann Tamsweg Zell am See**  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `FA St. Johann Tamsweg Zell am See` (organisation)
- predicted in sentence: `Finanzamt`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_36`)

Schon daraus zeigt sich ganz klar, dass es zum Zeitpunkt des Abschlusses des Kaufvertrages  keine vertragliche Bindung an die Firma **MH-Bau GmbH** zwecks Errichtung des Hauses gegeben  hat.“

- missed: `MH-Bau GmbH` (organisation)
- predicted in sentence: `Firma MH-Bau GmbH`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_107`)

Der **Gerichtshof der Europäischen Union** hat die Rechtsfrage, ob ein Anpassungsmechanismus  in Form der Indexierung nach der Kaufkraft in den einzelnen Mitgliedsstaaten bzw.  Vertragsstaaten in Bezug auf die Familienbeihilfe und den Kinderabsetzbetrag für  Erwerbstätige, deren Kinder ständig in einem anderen Mitgliedstaat wohnen, mit dem  Unionsrecht vereinbar ist, eindeutig beantwortet.

- missed: `Gerichtshof der Europäischen Union` (organisation)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_444`)

Dem Vorbringen der beschwerdeführenden Partei, aus der zitierten Rechtsprechung des  **Verfassungsgerichtshofes** ergebe sich die Notwendigkeit einer Differenzierung zwischen den  Kostenstrukturen aufgrund der Verlängerung der Maßnahme, kann nicht gefolgt werden.

- missed: `Verfassungsgerichtshofes` (organisation)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_78`)

2 StudFG zutrifft, da er  nach drei Semestern  Wirtschaftsrecht an der WU Wien im Wintersemester 2017/2018 mit  dem Studium der Humanmedizin an der **Universität Wien** begann.

- missed: `Universität Wien` (organisation)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_40`)

Die Bf besteht nach den Eintragungen im elektronischen Akteninformationsssystem des  **Bundesministeriums für Finanzen** zumindest seit dem Jahr 2003, weil bis zu diesem Jahr  Eintragungen zurückverfolgt werden konnten.

- missed: `Bundesministeriums für Finanzen` (organisation)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_18`)

Folgende Punkte sind nach Ansicht des **Finanzamtes Landeck Reutte** noch ergänzungsbedürftig:   In der Beschwerdeschrift vom 10.10.2017 wird festgehalten, dass der Bf. in der Schweiz  ansässig ist, warum wurde auf den übermittelten Lohnzetteln aus der Schweiz bis  einschließlich 2015 eine österreichische Adresse vermerkt?

- missed: `Finanzamtes Landeck Reutte` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 7. Mai 2021 der Beschwerdeführerin Liu Maackens, LLM Bakk. techn., Alfons-Petzold-Hof 4, 2042 Grund, Österreich  vertreten durch die mit  Zustellvollmacht ausgewiesene **WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG**,  Blumauerstraße 35, 4020 Linz, gegen den Bescheid des Finanzamtes Österreich vom 8. April  2021 betreffend Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand gem. §  308 BAO betreffend Erklärung des Widerrufs des Regelbesteuerungsantrages gem. § 6 Abs 3  UStG 1994  zu Recht:    I)  Die Beschwerde wird als unbegründet abgewiesen.

- missed: `WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG` (organisation)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_165`)

Auf die von der Beschwerdeführerin bereits im vormaligen verwaltungsgerichtlichen Verfahren  ins Treffen geführte Entscheidung des **Obersten Gerichtshofes** vom 24. Juni 2019, 2 Ob  221/18s war mit Fokus auf die Sache des gegenständlichen Verfahrens primär auf die Thematik  der Bindungswirkung des „Vorprozesses“ einzugehen;

- missed: `Obersten Gerichtshofes` (organisation)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_23`)

04. 2020, RE/7100001/2020 an den **Gerichtshof der Europäischen Union**  gemäß Art. 267 AEUV gestellte Ersuchen um Vorabentscheidung, ob die Indexierung von  Familienleistungen durch den österreichischen Gesetzgeber nach der Kaufkraft in den  einzelnen Mitgliedsstaaten bzw. Vertragsstaaten unionsrechtskonform ist, protokolliert zu C- 163/20, gemäß Artikel 100 Abs. 1 Verfahrensordnung des Gerichtshofs der Europäischen Union  und § 290 Abs 3 BAO zurückgenommen.

- missed: `Gerichtshof der Europäischen Union` (organisation)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_107`)

Unter Verweis auf diese Ausführungen wird sohin gestellt der höfliche Antrag, der Beschwerde des FA 9/18/19 Klosterneuburg vom 07. Jänner 2019 gegen das Erkenntnis des Spruchsenates beim **Finanzamt Wien** 9 / 18 / 19/ Klosterneuburg vom 5. Dezember 2018, SpS *****,  keine Folge zu geben."

- missed: `Finanzamt Wien` (organisation)
- predicted in sentence: `Finanzamt`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_79`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. war Geschäftsführer der **NordGetränke GmbH**  über deren Vermögen über Antrag des Bf. mit  Beschluss des Landesgerichtes Feldkirch vom tt.11.2011 der Konkurs eröffnet wurde.

- missed: `NordGetränke GmbH` (organisation)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_45`)

Am 06.11.2023 wies sich die **Deloitte Tax Wirtschaftsprüfungs GmbH** als weitere steuerliche  Vertreterin der Bf. aus und erstattete umfassendes Vorbringen dazu, weshalb den  angefochtenen Erledigungen keine Bescheidqualität zukommen könne.

- missed: `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_17`)

Eine neuerliche Vorschreibung mit Bescheid des **Zollamtes Feldkirch Wolfurt**  vom 19.12.2019 hinsichtlich Zoll, EUSt und Verzugszinsen wurde mit Erkenntnis des BFG vom  28.2.2023, RV/1200014/2020 ebenso ersatzlos aufgehoben.

- missed: `Zollamtes Feldkirch Wolfurt` (organisation)
- predicted in sentence: `Zollamtes`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des **Finanzamtes Spittal  Villach** vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

- missed: `Finanzamtes Spittal  Villach` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_56`)

B) Rechtsprechung:  1. Zur Frage, ob ua. der frühestmögliche Studienbeginn im Sinne der angeführten Bestimmung  des § 2 Abs. 1 lit d FLAG 1967 gegeben ist, wenn ein beabsichtigt gewesenes Studium - zB  wegen bestehender Beschränkungen bei der Zulassung - nicht in dem Semester begonnen  wird, das unmittelbar nach dem Abschluss der Schulausbildung beginnt (im Beschwerdefall  wäre dies - nach Ablegung der Reifeprüfung im Juni 2018 – das im Herbst 2018 beginnende  Wintersemester 2018/19 gewesen), sondern dieses oder ein anderes Studium erst in einem  späteren Semester (hier: Sommersemester 2019) begonnen wird, gibt es eine inzwischen  gefestigte Rechtsprechung des VwGH und des Unabhängigen Finanzsenates (UFS) bzw. des  **Bundesfinanzgerichtes (BFG)**.

- missed: `Bundesfinanzgerichtes (BFG)` (organisation)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_61`)

Mangels Prüfungstermin der **WKO** konnte ich noch nicht zur Wiederholungsprüfung  antreten.

- missed: `WKO` (organisation)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_65`)

Der Erhalt bislang nicht erklärter Lohnzahlungen ergibt  sich zweifelsfrei aus dem Urteil des **Landesgerichtes** X, vom XX.X.2020, xx.

- missed: `Landesgerichtes` (organisation)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_70`)

Nach Auskunft des **Bundesministeriums für Finanzen** in gleichgelagerten Fällen ist der im  Signaturblock angegebene Tag im Allgemeinen jener Tag, an welchem der Bescheid in die  Databox eingebracht wurde, weil diese Einbringung in der Regel innerhalb einer Stunde ab  Erstellung der Amtssignatur erfolgt.

- missed: `Bundesministeriums für Finanzen` (organisation)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_12`)

Ein Abwickler wurde nicht bestellt.  6. Am 01.10.2020 wurde von der Bezirkshauptmannschaft Salzburg-Umgebung  über Ersuchen des Bundesfinanzgerichtes die vom  damaligen Vereinsobmann am 31. März 1951  unterzeichnete „Anzeige der freiwilligen  Vereinsauflösung (§ 28 Abs. 2 VerG)“ – eingebracht bei der **Bezirkshauptmannschaft Salzburg-Umgebung**  am 31. März 1951 –  übermittelt. Danach hatte der Verein am 23. August 1969  statutengemäß seine freiwillige  Auflösung mit Wirkung per 9. Februar 1989  beschlossen.

- missed: `Bezirkshauptmannschaft Salzburg-Umgebung` (organisation)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141488.1`) (sent_id: `deanon_BFG_20260814_TEST/141488.1_20`)

Das **Finanzamt Braunau Ried Schärding** wies diese Beschwerde mit  Beschwerdevorentscheidung vom 17. Mai 2016 als unbegründet zurück und führte es in der  Begründung im Wesentlichen aus, dass erst im Zuge eines Beschwerdeverfahrens betreffend  die GPLA-Prüfung Ende 2015/Anfang 2016 jene Tatsachen bekannt geworden seien, die zu der  angefochtenen Wiederaufnahme geführt hätten.

- missed: `Finanzamt Braunau Ried Schärding` (organisation)
- predicted in sentence: `Finanzamt`

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  **Magistrat der Stadt Wien, Magistratsabteilung 67**, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_17`)

In der Begründung führte das **Finanzamt**  für Gebühren, Verkehrsteuern und Glückspiel im Wesentlichen aus:  „Auf Grund des § 1 GebG 1957 unterliegen den Gebühren im Sinne des Gebührengesetzes ua.

- missed: `Finanzamt` (organisation)
- predicted in sentence: `Finanzamt  für Gebühren`

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_77`)

e) Bestätigung der Sozialversicherung v. Oktober 2012:  Demnach ist der Bf ab 22.10.2012 bei der **Fa.NiederImmobilien Institut GmbH** als Arbeiter/Hilfskraft vollbeschäftigt (=  40 Wochenstunden) und erhält einen Monatslohn von brutto € 1.513,60.

- missed: `Fa.NiederImmobilien Institut GmbH` (organisation)
- predicted in sentence: `NiederImmobilien Institut GmbH`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_16`)

Mit Schreiben vom 9.2.2024 teilte die belangte Behörde der Beschwerdeführerin mit, dass das  **Zollamt Österreich** beabsichtige, die Bescheidbeschwerde (vorbehaltlich einer Stellungnahme)  als unzulässig zurückzuweisen.

- missed: `Zollamt Österreich` (organisation)
- predicted in sentence: `Zollamt`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_78`)

Es ist somit ungewöhnlich, dass die Bf., bei der Frau B 100% beteiligt ist,  Aufträge an die **Mackwart und Reinink Automotive GmbH** vergibt, welche wiederum Arbeiter von der D GmbH, bei der Frau B  auch 100% beteiligt ist, zur Verfügung gestellt bekommt.

- missed: `Mackwart und Reinink Automotive GmbH` (organisation)
- predicted in sentence: `Reinink Automotive GmbH`, `D GmbH`

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des **Finanzamtes Wien 1/23** vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

- missed: `Finanzamtes Wien 1/23` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/142104.1`) (sent_id: `deanon_BFG_20260814_TEST/142104.1_59`)

Dieser  Fristverlängerungsantrag wurde laut Eingangsstempel jedoch tatsächlich erst am 17.12.2014  beim Infocenter des Finanzamtes **FA St. Johann Tamsweg Zell am See**  und somit nach Ablauf der bis zum 15.12.2014  erstreckten Rechtsmittelfrist zur Stellung des Vorlageantrags, daher verspätet eingebracht.

- missed: `FA St. Johann Tamsweg Zell am See` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_4`)

Darüber hinaus war er an der **Schifffahrtsgesellschaft S GmbH & Co KG** mit Sitz in H,  Deutschland, als Kommanditist beteiligt.

- missed: `Schifffahrtsgesellschaft S GmbH & Co KG` (organisation)
- predicted in sentence: `Schifffahrtsgesellschaft S GmbH`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_56`)

Anlagen oder elektronische Parkscheine zu verwenden (§ 1 der Verordnung, des **Wiener  Gemeinderates** über die Art der zu verwendenden Kontrolleinrichtungen in Kurzparkzonen,  kurz Kontrolleinrichtungenverordnung, ABI Nr 2013/29).

- missed: `Wiener  Gemeinderates` (organisation)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Dr. Katrin Allram in der Beschwerdesache  VetR Dipl. Kfm. Gernot Kurtius, Oberassling 20, 3921 Schmerbach, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des  **Finanzamtes Gänserndorf Mistelbach** vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Finanzamtes Gänserndorf Mistelbach` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/141488.1`) (sent_id: `deanon_BFG_20260814_TEST/141488.1_46`)

Die **Lump Bau GmbH**  verfügte in den Jahren 2012 und 2013 über einen BMW X5 xDrive 35 d E70  und einen BMW X6 M50d E71, die von der beschwerdeführenden Partei auch für Privatfahrten  genutzt wurden.

- missed: `Lump Bau GmbH` (organisation)
- predicted in sentence: `Die Lump Bau GmbH`

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  Basil Vanak, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des **Finanzamtes für Großbetriebe**, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

- missed: `Finanzamtes für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_146`)

Zusammengefasst ergibt sich aus der Anamnese, dass der Bf. laut eigenen Angaben die  Handelsakademie besuchte und anschließend BWL studierte (kein Abschluss) und an der  **Universität Wien** vom Sommersemester 1989 bis Wintersemester 1995 in der Studienrichtung  Soziologie, geisteswissenschaftliche Stzw Politikwissenschaft inskribiert war  (Studienzeitbestätigung der Universität Wien vom 28. Juli 2016).

- missed: `Universität Wien` (organisation)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_186`)

2. Berufliche/wirtschaftliche Nahebeziehung:  Fest steht nach dem Akteninhalt und bisher durchgeführten Erhebungen, dass der  Beschwerdeführer Sven Mitterhuber (Bf) ab 2009 im Inland berufstätig bzw. jedenfalls im strittigen  Zeitraum durchgehend bei der **Fa.NiederImmobilien Institut GmbH** in Vollzeit (42,5 Stunden/Woche) beschäftigt war  und laut Abfrage der Sozialversicherungsdaten nach wie vor ist.

- missed: `Fa.NiederImmobilien Institut GmbH` (organisation)
- predicted in sentence: `NiederImmobilien Institut GmbH`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Björn Augusto  in der Beschwerdesache Mona Reinhard,  Urschendorf 19, 4261 Kerschbaum, Österreich, vertreten durch IMMUNITAS Wirtschaftsprüfung GmbH, Schlickgasse 3 Tür 7,  1090 Wien, über die Beschwerde der beschwerdeführenden Partei vom 17.05.2022, beim  Bundesfinanzgericht eingelangt am 19.05.2022, wegen behaupteter Verletzung der  Entscheidungspflicht durch das **Finanzamt für Großbetriebe** betreffend Einkommen- und  Umsatzsteuer 2020 den Beschluss:   I. Das Säumnisbeschwerdeverfahren wird eingestellt.    II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Finanzamt für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamt`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/139407.1`) (sent_id: `deanon_BFG_20260814_TEST/139407.1_38`)

 Gegen die Einkommensteuerbescheide 2010 und 2011 des **Finanzamtes Wien 3/11  Schwechat Gerasdorf** vom 25. Mai 2012 hat Herr ursprünglicherBf kein Rechtsmittel  erhoben.

- missed: `Finanzamtes Wien 3/11  Schwechat Gerasdorf` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_11`)

In der am 4.4.2014 beim Finanzamt eingelangten Einkommensteuererklärung für 2012 erklärte  der Bf., dass die Beteiligung an der **S GmbH & Co KG** nicht mehr vorhanden sei.

- missed: `S GmbH & Co KG` (organisation)
- predicted in sentence: `Finanzamt`, `S GmbH`

</details>

---

