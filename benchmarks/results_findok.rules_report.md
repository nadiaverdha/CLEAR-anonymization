# RuleChef FinDok Benchmark - Rule Analysis- openai/gpt-oss-120b

Generated on: 2026-03-12T12:03:51.912641

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `fa_abbreviation` | 🔴 Weak | 0.335 | 0.942 | 0.203 | 414 |
| `company_legal_suffix` | 🔴 Weak | 0.302 | 0.518 | 0.213 | 789 |
| `finanzamt_full_extended` | 🔴 Weak | 0.270 | 0.750 | 0.164 | 420 |
| `finanzamt_full` | 🔴 Weak | 0.261 | 0.726 | 0.159 | 420 |
| `maschinenbau_org` | 🔴 Weak | 0.072 | 0.911 | 0.038 | 79 |
| `person_like_org` | 🔴 Weak | 0.061 | 0.938 | 0.031 | 64 |
| `versicherung_org` | 🔴 Weak | 0.031 | 0.909 | 0.016 | 33 |
| `bank_raiffeisen` | 🔴 Weak | 0.030 | 1.000 | 0.015 | 29 |
| `gericht_org` | 🔴 Weak | 0.023 | 1.000 | 0.011 | 22 |
| `luftfahrt_org` | 🔴 Weak | 0.019 | 0.900 | 0.009 | 20 |
| `verlag_org` | 🔴 Weak | 0.007 | 1.000 | 0.004 | 7 |
| `vahrenkamp_luftfahrt` | 🔴 Weak | 0.007 | 1.000 | 0.004 | 7 |
| `starker_beratung` | 🔴 Weak | 0.005 | 1.000 | 0.003 | 5 |
| `bank_bawag` | 🔴 Weak | 0.003 | 1.000 | 0.002 | 3 |

---

## `fa_abbreviation`

🔴 Weak rule

> Matches the abbreviation "FA" followed by a location and optionally a case number (e.g., "FA Wien 2/20/21/22").

**F1:** 0.335 | **Precision:** 0.942 | **Recall:** 0.203  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bFA\s+(?:[A-ZÄÖÜ][\wÄÖÜäöüß&\-\.]*)(?:[\s\-][A-ZÄÖÜ][\wÄÖÜäöüß&\-\.]*)*(?:\s+\d+\/\d+(?:\/\d+)?)?\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.942 | 0.203 | 0.335 | 414 | 390 | 24 | 390/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 390 | 24 | 1527 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

**Example 2**

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

**Example 3**

```
Bei Teilnahme erteilt der Spielteilnehmer FA Grieskirchen Wels  den Auftrag, für ihn bei 
9 von 27
Seite 10 von 27
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 4**

```
Damit erweist sich die 
Begründung des FA Grieskirchen Wels  auf Seite 13 Absatz 2 als unzutreffend bzw steht diese im 
Widerspruch zur Entscheidung des VwGH.
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 5**

```
Im Wirtschaftsjahr 2007 ist gemäß der beim FA Grieskirchen Wels  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84 
Tankstellen erzielt worden.
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Niederösterreich Mitte`


```
Begründung 
Mit Bescheid des FA Wien 2/20/21/22  vom 9. April 2015 wurde der Antrag vom 26. März 2015 auf 
Rückzahlung eines Guthabens in Höhe von 628,25 € abgewiesen, da geleistete AGH-Zahlungen 
gem. § 82a Abs. 4 EStG als Drittleistungen gelten und mit der ältesten Abgabenschuld 
aufgerechnet werden.
```

- Missed: `FA Wien 2/20/21/22`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Begründung 
Mit Bescheid des FA Wien 2/20/21/22  vom 9. April 2015 wurde der Antrag vom 26. März 2015 auf 
Rückzahlung eines Guthabens in Höhe von 628,25 € abgewiesen, da geleistete AGH-Zahlungen 
gem. § 82a Abs. 4 EStG als Drittleistungen gelten und mit der ältesten Abgabenschuld 
aufgerechnet werden.
```

- FP: `FA Wien 2/20/21`


</details>

---

## `company_legal_suffix`

🔴 Weak rule

> Matches organisation names ending with a legal suffix (GmbH/GMBH, AG, KG, OG) while excluding generic preceding nouns. Updated to recognise uppercase "GMBH" and the optional "& Co" construct.

**F1:** 0.302 | **Precision:** 0.518 | **Recall:** 0.213  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?!Arbeitgeber\b|Firma\b|Unternehmen\b|Gesellschaft\b)(?:[A-ZÄÖÜ][\w&\+\-\u2011']*(?:[-&][\w&\+\-\u2011']*)*)(?:\s+(?:[A-ZÄÖÜ][\w&\+\-\u2011']*(?:[-&][\w&\+\-\u2011']*)*))*\s+(?: (?:GmbH|GMBH)\s*&\s*Co\.?\s*(?:KG|KGaA)?|(?:GmbH|GMBH)|AG|KG|OG)\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.518 | 0.213 | 0.302 | 789 | 409 | 380 | 409/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 409 | 380 | 1508 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

**Example 2**

```
Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch 
einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH 
hinsichtlich der oa.
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3**

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

| Prediction | Gold |
|------------|------|
| `Talkel-Versand AG` | `Talkel-Versand AG` |
| `Hebebrand Recycling AG` | `Hebebrand Recycling AG` |

**Example 4**

