# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-29T13:08:49.483688

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-29/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 800 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 548 |
| Validation documents | 138 |
| Test documents | 786 |
| Train sentences | 3122 |
| Validation sentences | 588 |
| Test sentences | 92563 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | True |
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
| Accuracy (exact match) | 98.8% |
| True Positives | 733 |
| False Positives | 1202 |
| False Negatives | 621 |
| Total Gold Entities | 1354 |
| Micro Precision | 37.9% |
| Micro Recall | 54.1% |
| Micro F1 | 44.6% |
| Macro F1 | 44.6% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `FA Acronym Entities` | 6.1% | 84.3% | 3.2% | 51 | 43 | 8 |
| `German Company Entities (GmbH/AG/KG)` | 42.0% | 36.9% | 48.8% | 1792 | 661 | 1131 |
| `Raiffeisenbank Entities` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `Finanzamt Full Name Entities` | 3.9% | 31.5% | 2.1% | 89 | 28 | 61 |
| `Specific Company Patterns` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `FA Acronym Entities` 🏆

**F1:** 0.061 | **Precision:** 0.843 | **Recall:** 0.032  

**Format:** `regex`  
**Rule ID:** `850bf205`  
**Description:**
Matches 'FA' (Finanzamt) followed by location names, handling abbreviations and specific locations.

**Content:**
```
(?<![a-zA-Z])(?:\b|\s|(?<=\)))(FA\s+(?:Grieskirchen\s+Wels|Spittal\s+Villach|Klosterneuburg|Tirol\s+Ost|Vorarlberg|Landeck\s+Reutte|Wien\s+2/20/21/22|Wien\s+8/16/17|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Judenburg\s+Liezen|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Innsbruck|Linz|Purkersdorf|Schwechat\s+Gerasdorf|Steiermark\s+Mitte|Gmunden\s+V\u00f6cklabruck|Amstetten\s+Melk\s+Scheibbs|Salzburg-Land|Schwechat|Gmunden|V\u00f6cklabruck|Innsbruck|Braunau\s+Ried\s+Sch\u00e4rding|Oststeiermark|Nieder\u00f6sterreich\s+Mitte|Kirchdorf\s+Perg\s+Steyr|Graz-Stadt))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.843 | 0.032 | 0.061 | 51 | 43 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 43 | 8 | 1292 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Vanessa Nemetz  in der Beschwerdesache Lydia Medert, BSc,  Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Innsbruck  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 02-329/4844  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Vanessa Nemetz` (person)
- `Lydia Medert, BSc` (person)
- `Hochbaustraße 33, 9335 Lölling Sonnseite, Österreich` (address)
- `02-329/4844` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Landeck Reutte` | `FA Landeck Reutte` |

**Missed by this rule (FN):**

- `Priv.-Doz. Eckard Sellnow` (person)
- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130001.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130001.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Ruprecht Blübaum  in der Beschwerdesache Lee Heterich, Bakk. art. Bakk. iur.,  Economogasse 27, 7503 Zuberbach, Österreich, über die Beschwerde vom 13. Dezember 2016 gegen den Bescheid des  FA Kirchdorf Perg Steyr  vom 24. November 2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2015 zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Dr. Ruprecht Blübaum` (person)
- `Lee Heterich, Bakk. art. Bakk. iur.` (person)
- `Economogasse 27, 7503 Zuberbach, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Dr. Hon.-Prof. Dragan Höh` (person)
- `ÖkR Mag.a Catharina Schmalenstrot` (person)
- `8.b Straße 126, 4632 Buchet, Österreich` (address)
- `Floriane Herppich` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133447.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Philipp Harazin  in der Beschwerdesache Priv.-Doz. Kevin Morzinsky,  Strußnighof 37, 9631 Kleinbergl, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Bruck Eisenstadt Oberwart), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 58-060/5953  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Dr. Philipp Harazin` (person)
- `Priv.-Doz. Kevin Morzinsky` (person)
- `Strußnighof 37, 9631 Kleinbergl, Österreich` (address)
- `58-060/5953` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Francois Huppertz  in der Beschwerdesache OSR Isolde Bohnenkämper  vertreten  durch StB, über die Beschwerde vom 5. Dezember 2014 gegen die Bescheide des FA Klagenfurt St. Veit Wolfsberg  (nunmehr FA) vom 31. Oktober 2014 betreffend Einkommensteuer 2009 und 2010 St.Nr.  80-848/9629 (nunmehr xx-yyy/yyyy) zu Recht erkannt:     I. Die Beschwerde gegen den Einkommensteuerbescheid 2009 wird gemäß § 279  Bundesabgabenordnung (BAO) als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Univ.-Prof. Francois Huppertz` (person)
- `OSR Isolde Bohnenkämper` (person)
- `80-848/9629` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lorena Zydat  in der Beschwerdesache Knut Duchoslav,  Felbauweg 4, 8435 Wagendorf, Österreich, vertreten durch Dr. Heinz Häupl Rechtsanwalts GmbH, Stockwinkl 18, 4865  Nußdorf/Attersee, über die   1) Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamt Purkersdorf  vom 9. August  2019 betreffend Festsetzung von ersten Säumniszuschlägen in Höhe von 128,38 €,  568,79 € und 266,87 €;  2) Beschwerde vom 15. Oktober 2019 gegen den Bescheid des FA Purkersdorf  vom 13.  September 2019 über die Abweisung eines Aussetzungsantrages;

| Predicted | Gold |
|---|---|
| `FA Purkersdorf` | `FA Purkersdorf` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Lorena Zydat` (person)
- `Knut Duchoslav` (person)
- `Felbauweg 4, 8435 Wagendorf, Österreich` (address)
- `Finanzamt Purkersdorf` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_2`)


3) Beschwerde vom 15. Oktober 2019 gegen den Bescheid des FA Purkersdorf  vom 2. Oktober  2019 über die Abweisung eines Aussetzungsantrages,  Steuernummer 62-389/9476, zu Recht erkannt:   I. Der Beschwerde vom 12. September 2019 betreffend Festsetzung eines ersten  Säumniszuschlages in Höhe von 128,38 € wird gemäß § 279 BAO Folge gegeben und der  angefochtene Bescheid - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `FA Purkersdorf` | `FA Purkersdorf` |

**Missed by this rule (FN):**

- `62-389/9476` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134777.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134777.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Mag.a Estelle Grimaudo  in der Beschwerdesache des  Karin Dinnebier Bf1-Adr***V über die Beschwerde vom 18. Mai 2021 gegen den Bescheid des  FA Innsbruck  vom 22. April 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  zu Steuernummer 51-562/2946  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Mag.a Mag.a Estelle Grimaudo` (person)
- `Karin Dinnebier` (person)
- `51-562/2946` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/134859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134859.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Liu Leitgebel  in der Beschwerdesache Hon.-Prof.in Pascal Fredecke, MA BA,  Larchach 48, 7301 Girm, Österreich, über die Beschwerde vom 30. März 2021 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 15. Jänner 2021 betreffend Umsatzsteuer 2019 Steuernummer 40-437/5867  zu Recht  erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Amstetten Melk Scheibbs` | `FA Amstetten Melk Scheibbs` |

**Missed by this rule (FN):**

- `Mag. Liu Leitgebel` (person)
- `Hon.-Prof.in Pascal Fredecke, MA BA` (person)
- `Larchach 48, 7301 Girm, Österreich` (address)
- `40-437/5867` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Leitgebel  in der Beschwerdesache ÖkR Achmed von Lampe,  Kreuzbach 25, 6441 Köfels, Österreich, vertreten durch WIRTSCHAFTSTREUHAND Steuerberatung GmbH,  Ohlsdorferstraße 18, 4810 Gmunden, über die Beschwerde vom 31. Jänner 2020 gegen den  Bescheid des FA Steiermark Mitte  vom 28. Jänner 2020 betreffend Abweisung eines Antrages auf  Aussetzung der Einhebung gemäß § 212a BAO, Steuernummer 05-972/9664, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Dr.in Huberta Leitgebel` (person)
- `ÖkR Achmed von Lampe` (person)
- `Kreuzbach 25, 6441 Köfels, Österreich` (address)
- `05-972/9664` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Edeltraud Kooper  in der Beschwerdesache des *Bf*,  vertreten durch Rechtsanwälte AB, über die Beschwerde vom 20. November 2017 gegen die  Bescheide des FA Judenburg Liezen  vom 19. Oktober 2015 betreffend Einkommensteuer und  Anspruchszinsen für die Jahre 2005 bis 2008 zu Recht erkannt:  I. Der Beschwerde gegen die Einkommensteuerbescheide für die Jahre 2005 bis 2008  wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Judenburg Liezen` | `FA Judenburg Liezen` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Edeltraud Kooper` (person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Juliana Preissle  in der Beschwerdesache des  OStR Adalbert Rehak, Untere Morgengabe 6, 4150 Märzing, Österreich, vertreten durch murtax Steuerberatungs GmbH, Bundesstraße  13b, 8850 Murau, über die Beschwerde vom 17. März 2021 gegen den Bescheid des FA Niederösterreich Mitte  vom 18. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017  Steuernummer 18-360/7906  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Hon.-Prof.in Juliana Preissle` (person)
- `OStR Adalbert Rehak` (person)
- `Untere Morgengabe 6, 4150 Märzing, Österreich` (address)
- `18-360/7906` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/135979.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Katharina Stockenbrand  in der Beschwerdesache des Bf,  vertreten durch StB, über die Beschwerde vom 19. Oktober 2020 gegen den Bescheid des  FA Landeck Reutte  vom 16. September 2020 betreffend Normverbrauchsabgabe für den  Kalendermonat April 2014 zu Steuernummer 37-205/0632  nach Durchführung einer  mündlichen Verhandlung zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Landeck Reutte` | `FA Landeck Reutte` |

**Missed by this rule (FN):**

- `Dr.in Katharina Stockenbrand` (person)
- `37-205/0632` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/136478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136478.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Erna Wachtmeister  in der Beschwerdesache des  Sheila Ferrarius, St. Gertraud 8B, 4203 Stratreith, Österreich  vertreten durch StB, über die Beschwerden vom 12. Februar 2019  gegen die Bescheide des FA Purkersdorf  vom 15. Jänner 2019 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre 2011 bis 2015 und Einkommensteuer  für die Jahre 2011 bis 2015 zu Steuernummer 94-277/7826  zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer für die Jahre 2011 bis 2013 werden abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Purkersdorf` | `FA Purkersdorf` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Erna Wachtmeister` (person)
- `Sheila Ferrarius` (person)
- `St. Gertraud 8B, 4203 Stratreith, Österreich` (address)
- `94-277/7826` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/136687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Nannemann  in der Beschwerdesache  Dipl.-Ing. Kirstin Bergjohann, Oberhöfen 28, 3621 Mitterarnsdorf, Österreich,   über die Beschwerde vom 31. Mai 2021 gegen den Bescheid des FA Steiermark Mitte  vom 28. Mai 2021  betreffend Einkommensteuer 2020, Steuernummer **** zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Dr.in Valentina Nannemann` (person)
- `Dipl.-Ing. Kirstin Bergjohann` (person)
- `Oberhöfen 28, 3621 Mitterarnsdorf, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/136951.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136951.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Juliette Keisers  in der Beschwerdesache   Daria Oberven, Reschenhof 9, 6622 Tal, Österreich, vertreten durch 1A Steuerberatungs GmbH, Münchner Straße 26,  6130 Schwaz,   über die Beschwerde vom 12. April 2021 gegen den Bescheid des FA Vorarlberg  vom 10. März  2021, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `FA Vorarlberg` | `FA Vorarlberg` |

**Missed by this rule (FN):**

- `Dr.in Juliette Keisers` (person)
- `Daria Oberven` (person)
- `Reschenhof 9, 6622 Tal, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/138666.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138666.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Charlotte Bublies  in der Beschwerdesache des  Mario Bohms, Gruberweg 21, 2372 Gießhübl, Österreich, vertreten durch RA Dr. Rainer Wechselberger, Laubichl 121, 6290  Mayrhofen, über die Beschwerde vom 30. Dezember 2014 gegen die Bescheide des FA Bruck Eisenstadt Oberwart  vom 24. November 2014 betreffend Festsetzung der Normverbrauchsabgabe und Festsetzung  eines Verspätungszuschlages für den Zeitraum 06/2010 sowie Festsetzung der  Kraftfahrzeugsteuer für die Monate 06-12/2010, 01-12/2011, 01-12/2012, 01-12/2013 und 01-

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Dr.in Charlotte Bublies` (person)
- `Mario Bohms` (person)
- `Gruberweg 21, 2372 Gießhübl, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Oskar Stahmer  in der Beschwerdesache Manuela Guenter  vertreten  durch STB2, über die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des FA Niederösterreich Mitte  vom 10. Dezember 2015, Steuernummer 37-652/4810, betreffend Einkommensteuer 2014  zu Recht erkannt:    Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Missed by this rule (FN):**

- `Dr. Oskar Stahmer` (person)
- `Manuela Guenter` (person)
- `37-652/4810` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Andrea Drom  in der Beschwerdesache Corbinian Neumetzler,  Am Haidbach 19, 9620 Obervellach, Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des FA Graz-Stadt  vom  12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer  85-520/0851, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Hon.-Prof. Univ.-Prof. Andrea Drom` (person)
- `Corbinian Neumetzler` (person)
- `Am Haidbach 19, 9620 Obervellach, Österreich` (address)
- `85-520/0851` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/140219.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140219.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Noel Bredenkamp  in der Beschwerdesache KzlR Hedwig Gröpler, Bakk. phil.,  Kaiseredter Straße 7, 9341 Gassarest, Österreich, über die Beschwerde vom 31. Dezember 2012 gegen den Bescheid des  FA Schwechat Gerasdorf (nunmehr Finanzamt FA) vom 27. November 2012 betreffend Körperschaftsteuer  2011 (Steuernummer 12-667/4807 ) zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Schwechat Gerasdorf` | `FA Schwechat Gerasdorf` |

**Missed by this rule (FN):**

