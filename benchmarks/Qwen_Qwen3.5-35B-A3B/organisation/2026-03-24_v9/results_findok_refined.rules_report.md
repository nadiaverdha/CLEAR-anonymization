# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-24T20:42:41.951895

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
| Accuracy (exact match) | 30.0% |
| Coverage | 100.0% (50/50 got a label) |
| Micro Precision | 0.560 |
| Micro Recall | 0.400 |
| Micro F1 | 0.467 |
| Macro F1 | 0.467 |

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `Specific Organisation Names` | 🔴 Weak | 0.228 | 1.000 | 0.129 | 9 |
| `German Finanzamt Entities` | 🔴 Weak | 0.175 | 0.700 | 0.100 | 10 |
| `German FA Entities` | 🔴 Weak | 0.130 | 0.714 | 0.071 | 7 |
| `German GmbH Entities` | 🔴 Weak | 0.119 | 0.357 | 0.071 | 14 |
| `German Versicherung Entities` | 🔴 Weak | 0.082 | 1.000 | 0.043 | 3 |
| `German AG Entities` | 🔴 Weak | 0.027 | 0.250 | 0.014 | 4 |
| `German KG Entities` | 🔴 Weak | 0.026 | 0.167 | 0.014 | 6 |
| `German GmbH & Co KG Entities` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |
| `German GmbH & Co Entities` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |

---

## `Specific Organisation Names`

🔴 Weak rule

> Matches specific known organisation names that do not follow the standard GMBH/AG/KG pattern or have unique structures.

**F1:** 0.228 | **Precision:** 1.000 | **Recall:** 0.129  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Chen Setzekorn|Vahrenkamp Luftfahrt|Bezirksgericht Silz|WaldTouristik Technologien|Dorfcon-Verlag|Depp Versand|Kraftver-Gastronomie GMBH|Gartgart Dienstleistungen GMBH|OGEM Landwirtschaft GMBH|Waldver E‑Commerce Systeme GMBH|Finanzamt Niederösterreich Mitte)\b`

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

</details>

<details>
<summary>❌ Missed (3)</summary>

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
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Graz-Stadt`


</details>

---

## `German Finanzamt Entities`

🔴 Weak rule

> Matches German tax offices (Finanzamt) followed by location names, including broader location patterns.

**F1:** 0.175 | **Precision:** 0.700 | **Recall:** 0.100  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(Finanzamt\s+(?:Steiermark\s+Mitte|Wien\s+8/16/17|Innsbruck|Grieskirchen\s+Wels|Silz|Steiermark|Wien|Innsbruck|Grieskirchen|Nieder\u00f6sterreich\s+Mitte|Deutschlandsberg\s+Leibnitz\s+Voitsberg|\w+\s+\w+))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.700 | 0.100 | 0.175 | 10 | 7 | 3 | 7/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 7 | 3 | 63 |

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
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

- Missed: `Roelfsen Versicherung`

- Missed: `Dorfcon-Verlag`

