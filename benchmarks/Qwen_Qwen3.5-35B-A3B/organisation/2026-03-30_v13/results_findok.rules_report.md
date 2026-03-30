# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-30T17:08:46.989746

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

### Configuration

| Parameter | Value |
|-----------|-------|
| Pool size | 1000 |
| Train ratio | 0.70 |
| Test ratio | 0.10 |
| Shots per class | None |
| Training examples | 700 |
| Test examples | 161 |
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
| Accuracy (exact match) | 59.0% |
| Coverage | 111.2% (179/161 got a label) |
| Micro Precision | 0.816 |
| Micro Recall | 0.723 |
| Micro F1 | 0.766 |
| Macro F1 | 0.766 |

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `specific_legal_entities` | 🟡 Medium | 0.594 | 0.956 | 0.431 | 91 |
| `tax_authority_complex` | 🔴 Weak | 0.431 | 0.966 | 0.277 | 58 |
| `tax_authority` | 🔴 Weak | 0.350 | 0.977 | 0.213 | 44 |
| `specific_hyphenated_orgs` | 🔴 Weak | 0.288 | 1.000 | 0.168 | 34 |
| `raiffeisenbank` | 🔴 Weak | 0.057 | 0.750 | 0.030 | 8 |
| `court_organisation` | 🔴 Weak | 0.039 | 1.000 | 0.020 | 4 |
| `ag_organisation` | 🔴 Weak | 0.029 | 0.429 | 0.015 | 7 |
| `missed_org_nord_willemtri` | 🔴 Weak | 0.020 | 1.000 | 0.010 | 2 |
| `finanzen_tradonnex` | 🔴 Weak | 0.010 | 1.000 | 0.005 | 1 |
| `missed_org_fa_niederoesterreich` | 🔴 Weak | 0.010 | 1.000 | 0.005 | 1 |
| `kg_organisation` | 🔴 Weak | 0.010 | 0.200 | 0.005 | 5 |
| `gmbh_organisation` | 🔴 Weak | 0.009 | 0.050 | 0.005 | 20 |
| `olivier_bartha_pattern` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |
| `tax_authority_waldviertel_klosterneuburg` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |
| `company_with_plus` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 2 |
| `missed_org_sud_sudwil` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |
| `missed_org_dlcg_bildung` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |

---

## `specific_legal_entities`

🟡 Medium rule

**F1:** 0.594 | **Precision:** 0.956 | **Recall:** 0.431  

