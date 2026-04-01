# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-01T09:08:37.223631

---

### Configuration

| Parameter | Value |
|-----------|-------|
| Pool size | 1000 |
| Train ratio | 0.70 |
| Test ratio | 0.30 |
| Shots per class | None |
| Training examples | 700 |
| Test examples | 1635 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 50 |
| Refinement iterations | 2 |
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
| Accuracy (exact match) | 93.0% |
| Coverage | 22.9% (375/1635 got a label) |
| Micro Precision | 0.819 |
| Micro Recall | 0.758 |
| Micro F1 | 0.787 |
| Macro F1 | 0.787 |

---

## 📊 Summary

| Rule | F1 | Precision | Recall | Matches |
|------|----|----------|--------|--------|
| `specific_legal_entities` |0.618 | 0.954 | 0.457 | 194 |
| `tax_authority_complex` |0.523 | 0.903 | 0.368 | 165 |
| `tax_authority` |0.391 | 0.943 | 0.247 | 106 |
| `specific_hyphenated_orgs` |0.258 | 1.000 | 0.148 | 60 |
| `tax_authority_waldviertel_klosterneuburg` |0.062 | 1.000 | 0.032 | 13 |
| `raiffeisenbank` |0.029 | 1.000 | 0.015 | 6 |
| `court_organisation` |0.029 | 0.857 | 0.015 | 7 |
| `finanzen_tradonnex` |0.010 | 1.000 | 0.005 | 2 |
| `missed_org_fa_niederoesterreich` |0.005 | 1.000 | 0.002 | 1 |
| `missed_org_dlcg_bildung` |0.005 | 1.000 | 0.002 | 1 |
| `company_with_plus` |0.005 | 0.500 | 0.002 | 2 |
| `ag_organisation` |0.005 | 0.077 | 0.002 | 13 |
| `olivier_bartha_pattern` |0.000 | 0.000 | 0.000 | 0 |
| `gmbh_organisation` |0.000 | 0.000 | 0.000 | 32 |
| `kg_organisation` |0.000 | 0.000 | 0.000 | 6 |
| `missed_org_sud_sudwil` |0.000 | 0.000 | 0.000 | 0 |
| `missed_org_nord_willemtri` |0.000 | 0.000 | 0.000 | 0 |

---

## `specific_legal_entities`

🟢 Strong rule

**F1:** 0.618 | **Precision:** 0.954 | **Recall:** 0.457  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Milan\s+H\u00e4ndlein|Manfredo\s+Herrschmann|Pastel\s+Pharma|Finanzamt\s+Grieskirchen\s+Wels|FA\s+Oststeiermark|D\u00fcfel\s+Technik\s+KG|Nord\s+Kellex|Finanzamt\s+Wien\s+8/16/17|FA\s+Wien\s+8/16/17|S\u00fcdEvent\s+AG|Finanzamt\s+Vorarlberg|Waldtra\-Sicherheit|AlpenSicherheit\s+GMBH|G\u00f6zc\u00fc\s+Getr\u00e4nke|Celikkanat\s+Garten|Finanzamt\s+Klosterneuburg|Trafenfen\s+Automotive|Gartgart\s+Dienstleistungen\s+GMBH|Mur\s+Ververzor\s+Betriebe|Planung\s+Monuniost|K\u00f6k\s+&\s+Heberlein\s+Bau|Leiss\s+Software|Okur\s+Automotive|Finanzamt\s+Bruck\s+Eisenstadt\s+Oberwart|Finanzamt\s+Spittal\s+Villach|Finanzamt\s+Gmunden\s+V\u00f6cklabruck|Raiffeisenbank\s+Wels\s+S\u00fcd|Raiffeisenkasse\s+Retz-Pulkautal|Event\s+Sudkraftlex\s+GMBH|KQPC\s+Versand\s+GMBH|Ostgart\s+AG|Rosilius\s+Pflege\s+AG|Yavasoglu\s+Analyse\s+AG|Pastl\+B\u00e4chle\s+Handel|Textil\s+Steingartlog|Gr\u00f6ne&H\u00f6velberndt\s+E-Commerce|Roelfsen\s+Versicherung|Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|WOD\s+Sicherheit\s+KG|Zumholte\s+Verlag\s+OG|Dorfcon-Verlag|Istvan\s+Gerart|Rhein\s+Normonkel\s+Manufaktur\s+GMBH|Lexdon\s+IT|Chen\s+Setzekorn|Hagdorn\s+Robotik|ZFGQ\s+Pharma\s+GMBH|Kubzyk\s+Elektro\s+AG|Finanzamt\s+Salzburg-Stadt|FA\s+Salzburg-Stadt|FA\s+Braunau\s+Ried\s+Sch\u00e4rding|Annemie\s+Bott|Kraftnex\s+Technologien\s+GMBH|Meretick\s+und\s+Adelsheimer\s+Recycling\s+KG|Landesgericht\s+Innsbruck|Schiwick\s+Finanzen\s+AG|Kraftver-Gastronomie\s+GMBH|FWV\s+Luftfahrt\s+GMBH|Biletzki&Emmert\s+Medien\s+GMBH|ZYJY\s+Automotive\s+AG|NYJ\s+Event\s+AG|Sievens\s+Automotive|OstGetr\u00e4nke|Nord\s+Druck|Donau\s+Furtkraftwald|Valbruckzor\-Energie|Bahrdt\s+Digital|OstTechnik|Naa\u00df\s+Elektro|Bersud\s+M\u00f6bel|Unter\s+Heimdorf|Hudec&Christian\s+Immobilien\s+GMBH|Reinemut\s+\+\s+Smoch\s+Handel|YXTG\s+Maschinenbau|Unter\s+Gartglanz\s+GMBH|Sudver\s+Handel\s+Services\s+GMBH|Glanznorost\s+Institut\s+GMBH|Stefansky\s+Bau\s+GMBH|Heimwald\-Forschung\s+GMBH|Dersyn\s+Immobilien\s+GMBH|Mittel\s+Unisyn\s+GMBH|Verdonlex\s+Automotive\s+GMBH|FA\s+Judenburg\s+Liezen|FA\s+Linz|H\u00f6rup\s+Gastronomie\s+AG|UnterRecycling\s+Services\s+GMBH|F\u00fcchsl\s+Touristik\s+GMBH|Bierwerth|Traun-Digital\s+KG|Mur\s+Alver\s+OG|VOLKSBANK\s+WIEN|Unter\s+Donunisee\s+AG|Forschung\s+Waldlemtal|Vahrenkamp\s+Luftfahrt|Nowothnig\s+Wind|Englert\s+M\u00f6bel|Zimmerhackel\s+Bau|Wald\s+Bruckval\s+AG|Berend\s+Energie\s+AG|Blazickova\s+&\s+Hepprich\s+Energie\s+AG|Noruniwald-Technik|Finanzamt\s+Baden\s+M\u00f6dling|FA\s+Wien\s+1/23|Finanzamt\s+Purkersdorf|FA\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|FA\s+Salzburg-Land)
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.954 | 0.457 | 0.618 | 194 | 185 | 9 | 185/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 185 | 9 | 220 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