- Missed: `Roelfsen Versicherung`


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
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Desiree Hertwick  in der Beschwerdesache des 
Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April 
2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Deutschlandsberg Leibnitz Voitsberg  vom 
7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer 
54-373/7804  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- Missed: `FA Deutschlandsberg Leibnitz Voitsberg`


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
BESCHLUSS 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Janina Schuetter  in der Rechtssache des A, Adresse_A, 
über den Antrag vom 28. April 2021 auf Gewährung von Verfahrenshilfe im 
Beschwerdeverfahren betreffend die Wiederaufnahme der Verfahren hinsichtlich 
Umsatzsteuer und Einkommensteuer jeweils für die Jahre 2014 bis 2016, die Aufhebung des 
Umsatzsteuerbescheides und des Einkommensteuerbescheides jeweils für das Jahr 2017, die 
Umsatzsteuerbescheide und die Einkommensteuerbescheide für die Jahre 2014 bis 2017 sowie 
die Bescheide über die Festsetzung von Anspruchszinsen für die Jahre 2014 und 2015 
(Bescheide des Finanzamt Oststeiermark  vom 18.12.2019 zu Steuernummer Steuernummer_A ) beschlossen: 
Der Antrag auf Gewährung von Verfahrenshilfe wird abgewiesen.
```

- Missed: `Finanzamt Oststeiermark`


</details>

<details>
<summary>⚠️ False Positives (3)</summary>

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

- FP: `Finanzamt den erzielten`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Desiree Hertwick  in der Beschwerdesache des 
Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April 
2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Deutschlandsberg Leibnitz Voitsberg  vom 
7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer 
54-373/7804  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `Finanzamt eingelangt am`


```
BESCHLUSS 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Janina Schuetter  in der Rechtssache des A, Adresse_A, 
über den Antrag vom 28. April 2021 auf Gewährung von Verfahrenshilfe im 
Beschwerdeverfahren betreffend die Wiederaufnahme der Verfahren hinsichtlich 
Umsatzsteuer und Einkommensteuer jeweils für die Jahre 2014 bis 2016, die Aufhebung des 
Umsatzsteuerbescheides und des Einkommensteuerbescheides jeweils für das Jahr 2017, die 
Umsatzsteuerbescheide und die Einkommensteuerbescheide für die Jahre 2014 bis 2017 sowie 
die Bescheide über die Festsetzung von Anspruchszinsen für die Jahre 2014 und 2015 
(Bescheide des Finanzamt Oststeiermark  vom 18.12.2019 zu Steuernummer Steuernummer_A ) beschlossen: 
Der Antrag auf Gewährung von Verfahrenshilfe wird abgewiesen.
```

- FP: `Finanzamt Oststeiermark  vom`


</details>

---

## `German FA Entities`

🔴 Weak rule

> Matches the abbreviation FA (Finanzamt) followed by specific location names.

**F1:** 0.130 | **Precision:** 0.714 | **Recall:** 0.071  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(FA\s+(?:Steiermark\s+Mitte|Wien\s+8/16/17|Innsbruck|Grieskirchen\s+Wels|Silz|Steiermark|Wien|Innsbruck|Grieskirchen|Nieder\u00f6sterreich\s+Mitte|Deutschlandsberg\s+Leibnitz\s+Voitsberg|\w+\s+\w+))\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.714 | 0.071 | 0.130 | 7 | 5 | 2 | 5/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 2 | 65 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

**Example 2**

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

**Example 3**

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

**Example 4**

```
Bei Teilnahme erteilt der Spielteilnehmer FA Grieskirchen Wels  den Auftrag, für ihn bei 
9 von 27
Seite 10 von 27
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 5**

```
Damit erweist sich die 
Begründung des FA Grieskirchen Wels  auf Seite 13 Absatz 2 als unzutreffend bzw steht diese im 
Widerspruch zur Entscheidung des VwGH.
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

</details>

<details>
<summary>❌ Missed (3)</summary>

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
Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R-
Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Frau M.: 
Frau  
Vahrenkamp Luftfahrt  
B-Straße 4/7 
9999 Wien 
Betreff: M.-GmbH in Liqu.
```

- Missed: `Vahrenkamp Luftfahrt`


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

- Missed: `Chen Setzekorn`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Am 5.Nov.2019 erging - als eine von drei getrennt an die Miteigentümer der Liegenschaft R-
Gasse 15 ausgefertigten Bescheiden - folgende Erledigung des FA an Frau M.: 
Frau  
Vahrenkamp Luftfahrt  
B-Straße 4/7 
9999 Wien 
Betreff: M.-GmbH in Liqu.
```

- FP: `FA an Frau`


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

- FP: `FA gemeldeten 
Betriebsort`


</details>

---

## `German GmbH Entities`

🔴 Weak rule

> Matches German limited liability companies ending in GMBH, requiring the name to start with a capital letter to avoid matching preceding context.

**F1:** 0.119 | **Precision:** 0.357 | **Recall:** 0.071  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+GMBH\b)`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.357 | 0.071 | 0.119 | 14 | 5 | 9 | 5/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 9 | 65 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

**Example 2**

```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3**

```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

| Prediction | Gold |
|------------|------|
| `Nexgartuni Finanzen Planung GMBH` | `Nexgartuni Finanzen Planung GMBH` |

**Example 4**

```
Zu berücksichtigen ist in diesem Zusammenhang, dass die Bludszat Maschinenbau GMBH  über einen bereits 
länger davor liegenden Zeitraum Bautätigkeiten ausgeführt hat und jeweils fristgerecht um 
notwendige Genehmigungen angesucht und auch die vorgeschriebenen Gebühren entrichtet 
hat.
```

| Prediction | Gold |
|------------|------|
| `Bludszat Maschinenbau GMBH` | `Bludszat Maschinenbau GMBH` |

**Example 5**

