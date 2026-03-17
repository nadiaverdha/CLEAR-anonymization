# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-16T13:08:28.049584

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `specific_organisation_names` | 🔴 Weak | 0.445 | 0.991 | 0.287 | 568 |
| `finanzamt_organisation` | 🔴 Weak | 0.301 | 0.849 | 0.183 | 423 |
| `company_with_hyphen` | 🔴 Weak | 0.249 | 0.562 | 0.160 | 559 |
| `standalone_legal_form` | 🔴 Weak | 0.163 | 0.813 | 0.091 | 219 |
| `organisation_generic` | 🔴 Weak | 0.075 | 0.350 | 0.042 | 234 |
| `organisation_with_special_chars` | 🔴 Weak | 0.014 | 0.560 | 0.007 | 25 |
| `company_legal_form_suffix` | 🔴 Weak | 0.009 | 0.196 | 0.005 | 46 |
| `umwelt_organisation` | 🔴 Weak | 0.003 | 1.000 | 0.002 | 3 |
| `organisation_og` | 🔴 Weak | 0.003 | 0.429 | 0.002 | 7 |
| `bank_kasse_organisation` | 🔴 Weak | 0.002 | 0.143 | 0.001 | 14 |

---

## `specific_organisation_names`

🔴 Weak rule

> Matches specific known organisation names. Updated to include missing names from failures and ensure special characters are handled correctly.

**F1:** 0.445 | **Precision:** 0.991 | **Recall:** 0.287  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|Roelfsen\s+Versicherung|Dorfcon-Verlag|Pastel\s+Pharma|Psomadakis\s+Touristik|Bezirksgericht\s+Neunkirchen|Raiffeisenbank\s+Karnische\s+Rion|Lexkel\s+Vertrieb\s+KG|Luehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH|Finanzamt\s+Judenburg\s+Liezen|Finanzamt\s+Landeck\s+Reutte|Finanzamt\s+Linz|FA\s+Salzburg-Stadt|TraunChemie\s+GMBH|Wien\s+Waldnor\s+KG|UGQQ\s+Verlag\s+OG|Vahrenkamp\s+Luftfahrt|Klusner\s*&\s*P\u00e4ffgen\s+Bildung\s+GMBH|Pastl\+B\u00e4chle\s+Handel|Traun-Digital\s+KG|Gartgart\s+Dienstleistungen\s+GMBH|Kraftver-Gastronomie\s+GMBH|KQPC\s+Versand\s+GMBH|Event\s+Sudkraftlex\s+GMBH|S\u00fcd\s+Lemkel|Chen\s+Setzekorn|Scheibenzuber\s+Textil|Krolitzki\s+Beratung|Milan\s+H\u00e4ndlein|UnterRecycling\s+Services\s+GMBH|Talkel-Versand\s+AG|Hebebrand\s+Recycling\s+AG|FA\s+Gmunden\s+V\u00f6cklabruck|FA\s+Graz-Stadt|Finanzamt\s+Grieskirchen\s+Wels|Annemie\s+Bott)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.991 | 0.287 | 0.445 | 568 | 563 | 5 | 563/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 563 | 5 | 1401 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
BESCHLUSS-VERFAHRENSHILFE  
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yussuf Höckenschnieder  über den Antrag auf Gewährung der 
Verfahrenshilfe des Antragstellers Gotthard Sassenburg, Kosakenweg 4, 9602 Unterthörl, Österreich  vom 19.12.2024 für das 
Beschwerdeverfahren betreffend die Beschwerde vom 26. Mai 2023 gegen den Bescheid des 
Finanzamt Linz  vom 27. April 2023 über die Abweisung einer Nachsicht von Abgabenschuldigkeiten 
beschlossen: 
Der Antrag auf Gewährung der Verfahrenshilfe gemäß § 292 BAO wird abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 2**

