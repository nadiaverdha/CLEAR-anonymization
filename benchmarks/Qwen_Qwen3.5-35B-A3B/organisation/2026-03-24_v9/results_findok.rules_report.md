# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-24T19:46:33.272422

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

### Configuration

| Parameter | Value |
|-----------|-------|
| Shots per class | 20 |
| Training examples | 20 |
| Test examples | 50 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 10 |
| Refinement iterations | 10 |
| Seed | 42 |
| Agentic | True|
| Enable Critic | False |
| Enable Prune | False|
| Critic Interval | 0 |
| Audit Interval | 0|
| Use GREX | True |

### Results

| Metric | Value |
|--------|-------|
| Accuracy (exact match) | 34.0% |
| Coverage | 80.0% (40/50 got a label) |
| Micro Precision | 0.650 |
| Micro Recall | 0.371 |
| Micro F1 | 0.473 |
| Macro F1 | 0.473 |

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `German FA Entities` | 🔴 Weak | 0.302 | 0.812 | 0.186 | 16 |
| `German GmbH Entities` | 🔴 Weak | 0.186 | 0.500 | 0.114 | 16 |
| `German Specific Org Entities` | 🔴 Weak | 0.108 | 1.000 | 0.057 | 4 |
| `German Specific Compound GmbH Entities` | 🔴 Weak | 0.082 | 1.000 | 0.043 | 3 |
| `German AG Entities` | 🔴 Weak | 0.027 | 0.250 | 0.014 | 4 |
| `German GmbH & Co KG Entities` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |

---

## `German FA Entities`

🔴 Weak rule

> Matches Finanzamt or FA followed by specific location patterns including numbers, hyphens, and multi-word locations to prevent partial matches.

**F1:** 0.302 | **Precision:** 0.812 | **Recall:** 0.186  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Finanzamt|FA)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*|\d+(?:[\s/\-]+\d+)*|\d+(?:[\s/\-]+\d+)*\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|\d+(?:[\s/\-]+\d+)*\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.812 | 0.186 | 0.302 | 16 | 13 | 3 | 13/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 13 | 3 | 57 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die 
Beschwerde des Tobias Dörffler, Castellezgasse 2, 6234 Brandenberg, Österreich, vom 8. Oktober 2020 gegen den Bescheid des 
Finanzamt Landeck Reutte  vom 21. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 
2019 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Landeck Reutte` | `Finanzamt Landeck Reutte` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht erkennt durch den Richter Hon.-Prof. René Hucken  in der Beschwerdesache 
Georgette Nessler, LLB, Dr. Stefan Lehner-Gasse 37, 3200 Grub, Österreich, über die Beschwerde vom 5. Dezember 2022 gegen den 
Abweisungsbescheid des Finanzamt Judenburg Liezen  vom 25. November 2022 betreffend Aufhebung des 
Einkommensteuerbescheides 2019, Steuernummer 10-922/4406, zu Recht:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Niederösterreich Mitte` | `Finanzamt Niederösterreich Mitte` |
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dagmar de Lang  in der Beschwerdesache 
Liu Rempis, Reichenfeldgasse 12, 3664 Roggenreith, Österreich, vertreten durch BDO Audit GmbH Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, 
über die Beschwerde vom 5. Oktober 2015 gegen den Bescheid des Finanzamt Judenburg Liezen  vom 
14. September 2015 betreffend Dienstgeberbeitrag 2010, 2011, 2012 und 2013 zu Recht 
erkannt:  
 
Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 5**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Desiree Hertwick  in der Beschwerdesache des 
Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April 
2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Deutschlandsberg Leibnitz Voitsberg  vom 
7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer 
54-373/7804  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
FA Salzburg-Stadt  ist für das Betreiben der Website, das Einrichten und die laufende Betreuung der 
Teilnehmerkonten, die Vermittlung von Tipps auf den Ausgang von Lotterien an KommR Ing. Roberta Gossling, die 
Organisation und entsprechende Vermittlung von Spielgemeinschaften, die Leistung der 
Einsätze der Teilnehmer an KommR Ing. Roberta Gossling  und die Weiterleitung der von KommR Ing. Roberta Gossling  erhaltenen 
Gewinne an die Teilnehmer gemäß diesen Geschäftsbedingungen verantwortlich.
```

- Missed: `FA Salzburg-Stadt`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Emma Stranghöhner  in der Beschwerdesache der 
Psomadakis Touristik, Andreas-Rainer-Weg 13, 9111 Mittertrixen, Österreich, über die Beschwerde vom 10. September 2018 gegen die 
Bescheide des Finanzamt Salzburg-Stadt  vom 20. August 2018 betreffend Festsetzung der 
Normverbrauchsabgabe für den Zeitraum April 2014 und Festsetzung der Kraftfahrzeugsteuer 
für die Zeiträume April bis Juni 2014, Juli bis Dezember 2014, Jänner bis Dezember 2015, 
Jänner bis Dezember 2016, Jänner bis Dezember 2017 und Jänner bis Juni 2018 zu Recht 
erkannt:  
 
I. Die Beschwerde gegen den Bescheid über die Festsetzung der 
Normverbrauchsabgabe für den Zeitraum April 2014 wird als unbegründet 
abgewiesen.
```