```
Das von der Tochter der Bf in den Monaten März bis Mai 2022 absolvierte Praktikum in den 
Kliniken „Logseemon-Metall AG“, Bildungszentrum für Gesundheitsberufe war - für sich alleine 
betrachtet - zweifellos nicht in Form einer schulischen oder kursmäßigen Ausbildung 
organisiert.
```

| Prediction | Gold |
|------------|------|
| `Logseemon-Metall AG` | `Logseemon-Metall AG` |

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
<summary>❌ Missed (2)</summary>

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


```
Seitens der [Bf.] wurden UID- und HFU-Abfragen durchgeführt und der Reisepass von Herrn PM 
kopiert , von Herrn S liegen keine Dokumente vor, auch war niemand mit diesem Namen im 
Zeitraum der Geschäftsbeziehungen zur Chen Setzekorn  bei der A-Bau GMBH angestellt.
```

- Missed: `Chen Setzekorn`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

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

- FP: `C 
GmbH`


```
Seitens der [Bf.] wurden UID- und HFU-Abfragen durchgeführt und der Reisepass von Herrn PM 
kopiert , von Herrn S liegen keine Dokumente vor, auch war niemand mit diesem Namen im 
Zeitraum der Geschäftsbeziehungen zur Chen Setzekorn  bei der A-Bau GMBH angestellt.
```

- FP: `A-Bau GMBH`


</details>

---

## `finanzamt_full_extended`

🔴 Weak rule

> Matches "Finanzamt" followed by a location and optionally a case number like "8/16/17".

**F1:** 0.270 | **Precision:** 0.750 | **Recall:** 0.164  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bFinanzamt\s+(?:[A-ZÄÖÜ][\w&\-\.\u00df]*)(?:[\s\-][A-ZÄÖÜ][\w&\-\.\u00df]*)*(?:\s+\d+\/\d+\/\d+)?\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.750 | 0.164 | 0.270 | 420 | 315 | 105 | 315/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 315 | 105 | 1602 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

| Prediction | Gold |
|------------|------|
| `Finanzamt Oststeiermark` | `Finanzamt Oststeiermark` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Niederösterreich Mitte` | `Finanzamt Niederösterreich Mitte` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ingeborg Nicklass  in der Beschwerdesache  
Li Demmelmeir, Oberlängenfeld 11, 2164 Alt-Prerau, Österreich, vertreten durch Michael Haberl, Hauptstraße 65, 8962 Gröbming,  
über die Beschwerde vom 16. Mai 2022 gegen den Bescheid des Finanzamt Judenburg Liezen  vom 28. Februar 
2022 betreffend Wiedereinsetzung der Frist zur Einbringung von Beschwerden gegen die 
Umsatzsteuer- und Körperschaftsteuerbescheide 2012 -2016 sowie die Bescheide betreffend 
Anspruchszinsen 2013 - 2016 gem. § 308 BAO zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Kröner  in der Beschwerdesache Prof.in HR StR Marlies Hyna, MSc, 
Mitterbrunnwald 43, 5342 Sankt Gilgen, Österreich, vertreten durch Mag. Theresia-Anna Koller, Friedrich-Schmidt-Platz 7/3, 1080 
Wien, über die Beschwerde vom 2. Oktober 2023 gegen den Bescheid des Finanzamt Steiermark Mitte  vom 31. 
August 2023 betreffend die Abweisung eines Aussetzungsantrages zur Steuernummer 
29-523/5865  zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Example 5**

```
Querweg 40, 4048 Oberpuchenau, Österreich, vertreten durch Schrettl Herbert & Partner 
Steuerberatungsgesellschaft m.b.H., über die Beschwerde vom 20. März 2019 gegen die 
Bescheide des Finanzamt Wien 8/16/17  vom 9. Jänner 2019 betreffend Einkommensteuer 2015 und 2016 zu 
Recht erkannt:  
 
I. Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Graz-Stadt`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Adelheid Eppl  in der Beschwerdesache der 
Depp Versand  und Miteigentümer vertreten durch Rechtsanwälte R, über die Beschwerde vom 
20.2.2020 gegen den Grundsteuermessbescheid zum 1.1.2018 – Fortschreibungsveranlagung 
gemäß § 21 GrStG 1955 des Finanzamt Niederösterreich Mitte  vom 26. Jänner 2020 zu Einheitswertaktenzeichen E zu 
Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `Depp Versand`


</details>

---

## `finanzamt_full`

🔴 Weak rule

> Matches full "Finanzamt" mentions followed by one or more location words (including hyphens, periods, ampersands, etc.).

**F1:** 0.261 | **Precision:** 0.726 | **Recall:** 0.159  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bFinanzamt\s+(?:[A-ZÄÖÜ][\wÄÖÜäöüß&\-\.]*)(?:[\s\-][A-ZÄÖÜ][\wÄÖÜäöüß&\-\.]*)*\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.726 | 0.159 | 0.261 | 420 | 305 | 115 | 305/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 305 | 115 | 1612 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

| Prediction | Gold |
|------------|------|
| `Finanzamt Oststeiermark` | `Finanzamt Oststeiermark` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Niederösterreich Mitte` | `Finanzamt Niederösterreich Mitte` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ingeborg Nicklass  in der Beschwerdesache  
Li Demmelmeir, Oberlängenfeld 11, 2164 Alt-Prerau, Österreich, vertreten durch Michael Haberl, Hauptstraße 65, 8962 Gröbming,  
über die Beschwerde vom 16. Mai 2022 gegen den Bescheid des Finanzamt Judenburg Liezen  vom 28. Februar 
2022 betreffend Wiedereinsetzung der Frist zur Einbringung von Beschwerden gegen die 
Umsatzsteuer- und Körperschaftsteuerbescheide 2012 -2016 sowie die Bescheide betreffend 
Anspruchszinsen 2013 - 2016 gem. § 308 BAO zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Kröner  in der Beschwerdesache Prof.in HR StR Marlies Hyna, MSc, 
Mitterbrunnwald 43, 5342 Sankt Gilgen, Österreich, vertreten durch Mag. Theresia-Anna Koller, Friedrich-Schmidt-Platz 7/3, 1080 
Wien, über die Beschwerde vom 2. Oktober 2023 gegen den Bescheid des Finanzamt Steiermark Mitte  vom 31. 
August 2023 betreffend die Abweisung eines Aussetzungsantrages zur Steuernummer 
29-523/5865  zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Example 5**

