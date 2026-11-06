# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-10-19T09:04:35.167751

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-10-19_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 50 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 40 |
| Validation documents | 10 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 625 |
| Validation sentences | 363 |
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
| Accuracy (exact match) | 97.4% |
| True Positives | 10343 |
| False Positives | 1020 |
| False Negatives | 1405 |
| Total Gold Entities | 11748 |
| Micro Precision | 91.0% |
| Micro Recall | 88.0% |
| Micro F1 | 89.5% |
| Macro F1 | 89.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Special Agencies` | 0.6% | 100.0% | 0.3% | 38 | 38 | 0 |
| `Municipal Councils` | 0.5% | 100.0% | 0.3% | 30 | 30 | 0 |
| `Tax Offices Extended` | 0.0% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Pensionsversicherungsanstalt` | 0.4% | 100.0% | 0.2% | 21 | 21 | 0 |
| `Police and Local Courts` | 0.7% | 100.0% | 0.4% | 44 | 44 | 0 |
| `Courts with Article` | 60.0% | 99.9% | 42.9% | 5042 | 5038 | 4 |
| `Acronyms AMS BMF BFG` | 24.5% | 98.2% | 14.0% | 1675 | 1645 | 30 |
| `Universities and Health Funds` | 0.5% | 96.6% | 0.2% | 29 | 28 | 1 |
| `Tax Offices` | 39.2% | 93.1% | 24.9% | 3137 | 2920 | 217 |
| `Municipal Authorities` | 5.4% | 67.2% | 2.8% | 488 | 328 | 160 |
| `European Institutions` | 0.1% | 33.3% | 0.0% | 9 | 3 | 6 |
| `Companies with Legal Form` | 3.7% | 32.5% | 1.9% | 704 | 229 | 475 |
| `Social Ministries/Offices` | 0.3% | 21.2% | 0.1% | 80 | 17 | 63 |
| `Ministers/Departments` | 0.0% | 0.0% | 0.0% | 64 | 0 | 64 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Special Agencies` 🏆

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e52810b2`  
**Description:**
Matches specific agency names like Finanzpolizei and Amt für Betrugsbekämpfung which are not covered by general patterns.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(Finanzpolizei|Amt\s+für\s+Betrugsbekämpfung)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 38 | 38 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 38 | 0 | 11710 |

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

- `Bundesfinanzgericht` (organisation)
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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Dipl.-Ing. Heinz Riechels` (person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

</details>

---

## `Municipal Councils` 🏆

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `f9538832`  
**Description:**
Matches Wiener Gemeinderat and its genitive form Wiener Gemeinderates.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:des|dem|der|vom|von\s+der|der\s+)?\s*(Wiener\s+Gemeinderat(?:es)?)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.005 | 30 | 30 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 30 | 0 | 11718 |

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

## `Tax Offices Extended` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `895c18c7`  
**Description:**
Matches 'FA Linz' abbreviation variations, handling genitive cases and surrounding punctuation.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(FA\s+Linz(?:es)?)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 11746 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Basil Eberhards` (person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139879.1`) (sent_id: `deanon_BFG_20260814_TEST/139879.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Giacomello  in der Beschwerdesache Natascha Theys vertreten  durch StB über die Beschwerde vom 3. Oktober 2022 gegen den Bescheid des FA Linz  vom  9. September 2022 über die Festsetzung eines ersten Säumniszuschlages (Steuernummer  86-989/6915 ) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Wilfried Giacomello` (person)
- `Natascha Theys` (person)
- `86-989/6915` (tax_number)

</details>

---

## `Pensionsversicherungsanstalt` 🏆

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `92c1c404`  
**Description:**
Matches Pensionsversicherungsanstalt in various cases (nominative, genitive, dative).

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(Pensionsversicherungsanstalt(?:s)?)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 11727 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_128`)


Lebensjahres seit 01.11.2016 die  Korridorpension von der österreichischen Pensionsversicherungsanstalt.   8 von 9 Seite 9 von 9

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `Police and Local Courts` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `fd0f10e7`  
**Description:**
Matches specific police and local court bodies like Landespolizeidirektion Wien and Verwaltungsgericht Wien.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(Landespolizeidirektion\s+Wien|Verwaltungsgericht\s+Wien)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 44 | 44 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 44 | 0 | 11704 |

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

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_38`)


In der am 17. Juni 2020 durchgeführten mündlichen Verhandlung vor dem  Bundesfinanzgericht wurde das Kontrollorgan der MA 67 der Landespolizeidirektion Wien als  Zeuge vernommen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

- `Verwaltungsgerichtshofes` (organisation)
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

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

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

## `Courts with Article` 🏆

**F1:** 0.600 | **Precision:** 0.999 | **Recall:** 0.429  

**Format:** `regex`  
**Rule ID:** `2dbe4c73`  
**Description:**
Matches court names (Bundesfinanzgericht, Verwaltungsgerichtshof, Verfassungsgerichtshof, Oberster Gerichtshof) with or without preceding articles, handling genitive cases and standalone mentions.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|an\s+den|vom|von\s+der|der\s+)?\s*(Bundesfinanzgericht(?:es)?(?:\s*\(BFG\))?|Verwaltungsgerichtshof(?:es)?|Verfassungsgerichtshof(?:es)?|Oberster\s+Gerichtshof(?:es)?)\s*(?:\(BFG\))?\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.999 | 0.429 | 0.600 | 5042 | 5038 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5038 | 4 | 6710 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist gem. Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_7`)


Der Bf. beantragte daraufhin die Vorlage der Beschwerde an das Bundesfinanzgericht und die Durchführung einer mündlichen Verhandlung (Vorlageantrag vom 23. Juni 2015).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_8`)


Seite 2 von 3 Das FA legte das Rechtsmittel und diverse Aktenteile am 8. Juli 2015 elektronisch an das Bundesfinanzgericht vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_9`)


Mit 9. November 2015 erließ das Bundesfinanzgericht einen Mängelbehebungsauftrag, dem der Bf. mit Schreiben vom 30. November 2015 nachkam.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_22`)


Das Bundesfinanzgericht erlaubt sich den Hinweis, dass für die Aussetzung von Anspruchszinsen (§ 212a BAO) abgesehen von den sonstigen Voraussetzungen keine Beschwerde gegen den Anspruchszinsenbescheid selbst, sondern - da der Anspruchszinsenbescheid vom jeweiligen Einkommensteuerbescheid abhängt – nur eine Beschwerde gegen den zugrunde liegenden Einkommensteuerbescheid erforderlich ist (Ritz, BAO  5  , § 205 Tz 36 und § 212a Tz 7 unter Hinweis auf VwGH 27.3.2008, 2008/13/0036).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_25`)


Gegen ein Erkenntnis des Verwaltungsgerichtes ist eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird (Art. 133 Abs. 4 B-VG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Dr. Heinz Neuner` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_62`)


------ Mit Vorhalt des Bundesfinanzgerichtes vom 9.4.2019 wurde der Beschuldigte  aufgefordert, die Mittelherkunft der behaupteter Weise von ihm in den Jahren 2012 und Seite 6 von 21 2013 geleisteten Barzahlungen an die Subfirmen X. mit Sitz in L.,Furtder Technologien GmbH und NEP Lebensmittel GmbH anhand vorzulegender Kopien sämtlicher Kontenbewegungen oder anhand anderer geeigneter Unterlagen nachzuweisen bzw. glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Furtder Technologien GmbH` (organisation)
- `NEP Lebensmittel GmbH` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_85`)


Ich werde - so mir dies möglich ist - zur noch anzuberaumenden mündlichen Verhandlung vor dem Bundesfinanzgericht auch eine Bestätigung der Wiener Gebietskrankenkasse mitnehmen, aus der die Anzahl der bei mir in den Jahren 2012 und 2013 durchschnittlich beschäftigten Mitarbeiter ersichtlich ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Wiener Gebietskrankenkasse` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_108`)


------- In der mündlichen Verhandlung vor dem Senat des Bundesfinanzgerichtes führte der Beschuldigte ergänzend aus, er sei derzeit Angestellter einer Parkettbodenfirma und sein monatliches Nettogehalt betrage € 1.454,00, davon würden etwas mehr als € 300,00 für Zahlungen aufgrund Privatkonkurses einbehalten und abgeführt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_130`)


Auf den Vorhalt, im Rahmen der GPLA-Prüfungen vom 2.11.2017 für den Zeitraum 1.1.2012 bis 31.12.2014 und vom 14.12.2017 für den Zeitraum 1.1.2015 bis 9.11.2017 seien für das gegenständliche Verfahren relevante Abfuhrdifferenzen an lohnabhängigen Abgaben in Höhe von insgesamt € 5.821,93 festgestellt worden, wobei es sich dabei um auf den Lohnkonten selbst berechnete Beträge, die von ihm  nicht ans Finanzamt abgeführt wurden, handelte, führte der Beschuldigte in der mündlichen Verhandlung vor dem Bundesfinanzgericht aus: Die Abfuhrdifferenzen könne er sich überhaupt nicht erklären, die Lohnverrechnung sei durch den Steuerberater durchgeführt worden und alle Erlagscheine, die ihm von diesem übermittelt worden seien, habe er auch an das Seite 12 von 21 Finanzamt bezahlt. Er habe in diesem Zeitraum keine finanziellen Probleme gehabt und sei seinen Zahlungspflichten regelmäßig nachkommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_200`)


Vorsätzliches Handeln beruht nach ständiger Rechtsprechung des Verwaltungsgerichtshofes zwar auf einem nach außen nicht erkennbaren Willensvorgang, ist aber aus dem nach außen in Erscheinung tretenden Verhalten des Täters zu erschließen, wobei sich die diesbezüglichen Schlussfolgerungen als Ausfluss der freien Beweiswürdigung erweisen (VwGH 28.11.2007, 2007/15/0165).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_206`)


Seite 18 von 21 Keine der Verfahrensparteien konnte - trotz Aufforderung in der mündlichen Verhandlung vor dem Bundesfinanzgericht - Personen als Zeugen namhaft machen, die Aussage darüber treffen hätten können, von wem (von welchen Arbeitern) in wessen Auftrag die hier in Rede stehenden Leistungen der drei genannten Subfirmen tatsächlich erbracht wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_212`)


Nach Ansicht des Bundesfinanzgerichtes kann im gegenständlichen Fall, aufgrund der vorliegenden Beweisergebnisse und der gegenüber dem Abgabenverfahren geänderten Beweislast, schon in objektiver Hinsicht nicht mit der für ein Finanzstrafverfahren erforderlichen Sicherheit der Nachweis der angeschuldigten Abgabenhinterziehung gemäß § 33 Abs. 1 FinStrG an Einkommensteuer 2012 und 2013 sowie der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG betreffend Nichtabfuhr von lohnabhängigen Abgaben (L, DB, DZ) 1/2012-09/2017 für schwarz beschäftigte (bei der Sozialversicherung nicht angemeldete) Dienstnehmer mit der für ein Finanzstrafverfahren erforderlichen Sicherheit erbracht werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_220`)


Zweifelsfrei kannte der Beschuldigte seine diesbezüglichen Entrichtungs- bzw. Meldepflichten zu den jeweiligen gesetzlichen Fälligkeitstagen und er hat sich vor dem Bundesfinanzgericht dahingehend gerechtfertigt, sämtliche von seinem Steuerberater monatlich berechneten und ihm bekanntgegebenen Lohnabgaben auch entrichtet zu haben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_195`)


Seite 15 von 23 Gemäß § 323 Abs. 38 Bundesabgabenordnung (BAO, idF des FVwGG 2012, BGBl. I 2013/14 ab 1.1.2014) sind die am 31. Dezember 2013 bei dem unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen Berufungen vom Bundesfinanzgericht als Beschwerde im Sinne des Art. 130 Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_273`)


Der Berechnung der fiktiven Anschaffungskosten im ersten Gutachten kann das Bundesfinanzgericht - unter Heranziehung der vorstehenden Rechtsprechung - nicht folgen, da in diesem Gutachten der Herstellungswert für Versicherungszwecken herangezogen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_283`)


Das Bundesfinanzgericht kann daher auch anhand dieses Gutachtens nicht die kürzere Nutzungsdauer für die Ru. von ca. 40 Jahre und für die Pf. von maximal 15 Jahre erkennen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_287`)


Das Bundesfinanzgericht kann unter Heranziehung der im Akt aufliegenden Unterlagen, auch der angeführten anderen Nutzungsdauern (42 Jahre) und den Zinssätze, die der nunmehrigen Berechnungen zugrunde gelegt wurde, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_297`)


Das Bundesfinanzgericht geht daher von einer Nutzungsdauer jährlich von 2 % aus, da die Liegenschaft (vorwiegend) bereits vor 1920 errichtet worden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_298`)


Eine kürzere Nutzungsdauer kann das Bundesfinanzgericht auf Grund der vorgelegten Gutachten nicht erkennen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_314`)


Das Bundesfinanzgericht teilt den von der belangten Behörde und im 2.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_319`)


Das Bundesfinanzgericht kommt auf Grund der nachfolgenden Berechnung zu der anerkannten AfA: Nutzungsdauer 50 Jahre AfA 2%

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_325`)


Zulässigkeit einer Revision Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des Verwaltungsgerichts- hofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_327`)


Das Bundesfinanzgericht orientiert sich bei den zu lösenden Rechtsfragen an der einheitlichen höchstgerichtlichen Judikatur, darüber hinaus hing die Entscheidung im Wesentlichen von den Umständen des Einzelfalles sowie auf der Ebene der Beweiswürdigung zu beantwortenden Sachfragen ab.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_328`)


Die Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Alexander Schnelldorfer` (person)
- `Finanzamt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_4`)


Die im Kalenderjahr 2008 erzielten Einkünfte werden gemäß § 188 BAO wie folgt festgestellt: [...] III.  Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4 B-VG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_15`)


4.     Gemäß § 323 Abs. 38 BAO sind die am 31. Dezember 2013 beim Unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz anhängigen Berufungen vom Bundesfinanzgericht als Beschwerden im Sinne des Art. 130 Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_16`)


Solche Verfahren betreffende Anbringen wirken mit 1. Jänner 2014 auch gegenüber dem Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_17`)


5.     Die Beschwerde (Berufung) war beim Bundesfinanzgericht unter GZ. RV/3100022/2011 der Geschäftsabteilung 4004 zugeordnet, wurde dieser mit Verfügung des Geschäftsverteilungsausschusses vom 18. Februar 2019 abgenommen und mit Wirkung vom 6. März 2019 der Geschäftsabteilung 4019 zugeteilt. 6.     Die steuerliche Vertretung der Beschwerdeführerin hat mit Schreiben vom 09.10.2019 mitgeteilt, dass der Antrag auf Entscheidung durch den gesamten Senat und der Antrag auf Durchführung einer mündlichen Verhandlung zurückgezogen wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_18`)


II.   Sachverhalt Seite 3 von 7 Folgender Sachverhalt ist für das Bundesfinanzgericht entscheidungswesentlich und erwiesen: 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_47`)


Mit Vorhalt vom 18.04.2019 hat das Bundesfinanzgericht die Beschwerdeführerin unter anderem aufgefordert, nachweislich den Mittelpunkt der Lebensinteressen für die unter Punkt II.9. genannten Personen sowie die tatsächliche Nutzung der Liegenschaft EZ*01 zu belegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_50`)


Somit geht auch das Bundesfinanzgericht davon aus, dass das Einfamilienhaus an der Adresse*** von D, G und E zwischen Oktober 2005 und April 2008 tatsächlich für Wohnzwecke genutzt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_90`)


Für das Bundesfinanzgericht steht fest, dass die Liegenschaft EZ*01 im Jahr 2008 nicht Betriebsvermögen der Beschwerdeführerin war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_97`)


Die Ansicht der Abgabenbehörde, die Liegenschaft habe "durch das kurzfristige Bewohnen […] nicht den Charakter als Betriebsvermögen verloren", teilt das Bundesfinanzgericht nicht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_107`)


V.     Zulässigkeit einer Revision Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_108`)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_110`)


Die ordentliche Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_111`)


Zur außerordentlichen Revision an den Verwaltungsgerichtshof siehe nachstehende Rechtsbelehrung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_42`)


-------- Die gegenständliche Beschwerde vom 16.01.2017 wurde dem Bundesfinanzgericht am 05.11.2019 zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_47`)


Überzeugt sich das Bundesfinanzgericht aus Anlass der Beschwerde, dass zum Nachteil eines anderen Beschuldigten oder Nebenbeteiligten, welcher keine Beschwerde eingebracht hat, das Gesetz unrichtig angewendet wurde, so hat es so vorzugehen, als wäre auch von diesen Personen eine Beschwerde eingebracht worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_57`)


Da dem angefochtenen Erkenntnis eine im Zeitpunkt der Erlassung des angefochtenen Erkenntnisses nicht mehr strafbare fahrlässige Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zugrunde gelegt wurde und dem Bundesfinanzgericht gemäß § 161 Abs. 3 FinStrG  eine strengere Qualifikation des Handelns des Bf. als grob fahrlässige Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG (BGBl. I Nr. 118/2015 ab 1.1.2016) bei zugunsten des Bf. eingebrachter Beschwerde rechtlich verwehrt ist (Verböserungsverbot), war das angefochtene Erkenntnis wegen inhaltlicher Rechtswidrigkeit aufzuheben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_60`)


Zur Unzulässigkeit der ordentlichen Revision Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_3`)


Begründung  Zunächst ist festzuhalten:   Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichtes (BFG) vom  11.10.2019 wurde der streitgegenständliche Fall, der ursprünglich der Gerichtsabteilung 7005  des BFG zugeteilt war, nunmehr der Gerichtsabteilung 7019 des BFG zugeteilt. Damit bestand  für die nun zuständige Gerichtsabteilung 7019 des BFG erst ab 14.10.2019 (Inkrafttretung der  Umverteilung) die Möglichkeit, das streitgegenständliche Verfahren abzuführen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes (BFG)` | `Bundesfinanzgerichtes (BFG)` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)
- `BFG` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_10`)


Die Bf brachte am 23.08.2018 den Antrag ein, die Beschwerde dem Bundesfinanzgericht (BFG)  zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht (BFG)` | `Bundesfinanzgericht (BFG)` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_52`)


Erst am 23.08.2018 brachte die Bf den Antrag ein, die Beschwerde dem Bundesfinanzgericht  (BVE) zur Entscheidung vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_18`)


Mit am 31.5.2017 bei der belangten Behörde eingelangtem Sch reiben wurde vom  Parteienvertreter beantragt, die oa Beschwerde dem Bundesfinanzgericht zur Entscheidung  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_23`)


Am 9.6.2017 erfolgte durch die belangte Behörde die Vorlage der gegenständlichen Beschwerde  an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_24`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_38`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen  gemäß § 167 Abs 2 BAO als erwiesen annehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_70`)


Wie der Verwaltungsgerichtshof ausgesprochen hat, steht der  Abgabenbehörde sowohl bei der Frage der Zuschlagsfestsetzung dem Grunde nach als auch bei  der Festlegung des Ausmaßes des Verspätungszuschlages Ermessen zu (vgl zB VwGH 12.8.2002,  98/17/0292;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_90`)


Unter Berücksichtigung aller oben angeführter Umstände erachtet das Bundesfinanzgericht die  Berechnung des Verspätungszuschlages mit 2% des Vorauszahlungsbetrages als angemessen  (vgl zB auch BFG 27.2.2014, RV/2100455/2012).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_94`)


Gegen eine Entscheidung des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 B-VG die Revision  zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine s olche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_96`)


Mit dem vorliegenden Erkenntnis weicht das Bundesfinanzgericht nicht von der Rechtsprechung  des Verwaltungsgerichtshofes ab, sondern folgt insbesondere dem Erkenntnis des VwGH vom  25.6.2007, 2006/14/0054, weshalb gemäß § 25a Abs 1 VwGG spruchgemäß zu entscheiden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht (BFG)` | `Bundesfinanzgericht (BFG)` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_10`)


Das Bundesfinanzgericht hat erwogen:  I. Unstrittig ist nach den abgabenbehördlichen Verfahrensunterlagen, dass der Bf zumindest ab  April 2012 und im Jahr 2013 ganzjährig ein Imbisslokal in Form eines Kebab-Standes betrieb,  dessen Gewinnermittlung weder durch Betriebsvermögensvergleich zu erfolgen hatte, noch  auf diese Weise erfolgte und dessen Jahresumsatz iSd § 125 BAO unter 255.000,- € lag.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_74`)


Zulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Ophelia Dutschka` (person)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_67`)


III. Das Bundesfinanzgericht hat erwogen:  1. Rechtslage

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_133`)


3. Zur Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  9 von 10 Seite 10 von 10

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_134`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Gabriele Grossgut-Palotás` (person)
- `Lewis Rzehula` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_13`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_68`)


Das Bundesfinanzgericht verkennt nicht, dass die besuchten Seminare auch geeignet waren,  die beruflichen Kenntnisse und Fertigkeiten des Beschwerdeführers zu verbessern;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_75`)


Seitens des Bundesfinanzgerichtes wird nicht in Abrede gestellt, dass die besuchten Seminare  einen positiven Effekt auf die berufliche Tätigkeit des Beschwerdeführers hatten;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_77`)


Dass der Besuch von Seminaren zur  Kommunikationsverbesserung im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den  Bereich der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof  wiederholt bejaht (zB VwGH 29.1.2004, 2000/15/0009;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_81`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_83`)


Zum  § 16 liegt eine einheitliche Rechtsprechung des Verwaltungsgerichtshofes vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Dr. Kurt Bartold` (person)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_3`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_9`)


Das Bundesfinanzgericht hat erwogen:  In seinem Erkenntnis RV/2100723/2018 vom 6.9.2018 gelangte das BFG unter Hinweis auf  § 295 Abs. 4 iVm. § 304 BAO (zunächst) zu dem Schluss, der am 9.12.2014 eingebrachte Antrag  sei nach dem klaren Gesetzeswortlaut erst nach Eintritt der Verjährung – und damit verspätet -  eingebracht worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_25`)


Ist ein Gesetz wegen Verfassungswidrigkeit aufgehoben worden oder hat der  Verfassungsgerichtshof gemäß Art. 140 B-VG Abs. 4 ausgesprochen, dass ein Gesetz  verfassungswidrig war, so sind alle Gerichte und Verwaltungsbehörden an den Spruch des  Verfassungsgerichtshofes gebunden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_26`)


Auf die vor der Aufhebung verwirklichten Tatbestände  mit Ausnahme des Anlassfalles ist jedoch das Gesetz weiterhin anzuwenden, sofern der  Verfassungsgerichtshof nicht in seinem aufhebenden Erkenntnis anderes ausspricht (Art. 140  Abs. 7 B-VG).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_36`)


Zur Revision:   Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_4`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht (BFG)` | `Bundesfinanzgericht (BFG)` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_111`)


IV. Rechtslage:  Gemäß § 323 Abs. 38 Bundesabgabenordnung (BAO), BGBl 1961/194 idgF., sind die am 31.  Dezember 2013 beim Unabhängigen Finanzsenat als Abgabenbehörde zweiter Instanz  anhängigen Berufungen vom Bundesfinanzgericht als Beschwerden im Sinne des Art. 130  Abs. 1 B-VG zu erledigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_124`)


V. Erwägungen:  1. Dauernder Standort, widerrechtliche Verwendung:   Nach der Judikatur des Verwaltungsgerichtshofes (siehe zB Erkenntnis 21.5.1996, 95/11/0378)  ist das Lenken von im Ausland zugelassenen Kraftfahrzeugen (und zwar in einem der  Mitgliedsstaaten eines der in § 82 Abs. 1 KFG 1967 genannten internationalen  Übereinkommen) nach Maßgabe des § 82 KFG 1967 erlaubt, also ohne dauernden Standort in  Österreich bis zu einer Höchstdauer von 1 Jahr (§ 79 Abs. 1 KFG).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_167`)


Unzulässigkeit einer Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_2`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_156`)


Am 17.6.2020 fand vor dem Bundesfinanzgericht die beantragte mündliche Verhandlung  statt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_157`)


Das Bundesfinanzgericht hat erwogen:  Die Bf. betrieb in den Streitjahren eine Bar in der A-Gasse 8 in G mit vier (im Obergeschoß  befindlichen) Zimmern.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_169`)


Der Verwaltungsgerichtshof hat jedoch bereits mehrfach zum Ausdruck gebracht hat, dass bei  einem Barbetrieb mit angeschlossenen Separees (bzw. Zimmern) die Leistung des  Barbetreibers nach der Kundenerwartung nicht nur im Getränkeausschank, sondern  entscheidend auch in der Gelegenheit zum Separee-Besuch besteht.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_240`)


Zur Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

## `Acronyms AMS BMF BFG` 🏆

**F1:** 0.245 | **Precision:** 0.982 | **Recall:** 0.140  

**Format:** `regex`  
**Rule ID:** `4eeae7f0`  
**Description:**
Matches 'BFH' (Bundesfinanzhof) and 'BFG' in legal contexts, handling possessive forms and surrounding punctuation.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(BFH|BFG|AMS|BMF)(?:\s*(?:Erkenntnis|Vorhalt|Bescheid|RV/|\d+|\.[0-9]{2}\.[0-9]{2}\.[0-9]{4}|/|\s|$|[^a-zA-Z])|\s*(?:des|dem|der|vom|von)\s+|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.982 | 0.140 | 0.245 | 1675 | 1645 | 30 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1645 | 30 | 10103 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_3`)


Begründung  Zunächst ist festzuhalten:   Mit Verfügung des Geschäftsverteilungsausschusses des Bundesfinanzgerichtes (BFG) vom  11.10.2019 wurde der streitgegenständliche Fall, der ursprünglich der Gerichtsabteilung 7005  des BFG zugeteilt war, nunmehr der Gerichtsabteilung 7019 des BFG zugeteilt. Damit bestand  für die nun zuständige Gerichtsabteilung 7019 des BFG erst ab 14.10.2019 (Inkrafttretung der  Umverteilung) die Möglichkeit, das streitgegenständliche Verfahren abzuführen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes (BFG)` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_90`)


Unter Berücksichtigung aller oben angeführter Umstände erachtet das Bundesfinanzgericht die  Berechnung des Verspätungszuschlages mit 2% des Vorauszahlungsbetrages als angemessen  (vgl zB auch BFG 27.2.2014, RV/2100455/2012).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_11`)


Nach den Angaben in den Abgabenerklärungen des Bf wurde der Gewinn dieses Betriebes  sowohl für das Jahr 2012 als auch für 2013 durch Pauschalierung ermittelt.   Im Zuge einer abgabenbehördlichen Außenprüfung (AP) für 2012/2013 wurde die  Gewinnermittlungsart für 2012 (BFG-Anmerkung: nach der  GaststättenpauschalierungsVO 1999) nicht beanstandet, eine Gewinnermittlung für 2013 nach  der GastgewerbepauschVO 2013 wurde dagegen als unzulässig erachtet (AP-Bericht 28.9.2015,  Tz 1 u. Tz 3).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_16`)


Hervorhebungen durch das BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_20`)


„Gastgewerbe in der Betriebsart "Imbiss" gemäß § 94 Z. 26 GewO 1994 mit der Berechtigung  gemäß § 111 Abs. 1 Z. 2 Gew0 1994, wobei ein Befähigungsnachweis gem. § 19 GewO 1994  erbracht wurde.“ (Hervorhebungen durch das BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_25`)


Entsprechend geht das BFG davon  aus, dass die Erbringung des Befähigungsnachweises (§ 19 GewO 1994) gegenüber der  Gewerbebehörde im Zuge der Zurücklegung und Neuvergabe der Gewerbeberechtigung im  Sept.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_27`)


