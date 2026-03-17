# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-16T14:40:06.174908

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `specific_organisation_names` | 🔴 Weak | 0.442 | 0.991 | 0.284 | 562 |
| `finanzamt_organisation` | 🔴 Weak | 0.425 | 0.987 | 0.271 | 538 |
| `standalone_legal_form` | 🔴 Weak | 0.258 | 0.574 | 0.166 | 566 |
| `company_legal_form_suffix` | 🔴 Weak | 0.253 | 0.563 | 0.163 | 567 |
| `company_with_hyphen` | 🔴 Weak | 0.253 | 0.563 | 0.163 | 567 |
| `organisation_generic` | 🔴 Weak | 0.126 | 0.273 | 0.082 | 586 |
| `organisation_with_special_chars` | 🔴 Weak | 0.020 | 0.169 | 0.011 | 124 |
| `bank_kasse_organisation` | 🔴 Weak | 0.018 | 0.529 | 0.009 | 34 |
| `organisation_og` | 🔴 Weak | 0.005 | 0.500 | 0.003 | 10 |
| `umwelt_organisation` | 🔴 Weak | 0.003 | 1.000 | 0.002 | 3 |

---

## `specific_organisation_names`

🔴 Weak rule

> specific_organisation_names

**F1:** 0.442 | **Precision:** 0.991 | **Recall:** 0.284  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|Roelfsen\s+Versicherung|Dorfcon-Verlag|Pastel\s+Pharma|Psomadakis\s+Touristik|Bezirksgericht\s+Neunkirchen|Raiffeisenbank\s+Karnische\s+Rion|Lexkel\s+Vertrieb\s+KG|Luehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH|Finanzamt\s+Judenburg\s+Liezen|Finanzamt\s+Landeck\s+Reutte|Finanzamt\s+Linz|FA\s+Salzburg-Stadt|TraunChemie\s+GMBH|Wien\s+Waldnor\s+KG|UGQQ\s+Verlag\s+OG|Vahrenkamp\s+Luftfahrt|Klusner\s*&\s*P\u00e4ffgen\s+Bildung\s+GMBH|Pastl\+B\u00e4chle\s+Handel|Traun-Digital\s+KG|Gartgart\s+Dienstleistungen\s+GMBH|Kraftver-Gastronomie\s+GMBH|KQPC\s+Versand\s+GMBH|Event\s+Sudkraftlex\s+GMBH|S\u00fcd\s+Lemkel|Chen\s+Setzekorn|Scheibenzuber\s+Textil|Krolitzki\s+Beratung|Milan\s+H\u00e4ndlein|UnterRecycling\s+Services\s+GMBH|Talkel-Versand\s+AG|Hebebrand\s+Recycling\s+AG|FA\s+Gmunden\s+V\u00f6cklabruck|FA\s+Graz-Stadt|Finanzamt\s+Grieskirchen\s+Wels|Annemie\s+Bott)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.991 | 0.284 | 0.442 | 562 | 557 | 5 | 557/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 557 | 5 | 1401 |

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
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten 
Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und 
verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007 
ausschließlich an die Roelfsen Versicherung.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3**

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 4**

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

**Example 5**

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

</details>

<details>
<summary>❌ Missed (2)</summary>

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

- Missed: `Finanzamt Salzburg-Stadt`