- Missed: `Psomadakis Touristik`

- Missed: `Finanzamt Salzburg-Stadt`


```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Annemie Bott`

- Missed: `Grönemeier&Hövelberndt E‑Commerce`

- Missed: `Krolitzki Beratung`

- Missed: `Milan Händlein`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
FA Salzburg-Stadt  ist für das Betreiben der Website, das Einrichten und die laufende Betreuung der 
Teilnehmerkonten, die Vermittlung von Tipps auf den Ausgang von Lotterien an KommR Ing. Roberta Gossling, die 
Organisation und entsprechende Vermittlung von Spielgemeinschaften, die Leistung der 
Einsätze der Teilnehmer an KommR Ing. Roberta Gossling  und die Weiterleitung der von KommR Ing. Roberta Gossling  erhaltenen 
Gewinne an die Teilnehmer gemäß diesen Geschäftsbedingungen verantwortlich.
```

- FP: `FA Salzburg`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Emma Stranghöhner  in der Beschwerdesache der 
Psomadakis Touristik, Andreas-Rainer-Weg 13, 9111 Mittertrixen, Österreich, über die Beschwerde vom 10. September 2018 gegen die 
Bescheide des Finanzamt Salzburg-Stadt  vom 20. August 2018 betreffend Festsetzung der 
Normverbrauchsabgabe für den Zeitraum April 2014 und Festsetzung der Kraftfahrzeugsteuer 
für die Zeiträume April bis Juni 2014, Juli bis Dezember 2014, Jänner bis Dezember 2015, 
Jänner bis Dezember 2016, Jänner bis Dezember 2017 und Jänner bis Juni 2018 zu Recht 
erkannt:  
 
I. Die Beschwerde gegen den Bescheid über die Festsetzung der 
Normverbrauchsabgabe für den Zeitraum April 2014 wird als unbegründet 
abgewiesen.
```

- FP: `Finanzamt Salzburg`


</details>

---

## `German GmbH Entities`

🔴 Weak rule

> Matches [Name] GmbH/GMBH, excluding common nouns like 'Bau', 'Firma', 'Gesellschaft' at the start, and ensuring the name is substantial.