```
Die Säumnisbeschwerden waren daher schon deshalb zurückzuweisen, da am 8. Februar 2021 
das Finanzamt Innsbruck  nicht mehr existierte und somit keine Säumnis dieses Finanzamtes vorliegen 
konnte (ebenso BFG vom 1.2.2021, RS/5100003/2021).
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Innsbruck` | `Finanzamt Innsbruck` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `FA Graz-Stadt`


```
Querweg 40, 4048 Oberpuchenau, Österreich, vertreten durch Schrettl Herbert & Partner 
Steuerberatungsgesellschaft m.b.H., über die Beschwerde vom 20. März 2019 gegen die 
Bescheide des Finanzamt Wien 8/16/17  vom 9. Jänner 2019 betreffend Einkommensteuer 2015 und 2016 zu 
Recht erkannt:  
 
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `Finanzamt Wien 8/16/17`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Adelheid Eppl  in der Beschwerdesache der 
Depp Versand  und Miteigentümer vertreten durch Rechtsanwälte R, über die Beschwerde vom 
20.2.2020 gegen den Grundsteuermessbescheid zum 1.1.2018 – Fortschreibungsveranlagung 
gemäß § 21 GrStG 1955 des Finanzamt Niederösterreich Mitte  vom 26. Jänner 2020 zu Einheitswertaktenzeichen E zu 
Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `Depp Versand`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Querweg 40, 4048 Oberpuchenau, Österreich, vertreten durch Schrettl Herbert & Partner 
Steuerberatungsgesellschaft m.b.H., über die Beschwerde vom 20. März 2019 gegen die 
Bescheide des Finanzamt Wien 8/16/17  vom 9. Jänner 2019 betreffend Einkommensteuer 2015 und 2016 zu 
Recht erkannt:  
 
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `Finanzamt Wien`


</details>

---

## `maschinenbau_org`

🔴 Weak rule

> Matches organisations ending with "Maschinenbau" (e.g., Houdek Maschinenbau).

**F1:** 0.072 | **Precision:** 0.911 | **Recall:** 0.038  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-ZÄÖÜ][\w\.‑&-]*\s+Maschinenbau\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.911 | 0.038 | 0.072 | 79 | 72 | 7 | 72/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 72 | 7 | 1845 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2**

```
95-002/7970, BV 24: 
Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3**

```
Auf Grundlage dieser bestehenden Vereinbarungen hat die 
YXTG Maschinenbau  das Recht (und sobald die Stadtwerke X ihrerseits die Lieferung der erzeugten 
Energie nach Maßgabe des bestehenden Rahmenvertrages an sie verlangt, auch die Pflicht), die 
aus dem Wasserkraftwerk erzeugte, in das öffentliche Netz eingespeiste elektrische Energie an 
die Stadtwerke X gegen Bezahlung der vereinbarten Vergütung zu liefern.
```

| Prediction | Gold |
|------------|------|
| `YXTG Maschinenbau` | `YXTG Maschinenbau` |

**Example 4**

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende 
Umgründungsschritte bei Houdek Maschinenbau  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des 
Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung 
und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI 
UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln 
benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5**

```
Begründend führte das Finanzamt zusammenfassend aus, 
dass die Houdek Maschinenbau  aufgrund der Rechtsform eine nach unternehmensrechtlichen 
Vorschriften zur Rechnungslegung verpflichtete Körperschaft im Sinne des § 7 Abs. 3 KStG 1988 
3 von 39
Seite 4 von 39
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Rechtsansicht 
des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten 
innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei 
der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen 
Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen 
Verlusten) bei der Roelfsen Versicherung  führt.
```

- Missed: `Roelfsen Versicherung`


```
Weiters haben Sie als handelsrechtlicher Geschäftsführer der Bludszat Maschinenbau GMBH  von 31.12.2019 bis 
30.4.2020 vor der Liegenschaft in 1220 Wien, Josef-Witternigg-Straße 66, 9121 Tainach, Österreich  den öffentlichen Gemeindegrund, 
der dem öffentlichen Verkehr dient, durch ein Gerüst im Ausmaß von 27 m2 genutzt, wobei Sie 
hiefür bis zum 14.4.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet haben.
```

- Missed: `Bludszat Maschinenbau GMBH`


```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende 
Umgründungsschritte bei Houdek Maschinenbau  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des 
Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung 
und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI 
UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln 
benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

- Missed: `Schmeltz Luftfahrt`


```
Die Dorfcon-Verlag  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle) 
Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