```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- FP: `Raiffeisenbank Karnische Rion`


</details>

---

## `finanzamt_organisation`

🔴 Weak rule

> Matches Finanzamt or FA followed by location names, handling complex locations and missing prepositions.

**F1:** 0.425 | **Precision:** 0.987 | **Recall:** 0.271  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Finanzamt|FA)\s+(?:[A-Z][a-zA-Z\s-]+?)(?=\s+(?:vom|am|von|im|auf|bei|in|zu|\d{1,2}\.\d{1,2}|\d{4})\b|\s*$|\s+vom|\s+am|\s+von|\s+im|\s+auf|\s+bei|\s+in|\s+zu|\s+\d{1,2}\.\d{1,2}|\s+\d{4}|\s+\.|\s+\,|\s+\)|\s+\]|\s+\n|\s+\s)`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.987 | 0.271 | 0.425 | 538 | 531 | 7 | 531/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 531 | 7 | 1427 |

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
FA Salzburg-Stadt  ist für das Betreiben der Website, das Einrichten und die laufende Betreuung der 
Teilnehmerkonten, die Vermittlung von Tipps auf den Ausgang von Lotterien an KommR Ing. Roberta Gossling, die 
Organisation und entsprechende Vermittlung von Spielgemeinschaften, die Leistung der 
Einsätze der Teilnehmer an KommR Ing. Roberta Gossling  und die Weiterleitung der von KommR Ing. Roberta Gossling  erhaltenen 
Gewinne an die Teilnehmer gemäß diesen Geschäftsbedingungen verantwortlich.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 4**

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
<summary>❌ Missed (2)</summary>

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

---

## `standalone_legal_form`

🔴 Weak rule

> Matches names with exactly one word before the legal suffix, allowing hyphens.

**F1:** 0.258 | **Precision:** 0.574 | **Recall:** 0.166  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<!Firma\s)(?<!Arbeitgeber\s)\b[A-Z][a-zA-Z0-9-]+(?:\s+[A-Z][a-zA-Z0-9-]+)?\s+(?:GMBH|AG|KG|UG|OG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.574 | 0.166 | 0.258 | 566 | 325 | 241 | 325/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 325 | 241 | 1633 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 2**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

**Example 3**

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 4**

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

**Example 5**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- Missed: `Klusner&Päffgen Bildung GMBH`


```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- Missed: `Nexgartuni Finanzen Planung GMBH`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Bildung GMBH`


```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- FP: `Finanzen Planung GMBH`


</details>

---

## `company_legal_form_suffix`

🔴 Weak rule

> Matches company names ending in legal forms, excluding 'Firma' and 'Arbeitgeber', and allowing hyphens.

**F1:** 0.253 | **Precision:** 0.563 | **Recall:** 0.163  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<!Firma\s)(?<!Arbeitgeber\s)\b[A-Z][a-zA-Z0-9-]+(?:\s+[A-Z][a-zA-Z0-9-]+)*\s+(?:GMBH|AG|KG|GmbH\s*&\s*Co\s*KG|UG|OG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.563 | 0.163 | 0.253 | 567 | 319 | 248 | 319/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 319 | 248 | 1639 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 2**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

**Example 3**

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 4**

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

**Example 5**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

</details>

<details>
<summary>❌ Missed (2)</summary>

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


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Bildung GMBH`


```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

- FP: `Die KQPC Versand GMBH`


</details>

---

## `company_with_hyphen`

🔴 Weak rule

> Matches names with hyphens and legal suffixes.

**F1:** 0.253 | **Precision:** 0.563 | **Recall:** 0.163  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][A-Za-z0-9-]+(?:\s+[A-Z][A-Za-z0-9-]+)*\s+(?:GMBH|AG|KG|GmbH\s*&\s*Co\s*KG|UG|OG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.563 | 0.163 | 0.253 | 567 | 319 | 248 | 319/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 319 | 248 | 1639 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 2**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

**Example 3**

```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 4**

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

**Example 5**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

</details>

<details>
<summary>❌ Missed (2)</summary>

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


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Bildung GMBH`


```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

- FP: `Die KQPC Versand GMBH`


</details>

---

## `organisation_generic`

🔴 Weak rule

> Matches organization names ending in keywords like Beratung, Versicherung, Planung, etc., even without legal suffixes.

**F1:** 0.126 | **Precision:** 0.273 | **Recall:** 0.082  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-zA-Z0-9-]+(?:\s+[A-Z][a-zA-Z0-9-]+)*\s+(?:Beratung|Versicherung|Planung|Dienstleistungen|Vertrieb|Handel|Logistik|Immobilien|Textil|E-Commerce|GmbH|AG|KG|GmbH\s*&\s*Co\s*KG|UG|OG|Bankstelle)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.273 | 0.082 | 0.126 | 586 | 160 | 426 | 160/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 160 | 426 | 1798 |

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
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2**