**Format:** `regex`  
**Content:**
```
(?:Milan\s+H\u00e4ndlein|Manfredo\s+Herrschmann|Pastel\s+Pharma|Finanzamt\s+Grieskirchen\s+Wels|FA\s+Oststeiermark|D\u00fcfel\s+Technik\s+KG|Nord\s+Kellex|Finanzamt\s+Wien\s+8/16/17|FA\s+Wien\s+8/16/17|S\u00fcdEvent\s+AG|Finanzamt\s+Vorarlberg|Waldtra\-Sicherheit|AlpenSicherheit\s+GMBH|G\u00f6zc\u00fc\s+Getr\u00e4nke|Celikkanat\s+Garten|Finanzamt\s+Klosterneuburg|Trafenfen\s+Automotive|Gartgart\s+Dienstleistungen\s+GMBH|Mur\s+Ververzor\s+Betriebe|Planung\s+Monuniost|K\u00f6k\s+&\s+Heberlein\s+Bau|Leiss\s+Software|Okur\s+Automotive|Finanzamt\s+Bruck\s+Eisenstadt\s+Oberwart|Finanzamt\s+Spittal\s+Villach|Finanzamt\s+Gmunden\s+V\u00f6cklabruck|Raiffeisenbank\s+Wels\s+S\u00fcd|Raiffeisenkasse\s+Retz-Pulkautal|Event\s+Sudkraftlex\s+GMBH|KQPC\s+Versand\s+GMBH|Ostgart\s+AG|Rosilius\s+Pflege\s+AG|Yavasoglu\s+Analyse\s+AG|Pastl\+B\u00e4chle\s+Handel|Textil\s+Steingartlog|Gr\u00f6ne&H\u00f6velberndt\s+E-Commerce|Roelfsen\s+Versicherung|Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|WOD\s+Sicherheit\s+KG|Zumholte\s+Verlag\s+OG|Dorfcon-Verlag|Istvan\s+Gerart|Rhein\s+Normonkel\s+Manufaktur\s+GMBH|Lexdon\s+IT|Chen\s+Setzekorn|Hagdorn\s+Robotik|ZFGQ\s+Pharma\s+GMBH|Kubzyk\s+Elektro\s+AG|Finanzamt\s+Salzburg-Stadt|FA\s+Salzburg-Stadt|FA\s+Braunau\s+Ried\s+Sch\u00e4rding|Annemie\s+Bott|Kraftnex\s+Technologien\s+GMBH|Meretick\s+und\s+Adelsheimer\s+Recycling\s+KG|Landesgericht\s+Innsbruck|Schiwick\s+Finanzen\s+AG|Kraftver-Gastronomie\s+GMBH|FWV\s+Luftfahrt\s+GMBH|Biletzki&Emmert\s+Medien\s+GMBH|ZYJY\s+Automotive\s+AG|NYJ\s+Event\s+AG|Sievens\s+Automotive|OstGetr\u00e4nke|Nord\s+Druck|Donau\s+Furtkraftwald|Valbruckzor\-Energie|Bahrdt\s+Digital|OstTechnik|Naa\u00df\s+Elektro|Bersud\s+M\u00f6bel|Unter\s+Heimdorf|Hudec&Christian\s+Immobilien\s+GMBH|Reinemut\s+\+\s+Smoch\s+Handel|YXTG\s+Maschinenbau|Unter\s+Gartglanz\s+GMBH|Sudver\s+Handel\s+Services\s+GMBH|Glanznorost\s+Institut\s+GMBH|Stefansky\s+Bau\s+GMBH|Heimwald\-Forschung\s+GMBH|Dersyn\s+Immobilien\s+GMBH|Mittel\s+Unisyn\s+GMBH|Verdonlex\s+Automotive\s+GMBH|FA\s+Judenburg\s+Liezen|FA\s+Linz|H\u00f6rup\s+Gastronomie\s+AG|UnterRecycling\s+Services\s+GMBH|F\u00fcchsl\s+Touristik\s+GMBH|Bierwerth|Traun-Digital\s+KG|Mur\s+Alver\s+OG|VOLKSBANK\s+WIEN|Unter\s+Donunisee\s+AG|Forschung\s+Waldlemtal|Vahrenkamp\s+Luftfahrt|Nowothnig\s+Wind|Englert\s+M\u00f6bel|Zimmerhackel\s+Bau|Wald\s+Bruckval\s+AG|Berend\s+Energie\s+AG|Blazickova\s+&\s+Hepprich\s+Energie\s+AG|Noruniwald-Technik|Finanzamt\s+Baden\s+M\u00f6dling|FA\s+Wien\s+1/23|Finanzamt\s+Purkersdorf|FA\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|FA\s+Salzburg-Land)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.956 | 0.431 | 0.594 | 91 | 87 | 4 | 87/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 87 | 4 | 115 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Bei Teilnahme erteilt der Spielteilnehmer Finanzamt Salzburg-Stadt  den Auftrag, für ihn bei 
KommR Ing. Roberta Gossling  ein Los der Sofortlotterie zu erwerben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 2**

```
Dass der Vorlageantrag gegen die an die Kraftver-Gastronomie GMBH  ergangene 
Beschwerdevorentscheidung unter der FinanzOnline-Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH  gestellt wurde, ergibt sich unzweifelhaft aus den vom Finanzamt erstellten, 
aktenkundigen Ausdrucken aus der Anfragedatenbank der Finanzverwaltung.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 3**

```
Die WOD Sicherheit KG  hat ihren Gewinn nach § 4 Abs. 3 EStG 1988 ermittelt.
```

| Prediction | Gold |
|------------|------|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

**Example 4**

```
Pendlerpauschale in Höhe von EUR 2.184,00 und 
Pendlereuro in Höhe von EUR 350,00 betreffend die Zeit von Jänner bis Oktober beim 
Arbeitgeber „Rosilius Pflege AG“ fanden, anders als im Einkommensteuerbescheid vom 
09.04.2024, keine Berücksichtigung mehr.
```

| Prediction | Gold |
|------------|------|
| `Rosilius Pflege AG` | `Rosilius Pflege AG` |