| Prediction | Gold |
|------------|------|
| `Leiss Software` | `Leiss Software` |

**Example 2**

```
 KommR Ing. Roberta Gossling  sei die Veranstalterin und FA Salzburg-Stadt  zumindest Vermittlerin der 
Ausspielungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 3**

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

| Prediction | Gold |
|------------|------|
| `Blazickova & Hepprich Energie AG` | `Blazickova & Hepprich Energie AG` |
| `Berend Energie AG` | `Berend Energie AG` |

**Example 4**

```
Am 11.11.2022 
ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am 
Abgabenkonto des Beschwerdeführers verbucht.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 5**

```
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Vitus Preimesser  in der Beschwerdesache Dipl.-Ing. Zdenko Faiss, 
Fützental 41, 2053 Jetzelsdorf, Österreich, über die Beschwerde vom 15.05.2019 gegen den Bescheid des seinerzeitigen 
Finanzamt Baden Mödling  vom 26.04.2019, betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2017, zu Recht erkannt: 
I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `FA Grieskirchen Wels` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Elena Folkens  in der Beschwerdesache der 
Christöfl KI, Zedlacher Ochsenalm 45, 8463 Eichberg-Trautenburg, Österreich, vertreten durch StB, über die Beschwerde vom 21.3.2018 gegen 
die Bescheide des Finanzamt Purkersdorf  vom 27.2.2018 betreffend Wiederaufnahme des Verfahrens 
hinsichtlich Feststellungsbescheid Gruppenträger 2013 und Feststellungsbescheid 
Gruppenträger 2013 zu Steuernummer 30-221/9230   
I. zu Recht erkannt: Der Beschwerde gegen den Bescheid über die Wiederaufnahme 
des Verfahrens hinsichtlich Feststellungsbescheid Gruppenträger 2013 wird gemäß 
§ 266 Abs. 4 BAO Folge gegeben.
```

- Missed: `Christöfl KI` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

- Missed: `Alal-Medien` (organisation)


</details>

<details>
<summary>⚠️ False Positives (3)</summary>

```
Kff. Finn Jonigk, Arthur-Krupp-Straße 27, 9655 Moos, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH & 
Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 16. Februar 2018 gegen 
den Bescheid  
a. vom 17. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 sowie  
b. vom 18. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, beide 
erlassen vom Finanzamt Spittal Villach, Steuernummer 46-794/1326, zu Recht erkannt:  
I. Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO 
als unbegründet abgewiesen.
```

- FP: `Finanzamt Spittal Villach` (organisation)