- `Dr. Noel Bredenkamp` (person)
- `KzlR Hedwig Gröpler, Bakk. phil.` (person)
- `Kaiseredter Straße 7, 9341 Gassarest, Österreich` (address)
- `12-667/4807` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/140894.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140894.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Achmed Wethkamp  in der Beschwerdesache Rosemarie Dobereiner,  Nobelstraße 5, 6623 Namlos, Österreich, vertreten durch Dr. Carolin Schmid-Gasser, Zollgasse 4, 6850 Dornbirn, über  die Beschwerde vom 9. Dezember 2016 gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 24. November  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, Steuernummer  54-026/3265, zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Bruck Eisenstadt Oberwart` | `FA Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Mag. Achmed Wethkamp` (person)
- `Rosemarie Dobereiner` (person)
- `Nobelstraße 5, 6623 Namlos, Österreich` (address)
- `54-026/3265` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Camilla Tutschek  in der Beschwerdesache des  Karola Poepping, Gemeine Brongen 4, 9433 St. Jakob, Österreich, vertreten durch X-Steuerberatung betreffend Beschwerde vom  20. März 2020 gegen die zur Steuernummer 34-783/3935  ergangenen Bescheide des  FA Niederösterreich Mitte (nunmehr Dienststelle des Finanzamtes Österreich) vom 17. Februar 2020  betreffend Umsatz- und Einkommensteuer 2012 und 2013 beschlossen:  Die angefochtenen Bescheide vom 17. Februar 2020 betreffend Umsatz- und  Einkommensteuer 2012 und 2013 werden gemäß § 278 Abs. 1 BAO aufgehoben und das  Verfahren an die Abgabenbehörde zurückverwiesen.

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Camilla Tutschek` (person)
- `Karola Poepping` (person)
- `Gemeine Brongen 4, 9433 St. Jakob, Österreich` (address)
- `34-783/3935` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/141789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141789.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Larissa Weßeloh  in der Beschwerdesache der  Miri Ache, Gumitschstraße 143, 5163 Weikertsham, Österreich, vertreten durch Vertr-Bf, Vertr-Adr, über die Beschwerde vom  24. August 2018 gegen den Bescheid des FA Klagenfurt St. Veit Wolfsberg (jetzt Finanzamt Österreich) vom 24. Juli  2018 betreffend Forschungsprämie für das Jahr 2015, Steuernummer 62-612/4228, zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Larissa Weßeloh` (person)
- `Miri Ache` (organisation)
- `Gumitschstraße 143, 5163 Weikertsham, Österreich` (address)
- `62-612/4228` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Judith Brocks  in der Beschwerdesache des  VetR Stephanie Kabak, Zennergasse 325, 9360 Engelsdorf, Österreich, über die Beschwerde vom 12. Juli 2023 gegen den Bescheid des  FA Graz-Stadt  vom 21. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  zu Steuernummer 70-314/9067  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Dr.in Judith Brocks` (person)
- `VetR Stephanie Kabak` (person)
- `Zennergasse 325, 9360 Engelsdorf, Österreich` (address)
- `70-314/9067` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/143942.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143942.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Dr.in Abigail Radowan  in der Beschwerdesache der  Mathiessen Event, Rothböck-Straße 16, 9130 Kreuth, Österreich, über die Beschwerde vom 19. März 2021 gegen den zur  Steuernummer 51-888/5055  ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle  des FA Klagenfurt St. Veit Wolfsberg ) vom 25. August 2020 betreffend Einkommensteuer 2018 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Dr.in Dr.in Abigail Radowan` (person)
- `Mathiessen Event` (organisation)
- `Rothböck-Straße 16, 9130 Kreuth, Österreich` (address)
- `51-888/5055` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/144651.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144651.1_88`)


Aus einer vorgelegten Rechnung vom 18.8.2011 geht hervor, dass die FA Niederösterreich Mitte  eine Wartung  des Treppenlifts zu einem Gesamtbetrag von 266,40 Euro durchgeführt hat.

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/144830.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144830.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Alexander Kazenwadel  in der Beschwerdesache Eckard Langfeld,  Körpersportverein Oase 16, 5211 Friedburg, Österreich, über die Beschwerde vom 24. Dezember 2017 gegen den Bescheid des  FA Innsbruck  vom 15. Dezember 2017 betreffend Zahlungserleichterungen § 212 BAO 15.12.2017  Steuernummer 72-623/4945  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Hon.-Prof. Alexander Kazenwadel` (person)
- `Eckard Langfeld` (person)
- `Körpersportverein Oase 16, 5211 Friedburg, Österreich` (address)
- `72-623/4945` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/144851.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144851.1_13`)


Dem Fahrzeughalter, der FA Steiermark Mitte, wurde in der Folge ein Auftrag zur Lenkernennung erteilt  und anschließend das Verwaltungsstrafverfahren betreffend Parkometerabgabe gegen den  nunmehrigen Bf geführt.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/145179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dario Ribbeck  in der Beschwerdesache Otto Koschinski,  Stockham 43, 3334 Gaflenz, Österreich, vertreten durch Dr. Michael Kotschnigg, Stadlauer Straße 39/I/Top12, 1220  Wien, über die Beschwerde vom 13. Februar 2023 gegen den Bescheid über die Festsetzung  von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens des FA Wien 8/16/17  vom  11. Jänner 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Wien 8/16/17` | `FA Wien 8/16/17` |

**Missed by this rule (FN):**

- `Dr. Dario Ribbeck` (person)
- `Otto Koschinski` (person)
- `Stockham 43, 3334 Gaflenz, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/145184.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Eleonore Semenow  in der Beschwerdesache   Eva Zvirbulis, Ettingshausengasse 4, 9560 Waiern, Österreich,   über die Beschwerde vom 8. August 2023 gegen den Bescheid des FA Spittal Villach  vom 27. Juli 2023  zu Steuernummer 38-059/7614  betreffend Einkommensteuer 2021 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Spittal Villach` | `FA Spittal Villach` |

**Missed by this rule (FN):**

- `Dr.in Eleonore Semenow` (person)
- `Eva Zvirbulis` (person)
- `Ettingshausengasse 4, 9560 Waiern, Österreich` (address)
- `38-059/7614` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/145277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145277.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mirko Leinekugel  in der Beschwerdesache VetR Mike Schmädtke,  Koglreith 23, 5121 Haid, Österreich, betreffend die Beschwerde vom 5. März 2024 gegen die Zahlungsaufforderung  des FA Innsbruck  vom 23. Februar 2024 zu Steuernummer 39-704/8646  betreffend Gebühren  2022 in Höhe von 360,00 € beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA Innsbruck` | `FA Innsbruck` |

**Missed by this rule (FN):**

- `Univ.-Prof. Mirko Leinekugel` (person)
- `VetR Mike Schmädtke` (person)
- `Koglreith 23, 5121 Haid, Österreich` (address)
- `39-704/8646` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/145398.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145398.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wendelin Bönecke  in der Beschwerdesache Arnd Miesen,  Stadtwassergasse 62, 4753 Ellerbach bei Taiskirchen im Innkreis, Österreich, über die Beschwerde vom 26. März 2024 gegen den Bescheid des FA Steiermark Mitte  vom 25. März 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 37-029/2413  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Dr. Wendelin Bönecke` (person)
- `Arnd Miesen` (person)
- `Stadtwassergasse 62, 4753 Ellerbach bei Taiskirchen im Innkreis, Österreich` (address)
- `37-029/2413` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/145620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pascal Seyberth  in der Beschwerdesache Dorothea Bartelme,  Aiden 2, 4742 Schulterzucker, Österreich, Ungarn, über die Beschwerde vom 6. September 2023, eingelangt am  8. September 2023, gegen die Bescheide des FA Klagenfurt St. Veit Wolfsberg  vom 10. August 2023 und 28. August  2023 zu Steuernummer 72-223/9755, mit denen Anträge auf Durchführung der  Arbeitnehmerveranlagung für die Jahr 2019 bis 2021 zurückgewiesen wurden, zu Recht  erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Mag. Pascal Seyberth` (person)
- `Dorothea Bartelme` (person)
- `Aiden 2, 4742 Schulterzucker, Österreich` (address)
- `72-223/9755` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/146333.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146333.1_41`)


Es erübrigt sich daher, zum Antrag auf aufschiebende Wirkung eine Stellungnahme des  FA Klosterneuburg  einzuholen.

| Predicted | Gold |
|---|---|
| `FA Klosterneuburg` | `FA Klosterneuburg` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Elisabeth Buchholzer  in der Beschwerdesache Suleika Rohrmüller, LLM,  Lothringenstraße 19, 9360 Gaudritz, Österreich  über die Beschwerde vom 26. April 2024 gegen den Bescheid des FA Vorarlberg  vom 24. April 2024 über die Abweisung des Antrages vom 7.5.2023 auf Familienbeihilfe für den  Zeitraum ab 09.2022, Steuernummer 05-518/9371, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Vorarlberg` | `FA Vorarlberg` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Elisabeth Buchholzer` (person)
- `Suleika Rohrmüller, LLM` (person)
- `Lothringenstraße 19, 9360 Gaudritz, Österreich` (address)
- `05-518/9371` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/146868.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Ludger Günzkofer  in der Beschwerdesache Fiona Strübel,  Bruno-Kreisky-Weg 5, 8793 Treffning, Österreich, über die Beschwerde vom 30. Mai 2023 gegen den Bescheid des FA Schwechat Gerasdorf  vom 20. April 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017,  Steuernummer 04-913/7352, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Schwechat Gerasdorf` | `FA Schwechat Gerasdorf` |

**Missed by this rule (FN):**

- `Mag. Mag. Ludger Günzkofer` (person)
- `Fiona Strübel` (person)
- `Bruno-Kreisky-Weg 5, 8793 Treffning, Österreich` (address)
- `04-913/7352` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/148676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148676.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch die Richterin Mag. Julia Schlegl in der  Beschwerdesache Daphne Steigemann, Niedertrattnach 11, 2013 Göllersdorf, Österreich, betreffend die Beschwerde vom 6. März 2025  gegen die Mitteilung des FA Braunau Ried Schärding  vom 5. März 2025 betreffend den Bezug der  Differenzzahlung:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Missed by this rule (FN):**

- `Daphne Steigemann` (person)
- `Niedertrattnach 11, 2013 Göllersdorf, Österreich` (address)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jasmin Phillipps  in der Beschwerdesache Gloria Nannen,  Alling 11, 4694 Ohlsdorf, Österreich, über die Beschwerde vom 7. Dezember 2023 gegen den Bescheid des  FA Tirol Ost  vom 7. Dezember 2023 betreffend Mehrkindzuschlag aufgrund der Verhältnisse des  Jahres 2022 zu Steuernummer 16-991/4615  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Jasmin Phillipps` (person)
- `Gloria Nannen` (person)
- `Alling 11, 4694 Ohlsdorf, Österreich` (address)
- `16-991/4615` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_117`)


Der vom FA Tirol Ost  ergangene Aufhebungsbescheid besteht somit zu Recht, und es war der  Beschwerde kein Erfolg beschieden.

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_118`)


Ergänzend werden die Ausführungen der Beschwerdevorentscheidung des FA Tirol Ost  vom 19.  Dezember 2023 auch zum Inhalt dieses Erkenntnisses erhoben.

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/148789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148789.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Priv.-Doz. Siegmund Michelus  in der Beschwerdesache RgR Nadja Weitekamper,  Tschriet 5, 3653 Tottendorf, Österreich, über die Beschwerde vom 30. Dezember 2024  gegen den Bescheid des  FA Amstetten Melk Scheibbs  vom 9. Dezember 2024 über die Abweisung eines Zahlungserleichterungsansuchens,  Steuernummer 43-675/3632, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Amstetten Melk Scheibbs` | `FA Amstetten Melk Scheibbs` |

**Missed by this rule (FN):**

- `Univ.-Prof. Priv.-Doz. Siegmund Michelus` (person)
- `RgR Nadja Weitekamper` (person)
- `Tschriet 5, 3653 Tottendorf, Österreich` (address)
- `43-675/3632` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/148922.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148922.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Moses Vasylevskyy, Koralmblickweg 21, 3661 Lohsdorf, Österreich, vertreten durch Dr. Hugo Mlejnek  Wirtschaftstreuhand- gesellschaft m.b.H., Herrengasse 6-8/1/1, 1010 Wien, vom 28. April 2023  gegen den Bescheid des FA Steiermark Mitte  vom 11. April 2023 betreffend Säumniszuschlag 2023 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Missed by this rule (FN):**

- `Moses Vasylevskyy` (person)
- `Koralmblickweg 21, 3661 Lohsdorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_29`)


In den gegenständlichen Beschwerdeverfahren, die vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_35`)


In den gegenständlichen Beschwerdeverfahren, das vom FA Salzburg-Land dem BFG vorgelegt  worden waren, ist somit ab 01.01.2021 das FA Österreich zuständig.

**False Positives:**

- `FA Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/138464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138464.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Constantin Mosmüller  in der Angelegenheit der Parteien   Sean Spies (Beschwerdeführer), vertreten durch die Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH, 1010 Wien und    FA Freistadt Rohrbach Urfahr  als Amtspartei und Gesamtrechtsnachfolger des FA Wien 2/20/21/22 betreffend die  Beschwerde vom 25.9.2020               gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 25.8.2020 betreffend  Abweisung eines Antrages auf Aufhebung des Einkommensteuerbescheides 2017 vom  28.6.2019 gem. § 299 BAO   den Beschluss gefasst:  Der Vorlageantrag des Beschwerdeführers vom 23.8.2022 gegen die  Beschwerdevorentscheidung vom 21.7.2022 über die Beschwerde gegen den Bescheid vom  25.8.2020 über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides  2017 vom 28.6.2019 gem. § 299 BAO   wird als unzulässig zurückgewiesen.

**False Positives:**