**Example 5**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Aurelia Kleinicke  in der Beschwerdesache der I AG & 
atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung, 
Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen 
1. Kök & Heberlein Bau  GmbH & Co KG, Straße3, Ort, 
2. Leiss Software  GmbH & Co KG, Straße3, Ort,  
3. Okur Automotive  GmbH & Co KG, Straße3, Ort und 
4.
```

| Prediction | Gold |
|------------|------|
| `Leiss Software` | `Leiss Software` |
| `Okur Automotive` | `Okur Automotive` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

</details>

<details>
<summary>❌ Missed (5)</summary>

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

- Missed: `Psomadakis Touristik` (organisation)


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

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)


```
Ob diese Kurse für eine 
vom Beschwerdeführer im Jahr 2017 beruflich ausgeübte Tätigkeit, insbesondere für seine 
Tätigkeit als Fotograf bei der Donau Furtkraftwald AG  erforderlich waren bzw. dadurch verursacht wurden, 
konnte mangels Beantwortung der diesbezüglichen Vorhalte durch den Beschwerdeführer 
ebenfalls nicht festgestellt werden.
```

- Missed: `Donau Furtkraftwald AG` (organisation)


```
Zur Werbefotografie ist noch festzuhalten, dass die 
Donau Furtkraftwald AG  zwar in der Werbebranche tätig ist, ihr Unternehmensgegenstand jedoch vor allem 
darin besteht, Plakatflächen zu Werbezwecken zu vermieten (s. 
https://www.Donau Furtkraftwald AG .at/de).
```

- Missed: `Donau Furtkraftwald AG` (organisation)

- Missed: `Donau Furtkraftwald AG` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- Missed: `Gökdemir Landwirtschaft AG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (3)</summary>

```
Ob diese Kurse für eine 
vom Beschwerdeführer im Jahr 2017 beruflich ausgeübte Tätigkeit, insbesondere für seine 
Tätigkeit als Fotograf bei der Donau Furtkraftwald AG  erforderlich waren bzw. dadurch verursacht wurden, 
konnte mangels Beantwortung der diesbezüglichen Vorhalte durch den Beschwerdeführer 
ebenfalls nicht festgestellt werden.
```

- FP: `Donau Furtkraftwald` (organisation)


```
Zur Werbefotografie ist noch festzuhalten, dass die 
Donau Furtkraftwald AG  zwar in der Werbebranche tätig ist, ihr Unternehmensgegenstand jedoch vor allem 
darin besteht, Plakatflächen zu Werbezwecken zu vermieten (s. 
https://www.Donau Furtkraftwald AG .at/de).
```

- FP: `Donau Furtkraftwald` (organisation)

- FP: `Donau Furtkraftwald` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


</details>

---

## `tax_authority_complex`

🔴 Weak rule

**F1:** 0.431 | **Precision:** 0.966 | **Recall:** 0.277  

**Format:** `regex`  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Judenburg\s+Liezen|Tirol\s+Ost|Salzburg-Stadt|Steiermark\s+Mitte|Wien\s+2/20/21/22|Oststeiermark|Grieskirchen\s+Wels|Landeck\s+Reutte|Bregenz|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Spittal\s+Villach|Gmunden\s+Vöcklabruck|Wien\s+8/16/17|Braunau\s+Ried\s+Schärding|Amstetten\s+Melk\s+Scheibbs|Deutschlandsberg\s+Leibnitz\s+Voitsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Freistadt\s+Rohrbach\s+Urfahr|Salzburg-Land|Graz-Stadt|Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|Wien\s+1/23|Purkersdorf|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Waldviertel|Klosterneuburg|Innsbruck|Wien\s+4/5/10)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.966 | 0.277 | 0.431 | 58 | 56 | 2 | 56/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 56 | 2 | 146 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Bei Teilnahme erteilt der Spielteilnehmer Finanzamt Salzburg-Stadt  den Auftrag, für ihn bei 
KommR Ing. Roberta Gossling  ein Los der Sofortlotterie zu erwerben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 2**

```
Begründung 
Mit Bescheid des Finanzamt Grieskirchen Wels  vom 5. Februar 2021 wurde zur Steuernummer 57-862/6163 
der beschwerdeführenden Partei (Bf) die UVZ 9/2020 festgesetzt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Priv.-Doz.in Vanessa de Marco  in der Beschwerdesache Bruno Valtinat, 
Oberweitersdorfer Straße 20, 3300 Greinsfurth, Österreich, über die Beschwerde vom 30. September 2022 gegen den Bescheid des 
FA Oststeiermark  vom 1. September 2022 über die Abweisung des Antrages vom 17.5.2022 auf 
Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung (erhöhte 
Familienbeihilfe) ab Jän.
```

| Prediction | Gold |
|------------|------|
| `FA Oststeiermark` | `FA Oststeiermark` |

**Example 4**

```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Janina Greiner-Jopp  in der Beschwerdesache HR Jeremias Meincke, 
Johann-Ennser-Straße 4, 3492 Engabrunn, Österreich, über die Beschwerde vom 13. Juni 2019 gegen den Bescheid des FA St. Johann Tamsweg Zell am See 
vom 3. Juni 2019 über die Rückforderung zu Unrecht bezogener Beträge Familienbeihilfe und 
Kinderabsetzbetrag für März 2018 bis Mai 2019 zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 5**

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

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


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

- Missed: `Psomadakis Touristik` (organisation)


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

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Calvin Borggrebe  in der Beschwerdesache Julia Mühlenweg, 
Fritz-Müller-Weg 118, 4251 Weinviertl, Österreich, über die Beschwerde vom 13. April 2016 gegen den Bescheid des FA Graz-Stadt – 
nunmehr Finanzamt Niederösterreich Mitte  vom 9. März 2016 betreffend Säumniszuschlag 2016 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Niederösterreich Mitte` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Regina Jaross  in der Beschwerdesache der 
Maschinenbau Derwilsee, Scheunengasse 22, 9560 Fasching, Österreich, über die Beschwerde vom 19. März 2021 gegen den zur 
Steuernummer 50-226/7982  ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des Finanzamt Steiermark Mitte ) vom 25. August 2020 betreffend Einkommensteuer 2018 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