```
In dieser Stellungnahme teilte das Finanzamt Salzburg-Stadt als Finanzstrafbehörde mit, dass 
nach dessen Ansicht gegen die bP der begründete Verdacht bestehe, dass diese 
Finanzvergehen der Abgabenhinterziehung gem § 33 Abs 1 FinstrG sowie 
Finanzordnungswidrigkeiten gem § 51 Abs 1 lit a FinStrG, jeweils im og Umfang, begangen 
habe, wobei DDr.in Kerstin Tittrich, BA  als steuerlicher Vertreter der bP dazu beigetragen habe, dass die 
bP die Abgabenhinterziehung betreffend Umsatzsteuer 2016 iHv € 58.333,33 begehen konnte.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache 
Dagobert Trübert, Ritzstraße 27, 2853 Maierhöfen, Österreich, vertreten durch Treuhand - Salzburg GmbH, Wirtschaftsprüfungs- 
und Steuerberatungsgesellschaft, Kleßheimer Allee 47, 5020 Salzburg, über die Beschwerde 
vom 27. Juni 2016 gegen den Bescheid des Finanzamtes Österreich (vormals Finanzamt 
Salzburg-Stadt) vom 21. Mai 2014 betreffend Umsatzsteuer 2008, Steuernummer 
22-918/4878  zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

- FP: `Finanzamt 
Salzburg-Stadt` (organisation)


</details>

---

## `tax_authority_complex`

🟢 Strong rule

**F1:** 0.523 | **Precision:** 0.903 | **Recall:** 0.368  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Judenburg\s+Liezen|Tirol\s+Ost|Salzburg-Stadt|Steiermark\s+Mitte|Wien\s+2/20/21/22|Oststeiermark|Grieskirchen\s+Wels|Landeck\s+Reutte|Bregenz|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Spittal\s+Villach|Gmunden\s+Vöcklabruck|Wien\s+8/16/17|Braunau\s+Ried\s+Schärding|Amstetten\s+Melk\s+Scheibbs|Deutschlandsberg\s+Leibnitz\s+Voitsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Freistadt\s+Rohrbach\s+Urfahr|Salzburg-Land|Graz-Stadt|Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|Wien\s+1/23|Purkersdorf|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Waldviertel|Klosterneuburg|Innsbruck|Wien\s+4/5/10)
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.903 | 0.368 | 0.523 | 165 | 149 | 16 | 149/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 149 | 16 | 254 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
 KommR Ing. Roberta Gossling  sei die Veranstalterin und FA Salzburg-Stadt  zumindest Vermittlerin der 
Ausspielungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Mag. Balthasar Weichslgartner  in der Beschwerdesache Basil Könemund, 
Ing.-Julius-Lott-Weg 67, 8103 Stübinggraben, Österreich, vertreten durch Dipl.-Ing. Linn Stoltefoß, über die Beschwerde vom 1. April 2020 gegen den 
Bescheid des Finanzamt Judenburg Liezen  vom 25. März 2020 zu Steuernummer 29-755/4143, mit dem ein 
Antrag gemäß § 217 Abs. 7 BAO auf Herabsetzung des mit Bescheid vom 9. März 2020 von der 
Umsatzsteuer 12/2019 festgesetzten Säumniszuschlages in Höhe von 168,07 € abgewiesen 
wurde, zu Recht erkannt:  
I. Der Beschwerde wird Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
Das Bundesfinanzgericht hat durch den Richter Mag. Berthold Brodag  in der Beschwerdesache VetR Frauke Gibhardt, 
Trulitsch 43, 8832 Hinterburg, Österreich, vertreten durch Standfest & Partner Rechtsanwälte GmbH, Wallnerstraße 
4/5/MT 44, 1010 Wien, über die Beschwerde vom 27. Jänner 2017 gegen den Bescheid des 
Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt FA) vom 15. Dezember 2016 betreffend 
Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff Bundesabgabenordnung (BAO), 
Steuernummer St.Nr., beschlossen: 
 
I. Der angefochtene Bescheid vom 15. Dezember 2016 und die Beschwerdevorentscheidung 
vom 27. September 2018 werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache 
an die Abgabenbehörde aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Example 4**

```
Am 11.11.2022 
ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am 
Abgabenkonto des Beschwerdeführers verbucht.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 5**

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Leila Coutand  in der Beschwerdesache des 
Evelyn Kogelheide, Rechte Fischa-Promenade 64, 4812 Pinsdorfberg, Österreich  vertreten durch RA,  über die Beschwerde vom 20. November 2017 
gegen die Bescheide des FA Vorarlberg (nunmehr: Finanzamt Österreich) vom 19. Oktober 2015 
betreffend Einkommensteuer 2007 und 2008 zu Steuernummer 11-143/2882  beschlossen: 
I. Die Einkommensteuerbescheide für die Jahre 2007 und 2008 vom 19. Oktober 2015 
und die Beschwerdevorentscheidung vom 6. Feber 2018 werden gemäß § 278 Abs. 1 
BAO unter Zurückverweisung der Sache an die Abgabenbehörde aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `FA Vorarlberg` | `FA Vorarlberg` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `Annemie Bott` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `Houdek Maschinenbau` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Elena Folkens  in der Beschwerdesache der 
Christöfl KI, Zedlacher Ochsenalm 45, 8463 Eichberg-Trautenburg, Österreich, vertreten durch StB, über die Beschwerde vom 21.3.2018 gegen 
die Bescheide des Finanzamt Purkersdorf  vom 27.2.2018 betreffend Wiederaufnahme des Verfahrens 
hinsichtlich Feststellungsbescheid Gruppenträger 2013 und Feststellungsbescheid 
Gruppenträger 2013 zu Steuernummer 30-221/9230   
I. zu Recht erkannt: Der Beschwerde gegen den Bescheid über die Wiederaufnahme 
des Verfahrens hinsichtlich Feststellungsbescheid Gruppenträger 2013 wird gemäß 
§ 266 Abs. 4 BAO Folge gegeben.
```

- Missed: `Christöfl KI` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Milan Händlein` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache 
Jennifer Wildfang, Kirchbrücke 7, 3352 St. Peter in der Au-Markt, Österreich, über die Beschwerde vom 20. August 2013 gegen den Bescheid des 
FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Körperschaftsteuer 2008 bis 2010, 
Steuernummer 24-852/6682  zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `FA Kirchdorf Perg Steyr` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der 
Beschwerdesache Othmar Möhlenberg, Ritzhofstraße 36, 6060 Hall in Tirol, Österreich, vertreten durch Mag. Rainer Hochstöger, 
Breitwiesergutstraße 10, 4020 Linz, über die Beschwerde - Maßnahmenbeschwerde – vom 
23. Dezember 2017 wegen Ausübung unmittelbarer verwaltungsbehördlicher Befehls- und 
Zwangsgewalt in einer Angelegenheit nach dem Glücksspielgesetz am 15.11.2017 im Lokal 
Adresse durch Organe der belangten Behörde FA Wien 4/5/10, FPFPT  
zu Recht erkannt:  
I. Die angefochtene Maßnahme – Mitnahme eines Reporters zur Kontrolle – wird 
gem. § 28 Abs. 6 erster Satz VwGVG für rechtswidrig erklärt.
```

- FP: `FA Wien 4/5/10` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Finanzamt Graz-Stadt` (organisation)