- `FA Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof. Constantin Mosmüller`(person)
- `Sean Spies`(person)
- `FA Freistadt Rohrbach Urfahr`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_17`)


Verbindungsstelle hat Frau B ab 1.1.2012 bis laufend keine berufliche  Tätigkeit in Deutschland ausgeübt (lt. e-mail des FA Innsbruck v. 20.3.2014).

**False Positives:**

- `FA Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/145293.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145293.1_8`)


Voranzustellen ist, dass auf der Grundlage von Feststellungsbescheiden des FA Graz-Stadt  vom 24.05.2019 betreffend die XYOG, St.Nr.2, am 28.05.2019 gemäß § 295 Abs. 1 BAO  geänderte Einkommensteuerbescheide für die Jahre 2014 bis 2016 an die antragstellende  Partei ergingen.

**False Positives:**

- `FA Graz-Stadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/145885.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145885.1_3`)


Begründung  Mit Erkenntnis des Bundesfinanzgerichtes vom 02.08.2024, RV/7100602/2024, wurde die  Bescheidbeschwerde der Revisionswerberin vom 28.10.2003 gegen die Bescheide des FA Wien  8/16/17 vom 22.08.2003, betreffend Festsetzung Umsatzsteuer 10-11/2002, Festsetzung  Umsatzsteuer 1-4/2003, Festsetzung Umsatzsteuer 6/2003 und vom 18.09.2003, betreffend  Festsetzung Umsatzsteuer 7/2003, sowie gemäß § 253 BAO gegen die Bescheide des FA Wien  8/16/17 vom 05.10.2005 betreffend Umsatzsteuer 2002 und 2003 abgewiesen und die  Umsatzsteuerbescheide 2002 und 2003 zu Ungunsten der Revisionswerberin abgeändert.

**False Positives:**

- `FA Wien  8/16/17` — no gold match — likely missing annotation
- `FA Wien  8/16/17` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/148272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148272.1_73`)


Die Begründung des FA Graz-Stadt wonach im Jahre 2021 die Steuerberatungskosten verglichen  mit den Vorjahren angewachsen sind ist nicht nachvollziehbar.

**False Positives:**

- `FA Graz-Stadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Company Entities (GmbH/AG/KG)` 🏆

**F1:** 0.420 | **Precision:** 0.369 | **Recall:** 0.488  

**Format:** `regex`  
**Rule ID:** `70fb3657`  
**Description:**
Matches company names with suffixes GmbH, AG, KG, excluding context words like Firma/Unternehmens and handling Fa. prefixes.

**Content:**
```
(?<![a-zA-Z])(?<!Firma\s)(?<!Unternehmens\s)(?<!Arbeitgeber\s)(?<!Seitens\s)(?<!\w)(?:Fa\.)?([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\-\+\&]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\-\+\&]+)*\s+(?:GmbH|KG|AG))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.369 | 0.488 | 0.420 | 1792 | 661 | 1131 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 661 | 1131 | 693 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_8`)


Entscheidungsgründe Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg vom 8. Juni 2016, SpS 16, wurde Herr J. (in weiterer Folge: Beschuldigter), geb., österreichischer Staatsbürger, Geschäftsführer, aufhältig in Adr.Wien****, in Abwesenheit schuldig erkannt, er habe im Bereich des Finanzamtes Wien 1/23 als für die Wahrnehmung der abgabenrechtlichen Obliegenheiten der Derber-Robotik GmbH vorsätzlich a) durch die verspätete Abgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Anzeige- ‚ Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von € 2.403,50 zu verkürzen versucht, b) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2014, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2014 in Höhe von € 11.919,91 zu verkürzen versucht, c) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG entsprechenden Voranmeldungen Verkürzungen von Vorauszahlungen an Umsatzsteuer für 02/2015 in Höhe von € 520,51, 04 – 05 /2015 in Höhe von € 3.814,30 bewirkt, wobei er den Eintritt der Verkürzungen nicht nur für möglich, sondern für gewiss gehalten habe, d) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

| Predicted | Gold |
|---|---|
| `Derber-Robotik GmbH` | `Derber-Robotik GmbH` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_15`)


Seit dem 31.08.2001 ist er für die Wahrnehmung der abgabenrechtlichen Obliegenheiten verantwortlicher Geschäftsführer der im Firmenbuch unter FN erfassten Derber-Robotik GmbH  Mit Beschluss des HG Wien wurde über das Vermögen der Gesellschaft das Konkursverfahren eröffnet.

| Predicted | Gold |
|---|---|
| `Derber-Robotik GmbH` | `Derber-Robotik GmbH` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_67`)


Ende 10:40 h Die Insolvenz der Derber-Robotik GmbH wurde deshalb erforderlich, da die Derber-Robotik GmbH& Co KG bereits seit Datum***** im Konkurs war und die Haftungen daraus den Konkurs der gegenständlichen Gesellschaft erzwungen hat.

| Predicted | Gold |
|---|---|
| `Derber-Robotik GmbH` | `Derber-Robotik GmbH` |

**Missed by this rule (FN):**

- `Derber-Robotik GmbH&` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_121`)


Die entsprechenden Beträge sind aus dem Dienstgeber - Lohnkonto 2015 der Derber-Robotik GmbH eindeutig nachvollziehbar und können daher als objektive Grundlage für das weitere Verfahren herangezogen werden.

| Predicted | Gold |
|---|---|
| `Derber-Robotik GmbH` | `Derber-Robotik GmbH` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_3`)


I. Zugrundeliegender Sachverhalt und Verfahrensgang Strittig erwies sich in der gegenständlichen Beschwerdesache, ob zwischen den Vertragsparteien eine der Bestandvertragsgebühr unterliegende Option oder ein gebührenrechtlich nicht steuerbarer Vorvertrag vereinbart wurde: Die Beschwerdeführerin schloss als Bestandnehmerin mit der Hötzel Lebensmittel GmbH  als Bestandgeberin den mit 14.9.2019 datieren schriftlichen Pachtvertrag über eine Geschäftsräumlichkeit (Betrieb einer Apotheke) ab.

| Predicted | Gold |
|---|---|
| `Hötzel Lebensmittel GmbH` | `Hötzel Lebensmittel GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Silvestri Bau GmbH` | `Silvestri Bau GmbH` |

**Missed by this rule (FN):**

- `Priv.-Doz.in DDr.in Rafaela Ringart` (person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich` (address)
- `38-663/2876` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_13`)


3. a. Am 28. Mai 2010 wurde ein Ergänzungsersuchen des Finanzamtes an ER versandt:  (1) Am ****2006 sei über das Vermögen der WaldVersicherung KG das Konkursverfahren eröffnet worden.

| Predicted | Gold |
|---|---|
| `WaldVersicherung KG` | `WaldVersicherung KG` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_20`)


(3) Mit Schreiben vom 16. Juni 2010 gab ER bekannt, dass nach seinem Wissensstand nach  dem 31.12.2005 keine Einlagen und Entnahmen in der WaldVersicherung KG durchgeführt worden seien.

| Predicted | Gold |
|---|---|
| `WaldVersicherung KG` | `WaldVersicherung KG` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_44`)


Am ****2006 sei über das Vermögen der WaldVersicherung KG das Konkursverfahren eröffnet worden.

| Predicted | Gold |
|---|---|
| `WaldVersicherung KG` | `WaldVersicherung KG` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_196`)


b. Schreiben des KommR Stephanie Stickling an das Finanzamt zum Konkurs der Bf. vom 6. Juli 2010:  Ich beziehe mich auf das Telefonat vom 5. Juli 2010 und gestatte festzuhalten, dass das  Konkursverfahren über das Vermögen der WaldVersicherung KG nach der Verteilung aufgehoben worden ist.

| Predicted | Gold |
|---|---|
| `WaldVersicherung KG` | `WaldVersicherung KG` |

**Missed by this rule (FN):**

- `KommR Stephanie Stickling` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_200`)


c. Antwortschreiben des Masseverwalters der WaldVersicherung KG vom 4. September 2006 auf das Schreiben  des Finanzamtes vom 4. August 2006 zur Abgabenfestsetzung im Konkurs (Auszug):  12 von 20 Seite 13 von 20

| Predicted | Gold |
|---|---|
| `WaldVersicherung KG` | `WaldVersicherung KG` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_5`)


12.2015 wurde zwischen der See Wilbach Dienstleistungen GmbH als Verpächterin und Hrn. K sowie der Vincent und Zielinska Solar GmbH  als Pächter (= Bf) ein Pachtvertrag mit auszugsweise folgendem Inhalt abgeschlossen:     "Definitionen

| Predicted | Gold |
|---|---|
| `See Wilbach Dienstleistungen GmbH` | `See Wilbach Dienstleistungen GmbH` |

**Missed by this rule (FN):**

- `Vincent und Zielinska Solar GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Missed by this rule (FN):**

- `Spies&Wickert Solar GmbH€` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_95`)


Am 29.11.2012 wurde die Spies&Wickert Solar GmbH infolge rechtskräftiger Nichteröffnung eines  Insolvenzverfahrens mangels kostendeckenden Vermögens und Zahlungsunfähigkeit aufgelöst.

| Predicted | Gold |
|---|---|
| `Spies&Wickert Solar GmbH` | `Spies&Wickert Solar GmbH` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129437.1_35`)


Er bezog im Jahr 2017 Pensionszahlungen von der  Deutschen Rentenversicherung Bund in A (Deutschland) in Höhe von EUR 18.333,- und  Firmenpensionszahlungen von der Werkzorkraft-Solar AG in A (Deutschland) in Höhe von EUR 22.279,98.

| Predicted | Gold |
|---|---|
| `Werkzorkraft-Solar AG` | `Werkzorkraft-Solar AG` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129437.1_45`)


Zwischen den Verfahrensparteien ist unstrittig, dass die von der Werkzorkraft-Solar AG erhaltenen Bezüge solche  im Sinn des Art. 18 Abs. 1 DBA-Deutschland sind und daher der Besteuerung in Österreich  unterliegen.

| Predicted | Gold |
|---|---|
| `Werkzorkraft-Solar AG` | `Werkzorkraft-Solar AG` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_5`)


Verfahrensverlauf  Mir Haftungsvorhalt vom 1. Oktober 2014 teilte die belangte Behörde der Beschwerdeführerin  (in der Folge Bf) mit, dass beabsichtigt sei, sie für diverse Abgabenschuldigkeiten  (Umsatzsteuer, Körperschaftsteuer, Lohnsteuer, Dienstgeberbeitrag samt Zuschlag sowie  Nebenansprüche) betreffend den Zeitraum 2012 bis 2013 der Garten Taltralex GmbH (in der Folge  Gesellschaft), deren Geschäftsführerin die Bf gewesen sei, im Gesamtausmaß von 37.817,42  Euro als Haftungsverpflichtete in Anspruch zu nehmen.

| Predicted | Gold |
|---|---|
| `Garten Taltralex GmbH` | `Garten Taltralex GmbH` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_94`)


Die Bf war seit Gründung der Garten Taltralex GmbH Alleingesellschafterin und alleinige Geschäftsführerin  der Gesellschaft.

| Predicted | Gold |
|---|---|
| `Garten Taltralex GmbH` | `Garten Taltralex GmbH` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Baden Mödling als Finanzstrafbehörde vom 12. April 2018, SpS 18, , Strafnummer  001 ff, 002 ff, wurde in den Finanzstrafsachen gegen   1. A B Geschäftsführer, wohnhaft in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  2. C B Geschäftsführerin, wohnhaft in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  3. V1 als belangter Verband, mit Sitz in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  4.Lexlog Automotive GmbH als belangter Verband, mit Sitz in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  zu Recht erkannt:   A B, die V1 und die Lexlog Automotive GmbH sind schuldig, es haben im Bereich des Finanzamtes Baden Mödling  grob fahrlässig  1) A B   I) als Geschäftsführer der Firma V1  a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter  Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bescheidmäßig  festzusetzende Abgaben, nämlich    2011 2012 2013 2014 2015 Summe  Umsatzsteuer iHv 2.619,96 8.934,65 300,00 437,00 450,00 € 12.741,61  Köst iHv 1.500,59 10.337,20 7.250,00 3.796,88 562,50 € 21.447,30  Summe in € 4.120,55 19.271,85 7.550,00 4.233,88 1.012,50 € 36.188.78  verkürzt, sowie  b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden  Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen  Offenlegungs- und Wahrheitspﬂicht, Verkürzung an  Kapitalertragsteuer 2012 in der Höhe von € 1.440,63  2013 in der Höhe von € 9.765,69  2014 in der Höhe von € 5.207,81  2015 in der Höhe von € 899,91  insgesamt somit € 17.312,04 bewirkt.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Missed by this rule (FN):**

- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich` (address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich` (address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich` (address)
- `4.Lexlog Automotive GmbH` (organisation)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_16`)


Als Begründung wurde ausgeführt:  [...]  C B ist im Firmenbuch im Raume des Finanzamtes Baden Mödling ebenso als Geschäftsführerin  der Lexlog Automotive GmbH eingetragen.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_19`)


Die ursprüngliche Lexlog Automotive GmbH wurde 1993 gegründet und 2013 in V1 umbenannt.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_20`)


Die  ursprüngliche V1 wurde 2011 gegründet und wurde im Jahr 2013 in die Lexlog Automotive GmbH umbenannt.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_21`)


Der operative Betrieb ist in der Lexlog Automotive GmbH angesiedelt.  5 von 17 Seite 6 von 17

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_37`)


A B handelte dabei  ungewöhnlich auffallend sorgfaltswidrig und waren die dadurch entstanden  Abgabenverkürzungen für ihn geradezu wahrscheinlich vorhersehbar, ein korrektes Vorgehen  war dem Beschuldigten angesichts seiner langjährigen Unternehmenseigenschaft als  Geschäftsführer der V1 und Lexlog Automotive GmbH zumutbar.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_40`)


Für die beiden Verbände und V1 und Lexlog Automotive GmbH hat jeweils der Geschäftsführer A B die Verantwortung der Abgabenverkürzungen zu  übernehmen und waren diese Verbände wie im Spruch auch entsprechend zu verurteilen.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_44`)


Der Senat beachtete dabei auch die  vollständige Schadensgutmachung und war aufgrund der Angaben des Verteidigers dessen  Verantwortung für A B und den Verbänden V1 und Lexlog Automotive GmbH als glaubwürdig den Feststellungen  zu Grunde zu legen, wodurch auf die Vernehmung der beiden Beschuldigten und der Zeugen  verzichtet werden konnte und somit ein Vertrauensvorschuss von Seiten des Senates dem  Verteidiger und den Beschuldigten gewährt wurde.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_67`)