```
Begründend führte die 
Beschwerdeführerin in der Beschwerde aus, dass die Gewinnermittlung für 2007 auf der Ebene 
der Houdek Maschinenbau  nach allgemeinen Grundsätzen durchzuführen sei, da der 
Vermögensübergang hinsichtlich der 11 Tankstellen auf die Schmeltz Luftfahrt  erst mit Ablauf des 
Spaltungsstichtages (Spaltungsstichtag 31.12.2007) per 1.1.2008 stattgefunden habe.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3**

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

| Prediction | Gold |
|------------|------|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

**Example 4**

```
Die TraunChemie GMBH  haftet gemäß § 9 Abs 7 VStG über die verhängten Geldstrafen und 
Verfahrenskosten sowie für sonstige in Geld bemessene Unrechtsfolgen und zur ungeteilten 
Hand.
```

| Prediction | Gold |
|------------|------|
| `TraunChemie GMBH` | `TraunChemie GMBH` |

**Example 5**

```
Die Tatsache, dass der 
klagenden/widerbeklagten Partei im Scheidungsverfahren Verfahrenshilfe durch Beigebung 
eines Rechtsanwalts gewährt wurde, ergibt sich aus dem vorgelegten Beschluss des 
Bezirksgericht Neunkirchen  vom 05.01.2017 (Verweis auf den Beschluss vom 03.10.2016).
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

</details>

---

## `finanzamt_organisation`

🔴 Weak rule

> Matches 'Finanzamt' or 'FA' followed by location names, including complex multi-word locations. Relaxed to stop at sentence boundaries or common delimiters without requiring specific prepositions immediately after.

**F1:** 0.301 | **Precision:** 0.849 | **Recall:** 0.183  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Finanzamt|FA)\s+(?:[A-Z][a-zA-Z\s-]+?)(?=\s+(?:vom|am|von|im|auf|bei|in|zu|\d{1,2}\.\d{1,2}|\d{4})\b|\s*$|\s+vom|\s+am|\s+von|\s+im|\s+auf|\s+bei|\s+in|\s+zu|\s+\d{1,2}\.\d{1,2}|\s+\d{4}|\s+\.|\s+\,|\s+\)|\s+\]|\s+\n)`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.849 | 0.183 | 0.301 | 423 | 359 | 64 | 359/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 359 | 64 | 1605 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
BESCHLUSS-VERFAHRENSHILFE  
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yussuf Höckenschnieder  über den Antrag auf Gewährung der 
Verfahrenshilfe des Antragstellers Gotthard Sassenburg, Kosakenweg 4, 9602 Unterthörl, Österreich  vom 19.12.2024 für das 
Beschwerdeverfahren betreffend die Beschwerde vom 26. Mai 2023 gegen den Bescheid des 
Finanzamt Linz  vom 27. April 2023 über die Abweisung einer Nachsicht von Abgabenschuldigkeiten 
beschlossen: 
Der Antrag auf Gewährung der Verfahrenshilfe gemäß § 292 BAO wird abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 2**

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

**Example 3**

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
Im Wirtschaftsjahr 2007 ist gemäß der beim FA Grieskirchen Wels  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84 
Tankstellen erzielt worden.
```