```
Kff. Finn Jonigk, Arthur-Krupp-Straße 27, 9655 Moos, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH & 
Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 16. Februar 2018 gegen 
den Bescheid  
a. vom 17. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 sowie  
b. vom 18. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, beide 
erlassen vom Finanzamt Spittal Villach, Steuernummer 46-794/1326, zu Recht erkannt:  
I. Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO 
als unbegründet abgewiesen.
```

- FP: `Finanzamt Spittal Villach` (organisation)


```
Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der 
Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische 
Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur 
Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit 
1 von 20
Seite 2 von 20
```

- FP: `Finanzamt Innsbruck` (organisation)


</details>

---

## `tax_authority`

🟢 Strong rule

**F1:** 0.391 | **Precision:** 0.943 | **Recall:** 0.247  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Judenburg\s+Liezen|Tirol\s+Ost|Salzburg-Stadt|Steiermark\s+Mitte|Wien\s+2/20/21/22|Oststeiermark|Grieskirchen\s+Wels|Landeck\s+Reutte|Bregenz|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Spittal\s+Villach|Gmunden\s+V\u00f6cklabruck|Wien\s+8/16/17|Braunau\s+Ried\s+Sch\u00e4rding|Amstetten\s+Melk\s+Scheibbs|Deutschlandsberg\s+Leibnitz\s+Voitsberg)
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.943 | 0.247 | 0.391 | 106 | 100 | 6 | 100/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 100 | 6 | 303 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
 KommR Ing. Roberta Gossling  sei die Veranstalterin und FA Salzburg-Stadt  zumindest Vermittlerin der 
Ausspielungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Mag. Balthasar Weichslgartner  in der Beschwerdesache Basil Könemund, 
Ing.-Julius-Lott-Weg 67, 8103 Stübinggraben, Österreich, vertreten durch Dipl.-Ing. Linn Stoltefoß, über die Beschwerde vom 1. April 2020 gegen den 
Bescheid des Finanzamt Judenburg Liezen  vom 25. März 2020 zu Steuernummer 29-755/4143, mit dem ein 
Antrag gemäß § 217 Abs. 7 BAO auf Herabsetzung des mit Bescheid vom 9. März 2020 von der 
Umsatzsteuer 12/2019 festgesetzten Säumniszuschlages in Höhe von 168,07 € abgewiesen 
wurde, zu Recht erkannt:  
I. Der Beschwerde wird Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
Am 11.11.2022 
ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am 
Abgabenkonto des Beschwerdeführers verbucht.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 4**

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Leila Coutand  in der Beschwerdesache des 
Evelyn Kogelheide, Rechte Fischa-Promenade 64, 4812 Pinsdorfberg, Österreich  vertreten durch RA,  über die Beschwerde vom 20. November 2017 
gegen die Bescheide des FA Vorarlberg (nunmehr: Finanzamt Österreich) vom 19. Oktober 2015 
betreffend Einkommensteuer 2007 und 2008 zu Steuernummer 11-143/2882  beschlossen: 
I. Die Einkommensteuerbescheide für die Jahre 2007 und 2008 vom 19. Oktober 2015 
und die Beschwerdevorentscheidung vom 6. Feber 2018 werden gemäß § 278 Abs. 1 
BAO unter Zurückverweisung der Sache an die Abgabenbehörde aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `FA Vorarlberg` | `FA Vorarlberg` |

**Example 5**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker, 
Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und 
Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom 
14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend 
Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `Annemie Bott` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Milan Händlein` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

- Missed: `Alal-Medien` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Priv.-Doz.in Dr.in Pamela Gscheidt  in der Beschwerdesache der 
Kudla&Kühnel Solar, Josef-Schlesinger-Straße 22, 9330 Rabenstein, Österreich, über die Beschwerde vom 6. August 2021 gegen den Bescheid des 
FA Deutschlandsberg Leibnitz Voitsberg  vom 5. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 
zu Steuernummer 49-615/4779  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `Kudla&Kühnel Solar` (organisation)


</details>

<details>
<summary>⚠️ False Positives (4)</summary>

```
Kff. Finn Jonigk, Arthur-Krupp-Straße 27, 9655 Moos, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH & 
Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 16. Februar 2018 gegen 
den Bescheid  
a. vom 17. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 sowie  
b. vom 18. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, beide 
erlassen vom Finanzamt Spittal Villach, Steuernummer 46-794/1326, zu Recht erkannt:  
I. Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO 
als unbegründet abgewiesen.
```

- FP: `Finanzamt Spittal Villach` (organisation)


```
In dieser Stellungnahme teilte das Finanzamt Salzburg-Stadt als Finanzstrafbehörde mit, dass 
nach dessen Ansicht gegen die bP der begründete Verdacht bestehe, dass diese 
Finanzvergehen der Abgabenhinterziehung gem § 33 Abs 1 FinstrG sowie 
Finanzordnungswidrigkeiten gem § 51 Abs 1 lit a FinStrG, jeweils im og Umfang, begangen 
habe, wobei DDr.in Kerstin Tittrich, BA  als steuerlicher Vertreter der bP dazu beigetragen habe, dass die 
bP die Abgabenhinterziehung betreffend Umsatzsteuer 2016 iHv € 58.333,33 begehen konnte.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Benedikt Rüecker  in der Beschwerdesache Prof.in Brunhild Nußbaumer, 
Schloss Rosegg 11, 4120 Unterfeuchtenbach, Österreich, über die Beschwerde vom 29.3.2017 gegen den Bescheid der belangten 
Behörde Finanzamt Judenburg Liezen vom 21.3.2017 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2016 beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht 
fristgerecht eingebracht zurückgewiesen.
```

- FP: `Finanzamt Judenburg Liezen` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache 
Dagobert Trübert, Ritzstraße 27, 2853 Maierhöfen, Österreich, vertreten durch Treuhand - Salzburg GmbH, Wirtschaftsprüfungs- 
und Steuerberatungsgesellschaft, Kleßheimer Allee 47, 5020 Salzburg, über die Beschwerde 
vom 27. Juni 2016 gegen den Bescheid des Finanzamtes Österreich (vormals Finanzamt 
Salzburg-Stadt) vom 21. Mai 2014 betreffend Umsatzsteuer 2008, Steuernummer 
22-918/4878  zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

- FP: `Finanzamt 
Salzburg-Stadt` (organisation)


</details>

---

## `specific_hyphenated_orgs`

🟢 Strong rule

**F1:** 0.258 | **Precision:** 1.000 | **Recall:** 0.148  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Conuni\-Heizung|Stadt\s+Dorfkraft|Inn\s+Monost|Digital\s+Seeal|Nord\s+Kellex|Milan\s+Händlein|Schmeltz\s+Luftfahrt|Houdek\s+Maschinenbau|Hörup\s+Gastronomie\s+AG|Wien\s+Waldnor\s+KG|Reinemut\s+\+\s+Smoch\s+Handel|Düfel\s+Technik\s+KG|Schoenfelder\s+Textil\s+KG|Gartgart\s+Dienstleistungen\s+GMBH|Kraftver\-Gastronomie\s+GMBH|TraunChemie\s+GMBH|InnLuftfahrt\s+GMBH|Hudec&Christian\s+Immobilien\s+GMBH|Gumpold\s+Technik\s+GMBH|RheinMetall\s+Technologien\s+GMBH|EnnsBildung|Donau\s+Furtkraftwald\s+AG|Landwirtschaft\s+Zorfurt\s+GMBH|Marzell\s+Versicherung\s+GMBH|Slenzak\s+IT\s+GMBH|BergPlanung|Holz\s+WaldTouristik\s+Technologien\s+GmbH|OGEM\s+Landwirtschaft\s+GMBH|Sud\s+Sudwil)
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.148 | 0.258 | 60 | 60 | 0 | 60/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 60 | 0 | 342 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Mit Haftungsbescheid vom 7. April 2016 wurde der Bf. als ehemaliger Geschäftsführer für die 
aushaftende Abgabenschuld der OGEM Landwirtschaft GMBH  in Höhe von Euro 22.605,06 in Anspruch 
genommen.
```