- Missed: `Dorfcon-Verlag`

- Missed: `Schmeltz Luftfahrt`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die VorsitzendeRi_1, die beisitzende Richterin Ri_2 und die 
fachkundigen Laienrichter Ri_3 und Ri_4 in der Beschwerdesache der YXTG Maschinenbau, Weghofstraße 33, 8113 Eisbach, Österreich, vertreten durch ECA Innsbruck Steuerberatung GmbH & Co KG, Rennweg 25, 6020 
Innsbruck, über die Beschwerde vom 27. November 2022 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr 
vom 28. Oktober 2022 betreffend Wiederaufnahme des Verfahrens hinsichtlich 
Körperschaftsteuer für die Jahre 2018, 2019 und 2020 sowie Körperschaftsteuer für die Jahre 
2018, 2019 und 2020 zu Steuernummer 81-052/6903  in der mündlichen Verhandlung am 
22. Mai 2024 in Anwesenheit der Schriftführerin S zu Recht erkannt:  
I. Die Beschwerde gegen die Wiederaufnahme der Verfahren hinsichtlich 
Körperschaftsteuer für die Jahre 2018, 2019 und 2020 wird abgewiesen.
```

- Missed: `Finanzamt Kirchdorf Perg Steyr`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Weiters haben Sie als handelsrechtlicher Geschäftsführer der Bludszat Maschinenbau GMBH  von 31.12.2019 bis 
30.4.2020 vor der Liegenschaft in 1220 Wien, Josef-Witternigg-Straße 66, 9121 Tainach, Österreich  den öffentlichen Gemeindegrund, 
der dem öffentlichen Verkehr dient, durch ein Gerüst im Ausmaß von 27 m2 genutzt, wobei Sie 
hiefür bis zum 14.4.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet haben.
```

- FP: `Bludszat Maschinenbau`


</details>

---

## `person_like_org`

🔴 Weak rule

> Matches personal‑style organisation names without suffixes (e.g., Milan Händlein, Chen Setzekorn).

**F1:** 0.061 | **Precision:** 0.938 | **Recall:** 0.031  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b(?:Milan|Chen)\s+[A-ZÄÖÜ][\w\-\u00df]*\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.938 | 0.031 | 0.061 | 64 | 60 | 4 | 60/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 60 | 4 | 1857 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Da das BFG eindeutig der Beschwerde 
stattgegeben hat und das freie Wahlrecht bejaht hat, wurde damit durch das BFG in bindender 
Weise festgestellt, dass der Gesamtverlust von EUR 3.632.188,29 ausschließlich durch bei der 
Milan Händlein  verbleibende Tankstellen und geschlossene Tankstellen entstanden ist und 
deshalb in den Nachfolgejahren auch nur bei dieser Gesellschaft (bzw. bei deren 
Nachfolgegesellschaft) vortragsfähig ist.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 2**

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

**Example 3**

```
Seitens der [Bf.] wurden UID- und HFU-Abfragen durchgeführt und der Reisepass von Herrn PM 
kopiert , von Herrn S liegen keine Dokumente vor, auch war niemand mit diesem Namen im 
Zeitraum der Geschäftsbeziehungen zur Chen Setzekorn  bei der A-Bau GMBH angestellt.
```

| Prediction | Gold |
|------------|------|
| `Chen Setzekorn` | `Chen Setzekorn` |

**Example 4**

```
Die Krolitzki Beratung  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Manfredo Herrschmann (partielle) 
Gesamtrechtsnachfolgerin der Milan Händlein.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 5**

```
Bei den aus der Milan Händlein 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Annemie Bott  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Annemie Bott).
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Die Krolitzki Beratung  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Manfredo Herrschmann (partielle) 
Gesamtrechtsnachfolgerin der Milan Händlein.
```

- Missed: `Krolitzki Beratung`

- Missed: `Manfredo Herrschmann`


```
Bei den aus der Milan Händlein 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Annemie Bott  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Annemie Bott).
```

- Missed: `Annemie Bott`

- Missed: `Annemie Bott`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Chen Simony  in der Beschwerdesache des 
Mathias Schwörer, Bommern 17, 9831 Laas, Österreich, über die Beschwerde vom 22. September 2014 gegen den 
Bescheid des Finanzamt Purkersdorf  vom 17. September 2014 betreffend Normverbrauchsabgabe 09.2014 
zu Steuernummer 22-797/3077  zu Recht erkannt:  
I. Der Beschwerde wird Folge gegeben.
```

- Missed: `Finanzamt Purkersdorf`


```
BESCHLUSS 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Chen Hunkemöller  in der Beschwerdesache des 
Leander Hanschur, BEd, Rupertiweg 3, 9632 Wassertheurerberg, Österreich, vertreten durch X-Steuerberatung betreffend Beschwerde vom 
20. März 2020 gegen die zur Steuernummer 60-849/8612  ergangenen Bescheide des 
FA Bruck Eisenstadt Oberwart (nunmehr Dienststelle des Finanzamtes Österreich) vom 17. Februar 2020 
betreffend Umsatz- und Einkommensteuer 2012 und 2013 beschlossen: 
Die angefochtenen Bescheide vom 17. Februar 2020 betreffend Umsatz- und 
Einkommensteuer 2012 und 2013 werden gemäß § 278 Abs. 1 BAO aufgehoben und das 
Verfahren an die Abgabenbehörde zurückverwiesen.
```