- Missed: `Maschinenbau Derwilsee` (organisation)


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Finanzamt Graz-Stadt` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


</details>

---

## `tax_authority`

🔴 Weak rule

**F1:** 0.350 | **Precision:** 0.977 | **Recall:** 0.213  

**Format:** `regex`  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Judenburg\s+Liezen|Tirol\s+Ost|Salzburg-Stadt|Steiermark\s+Mitte|Wien\s+2/20/21/22|Oststeiermark|Grieskirchen\s+Wels|Landeck\s+Reutte|Bregenz|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Spittal\s+Villach|Gmunden\s+V\u00f6cklabruck|Wien\s+8/16/17|Braunau\s+Ried\s+Sch\u00e4rding|Amstetten\s+Melk\s+Scheibbs|Deutschlandsberg\s+Leibnitz\s+Voitsberg)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.977 | 0.213 | 0.350 | 44 | 43 | 1 | 43/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 43 | 1 | 159 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Bei Teilnahme erteilt der Spielteilnehmer Finanzamt Salzburg-Stadt  den Auftrag, für ihn bei 
KommR Ing. Roberta Gossling  ein Los der Sofortlotterie zu erwerben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 2**

```
Begründung 
Mit Bescheid des Finanzamt Grieskirchen Wels  vom 5. Februar 2021 wurde zur Steuernummer 57-862/6163 
der beschwerdeführenden Partei (Bf) die UVZ 9/2020 festgesetzt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Priv.-Doz.in Vanessa de Marco  in der Beschwerdesache Bruno Valtinat, 
Oberweitersdorfer Straße 20, 3300 Greinsfurth, Österreich, über die Beschwerde vom 30. September 2022 gegen den Bescheid des 
FA Oststeiermark  vom 1. September 2022 über die Abweisung des Antrages vom 17.5.2022 auf 
Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung (erhöhte 
Familienbeihilfe) ab Jän.
```

| Prediction | Gold |
|------------|------|
| `FA Oststeiermark` | `FA Oststeiermark` |

**Example 4**

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

**Example 5**

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

- Missed: `Psomadakis Touristik` (organisation)


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

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Regina Jaross  in der Beschwerdesache der 
Maschinenbau Derwilsee, Scheunengasse 22, 9560 Fasching, Österreich, über die Beschwerde vom 19. März 2021 gegen den zur 
Steuernummer 50-226/7982  ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des Finanzamt Steiermark Mitte ) vom 25. August 2020 betreffend Einkommensteuer 2018 zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

- Missed: `Maschinenbau Derwilsee` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- Missed: `Gökdemir Landwirtschaft AG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


</details>

---

## `specific_hyphenated_orgs`

🔴 Weak rule

**F1:** 0.288 | **Precision:** 1.000 | **Recall:** 0.168  

**Format:** `regex`  
**Content:**
```
(?:Conuni\-Heizung|Stadt\s+Dorfkraft|Inn\s+Monost|Digital\s+Seeal|Nord\s+Kellex|Milan\s+Händlein|Schmeltz\s+Luftfahrt|Houdek\s+Maschinenbau|Hörup\s+Gastronomie\s+AG|Wien\s+Waldnor\s+KG|Reinemut\s+\+\s+Smoch\s+Handel|Düfel\s+Technik\s+KG|Schoenfelder\s+Textil\s+KG|Gartgart\s+Dienstleistungen\s+GMBH|Kraftver\-Gastronomie\s+GMBH|TraunChemie\s+GMBH|InnLuftfahrt\s+GMBH|Hudec&Christian\s+Immobilien\s+GMBH|Gumpold\s+Technik\s+GMBH|RheinMetall\s+Technologien\s+GMBH|EnnsBildung|Donau\s+Furtkraftwald\s+AG|Landwirtschaft\s+Zorfurt\s+GMBH|Marzell\s+Versicherung\s+GMBH|Slenzak\s+IT\s+GMBH|BergPlanung|Holz\s+WaldTouristik\s+Technologien\s+GmbH|OGEM\s+Landwirtschaft\s+GMBH|Sud\s+Sudwil)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.168 | 0.288 | 34 | 34 | 0 | 34/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 34 | 0 | 168 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Dass der Vorlageantrag gegen die an die Kraftver-Gastronomie GMBH  ergangene 
Beschwerdevorentscheidung unter der FinanzOnline-Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH  gestellt wurde, ergibt sich unzweifelhaft aus den vom Finanzamt erstellten, 
aktenkundigen Ausdrucken aus der Anfragedatenbank der Finanzverwaltung.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 2**

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

| Prediction | Gold |
|------------|------|
| `InnLuftfahrt GMBH` | `InnLuftfahrt GMBH` |

**Example 3**

```
Begründend führte die 
Beschwerdeführerin in der Beschwerde aus, dass die Gewinnermittlung für 2007 auf der Ebene 
der Houdek Maschinenbau  nach allgemeinen Grundsätzen durchzuführen sei, da der 
Vermögensübergang hinsichtlich der 11 Tankstellen auf die Schmeltz Luftfahrt  erst mit Ablauf des 
Spaltungsstichtages (Spaltungsstichtag 31.12.2007) per 1.1.2008 stattgefunden habe.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

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
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)