II. Nach § 17 Abs. 1 und Abs. 4 EStG können bei den Einkünften aus einer Tätigkeit im Sinne der  §§ 22 und 23 EStG die Betriebsausgaben im Rahmen der Gewinnermittlung gemäß § 4  Abs. 3 EStG mit einem Durchschnittssatz ermittelt werden, wobei mit BMF-Verordnung  Durchschnittssätze für Gruppen von Steuerpflichtigen auf Grund von Erfahrungen über deren  wirtschaftliche Verhältnisse festzusetzen sind.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_36`)


Unbeschadet allfälliger  Ausübungsvorschriften ist für diese kein Befähigungsnachweis zu erbringen.“  § 111 GewO 1994 hatte im Jahr 2013 – soweit verfahrensrelevant – folgende Fassungen  (Hervorhebung durch das BFG):  1.Jänner bis 28.Mai 2013 (BGBl. I Nr. 42/2008):  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_112`)


Die KG/OG als  Eigentümerin der Grundstücke (dokumentiert im Grundbuch) ist eine von den Gesellschaftern  zu unterscheidende und selbständige Rechtspersönlichkeit, dh. der Erwerb der  Liegenschaften durch den verbleibenden Gesellschafter im Zuge der Anwachsung nach § 142  UGB erfolgte nicht vom ausscheidenden Gesellschafter der KG/OG, sondern vielmehr von  Seiten der KG/OG als eigenständigem Rechtsträger (vgl. BFG 16.10.2014, RV/6100226/2008).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_6`)


Strittig war vor dem BFG, ob dieser Antrag fristgerecht eingebracht wurde oder nicht.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_9`)


Das Bundesfinanzgericht hat erwogen:  In seinem Erkenntnis RV/2100723/2018 vom 6.9.2018 gelangte das BFG unter Hinweis auf  § 295 Abs. 4 iVm. § 304 BAO (zunächst) zu dem Schluss, der am 9.12.2014 eingebrachte Antrag  sei nach dem klaren Gesetzeswortlaut erst nach Eintritt der Verjährung – und damit verspätet -  eingebracht worden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_27`)


Der VwGH hob in der Folge das BFG-Erkenntnis vom 6.9.2018, RV/2100723/2018, – unter  Verweis auf VfGH vom 4.12.2019, G 159/2019 ua. - mit Entscheidung vom 18.5.2020,  Ra 2018/15/0121, auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_29`)


Das BFG habe – so der VwGH – das angefochtene Erkenntnis  auf die aufgehobene Gesetzesbestimmung gestützt, die im Revisionsfall nicht (mehr)  anzuwenden sei.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_31`)


Nach § 279 Abs.1 BAO hat eine Aufhebung durch das BFG ua. zu erfolgen, wenn ein  verfahrensrechtlicher Bescheid (zB Zurückweisung eines Antrages) zu Unrecht erlassen wurde  (Ritz, BAO 6.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_37`)


Da das BFG auf Grund der oa. VfGH- bzw. VwGH-Judikatur spruchgemäß zu entscheiden hatte,  liegt keine Rechtsfrage iSd. Art. 133 Abs. 4 B-VG vor.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_71`)


3) BFG-Vorhaltschreiben vom 13.12.2019 an die Bf wie folgt:  "Im anhängigen Berufungs- bzw. nunmehr Beschwerdeverfahren ist im Wesentlichen strittig,  wer als "Steuerschuldner" in Betracht komme und wo sich der "dauernde Standort" des  Fahrzeuges Range Rover Sport befunden habe.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_86`)


In Beantwortung eines Urgenzschreibens des BFG hat der Rechtsvertreter nun letztlich im  Schreiben vom 1.7.2020 mitgeteilt, dass bislang keine Antwort der Bf bzw. beider Ehegatten Bf  vorliege und er mangels Kontakt zugleich mit beiliegendem, an die Bf (unter der eruierten  deutschen Adresse des Ehegatten) gerichteten Schreiben seine Vertretungs- und  Zustellvollmacht aufgekündigt hat.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_130`)


Festzuhalten ist, dass eine diesbezüglich ausführliche Anfrage mit BFG-Vorhaltschreiben zur  weiteren Sachverhaltsabklärung trotz langwieriger und vielfacher Versuche durch den  Rechtsvertreter zwecks Beantwortung ohne Ergebnis geblieben ist.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_154`)


Abgesehen davon, dass im Gegenstandsfalle die Leasinggeberin Eigentümerin und  Zulassungsbesitzerin des Fahrzeuges ist, welchen Umständen wie auch der Frage nach dem  rechtmäßigen Besitzer oder auf wen die Zulassung im Inland erfolgen könnte aber nach  Obigem keine ausschlaggebende Bedeutung zukommt, kann nach dem Dafürhalten des BFG  die Bf nicht als Verwenderin im Sinne der "Halterin" des Fahrzeuges qualifiziert werden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_159`)


Nach dem Dafürhalten des BFG kann nahezu  ausgeschlossen werden, dass die Bf von ihrem Haushaltsgeld allein rund € 700 an mtl.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_121`)


5)Entgelt für Zimmer:  Die Leistung besteht in der Ermöglichung der Ausübung der Prostitution in einem behördlich  bewilligten Bordellbetrieb.“  (4) Mit Ergänzungsersuchen vom 11.3.2020 brachte das BFG der Bf. die Stellungnahme des  Prüfers zur Kenntnis und ersuchte um Übermittlung der behördlichen Bewilligung nach den §§  4 des Stmk.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_164`)


Wir sind auch die beste Adresse für Transsexuelle! (…)“ (s. zB den vom  Prüfer seiner Stellungnahme zur Beschwerde beigelegten Ausdruck aus dem Sexmagazin vom  5.5.2017, welcher der Bf. vom BFG zur Stellungnahme übermittelt wurde).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_194`)


s. Beschwerde S. 5f. sowie  Vorbringen in der mündlichen Verhandlung vom 17.6.2020) nach Meinung des BFG jedenfalls  ein weiteres – hier jedoch letztlich nicht mehr entscheidungsrelevantes - Indiz dafür darstellt,  dass die Prostitutionserlöse der Bf. zuzurechnen sind.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_200`)


Letztlich  ändert aber auch ein Inkasso durch die Prostituierten bei Vorliegen eines Bordellbetriebes an  der Zurechnung des Gesamtentgeltes an die Bordellbetreiberin nichts (zB VwGH 20.5.2010,  2006/15/0290; in diesem Sinne auch etwa BFG 13.8.2019, RV/2100289/2018, uva.).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_226`)


Dies begründet  notwendig eine funktionelle Verknüpfung zwischen dem Bordellbetrieb und den  Sexualdienstleistungen und geht zugleich hinsichtlich jener (dem Bordell zugeordneten)  Räumlichkeiten, in welchen die Sexualdienstleistungen erbracht werden, weit über den  Rahmen einer bloßen „Wohnraummiete“ hinaus (so zB BFG 13.8.2019, RV/2100289/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_241`)


Das BFG konnte sich im vorliegenden Fall auf zahlreiche – oben zitierte – Erkenntnisse des  VwGH stützen, und zwar sowohl hinsichtlich der Zurechnung der Umsätze an die Bf. (als  Bordellbetreiberin) als auch der Besteuerung der Umsätze mit 20%.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_94`)


Die Wartefrist für den neuerlichen Bezug der Familienbeihilfe beträgt daher soviele Semester  wie in dem zuvor betriebenen Studium verbracht wurden (BFG vom 27.2.2019, RV/6100043),  somit im gegenständlichen Fall drei Semester.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_15`)


Eine Gegenverrechnung der Pflegekosten mit  Vermögenswerten (Wohnung der Ehegattin) sei von Erlässen des BMF nicht gedeckt.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_20`)


Verfügt etwa eine pflegebedürftige Person über kein ausreichendes Einkommen zur  Begleichung aller Pflegekosten, ist aber Eigentümer einer Liegenschaft (Wohnung) und trägt ein  Angehöriger einen Teil der Pflegekosten, ist nach Ansicht des BMF auf „verwertbares  Vermögen" beim Pflegebedürftigen abzustellen.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_82`)


BFG 20.4.2017, RV/2100808/2015;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_83`)


BFG 20.4.2017, RV/2100808/2015).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_25`)


In Zweifelsfällen ist anhand  objektiver, äußerer Merkmale und Umstände darzulegen, dass die geplante Tätigkeit die  Kriterien einer selbständig ausgeübten gewerblichen oder beruflichen Tätigkeit erfüllt (BFH  8.3.2001, V R 24/98;

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_26`)


BFH 22.3.2001, V R 46/00).

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_30`)


Das Finanzamt hat ausgehend von diesen  Unterlagen eine „Auswertung Fahrplan – Dienstzeit“ erstellt und dem BFG vorgelegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_31`)


Abgabenverkürzung nach § 4 Parkometergesetz 2006 verwirklicht, die objektive Tatseite ist  daher gegeben (vgl. BFG 18.8.2015, RV/7500838/2015).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_167`)


Im umgekehrten Fall - wenn also die Bestätigung der Buchung innerhalb dieser  Zeitspanne von einer Minute vor der Abfrage des Kontrollorgans erfolgt - würde dieses die  Meldung mit den Daten des gebuchten Parkscheines erhalten (vgl. BFG 09.01.2019,  RV/7501078/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_174`)


Mit dem Entfernen vom Fahrzeug gibt der Lenker klar zu verstehen, dass aus seiner Sicht die  Phase des Abstellens, die zur Abgabenentrichtung zur Verfügung steht, beendet ist und er den  Vorgang des Einparkens für abgeschlossen erachtet (vgl BFG 04.01.2016, RV/7501247/2015,  BFG 21.12.2017, RV/7500943/2017, BFG 10.01.2018, RV/7500016/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_176`)


iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 zu bestrafen, auch wenn nachträglich die  Parkometerabgabe wirksam entrichtet wird (VwGH 26.01.1998, 96/17/0354, s. auch BFG  09.03.2017, RV/7500355/2016);

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_177`)


dies selbst dann, wenn der Lenker die Bestätigungs-SMS noch  innerhalb derselben Minute erhält.   Die Gültigkeit des elektronischen Parkscheins beginnt nicht mit der Sekunde 00 der Minute des  Einlangens der Bestätigung (vgl. etwa BFG 27.11.2014, RV/7500586/2014, BFG 23.04.2019,  RV/7501053/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_190`)


Bedient sich jemand des Handyparkens, bedeutet dies, die damit  allfällig verbundenen Unzulänglichkeiten in Kauf zu nehmen und ändert dies nichts an der  Verpflichtung zur Einhaltung der in einer gebührenpflichtigen Kurzparkzone einhergehenden  Rechtsvorschriften (BFG 17.04.2018, RV/7500201/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_197`)


In dieser Hinsicht besteht kein  Unterschied zum Handy-Parken (BFG 14.02.2017, RV/7500080/2017).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_222`)


Nach Ansicht des BFG fehlt es dem angefochtenen Straferkenntnis nicht an einer schlüssigen  Begründung (vgl. VwGH 10.12.2009, 2009/09/0065;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_255`)


Eine "Kulanzzeit" zwischen Abstellen des Fahrzeuges und der Entrichtung der  Parkometerabgabe in der in der Kontrolleinrichtungsverordnung vorgesehenen Form ist nicht  vorgesehen (vgl. etwa BFG 24.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_258`)


Die Strafbarkeit dieses vollendeten Abgabendeliktes fällt nicht weg, wenn nachträglich  innerhalb der angefangenen Viertelstunde die Parkgebühr entrichtet wird, auch wenn durch  die de facto Steuerbefreiung für die angefangene Viertelstunde der Erfolg der  Gebührenverkürzung wegfällt (vgl. etwa BFG 27.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_92`)


Wurde der Parkschein - bezogen auf die Abstellzeit  - falsch ausgefüllt, liegt insoweit eine Abgabenverkürzung vor (vgl. VwGH 25.01.1982,  0634/80, zur Angabe einer falschen Uhrzeit auf dem Parkschein (wie im Fall des Bf.), VwGH  29.09.1997, 96/17/0099, zur Angabe des falschen Tages auch BFG 26.02.2018,  RV/7500051/2018, BFG 04.03.2019, RV/7500144/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_99`)


Wurde - wie im Beschwerdefall irrtümlich - der Parkschein falsch (bezogen auf die Abstellzeit)  ausgefüllt, so liegt insoweit eine Abgabenverkürzung vor" (BFG 06.12.2017,  RV/7500809/2017, BFG 04.03.2019, RV/7500144/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_172`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_37`)


BFG 27.9.2017, RV/7104167/2017).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_39`)


BAO alleine dem Bundesfinanzgericht zu; die „Beschwerdevorentscheidung“ der belangten  Behörde vom 5. Februar 2018 ist folglich als absolut nichtiger Vorgang zu qualifizieren (vgl BFG  9.1.2020, RV/6100475/2017).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_142`)


c) 1 Konvolut an monatlichen Arbeitszeitnachweislisten des Bf bei der Fa.NiederImmobilien Institut GmbH  Zeitraum  Jänner 2014 – Dezember 2015:  Eine nähere Überprüfung durch das BFG hat in Gegenüberstellung des Arbeitszeitnachweises  (siehe untentstehend 2 rechte Spalten) zu den vom Bf vorgelegten Aufzeichnungen seiner  "Heimfahrten" Ö-D-Ö (siehe untenstehend die 2 linken Spalten) folgende Divergenzen  ergeben:    Fahrten Ö-D-Ö lt.  Aufzeichnung Bf    Lt. Zeitnachweisliste  des Arbeitgebers

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Fa.NiederImmobilien Institut GmbH` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_161`)


B) Verfahren vor dem Bundesfinanzgericht:  Das BFG hat folgende Erhebungen durchgeführt:  1.) Aktuelle ZMR-Abfrage:  Der Bf, Familienstand: ledig, war vom 6.6.2016 – 31.10.2016 mit Nebenwohnsitz und ist seit  2.11.2016 bis dato mit Hauptwohnsitz im Inland gemeldet.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_170`)


5.) BFG-Vorhaltschreiben vom 29.11.2019 an den Bf wie folgt:  " … Gemäß § 82 Abs. 8 KFG 1967 (in der im Streitzeitraum geltenden Fassung Mai 2014 – Mai  2015) sind Fahrzeuge mit ausländischem Kennzeichen, die von Personen mit dem  Hauptwohnsitz oder Sitz im Inland in das Bundesgebiet eingebracht oder in diesem verwendet  werden, bis zum Gegenbeweis als Fahrzeuge mit dauerndem Standort im Inland anzusehen  (Standortvermutung).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_185`)


Festzuhalten ist, dass für das BFG dagegen nicht - wie in der Beschwerde angesprochen (arg.:  "ist nur mit Nebenwohnsitz gemeldet") - ausschlaggebend erscheint, ob eine Wohnsitznahme  als "Hauptwohnsitz" oder "Nebenwohnsitz" bezeichnet wird, da die Bezeichnung für sich wohl  nur eines von vielen zu beurteilenden Indizien darstellen wird.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_189`)


Im Rahmen einer Betrachtung der beruflichen und wirtschaftlichen Beziehungen wäre daher  nach Ansicht des BFG insgesamt von einer weitaus überwiegenden Nahebeziehung zu  Österreich auszugehen, die insbesondere aufgrund der langjährigen und durchgehenden  beruflichen Tätigkeit bei der Fa.NiederImmobilien Institut GmbH bereits seit vielen Jahren besteht.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Fa.NiederImmobilien Institut GmbH` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_216`)


Nach Ansicht des BFG bedeutet dies im Ergebnis, dass abzüglich der nachgewiesenen  Betankung in Deutschland in Höhe von rund € 1.200 (= mtl. im Durchschnitt € 100 x 12) die  weitaus überwiegende Betankung im Restbetrag von ca. € 4.800 im Inland erfolgte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_223`)


Aufgrund der vorgenannten Umstände ergeben sich für das BFG nunmehr folgende Fragen:  14 von 29 Seite 15 von 29

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_229`)


Nach dem Dafürhalten des BFG bedürfte es zwecks diesbezüglich konkreter Feststellungen  wohl der Bekanntgabe aller erforderlichen Daten durch den Bf. Bislang wurden seinerseits  lediglich die Aufzeichnungen über die "Heimfahrten Ö-D-Ö" zur Vorlage gebracht, woraus ua.  lediglich zu erahnen ist, dass es sich hiebei um Fahrten von A/XX nach D/XX und retour handeln  wird.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_246`)


Entgegen der Ansicht des BFG könne der "Familienwohnsitz" (in Zhg mit der  "Pendlerregelung") nicht nur verheirateten Paaren mit Kindern vorbehalten sein.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_252`)


Die vom BFG hochgerechneten Tankkosten seien wegen nicht realistischer  Verbrauchszahlen (13,5 l/100 km) nicht nachvollziehbar, wobei zahlreiche Betankungen auch  bar bezahlt worden wären.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_261`)


Obiger BFG-Vorhalt samt Antwortschreiben des Bf wurden dem Finanzamt zur Kenntnis  übermittelt. Das Finanzamt hat sich dazu im Schreiben vom 17.2.2020 ua.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamt` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_274`)


In der am 13.8.2020 vor dem BFG abgehaltenen mündlichen Verhandlung wurde vom  Vertreter des Bf zusätzlich noch vorgebracht:  Von einem Verlegen des dauernden Standortes eines Kfz könne nur gesprochen werden, wenn  der nach den Kriterien des Hauptwohnsitzes bestimmte dauernde Standort NACH Zulassung  aufgegeben werde und wenn im zeitlichen Zhg.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_287`)


Der vom Vertreter gestellte Antrag auf Parteieneinvernahme zur  Beantwortung weiterer Fragen des BFG wurde abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_330`)


Ausgehend von  den eigenen Fahrtaufzeichnungen, wonach der Bf jedenfalls einmal pro Monat regelmäßig  Fahrten Ö-D-Ö durchgeführt hat, dies in Übereinstimmung großteils mit den  Kreditkartenabrechnungen (Daten der Betankung in Deutschland) wie auch mit der Aussage  der Vermieterin vom 25.2.2016, wonach er monatlich ca. 3-4 Tage in Deutschland und  ansonsten durchgehend am Wohnsitz in Österreich aufhältig war, sowie im Hinblick darauf,  dass ein Fahrzeug dieses Typus wie erhoben einen Benzin-Mindestverbrauch von 11 l/100 km  hat, sohin pro Fahrt (rund 1.600 km) allein von Treibstoffkosten in Höhe von rund € 200  auszugehen sein wird, erachtet es das BFG als wenig glaubhaft, dass der Bf monatlich mehrere  Wochenenden bzw. jedes Wochenende in Deutschland verbracht habe.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_336`)


Widersprüchlich erscheint dem BFG auch die nachmalige Angabe (Stellungnahme vom  27.12.2019), der Bf habe auf Bitte eines Arbeitskollegen 2012/2013 lediglich die Website der  Theatergruppe G "gestaltet", wohingegen er am 22.4.2015 aussagte, er "verwaltet" für diesen  Verein die homepage, was also durchaus – entgegen der Bestreitung jeglicher inländischer  sozialer Beziehungen – auf irgendeine Art von laufendem Kontakt zu diesem Verein schließen  läßt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_338`)


mit BFG-

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_346`)


widerspricht absolut jeglicher Lebenserfahrung und ist daher nach Ansicht des BFG wohl  ebenso als Schutzbehauptung zu qualifizieren;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_351`)


mit der deutschen Wohnsitzmeldung ein seit 2010 bestehender "Hauptwohnsitz" des Bf in  Deutschland argumentiert wird, erscheint dem BFG zum Einen die Aufteilung der Miete 50:50  (Anteil des Bf mtl. € 250) im Hinblick auf seinen monatlichen Aufenthalt dort von nur wenigen  Tagen schlicht nicht nachvollziehbar.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_353`)


Zum Anderen läßt die auf den deutschen Kontoauszügen vorgenommene  durchgehende Schwärzung der monatlichen Gutschrift unter dem Titel "Verwendungszweck  Auslagen" mit Ausnahme der einen diesbezüglichen Überweisung am 1.10.2013 in exakt der  Höhe der Mietzahlung für das BFG durchaus den Schluss zu, dass der monatliche Mietbetrag an  den Bf jeweils wieder zurücküberwiesen wird und es sich sohin überhaupt um eine Schein- Wohnsitzmeldung in Deutschland handeln könnte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_356`)


Damit kann letztlich die für das BFG  naheliegende Annahme der Rücküberweisung der Miete nicht abschließend verifiziert werden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_385`)


Entgegen dem zusätzlichen Vorbringen in der mündlichen Verhandlung stellt sich – soweit für  das BFG verständlich – gegenständlich auch nicht die Frage der "Verlegung" des Standortes  eines Fahrzeuges, sondern ist abzuklären, wo der dauernde Standort der Fahrzeuge nach den  Kriterien des § 82 Abs. 8 KFG (= Hauptwohnsitz und Verwendung im Inland) in den  betreffenden Zeiträumen gelegen war.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_411`)


Dieser  wäre nach Ansicht des BFG grundsätzlich dort zu sehen, wo eine Person mit eigener Familie,  also mit Ehepartner/Lebensgefährten und ev. gemeinsamen Kindern als den nächsten  Familienangehörigen, zu dem oder denen wohl die engsten persönlichen Verhältnisse  bestehen, zusammen lebt, nicht jedoch - etwa aufgrund von wiederkehrenden Besuchsfahrten  - am Wohnsitz der Herkunftsfamilie, dh. der Eltern und sonstigen Verwandtschaft.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_424`)


Neben den unzweifelhaft vorliegenden engsten beruflichen sowie  weitaus engeren wirtschaftlichen und finanziellen Beziehungen zu bzw. in Österreich ist  nämlich nach dem Dafürhalten des BFG nach der Lebenserfahrung auszuschließen, dass der Bf  in einem derart langen Zeitraum keinen persönlichen, freundschaftlichen oder sonstigen  sozialen Anschluss gefunden haben sollte, welcher sohin wohl nicht ernsthaft zur Gänze in  27 von 29 Seite 28 von 29

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_31`)


In der Folge legte das BFG dem Erkenntnis nachstehenden, aus der Aktenlage sowie dem  Parteienvorbringen resultierenden Sachverhalt zu Grunde:  Im Anschluss an die am 12.06.2018 erfolgreich absolvierte Matura hat der Sohn des Bf. gemäß  den Angaben der mit 13.07.2018 datierten Beantwortung des Überprüfungsschreibens in der  Zeit vom 01.10.2018 bis zum 30.06.2019 seinen Zivildienst geleistet.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_50`)


BFG 29.6.2017, RV/5100439/2016).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_53`)


In Ansehung vorstehender Ausführungen war daher seitens des BFG ein im Zeitraum vom  01.07.2018 bis zum 30.09.2018 bestehender Anspruch des Bf. auf Familienbeihilfe und  Kinderabsetzbeträge zu verneinen, weswegen die Rückforderung der für nämlichen Zeitraum  bezogenen Beträge völlig zu Recht erfolgte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_56`)


2.3.2. Anspruch des Bf. auf Familienbeihilfe im Zeitraum vom 01.07.2019 bis zum 30.09.2019  Ausgehend von dem unter Punkt 1 dargestellten Sachverhalt, wonach der Bf. in seinem  Antwortschreiben vom 22.10.2019 einräumte, dass das Kind x erst ab dem Jahr 2020 ein  Studium beginnen werde, steht für das BFG zweifelsfrei fest, dass nach § 2 Abs. 1 lit. e FLAG  1967 von einem Beginn der Berufsausbildung zum frühestmöglichen Zeitpunkt nach Ableistung  des Zivildienstes keine Rede sein kann, weswegen in Ermangelung einer  Anspruchsberechtigung auch die Rückforderung der Familienbeihilfe und der  Kinderabsetzträge für diesen Zeitraum in Übereinstimmung mit den gesetzlichen Vorschriften  erfolgte.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_55`)


Weiters forderte das BFG den Bf. mit Schreiben vom 25. Juni 2020 zur Vorlage diverser  Unterlagen wie Kreditvertrag, Zahlungsbelege über die Kreditrückzahlungen, Verfügungen über  das Sparguthaben usw. auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_148`)


Dies wäre  etwa bei Sicherstellungsaufträgen (§ 232 BAO) und bei der Festsetzung von Zwangsstrafen (§  111 BAO) der Fall (BFG 24.06.2020, RV/7103717/2019 mwN).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_4`)


Mit Erkenntnis des BFG vom 15.10.2020, RV/7103544 wurde der gegen die die  Wiederaufnahme der Verfahren zur Einkommensteuer 2008 bis 2010 verfügenden Bescheide  gerichteten Beschwerde vom 18.12.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_13`)


Am 13.03.2018 langte bei der belangten Behörde ein Schreiben des Bf. mit folgendem Inhalt  ein:  „Gegen den Bescheid vom 16.02.2018 lege ich Beschwerde ein und beantrage eine  Entscheidung über die Beschwerdevorentscheidung vom 16.02.2018 durch das BFG, zumal die  Republik für den entstandenen Schaden haftet.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_22`)


Sohin verbleibt dem BFG, aufgrund des o.a. Vorlageantrages, über die Beschwerde gegen die  o.a. Buchungsmitteilung zu entscheiden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_24`)


Das BFG hat hiezu erwogen:  Gemäß § 260 Abs.1 lit.a Bundesabgabenordnung,(BAO), ist die Bescheidbeschwerde mit  Beschwerdevorentscheidung oder mit Beschluss zurückzuweisen, wenn sie unzulässig ist.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_441`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_53`)


11; BFG 09.06.2017, RV/7400198/2016-RS1).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_66`)


Das Bundesfinanzgericht hat zu dieser Frage beispielsweise entschieden, dass kein minderes  Verschulden vorliegt, wenn die Databox nicht kontrolliert wird (BFG vom 28.09.2020,  RV/3100475/2020), genausowenig wie im Fall der Nichtbeachtung einer Bescheidzustellung in  die Databox (BFG vom 13.08.2020, RV/3100480/2020).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |
| `BFG` | `BFG` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_15`)


Darin habe das BFG die operative Tätigkeit der L  Schweiz AG als erwiesen angesehen und auf Unterlagen seitens der Schweizer Steuerbehörde  verwiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_22`)


Es werde nochmals auf  die Entscheidung des BFG vom 27.05.2019, RV/2100552/2018 verwiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_45`)


…"  Die nunmehr vorgelegten AGBs belegen eine Abweichung zu den, dem Erkenntnis des BFG vom  24.06.2019, RV/7100189/2015, zugrundegelegten AGBs.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_68`)


Dafür ist – wie oben ausgeführt – maßgebend, wer sich zivilrechtlich die Leistung  ausbedungen hat, wer aus dem zivilrechtlichen Verpflichtungsgeschäft berechtigt und  verpflichtet ist (vgl. BFG 27.05.2019, RV/2100552/2018).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_183`)


Die Abgabenbehörde ist jedenfalls befugt, die Schätzung zu überprüfen und von ihr  abzuweichen, wenn sie sich als unzutreffend erweist (vgl BFG 27. November 2018,  RV/7105272/2015).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_190`)