```
Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch 
einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH 
hinsichtlich der oa.
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- Missed: `Gartgart Dienstleistungen GMBH`

- Missed: `Kraftver-Gastronomie GMBH`


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- Missed: `Klusner&Päffgen Bildung GMBH`


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


```
Der Wille der Bf als Gruppenträgerin und der Klusner&Päffgen Bildung GMBH  auf 
Aufnahme der Klusner&Päffgen Bildung GMBH  in die Gruppe ab dem Jahr 2018 geht schon aus den 
eingebrachten Beschwerden der Bf und der Klusner&Päffgen Bildung GMBH (GZ RV/6100502/2017) hervor.
```

- Missed: `Klusner&Päffgen Bildung GMBH`

- Missed: `Klusner&Päffgen Bildung GMBH`

- Missed: `Klusner&Päffgen Bildung GMBH`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- FP: `Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH`


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Päffgen Bildung GMBH`


```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

- FP: `Die KQPC Versand GMBH`


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

- FP: `Geschäftsführer der Firma UnterRecycling Services GMBH`

- FP: `Geschäftsführer der Firma UnterRecycling Services GMBH`


```
Der Wille der Bf als Gruppenträgerin und der Klusner&Päffgen Bildung GMBH  auf 
Aufnahme der Klusner&Päffgen Bildung GMBH  in die Gruppe ab dem Jahr 2018 geht schon aus den 
eingebrachten Beschwerden der Bf und der Klusner&Päffgen Bildung GMBH (GZ RV/6100502/2017) hervor.
```

- FP: `Päffgen Bildung GMBH`

- FP: `Päffgen Bildung GMBH`

- FP: `Päffgen Bildung GMBH`


</details>

---

## `German Versicherung Entities`

🔴 Weak rule

> Matches German insurance companies ending in Versicherung, requiring the name to start with a capital letter.

**F1:** 0.082 | **Precision:** 1.000 | **Recall:** 0.043  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+Versicherung\b)`

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
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2**

```
Rechtsansicht 
des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten 
innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei 
der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen 
Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen 
Verlusten) bei der Roelfsen Versicherung  führt.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

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

- Missed: `Dorfcon-Verlag`


```
Rechtsansicht 
des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten 
innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei 
der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen 
Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen 
Verlusten) bei der Roelfsen Versicherung  führt.
```

- Missed: `Houdek Maschinenbau`


</details>

---

## `German AG Entities`

🔴 Weak rule

> Matches German stock corporations ending in AG, requiring the name to start with a capital letter.

**F1:** 0.027 | **Precision:** 0.250 | **Recall:** 0.014  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+AG\b)`

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
<summary>❌ Missed (2)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- Missed: `Talkel-Versand AG`

- Missed: `Hebebrand Recycling AG`


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Schiwick Finanzen AG`

- Missed: `Verdonlex Automotive GMBH`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG`

- FP: `Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG`


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- FP: `Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG`


</details>

---

## `German KG Entities`

🔴 Weak rule

> Matches German limited partnerships ending in KG, requiring the name to start with a capital letter to avoid matching preceding context.

**F1:** 0.026 | **Precision:** 0.167 | **Recall:** 0.014  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+KG\b)`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.167 | 0.014 | 0.026 | 6 | 1 | 5 | 1/70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 5 | 69 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

- Missed: `Lexkel Vertrieb KG`


```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

- Missed: `Lexkel Vertrieb KG`


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
Im Jahr 2015 erfolgte eine Betriebsprüfung bei der Schoenfelder Textil KG  hinsichtlich Feststellung von 
Einkünften gemäß § 188 BAO betreffend ua. das Jahr 2005.
```

- Missed: `Schoenfelder Textil KG`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

- FP: `Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG`


```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

- FP: `Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG`


```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- FP: `Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG`


```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

- FP: `Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG`


```
Im Jahr 2015 erfolgte eine Betriebsprüfung bei der Schoenfelder Textil KG  hinsichtlich Feststellung von 
Einkünften gemäß § 188 BAO betreffend ua. das Jahr 2005.
```

- FP: `Betriebsprüfung bei der Schoenfelder Textil KG`


</details>

---

## `German GmbH & Co KG Entities`

🔴 Weak rule

> Matches German limited partnerships with GmbH & Co KG structure.

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+GmbH\s*&\s*Co\s*KG\b)`

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

## `German GmbH & Co Entities`

🔴 Weak rule

> Matches German entities with GmbH & Co structure (without KG).

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<![\w])([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s\-]*\s+GmbH\s*&\s*Co\b)`

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