```
Rechtsansicht 
des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten 
innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei 
der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen 
Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen 
Verlusten) bei der Roelfsen Versicherung  führt.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

- Missed: `Dorfcon-Verlag` (organisation)


```
Die Krolitzki Beratung  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Manfredo Herrschmann (partielle) 
Gesamtrechtsnachfolgerin der Milan Händlein.
```

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Manfredo Herrschmann` (organisation)


```
Bei den aus der Milan Händlein 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Annemie Bott  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Annemie Bott).
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Annemie Bott` (organisation)


</details>

---

## `raiffeisenbank`

🔴 Weak rule

**F1:** 0.057 | **Precision:** 0.750 | **Recall:** 0.030  

**Format:** `regex`  
**Content:**
```
Raiffeisenbank\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+)*(?:\s+Bankstelle\s+[A-Z][a-zA-ZäöüÄÖÜß\-]+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.750 | 0.030 | 0.057 | 8 | 6 | 2 | 6/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 2 | 196 |

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
| `Raiffeisenbank Mittleres Mostviertel` | `Raiffeisenbank Mittleres Mostviertel` |

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
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |
| `Raiffeisenbank Süd-Weststeiermark` | `Raiffeisenbank Süd-Weststeiermark` |

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
<summary>❌ Missed (4)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` (organisation)


```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- Missed: `Niederösterreichische Vorsorgekasse` (organisation)


```
Aus diesem Grunde sowie um allfälligen weiteren Gläubigern des Beschwerdeführers 
zuvorzukommen war es daher gerechtfertigt, gleichzeitig auf alle drei Konten zuzugreifen, 
wobei die Behörde die Kontenpfändungen bei der Raiffeisenbank Süd-Weststeiermark  und der BAWAG P.S.K. Wohnbaubank 
ohnedies eingestellt hat, nachdem die Abgabenforderung von der Raiffeisenbank Wienerwald  bezahlt 
wurde.
```

- Missed: `BAWAG P.S.K. Wohnbaubank` (organisation)


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- Missed: `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` (organisation)


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend 
Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

- FP: `Raiffeisenbank Karnische Rion  Bankstelle St` (organisation)


```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis 
zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der 
Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

- FP: `Raiffeisenbank Karnische Rion  Bankstelle St` (organisation)


</details>

---

## `court_organisation`

🔴 Weak rule

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Content:**
```
(?:Bundesfinanzgericht|(?<!Bezirksgericht\s)Bezirksgericht)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.020 | 0.039 | 4 | 4 | 0 | 4/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 198 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Die Tatsache, dass der 
klagenden/widerbeklagten Partei im Scheidungsverfahren Verfahrenshilfe durch Beigebung 
eines Rechtsanwalts gewährt wurde, ergibt sich aus dem vorgelegten Beschluss des 
Bezirksgericht Neunkirchen  vom 05.01.2017 (Verweis auf den Beschluss vom 03.10.2016).
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 2**

```
Beiliegend wurde erneut der Beschluss des BG Bezirksgericht Silz  vom 03.02.2023 sowie ein 
Kontoauszug betreffend die Unterhaltszahlungen im Jahr 2022 übermittelt.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 3**

```
Die Tatsache, dass beide Parteien des Scheidungsverfahrens anwaltlich vertreten wurden, 
ergibt sich ebenfalls aus dem Vorbringen des Beschwerdeführers bzw. aus den übermittelten 
Dokumenten (Scheidungsurteil des Bezirksgericht Neunkirchen).
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 4**

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

</details>

---

## `ag_organisation`

🔴 Weak rule

**F1:** 0.029 | **Precision:** 0.429 | **Recall:** 0.015  

**Format:** `regex`  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.429 | 0.015 | 0.029 | 7 | 3 | 4 | 3/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 4 | 199 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Pendlerpauschale in Höhe von EUR 2.184,00 und 
Pendlereuro in Höhe von EUR 350,00 betreffend die Zeit von Jänner bis Oktober beim 
Arbeitgeber „Rosilius Pflege AG“ fanden, anders als im Einkommensteuerbescheid vom 
09.04.2024, keine Berücksichtigung mehr.
```

| Prediction | Gold |
|------------|------|
| `Rosilius Pflege AG` | `Rosilius Pflege AG` |

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

**Example 3**