Maßgeblich für die Nutzungsdauer ist nicht das fiktive oder tatsächliche Alter oder die  gewöhnliche Lebensdauer, sondern der konkrete Bauzustand eines Gebäudes im Zeitpunkt des  Erwerbs, und nur wenn nachgewiesen werden kann, dass dieser keine Nutzungsdauer von  66,67 Jahren erlaubt, kann die (nachvollziehbar begründete und berechnete) kürzere  Nutzungsdauer gewählt werden (vgl BFG 12.02.2015, RV/5100393/2013).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_9`)


Mit diesem Erkenntnis hob der VwGH aufgrund der außerordentlichen Revision der Bf. die  Entscheidung des BFG vom 21.6.2018, Gz. RV/7103576/2017, zur Beschwerde der Bf. vom  5.12.2016 hinsichtlich der Festsetzung des Dienstgeberbeitrages und Zuschlags zum  Dienstgeberbeitrag der Jahre 2010 bis 2013 wegen Rechtswidrigkeit des Inhaltes auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_29`)


Nach durchgeführter mündlicher Verhandlung wurde die Beschwerde mit Erkenntnis des BFG  vom 21.6.2018, Gz. RV/7103576/2017, soweit sie die Festsetzung der Dienstgeberbeiträge  sowie der Zuschläge zum Dienstgeberbeitrag der Jahre 2010 bis 2013 betraf, abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_32`)


Der VwGH hob in der Folge die Entscheidung des BFG mit Erkenntnis, Zl. Ra 2018/13//0061,  vom 19.5.2020, wegen inhaltlicher Rechtswidrigkeit auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_34`)


Im nun fortgesetzten Verfahren vor dem BFG wurde der ursprüngliche Antrag auf  Durchführung einer mündlichen Senatsverhandlung mit Fax vom 25.6.2020 zurückgenommen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_36`)


Mit dem angefochtenen Erkenntnis des BFG vom 21.6.2018, auf das verwiesen wird, war vom  Vorliegen von Dienstverhältnissen, sowohl der wesentlich beteiligten Gesellschafter-

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_40`)


Die außerordentliche Revision der Bf. richtete sich gegen die im Erkenntnis des BFG  angewendete gesetzliche Bestimmung des § 25 Abs. 1 Z 1 lit b EStG 1988 im Zusammenhang  mit der Tätigkeit der vier nicht wesentlich beteiligten Gesellschafter der Bf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_41`)


Die Revision richtete sich nicht gegen die im Erkenntnis des BFG zur Tätigkeit der wesentlich  beteiligten Gesellschafter-Geschäftsführerin getroffene Feststellung hinsichtlich der  Beurteilung der Honorare als Arbeitslöhne iSd § 22 Z 2 EStG und deren Einbeziehung in die  Bemessungsgrundlage für den Dienstgeberbeitrag gem. § 41 FLAG.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_57`)


Aufgrund des als unstrittig zu beurteilenden Sachverhalts, war daher wie im Erkenntnis des  BFG vom 21.6.2018 zu entscheiden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 99** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_58`)


Hinsichtlich des entscheidungsrelevanten Sachverhalts wird auf die Entscheidung des BFG  verwiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

## `Universities and Health Funds` 🏆

**F1:** 0.005 | **Precision:** 0.966 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `6ef015ec`  
**Description:**
Matches universities (Universität, FH, Fachhochschule) with specific prefixes or locations, and health funds. Requires context to avoid partial matches.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:des|dem|der|vom|von\s+der|der\s+)?\s*((?:Karl\-Franzens\-\s+Universität\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?|Fachhochschule\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?|FH\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?|Universität\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:\s+\d+)?|Wiener\s+Gebietskrankenkasse|Krankenfürsorgeanstalten))\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.966 | 0.002 | 0.005 | 29 | 28 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 1 | 11720 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_85`)


Ich werde - so mir dies möglich ist - zur noch anzuberaumenden mündlichen Verhandlung vor dem Bundesfinanzgericht auch eine Bestätigung der Wiener Gebietskrankenkasse mitnehmen, aus der die Anzahl der bei mir in den Jahren 2012 und 2013 durchschnittlich beschäftigten Mitarbeiter ersichtlich ist.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_32`)


Unstrittig ist, dass der Sohn des Bf. im Wintersemester 2017/2018 mit dem Studium der  Humanmedizin an der Universität Wien begann und davor, beginnend  mit dem  Sommersemester 2016, das Bachelorstudium Wirtschaftsrecht an der Wirtschaftsuniversität  Wien betrieb.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `Wirtschaftsuniversität  Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_78`)


2 StudFG zutrifft, da er  nach drei Semestern  Wirtschaftsrecht an der WU Wien im Wintersemester 2017/2018 mit  dem Studium der Humanmedizin an der Universität Wien begann.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_54`)


Beschwerdegründe:  Der Beschwerdeführer hat nach der Erlangung seiner Matura ein Studium der  Betriebswirtschaft an der Universität Wien aufgenommen.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_146`)


Zusammengefasst ergibt sich aus der Anamnese, dass der Bf. laut eigenen Angaben die  Handelsakademie besuchte und anschließend BWL studierte (kein Abschluss) und an der  Universität Wien vom Sommersemester 1989 bis Wintersemester 1995 in der Studienrichtung  Soziologie, geisteswissenschaftliche Stzw Politikwissenschaft inskribiert war  (Studienzeitbestätigung der Universität Wien vom 28. Juli 2016).

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `Prof. Maida` (person)
- `Dr. Wolfgang Baischer` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_164`)


Laut Studienzeitbestätigung der Universität Wien vom 28. Juli 2016 war der Bf. in der  Studienrichtung Soziologie, geisteswissenschaftliche Stzw Politikwissenschaft vom  Sommersemester 1989 bis Wintersemester 1995 inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_165`)


Über abgelegte Prüfungen gibt es  keine Nachweise, da diese laut Auskunft der Universität Wien nicht elektronisch erfasst  wurden (Schreiben des Sachwalters vom 25. August 2016).

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_45`)


Am 01.10.2018 begann sie das Bachelorstudium Biologie an der Universität Wien.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_47`)


Ab dem Sommersemester 2019 absolviert sie an der Universität Wien das Bachelorstudium  Astronomie, UA 033 661.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_53`)


Ab dem Wintersemester 2019/20 legte sie laut der Bestätigung der Universität Wien über  positiv absolvierte Prüfungen vom 28.07.2020 folgende Prüfungen ab:    PUE STEOP 2: Einführung in die physikalischen  Rechenmethoden  3 ECTS 2 SSt 10.01.2020  STEOP Modulprüfung Einführung in die Astronomie 4 ECTS 0 SSt 30.01.2020  STEOP 1: Modulprüfung Experimentalphysik I 8 ECTS 7 SSt 29.06.2020  UE Experimentalphysik II: Optik, Elektromagnetismus,  Relativität  3 ECTS 2 SSt 29.06.2020  STEOP 2: Modulprüfung Einführung in die physikalischen  Rechnungsmethoden  7 ECTS 6 SSt 20.07.2020  VU PM-AP1 VU Astrophysik I (Teil 1) 4 ECTS 3 SSt 23.07.2020  Summe 29 ECTS    Um zu einer Reduktion der weiteren Verbreitung einer SARS CoV-2 Infektion bestmöglich  beitragen zu können, beschloss das Rektorat der Universität Wien entsprechend der  Anordnung der Behörden folgende Maßnahmen für den Studienbetrieb: An der Universität  Wien werden von Mittwoch, 11.03.2020, bis voraussichtlich einschließlich Freitag, 03.04.2020  keine Prüfungen mit physischer Präsenz abgehalten.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |
| `Universität Wien` | `Universität Wien` |
| `Universität  Wien` | `Universität  Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_54`)


Daher wurde die Tochter des BF von der  Universität Wien automatisch von der Prüfung „26-0777 STEOP 1: Modulprüfung  Experimentalphysik I“, die ursprünglich auf den 01.04.2020 angesetzt war, abgemeldet.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_26`)


Laut Bestätigung der Veterinärmedizinischen Universität Wien hat die Tochter im Studienjahr  2019/20 im Bachelorstudium Pferdewissenschaften (in chronologischer Abfolge) bis zum  25.05.2020 folgende Prüfungen/Lehrveranstaltungen positiv abgelegt bzw. mit Erfolg  teilgenommen:    Titel Note Semesterstunden ECTS Punkte Prüfungs- /  Anerkennungsdatum  Pferderassen und  Pferdebeurteilung  mit Erfolg  teilgenommen  1,00 0,00 20.11.2019  Organisation des Reit- und  Rennsports  1 1,00 1,50 03.12.2019  Pferdezucht- und Gestütmedizin mit Erfolg  teilgenommen  1,00 0,00 04.12.2019  Geschichte der Reiterei und  Pferdezucht  2 0,00 1,50 10.12.2019  Geschichte der Reiterei und  Pferdezucht  mit Erfolg  teilgenommen  1,00 0,00 10.12.2019  Pferderassen und  Pferdebeurteilung  1 0,00 1,50 11.12.2019  Pferdezucht und Gestütmedizin 2 1,00 1,50 18.12.2019  Naturwissenschaftliche  Grundlagen-Physik  mit Erfolg  teilgenommen  1,00 0,00 23.01.2020  Naturwissenschaftliche  Grundlagen-Chemie  3 0,00 4,50 30.01.2020  Naturwissenschaftliche  Grundlagen-Chemie  mit Erfolg  teilgenommen  3,00 0,00 30.01.2020  Ethologie des Pferdes 4 1,00   1,50  30.01.2020  Zoologie für  Pferdewissenschaften  3 2,00 3,00  26.02.2020  Klassische Reitlehre und  Pferdeausbildung  mit Erfolg  teilgenommen  1,00 1,00 25.05.2020  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_37`)


Den Familien- wohnsitz zu verlegen, sei nicht zumutbar, da die Ehegattin in der Universität Graz arbeite, das  1999 aufgestockte Elternhaus wegen der Lage in einem strukturschwachen Gebiet nur mit Ver- lust verkauft werden können, weshalb eine Wohnmöglichkeit am Beschäftigungsort LKW – Ab- stellplatz nicht finanzierbar sei.

| Predicted | Gold |
|---|---|
| `Universität Graz` | `Universität Graz` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_231`)


Der Kanzler informierte dabei  gemeinsam mit Gesundheitsminister Rudolf Anschober, dem steirischen Landeshauptmann  Hermann Schützenhöfer, dem Wiener Bürgermeister Michael Ludwig und Univ.-Prof. Dr.  Oswald Wagner, Vizerektor der Medizinischen Universität Wien und Leiter des klinischen  Institutes für Labormedizin, über die weitere Vorgehensweise in der Corona-Krise.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `Hermann` (person)
- `Michael Ludwig` (person)
- `Univ.-Prof. Dr.  Oswald Wagner` (person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_12`)


Begründend wurde wie folgt ausgeführt:  Sachverhalt:  Ihr Sohn StR Armin Dürrwaechter, geboren am 29. Januar 2024, studierte im Zeitraum vom Wintersemester  2020 bis inklusive Wintersemester 2021 "A033 630 Biologie" an der Universität Wien.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `StR Armin Dürrwaechter` (person)
- `29. Januar 2024` (date)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_34`)


Dem Schreiben war eine Bestätigung des Studienerfolges  von der FH Campus Wien beigefügt, aus dem die positiv absolvierte Gesamtanzahl von 19,5  ECTS-Credits hervorgeht.

| Predicted | Gold |
|---|---|
| `FH Campus Wien` | `FH Campus Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_38`)


StR Armin Dürrwaechter  hat ab dem  Wintersemester 2020 bis inkl. Wintersemester 2021 (das heißt für insgesamt 3 Semester) an  der Universität Wien das Studium „A033 630 Biologie“ belegt und nach Ende des  Wintersemesters 2021 – und somit vor Beendigung – abgebrochen.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Missed by this rule (FN):**

- `StR Armin Dürrwaechter` (person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_39`)


Da für dieses Studium kein  Studienerfolg nachgewiesen werden konnte, wurde der Familienbeihilfebezug mit September  2021 eingestellt.  Mit Februar 2022 (somit ab dem Sommersemester 2022) hat StR Armin Dürrwaechter  das Studium  gewechselt und studiert nunmehr an der FH Campus Wien („0599 FH-Bachelor Gesundheits-  und Krankenpflege).

| Predicted | Gold |
|---|---|
| `FH Campus Wien` | `FH Campus Wien` |

**Missed by this rule (FN):**

- `StR Armin Dürrwaechter` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_65`)


Im vorliegenden Fall hat der Studierende StR Armin Dürrwaechter – wie aus dem festgestellten Sachverhalt  ersichtlich – zunächst für drei Semester (Wintersemester 2020 bis inklusive Wintersemester  2021) Biologie studiert, bevor er dann mit Februar 2022 (und somit ab dem Sommersemester  2022) das Studium „Gesundheits- und Krankenpflege“ an der FH Campus Wien begonnen hat.

| Predicted | Gold |
|---|---|
| `FH Campus Wien` | `FH Campus Wien` |

**Missed by this rule (FN):**

- `StR Armin Dürrwaechter` (person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_98`)


Die Feststellung, dass er im Zeitpunkt der Ausstellung der Honorarnoten von einer  nichtselbständigen Tätigkeit ausgegangen ist, beruht auf nachstehenden Erwägungen:  Anlässlich einer Befragung am 28.04.2016 bei der Wiener Gebietskrankenkasse durch die  Beitragsprüferin gab der Bf. u.a. zu Protokoll, „ihm sei nicht bewusst gewesen, dass er für die  6 von 11 Seite 7 von 11

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_108`)


Vor dem  Hintergrund seiner Angaben im Rahmen der Verfahren vor dem Arbeits- und Sozialgericht und  der Wiener Gebietskrankenkasse lässt die Tatsache, dass der Bf. nicht zu Beginn seines  Arbeitsverhältnisses, sondern erst im August 2014 eine UID-Nummer beantragt hat, nach  Auffassung des erkennenden Senates nur den Schluss zu, dass er davon überzeugt war, keine  unternehmerische Tätigkeit auszuüben.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_8`)


Ihre ANV-Erklärung 2018 wurde dem FA im Dez 2019 vom Sohn via FAX-Anschluss der  Universität Graz dreimal unvollständig übermittelt. Die Bf machte darin, soweit  verfahrensrelevant, unter der Kz 731 (Begräbniskosten) eine außergewöhnliche Belastung in  Höhe von 10.000,- € geltend.

| Predicted | Gold |
|---|---|
| `Universität Graz` | `Universität Graz` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_9`)


Im nachfolgenden Ermittlungsverfahren angeforderte Unterlagen (Niederschrift zur  Verlassabhandlung, Einantwortungsurkunde, Rechnungen, Zahlungsbelege) wurden dem FA  am Tag des Fristablaufes neuerlich vom FAX-Anschluss des Sohnes der Universität Graz  übermittelt und waren wiederum teilweise unvollständig.

| Predicted | Gold |
|---|---|
| `Universität Graz` | `Universität Graz` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_5`)


S. wohnt und studiert seit dem Wintersemester 2019 an der Universität Wien.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_73`)


Im zweiten  Fall, läge jedenfalls eine Ergänzung ihres Berufsfeldes vor, sodass jedenfalls Werbungskosten  im Sinne des § 16 EStG bezüglich der Studiengebühr an der Fachhochschule Modul vorlägen.

**False Positives:**

- `Fachhochschule Modul` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Offices` 🏆

**F1:** 0.392 | **Precision:** 0.931 | **Recall:** 0.249  

**Format:** `regex`  
**Rule ID:** `4bdfd917`  
**Description:**
Matches Finanzamt variations including genitive cases, specific locations, and special departments like 'für Großbetriebe' or 'für Gebühren', handling missing articles.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(Finanzamt(?:es)?(?:\s+(?:Österreich|St\.\s+Veit\s+Wolfsberg|Kirchdorf\s+Perg\s+Steyr|Linz|Gmunden\s+Vöcklabruck|Wien\s+\d+/\d+/\d+|für\s+(?:Großbetriebe|Gebühren|Verkehrsteuern|Glücksspiel)|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Innsbruck|Neunkirchen\s+Wr\.\s+Neustadt|Feldkirch|faxy))?)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.931 | 0.249 | 0.392 | 3137 | 2920 | 217 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2920 | 217 | 8828 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `N.N.` (person)
- `Mag. Michael Nierla` (person)
- `N.N.` (person)
- `Verwaltungsgerichtshof` (organisation)

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

- `Bundesfinanzgericht` (organisation)
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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Gmunden Vöcklabruck` | `Finanzamtes Gmunden Vöcklabruck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Lehwaldt` (person)
- `Waltraud Hinterlandt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_42`)


Tag  (Fälligkeitstag) des auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden  Kalendermonates eine Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen  Finanzamt einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  (Vorauszahlung) oder den auf den Voranmeldungszeitraum entfallenden Überschuß unter  entsprechender Anwendung des § 20 Abs. 1 und 2 und des § 16 selbst zu berechnen hat.“

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_4`)


Das Finanzamt X (FA) verneint die Anwendbarkeit, weil der Betrieb des Bf im  Verfahrenszeitraum der Bestimmung des § 111 Abs. 2 GewO 1994 zuzuordnen gewesen und  damit nicht ganzjährig einer Verpflichtung zur Innehabung einer Gewerberechtigung  unterlegen sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes für Gebühren` | `Finanzamtes für Gebühren` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Ophelia Dutschka` (person)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_29`)


In weiteren Schreiben durch unsere Kanzlei  vom 6.6.2018 sowie 26.6.2018 an das zuständige Finanzamt für Gebühren, Verkehrssteuern  und Glückspiel wurde der Sachverhalt nochmals konkret aufgezeigt und erläutert.

| Predicted | Gold |
|---|---|
| `Finanzamt für Gebühren` | `Finanzamt für Gebühren` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_4`)


Der Beschwerdeführer machte im Rahmen der Arbeitnehmerveranlagung 2017 nachstehende  Werbungskosten geltend:  Fachliteratur 419,16 €  Fortbildungs-, Ausbildungs- und Umschulungskosten 5.364,12 €  Werbungskosten gesamt 5.783,28 €  Bei der Veranlagung anerkannte das Finanzamt lediglich den Pauschbetrag für  Werbungskosten in Höhe von 132 €; (Bescheid vom 22.1.2019).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_8`)


Mit Beschwerdevorentscheidung vom 11.7.2019 wies das Finanzamt die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_12`)


Mit Vorlagebericht vom 29.1.2020 legte das Finanzamt die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_38`)


Die Frage des Finanzamtes in seinem Vorhalt vom 22.10.2018 „Wollen Sie die erworbenen  Kenntnisse als selbständig Tätiger verwerten?“ hat der Beschwerdeführer folgendermaßen  beantwortet:  „Ich stelle Überlegungen an, die mit der laufenden Aus- bzw. Weiterbildung erworbenen  Kenntnisse auch als selbständig Tätiger zu verwerten.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_15`)


Dagegen sei weder Berufung erhoben, noch seien seitens des Finanzamtes weitere  nach außen erkennbare (verjährungsverlängernde) Amtshandlungen gesetzt worden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_35`)


Da die als verfassungswidrig erkannte Befristung für den hier zu beurteilenden Beschwerdefall  keine Wirkung (mehr) zu entfalten vermag, war der Beschwerde gegen den  Zurückweisungsbescheid des Finanzamtes vom 2.3.2018 auf Grund der oa. VfGH- bzw. VwGH- Erkenntnisse stattzugeben und der Zurückweisungsbescheid aufzuheben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Siegfried Basyurt` (person)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_24`)


Im Akt erliegen zwei Internet-Abfragen des Finanzamtes (EurotaxGlass-Fahrzeugbewertung;

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_26`)


Mit Bescheid vom 9.11.2010, StrNr, hat das Finanzamt der Bf für das Fahrzeug Range Rover  Sport 3.0 TDV6 HSE mit der Fahrgestellnummer X1:  a) ausgehend von der Bemessungsgrundlage € 57.090,64 die Normverbrauchsabgabe (NoVA)  im Ausmaß von 14 % unter Berücksichtigung von Malus (§ 6a NoVAG) und Abgabenerhöhung  (§ 6 Abs. 6 NoVAG) im Betrag von€

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_54`)


Das Finanzamt hat in der Folge, ohne eine Berufungsvorentscheidung zu erlassen, die Berufung  samt Verwaltungsakt dem Unabhängigen Finanzsenat zur Entscheidung vorgelegt und die  Abweisung der Berufung beantragt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_55`)


Vom (nunmehr zuständigen) Bundesfinanzgericht (BFG) wurden Erhebungen durchgeführt wie  folgt:  1) Anforderung von Aktenteilen:  Vom Finanzamt wurden an bislang nicht vorliegenden Aktenteilen am 16.12.2019  nachgereicht:  a) Schreiben an C vom 9.8.2010 zum Betreff "PKW Land Rover, KZ B1" folgenden Inhalts:  " … Lt. Telefonat am 27.7.2010 wollten Sie innerhalb weniger Tage den Leasingvertrag zu o.a.  PKW nachreichen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_58`)


Es ist daher dem Finanzamt zu erläutern und nachzuweisen,  inwieweit die Frau falsche Angaben gemacht haben soll (bezüglich Familienwohnsitz,  Angestelltenverhältnis, Verwendung des PKWs etc.).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_60`)


…"  b) Mail-Schreiben des C vom 26.8.2010, mit dem in der Beilage der Leasingvertrag zum PKW  dem Finanzamt übermittelt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Basyurt` (person)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_73`)


Im Zeitpunkt der Unterfertigung der Niederschrift vor dem Finanzamt durch die Bf (= am  27.7.2010) habe der Tachostand des Fahrzeuges ca. 25.000 km betragen, der aufgrund der  Fahrten des Gatten D-A1-D zustande gekommen wäre;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_105`)


Die obigen Sachverhaltsfeststellungen werden weitgehend auf die von der Bf in ihrer  Befragung am 27.7.2010 gemachten Angaben (siehe Niederschrift) insofern gestützt, als es sich  hiebei um die erstmaligen und somit wohl unvoreingenommenen Angaben der Bf vor dem  Finanzamt handelt. Diesen ist nach Ansicht des Bundesfinanzgerichtes im Rahmen der freien  Beweiswürdigung eine weitaus höhere Glaubwürdigkeit beizumessen als jenen, von Seiten des  Ehegatten (der nach Aussage des Rechtsvertreters dessen "Hauptansprechpartner" war) teils  unsubstantiierten, dh. nicht nachgewiesenen und teils auch widersprüchlich aufgestellten  Behauptungen in Form des Beschwerdevorbringens, die sohin als Schutzbehauptungen zu  werten sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_165`)


Die Beschwerde richtet sich primär dagegen, dass die Umsätze für die Sexdienstleistungen vom  Finanzamt der Bf. zugerechnet werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_214`)


Die Prostitutionserlöse waren daher vom Finanzamt zu Recht der Bf. zuzurechnen, da sie zum  Betrieb eines Bordells (mit den entsprechenden Auflagen) berechtigt war und sie in  einschlägigen Medien einerseits Werbung für „ihre Girls“ geschalten sowie andererseits –  mehrsprachig - Prostituierte für ihre Bar angeworben hat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_3`)


Entscheidungsgründe  Mit Bescheiden vom 6. Mai 2019 verfügte das Finanzamt die Pfändung und Überweisung einer  Geldforderung der Beschwerdeführerin an die X-Bank zur Hereinbringung der in Höhe von  € 7.870,70 (Abgabenschuldigkeiten in Höhe von € 7.786,22 zuzüglich Gebühren und  Barauslagen für diese Pfändung in Höhe von 84,48).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_4`)


Mit einem weiteren Bescheid vom 6. Mai 2019 setzte das Finanzamt gegenüber der Bf. für  diese Amtshandlung Pfändungsgebühren in Höhe von € 77,86 und Auslagenersätze in Höhe  von € 6,62 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_15`)


Mit Beschwerdevorentscheidungen von 22. Mai 2019 wies das Finanzamt die Beschwerden als  unbegründet ab und führte aus:  a) BVE zur Beschwerde gegen den Pfändungsbescheid  Die Pfändung einer Geldforderung sei gemäß § 65 AbgEO zu Recht erfolgt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_21`)


Informativ werde mitgeteilt, dass der Abzug von monatlich € 30,00 von der Pension nicht für  das Finanzamt erfolge.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_31`)


Sofern nicht die  Bestimmung des § 67 zur Anwendung kommt, geschieht die Pfändung dadurch, dass das  Finanzamt dem Drittschuldner verbietet, an den Abgabenschuldner zu bezahlen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_38`)


Werden beschränkt pfändbare Geldforderungen auf ein Konto des Abgabenschuldners bei  einem Kreditinstitut oder der Österreichischen Postsparkasse überwiesen, so ist gemäß § 54  Abs. 1 AbgEO eine Pfändung des Guthabens auf Antrag des Abgabenschuldners vom  Finanzamt insoweit aufzuheben, als das Guthaben dem der Pfändung nicht unterworfenen  Teil der Einkünfte für die Zeit von der Pfändung bis zum nächsten Zahlungstermin entspricht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_40`)


Gemäß § 54 Abs. 3 AbgEO hat das Finanzamt die Pfändung des Guthabens über Antrag des  Abgabenschuldners für den Teil aufzuheben, dessen dieser bis zum nächsten Zahlungstermin  dringend bedarf, um seinen notwendigen Unterhalt zu bestreiten und seine laufenden  gesetzlichen Unterhaltspflichten zu erfüllen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_54`)


Das Finanzamt hat den aufgrund der Pfändung überwiesenen Betrag in Höhe von € 939,67  mittlerweile dem Bf. zurücküberwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_55`)


Das Bundesfinanzgericht geht wie das Finanzamt davon aus, dass die auf das Konto des Bf.  überwiesenen Beträge, dem Pfändungsschutz des § 292i EO unterliegen (vgl. OGH 28.06.2018,  9 Ob 22/18b).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_5`)


Das Finanzamt erließ am 21.8.2018  den Einkommensteuerbescheid 2016, berücksichtigte die geltend gemachten Krankheitskosten  darin nicht und begründete dies wie folgt: „Die Krankheitskosten der Ehegattin konnten nicht  berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_16`)


Mit Beschwerdevorentscheidung vom 27.11.2018 gab das Finanzamt der Beschwerde teilweise  statt und berücksichtigte EUR 724,95 als außergewöhnliche Belastungen mit folgender  Begründung: „Hat ein Pflegebedürftiger sein Vermögen (zB Wohnung, Sparbuch) noch nicht  übertragen, gehen die Pflegekosten zunächst zulasten dieses Vermögens.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_33`)


Das Finanzamt legte die Beschwerde am 20.3.2019 dem Bundesfinanzgericht vor und  beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_35`)


Mit Schreiben vom  10.7.2020 ergänzte das Finanzamt sein Vorbringen dahin, dass in Umsetzung des  Leistungsfähigkeitsprinzips Krankheitskosten für den Ehepartner insoweit als  außergewöhnliche Belastungen anzuerkennen seien, als diese Aufwendungen das Einkommen  des erkrankten Ehepartners unter das steuerliche Existenzminimum von EUR 11.000,- jährlich  herabmindern würden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_95`)