```
2. Beweiswürdigung 
Der festgestellte Sachverhalt gründet sich auf die Einsichtnahme in die Insolvenzdatei, ins 
Firmenbuch sowie auf das Abgabenkonto der Lexkel Vertrieb KG. 
3. Rechtliche Beurteilung 
3.1.
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 3**

```
Wien Waldnor KG 
Ergebnisänderung                                    - 12.000,--  (nur DI Bf., Eing v. 17.2.2009) 
Einkünfte aus Gewerbebetrieb 2007     -19.683,68 Euro […]“
```

| Prediction | Gold |
|------------|------|
| `Wien Waldnor KG` | `Wien Waldnor KG` |

**Example 4**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 5**

```
Entscheidungsgründe 
I. Verfahrensgang 
Am 4.6.2013 wurde der belangten Behörde der am 25.4.2013 zwischen der UGQQ Verlag OG (Vermieterin) und der Beschwerdeführerin (Mieterin) abgeschlossene Mietvertrag zur 
Anzeige gebracht.
```

| Prediction | Gold |
|------------|------|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

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

- Missed: `Dorfcon-Verlag`


```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- Missed: `Gartgart Dienstleistungen GMBH`

- Missed: `Kraftver-Gastronomie GMBH`


```
Mit einer weiteren FinanzOnline-Eingabe vom 18.9.2020 brachte die Gartgart Dienstleistungen GMBH  unter 
ihrer FinanzOnline-Teilnehmeridentifikation unter der Rubrik „Sonstige Anbringen“ einen 
Vorlageantrag gegen eine an sie selbst gerichtete Beschwerdevorentscheidung vom 9.9.2020 
betreffend eine gegenüber ihr selbst festgesetzte Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO ein.
```

- Missed: `Gartgart Dienstleistungen GMBH`


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


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- FP: `Raiffeisenbank Karnische Rion  Bankstelle`


```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- FP: `Gartgart Dienstleistungen`


```
Mit einer weiteren FinanzOnline-Eingabe vom 18.9.2020 brachte die Gartgart Dienstleistungen GMBH  unter 
ihrer FinanzOnline-Teilnehmeridentifikation unter der Rubrik „Sonstige Anbringen“ einen 
Vorlageantrag gegen eine an sie selbst gerichtete Beschwerdevorentscheidung vom 9.9.2020 
betreffend eine gegenüber ihr selbst festgesetzte Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO ein.
```

- FP: `Gartgart Dienstleistungen`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- FP: `MONDSEE-TREUHAND Wiedlroither GmbH`


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

- FP: `BDO Audit GmbH`


</details>

---

## `organisation_with_special_chars`

🔴 Weak rule

> Matches names containing '&' or '+' between words, handling various spacing.

**F1:** 0.020 | **Precision:** 0.169 | **Recall:** 0.011  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-zA-Z0-9-]+(?:\s+&\s*|\s*\+\s*|\s*&\s*|\s*\+\s*|\s+\+\s+|\s+&\s+)[A-Z][a-zA-Z0-9-]+(?:\s+(?:&|\+)[A-Z][a-zA-Z0-9-]+)*\s+(?:GMBH|AG|KG|GmbH|OG|Beratung|Versicherung|Planung|Dienstleistungen|Vertrieb|Handel|Logistik|Immobilien|Textil|E-Commerce|Bankstelle)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.169 | 0.011 | 0.020 | 124 | 21 | 103 | 21/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 21 | 103 | 1937 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Umsatzsteuerverkürzungen bei der Firma Reinemut + Smoch Handel
```

| Prediction | Gold |
|------------|------|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 2**

```
Es ist weder ersichtlich, dass es sich für die Reinemut + Smoch Handel  um eine Selbstanzeige handeln 
soll, noch wurde für den Beschuldigten als Täter im Sinne des § 29 Abs. 5 FinStrG namentlich 
Selbstanzeige erstattet.
```