| Prediction | Gold |
|------------|------|
| `OGEM Landwirtschaft GMBH` | `OGEM Landwirtschaft GMBH` |

**Example 2**

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 3**

```
Im Feststellungsverfahren der (damaligen) Schoenfelder Textil KG  wurde am 23. Oktober 2006 ein 
Feststellungsbescheid erlassen, fand im Jahr 2015 eine Betriebsprüfung statt und wurde am 18. 
Dezember 2015 das Feststellunsgsverfahren 2005 wiederaufgenommen und ein neuer 
Feststellungsbescheid erlassen.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 4**

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

| Prediction | Gold |
|------------|------|
| `InnLuftfahrt GMBH` | `InnLuftfahrt GMBH` |

**Example 5**

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `FA Wien 1/23` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)


```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Kz 245): 
 
Donau Furtkraftwald AG  1.1.2017 - 31.12.2017 € 4.915,96 
Schoebel Getränke AG  1.1.2017 - 21.4.2017 € 4.466,60 
Donber AG  10.4.2017 - 10.4.2017 € 36,35 
Tal-Lebensmittel Gruppe AG  22.4.2017 - 30.6.2017 € 3.348,55 
Brucktraval AG  1.7.2017 - 31.12.2017 € 6.588,48
```

- Missed: `Schoebel Getränke AG` (organisation)

- Missed: `Donber AG` (organisation)

- Missed: `Tal-Lebensmittel Gruppe AG` (organisation)

- Missed: `Brucktraval AG` (organisation)


</details>

---

## `tax_authority_waldviertel_klosterneuburg`

🟢 Strong rule

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Waldviertel|Klosterneuburg)
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.032 | 0.062 | 13 | 13 | 0 | 13/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 13 | 0 | 380 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lara Plumenhoff  in der Beschwerdesache Knut Siewerth, 
Hundsgrub 29, 4173 Schindlberg, Österreich, über die Beschwerde vom 16.5.2022 gegen den Bescheid des Finanzamt Waldviertel  vom 
12. Mai 2022 über die Abweisung des Antrages auf Wiederaufnahme des Verfahrens 
betreffend Einkommensteuer 2019 vom 24.3.2022, Steuernummer 54-620/2027, zu Recht 
erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

**Example 2**

```
Nicht im Gemeinschaftsgebiet ansässige Unternehmer haben die Vorsteuererstattung laut § 3a 
der Erstattungsverordnung BGBl 279/1995 in der jeweiligen Fassung mittels amtlich 
vorgeschriebenen Vordruckes beim FA Waldviertel  zu beantragen.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Gertrude Schonefeld  in der Beschwerdesache des 
Fabienne Stegerwald, Almmeisterweg 31, 4212 Traidendorf, Österreich, über die Beschwerde vom 2.März 2023, eingebracht am 6. März 
2023, gegen den Bescheid des FA Waldviertel  vom 7. März 2023 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2022 zur Steuernummer 51-026/1591  zu Recht erkannt:  
I. Der angefochtene Bescheid wird abgeändert.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag.a Anita Müller  in der Beschwerdesache des 
Siegbert Koeberer, Obermayrstraße 19, 5270 Mauerkirchen, Österreich, vertreten durch Rechtsanwälte, über die Beschwerde vom 
31.8.2015 gegen den Haftungsbescheid des FA Waldviertel  vom 29.7.2015 zu Recht erkannt:  
I. Der Beschwerde wird teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 5**