Wenn das Finanzamt vermeint, der freiwillige Verzicht auf eine Verwertung des Vermögens der  Ehegattin führe dazu, dass die Pflegekosten für die Ehegattin vom Beschwerdeführer freiwillig  getragen würden und daher keine Zwangsläufigkeit der Belastungen vorliegen könne, so ist  ihm Folgendes entgegenzuhalten:  Im Zivilrecht wird zwischen Unterhaltsansprüchen von Eltern gegenüber ihren Kindern und  solchen zwischen Ehegatten insofern differenziert, als einerseits die Unterhaltsverpflichtung  von Kinder gegenüber ihren Eltern (unter anderem) jener zwischen Ehegatten im Rang  nachsteht (vgl § 234 Abs. 2 ABGB) und sich andererseits (nur) der Unterhaltsanspruch eines  Elternteiles (unter anderem) insoweit mindert, als dem Elternteil die Heranziehung des  Stammes eigenen Vermögens zumutbar ist (vgl § 234 Abs. 3 ABGB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_98`)


Somit ist der Verweis des Finanzamtes auf die Erkenntnisse  des VwGH vom 29.4.2015, 2012/13/0012 und vom 20.11.2019, Ro 2018/15/0024 ist nicht  geeignet, sein Vorbringen zu stützen: In beiden Erkenntnissen hat der Verwaltungsgerichtshof  über die Abzugsfähigkeit von Unterhaltsleistungen an einen Elternteil im Zusammenhang mit  einer vorangegangenen Vermögensübertragung vom Elternteil auf Nachkommen  abgesprochen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_99`)


Auch das vom Finanzamt angezogene Argument, das dem Abgabenrecht immanente  Leistungsfähigkeitsprinzip würde neben der vorrangigen Verwertung eigenen Vermögens die  Berücksichtigung eines steuerlichen Existenzminimums von EUR 11.000,- bei der Ehegattin  gebieten, würde nach Ansicht des Bundesfinanzgerichts die Abzugsfähigkeit von  außergewöhnlichen Belastungen durch Unterhaltsaufwendungen für Ehegatten über Gebühr  und in einer nicht vom Gesetz gedeckten Weise einschränken.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

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

**Missed by this rule (FN):**

- `BFG` (organisation)

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_47`)


4.2. Soweit das Finanzamt die Inanspruchnahme des Werkverkehrs in den Monaten Februar  und Juni für zumutbar gehalten und deshalb eine Kürzung des Pauschales vorgenommen  hat, ist festzuhalten:    Im Erkenntnis VwGH 27.07.2016, 2013/13/0088 hat der Verwaltungsgerichtshof klar- gestellt, dass die sich aus § 16 Abs. 1 Z 6 lit. b und c EStG 1988 ergebenden Pauschbe- träge auf Grund des Wortlautes des Gesetzes nicht schon dann nicht zustehen, wenn  der Arbeitnehmer im Werkverkehr befördert werden könnte und ihm dies auch zumut- bar wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Gmunden Vöcklabruck` | `Finanzamtes Gmunden Vöcklabruck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_23`)


Tag (Fälligkeitstag) des  auf einen Kalendermonat (Voranmeldungszeitraum) zweitfolgenden Kalendermonates eine  Voranmeldung bei dem für die Einhebung der Umsatzsteuer zuständigen Finanzamt  einzureichen, in der er die für den Voranmeldungszeitraum zu entrichtende Steuer  2 von 4 Seite 3 von 4

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_25`)


Nach § 21 Abs 3 UStG 1994 hat das Finanzamt die Steuer festzusetzen, wenn der Unternehmer  die Einreichung der Voranmeldung pflichtwidrig unterlässt oder wenn sich die Voranmeldung  als unvollständig oder die Selbstberechnung als nicht richtig erweist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Finanzamtes Neunkirchen Wr. Neustadt` | `Finanzamtes Neunkirchen Wr. Neustadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_5`)


Die Sachverständige Dr.in 1, FA für Neurologie und Psychiatrie, des Bundesamtes für Soziales  und Behindertenwesen erstellte am 16.12.2018 im Auftrag des Finanzamtes folgendes 1.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)
- `Bundesamtes für Soziales  und Behindertenwesen` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_36`)


Das Finanzamt wies den Antrag vom 10.08.2018 auf Familienbeihilfe und erhöhte  Familienbeihilfe mit Bescheid vom 16.01.2019 ab, führte begründend den § 6 Abs. 2 lit. d  FLAG 1967 an und verwies auf das vorstehend angeführte Gutachten.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_44`)


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

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
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

- `Finanzamt Wien 9/18/19` — partial — pred is substring of gold: `Finanzamt Wien 9/18/19 Klosterneuburg`
- `Finanzamt Wien 9/18/19` — similar text (different position): `Finanzamt Wien 9/18/19 Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
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

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

**False Positives:**

- `Finanzamtes` — similar text (different position): `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `RgR Amalia Schuetzke`(person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamtes`(organisation)
- `22-967/4918`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes  Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

**False Positives:**

- `Finanzamtes Wien  12/13/14` — partial — pred is substring of gold: `Finanzamtes Wien  12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chen Walcker`(person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `63-698/2600`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien 12/13/14` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Hedwig Mackiewicz`(person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Guntram Antepoth`(person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `70-875/4351`(tax_number)

</details>

---

## `Municipal Authorities` 🏆

**F1:** 0.054 | **Precision:** 0.672 | **Recall:** 0.028  

**Format:** `regex`  
**Rule ID:** `85b56016`  
**Description:**
Matches Magistrat/Magistrats der Stadt Wien variations, including department numbers, and standalone 'Stadt Wien' in legal contexts.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:des|dem|der|vom|von\s+der|der\s+)?\s*((?:Magistrat(?:s)?(?:\s+der\s+Stadt\s+Wien)?(?:,\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?|Stadt\s+Wien))\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.672 | 0.028 | 0.054 | 488 | 328 | 160 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 328 | 160 | 11420 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_4`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens (€ 12,00) ist zusammen mit der  Geldstrafe iHv € 60,00 und dem Beitrag zu den Kosten des erstinstanzlichen Verfahrens  (€ 10,00), insgesamt somit € 82,00, binnen einer Frist von zwei Wochen nach Zustellung des  Straferkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_5`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_9`)


Entscheidungsgründe  Verfahrensgang:   Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien mit Strafverfügung vom  25. April 2019 angelastet, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Vienna am 25. Februar 2019 um 14:35 Uhr in der gebührenpflichtigen  Kurzparkzone in 1090 Wien, Julius-Tandler-Platz 6, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die Parkometerabgabe  fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_22`)


Diese Zeitangabe ist deshalb  glaubwürdig, weil den Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die  Erfüllung der übertragenen Aufgaben elektronische Überwachungsgeräte (sog. PDA's) zur  Verfügung stehen, welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen Server  beziehen und vorgeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_33`)


Die Abgabe ist mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt Wien  vom 22.12.2005, Heft Nr. 51).

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_137`)


Sie haben dadurch folgende Rechtsvorschrift(en() verletzt:   § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung...

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_279`)


Der Magistrat der Stadt Wien ging daher zu Recht von einer zumindest fahrlässigen Verkürzung  der Parkometerabgabe iSd § 4 Abs. 1 Wiener Parkometergesetz 2006 aus.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_128`)


Auf Grund dieser Ausführungen des Verfassungsgerichtshofes hat das Bundesfinanzgericht  keine verfassungsrechtlichen Bedenken gegen die Bestimmungen Parkraumbewirtschaftung  der Stadt Wien, soweit sie im gegenständlichen Fall zur Anwendung gelangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofes` (organisation)
- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_172`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Nach einer bei der Woytekat & Köhlen Recycling KG durchgeführten gemeinsamen Prüfung der Lohnabgaben (GPLA)  setzte der Magistrat der Stadt Wien, Magistratsabteilung 6, Rechnungs- und Abgabenwesen,  mit Bescheid vom 09. März 2017 Kommunalsteuer für den Zeitraum 2012 und 2013 fest und  adressierte den Bescheid an die Beschwerdeführerin.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | `Magistrat der Stadt Wien, Magistratsabteilung 6` |

**Missed by this rule (FN):**

- `Woytekat & Köhlen Recycling KG` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_5`)


III: Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_11`)


Mit Strafverfügung vom 12.3.2019 lastete der Magistrat der Stadt Wien, Magistratsabteilung  67, Techn R Tosca Häfeli, in der Folge kurz mit Bf. bezeichnet, folgende Verwaltungsübertretung an:  "1. Datum/Zeit:  06.06.2018, 09:29 Uhr   Ort:   TATORT   betroffenes Fahrzeug: KENNZ (A)   Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den   Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder   Wochenpauschalkarte) gesorgt zu haben, da der im Fahrzeug angebrachte   Parkausweis für Behinderte gemäß § 29b der StVO kein Original war.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung  67` | `Magistrat der Stadt Wien, Magistratsabteilung  67` |

**Missed by this rule (FN):**

- `Techn R Tosca Häfeli` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_13`)


Verwaltungsübertretung(en) nach:  1. § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der   geltenden Fassung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,   LGBl. für Wien Nr.9/2006 in der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_33`)


Mit Schreiben vom 4.10.2019 verständigte der Magistrat den Bf. vom Ergebnis der  Beweisaufnahme wie folgt:  "Wir teilen Ihnen mit, dass in folgender Angelegenheit eine Beweisaufnahme stattgefunden  hat:  Vorfall vom 06.06.2018 um 09:29 Uhr, TATORT, Übertretung gem. § 5 Abs. 2  Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006,  in der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_85`)


Das Magistrat der Stadt Wien, Magistratsabteilung 67, erließ am 6.11.2019 ein Straferkenntnis,  Zahl GESCHÄFTSZAHL, in welchem die dem Bf. zur Last gelegte Verwaltungsübertretung als  erwiesen angesehen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_88`)


Er habe dadurch folgende Rechtsvorschrift(en) verletzt:  § 5 Abs. 2 Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_441`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_5`)


Die Kosten des Beschwerdeverfahrens (zusammen € 24,00) sind gemeinsam mit den  Geldstrafen (zusammen € 120,00) und dem Beitrag zu den Kosten der belangten Behörde  (zusammen € 20,00), insgesamt somit € 164,00, binnen zwei Wochen nach Zustellung dieses  Erkenntnisses an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_6`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_12`)


Zu 1) MA67/196701153394/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/196701153394 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 1) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_34`)


Zu 2) MA67/1967011579971/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/1967011579971 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 2) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien,  Magistratsabteilung 67` | `Magistrat der Stadt Wien,  Magistratsabteilung 67` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_7`)


Da er die mit Anonymverfügung vorgeschriebene Geldstrafe nicht zahlte, warf der Magistrat  der Stadt Wien dem Beschwerdeführer(Bf.) in der Strafverfügung vom 02. Jänner 2020 vor, er  habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt, dass er das mehrspurige  Kraftfahrzeug mit dem in der Strafverfügung näher bezeichneten behördlichen Kennzeichen  am 4. November 2019 um 17:31 Uhr in einer gebührenpflichtigen Kurzparkzone abgestellt,  ohne für seine Kennzeichnung mit einem zur Tatzeit gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_24`)


Laut Aktenvermerk vom 27. Februar 2020 (Akt Seite 41/58) teilte der Bf. dem Ma- gistrat der Stadt Wien mit, dass er sich dazu nicht äußere.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_26`)


Im Straferkenntnis vom 26. März 2020 warf der Magistrat der Stadt Wien dem Bf. die be- reits in der Strafverfügung vom 02. Jänner 2020 vorgeworfene Verwaltungsübertretung vor,  verhängte über ihn eine Geldstrafe in Höhe von EUR 60,00;

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_28`)


Zur Sach- und Beweislage stellte der Magistrat der Stadt Wien im Wesentlichen fest, der nach  dem Tattag vorgelegte Parkschein beweise nicht, dass er am Tattag zur Tatzeit im hinteren Be- reich des Armaturenbretts lag, weshalb der Bf. das objektive Tatbild der verkürzten Parkome- terabgabe erfüllt habe.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_36`)


Die von mir in der Vernehmung vom 17.01.2020 im Magistrat der  Stadt Wien in … angeführten Angaben wurden keinesfalls ernst genommen.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_45`)


Da  der nach dem Tattag dem Magistrat der Stadt Wien vorgelegte Parkschein nicht auf den Tatort- fotos zu sehen ist, ist als erwiesen anzusehen, dass der Bf. den Parkschein nicht ausgefüllt hat,  nachdem er das Fahrzeug in der gebührenpflichtigen Kurzparkzone geparkt hat.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_79`)


2. Beweiswürdigung  Der Sachverhalt ist auf Grund des Finanzamtsaktes sowie der Eingaben der Bf und der  schriftlichen Aussagen des Herrn C vor der KIAB (nunmehr Finanzpolizei) bzw. des  Strafverfahrens des Magistrats der Stadt Wien gegen die Geschäftsführerin der Bf wegen  illegaler Beschäftigung nach dem AuslBG als erwiesen anzusehen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Finanzpolizei` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_4`)


Ge- mäß § 25 Abs 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_7`)


II. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der  Stadt Wien vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, als unbegründet abge- wiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_10`)


Ge- mäß § 25 Abs 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_16`)


Da der Zulassungsbesitzer angab, seine Ehegattin habe sein Fahrzeug am 11.03.2020 um  10:54 Uhr und am 09.03.2020 um 13:31 Uhr ohne Parkschein in einer gebührenpflichtigen  Kurzparkzone abgestellt und da die Ehegattin die an sie adressierten und für diese Tattage und  Tatzeiten erlassenen Strafverfügungen fristgerecht angefochten hatte, erließ der Magistrat der  Stadt Wien am 24.08.2020 erstens ein an die Ehegattin adressiertes Straferkenntnis zur Ge- schäftszahl MA67/206700639161/2020 und zweitens ein an die Ehegattin adressiertes Strafer- kenntnis zur Geschäftszahl MA67/206700639163/2020.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_17`)


2. Im Straferkenntnis vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, warf der  Magistrat der Stadt Wien der in Folge als Beschwerdeführerin (Bf.) bezeichneten Ehegattin des  Zulassungsbesitzers vor, sie habe die Wiener Parkometerabgabe dadurch fahrlässig verkürzt,  dass sie das mehrspurige Kraftfahrzeug ihres Ehegatten mit dem im Straferkenntnis näher be- zeichneten behördlichen Kennzeichen am 11.03.2020 um 10:54 Uhr in einer gebührenpflichti- gen Kurzparkzone abgestellt habe, ohne für seine Kennzeichnung mit einem gültigen Park- schein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_18`)


Die dadurch verletzten Rechtsvorschriften waren § 5 Abs 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idgF in Verbindung mit § 4  Abs 1 Wiener Parkometergesetz 2006 LGBl. für Wien Nr. 9/2006 idgF.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_21`)


Im Straferkenntnis vom 24.08.2020, Geschäftszahl MA67/206700639163/2020, warf der Ma- gistrat der Stadt Wien der Bf. vor, sie habe die Wiener Parkometerabgabe dadurch fahrlässig  verkürzt, dass sie das mehrspurige Kraftfahrzeug ihres Ehegatten mit dem im Straferkenntnis  näher bezeichneten behördlichen Kennzeichen am 09.03.2020 um 13:31 Uhr in einer gebüh- renpflichtigen Kurzparkzone abgestellt habe, ohne für seine Kennzeichnung mit einem gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_22`)


Die dadurch verletzten Rechtsvorschriften waren § 5 Abs 2 Wie- ner Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idgF in Verbindung mit § 4  Abs 1 Wiener Parkometergesetz 2006 LGBl. für Wien Nr. 9/2006 idgF.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_29`)


Die Bf. habe den Magistrat der Stadt  Wien ersucht zu prüfen, ob statt Geldstrafen zu verhängen, Ermahnungen erteilt werden kön- nen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_30`)


Der Magistrat der Stadt Wien stellte fest, die Bf. hätte an beiden Tattagen jeweils einen  Parkschein im Fahrzeug hinterlegen müssen und da sie dies nicht tat, habe sie am 11.03.2020  um 10:54 Uhr und davor am 09.03.2020 um 13:31 Uhr die ihr vorgeworfenen Verwaltungs- übertretungen begangen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_39`)


4. Am 17.03.2020 erließ der Magistrat der Stadt Wien die Verordnung über die vorüberge- hende Aufhebung der Wiener Kurzparkzonen bis auf Widerruf.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_3`)


Am Ausspruch des Magistrats der Stadt Wien, dass der Beschwerdeführer gem. § 64 Abs. 2  VStG 1991 einen Beitrag zu den Kosten des erstinstanzlichen Strafverfahrens zu zahlen hat, tritt  keine Änderung ein.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_4`)


III. Der Magistrat der Stadt Wien wird gem. § 25 Abs. 2 BFGG als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_5`)


Der Beitrag zu den Kosten des Beschwerdeverfahrens i.H.v. 12 € ist zusammen mit der  Geldstrafe i.H.v. 60 € und dem Beitrag zu den Kosten des behördlichen Verfahrens i.H.v. 10 €,  somit insgesamt i.H.v. 82 €, an den Magistrat der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_9`)


Entscheidungsgründe  Mit Strafverfügung vom 6. Juli 2020 zu Zahl MA67/Zahl1/2020, wurde der Beschwerdeführer  (Bf.) schuldig erkannt, er habe am 06. Mai 2020 um 16:33 Uhr in einer näher genannten  Kurzparkzone in 1030 Wien, Guglgasse 1, mit dem mehrspurigen Kraftfahrzeug mit dem  behördlichen Kennzeichen W-123 (A) durch Abstellen des Fahrzeuges ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültig entwerteten Parkschein  gesorgt zu haben, eine Verwaltungsübertretung gem. § 5 Abs. 2  Parkometerabgabeverordnung, Abl. der Stadt Wien Nr. 51/2005, in der geltenden Fassung, in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, begangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_39`)


Im angefochtenen Straferkenntnis der MA 67 vom 18. September 2020 zur Zahl  MA67/Zahl1/2020 wird zum Einspruch vom 23. Juli 2020 wie folgt ausgeführt:  Der Bf. habe am 06. Mai 2020 um 16:33 Uhr in einer gebührenpflichtigen Kurzparkzone in 1030  Wien, Guglgasse 1, mit dem nach dem behördlichen Kennzeichen W-123 (A) bezeichneten  mehrspurigen Kfz durch Abstellen des Fahrzeuges ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben eine  Verwaltungsübertretung gem. § 5 Abs. 2 Parkometerabgabeverordnung, Abl. der Stadt Wien  Nr. 51/2005, in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, begangen.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_57`)


Der Bf. habe dadurch folgende Rechtsvorschriften verletzt:  § 5 Abs. 2 Parkometerabgabeverordnung, Abl. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der geltenden Fassung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_91`)


Als Beweis  in der Anlage finden Sie: Fotos vom Beanstandungsort, Google Maps Plan und Park Plan der  Stadt Wien sowie den ursprünglichen Einspruch und das Straferkenntnis.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_98`)


Die vom Bf. ins Treffen geführten von ihm vorgelegten  Fotos vom Beanstandungsort, sein Hinweis auf Google Maps Plan und auf den Park Plan der  Stadt Wien ändern an dieser Feststellung nichts.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_148`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_3`)


III. Der Beitrag zu den Kosten des Beschwerdeverfahrens ist zusammen mit der Geldstrafe und  dem Beitrag zu den Kosten des behördlichen Verfahrens an den Magistrat der Stadt Wien zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_4`)


Der Magistrat der Stadt Wien wird gemäß § 25 Abs. 2 BFGG als  Vollstreckungsbehörde bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_150`)


Hier erweist sich das Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_157`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `Magistrats der  Stadt Wien` | `Magistrats der  Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_18`)


Im elektronisch vorgelegten Akt befinden sich Ablichtungen von (Schulbesuchs-)Bestätigungen  und Zeugnissen sowie die erste Seite eines Bescheides des Magistrats der Stadt Wien für den  streitgegenständlichen Zeitraum.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_66`)


Dem Bf wurde laut Bescheid des Magistrats der Stadt Wien vom 06.10.2015, Betreff:  „Mindestsicherung, Zuerkennung“ eine Leistung zur Deckung des Lebensunterhalts und der  Grundbetrag zur Deckung des Wohnbedarfs ab November 2015 bis jedenfalls August 2016  zuerkannt.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_13`)


Das betreffende Kind befand sich ab 6.2.2019 in voller Erziehung der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_37`)


Sie befinden sich seit April 2019 in voller Erziehung der Stadt Wien und sind in einer  sozialpädagogischen Einrichtung Fremduntergebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_54`)


Das betreffende Kind befand sich ab 6.2.2019 in voller Erziehung der Stadt Wien.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_75`)


Der Bf. befindet sich seit 16.05.2019 im Krisenzentrum Pleischlgasse, einer  sozialpädagogischen Einrichtung der Stadt Wien, und erzielte seit Ende September 2019 eine  Lehrlingsentschädigung.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_92`)


II. Das Bundesfinanzgericht hat erwogen:  Der durch den Kinder- und Jugendhilfeträger Wien (Regionalstelle Rechtsvertretung Bezirke  13,14, 15) vertretene Bf. befand sich im beschwerdegegenständlichen Zeitraum - Mai 2019 bis  Juli 2020 -in voller Erziehung der Stadt Wien und war in einer sozialpädagogischen Einrichtung  fremduntergebracht.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_98`)


Dieser Sachverhalt ist unstrittig und ergibt sich aus dem oben wiedergegebenen Akteninhalt.  Die Beurteilung, ob der Kinder- und Jugendhilfeträger Wien als Vertreter des Bf. zu Recht für  den vergangenen Zeitraum Mai 2019 bis Juli 2020 – in welchem sich der Bf. bereits in voller  Erziehung der Stadt Wien befunden hatte und in einer sozialpädagogischen Einrichtung  fremduntergebracht war (!) – Familienbeihilfe geltend machen konnte oder nicht, ergibt  Folgendes:  Dem Beschluss des Obersten Gerichtshofes vom 20.05.2020, 6 Ob 62/20s (der Bescheid vom  11. August 2020 nennt das Datum 20.5.2020, keine GZ), lag Folgendes zugrunde:  Am 16.7.2019 beantragte der Kinder- und Jugendhilfeträger (KJHT) seine Betrauung mit der  Vermögensverwaltung im Umfang der Beantragung und Verwaltung des Eigenanspruchs des  Kindes auf Familienbeihilfe;

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_149`)


Im Hinblick auf den Umstand, dass sich der Bf. im beschwerdegegenständlichen ‚vergangenen  Zeitraum‘ Mai 2019 bis Juli 2020 bereits in voller Erziehung der Stadt Wien befunden hatte und  in einer sozialpädagogischen Einrichtung fremduntergebracht war, lassen die  höchstgerichtlichen Entscheidungen keinen Zweifel an der Richtigkeit des in der Beschwerde  bzw. im Vorlageantrag vertretenen Standpunktes.

| Predicted | Gold |
|---|---|
| `Stadt Wien` | `Stadt Wien` |

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_63`)


2014 war die Basis der Gewerbeausübung des Bf gemäß  §§ 339f GewO 1994 die aufgrund seiner Anmeldung (Anzeige) erfolgte Eintragung in das  Gewerberegister gewesen, die ihm am 27.Febr.2012 gemäß § 340 GewO 1994 durch  Übermittlung eines Auszugs aus dem Gewerberegister durch das Magistrat Graz/Referat  Gewerbeverfahren mitgeteilt worden war.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_146`)


Unter Einem wurde ein Bescheid des Magistrat Graz vom 4.8.1999 vorgelegt, mit welchem der  Bf. die Bewilligung zur Fortführung eines Bordells in ihrem Lokal (unter näher genannten  Auflagen) erteilt wurde.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_158`)


Mit Bescheid vom 4.8.1999 wurde ihr vom zuständigen Magistrat  gemäß den maßgeblichen Bestimmungen des Steiermärkischen Prostitutionsgesetzes (LGBl.  Nr. 16 vom 27.2.1998) die Bewilligung zum Betrieb bzw. zur Fortführung eines Bordells (einer  bordellähnlichen Einrichtung) unter den auszugsweise oben wörtlich wieder gegebenen  Auflagen erteilt. In der behördlich aufliegenden Hausordnung heißt es unter Punkt 10.: „Der  vom Betrieb für die Leistung der Prostituierten festgesetzte Preis darf nur von der  Betriebsleitung, nicht aber von der Prostituierten selbst, eingehoben werden.“

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien,  MA 67` — partial — gold is substring of pred: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Verwaltungsstrafsache gegen  Andrea Thünnissen, Kellergasse Helfens 32, 8074 Raaba, Österreich, vom 23. Februar 2020, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Februar 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 17. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet  abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien, MA 67` — partial — gold is substring of pred: `Magistrat der Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Andrea Thünnissen`(person)
- `Kellergasse Helfens 32, 8074 Raaba, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_3`)


Nr.  10/2013 über die Beschwerde des Beschuldigten vom 20. November 2019 gegen das  Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 6. November 2019,  Zahl: MA 67/186700510526/2018 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`
- `Stadt Wien` — similar text (different position): `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_8`)


Entscheidungsgründe  Mit Schreiben des Magistrates der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung, wurde VN-F NN als Zulassungsbesitzerin gemäß § 2 Parkometergesetz  2006, LBGl. für Wien Nr. 9/2006 in der geltenden Fassung aufgefordert, bekanntzugeben, wem  1 von 28 Seite 2 von 28

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_31`)


Mit Schreiben des Magistrates der Stadt Wien, Magistratsabteilung 67, wurde der Bf. als jene  Person, die das ihr vom Zulassungsbesitzer des mehrspurigen Kraftfahrzeuges mit dem  behördlichen Kennzeichen KENNZ zur Verfügung gestellte Fahrzeug einem Dritten überlassen  hat, gemäß § 2 Parkometergesetz 2006, LBGl. für Wien Nr. 9/2006 in der geltenden Fassung  aufgefordert, bekanntzugeben, wem sie das mehrspurige Kraftfahrzeug mit dem genannten  Kennzeichen am 6.6.2018 um 09:29 Uhr überlassen gehabt habe, sodass es zu diesem  Zeiptunkt in TATORT gestanden sei.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_33`)


Mit Schreiben vom 4.10.2019 verständigte der Magistrat den Bf. vom Ergebnis der  Beweisaufnahme wie folgt:  "Wir teilen Ihnen mit, dass in folgender Angelegenheit eine Beweisaufnahme stattgefunden  hat:  Vorfall vom 06.06.2018 um 09:29 Uhr, TATORT, Übertretung gem. § 5 Abs. 2  Parkometerabgabeverordnung, ABI. der Stadt Wien Nr. 51/2005, in der geltenden  Fassung, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006,  in der geltenden Fassung.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_92`)


Begründend führte der Magistrat wie folgt aus:  "Sie haben das verfahrensgegenständliche Kraftfahrzeug an der im Spruch bezeichneten  Örtlichkeit abgestellt, sodass es dort zur angeführten Zeit ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder  6 von 28 Seite 7 von 28

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_283`)


Frage: Ist Ihre Beurteilung als Fälschung schon einmal im Rechtsmittelverfahren (vor dem  Magistrat oder dem Bundesfinanzgericht) widerlegt worden?

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_316`)


Mit Mail vom 26.8.2020 übermittelte die Richterin dem Bf. per Mail die Beweisfotos, das  Schreiben, welches der Magistrat an Dr. YYY gerichtet hatte, den Rückschein, die Niederschrift  über die mündliche Verhandlung und ein Schreiben, dessen Inhalt in der Folge wiedergegeben  wird:  "Anbei wird die Niederschrift der heutigen mündlichen Verhandlung übermittelt, in welcher die  Zeugin (das Organ der Parkraumüberwachung, welches die Anzeige gelegt hat, Frau ZEUGIN)  einvernommen wurde.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. YYY`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_319`)