- Missed: `FA Grieskirchen Wels`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Im Wirtschaftsjahr 2007 ist gemäß der beim FA Grieskirchen Wels  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84 
Tankstellen erzielt worden.
```

- FP: `FA Grieskirchen Wels  eingereichten`


</details>

---

## `company_with_hyphen`

🔴 Weak rule

> Matches company names containing hyphens followed by legal forms, ensuring the hyphenated part is substantial.

**F1:** 0.249 | **Precision:** 0.562 | **Recall:** 0.160  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][A-Za-z0-9-]+(?:\s+[A-Z][A-Za-z0-9-]+)*\s+(?:GMBH|AG|KG|GmbH\s*&\s*Co\s*KG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.562 | 0.160 | 0.249 | 559 | 314 | 245 | 314/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 314 | 245 | 1650 |

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
<summary>❌ Missed (4)</summary>

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

- Missed: `Luehrig + Hundertmarck Holz GMBH`


```
Die TraunChemie GMBH  haftet gemäß § 9 Abs 7 VStG über die verhängten Geldstrafen und 
Verfahrenskosten sowie für sonstige in Geld bemessene Unrechtsfolgen und zur ungeteilten 
Hand.
```

- Missed: `TraunChemie GMBH`


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
<summary>⚠️ False Positives (4)</summary>

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

- FP: `Hundertmarck Holz GMBH`


```
Die TraunChemie GMBH  haftet gemäß § 9 Abs 7 VStG über die verhängten Geldstrafen und 
Verfahrenskosten sowie für sonstige in Geld bemessene Unrechtsfolgen und zur ungeteilten 
Hand.
```

- FP: `Die TraunChemie GMBH`


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

## `standalone_legal_form`

🔴 Weak rule

> Matches standalone legal forms. Added negative lookbehind to exclude preceding words like 'Firma' or 'Arbeitgeber'.

**F1:** 0.163 | **Precision:** 0.813 | **Recall:** 0.091  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<!Firma\s)(?<!Arbeitgeber\s)\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)\s+(?:GMBH|AG|KG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.813 | 0.091 | 0.163 | 219 | 178 | 41 | 178/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 178 | 41 | 1786 |

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
<summary>❌ Missed (4)</summary>

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

- Missed: `Luehrig + Hundertmarck Holz GMBH`


```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- Missed: `Kraftver-Gastronomie GMBH`


```
Die KQPC Versand GMBH  war Bauherrin und 
Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war 
mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

- Missed: `KQPC Versand GMBH`


```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- Missed: `Nexgartuni Finanzen Planung GMBH`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

- FP: `Hundertmarck Holz GMBH`


```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- FP: `Finanzen Planung GMBH`


</details>

---

## `organisation_generic`

🔴 Weak rule

> Matches organization names that do not have standard legal forms (GmbH, AG, KG) but end in common organizational nouns like Textil, Beratung, Planung, Dienstleistungen, etc. Requires at least two words to avoid false positives.

**F1:** 0.075 | **Precision:** 0.350 | **Recall:** 0.042  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\s+(?:Textil|Beratung|Planung|Dienstleistungen|Vertrieb|Handel|Versicherung|Logistik|Immobilien|GmbH|AG|KG|GmbH\s*&\s*Co\s*KG|OG|UG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.350 | 0.042 | 0.075 | 234 | 82 | 152 | 82/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 82 | 152 | 1882 |

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

**Example 4**

```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

| Prediction | Gold |
|------------|------|
| `Nord Willemtri KG` | `Nord Willemtri KG` |

**Example 5**

```
Im Jahr 2015 erfolgte eine Betriebsprüfung bei der Schoenfelder Textil KG  hinsichtlich Feststellung von 
Einkünften gemäß § 188 BAO betreffend ua. das Jahr 2005.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- Missed: `Nexgartuni Finanzen Planung GMBH`


```
IV. Die Scheibenzuber Textil  haftet gem. § 9 Abs. 7 VStG nicht über die verhängte Geldstrafe, 
sonstige in Geld bemessene Unrechtsfolgen und die Verfahrenskosten zur ungeteilten 
Hand.
```

- Missed: `Scheibenzuber Textil`


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

- Missed: `Verdonlex Automotive GMBH`


</details>

<details>
<summary>⚠️ False Positives (3)</summary>

```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

- FP: `Nexgartuni Finanzen Planung`


```
IV. Die Scheibenzuber Textil  haftet gem. § 9 Abs. 7 VStG nicht über die verhängte Geldstrafe, 
sonstige in Geld bemessene Unrechtsfolgen und die Verfahrenskosten zur ungeteilten 
Hand.
```

- FP: `Die Scheibenzuber Textil`


```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Arbeitgeber Hebebrand Recycling AG`