| Prediction | Gold |
|------------|------|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vanessa Winken  in der Beschwerdesache I AG & 
atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung, 
Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen 
1. Conuni-Heizung  GmbH & Co KG, Straße3, Ort,  
2. Stadt Dorfkraft  GmbH & Co KG, Straße3, Ort, 
3. Digital Seeal  GmbH & Co KG, Straße3, Ort und 
4.
```

- Missed: `Conuni-Heizung`

- Missed: `Stadt Dorfkraft`

- Missed: `Digital Seeal`


```
3. Okur Automotive  GmbH & Co KG: Insgesamt wurden 311 private Anleger mit einer Einlage im 
Betrag von gesamt € 6.000.000,00 angeworben.
```

- Missed: `Okur Automotive`


```
der atypisch stillen Gesellschafterinnen wie folgt 
zugerechnet: 
1. Kök & Heberlein Bau  GmbH & Co KG: € 0,00, 
2.
```

- Missed: `Kök & Heberlein Bau`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Barbara Schmeynk  in der Beschwerdesache Rut Fritschel, 
Kalmusweg 35, 3041 Grabensee, Österreich, vertreten durch Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG, 
Hadeldorfstraße 30, 6830 Rankweil über die Beschwerde vom 17. November 2016 gegen die 
Bescheide des FA Landeck Reutte (nunmehr Finanzamt Österreich) vom 4. November 2016, 
Steuernummer 42-146/4996, betreffend die Festsetzung des Dienstgeberbeitrages (DB) 
und des Zuschlags zum Dienstgeberbeitrag (DZ) für das Jahr 2015 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Landeck Reutte`


```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- Missed: `Okur Automotive`

- Missed: `Celikkanat Garten`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vanessa Winken  in der Beschwerdesache I AG & 
atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung, 
Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen 
1. Conuni-Heizung  GmbH & Co KG, Straße3, Ort,  
2. Stadt Dorfkraft  GmbH & Co KG, Straße3, Ort, 
3. Digital Seeal  GmbH & Co KG, Straße3, Ort und 
4.
```

- FP: `GmbH & Co KG`

- FP: `GmbH & Co KG`

- FP: `GmbH & Co KG`


```
3. Okur Automotive  GmbH & Co KG: Insgesamt wurden 311 private Anleger mit einer Einlage im 
Betrag von gesamt € 6.000.000,00 angeworben.
```

- FP: `GmbH & Co KG`


```
der atypisch stillen Gesellschafterinnen wie folgt 
zugerechnet: 
1. Kök & Heberlein Bau  GmbH & Co KG: € 0,00, 
2.
```

- FP: `GmbH & Co KG`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Barbara Schmeynk  in der Beschwerdesache Rut Fritschel, 
Kalmusweg 35, 3041 Grabensee, Österreich, vertreten durch Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG, 
Hadeldorfstraße 30, 6830 Rankweil über die Beschwerde vom 17. November 2016 gegen die 
Bescheide des FA Landeck Reutte (nunmehr Finanzamt Österreich) vom 4. November 2016, 
Steuernummer 42-146/4996, betreffend die Festsetzung des Dienstgeberbeitrages (DB) 
und des Zuschlags zum Dienstgeberbeitrag (DZ) für das Jahr 2015 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- FP: `GmbH & Co KG`


```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- FP: `GmbH & Co KG`

- FP: `GmbH & Co KG`


</details>

---

## `bank_kasse_organisation`

🔴 Weak rule

> Matches specific bank and insurance institution names with locations or types.

**F1:** 0.018 | **Precision:** 0.529 | **Recall:** 0.009  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Raiffeisenbank\s+[A-Z][a-zA-Z\s-]+?|Sparkasse\s+[A-Z][a-zA-Z\s-]+?|Volksbank\s+[A-Z][a-zA-Z\s-]+?|Niederösterreichische\s+Vorsorgekasse|Vorsorgekasse|BAWAG\s+(?:P\.S\.K\.\s+)?[A-Za-z\s-]+?|BAWAG\s+P\.S\.K\.\s+Wohnbaubank)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.529 | 0.009 | 0.018 | 34 | 18 | 16 | 18/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 18 | 16 | 1940 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

| Prediction | Gold |
|------------|------|
| `Niederösterreichische Vorsorgekasse` | `Niederösterreichische Vorsorgekasse` |

**Example 2**

```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