Bei der V1 und der Lexlog Automotive GmbH wertete der Spruchsenat mildernd: das Geständnis, die  Unbescholtenheit, die Schadensgutmachung und die Bestrafung des Geschäftsführers,  erschwerend: keinen Umstand.

| Predicted | Gold |
|---|---|
| `Lexlog Automotive GmbH` | `Lexlog Automotive GmbH` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_54`)


In den  Bescheiden für Juni 2010 und August 2010 wurde zusätzlich das Ergebnis der Betriebsprüfung  der Heynoldt Finanzen AG (fortan Heynoldt Finanzen AG  vom 03.08.2017, Zl: 555 angeführt.

| Predicted | Gold |
|---|---|
| `Heynoldt Finanzen AG` | `Heynoldt Finanzen AG` |
| `Heynoldt Finanzen AG` | `Heynoldt Finanzen AG` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_75`)


Die Abgabenbehörde habe bei diversen Luftfahrtunternehmen (insbesondere bei der Heynoldt Finanzen AG bei  der R , als Rechtsvorgängerin der L, sowie der  I) Nachschauen gepflogen;

| Predicted | Gold |
|---|---|
| `Heynoldt Finanzen AG` | `Heynoldt Finanzen AG` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_86`)


Bereits im erstinstanzlichen Beschwerdeverfahren seien von der Wilkellem KI GmbH (fortan Wilkellem KI GmbH  der  V GmbH (Fortan V GmbH) sowie der M G.m.b.H., Nachweise für das Vorliegen der  Voraussetzungen nach § 4 Abs.1 Z 1 MinStG, bei von ihnen durchgeführten Flügen, beigebracht  worden, die aber in den Beschwerdevorentscheidungen keinen Einlass gefunden hätten.

| Predicted | Gold |
|---|---|
| `Wilkellem KI GmbH` | `Wilkellem KI GmbH` |
| `Wilkellem KI GmbH` | `Wilkellem KI GmbH` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_114`)


Die, in den bekämpften Bescheiden  angeführten Niederschriften und Prüfberichte, betreffend die J GmbH und die Lexost Daten GmbH samt  Anlagen seien der Bf. mit Schreiben vom 11.04.2018 übermittelt worden.

| Predicted | Gold |
|---|---|
| `Lexost Daten GmbH` | `Lexost Daten GmbH` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_115`)


Ebenso seien der Bf.  mit diesem Schreiben die Niederschrift und der Prüfbericht samt Anlagen, betreffend die Heynoldt Finanzen AG  zugekommen, welche die belangte Behörde in den Bescheiden, betreffend die Festsetzung der  Mineralölsteuer für Juni und August 2010, als Luftfahrtunternehmen erwähnt hatte.

| Predicted | Gold |
|---|---|
| `Heynoldt Finanzen AG` | `Heynoldt Finanzen AG` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_130`)


Die von der V GmbH und der Wilkellem KI GmbH vorgelegten Beweismittel seien unzulänglich, da es sich  dabei nur um Rechnungen und nicht auch um Auszüge aus den Tech- Logs gehandelt habe.

| Predicted | Gold |
|---|---|
| `Wilkellem KI GmbH` | `Wilkellem KI GmbH` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_309`)


Dagegen können die, von der V GmbH und der Wilkellem KI GmbH  vorgelegten, Rechnungen über die Durchführung von Flügen, alleine für sich nicht als geeignete  Nachweise für die Rechtmäßigkeit der Gewährung der in Rede stehenden Steuerbefreiung  angesehen werden.

| Predicted | Gold |
|---|---|
| `Wilkellem KI GmbH` | `Wilkellem KI GmbH` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_7`)


Die Prüferin traf im Bericht über das Ergebnis der Außenprüfung folgende  beschwerdegegenständliche Feststellung:   Tz. 1 Scheinrechnungen Nord Willexlex GmbH [im Folgenden: D.GmbH]  Die Leistungen der Nord Willexlex GmbH an die Bf. wurden nicht von dieser Firma erbracht, sondern von  J.N. [im Folgenden: J.N.], der den Mantel der Nord Willexlex GmbH mit Einverständnis seines Onkels FN  benutzt hat.

| Predicted | Gold |
|---|---|
| `Nord Willexlex GmbH` | `Nord Willexlex GmbH` |
| `Nord Willexlex GmbH` | `Nord Willexlex GmbH` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_19`)


Den Erhebungen der BP nach hat J.N. die Baustellen von X auf eigene Rechnung geführt und  dabei den Mantel der Nord Willexlex GmbH benützt.

| Predicted | Gold |
|---|---|
| `Nord Willexlex GmbH` | `Nord Willexlex GmbH` |

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_20`)


Bezüglich der Rechnungen der Nord Willexlex GmbH an die 3 Firmen von X ist J.N. als deren faktischer  Machthaber zu betrachten.

| Predicted | Gold |
|---|---|
| `Nord Willexlex GmbH` | `Nord Willexlex GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/125056.1`) (sent_id: `deanon_BFG_20260814_TRAIN/125056.1_67`)


Ende 10:40 h Die Insolvenz der Derber-Robotik GmbH wurde deshalb erforderlich, da die Derber-Robotik GmbH& Co KG bereits seit Datum***** im Konkurs war und die Haftungen daraus den Konkurs der gegenständlichen Gesellschaft erzwungen hat.

**False Positives:**

- `Derber-Robotik GmbH& Co KG` — similar text (different position): `Derber-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber-Robotik GmbH`(organisation)
- `Derber-Robotik GmbH&`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Jank Weiler Operenyi Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zeno Matyssek`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_14`)


Die Beschwerdeführerin ist in der B & Co GmbH als kaufmännische Angestellte im  Arbeitsbereich Leitung Expedit und Lager beschäftigt und gleichzeitig als  Gefahrengutbeauftragte tätig.

**False Positives:**

- `Co GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_97`)


Wenn der  Beschwerdeführer von einer geringfügigen Anstellung spricht, sei er an seine Tätigkeit bei der  XY Gaststättenbetriebs GmbH erinnert, wo er auch nur von fallweisen geringfügigen Tätigkeiten  spricht, die aber bei dem Saisonbetrieb 2011 (1.4.-31.10.2011) immerhin mit brutto € 12.703,99  entlohnt wurden (laut Selbstanzeige der Arbeitgeberin, wofür diese Lohnabgaben und  Sozialversicherungsbeiträge nachzahlen musste).“

**False Positives:**

- `XY Gaststättenbetriebs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_61`)


Der BF war im Zeitraum 09/2008 - 04/2011 als Lkw-Fahrer bei der GmbH (in der Folge GmbH)  beschäftigt.

**False Positives:**

- `Folge GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_72`)


Der GmbH wurden vom FA im Zuge von Prüfungshandlungen bis Dezember 2010  Umsatzsteuern in Gesamthöhe von ca. € 1,9 Mio aufgrund von Umsatzsteuerhinterziehungen  im Zusammenhang mit Heizölverkäufen vorgeschrieben.

**False Positives:**

- `Der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_3`)


Der Beschwerde wird teilweise stattgegeben und der Beschwerdeführer für folgende Abgaben  als Geschäftsführer der AlpenMonwilderSoftware GmbH GmbH in Anspruch genommen:    Umsatzsteuer 10/2017 170,46  Umsatzsteuer 11/2017 4.559,13  Lohnsteuer 11/2017 1.005,18  Lohnsteuer 01/2018 147,92  Dienstgeberbeitrag (DB) 11/2017 693,46  Dienstgeberbeitrag 12/2017 48,42  Dienstgeberbeitrag 01/2018 66,92  Zuschlag zum DB (DZ) 11/2017 44,90  Zuschlag zum DB (DZ) 01/2018 5,80  Körperschaftsteuer 01-03/2018 117,88    6.860,07

**False Positives:**

- `AlpenMonwilderSoftware GmbH GmbH` — partial — gold is substring of pred: `AlpenMonwilderSoftware GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `AlpenMonwilderSoftware GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Cornelia Pranckaitis, Petersbergweg 142, 4212 Steigersdorf, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

**False Positives:**

- `Unternehmensberatungs GmbH` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Cornelia Pranckaitis`(person)
- `Petersbergweg 142, 4212 Steigersdorf, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Mercuria Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oleg Kreissl`(person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_33`)


Über dessen BM GmbH und über sein eigenes Vermögen seien 2008 und 2010  Konkursverfahren eröffnet worden.

**False Positives:**

- `BM GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Zielinska Solar GmbH` — partial — pred is substring of gold: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_2`)


Salzburg Steuerberatung und Wirtschaftsprüfung  GmbH, Mildenburggasse 4A, 5020 Salzburg, über die Beschwerde vom 6. Februar 2020 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 15. Jänner  2020 betreffend Gebühren zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wirtschaftsprüfung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_5`)


12.2015 wurde zwischen der See Wilbach Dienstleistungen GmbH als Verpächterin und Hrn. K sowie der Vincent und Zielinska Solar GmbH  als Pächter (= Bf) ein Pachtvertrag mit auszugsweise folgendem Inhalt abgeschlossen:     "Definitionen

**False Positives:**

- `Zielinska Solar GmbH` — partial — pred is substring of gold: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See Wilbach Dienstleistungen GmbH`(organisation)
- `Vincent und Zielinska Solar GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_35`)


In diesem Ausgabenbetrag seien Fremdleistungen von zwei Subunternehmen enthalten:  1.) Rechnungen der Firma C Bau GmbH € 228.630,13  2.)

**False Positives:**

- `Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_48`)


Die vom Bf. vorgelegten Unterlagen wurden seitens des Bundesfinanzgerichts dem Finanzamt  zur Stellungnahme übermittelt.  In der Stellungnahme führte das Finanzamt aus, dass die Firma Spies&Wickert Solar GmbH geprüft worden sei  und die UIDNR.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_51`)


Im Zuge einer Betriebsprüfung in einem  anderen Unternehmen seien die Rechnungen der Firma Spies&Wickert Solar GmbH überprüft und als  Scheinrechnungen beurteilt worden.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_54`)


Alle Erhebungen der Betriebsprüfung hätten ergeben, dass die Firma Spies&Wickert Solar GmbH nur dazu diene,  Scheinrechnungen zu ermöglichen.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_58`)


Ergänzend legte das Finanzamt Teile des Betriebsprüfungsberichtes betreffend die Firma Spies&Wickert Solar GmbH in Ablichtung vor.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_60`)


Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma Spies&Wickert Solar GmbH führte der Bf. aus, dass am 29.11.2012 der Konkurs über das  Vermögen dieser Firma eröffnet und mangels Masse abgelehnt worden sei.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_62`)


es sei lediglich der Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma Ch angezweifelt worden.

**False Positives:**

- `Subunternehmern Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_88`)


Firma Spies&Wickert Solar GmbH€ 228.630,13  b.) Firma Ch G € 10.514,-  Bezüglich der Fremdleistungen der Firma Spies&Wickert Solar GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der Spies&Wickert Solar GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — positional overlap with gold: `Spies&Wickert Solar GmbH€`
- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH€`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)
- `Spies&Wickert Solar GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_96`)


Die UID Nummer der Firma Spies&Wickert Solar GmbH war laut Finanzamtsunterlagen mit 15.8.2012 begrenzt.

**False Positives:**

- `Firma Spies&Wickert Solar GmbH` — partial — gold is substring of pred: `Spies&Wickert Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `ICON Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_155`)


Diese Anknüpfung ziele nicht auf eine unterschiedliche Behandlung von  Abfertigungen (hier Vorstandsmitglieder AG und Geschäftsführer GmbH) ab, sondern enthalte  den Grundgedanken, dass Abfertigungen, die nicht zwingend seien, sondern individualrechtlich  vereinbart würden und damit im Gestaltungsspielraum des Unternehmers lägen, nur mehr  beschränkt zum Betriebsausgabenabzug zugelassen seien.

**False Positives:**

- `Vorstandsmitglieder AG` — no gold match — likely missing annotation
- `Geschäftsführer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_161`)


Wie im konkreten Fall der vorangehend geschilderten  VfGH-Rspr (mit dem Gegensatz Vorstand AG und Geschäftsführer GmbH), ist auch im  vorliegenden Fall nicht auf etwaige Unterschiede in der Zielgruppe von § 67 Abs 6 und Abs 8 lit  f EStG abzustellen, sondern auf den Unterschied zwischen freiwilligen und zwingenden  Abfertigungen.

**False Positives:**

- `Gegensatz Vorstand AG` — no gold match — likely missing annotation
- `Geschäftsführer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Partner  KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vivian Malek`(person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `DI Heinrich Richter Steuerberatungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Thomas Kreul`(person)
- `Preberstraße 4, 3911 Dietharts, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_21`)


Die Methode bzw. Vorgangsweise wurde wie folgt beschrieben:  Ad 1) die Erstellung von Unterlagen durch die Ferro Montagetechnik GmbH (i.d.F. FMT) nach  eigenen Vorgaben und Erkenntnissen der von der Güssing Energie Technologies (i.d.F. GET)  erzeugten Pilotanlage und den damit erzielten Ergebnissen;

**False Positives:**

- `Ferro Montagetechnik GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_5`)


Entscheidungsgründe  Mit Schreiben vom 28 April 2014 zeigte die Verpächterin, die Fr. GmbH den Pachtvertrag vom  23.04.2014, abgeschlossen zwischen ihr und der S1.2 Gesellschaft m.b.H. & Co KG (im  Folgenden: KG), für das Pachtobjekt (Restaurantbetrieb), mit dem Ersuchen um Vergebührung  an.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_35`)


Im Jahr 2016 änderte sich die gesellschaftsrechtliche Situation der Beschwerdeführerin, der  S1.2 Gesellschaft m.b.H. & Co KG, wie folgt:  S1.2 Gesellschaft m.b.H.:  Mit Umwandlungsvertrag gemäß § 2 UmwG vom 23.05.2016, abgeschlossen zwischen der S1.2  Gesellschaft m.b.H. als übertragende Gesellschaft einerseits und F.K S1.2 als einzigen  übernehmenden Gesellschafter, hat die GmbH ihr gesamtes Vermögen als Ganzes mit allen  Rechten und Pflichten auf den einzig übernehmenden Gesellschafter übertragen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_39`)