```
Zum Übermittlungsvorgang wird seitens der beschwerdeführenden Partei Folgendes 
vorgebracht: Die Beschwerde sei am 4.3.2024 eingeschrieben an das Finanzamt Klosterneuburg (FAÖ) per 
Adresse Postfach 260, 1000 Wien gesendet worden.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Klosterneuburg` | `Finanzamt Klosterneuburg` |

</details>

---

## `raiffeisenbank`

🟢 Strong rule

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
Raiffeisenbank\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+)*(?:\s+Bankstelle\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+)?
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.015 | 0.029 | 6 | 6 | 0 | 6/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 0 | 313 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Am 27.12.2022 bezahlte die Raiffeisenbank Wienerwald  den Betrag von € 28.423,94 zuzüglich der 
gegenständlichen Pfändungsgebühr und Barauslagen (insg. sohin € 28.721,13) an die belangte 
Behörde, welche sodann die beiden anderen Forderungspfändungen einstellte.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 2**

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

**Example 3**

```
Wegen eines Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende 
Forderung gepfändet.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wels Süd` | `Raiffeisenbank Wels Süd` |

**Example 4**

```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Mittleres Mostviertel` | `Raiffeisenbank Mittleres Mostviertel` |

**Example 5**

```
Hierauf übermittelte der Beschwerdeführer ein Schreiben der Raiffeisenbank Stallhofen  vom 
24.2.2014, in welchem bestätigt wurde, dass er im Jahre 2013 € 4.377,00 an Kreditrückzahlung 
geleistet hat.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- Missed: `Niederösterreichische Vorsorgekasse` (organisation)


</details>

---

## `court_organisation`

🟢 Strong rule

**F1:** 0.029 | **Precision:** 0.857 | **Recall:** 0.015  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?:Bundesfinanzgericht|(?<!Bezirksgericht\s)Bezirksgericht)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.857 | 0.015 | 0.029 | 7 | 6 | 1 | 6/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 1 | 382 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Dies würde der 
Berechnungsmethode des BG Bezirksgericht Silz  entsprechen, das sowohl auf Seiten des 
Unterhaltsbedarfes wie auch auf Seiten des geleisteten Unterhalts eine Berechnung über den 
gesamten Zeitraum (Juni 2017 bis Februar 2023) angestellt hat.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 2**

```
Ich habe inzwischen auch noch 
einen letztinstanzlichen Beschluss des LG Innsbruck, der den bereits 2 x vorgelegten Beschluss des 
Bezirksgerichtes Bezirksgericht Silz  vom 16.03.2023 bestätigt: Es liegt gerichtlich geprüft keinerlei 
Unterhaltsverletzung vor!
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 3**

```
Die Summe 
entspricht jener, die auch das BG Bezirksgericht Silz  errechnet hat.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 4**

```
Das Geburtsdatum der minderjährigen Tochter sowie die Feststellung, dass gegenüber dem 
Beschwerdeführer kein Unterhaltstitel besteht, ergibt sich aus dem Beschluss des BG 
Bezirksgericht Silz  vom 03.02.2023 bzw. dem Vorbringen des Beschwerdeführers.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 5**

```
Mit Eingabe vom 24.04.2023 wurde seitens des Beschwerdeführers im Wesentlichen 
ausgeführt, dass im fraglichen Beschluss des BG Bezirksgericht Silz  kein Unterhaltsanspruch von 
EUR 320,00 festgestellt worden sei.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Ich habe inzwischen auch noch 
einen letztinstanzlichen Beschluss des LG Innsbruck, der den bereits 2 x vorgelegten Beschluss des 
Bezirksgerichtes Bezirksgericht Silz  vom 16.03.2023 bestätigt: Es liegt gerichtlich geprüft keinerlei 
Unterhaltsverletzung vor!
```

- Missed: `LG Innsbruck` (organisation)


```
Dagegen stellte der Beschwerdeführer mit Antrag vom 2. Juli 2019 ohne weitere Begründung 
den Antrag auf Entscheidung über die Beschwerde durch das Bundesfinanzgericht 
Das Bundesfinanzgericht hat erwogen: 
Zu Spruchpunkt I. 
Der Beschwerdeführer war im haftungsrelevanten Zeitraum Beschwerdeführer und ab 28. April 
2009 Liquidator der Hempel Heizung GMBH.
```

- Missed: `Hempel Heizung GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Dagegen stellte der Beschwerdeführer mit Antrag vom 2. Juli 2019 ohne weitere Begründung 
den Antrag auf Entscheidung über die Beschwerde durch das Bundesfinanzgericht 
Das Bundesfinanzgericht hat erwogen: 
Zu Spruchpunkt I. 
Der Beschwerdeführer war im haftungsrelevanten Zeitraum Beschwerdeführer und ab 28. April 
2009 Liquidator der Hempel Heizung GMBH.
```

- FP: `Bundesfinanzgericht 
Das Bundesfinanzgericht` (organisation)


</details>

---

## `finanzen_tradonnex`

🟢 Strong rule

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
Finanzen\s+Tradonnex
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 | 2/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 249 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Dagegen erhob der Beschwerdeführer durch seinen steuerlichen Vertreter mit Schriftsatz vom 
23. Juni 2015 Beschwerde und beantragte, den Mietaufwand der Garagen (2011 bis 2013) und 
die Aufwendungen für Marken- und Musterschutzrechte (2012 und 2013) der Finanzen Tradonnex 
GmbH anzuerkennen, verdeckte Ausschüttungen nicht anzunehmen und dementsprechend 
keine Kapitalertragsteuer festzusetzen.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

**Example 2**