| Prediction | Gold |
|------------|------|
| `BAWAG P.S.K. Wohnbaubank` | `BAWAG P.S.K. Wohnbaubank` |
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 3**

```
Darüber hinaus habe die belangte 
Behörde das Konto des Beschwerdeführers vor Weihnachten unrechtmäßig um den Betrag 
vom € 28.423,94 „ausgeplündert“ und zudem auf zwei Konten gleichzeitig zugegriffen, obwohl 
eines dieser Konten zwei Personen gemeinsam gehört und der Zugriff auf das andere Konto 
(bei der Raiffeisenbank Wienerwald) ausgereicht hätte, um die Forderung vollständig zu befriedigen.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 4**

```
Letztlich bemängelt der Beschwerdeführer, dass die belangte Behörde nicht mit 
größtmöglicher Schonung vorgegangen ist, sondern auf mehrere Konten gleichzeitig 
zugegriffen hat, obwohl der Einlagestand des Kontos bei der Raiffeisenbank Wienerwald  ausgereicht hätte, 
um die Abgabenforderung zu befriedigen.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 5**

```
Die Feststellungen im 
Zusammenhang mit dem Kredit bei der Raiffeisenbank Stallhofen  ergeben sich aus deren Schreiben vom 
24.2.2014 und 16.4.2015.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- Missed: `Raiffeisenbank Mittleres Mostviertel`


```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- Missed: `Raiffeisenbank Süd-Weststeiermark`


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


```
Wegen eines Teilbetrages in Höhe von 
€ 10.000,00 wird die dem Bf gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem 
bezeichneten Girokonto zustehende Forderung gepfändet.
```

- Missed: `Raiffeisenbank Wels Süd`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- FP: `Raiffeisenbank Karnische`


```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- FP: `Raiffeisenbank Mittleres`


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- FP: `Raiffeisenbank Karnische`


```
Wegen eines Teilbetrages in Höhe von 
€ 10.000,00 wird die dem Bf gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem 
bezeichneten Girokonto zustehende Forderung gepfändet.
```

- FP: `Raiffeisenbank Wels`


```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

- FP: `Raiffeisenbank Wels`


</details>

---

## `organisation_og`

🔴 Weak rule

> Specifically matches names ending in OG.

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.003  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-zA-Z0-9-]+(?:\s+[A-Z][a-zA-Z0-9-]+)*\s+OG\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.500 | 0.003 | 0.005 | 10 | 5 | 5 | 5/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 5 | 1953 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Entscheidungsgründe 
I. Verfahrensgang 
Am 4.6.2013 wurde der belangten Behörde der am 25.4.2013 zwischen der UGQQ Verlag OG (Vermieterin) und der Beschwerdeführerin (Mieterin) abgeschlossene Mietvertrag zur 
Anzeige gebracht.
```

| Prediction | Gold |
|------------|------|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

**Example 2**

```
II. Das Bundesfinanzgericht hat erwogen 
1. Feststellungen & Beweiswürdigung 
Mit vorliegendem Mietvertrag, unterzeichnet am 25.4.2013, werden von der UGQQ Verlag OG  als Vermieterin Geschäftsräumlichkeiten im Ausmaß von etwa 574 Quadratmeter an 
die Beschwerdeführerin als Mieterin vermietet.
```

| Prediction | Gold |
|------------|------|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

**Example 3**

```
Entscheidungsgründe 
I. Verfahrensgang und Sachverhalt 
Der Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der WOD Sicherheit KG  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt.
```

| Prediction | Gold |
|------------|------|
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |

**Example 4**

```
keine Leistungsbeschreibung enthalte und nicht der Bf als Empfänger aufscheine und eine 
Rechnung der „Mur Alver OG“ Leuchten aus dem Luxussegment anführe.
```

| Prediction | Gold |
|------------|------|
| `Mur Alver OG` | `Mur Alver OG` |

**Example 5**

```
Mit Bescheid vom 5.3.2020 stellte es die gemeinschaftlichen Einkünfte 2018 der Zumholte Verlag OG 
mit 427.541,96 Euro und den auf die Beteiligung an der OG entfallenden Anteil des Bf. an den 
gemeinschaftlichen Einkünften mit 142.172,03 Euro fest.
```

| Prediction | Gold |
|------------|------|
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Entscheidungsgründe 
I. Verfahrensgang und Sachverhalt 
Der Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der WOD Sicherheit KG  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt.
```