Mit der Umwandlung der S1.2 Gesellschaft m.b.H. auf F.K S1.2 e.U. wurden sämtliche Anteile  an der S1.2 Gesellschaft m.b.H. & Co KG vereinigt, und ging sämtliches Vermögen der KG  (somit auch der Restaurantbetrieb Co KG) durch Anwachsung auf den einzig verbliebenen  Gesellschafter F.K S1.2 über.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Restaurantbetrieb Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_40`)


Am 18.06.2016 wurde das Vermögen gemäß § 142 UGB durch Herrn F.K S1.2 e.U.  übernommen (FN n123r k); die S1.2 Gesellschaft m.b.H & Co KG aufgelöst und im Firmenbuch  gelöscht.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_41`)


Die KG ist somit ab 18.06.2016 vermögenslos.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_61`)


Die KG verpflichtete  sich, auf ihre Kosten während der gesamten Dauer eine Pachtzinsversicherung  (Betriebsunterbrechungsversicherung) und eine Allgefahrenversicherung abzuschließen.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130561.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130561.1_76`)


Die KG hat mit gesondertem Vertrag das  Restaurant und gegebenenfalls dessen Einrichtung zu pachten (§ 4 Pflichten des  Franchisenehmers 1).

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_90`)


Über die Beschwerde wurde erwogen:    Entscheidungsrelevanter Sachverhalt  Die Garten Taltralex GmbH wurde mit Errichtungserklärung vom 23. April 2007 gegründet und am 24. Mai  2007 unter der Firmenbuchnummer xxxxxxy im Firmenbuch eingetragen.

**False Positives:**

- `Entscheidungsrelevanter Sachverhalt  Die Garten Taltralex GmbH` — partial — gold is substring of pred: `Garten Taltralex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Garten Taltralex GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  2. [...], Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  3. [...]., Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `BKS Steuerberatungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Baden Mödling als Finanzstrafbehörde vom 12. April 2018, SpS 18, , Strafnummer  001 ff, 002 ff, wurde in den Finanzstrafsachen gegen   1. A B Geschäftsführer, wohnhaft in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  2. C B Geschäftsführerin, wohnhaft in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  3. V1 als belangter Verband, mit Sitz in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  4.Lexlog Automotive GmbH als belangter Verband, mit Sitz in Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich  zu Recht erkannt:   A B, die V1 und die Lexlog Automotive GmbH sind schuldig, es haben im Bereich des Finanzamtes Baden Mödling  grob fahrlässig  1) A B   I) als Geschäftsführer der Firma V1  a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter  Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bescheidmäßig  festzusetzende Abgaben, nämlich    2011 2012 2013 2014 2015 Summe  Umsatzsteuer iHv 2.619,96 8.934,65 300,00 437,00 450,00 € 12.741,61  Köst iHv 1.500,59 10.337,20 7.250,00 3.796,88 562,50 € 21.447,30  Summe in € 4.120,55 19.271,85 7.550,00 4.233,88 1.012,50 € 36.188.78  verkürzt, sowie  b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden  Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen  Offenlegungs- und Wahrheitspﬂicht, Verkürzung an  Kapitalertragsteuer 2012 in der Höhe von € 1.440,63  2013 in der Höhe von € 9.765,69  2014 in der Höhe von € 5.207,81  2015 in der Höhe von € 899,91  insgesamt somit € 17.312,04 bewirkt.

**False Positives:**

- `Lexlog Automotive GmbH` — similar text (different position): `4.Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `4.Lexlog Automotive GmbH`(organisation)
- `Franz Kranebitter-Straße 69, 4794 Ruholding, Österreich`(address)
- `Lexlog Automotive GmbH`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_5`)


II) als Geschäftsführer der Firma Lexlog Automotive GmbH  a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter  Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspﬂicht bescheidmäßig  festzusetzende Abgaben, nämlich    2013 2014 2015 Summe  Umsatzsteuer iHv 1.309,98 541,53 727,11 € 2.578,52  Köst iHv 2.551,33 1.220,16 1.625,70 € 5.397,19  Summe in €       € 7.975,71  verkürzt, sowie  b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden  Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen  Offenlegungs- und Wahrheitspﬂicht, Verkürzung an   Kapitalertragsteuer 2013 in der Höhe von € 927,71  2014 in der Höhe von € 934,37  2015 in der Höhe von € 1.197,31  insgesamt somit € 3.059,38 bewirkt.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_12`)


3) die Firma Lexlog Automotive GmbH durch A B als Entscheidungsträger im Sinne des § 2 Abs. 1 VbVG iVm § 28a  FinStrG zu Gunsten des Verbandes unter Verletzung den Verband treffender Verpﬂichtungen  a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter  Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspﬂicht bescheidmäßig  festzusetzende Abgaben, nämlich  4 von 17 Seite 5 von 17

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_14`)


Summe der Verkürzungen betreffend B GmbH: € 11.035,09  Die Firma Lexlog Automotive GmbH hat hiedurch das Finanzvergehen der grob fahrlässigen Abgabenverkürzung  nach § 34 Abs. 1 FinStrG iVm. § 28a Abs. 2 FinStrG iVm. § 3 Abs. 2 VbVG begangen und wird  hiefür nach § 34 Abs. 3 FinStrG iVm. § 3 Abs. 2 VbVG zu einer Geldbuße in der Höhe von €  1.500,-- (in Worten: Tausendfünfhundert Euro) verurteilt.   Gemäß dem § 185 Abs. 1 lit. a FinStrG hat die Firma Lexlog Automotive GmbH die Kosten des Verfahrens in Höhe  von € 150,-- zu ersetzen.

**False Positives:**

- `Die Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`
- `Firma Lexlog Automotive GmbH` — similar text (different position): `Lexlog Automotive GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)
- `Lexlog Automotive GmbH`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_17`)


Betriebsgegenstand der Firma Lexlog Automotive GmbH ist der Handel mit Kunststoff.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_27`)


Mit Prüfungsbericht vom 23.3.2017 wurde ebenfalls bei der Firma Lexlog Automotive GmbH für die Jahre 2013  bis 2015 die Betriebsprüfung abgeschlossen.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_34`)


Das steuerliche  Fehlverhalten bzgl. der ÖBB-Reisegutscheine wurde daher aufgrund des glaubwürdigen Irrtums  des Steuerberaters als nicht strafrechtlich relevant anerkannt und waren diese aus den  Berechnungen des strafbestimmenden Wertbetrages abzuziehen, und wurde dieser betreffend  Körperschaftsteuer 2015 bei der Firma Lexlog Automotive GmbH entsprechend gekürzt auf € 1.625,70, statt €  3.625,70.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_36`)


II) als Geschäftsführer der Firma Lexlog Automotive GmbH unter Verletzung der abgabenrechtlichen Anzeige-,  Offenlegungs- und Wahrheitspﬂicht bescheidmäßig festzusetzende Abgaben,  1) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, nämlich  Verkürzungen von Umsatzsteuer und Körperschaftsteuer für 2015 in der Gesamtsumme von €  7.975,71, sowie  2) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 (3) EStG entsprechend  Kapitalertragsteueranmeldungen Verkürzungen an Kapitalertragsteuer von 2013 bis 2015 in  der Gesamthöhe von € 3.059,9  jeweils bewirkt und somit das im Spruch genannte Fehlverhalten begangen.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_39`)


Nicht festgestellt werden konnte, dass C B für die Firma Lexlog Automotive GmbH Abgabenverkürzungen, wie in  den Anlastungen genannt, grob fahrlässig begangen hat.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_61`)


Im vorliegenden Fall war bezüglich A B von einem gesamtstrafbestimmenden Wertbetrag in  der Höhe von € 64.535,91 auszugehen, bei der Firma Lexlog Automotive GmbH von einem strafbestimmenden  Wertbetrag von € 11.035,09 und bei der Firma V1 von einem strafbestimmenden Wertbetrag  von € 53.500,82.

**False Positives:**

- `Firma Lexlog Automotive GmbH` — partial — gold is substring of pred: `Lexlog Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexlog Automotive GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130834.1_75`)


Erkenntnis wurde der Geschäftsführer A B gemäß § 34 Abs 1 FinStrG mit einer  Geldstrafe von EUR 10.000,00 zzgl. Kostenersatz von EUR 500,00 bestraft (im NEF GmbH  Geldstrafe 25 Tage Ersatzfreiheitsstrafe).

**False Positives:**

- `NEF GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130909.1_10`)


In der Bescheidbegründung wurde ausgeführt:  Die Kanalanschlussgebühren, Wasseranschlussgebühren, Strom-Energie AG Anschlusskosten,  Kosten für die Verlegung der 30-KV Starkstromleitung der Energie AG und die Netzbereit- stellungsgebühr i.H.v. gesamt € 27.423,95 stellen keine Anschaffungsnebenkosten von Grund  und Boden dar, sondern sind aufgrund der Gebäudeerrichtung als Herstellungsnebenkosten des  Gebäudes zu qualifizieren (Urtz (Hg.)

**False Positives:**

- `Strom-Energie AG` — no gold match — likely missing annotation
- `Energie AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_3`)


Entscheidungsgründe  Am 3.April 2015 wurde zwischen der Bf., als Mieterin, und der V, als Vermieterin, ein  Mietvertrag über die Anmietung von Büroflächen, in dem, im Eigentum der Vermieterin  stehenden Büro-und Geschäftsgebäude der Liegenschaft KG bbb, BG Innere Stadt Wien,  (Adresse:  ccc) abgeschlossen.

**False Positives:**

- `Liegenschaft KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Astoria Steuerberatung GmbH` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131064.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131064.1_91`)


Graz GmbH am Standort Ort1 (5 Monate, Fitnesscenter,  steuerpflichtige Bezüge von EUR 5.944,51)  • 21.10.-31.12.2013: C.K., Ort1 (geringfügig, 74 Tage, Fitnesscenter, steuerpflichtige  Bezüge von EUR 381,60)

**False Positives:**

- `Graz GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_18`)


Weiters wurden vom Autohaus XX GmbH nachweislich (siehe beil. Rechnungen)  gebrauchte Fahrzeuge erworben.

**False Positives:**

- `Autohaus XX GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_14`)


In der dagegen erhobenen Beschwerde wird Folgendes vorgebracht:  „Im Jahr 2011 informierte die Y Austria GmbH alle für das Unternehmen tätige selbständige  Kundenvermittler darüber, dass die Abrechnung der erwirtschafteten Provisionen über die  Schweizer Zentrale abgewickelt werden.

**False Positives:**

- `Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_18`)


Derzeit ist eine Betriebsprüfung bei der Y Austria GmbH anhängig.

**False Positives:**

- `Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_42`)


Die vorliegende Beschwerde bringt nur ganz allgemein gehalten vor, die Y Austria GmbH habe  im Jahr 2011 alle für das Unternehmen tätigen Kundenvermittler darüber informiert, dass die  Abrechnung der Provisionen über die Schweizer Zentrale abgewickelt würde.

**False Positives:**

- `Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131096.1_116`)


Die, bei  der AG AG durchgeführten, Ermittlungen hätten keinen Einlass in die bekämpften Bescheide  gefunden.

**False Positives:**

- `AG AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `LeitnerLeitner GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendy Schärff`(person)
- `Krainberg 12, 4633 Weilbach, Österreich`(address)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom  29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer  ***, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `BKS Steuerberatung GmbH` — no gold match — likely missing annotation
- `Co  KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Hon.-Prof.in Dominika Kronimus`(person)
- `Am Spitzteich 225, 5114 Göming, Österreich`(address)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131467.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131467.1_4`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Hon.-Prof.in Dominika Kronimus, Am Spitzteich 225, 5114 Göming, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, betreffend Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Einkommensteuer 2003 – 2010 und vom 29.4.2013 betreffend Einkommensteuer  2011, Steuernummer **, beschlossen:   Die Beschwerde vom 18. Mai 2013 wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `BKS Steuerberatung GmbH` — no gold match — likely missing annotation
- `Co  KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Hon.-Prof.in Dominika Kronimus`(person)
- `Am Spitzteich 225, 5114 Göming, Österreich`(address)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Selma Papenmeyer, Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Selma Papenmeyer`(person)
- `Brauweg 2, 3613 Marbach an der Kleinen Krems, Österreich`(address)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_7`)


Die Prüferin traf im Bericht über das Ergebnis der Außenprüfung folgende  beschwerdegegenständliche Feststellung:   Tz. 1 Scheinrechnungen Nord Willexlex GmbH [im Folgenden: D.GmbH]  Die Leistungen der Nord Willexlex GmbH an die Bf. wurden nicht von dieser Firma erbracht, sondern von  J.N. [im Folgenden: J.N.], der den Mantel der Nord Willexlex GmbH mit Einverständnis seines Onkels FN  benutzt hat.

**False Positives:**

- `Scheinrechnungen Nord Willexlex GmbH` — partial — gold is substring of pred: `Nord Willexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nord Willexlex GmbH`(organisation)
- `Nord Willexlex GmbH`(organisation)
- `Nord Willexlex GmbH`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_9`)


Der Aufwand und die Vorsteuer der  Fa.Nord Willexlex GmbH wird von der BP nicht anerkannt.

**False Positives:**

- `Nord Willexlex GmbH` — partial — pred is substring of gold: `Fa.Nord Willexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Nord Willexlex GmbH`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_23`)


Die Beschwerde wurde mit folgender Begründung erhoben:    „ad Tz. 1 (des BP Berichts vom 29.10.2014): Scheinrechnungen  Die Betriebsprüfung hat unter der unrichtigen Annahme einer Scheinrechnung den  Vorsteuerabzug im Jahr 2009 bei Rechnungen im Zusammenhang mit der Firma Nord Willexlex GmbH in  Höhe von insgesamt € 3.333,33 verwehrt.

**False Positives:**

- `Firma Nord Willexlex GmbH` — partial — gold is substring of pred: `Nord Willexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nord Willexlex GmbH`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_27`)