- Missed: `FA Bruck Eisenstadt Oberwart`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Chen Simony  in der Beschwerdesache des 
Mathias Schwörer, Bommern 17, 9831 Laas, Österreich, über die Beschwerde vom 22. September 2014 gegen den 
Bescheid des Finanzamt Purkersdorf  vom 17. September 2014 betreffend Normverbrauchsabgabe 09.2014 
zu Steuernummer 22-797/3077  zu Recht erkannt:  
I. Der Beschwerde wird Folge gegeben.
```

- FP: `Chen Simony`


```
BESCHLUSS 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Chen Hunkemöller  in der Beschwerdesache des 
Leander Hanschur, BEd, Rupertiweg 3, 9632 Wassertheurerberg, Österreich, vertreten durch X-Steuerberatung betreffend Beschwerde vom 
20. März 2020 gegen die zur Steuernummer 60-849/8612  ergangenen Bescheide des 
FA Bruck Eisenstadt Oberwart (nunmehr Dienststelle des Finanzamtes Österreich) vom 17. Februar 2020 
betreffend Umsatz- und Einkommensteuer 2012 und 2013 beschlossen: 
Die angefochtenen Bescheide vom 17. Februar 2020 betreffend Umsatz- und 
Einkommensteuer 2012 und 2013 werden gemäß § 278 Abs. 1 BAO aufgehoben und das 
Verfahren an die Abgabenbehörde zurückverwiesen.
```

- FP: `Chen Hunkemöller`


</details>

---

## `versicherung_org`

🔴 Weak rule

> Matches organisations ending with "Versicherung" (e.g., Roelfsen Versicherung).

**F1:** 0.031 | **Precision:** 0.909 | **Recall:** 0.016  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-ZÄÖÜ][\w\.‑&-]*\s+Versicherung\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.909 | 0.016 | 0.031 | 33 | 30 | 3 | 30/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 30 | 3 | 1887 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

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

**Example 2**

```
Kff. Sandra Khartchenko (FN ***) ist die Rechtsnachfolgerin der Roelfsen Versicherung.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3**

```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT 
und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4**

```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 5**

```
Ergebnis 
Roelfsen Versicherung 
-2.966.376,17      
Gegen den Körperschaftsteuerbescheid 2007 wurde von der mitbeteiligten Partei 
Roelfsen Versicherung (als partieller Gesamtrechtsnachfolger der Houdek Maschinenbau) mit Schreiben vom 
31.05.2013 Beschwerde erhoben.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Rechtsansicht 
des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten 
innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei 
der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen 
Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen 
Verlusten) bei der Roelfsen Versicherung  führt.
```

- Missed: `Houdek Maschinenbau`


```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT 
und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `FA Wien 1/23`

- Missed: `Lexdon IT`

- Missed: `Dorfcon-Verlag`

- Missed: `Houdek Maschinenbau`


```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

- Missed: `Houdek Maschinenbau`


```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- Missed: `Süd Nortri`

- Missed: `Hülsebusch + Breithaupt Versicherung`


```
Ergebnis 
Roelfsen Versicherung 
-2.966.376,17      
Gegen den Körperschaftsteuerbescheid 2007 wurde von der mitbeteiligten Partei 
Roelfsen Versicherung (als partieller Gesamtrechtsnachfolger der Houdek Maschinenbau) mit Schreiben vom 
31.05.2013 Beschwerde erhoben.
```

- Missed: `Houdek Maschinenbau`


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- FP: `Breithaupt Versicherung`


</details>

---

## `bank_raiffeisen`

🔴 Weak rule

> Matches Raiffeisenbank names (e.g., Raiffeisenbank Süd-Weststeiermark, Raiffeisenbank Wienerwald).

**F1:** 0.030 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bRaiffeisenbank\s+[A-ZÄÖÜ][\w\.‑&-]*\b(?:\s+[A-ZÄÖÜ][\w\.‑&-]*)*\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.015 | 0.030 | 29 | 29 | 0 | 29/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 29 | 0 | 1888 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Süd-Weststeiermark` | `Raiffeisenbank Süd-Weststeiermark` |
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 2**

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

**Example 3**

```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4**

```
Wegen eines Teilbetrages in Höhe von 
€ 10.000,00 wird die dem Bf gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem 
bezeichneten Girokonto zustehende Forderung gepfändet.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wels Süd` | `Raiffeisenbank Wels Süd` |

**Example 5**

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wels Süd` | `Raiffeisenbank Wels Süd` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- Missed: `BAWAG P.S.K. Wohnbaubank`


```
Die Mittel Unisyn GMBH  hat mit Wirksamkeit 
vom 22.12.1993 bei der Raiffeisenbank Stallhofen  einen Kredit zur Finanzierung der Geschäftsablöse einer 
Pizzeria im Betrag von ATS 1,200.000,00 aufgenommen.
```

- Missed: `Mittel Unisyn GMBH`


```
einer vorherigen Kontenregister-Einsicht mit Bescheiden vom 20.12.2022 die dem 
Beschwerdeführer gegenüber der Raiffeisenbank Süd-Weststeiermark, der Raiffeisenbank Wienerwald  und der BAWAG P.S.K. Wohnbaubank 
zustehenden Forderungen aus Kontokorrent oder einem Girokonto, insbesondere aus einem 
jeweils mit IBAN bezeichneten Konto.
```

- Missed: `BAWAG P.S.K. Wohnbaubank`