- Missed: `WOD Sicherheit KG`


```
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Hugo Biagi  in der Beschwerdesache Ing. RgR Irene Tomischat, 
Sr. Elfriede Ettl-Platz 3Q, 8524 Gamsgebirg, Österreich, vertreten durch Gsaxner + Mair OG Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Meinhardstraße 9/4/4, 6020 Innsbruck, über die Beschwerde 
vom 17. März 2014 bzw. 19. März 2014 gegen die Bescheide des FA Steiermark Mitte  betreffend 
Körperschaftsteuer 2009 bis 2012 (Ausfertigungsdaten 14. Februar 2014 sowie 17. Februar 
2014), betreffend Umsatzsteuer für die Jahre 2009 bis 2013 (Ausfertigungsdaten 14. Februar 
2014, 17. Februar 2014 bzw. 15. Februar 2016) sowie betreffend den Haftungsbescheid für die 
Kapitalertragsteuer für das Jahr 2013 (Ausfertigungsdatum 17. Februar 2014), zu 
Steuernummer 97-017/0451, zu Recht erkannt: 
I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.
```

- Missed: `FA Steiermark Mitte`


```
BESCHLUSS  
Das Bundesfinanzgericht hat durch den Richter ER in der Beschwerdesache Valerie Bastendorf, Josef-Reiter-Straße 22, 8063 Eggersdorf bei Graz, Österreich, vertreten durch Aicher & Partner Steuerberater OG, Schillerplatz 5, 9300 St.Veit/Glan, 
betreffend Beschwerde vom 18. Juli 2018 gegen die Bescheide des Finanzamt Salzburg-Stadt 
(nunmehr Finanzamt Österreich) vom 13. Juni 2018 betreffend Umsatzsteuer 2015, und 2016 
sowie Umsatzsteuer 04.2017-12.2017 und Umsatzsteuer 01.2018-04.2018 Steuernummer 
01-451/8558  beschlossen:  
Die Beschwerde vom 18. Juli 2018 wird als gegenstandslos geworden erklärt.
```

- Missed: `Finanzamt Salzburg-Stadt`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Nikolaus Kristen  in der Beschwerdesache Esmeralda Henzchen, 
Stiblerweg 5, 3925 Schwarzau, Österreich, vertreten durch die Djuric & Oberger Wth OG Steuerberatungsgesellschaft, 
Hietzinger Kai 67/4 über die Beschwerde vom 13. Jänner 2020 gegen den Bescheid des 
ehemaligen Finanzamtes Wien 4/5/10 vom 25. Oktober 2019 betreffend Haftung gemäß §§ 9 
und 80 BAO für Abgabenschuldigkeiten der RheinMetall Technologien GMBH  zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- Missed: `RheinMetall Technologien GMBH`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser 
Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den 
Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von 
Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- Missed: `Bauermeister Getränke`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Hugo Biagi  in der Beschwerdesache Ing. RgR Irene Tomischat, 
Sr. Elfriede Ettl-Platz 3Q, 8524 Gamsgebirg, Österreich, vertreten durch Gsaxner + Mair OG Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Meinhardstraße 9/4/4, 6020 Innsbruck, über die Beschwerde 
vom 17. März 2014 bzw. 19. März 2014 gegen die Bescheide des FA Steiermark Mitte  betreffend 
Körperschaftsteuer 2009 bis 2012 (Ausfertigungsdaten 14. Februar 2014 sowie 17. Februar 
2014), betreffend Umsatzsteuer für die Jahre 2009 bis 2013 (Ausfertigungsdaten 14. Februar 
2014, 17. Februar 2014 bzw. 15. Februar 2016) sowie betreffend den Haftungsbescheid für die 
Kapitalertragsteuer für das Jahr 2013 (Ausfertigungsdatum 17. Februar 2014), zu 
Steuernummer 97-017/0451, zu Recht erkannt: 
I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `Mair OG`