```
Gegen dieses Erkenntnis erhob die Finanzen Tradonnex  GmbH außerordentliche Revision beim 
Verwaltungsgerichtshof.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

</details>

---

## `missed_org_fa_niederoesterreich`

🟢 Strong rule

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
FA\s+Niederösterreich\s+Mitte
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 | 1/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 348 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch den Richter Dr. Martin Christoph Wittmann in der 
Beschwerdesache Franz Gscheidner, Peter-Thumb-Straße 33, 5151 Eisping, Österreich, vertreten durch Köstenbauer 
Wirtschaftstreuhand KG, Stefan Seedoch Allee 14, 8230 Hartberg, über die Beschwerde vom 
24. Jänner 2018 gegen den Bescheid des FA Niederösterreich Mitte (nunmehr Finanzamt Österreich) vom 
19. Dezember 2017, Steuernummer 47-142/1476, betreffend Wiederaufnahme des 
Verfahrens gemäß § 303 BAO hinsichtlich Energieabgabenvergütung für das Kalenderjahr 2011 
erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

</details>

---

## `missed_org_dlcg_bildung`

🟢 Strong rule

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
DLCG\s+Bildung
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 | 1/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 276 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Des Weiteren wurde keineswegs behauptet, Frau DLCG Bildung  hätte sich „ausreichend 
Informationen" verschafft.
```

| Prediction | Gold |
|------------|------|
| `DLCG Bildung` | `DLCG Bildung` |

</details>

---

## `company_with_plus`

🟡 Medium rule

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)([A-Z][a-zA-ZäöüÄÖÜß\s\&\-]+\s*\+\s*[A-Z][a-zA-ZäöüÄÖÜß\s\&\-]+(?:\s+(?:GmbH|KG|AG|Versicherung|Handel|Logistik|Solutions|Verlag|Dienstleistungen|Cloud)?))\b
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.500 | 0.002 | 0.005 | 2 | 1 | 1 | 1/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 1 | 358 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Zu den Oldtimern und Garagierungskosten halten wir fest, dass auf Grund des 
Firmenwortlautes (Pastl+Bächle Handel = Besitz/Vermögen), der aufrechten Gewerbeberechtigung und 
des Unternehmensgegenstandes u.a. auch der Handel mit Fahrzeugen beabsichtigt war.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Was die dem Vorlageantrag beigelegten Umsatzlisten des Kontos von Frau Partnerin betrifft, 
die 250 Euro monatlich unter dem Verwendungszweck Alimente ausweisen, ist bei dieser 
Sachlage (Bestätigung der vollständigen Zahlung + Klage auf Unterhaltserhöhung) davon 
auszugehen, dass die ausgewiesene Überweisung von 250 Euro pro Monat nur den Unterhalt 
für Kimberly Schindlmayer  darstellt.
```

- FP: `Bestätigung der vollständigen Zahlung + Klage auf ` (organisation)


</details>

---

## `ag_organisation`

🔴 Weak rule

**F1:** 0.005 | **Precision:** 0.077 | **Recall:** 0.002  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+AG)\b
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.077 | 0.002 | 0.005 | 13 | 1 | 12 | 1/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 12 | 366 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Kubzyk Elektro AG  GmbH € 17.356,99 
Meldung 3(2) 19.09.-02.10.
```

| Prediction | Gold |
|------------|------|
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Festgestellter Sachverhalt  
Im Jahr 2016 war die beschwerdeführende Partei beim Unternehmen Logbach-Bildung AG  als Key 
Account Manager / Business Development Manager – Angestellter tätig.
```

- Missed: `Logbach-Bildung AG` (organisation)


```
Vor diesem Hintergrund kann die in der im Beschwerdefall vereinbarte Bedingun g der 
Inanspruchnahme der Schiwick Finanzen AG , „ dass der Pächter trotz schriftlicher Aufforderung und 
Fristsetzung von 4 Wochen seinen Verpflichtungen aus dem Vertrag nicht nachkommt “, nicht 
5 von 7
Seite 6 von 7
```

- Missed: `Schiwick Finanzen AG` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Schiwick Finanzen AG` (organisation)

- Missed: `Verdonlex Automotive GMBH` (organisation)


```
Beweiswürdigung 
Der Bezug der inländischen Pension und der Einkünfte aus dem Dienstverhältnis zur Ostgart AG 
ergeben sich aus den jeweiligen übermittelten Lohnzetteln.
```

- Missed: `Ostgart AG` (organisation)


```
In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG  als „Garant“ 
bezeichnet und es erfolgt dabei eine ausdrückliche Bezugnahme auf § 880a 2.
```

- Missed: `Schiwick Finanzen AG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Festgestellter Sachverhalt  
Im Jahr 2016 war die beschwerdeführende Partei beim Unternehmen Logbach-Bildung AG  als Key 
Account Manager / Business Development Manager – Angestellter tätig.
```

- FP: `Bildung AG` (organisation)


```
Vor diesem Hintergrund kann die in der im Beschwerdefall vereinbarte Bedingun g der 
Inanspruchnahme der Schiwick Finanzen AG , „ dass der Pächter trotz schriftlicher Aufforderung und 
Fristsetzung von 4 Wochen seinen Verpflichtungen aus dem Vertrag nicht nachkommt “, nicht 
5 von 7
Seite 6 von 7
```

- FP: `Vor diesem Hintergrund kann die in der im Beschwerdefall vereinbarte Bedingun g der 
Inanspruchnahme der Schiwick Finanzen AG` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- FP: `Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG` (organisation)


```
Beweiswürdigung 
Der Bezug der inländischen Pension und der Einkünfte aus dem Dienstverhältnis zur Ostgart AG 
ergeben sich aus den jeweiligen übermittelten Lohnzetteln.
```