```
Zur Werbefotografie ist noch festzuhalten, dass die 
Donau Furtkraftwald AG  zwar in der Werbebranche tätig ist, ihr Unternehmensgegenstand jedoch vor allem 
darin besteht, Plakatflächen zu Werbezwecken zu vermieten (s. 
https://www.Donau Furtkraftwald AG .at/de).
```

| Prediction | Gold |
|------------|------|
| `Donau Furtkraftwald AG` | `Donau Furtkraftwald AG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- Missed: `Talkel-Versand AG` (organisation)

- Missed: `Hebebrand Recycling AG` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Schiwick Finanzen AG` (organisation)

- Missed: `Verdonlex Automotive GMBH` (organisation)


```
In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG  als „Garant“ 
bezeichnet und es erfolgt dabei eine ausdrückliche Bezugnahme auf § 880a 2.
```

- Missed: `Schiwick Finanzen AG` (organisation)


```
Zur Werbefotografie ist noch festzuhalten, dass die 
Donau Furtkraftwald AG  zwar in der Werbebranche tätig ist, ihr Unternehmensgegenstand jedoch vor allem 
darin besteht, Plakatflächen zu Werbezwecken zu vermieten (s. 
https://www.Donau Furtkraftwald AG .at/de).
```


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- Missed: `Gökdemir Landwirtschaft AG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (4)</summary>

```
Verjährung sei nicht eingetreten, weil es am 16. Oktober 2014 zu einer erfolglosen 
Lohnpfändung an den damaligen Arbeitgeber Talkel-Versand AG  und am 5. April 2016 zu einer 
Lohnpfändung an den damaligen Arbeitgeber Hebebrand Recycling AG  gekommen sei.
```

- FP: `Versand AG` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- FP: `Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG` (organisation)


```
In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG  als „Garant“ 
bezeichnet und es erfolgt dabei eine ausdrückliche Bezugnahme auf § 880a 2.
```

- FP: `In der im Beschwerdefall maßgeblichen Vertragsklausel wird die Schiwick Finanzen AG` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- FP: `Stadt gegenüber Gökdemir Landwirtschaft AG` (organisation)


</details>

---

## `missed_org_nord_willemtri`

🔴 Weak rule

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
Nord\s+Willemtri\s+KG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.010 | 0.020 | 2 | 2 | 0 | 2/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 200 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

| Prediction | Gold |
|------------|------|
| `Nord Willemtri KG` | `Nord Willemtri KG` |

**Example 2**

```
Die belangte Behörde 
bringt dazu vor, dass sich der ursprüngliche Antrag auf Aussetzung gem § 212a BAO rein auf 
das Verfahren betreffend den (abgeleiteten) Einkommensteuerbescheid 2021 beziehe und 
keine Berufung auf das Beschwerdeverfahren bei der Nord Willemtri KG  erfolgt sei.
```

| Prediction | Gold |
|------------|------|
| `Nord Willemtri KG` | `Nord Willemtri KG` |

</details>

---

## `finanzen_tradonnex`

🔴 Weak rule

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
Finanzen\s+Tradonnex
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.005 | 0.010 | 1 | 1 | 0 | 1/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 201 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Die Finanzen Tradonnex  GmbH brachte ihrerseits Beschwerde gegen die Bescheide betreffend 
Wiederaufnahme des Verfahrens hinsichtlich Körperschaftsteuer 2011 und 2012 sowie 
Umsatzsteuer 2012 und Körperschaftsteuer 2011 bis 2013 und Umsatzsteuer 2012 ein.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

</details>

---

## `missed_org_fa_niederoesterreich`

🔴 Weak rule

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
FA\s+Niederösterreich\s+Mitte
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 1.000 | 0.005 | 0.010 | 1 | 1 | 0 | 1/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 201 |

</details>

<details>
<summary>✅ Worked (1)</summary>

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

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat den Richter Mag. Hermann Weckauf  in der Beschwerdesache Manuela Neuenfeldt, Horneburgstraße 68, 9815 Unterkolbnitz, Österreich, vertreten durch MONDSEE-TREUHAND Wiedlroither GmbH Wirtschaftsprüfer & 
Steuerberater, Alfred Jaeger-Weg 4, 5310 Mondsee, über die Beschwerde vom 14. September 
2017 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 21. August 2017 betreffend Einkommensteuer 
2014 und vom 20. Jänner 2017 gegen den Bescheid des FA Niederösterreich Mitte  vom 30. November 2016 
betreffend Einkommensteuer 2015, beide Steuernummer 33-759/4012  zu Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

- Missed: `Finanzamt Niederösterreich Mitte` (organisation)


</details>

---

## `kg_organisation`

🔴 Weak rule

**F1:** 0.010 | **Precision:** 0.200 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.200 | 0.005 | 0.010 | 5 | 1 | 4 | 1/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 4 | 201 |

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
<summary>❌ Missed (4)</summary>

```
Die WOD Sicherheit KG  hat ihren Gewinn nach § 4 Abs. 3 EStG 1988 ermittelt.
```

- Missed: `WOD Sicherheit KG` (organisation)


```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- Missed: `Traun-Digital KG` (organisation)