</details>

---

## `organisation_with_special_chars`

🔴 Weak rule

> Matches company names containing special characters like '+', '&', or '&' which are common in German company names but often missed by standard word boundaries.

**F1:** 0.014 | **Precision:** 0.560 | **Recall:** 0.007  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s*(?:\+|&|\&|\s+\+\s+|\s+&\s+|\s+\&\s+)[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:GMBH|AG|KG|GmbH|OG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.560 | 0.007 | 0.014 | 25 | 14 | 11 | 14/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 14 | 11 | 1950 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Mit Haftungsbescheid vom 6. September 2018 wurde der Bf. als ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der Luehrig + Hundertmarck Holz GMBH  in Höhe von Euro 396.769,30 in 
Anspruch genommen.
```

| Prediction | Gold |
|------------|------|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

**Example 2**

```
Laut den der Abgabenbehörde vorliegenden Lohnzetteln hat der BF neben den 
Aktivbezügen (Blazickova & Hepprich Energie AG  02.05.-31.12.2014 und Berend Energie AG  01.01.-21.02.2014) für den 
Zeitraum vom 01.01.
```

| Prediction | Gold |
|------------|------|
| `Blazickova & Hepprich Energie AG` | `Blazickova & Hepprich Energie AG` |

**Example 3**

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
An die Hudec&Christian Immobilien GMBH (im Folgenden nur „GmbH & Co KG“), an der sich mehrere 
Personen als atypisch stille Gesellschafter beteiligt haben, erging am 14. Jänner 2019 zur GZ 
RV/4100211/2012 eine Erledigung des BFG, deren Spruch zufolge eine Beschwerde der GmbH 
& Co KG gegen die – mit an die GmbH & Co KG gerichteten Bescheiden vorgenommene – 
einheitliche und gesonderte Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2003 
bis 2005 mangels Bescheidqualität der angefochtenen Bescheide als unzulässig 
zurückgewiesen werde (§ 260 Abs 1 lit a BAO).
```

| Prediction | Gold |
|------------|------|
| `Hudec&Christian Immobilien GMBH` | `Hudec&Christian Immobilien GMBH` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Dr.in Frauke Kennedy  über die Beschwerde der Roderich Schleheider 
als Masseverwalterin im Insolvenzverfahren der FWV Luftfahrt GMBH  als Rechtsnachfolgerin der 
Biletzki&Emmert Medien GMBH, Martinkaserne 4, 4906 Prinsach, Österreich, vertreten durch die N&N Steuerberatungsgesellschaft m.b.H., 
Schubertstraße 68, 8010 Graz, vom 21.09.2020 wegen Verletzung der Entscheidungspflicht 
betreffend den Antrag vom 30.01.2018 auf Abrechnung (§ 216 BAO) zu Recht erkannt:  
Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Biletzki&Emmert Medien GMBH` | `Biletzki&Emmert Medien GMBH` |

**Example 5**

```
Begründend wurde dabei ausgeführt, dass die betreffenden Bescheide auf die als 
Feststellungsbescheide für die Jahre 2003 und 2004 gedachten, zur StNr 88-963/0756 
(Hudec&Christian Immobilien GMBH) ergangenen Erledigungen des Finanzamts Klagenfurt (jeweils vom 13. 
November 2009) gestützt gewesen seien.
```

| Prediction | Gold |
|------------|------|
| `Hudec&Christian Immobilien GMBH` | `Hudec&Christian Immobilien GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Laut den der Abgabenbehörde vorliegenden Lohnzetteln hat der BF neben den 
Aktivbezügen (Blazickova & Hepprich Energie AG  02.05.-31.12.2014 und Berend Energie AG  01.01.-21.02.2014) für den 
Zeitraum vom 01.01.
```

- Missed: `Berend Energie AG`


```
Durch die zuletzt sehr turbulente 
Vergangenheit des Geschäftsführers der Gesellschaft Gemke+Gamper Logistik  GmbH war aufgrund von 
Scheidung und Umzug keinesfalls von einer üblichen Geschäftstätigkeit auszugehen.
```

- Missed: `Gemke+Gamper Logistik`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Dr.in Frauke Kennedy  über die Beschwerde der Roderich Schleheider 
als Masseverwalterin im Insolvenzverfahren der FWV Luftfahrt GMBH  als Rechtsnachfolgerin der 
Biletzki&Emmert Medien GMBH, Martinkaserne 4, 4906 Prinsach, Österreich, vertreten durch die N&N Steuerberatungsgesellschaft m.b.H., 
Schubertstraße 68, 8010 Graz, vom 21.09.2020 wegen Verletzung der Entscheidungspflicht 
betreffend den Antrag vom 30.01.2018 auf Abrechnung (§ 216 BAO) zu Recht erkannt:  
Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `FWV Luftfahrt GMBH`


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
Das Finanzamt erließ erklärungsgemäß einen Einkommensteuerbescheid für das Jahr 2014, in 
dem Einkünfte aus nichtselbständiger Arbeit aufgrund folgender Lohnzettel enthalten waren: 
Bezugszeitraum: 1.1.2014 bis 21.02.2014, Bezugsauszahlende Stelle: Berend Energie AG 
Bezugszeitraum: 1.1.2014 bis 31.12.2014, Bezugsauszahlende Stelle: Valida Plus   
Bezugszeitraum: 02.05.2014 bis 31.12.2014, Bezugsauszahlende Stelle: Blazickova & Hepprich Energie AG  
In diesem Kalenderjahr bezog der BF noch in folgenden Zeiträumen Leistungen des 
Arbeitsmarktservice Österreich (AMS): 
22.02.2014 bis 09.06.2014 
10.06.2014 bis 30.06.2014 
01.07.2014 bis 09.09.2014 
1 von 8
Seite 2 von 8
```

- Missed: `Berend Energie AG`


</details>

<details>
<summary>⚠️ False Positives (3)</summary>

```
Durch die zuletzt sehr turbulente 
Vergangenheit des Geschäftsführers der Gesellschaft Gemke+Gamper Logistik  GmbH war aufgrund von 
Scheidung und Umzug keinesfalls von einer üblichen Geschäftstätigkeit auszugehen.
```

- FP: `Gesellschaft Gemke+Gamper Logistik  GmbH`


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

- FP: `Gsaxner + Mair OG`


```
BESCHLUSS  
Das Bundesfinanzgericht hat durch den Richter ER in der Beschwerdesache Valerie Bastendorf, Josef-Reiter-Straße 22, 8063 Eggersdorf bei Graz, Österreich, vertreten durch Aicher & Partner Steuerberater OG, Schillerplatz 5, 9300 St.Veit/Glan, 
betreffend Beschwerde vom 18. Juli 2018 gegen die Bescheide des Finanzamt Salzburg-Stadt 
(nunmehr Finanzamt Österreich) vom 13. Juni 2018 betreffend Umsatzsteuer 2015, und 2016 
sowie Umsatzsteuer 04.2017-12.2017 und Umsatzsteuer 01.2018-04.2018 Steuernummer 
01-451/8558  beschlossen:  
Die Beschwerde vom 18. Juli 2018 wird als gegenstandslos geworden erklärt.
```

- FP: `Aicher & Partner Steuerberater OG`


</details>

---

## `company_legal_form_suffix`

🔴 Weak rule

> Matches German company names ending in GMBH, AG, KG. Added negative lookbehind to exclude preceding words like 'Firma' or 'Arbeitgeber' which were causing incorrect spans.

**F1:** 0.009 | **Precision:** 0.196 | **Recall:** 0.005  

**Format:** `RuleFormat.REGEX`  
**Content:** `(?<!Firma\s)(?<!Arbeitgeber\s)\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){2,}\s+(?:GMBH|AG|KG|GmbH\s*&\s*Co\s*KG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.196 | 0.005 | 0.009 | 46 | 9 | 37 | 9/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 9 | 37 | 1955 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Der Bf. war im Streitjahr 2011 im Zeitraum 1. Jänner bis 7. Mai 2011 bei einem 
österreichischen Arbeitgeber, der Nexgartuni Finanzen Planung GMBH, beschäftigt.
```

| Prediction | Gold |
|------------|------|
| `Nexgartuni Finanzen Planung GMBH` | `Nexgartuni Finanzen Planung GMBH` |

**Example 2**

```
II. Über die Beschwerde wurde erwogen: 
1. Festgestellter Sachverhalt: 
Der Bf war im Streitjahr für die in Wien ansässige Rhein Normonkel Manufaktur GMBH, einem Marktführer im 
institutionellen Hygienebereich, als Außendienstmitarbeiter (Vertreter) nichtselbständig tätig.
```

| Prediction | Gold |
|------------|------|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- Missed: `Talkel-Versand AG`

- Missed: `Hebebrand Recycling AG`


```
Im Beschwerdefall steht fest, dass die Arbeitsstätte der Beschwerdeführerin unterschied-
liche Filialen der Firma Keldonbach Sicherheit GMBH  war.
```

- Missed: `Keldonbach Sicherheit GMBH`


```
Vom 01.01.2009 bis 
31.08.2009 stand sie in einem Dienstverhältnis zur österreichischen Zweigniederlassung der in 
Deutschland ansässigen Firma Keldonbach Sicherheit GMBH (Damenmoden).
```

- Missed: `Keldonbach Sicherheit GMBH`


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
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Arbeitgeber Hebebrand Recycling AG`


```
Im Beschwerdefall steht fest, dass die Arbeitsstätte der Beschwerdeführerin unterschied-
liche Filialen der Firma Keldonbach Sicherheit GMBH  war.
```

- FP: `Firma Keldonbach Sicherheit GMBH`


```
Vom 01.01.2009 bis 
31.08.2009 stand sie in einem Dienstverhältnis zur österreichischen Zweigniederlassung der in 
Deutschland ansässigen Firma Keldonbach Sicherheit GMBH (Damenmoden).
```

- FP: `Firma Keldonbach Sicherheit GMBH`


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

- FP: `Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG`


```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- FP: `Kapitalmarktprospekt Okur Automotive  GmbH & Co KG`


</details>

---

## `umwelt_organisation`

🔴 Weak rule

> Matches organizations containing 'Umwelt' which often appear as a suffix or prefix without a legal form in the text.

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-z]+\s+Umwelt\b|\bUmwelt\s+[A-Z][a-z]+\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 | 3/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 1961 |

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