Weiters ist festzuhalten,  dass Herr J.N. bevollmächtigt war für die Firma Nord Willexlex GmbH zu handeln.

**False Positives:**

- `Firma Nord Willexlex GmbH` — partial — gold is substring of pred: `Nord Willexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nord Willexlex GmbH`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131483.1_38`)


Im gegenständlichen Fall wurden auf Grund der Erhebungen der Finanzpolizei festgestellt, dass  die Rechnungen der Fa.Nord Willexlex GmbH in Liquidation Scheinrechnungen waren und die in diesen  Rechnungen ausgewiesenen Leistungen nicht von den oben Genannten erbracht worden sind.

**False Positives:**

- `Nord Willexlex GmbH` — partial — pred is substring of gold: `Fa.Nord Willexlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Nord Willexlex GmbH`(organisation)

</details>

---

## `Raiffeisenbank Entities` 

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `bafd8532`  
**Description:**
Matches Raiffeisenbank entities which often have complex names with hyphens and dots.

**Content:**
```
(?<![a-zA-Z])(?:\b|\s|(?<=\)))(Raiffeisenbank\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\-\.]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\-\.]+)*)(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 461 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/146758.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146758.1_9`)


Das Bundesfinanzgericht hat erwogen:  Laut Aktenlage wurde zur Einbringung des vollstreckbaren Rückstandes des Bf in Höhe von  EUR 20.694,41 laut Rückstandsausweis vom 4. Juli 2024 bei der Raiffeisenbank Kössen-Kirchdorf  eine Pfändung  durchgeführt und dafür die Pfändungsgebühr in Höhe von EUR 206,94 und der Auslagenersatz  in Höhe von EUR 12,50 festgesetzt.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Kössen-Kirchdorf` | `Raiffeisenbank Kössen-Kirchdorf` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/145899.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145899.1_381`)


Aus den vorgelegten Aufstellungen der Sparbuchbehebungen ist ersichtlich, dass vom  Sparbuch 315 (Raiffeisenbank Stein/Enns) vor 2006 ca. € 96.000,- behoben wurden und vom  Sparbuch 316 (Raiffeisenbank Stein/Enns) vor 2006 ca. € 111.000,- wodurch die Angaben zu  Einzahlungen iHv ca. € 200.000,- bestätigt werden.

**False Positives:**

- `Raiffeisenbank Stein` — no gold match — likely missing annotation
- `Raiffeisenbank Stein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Finanzamt Full Name Entities` 🏆

**F1:** 0.039 | **Precision:** 0.315 | **Recall:** 0.021  

**Format:** `regex`  
**Rule ID:** `56376b2d`  
**Description:**
Matches full 'Finanzamt' names followed by locations.

**Content:**
```
(?<![a-zA-Z])(?:\b|\s|(?<=\)))(Finanzamt\s+(?:Purkersdorf|Innsbruck|Linz|Wien\s+2/20/21/22|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Spittal\s+Villach|Tirol\s+Ost|Judenburg\s+Liezen|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Klosterneuburg|Wien\s+8/16/17|Vorarlberg|Landeck\s+Reutte|Schwechat\s+Gerasdorf|Steiermark\s+Mitte|Gmunden\s+V\u00f6cklabruck|Amstetten\s+Melk\s+Scheibbs|Salzburg-Land))(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.315 | 0.021 | 0.039 | 89 | 28 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 61 | 1311 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Spittal Villach` | `Finanzamt Spittal Villach` |

**Missed by this rule (FN):**

- `Univ.-Prof. Niels Aleksejew` (person)
- `Dominik Kuzu` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130057.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130057.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Seidenstecher  in der Beschwerdesache des  HR Edith Tuncel, Bakk. rer. nat., Heide, 18.a Straße 30h, 4674 Untergmain, Österreich, über die Beschwerde vom 6. März 2017 gegen den Bescheid des  Finanzamt Bruck Eisenstadt Oberwart  vom 30. Jänner 2017 betreffend Grunderwerbsteuer 2017 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Leila Seidenstecher` (person)
- `HR Edith Tuncel, Bakk. rer. nat.` (person)
- `Heide, 18.a Straße 30h, 4674 Untergmain, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Missed by this rule (FN):**

- `Univ.-Prof. Merlin Thorschmidt` (person)
- `Adrian Radakovitsch` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134021.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134021.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Kaspar Dolezil  in der Beschwerdesache StR Adam Reulmann,  Schipfäckerweg 22x, 9102 Obertrixen, Österreich, über die Beschwerde vom 31. Juli 2018 gegen den Bescheid des Finanzamt Judenburg Liezen  vom  28. Juni 2018 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80  Bundesabgabenordnung (BAO) (St.Nr. xx-xxx/xxxx HB) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Missed by this rule (FN):**

- `Univ.-Prof. Kaspar Dolezil` (person)
- `StR Adam Reulmann` (person)
- `Schipfäckerweg 22x, 9102 Obertrixen, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lorena Zydat  in der Beschwerdesache Knut Duchoslav,  Felbauweg 4, 8435 Wagendorf, Österreich, vertreten durch Dr. Heinz Häupl Rechtsanwalts GmbH, Stockwinkl 18, 4865  Nußdorf/Attersee, über die   1) Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamt Purkersdorf  vom 9. August  2019 betreffend Festsetzung von ersten Säumniszuschlägen in Höhe von 128,38 €,  568,79 € und 266,87 €;  2) Beschwerde vom 15. Oktober 2019 gegen den Bescheid des FA Purkersdorf  vom 13.  September 2019 über die Abweisung eines Aussetzungsantrages;

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Lorena Zydat` (person)
- `Knut Duchoslav` (person)
- `Felbauweg 4, 8435 Wagendorf, Österreich` (address)
- `FA Purkersdorf` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/134201.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134201.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterDr. Martin Wittmann in der Beschwerdesache  [...], [...], vertreten durch Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Brockmanngasse 75, 8010 Graz, über die Beschwerde vom  27. Jänner 2017 gegen die Bescheide des Finanzamt Landeck Reutte  jeweils vom 10. Jänner 2017,  Steuernummer 16-981/1693, betreffend Energieabgabenvergütung 2011 -2015 zu Recht  erkannt:   I. Der Bescheid vom 10. Jänner 2017 betreffend Festsetzung des Vergütungsbetrages  nach dem Energieabgabenvergütungsgesetz für das Kalenderjahr 2011 wird  abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamt Landeck Reutte` | `Finanzamt Landeck Reutte` |

**Missed by this rule (FN):**

- `16-981/1693` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136478.1_72`)


Es ist nicht erwiesen, dass das Finanzamt Purkersdorf  am 11.2.2013, am 11.6.2014 oder am Datum_1.2015  bezogen auf die für die Veranlagung zur Einkommensteuer maßgeblichen Zeiträume der  Kalenderjahre 2011, 2012 und 2013 Kenntnis davon hatte, dass V im Jahr 2000 das Eigentum  an den Liegenschaften Adresse_1, Adresse_2, Adresse_3 und Adresse_4 unter  Zurückbehaltung des Fruchtgenussrechtes übertragen hatte, ohne dass eine Abgeltung für  Substanzminderung vereinbart wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/136622.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136622.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Silke Rheinerth  in der Beschwerdesache des S1,  vertreten durch StB, über die Beschwerden vom 12. Februar 2019 gegen die Bescheide des  Finanzamt Innsbruck  vom 15. Jänner 2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer für die Jahre 2011 bis 2015 und Einkommensteuer für die Jahre 2011 bis  2015 zu Steuernummer 29-851/4674  zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer für die Jahre 2011 bis 2013 werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Innsbruck` | `Finanzamt Innsbruck` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Silke Rheinerth` (person)
- `29-851/4674` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/136622.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136622.1_72`)


Es ist nicht erwiesen, dass das Finanzamt Innsbruck  am 11.2.2013, am 11.6.2014 oder am 4.3.2015  bezogen auf die für die Veranlagung zur Einkommensteuer maßgeblichen Zeiträume der  Kalenderjahre 2011, 2012 und 2013 Kenntnis davon hatte, dass V im Jahr 2000 das Eigentum  an den Liegenschaften Adresse_1, Adresse_2, Adresse_3 und Adresse_4 unter  Zurückbehaltung des Fruchtgenussrechtes übertragen hatte, ohne dass eine Abgeltung für  Substanzminderung vereinbart wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt Innsbruck` | `Finanzamt Innsbruck` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/137437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Armin Maierle  in der Beschwerdesache HR Verona Hajny, LLM,  Heiligengestadeweg 46, 4841 Hocheck, Österreich, über die Beschwerde vom 5. Oktober 2011 gegen den Bescheid des Finanzamt Klagenfurt St. Veit Wolfsberg  vom 1. September 2011 betreffend Körperschaftsteuer 2009 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Univ.-Prof. Armin Maierle` (person)
- `HR Verona Hajny, LLM` (person)
- `Heiligengestadeweg 46, 4841 Hocheck, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/137574.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Jasmin Juengst  in der Beschwerdesache des  Roxana Kalvelage, Talgraben 11, 9341 St. Johann, Österreich  vertreten durch StB, über die Beschwerde vom 15.4.2020 gegen  den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 24.3.2020 über die Aufhebung des  Einkommensteuerbescheides 2018 gemäß § 299 BAO und gegen den  Einkommensteuerbescheid 2018 zu Steuernummer 42-836/8274    I. zu Recht erkannt: Der Beschwerde gegen den Bescheid über die Aufhebung des  Einkommensteuerbescheides 2018 gemäß § 299 BAO wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Mag.a Jasmin Juengst` (person)
- `Roxana Kalvelage` (person)
- `Talgraben 11, 9341 St. Johann, Österreich` (address)
- `42-836/8274` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/140641.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140641.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Josefine Adamkiewitz  in der Beschwerdesache des  Aloisa Wuhrmann, Dachauer-Park 21, 6622 Mitteregg, Österreich, über die Beschwerde vom 5. Juli 2022 gegen die Bescheide des  Finanzamt Spittal Villach  vom 1. Juni 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  und 2020 zu Steuernummer 08-534/4140  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Spittal Villach` | `Finanzamt Spittal Villach` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Josefine Adamkiewitz` (person)
- `Aloisa Wuhrmann` (person)
- `Dachauer-Park 21, 6622 Mitteregg, Österreich` (address)
- `08-534/4140` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/142627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Flora Fredewold  in der Beschwerdesache der  Versand Bersynbruck  i.L., Burgholz 10, 3072 Außerkasten, Österreich  vertreten durch Rechtsanwalt-X, über die Beschwerde vom  3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99- 999/9999 (M.-GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle des  Finanzamt Klagenfurt St. Veit Wolfsberg) vom 5. November 2019 betreffend Heranziehung als Gemeinschuldnerin für  „Umsatzsteuerveranlagungen und div.

| Predicted | Gold |
|---|---|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Flora Fredewold` (person)
- `Versand Bersynbruck` (organisation)
- `Burgholz 10, 3072 Außerkasten, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/142810.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142810.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marceline Weizenkorn  in der Beschwerdesache Georg Strüve,  Laubweg 96, 4300 St. Valentin, Österreich, vertreten durch Bahl Fend Bitschi Fend Steuerberatung GmbH & Co KG,  Hadeldorfstraße 30, 6830 Rankweil, über die Beschwerde vom 2. November 2022 gegen den  Bescheid des Finanzamt Purkersdorf  vom 28. September 2022 betreffend Feststellung von Einkünften  gemäß § 188 BAO für 2018, Steuernummer 36-621/8395, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO in Verbindung mit § 260 Abs. 1 lit. a BAO  als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Missed by this rule (FN):**

- `Mag.a Marceline Weizenkorn` (person)
- `Georg Strüve` (person)
- `Laubweg 96, 4300 St. Valentin, Österreich` (address)
- `36-621/8395` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/144096.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144096.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Elias Oberendfellner  in der Beschwerdesache Ali Kupzick,  Stillestraße 33, 8530 Freiland bei Deutschlandsberg, Österreich, über die Beschwerde vom 12. Juli 2020 gegen den Bescheid des Finanzamt Klosterneuburg  vom  18. Juni 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 Steuernummer  90-055/0291  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Klosterneuburg` | `Finanzamt Klosterneuburg` |

**Missed by this rule (FN):**

- `Dr. Elias Oberendfellner` (person)
- `Ali Kupzick` (person)
- `Stillestraße 33, 8530 Freiland bei Deutschlandsberg, Österreich` (address)
- `90-055/0291` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/144651.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144651.1_85`)


Aus einer vorgelegten Rechnung vom 30.9.2010 geht hervor, dass die Finanzamt Purkersdorf  eine Prüfung  Treppenaufzug zu einem Gesamtbetrag von 102,00 Euro durchgeführt hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/144651.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144651.1_89`)


Aus einer vorgelegten Rechnung vom 13.9.2012 geht hervor, dass die Finanzamt Purkersdorf  eine Prüfung  des Treppenaufzugs zu einem Gesamtbetrag von 108 Euro durchgeführt hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/146142.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hon.-Prof. Janosch Weinberger  in der Beschwerdesache Igor Golobic,  Fernitz 24, 8832 Krumegg, Österreich, vertreten durch Peter Weinmar, Lerchengasse 18, 1080 Wien, über die  Beschwerde vom 14.November 2023 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. Oktober 2023  betreffend Zahlungserleichterungen § 212 BAO 24.10.2023 zur Steuernummer  58-685/2299  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Missed by this rule (FN):**

- `Hon.-Prof. Hon.-Prof. Janosch Weinberger` (person)
- `Igor Golobic` (person)
- `Fernitz 24, 8832 Krumegg, Österreich` (address)
- `58-685/2299` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/146513.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Felizia Püttrich, Grades Marktplatz 3, 4190 Haid, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Handelsstraße 8/Stiege 2/Top 2, 3130 Herzogenburg, vom 17. Oktober 2022 gegen den  Bescheid des Finanzamt Klagenfurt St. Veit Wolfsberg  vom 6. Oktober 2022 betreffend Einkommensteuer 2020 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Missed by this rule (FN):**

- `Felizia Püttrich` (person)
- `Grades Marktplatz 3, 4190 Haid, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/146625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ernst Beerenbrock  in der Beschwerdesache Richarda Kazimiersch,  Kernjakstraße 22, 4817 Steg, Österreich, über die Beschwerde vom 10. Jänner 2024 gegen den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 14. Dezember 2023 betreffend die teilweise Abweisung eines Rückzahlungsantrages zur  Steuernummer 15-227/3632  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