</details>

---

## `gericht_org`

🔴 Weak rule

> Matches court names like "Bezirksgericht Silz".

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bBezirksgericht\s+Silz\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.011 | 0.023 | 22 | 22 | 0 | 22/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 22 | 0 | 1895 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Beiliegend wurde erneut der Beschluss des BG Bezirksgericht Silz  vom 03.02.2023 sowie ein 
Kontoauszug betreffend die Unterhaltszahlungen im Jahr 2022 übermittelt.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 2**

```
2. Beweiswürdigung 
Die Feststellungen betreffend die Höhe sowie Art des geleisteten Unterhalts (laufender 
Unterhalt, Naturalunterhalt, Unterhaltsvorschuss) ergeben sich aus dem Beschluss des BG 
Bezirksgericht Silz  vom 03.02.2023 bzw. soweit der Naturalunterhalt und der Unterhaltsvorschuss 
betroffen sind, auch aus dem Beschluss des LG für ZRS Wien vom 02.05.2023.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 3**

```
Beiliegend wurde außerdem ein Beschluss des Bezirksgerichtes Bezirksgericht Silz  vom 03.02.2023 
übermittelt.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 4**

```
Mit Eingabe vom 24.04.2023 wurde seitens des Beschwerdeführers im Wesentlichen 
ausgeführt, dass im fraglichen Beschluss des BG Bezirksgericht Silz  kein Unterhaltsanspruch von 
EUR 320,00 festgestellt worden sei.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 5**

```
des BG Bezirksgericht Silz  vom 03.02.2023, ersichtlich ist, liegt der im Zeitraum Juni 2017 bis 
Dezember 2018 (noch ohne Berücksichtigung der Einmalzahlung iHv EUR 8.000,00 als 
Vorschuss auf die laufenden Unterhaltszahlungen) tatsächlich geleistete Unterhalt deutlich 
über dem Unterhaltsbedarf.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

</details>

---

## `luftfahrt_org`

🔴 Weak rule

> Matches organisations ending with the word "Luftfahrt" (e.g., Vahrenkamp Luftfahrt, Schmeltz Luftfahrt).

**F1:** 0.019 | **Precision:** 0.900 | **Recall:** 0.009  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-ZÄÖÜ][\w\.‑&-]*\s+Luftfahrt\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.900 | 0.009 | 0.019 | 20 | 18 | 2 | 18/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 18 | 2 | 1899 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
2019 langte beim FA auf dem Postweg der nachfolgende Schriftsatz ein: 
„XY Steuerberater  
Mag. Dr. X.Y.  
Wirtschaftstreuhand- 
gesellschaft m.b.H.  
Steuerberater  
Zertifizierter Mediator       Wien, 2019-12-03 
Betreff: Vahrenkamp Luftfahrt, 9999 Wien B-Straße 4/7 
 Beschwerde gegen den Bescheid - Leistungsgebot 
Meine Beschwerde richtet sich gegen den Bescheid-Leistungsgebot an Frau Vahrenkamp Luftfahrt  vom 
5.11.2019, zugestellt am 13.11.2019 (siehe Anhang) mit dem Antrag auf Aufhebung dieses 
Bescheides.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 2**

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Mag.a Paulina Hanskötter  in der Beschwerdesache der 
Schickli Luftfahrt  i.L., Friesenplatz 103, 5142 Oberhaslach, Österreich  vertreten durch Rechtsanwalt-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999 (M.-GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle des 
Finanzamt Landeck Reutte) vom 5. November 2019 betreffend Heranziehung als Gemeinschuldnerin für 
„Umsatzsteuerveranlagungen und div.
```

| Prediction | Gold |
|------------|------|
| `Schickli Luftfahrt` | `Schickli Luftfahrt` |

**Example 4**

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende 
Umgründungsschritte bei Houdek Maschinenbau  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des 
Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung 
und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI 
UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln 
benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 5**

```
Die Dorfcon-Verlag  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle) 
Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

- Missed: `Dorfcon-Verlag`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Mag.a Paulina Hanskötter  in der Beschwerdesache der 
Schickli Luftfahrt  i.L., Friesenplatz 103, 5142 Oberhaslach, Österreich  vertreten durch Rechtsanwalt-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999 (M.-GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle des 
Finanzamt Landeck Reutte) vom 5. November 2019 betreffend Heranziehung als Gemeinschuldnerin für 
„Umsatzsteuerveranlagungen und div.
```

- Missed: `Finanzamt Landeck Reutte`


```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende 
Umgründungsschritte bei Houdek Maschinenbau  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des 
Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung 
und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI 
UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln 
benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

- Missed: `Houdek Maschinenbau`

- Missed: `Houdek Maschinenbau`