```
BESCHLUSS  
Das Bundesfinanzgericht hat durch den Richter ER in der Beschwerdesache Valerie Bastendorf, Josef-Reiter-Straße 22, 8063 Eggersdorf bei Graz, Österreich, vertreten durch Aicher & Partner Steuerberater OG, Schillerplatz 5, 9300 St.Veit/Glan, 
betreffend Beschwerde vom 18. Juli 2018 gegen die Bescheide des Finanzamt Salzburg-Stadt 
(nunmehr Finanzamt Österreich) vom 13. Juni 2018 betreffend Umsatzsteuer 2015, und 2016 
sowie Umsatzsteuer 04.2017-12.2017 und Umsatzsteuer 01.2018-04.2018 Steuernummer 
01-451/8558  beschlossen:  
Die Beschwerde vom 18. Juli 2018 wird als gegenstandslos geworden erklärt.
```

- FP: `Partner Steuerberater OG`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Nikolaus Kristen  in der Beschwerdesache Esmeralda Henzchen, 
Stiblerweg 5, 3925 Schwarzau, Österreich, vertreten durch die Djuric & Oberger Wth OG Steuerberatungsgesellschaft, 
Hietzinger Kai 67/4 über die Beschwerde vom 13. Jänner 2020 gegen den Bescheid des 
ehemaligen Finanzamtes Wien 4/5/10 vom 25. Oktober 2019 betreffend Haftung gemäß §§ 9 
und 80 BAO für Abgabenschuldigkeiten der RheinMetall Technologien GMBH  zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `Oberger Wth OG`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser 
Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den 
Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von 
Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `Partner Steuerberater OG`


```
Das Bundesfinanzgericht hat durch den Richter Dr. Jaden Riechelmann  in der Beschwerdesache PhD Liliana Bressler, 
C - Ringstraße 42, 9962 Gassen, Österreich, vertreten durch Adelsberger & Thaler Steuerberatungsgesellschaft OG, 
Oberndorferstraße 44, 6322 Kirchbichl über die Beschwerde vom 13. November 2020 gegen 
den Bescheid des FA Bruck Eisenstadt Oberwart (nunmehr Finanzamt Österreich) vom 6. November 2020 
betreffend Einkommensteuer 2013 (Berichtigung gem § 293b BAO zu Bescheid vom 
19.6.2019), Steuernummer 76-767/4831, zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- FP: `Thaler Steuerberatungsgesellschaft OG`


</details>

---

## `umwelt_organisation`

🔴 Weak rule

> umwelt_organisation

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-z]+\s+Umwelt\b|\bUmwelt\s+[A-Z][a-z]+\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 | 3/1958 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 1955 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die Laskowsky Umwelt  seit 15.5.2024 aufgrund 
einer Neufassung des Gesellschaftsvertrages infolge Verkaufs nunmehr PhD Marianne Yener  heißt.
```

| Prediction | Gold |
|------------|------|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

**Example 2**

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

| Prediction | Gold |
|------------|------|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

**Example 3**

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) ist als Rechtsnachfolgerin der 
Annemie Bott  auch partielle Rechtsnachfolgerin der Milan Händlein.
```

| Prediction | Gold |
|------------|------|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

- Missed: `StadtEnergie Holding`


```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) ist als Rechtsnachfolgerin der 
Annemie Bott  auch partielle Rechtsnachfolgerin der Milan Händlein.
```

- Missed: `Annemie Bott`

- Missed: `Milan Händlein`


</details>

---