- FP: `Beweiswürdigung 
Der Bezug der inländischen Pension und der Einkünfte aus dem Dienstverhältnis zur Ostgart AG` (organisation)


```
In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG  als „Garant“ 
bezeichnet und es erfolgt dabei eine ausdrückliche Bezugnahme auf § 880a 2.
```

- FP: `In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG` (organisation)


</details>

---

## `olivier_bartha_pattern`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
Olivier\s+u\.\s+Bartha\s+Recycling
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/3429 |

</details>

---

## `gmbh_organisation`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+GMBH)\b
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 32 | 0 | 32 | 0/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 32 | 404 |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Vor dieser Eintragung verfügte die Bf im 
beschwerdegegenständlichen Zeitraum über keinen Anteil an der Klusner&Päffgen Bildung GMBH.
```

- Missed: `Klusner&Päffgen Bildung GMBH` (organisation)


```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

- Missed: `Gartgart Dienstleistungen GMBH` (organisation)

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


```
Auch in den von der Rhein Normonkel Manufaktur GMBH  an das Finanzamt 
übermittelten Lohnzettel, der den im Einkommensteuerbescheid 2014 vom 20.5.2015 
ausgewiesenen Einkünften aus nichtselbständiger Arbeit zugrunde liegt, hat der volle Pkw-
Sachbezug Eingang gefunden.
```

- Missed: `Rhein Normonkel Manufaktur GMBH` (organisation)


```
Soweit es den Mitarbeitern der Bludszat Maschinenbau GMBH  möglich war, haben diese auch Kontakt mit der 
MA 6 gehalten.
```

- Missed: `Bludszat Maschinenbau GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Vor dieser Eintragung verfügte die Bf im 
beschwerdegegenständlichen Zeitraum über keinen Anteil an der Klusner&Päffgen Bildung GMBH.
```

- FP: `Päffgen Bildung GMBH` (organisation)


```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

- FP: `Gastronomie GMBH` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Stadt die InnLuftfahrt GMBH` (organisation)


```
Auch in den von der Rhein Normonkel Manufaktur GMBH  an das Finanzamt 
übermittelten Lohnzettel, der den im Einkommensteuerbescheid 2014 vom 20.5.2015 
ausgewiesenen Einkünften aus nichtselbständiger Arbeit zugrunde liegt, hat der volle Pkw-
Sachbezug Eingang gefunden.
```

- FP: `Auch in den von der Rhein Normonkel Manufaktur GMBH` (organisation)


```
Soweit es den Mitarbeitern der Bludszat Maschinenbau GMBH  möglich war, haben diese auch Kontakt mit der 
MA 6 gehalten.
```

- FP: `Soweit es den Mitarbeitern der Bludszat Maschinenbau GMBH` (organisation)


</details>

---

## `kg_organisation`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+KG)\b
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 | 0/405 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 6 | 374 |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- Missed: `Traun-Digital KG` (organisation)


```
Er sei als Kommanditist bei 
der Düfel Technik KG  bereits seit Ende 2020 ausgeschieden und sei seit 2021 nur mehr als 
Angestellter/Arbeiter bei der KG beschäftigt.
```

- Missed: `Düfel Technik KG` (organisation)


```
Sowohl der am 25. Mai 2016 erlassene Feststellungsbescheid als auch die am 22. Dezember 
2016 erlassene Beschwerdevorentscheidung wurden an die Traun-Digital KG  adressiert.
```

- Missed: `Traun-Digital KG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- FP: `Digital KG` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Xaver Quaas  in der Beschwerdesache StR Laetitia Dingwerth, 
Winkler Straße 6, 9971 Feld, Österreich, vertreten durch Wirtschaftstreuhand Tirol Steuerberatungs GmbH&Co KG, 
Rennweg 18, 6020 Innsbruck, über die Beschwerde vom 13. Dezember 2021 gegen den 
Bescheid des Finanzamtes Österreich vom 15. November 2021 betreffend Abweisung eines 
Antrages auf Aufhebung des Bescheides vom 21. Juni 2021, mit welchem eine Zwangsstrafe 
festgesetzt wurde, nach § 299 BAO, Steuernummer 41-421/3086, 
zu Recht erkannt: 
I. 
Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `Co KG` (organisation)


```
Entsprechend den Angaben der steuerlichen Vertretung („Das Betriebsareal B-A ist zunächst je 
zur Hälfte von der KommR Lukas Kirischenko  und der A. KG genutzt worden.“) und von M. (im Rahmen der 
Prüfung wurde das Nutzungsverhältnis des Gebäudes von M. mit jeweils 50% [GmbH u KG] 
angegeben [siehe BP Bericht TZ 2 vom 31.07.2013]) wird die Nutzung des Gebäudes der beiden 
Betriebe im Schätzungswege mit jeweils 50% angenommen.
```

- FP: `GmbH u KG` (organisation)


```
Er sei als Kommanditist bei 
der Düfel Technik KG  bereits seit Ende 2020 ausgeschieden und sei seit 2021 nur mehr als 
Angestellter/Arbeiter bei der KG beschäftigt.
```

- FP: `Er sei als Kommanditist bei 
der Düfel Technik KG` (organisation)

- FP: `Arbeiter bei der KG` (organisation)


```
Sowohl der am 25. Mai 2016 erlassene Feststellungsbescheid als auch die am 22. Dezember 
2016 erlassene Beschwerdevorentscheidung wurden an die Traun-Digital KG  adressiert.
```

- FP: `Digital KG` (organisation)


</details>

---

## `missed_org_sud_sudwil`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
Süd\s+Sudwil
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/3429 |

</details>

---

## `missed_org_nord_willemtri`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Format:** ``  
**Content:**
```
Nord\s+Willemtri\s+KG
```

**Description:**
`

`

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/3429 |

</details>

---