```
Die Dorfcon-Verlag  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle) 
Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

- Missed: `Dorfcon-Verlag`

- Missed: `Houdek Maschinenbau`


```
Abgespaltene 
Tankstellen 
Schmeltz Luftfahrt
**  
Geschlossene 
Tankstellen 
Houdek Maschinenbau
** 
Verkaufte 
Tankstellen 
Houdek Maschinenbau
** 
Verbleibende 
Tankstellen 
Houdek Maschinenbau
** 
Verbleibende 
Tankstellen 
Houdek Maschinenbau
**
```

- Missed: `Houdek Maschinenbau`

- Missed: `Houdek Maschinenbau`

- Missed: `Houdek Maschinenbau`

- Missed: `Houdek Maschinenbau`


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Dr.in Frauke Kennedy  über die Beschwerde der Roderich Schleheider 
als Masseverwalterin im Insolvenzverfahren der FWV Luftfahrt GMBH  als Rechtsnachfolgerin der 
Biletzki&Emmert Medien GMBH, Martinkaserne 4, 4906 Prinsach, Österreich, vertreten durch die N&N Steuerberatungsgesellschaft m.b.H., 
Schubertstraße 68, 8010 Graz, vom 21.09.2020 wegen Verletzung der Entscheidungspflicht 
betreffend den Antrag vom 30.01.2018 auf Abrechnung (§ 216 BAO) zu Recht erkannt:  
Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `FWV Luftfahrt`


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Maja Hilbich  in der Beschwerdesache der 
NKAH Luftfahrt Vertrieb, Schießstättenweg 11, 9844 Schachnern, Österreich, über die Beschwerde vom 19. Jänner 2024 gegen den Bescheid des 
Finanzamt Landeck Reutte  vom 16. Jänner 2024 betreffend Einkommensteuer 2022 zu Steuernummer 
27-855/7684  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `NKAH Luftfahrt`


</details>

---

## `verlag_org`

🔴 Weak rule

> Matches organisations ending with "Verlag" (e.g., Dorfcon-Verlag).

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `RuleFormat.REGEX`  
**Content:** `\b[A-ZÄÖÜ][\w\.‑&-]*-Verlag\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.004 | 0.007 | 7 | 7 | 0 | 7/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 7 | 0 | 1910 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2**

```
Die Dorfcon-Verlag  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle) 
Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 3**

```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT 
und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4**

```
(Der Körperschaftsteuerbescheid 2007 des partiellen 
Gesamtrechtsnachfolgers Dorfcon-Verlag  vom 26.04.2013, wo Einkünfte aus Gewerbebetrieb 
von € -665.812,12 festgesteilt wurden, erwuchs in Rechtskraft).
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 5**

```
Die Schmeltz Luftfahrt  wurde in weiterer Folge mit der 
Dorfcon-Verlag  verschmolzen.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

- Missed: `Schmeltz Luftfahrt`


```
Die Dorfcon-Verlag  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle) 
Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

- Missed: `Schmeltz Luftfahrt`

- Missed: `Houdek Maschinenbau`


```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT 
und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `FA Wien 1/23`

- Missed: `Roelfsen Versicherung`

- Missed: `Lexdon IT`

- Missed: `Houdek Maschinenbau`


```
Die Schmeltz Luftfahrt  wurde in weiterer Folge mit der 
Dorfcon-Verlag  verschmolzen.
```

- Missed: `Schmeltz Luftfahrt`


```
Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre 
daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung 
einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen: 
Gewinne verkaufte Teilbetriebe 
Houdek Maschinenbau: 
596.815,17 
Gewinne verbleibende Teilbetriebe 
Houdek Maschinenbau 
586.237,84 
Summe Gewinne: 1.183.053,01
```

- Missed: `Roelfsen Versicherung`

- Missed: `Houdek Maschinenbau`

- Missed: `Houdek Maschinenbau`


</details>

---

## `vahrenkamp_luftfahrt`

🔴 Weak rule

> Matches the specific organisation "Vahrenkamp Luftfahrt".

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bVahrenkamp\s+Luftfahrt\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.004 | 0.007 | 7 | 7 | 0 | 7/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 7 | 0 | 1910 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
2019 langte beim FA auf dem Postweg der nachfolgende Schriftsatz ein: 
„XY Steuerberater  
Mag. Dr. X.Y.  
Wirtschaftstreuhand- 
gesellschaft m.b.H.  
Steuerberater  
Zertifizierter Mediator       Wien, 2019-12-03 
Betreff: Vahrenkamp Luftfahrt, 9999 Wien B-Straße 4/7 
 Beschwerde gegen den Bescheid - Leistungsgebot 
Meine Beschwerde richtet sich gegen den Bescheid-Leistungsgebot an Frau Vahrenkamp Luftfahrt  vom 
5.11.2019, zugestellt am 13.11.2019 (siehe Anhang) mit dem Antrag auf Aufhebung dieses 
Bescheides.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 2**

```
Die Inanspruchnahme von Frau Vahrenkamp Luftfahrt  als Zahlungsverpflichtete erfolgte, weil die als 
Leistungsgerbringerin fungierende M- GmbH in Liqu.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 3**

```
Als Begründung ist anzuführen, dass Frau Vahrenkamp Luftfahrt  keine Gesamtschuldnerin aufgrund von 
Bauleistungen ist, da es sich bei den Rechnungen der M- GmbH nicht um Bauleistungen 
handelt.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 4**

```
BESCHLUSS 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Georgette Alfschnieder  in der Beschwerdesache der 
Vahrenkamp Luftfahrt, (Bf-Adresse), vertreten durch Dr. (Parteienvertretername), RA, 
(Parteienvertreteradresse), zur Beschwerde vom 3. Dezember 2019 gegen den als 
Leistungsgebot gem. § 6 BAO zur Steuernummer 99-999/9999 (M.-GmbH i.L.) ergangenen 
Bescheid des Finanzamtes Wien X (jetzt Dienststelle des Finanzamtes Österreich) vom 
5. November 2019 betreffend „Umsatzsteuerveranlagungen und div.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 5**

```
Da es sich demnach nicht um Bauleistungen handelt, ist Frau Vahrenkamp Luftfahrt  keine Person, die 
gemeinsam zur Abgabenentrichtung heranzuziehen ist, da sie nicht Gesamtschuldnerin ist.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