```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

- Missed: `Nord Willemtri KG` (organisation)


```
Zum Nachweis des Ausscheidens als Kommanditist aus der KG 
übermittelte er ein Schreiben samt Unterschriftsbeglaubigung an das Handelsgericht Wien 
(Firmenbuch), in dem die Düfel Technik KG  die Änderung der Gesellschafterverhältnisse bekanntgab 
und um entsprechende Eintragung im Firmenbuch ersuchte.
```

- Missed: `Düfel Technik KG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (4)</summary>

```
Die WOD Sicherheit KG  hat ihren Gewinn nach § 4 Abs. 3 EStG 1988 ermittelt.
```

- FP: `Die WOD Sicherheit KG` (organisation)


```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

- FP: `Digital KG` (organisation)


```
Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG  gegen den 
Feststellungsbescheid als nicht wenig erfolgsversprechend.
```

- FP: `Wie im Sachverhaltsteil festgestellt erscheint die Beschwerde der Nord Willemtri KG` (organisation)


```
Zum Nachweis des Ausscheidens als Kommanditist aus der KG 
übermittelte er ein Schreiben samt Unterschriftsbeglaubigung an das Handelsgericht Wien 
(Firmenbuch), in dem die Düfel Technik KG  die Änderung der Gesellschafterverhältnisse bekanntgab 
und um entsprechende Eintragung im Firmenbuch ersuchte.
```

- FP: `Zum Nachweis des Ausscheidens als Kommanditist aus der KG` (organisation)


</details>

---

## `gmbh_organisation`

🔴 Weak rule

**F1:** 0.009 | **Precision:** 0.050 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)(?<![bei\s])(?<![von\s])(?<![für\s])(?<![in\s])(?<![an\s])(?<![auf\s])(?<![mit\s])(?<![zur\s])(?<![zum\s])([A-Z][a-zA-ZäöüÄÖÜß\s\-]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß\s\-]+)*\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.050 | 0.005 | 0.009 | 20 | 1 | 19 | 1/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 19 | 201 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Gegenstand der 
vorzunehmenden Ermittlungshandlungen werden vor diesem Hintergrund auch die 
betroffenen „verbundenen Unternehmen“ (DonauRecycling GMBH, XJOV Cloud Dienstleistungen GMBH) sein.
```

| Prediction | Gold |
|------------|------|
| `DonauRecycling GMBH` | `DonauRecycling GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Dass der Vorlageantrag gegen die an die Kraftver-Gastronomie GMBH  ergangene 
Beschwerdevorentscheidung unter der FinanzOnline-Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH  gestellt wurde, ergibt sich unzweifelhaft aus den vom Finanzamt erstellten, 
aktenkundigen Ausdrucken aus der Anfragedatenbank der Finanzverwaltung.
```

- Missed: `Kraftver-Gastronomie GMBH` (organisation)

- Missed: `Gartgart Dienstleistungen GMBH` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


```
Die TraunChemie GMBH  haftet gemäß § 9 Abs 7 VStG über die verhängten Geldstrafen und 
Verfahrenskosten sowie für sonstige in Geld bemessene Unrechtsfolgen und zur ungeteilten 
Hand.
```

- Missed: `TraunChemie GMBH` (organisation)