Dies war für den Magistrat nicht überprüfbar, weil ein Vera Schliephacke an der  angegebenen Adresse nicht bekannt war.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vera Schliephacke`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_322`)


Eine Überprüfung war dem Magistrat daher nicht möglich.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_406`)


Bei der Strafbemessung hat das Magistrat berücksichtigt, dass durch das rechtswidrig  abgestellte Kraftfahrzeug der Schutzzweck der Norm, nämlich die ordnungsgemäße  Entrichtung der Parkometerabgabe und die Rationierung des Parkraumes, in nicht  unerheblichem Maß verletzt worden ist.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_419`)


Als mildernd hat das Magistrat das Fehlen von Vorstrafen nach dem Wiener Parkometergesetz  angenommen.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)


Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, Prof.in StR DDr.in Reneé Plein  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

**False Positives:**

- `Magistrat der Stadt Wien, MA 67` — partial — gold is substring of pred: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Prof.in StR DDr.in Reneé Plein`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_57`)


Der Magistrat legte die Beschwerden samt den dazugehörigen Verwaltungsakten dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 27. Mai 2020).

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_69`)


Rechtsgrundlagen:   § 2 Wiener Parkometergesetz 2006 normiert:   (1) Der Zulassungsbesitzer und jeder, der einem Dritten das Lenken eines mehrspurigen  Kraftfahrzeuges oder die Verwendung eines mehrspurigen Kraftfahrzeuges überlässt, für  dessen Abstellen gemäß Verordnung des Wiener Gemeinderates eine Parkometerabgabe zu  entrichten war, hat, falls das Kraftfahrzeug in einer gebührenpflichtigen Kurzparkzone gemäß §  25 StVO 1960, BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005,  abgestellt war, dem Magistrat darüber Auskunft zu geben, wem er das Kraftfahrzeug zu einem  bestimmten Zeitpunkt überlassen gehabt hat.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_126`)


Für allfällige Ratenvereinbarungen ist der Magistrat zuständig.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_37`)


Ich beantrage die  Durchführung einer öffentlichen mündlichen Verhandlung und werde zu dieser auch mein Fahr- zeug mitnehmen, damit vor Ort ein Lokalaugenschein möglich ist, da bis jetzt vom Magistrat  nicht erkannt wurde, wo mein Parkschein hinterlegt war und ich dies zeigen möchte.“

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_8`)


Am 27.8.2009 erließ der Magistrat Wien ein diesbezügliches Straferkenntnis gegen die  Geschäftsführerin wegen illegaler Ausländerbeschäftigung nach § 28 Abs: 1 Z 1 lit.a iVm § 3 Abs  1 AuslBG.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_74`)


Am 27.8.2009 erließ der Magistrat Wien ein diesbezügliches Straferkenntnis gegen die  Geschäftsführerin wegen illegaler Ausländerbeschäftigung nach § 28 Abs: 1 Z 1 lit.a iVm § 3 Abs  1 AuslBG.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `Susette Volmari`(person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_156`)


Für allfällige Ratenvereinbarungen ist der Magistrat zuständig.

**False Positives:**

- `Magistrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_19`)


Mit Vorhalt vom 15.12.2020 ersuchte das Bundesfinanzgericht den Bf, nachstehende Fragen zu  beantworten und die angesprochenen Unterlagen vorzulegen:  1) Vorzulegen sei nicht nur das Deckblatt, sondern der gesamte Bescheid des Magistrates der  Stadt Wien vom 06.10.2015 betreffend „Mindestsicherung, Zuerkennung“.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Magistrates der  Stadt Wien`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


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

</details>

---

## `European Institutions` 

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2b696a75`  
**Description:**
Matches European institutions like Europäische Gerichtshof and Europäische Union.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*(Europäische\s+Gerichtshof(?:s)?|Europäische\s+Union|Statistisches\s+Amt\s+der\s+Europäischen\s+Union)\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.000 | 0.001 | 9 | 3 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 6 | 11745 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_61`)


Schließlich ist auch aus unionsrechtlichen Gründen ein Anrechnungsvortrag für ausländische  Quellensteuern auf Dividenden nicht geboten: Wie der Europäische Gerichtshof in seinem Urteil  vom 10. Februar 2011, verbundene Rechtssachen C-436/08 und C-437/08 - Haribo und  Österreichische Salinen -, ausgesprochen hat, sind die Mitgliedstaaten beim gegenwärtigen  Stand des Unionsrechts nicht verpflichtet, die Anrechnung der in einem anderen  (Mitglied- )Staat auf Dividenden erhobenen Quellensteuer vorzusehen, um zu verhindern, dass  6 von 8 Seite 7 von 8

| Predicted | Gold |
|---|---|
| `Europäische Gerichtshof` | `Europäische Gerichtshof` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_170`)


Absehen von der mündlichen Verhandlung  Der Europäische Gerichtshof für Menschenrechte hat zu Art 6 EMRK die Auffassung vertreten,  dass die Durchführung einer mündlichen Verhandlung nicht geboten ist, wenn etwa keine  Fragen der Beweiswürdigung auftreten oder die Tatsachenfeststellungen nicht bestritten sind,  sodass eine Verhandlung nicht notwendig ist und das Gericht aufgrund des schriftlichen  Vorbringens und der schriftlichen Unterlagen entscheiden kann.

| Predicted | Gold |
|---|---|
| `Europäische Gerichtshof` | `Europäische Gerichtshof` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_491`)


Der Europäische Gerichtshof betont, dass die Mitgliedstaaten bei einer im Wesentlichen  dauerhaften Nutzung eines ausländischen Fahrzeuges in ihrem Hoheitsgebiet eine  Zulassungssteuer erheben dürfen.

| Predicted | Gold |
|---|---|
| `Europäische Gerichtshof` | `Europäische Gerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_79`)


Es sei aber nicht nur ein großer Tag für  Österreich, sondern auch für die Europäische Union.

**False Positives:**

- `Europäische Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_215`)


Zudem sei es wichtig, sich auf möglichst einheitliche  Reisebestimmungen für die Europäische Union zu einigen, insbesondere betreffend die Einreise  aus Drittstaaten.

**False Positives:**

- `Europäische Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_102`)


Das Bundesfinanzgericht legte dem Gerichtshof der Europäischen Union gemäß Artikel 267  AEUV folgende Frage zur Vorabentscheidung vor:  "Sind Artikel 18 und Artikel 45 Absatz 1 des Vertrags über die Arbeitsweise der Europäischen  Union, Artikel 7 Absätze 1 und 2 der Verordnung (EG) Nr. 492/2011 des Europäischen  Parlaments und des Rates vom 5. April 2011 über die Freizügigkeit der Arbeitnehmer innerhalb  der Union, Artikel 4, Artikel 5 Buchstabe b, Artikel 7 und Artikel 67 der Verordnung (EG) Nr.  883/2004 des Europäischen Parlaments und des Rates vom 29. April 2004 zur Koordinierung  der Systeme der sozialen Sicherheit sowie Artikel 60 Absatz 1 Satz 2 der Verordnung (EG) Nr.  987/2009 des Europäischen Parlaments und des Rates vom 16. September 2009 zur Festlegung  der Modalitäten für die Durchführung der Verordnung (EG) Nr. 883/2004 über die Koordi- nierung der Systeme der sozialen Sicherheit dahin auszulegen, dass sie der Anwendung einer  nationalen Regelung entgegenstehen, die vorsieht, dass Familienleistungen für ein Kind, das  sich nicht tatsächlich ständig in dem diese Familienleistungen zahlenden Mitgliedstaat, sondern  tatsächlich in einem anderen Mitgliedstaat der Europäischen Union, einer anderen Vertrags- partei des Abkommens über den Europäischen Wirtschaftsraum oder der Schweiz aufhält, auf  Basis der vom Statistischen Amt der Europäische Union veröffentlichten vergleichenden Preis- niveaus für den jeweiligen Staat im Verhältnis zu dem die Familienleistungen zahlenden  Mitgliedstaat anzupassen?"

**False Positives:**

- `Europäische Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)
- `Europäischen  Union`(organisation)
- `Europäischen Parlaments`(organisation)
- `Europäischen Parlaments`(organisation)
- `Europäischen Union`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_13`)


In der Folge wurde gemäß § 271 Bundesabgabenordnung (BAO) die Entscheidung über die  verfahrensgegenständliche Beschwerde bis zur Beendigung des beim EuGH anhängigen  Vorabentscheidungsverfahrens C-163/20 anhängigen Verfahrens ausgesetzt, da der Ausgang  dieses Verfahrens hinsichtlich der Frage, ob Artikel 18 und Artikel 45 Absatz 1 des Vertrags  über die Arbeitsweise der Europäischen Union, Artikel 7 Absätze 1 und 2 der Verordnung (EG)  Nr. 492/2011 des Europäischen Parlaments und des Rates vom 5. April 2011 über die  Freizügigkeit der Arbeitnehmer innerhalb der Union, Artikel 4, Artikel 5 Buchstabe b, Artikel 7  und Artikel 67 der Verordnung (EG) Nr. 883/2004 des Europäischen Parlaments und des Rates  vom 29. April 2004 zur Koordinierung der Systeme der sozialen Sicherheit sowie Artikel 60  Absatz 1 Satz 2 der Verordnung (EG) Nr. 987/2009 des Europäischen Parlaments und des Rates  vom 16. September 2009 zur Festlegung der Modalitäten für die Durchführung der Verordnung  (EG) Nr. 883/2004 über die Koordinierung der Systeme der sozialen Sicherheit dahin  auszulegen sind, dass sie der Anwendung einer nationalen Regelung entgegenstehen, die  vorsieht, dass Familienleistungen für ein Kind, das sich nicht tatsächlich ständig in dem diese  Familienleistungen zahlenden Mitgliedstaat, sondern tatsächlich in einem anderen  Mitgliedstaat der Europäischen Union, einer anderen Vertragspartei des Abkommens über den  Europäischen Wirtschaftsraum oder der Schweiz aufhält, auf Basis der vom Statistischen Amt  der Europäische Union veröffentlichten vergleichenden Preisniveaus für den jeweiligen Staat  2 von 14 Seite 3 von 14

**False Positives:**

- `Europäische Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Europäischen Union`(organisation)
- `Europäischen Parlaments`(organisation)
- `Europäischen Parlaments`(organisation)
- `Europäischen Parlaments`(organisation)
- `Europäischen Union`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_13`)


In ihrer Beschwerde führt die Bf zum rechtlichen Zusammenhang aus, dass im Zuge der  gestiegenen Energiepreise nach der russischen Invasion der Ukraine die Europäische Union im  Oktober 2022 die EU-Notfallmaßnahmen-VO (EU-VO 2022/1854) beschlossen habe.

**False Positives:**

- `Europäische Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_73`)


Abstandnahme von der Durchführung einer mündlichen Verhandlung:     Im Urteil EGMR 18.07.2013, Nr. 56.422/09 (Schädler-Eberle-Liechtenstein) hat der Europäische  Gerichtshof für Menschenrechte festgestellt, dass es Verfahren gibt, in denen eine  Verhandlung nicht geboten sei, etwa wenn keine Fragen der Beweiswürdigung auftreten oder  die Tatsachenfeststellung nicht bestritten ist, sodass eine Verhandlung nicht notwendig ist, und  das Gericht auf Grund des schriftlichen Vorbringens und der schriftlichen Unterlagen  entscheiden kann (vgl. VwGH 27.08.2014, 2013/05/0009;

**False Positives:**

- `Europäische  Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Companies with Legal Form` 🏆

**F1:** 0.037 | **Precision:** 0.325 | **Recall:** 0.019  

**Format:** `regex`  
**Rule ID:** `1a473a98`  
**Description:**
Matches company names ending in GmbH, AG, KG, etc., allowing for long names with 'und', hyphens, and multiple words before the legal form.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:der|des|dem|der\s+)?\s*((?:See\s+)?[A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+(?:GmbH|AG|KG|OHG|UG|mbH|\.\s*mbH))\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.325 | 0.019 | 0.037 | 704 | 229 | 475 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 229 | 475 | 11519 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_23`)


Mit Übergabevertrag vom 12. Juli 2012 habe der Bf. die Wohnung wiederum seinem Sohn zu  einem Übergabepreis in Höhe der per 26. Juni 2012 offenen Kreditforderung der Bank AG mit  einem offenen Saldo von EUR 110.461,17 übergeben.

| Predicted | Gold |
|---|---|
| `Bank AG` | `Bank AG` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_89`)


Der Übernehmer erklärt ferner in Kenntnis  des zwischen der Bank AG und dem Übergeber bestehenden Kreditvertrages zu sein und  verpflichtet sich ausdrücklich, in sämtliche Rechte und Pflichten aus dem Kreditvertrag  einzutreten.“

| Predicted | Gold |
|---|---|
| `Bank AG` | `Bank AG` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_127`)


Informativ wird mitgeteilt, dass die Einzahlung auf folgendes Bankkonto des Magistrats der  Stadt Wien bei der UniCredit Bank Austria AG zu erfolgen hat:  Empfänger: MA 6 - BA 32 – Verkehrsstrafen IBAN: AT13 1200 0100 2281 3611 (BIC:  BKAUATWWXXX).

| Predicted | Gold |
|---|---|
| `UniCredit Bank Austria AG` | `UniCredit Bank Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der  Stadt Wien` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `TPA Steuerberatung GmbH` | `TPA Steuerberatung GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Isidor Czebulla` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `PROCURA Steuerberatung  GmbH` | `PROCURA Steuerberatung  GmbH` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Hon.-Prof. Clemens Mooß` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Treuhand Steuerberatung GmbH` — partial — pred is substring of gold: `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
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

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_33`)


Auf der Liegenschaft wurde auf Name und Rechnung der A- KG ein Einfamilienhaus mit Doppelgarage und Carport errichtet.

**False Positives:**

- `A- KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_1`)


Entscheidungsgründe Mit Erkenntnis des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016 wurde der nunmehrige Beschwerdeführer N.N. (in der Folge kurz Bf. genannt) der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG für schuldig erkannt, er habe fahrlässig unter Verletzung der ihm gemäß § 10 Grunderwerbsteuergesetz obliegenden Anzeige-, Offenlegungs- und Wahrheitspflicht, indem er es als anzeigepﬂichtiger Erwerber unterlassen habe, den Kaufvertrag mit A.B. vom 07.01.2013 betreffend die Liegenschaft EZ Berg-Bildung KG  Ortsname bis zum 15.

**False Positives:**

- `Liegenschaft EZ Berg-Bildung KG` — partial — gold is substring of pred: `Berg-Bildung KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes für Gebühren`(organisation)
- `N.N.`(person)
- `A.B.`(person)
- `Berg-Bildung KG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_50`)


Mit dem hier angefochtenen Erkenntnis der Finanzstrafbehörde vom 05.12.2016 wurde der Bf. der fahrlässigen Abgabenverkürzung nach § 34 Abs. 1 FinStrG für schuldig erkannt, er habe fahrlässig unter Verletzung der ihm gemäß § 10 Grunderwerbsteuergesetz obliegenden Anzeige-, Offenlegungs- und Wahrheitspflicht, indem er es als anzeigepﬂichtiger Erwerber unterlassen habe, den Kaufvertrag mit A.B. vom 07.01.2013 betreffend die Liegenschaft EZ Berg-Bildung KG  Ortsname bis zum 15.

**False Positives:**

- `Liegenschaft EZ Berg-Bildung KG` — partial — gold is substring of pred: `Berg-Bildung KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `A.B.`(person)
- `Berg-Bildung KG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Partner Steuerberatung GmbH` — partial — pred is substring of gold: `ECA Mag. Pichler & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Partner GmbH` — partial — pred is substring of gold: `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Ophelia Dutschka`(person)
- `Diepolding 3, 3754 Trabenreith, Österreich`(address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_7`)


Mit Baurechtsvertrag vom 05.08.2004 war der F KG als  Baurechtsnehmerin von der Wohlgemut Getränke GmbH& Co KG ein Baurecht gegen monatliches Entgelt  eingeräumt worden.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_15`)


Die KG als Eigentümerin der Liegenschaft ist eine von den  Gesellschaftern zu unterscheidende und selbständige Rechtspersönlichkeit.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_24`)


Einziger Unternehmensgegenstand der F KG war die  Vermietung des Baurechtes Villach an die gewerblich tätige Wohlgemut Getränke GmbH& Co KG  (Mitunternehmerschaft), an der Herr F als alleiniger Kommanditist  zu 100% beteiligt war.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH&`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_26`)


Nach dem Ableben von Herrn F erwarb unsere Mandantin im Erbwege (unentgeltlich) unter  anderem sämtliche Kommanditanteile des Herrn F an der Wohlgemut Getränke GmbH& Co KG sowie an der F KG.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH&`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_34`)


Im vorliegenden Fall ist nämlich der anwachsungsbedingte Erwerb des Grundstücks nicht  isoliert sondern in Zusammenschau mit dem Erwerb der Mitunternehmeranteile an der Wohlgemut Getränke GmbH & Co KG sowie des damit in Verbindung stehenden Sonderbetriebsvermögens zu sehen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_38`)


Dementsprechend richtet sich  die Einstufung, ob es sich bei dem Baurecht um Sonderbetriebsvermögen gehandelt habe und  somit die Befreiungsbestimmung des § 3 Abs. 1 Z 2 lit. a zweiter Teilstrich GrEStG anzuwenden  wäre, da der anwachsungsbedingte Erwerb nicht isoliert, sondern in Zusammenschau mit dem  Erwerb der Mitunternehmeranteile an der Wohlgemut Getränke GmbH& Co KG sowie des damit in Verbindung  stehenden Sonderbetriebsvermögens zu bewerten wäre.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_45`)


Nachdem das Baurecht an die Wohlgemut Getränke GmbH& Co KG entgeltlich zur Nutzung  überlassen wurde stellte dieses in Bezug auf Herrn F (99%) Sonderbetriebsvermögen der Wohlgemut Getränke GmbH& Co KG dar.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)
- `Wohlgemut Getränke GmbH&`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_48`)


Aufgrund der entgeltlichen Nutzungsüberlassung lag Sonderbetriebsvermögen  der Wohlgemut Getränke GmbH& Co KG.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH&`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_49`)


Herr F übertrug von Todes wegen unentgeltlich dieses  Sonderbetriebsvermögen (Baurechtseinlage EZ 2 KG XY) der Wohlgemut Getränke GmbH& Co KG bei gleichzeitiger  Zuwendung von 100% der Mitunternehmeranteile der Wohlgemut Getränke GmbH& Co an Frau A. Der Begriff  Sonderbetriebsvermögen  in § 3 Abs. 1 Z 2 lit a zweiter Teilstrich GrEStG ist ertragsteuerlich zu definieren.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)
- `Wohlgemut Getränke GmbH&`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_66`)


Nach Einsicht in den Baurechtsvertrag wurde vom Gericht festgestellt,  dass die F KG Baurechtsnehmerin und die Wohlgemut Getränke GmbH& Co KG Baurechtsgeberin war und nicht –  wie von der Bf erklärt „das Baurecht an die Wohlgemut Getränke GmbH& Co KG entgeltlich zur Nutzung  überlassen wurde.“

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)
- `Wohlgemut Getränke GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_131`)


Um letztendlich noch auf den Einwand des Sonderbetriebsvermögens der Wohlgemut Getränke GmbH&  Co KG einzugehen wird festgehalten, dass das Baurecht (= Grundstück) gegenständlich nicht als  Sonderbetriebsvermögen der KG zur Nutzung überlassen worden war, sondern sich vielmehr  im Eigentum der KG (siehe Grundbuchsauszug) befunden hat.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Steuerberatung GmbH` — partial — pred is substring of gold: `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Steuerberater  KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_18`)


Es wurden EUR 200,00 an Vorsteuern im Zusammenhang mit der  vorgelegten Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 anstatt EUR 11.220,00 anerkannt.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_31`)


Die GmbH sei am Datum1 amtswegig im Firmenbuch gelöscht worden.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_82`)


Am TTMM 2016 erging eine an die Bf. gerichtete Rechnung der Kraußkopf Chemie GmbH iHv EUR 1.000,00  netto zuzüglich EUR 200,00 Umsatzsteuer.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_126`)


Somit waren bereits im beschwerdegegenständlichen Zeitraum die materiellen  Voraussetzungen für die Entstehung des Vorsteuerabzuges erfüllt.  Deshalb und da die Anerkennung des Vorsteuerabzuges iHv EUR 200,00 aus der Rechnung der Kraußkopf Chemie GmbH vom TTMM 2016 unstrittig war, war spruchgemäß zu entscheiden.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Kraußkopf Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraußkopf Chemie GmbH`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_9`)


Bei einer Kontrolle am  18.2.2015, 15:15 Uhr, befand sich das Fahrzeug in B am Parkplatz der Fa.NiederImmobilien Institut GmbH  Der Bf sei  von April 2010 bis Juni 2013 – dh. im Zeitraum der Einbringung des Fahrzeuges - an  1 von 29 Seite 2 von 29

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_19`)


Diese Leasingfirma ist in Konkurs gegangen und aus diesem Grund hat mich die Fa.NiederImmobilien Institut GmbH im Oktober 2012 übernommen und bin seitdem Vollzeit mit 42,5 Stunden pro Woche  beschäftigt.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_46`)


Auf  die Frage, warum ich dieses KFZ in Deutschland angemeldet habe, gebe ich an, dass ich nicht  weiß, wie lange ich hier bleibe, da es sein kann, dass ich bei der Fa.NiederImmobilien Institut GmbH kündigen werde.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_77`)


e) Bestätigung der Sozialversicherung v. Oktober 2012:  Demnach ist der Bf ab 22.10.2012 bei der Fa.NiederImmobilien Institut GmbH als Arbeiter/Hilfskraft vollbeschäftigt (=  40 Wochenstunden) und erhält einen Monatslohn von brutto € 1.513,60.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_90`)


Aufgrund der  seit 22.10.2012 bestehenden Vollzeitbeschäftigung bei der Fa.NiederImmobilien Institut GmbH liege ein quantitativ  überwiegender Aufenthalt samt Wohnsitz im Inland vor, weshalb sich der Mittelpunkt der  Lebensinteressen des Bf in Österreich befinde.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_142`)


c) 1 Konvolut an monatlichen Arbeitszeitnachweislisten des Bf bei der Fa.NiederImmobilien Institut GmbH  Zeitraum  Jänner 2014 – Dezember 2015:  Eine nähere Überprüfung durch das BFG hat in Gegenüberstellung des Arbeitszeitnachweises  (siehe untentstehend 2 rechte Spalten) zu den vom Bf vorgelegten Aufzeichnungen seiner  "Heimfahrten" Ö-D-Ö (siehe untenstehend die 2 linken Spalten) folgende Divergenzen  ergeben:    Fahrten Ö-D-Ö lt.  Aufzeichnung Bf    Lt. Zeitnachweisliste  des Arbeitgebers

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)
- `BFG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_152`)


c) Abfrage der Sozialversicherungs-Daten:  Demnach war der Bf ab 22.10.2012 – 16.4.2016 und ist seit 6.6.2016 laufend als Arbeiter bei  der Fa.NiederImmobilien Institut GmbH in B (Ö) als Arbeiter beschäftigt, Bruttogehalt 2014/2015 jährlich rund €  33.000.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_166`)


3.) Einsicht in die Sozialversicherungs-Daten:  Der Bf war mit kurzzeitigen Unterbrechungen, in denen meist Arbeitslosengeld bezogen  wurde, ab 5.5.2008 bis 21.10.2012 bei E und ab 22.10.2012 bei der Fa.NiederImmobilien Institut GmbH beschäftigt.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_186`)


2. Berufliche/wirtschaftliche Nahebeziehung:  Fest steht nach dem Akteninhalt und bisher durchgeführten Erhebungen, dass der  Beschwerdeführer Sven Mitterhuber (Bf) ab 2009 im Inland berufstätig bzw. jedenfalls im strittigen  Zeitraum durchgehend bei der Fa.NiederImmobilien Institut GmbH in Vollzeit (42,5 Stunden/Woche) beschäftigt war  und laut Abfrage der Sozialversicherungsdaten nach wie vor ist.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sven Mitterhuber`(person)
- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_189`)


Im Rahmen einer Betrachtung der beruflichen und wirtschaftlichen Beziehungen wäre daher  nach Ansicht des BFG insgesamt von einer weitaus überwiegenden Nahebeziehung zu  Österreich auszugehen, die insbesondere aufgrund der langjährigen und durchgehenden  beruflichen Tätigkeit bei der Fa.NiederImmobilien Institut GmbH bereits seit vielen Jahren besteht.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_296`)


Insolvenz und schlechter Arbeitslage in D) zunächst 2008 als Leasingarbeiter  bei Fa. E nach Österreich gekommen und ist seit Oktober 2012 bei der Fa.NiederImmobilien Institut GmbH als Arbeiter  in Vollzeit im Umfang von 40 h, lt. eigenen Angaben mit 42,5 h (siehe Niederschrift v.  22.4.2015) nahezu durchgehend tätig.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_403`)


Er war ab 2008 zunächst als  Leiharbeiter und ist seit Oktober 2012 als Arbeiter bei der Fa.NiederImmobilien Institut GmbH nahezu durchgehend im  Inland berufstätig, bezieht daraus seither Einkünfte aus nichtselbständiger Arbeit und hat ua.  die Arbeitnehmerveranlagung durchführen lassen.

**False Positives:**

- `NiederImmobilien Institut GmbH` — partial — pred is substring of gold: `Fa.NiederImmobilien Institut GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.NiederImmobilien Institut GmbH`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Nach einer bei der Woytekat & Köhlen Recycling KG durchgeführten gemeinsamen Prüfung der Lohnabgaben (GPLA)  setzte der Magistrat der Stadt Wien, Magistratsabteilung 6, Rechnungs- und Abgabenwesen,  mit Bescheid vom 09. März 2017 Kommunalsteuer für den Zeitraum 2012 und 2013 fest und  adressierte den Bescheid an die Beschwerdeführerin.

**False Positives:**

- `Recycling KG` — partial — pred is substring of gold: `Woytekat & Köhlen Recycling KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Woytekat & Köhlen Recycling KG`(organisation)
- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Consulting GmbH` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_32`)


Sie sind bereits seit November 2012 bei der Firma AG in A-P beschäftigt.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_10`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna war zu den  Beanstandungszeiten (22. und 23. Oktober 2019) auf die Fa.RIL Planung GmbH  Dorf, zugelassen.

**False Positives:**

- `RIL Planung GmbH` — partial — pred is substring of gold: `Fa.RIL Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.RIL Planung GmbH`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_12`)


