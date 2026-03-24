# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-24T18:30:35.520783

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
| Agentic | False|
| Enable Critic | False |
| Enable Prune | False|
| Critic Interval | 0 |
| Audit Interval | 0|
| Use GREX | True |

### Results

| Metric | Value |
|--------|-------|
| Accuracy (exact match) | 38.0% |
| Coverage | 66.0% (33/50 got a label) |
| Micro Precision | 0.818 |
| Micro Recall | 0.386 |
| Micro F1 | 0.524 |
| Macro F1 | 0.524 |

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `Specific Organisation Entities` | 🔴 Weak | 0.272 | 1.000 | 0.157 | 11 |
| `German Finanzamt Entities` | 🔴 Weak | 0.228 | 1.000 | 0.129 | 9 |
| `FA Abbreviation Entities` | 🔴 Weak | 0.182 | 1.000 | 0.100 | 7 |
| `German GmbH Entities` | 🔴 Weak | 0.051 | 0.250 | 0.029 | 8 |

---

## `Specific Organisation Entities`

🔴 Weak rule

> Matches specific known entities that do not follow standard suffix patterns or use abbreviations like FA.

**F1:** 0.272 | **Precision:** 1.000 | **Recall:** 0.157  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b((?:FA\s+Grieskirchen\s+Wels|Chen\s+Setzekorn|Vahrenkamp\s+Luftfahrt|Waldver\s+E\u2011Commerce\s+Systeme\s+GMBH|Bezirksgericht\s+Silz|Gartgart\s+Dienstleistungen\s+GMBH|Kraftver\-Gastronomie\s+GMBH|Finanzamt\s+Steiermark\s+Mitte|Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Finanzamt\s+Wien\s+8/16/17|OGEM\s+Landwirtschaft\s+GMBH|WaldTouristik\s+Technologien|Finanzamt\s+Innsbruck|Depp\s+Versand|Heimwald\-Forschung\s+GMBH|Bludszat\s+Maschinenbau\s+GMBH|Schiwick\s+Finanzen\s+AG|Donau\s+Furtkraftwald\s+AG))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.157 | 0.272 | 11 | 11 | 0 | 11/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 11 | 0 | 59 |

</details>

<details>
<summary>✅ Worked (5)</summary>

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
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 3**

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

**Example 4**

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

**Example 5**

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

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

- Missed: `Roelfsen Versicherung`

- Missed: `Roelfsen Versicherung`


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Verdonlex Automotive GMBH`


</details>

---

## `German Finanzamt Entities`

🔴 Weak rule

> Matches Finanzamt with specific known locations or multi-word location patterns to ensure full entity capture.

**F1:** 0.228 | **Precision:** 1.000 | **Recall:** 0.129  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Finanzamt\s+(?:Steiermark\s+Mitte|Wien\s+8/16/17|Innsbruck|Gmunden\s+V\u00f6cklabruck|Judenburg\s+Liezen|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Nieder\u00f6sterreich\s+Mitte|[A-Z][A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\-]+(?:\s+[A-Z][A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\-]+)*))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.129 | 0.228 | 9 | 9 | 0 | 9/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 9 | 0 | 61 |

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

| Prediction | Gold |
|------------|------|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 4**

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

**Example 5**

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

</details>

<details>
<summary>❌ Missed (4)</summary>

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


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Niederösterreich Mitte`


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


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Graz-Stadt`


</details>

---

## `FA Abbreviation Entities`

🔴 Weak rule

> Matches Finanzamt abbreviations (FA) followed by one or more capitalized location words, ensuring strict boundaries to avoid context capture.

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bFA\s+([A-Z][A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\-]+(?:\s+[A-Z][A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\-]+)*)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.100 | 0.182 | 7 | 7 | 0 | 7/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 7 | 0 | 63 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
FA Salzburg-Stadt  ist für das Betreiben der Website, das Einrichten und die laufende Betreuung der 
Teilnehmerkonten, die Vermittlung von Tipps auf den Ausgang von Lotterien an KommR Ing. Roberta Gossling, die 
Organisation und entsprechende Vermittlung von Spielgemeinschaften, die Leistung der 
Einsätze der Teilnehmer an KommR Ing. Roberta Gossling  und die Weiterleitung der von KommR Ing. Roberta Gossling  erhaltenen 
Gewinne an die Teilnehmer gemäß diesen Geschäftsbedingungen verantwortlich.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

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
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Example 3**

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

**Example 4**

```
BESCHLUSS 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Rebecca Altenhöfer  in der Beschwerdesache 
Verlass nach VetR Oskar Wäger, Am Mautbühel 21, 4925 Kronawitten, Österreich, betreffend die Beschwerde vom 15.Okt 2014 gegen 
die zur Steuernummer 80-591/3533  ergangenen Bescheide des FA Gmunden Vöcklabruck (jetzt 
Dienststelle des Finanzamtes Österreich) vom 23. Juni 2014 betreffend Umsatzsteuer und 
Einkommensteuer 2006 - 2010 beschlossen: 
Die Beschwerde wird gemäß § 278 Abs. 1 lit. b BAO als gegenstandslos erklärt.
```

| Prediction | Gold |
|------------|------|
| `FA Gmunden Vöcklabruck` | `FA Gmunden Vöcklabruck` |

**Example 5**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

</details>

<details>
<summary>❌ Missed (2)</summary>

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


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Niederösterreich Mitte`