**F1:** 0.186 | **Precision:** 0.500 | **Recall:** 0.114  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b((?!Bau|Firma|Gesellschaft|Dienstleistungen|Systeme|Technologien|Landwirtschaft|Gastronomie|Versand|Luftfahrt|Verlag|Sicherheit|Steuerberatung|Forschung|Handel|Immobilien|Bau|Bau-|Bau_)[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*|\b[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)\s+(?:GmbH|GMBH)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.500 | 0.114 | 0.186 | 16 | 8 | 8 | 8/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 8 | 8 | 62 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 2**

```
Mit einer weiteren FinanzOnline-Eingabe vom 18.9.2020 brachte die Gartgart Dienstleistungen GMBH  unter 
ihrer FinanzOnline-Teilnehmeridentifikation unter der Rubrik „Sonstige Anbringen“ einen 
Vorlageantrag gegen eine an sie selbst gerichtete Beschwerdevorentscheidung vom 9.9.2020 
betreffend eine gegenüber ihr selbst festgesetzte Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO ein.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 3**

```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4**

```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

| Prediction | Gold |
|------------|------|
| `Nexgartuni Finanzen Planung GMBH` | `Nexgartuni Finanzen Planung GMBH` |

**Example 5**

```
Zu berücksichtigen ist in diesem Zusammenhang, dass die Bludszat Maschinenbau GMBH  über einen bereits 
länger davor liegenden Zeitraum Bautätigkeiten ausgeführt hat und jeweils fristgerecht um 
notwendige Genehmigungen angesucht und auch die vorgeschriebenen Gebühren entrichtet 
hat.
```

| Prediction | Gold |
|------------|------|
| `Bludszat Maschinenbau GMBH` | `Bludszat Maschinenbau GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Niederösterreich Mitte`

- Missed: `FA Niederösterreich Mitte`


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- Missed: `Klusner&Päffgen Bildung GMBH`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dagmar de Lang  in der Beschwerdesache 
Liu Rempis, Reichenfeldgasse 12, 3664 Roggenreith, Österreich, vertreten durch BDO Audit GmbH Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, 
über die Beschwerde vom 5. Oktober 2015 gegen den Bescheid des Finanzamt Judenburg Liezen  vom 
14. September 2015 betreffend Dienstgeberbeitrag 2010, 2011, 2012 und 2013 zu Recht 
erkannt:  
 
Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Judenburg Liezen`


```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

- Missed: `KQPC Versand GMBH`


```
II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ. 
MA6/206000003065/2020, wurde Herr Valentina Riehmers, (in weiterer Folge: Beschuldigter) als 
handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  mit Sitz in Mosletzberg 2, 4084 Dörfledt, Österreich, 
schuldig erkannt,  
1. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juni 2020 vor 
der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür 
bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet habe.
```

- Missed: `UnterRecycling Services GMBH`

- Missed: `UnterRecycling Services GMBH`


</details>

<details>
<summary>⚠️ False Positives (4)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- FP: `Wiedlroither GmbH`


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Päffgen Bildung GMBH`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dagmar de Lang  in der Beschwerdesache 
Liu Rempis, Reichenfeldgasse 12, 3664 Roggenreith, Österreich, vertreten durch BDO Audit GmbH Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, 
über die Beschwerde vom 5. Oktober 2015 gegen den Bescheid des Finanzamt Judenburg Liezen  vom 
14. September 2015 betreffend Dienstgeberbeitrag 2010, 2011, 2012 und 2013 zu Recht 
erkannt:  
 
Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- FP: `Audit GmbH`


```
II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ. 
MA6/206000003065/2020, wurde Herr Valentina Riehmers, (in weiterer Folge: Beschuldigter) als 
handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  mit Sitz in Mosletzberg 2, 4084 Dörfledt, Österreich, 
schuldig erkannt,  
1. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juni 2020 vor 
der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür 
bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet habe.
```

- FP: `Services GMBH`

- FP: `Services GMBH`


</details>

---

## `German Specific Org Entities`

🔴 Weak rule

> Matches specific known entities that might not fit the general patterns (e.g., 'Bezirksgericht', 'Verlag', 'Luftfahrt' without GmbH/AG, and specific names like Chen Setzekorn).

**F1:** 0.108 | **Precision:** 1.000 | **Recall:** 0.057  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Bezirksgericht\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|Dorfcon\-Verlag|Depp\s+Versand|Chen\s+Setzekorn|Vahrenkamp\s+Luftfahrt|Schmeltz\s+Luftfahrt|WaldTouristik\s+Technologien|Heimwald\-Forschung\s+GMBH)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.057 | 0.108 | 4 | 4 | 0 | 4/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 66 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2**

```
Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R-
Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Frau M.: 
Frau  
Vahrenkamp Luftfahrt  
B-Straße 4/7 
9999 Wien 
Betreff: M.-GmbH in Liqu.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 3**

```
Gewinne 
216.864,04 80.229,07   885.959,89 1.183.053,01 
Ergebnis lt. BP -665.812,12 -246.317,88   -2.720.058,29  -3.632.188,28 
Ergebnis 
Dorfcon-Verlag 
-665.812,12      
5 von 39
Seite 6 von 39
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4**

```
Da die Auskünfte des vertretungsbefugten Gesellschafters der Chen Setzekorn  wenig aufschlussreich 
waren, begann der Außenprüfer, aber auch der Sachbearbeiter des Rechtsmittels, die 
Abgabengebarung der angeblichen Subunternehmer im maßgeblichen Zeitraum zu 
durchleuchten: 
1. C BaugmbH: 
Eine Außenprüfung des zuständigen Finanzamtes hat für den Zeitraum 11/2011 - 6/2012 
ergeben, dass im fraglichen Zeitraum zwar geringfügige Abgabenbetrage im Namen der C 
GmbH gemeldet wurden, aber aufgrund durchgeführter Ermittlungen am dem FA gemeldeten 
Betriebsort kein Anhaltspunkt für eine Betriebstätigkeit - Leistungen im Bereich des 
Baunebengewerbes - gefunden werden konnten.
```

| Prediction | Gold |
|------------|------|
| `Chen Setzekorn` | `Chen Setzekorn` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

- Missed: `Roelfsen Versicherung`

- Missed: `Roelfsen Versicherung`


</details>

---

## `German Specific Compound GmbH Entities`

🔴 Weak rule

> Matches specific known compound names that fail the general pattern due to hyphens or specific structures (Waldver, Kraftver, Gartgart, OGEM). Priority 10 to ensure full match before general rules.

**F1:** 0.082 | **Precision:** 1.000 | **Recall:** 0.043  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Waldver\s+E\u2011Commerce\s+Systeme\s+GMBH|Kraftver\-Gastronomie\s+GMBH|Gartgart\s+Dienstleistungen\s+GMBH|OGEM\s+Landwirtschaft\s+GMBH)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.043 | 0.082 | 3 | 3 | 0 | 3/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 67 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 2**