In der Begründung  sei ausgeführt worden, die Kundengewinnung durch den Beschwerdeführer stelle eine  Vermittlungsleistung dar, Leistungsempfänger sei die Zäsar u. Cankurt Analyse GmbH  da diese im eigenen Namen  auftrete.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_15`)


Darin habe das BFG die operative Tätigkeit der L  Schweiz AG als erwiesen angesehen und auf Unterlagen seitens der Schweizer Steuerbehörde  verwiesen.

**False Positives:**

- `Schweiz AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_16`)


Ergänzend sei darauf hingewiesen, dass der Beschwerdeführer niemals Umsatzsteuer  ausgewiesen habe bzw. die Gutschriftsabrechnungen der L Schweiz AG immer ohne  (österreichische) Umsatzsteuer erstellt habe.

**False Positives:**

- `Schweiz AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_17`)


Die Schweizer M-AG oder auch die im Erkenntnis  RV/7100189/2015 angeführte Tochtergesellschaft Zäsar u. Cankurt Analyse GmbH als vermeintliche  Leistungsempfängerin habe daher niemals einen spiegelbildlichen Vorsteuerabzug gehabt,  sodass die einseitige Vorschreibung von Umsatzsteuer auf Ebene des Beschwerdeführers aus  den erhaltenen Nettohonoraren gegen die Mehrwertsteuersystemrichtlinie idF RL 2010/45/EU  2 von 7 Seite 3 von 7

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_26`)


Als Leistungsempfänger der beschwerdegegenständlichen  Vermittlungsleistungen trat in den Streitjahren die unternehmerisch tätige Muttergesellschaft  M-AG und nicht die Tochtergesellschaft Zäsar u. Cankurt Analyse GmbH auf.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_33`)


L wird in Österreich durch die Zäsar u. Cankurt Analyse GmbH mit Sitz AdresseT-GmbH (im  Folgenden " T-GmbH" genannt) vertreten.

**False Positives:**

- `Cankurt Analyse GmbH` — partial — pred is substring of gold: `Zäsar u. Cankurt Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zäsar u. Cankurt Analyse GmbH`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wthrd GmbH` — partial — pred is substring of gold: `Heinz Neuböck Wthrd GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_94`)


b) Beiträge zu den zusätzlichen Pensionsversicherungen, die vom Pensionsinstitut der Linzer  Elektrizitäts-, Fernwärme- und Verkehrsbetriebe AG, vom Pensionsinstitut für Verkehr und  öffentliche Einrichtungen und nach der Bundesforste-Dienstordnung durchgeführt werden.

**False Positives:**

- `Verkehrsbetriebe AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_4`)


Darüber hinaus war er an der Schifffahrtsgesellschaft S GmbH & Co KG mit Sitz in H,  Deutschland, als Kommanditist beteiligt.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_11`)


In der am 4.4.2014 beim Finanzamt eingelangten Einkommensteuererklärung für 2012 erklärte  der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_13`)


In der am 12.1.2015 beim Finanzamt eingelangten Einkommensteuererklärung für 2013  erklärte der Bf., dass die Beteiligung an der S GmbH & Co KG nicht mehr vorhanden sei.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)


Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der Mohrlock Metall GmbH & Co KG vor.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Co KG` — similar text (different position): `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`
- `Co KG` — similar text (different position): `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)
- `L GmbH &  Co`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_24`)


Die GmbH unterrichtet die Gesellschafter und den Beirat über die Entwicklung der  Geschäfte…  2 von 13 Seite 3 von 13

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_45`)


In der gesonderten zugestellten Bescheidbegründung wurde ausgeführt:  „Aus dem übermittelten „Reeder-Zertifikat“ Nr. 277 geht hervor, dass der Bf. an der Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG) beteiligt ist.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Co KG` — similar text (different position): `Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)
- `S GmbH & Co KG`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_48`)


Die Bereederung des Schiffes wurde durch 2 Verträge geregelt (technische Bereederung inkl.  Operating und Crewing durch Bürgin & Siedle Umwelt GmbH& Co KG; kaufmännische Bereederung durch QGM Technik GmbH & Co KG.

**False Positives:**

- `QGM Technik GmbH` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bürgin & Siedle Umwelt GmbH&`(organisation)
- `QGM Technik GmbH & Co KG`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_71`)


Er beantragte die Anerkennung der Verlusttangente 2011 aus der Beteiligung an der S GmbH &  Co KG in Höhe von 34.275,23 €, die Zurücknahme der Endgültigkeitserklärung des  Einkommensteuerbescheides 2012 sowie die Erklärung des Einkommensteuerbescheides 2013  als gemäß § 200 Abs. 1 BAO vorläufiger Bescheid.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_119`)


Im  kaufmännischen Reedervertrag mit der QGM Technik GmbH & Co KG nimmt der Vertragsreeder alle  Geschäfts- und Rechtshandlungen vor, die der kaufmännische Geschäftsbetrieb einer Reederei  gewöhnlich mit sich bringt und erfordert (Einsatz und Beschäftigung des Schiffes, Versicherung,  Interessenswahrnehmung).

**False Positives:**

- `QGM Technik GmbH` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `QGM Technik GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `QGM Technik GmbH & Co KG`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_120`)


Im technischen Reedervertrag mit der Mohrlock Metall GmbH & Co KG nimmt  der Vertragsreeder alle Geschäfts- und Rechtshandlungen vor, die der technische  8 von 13 Seite 9 von 13

**False Positives:**

- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Mohrlock Metall GmbH & Co KG`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_122`)


Der Betrieb des Schiffes, wobei sich die Gesellschaft Dritter (Vertragsreeder) bedient, die für  die S GmbH & Co KG handeln, geht jedenfalls über eine Vermögensverwaltung hinaus.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `S GmbH & Co KG`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_126`)


2. Beweiswürdigung  Strittig ist, ob es sich bei der Beteiligung an der Schifffahrtsgesellschaft S GmbH & Co KG um  eine mitunternehmerische Beteiligung handelt und damit Einkünfte aus Gewerbebetrieb  vorliegen oder um eine Beteiligung nach Art eines stillen Gesellschafters und damit Einkünfte  aus Kapitalvermögen vorliegen.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_149`)


Aufgrund der Bestimmung des § 21 Abs. 1 BAO ist es durchaus zulässig, dass die Abgaben- behörde die Beteiligung als Kommanditist an einer deutschen GmbH & Co KG als eine  Beteiligung nach Art eines stillen Gesellschafters beurteilt und die aus dieser Beteiligung  10 von 13 Seite 11 von 13

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_151`)


Die Abgabenbehörde beurteilt den Gesellschaftsvertrag, welcher zwischen der Dörfel u. Rudolphson Heizung GmbH & Co KG und dem Bf. abgeschlossen wurde, in wirtschaftlicher Betrachtungsweise als Vertrag, mit  welchem eine Beteiligung nach Art eines stillen Gesellschafters abgeschlossen wurde.

**False Positives:**

- `Rudolphson Heizung GmbH` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`
- `Co KG` — partial — pred is substring of gold: `Dörfel u. Rudolphson Heizung GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dörfel u. Rudolphson Heizung GmbH & Co KG`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_167`)


Kann kein Firmenwert entstehen, weil die operativen Geschäfte (Vertragsreederei mit  Unternehmerrisiko) nicht von der Schifffahrtsgesellschaft S GmbH & Co KG, sondern von der L  GmbH & Co und der Mohrlock Metall GmbH & Co KG durchgeführt werden und besteht deshalb der Wert der  Gesellschaft lediglich im Buchwert inklusive der stillen Reserven des Schiffes, so ist dies ein  weiterer Hinweis dafür, dass keine mitunternehmerische Beteiligung, sondern eine Beteiligung  nach Art eines stillen Gesellschafters vorliegt.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Schifffahrtsgesellschaft S GmbH & Co KG`
- `Mohrlock Metall GmbH` — partial — pred is substring of gold: `Mohrlock Metall GmbH & Co KG`
- `Co KG` — similar text (different position): `Schifffahrtsgesellschaft S GmbH & Co KG`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Schifffahrtsgesellschaft S GmbH & Co KG`(organisation)
- `Mohrlock Metall GmbH & Co KG`(organisation)

</details>

---

## `Social Ministries/Offices` 💣

**F1:** 0.003 | **Precision:** 0.212 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `eefb990d`  
**Description:**
Matches Bundesamt für Soziales und Behindertenwesen and Sozialministeriumservice, handling genitive cases and parentheses.

**Content:**
```
(?:^|\s|\(|,|\.)\s*(?:das|des|dem|der|vom|von\s+der|der\s+)?\s*((?:Bundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen|Sozialministeriumservice(?:s)?))\s*(?:$|\s|,|\.|\(|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.212 | 0.001 | 0.003 | 80 | 17 | 63 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 63 | 11731 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_48`)


Sachverständigengutachten nach der Einschätzungsverordnung von Dr.in 2, Neurologin,  Bundesamt für Soziales und Behindertenwesen, am 07.05.2019 erstellt:  „Anamnese:  In einem Vorgutachten wurde eine Persönlichkeitsstörung (histrionisch), Panikstörung,  posttraumatische Belastungsstörung, chronische Kopfschmerzen mit 50% GdB rückwirkend an  Hand der Befunde ab 10/2012 beurteilt. Die Behinderung bestehe bereits vor dem 21.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_93`)


Die erhöhte Familienbeihilfe steht daher nicht zu.  Im Zuge dieser Erledigung erstellte das Bundesamt für Soziales und Behindertenwesen im  Auftrag des Finanzamtes folgende Bescheinigung(en) über das Ausmaß der Behinderung, die  Ihnen zeitnah und mit separater Post zugesendet wird/werden.“

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_255`)


Für die Abgabenbehörden und auch das Bundesfinanzgericht besteht - wie bereits vorstehend  ausgeführt, eine Bindung an die im vom Bundesamt für Soziales und Behindertenwesen  erstellten Gutachten, sofern sie schlüssig sind.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_46`)


Am 25.06.2014 fand eine fachärztliche  Untersuchung aus dem Bereich der Neurologie des Beschwerdeführers beim Bundesamt für  Soziales und Behindertenwesen, zur Erstellung eines Sachverständigengutachtens, statt.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_74`)


Dem Beschwerdeführer wurde vom Bundesamt für Soziales und Behindertenwesen ein durch  die Epilepsie bedingter Gesamtgrad der Behinderung von 40% und ein durch die Erkrankung  des Verdauungssystems bedingter Grad der Behinderung von 10% bescheinigt, wobei eine  wechselseitige Beeinflussung nicht festgestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_10`)


Aus dem diesbezüglich vom Sozialministeriumservice (vormals Bundesamt für Soziales und  Behindertenwesen) am 12./13.3.2020 erstellten und der Bf übermittelten ärztlichen  Sachverständigengutachten "mit Untersuchung" durch Amanda Zacharek  Fachärztin für Kinder- und  Jugendheilkunde, geht auszugsweise Folgendes hervor:  "Anamnese:  Termingeburt, verzögerte Meilensteine der Entwicklung, freies Laufen mit 23 Monaten, Sitzen  mit 12 Monaten, Sprachentwicklungsverzögerung.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Amanda Zacharek` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_210`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  als Amtssachverständige bedient, die in die bei dieser Behörde gem. § 90 KOVG 1957 zu  führende Sachverständigenliste, nicht aber in die Liste der allgemein beeideten und gerichtlich  12 von 18 Seite 13 von 18

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_22`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 18. Oktober 2019 wies das Finanzamt den Antrag der Beschwerdeführerin  (Bf.) vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur Familienbeihilfe für  ihren im Mai 2007 geborenen Sohn A. - ab dem im Antrag genannten Zeitpunkt Juli 2019 - mit  dem Hinweis auf die im Zuge dieser Erledigung vom Bundesamt für Soziales und  Behindertenwesen im Auftrag des Finanzamtes erstellte Bescheinigung vom 15. Oktober 2019  über das Ausmaß der Behinderung des Sohnes mit der Begründung ab, es sei ein Grad der  Behinderung von 30% festgestellt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_14`)


Über Anforderung des Finanzamtes an das Bundesamt für Soziales und Behindertenwesen  wurde der Sohn der Bf. am 31. August 2020 durch einen Arzt für Kinder und Jugendheilkunde  ein weiteres Mal untersucht und ein Sachverständigengutachten erstellt.   (Die Sachverständigengutachten werden im Erwägungsteil wiedergegeben).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_94`)


Das Bundesamt für Soziales und Behindertenwesen hat mit ausdrücklicher Einwilligung der  betroffenen Person dem zuständigen Finanzamt und dem Arbeitgeber, der Bezüge aus einer  gesetzlichen Sozialversicherung oder Ruhegenussbezüge einer Gebietskörperschaft im Sinne  des § 25 Abs. 1 Z 1, 3 oder 4 auszahlt, die vom Bundesamt für Soziales und Behindertenwesen  gespeicherten und für die Berücksichtigung von Freibeträgen im Sinne der Abs. 1 bis 3 und 7  erforderlichen personenbezogenen Daten elektronisch zu übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_105`)


Diese ist - abgesehen von im vorliegenden Fall nicht relevanten Ausnahmen - regelmäßig das  Bundesamt für Soziales und Behindertenwesen (nunmehr kurz: Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_108`)


Die Feststellung einer Behinderung und ihres Ausmaßes der Minderung der Erwerbsfähigkeit  bzw. des Grades der Behinderung, ist somit nicht von der Abgabenbehörde, sondern bindend  vom Bundesamt für Soziales und Behindertenwesen zu treffen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_166`)


§ 8 Abs. 6 FLAG 1967 normiert:  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist vom Bundesamt für Soziales und Behindertenwesen (Sozial- ministeriumservice) dem Finanzamt Österreich durch eine Bescheinigung auf Grund eines  ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_168`)


Das ärztliche Sachverständigengutachten ist vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) gegen Ersatz der Kosten aus Mitteln des  Ausgleichsfonds für Familienbeihilfen an die antragstellende Person zu übermitteln, eine  Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das Finanzamt  Österreich hat nicht zu erfolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt  Österreich` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_169`)


Der Nachweis des Grades der Behinderung in Form der  Bescheinigung entfällt, sofern der Grad der Behinderung durch Übermittlung der anspruchs- relevanten Daten durch das Bundesamt für Soziales und Behindertenwesen (Sozialministerium- service) aufgrund des Verfahrens nach § 40 des Bundesbehindertengesetzes (BBG), BGBl.  Nr. 283/1990, zur Ausstellung eines Behindertenpasses, nachgewiesen wird.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_242`)


Zufolge den Bestimmungen des § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die  voraussichtlich dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine  Bescheinigung des Sozialministeriumservice (früher Bundesamtes für Soziales und  Behindertenwesen) auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl.  VwGH 20.09.1995, 95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006,  2003/13/0123, VwGH 30.05.2017, Ro 2017/16/0009).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und  Behindertenwesen`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_266`)


Bei der Frage, wie hoch der Behinderungsgrad in einem bestimmten Zeitraum war bzw. wann  die voraussichtlich dauernde Erwerbsunfähigkeit eingetreten ist, handelt es sich um eine  Tatfrage und ist das Bundesfinanzgericht an das vom Sozialministeriumservice erstellte  ärztliche Gutachten de facto gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_6`)


Der Bf. wurde auf Grund des Antrages im Sozialministeriumservice am 25. Juni 2014 untersucht  und am 7. Juli 2014 folgendes Gutachten erstellt:  "Anamnese:  Lt. eigenen Angaben habe er die Handelsakademie besucht, anschließend BWL studiert (nicht  abgeschlossen).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_153`)


Im Gutachten des Sozialministeriumservice vom 7. Juli 2014 wurde dem Bf. eine primär  chronisch progrediente Multiple Sklerose attestiert und der Gesamtgrad der Behinderung mit  100 vH festgesetzt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Universität Wien`(organisation)
- `Prof. Maida`(person)
- `Dr. Wolfgang Baischer`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_177`)


Wie schon festgehalten, wurde dem Bf. im Gutachten des Bundessozialamtes für Soziales und  Behindertenwesen (nunmehr: Sozialministeriumservice) vom 7. Juli 2014 auf Grund seiner  Erkrankung an Multipler Sklerose ein Grad der Behinderung von 100 vH und der Eintritt der  Erwerbsunfähigkeit rückwirkend ab Jänner 2006 bescheinigt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_272`)


Bescheinigung des Sozialministeriumservice auf Grund eines ärztlichen  Sachverständigengutachtens

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_273`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_279`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der  Beweisführung  Zufolge § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation
- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_299`)


Bei der Frage, wie hoch der Behinderungsgrad in einem bestimmten Zeitraum war bzw. wann  die voraussichtlich dauernde Erwerbsunfähigkeit eingetreten ist, handelt es sich um eine  Tatfrage und ist das Bundesfinanzgericht an das vom Sozialministeriumservice erstellte  ärztliche Gutachten de facto gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_7`)


Begründend führt das Finanzamt nach Darstellung der Bestimmung gemäß § 8  Abs. 5 Familienlastenausgleichsgesetz 1967 (FLAG), BGBl 1967/376 idgF., aus, vom  Sozialministeriumservice sei für die Tochter der Grad der Behinderung (GdB) ab 1.1.2016 mit  lediglich 40 % (dh. nicht zumindest 50 %) und erst ab 1.1.2018 mit 60 % eingestuft worden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_10`)


Aus dem diesbezüglich vom Sozialministeriumservice (vormals Bundesamt für Soziales und  Behindertenwesen) am 12./13.3.2020 erstellten und der Bf übermittelten ärztlichen  Sachverständigengutachten "mit Untersuchung" durch Amanda Zacharek  Fachärztin für Kinder- und  Jugendheilkunde, geht auszugsweise Folgendes hervor:  "Anamnese:  Termingeburt, verzögerte Meilensteine der Entwicklung, freies Laufen mit 23 Monaten, Sitzen  mit 12 Monaten, Sprachentwicklungsverzögerung.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamt für Soziales und  Behindertenwesen`(organisation)
- `Amanda Zacharek`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_32`)


5. In der Folge wurde vom Sozialministeriumservice (kurz: SMS) ein zweites  Sachverständigengutachten am 11./13.5.2020 "aufgrund der Aktenlage" auszugsweise  folgenden Inhaltes erstellt:  3 von 18 Seite 4 von 18

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_105`)


8. Vom Bundesfinanzgericht (BFG) wurde mit Schreiben vom 19.2.2021 – samt Übermittlung  der beiden Vorgutachten und des Vorlageantrages - beim Sozialministeriumservice, ua. wegen  teilweiser Unvollständigkeit, ergänzend ein nochmaliges Gutachten angefordert bzw. die  Beantwortung folgender Fragen erbeten:   "a) Verwiesen wird auf das Vorbringen im beiliegend übermittelten Vorlageantrag der Bf:  Trifft es zu, dass trotz Titulierung des Erstgutachtens "mit Untersuchung" und dortigen  Angaben zu "Status" und "Gangbild" etc.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_108`)


e) Ist die gegenständliche Erkrankung als derart spezifisch zu erachten, dass - wie im  Vorlageantrag behauptet (Pkt. 2.2.) – die Begutachtung durch eine Fachärztin für Kinder- und  Jugendheilkunde "ungeeignet" ist und es vielmehr eines Sachverständigen für Medizinische  Genetik bzw. Humangenetik bedürfte ?"  9. Seitens des Sozialministeriumservice wurde dazu von Amanda Zacharek im Schreiben vom 14.3.2021 wie  folgt Stellung genommen:  " … Der beklagte Zeitraum liegt in der Vergangenheit und kann daher nur anhand der  vorgelegten schriftlichen Befunde beurteilt werden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Amanda Zacharek`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_161`)


Aus dem CV geht ua. hervor, dass die als Gutachterin für das  Sozialministeriumservice tätige Amanda Zacharek seit 1995 Fachärztin für Kinder- und Jugendheilkunde ist,  seit 1997 mit dem Additivfach Humangenetik, Habilitation am 22.6.1998 ("Localization of  Cancer Susceptibility Genes"), und seit 2008 mit dem Additivfach Endokrinologie und Diabetes.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Amanda Zacharek`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_225`)


(siehe zu vor in: Lenneis/Wanke, FLAG-Kommentar, 2. Aufl., Rzn. 11, 29, 31, 32 zu § 8)  3.) Rechtliche Würdigung:   In gegenständlichem Beschwerdefall wurden seitens der Fachärztin des  Sozialministeriumservice insgesamt zwei ärztliche Sachverständigen-Gutachten (samt  Vidierung und sohin Zustimmung durch den leitenden Arzt) sowie – auf Veranlassung durch  das BFG zur nochmaligen Überprüfung und Vervollständigung - eine ergänzende  Stellungnahme erstellt:  13 von 18 Seite 14 von 18

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_254`)


Da sich das Sozialministeriumservice sehr wohl aus einer eigenen Sachverständigenliste von zur  Berufsausübung berechtigter Ärzte zwecks Erstattung der Bescheinigungen gem. § 8 Abs. 6  FLAG bedienen kann, die nicht in der Liste der allgemein beeideten und gerichtlich  zertifizierten Sachverständigen eingetragen sind (siehe wiederum BFG 15.12.2017,  RV/7102062/2017), kommt dem diesbezüglichen Beschwerdeeinwand ebenso keine  Berechtigung zu.  Insgesamt besteht daher für das BFG keine Veranlassung, die fachliche Qualifikation der  begutachtenden Ärztin Amanda Zacharek in Zweifel zu ziehen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)
- `Amanda Zacharek`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_282`)


Wie oben ausgeführt, ist das Bundesfinanzgericht an die Feststellungen der im Wege des  Sozialministeriumservice erstellten Gutachten gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_287`)


Der Gesamtgrad der  Behinderung ist seitens des Sozialministeriumservice festzustellen;

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_5`)


Der Antrag  wurde rückwirkend ab März 2020 gestellt.  Dr. Dok1, Facharzt für Psychiatrie, bescheinigte dem Bf. nach der am 21. Oktober 2020 im  Sozialministeriumservice durchgeführten Untersuchung weder einen Grad der Behinderung  noch eine Erwerbsunfähigkeit, dies mit der Begründung, dass keine ausreichenden Patienten-  bzw. aufschlussreichen medizinischen Unterlagen – bis auf einen 4 Jahre alten Diabetespass –  vorgelegt worden seien.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_19`)


Auf Grund Ihrer Beschwerde wurde eine neuerliche Anfrage beim Sozialministeriumservice  gemacht.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_67`)


Bescheinigung des Sozialministeriumservice:  Der Grad der Behinderung und die Feststellung, ob bzw. ab wann eine voraussichtlich dauern- de Erwerbsunfähigkeit vorliegt, ist gemäß den Bestimmungen des § 8 Abs. 6 FLAG 1967 durch  eine Bescheinigung des Sozialministeriumservice auf Grund eines ärztlichen Sachverständigen- gutachtens nachzuweisen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_79`)


Die sachverständigen Ärzte des Sozialministeriumservice ziehen für ihre zu treffenden Fest- stellungen, wie hoch der Grad der Behinderung bzw. wann die voraussichtlich dauernde  Erwerbsunfähigkeit eingetreten ist, neben der durchgeführten Anamnese und Untersuchung  des Antragstellers die Kenntnisse der Medizin und ihr eigenes Fachwissen heran.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_134`)


Bei der Frage, ob eine voraussichtlich dauernde Erwerbsunfähigkeit vorliegt, handelt es sich  um eine Tatfrage und ist das Bundesfinanzgericht an das vom Sozialministeriumservice er- stellte ärztliche Gutachten de facto gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_14`)


In seinem Vorlagebericht vom 7.1.2020, der auch der Bf zugestellt wurde, verwies der  Finanzamtsvertreter darauf, dass laut den im elektronischen Akt aufliegenden Daten des  Sozialministeriumservice der Grad der Behinderung 40 % betrage, aber keine Unzumutbarkeit  der Benutzung öffentlicher Verkehrsmittel bestehe und auch kein Ausweis gemäß § 29b StVO  ausgestellt worden sei.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_22`)


- in allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen (kurz: Sozialministeriumservice).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamt für Soziales und Behindertenwesen`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_5`)


3. Auf Anforderung des Finanzamtes wurde daraufhin in dem vom Sozialministeriumservice  (SMS) "mit Untersuchung" erstellten Sachverständigengutachten vom 13.1./21.1.2021 durch  den Gutachter DrA, FA f. Psychiatrie, ua. Folgendes bescheinigt:  1 von 13 Seite 2 von 13

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_32`)


8. Das Finanzamt hat eine nochmalige Begutachtung beim Sozialministeriumservice veranlasst;

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_47`)


Aufgrund ihres Eigenantrages auf Gewährung der erhöhten Familienbeihilfe wurden durch das  Sozialministeriumservice am 21.1.2021 und am 5.2.2022 Sachverständigengutachten erstellt:  Es wurde der Bf zufolge der vom Gutachter durchgeführten Untersuchungen unter  Berücksichtigung der ihm vorliegenden relevanten ärztlichen Befunde, wobei der früheste  Befundbericht der Univ-Klinik Ort1 f.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_72`)


Nach § 8 Abs. 6 FLAG ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Bundesamtes für Soziales und Behindertenwesen (nunmehr Sozialministeriumservice) auf  Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_77`)


Lebensjahr  eingetretene dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, steht weder der  Grund- noch der Erhöhungsbetrag an Familienbeihilfe zu.   Zum Nachweis dieser Voraussetzung ist eine Bescheinigung des Sozialministeriumservice iSd  § 8 Abs. 6 FLAG zwingend erforderlich.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_89`)


Das BFG führt in seiner Begründung ua.  aus:  "Bescheinigung des Sozialministeriumservice auf Grund eines ärztlichen  Sachverständigengutachtens

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_90`)


Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_96`)


Bindung an die Gutachten des Sozialministeriumservice - keine andere Form der Beweisführung  Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher Bundesamtes für Soziales und Behindertenwesen) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation
- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_120`)


V. Erwägungen:  Gegenständlich wurde in beiden von Seiten des Sozialministeriumservice erstellten  Sachverständigengutachten bescheinigt, dass bei der Bf ein Gesamtgrad der Behinderung  (GdB) von 70 % und zwar – gestützt auf den frühest dem Gutachter vorliegenden relevanten  Befund – rückwirkend seit September 2015 vorliegt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_151`)


Wie oben ausgeführt, ist ua. das Bundesfinanzgericht an die Feststellungen der im Wege des  Sozialministeriumservice erstellten Gutachten gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_158`)


Lj. eine "dauernde Erwerbsunfähigkeit"  eingetreten war, ist das BFG an die Bescheinigungen (gutachterlichen Feststellungen) des  Sozialministeriumservice gebunden.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_166`)


Beweiswürdigung  Die Feststellungen beruhen auf den im Verwaltungsverfahren von der Bf. übermittelten  Befunden und den vom Sozialministeriumservice erstellten Sachverständigengutachten.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_195`)


Auch die Gutachten der Ärzte des Sozialministeriumservice haben den an ärztliche  Sachverständigengutachten zu stellenden Anforderungen an ihre Nachvollziehbarkeit zu  entsprechen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_198`)


Die Behörden des Verwaltungsverfahrens sind verpflichtet, die Beweiskraft der Gutachten des  Sozialministeriumservice zu prüfen und erforderlichenfalls für deren Ergänzung zu sorgen (vgl.  etwa VwGH 25.11.2010, 2010/16/0068, m.w.N.; BFG 27.9.2017, RV/7102586/2017).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_18`)


Die Behinderung und ihr Ausmaß sind durch eine amtliche Bescheinigung der folgenden  zuständigen Stellen nachzuweisen:  • Landeshauptfrau oder Landeshauptmann bei Empfängerinnen und Empfängern einer  Opferrente  • Sozialversicherungsträger bei Berufskrankheiten oder Berufsunfällen von  Arbeitnehmerinnen und Arbeitnehmern  • Sozialministeriumservice in allen übrigen Fällen sowie bei Zusammentreffen von  Behinderungen verschiedener Art  Der Nachweis kann auch durch einen Behindertenpass bzw. durch einen abschlägigen  Bescheid darüber (aus dem der Grad der Behinderung ersichtlich ist) erfolgen.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_19`)


Der  Behindertenpass bzw. Bescheid wird vom Sozialministeriumservice ausgestellt.  Für die im Betreff angeführten Veranlagungsjahre wurde keine der voranstehend genannten  Unterlagenbzw. Nachweise beigelegt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_51`)