</details>

---

## `German GmbH Entities`

🔴 Weak rule

> Matches German company names ending in GmbH, AG, KG, etc., ensuring the name starts with a capitalized letter and excludes preceding articles/prepositions.

**F1:** 0.051 | **Precision:** 0.250 | **Recall:** 0.029  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![a-zA-Z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\s])([A-Z][A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF\s\-\.]+?\s+(?:GmbH|AG|KG|GmbH\s*&\s*Co\s*KG))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.250 | 0.029 | 0.051 | 8 | 2 | 6 | 2/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 6 | 68 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

**Example 2**

```
Das von der Tochter der Bf in den Monaten März bis Mai 2022 absolvierte Praktikum in den 
Kliniken „Logseemon-Metall AG“, Bildungszentrum für Gesundheitsberufe war - für sich alleine 
betrachtet - zweifellos nicht in Form einer schulischen oder kursmäßigen Ausbildung 
organisiert.
```

| Prediction | Gold |
|------------|------|
| `Logseemon-Metall AG` | `Logseemon-Metall AG` |

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
A B handelte dabei 
ungewöhnlich auffallend sorgfaltswidrig und waren die dadurch entstanden 
Abgabenverkürzungen für ihn geradezu wahrscheinlich vorhersehbar, ein korrektes Vorgehen 
war dem Beschuldigten angesichts seiner langjährigen Unternehmenseigenschaft als 
Geschäftsführer der Pastl+Bächle Handel  und B GmbH zumutbar.
```

- Missed: `Pastl+Bächle Handel`


```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- Missed: `Traun-Digital KG`


```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

- Missed: `Nord Willemtri KG`


```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- Missed: `Talkel-Versand AG`

- Missed: `Hebebrand Recycling AG`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- FP: `TREUHAND Wiedlroither GmbH`


```
A B handelte dabei 
ungewöhnlich auffallend sorgfaltswidrig und waren die dadurch entstanden 
Abgabenverkürzungen für ihn geradezu wahrscheinlich vorhersehbar, ein korrektes Vorgehen 
war dem Beschuldigten angesichts seiner langjährigen Unternehmenseigenschaft als 
Geschäftsführer der Pastl+Bächle Handel  und B GmbH zumutbar.
```

- FP: `Bächle Handel  und B GmbH`


```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- FP: `Digital KG`


```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

- FP: `Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG`


```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Versand AG`


</details>

---