</details>

---

## `starker_beratung`

🔴 Weak rule

> Matches the specific organisation "Starker Beratung".

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bStarker\s+Beratung\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.003 | 0.005 | 5 | 5 | 0 | 5/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 1912 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Entscheidungsgründe 
I. Verfahrensgang 
Über das Vermögen der Starker Beratung (im Folgenden „Gemeinschuldnerin“) wurde am 10.01.2024 
das Insolvenzverfahren eröffnet.
```

| Prediction | Gold |
|------------|------|
| `Starker Beratung` | `Starker Beratung` |

**Example 2**

```
Im gegenständlichen Fall bewegt sich die festgesetzte Zwangsstrafe bei 10% der maximal 
zulässigen Höhe (pro säumiger Erklärung), womit ausreichend berücksichtigt scheint, dass die 
Säumnis zwei Erklärungen betraf, die Starker Beratung  vor und nach Konkurseröffnung ihren 
steuerlichen Verpflichtungen kaum zeitgerecht nachgekommen ist und vorliegend ein 
Missgeschick des Insolvenzverwalters zur Säumnis geführt hat.
```

| Prediction | Gold |
|------------|------|
| `Starker Beratung` | `Starker Beratung` |

**Example 3**

```
Dieser Aufforderung wurde nicht nachgekommen und reichte der Insolvenzverwalter als 
Vertreter der Starker Beratung  in der Folge auch keine Abgabenerklärungen ein bzw. übermittelte 
der belangten Behörde binnen der gesetzten Nachfrist auch sonst keinerlei Informationen, aus 
denen sich eine vorläufige Abgabenerklärung oder ein Antrag auf Fristverlängerung ergeben 
hätte können.
```

| Prediction | Gold |
|------------|------|
| `Starker Beratung` | `Starker Beratung` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Hermine Heufelder  in der Beschwerdesache der 
Starker Beratung, Klein-Veitsch-Alm 43, 4926 Baching, Österreich, vertreten durch Lena Lokämper  als Masseverwalter im 
Insolvenzverfahren der Starker Beratung, Triestingweg 4, 5632 Klammstein, Österreich, über die Beschwerde vom 5. März 2025 
gegen den Bescheid des Finanzamtes Österreich vom 6. Februar 2025 betreffend 
Zwangsstrafen 2025 Steuernummer 49-579/4181  zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Starker Beratung` | `Starker Beratung` |
| `Starker Beratung` | `Starker Beratung` |

</details>

---

## `bank_bawag`

🔴 Weak rule

> Matches the specific BAWAG P.S.K. Wohnbaubank name.

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `RuleFormat.REGEX`  
**Content:** `\bBAWAG\s+P\.S\.K\.\s+Wohnbaubank\b`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 | 3/1917 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 1914 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

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

**Example 2**

```
einer vorherigen Kontenregister-Einsicht mit Bescheiden vom 20.12.2022 die dem 
Beschwerdeführer gegenüber der Raiffeisenbank Süd-Weststeiermark, der Raiffeisenbank Wienerwald  und der BAWAG P.S.K. Wohnbaubank 
zustehenden Forderungen aus Kontokorrent oder einem Girokonto, insbesondere aus einem 
jeweils mit IBAN bezeichneten Konto.
```

| Prediction | Gold |
|------------|------|
| `BAWAG P.S.K. Wohnbaubank` | `BAWAG P.S.K. Wohnbaubank` |

**Example 3**

```
Nachdem 
keine Hemmungsgründe gemäß § 230 BAO vorlagen, sei die Vollstreckungshandlung vom 
20.12.2022 (Forderungspfändungen bei der Raiffeisenbank Süd-Weststeiermark, bei der Raiffeisenbank Wienerwald  und der 
BAWAG P.S.K. Wohnbaubank) zu Recht erfolgt.
```

| Prediction | Gold |
|------------|------|
| `BAWAG P.S.K. Wohnbaubank` | `BAWAG P.S.K. Wohnbaubank` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- Missed: `Raiffeisenbank Süd-Weststeiermark`

- Missed: `Raiffeisenbank Wienerwald`


```
einer vorherigen Kontenregister-Einsicht mit Bescheiden vom 20.12.2022 die dem 
Beschwerdeführer gegenüber der Raiffeisenbank Süd-Weststeiermark, der Raiffeisenbank Wienerwald  und der BAWAG P.S.K. Wohnbaubank 
zustehenden Forderungen aus Kontokorrent oder einem Girokonto, insbesondere aus einem 
jeweils mit IBAN bezeichneten Konto.
```

- Missed: `Raiffeisenbank Süd-Weststeiermark`

- Missed: `Raiffeisenbank Wienerwald`


```
Nachdem 
keine Hemmungsgründe gemäß § 230 BAO vorlagen, sei die Vollstreckungshandlung vom 
20.12.2022 (Forderungspfändungen bei der Raiffeisenbank Süd-Weststeiermark, bei der Raiffeisenbank Wienerwald  und der 
BAWAG P.S.K. Wohnbaubank) zu Recht erfolgt.
```

- Missed: `Raiffeisenbank Süd-Weststeiermark`

- Missed: `Raiffeisenbank Wienerwald`


</details>

---