Insbesondere wurde er auch  darauf hingewiesen, dass der Behindertenpass vom Sozialministeriumservice ausgestellt wird.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_105`)


Diese ist - abgesehen von im vorliegenden Fall nicht relevanten Ausnahmen - regelmäßig das  Bundesamt für Soziales und Behindertenwesen (nunmehr kurz: Sozialministeriumservice).

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamt für Soziales und Behindertenwesen`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_112`)


Nach dem oben Gesagten wären jedoch auch die Mehraufwendungen für eine  Krankendiätverpflegung nur dann als außergewöhnliche Belastung abzugsfähig, wenn die zu  Grunde liegende Krankheit durch das Sozialministeriumservice festgestellt würde.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_21`)


Auf Nachfrage beim Sozialministeriumservice, 1010 Wien,  sei der Behörde mitgeteilt worden, dass der für Frau N. ausgestellte Ausweis zum  Beanstandungszeitpunkt keine Gültigkeit mehr besessen habe, da dieser bis 1. August 2020  befristet gewesen sei.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_46`)


neuer gültiger Parkausweis nicht mehr ausgestellt wurde, weil die Voraussetzungen nicht  vorlagen, ergibt sich aus der Auskunft des Sozialministeriumservice vom 31. Oktober 2022.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_55`)


Vom Bundessozialamt für Soziales und Behindertenwesen (Sozialministeriumservice) wurde in  der Folge der Gutachter Dr. 2 mit der Erstellung eines neuen Gutachtens beauftragt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. 2`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_61`)


Vor diesem Hintergrund erwiesen sich für das Bundesfinanzgericht die der Bescheinigung des  Sozialministeriumservice zugrundeliegenden Gutachten vom 22. (gemeint: 24.) März 2021 und  die vom Bundesfinanzgericht angeforderte Ergänzung (erstellt in Form einer Neuerstellung am  17. Mai 2021) in Bezug auf die Frage, ob eine dauernde Unfähigkeit, sich selbst den Unterhalt  zu verschaffen vorliegt, und bejahendenfalls, wann dieser Umstand eingetreten ist, als  schlüssig, wenn unter den gegebenen Umständen der Gutachter den Eintritt der  Erwerbsunfähigkeit mit 09/2016 feststellt.   Das Bundesfinanzgericht hat sodann als Ergebnis seiner Überlegungen zur Würdigung des  Sachverständigenbeweises, die durch diesen Beweis gewonnene Tatsache als erwiesen  angenommen, eine dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, liege erst  ab September 2016 vor und hat deshalb seiner Entscheidung die hierauf lautende  Bescheinigung des Bundesamtes für Soziales und Behindertenwesen vom 16. Juli 2021 zu  Grunde gelegt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bundesamtes für Soziales und Behindertenwesen`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_72`)


Beweiswürdigung  Die Feststellungen, dass   (1) sich für das Bundesfinanzgericht die der Bescheinigung des Sozialministeriumservice  zugrundeliegenden Gutachten vom 22.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_8`)


Die belangte Behörde erhielt dazu vom Sozialministeriumservice die Auskunft, dass der  genannte - für eine andere Person ausgestellte - Ausweis als verloren gemeldet worden sei.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_107`)


Sozialministeriumservice durchgeführten Erhebungen haben aber ergeben, dass Rudolf B nicht  im Besitz eines § 29b-Parkausweises ist und dass der im Fahrzeug hinterlegte, teilweise mit  einer Postkarte abgedeckte §29b-Parkausweis mit den Endziffern „…hij“ die Nummer fghij hat  und auf eine andere Person ausgestellt gewesen ist.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_3`)


Entscheidungsgründe  Verfahrensgang  Dem Sohn der Beschwerdeführerin (Bf.), S., geb. 1998, wurde im Gutachten des  Sozialministeriumservice, letztes Gutachten vom 2. September 2016, wegen seiner  Behinderung (ADHS, Intelligenzminderung) ein Behinderungsgrad von 50 % ab Februar 2002  und eine voraussichtlich dauernde Erwerbsunfähigkeit vor dem 18.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_103`)


Für den Beschwerdeführer wurde weiters aufgrund seiner Behinderung ein Antrag auf  Ausstellung eines Behindertenpasses am 18.07.2022 gestellt.  Das beim Sozialministeriumservice durchgeführte medizinische Ermittlungsverfahren hat im  Zuge einer Untersuchung des Beschwerdeführers rechtskräftig ein Grad der Behinderung von  50% festgestellt und wurde dem Beschwerdeführer ein unbefristeter Behindertenpass  ausgestellt.  Beweis: beiliegendes Sachverständigengutachten des Sozialministeriumservice  beiliegender Behindertenpass  Inhaltlich liegen die Voraussetzungen für die Zuerkennung der erhöhten Familienbeihilfe nach  § 8 FLAG beim Betroffenen jedenfalls vor.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation
- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_126`)


Im (Vor)Gutachten des Sozialministeriumservice vom 2. September 2016 wurde S. ein  Behinderungsgrad von 50 vH bescheinigt.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_186`)


Bescheinigung des Sozialministeriumservice  § 8 Abs. 6 FLAG 1967 regelt, dass der Grad der Behinderung und die Feststellung, ob bzw. ab  wann eine voraussichtlich dauernde Erwerbsunfähigkeit vorliegt, durch eine Bescheinigung des  Sozialministeriumservice auf Grund eines ärztlichen Sachverständigengutachtens  nachzuweisen ist.

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation
- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_225`)


Der Gesamtgrad der Behinderung bzw. die Erwerbs(un)fähigkeit ist seitens des  Sozialministeriumservice festzustellen;

**False Positives:**

- `Sozialministeriumservice` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Ministers/Departments` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d8a0d18`  
**Description:**
Matches Bundesminister variations.

**Content:**
```
(?:des)\s+Bundesministers(?:in)?\s+für\s+[A-Z][a-z]+(?:,\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 64 | 0 | 64 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 64 | 11748 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_246`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und Konsumentenschutz`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_260`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und Konsumentenschutz`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_88`)


Dadurch würde im Falle positiver Einkünfte eine Doppelbesteuerung  entstehen, welche eine unilaterale Maßnahme gemäß § 48 BAO des Bundesministers für  Finanzen erforderlich machen würde.

**False Positives:**

- `des Bundesministers für  Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_178`)


Eine unilaterale Maßnahme gemäß § 48 BAO des Bundesministers für  Finanzen ist daher nicht erforderlich.

**False Positives:**

- `des Bundesministers für  Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_43`)


Laut vorgelegten lückenlosen Zeitaufzeichnungen hätte der Bf. jeweils nicht mehr als  die Hälfte der Gesamtarbeitszeit im Außendienst verbracht, sodass kein Anspruch auf den  Werbungskostenpauschbetrag gemäß § 17 Absatz 6 EStG 1988 in Verbindung mit der  Verordnung des Bundesministers für Finanzen über die Aufstellung von Durchschnittssätzen  für Werbungskosten von Angehörigen bestimmter Berufsgruppen bestünde.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_132`)


Zu Spruchpunkt I. (Abweisung)  Rechtslage  § 1 Z 9 der Verordnung des Bundesministers für Finanzen über die Aufstellung von  Durchschnittssätzen für Werbungskosten, BGBl II 2001/382 lautet wie folgt:  Für nachstehend genannte Gruppen von Steuerpflichtigen werden nach den jeweiligen  Erfahrungen der Praxis anstelle des Werbungskostenpauschbetrages gemäß § 16 Abs. 3 EStG  1988 folgende Werbungskosten auf die Dauer des aufrechten Dienstverhältnisses festgelegt:  Vertreter  5% der Bemessungsgrundlage höchstens 2 190 Euro jährlich.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Mag. Thassilo Wedekinn`(person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich`(address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_38`)


Bescheid des Bundesministers für Finanzen vom 1. August 2019  3 von 12 Seite 4 von 12

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_57`)


Auf die Erwägungen des Bundesministers für Finanzen im Einzelnen wird in weiterer Folge im  Erwägungsteil eingegangen werden.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_63`)


Zudem sei das Ermessen unrichtig geübt  worden (Die Beanstandungen des BF werden im Erwägungsteil den Ausführungen des  Bundesministers für Finanzen gegenübergestellt).

**False Positives:**

- `des  Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_93`)


Der BF meint noch, dass – entgegen der Ansicht des Bundesministers für Finanzen – der  Umstand, dass die Unterlassung der Erhebung eines Rechtsmittels gegen die im Anschluss an  die abgabenbehördliche Prüfung ergangenen Bescheide die Setzung einer Maßnahme nach  § 48 BAO nicht hindere.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_105`)


2.) zur Ermessensübung:  Die Erlassung von auf § 48 BAO gestützten Begünstigungsbescheiden liegt stets im Ermessen  des Bundesministers für Finanzen.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_120`)


Dazu merkt das Bundesfinanzgericht an, dass diese Ausführungen des Bundesministers für  Finanzen im Einklang mit der Judikatur des Verwaltungsgerichthofes stehen.

**False Positives:**

- `des Bundesministers für  Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_54`)


Fährt der Arbeitnehmer an  mindestens acht Tagen, aber an nicht mehr als zehn Tagen im Kalendermonat von der  Wohnung zur Arbeitsstätte, steht das jeweilige Pendlerpauschale zu zwei Drittel zu.  Die Verordnung des Bundesministers für Finanzen über die Kriterien zur Ermittlung des  Pendlerpauschales und des Pendlereuros, zur Einrichtung eines Pendlerrechners und zum  Vorliegen eines Familienwohnsitzes (Pendlerverordnung, BGBl. II Nr. 276/2013 idF BGBl. II Nr.  154/2014, legt auszugsweise fest wie nachstehend:  § 1 Pendlerverordnung lautet auszugsweise:  (2)

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_36`)


Rechtliche Grundlagen  § 30b BAG (Überbetriebliche Lehrausbildung im Auftrag des Arbeitsmarktservice) in der  Fassung BGBl. I Nr. 40/2010 lautet:  „(1) Hat das Arbeitsmarktservice entsprechend den Richtlinien des Verwaltungsrates für die  überbetriebliche Lehrausbildung, die den Bestimmungen des § 30 BAG oder des § 8c BAG  vergleichbare Qualitätsstandards enthalten, eine Ausbildungseinrichtung mit der  überbetrieblichen Lehrausbildung beauftragt, so ist für den Zeitraum der Beauftragung keine  Bewilligung des Bundesministers für Wirtschaft, Familie und Jugend gemäß § 30 Abs. 1 BAG  bzw. gemäß § 8c Abs. 1 BAG erforderlich.

**False Positives:**

- `des Bundesministers für Wirtschaft, Familie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_180`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und  Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und  Konsumentenschutz`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_33`)


Gemäß § 1 Z 9 der Verordnung des Bundesministers für Finanzen über die Aufstellung von  Durchschnittssätzen für Werbungskosten von Angehörigen bestimmter Berufsgruppen (VO),  BGBl II 382/2001, werden für Vertreter anstelle des Werbungskostenpauschbetrages gemäß  § 16 Abs. 3 EStG 1988 5 % der Bemessungsgrundlage, höchstens 2.190 Euro jährlich, auf die  Dauer des aufrechten Dienstverhältnisses als Werbungskosten festgelegt.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_75`)


Zu § 17 Abs. 6 EStG 1988 iVm § 1 Z 9 der Verordnung des Bundesministers für Finanzen über  die Aufstellung von Durchschnittssätzen für Werbungskosten von Angehörigen bestimmter  Berufsgruppen liegt eine einheitliche Rechtsprechung vor.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_29`)


Auf Grund des § 21 Abs. 9 UStG 1994 erging die Verordnung des Bundesministers für Finanzen,  BGBl. Nr. 279/1995 in der hier anzuwendenden Fassung BGBl. II Nr. 158/2014, "mit der ein  eigenes Verfahren für die Erstattung der abziehbaren Vorsteuern an ausländische  Unternehmen geschaffen wird", wenn der Unternehmer (von gegenständlich nicht in Betracht  kommenden Ausnahmen abgesehen) keine Umsätze iSd § 1 Abs. 1 Z 1 und 2 und Art. 1 UStG  1994 ausgeführt hat.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_34`)


§ 1 der Verordnung des Bundesministers für Finanzen über die Verlagerung des Ortes der  sonstigen Leistung bei Telekommunikationsdiensten sowie Rundfunk- und  Fernsehdienstleistungen, BGBl. II Nr. 383/2003 idF BGBl. II Nr. 221/2009, bestimmt:   3 von 8 Seite 4 von 8

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_28`)


Rechtslage und Erwägungen:  § 1 Abs 1 der Verordnung des Bundesministers für Finanzen über die Einreichung von  Anbringen, die Akteneinsicht und die Zustellung von Erledigungen in automationsunterstützter  Form (FinanzOnline-Verordnung 2006 - FOnV 2006), BGBl II 97/2006 idF BGBl II 122/2020,  regelt die automationsunterstützte Datenübertragungen in Bezug auf Anbringen (§ 86a BAO),  Erledigungen (§ 97 Abs 3 BAO) und Akteneinsicht (§ 90a BAO), soweit nicht eigene Vorschriften  bestehen.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_12`)


Die Bewertung des landwirtschaftlichen Vermögens erfolgte auf Basis der Kundmachung des  Bundesministers für Finanzen vom 4. März 2014 (GZ: BMF-010202/0100-VI/3/2014).

**False Positives:**

- `des  Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_16`)


Die Berechnung des Ertragswertes des forstwirtschaftlichen Vermögens erfolgt gemäß § 14  und Anlage 13 der Kundmachung des Bundesministers für Finanzen vom 5. März 2014 (GZ:  BMF-010202/0104-VI/3/2014) in der Fassung der Kundmachung vom 30. Dezember 2014.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_69`)


In der Kundmachung des Bundesministers für Finanzen vom 4. März 2014  wurde dieser Hauptvergleichsbetrieb definiert.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_84`)


Die Bewertung des forstwirtschaftlichen Vermögens erfolgte auf Grundlage der Kundmachung  des Bundesministers für Finanzen über die Bewertung von forstwirtschaftlichem Vermögen, GZ:  BMF-010202/0104-VI/3/2014.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_291`)


Betreffend die forstwirtschaftlich genutzten Flächen (forstwirtschaftliches Vermögen) des  gegenständlichen Betriebes, die weniger als 10 Hektar betragen, ist gemäß § 14 der  Kundmachung des Bundesministers für Finanzen vom 5. März 2014 GZ: BMF-010202/0104-

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_321`)


Mit der Kundmachung des Bundesministers für Finanzen über die Bewertungsgrundlagen für  das landwirtschaftliche Vermögen zum 01.01.2014 (Beschreibung des  26 von 30 Seite 27 von 30

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_31`)


Gemäß § 1 der auf §§ 34 und 35 EStG gestützten Verordnung des Bundesministers für Finanzen  über außergewöhnliche Belastungen, BGBl 303/1996 idF BGBl II 2010/430 (nachfolgend VO zu  § 35 EStG) sind die in den §§ 2 bis 4 genannten Mehraufwendungen als außergewöhnliche  Belastungen zu berücksichtigen, wenn ein Steuerpflichtiger Aufwendungen durch eine eigene  körperliche oder geistige Behinderung hat.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_99`)


Zur Höhe  der Schätzung ist auszuführen, dass – mangels konkreter Nachvollziehbarkeit der Fahrten – die  Verordnung des Bundesministers für Finanzen über die Aufstellung von Durchschnittssätzen  für Werbungskosten von Angehörigen bestimmter Berufsgruppen, BGBl. II Nr. 382/2001 von  der belangten Behörde herangezogen wurde.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_28`)


Für die Einschätzung des Grades der Behinderung  sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des Behinderten- einstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere Be- stimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und Konsumentenschutz`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138120.1`) (sent_id: `deanon_BFG_20260814_TEST/138120.1_55`)


Darüber hinaus kann  durch Verordnung des Bundesministers für Finanzen die Mitteilung des Inhalts von  Erledigungen auch im Wege automationsunterstützter Datenübertragung oder in jeder anderen  technisch möglichen Weise vorgesehen werden, wobei zugelassen werden kann, daß sich die  Behörde einer bestimmten geeigneten öffentlich-rechtlichen oder privatrechtlichen  Übermittlungsstelle bedienen darf.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_55`)


Hierzu ist festzuhalten, dass Anbringen zur Geltendmachung von Rechten und zur Erfüllung von  Verpflichtungen nach den Bestimmungen der Bundesabgabenordnung (§ 85 Abs. 1 BAO, § 86a  BAO) grundsätzlich schriftlich, telegrafisch, fernmündlich oder, soweit durch Verordnung des  Bundesministers für Finanzen zugelassen, im Wege automationsunterstützter  Datenübertragung (= FinanzOnline) einzubringen sind.

**False Positives:**

- `des  Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_75`)


Darüber hinaus kann durch Verordnung des Bundesministers für Finanzen  die Mitteilung des Inhalts von Erledigungen auch im Wege automationsunterstützter  Datenübertragung oder in jeder anderen technisch möglichen Weise vorgesehen werden,  wobei zugelassen werden kann, dass sich die Behörde einer bestimmten geeigneten öffentlich- rechtlichen oder privatrechtlichen Übermittlungsstelle bedienen darf.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_19`)


Für die Einschätzung des Grades der Behinderung sind § 14 Absatz 3 des  Behinderteneinstellungsgesetzes und die Verordnung des Bundesministers für Arbeit, Soziales  und Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades  der Behinderung (Einschätzungsverordnung) vom 18.8.2010 anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_172`)


Für die Einschätzung des Grades der  Behinderung sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und Konsumentenschutz`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_81`)


b. „Heimarbeiterpauschale“  Der Bf. vermeint, dass seine Tätigkeit eine solche im Sinne des § 1 Z 8 der Verordnung des  Bundesministers für Finanzen über die Aufstellung von Durchschnittssätzen für  Werbungskosten (idF kurz: Durchschnittssatzverordnung;

**False Positives:**

- `des  Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/139653.1`) (sent_id: `deanon_BFG_20260814_TEST/139653.1_21`)


Darüber hinaus kann  durch Verordnung des Bundesministers für Finanzen die Mitteilung des Inhalts von  Erledigungen auch im Wege automationsunterstützter Datenübertragung oder in jeder anderen  technisch möglichen Weise vorgesehen werden, wobei zugelassen werden kann, dass sich die  Behörde einer bestimmten geeigneten öffentlich-rechtlichen oder privatrechtlichen  Übermittlungsstelle bedienen darf […]“  Die FinanzOnline-Verordnung 2006 (FonV), BGBl II Nr 97/2006 idF BGBl II 2018/82, ist eine  Verordnung im Sinne dieser Bestimmung.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_58`)


Die auf dieser Grundlage erlassene Verordnung des Bundesministers für Finanzen zur  Verlustberücksichtigung 2019 und 2018 (COVID-19-Verlustberücksichtigungsverordnung),BGBl.  II Nr. 405/2020, lautet auszugsweise wie folgt:   „1. Abschnitt  COVID-19-Rücklage  § 1. (1)

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_21`)


Anbringen können im Wege automationsunterstützter Datenübertragung oder in jeder anderen  technisch möglichen Weise eingereicht werden, soweit es durch Verordnung des  Bundesministers für Finanzen zugelassen wird.

**False Positives:**

- `des  Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_120`)


Gemäß § 17 Abs. 4 EStG 1988 können für die Ermittlung des Gewinnes weiters mit Verordnung  des Bundesministers für Finanzen Durchschnittssätze für Gruppen von Steuerpflichtigen  aufgestellt werden.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_117`)


Gemäß § 17 Abs. 4 EStG 1988 können für die Ermittlung des Gewinnes weiters mit Verordnung  des Bundesministers für Finanzen Durchschnittssätze für Gruppen von Steuerpflichtigen  aufgestellt werden.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_97`)


[…]  § 2 der Verordnung des Bundesministers für Finanzen über außergewöhnliche Belastungen,  BGBl. Nr. 303/1996 (idF BGBl. II Nr. 430/2010) lautet:  (1)

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_121`)


…"  B) Im VwGH-Erkenntnis vom 13.12.2022, Ro 2019/16/0005, worauf der VwGH Bezug nimmt,  wird dargelegt:  " … 19 Die aufgrund des § 4 Abs. 1 GrEStG 1987 ergangene „Verordnung des Bundesministers  für Finanzen betreffend Festlegung der Ermittlung des Grundstückswertes (Grundstücks- wertverordnung - GrWV)“, BGBl. II Nr. 442/2015, lautete auszugsweise wie folgt:  „Methoden der Grundstückswertermittlung  § 1.

**False Positives:**

- `des Bundesministers  für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_69`)


Die dazu ergangene Verordnung des Bundesministers für Finanzen betreffend Unbilligkeit der  Einhebung im Sinn des § 236 BAO, BGBl. II Nr. 2005/435 idF BGBl II 2019/236 konkretisiert das  Erfordernis der Unbilligkeit wie folgt:  "§ 1.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/143111.1`) (sent_id: `deanon_BFG_20260814_TEST/143111.1_85`)


Darüber hinaus kann durch Verordnung des Bundesministers für Finanzen die  Mitteilung des Inhalts von Erledigungen auch im Wege automationsunterstützter  Datenübertragung oder in jeder anderen technisch möglichen Weise vorgesehen werden,  wobei zugelassen werden kann, dass sich die Behörde einer bestimmten geeigneten öffentlich- rechtlichen oder privatrechtlichen Übermittlungsstelle bedienen darf (Satz zwei).

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_56`)


Auf Grund des § 21 Abs. 9 UStG 1994 erging die Verordnung des Bundesministers für Finanzen,  BGBl. Nr. 279/1995 in der hier anzuwendenden Fassung BGBl. II Nr. 222/2009, "mit der ein  eigenes Verfahren für die Erstattung der abziehbaren Vorsteuern an ausländische  Unternehmen geschaffen wird", wenn der Unternehmer (von gegenständlich nicht in Betracht  kommenden Ausnahmen abgesehen) keine Umsätze iSd § 1 Abs. 1 Z 1 und 2 und Art. 1 UStG  1994 ausgeführt hat.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_60`)


§ 1 der Verordnung des Bundesministers für Finanzen über die Verlagerung des Ortes der  sonstigen Leistung bei Telekommunikationsdiensten sowie Rundfunk- und  Fernsehdienstleistungen (Telekom-Verordnung), BGBl. II Nr. 383/2003 idF BGBl. II Nr.  221/2009, bestimmt:  "Liegt bei einer in § 3a Abs. 14 Z 12 und 13 des Umsatzsteuergesetzes 1994, BGBl. Nr. 663, in  der Fassung des Bundesgesetzes BGBl. I Nr. 52/2009, bezeichneten Leistung der Ort der  Leistung gemäß § 3a des Umsatzsteuergesetzes 1994 außerhalb des Gemeinschaftsgebietes, so  wird die Leistung im Inland ausgeführt, wenn sie dort genutzt oder ausgewertet wird."

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_16`)


Zu Spruchpunkt I. (Abweisung)  Gemäß § 1 Abs. 1 der Verordnung des Bundesministers für Finanzen, mit der ein eigenes  Verfahren für die Erstattung der abziehbaren Vorsteuern an ausländische Unternehmer  geschaffen wird, BGBl. Nr. 279/1995 idF BGBl. II Nr. 389/2010 (in der Folge:  Erstattungsverordnung), hat die Erstattung der abziehbaren Vorsteuerbeträge an nicht im  Inland ansässige Unternehmer, das sind solche, die im Inland weder ihren Sitz noch eine  Betriebsstätte haben, abweichend von den §§ 20 und 21 Abs. 1 bis 5 UStG 1994 nach Maßgabe  der §§ 2, 3, und 3a durchzuführen, wenn der Unternehmer im Erstattungszeitraum  1.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_75`)


Darüber hinaus kann durch Verordnung des Bundesministers für Finanzen die Mitteilung des  Inhalts von Erledigungen auch im Wege automationsunterstützter Datenübertragung oder in  jeder anderen technisch möglichen Weise vorgesehen werden, wobei zugelassen werden kann,  daß sich die Behörde einer bestimmten geeigneten öffentlich-rechtlichen oder privatrechtlichen  Übermittlungsstelle bedienen darf.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144088.1`) (sent_id: `deanon_BFG_20260814_TEST/144088.1_62`)


Gemäß § 86a Abs 1 BAO können Anbringen können im Wege automationsunterstützter  Datenübertragung oder in jeder anderen technisch möglichen Weise eingereicht werden,  soweit es durch Verordnung des Bundesministers für Finanzen zugelassen wird.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_29`)


Hinsichtlich des Freibetrages für gehbehinderte Menschen verwies der Beschwerdeführer auf  § 3 Abs. 1 der Verordnung des Bundesministers für Finanzen, BGBl. Nr. 303/1996, der hinsicht- lich der Gewährung des gegenständlichen Freibetrages keinerlei Einschränkungen durch den  Bezug einer erhöhten Familienbeihilfe vorsehe.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_94`)


Hat der Steuerpflichtige gemäß § 35 Abs. 1 TS 4 EStG 1988 idF. BGBl. I Nr. 112/2012 außer- gewöhnliche Belastungen durch eine Behinderung eines Kindes (§ 106 Abs. 1 und 2), für das  keine erhöhte Familienbeihilfe gemäß § 8 Abs. 4 des Familienlastenausgleichsgesetzes 1967  gewährt wird, und erhält weder der Steuerpflichtige noch sein (Ehe-)Partner noch sein Kind eine  pflegebedingte Geldleistung (Pflegegeld, Pflegezulage, Blindengeld oder Blindenzulage), so  steht ihm jeweils ein Freibetrag (Abs. 3) zu.  Gemäß § 1 Abs. 1 TS 4 der Verordnung des Bundesministers für Finanzen über  außergewöhnliche Belastungen, BGBl. Nr. 303/1996 idF. BGBl II Nr. 430/2010, sind die in den  §§ 2 bis 4 dieser Verordnung genannten Mehraufwendungen als außergewöhnliche  Belastungen zu berücksichtigen, wenn der Steuerpflichtige Aufwendungen bei Anspruch des  Steuerpflichtigen selbst oder seines (Ehe-)Partners auf den Kinderabsetzbetrag oder den  Unterhaltsabsetzbetrag, durch eine Behinderung des Kindes (§ 106 Abs. 1 und 2 EStG 1988) hat,  für das keine erhöhte Familienbeihilfe gemäß § 8 Abs. 4 des Familienlastenausgleichsgesetzes  1967 gewährt wird.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_108`)


Der Gewährung des Freibetrages nach § 5 der Verordnung des Bundesministers für Finanzen  über außergewöhnliche Belastungen steht zwar der Bezug der erhöhten Familienbeihilfe nicht  entgegen, jedoch sind Mehraufwendungen Voraussetzung.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_113`)


ad Freibetrag für gehbehinderte Menschen  Gemäß § 1 Abs. 1 TS 4 der Verordnung des Bundesministers für Finanzen über  außergewöhnliche Belastungen, BGBl. Nr. 303/1996 idF. BGBl II Nr. 430/2010, sind die in den  §§ 2 bis 4 dieser Verordnung genannten Mehraufwendungen als außergewöhnliche  Belastungen zu berücksichtigen, wenn der Steuerpflichtige Aufwendungen bei Anspruch des  Steuerpflichtigen selbst oder seines (Ehe-)Partners auf den Kinderabsetzbetrag oder den  Unterhaltsabsetzbetrag, durch eine Behinderung des Kindes (§ 106 Abs. 1 und 2 EStG 1988) hat,  für das keine erhöhte Familienbeihilfe gemäß § 8 Abs. 4 des Familienlastenausgleichsgesetzes  1967 gewährt wird.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_174`)