## `organisation_og`

🔴 Weak rule

> Matches companies ending in OG (Offene Gesellschaft). Requires at least two words before OG to avoid sub-segmentation.

**F1:** 0.003 | **Precision:** 0.429 | **Recall:** 0.002  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)\s+OG\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.429 | 0.002 | 0.003 | 7 | 3 | 4 | 3/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 4 | 1961 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Entscheidungsgründe 
I. Verfahrensgang und Sachverhalt 
Der Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der WOD Sicherheit KG  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt.
```

| Prediction | Gold |
|------------|------|
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |

**Example 2**

```
keine Leistungsbeschreibung enthalte und nicht der Bf als Empfänger aufscheine und eine 
Rechnung der „Mur Alver OG“ Leuchten aus dem Luxussegment anführe.
```

| Prediction | Gold |
|------------|------|
| `Mur Alver OG` | `Mur Alver OG` |

**Example 3**

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


```
Das Bundesfinanzgericht hat durch den Richter Dr. Jaden Riechelmann  in der Beschwerdesache PhD Liliana Bressler, 
C - Ringstraße 42, 9962 Gassen, Österreich, vertreten durch Adelsberger & Thaler Steuerberatungsgesellschaft OG, 
Oberndorferstraße 44, 6322 Kirchbichl über die Beschwerde vom 13. November 2020 gegen 
den Bescheid des FA Bruck Eisenstadt Oberwart (nunmehr Finanzamt Österreich) vom 6. November 2020 
betreffend Einkommensteuer 2013 (Berichtigung gem § 293b BAO zu Bescheid vom 
19.6.2019), Steuernummer 76-767/4831, zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Bruck Eisenstadt Oberwart`


</details>

<details>
<summary>⚠️ False Positives (4)</summary>

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

## `bank_kasse_organisation`

🔴 Weak rule

> Matches banks and insurance funds. Improved to stop at common delimiters or specific keywords like 'Bankstelle' if they appear as separate entities, and to handle names without strict location suffixes.

**F1:** 0.002 | **Precision:** 0.143 | **Recall:** 0.001  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Raiffeisenbank|Sparkasse|Volksbank|Nieder\u00f6sterreichische\s+Vorsorgekasse|Vorsorgekasse|BAWAG)\s+(?:[A-Z][a-zA-Z\s-]+?)(?=\s+(?:Bankstelle|Sitz|mit|in|und|der|die|das|\d{1,2}\.\d{1,2}|\d{4})\b|\s*$|\s+Bankstelle|\s+mit|\s+in|\s+und|\s+der|\s+die|\s+das|\s+\d{1,2}\.\d{1,2}|\s+\d{4}|\s+\.|\s+\,|\s+\)|\s+\]|\s+\n)`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.143 | 0.001 | 0.002 | 14 | 2 | 12 | 2/1964 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 12 | 1962 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
einer vorherigen Kontenregister-Einsicht mit Bescheiden vom 20.12.2022 die dem 
Beschwerdeführer gegenüber der Raiffeisenbank Süd-Weststeiermark, der Raiffeisenbank Wienerwald  und der BAWAG P.S.K. Wohnbaubank 
zustehenden Forderungen aus Kontokorrent oder einem Girokonto, insbesondere aus einem 
jeweils mit IBAN bezeichneten Konto.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- Missed: `Raiffeisenbank Süd-Weststeiermark`