**Missed by this rule (FN):**

- `Mag. Ernst Beerenbrock` (person)
- `Richarda Kazimiersch` (person)
- `Kernjakstraße 22, 4817 Steg, Österreich` (address)
- `15-227/3632` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/146845.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Vanessa Prüs, Kaltenbach 28, 8904 Frauenberg, Österreich, vertreten durch RPW Wirtschaftstreuhand GmbH,  Roseggerstraße 2, 3500 Krems/Donau, vom 21. August 2020 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. Juli 2020 betreffend Körperschaftsteuer 2016 und 2017 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Missed by this rule (FN):**

- `Vanessa Prüs` (person)
- `Kaltenbach 28, 8904 Frauenberg, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/147075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Bruno Maquardt  in der Angelegenheit der Parteien Dr.  AN Bf, Rechtsanwältin in Stadt37, vertreten durch next Steuerberatung Wien GmbH, 1150  Wien, und Finanzamt Linz  als Amtspartei über die Beschwerde vom 27.9.2024 gegen den Bescheid  des Finanzamtes vom 27.8.2024 betreffend Einkommensteuer 2022  zu Recht erkannt:  Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Missed by this rule (FN):**

- `Mag. Bruno Maquardt` (person)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/148276.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148276.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Maximiliane Nebauer  in der Beschwerdesache des  Dr.in Rosalia Scheingruber, MBA, Povat 90, 8942 Maitschern, Österreich  vertreten durch RA,  über die Beschwerde vom 20. November 2017  gegen die Bescheide des Finanzamt Judenburg Liezen (nunmehr: Finanzamt Österreich) vom 19. Oktober 2015  betreffend Einkommensteuer 2007 und 2008 zu Steuernummer 88-949/2556  beschlossen:  I. Die Einkommensteuerbescheide für die Jahre 2007 und 2008 vom 19. Oktober 2015  und die Beschwerdevorentscheidung vom 6. Feber 2018 werden gemäß § 278 Abs. 1  BAO unter Zurückverweisung der Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Maximiliane Nebauer` (person)
- `Dr.in Rosalia Scheingruber, MBA` (person)
- `Povat 90, 8942 Maitschern, Österreich` (address)
- `88-949/2556` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_67`)


Im Vorlageantrag – beim Finanzamt Tirol Ost  am 8. Jänner 2024 eingelangt – gab der Beschwerdeführer  wie folgt an:  „Seit ich meiner (noch) Frau informiert habe dass ich mich Scheiden will versucht

| Predicted | Gold |
|---|---|
| `Finanzamt Tirol Ost` | `Finanzamt Tirol Ost` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_86`)


Die Ehefrau des BF hat laut Feststellungen des Finanzamt Tirol Ost  im Kalenderjahr 2022 ganzjährig  Familienbeihilfe für die genannten Kinder bezogen.

| Predicted | Gold |
|---|---|
| `Finanzamt Tirol Ost` | `Finanzamt Tirol Ost` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/148726.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148726.1_98`)


Auf die diesbezüglichen Ausführungen in den  Bescheiden des Finanzamt Tirol Ost  wird verwiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Tirol Ost` | `Finanzamt Tirol Ost` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149012.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149012.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Anselm Kajris  in der Beschwerdesache Mercedes Sontagh,  Schleusenstraße 32F, 9556 Rohnsdorf, Österreich, betreffend die Beschwerde vom 27. März 2024 gegen den Bescheid des  Finanzamt Tirol Ost  vom 1. März 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  Steuernummer 96-637/4189, beschlossen:   Die Beschwerde vom 27. März 2024 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamt Tirol Ost` | `Finanzamt Tirol Ost` |

**Missed by this rule (FN):**

- `Univ.-Prof. Mag. Anselm Kajris` (person)
- `Mercedes Sontagh` (person)
- `Schleusenstraße 32F, 9556 Rohnsdorf, Österreich` (address)
- `96-637/4189` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149012.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149012.1_3`)


Begründung  Am 1. März 2024 erging an die beschwerdeführende Partei der Bescheid des Finanzamt Tirol Ost  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022.

| Predicted | Gold |
|---|---|
| `Finanzamt Tirol Ost` | `Finanzamt Tirol Ost` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129778.1_4`)


Entscheidungsgründe  Verfahrensgang  Mit Festsetzungsbescheid vom 19.12.2018 setzte das Finanzamt Wien 8/16/17 (belangte  Behörde) die Umsatzsteuer für den Zeitraum 05-10/2018 fest.

**False Positives:**

- `Finanzamt Wien 8/16/17` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129778.1_32`)


Der Beschluss lautet wie folgt:  "I. Auf Grund der derzeit vorliegenden Unterlagen ist derzeit von folgendem Sachverhalt  auszugehen:  Am 19.12.2018 erließ das Finanzamt Wien 8/16/17 (belangte Behörde) einen Bescheid über die  Festsetzung von Umsatzsteuer für den Zeitraum 5-10/2018, der zu einer Nachforderung von €  105.000,-- führte.

**False Positives:**

- `Finanzamt Wien 8/16/17` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129778.1_49`)


>> Das Finanzamt Wien 8/16/17 wird ersucht, bekannt zu geben, ob der  Säumniszuschlagsbescheid vom 9.1.2019 mittels Zustellnachweis zugestellt wurde und falls  ja, welches Zustelldatum darauf vermerkt wurde.

**False Positives:**

- `Finanzamt Wien 8/16/17` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_88`)


Aufgrund der Rechtsprechung des VwGH beabsichtigt das Finanzamt Spittal Villach an der  bisherigen Verwaltungspraxis festzuhalten und die Hauptwohnsitzbefreiung auch im  Beschwerdefall nur für eine Grundstücksfläche von 1.000 m2 zu gewähren.

**False Positives:**

- `Finanzamt Spittal Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Finanzamt Wien 8/16/17` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Frieda Krein`(person)
- `Priv.-Doz.in Elena Kaminskiy`(person)
- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich`(address)
- `60-936/8299`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_9`)


Im Einkommensteuerbescheid für 2011 vom 10. Juli 2013 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

**False Positives:**

- `Finanzamt  Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_10`)


Im Einkommensteuerbescheid für 2012 vom 30. April 2014 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

**False Positives:**

- `Finanzamt  Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131440.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131440.1_11`)


Im Einkommensteuerbescheid für 2013 vom 22. Juli 2014 berücksichtigte das Finanzamt  Salzburg-Land im Rahmen der Einkünfte aus nichtselbständiger Arbeit Werbungskosten, die  der Arbeitgeber nicht berücksichtigen konnte, in Höhe von 3.672,00 €.

**False Positives:**

- `Finanzamt  Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

**False Positives:**

- `Finanzamt Salzburg-Land` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Natalie Emmerling`(person)
- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133808.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133808.1_9`)


Das Finanzamt Wien 2/20/21/22 erließ den angefochtenen, mit 27. Juni 2019 datierten  Einkommensteuerbescheid 2018 an die Bf., mit welchem die Einkommensteuer für das  Jahr 2018 mit 1.811,00 € festgesetzt wurde, und in welchem bei der Ermittlung der Einkünfte  aus nichtselbständiger Arbeit 13 Lohnzettel, die von der Wiener Gebietskrankenkasse (WGKK)  betreffend Rehabilitationsgeld (bezeichnet als Krankengeld) übermittelt worden waren,  angesetzt wurden.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133808.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133808.1_17`)


Das Finanzamt Wien 2/20/21/22 erließ eine abweisende, mit 7. Oktober 2019 datierte  Beschwerdevorentscheidung gemäß § 262 BAO zu der am 04.07.2019 eingebrachten  Beschwerde der Bf. gegen den Einkommensteuerbescheid 2018 vom 27.06.2019.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133808.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133808.1_20`)


Das Finanzamt Wien 2/20/21/22 legte die Beschwerde der Bf. am 11. Februar 2020 dem  Bundesfinanzgericht (BFG) vor.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134272.1_28`)


Der Beschwerdeführer beantragte in der im Adressfeld an das Finanzamt Wien 2/20/21/22  gerichteten Beschwerde vom 10. Februar 2021 gegen den Einkommensteuerbescheid für das  Jahr 2015 von der Erlassung einer Beschwerdevorentscheidung abzusehen.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134272.1_41`)


Die in der Anschrift an das (vormalige) Finanzamt Wien 2/20/21/22 gerichtete Beschwerde  vom 10. Februar 2021 ist somit nach § 323b Abs. 6 BAO als wirksam eingebracht anzusehen.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134633.1_24`)


Die angeführten Mängel sind beim Finanzamt Innsbruck gemäß § 85 Abs. 2 BAO bis zum  05.11.2018 zu beheben.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135041.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135041.1_5`)


Abweichend wurde dem Veräußerungsgewinn  des Gesellschafters A B kein begünstigter Hälftesteuersatz zuerkannt bzw. keine Veräußerung  eines Mitunternehmeranteils unterstellt.  Diese Änderung wurde in der gesonderten Bescheidbegründung wie folgt dargestellt:   Verfahrensablauf:  Am 20.09.2019 wurde die Erklärung über die Feststellung von Einkünften gem. § 188 BAO für  2018 (Wirtschaftsjahr 01.02.2017 - 31.01.2018) beim Finanzamt Linz elektronisch eingereicht.

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135041.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135041.1_39`)


Zudem wurden die Bestands- und  Superädifikatsverträge vom 15.1.1993, 15.09.2000 und 15.10.2010 gemeinsam mit der  aktuellen Dauerrechnung über das Mietentgelt vom 23.10.2017 übermittelt.  Der Sachverhalt wird durch das Finanzamt Linz wie folgt als erwiesen angenommen (der als  erwiesen angenommene Sachverhalt ergibt sich unstrittig aus den vorgelegten Verträgen  sowie Vorhaltsbeantwortungen):  Beim Unternehmen B KNO Metall GmbH (FN1, Str. Nr. Nr1) stellen sich seit 1992 die Organ- und  Beteiligungsverhältnisse wie folgt dar:  Name Bet./Zeitp.

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KNO Metall GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135041.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135041.1_68`)


Für das Finanzamt Linz ist es als erwiesen anzunehmen, dass die Gewinnverteilung des  laufenden Gewinnes von 70%, 25% und 5% (trotz der erst am 25.10.2017 zivilrechtlich  eingetretenen Neugesellschafter) eine angemessene - den tatsächlichen Arbeitsleistungen  entsprechende - Gewinnverteilung darstellt.  Die Beteiligungsverhältnisse für die Beschwerdeführerin stellen sich demgemäß It.  Gesellschaftsvertrag vom 25.10.2017 wie folgt dar:  Name Bet.

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135041.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135041.1_85`)


Es ist daher für das Finanzamt Linz als erwiesen anzunehmen, dass nach der Anteilsabtretung  von 75% nur mehr von einem verbleibenden kapitalistischen Mitunternehmeranteil in Höhe  von 25% auszugehen ist.

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/135041.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135041.1_394`)


Übertragung von 75% des Kommanditanteils mit allen damit verbundenen  Gesellschafterrechten sowie der unveränderten Vermietung der zum Sonderbetriebsvermögen  zählenden Grundstücke (Grund und Boden) erfüllt.   Selbst wenn man aber wie das Finanzamt Linz grundsätzlich eine umfassende anteilige  Aufdeckung aller stillen Reserven vertritt, ist festzuhalten, dass gerade im vorliegenden  Sachverhalt, bei dem die anteilige Nichtaufdeckung der stillen Reserven nur das  Sonderbetriebsvermögen betrifft und das Sonderbetriebsvermögen nur aus Grund und Boden  besteht, einer Nichtanwendung des § 24 EStG wegen der fehlenden anteiligen Aufdeckung der  stillen Reserven aller Wirtschaftsgüter des Mitunternehmeranteils durch die Bestimmung des  § 24 Abs. 3 iVm § 6 Z 4 EStG die Rechtsgrundlage entzogen wurde, sodass das Zurückbehalten  des Grund und Bodens im vorliegenden Fall keine Auswirkung auf die Anwendung des § 24 EStG  hat, da das Zurückbehalten des Grund und Bodens selbst bei vollständiger Veräußerung des  100%igen Kommanditanteils zu keiner Steuerpflichtigen Aufdeckung der stillen Reserve geführt  hätte.

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/136053.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136053.1_7`)


In dem, vom zuständigen Finanzamt Wien 2/20/21/22 am 28. Mai 2020 ergangenen Bescheid  fanden die beantragten Werbungskosten keine Berücksichtigung.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_15`)


Das Finanzamt Wien 2/20/21/22 richtete am 8. Oktober 2020 ein Ersuchen um Ergänzung  zu den Berechnungsgrundlagen für den erklärten Verlust aus der privaten  Grundstücksveräußerung an die Bf. (BFG-Akt Bl. 8).

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_50`)


Das Finanzamt Wien 2/20/21/22 erließ den mit 22. Oktober 2020 datierten  Einkommensteuerbescheid 2019 (BFG-Akt Bl. 10 ff.), in welchem  3 von 18 Seite 4 von 18

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_83`)