b) Einkunftsquelle (Liebhaberei)  Nach § 1 Abs. 1 der Verordnung des Bundesministers für Finanzen über das Vorliegen von  Einkünften, über die Annahme einer gewerblichen oder beruflichen Tätigkeit und über die  Erlassung vorläufiger Bescheide (Liebhabereiverordnung), BGBl. Nr. 33/1993 idgF (kurz: LVO),  liegen Einkünfte vor bei einer Betätigung (einer Tätigkeit oder einem Rechtsverhältnis), die  durch die Absicht veranlaßt ist, einen Gesamtgewinn oder einen Gesamtüberschuß der  Einnahmen über die Werbungskosten (§ 3) zu erzielen, und nicht unter Abs. 2 fällt.   Nach § 1 Abs. 2 Z 3 LVO ist Liebhaberei bei einer Betätigung anzunehmen, wenn Verluste  entstehen aus der Bewirtschaftung von Eigenheimen, Eigentumswohnungen und  Mietwohngrundstücken mit qualifizierten Nutzungsrechten.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_184`)


Die Verordnung des Bundesministers für Finanzen BGBl. Nr. 33/1993 (Liebhabereiverordnung- LVO) ist auch zu § 7 Abs. 2 KStG 1988 ergangen und gilt demnach auch für der  Körperschaftsteuer unterliegende Rechtssubjekte (vgl. zB VwGH 25.05.2022, Ra 2022/15/0009;

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_73`)


Darüber hinaus kann durch Verordnung des Bundesministers für Finanzen die  Mitteilung des Inhalts von Erledigungen auch im Wege automationsunterstützter  Datenübertragung oder in jeder anderen technisch möglichen Weise vorgesehen werden,  wobei zugelassen werden kann, dass sich die Behörde einer bestimmten geeigneten öffentlich  rechtlichen oder privatrechtlichen Übermittlungsstelle bedienen darf.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_72`)


Die verfahrensrelevanten Bestimmungen der aufgrund des § 16 Abs. 1 Z 6 lit. j EStG 1988  erlassenen Verordnung des Bundesministers für Finanzen über die Kriterien zur Ermittlung des  Pendlerpauschales und des Pendlereuros, zur Einrichtung eines Pendlerrechners und zum  Vorliegen eines Familienwohnsitzes, BGBl II 2013/276 (nachfolgend PendlerV) lauten für den  Verfahrenszeitraum auszugsweise:   „§ 1. (1)

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/146646.1`) (sent_id: `deanon_BFG_20260814_TEST/146646.1_89`)


§ 34 Abs. 7 und 8 EStG 1988 […]  § 1 der Verordnung des Bundesministers für Finanzen über außergewöhnliche Belastungen,  BGBl 303/1996, idF BGBl II 91/1998   (1)Hat der Steuerpflichtige Aufwendungen  -durch eine eigene körperliche oder geistige Behinderung, (TS I)  …  8 von 13 Seite 9 von 13

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/146646.1`) (sent_id: `deanon_BFG_20260814_TEST/146646.1_95`)


§ 4 der Verordnung des Bundesministers für Finanzen über außergewöhnliche Belastungen  Nicht regelmäßig anfallende Aufwendungen für Hilfsmittel (zB Rollstuhl, Hörgerät,  Blindenhilfsmittel) sowie Kosten der Heilbehandlung sind im nachgewiesenen Ausmaß zu  berücksichtigen.

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_351`)


die Verordnung des Bundesministers für Finanzen  und der Bundesministerin für Klimaschutz, Umwelt, Energie, Mobilität, Innovation und  Technologie über den Absetzbetrag für begünstigte Investitionen im Rahmen der  Energiekrisenbeiträge [EKB-InvestitionsV], BGBl. II 194/2023, idF BGBl. II 244/2024).

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_351`)


die Verordnung des Bundesministers für Finanzen  und der Bundesministerin für Klimaschutz, Umwelt, Energie, Mobilität, Innovation und  Technologie über den Absetzbetrag für begünstigte Investitionen im Rahmen der  Energiekrisenbeiträge [EKB-InvestitionsV], BGBl. II 194/2023, idF BGBl. II 244/2024).

**False Positives:**

- `des Bundesministers für Finanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_164`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

**False Positives:**

- `des Bundesministers für Arbeit, Soziales` — positional overlap with gold: `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesministers für Arbeit, Soziales und Konsumentenschutz`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_65`)


Verordnung des Bundesministers für Wirtschaft und Arbeit über die Zugehörigkeit der von  Land- und Forstwirten hergestellten Produkte zur land- und forstwirtschaftlichen Urproduktion  (Urprodukteverordnung)  Auf Grund des § 2 Abs. 3a der Gewerbeordnung 1994, BGBl. Nr. 194, zuletzt geändert durch das  Bundesgesetz BGBl. I Nr. 68/2008, wird im Einvernehmen mit dem Bundesminister für Land-  und Forstwirtschaft, Umwelt und Wasserwirtschaft, der Bundesministerin für Gesundheit,  Familie und Jugend und dem Bundesminister für Finanzen verordnet:“  § 1 Z. 6 Urprodukteverordnung   5 von 13 Seite 6 von 13

**False Positives:**

- `des Bundesministers für Wirtschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1405, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_38`)

Am 21.12.2018 wurde eine Vereinbarung zwischen der Bf. und der X GmbH abgeschlossen  welche – neben einer weiteren Kreditvergabe der Bf. an die X GmbH - betreffend  gegenständlicher Liegenschaften festhielt, dass sich die **X GmbH** verpflichtete die  Liegenschaften EZ BBB und EZ CCC, KG XX, Bezirksgericht Weiz zu einem Pauschalkaufpreis von  100.000,00 Euro an die Bf. zu veräußern, das Verfahren vor dem LGZ Graz zu GZ Cg nach  Umsetzung dieser Vereinbarung ewig ruhend gestellt wird sowie mit Umsetzung dieser  Vereinbarung das beim Bezirksgericht Weiz zu GZ E eingeleitete  Zwangsversteigerungsverfahren eingestellt wird.

- missed: `X GmbH` (organisation)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_19`)

Mit Vorhalt vom 15.12.2020 ersuchte das Bundesfinanzgericht den Bf, nachstehende Fragen zu  beantworten und die angesprochenen Unterlagen vorzulegen:  1) Vorzulegen sei nicht nur das Deckblatt, sondern der gesamte Bescheid des **Magistrates der  Stadt Wien** vom 06.10.2015 betreffend „Mindestsicherung, Zuerkennung“.

- missed: `Magistrates der  Stadt Wien` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Stadt Wien`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des **Finanzamtes Wien  12/13/14 Purkersdorf** vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

- missed: `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Wien  12/13/14`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_41`)

Abweichend von Z 1 ist für Kinder, die sich ständig in einem anderen Mitgliedstaat der EU  oder Hoheitsgebiet einer anderen Vertragspartei des Abkommens über den Europäischen  Wirtschaftsraum oder der Schweiz aufhalten, die Höhe des Familienbonus Plus sowie der  Absetzbeträge gemäß Abs. 4 auf Basis der vom Statistischen Amt der **Europäischen Union**  veröffentlichten vergleichenden Preisniveaus für jeden einzelnen Mitgliedstaat der EU, jede  Vertragspartei des Europäischen Wirtschaftsraumes und die Schweiz im Verhältnis zu  Österreich zu bestimmen:  a)

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_4`)

Entscheidungsgründe  In der Folge werden für die im Erkenntnis angeführten Gesellschaften nachstehende  Abkürzungen verwendet:  Firma FN Abkürzung  P-GmbH 1-t P-GmbH  G-GmbH 2-x G-GmbH  MH-Bau GmbH 3-f MH-Bau GmbH  MH-Immo GmbH 4-h **MH-Immo GmbH**

- missed: `MH-Immo GmbH` (organisation)
- predicted in sentence: `G-GmbH  MH-Bau GmbH`, `MH-Bau GmbH  MH-Immo GmbH`, `MH-Immo GmbH`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_8`)

Entscheidungsgründe  Mit Straferkenntnis des **Magistrats der Stadt Wien**, Magistratsabteilung 67, vom 3. Jänner  2022, Zahl MA67/Zahl/2021, wurde über die Beschwerdeführerin (in der Folge kurz Bf.  genannt) eine Geldstrafe in Höhe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt, weil sie das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 6. Oktober 2021 um 18:35 Uhr in einer  gebührenpflichtigen Kurzparkzone in 1010 Wien, Adresse, abgestellt habe ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

- missed: `Magistrats der Stadt Wien` (organisation)
- predicted in sentence: `Magistrats der Stadt Wien, Magistratsabteilung 67`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_41`)

Weiters sei darauf hinzuweisen, dass weder bekannt sei, wann das letzte  Fristverlängerungsansuchen eingebracht (Anmerkung **Bundesfinanzgericht**: sprich aufgegeben)  wurde, noch wann der abweisende Bescheid vom 11.01.2018 zugestellt worden war.

- missed: `Bundesfinanzgericht` (organisation)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_10`)

5. Am 23.09.2020 wurde von der belangten Behörde ein Vereinsregisterauszug der  zuständigen Vereinsbehörde (**Bezirkshauptmannschaft Salzburg-Umgebung**) zum Stichtag 16. März 1996  nachgereicht, aus dem  hervorgeht, dass der beschwerdeführende Verein mit 9. Februar 1989  rechtskräftig freiwillig  aufgelöst worden war.

- missed: `Bezirkshauptmannschaft Salzburg-Umgebung` (organisation)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/149565.1`) (sent_id: `deanon_BFG_20260814_TEST/149565.1_39`)

Zweckmäßig erfolgt diese Verständigung dadurch, dass eine Ausfertigung des  verfahrensleitenden Beschlusses (samt Begründung, in der die Ansicht des  **Bundesfinanzgerichts** dargelegt wird) den Parteien zugestellt wird (vgl VwGH 20.09.2023,  Ro 2023/13/0015, mwN).

- missed: `Bundesfinanzgerichts` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad über die Beschwerde des  Arthur Soyal, Josef-Prangl-Straße 16, 8342 Perlsdorf, Österreich, vom 23. Jänner 2024 gegen das Straferkenntnis des **Magistrates  der Stadt Wien** vom 27. Dezember 2023, Geschäftszahl MA67/111111/2023, betreffend  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung, ABl der Stadt  Wien 2005/51 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBI für Wien  2006/9 in der Fassung LGBl für Wien 2012/24, nach Durchführung einer mündlichen  Verhandlung am 21. Mai 2024, im Beisein des Schriftführers AD Rudolf Keinberger, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs  1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

- missed: `Magistrates  der Stadt Wien` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Stadt Wien`, `Stadt  Wien`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_14`)

Auf Vorhalt des Finanzamtes vom 3.12.2014 legte der Bf. in Beantwortung dieses Vorhaltes am  26.1.2015 den Gesellschaftsvertrag der Fa.Dörfel u. Rudolphson Heizung GmbH & Co KG (nunmehr S GmbH & Co KG), den  Treuhand- und Verwaltungsvertrag mit T AG und die Vertragsreederverträge mit der L GmbH &  Co und der **Mohrlock Metall GmbH & Co KG** vor.

- missed: `Mohrlock Metall GmbH & Co KG` (organisation)
- predicted in sentence: `Finanzamtes`, `Rudolphson Heizung GmbH`, `Co KG`, `Co KG`, `Mohrlock Metall GmbH`, `Co KG`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Huberta Maginot  in der Beschwerdesache der  **Wolensky Logistik**, Knödelhütte 10, 9462 St. Peter im Lavanttal, Österreich, über die Beschwerde vom 10.Okt.2022, eingebracht am  12. Oktober 2022, gegen den zur Steuernummer 61-790/6327  ergangenen Bescheid des  Finanzamt Spittal Villach  vom 14. September 2022 betreffend Abweisung eines Antrages auf  Wiederaufnahme (§ 303 BAO) des Einkommensteuerbescheides 2018 vom 29.Jän 2020 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Wolensky Logistik` (organisation)
- predicted in sentence: `Bundesfinanzgericht (BFG)`, `Finanzamt`

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_149`)

Zahlungen wie jene für 10-Tages-Vignetten, Reisekosten oder einen Besuch in der **Allianz** Arena  München seien Ersätze an die jeweiligen Kunden zur Aufrechterhaltung einer tragfähigen  Geschäftsbeziehung.

- missed: `Allianz` (organisation)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_52`)

Das Einkommen 2007 und die darauf entfallende Abgabe waren wie folgt zu berechnen:    Einkommensteuer für 2007  Einkünfte aus nichtselbständiger Arbeit  Übermittelte Lohnzettel (KZ 245)  **ÖBB** 25.324,62 €  Sonstige Werbungskosten ohne Anrechnung  Auf den Pauschbetrag -1.125,00 €  Pauschbetrag für Werbungskosten -132,00 € 24.067,62 €  Einkünfte aus Vermietung und Verpachtung  -1.688,49 €   -----------------  4 von 6 Seite 5 von 6

- missed: `ÖBB` (organisation)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_18`)

Auf der zweitgenannten Teilstrecke habe für **ÖBB**-Bedienstete  ein Werksverkehr bestanden.

- missed: `ÖBB` (organisation)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Verwaltungsstrafsache gegen  Heidrun Engehausen, Weinzierlstraße 31, 2292 Engelhartstetten, Österreich, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  über die Beschwerde vom 13. Oktober 2020 gegen das Straferkenntnis des **Magistrates der  Stadt Wien**, Magistratsabteilung 67- Parkraumüberwachung, als Abgabenstrafbehörde vom  18. September 2020, Zahl: MA67/Zahl1/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

- missed: `Magistrates der  Stadt Wien` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Stadt Wien`, `Stadt Wien`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_6`)

Mit Schreiben des **Magistrates der Stadt Wien**, der Magistratsabteilung (MA) 67 vom 8. März  2021 wurde die Firma xKG, als Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem  behördlichen Kennzeichen Autonummer (A) aufgefordert, binnen zwei Wochen nach  1 von 5 Seite 2 von 5

- missed: `Magistrates der Stadt Wien` (organisation)
- predicted in sentence: `Stadt Wien`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_240`)

Nach Beratung im Bewertungsbeirat trifft das **Bundesministerium für Finanzen** über den  Gegenstand der Beratung die Entscheidung.

- missed: `Bundesministerium für Finanzen` (organisation)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dagobert Rönnecke  in der Revisionssache PhD ÖkR Peter Stankeit,  Im Alauntal 10, 3243 Eselsteiggraben, Österreich  vertreten durch **Aigner Rechtsanwalts-GmbH**, Lugeck 1-2/Stiege 2/Top 12, 1010  Wien, über den Antrag des Revisionswerbers vom 2.Februar 2024, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 12.Dezember 2023, RV/5100686/2021, betreffend  Einkommensteuer 2019 und die Aufhebung des Einkommenssteuerbescheides 2019  erhobenen außerordentlichen Revision die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

- missed: `Aigner Rechtsanwalts-GmbH` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Bundesfinanzgerichtes`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_308`)

Nach Ansicht des **Bundesfinanzgerichts** hat das Finanzamt seine Feststellungen zu den  innergemeinschaftlichen Erwerben und innergemeinschaftlichen Dienstleistungen getroffen,  ohne auf die Einwendungen der Bf. in rechtlich gebotener Weise einzugehen und ohne die  dafür unionsrechtlich vorgegebenen bzw. gebotenen Ermittlungen vorzunehmen.

- missed: `Bundesfinanzgerichts` (organisation)
- predicted in sentence: `Finanzamt`

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_32`)

Unstrittig ist, dass der Sohn des Bf. im Wintersemester 2017/2018 mit dem Studium der  Humanmedizin an der Universität Wien begann und davor, beginnend  mit dem  Sommersemester 2016, das Bachelorstudium Wirtschaftsrecht an der **Wirtschaftsuniversität  Wien** betrieb.

- missed: `Wirtschaftsuniversität  Wien` (organisation)
- predicted in sentence: `Universität Wien`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/145708.1`) (sent_id: `deanon_BFG_20260814_TEST/145708.1_65`)

3.2 Zu Spruchpunkt II. (Unzulässigkeit der Revision)  Gegen ein Erkenntnis des **Bundesfinanzgerichts** ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

- missed: `Bundesfinanzgerichts` (organisation)
- predicted in sentence: `Verwaltungsgerichtshofes`, `Verwaltungsgerichtshofes`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch **Hopmeier Wagner Kirnbauer  Rechtsanwälte OG**, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Wien 12/13/14`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/148797.1`) (sent_id: `deanon_BFG_20260814_TEST/148797.1_53`)

Der  dritte Absatz von Artikel 47 der Charta der Grundrechte der **Europäischen Union** („Personen,  die nicht über ausreichende Mittel verfügen, wird Prozesskostenhilfe bewilligt, soweit diese  Hilfe erforderlich ist, um den Zugang zu den Gerichten wirksam zu gewährleisten“) bekräftigt  ebenfalls den Inhalt des § 40 Abs. 1 VwGVG.

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Roberta Sellerer  in der   Beschwerdesache Univ.-Prof.in Susette Teebken, Günther Benedikt-Straße 26, 8052 Graz, Österreich, vertreten durch **Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft**, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 29. Mai 2017 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 3. Mai 2017,   ErfNr, betreffend 1. Aufhebung gemäß § 299 Abs. 1 BAO und 2. Festsetzung der  Grunderwerbsteuer, im fortgesetzten Verfahren zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 3.5.2017 betreffend Aufhebung des      Grunderwerbsteuerbescheides vom 24.2.2017 gemäß § 299 Abs. 1 BAO wird als      unbegründet abgewiesen.

- missed: `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Partner GmbH`, `Finanzamtes für  Gebühren`, `Finanzamt`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_18`)

Mit Erkenntnis des Bundesfinanzgerichtes zu GZ. RV/7500480/2021 vom 4. August 2021 wurde  die von X als Geschäftsführer der X_KG eingebrachte Beschwerde vom 21. Mai 2021 gegen den  Zurückweisungsbescheid des **Magistrates der Stadt Wien** vom 10. Mai 2021, mit dem der  Einspruch gegen die an Bf ergangene Strafverfügung vom 16. März 2021 zurückgewiesen  2 von 5 Seite 3 von 5

- missed: `Magistrates der Stadt Wien` (organisation)
- predicted in sentence: `Bundesfinanzgerichtes`, `Stadt Wien`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_24`)

Nach detaillierten Ausführungen des bundesweiten Fachbereiches für Einkommen– und  Körperschaftssteuer vom 31. August 2012 und nach Schlussbesprechung vom 12. Oktober  2012 wurden im Bericht über das Ergebnis der abgabenbehördlichen Prüfung in hier  interessierender Hinsicht folgende steuerlichen Feststellungen getroffen:   „TZ 1. Sonderbetriebsausgaben  a) Sachverhalt:  …  b) Steuerliche Würdigung:  Bei den angeführten „Modellentwicklungsaufwendungen“ handelt es sich um von der **AbisJ  GmbH & Co KG** an Dritte geleistete Ausgaben.

- missed: `AbisJ  GmbH & Co KG` (organisation)
- predicted in sentence: `AbisJ  GmbH`, `Co KG`

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_4`)

Entscheidungsgründe  Verfahrensgang:  Mit Bescheid des **Amtes für Betrugsbekämpfung** als Finanzstrafbehörde vom 25. März 2024,  Geschäftszahl *GZ*, wurde der Antrag der Beschwerdeführerin auf Wiedereinsetzung in den  vorigen Stand vom 05. März 2024 als unbegründet abgewiesen.

- missed: `Amtes für Betrugsbekämpfung` (organisation)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_54`)

Sie hat ab 1.6.2015 bis 31.10.2021 Rehabilitationsgeld, dies zwecks Wiederherstellung der  Arbeitsfähigkeit durch Reha-Maßnahmen, erhalten (siehe Schreiben **ÖGK** v. 8.10.2020 und PV- Bescheid 31.8.2021).

- missed: `ÖGK` (organisation)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_119`)

Zu den im Rahmen der Außenprüfung nicht zum Betriebsausgabenabzug anerkannten Eingangsrechnungen der **Fa.NEP Lebensmittel GmbH** und der Kisteler Telekom GmbH führte der Beschuldigte auf Befragung aus, er habe diese Firmen zwar am Beginn ihrer Tätigkeit dahingehend kontrolliert, dass er Firmenbuchauszug, Auszug aus dem Gewerberegister und der HFU- Liste sowie UID Nummern überprüft habe.

- missed: `Fa.NEP Lebensmittel GmbH` (organisation)
- predicted in sentence: `NEP Lebensmittel GmbH`, `Kisteler Telekom GmbH`

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch **Pilz + Rath Steuerberatung**, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

- missed: `Pilz + Rath Steuerberatung` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Bruck Eisenstadt Oberwart`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Li Lübkemann  in der   Beschwerdesache Theobald Tormöllen, Am Hora 38, 9554 Trenk, Österreich, vertreten durch **Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft**, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 2. September 2016 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 24. August 2016, ErfNr, betreffend Grunderwerbsteuer im  fortgesetzten Verfahren   zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Partner GmbH`, `Finanzamtes  für Gebühren`, `Finanzamt`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_61`)

Die Bf. habe höchstwahrscheinlich vermutet, dass sie bei der **Fa.DonauLogistik GmbH** als Angestellte  angemeldet gewesen sei.

- missed: `Fa.DonauLogistik GmbH` (organisation)
- predicted in sentence: `DonauLogistik GmbH`

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache OSR Juliette Franzisi, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des **Finanzamtes Wien  2/20/21/22** vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Finanzamtes Wien  2/20/21/22` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des **Finanzamtes Wien 9/18/19 Klosterneuburg** (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `MITTEREGGER Steuerberatungs  GmbH`, `Finanzamtes Wien 9/18/19`, `Finanzamt Österreich`

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des **Finanzamtes Wien 9/18/19  Klosterneuburg** vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

- missed: `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Wien 9/18/19`, `Finanzamtes Wien 9/18/19`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_167`)

Kann kein Firmenwert entstehen, weil die operativen Geschäfte (Vertragsreederei mit  Unternehmerrisiko) nicht von der Schifffahrtsgesellschaft S GmbH & Co KG, sondern von der L  GmbH & Co und der **Mohrlock Metall GmbH & Co KG** durchgeführt werden und besteht deshalb der Wert der  Gesellschaft lediglich im Buchwert inklusive der stillen Reserven des Schiffes, so ist dies ein  weiterer Hinweis dafür, dass keine mitunternehmerische Beteiligung, sondern eine Beteiligung  nach Art eines stillen Gesellschafters vorliegt.

- missed: `Mohrlock Metall GmbH & Co KG` (organisation)
- predicted in sentence: `Co KG`, `Mohrlock Metall GmbH`, `Co KG`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_54`)

Die **WKO** hat mir allerdings, bis heute, noch keinen Termin zugeteilt. Ob die WKO damit  Vorschriften verletzt, kann ich nicht beurteilen.

- missed: `WKO` (organisation)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_55`)

Beweiswürdigung  Der festgestellte Sachverhalt ergibt sich aus dem vom Finanzamt vorgelegten Veranlagungsakt  und dem Urteil des **Landesgerichtes** X, vom XX.X.2020, Gz xx.

- missed: `Landesgerichtes` (organisation)
- predicted in sentence: `Finanzamt`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140413.1`) (sent_id: `deanon_BFG_20260814_TEST/140413.1_47`)

Beweiswürdigung:  Die Feststellungen ergeben sich aus den eigenen Wahrnehmungen und Anzeigedaten des  Kontrollorgans der Parkraumüberwachung, den zur Beanstandungszeit angefertigten Fotos  sowie aus den Bescheiden des **Magistrates der Stadt Wien**, Magistratisches Bezirksamt für den  4. und 5. Bezirk.

- missed: `Magistrates der Stadt Wien` (organisation)
- predicted in sentence: `Stadt Wien`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch **Henning & Partner Steuerberatung GmbH**,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

- missed: `Henning & Partner Steuerberatung GmbH` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Partner Steuerberatung GmbH`, `Finanzamtes`, `Finanzamt Österreich`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146819.1`) (sent_id: `deanon_BFG_20260814_TEST/146819.1_49`)

Vom **Finanzamt Klagenfurt** wurde nach Auskunft der Vertragsteile für  6.1.1.

- missed: `Finanzamt Klagenfurt` (organisation)
- predicted in sentence: `Finanzamt`

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_40`)

2. Abweichend von Z 1 ist für Kinder, die sich ständig in einem anderen Mitgliedstaat der EU  oder Hoheitsgebiet einer anderen Vertragspartei des Abkommens über den Europäischen  Wirtschaftsraum oder der Schweiz aufhalten, die Höhe des Familienbonus Plus sowie der  Absetzbeträge gemäß Abs. 4 auf Basis der vom Statistischen Amt der **Europäischen Union**  veröffentlichten vergleichenden Preisniveaus für jeden einzelnen Mitgliedstaat der EU, jede  4 von 11 Seite 5 von 11

- missed: `Europäischen Union` (organisation)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_6`)

Entscheidungsgründe  I. Verfahrensgang  A) Verfahren vor dem **Finanzamt**:  1.)

- missed: `Finanzamt` (organisation)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_102`)

Laut § 1 des Vertrages stellt die Bf. als atypisch stille Gesellschafterin und Beteiligungsgeberin  eine Einlage, welche dem wirtschaftlichen Eigenkapital des Beteiligungsnehmers (**I AG**)  zugerechnet wird, von zumindest € 800.000,00 bis zu € 1.725.000,00 zur Verfügung.

- missed: `I AG` (organisation)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/144925.1`) (sent_id: `deanon_BFG_20260814_TEST/144925.1_5`)

Am 20.2.2024 übermittelte die Österreichische Gesundheitskasse (**ÖGK**) einen weiteren  Lohnzettel betreffend den Bf. für das Jahr 2023.

- missed: `ÖGK` (organisation)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_71`)

Wie bereits im angefochtenen Bescheid ausgeführt wurde, normiert § 48 BAO Folgendes:  „Das **Bundesministerium für Finanzen** kann bei Abgabepflichtigen, die der Abgabenhoheit  mehrerer Staaten unterliegen, soweit dies zur Ausgleichung der in- und ausländischen  Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit entsprechenden  Behandlung erforderlich ist anordnen, bestimmte Gegenstände ganz oder teilweise aus der  5 von 12 Seite 6 von 12

- missed: `Bundesministerium für Finanzen` (organisation)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_29`)

der Prüfungsbehörde **WKO** zur Wiederholung der Prüfung angemeldet.

- missed: `WKO` (organisation)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des **Finanzamtes Wien 12/13/14 Purkersdorf** vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- predicted in sentence: `Bundesfinanzgericht`, `Finanzamtes Wien 12/13/14`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des **FA Braunau Ried Schärding**  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

- missed: `FA Braunau Ried Schärding` (organisation)
- predicted in sentence: `Bundesfinanzgericht (BFG)`

</details>

---