```
Mit einer weiteren FinanzOnline-Eingabe vom 18.9.2020 brachte die Gartgart Dienstleistungen GMBH  unter 
ihrer FinanzOnline-Teilnehmeridentifikation unter der Rubrik „Sonstige Anbringen“ einen 
Vorlageantrag gegen eine an sie selbst gerichtete Beschwerdevorentscheidung vom 9.9.2020 
betreffend eine gegenüber ihr selbst festgesetzte Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO ein.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

</details>

---

## `German AG Entities`

🔴 Weak rule

> Matches [Name] AG or Aktiengesellschaft to catch unseen companies.

**F1:** 0.027 | **Precision:** 0.250 | **Recall:** 0.014  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*\s+(?:AG|Aktiengesellschaft))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.250 | 0.014 | 0.027 | 4 | 1 | 3 | 1/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 3 | 69 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

| Prediction | Gold |
|------------|------|
| `Schiwick Finanzen AG` | `Schiwick Finanzen AG` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- Missed: `Talkel-Versand AG`

- Missed: `Hebebrand Recycling AG`


```
Das von der Tochter der Bf in den Monaten März bis Mai 2022 absolvierte Praktikum in den 
Kliniken „Logseemon-Metall AG“, Bildungszentrum für Gesundheitsberufe war - für sich alleine 
betrachtet - zweifellos nicht in Form einer schulischen oder kursmäßigen Ausbildung 
organisiert.
```

- Missed: `Logseemon-Metall AG`


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Verdonlex Automotive GMBH`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Versand AG`

- FP: `Arbeitgeber Hebebrand Recycling AG`


```
Das von der Tochter der Bf in den Monaten März bis Mai 2022 absolvierte Praktikum in den 
Kliniken „Logseemon-Metall AG“, Bildungszentrum für Gesundheitsberufe war - für sich alleine 
betrachtet - zweifellos nicht in Form einer schulischen oder kursmäßigen Ausbildung 
organisiert.
```

- FP: `Metall AG`


</details>

---

## `German GmbH & Co KG Entities`

🔴 Weak rule

> Matches [Proper Noun] GmbH & Co KG. Tightened to require a proper noun start to avoid common nouns like 'Heizung'.

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*\s+GmbH\s*&\s*Co\s*KG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 0 | 70 |

</details>

---