Das Finanzamt Wien 2/20/21/22 erließ eine abweisende, mit 5. November 2020 datierte  Beschwerdevorentscheidung (BVE), welche folgendermaßen begründet war:  „Für das FA ist der Tatbestand des § 262 Abs. 3 BAO nicht erfüllt, da unter Pkt. 3 der  Beschwerde auch Begründungsmängel im Bescheid moniert werden und die Begründung ein  gesetzliches Inhaltserfordernis des Bescheides ist.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_40`)


Hinsichtlich ihres Zurückweisungsantrages führte die belangte Behörde aus, indem der an das  „Finanzamt für Gebühren und Verkehrssteuern, Marxergasse 4, 4810 Gmunden“ gerichtete  Vorlageantrag am 28. Dezember 2018 beim Finanzamt Gmunden Vöcklabruck einlangte, dieses  Finanzamt jedoch sachlich und örtlich unzuständig gewesen sei und infolge Weiterleitung an  das zuständige Finanzamt (Finanzamt für Gebühren, Verkehrssteuern und Glücksspiel,  Marxergasse 4,1030 Wien) bei diesem am 18. Jänner 2019 einlangte, die Rechtsmittelfrist beim  Einlangen bereits verstrichen sei und der Vorlage Antrag somit als nicht rechtzeitig eingebracht  anzusehen sei.

**False Positives:**

- `Finanzamt Gmunden Vöcklabruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_60`)


Dieser Schriftsatz vom 28. Dezember 2018 war gerichtet an:  “Finanzamt für Gebühren und Verkehrssteuern, Marxergasse 4, 4810 Gmunden“ und wurde  am selben Tag beim Finanzamt Gmunden Vöcklabruck in Gmunden persönlich durch Einwurf in  die „ Postbox“ der belangten Behörde und Selbststempelung eingebracht.

**False Positives:**

- `Finanzamt Gmunden Vöcklabruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_63`)


In der Folge wurde der Vorlageantrag – zuständigkeitshalber - durch das Finanzamt Gmunden  Vöcklabruck an das „Finanzamt für Gebühren und Verkehrsst.

**False Positives:**

- `Finanzamt Gmunden  Vöcklabruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_96`)


Beispiel:   Ein Tagespendler aus Oberwart, der tagsüber in Wien arbeitet und abends heimkehrt, konnte  nach der Rechtslage vor dem Inkrafttreten dieses Bundesgesetzes beispielsweise seine  Steuererklärung persönlich nur bei seinem sachlich und örtlich zuständigen Finanzamt (in dem  Fall Finanzamt Bruck Eisenstadt Oberwart) fristwahrend abgeben.

**False Positives:**

- `Finanzamt Bruck Eisenstadt Oberwart` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/137593.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137593.1_109`)


Hier wird die Behörde im Adressfeld durch das weiterleitende Amt (Finanzamt  Gmunden Vöcklabruck) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet.

**False Positives:**

- `Finanzamt  Gmunden Vöcklabruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/139532.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139532.1_16`)


am 19.12.2012, 10% der Dividende  336.000  + Anspruchszinsen                           1.747  Auszahlungen an Bf. auf Grund der drei DBA-Rückzahlungsanträge 2012, gesamt Euro   838.847  (Tabelle 1)  Auf Grund der o.a. Aktienerwerbe hat die Bf. im Jahr 2012 Anträge auf KESt-Rückerstattung  (Formblatt ZS-RE1) beim Finanzamt Bruck Eisenstadt Oberwart (FA BEO) eingebracht.

**False Positives:**

- `Finanzamt Bruck Eisenstadt Oberwart` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/139532.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139532.1_18`)


Das Finanzamt Bruck Eisenstadt Oberwart (FA BAO, nunmehr FA Großbetriebe) ist bundesweit  für Quellensteuerrückerstattungen zuständig.

**False Positives:**

- `Finanzamt Bruck Eisenstadt Oberwart` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/140792.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140792.1_23`)


Das Finanzamt Wien 2/20/21/22 hat unzutreffend und rechtswidrig eine Ausbildungsphase der  fremden- und grenzpolizeilichen exekutivdienstlichen Ausbildung, die keinen Anspruch auf  Familienbeihilfe begründet (weil das FLAG 1967 den Begriff der Ausbildungsphase nicht kennt),  bei der 24-monatigen durchgehenden Ausbildung meines Sohnes angenommen.

**False Positives:**

- `Finanzamt Wien 2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/141346.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141346.1_5`)


Verfahren vor der belangten Behörde:  Am 22. Februar 2018 erließ das Finanzamt Bruck Eisenstadt Oberwart, nunmehr Finanzamt  Österreich (in der Folge als belangte Behörde bezeichnet) den Einkommensteuerbescheid 2017  als Ergebnis der Arbeitnehmerveranlagung.

**False Positives:**

- `Finanzamt Bruck Eisenstadt Oberwart` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_57`)


Am 7. November 2013 teilte die Bundesagentur für Arbeit, Familienkasse D-Ort1 … dem  Finanzamt Innsbruck mit, dass Frau B in Deutschland Kindergeld in Höhe von 9.115,80 Euro bis  einschließlich März 2013 zu Unrecht erhalten habe und der Aufhebungs- und  Erstattungsbescheid unanfechtbar (rechtskräftig) geworden sei.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_64`)


Dementsprechend hat das Finanzamt Innsbruck dem Ersuchen der Bundesagentur für Arbeit,  Familienkasse D-Ort2 vom 30. Oktober 2013 (eingelangt am 7. November 2013) aufgrund der  innerstaatlichen Bestimmungen des Familienlastenausgleichsgesetzes nachzukommen.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_74`)


Sachverhalt  1.1  Erika Puttfarken  als Beschwerdeführer wurde vom Finanzamt Innsbruck als Wohnsitzfinanzamt  Familienbeihilfe für die Kinder E …, D …, C … und A … seit dem Jahr 2012 und laufend gewährt.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erika Puttfarken`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_77`)


Der Beschwerdeführer erhält - trotz entgegenstehender Mitteilungen des Finanzamtes  Innsbruck (zum Beispiel vom 19. März 2013) - seit Oktober 2013 keine Auszahlungen der  gewährten Familienbeihilfe hinsichtlich sämtlicher genannter Kinder an die dem Finanzamt  Innsbruck bekannt gegebene Bankverbindung Konto ….

**False Positives:**

- `Finanzamt  Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_84`)


1.3  Das Finanzamt Innsbruck zahlt keine Familienbeihilfe an den Beschwerdeführer mehr aus.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_86`)


Das Finanzamt  Innsbruck behält Familienbeihilfe ein.

**False Positives:**

- `Finanzamt  Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_87`)


Das Finanzamt Innsbruck fordert den Beschwerdeführer  zur Zahlung von € 9.115,80 auf.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_93`)


Die Rückzahlung bezogener Leistungen an deutschem Familiengeld kann nicht dreimal erfolgen  - durch mit deutschen Behörden vereinbarte Ratenzahlung, durch Einbehalt von  Familienbeihilfenleistungen durch das Finanzamt Innsbruck und durch Aufforderung im Wege  eines Haftungsbescheid zur Zahlung von € 9.115,80.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_94`)


1.4  Mit dem angefochtenen Haftungsbescheid führt das Finanzamt Innsbruck aus, dass der  Beschwerdeführer haftungspflichtig für die deutsche Rückforderung deutschen Kindergeldes  gegenüber seiner Ehefrau sei und fordert ihn zur Entrichtung von € 9.115,80 auf.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_99`)


Das Finanzamt Innsbruck als Erstbehörde hat sich mit diesem Vorbringen nicht auseinander-  gesetzt.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_101`)


Wie deutsche Behörden die Rückzahlung von Kindergeld  organisieren, bleibt aber den deutschen Behörden vorbehalten und ist nicht vom Finanzamt  Innsbruck zu überprüfen.

**False Positives:**

- `Finanzamt  Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_103`)


Finanzamt Innsbruck hierauf im Verfahren und bei der Entscheidung Rücksicht zu nehmen.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_104`)


2.2  Das Finanzamt Innsbruck hat keine Erkundigung bei deutschen Behörden eingezogen, ob die  Stundung bewilligt wurde.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_110`)


Infolge eines unzulänglichen Verfahrens und Ignorierens von Vorbringen und vorgelegten  Beweismitteln gelangt das Finanzamt Innsbruck zu einem Haftungsbescheid für eine  Rückforderung deutschen Kindergeldes, die von den deutschen Behörden gegenwärtig auch von  der Kindesmutter infolge von Stundung nicht zurückgefordert wird.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_111`)


In einem korrekten Verfahren hätte sich das Finanzamt Innsbruck mit den deutschen Behörden  in Kontakt gesetzt, sodass dem Finanzamt Innsbruck bekannt wäre, dass ein allfälliges Ersuchen  im Sinn der Bestimmungen des Artikel 84 VO EU 883/04 bzw Artikel 72 VO EU 987/2009 gar  nicht mehr aufrecht ist.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation
- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_129`)


Das Finanzamt Innsbruck als Erstbehörde beurteilt die gesamte Rechtslage nach dem  österreichischen Recht.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_145`)


…"  7. Mit Beschwerdevorentscheidung vom 10.6.2014 wurde die Beschwerde als unbegründet  abgewiesen und in der Begründung ausgeführt:  " … Mit Eingabe vom 30. Oktober 2013, eingelangt am 7. November 2013, ersuchte die  Bundesagentur für Arbeit, Familienkasse D-Ort1, das Finanzamt Innsbruck gemäß Art. 84 der  Verordnung (EG) Nr. 883/2004 i. V. m. Art. 72 ff. der Verordnung (EG) Nr. 987/2009 um  Einbehaltung und Erstattung von zu Unrecht erbrachten Leistungen aus dem Anspruch von Frau  B, geboren am    September 1974, wohnhaft A-Ort2.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_178`)


Dementsprechend ist das Finanzamt Innsbruck verpflichtet, dem Ersuchen der Bundesagentur  für Arbeit, Familienkasse D-Ort2, vom 30. Oktober 2013 (eingelangt am 7. November 2013)  aufgrund der innerstaatlichen Bestimmungen des Familienlastenausgleichsgesetzes  nachzukommen.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_196`)


Dieser rechtswidrige Zustand hält nach wie vor an, denn der Beschwerdeführer hat am  17.06.2014 vom Finanzamt Innsbruck lediglich einen Teilbetrag von € 1.897,50 ausbezahlt  erhalten.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_223`)


Im Weiteren erliegen im Akt zwei Schreiben der Familienkasse D-Ort3 v. 13.8.2014 samt  zwei beigeschlossenen Formularen E 411 an das Finanzamt Innsbruck, woraus hervorgeht:  a) zu B: Bescheinigt wird deren mtl.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_269`)


Behörde das Finanzamt  Innsbruck unter Verweis auf Art. 84 der Verordnung (EG) Nr. 883/2004 iVm Art. 72 ff. der  Verordnung (EG) Nr. 987/2009 um Einbehaltung des ausstehenden Rückforderungsbetrages  von € 9.115,80 und Überweisung an die dte.

**False Positives:**

- `Finanzamt  Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_331`)


Kindergeld an das Finanzamt Innsbruck als  zuständige Behörde gerichteten Ersuchen der dten.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_334`)


Der Träger des Ms Österreich (di. das Finanzamt Innsbruck bzw. nunmehr Finanzamt  Österreich) hat den entsprechenden Betrag unter den Bedingungen und in den Grenzen  einzubehalten, die nach den von ihm anzuwendenden Rechtsvorschriften für einen solchen  Ausgleich vorgesehen sind, als ob es sich um von ihm selbst zu viel gezahlte Beträge handelte.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_368`)


Der  Bf moniert, dass das Finanzamt Innsbruck "die gesamte Rechtslage nach dem österreichischen  Recht" beurteile und die deutschen Gesetze nicht berücksichtige, wonach kein deutscher  Haftungsbescheid betr.

**False Positives:**

- `Finanzamt Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/142375.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Selina Kranick, Panidorf 26, 4203 Kulm, Österreich, vertreten durch Taferner Steuerberatungs  GmbH, Oberboden 58, 9562 Himmelberg, über die Beschwerde vom 9. September 2019 gegen  den Bescheid des Finanzamtes Österreich (vormals Finanzamt Spittal Villach) vom 19. Juli 2019  betreffend Feststellung der Einkünfte § 188 BAO 2015 (Steuernummer 05-792/7353 ) nach  Durchführung einer mündlichen Verhandlung am 14. August 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamt Spittal Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Selina Kranick`(person)
- `Panidorf 26, 4203 Kulm, Österreich`(address)
- `05-792/7353`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/143573.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143573.1_10`)


Auf Grundlage von Kontrollmitteilungen der deutschen Behörden erließ das Finanzamt Wien  2/20/21/22 neue Einkommensteuerbescheide.

**False Positives:**

- `Finanzamt Wien  2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/144310.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144310.1_4`)


Finanzamt Wien  2/20/21/22, nunmehr Finanzamt Österreich (belangte Behörde), am selben Tag den  Einkommensteuerbescheid für 2017, mit dem die Einkommensteuer iHv € -113,00 (Gutschrift)  festgesetzt wurde.

**False Positives:**

- `Finanzamt Wien  2/20/21/22` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Specific Company Patterns` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d935d848`  
**Description:**
Matches specific known company patterns that don't fit the generic rule or have special prefixes like Fa.Frohriep.

**Content:**
```
(?<![a-zA-Z])(?:Fa\.)?(?:Frohriep\s+\+\s+Wigand\s+Finanzen|Brucksyn\-Analyse|Wilsee\s+IT\s+Werke|Glanzzorber\-Logistik|Donau\s+Dorfsuduni|Bayer\s+Finanzen|Vorbrodt\s+Sanit\u00e4r|Alpen\s+Lexostfurt|Verlag\s+Osttri|S\u00fcdNextriTouristik|Stadt\-Gastronomie|Lognexuni\-Lebensmittel|Stadt\s+Glanzaltal|Lohberg\s+Beratung|Synval\s+IT|H\u00fcltenschmidt\s+Heizung|Waldsteinmon|Ost\s+Werknexstein|Fa\.IGN\s+Gastronomie\s+Consulting|Heimlemgart\s+Marine\s+Holding|Fa\.RDTM\s+Gastronomie|Fa\.Brucksyn\-Analyse|Fa\.Frohriep\s+\+\s+Wigand\s+Finanzen|Fa\.IGN|Fa\.RDTM|Fa\.Brucksyn|Fa\.Frohriep)(?:\s+(?:GmbH|AG|KG|\.)?)?(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

</details>

---