- Missed: `BAWAG P.S.K. Wohnbaubank`

- Missed: `Raiffeisenbank Wienerwald`


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan`


```
Die Feststellungen im 
Zusammenhang mit dem Kredit bei der Raiffeisenbank Stallhofen  ergeben sich aus deren Schreiben vom 
24.2.2014 und 16.4.2015.
```

- Missed: `Raiffeisenbank Stallhofen`


```
Die Mittel Unisyn GMBH  hat mit Wirksamkeit 
vom 22.12.1993 bei der Raiffeisenbank Stallhofen  einen Kredit zur Finanzierung der Geschäftsablöse einer 
Pizzeria im Betrag von ATS 1,200.000,00 aufgenommen.
```

- Missed: `Mittel Unisyn GMBH`

- Missed: `Raiffeisenbank Stallhofen`


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- FP: `Raiffeisenbank Karnische Rion`


```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- FP: `Raiffeisenbank Wienerwald  bezahlt`


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- FP: `Raiffeisenbank Karnische Rion`


```
Die Feststellungen im 
Zusammenhang mit dem Kredit bei der Raiffeisenbank Stallhofen  ergeben sich aus deren Schreiben vom 
24.2.2014 und 16.4.2015.
```

- FP: `Raiffeisenbank Stallhofen  ergeben sich aus`


```
Die Mittel Unisyn GMBH  hat mit Wirksamkeit 
vom 22.12.1993 bei der Raiffeisenbank Stallhofen  einen Kredit zur Finanzierung der Geschäftsablöse einer 
Pizzeria im Betrag von ATS 1,200.000,00 aufgenommen.
```

- FP: `Raiffeisenbank Stallhofen  einen Kredit zur Finanzierung`


</details>

---