```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- Missed: `Gartgart Dienstleistungen GMBH` (organisation)

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- Missed: `Klusner&Päffgen Bildung GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Dass der Vorlageantrag gegen die an die Kraftver-Gastronomie GMBH  ergangene 
Beschwerdevorentscheidung unter der FinanzOnline-Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH  gestellt wurde, ergibt sich unzweifelhaft aus den vom Finanzamt erstellten, 
aktenkundigen Ausdrucken aus der Anfragedatenbank der Finanzverwaltung.
```

- FP: `Dass der Vorlageantrag gegen die an die Kraftver-Gastronomie GMBH  ergangene 
Beschwerdevorentscheidung unter der FinanzOnline-Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH` (organisation)


```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Stadt die InnLuftfahrt GMBH` (organisation)


```
Die TraunChemie GMBH  haftet gemäß § 9 Abs 7 VStG über die verhängten Geldstrafen und 
Verfahrenskosten sowie für sonstige in Geld bemessene Unrechtsfolgen und zur ungeteilten 
Hand.
```

- FP: `Die TraunChemie GMBH` (organisation)


```
Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  im 
Namen der Kraftver-Gastronomie GMBH  gehandelt hätte, finden sich weder in der FinanzOnline-Eingabe 
selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben.
```

- FP: `Gastronomie GMBH` (organisation)


```
Ebenso unstrittig ist, dass die materiellen 
Voraussetzungen hinsichtlich der Einbeziehung der Klusner&Päffgen Bildung GMBH  ab dem Jahr 2018 
vorliegen.
```

- FP: `Päffgen Bildung GMBH` (organisation)


</details>

---

## `olivier_bartha_pattern`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
Olivier\s+u\.\s+Bartha\s+Recycling
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 0 | 202 |

</details>

---

## `tax_authority_waldviertel_klosterneuburg`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
(?:Finanzamt\s+|FA\s+)(?:Waldviertel|Klosterneuburg)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 0 | 202 |

</details>

---

## `company_with_plus`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
(?<![a-zA-ZäöüÄÖÜß\s])(?<!Der\s)(?<!Die\s)(?<!Das\s)(?<!Den\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!den\s)([A-Z][a-zA-ZäöüÄÖÜß\s\&\-]+\s*\+\s*[A-Z][a-zA-ZäöüÄÖÜß\s\&\-]+(?:\s+(?:GmbH|KG|AG|Versicherung|Handel|Logistik|Solutions|Verlag|Dienstleistungen|Cloud)?))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 | 0/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 2 | 202 |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Pastl+Bächle Handel  als belangter Verband, mit Sitz in [...] 
4. B GmbH als belangter Verband, mit Sitz in Wienerweltenweg 9, 3200 Neustift, Österreich 
zu Recht erkannt:  
A B, die Pastl+Bächle Handel  und die B GmbH sind schuldig, es haben im Bereich des Finanzamtes Baden 
Mödling grob fahrlässig 
1) A B  
I) als Geschäftsführer der Firma Pastl+Bächle Handel 
a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter 
Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bescheidmäßig 
festzusetzende Abgaben, nämlich 
  2011 2012 2013 2014 2015 Summe 
Umsatzsteuer iHv 2.619,96 8.934,65 300,00 437,00 450,00 € 12.741,61 
Köst iHv 1.500,59 10.337,20 7.250,00 3.796,88 562,50 € 21.447,30 
Summe in € 4.120,55 19.271,85 7.550,00 4.233,88 1.012,50 € 36.188.78 
verkürzt, sowie 
b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden 
Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen 
Offenlegungs- und Wahrheitspﬂicht, Verkürzung an 
Kapitalertragsteuer 2012 in der Höhe von € 1.440,63 
2013 in der Höhe von € 9.765,69 
2014 in der Höhe von € 5.207,81 
2015 in der Höhe von € 899,91 
insgesamt somit € 17.312,04 bewirkt.
```

- Missed: `Pastl+Bächle Handel` (organisation)

- Missed: `Pastl+Bächle Handel` (organisation)

- Missed: `Pastl+Bächle Handel` (organisation)


```
Meine Belege werden in einer Mappe gesammelt und die werden von ÖU(Name abgekürzt) 
(Rüterborries+Friderich Möbel) aufbewahrt.
```

- Missed: `Rüterborries+Friderich Möbel` (organisation)


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
Pastl+Bächle Handel  als belangter Verband, mit Sitz in [...] 
4. B GmbH als belangter Verband, mit Sitz in Wienerweltenweg 9, 3200 Neustift, Österreich 
zu Recht erkannt:  
A B, die Pastl+Bächle Handel  und die B GmbH sind schuldig, es haben im Bereich des Finanzamtes Baden 
Mödling grob fahrlässig 
1) A B  
I) als Geschäftsführer der Firma Pastl+Bächle Handel 
a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter 
Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bescheidmäßig 
festzusetzende Abgaben, nämlich 
  2011 2012 2013 2014 2015 Summe 
Umsatzsteuer iHv 2.619,96 8.934,65 300,00 437,00 450,00 € 12.741,61 
Köst iHv 1.500,59 10.337,20 7.250,00 3.796,88 562,50 € 21.447,30 
Summe in € 4.120,55 19.271,85 7.550,00 4.233,88 1.012,50 € 36.188.78 
verkürzt, sowie 
b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden 
Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen 
Offenlegungs- und Wahrheitspﬂicht, Verkürzung an 
Kapitalertragsteuer 2012 in der Höhe von € 1.440,63 
2013 in der Höhe von € 9.765,69 
2014 in der Höhe von € 5.207,81 
2015 in der Höhe von € 899,91 
insgesamt somit € 17.312,04 bewirkt.
```

- FP: `Pastl+Bächle Handel  als belangter ` (organisation)


```
Meine Belege werden in einer Mappe gesammelt und die werden von ÖU(Name abgekürzt) 
(Rüterborries+Friderich Möbel) aufbewahrt.
```

- FP: `Rüterborries+Friderich ` (organisation)


</details>

---

## `missed_org_sud_sudwil`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
Süd\s+Sudwil
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 0 | 202 |

</details>

---

## `missed_org_dlcg_bildung`

🔴 Weak rule

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
DLCG\s+Bildung
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP | Coverage |
|-----------|--------|----|---------|----|----|----------|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0/202 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 0 | 0 | 202 |

</details>

---

